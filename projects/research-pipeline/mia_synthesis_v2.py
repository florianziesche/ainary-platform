#!/usr/bin/env python3
"""MIA Synthesis v2 — Outline-First Report Generation.

Replaces Phase 3 (Synthesis) of mia_pipeline.py.
Standalone CLI or importable module. No external dependencies.

Usage:
    python3 mia_synthesis_v2.py /path/to/pipeline-output-dir/
    python3 mia_synthesis_v2.py /path/to/pipeline-output-dir/ --version v4
    python3 mia_synthesis_v2.py /path/to/pipeline-output-dir/ --dry-run
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import re
import subprocess
import time
from datetime import datetime
from pathlib import Path
from typing import Any, Optional

# ============================================================
# CONSTANTS
# ============================================================

ADMIRALTY_MAP: dict[str, float] = {
    "A1": 0.95, "A2": 0.85, "B1": 0.80, "B2": 0.70, "B3": 0.55,
    "C3": 0.40, "C4": 0.30, "D4": 0.20, "D5": 0.15, "E2": 0.10,
}

EIJA_CONSISTENCY: dict[str, float] = {"E": 0.85, "I": 0.60, "J": 0.30, "A": 0.40}
EIJA_WEIGHT: dict[str, float] = {"E": 1.0, "I": 0.7, "J": 0.3, "A": 0.0}

BANNED_WORDS: list[str] = [
    "landscape", "tapestry", "delve", "synergy", "cutting-edge",
    "game-changer", "It's worth noting", "In today's world",
]

WORKSPACE = Path(os.path.expanduser("~/.openclaw/workspace"))

# ============================================================
# SYSTEM PROMPTS
# ============================================================

OUTLINE_SYSTEM = """You are MIA, a research intelligence analyst. You produce structured research outlines.

## 3 Laws of MIA Research
1. EVERY claim has a source. No source = not a claim.
2. EVERY source has an Admiralty rating. No rating = C3 (unknown reliability).
3. The Beipackzettel is MANDATORY — it's the research insert that tells the reader what they're getting.

## E/I/J/A Classification
- [E] Empirical: Verifiable data, statistics, published research (DOI, URL, named study)
- [I] Informed: Expert analysis, reasoned inference from multiple sources
- [J] Judgment: Opinion, prediction, single-source claim
- [A] Assumption: Unstated premise made explicit

## 3-Signal Confidence Formula
claim_confidence = 0.5 × source_signal + 0.3 × consistency_signal + 0.2 × structural_signal

## Admiralty Rating Table
A1=0.95 A2=0.85 B2=0.70 C3=0.40 D4=0.20 E2=0.10

## Beipackzettel Schema (7 fields)
1. confidence: float 0-1
2. risk_level: HIGH/MEDIUM/LOW
3. sources: list of source IDs used
4. uncertainties: list of things we're not sure about
5. risks: list of risks to the decision
6. not_checked: list of things we didn't verify
7. eija: {E: count, I: count, J: count, A: count}

## Example Claim
CL-01 [E] "73% of enterprise AI deployments fail to reach production (Gartner 2024, A2)" → [S3]

## Your Task
Given the full research context, produce a JSON outline for a 7-section report.
Output ONLY valid JSON (you may wrap in ```json ... ```).
The JSON must match the schema described in the user prompt."""

SECTION_SYSTEM = """You are MIA, writing ONE section of a research report.

