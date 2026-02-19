#!/usr/bin/env python3
"""
Opus Mega-Synthesis: Full-context research using 1M token window.

Combines:
- Florian's Executive Research System Prompt v2 (phases, evidence discipline)
- AgentTrust (Beipackzettel, confidence formula, self-calibration)
- Proprietary knowledge (CRTs, corrections, decisions, vault)
- Reference Library (verified papers with DOIs)

Usage:
    python3 opus_synthesis.py --topic "Trust Calibration" --risk-tier 2
    python3 opus_synthesis.py --topic "EU AI Act Compliance" --phase 1  # Brief only
"""

import json
import os
import re
import sys
import time
import httpx
from pathlib import Path
from datetime import datetime
from typing import Optional

# Paths
WORKSPACE = Path(os.path.expanduser("~/.openclaw/workspace"))
RESEARCH_BASE = WORKSPACE / "research-base"
MEMORY = WORKSPACE / "memory"
VAULT = Path(os.path.expanduser(
    "~/Library/Mobile Documents/iCloud~md~obsidian/Documents/System_OS"
))

# ============================================================
# KNOWLEDGE LOADER — Proprietary + Verified
# ============================================================

def load_crts() -> str:
    """Load Compounding Research Truths."""
    p = RESEARCH_BASE / "compounding-research-truths.json"
    if not p.exists():
        return ""
    data = json.loads(p.read_text())
    truths = data.get("truths", [])
    lines = []
    for t in truths:
        status = t.get("status", "ACTIVE")
        if status != "ACTIVE":
            continue
        lines.append(
            f"[{t['id']}] {t['claim']} "
            f"(conf: {t.get('confidence', '?')}, source: {t.get('source', '?')}, "
            f"expires: {t.get('expiry_date', '?')})"
        )
    return "\n".join(lines)


def load_corrections() -> str:
    """Load corrections (things we got wrong)."""
    p = RESEARCH_BASE / "corrections.json"
    if not p.exists():
        return ""
    data = json.loads(p.read_text())
    corrections = data.get("corrections", [])
    lines = []
    for c in corrections:
        lines.append(
            f"[{c['id']}] WRONG: {c['wrong']}\n"
            f"  RIGHT: {c['right']}\n"
            f"  Severity: {c.get('severity', '?')} | Source: {c.get('source', '?')}"
        )
    return "\n".join(lines)


def load_reference_library() -> str:
    """Load verified reference papers."""
    p = RESEARCH_BASE / "reference-library.json"
    if not p.exists():
        return ""
    refs = json.loads(p.read_text())
    lines = []
    for r in refs:
        tier = f"Tier {r['tier']}"
        doi = f" DOI: {r['doi']}" if r.get('doi') else ""
        caveat = f" | CAVEAT: {r['caveat']}" if r.get('caveat') else ""
        lines.append(
            f"[{r['id']}] {r['title']} ({r['venue']}, {tier}): "
            f"{r['key_finding']}{doi}{caveat}"
        )
    return "\n".join(lines)


def load_decisions(max_chars: int = 5000) -> str:
    """Load key decisions."""
    p = MEMORY / "decisions.md"
    if not p.exists():
        return ""
    return p.read_text()[:max_chars]


def load_papers(max_chars: int = 50000) -> str:
    """Load all stored papers (full text)."""
    papers_dir = RESEARCH_BASE / "llm-trust-calibration" / "papers"
    if not papers_dir.exists():
        return ""
    texts = []
    total = 0
    for f in sorted(list(papers_dir.glob("*.md")) + list(papers_dir.glob("*.txt"))):
        content = f.read_text()
        if total + len(content) > max_chars:
            break
        texts.append(f"### {f.stem}\n{content}")
        total += len(content)
    return "\n\n".join(texts)


def load_vault_knowledge(topics: list, max_chars: int = 200000) -> str:
    """Load relevant vault files by topic keyword matching.
    
    Only loads knowledge-relevant dirs (no projects, no consulting).
    """
    relevant_dirs = [
        "20_Areas",         # Knowledge areas
        "70_Mia",           # Memory, patterns, learnings
        "60_Resources",     # Resources, references
    ]
    
    texts = []
    total = 0
    topic_keywords = [t.lower() for t in topics]
    
    for dir_name in relevant_dirs:
        dir_path = VAULT / dir_name
        if not dir_path.exists():
            continue
        for f in sorted(dir_path.rglob("*.md")):
            try:
                content = f.read_text()
            except Exception:
                continue
            # Relevance filter: file name or content matches topics
            name_lower = f.stem.lower()
            content_lower = content[:500].lower()
            if any(kw in name_lower or kw in content_lower for kw in topic_keywords):
                if total + len(content) > max_chars:
                    break
                rel_path = f.relative_to(VAULT)
                texts.append(f"### {rel_path}\n{content[:5000]}")
                total += len(content[:5000])
    
    return "\n\n".join(texts)


