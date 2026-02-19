#!/usr/bin/env python3
"""
McKinsey-Grade 6-Prompt Pipeline.

6 specialized prompts instead of 1 mega-prompt.
Each prompt has ONE job. Quality gates between steps.

Usage:
    python3 mckinsey_pipeline.py --topic "Trust Calibration for AI Agents"
    python3 mckinsey_pipeline.py --topic "EU AI Act Compliance" --prompt 1  # Framer only
"""

import json
import os
import re
import sys
import time
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict

# Import shared infra from opus_synthesis and research_factory
sys.path.insert(0, str(Path(__file__).parent))
from opus_synthesis import (
    load_crts, load_corrections, load_reference_library,
    load_decisions, load_papers, load_vault_knowledge,
    load_best_report, call_opus, WORKSPACE, RESEARCH_BASE
)
from research_factory import llm_call, init_client, MODELS

# ============================================================
# 6 PROMPTS — Each has ONE job
# ============================================================

PROMPTS = {}

PROMPTS["framer"] = """You are the FRAMER. Your ONE job: find the real question behind the question.

## TOPIC
{topic}

## INITIAL DECISION CONTEXT
{decision}

## WHAT A PARTNER AT McKINSEY WOULD ASK
- "What's the question behind the question?"
- "What decision does this actually inform?"
- "What's the cost of being wrong?"
- "Why now — what changed?"

## YOUR OUTPUT (Research Brief)
1. THE REAL QUESTION (1 sentence — not the obvious one)
2. WHY NOW (what changed in the last 90 days)
3. DECISION CONTEXT (who decides, what happens if wrong)
4. SUB-QUESTIONS (5-8, MECE, non-overlapping)
5. EVIDENCE CRITERIA (what counts as evidence, what doesn't)
6. STOPPING CRITERIA (what confidence is "enough")
7. SCOPE BOUNDARIES (what's IN, what's OUT, what's ADJACENT)

Be specific. "Improve AI trust" is not a question. "Should we build calibration infrastructure before EU AI Act enforcement in Aug 2026, or wait for standards?" IS a question.
"""

PROMPTS["researcher"] = """You are the RESEARCHER. Your ONE job: find and organize the evidence.

## RESEARCH BRIEF (from Framer)
{framer_output}

## VERIFIED REFERENCE LIBRARY (cite as [S#])
{references}

## PAPER TEXTS (for claim verification)
{papers}

## VAULT KNOWLEDGE (proprietary, verified)
{vault}

## CRTs (do not contradict)
{crts}

## CORRECTIONS (learn from these)
{corrections}

## YOUR OUTPUT
### SOURCE LOG
For each source (S1, S2, ...):
- Title, Publisher/Type, URL/DOI, Access date
- Key finding (1-2 sentences)
- What it supports (which sub-question)
- Caveats/limits

### RAW CLAIM LEDGER (12 claims)
For each claim:
- Text (verbatim from source)
- Source [S#]
- E/I/J label:
  [E] = directly stated in source with data
  [I] = inferred from source through logic
  [J] = your assessment, not in any source
- Admiralty rating (A1-E2)
- Confidence (AgentTrust formula)

### CONTRADICTION REGISTER
- Claim vs Claim, Source vs Source
- Why they differ
- Impact on the decision

Rules:
- NO new claims without [S#]
- If no source exists: label [J] and state "no source found"
- Be SKEPTICAL. Default Admiralty: C3. A1 only with DOI.
"""

PROMPTS["synthesizer"] = """You are the SYNTHESIZER. Your ONE job: turn evidence into insights with a custom framework.

## RESEARCH BRIEF
{framer_output}

## SOURCE LOG + CLAIMS + CONTRADICTIONS (from Researcher)
{researcher_output}

## BEST PREVIOUS REPORT (improve on this)
{best_report}

## YOUR OUTPUT

### CUSTOM FRAMEWORK
Design ONE original framework/model that:
- Shows relationships that can't be googled
- Is specific to this topic (not a generic 2x2)
- Has a name (e.g., "Trust Calibration Maturity Model", "The Confidence Stack")
- Can be drawn as a diagram

Describe it in detail: axes, quadrants/levels, where key findings map.

### FINDINGS (5-7, each with E/I/J/A labels)
For each finding:
- **Finding** (1 sentence)
- **Label:** [E], [I], [J], or [A]
- **Evidence:** [S#] references
- **So What:** What this means for the decision maker (1-2 sentences)
- **If Wrong:** What happens if this finding is incorrect
- **Section Confidence:** X% (explain why)

### CASE STUDIES (2-3)
Real examples with:
- What happened
- Why it matters for this topic  
- Source
- Lesson (1 sentence)

Rules:
- Every section MUST end with "So What: ..."
- The Custom Framework MUST be original (not from any source)
- Findings must build on each other (not a list of disconnected facts)
"""