## Style Rules
- Write for a decision-maker: direct, evidence-dense, no filler
- BANNED words/phrases: landscape, tapestry, delve, synergy, cutting-edge, game-changer, "It's worth noting", "In today's world"
- E/I/J/A labels appear ONLY in the Claim Ledger (appendix). Prose flows narratively.
- End each section with: "**For the decision maker:** [one actionable sentence]"
- Include Section Confidence % at the end: "Section Confidence: X%"
- Reference claims as CL-## and sources as [S#] inline
- Be specific. Numbers > adjectives. Evidence > opinion."""


# ============================================================
# API CALL
# ============================================================

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
            print(f"  [OPUS] Retry after 30s...")
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
            print(f"  [OPUS] Error (attempt {attempt+1}): {e}")
            if attempt == 0 and retry:
                continue
            raise

    return ""  # unreachable


def extract_json(text: str) -> Any:
    """Extract JSON from text, handling ```json...``` wrapping."""
    # Try direct parse first
    text = text.strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass

    # Try ```json ... ``` block
    m = re.search(r"```(?:json)?\s*\n?(.*?)```", text, re.DOTALL)
    if m:
        try:
            return json.loads(m.group(1).strip())
        except json.JSONDecodeError:
            pass

    raise ValueError(f"Could not parse JSON from response (first 200 chars): {text[:200]}")


# ============================================================
# CONTEXT LOADING
# ============================================================

def _read_safe(path: Path, max_chars: int = 50000) -> str:
    """Read file if exists, return empty string otherwise."""
    if path.exists():
        return path.read_text()[:max_chars]
    return ""


def load_context(output_dir: Path) -> dict[str, Any]:
    """Load all research context from pipeline output dir + workspace."""
    ctx: dict[str, Any] = {}

    # From output dir
    brief_path = output_dir / "research-brief.json"
    if brief_path.exists():
        ctx["brief"] = json.loads(brief_path.read_text())
    else:
        ctx["brief"] = {}

    # Sub-reports
    sub_reports: list[str] = []
    for sq_dir in sorted(output_dir.glob("sq-*")):
        report = sq_dir / "report.md"
        if report.exists():
            sub_reports.append(f"--- Sub-Report: {sq_dir.name} ---\n{report.read_text()[:30000]}")
    ctx["sub_reports"] = "\n\n".join(sub_reports) if sub_reports else "(none)"

    # Claims, contradictions, reviews
    for name in ("all-claims.json", "contradictions.json", "sub-reviews.json"):
        p = output_dir / name
        ctx[name.replace(".json", "").replace("-", "_")] = _read_safe(p, 30000)

    # Workspace resources
    rb = WORKSPACE / "research-base"
    ctx["crts"] = _read_safe(rb / "compounding-research-truths.json", 20000)
    ctx["corrections"] = _read_safe(rb / "corrections.json", 10000)
    ctx["reference_library"] = _read_safe(rb / "reference-library.json", 20000)

    best_report = WORKSPACE / "research/ar-020-agent-trust-calibration/ar-020-v5-state-of-agent-trust.md"
    ctx["best_report"] = _read_safe(best_report, 30000)

    # Vault index (optional)
    vault_dir = WORKSPACE / "vault-index"
    if vault_dir.exists():
        vault_files = list(vault_dir.glob("*.md"))[:5]
        ctx["vault"] = "\n".join(_read_safe(f, 5000) for f in vault_files)
    else:
        ctx["vault"] = ""

    return ctx


# ============================================================
# PHASE A: OUTLINE
# ============================================================

def build_outline_prompt(ctx: dict[str, Any]) -> str:
    """Build the user prompt for outline generation."""
    brief = ctx.get("brief", {})
    real_q = brief.get("real_question", brief.get("question", "(unknown)"))
    why_now = brief.get("why_now", "")
    blindspots = brief.get("blindspots", [])
    if isinstance(blindspots, list):
        blindspots = ", ".join(str(b) for b in blindspots)

    prompt = f"""# Research Synthesis — Generate Outline

## Real Question
{real_q}

## Why Now
{why_now}

## Blindspots
{blindspots}

## Sub-Reports
{ctx.get('sub_reports', '(none)')}

## Claims
{ctx.get('all_claims', '(none)')}

## Contradictions
{ctx.get('contradictions', '(none)')}

## Validation Results
{ctx.get('sub_reviews', '(none)')}

## Compounding Research Truths (CRTs)
{ctx.get('crts', '(none)')[:10000]}

## Corrections
{ctx.get('corrections', '(none)')[:5000]}

## Reference Library
{ctx.get('reference_library', '(none)')[:10000]}

## Best Report (Style Reference)
{ctx.get('best_report', '(none)')[:15000]}

---

Generate a JSON outline for a 7-section research report. The sections MUST be:
1. beipackzettel — Research insert (confidence, sources, risks, uncertainties)
2. executive_summary — Key findings + recommendation
3. framework — Analytical framework used
4. key_findings — Evidence-backed findings with claim IDs
5. recommendations — Actionable recommendations
6. risks — Risks and uncertainties
7. appendix — Claim ledger + source log