def load_best_report(topic_slug: str = "AR-020", max_chars: int = 60000) -> str:
    """Load the best existing report for context."""
    # Try v5 first, then v4, v3
    for version in ["v5-full", "v4-full", "v3-full"]:
        p = WORKSPACE / "research" / f"{topic_slug}-{version}.md"
        if p.exists():
            return p.read_text()[:max_chars]
    return ""


# ============================================================
# OPUS CALL (OAuth)
# ============================================================

def call_opus(prompt: str, max_tokens: int = 16000) -> str:
    """Call Claude Opus via OAuth token. Full 1M context."""
    # Load OAuth token
    auth_path = Path(os.path.expanduser(
        "~/.openclaw/agents/main/agent/auth-profiles.json"
    ))
    if not auth_path.exists():
        raise RuntimeError("No OAuth token found at auth-profiles.json")
    
    auth_data = json.loads(auth_path.read_text())
    token = None
    for profile in auth_data:
        if profile.get("accessToken", "").startswith("sk-ant-oat"):
            token = profile["accessToken"]
            break
    
    if not token:
        raise RuntimeError("No sk-ant-oat token found in auth-profiles.json")
    
    print(f"  [OPUS] Sending {len(prompt)} chars ({len(prompt)//4}K tokens est.)...")
    print(f"  [OPUS] This will take 5-15 minutes. Be patient.")
    
    start = time.time()
    resp = httpx.post(
        "https://api.anthropic.com/v1/messages",
        headers={
            "Authorization": f"Bearer {token}",
            "anthropic-version": "2023-06-01",
            "anthropic-beta": "oauth-2025-04-20",
            "content-type": "application/json",
        },
        json={
            "model": "claude-opus-4-20250514",
            "max_tokens": max_tokens,
            "messages": [{"role": "user", "content": prompt}],
        },
        timeout=900,  # 15 min
    )
    elapsed = time.time() - start
    
    if resp.status_code != 200:
        raise RuntimeError(f"Opus call failed ({resp.status_code}): {resp.text[:500]}")
    
    data = resp.json()
    text = data["content"][0]["text"]
    print(f"  [OPUS] Response: {len(text)} chars in {elapsed:.0f}s")
    return text


# ============================================================
# MEGA-PROMPT BUILDER
# ============================================================