PROMPTS["challenger"] = """You are the CHALLENGER. Your ONE job: find what's wrong, weak, or missing.

## RESEARCH BRIEF
{framer_output}

## SYNTHESIZED FINDINGS + FRAMEWORK
{synthesizer_output}

## CLAIM LEDGER
{researcher_output}

## CRTs (verified truths)
{crts}

## CORRECTIONS (past mistakes)
{corrections}

## YOUR OUTPUT

### CHALLENGES (for each finding)
- Which finding
- Your challenge (specific, not vague)
- Evidence for the challenge (or "no counter-evidence found")
- Severity: Minor (nuance) / Major (changes conclusion) / Critical (invalidates finding)

### MISSING PERSPECTIVES
- What angles were not considered?
- What stakeholder views are absent?
- What data would change the conclusion?

### STRONGEST COUNTER-ARGUMENT
Write 1 paragraph: the best possible argument AGAINST the report's main recommendation.
Make it strong enough that the Synthesizer would need to respond.

### "WHAT WOULD CHANGE THIS"
For each major recommendation:
- Specific trigger/event that would invalidate it
- How likely is that trigger (High/Med/Low)
- What should the reader monitor

Rules:
- Be adversarial. Your job is to make the report BETTER by finding weaknesses.
- "Looks good" is not acceptable output.
- Find at least 3 challenges and 2 missing perspectives.
"""

PROMPTS["writer"] = """You are the WRITER. Your ONE job: write a report a CEO can act on Monday morning.

## RESEARCH BRIEF
{framer_output}

## FINDINGS + FRAMEWORK (from Synthesizer)
{synthesizer_output}

## CHALLENGES + COUNTER-ARGUMENTS (from Challenger)
{challenger_output}

## WRITING RULES
1. OPENER: Start with something an expert DOESN'T already know. Not a definition. Not history. A surprise.
2. "SO WHAT" DISCIPLINE: Every paragraph ends with why the reader should care.
3. NARRATIVE: Tell a story. V3-style. Case studies inline, not in appendix.
4. E/I/J/A LABELS: In the Claim Ledger (appendix), NOT inline in prose. Prose must flow.
5. RECOMMENDATIONS: Phased plan. Week 1 / Month 1 / Quarter 1. Specific, not aspirational.
6. HONEST: Weaknesses BEFORE strengths. "Despite X, Y" not "Y (but also X)".
7. LENGTH: 4000-6000 words. Not longer. Every word must earn its place.

## STRUCTURE
1. **Title + Date**
2. **Executive Summary** (SCR: Situation → Complication → Resolution, 3 paragraphs)
   - "If you read nothing else:" (3-5 bullets)
3. **Custom Framework** (from Synthesizer — describe so reader can sketch it)
4. **Key Findings** (5-7, narrative style, case studies woven in)
   - Each ends with "For the decision maker: ..."
5. **Recommendations**
   - Decision Matrix (if Scenario A → do X, if Scenario B → do Y)
   - Phased Plan (Week 1 / Month 1 / Quarter 1)
   - "Do Not Deploy If" (5 specific conditions)
6. **Risks & What Would Change This** (from Challenger)
7. **Appendix**
   - Claim Ledger (12 claims, E/I/J/A labeled, [S#], confidence)
   - Source Log
   - Contradiction Register

NO: landscape, tapestry, delve, synergy, cutting-edge, game-changer, "It's worth noting"
"""

PROMPTS["calibrator"] = """You are the CALIBRATOR. Your ONE job: measure how trustworthy this report is.

## FULL REPORT (from Writer)
{writer_output}

## CLAIM LEDGER (from Researcher)
{researcher_output}

## CRTs (verified truths — check report against these)
{crts}

## CORRECTIONS (past mistakes — is the report repeating any?)
{corrections}

## YOUR OUTPUT

### BEIPACKZETTEL (AgentTrust format)
| Field | Value |
|-------|-------|
| Confidence | X% (compute using formula below) |
| Risk Level | HIGH/MEDIUM/LOW |
| Grounded | Yes/No (has sources?) |
| Sources | count |
| E/I/J/A Distribution | E: X, I: X, J: X, A: X |
| Weakest Category | which label type is weakest and where |
| Research Type | Systematic Review / Expert Synthesis / Dialectic |

### Sources (list top 10)
### Uncertainties (list)
### Risks (list)  
### Not Checked (list)

### SELF-CALIBRATION
1. **CRT Cross-Check:** Does the report contradict any CRT? List matches/conflicts.
2. **Correction Check:** Does the report repeat any known correction? List.
3. **E/I/J/A Health:** >50% E? <20% J? Flag if unhealthy.
4. **"Monday Morning" Test:** Can the reader act on the recommendations this week? Yes/No + why.

### REVIEWER RUBRIC (0-2 each, total /16)
1) Decision alignment
2) Evidence discipline
3) Uncertainty integrity
4) Contradictions handled
5) Actionability
6) Structure compliance
7) Failure modes realism
8) Risk mitigation

### VERDICT
- SHIP IT (≥13/16, no Major/Critical challenges unaddressed)
- REVISE (10-12/16 or unaddressed Major challenges)  
- REJECT (<10/16 or unaddressed Critical challenges)

### CONFIDENCE FORMULA
claim_conf = 0.5 * SOURCE + 0.3 * CONSISTENCY + 0.2 * STRUCTURAL
Where SOURCE = admiralty × verification × recency
Report each claim's confidence. Then weighted average = overall.
"""