Output format (JSON only):
{{
  "thesis": "one-sentence thesis",
  "framework": {{"name": "...", "layers": [{{"id": 1, "name": "...", "description": "..."}}]}},
  "sections": [
    {{"id": 1, "type": "beipackzettel", "claims": ["CL-01"], "sources": ["S1"], "guidance": "..."}},
    {{"id": 2, "type": "executive_summary", "key_points": ["..."], "guidance": "..."}},
    {{"id": 3, "type": "framework", "guidance": "..."}},
    {{"id": 4, "type": "key_findings", "findings": [{{"id": "F1", "claim": "CL-01", "sources": ["S1"]}}], "guidance": "..."}},
    {{"id": 5, "type": "recommendations", "guidance": "..."}},
    {{"id": 6, "type": "risks", "guidance": "..."}},
    {{"id": 7, "type": "appendix", "claim_ledger": [{{"id": "CL-01", "text": "...", "label": "E", "admiralty": "A2", "sources": ["S1"]}}], "source_log": [{{"id": "S1", "title": "...", "url": "...", "admiralty": "A2"}}], "guidance": "..."}}
  ],
  "claim_assignments": {{"CL-01": [4, 7]}},
  "source_assignments": {{"S1": [2, 4, 7]}}
}}

Output ONLY the JSON."""
    return prompt


def phase_a_outline(ctx: dict[str, Any], dry_run: bool = False) -> dict[str, Any]:
    """Phase A: Generate report outline via single Opus call."""
    print("[PHASE A] Generating outline...")
    start = time.time()

    prompt = build_outline_prompt(ctx)
    print(f"[PHASE A] Outline prompt: {len(prompt)} chars")

    if dry_run:
        print("[PHASE A] DRY RUN — prompt built, no API call")
        print(f"[PHASE A] Prompt preview (first 2000 chars):\n{prompt[:2000]}")
        return {"thesis": "DRY_RUN", "sections": [], "claim_assignments": {}, "source_assignments": {}}

    response = call_opus(prompt, system=OUTLINE_SYSTEM, max_tokens=2000)
    outline = extract_json(response)

    elapsed = time.time() - start
    print(f"[PHASE A] Outline generated in {elapsed:.0f}s — {len(outline.get('sections', []))} sections")
    return outline


# ============================================================
# PHASE B: SECTIONS
# ============================================================

def build_section_prompt(
    ctx: dict[str, Any],
    outline: dict[str, Any],
    section: dict[str, Any],
    prev_section_tail: str = "",
) -> str:
    """Build prompt for writing a single section."""
    brief = ctx.get("brief", {})
    real_q = brief.get("real_question", brief.get("question", "(unknown)"))

    prev_context = ""
    if prev_section_tail:
        prev_context = f"\n## Previous Section (last paragraph, for transition)\n{prev_section_tail}\n"

    return f"""# Write Section {section['id']}: {section['type']}

## Real Question
{real_q}

## Full Outline
```json
{json.dumps(outline, indent=2)[:8000]}
```

## Sub-Reports
{ctx.get('sub_reports', '(none)')[:20000]}

## Claims
{ctx.get('all_claims', '(none)')[:15000]}

## Guidance for this section
{section.get('guidance', '(none)')}
{prev_context}
---

