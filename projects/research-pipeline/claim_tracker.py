#!/usr/bin/env python3
"""
Claim Registry Generator
Extracts claims from a research report, assigns IDs, cross-references with dossier.

Usage: python3 claim_tracker.py <report.md> --dossier <dossier_dir> [--output claims_registry.json]
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any

WORKSPACE = Path(os.path.expanduser("~/.openclaw/workspace"))

# Claim detection patterns
CLAIM_PATTERNS = [
    re.compile(r'.*\d+[\.\d]*\s*%.*', re.IGNORECASE),  # percentages
    re.compile(r'.*\$[\d,]+.*', re.IGNORECASE),  # dollar amounts
    re.compile(r'.*\b(?:show|demonstrate|find|reveal|indicate|suggest|confirm|prove)s?\b.*', re.IGNORECASE),
    re.compile(r'.*\b(?:better than|outperform|superior|unlike|compared to|exceed|surpass)s?\b.*', re.IGNORECASE),
    re.compile(r'.*\b(?:should|must|recommend|require|need to|essential)\b.*', re.IGNORECASE),
    re.compile(r'.*\b(?:achieve|reduce|improve|increase|decrease)\w*\s+(?:by\s+)?\d+.*', re.IGNORECASE),
]

# Exclusion patterns (not claims)
EXCLUDE_PATTERNS = [
    re.compile(r'^\s*#', re.IGNORECASE),  # headings
    re.compile(r'^\s*[-*]\s*$'),  # empty list items
    re.compile(r'^\s*\|.*\|.*\|', re.IGNORECASE),  # table rows (standalone)
    re.compile(r'^\s*>'),  # blockquotes
    re.compile(r'^\s*```'),  # code blocks
    re.compile(r'^\s*Generated:|^\s*Date:|^\s*Confidence:', re.IGNORECASE),  # metadata
]


def extract_sections(text: str) -> List[Dict[str, Any]]:
    """Parse markdown into sections with headings."""
    sections: List[Dict[str, Any]] = []
    current_section = "Preamble"
    current_lines: List[tuple[str, int]] = []

    for i, line in enumerate(text.splitlines(), 1):
        m = re.match(r'^#{1,6}\s+(.+)', line)
        if m:
            if current_lines:
                sections.append({"heading": current_section, "lines": current_lines})
            current_section = m.group(1).strip()
            current_lines = []
        else:
            current_lines.append((line, i))

    if current_lines:
        sections.append({"heading": current_section, "lines": current_lines})
    return sections


def is_claim(sentence: str) -> bool:
    """Heuristic check if a sentence contains a claim."""
    s = sentence.strip()
    if len(s) < 30 or len(s) > 500:
        return False
    for ep in EXCLUDE_PATTERNS:
        if ep.match(s):
            return False
    for cp in CLAIM_PATTERNS:
        if cp.match(s):
            return True
    return False


def extract_claims_heuristic(text: str) -> List[Dict[str, Any]]:
    """Extract claims using regex heuristics."""
    sections = extract_sections(text)
    claims: List[Dict[str, Any]] = []

    for section in sections:
        for line_text, line_num in section["lines"]:
            # Split line into sentences
            sentences = re.split(r'(?<=[.!?])\s+', line_text)
            for sent in sentences:
                sent = sent.strip()
                if is_claim(sent):
                    # Detect claim type
                    ctype = "general"
                    if re.search(r'\d+[\.\d]*\s*%|\$[\d,]+', sent):
                        ctype = "empirical"
                    elif re.search(r'\b(?:should|must|recommend)\b', sent, re.I):
                        ctype = "recommendation"
                    elif re.search(r'\b(?:better|outperform|superior)\b', sent, re.I):
                        ctype = "comparative"

                    # Extract cited source (rough)
                    source_match = re.search(r'\(([^)]+\d{4}[^)]*)\)', sent)
                    source = source_match.group(1) if source_match else ""

                    claims.append({
                        "text": sent,
                        "section": section["heading"],
                        "line": line_num,
                        "source_cited": source,
                        "type": ctype,
                    })
    return claims


def extract_claims_llm(text: str) -> Optional[List[Dict[str, Any]]]:
    """Try LLM-based claim extraction. Returns None if unavailable."""
    api_key = os.environ.get("ANTHROPIC_API_KEY") or os.environ.get("OPENAI_API_KEY")
    if not api_key:
        return None

    try:
        if os.environ.get("ANTHROPIC_API_KEY"):
            import anthropic
            client = anthropic.Anthropic()
            # Use first 8000 chars to stay within budget
            excerpt = text[:8000]
            resp = client.messages.create(
                model="claude-haiku-4-5-20250514",
                max_tokens=4096,
                temperature=0,
                system="Extract claims from this research report. Return JSON array of objects with: text, section, type (empirical/recommendation/comparative/general), source_cited.",
                messages=[{"role": "user", "content": f"Extract all claims from:\n\n{excerpt}"}],
            )
            result = resp.content[0].text
        else:
            import openai
            client = openai.OpenAI()
            excerpt = text[:8000]
            resp = client.chat.completions.create(
                model="gpt-4o-mini",
                max_tokens=4096,
                temperature=0,
                messages=[
                    {"role": "system", "content": "Extract claims from this research report. Return JSON array of objects with: text, section, type (empirical/recommendation/comparative/general), source_cited."},
                    {"role": "user", "content": f"Extract all claims from:\n\n{excerpt}"},
                ],
            )
            result = resp.choices[0].message.content

        # Parse JSON
        result = result.strip()
        if result.startswith("```"):
            result = re.sub(r'^```\w*\n?', '', result)
            result = re.sub(r'\n?```$', '', result)
        return json.loads(result)
    except Exception as e:
        print(f"  ⚠ LLM extraction failed: {e}, falling back to heuristic")
        return None


def word_overlap_score(text1: str, text2: str) -> float:
    """Simple word overlap similarity."""
    w1 = set(re.findall(r'[a-z]+', text1.lower()))
    w2 = set(re.findall(r'[a-z]+', text2.lower()))
    stops = {"the", "a", "an", "in", "of", "for", "and", "or", "to", "is", "on", "at", "by", "with", "that", "this"}
    w1 -= stops
    w2 -= stops
    if not w1 or not w2:
        return 0.0
    return len(w1 & w2) / max(len(w1 | w2), 1)


def cross_reference_dossier(claims: List[Dict], dossier_dir: Path) -> List[Dict]:
    """Cross-reference claims with dossier knowledge."""
    # Load knowledge.json
    know_path = dossier_dir / "knowledge.json"
    dossier_claims: List[Dict] = []
    if know_path.exists():
        try:
            kdata = json.loads(know_path.read_text())
            dossier_claims = kdata.get("all_claims", [])
            print(f"  ✓ Loaded {len(dossier_claims)} dossier claims")
        except Exception:
            pass

    # Load CRTs
    crt_path = WORKSPACE / "research-base" / "compounding-research-truths.json"
    crts: List[Dict] = []
    if crt_path.exists():
        try:
            crts = json.loads(crt_path.read_text()).get("truths", [])
            print(f"  ✓ Loaded {len(crts)} CRTs")
        except Exception:
            pass

    for claim in claims:
        claim["dossier_support"] = []
        claim["dossier_contradict"] = []
        claim["crt_match"] = ""

        # Match against dossier claims
        for dc in dossier_claims:
            score = word_overlap_score(claim["text"], dc.get("text", ""))
            if score > 0.3:
                claim["dossier_support"].append(dc.get("paper_id", "unknown"))

        # Match against CRTs
        best_crt_score = 0.0
        for crt in crts:
            score = word_overlap_score(claim["text"], crt.get("claim", ""))
            if score > best_crt_score:
                best_crt_score = score
                if score > 0.25:
                    claim["crt_match"] = crt.get("id", "")

    return claims


def assign_confidence(claim: Dict) -> float:
    """Assign confidence based on source and dossier support."""
    conf = 0.5
    if claim.get("source_cited"):
        conf += 0.15
    if claim.get("dossier_support"):
        conf += 0.1 * min(len(claim["dossier_support"]), 3)
    if claim.get("crt_match"):
        conf += 0.1
    if claim.get("type") == "empirical":
        conf += 0.05
    return min(conf, 0.95)


def main() -> None:
    parser = argparse.ArgumentParser(description="Claim Registry Generator")
    parser.add_argument("report", help="Path to report markdown file")
    parser.add_argument("--dossier", required=True, help="Path to dossier directory")
    parser.add_argument("--output", default=None, help="Output JSON file")
    args = parser.parse_args()

    report_path = Path(args.report)
    if not report_path.exists():
        # Try relative to workspace
        report_path = WORKSPACE / args.report
    if not report_path.exists():
        print(f"❌ Report not found: {args.report}")
        sys.exit(1)

    dossier_dir = Path(args.dossier)
    if not dossier_dir.exists():
        dossier_dir = WORKSPACE / args.dossier
    if not dossier_dir.exists():
        print(f"❌ Dossier directory not found: {args.dossier}")
        sys.exit(1)

    print(f"\n🔍 Extracting claims from: {report_path.name}")
    text = report_path.read_text(encoding="utf-8")

    # Try LLM first, fallback to heuristic
    print("  Attempting LLM-based extraction...")
    claims = extract_claims_llm(text)
    if claims is None:
        print("  Using heuristic extraction...")
        claims = extract_claims_heuristic(text)
    print(f"  Found {len(claims)} raw claims")

    # Cross-reference
    print("  Cross-referencing with dossier...")
    claims = cross_reference_dossier(claims, dossier_dir)

    # Assign IDs and confidence
    for i, claim in enumerate(claims, 1):
        claim["id"] = f"C-{i:03d}"
        claim["confidence"] = assign_confidence(claim)
        claim.setdefault("agent_votes", {})
        claim.setdefault("dossier_support", [])
        claim.setdefault("dossier_contradict", [])

    # Build output
    registry = {
        "report": report_path.name,
        "generated": datetime.now().isoformat(),
        "total_claims": len(claims),
        "claims": claims,
    }

    if args.output:
        out_path = Path(args.output)
        out_path.write_text(json.dumps(registry, indent=2, ensure_ascii=False))
        print(f"\n✅ Registry written to {out_path} ({len(claims)} claims)")
    else:
        print(json.dumps(registry, indent=2, ensure_ascii=False))
        print(f"\n✅ Extracted {len(claims)} claims")

    # Summary
    types = {}
    for c in claims:
        t = c.get("type", "general")
        types[t] = types.get(t, 0) + 1
    print(f"  Types: {types}")
    supported = sum(1 for c in claims if c.get("dossier_support"))
    crt_matched = sum(1 for c in claims if c.get("crt_match"))
    print(f"  Dossier-supported: {supported}, CRT-matched: {crt_matched}")


if __name__ == "__main__":
    main()