# ============================================================
# PIPELINE RUNNER
# ============================================================

def run_prompt(prompt_name: str, template: str, context: Dict,
               use_opus: bool = False, output_dir: Path = None) -> str:
    """Run a single prompt with context substitution."""
    
    # Fill template
    prompt = template.format(**{k: context.get(k, "") for k in
        re.findall(r'\{(\w+)\}', template)})
    
    print(f"\n{'='*60}")
    print(f"[{prompt_name.upper()}] {len(prompt):,} chars (~{len(prompt)//4:,} tokens)")
    print(f"{'='*60}")
    
    if output_dir:
        (output_dir / f"{prompt_name}-prompt.md").write_text(prompt)
    
    start = time.time()
    if use_opus:
        result = call_opus(prompt, max_tokens=8000)
    else:
        client = init_client()
        result = llm_call(client, MODELS["stage1_producer"], prompt, max_tokens=8000)
    elapsed = time.time() - start
    
    print(f"  → {len(result):,} chars in {elapsed:.0f}s")
    
    if output_dir:
        (output_dir / f"{prompt_name}-output.md").write_text(result)
    
    return result


def run_pipeline(
    topic: str,
    decision: str = "",
    use_opus: bool = False,
    start_prompt: int = 1,
    end_prompt: int = 6,
    output_dir: Optional[Path] = None,
) -> Dict:
    """Run the 6-prompt McKinsey pipeline."""
    
    if output_dir is None:
        slug = re.sub(r'[^a-z0-9]+', '-', topic.lower()).strip('-')
        ts = datetime.now().strftime("%Y%m%d-%H%M")
        output_dir = WORKSPACE / "research" / "mckinsey" / f"{slug}-{ts}"
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Load all knowledge once
    crts = load_crts()
    corrections = load_corrections()
    references = load_reference_library()
    papers = load_papers(max_chars=80000)
    vault = load_vault_knowledge(
        topic.lower().split() + ["calibration", "trust", "agent"],
        max_chars=100000
    )
    best_report = load_best_report()
    
    # Context accumulates across prompts
    ctx = {
        "topic": topic,
        "decision": decision or f"Should we invest in {topic}?",
        "crts": crts,
        "corrections": corrections,
        "references": references,
        "papers": papers,
        "vault": vault,
        "best_report": best_report[:30000],
        "framer_output": "",
        "researcher_output": "",
        "synthesizer_output": "",
        "challenger_output": "",
        "writer_output": "",
    }
    
    pipeline_order = [
        (1, "framer"),
        (2, "researcher"),
        (3, "synthesizer"),
        (4, "challenger"),
        (5, "writer"),
        (6, "calibrator"),
    ]
    
    print(f"\n{'#'*60}")
    print(f"# McKINSEY-GRADE PIPELINE: {topic}")
    print(f"# Prompts {start_prompt}-{end_prompt} | {'Opus' if use_opus else 'GPT-4o'}")
    print(f"# Output: {output_dir}")
    print(f"{'#'*60}")
    
    results = {}
    
    for num, name in pipeline_order:
        if num < start_prompt or num > end_prompt:
            continue
        
        output = run_prompt(
            name, PROMPTS[name], ctx,
            use_opus=use_opus, output_dir=output_dir
        )
        
        # Feed output to next prompt
        ctx[f"{name}_output"] = output
        results[name] = output
    
    # Save pipeline metadata
    meta = {
        "topic": topic,
        "decision": ctx["decision"],
        "model": "opus" if use_opus else MODELS["stage1_producer"],
        "prompts_run": [name for num, name in pipeline_order 
                        if start_prompt <= num <= end_prompt],
        "timestamp": datetime.now().isoformat(),
        "output_dir": str(output_dir),
    }
    (output_dir / "pipeline.json").write_text(json.dumps(meta, indent=2))
    
    # If writer ran, save final report
    if "writer" in results:
        (output_dir / "final-report.md").write_text(results["writer"])
    
    print(f"\n{'#'*60}")
    print(f"# DONE — {len(results)} prompts completed")
    print(f"# Output: {output_dir}")
    print(f"{'#'*60}")
    
    return results


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="McKinsey-Grade 6-Prompt Pipeline")
    parser.add_argument("--topic", required=True)
    parser.add_argument("--decision", default="")
    parser.add_argument("--opus", action="store_true", help="Use Opus instead of GPT-4o")
    parser.add_argument("--prompt", type=int, default=None, help="Run single prompt (1-6)")
    parser.add_argument("--start", type=int, default=1)
    parser.add_argument("--end", type=int, default=6)
    parser.add_argument("--output", default=None)
    args = parser.parse_args()
    
    if args.prompt:
        args.start = args.prompt
        args.end = args.prompt
    
    run_pipeline(
        topic=args.topic,
        decision=args.decision,
        use_opus=args.opus,
        start_prompt=args.start,
        end_prompt=args.end,
        output_dir=Path(args.output) if args.output else None,
    )