Write ONLY the markdown content for Section {section['id']}: {section['type']}.
Start with ## heading. End with "**For the decision maker:**" and "Section Confidence: X%".
For the appendix: include full Claim Ledger with [E]/[I]/[J]/[A] labels and Source Log."""


def phase_b_sections(
    ctx: dict[str, Any],
    outline: dict[str, Any],
    output_dir: Path,
    dry_run: bool = False,
) -> list[tuple[int, str, str]]:
    """Phase B: Write each section sequentially. Returns [(id, type, content)]."""
    print("[PHASE B] Writing sections...")
    start = time.time()
    sections = outline.get("sections", [])
    results: list[tuple[int, str, str]] = []
    prev_tail = ""

    for sec in sections:
        sec_id = sec["id"]
        sec_type = sec["type"]
        sec_start = time.time()
        print(f"[PHASE B] Section {sec_id}: {sec_type}")

        if dry_run:
            content = f"## {sec_type.replace('_', ' ').title()}\n\n(dry run — no content)\n"
            results.append((sec_id, sec_type, content))
            continue

        prompt = build_section_prompt(ctx, outline, sec, prev_tail)

        try:
            content = call_opus(prompt, system=SECTION_SYSTEM, max_tokens=4096)
        except Exception as e:
            print(f"[PHASE B] WARNING: Section {sec_id} failed: {e}")
            content = f"## {sec_type.replace('_', ' ').title()}\n\n(Generation failed: {e})\n"

        # Save individual section
        sec_file = output_dir / f"section-{sec_id}-{sec_type}.md"
        sec_file.write_text(content)

        # Keep last paragraph for transition
        paragraphs = [p.strip() for p in content.split("\n\n") if p.strip()]
        prev_tail = paragraphs[-1] if paragraphs else ""

        sec_elapsed = time.time() - sec_start
        print(f"[PHASE B] Section {sec_id} done in {sec_elapsed:.0f}s ({len(content)} chars)")
        results.append((sec_id, sec_type, content))

    elapsed = time.time() - start
    print(f"[PHASE B] All {len(results)} sections written in {elapsed:.0f}s")
    return results


# ============================================================
# PHASE C: MERGE + VALIDATE
# ============================================================

def _count_eija(text: str) -> dict[str, int]:
    """Count [E], [I], [J], [A] occurrences."""
    return {
        "E": len(re.findall(r"\[E\]", text)),
        "I": len(re.findall(r"\[I\]", text)),
        "J": len(re.findall(r"\[J\]", text)),
        "A": len(re.findall(r"\[A\]", text)),
    }


def _compute_claim_confidence(
    claim_text: str, label: str, admiralty: str
) -> float:
    """3-Signal confidence for a single claim."""
    source_signal = ADMIRALTY_MAP.get(admiralty, 0.40)
    consistency = EIJA_CONSISTENCY.get(label, 0.40)

    structural = 0.0
    if "doi" in claim_text.lower() or "10." in claim_text:
        structural += 0.30
    if "http" in claim_text:
        structural += 0.15
    if "%" in claim_text:
        structural += 0.10
    if re.search(r"20[12]\d", claim_text):
        structural += 0.05
    if re.search(r"\[S\d+\]", claim_text):
        structural += 0.10
    structural = min(structural, 0.50)

    return 0.5 * source_signal + 0.3 * consistency + 0.2 * structural


def _extract_claims_from_report(text: str) -> list[dict[str, str]]:
    """Extract claims from the Claim Ledger in the report text."""
    claims: list[dict[str, str]] = []
    # Pattern: CL-## [E/I/J/A] "text" (source, admiralty)
    for m in re.finditer(
        r"(CL-\d+)\s*\[([EIJA])\]\s*\"?(.*?)\"?\s*(?:\(([^)]*)\))?(?:\s*->?\s*\[?(S\d+(?:,\s*S\d+)*)\]?)?",  # noqa
        text,
    ):
        claim_id = m.group(1)
        label = m.group(2)
        claim_text = m.group(3)
        parens = m.group(4) or ""
        # Try to extract admiralty from parens
        adm_match = re.search(r"([A-E][1-5])", parens)
        admiralty = adm_match.group(1) if adm_match else "C3"
        claims.append({
            "id": claim_id,
            "label": label,
            "text": claim_text,
            "admiralty": admiralty,
        })
    return claims


def _find_source_refs(text: str, section_type: str = "") -> set[str]:
    """Find all [S#] references in text."""
    return set(re.findall(r"\[S(\d+)\]", text))


def phase_c_validate(
    sections: list[tuple[int, str, str]],
    outline: dict[str, Any],
    output_dir: Path,
    version: str = "v4",
) -> dict[str, Any]:
    """Phase C: Merge sections, validate, produce outputs. 0 LLM calls."""
    print("[PHASE C] Merging and validating...")
    start = time.time()
    warnings: list[str] = []

    # Step 1: Merge
    merged = "\n\n".join(content for _, _, content in sections)

    # Step 2: E/I/J/A count
    eija = _count_eija(merged)
    total_eija = sum(eija.values()) or 1
    e_pct = (eija["E"] / total_eija) * 100
    j_pct = (eija["J"] / total_eija) * 100
    print(f"[PHASE C] E/I/J/A: E={eija['E']}({e_pct:.0f}%) I={eija['I']} J={eija['J']}({j_pct:.0f}%) A={eija['A']}")

    # Step 3: Claim confidence
    claims = _extract_claims_from_report(merged)
    claim_confs: list[tuple[str, float, str]] = []
    weighted_sum = 0.0
    weight_sum = 0.0

    for cl in claims:
        conf = _compute_claim_confidence(cl["text"], cl["label"], cl["admiralty"])
        claim_confs.append((cl["id"], conf, cl["label"]))
        w = EIJA_WEIGHT.get(cl["label"], 0.5)
        weighted_sum += conf * w
        weight_sum += w

    report_confidence = weighted_sum / weight_sum if weight_sum > 0 else 0.50
    print(f"[PHASE C] Report confidence: {report_confidence:.2f} ({len(claims)} claims)")

    # Step 4: Beipackzettel correction
    risk_level = "HIGH" if report_confidence < 0.60 else "MEDIUM" if report_confidence < 0.80 else "LOW"

    # Replace confidence in beipackzettel section
    conf_pattern = re.compile(r"(?i)(confidence[:\s]*)\d+\.?\d*%?")
    eija_pattern = re.compile(r"(?i)(E[:/]\s*)\d+.*?(I[:/]\s*)\d+.*?(J[:/]\s*)\d+.*?(A[:/]\s*)\d+")
    risk_pattern = re.compile(r"(?i)(risk[_ ]level[:\s]*)(HIGH|MEDIUM|LOW)")

    merged = conf_pattern.sub(
        lambda m: f"{m.group(1)}{report_confidence:.0%}", merged, count=2
    )
    merged = risk_pattern.sub(
        lambda m: f"{m.group(1)}{risk_level}", merged, count=2
    )

    # Step 5: Source orphan check
    # Split report: everything before appendix = prose, appendix = source log
    appendix_idx = merged.lower().find("## appendix")
    if appendix_idx == -1:
        appendix_idx = merged.lower().find("## source log")
    if appendix_idx == -1:
        appendix_idx = len(merged)

    prose_text = merged[:appendix_idx]
    appendix_text = merged[appendix_idx:]

    prose_refs = _find_source_refs(prose_text)
    # Source log refs: look for S# definitions in appendix
    log_refs = set(re.findall(r"\*?\*?\[?S(\d+)\]?\*?\*?\s*[-–:]", appendix_text))
    if not log_refs:
        log_refs = _find_source_refs(appendix_text)

    orphan_refs = prose_refs - log_refs
    orphan_sources = log_refs - prose_refs

    if orphan_refs:
        w = f"Orphan references (in text, not in source log): S{', S'.join(sorted(orphan_refs))}"
        warnings.append(w)
        print(f"[PHASE C] WARNING: {w}")
    if orphan_sources:
        w = f"Orphan sources (in log, not in text): S{', S'.join(sorted(orphan_sources))}"
        warnings.append(w)
        print(f"[PHASE C] WARNING: {w}")

    # Step 6: Cross-reference check
    claim_assignments = outline.get("claim_assignments", {})
    source_assignments = outline.get("source_assignments", {})

    for claim_id, section_ids in claim_assignments.items():
        for sid in section_ids:
            sec_content = next((c for i, t, c in sections if i == sid), "")
            if claim_id not in sec_content:
                w = f"Missing claim {claim_id} in section {sid}"
                warnings.append(w)

    for source_id, section_ids in source_assignments.items():
        for sid in section_ids:
            sec_content = next((c for i, t, c in sections if i == sid), "")
            if f"[{source_id}]" not in sec_content and source_id not in sec_content:
                w = f"Missing source {source_id} in section {sid}"
                warnings.append(w)

    # Step 7: Grade
    blocks_present = sum(1 for _, _, c in sections if len(c.strip()) > 50)
    if (blocks_present == 7 and e_pct > 50 and j_pct < 20
            and len(orphan_refs) == 0 and len(orphan_sources) == 0
            and len(claims) >= 12):
        grade = "A+++"
    elif blocks_present == 7 and e_pct > 50 and j_pct < 20:
        grade = "A++"
    elif blocks_present >= 5 and e_pct > 40:
        grade = "A+"
    else:
        grade = "B"
    print(f"[PHASE C] Grade: {grade} (blocks={blocks_present}, E%={e_pct:.0f}, J%={j_pct:.0f})")

    # Step 8: Outputs
    report_path = output_dir / f"final-report-{version}.md"
    report_path.write_text(merged)
    print(f"[PHASE C] Wrote {report_path}")

    # Collect source list and uncertainties from outline
    outline_sources = []
    uncertainties = []
    risks = []
    not_checked = []

    for sec in outline.get("sections", []):
        if sec.get("type") == "appendix":
            outline_sources = [s.get("id", "") for s in sec.get("source_log", [])]
        if sec.get("type") == "risks":
            risks.append(sec.get("guidance", ""))
        if sec.get("type") == "beipackzettel":
            uncertainties.append(sec.get("guidance", ""))

    beipackzettel = {
        "confidence": round(report_confidence, 2),
        "risk_level": risk_level,
        "sources": outline_sources or [f"S{s}" for s in sorted(prose_refs | log_refs)],
        "uncertainties": uncertainties,
        "risks": risks,
        "not_checked": not_checked,
        "eija": eija,
    }

    bp_path = output_dir / "beipackzettel.json"
    bp_path.write_text(json.dumps(beipackzettel, indent=2, ensure_ascii=False))
    print(f"[PHASE C] Wrote {bp_path}")

    validation = {
        "timestamp": datetime.now().isoformat(),
        "grade": grade,
        "report_confidence": round(report_confidence, 2),
        "risk_level": risk_level,
        "eija": eija,
        "e_pct": round(e_pct, 1),
        "j_pct": round(j_pct, 1),
        "claims_found": len(claims),
        "claim_confidences": [
            {"id": cid, "confidence": round(c, 2), "label": lbl}
            for cid, c, lbl in claim_confs
        ],
        "blocks_present": blocks_present,
        "orphan_refs": sorted(orphan_refs),
        "orphan_sources": sorted(orphan_sources),
        "warnings": warnings,
    }

    val_path = output_dir / "validation-report.json"
    val_path.write_text(json.dumps(validation, indent=2, ensure_ascii=False))
    print(f"[PHASE C] Wrote {val_path}")

    elapsed = time.time() - start
    print(f"[PHASE C] Validation complete in {elapsed:.1f}s")
    return validation


# ============================================================
# MAIN PIPELINE
# ============================================================

def run_synthesis(
    output_dir: Path,
    version: str = "v4",
    dry_run: bool = False,
) -> dict[str, Any]:
    """Run the full 3-phase synthesis pipeline."""
    print(f"{'='*60}")
    print(f"MIA Synthesis v2 — Outline-First")
    print(f"Output dir: {output_dir}")
    print(f"Version: {version}")
    print(f"Dry run: {dry_run}")
    print(f"{'='*60}")

    total_start = time.time()

    # Load context
    ctx = load_context(output_dir)
    print(f"Context loaded: brief={bool(ctx.get('brief'))}, sub_reports={len(ctx.get('sub_reports',''))}>0")

    # Phase A
    outline = phase_a_outline(ctx, dry_run=dry_run)

    # Save outline
    outline_path = output_dir / "outline.json"
    outline_path.write_text(json.dumps(outline, indent=2, ensure_ascii=False))

    # Phase B
    section_results = phase_b_sections(ctx, outline, output_dir, dry_run=dry_run)

    # Phase C
    validation = phase_c_validate(section_results, outline, output_dir, version=version)

    total_elapsed = time.time() - total_start
    print(f"\n{'='*60}")
    print(f"DONE in {total_elapsed:.0f}s — Grade: {validation['grade']} — Confidence: {validation['report_confidence']}")
    print(f"{'='*60}")

    return validation


# ============================================================
# CLI
# ============================================================

def main() -> None:
    """CLI entry point."""
    parser = argparse.ArgumentParser(description="MIA Synthesis v2 — Outline-First Report Generation")
    parser.add_argument("output_dir", type=Path, help="Pipeline output directory")
    parser.add_argument("--version", default="v4", help="Report version tag (default: v4)")
    parser.add_argument("--dry-run", action="store_true", help="Print outline prompt without API calls")
    args = parser.parse_args()

    if not args.output_dir.exists():
        print(f"ERROR: Directory not found: {args.output_dir}")
        raise SystemExit(1)

    run_synthesis(args.output_dir, version=args.version, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
