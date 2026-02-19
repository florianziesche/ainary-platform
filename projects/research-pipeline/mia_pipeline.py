#!/usr/bin/env python3
"""
MIA Pipeline: Opus as brain, GPT-4o as researcher.

Architecture:
1. MIA (Opus) frames the research brief + sub-questions
2. GPT-4o researches EACH sub-question independently (RAG + Brave + Producer)
3. MIA (Opus) receives ALL sub-reports → synthesizes final report + assets

Hallucination is isolated per sub-question, not compounded across agents.

Usage:
    python3 mia_pipeline.py --topic "Trust Calibration for AI Agents"
    python3 mia_pipeline.py --topic "EU AI Act Compliance" --sub-questions 5
"""

import json
import os
import re
import sys
import time
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict, List

sys.path.insert(0, str(Path(__file__).parent))
from opus_synthesis import (
    load_crts, load_corrections, load_reference_library,
    load_decisions, load_papers, load_vault_knowledge,
    load_best_report, call_opus, WORKSPACE, RESEARCH_BASE
)
from research_factory import (
    llm_call, init_client, MODELS,
    web_enrich_dossier, run_prepare,
    make_beipackzettel, beipackzettel_to_json,
    _load_reference_library,
)


# ============================================================
# PHASE 1: MIA FRAMES (Opus)
# ============================================================

MIA_FRAMER_PROMPT = """You are MIA, a research strategist. Your job: decompose a complex topic into researchable sub-questions.

## TOPIC
{topic}

## DECISION CONTEXT
{decision}

## WHAT YOU KNOW (proprietary — verified truths)
{crts}

## WHAT WE GOT WRONG BEFORE (learn from these)
{corrections}

## KEY DECISIONS WE'VE MADE
{decisions}

## TASK
1. State THE REAL QUESTION (not the obvious one — the question behind the question)
2. Explain WHY NOW (what changed)
3. Decompose into {n_sub} SUB-QUESTIONS that are:
   - MECE (mutually exclusive, collectively exhaustive)
   - Each independently researchable
   - Each answerable with available evidence
   - Ordered by importance to the decision

4. For EACH sub-question, specify:
   - The question (1 sentence)
   - Why it matters for the decision (1 sentence)
   - What EVIDENCE would answer it (be specific: "paper showing X", "data on Y")
   - Search queries for Brave (2-3 specific queries)

## BLINDSPOT ANALYSIS
After framing, challenge your own thinking. Find 3 questions nobody is asking:
- What would a CRITIC ask?
- What would someone from a DIFFERENT FIELD ask?
- What ASSUMPTION could be wrong?
- What SECOND-ORDER EFFECT are we ignoring?
- What worked in ANALOGOUS SITUATIONS that we're not considering?
Be specific. "We might be missing something" is NOT a blindspot.

## OUTPUT FORMAT (JSON)
```json
{{
  "real_question": "...",
  "why_now": "...",
  "sub_questions": [
    {{
      "id": "SQ-1",
      "question": "...",
      "why_it_matters": "...",
      "evidence_needed": "...",
      "search_queries": ["...", "..."]
    }}
  ],
  "blindspots": [
    {{
      "question": "...",
      "why_its_a_blindspot": "...",
      "confidence": 75,
      "reasoning": "...",
      "recommendation": "YES — priority 2 / MAYBE / NO"
    }}
  ]
}}
```

Output ONLY the JSON block.
"""


# ============================================================
# PHASE 2: GPT-4o RESEARCHES (per sub-question)
# ============================================================