def build_opus_prompt(
    topic: str,
    decision: str = "",
    audience: str = "Founder",
    risk_tier: int = 2,
    freshness: str = "last_12m",
    phase: str = "full",
) -> str:
    """Build the Opus mega-prompt with all proprietary knowledge."""
    
    # Load standards
    standards_dir = WORKSPACE / "standards"
    erf_system_prompt = ""
    if (standards_dir / "ERF-SYSTEM-PROMPT-v2.md").exists():
        erf_system_prompt = (standards_dir / "ERF-SYSTEM-PROMPT-v2.md").read_text()
    erf_templates = ""
    if (standards_dir / "ERF-TEMPLATES.md").exists():
        erf_templates = (standards_dir / "ERF-TEMPLATES.md").read_text()

    # Load all knowledge
    crts = load_crts()
    corrections = load_corrections()
    refs = load_reference_library()
    decisions = load_decisions()
    papers = load_papers(max_chars=80000)
    best_report = load_best_report()
    
    # Topic keywords for vault search
    topic_words = topic.lower().split() + ["calibration", "trust", "agent", "confidence"]
    vault_knowledge = load_vault_knowledge(topic_words, max_chars=150000)
    
    # Phase commands
    phase_instruction = {
        "1": "Run Phase 1 only — output Research Brief only.",
        "1-2": "Run Phases 1-2 — Research Brief + Source Log + recommended sources.",
        "full": "Run full report (Phases 0-4.5 + Knowledge Writeback).",
        "review": "Reviewer Pass only — rubric + claim audit.",
    }.get(phase, "Run full report.")
    
    prompt = f"""## EXEC RESEARCH FACTORY — CANONICAL SYSTEM PROMPT

{erf_system_prompt}

---

## CONTROL PANEL
- TOPIC: {topic}
- DECISION_TO_INFORM: {decision or f"Should we invest in {topic}? What's real, what's hype?"}
- DECISION_OWNER: Florian Ziesche (Founder, Ainary Ventures)
- AUDIENCE: {audience}
- RISK_TIER: {risk_tier}
- FRESHNESS: {freshness}
- BROWSING: not_allowed
- OUTPUT_WRITEBACK: true
- OUTPUT_LENGTH: extensive

## COMMAND
{phase_instruction}

## TEMPLATES (use these exact structures)
{erf_templates}

---

## ADDITIONAL RULES (Ainary-specific)
- NO: landscape, tapestry, delve, synergy, cutting-edge, game-changer
- Lead with something an expert DOESN'T already know
- Use [S#] citations (not [1], [2]) to match our Source Log format

## E/I/J/A EPISTEMIC LABELING (MANDATORY for every sentence in findings)
Label EVERY claim in the report body:
- [E] Evidenced: Peer-reviewed, primary data, cites [S#]. Admiralty A1-A2. Confidence >=70%.
- [I] Interpreted: Derived from evidence, explain logic chain. Admiralty B2-C3. Confidence 40-70%.
- [J] Judged: Pattern recognition, state assumptions. Admiralty C3-D4. Confidence 20-50%. If <50%: "NEEDS HUMAN REVIEW".
- [A] Actionable: Recommendation. MUST reference supporting E/I/J. MUST include "If wrong:" scenario.

Report MUST disclose E/I/J/A distribution in Beipackzettel.
Healthy: >50% E, <20% J. Red flag: >50% J.

## SELF-CALIBRATING PROTOCOL

This report must calibrate itself using the methods it describes:
1. Every section carries a confidence score (AgentTrust formula)
2. Key claims tested against our Compounding Research Truths below
3. Claims contradicting our Corrections are flagged immediately
4. Claims with <50% confidence marked: "NEEDS HUMAN REVIEW"
5. At the end: Beipackzettel (confidence, sources, uncertainties, risks, not_checked)

AgentTrust Confidence Formula:
  claim_conf = 0.5 * SOURCE + 0.3 * CONSISTENCY + 0.2 * STRUCTURAL
  Where SOURCE = admiralty_score * verification_score * recency
  CONSISTENCY: verified=0.85, partial=0.60, unverifiable=0.30
  STRUCTURAL: DOI=+0.30, URL=+0.15, specific_pct=+0.10, year=+0.05, cap 0.50

---

## PROPRIETARY KNOWLEDGE (our verified truths — DO NOT contradict)

### Compounding Research Truths (CRTs)
{crts or "None loaded."}

### Corrections (things we got wrong — learn from these)
{corrections or "None loaded."}

### Key Decisions (why we chose what we chose)
{decisions[:3000] if decisions else "None loaded."}

---

## VERIFIED REFERENCE LIBRARY (use [S#] to cite)
{refs or "None loaded."}

---

## FULL PAPER TEXTS (for claim verification)
{papers[:80000] if papers else "No papers loaded."}

---

## BEST EXISTING REPORT (improve on this, don't restart from scratch)
{best_report[:40000] if best_report else "No previous report."}

---

## VAULT KNOWLEDGE (our proprietary research notes)
{vault_knowledge[:100000] if vault_knowledge else "No vault knowledge loaded."}

---

## OUTPUT STRUCTURE

### Phase 1: Research Brief
1. Primary Research Question (why now)
2. Decision Context (who decides, consequence if wrong)
3. Sub-Questions (5-12, MECE)
4. Evidence Criteria
5. Stopping Criteria (what confidence is "enough")

### Phase 2: Investigation
- Artifact A: Source Log (every [S#])
- Artifact B: Claim Ledger (12 claims, AgentTrust-rated)
- Artifact C: Contradiction Register

### Phase 3: Validation & Gap Check
- Cross-check claims against CRTs and Corrections
- What's missing? What would change conclusions?

### Phase 4: Synthesis
1. Beipackzettel (AgentTrust format: confidence, sources, uncertainties, risks, not_checked, risk_level)
2. Assumption Register
3. Executive Summary (SCR: Situation → Complication → Resolution)
4. Key Takeaways (standalone bullets with [S#])
5. Detailed Findings (each: Finding → [EVIDENCE/INTERPRETATION/JUDGMENT] → Caveat → Implication)
6. Case Studies (2-3, real, sourced)
7. "Do Not Deploy If" section
8. Recommendations (decision criteria + phased plan)
9. Appendix: Source Log + Claim Ledger + Contradiction Register

### Phase 4.5: Reviewer Pass
Score 0-2 on: decision alignment, evidence discipline, uncertainty integrity,
contradictions handled, actionability, structure, failure modes, risk mitigation.
Fix any failures before output.

### Phase 5: Knowledge Writeback
JSON blocks: new CRTs, updated CRTs, new corrections, entity relations.

## BEIPACKZETTEL FORMAT (mandatory, first thing in output)
| Field | Value |
|-------|-------|
| Confidence | X% (AgentTrust formula) |
| Risk Level | HIGH/MEDIUM/LOW |
| Grounded | Yes/No |
| Sources | count |
| Research Type | Systematic Review / Expert Synthesis / Dialectic |
| Data Source | Primary / Secondary / Mixed |

### Sources (list)
### Uncertainties (list)  
### Risks (list)
### Not Checked (list)
"""
    
    return prompt


