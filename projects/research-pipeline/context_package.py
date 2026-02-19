#!/usr/bin/env python3
"""
Agent Context Package Generator
Generates a standardized briefing document for research agents.

Usage: python3 context_package.py --topic "LLM Trust Calibration" [--output acp.md]

Sources:
1. verified-truths.md (from Obsidian vault via symlink)
2. compounding-research-truths.json (research-specific)
3. corrections.json (known errors to avoid)
4. Topic filtering (only load relevant CRTs)
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
MEMORY_DIR = WORKSPACE / "memory"
RESEARCH_BASE = WORKSPACE / "research-base"


def load_verified_truths() -> str:
    """Load verified-truths.md from vault symlink."""
    candidates = [
        MEMORY_DIR / "verified-truths.md",
        MEMORY_DIR / "knowledge" / "verified-truths.md",
        WORKSPACE / "verified-truths.md",
    ]
    for p in candidates:
        if p.exists():
            print(f"  ✓ Loaded verified-truths from {p}")
            return p.read_text(encoding="utf-8")
    print("  ⚠ verified-truths.md not found, using fallback")
    return ""


def load_json_safe(path: Path) -> Dict[str, Any]:
    """Load JSON with error handling."""
    if not path.exists():
        print(f"  ⚠ {path.name} not found")
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        print(f"  ✓ Loaded {path.name}")
        return data
    except json.JSONDecodeError as e:
        print(f"  ❌ JSON error in {path.name}: {e}")
        return {}


def keyword_match(text: str, topic: str) -> bool:
    """Check if text matches topic via keyword overlap."""
    topic_words = set(re.findall(r'[a-z]+', topic.lower()))
    text_words = set(re.findall(r'[a-z]+', text.lower()))
    # Remove stopwords
    stops = {"the", "a", "an", "in", "of", "for", "and", "or", "to", "is", "on", "at", "by", "with"}
    topic_words -= stops
    text_words -= stops
    if not topic_words:
        return True
    overlap = len(topic_words & text_words)
    return overlap >= max(1, len(topic_words) // 3)


def filter_crts(truths: List[Dict], topic: str) -> tuple[List[Dict], List[Dict]]:
    """Filter CRTs by topic relevance. Returns (active, open_questions)."""
    active = []
    open_qs = []
    for t in truths:
        searchable = f"{t.get('claim', '')} {' '.join(t.get('tags', []))} {t.get('category', '')}"
        if not keyword_match(searchable, topic):
            continue
        status = t.get("status", "ACTIVE").upper()
        if status in ("ACTIVE", "VERIFIED"):
            active.append(t)
        elif status in ("NEEDS_VERIFICATION", "CONTESTED"):
            open_qs.append(t)
    active.sort(key=lambda x: x.get("confidence", 0), reverse=True)
    return active, open_qs


def format_crt(t: Dict) -> str:
    """Format a single CRT as markdown."""
    conf = t.get("confidence", 0)
    return (
        f"- **[{t.get('id', '?')}]** (conf: {conf:.0%}) "
        f"{t.get('claim', 'N/A')}\n"
        f"  Source: {t.get('source', 'unknown')} | "
        f"Tags: {', '.join(t.get('tags', []))}"
    )


def format_correction(c: Dict) -> str:
    """Format a correction entry."""
    return (
        f"- ❌ WRONG: {c.get('wrong', 'N/A')}\n"
        f"  ✅ RIGHT: {c.get('right', 'N/A')}\n"
        f"  Source: {c.get('source', 'unknown')} | Severity: {c.get('severity', '?')}"
    )


def generate_acp(topic: str) -> str:
    """Generate Agent Context Package markdown."""
    print(f"\n📦 Generating ACP for topic: {topic}")

    # Load sources
    verified_raw = load_verified_truths()
    crt_data = load_json_safe(RESEARCH_BASE / "compounding-research-truths.json")
    corrections_data = load_json_safe(RESEARCH_BASE / "corrections.json")

    # Filter CRTs
    truths = crt_data.get("truths", [])
    active_crts, open_crts = filter_crts(truths, topic)
    print(f"  Filtered: {len(active_crts)} active, {len(open_crts)} open questions")

    # Filter corrections
    all_corrections = crt_data.get("corrections", []) + corrections_data.get("corrections", [])
    # Deduplicate by id
    seen_ids: set[str] = set()
    corrections: List[Dict] = []
    for c in all_corrections:
        cid = c.get("id", "")
        if cid not in seen_ids:
            seen_ids.add(cid)
            corrections.append(c)

    # Filter verified truths by topic
    vt_lines: List[str] = []
    if verified_raw:
        for line in verified_raw.splitlines():
            if line.strip() and keyword_match(line, topic):
                vt_lines.append(line)

    # Build ACP
    now = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    sections: List[str] = []

    sections.append(f"""# Agent Context Package
Generated: {now} | Topic: {topic}

## Identity
Ainary Ventures. Florian Ziesche, Ex-CEO 36ZERO Vision.
Raised €5.0M (€3.5M equity + €1.5M grants). Clients: BMW, Siemens, Bosch.
Focus: AI Trust Calibration infrastructure.""")

    # Verified Truths from vault
    if vt_lines:
        sections.append(f"\n## Verified Truths from Vault (relevant to {topic})\n" + "\n".join(vt_lines[:20]))

    # Active CRTs
    if active_crts:
        crts_formatted = "\n\n".join(format_crt(t) for t in active_crts)
        sections.append(f"\n## Compounding Research Truths ({len(active_crts)} active)\n\n{crts_formatted}")

    # Open Questions
    if open_crts:
        oq_formatted = "\n\n".join(format_crt(t) for t in open_crts)
        sections.append(f"\n## Open Questions\n\n{oq_formatted}")

    # Corrections
    if corrections:
        corr_formatted = "\n\n".join(format_correction(c) for c in corrections)
        sections.append(f"\n## Known Errors — DO NOT REPEAT\n\n{corr_formatted}")

    # Anti-patterns
    sections.append("""
## Anti-Patterns
- Never present simulated data as empirical
- Never use unverified market numbers without source
- Every claim needs a source or "author estimate" label
- Executive Summary must lead with NOVEL insight, not known fact
- No LLM phrases: landscape, tapestry, delve, synergy, cutting-edge, game-changer

## Quality Bar
This report goes to professors and VCs.
Would an expert learn something new? If not, rewrite.""")

    return "\n".join(sections)


def main() -> None:
    parser = argparse.ArgumentParser(description="Agent Context Package Generator")
    parser.add_argument("--topic", required=True, help="Research topic")
    parser.add_argument("--output", default=None, help="Output file (default: stdout)")
    args = parser.parse_args()

    acp = generate_acp(args.topic)

    if args.output:
        out_path = Path(args.output)
        out_path.write_text(acp, encoding="utf-8")
        print(f"\n✅ ACP written to {out_path} ({len(acp)} chars)")
    else:
        print("\n" + "=" * 60)
        print(acp)
        print("=" * 60)
        print(f"\n✅ ACP generated ({len(acp)} chars)")


if __name__ == "__main__":
    main()