SUB_RESEARCH_PROMPT = """You are a research analyst answering ONE specific question with evidence.

## YOUR QUESTION
{question}

## WHY IT MATTERS
{why_it_matters}

## EVIDENCE NEEDED
{evidence_needed}

## WEB SEARCH RESULTS (from Brave — real, current)
{web_results}

## VERIFIED REFERENCES (cite as [S#])
{references}

## RULES
1. ONLY use evidence from the web results and references above
2. Cite EVERY claim with [S#] or source URL
3. If no evidence found: say "No evidence found" — do NOT invent
4. Label each finding:
   [E] Evidenced — directly from source with citation
   [I] Interpreted — inferred from sources, explain logic
   [J] Judged — your assessment, no direct source
5. End with "SO WHAT: ..." (1-2 sentences for the decision maker)
6. Max 800 words. Be dense, not verbose.

## OUTPUT STRUCTURE
### Answer to: {question}

**Key Findings:**
- Finding 1 [E/I/J] [S#]
- Finding 2 ...

**Evidence Quality:**
- Strongest source: ...
- Weakest point: ...
- What's missing: ...

**So What:** ...

**Claims (for Claim Ledger):**
- Claim 1 | [S#] | E/I/J | Admiralty | Confidence
- Claim 2 | ...
"""


# ============================================================
# PHASE 3: MIA SYNTHESIZES (Opus — full context)
# ============================================================

MIA_SYNTHESIS_PROMPT = """You are MIA, synthesizing multiple research sub-reports into one executive report.

## THE REAL QUESTION
{real_question}

## WHY NOW
{why_now}

## SUB-REPORTS (each independently researched — DO NOT add claims not in these reports)
{sub_reports}

## PROPRIETARY KNOWLEDGE
### CRTs (verified truths)
{crts}

### Corrections (past mistakes)
{corrections}

### Best Previous Report (improve on this)
{best_report}

### Vault Knowledge
{vault}

## YOUR TASK
Synthesize the sub-reports into ONE report. Rules:

1. **NO NEW FACTS** — only combine what's in the sub-reports + CRTs. If it's not sourced, mark [J].
2. **DESIGN A CUSTOM FRAMEWORK** — one original model that shows relationships across sub-questions.
   Name it. Make it drawable. Map findings to it.
3. **E/I/J/A LABELS** — in the Claim Ledger (appendix). Prose must flow narratively.
4. **NARRATIVE STYLE** — like V3 (engaging opener, case studies inline, section confidence).
   Start with something an expert DOESN'T already know.
5. **"SO WHAT" per section** — every section ends with "For the decision maker: ..."
6. **RECOMMENDATIONS** — phased (Week 1 / Month 1 / Quarter 1). Specific.
   Include "Do Not Deploy If" (5 conditions). Include "If Wrong:" for each recommendation.
7. **SELF-CALIBRATING** — apply the trust methods this report describes to itself.

## STRUCTURE
1. Beipackzettel (confidence, risk level, E/I/J/A distribution, sources, uncertainties, risks)
2. Executive Summary (SCR, 3 paragraphs + "If you read nothing else" bullets)
3. Custom Framework (describe so reader can draw it)
4. Key Findings (5-7, narrative, case studies woven in, section confidence %)
5. Recommendations (Decision Matrix + Phased Plan + "Do Not Deploy If")
6. Risks & "What Would Change This"
7. Appendix: Claim Ledger (12 claims, E/I/J/A, [S#], confidence) + Source Log + Contradictions

## QUALITY CHECK (verify before output)
- [ ] Opener: would an expert learn something new?
- [ ] Every section has "So What"
- [ ] Custom Framework is original (not from any source)
- [ ] >50% E labels, <20% J labels
- [ ] Phased plan: reader can start Monday
- [ ] No claims without [S#] or [J] label
- [ ] Self-calibration applied

NO: landscape, tapestry, delve, synergy, cutting-edge, game-changer
Target: 5000-8000 words.
"""


# ============================================================
# PHASE 4: ASSET SYNTHESIS (GPT-4o — fast)
# ============================================================

ASSET_SYNTHESIS_PROMPT = """You are the Asset Builder. Convert this research report into reusable assets.

## REPORT
{report}

## ASSET RULES
- NO NEW FACTS beyond the report
- Every asset: ID (AB-[slug]-[TYPE]-[0001]), classification (Evidenced/Derived/Operational), confidence, sources
- Dedupe: one canonical asset + aliases, not duplicates
- Carry contradictions forward as "Known Conflicts"

## OUTPUT
1. Asset Index (counts + coverage map to Key Findings)
2. Atomic Notes (10-15): ID, Title, "This answers:", Content, Classification, Confidence, Sources, Tags
3. Playbooks (2-3): Trigger, Goal, Inputs, Steps, Outputs, Failure modes, Mitigations, Acceptance criteria
4. Templates (1-2): When to use, Copy/paste block, Pitfalls
5. RAG JSON (array of asset/entity/relation objects)
"""


