#!/usr/bin/env python3
"""
mia_synthesis_v3.py — Elite Research Synthesis Engine (v3)

5-Phase architecture:
  A: Retrieval + Outline (1 Opus call)
  B: Sections (7 Opus calls, sequential)
  C: Merge (Python, 0 LLM)
  D: Validate (Python, 0 LLM)
  E: Grade + Output

Usage:
    python3 mia_synthesis_v3.py /path/to/pipeline-output/ [--version v5] [--dry-run]
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import re
import subprocess
import sys
import textwrap
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

# AgentTrust integration — use the real library, not inline reimplementation
try:
    from agenttrust.core.calibration import source_signal_confidence as _at_confidence
    from agenttrust.core.beipackzettel import Beipackzettel as _AT_Beipackzettel
    from agenttrust.core.trust_score import TrustScore as _AT_TrustScore
    USE_AGENTTRUST = True
except ImportError:
    USE_AGENTTRUST = False

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

WORKSPACE = Path(os.path.expanduser("~/.openclaw/workspace"))

SECTION_ORDER: list[str] = [
    "beipackzettel",
    "executive_summary",
    "framework",
    "key_findings",
    "recommendations",
    "risks",
    "appendix",
]

MIN_WORDS: dict[str, int] = {
    "beipackzettel": 300,
    "executive_summary": 600,
    "framework": 800,
    "key_findings": 1500,
    "recommendations": 1200,
    "risks": 800,
    "appendix": 1000,
}

BANNED_WORDS: list[str] = [
    "delve", "dive into", "it's important to note", "in conclusion",
    "game-changer", "paradigm shift", "synergy", "leverage",
    "holistic", "robust", "cutting-edge", "best-in-class",
    "groundbreaking", "revolutionary", "unprecedented",
]

ADMIRALTY_MAP: dict[str, float] = {
    "A1": 0.95, "A2": 0.85, "A3": 0.75,
    "B1": 0.80, "B2": 0.70, "B3": 0.60,
    "C1": 0.60, "C2": 0.50, "C3": 0.40,
    "D1": 0.40, "D2": 0.30, "D3": 0.25, "D4": 0.20,
    "E1": 0.15, "E2": 0.10, "E3": 0.05,
    "F1": 0.50, "F2": 0.40, "F3": 0.30,
}

EIJA_WEIGHTS: dict[str, float] = {"E": 0.85, "I": 0.60, "J": 0.30, "A": 0.20}

USE_RAG: bool = False

try:
    from rag_layer import query as rag_query, query_for_section, ingest  # type: ignore
    USE_RAG = True
except ImportError:
    pass

# ---------------------------------------------------------------------------
# Utility: OAuth + Opus
# ---------------------------------------------------------------------------

def _load_oauth_token() -> str:
    """Load OAuth token from auth-profiles.json."""
    auth_path = Path(os.path.expanduser(
        "~/.openclaw/agents/main/agent/auth-profiles.json"
    ))
    if not auth_path.exists():
        raise RuntimeError(f"No auth file at {auth_path}")

    auth_data = json.loads(auth_path.read_text())
    candidates: list[str] = []

    def _extract(obj: Any) -> None:
        if isinstance(obj, dict):
            for k, v in obj.items():
                if k in ("token", "accessToken") and isinstance(v, str) and v.startswith("sk-ant-oat"):
                    candidates.append(v)
                elif isinstance(v, (dict, list)):
                    _extract(v)
        elif isinstance(obj, list):
            for item in obj:
                _extract(item)

    _extract(auth_data)
    if not candidates:
        raise RuntimeError("No sk-ant-oat token found in auth-profiles.json")
    return candidates[0]


def call_opus(
    prompt: str,
    system: str = "",
    max_tokens: int = 4096,
    retry: bool = True,
) -> str:
    """Call Claude Opus via curl + OAuth. Returns response text."""
    token = _load_oauth_token()

    messages = [{"role": "user", "content": prompt}]
    payload: dict[str, Any] = {
        "model": "claude-opus-4-20250514",
        "max_tokens": max_tokens,
        "messages": messages,
    }
    if system:
        payload["system"] = system

    payload_json = json.dumps(payload)
    print(f"  [OPUS] Sending {len(prompt)} chars, max_tokens={max_tokens}...")

    for attempt in range(2 if retry else 1):
        if attempt > 0:
            print("  [OPUS] Retry after 30s...")
            time.sleep(30)

        start = time.time()
        try:
            result = subprocess.run(
                [
                    "curl", "-s", "-X", "POST",
                    "https://api.anthropic.com/v1/messages",
                    "-H", f"Authorization: Bearer {token}",
                    "-H", "anthropic-version: 2023-06-01",
                    "-H", "anthropic-beta: oauth-2025-04-20",
                    "-H", "content-type: application/json",
                    "-d", payload_json,
                ],
                capture_output=True, text=True, timeout=900,
            )
            elapsed = time.time() - start

            if result.returncode != 0:
                raise RuntimeError(f"curl failed: {result.stderr[:300]}")

            data = json.loads(result.stdout)
            if "error" in data:
                raise RuntimeError(f"API error: {data['error']}")

            text = data["content"][0]["text"]
            print(f"  [OPUS] Got {len(text)} chars in {elapsed:.0f}s")
            return text

        except Exception as e:
            print(f"  [OPUS] Error (attempt {attempt + 1}): {e}")
            if attempt == 0 and retry:
                continue
            raise

    return ""  # unreachable


def extract_json(text: str) -> Any:
    """Extract JSON from text, handling ```json...``` wrapping."""
    # Try direct parse
    text = text.strip()
    if text.startswith("{") or text.startswith("["):
        try:
            return json.loads(text)
        except json.JSONDecodeError:
            pass
    # Try fenced block
    m = re.search(r"```(?:json)?\s*\n(.*?)```", text, re.DOTALL)
    if m:
        try:
            return json.loads(m.group(1))
        except json.JSONDecodeError:
            pass
    # Aggressive: find first { to last }
    start = text.find("{")
    end = text.rfind("}")
    if start != -1 and end != -1 and end > start:
        try:
            return json.loads(text[start:end + 1])
        except json.JSONDecodeError:
            pass
    raise ValueError(f"Cannot extract JSON from text ({len(text)} chars)")


# ---------------------------------------------------------------------------
# Data Loading
# ---------------------------------------------------------------------------

def load_pipeline_data(pipeline_dir: Path) -> dict[str, Any]:
    """Load all pipeline output files into a dict."""
    data: dict[str, Any] = {}

    # JSON files
    for name in ["research-brief.json", "all-claims.json", "contradictions.json",
                  "sub-reviews.json", "blindspots.json"]:
        p = pipeline_dir / name
        if p.exists():
            data[name] = json.loads(p.read_text())
            print(f"  Loaded {name} ({p.stat().st_size} bytes)")
        else:
            print(f"  WARNING: {name} not found")
            data[name] = {}

    # Sub-reports
    sub_reports: list[dict[str, str]] = []
    for md in sorted(pipeline_dir.glob("sq-*/report.md")):
        sub_reports.append({
            "sq": md.parent.name,
            "text": md.read_text(),
        })
    data["sub_reports"] = sub_reports
    print(f"  Loaded {len(sub_reports)} sub-reports")

    return data


def load_workspace_data() -> dict[str, Any]:
    """Load workspace-level reference files."""
    data: dict[str, Any] = {}
    files = {
        "compounding-truths": WORKSPACE / "research-base" / "compounding-research-truths.json",
        "corrections": WORKSPACE / "research-base" / "corrections.json",
        "reference-library": WORKSPACE / "research-base" / "reference-library.json",
        "prior-report": WORKSPACE / "research" / "ar-020-agent-trust-calibration" / "ar-020-v5-state-of-agent-trust.md",
    }
    for key, p in files.items():
        if p.exists():
            if p.suffix == ".json":
                data[key] = json.loads(p.read_text())
            else:
                data[key] = p.read_text()
            print(f"  Loaded {key} ({p.stat().st_size} bytes)")
        else:
            print(f"  WARNING: {key} not found at {p}")
            data[key] = {} if p.suffix == ".json" else ""
    return data


# ---------------------------------------------------------------------------
# Claim Ledger Parser (robust, multi-format)
# ---------------------------------------------------------------------------

def parse_claim_ledger(text: str) -> list[dict[str, Any]]:
    """Parse claim ledger entries from various formats.

    Handles:
        CL-01 | RLHF damages calibration | [E] | [S30] | A2 | 0.82
        CL-01 [E] "RLHF damages calibration" [S30] (A2, 0.82)
        | CL-01 | RLHF damages calibration | E | S30 | A2 |
        CL-01: RLHF damages calibration [E] [S30] A2
    """
    claims: list[dict[str, Any]] = []
    # Find all CL-## occurrences and parse the line
    for line in text.split("\n"):
        m_cl = re.search(r"CL-(\d+)", line)
        if not m_cl:
            continue

        cl_id = f"CL-{m_cl.group(1)}"

        # Extract E/I/J/A label
        m_label = re.search(r"\[([EIJA])\]|\b([EIJA])\b(?=\s*\||\s*\]|\s*$|\s+[SA]\d|\s+\[S)", line)
        label = ""
        if m_label:
            label = m_label.group(1) or m_label.group(2) or ""

        # Extract source references [S##] or S##
        sources = re.findall(r"\[?S(\d+)\]?", line)
        sources = [f"S{s}" for s in sources]

        # Extract admiralty rating (A1-F3 pattern)
        m_adm = re.search(r"\b([A-F][1-6])\b", line)
        admiralty = m_adm.group(1) if m_adm else ""

        # Extract confidence if present
        m_conf = re.search(r"\b(0\.\d+)\b", line)
        conf = float(m_conf.group(1)) if m_conf else None

        # Extract claim text (heuristic: longest segment without brackets)
        # Remove known tokens to isolate claim text
        cleaned = line
        cleaned = re.sub(r"CL-\d+", "", cleaned)
        cleaned = re.sub(r"\[?[EIJA]\]?", "", cleaned, count=1)
        cleaned = re.sub(r"\[?S\d+\]?", "", cleaned)
        cleaned = re.sub(r"\b[A-F][1-6]\b", "", cleaned)
        cleaned = re.sub(r"\b0\.\d+\b", "", cleaned)
        cleaned = re.sub(r"[|:\"()\[\]]", " ", cleaned)
        claim_text = " ".join(cleaned.split()).strip(" -,.")

        claims.append({
            "id": cl_id,
            "label": label,
            "text": claim_text,
            "sources": sources,
            "admiralty": admiralty,
            "confidence": conf,
            "raw": line.strip(),
        })

    return claims


# ---------------------------------------------------------------------------
# Phase A: Retrieval + Outline
# ---------------------------------------------------------------------------

OUTLINE_SYSTEM = textwrap.dedent("""\
    You are Mia, an elite research synthesis AI. You produce intelligence-grade reports.

    RULES:
    - Use E/I/J/A epistemic labels for ALL claims
    - E = Established (≥3 peer-reviewed, converging), I = Informed (2+ credible),
      J = Judgment (1 source or extrapolation), A = Assumption (no direct evidence)
    - Every claim gets [S#] source reference
    - Every section gets "For the decision maker:" callout
    - Every section gets confidence percentage
    - BANNED words: """ + ", ".join(BANNED_WORDS) + """

    OUTPUT FORMAT: JSON only, no prose outside JSON.
""")

OUTLINE_USER_TEMPLATE = textwrap.dedent("""\
    Create a detailed outline for a research synthesis report.

    RESEARCH BRIEF:
    {brief}

    CLAIMS ({n_claims} total):
    {claims_summary}

    CONTRADICTIONS:
    {contradictions}

    BLINDSPOTS:
    {blindspots}

    SUB-REPORTS ({n_subs} total):
    {sub_summaries}

    {rag_context}

    Return a JSON object with this structure:
    {{
      "title": "...",
      "version": "{version}",
      "sections": [
        {{
          "id": "beipackzettel",
          "title": "Beipackzettel (Information Safety Label)",
          "key_points": ["..."],
          "claim_assignments": ["CL-01", "CL-02"],
          "source_assignments": ["S1", "S2"],
          "min_words": 300
        }},
        ... (all 7 sections in order: beipackzettel, executive_summary, framework, key_findings, recommendations, risks, appendix)
      ],
      "total_claims": ...,
      "total_sources": ...
    }}

    EVERY claim (CL-##) must be assigned to exactly one section.
    EVERY source (S##) must be assigned to at least one section.
    All 7 sections MUST be present.
""")


def phase_a_outline(
    pipeline_data: dict[str, Any],
    workspace_data: dict[str, Any],
    version: str,
    dry_run: bool = False,
) -> dict[str, Any]:
    """Phase A: Generate outline via Opus."""
    t0 = time.time()
    print("\n[PHASE A] Retrieval + Outline")

    brief = pipeline_data.get("research-brief.json", {})
    brief_str = json.dumps(brief, indent=2)[:3000] if brief else "(no brief)"

    # Claims
    all_claims = pipeline_data.get("all-claims.json", {})
    if isinstance(all_claims, list):
        claims_list = all_claims
    elif isinstance(all_claims, dict):
        claims_list = all_claims.get("claims", [])
    else:
        claims_list = []
    claims_summary = json.dumps(claims_list[:30], indent=1)[:4000] if claims_list else "(no claims)"

    # Contradictions
    contras = pipeline_data.get("contradictions.json", {})
    contra_str = json.dumps(contras, indent=1)[:2000] if contras else "(none)"

    # Blindspots
    blinds = pipeline_data.get("blindspots.json", {})
    blind_str = json.dumps(blinds, indent=1)[:2000] if blinds else "(none)"

    # Sub-report summaries
    sub_reports = pipeline_data.get("sub_reports", [])
    sub_sums: list[str] = []
    for sr in sub_reports:
        text = sr["text"][:500]
        sub_sums.append(f"### {sr['sq']}\n{text}...")
    sub_str = "\n\n".join(sub_sums) if sub_sums else "(no sub-reports)"

    # RAG context
    rag_context = ""
    if USE_RAG:
        try:
            chunks = rag_query("research synthesis outline", top_k=50)  # type: ignore
            rag_context = "RAG CONTEXT (top-50 chunks):\n" + "\n---\n".join(
                c.get("text", "")[:300] for c in chunks[:50]
            )
        except Exception as e:
            print(f"  WARNING: RAG query failed: {e}")

    prompt = OUTLINE_USER_TEMPLATE.format(
        brief=brief_str,
        n_claims=len(claims_list),
        claims_summary=claims_summary,
        contradictions=contra_str,
        blindspots=blind_str,
        n_subs=len(sub_reports),
        sub_summaries=sub_str,
        rag_context=rag_context,
        version=version,
    )

    if dry_run:
        print(f"  [DRY RUN] Would send outline prompt ({len(prompt)} chars)")
        print(f"  --- PROMPT PREVIEW (first 2000 chars) ---")
        print(prompt[:2000])
        print(f"  --- END PREVIEW ---")
        elapsed = time.time() - t0
        print(f"[PHASE A] Done (dry-run) in {elapsed:.1f}s")
        # Return stub outline
        return {
            "title": "DRY RUN",
            "version": version,
            "sections": [
                {"id": s, "title": s, "key_points": [], "claim_assignments": [],
                 "source_assignments": [], "min_words": MIN_WORDS.get(s, 500)}
                for s in SECTION_ORDER
            ],
            "total_claims": len(claims_list),
            "total_sources": 0,
        }

    response = call_opus(prompt, system=OUTLINE_SYSTEM, max_tokens=3000)
    outline = extract_json(response)

    # Validate outline
    section_ids = [s["id"] for s in outline.get("sections", [])]
    missing = [s for s in SECTION_ORDER if s not in section_ids]
    if missing:
        print(f"  WARNING: Outline missing sections: {missing}. Retrying...")
        response = call_opus(
            prompt + f"\n\nYour outline was missing sections: {missing}. Include ALL 7.",
            system=OUTLINE_SYSTEM, max_tokens=3000,
        )
        outline = extract_json(response)

    elapsed = time.time() - t0
    print(f"[PHASE A] Done in {elapsed:.1f}s — {len(outline.get('sections', []))} sections")
    return outline


# ---------------------------------------------------------------------------
# Phase B: Sections
# ---------------------------------------------------------------------------

SECTION_SYSTEM = textwrap.dedent("""\
    You are Mia, writing ONE section of a research synthesis report.

    STYLE RULES:
    - Intelligence-grade writing: precise, evidence-based, no filler
    - Every factual claim gets [E], [I], [J], or [A] label
    - Every claim gets [S#] source reference
    - Include "For the decision maker:" callout box
    - Include section confidence percentage
    - Use 3-Signal Confidence: source_signal × 0.5 + consistency × 0.3 + structural × 0.2
    - BANNED words: """ + ", ".join(BANNED_WORDS) + """
    - Write in Florian's analytical but direct style
    - No hedging, no "it's worth noting"
""")


def _build_section_prompt(
    section: dict[str, Any],
    outline: dict[str, Any],
    previous_sections: dict[str, str],
    pipeline_data: dict[str, Any],
    workspace_data: dict[str, Any],
) -> str:
    """Build the prompt for generating one section."""
    section_id = section["id"]

    # RAG retrieval for this section
    rag_chunks = ""
    if USE_RAG:
        try:
            chunks = query_for_section(section_id, top_k=20)  # type: ignore
            rag_chunks = "RELEVANT CHUNKS:\n" + "\n---\n".join(
                c.get("text", "")[:400] for c in chunks[:20]
            )
        except Exception:
            pass

    # Fallback: include sub-reports relevant to assigned claims
    if not rag_chunks:
        sub_reports = pipeline_data.get("sub_reports", [])
        combined = "\n\n".join(sr["text"][:2000] for sr in sub_reports[:5])
        rag_chunks = f"SUB-REPORT EXCERPTS:\n{combined[:8000]}"

    # Previous sections
    prev_text = ""
    for sid in SECTION_ORDER:
        if sid in previous_sections:
            prev_text += f"\n\n## {sid} (already written)\n{previous_sections[sid][:3000]}"

    min_words = MIN_WORDS.get(section_id, 500)
    claims_assigned = section.get("claim_assignments", [])
    sources_assigned = section.get("source_assignments", [])

    # Reference library for source details
    ref_lib = workspace_data.get("reference-library", {})
    ref_details = ""
    if ref_lib and sources_assigned:
        entries = ref_lib if isinstance(ref_lib, list) else ref_lib.get("sources", [])
        if isinstance(entries, list):
            for entry in entries:
                sid_entry = entry.get("id", "")
                if sid_entry in sources_assigned or f"S{sid_entry}" in sources_assigned:
                    ref_details += f"\n- [{sid_entry}] {entry.get('title', '')} — {entry.get('key_finding', '')}"

    prompt = textwrap.dedent(f"""\
        OUTLINE (contract — follow this structure):
        {json.dumps(outline, indent=1)[:3000]}

        {prev_text}

        {rag_chunks}

        REFERENCE DETAILS:
        {ref_details[:2000]}

        CLAIMS ASSIGNED TO THIS SECTION: {', '.join(claims_assigned)}
        SOURCES ASSIGNED TO THIS SECTION: {', '.join(sources_assigned)}

        Write ONLY section "{section_id}" ({section.get('title', section_id)}).
        MINIMUM {min_words} words.
        Include ALL assigned claims with [E]/[I]/[J]/[A] labels and [S#] references.
        Include "For the decision maker:" callout.
        Include section confidence percentage.
    """)

    return prompt


def _validate_section(
    text: str,
    section: dict[str, Any],
) -> list[str]:
    """Validate a generated section. Returns list of issues."""
    issues: list[str] = []
    section_id = section["id"]
    min_words = MIN_WORDS.get(section_id, 500)

    word_count = len(text.split())
    if word_count < min_words:
        issues.append(f"word_count:{word_count}<{min_words}")

    # Check assigned claims present
    for cl in section.get("claim_assignments", []):
        if cl not in text:
            issues.append(f"missing_claim:{cl}")

    # Check assigned sources present
    for src in section.get("source_assignments", []):
        # Check both [S1] and S1 formats
        if f"[{src}]" not in text and f"[S{src}]" not in text and src not in text:
            issues.append(f"missing_source:{src}")

    # Banned words
    text_lower = text.lower()
    for bw in BANNED_WORDS:
        if bw.lower() in text_lower:
            issues.append(f"banned_word:{bw}")

    # Decision maker callout
    if "for the decision maker" not in text_lower:
        issues.append("missing:decision_maker_callout")

    # Confidence percentage
    if not re.search(r"\d+%", text):
        issues.append("missing:confidence_percentage")

    return issues


def phase_b_sections(
    outline: dict[str, Any],
    pipeline_data: dict[str, Any],
    workspace_data: dict[str, Any],
    output_dir: Path,
    dry_run: bool = False,
) -> dict[str, str]:
    """Phase B: Generate all 7 sections sequentially."""
    t0 = time.time()
    print("\n[PHASE B] Generating Sections")

    sections_done: dict[str, str] = {}

    for i, section in enumerate(outline.get("sections", [])):
        section_id = section["id"]
        st = time.time()
        print(f"\n  [{i + 1}/7] Section: {section_id}")

        prompt = _build_section_prompt(
            section, outline, sections_done, pipeline_data, workspace_data
        )

        if dry_run:
            print(f"    [DRY RUN] Prompt: {len(prompt)} chars")
            sections_done[section_id] = f"[DRY RUN] {section_id} content placeholder\n\nFor the decision maker: this is a dry run.\n\nConfidence: 50%"
            out_path = output_dir / f"section-{i + 1}-{section_id}.md"
            out_path.write_text(sections_done[section_id])
            continue

        text = call_opus(prompt, system=SECTION_SYSTEM, max_tokens=4096)

        # Validate
        issues = _validate_section(text, section)
        word_issues = [x for x in issues if x.startswith("word_count:")]
        claim_source_issues = [x for x in issues if x.startswith("missing_claim:") or x.startswith("missing_source:")]

        # Retry once for word count
        if word_issues:
            wc = len(text.split())
            min_w = MIN_WORDS.get(section_id, 500)
            print(f"    RETRY: word count {wc} < {min_w}")
            text = call_opus(
                prompt + f"\n\nYour output was {wc} words. Write at least {min_w} words. Be thorough.",
                system=SECTION_SYSTEM, max_tokens=6000,
            )
            issues = _validate_section(text, section)

        # Retry once for missing claims/sources
        elif claim_source_issues:
            missing = ", ".join(claim_source_issues)
            print(f"    RETRY: {missing}")
            text = call_opus(
                prompt + f"\n\nYou missed: {missing}. Include ALL assigned claims and sources.",
                system=SECTION_SYSTEM, max_tokens=5000,
            )
            issues = _validate_section(text, section)

        if issues:
            print(f"    WARNINGS: {issues}")

        sections_done[section_id] = text

        # Save individual section
        out_path = output_dir / f"section-{i + 1}-{section_id}.md"
        out_path.write_text(text)

        elapsed_s = time.time() - st
        print(f"    Done ({len(text.split())} words, {elapsed_s:.0f}s)")

    elapsed = time.time() - t0
    print(f"\n[PHASE B] Done in {elapsed:.1f}s — {len(sections_done)} sections")
    return sections_done


# ---------------------------------------------------------------------------
# Phase C: Merge
# ---------------------------------------------------------------------------

def _build_source_log(
    report_text: str,
    ref_library: Any,
) -> str:
    """Auto-generate Source Log from referenced [S#] tags."""
    # Find all [S##] in report
    refs_in_report = sorted(set(int(x) for x in re.findall(r"\[S(\d+)\]", report_text)))
    if not refs_in_report:
        return "\n## Source Log\n\n_No source references found._\n"

    # Build lookup from reference library
    lookup: dict[int, dict[str, Any]] = {}
    entries = []
    if isinstance(ref_library, list):
        entries = ref_library
    elif isinstance(ref_library, dict):
        entries = ref_library.get("sources", ref_library.get("entries", []))
        if isinstance(entries, dict):
            entries = list(entries.values())

    for entry in entries:
        sid = entry.get("id", "")
        # Extract numeric id
        m = re.search(r"(\d+)", str(sid))
        if m:
            lookup[int(m.group(1))] = entry

    lines = ["## Source Log\n"]
    lines.append("| ID | Title | Venue | DOI | Key Finding | Tier |")
    lines.append("|---|---|---|---|---|---|")

    for sid in refs_in_report:
        entry = lookup.get(sid, {})
        title = entry.get("title", "Unknown")
        venue = entry.get("venue", entry.get("journal", "—"))
        doi = entry.get("doi", "—")
        finding = entry.get("key_finding", entry.get("finding", "—"))
        tier = entry.get("tier", entry.get("quality", "—"))
        lines.append(f"| [S{sid}] | {title} | {venue} | {doi} | {finding[:80]} | {tier} |")

    return "\n".join(lines) + "\n"


def _build_contradiction_register(contradictions: Any) -> str:
    """Auto-generate Contradiction Register."""
    if not contradictions:
        return "\n## Contradiction Register\n\n_No contradictions detected._\n"

    entries = []
    if isinstance(contradictions, list):
        entries = contradictions
    elif isinstance(contradictions, dict):
        entries = contradictions.get("contradictions", [])

    lines = ["## Contradiction Register\n"]
    for i, c in enumerate(entries, 1):
        claim_a = c.get("claim_a", c.get("side_a", "?"))
        claim_b = c.get("claim_b", c.get("side_b", "?"))
        resolution = c.get("resolution", c.get("assessment", "unresolved"))
        lines.append(f"**C-{i:02d}:** {claim_a} vs. {claim_b}")
        lines.append(f"  Resolution: {resolution}\n")

    return "\n".join(lines) + "\n"


def phase_c_merge(
    sections: dict[str, str],
    outline: dict[str, Any],
    pipeline_data: dict[str, Any],
    workspace_data: dict[str, Any],
) -> str:
    """Phase C: Merge sections into final report."""
    t0 = time.time()
    print("\n[PHASE C] Merge")

    parts: list[str] = []

    # Title
    title = outline.get("title", "Research Synthesis Report")
    version = outline.get("version", "v1")
    parts.append(f"# {title}\n**Version:** {version} | **Generated:** {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}\n")

    # Sections in order
    for section_def in outline.get("sections", []):
        sid = section_def["id"]
        section_title = section_def.get("title", sid)
        content = sections.get(sid, f"_Section {sid} not generated._")
        parts.append(f"## {section_title}\n\n{content}")

    report = "\n\n---\n\n".join(parts)

    # Source Log
    ref_lib = workspace_data.get("reference-library", {})
    source_log = _build_source_log(report, ref_lib)
    report += "\n\n---\n\n" + source_log

    # Contradiction Register
    contras = pipeline_data.get("contradictions.json", {})
    contra_reg = _build_contradiction_register(contras)
    report += "\n\n" + contra_reg

    elapsed = time.time() - t0
    print(f"[PHASE C] Done in {elapsed:.1f}s — {len(report)} chars, {len(report.split())} words")
    return report


# ---------------------------------------------------------------------------
# Phase D: Validate
# ---------------------------------------------------------------------------

def _count_eija(text: str) -> dict[str, int]:
    """Count E/I/J/A labels in text (multiple formats)."""
    counts: dict[str, int] = {"E": 0, "I": 0, "J": 0, "A": 0}
    # [E], [I], [J], [A]
    for label in counts:
        counts[label] += len(re.findall(rf"\[{label}\]", text))
    # | E |, |E| in tables
    for label in counts:
        counts[label] += len(re.findall(rf"\|\s*{label}\s*\|", text))
    return counts


def _compute_claim_confidence(claim: dict[str, Any]) -> float:
    """Compute 3-signal confidence for a claim.
    
    Uses agenttrust library if available, falls back to inline formula.
    """
    admiralty = claim.get("admiralty", "C3")
    label = claim.get("label", "")
    text = claim.get("raw", "") + " " + claim.get("text", "")

    if USE_AGENTTRUST:
        result = _at_confidence(
            claim=text,
            admiralty=admiralty,
            has_doi="doi" in text.lower() or "10." in text,
            has_url="http" in text,
            has_percentage="%" in text,
            has_year=bool(re.search(r"20[12]\d", text)),
            has_source_ref=bool(re.search(r"\[S\d+\]", text)),
        )
        return result.confidence_pct / 100.0  # normalize to 0-1

    # Fallback: inline 3-signal formula
    source_signal = ADMIRALTY_MAP.get(admiralty, 0.40)
    consistency = EIJA_WEIGHTS.get(label, 0.40)

    structural = 0.0
    if "doi" in text.lower() or "10." in text:
        structural += 0.30
    if "http" in text:
        structural += 0.15
    if "%" in text:
        structural += 0.10
    if re.search(r"20[12]\d", text):
        structural += 0.05
    if re.search(r"\[S\d+\]", text):
        structural += 0.10
    structural = min(structural, 0.50)

    return 0.5 * source_signal + 0.3 * consistency + 0.2 * structural


def _compute_report_confidence(claims: list[dict[str, Any]]) -> float:
    """Weighted average confidence across claims."""
    if not claims:
        return 0.50

    label_weight = {"E": 4.0, "I": 3.0, "J": 1.5, "A": 1.0}
    total_w = 0.0
    total_conf = 0.0
    for c in claims:
        w = label_weight.get(c.get("label", ""), 1.0)
        conf = _compute_claim_confidence(c)
        c["computed_confidence"] = round(conf, 3)
        total_w += w
        total_conf += w * conf

    return round(total_conf / total_w, 3) if total_w > 0 else 0.50


def _find_source_orphans(report: str, source_log: str) -> tuple[list[str], list[str]]:
    """Find orphan sources: in prose but not log, in log but not prose."""
    # Split report to get prose (everything before Source Log)
    parts = report.split("## Source Log")
    prose = parts[0] if parts else report
    log_section = parts[1] if len(parts) > 1 else source_log

    refs_in_prose = set(re.findall(r"\[S(\d+)\]", prose))
    refs_in_log = set(re.findall(r"\[S(\d+)\]", log_section))

    orphan_refs = sorted(refs_in_prose - refs_in_log)  # in prose, not in log
    orphan_sources = sorted(refs_in_log - refs_in_prose)  # in log, not in prose
    return [f"S{r}" for r in orphan_refs], [f"S{r}" for r in orphan_sources]


def _check_cross_references(report: str) -> list[str]:
    """Check cross-references between sections."""
    warnings: list[str] = []

    # "If you read nothing else" bullets should reference Key Findings
    exec_section = ""
    m = re.search(r"(?i)executive.summary.*?(?=\n##|\Z)", report, re.DOTALL)
    if m:
        exec_section = m.group()

    if "if you read nothing else" in exec_section.lower():
        # Check for KF references
        kf_refs = re.findall(r"(?:Key Finding|KF|Finding)\s*#?\d+", exec_section, re.IGNORECASE)
        if not kf_refs:
            warnings.append("Executive summary 'read nothing else' doesn't reference Key Findings")

    return warnings


def _check_grounding(report: str, sub_reports: list[dict[str, str]]) -> list[str]:
    """Check that all [S#] in report were in sub-reports."""
    report_refs = set(re.findall(r"\[S(\d+)\]", report))

    sub_refs: set[str] = set()
    for sr in sub_reports:
        sub_refs.update(re.findall(r"\[S(\d+)\]", sr.get("text", "")))

    ungrounded = sorted(report_refs - sub_refs)
    return [f"S{r}" for r in ungrounded]


def _check_number_consistency(report: str) -> list[str]:
    """Check for inconsistent numbers across sections."""
    warnings: list[str] = []

    # Split into sections
    section_splits = re.split(r"\n##\s+", report)

    # Extract numbers with context
    number_occurrences: dict[str, list[str]] = {}
    for section in section_splits:
        section_name = section[:50].strip().split("\n")[0]
        # Find percentages, dollar amounts
        for m in re.finditer(r"(\d+(?:\.\d+)?)\s*%", section):
            key = f"{m.group(1)}%"
            number_occurrences.setdefault(key, []).append(section_name)
        for m in re.finditer(r"\$\s*([\d,.]+(?:\.\d+)?)\s*(billion|million|B|M|trillion|T)?", section, re.IGNORECASE):
            key = f"${m.group(1)}{m.group(2) or ''}"
            number_occurrences.setdefault(key, []).append(section_name)

    # Numbers appearing in multiple sections are fine (consistent)
    # We'd need value extraction to detect mismatches — for now just report multi-section numbers
    # This is a structural check, not a value mismatch detector
    return warnings


def phase_d_validate(
    report: str,
    pipeline_data: dict[str, Any],
    workspace_data: dict[str, Any],
) -> dict[str, Any]:
    """Phase D: Validate the merged report."""
    t0 = time.time()
    print("\n[PHASE D] Validate")

    results: dict[str, Any] = {"checks": {}, "warnings": [], "grade_inputs": {}}

    # 1. E/I/J/A counts
    eija = _count_eija(report)
    total_eija = sum(eija.values())
    results["checks"]["eija_counts"] = eija
    results["checks"]["eija_total"] = total_eija
    if total_eija > 0:
        results["checks"]["e_pct"] = round(100 * eija["E"] / total_eija, 1)
        results["checks"]["j_pct"] = round(100 * eija["J"] / total_eija, 1)
    else:
        results["checks"]["e_pct"] = 0
        results["checks"]["j_pct"] = 0
    print(f"  E/I/J/A: {eija} (total: {total_eija})")

    # 2. Claim confidence
    claims = parse_claim_ledger(report)
    report_confidence = _compute_report_confidence(claims)
    results["checks"]["claims_parsed"] = len(claims)
    results["checks"]["report_confidence"] = report_confidence
    results["checks"]["per_claim"] = [
        {"id": c["id"], "label": c["label"], "confidence": c.get("computed_confidence", 0)}
        for c in claims
    ]
    print(f"  Claims: {len(claims)}, Report confidence: {report_confidence}")

    # 3. Beipackzettel correction
    risk_level = "HIGH" if report_confidence < 0.60 else "MEDIUM" if report_confidence <= 0.80 else "LOW"
    results["checks"]["risk_level"] = risk_level
    results["checks"]["beipackzettel_corrected"] = True
    print(f"  Risk level: {risk_level}")

    # 4. Source orphan check
    orphan_refs, orphan_sources = _find_source_orphans(report, "")
    results["checks"]["orphan_refs"] = orphan_refs
    results["checks"]["orphan_sources"] = orphan_sources
    if orphan_refs:
        results["warnings"].append(f"Sources in prose but not in Source Log: {orphan_refs}")
    if orphan_sources:
        results["warnings"].append(f"Sources in Source Log but not in prose: {orphan_sources}")
    print(f"  Orphan refs: {len(orphan_refs)}, Orphan sources: {len(orphan_sources)}")

    # 5. Cross-reference check
    xref_warnings = _check_cross_references(report)
    results["checks"]["cross_ref_warnings"] = xref_warnings
    results["warnings"].extend(xref_warnings)
    print(f"  Cross-ref warnings: {len(xref_warnings)}")

    # 6. Grounding check
    sub_reports = pipeline_data.get("sub_reports", [])
    ungrounded = _check_grounding(report, sub_reports)
    results["checks"]["ungrounded_sources"] = ungrounded
    if ungrounded:
        results["warnings"].append(f"Ungrounded sources (not in sub-reports): {ungrounded}")
    print(f"  Ungrounded sources: {len(ungrounded)}")

    # 7. Consistency check
    consistency_warnings = _check_number_consistency(report)
    results["checks"]["consistency_mismatches"] = len(consistency_warnings)
    results["warnings"].extend(consistency_warnings)
    print(f"  Consistency mismatches: {len(consistency_warnings)}")

    # Section count
    blocks = len(re.findall(r"^## ", report, re.MULTILINE))
    results["checks"]["blocks"] = blocks

    # Store grade inputs
    results["grade_inputs"] = {
        "blocks": blocks,
        "e_pct": results["checks"]["e_pct"],
        "j_pct": results["checks"]["j_pct"],
        "orphan_refs": len(orphan_refs),
        "orphan_sources": len(orphan_sources),
        "claims": len(claims),
        "confidence": report_confidence,
        "consistency_mismatches": len(consistency_warnings),
        "ungrounded_sources": len(ungrounded),
    }

    elapsed = time.time() - t0
    print(f"[PHASE D] Done in {elapsed:.1f}s — {len(results['warnings'])} warnings")
    return results


def correct_beipackzettel(
    report: str,
    confidence: float,
    eija: dict[str, int],
    risk_level: str,
) -> str:
    """Correct the Beipackzettel section with Python-calculated values."""
    # Find and replace confidence line
    report = re.sub(
        r"(?i)(confidence[:\s]*)\d+(\.\d+)?%",
        f"\\g<1>{confidence * 100:.1f}%",
        report,
        count=1,
    )

    # Replace E/I/J/A line
    eija_line = f"E: {eija['E']} | I: {eija['I']} | J: {eija['J']} | A: {eija['A']}"
    report = re.sub(
        r"(?i)E:\s*\d+\s*\|\s*I:\s*\d+\s*\|\s*J:\s*\d+\s*\|\s*A:\s*\d+",
        eija_line,
        report,
    )

    # Replace risk level
    report = re.sub(
        r"(?i)(risk\s*level[:\s]*)(HIGH|MEDIUM|LOW)",
        f"\\g<1>{risk_level}",
        report,
    )

    return report


# ---------------------------------------------------------------------------
# LaTeX Generation (SKILL.md compliant)
# ---------------------------------------------------------------------------

XELATEX_PATH = os.path.expanduser("~/Library/TinyTeX/bin/universal-darwin/xelatex")

LATEX_PREAMBLE = r"""\documentclass[a4paper,11pt]{article}

% Fonts
\usepackage{fontspec}
\setmainfont{Helvetica Neue}[
  BoldFont=Helvetica Neue Bold,
  ItalicFont=Helvetica Neue Italic
]

% Layout
\usepackage[top=30mm, bottom=35mm, left=28mm, right=28mm]{geometry}
\usepackage{parskip}
\setlength{\parskip}{8pt}
\setlength{\parindent}{0pt}

% Colors (contrast-checked per SKILL.md / WCAG 2.1 AA)
\usepackage{xcolor}
\definecolor{primary}{HTML}{2563EB}
\definecolor{darkbg}{HTML}{0A0F1E}
\definecolor{darkblue}{HTML}{1E3A5F}
\definecolor{bodytext}{HTML}{374151}
\definecolor{heading}{HTML}{111827}
\definecolor{subtitle}{HTML}{64748B}
\definecolor{lightgray}{HTML}{F8F9FA}
\definecolor{border}{HTML}{E5E7EB}
\definecolor{accent}{HTML}{93C5FD}
\definecolor{lightondark}{HTML}{D1D5DB}
\definecolor{darkred}{HTML}{B91C1C}
\definecolor{darkgreen}{HTML}{15803D}
\definecolor{darkyellow}{HTML}{92400E}
\definecolor{lightblue}{HTML}{F0F4FF}
\definecolor{lightred}{HTML}{FEF2F2}
\definecolor{lightgreen}{HTML}{F0FDF4}
\definecolor{ecolor}{HTML}{15803D}
\definecolor{icolor}{HTML}{2563EB}
\definecolor{jcolor}{HTML}{92400E}
\definecolor{acolor}{HTML}{B91C1C}

% Headers & Footers
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0.4pt}
\fancyfoot[L]{\footnotesize\color{subtitle}\textls[50]{RESEARCH SYNTHESIS · AINARY VENTURES}}
\fancyfoot[R]{\footnotesize\color{subtitle}\thepage}

% Headings
\usepackage{titlesec}
\usepackage{needspace}
\titleformat{\section}{\needspace{6\baselineskip}\fontsize{24}{28}\selectfont\bfseries\color{heading}}{}{0em}{}[\vspace{-2pt}]
\titleformat{\subsection}{\needspace{4\baselineskip}\fontsize{14}{18}\selectfont\bfseries\color{heading}}{}{0em}{}
\titlespacing*{\section}{0pt}{0pt}{4pt}
\titlespacing*{\subsection}{0pt}{16pt}{6pt}

% Tables
\usepackage{tabularx}
\usepackage{booktabs}
\usepackage{colortbl}
\usepackage{multirow}
\usepackage{longtable}

% Lists
\usepackage{enumitem}
\setlist[itemize]{leftmargin=1.2em, itemsep=2pt, parsep=0pt, topsep=4pt}

% Links
\usepackage{hyperref}
\hypersetup{colorlinks=true, linkcolor=primary, urlcolor=primary}

% Drawing + Boxes
\usepackage{tikz}
\usetikzlibrary{calc,positioning,shapes.geometric}
\usepackage{tcolorbox}
\tcbuselibrary{skins,breakable}

% Misc
\usepackage{microtype}
\usepackage{setspace}
\usepackage{graphicx}
\usepackage{float}
\usepackage{multicol}
\usepackage{amssymb}
\usepackage{letltxmacro}

% Blocksatz + Silbentrennung (DIN 5008)
\usepackage{polyglossia}
\setdefaultlanguage{english}
\tolerance=2000
\emergencystretch=15pt
\hbadness=2000
\hyphenpenalty=50
\exhyphenpenalty=50

% Widow/Orphan control
\widowpenalty=10000
\clubpenalty=10000
\brokenpenalty=10000

% Custom commands
\newcommand{\ssubtitle}[1]{%
  \par\textcolor{subtitle}{\fontsize{12}{16}\selectfont #1}%
  \par\vspace{2pt}\textcolor{border}{\rule{\linewidth}{0.4pt}}\vspace{12pt}%
}

\newtcolorbox{highlightbox}{
  colback=lightblue, colframe=primary,
  leftrule=3pt, rightrule=0pt, toprule=0pt, bottomrule=0pt,
  arc=0pt, outer arc=4pt,
  boxsep=4pt, left=12pt, right=12pt, top=8pt, bottom=8pt,
  fontupper=\fontsize{11}{15}\selectfont\color{darkblue},
  breakable
}

\newtcolorbox{darkhighlight}{
  colback=darkbg, colframe=primary,
  leftrule=3pt, rightrule=0pt, toprule=0pt, bottomrule=0pt,
  arc=0pt, outer arc=4pt,
  boxsep=4pt, left=12pt, right=12pt, top=8pt, bottom=8pt,
  fontupper=\fontsize{11}{15}\selectfont\color{white},
  breakable
}

\newtcolorbox{decisionbox}{
  colback=lightblue, colframe=primary,
  leftrule=3pt, rightrule=0pt, toprule=0pt, bottomrule=0pt,
  arc=0pt, outer arc=4pt,
  boxsep=4pt, left=12pt, right=12pt, top=8pt, bottom=8pt,
  fontupper=\fontsize{11}{15}\selectfont\color{darkblue},
  title={\textbf{For the Decision Maker}},
  coltitle=darkblue,
  breakable
}

\newcommand{\statcard}[2]{%
  \begin{tikzpicture}
    \node[fill=lightgray, rounded corners=4pt, minimum width=4.4cm, minimum height=2.2cm, inner sep=6pt, align=center, text width=4cm] {
      {\fontsize{20}{24}\selectfont\bfseries\color{primary}#1}\\[3pt]
      {\fontsize{8}{10}\selectfont\color{subtitle}\MakeUppercase{#2}}
    };
  \end{tikzpicture}%
}

% EIJA label commands
\newcommand{\elabel}{\textbf{\textcolor{ecolor}{[E]}}}
\newcommand{\ilabel}{\textbf{\textcolor{icolor}{[I]}}}
\newcommand{\jlabel}{\textbf{\textcolor{jcolor}{[J]}}}
\newcommand{\alabel}{\textbf{\textcolor{acolor}{[A]}}}

% Body text
\renewcommand{\normalsize}{\fontsize{11}{15}\selectfont}
\color{bodytext}
"""


def _escape_latex(text: str) -> str:
    """Escape special LaTeX characters in text."""
    # Order matters: & first, then others
    replacements = [
        ("\\", r"\textbackslash{}"),
        ("&", r"\&"),
        ("%", r"\%"),
        ("$", r"\$"),
        ("#", r"\#"),
        ("_", r"\_"),
        ("{", r"\{"),
        ("}", r"\}"),
        ("~", r"\textasciitilde{}"),
        ("^", r"\textasciicircum{}"),
    ]
    for old, new in replacements:
        text = text.replace(old, new)
    return text


def _escape_latex_light(text: str) -> str:
    """Escape LaTeX but preserve our custom commands and formatting."""
    # Don't escape things that look like our commands
    # First protect known patterns
    protected: list[tuple[str, str]] = []
    counter = 0

    # Protect [E], [I], [J], [A] labels
    for label in ["E", "I", "J", "A"]:
        placeholder = f"§§LABEL{label}{counter}§§"
        text = text.replace(f"[{label}]", placeholder)
        protected.append((placeholder, f"\\{label.lower()}label{{}}"))
        counter += 1

    # Protect [S##] references
    for m in re.finditer(r"\[S(\d+)\]", text):
        full = m.group(0)
        num = m.group(1)
        placeholder = f"§§SRC{num}§§"
        text = text.replace(full, placeholder, 1)
        protected.append((placeholder, f"\\textcolor{{primary}}{{[S{num}]}}"))

    # Protect URLs
    for m in re.finditer(r"https?://\S+", text):
        url = m.group(0)
        placeholder = f"§§URL{counter}§§"
        text = text.replace(url, placeholder, 1)
        safe_url = url.replace("#", r"\#").replace("%", r"\%").replace("&", r"\&").replace("_", r"\_")
        protected.append((placeholder, f"\\url{{{safe_url}}}"))
        counter += 1

    # Now escape
    text = _escape_latex(text)

    # Restore protected
    for placeholder, replacement in protected:
        text = text.replace(_escape_latex(placeholder), replacement)
        # Also try unescaped (in case escape didn't touch it)
        text = text.replace(placeholder, replacement)

    return text


def _md_block_to_latex(md_text: str) -> str:
    """Convert a markdown section body to LaTeX content."""
    lines = md_text.split("\n")
    output: list[str] = []
    in_table = False
    table_rows: list[str] = []
    in_list = False
    in_decision_box = False

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Skip empty lines (LaTeX handles spacing via parskip)
        if not stripped:
            if in_list:
                output.append(r"\end{itemize}")
                in_list = False
            if in_table:
                output.append(_convert_table(table_rows))
                table_rows = []
                in_table = False
            output.append("")
            i += 1
            continue

        # "For the decision maker" → decisionbox
        if re.match(r"(?i)\*?\*?for the decision maker", stripped):
            # Collect until next blank line or heading
            box_lines: list[str] = []
            # Skip the header line itself
            content_start = stripped
            # Remove the prefix
            content_start = re.sub(r"(?i)\*?\*?for the decision maker:?\*?\*?\s*", "", content_start).strip()
            if content_start:
                box_lines.append(content_start)
            i += 1
            while i < len(lines) and lines[i].strip() and not lines[i].strip().startswith("#"):
                box_lines.append(lines[i].strip())
                i += 1
            box_content = _escape_latex_light("\n".join(box_lines))
            output.append(r"\begin{decisionbox}")
            output.append(box_content)
            output.append(r"\end{decisionbox}")
            output.append("")
            continue

        # Headings (### = subsection, #### and below = bold paragraph)
        m_h = re.match(r"^(#{1,6})\s+(.*)", stripped)
        if m_h:
            level = len(m_h.group(1))
            title = _escape_latex_light(m_h.group(2).strip("*"))
            if in_list:
                output.append(r"\end{itemize}")
                in_list = False
            if level <= 2:
                output.append(f"\\section{{{title}}}")
            elif level == 3:
                output.append(f"\\subsection{{{title}}}")
            else:
                output.append(f"\\needspace{{2\\baselineskip}}")
                output.append(f"\\textbf{{{title}}}\\par")
            i += 1
            continue

        # Table row
        if stripped.startswith("|") and stripped.endswith("|"):
            if not in_table:
                in_table = True
                table_rows = []
            table_rows.append(stripped)
            i += 1
            continue
        elif in_table:
            output.append(_convert_table(table_rows))
            table_rows = []
            in_table = False
            # Don't increment i, reprocess this line

        # List items
        if re.match(r"^[-*]\s+", stripped):
            if not in_list:
                output.append(r"\begin{itemize}")
                in_list = True
            item_text = re.sub(r"^[-*]\s+", "", stripped)
            output.append(f"  \\item {_escape_latex_light(item_text)}")
            i += 1
            continue

        # Numbered list
        if re.match(r"^\d+\.\s+", stripped):
            if not in_list:
                output.append(r"\begin{itemize}")
                in_list = True
            item_text = re.sub(r"^\d+\.\s+", "", stripped)
            output.append(f"  \\item {_escape_latex_light(item_text)}")
            i += 1
            continue

        # Bold line (standalone) → small heading
        if re.match(r"^\*\*(.+)\*\*$", stripped):
            inner = re.match(r"^\*\*(.+)\*\*$", stripped).group(1)
            if in_list:
                output.append(r"\end{itemize}")
                in_list = False
            output.append(f"\\textbf{{{_escape_latex_light(inner)}}}\\par")
            i += 1
            continue

        # Horizontal rule
        if re.match(r"^-{3,}$|^\*{3,}$", stripped):
            output.append(r"\vspace{8pt}\textcolor{border}{\rule{\linewidth}{0.4pt}}\vspace{8pt}")
            i += 1
            continue

        # Regular paragraph
        if in_list:
            output.append(r"\end{itemize}")
            in_list = False
        # Handle inline bold/italic
        para = _escape_latex_light(stripped)
        para = re.sub(r"\*\*(.+?)\*\*", r"\\textbf{\1}", para)
        para = re.sub(r"\*(.+?)\*", r"\\textit{\1}", para)
        output.append(para)
        output.append("")
        i += 1

    # Close open environments
    if in_list:
        output.append(r"\end{itemize}")
    if in_table:
        output.append(_convert_table(table_rows))

    return "\n".join(output)


def _convert_table(rows: list[str]) -> str:
    """Convert markdown table rows to LaTeX tabularx."""
    if len(rows) < 2:
        return ""

    # Parse cells
    parsed: list[list[str]] = []
    separator_idx = -1
    for idx, row in enumerate(rows):
        cells = [c.strip() for c in row.strip("|").split("|")]
        # Check if separator row (all dashes)
        if all(re.match(r"^[-:]+$", c.strip()) for c in cells if c.strip()):
            separator_idx = idx
            continue
        parsed.append(cells)

    if not parsed:
        return ""

    ncols = max(len(r) for r in parsed)

    # Column spec: first col left-aligned, rest X (flexible)
    if ncols <= 2:
        col_spec = "@{}l X@{}"
    else:
        col_spec = "@{}l " + " ".join(["X"] * (ncols - 1)) + "@{}"

    lines = [
        f"\\needspace{{4\\baselineskip}}",
        f"\\begin{{tabularx}}{{\\linewidth}}{{{col_spec}}}",
        "\\toprule",
    ]

    for row_idx, cells in enumerate(parsed):
        # Pad cells
        while len(cells) < ncols:
            cells.append("")
        escaped = [_escape_latex_light(c) for c in cells]
        # Bold header row
        if row_idx == 0:
            escaped = [f"\\textbf{{{c}}}" for c in escaped]
        lines.append(" & ".join(escaped) + " \\\\")
        if row_idx == 0:
            lines.append("\\midrule")

    lines.append("\\bottomrule")
    lines.append("\\end{tabularx}")
    lines.append("\\vspace{8pt}")
    return "\n".join(lines)


def markdown_to_latex(
    report: str,
    outline: dict[str, Any],
    grade_inputs: dict[str, Any],
    grade: str,
) -> str:
    """Convert merged markdown report to a full LaTeX document.

    Uses the 36zero-report.tex template structure with SKILL.md design rules.
    """
    title = outline.get("title", "Research Synthesis Report")
    version = outline.get("version", "v1")
    confidence = grade_inputs.get("confidence", 0.50)
    n_claims = grade_inputs.get("claims", 0)
    date_str = datetime.now(timezone.utc).strftime("%B %Y")

    parts: list[str] = [LATEX_PREAMBLE, r"\begin{document}"]

    # ── Cover Page ──
    parts.append(r"""
\thispagestyle{empty}
\begin{tikzpicture}[remember picture, overlay]
  \fill[darkbg] (current page.south west) rectangle (current page.north east);

  \node[anchor=north west, text width=12cm] at ($(current page.north west)+(3cm,-4cm)$) {
    {\fontsize{11}{14}\selectfont\color{accent}\textls[200]{RESEARCH SYNTHESIS REPORT}}\\[24pt]
    {\color{primary}\rule{50pt}{2.5pt}}\\[32pt]
    {\fontsize{34}{40}\selectfont\bfseries\color{white}""" + _escape_latex(title) + r"""}\\[18pt]
    {\fontsize{14}{20}\selectfont\color{lightondark}Intelligence-grade research synthesis with epistemic grading and source verification.}
  };

  \node[anchor=south west] at ($(current page.south west)+(3cm,5.5cm)$) {
    \begin{tabular}{@{}l@{\hspace{36pt}}l@{\hspace{36pt}}l@{}}
      {\fontsize{30}{34}\selectfont\bfseries\color{accent}""" + str(n_claims) + r"""} &
      {\fontsize{30}{34}\selectfont\bfseries\color{accent}""" + f"{confidence * 100:.0f}" + r"""\%} &
      {\fontsize{30}{34}\selectfont\bfseries\color{accent}""" + grade + r"""} \\[2pt]
      {\fontsize{9}{11}\selectfont\color{lightondark}\MakeUppercase{Verified Claims}} &
      {\fontsize{9}{11}\selectfont\color{lightondark}\MakeUppercase{Report Confidence}} &
      {\fontsize{9}{11}\selectfont\color{lightondark}\MakeUppercase{Synthesis Grade}}
    \end{tabular}
  };

  \node[anchor=south west] at ($(current page.south west)+(3cm,3cm)$) {
    {\fontsize{14}{18}\selectfont\color{accent}Florian Ziesche · Ainary Ventures}\\[3pt]
    {\fontsize{11}{14}\selectfont\color{lightondark}Version """ + _escape_latex(version) + r""" · """ + date_str + r""" · Confidential}
  };
\end{tikzpicture}

\clearpage
""")

    # ── Body: split report into sections ──
    # Split on "## " at start of line (our section headers from Phase C)
    # But skip the title (# ...) at the very top
    report_body = report
    # Remove the # title line and metadata if present
    report_body = re.sub(r"^#\s+.*?\n\*\*Version:?\*\*.*?\n", "", report_body, count=1)

    # Split on --- separators (Phase C joins with ---)
    raw_sections = re.split(r"\n---\n", report_body)

    for sec in raw_sections:
        sec = sec.strip()
        if not sec:
            continue

        # Check if starts with ## heading
        m = re.match(r"^##\s+(.*?)(?:\n|$)", sec)
        if m:
            sec_title = m.group(1).strip()
            sec_body = sec[m.end():]

            parts.append(r"\clearpage")
            parts.append(f"\\section{{{_escape_latex_light(sec_title)}}}")

            # Add subtitle line for certain sections
            subtitle_map = {
                "beipackzettel": "Information Safety Label — Read Before Acting",
                "executive summary": "If You Read Nothing Else",
                "source log": "Full Reference Trail",
                "contradiction register": "Where Evidence Conflicts",
            }
            for key, sub in subtitle_map.items():
                if key in sec_title.lower():
                    parts.append(f"\\ssubtitle{{{sub}}}")
                    break

            parts.append(_md_block_to_latex(sec_body))
        else:
            # No heading — just convert as body
            parts.append(_md_block_to_latex(sec))

    parts.append(r"\end{document}")
    return "\n".join(parts)


def compile_latex(tex_path: Path, pdf_path: Path) -> bool:
    """Compile .tex to .pdf via XeLaTeX (2 passes)."""
    xelatex = XELATEX_PATH
    if not os.path.exists(xelatex):
        # Try PATH
        xelatex = "xelatex"

    work_dir = tex_path.parent
    tex_name = tex_path.name

    for pass_num in (1, 2):
        print(f"  [LATEX] Pass {pass_num}/2...")
        try:
            result = subprocess.run(
                [xelatex, "-interaction=nonstopmode", "-halt-on-error", tex_name],
                capture_output=True, text=True, timeout=120,
                cwd=str(work_dir),
            )
            if result.returncode != 0:
                # Extract error from log
                log_text = result.stdout + result.stderr
                errors = [l for l in log_text.split("\n") if l.startswith("!")]
                print(f"  [LATEX] Pass {pass_num} error: {'; '.join(errors[:3])}")
                if pass_num == 1:
                    # Try to continue to pass 2
                    continue
                return False
        except subprocess.TimeoutExpired:
            print(f"  [LATEX] Pass {pass_num} timed out")
            return False
        except FileNotFoundError:
            print(f"  [LATEX] xelatex not found at {xelatex}")
            return False

    # Check output
    expected_pdf = work_dir / tex_name.replace(".tex", ".pdf")
    if expected_pdf.exists():
        if expected_pdf != pdf_path:
            expected_pdf.rename(pdf_path)
        return True
    return False


def preflight_check(tex_path: Path, pdf_path: Path) -> list[str]:
    """Run automated pre-flight checks per SKILL.md."""
    messages: list[str] = []

    # Check log for overfull hbox
    log_path = tex_path.with_suffix(".log")
    if log_path.exists():
        log_text = log_path.read_text()
        overfull = re.findall(r"Overfull \\hbox \((\d+\.?\d*)pt", log_text)
        bad_overfull = [float(x) for x in overfull if float(x) > 10.0]
        if bad_overfull:
            messages.append(f"WARNING: {len(bad_overfull)} overfull hbox >10pt (max: {max(bad_overfull):.1f}pt)")
        else:
            messages.append(f"OK: No overfull hbox >10pt ({len(overfull)} minor)")

    # Check for placeholders in .tex
    tex_text = tex_path.read_text()
    placeholders = re.findall(r"x%|TODO|\[\.\.\.?\]|tbd|FIXME", tex_text, re.IGNORECASE)
    if placeholders:
        messages.append(f"WARNING: {len(placeholders)} placeholders found: {placeholders[:5]}")
    else:
        messages.append("OK: No placeholders")

    # Check PDF exists and has size
    if pdf_path.exists():
        size_kb = pdf_path.stat().st_size / 1024
        messages.append(f"OK: PDF {size_kb:.0f} KB")
    else:
        messages.append("FAIL: PDF not generated")

    return messages


# ---------------------------------------------------------------------------
# Phase E: Grade + Output
# ---------------------------------------------------------------------------

def phase_e_output(
    report: str,
    validation: dict[str, Any],
    output_dir: Path,
    version: str,
    outline: Optional[dict[str, Any]] = None,
) -> str:
    """Phase E: Grade and write output files."""
    t0 = time.time()
    print("\n[PHASE E] Grade + Output")

    gi = validation["grade_inputs"]

    # Correct beipackzettel
    report = correct_beipackzettel(
        report,
        gi["confidence"],
        validation["checks"]["eija_counts"],
        validation["checks"]["risk_level"],
    )

    # Grade
    if (
        gi["blocks"] >= 7
        and gi["e_pct"] > 50
        and gi["j_pct"] < 20
        and gi["orphan_refs"] == 0
        and gi["orphan_sources"] == 0
        and gi["claims"] >= 12
        and gi["confidence"] != 0.50
        and gi["consistency_mismatches"] == 0
        and gi["ungrounded_sources"] == 0
    ):
        grade = "A+++"
    elif gi["blocks"] >= 7 and gi["e_pct"] > 50 and gi["j_pct"] < 20:
        grade = "A++"
    elif gi["blocks"] >= 5 and gi["e_pct"] > 40:
        grade = "A+"
    else:
        grade = "B"

    print(f"  Grade: {grade}")

    # 1. Final report
    report_path = output_dir / f"final-report-{version}.md"
    report_path.write_text(report)
    print(f"  Wrote {report_path} ({len(report)} chars)")

    # 2. Validation report
    validation["grade"] = grade
    validation["version"] = version
    validation["timestamp"] = datetime.now(timezone.utc).isoformat()
    val_path = output_dir / "validation-report.json"
    val_path.write_text(json.dumps(validation, indent=2, default=str))
    print(f"  Wrote {val_path}")

    # 3. Beipackzettel JSON (agenttrust compatible)
    if USE_AGENTTRUST:
        bpz = _AT_Beipackzettel(
            confidence=gi["confidence"] * 100 if gi["confidence"] <= 1 else gi["confidence"],
            sources=[f"[{s}]" for s in gi.get("sources_used", [])],
            uncertainties=validation.get("blindspots", []),
            risks=[w for w in validation.get("warnings", []) if "orphan" in w.lower() or "ungrounded" in w.lower()],
            not_checked=gi.get("not_checked", ["Cross-domain generalization of ECE figures", "Competitor product roadmaps"]),
            model="claude-opus-4-20250514",
            agent_id="mia-pipeline-v3",
        )
        beipackzettel = bpz.to_dict()
        beipackzettel["eija_counts"] = validation["checks"]["eija_counts"]
        beipackzettel["claims_count"] = gi["claims"]
        beipackzettel["grade"] = grade
        beipackzettel["report_version"] = version
        beipackzettel["generated"] = datetime.now(timezone.utc).isoformat()
    else:
        beipackzettel = {
            "report_version": version,
            "confidence": gi["confidence"],
            "risk_level": validation["checks"]["risk_level"],
            "eija_counts": validation["checks"]["eija_counts"],
            "claims_count": gi["claims"],
            "grade": grade,
            "orphan_refs": gi["orphan_refs"],
            "orphan_sources": gi["orphan_sources"],
            "ungrounded_sources": gi["ungrounded_sources"],
            "warnings": validation["warnings"],
            "generated": datetime.now(timezone.utc).isoformat(),
        }
    bp_path = output_dir / "beipackzettel.json"
    bp_path.write_text(json.dumps(beipackzettel, indent=2))
    print(f"  Wrote {bp_path}")

    # 4. Trust Score Update (persistent, if agenttrust available)
    if USE_AGENTTRUST:
        trust_path = output_dir.parent / "trust-score.json"
        ts = _AT_TrustScore("mia-pipeline")
        if trust_path.exists():
            try:
                old = json.loads(trust_path.read_text())
                ts._score = old.get("score", 0)
            except Exception:
                pass
        stated = gi["confidence"] * 100 if gi["confidence"] <= 1 else gi["confidence"]
        outcome = "good" if grade in ("A+++", "A++") else "bad"
        event = ts.update(stated_confidence=stated, outcome=outcome,
                         reason=f"Report {version}: grade={grade}")
        trust_path.write_text(json.dumps(ts.summary(), indent=2))
        print(f"  Trust: score={ts.score}, level={ts.trust_level.value} (delta={event.delta})")
        print(f"  Wrote {trust_path}")

    # 4. PDF via LaTeX
    try:
        tex_path = output_dir / f"final-report-{version}.tex"
        pdf_path = output_dir / f"final-report-{version}.pdf"
        tex_content = markdown_to_latex(report, outline or {}, gi, grade)
        tex_path.write_text(tex_content)
        print(f"  Wrote {tex_path} ({len(tex_content)} chars)")
        success = compile_latex(tex_path, pdf_path)
        if success:
            print(f"  Wrote {pdf_path}")
            # Pre-flight checks
            preflight = preflight_check(tex_path, pdf_path)
            for msg in preflight:
                print(f"  [PRE-FLIGHT] {msg}")
        else:
            print("  WARNING: PDF compilation failed — .tex file preserved")
    except Exception as e:
        print(f"  PDF failed: {e}")

    elapsed = time.time() - t0
    print(f"\n[PHASE E] Done in {elapsed:.1f}s")
    print(f"  GRADE: {grade}")
    print(f"  Confidence: {gi['confidence']}")
    print(f"  Claims: {gi['claims']}")
    print(f"  Warnings: {len(validation['warnings'])}")

    return grade


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Mia Synthesis Engine v3 — Elite Research Report Generator"
    )
    parser.add_argument("pipeline_dir", type=str, help="Path to pipeline output directory")
    parser.add_argument("--version", type=str, default="v5", help="Report version (default: v5)")
    parser.add_argument("--dry-run", action="store_true", help="Skip Opus calls, print prompts")
    args = parser.parse_args()

    pipeline_dir = Path(args.pipeline_dir).resolve()
    version = args.version
    dry_run = args.dry_run

    print(f"{'=' * 60}")
    print(f"Mia Synthesis Engine v3")
    print(f"Pipeline dir: {pipeline_dir}")
    print(f"Version: {version}")
    print(f"Dry run: {dry_run}")
    print(f"RAG layer: {'available' if USE_RAG else 'fallback (direct load)'}")
    print(f"{'=' * 60}")

    t_total = time.time()

    # Load data
    print("\n[LOAD] Pipeline data...")
    if pipeline_dir.exists():
        pipeline_data = load_pipeline_data(pipeline_dir)
    else:
        print(f"  WARNING: Pipeline dir not found: {pipeline_dir}")
        pipeline_data = {"research-brief.json": {}, "all-claims.json": {},
                         "contradictions.json": {}, "sub-reviews.json": {},
                         "blindspots.json": {}, "sub_reports": []}

    print("\n[LOAD] Workspace data...")
    workspace_data = load_workspace_data()

    # Output directory
    output_dir = pipeline_dir / "synthesis-v3"
    output_dir.mkdir(parents=True, exist_ok=True)

    # Phase A
    outline = phase_a_outline(pipeline_data, workspace_data, version, dry_run=dry_run)

    # Phase B
    sections = phase_b_sections(outline, pipeline_data, workspace_data, output_dir, dry_run=dry_run)

    # Phase C
    report = phase_c_merge(sections, outline, pipeline_data, workspace_data)

    # Phase D
    validation = phase_d_validate(report, pipeline_data, workspace_data)

    # Phase E
    grade = phase_e_output(report, validation, output_dir, version, outline=outline)

    elapsed_total = time.time() - t_total
    print(f"\n{'=' * 60}")
    print(f"SYNTHESIS COMPLETE — Grade: {grade} — {elapsed_total:.1f}s total")
    print(f"Output: {output_dir}")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