# ============================================================
# MAIN
# ============================================================

def run_opus_synthesis(
    topic: str,
    decision: str = "",
    audience: str = "Founder",
    risk_tier: int = 2,
    freshness: str = "last_12m",
    phase: str = "full",
    output_dir: Optional[Path] = None,
) -> dict:
    """Run Opus mega-synthesis."""
    
    if output_dir is None:
        slug = re.sub(r'[^a-z0-9]+', '-', topic.lower()).strip('-')
        output_dir = WORKSPACE / "research" / "opus" / slug
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"\n{'='*60}")
    print(f"[OPUS MEGA-SYNTHESIS] {topic}")
    print(f"  Risk Tier: {risk_tier} | Audience: {audience} | Phase: {phase}")
    print(f"{'='*60}")
    
    # Build prompt
    prompt = build_opus_prompt(topic, decision, audience, risk_tier, freshness, phase)
    (output_dir / "prompt.md").write_text(prompt)
    
    token_est = len(prompt) // 4
    print(f"\n  Prompt: {len(prompt):,} chars (~{token_est:,} tokens)")
    print(f"  Opus budget: 1,000,000 tokens")
    print(f"  Usage: {token_est * 100 / 1000000:.1f}%")
    
    # Call Opus
    result = call_opus(prompt, max_tokens=16000)
    
    # Save
    (output_dir / "report.md").write_text(result)
    
    # Extract writeback if present
    wb_match = re.search(r'```json\s*(\{[^`]*"crt_updates"[^`]*\})\s*```', result, re.DOTALL)
    if wb_match:
        try:
            writeback = json.loads(wb_match.group(1))
            (output_dir / "writeback.json").write_text(json.dumps(writeback, indent=2))
            print(f"  [WRITEBACK] Extracted knowledge updates")
        except json.JSONDecodeError:
            pass
    
    # Summary
    print(f"\n{'='*60}")
    print(f"[DONE] Opus Mega-Synthesis")
    print(f"  Output: {output_dir / 'report.md'}")
    print(f"  Prompt: {output_dir / 'prompt.md'}")
    print(f"{'='*60}")
    
    return {
        "topic": topic,
        "prompt_chars": len(prompt),
        "prompt_tokens_est": token_est,
        "result_chars": len(result),
        "output_dir": str(output_dir),
    }


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Opus Mega-Synthesis")
    parser.add_argument("--topic", required=True)
    parser.add_argument("--decision", default="")
    parser.add_argument("--audience", default="Founder")
    parser.add_argument("--risk-tier", type=int, default=2)
    parser.add_argument("--freshness", default="last_12m")
    parser.add_argument("--phase", default="full", choices=["1", "1-2", "full", "review"])
    parser.add_argument("--output", default=None)
    args = parser.parse_args()
    
    run_opus_synthesis(
        topic=args.topic,
        decision=args.decision,
        audience=args.audience,
        risk_tier=args.risk_tier,
        freshness=args.freshness,
        phase=args.phase,
        output_dir=Path(args.output) if args.output else None,
    )