# ============================================================
# PIPELINE
# ============================================================

def run_mia_pipeline(
    topic: str,
    decision: str = "",
    n_sub_questions: int = 5,
    output_dir: Optional[Path] = None,
) -> Dict:
    """Run the MIA Pipeline: Opus frames, GPT-4o researches, Opus synthesizes."""

    if output_dir is None:
        slug = re.sub(r'[^a-z0-9]+', '-', topic.lower()).strip('-')
        ts = datetime.now().strftime("%Y%m%d-%H%M")
        output_dir = WORKSPACE / "research" / "mia-pipeline" / f"{slug}-{ts}"
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Load knowledge
    crts = load_crts()
    corrections = load_corrections()
    references = load_reference_library()
    decisions = load_decisions(max_chars=3000)
    papers = load_papers(max_chars=50000)
    vault = load_vault_knowledge(
        topic.lower().split() + ["calibration", "trust", "agent"],
        max_chars=100000
    )
    best_report = load_best_report()

    print(f"\n{'#'*60}")
    print(f"# MIA PIPELINE: {topic}")
    print(f"# Sub-Questions: {n_sub_questions}")
    print(f"# Output: {output_dir}")
    print(f"{'#'*60}")

    # ── PHASE 1: MIA FRAMES ──────────────────────────────────

    print(f"\n[PHASE 1] MIA frames the research...")
    framer_prompt = MIA_FRAMER_PROMPT.format(
        topic=topic,
        decision=decision or f"Should we invest in {topic}?",
        crts=crts,
        corrections=corrections,
        decisions=decisions,
        n_sub=n_sub_questions,
    )
    (output_dir / "phase1-framer-prompt.md").write_text(framer_prompt)

    framer_result = call_opus(framer_prompt, max_tokens=4000)
    (output_dir / "phase1-framer-output.md").write_text(framer_result)

    # Parse sub-questions
    try:
        json_match = re.search(r'\{.*\}', framer_result, re.DOTALL)
        brief = json.loads(json_match.group())
    except Exception as e:
        print(f"  [ERROR] Failed to parse framer output: {e}")
        brief = {"real_question": topic, "why_now": "Unknown", "sub_questions": []}

    sub_questions = brief.get("sub_questions", [])
    blindspots = brief.get("blindspots", [])

    print(f"  Real question: {brief.get('real_question', '?')}")
    print(f"  Sub-questions: {len(sub_questions)}")
    for sq in sub_questions:
        print(f"    {sq.get('id', '?')}: {sq.get('question', '?')[:70]}")

    if blindspots:
        print(f"  Blindspots: {len(blindspots)}")
        for bs in blindspots:
            rec = bs.get('recommendation', '?')
            conf = bs.get('confidence', '?')
            print(f"    [{conf}% {rec}] {bs.get('question', '?')[:70]}")
        (output_dir / "blindspots.json").write_text(json.dumps(blindspots, indent=2))

    # Checkpoint 1: Display for Florian
    print(f"\n{'='*60}")
    print(f"  🔴 CHECKPOINT 1: Review before continuing")
    print(f"  Real Question: {brief.get('real_question', '?')}")
    print(f"  {len(sub_questions)} Sub-Questions + {len(blindspots)} Blindspots")
    print(f"  Pipeline will continue automatically.")
    print(f"  To intervene: edit research-brief.json and re-run.")
    print(f"{'='*60}")

    # ── PHASE 2: GPT-4o RESEARCHES EACH SUB-QUESTION ─────────

    print(f"\n[PHASE 2] Sonnet researches {len(sub_questions)} sub-questions (parallel)...")
    client = init_client()
    sub_reports = []

    # Parallel research: launch all Brave searches first, then all LLM calls
    import concurrent.futures

    def research_sub_question(i_sq):
        i, sq = i_sq
        sq_dir = output_dir / f"sq-{i+1:02d}"
        sq_dir.mkdir(exist_ok=True)

        # Brave search
        search_queries = sq.get("search_queries", [sq.get("question", topic)])
        web_results = ""
        try:
            from research_factory import web_search_brave, _brave_fetch_and_store
            web_results = web_search_brave(search_queries, max_results=5)
            if web_results:
                stored = 0
                for line in web_results.split("\n"):
                    m = re.search(r'\(([^)]+)\)\s*$', line)
                    title_m = re.match(r'- (.+?):', line)
                    if m and title_m and stored < 3:
                        url = m.group(1)
                        title = title_m.group(1)
                        snippet = re.sub(r'\s*\([^)]+\)\s*$', '', line[len(title_m.group(0)):].strip())
                        _brave_fetch_and_store(url, title, snippet)
                        stored += 1
        except Exception as e:
            pass

        # Sonnet research
        sub_prompt = SUB_RESEARCH_PROMPT.format(
            question=sq.get("question", ""),
            why_it_matters=sq.get("why_it_matters", ""),
            evidence_needed=sq.get("evidence_needed", ""),
            web_results=web_results[:8000] if web_results else "No web results.",
            references=references,
        )
        (sq_dir / "prompt.md").write_text(sub_prompt)

        research_model = "claude-sonnet-4-20250514"
        sub_result = llm_call(client, research_model, sub_prompt, max_tokens=3000)
        (sq_dir / "report.md").write_text(sub_result)

        return {
            "id": sq.get("id", f"SQ-{i+1}"),
            "question": sq.get("question", ""),
            "report": sub_result,
            "chars": len(sub_result),
        }

    # Run all sub-questions in parallel (OAuth handles concurrent requests)
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        futures = list(executor.map(research_sub_question, enumerate(sub_questions)))
    
    sub_reports = futures
    for sr in sub_reports:
        print(f"  [{sr['id']}] {sr['question'][:50]}... → {sr['chars']:,} chars")

    # (old sequential loop removed — using parallel above)

    # ── PYTHON: Prepare validation data for Opus ─────────────

    print(f"\n[PYTHON] Pre-validating sub-reports before Opus synthesis...")

    # Python checks each sub-report: source count, E/I/J distribution, red flags
    sub_validations = []
    for sr in sub_reports:
        report_text = sr["report"]
        e_count = len(re.findall(r'\[E\]', report_text))
        i_count = len(re.findall(r'\[I\]', report_text))
        j_count = len(re.findall(r'\[J\]', report_text))
        source_refs = set(re.findall(r'\[S\d+\]', report_text))
        has_so_what = "so what" in report_text.lower()

        quality = "GOOD" if e_count >= j_count and len(source_refs) >= 2 else "WEAK"
        sub_validations.append({
            "id": sr["id"],
            "e": e_count, "i": i_count, "j": j_count,
            "sources": len(source_refs),
            "has_so_what": has_so_what,
            "quality": quality,
        })
        flag = " ⚠ WEAK" if quality == "WEAK" else ""
        print(f"  {sr['id']}: E:{e_count} I:{i_count} J:{j_count} | {len(source_refs)} sources{flag}")

    (output_dir / "sub-validations.json").write_text(json.dumps(sub_validations, indent=2))

    # Build validation summary for Opus
    validation_summary = "\n".join([
        f"- {v['id']}: {'GOOD' if v['quality'] == 'GOOD' else 'WEAK — fewer sources, more judgments'} "
        f"(E:{v['e']} I:{v['i']} J:{v['j']}, {v['sources']} sources)"
        for v in sub_validations
    ])

    # ── SONNET: Extract, Compare, Verify (no hallucination risk) ──

    print(f"\n[SONNET] Extracting claims from sub-reports...")

    CLAIM_EXTRACTOR_PROMPT = """Extract the 3 most important factual claims from this sub-report.

## SUB-REPORT
{report}

For each claim, output JSON:
- text: the claim (verbatim quote from the report)
- label: E, I, or J (as labeled in the report, or your assessment)
- source: [S#] if cited, or "none"
- admiralty: A1 (DOI cited) / B2 (URL cited) / C3 (source mentioned) / D4 (no source)

Output ONLY a JSON array. No explanation."""

    CONTRADICTION_PROMPT = """Compare these sub-reports and find contradictions.

## SUB-REPORTS
{reports}

Find claims that CONTRADICT each other across different sub-reports.
For each contradiction:
- claim_a: text + source (from which SQ)
- claim_b: text + source (from which SQ)  
- why_they_differ: 1 sentence
- which_is_stronger: A or B, and why
- impact: how this affects the main question

Output ONLY a JSON array. If no contradictions: output []"""

    REVIEWER_PROMPT = """Review this sub-report for quality. Be harsh.

## SUB-REPORT
{report}

Score 0-2 on:
1. Evidence discipline (are claims cited?)
2. Uncertainty explicit (does it say what it doesn't know?)
3. Actionability (is there a "So What"?)

Output JSON: {{"evidence": 0-2, "uncertainty": 0-2, "actionability": 0-2, "total": 0-6, "top_issue": "..."}}"""

    # 1. Extract claims from each sub-report (Sonnet, parallel)
    all_claims = []
    def extract_claims(sr):
        prompt = CLAIM_EXTRACTOR_PROMPT.format(report=sr["report"][:5000])
        result = llm_call(client, "claude-sonnet-4-20250514", prompt, max_tokens=1500)
        try:
            claims = json.loads(re.search(r'\[.*\]', result, re.DOTALL).group())
            return {"id": sr["id"], "claims": claims}
        except Exception:
            return {"id": sr["id"], "claims": []}

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        claims_results = list(executor.map(extract_claims, sub_reports))

    for cr in claims_results:
        all_claims.extend(cr["claims"])
        print(f"  {cr['id']}: {len(cr['claims'])} claims extracted")
    (output_dir / "all-claims.json").write_text(json.dumps(claims_results, indent=2))

    # 2. Find contradictions across sub-reports (Sonnet, 1 call)
    print(f"  Finding contradictions...")
    reports_combined = "\n\n".join([
        f"### {sr['id']}: {sr['question']}\n{sr['report'][:3000]}"
        for sr in sub_reports
    ])
    contra_result = llm_call(client, "claude-sonnet-4-20250514",
        CONTRADICTION_PROMPT.format(reports=reports_combined), max_tokens=2000)
    try:
        contradictions = json.loads(re.search(r'\[.*\]', contra_result, re.DOTALL).group())
    except Exception:
        contradictions = []
    print(f"  Contradictions found: {len(contradictions)}")
    (output_dir / "contradictions.json").write_text(json.dumps(contradictions, indent=2))

    # 3. Review each sub-report (Sonnet, parallel)
    print(f"  Reviewing sub-reports...")
    def review_sub(sr):
        prompt = REVIEWER_PROMPT.format(report=sr["report"][:5000])
        result = llm_call(client, "claude-sonnet-4-20250514", prompt, max_tokens=500)
        try:
            return json.loads(re.search(r'\{.*\}', result, re.DOTALL).group())
        except Exception:
            return {"total": 0, "top_issue": "parse error"}

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        reviews = list(executor.map(review_sub, sub_reports))

    for sr, rev in zip(sub_reports, reviews):
        print(f"  {sr['id']}: {rev.get('total', '?')}/6 — {rev.get('top_issue', '?')[:50]}")
    (output_dir / "sub-reviews.json").write_text(json.dumps(reviews, indent=2))

    # Build enriched validation for Opus
    validation_summary += "\n\n## EXTRACTED CLAIMS (verified by Sonnet)\n"
    for cr in claims_results:
        for cl in cr["claims"]:
            validation_summary += f"- [{cl.get('label','?')}] {cl.get('text','')[:80]} ({cl.get('source','none')}, {cl.get('admiralty','C3')})\n"

    if contradictions:
        validation_summary += "\n## CONTRADICTIONS FOUND\n"
        for c in contradictions:
            validation_summary += f"- {c.get('claim_a','')[:50]} VS {c.get('claim_b','')[:50]} — {c.get('why_they_differ','')}\n"

    validation_summary += "\n## SUB-REPORT REVIEWS\n"
    for sr, rev in zip(sub_reports, reviews):
        validation_summary += f"- {sr['id']}: {rev.get('total','?')}/6 | Issue: {rev.get('top_issue','?')[:60]}\n"

    # ── PHASE 3: MIA SYNTHESIZES (Opus — single session) ────

    print(f"\n[PHASE 3] MIA synthesizes {len(sub_reports)} sub-reports...")

    sub_reports_text = "\n\n".join([
        f"### {sr['id']}: {sr['question']}\n\n{sr['report']}"
        for sr in sub_reports
    ])

    synthesis_prompt = MIA_SYNTHESIS_PROMPT.format(
        real_question=brief.get("real_question", topic),
        why_now=brief.get("why_now", ""),
        sub_reports=sub_reports_text,
        crts=crts,
        corrections=corrections,
        best_report=best_report[:20000],
        vault=vault[:50000],
    )

    # Inject blindspots for documentation in final report
    blindspots_text = ""
    if blindspots:
        blindspots_text = "\n## DOCUMENTED BLINDSPOTS (include in Appendix)\n"
        for bs in blindspots:
            blindspots_text += (
                f"- **{bs.get('question', '?')}**\n"
                f"  Why overlooked: {bs.get('why_its_a_blindspot', '?')}\n"
                f"  Confidence: {bs.get('confidence', '?')}% | {bs.get('recommendation', '?')}\n"
            )

    # Inject Python's validation results so Opus knows which sub-reports are weak
    synthesis_prompt += f"""
{blindspots_text}

## PYTHON VALIDATION RESULTS (trust GOOD reports more, be skeptical of WEAK ones)
{validation_summary}

If a sub-report is marked WEAK: use its findings only if corroborated by another sub-report or CRT.
If a sub-report is marked GOOD: trust its [E] labeled findings.
"""

    (output_dir / "phase3-synthesis-prompt.md").write_text(synthesis_prompt)

    print(f"  Synthesis prompt: {len(synthesis_prompt):,} chars (~{len(synthesis_prompt)//4:,} tokens)")
    final_report = call_opus(synthesis_prompt, max_tokens=16000)
    (output_dir / "phase3-final-report.md").write_text(final_report)
    (output_dir / "final-report.md").write_text(final_report)

    print(f"  → Final report: {len(final_report):,} chars")

    # ── PHASE 3.5: PYTHON VALIDATES ──────────────────────────

    print(f"\n[PHASE 3.5] Python validates claims...")
    from research_factory import ADMIRALTY_SCORES, VERIFICATION_SCORES, WEIGHT_SCORES

    # Count E/I/J/A distribution
    eija = {"E": 0, "I": 0, "J": 0, "A": 0}
    for label in ["E", "I", "J", "A"]:
        eija[label] = len(re.findall(rf'\[{label}\]', final_report))
    total_labels = sum(eija.values()) or 1
    e_pct = eija["E"] / total_labels * 100
    j_pct = eija["J"] / total_labels * 100
    print(f"  E/I/J/A: E:{eija['E']} I:{eija['I']} J:{eija['J']} A:{eija['A']}")
    print(f"  E%: {e_pct:.0f}% {'GOOD' if e_pct > 50 else 'WARNING'} | J%: {j_pct:.0f}% {'GOOD' if j_pct < 20 else 'WARNING'}")

    # Compute real confidence from extracted claims (AgentTrust formula)
    try:
        claims_data = json.loads((output_dir / "all-claims.json").read_text())
        all_claim_confs = []
        for cr in claims_data:
            for cl in cr.get("claims", []):
                adm = cl.get("admiralty", "C3")
                ver_map = {"A1": 1.0, "A2": 0.85, "B2": 0.7, "C3": 0.4, "D4": 0.2, "E2": 0.1}
                source_q = ver_map.get(adm, 0.4)
                label = cl.get("label", "J")
                cons = {"E": 0.85, "I": 0.60, "J": 0.30}.get(label, 0.4)
                has_source = cl.get("source", "none") != "none"
                struct = 0.15 if has_source else 0.0
                conf = 0.5 * source_q + 0.3 * cons + 0.2 * struct
                all_claim_confs.append(conf)
        computed_confidence = sum(all_claim_confs) / len(all_claim_confs) * 100 if all_claim_confs else 0
    except Exception:
        computed_confidence = 0
    print(f"  Computed Confidence: {computed_confidence:.1f}% (AgentTrust formula, {len(all_claim_confs)} claims)")

    # Replace placeholders in final report with Python-computed values
    eija_str = f"E:{eija['E']} I:{eija['I']} J:{eija['J']} A:{eija['A']}"
    final_report = final_report.replace("{{CONFIDENCE}}", f"{computed_confidence:.1f}%")
    final_report = final_report.replace("{{EIJA}}", eija_str)
    # Also replace any Opus-guessed confidence with computed
    final_report = re.sub(
        r'(\|\s*Confidence\s*\|)\s*\d+(\.\d+)?%',
        f'\\1 {computed_confidence:.1f}%',
        final_report
    )
    # Rewrite final report with corrected values
    (output_dir / "final-report.md").write_text(final_report)
    print(f"  Replaced placeholders in final-report.md")

    # Count sources
    sources_used = set(re.findall(r'\[S(\d+)\]', final_report))
    print(f"  Sources referenced: {len(sources_used)}")

    # CRT cross-check
    crt_mentions = sum(1 for crt_line in crts.split("\n") if crt_line.strip()
                       and any(word in final_report.lower()
                               for word in crt_line.lower().split()[:5]))
    print(f"  CRT coverage: {crt_mentions} CRTs referenced")

    # ── LOG ENFORCEMENT (Python-verified) ───────────────────

    # Source Log completeness: every [S#] in body must have entry in Source Log section
    source_log_match = re.search(r'(?i)source\s*log(.*?)(?=\n##|\Z)', final_report, re.DOTALL)
    source_log_text = source_log_match.group(1) if source_log_match else ""
    sources_in_body = set(re.findall(r'\[S(\d+)\]', final_report))
    sources_in_log = set(re.findall(r'\[S(\d+)\]', source_log_text))
    orphan_sources = sources_in_body - sources_in_log  # in body but not logged
    log_issues = []
    if orphan_sources:
        log_issues.append(f"Sources referenced but not in Source Log: {sorted(orphan_sources)}")
        print(f"  WARNING: {len(orphan_sources)} orphan sources: {sorted(orphan_sources)}")

    # Claim Ledger completeness
    claim_ids = re.findall(r'CL-\d+', final_report)
    if len(claim_ids) < 10:
        log_issues.append(f"Claim Ledger has {len(claim_ids)} claims, need >= 10")
        print(f"  WARNING: Only {len(claim_ids)} claims in Claim Ledger (need 10+)")

    # Contradiction Register exists
    has_contradictions = "contradiction" in final_report.lower()
    if not has_contradictions:
        log_issues.append("No Contradiction Register found")
        print(f"  WARNING: No Contradiction Register")

    # Beipackzettel field completeness
    bpz_fields = ["Sources:", "Uncertainties:", "Risks:", "Not Checked:"]
    missing_bpz = [f for f in bpz_fields if f not in final_report]
    if missing_bpz:
        log_issues.append(f"Beipackzettel missing fields: {missing_bpz}")
        print(f"  WARNING: Beipackzettel missing: {missing_bpz}")

    if not log_issues:
        print(f"  Log enforcement: ALL PASS")

    validation = {
        "eija": eija,
        "e_pct": round(e_pct, 1),
        "j_pct": round(j_pct, 1),
        "sources_count": len(sources_used),
        "orphan_sources": sorted(orphan_sources),
        "claim_count": len(claim_ids),
        "has_contradiction_register": has_contradictions,
        "beipackzettel_missing_fields": missing_bpz,
        "log_issues": log_issues,
        "crt_coverage": crt_mentions,
        "healthy": e_pct > 50 and j_pct < 20 and len(log_issues) == 0,
    }
    (output_dir / "validation.json").write_text(json.dumps(validation, indent=2))

    # ── PHASE 4: ASSETS (Opus — full context) ────────────────

    print(f"\n[PHASE 4] Opus builds assets (full context)...")
    asset_prompt = ASSET_SYNTHESIS_PROMPT.format(report=final_report[:15000])

    # Enrich with vault context for cross-referencing
    asset_prompt += f"\n\n## EXISTING VAULT KNOWLEDGE (for cross-references)\n{vault[:30000]}"
    asset_prompt += f"\n\n## CRTs (link assets to verified truths)\n{crts}"

    assets = call_opus(asset_prompt, max_tokens=12000)
    (output_dir / "assets.md").write_text(assets)
    print(f"  → Assets: {len(assets):,} chars")

    # ── PHASE 5: PYTHON QUALITY GATE ─────────────────────────

    print(f"\n[PHASE 5] Quality gate...")

    # Check rubric score if present
    rubric_match = re.search(r'(\d+)/16', final_report)
    rubric_score = int(rubric_match.group(1)) if rubric_match else 0

    # Beipackzettel completeness
    has_beipackzettel = "BEIPACKZETTEL" in final_report.upper()
    has_uncertainties = "uncertaint" in final_report.lower()
    has_risks = "risk" in final_report.lower() and "do not deploy" in final_report.lower()
    has_framework = any(w in final_report.lower() for w in ["framework", "model", "maturity", "stack"])

    grade = "C"
    no_log_issues = len(log_issues) == 0
    if rubric_score >= 15 and e_pct > 50 and j_pct < 20 and has_beipackzettel and has_framework and no_log_issues:
        grade = "A+++"
    elif rubric_score >= 13 and e_pct > 50:
        grade = "A+"
    elif rubric_score >= 10:
        grade = "B"

    verdict = {
        "grade": grade,
        "rubric": rubric_score,
        "eija_healthy": validation["healthy"],
        "beipackzettel": has_beipackzettel,
        "framework": has_framework,
        "risks": has_risks,
        "log_enforcement": "PASS" if no_log_issues else f"FAIL ({len(log_issues)} issues)",
        "log_issues": log_issues,
        "decision": "SHIP" if grade in ("A+++", "A+") else "REVISE" if grade == "B" else "REJECT",
    }
    (output_dir / "quality-gate.json").write_text(json.dumps(verdict, indent=2))

    print(f"  Grade: {grade} | Rubric: {rubric_score}/16 | Decision: {verdict['decision']}")
    if verdict["decision"] != "SHIP":
        print(f"  Fix: {'E% too low' if e_pct <= 50 else ''} {'J% too high' if j_pct >= 20 else ''} {'No Beipackzettel' if not has_beipackzettel else ''}")

    # ── SAVE METADATA ─────────────────────────────────────────

    meta = {
        "topic": topic,
        "real_question": brief.get("real_question", ""),
        "sub_questions": len(sub_questions),
        "sub_reports_chars": sum(len(sr["report"]) for sr in sub_reports),
        "final_report_chars": len(final_report),
        "assets_chars": len(assets),
        "timestamp": datetime.now().isoformat(),
        "phases": {
            "phase1_framer": "opus",
            "phase2_research": f"gpt-4o × {len(sub_questions)} sub-questions",
            "phase3_synthesis": "opus",
            "phase4_assets": "gpt-4o",
        },
    }
    (output_dir / "pipeline.json").write_text(json.dumps(meta, indent=2))

    print(f"\n{'#'*60}")
    print(f"# DONE — MIA Pipeline")
    print(f"# Final: {output_dir / 'final-report.md'}")
    print(f"# Assets: {output_dir / 'assets.md'}")
    print(f"# Sub-reports: {len(sub_reports)} × {output_dir / 'sq-*'}")
    print(f"{'#'*60}")

    return meta


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="MIA Pipeline")
    parser.add_argument("--topic", required=True)
    parser.add_argument("--decision", default="")
    parser.add_argument("--sub-questions", type=int, default=5)
    parser.add_argument("--output", default=None)
    args = parser.parse_args()

    run_mia_pipeline(
        topic=args.topic,
        decision=args.decision,
        n_sub_questions=args.sub_questions,
        output_dir=Path(args.output) if args.output else None,
    )
