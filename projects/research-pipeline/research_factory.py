#!/usr/bin/env python3
"""
Exec Research Factory — 3-Stage Pipeline (v1.0)

Produces trusted research outputs in three independent stages:
  Stage 1: Research Report (Templates A-H)
  Stage 2: Asset Builder (Atomic Notes + Playbooks + Templates + RAG JSON)
  Stage 3: Knowledge Integration (CRT updates + Vault notes + Entity links)

Each stage is a separate LLM call. Each stage is verifiable.
Same input = same output. Report N benefits from assets of reports 1..N-1.

Usage:
    # Full pipeline
    python3 research_factory.py --topic "Trust Calibration" --intake intake.json

    # Single stage
    python3 research_factory.py --topic "Trust Calibration" --stage 2 --input report.md

    # List hardcoded topics
    python3 research_factory.py --agenda

    # Compute confidence from claim ledger
    python3 research_factory.py --confidence claims.json

Design Principles:
    - Simplicity beats complexity when executed well
    - Every report: honest comparison (what's better, worse, what to combine)
    - Formula-based confidence (not vibes)
    - Templates A-J are the process, not guidelines
    - Research first, consulting derivative second
"""

import anthropic
import argparse
import json
import os
import re
import sys
import hashlib
from dataclasses import dataclass, field, asdict
from datetime import datetime
from pathlib import Path
from typing import Optional, List, Dict, Any

# --- Paths ---
WORKSPACE = Path(os.path.expanduser("~/.openclaw/workspace"))
STANDARDS = WORKSPACE / "standards"
RESEARCH_DIR = WORKSPACE / "research"
RESEARCH_BASE = WORKSPACE / "research-base"
CRT_PATH = RESEARCH_BASE / "compounding-research-truths.json"
CORRECTIONS_PATH = RESEARCH_BASE / "corrections.json"
AGENDA_PATH = STANDARDS / "RESEARCH-AGENDA.md"

# --- Models (cost-optimized) ---
MODELS = {
    # Hybrid: GPT-4o produces (fast, cheap), Sonnet evaluates (skeptical, honest)
    "stage1_producer": "gpt-4o",                       # Research report (fast)
    "stage1_reviewer": "claude-sonnet-4-20250514",     # Review + rubric (skeptical)
    "stage2_assets":   "gpt-4o",                       # Asset extraction (fast)
    "stage3_integrate": "gpt-4o",                      # CRT updates (fast)
    "hypothesis_gen":  "gpt-4o",                       # Generate competing hypotheses
    "synthesis":       "claude-sonnet-4-20250514",     # Synthesize N reports (quality)
}

# --- API Backend ---
# Supports "anthropic-oauth", "anthropic", or "openai". Auto-detects.
API_BACKEND = None  # Set by init_client()
OAUTH_TOKEN = None  # For Anthropic OAuth

def _load_openclaw_oauth_token() -> str | None:
    """Load OAuth token from OpenClaw auth-profiles.json."""
    path = Path.home() / ".openclaw" / "agents" / "main" / "agent" / "auth-profiles.json"
    if not path.exists():
        return None
    try:
        data = json.loads(path.read_text())
        for profile_id in ["anthropic:default", "anthropic:manual"]:
            profile = data.get("profiles", {}).get(profile_id, {})
            token = profile.get("token", "")
            if token.startswith("sk-ant-oat01-"):
                return token
    except Exception:
        pass
    return None


def init_client():
    """Initialize the best available API client.

    Priority: 1) OpenAI (fast), 2) Anthropic API key, 3) Anthropic OAuth (slow but 1M context)
    Set ANTHROPIC_OAUTH_TOKEN or PREFER_OAUTH=1 to force OAuth.
    """
    global API_BACKEND, OAUTH_TOKEN

    # 0) Explicit OAuth preference
    if os.environ.get("PREFER_OAUTH") or os.environ.get("ANTHROPIC_OAUTH_TOKEN"):
        oauth = os.environ.get("ANTHROPIC_OAUTH_TOKEN") or _load_openclaw_oauth_token()
        if oauth:
            API_BACKEND = "anthropic-oauth"
            OAUTH_TOKEN = oauth
            return None

    # 1) OpenAI (fast, cheap)
    openai_key = os.environ.get("OPENAI_API_KEY", "")
    if openai_key:
        try:
            from openai import OpenAI
            client = OpenAI()
            API_BACKEND = "openai"
            return client
        except Exception:
            pass

    # 2) Standard Anthropic API key
    anthropic_key = os.environ.get("ANTHROPIC_API_KEY", "")
    if anthropic_key and not anthropic_key.startswith("sk-ant-oat01-"):
        try:
            client = anthropic.Anthropic()
            API_BACKEND = "anthropic"
            return client
        except Exception:
            pass

    # 3) Anthropic OAuth (slow but works, 1M context)
    oauth = _load_openclaw_oauth_token()
    if oauth:
        API_BACKEND = "anthropic-oauth"
        OAUTH_TOKEN = oauth
        return None

    raise RuntimeError("No working API key found. Set ANTHROPIC_OAUTH_TOKEN, ANTHROPIC_API_KEY, or OPENAI_API_KEY.")


# OpenAI model mapping
OPENAI_MODELS = {
    "claude-sonnet-4-5-20250514": "gpt-4o",
    "claude-haiku-4-5-20250514": "gpt-4o-mini",
    "claude-opus-4-20250514": "gpt-4o",
}


def llm_call(client, model: str, prompt: str, max_tokens: int = 16000,
             temperature: float = 0.0) -> str:
    """Unified LLM call — Anthropic OAuth, Anthropic API, or OpenAI."""
    global API_BACKEND, OAUTH_TOKEN

    # Hybrid routing: model name determines backend
    is_openai_model = model.startswith("gpt-") or model.startswith("o1-") or model.startswith("o3-")
    is_claude_model = model.startswith("claude-")

    # If model is explicitly OpenAI, use OpenAI client regardless of API_BACKEND
    if is_openai_model:
        openai_key = os.environ.get("OPENAI_API_KEY", "")
        if openai_key:
            from openai import OpenAI
            oai = OpenAI(api_key=openai_key)
            for attempt in range(3):
                response = oai.chat.completions.create(
                    model=model, max_tokens=max_tokens, temperature=temperature,
                    messages=[{"role": "user", "content": prompt}])
                text = response.choices[0].message.content
                # Retry on GPT-4o refusal (48 chars = "I'm sorry, but I can't assist with that request.")
                if len(text) > 100 or attempt == 2:
                    return text
                print(f"  [RETRY] GPT-4o refusal ({len(text)} chars), attempt {attempt+2}/3")
                import time; time.sleep(2)
            return text

    # If model is Claude and we have OAuth, use OAuth
    if is_claude_model and OAUTH_TOKEN:
        import httpx
        r = httpx.post("https://api.anthropic.com/v1/messages",
            headers={"Authorization": f"Bearer {OAUTH_TOKEN}", "anthropic-version": "2023-06-01",
                     "anthropic-beta": "oauth-2025-04-20", "content-type": "application/json"},
            json={"model": model, "max_tokens": max_tokens,
                  "messages": [{"role": "user", "content": prompt}]},
            timeout=httpx.Timeout(connect=30, read=600, write=30, pool=30))
        if r.status_code != 200:
            raise RuntimeError(f"Anthropic OAuth error {r.status_code}: {r.text[:200]}")
        return r.json()["content"][0]["text"]

    # Fallback to original routing
    if API_BACKEND == "anthropic-oauth":
        import httpx
        r = httpx.post("https://api.anthropic.com/v1/messages",
            headers={
                "Authorization": f"Bearer {OAUTH_TOKEN}",
                "anthropic-version": "2023-06-01",
                "anthropic-beta": "oauth-2025-04-20",
                "content-type": "application/json",
            },
            json={
                "model": model,
                "max_tokens": max_tokens,
                "messages": [{"role": "user", "content": prompt}],
            },
            timeout=httpx.Timeout(connect=30, read=600, write=30, pool=30),
        )
        if r.status_code != 200:
            raise RuntimeError(f"Anthropic OAuth error {r.status_code}: {r.text[:200]}")
        return r.json()["content"][0]["text"]

    elif API_BACKEND == "anthropic":
        response = client.messages.create(
            model=model,
            max_tokens=max_tokens,
            messages=[{"role": "user", "content": prompt}],
        )
        return response.content[0].text

    elif API_BACKEND == "openai" or (client and hasattr(client, 'chat')):
        oai_model = OPENAI_MODELS.get(model, "gpt-4o")
        response = client.chat.completions.create(
            model=oai_model,
            max_tokens=max_tokens,
            temperature=temperature,
            messages=[{"role": "user", "content": prompt}],
        )
        return response.choices[0].message.content

    else:
        raise RuntimeError(f"Unknown API backend: {API_BACKEND}")


# ============================================================
# CONFIDENCE FORMULA (AgentTrust-Enhanced)
# ============================================================
# Three independent signals, combined:
#
# 1. SOURCE SIGNAL (Admiralty × Verification × Recency)
#    = How trustworthy is the evidence?
#
# 2. CONSISTENCY SIGNAL (Budget-CoCoA, from agenttrust)
#    = If we ask 3 independent evaluators, do they agree?
#    Agreement 3/3 → 0.85, 2/3 → 0.60, 1/3 → 0.30
#
# 3. STRUCTURAL SIGNAL (deterministic)
#    = Does the claim have a DOI? A URL? A specific number?
#    DOI → +0.2, URL → +0.1, Specific number → +0.05
#
# Final: claim_confidence = 0.5 * source + 0.3 * consistency + 0.2 * structural
# Report_Confidence = sum(claim_conf * claim_weight) / sum(claim_weight)
#
# This formula is from: github.com/florianziesche/agenttrust
# Budget-CoCoA reference: Xiong et al. (2024), adapted for 3 samples
# Admiralty system: NATO standard intelligence grading
#
# claim_confidence (source component) =
#   source_quality          (Admiralty: A1=1.0, B2=0.7, C3=0.4, D4=0.2, E5=0.1, F6=0.0)
#   * verification_status   (verified=1.0, partial=0.7, unverifiable=0.3)
#   * consensus             (N_agree / N_total agents who evaluated)
#   * recency_factor        (2026=1.0, 2025=0.9, 2024=0.8, 2023=0.7, older=0.6)
#
# claim_weight =
#   1.0  if load-bearing (in Claim Ledger)
#   0.5  if supporting
#   0.2  if contextual

ADMIRALTY_SCORES = {
    "A1": 1.0, "A2": 0.9, "A3": 0.8,
    "B1": 0.9, "B2": 0.7, "B3": 0.6,
    "C1": 0.7, "C2": 0.5, "C3": 0.4,
    "D1": 0.5, "D2": 0.3, "D3": 0.2,
    "E1": 0.3, "E2": 0.2, "E3": 0.1,
    "F1": 0.1, "F2": 0.05, "F3": 0.0,
}

VERIFICATION_SCORES = {
    "verified": 1.0,
    "partial": 0.7,
    "unverifiable": 0.3,
}

WEIGHT_SCORES = {
    "load-bearing": 1.0,
    "supporting": 0.5,
    "contextual": 0.2,
}


@dataclass
class Claim:
    """A single claim in the Claim Ledger."""
    id: str
    text: str
    section: str
    evidence_sources: List[str]     # e.g. ["S1", "S3"]
    admiralty: str = "C2"           # Admiralty rating
    verification: str = "partial"   # verified | partial | unverifiable
    consensus: float = 1.0         # N_agree / N_total (0.0 - 1.0)
    recency_year: int = 2025       # Year of primary evidence
    weight: str = "load-bearing"   # load-bearing | supporting | contextual
    low_evidence_note: str = ""    # If Low: what would raise confidence?

    @property
    def source_quality(self) -> float:
        return ADMIRALTY_SCORES.get(self.admiralty, 0.4)

    @property
    def verification_score(self) -> float:
        return VERIFICATION_SCORES.get(self.verification, 0.3)

    @property
    def recency_factor(self) -> float:
        current = datetime.now().year
        diff = current - self.recency_year
        return max(0.5, 1.0 - (diff * 0.1))

    @property
    def claim_weight(self) -> float:
        return WEIGHT_SCORES.get(self.weight, 0.5)

    @property
    def confidence(self) -> float:
        """Compute claim-level confidence (0.0 - 1.0)."""
        return (
            self.source_quality
            * self.verification_score
            * self.consensus
            * self.recency_factor
        )


def compute_report_confidence(claims: List[Claim]) -> Dict[str, Any]:
    """
    Compute formula-based report confidence from Claim Ledger.

    Returns dict with:
      - confidence: float (0.0 - 1.0)
      - confidence_pct: int (0 - 100)
      - n_claims: int
      - breakdown: list of per-claim scores
      - weakest: list of 3 weakest claims
    """
    if not claims:
        return {"confidence": 0.0, "confidence_pct": 0, "n_claims": 0,
                "breakdown": [], "weakest": []}

    weighted_sum = 0.0
    weight_sum = 0.0
    breakdown = []

    for c in claims:
        conf = c.confidence
        w = c.claim_weight
        weighted_sum += conf * w
        weight_sum += w
        breakdown.append({
            "id": c.id,
            "text": c.text[:80],
            "confidence": round(conf, 3),
            "weight": c.weight,
            "factors": {
                "source_quality": c.source_quality,
                "verification": c.verification_score,
                "consensus": c.consensus,
                "recency": round(c.recency_factor, 2),
            }
        })

    overall = weighted_sum / weight_sum if weight_sum > 0 else 0.0

    # Sort by confidence ascending to find weakest
    breakdown.sort(key=lambda x: x["confidence"])
    weakest = breakdown[:3]

    return {
        "confidence": round(overall, 4),
        "confidence_pct": round(overall * 100),
        "n_claims": len(claims),
        "breakdown": sorted(breakdown, key=lambda x: x["id"]),
        "weakest": weakest,
    }


def load_claims_from_json(path: Path) -> List[Claim]:
    """Load claims from a JSON file."""
    with open(path) as f:
        data = json.load(f)
    return [Claim(**c) for c in data]


# ============================================================
# RESEARCH AGENDA
# ============================================================

HARDCODED_TOPICS = [
    {
        "id": "trust-calibration",
        "name": "Trust Calibration for AI Agents",
        "report_id": "AR-020",
        "status": "v5-in-progress",
        "refresh": "quarterly",
        "crt_pool": "calibration",
        "cross_refs": ["agent-governance", "multi-agent", "ai-cost-roi"],
    },
    {
        "id": "agent-governance",
        "name": "Agent Governance & Safety",
        "report_id": "AR-030",
        "status": "v1-from-gpt-export",
        "refresh": "quarterly",
        "crt_pool": "governance",
        "cross_refs": ["trust-calibration", "eu-ai-act"],
    },
    {
        "id": "multi-agent",
        "name": "Multi-Agent Architectures",
        "report_id": "AR-031",
        "status": "planned",
        "refresh": "quarterly",
        "crt_pool": "multi-agent",
        "cross_refs": ["trust-calibration", "agent-governance"],
    },
    {
        "id": "ai-cost-roi",
        "name": "AI Cost & ROI Models",
        "report_id": "AR-032",
        "status": "planned",
        "refresh": "semi-annual",
        "crt_pool": "market",
        "cross_refs": ["trust-calibration"],
    },
    {
        "id": "eu-ai-act",
        "name": "EU AI Act Compliance",
        "report_id": "AR-033",
        "status": "planned",
        "refresh": "on-regulation-change",
        "crt_pool": "regulatory",
        "cross_refs": ["agent-governance", "trust-calibration"],
    },
    {
        "id": "autonomous-research",
        "name": "Autonomous Research Methods",
        "report_id": "AR-034",
        "status": "next",
        "refresh": "quarterly",
        "crt_pool": "meta",
        "cross_refs": ["trust-calibration"],
        "note": "META: how WE do research. This IS the product.",
    },
]

OPEN_SLOTS = 3  # Max concurrent open topics

# Beipackzettel — AgentTrust format (structured, not just a table)
# Mirrors: agenttrust.core.beipackzettel.Beipackzettel
def make_beipackzettel(output_id: str, output_type: str, topic: str,
                       stage: str, round_num: int = 0, parent_id: str = "none",
                       research_type: str = "Expert Synthesis",
                       data_source: str = "Secondary",
                       confidence: float = 0.0,
                       sources: list = None,
                       uncertainties: list = None,
                       risks: list = None,
                       not_checked: list = None,
                       n_rag_queries: int = 0,
                       model: str = "") -> str:
    """Generate a Beipackzettel (AgentTrust format) for any output.

    Mirrors the agenttrust.core.beipackzettel.Beipackzettel dataclass:
    confidence, sources, uncertainties, risks, not_checked, risk_level.
    """
    sources = sources or []
    uncertainties = uncertainties or []
    risks = risks or []
    not_checked = not_checked or []

    # Risk level (same logic as AgentTrust)
    if confidence < 50 or len(risks) >= 3:
        risk_level = "HIGH"
    elif confidence >= 80 and len(risks) == 0:
        risk_level = "LOW"
    else:
        risk_level = "MEDIUM"

    # Grounded check
    is_grounded = len(sources) > 0

    bpz = f"""## BEIPACKZETTEL
| Field | Value |
|-------|-------|
| Output ID | {output_id} |
| Output Type | {output_type} |
| Research Type | {research_type} |
| Data Source | {data_source} |
| Topic | {topic} |
| Pipeline Stage | {stage} |
| Round | {round_num} |
| Parent Output | {parent_id} |
| Timestamp | {datetime.now().strftime("%Y-%m-%d %H:%M")} |
| Model | {model} |
| **Confidence** | **{confidence:.1f}%** |
| **Risk Level** | **{risk_level}** |
| Grounded | {"Yes" if is_grounded else "NO — ungrounded output"} |
| Sources | {len(sources)} |
| RAG Queries | {n_rag_queries} |

### Sources
{chr(10).join(f"- {s}" for s in sources[:20]) if sources else "- None (ungrounded)"}

### Uncertainties
{chr(10).join(f"- {u}" for u in uncertainties) if uncertainties else "- None declared"}

### Risks
{chr(10).join(f"- {r}" for r in risks) if risks else "- None declared"}

### Not Checked
{chr(10).join(f"- {nc}" for nc in not_checked) if not_checked else "- None declared"}
"""
    return bpz


def beipackzettel_to_json(bpz_text: str, output_id: str, confidence: float,
                          sources: list = None, uncertainties: list = None,
                          risks: list = None, not_checked: list = None,
                          model: str = "") -> dict:
    """Convert Beipackzettel to JSON (compatible with agenttrust.Beipackzettel.to_dict)."""
    sources = sources or []
    uncertainties = uncertainties or []
    risks = risks or []
    not_checked = not_checked or []

    if confidence < 50 or len(risks) >= 3:
        risk_level = "high"
    elif confidence >= 80 and len(risks) == 0:
        risk_level = "low"
    else:
        risk_level = "medium"

    return {
        "output_id": output_id,
        "confidence": confidence,
        "sources": sources,
        "uncertainties": uncertainties,
        "risks": risks,
        "not_checked": not_checked,
        "model": model,
        "risk_level": risk_level,
        "is_grounded": len(sources) > 0,
    }


# Legacy wrapper for backward compatibility
BEIPACKZETTEL_TEMPLATE = "DEPRECATED — use make_beipackzettel() directly"

def _legacy_beipackzettel_format(output_id, output_type, topic, stage,
                                  round_num=0, parent_id="none",
                                  research_type="Expert Synthesis",
                                  data_source="Secondary",
                                  confidence="not computed",
                                  n_sources=0, n_rag_queries=0,
                                  model="", limitations=""):
    """Legacy format — converts to new format."""
    return make_beipackzettel(
        output_id=output_id, output_type=output_type, topic=topic,
        stage=stage, round_num=round_num, parent_id=parent_id,
        research_type=research_type, data_source=data_source,
        confidence=float(confidence.replace('%','')) if isinstance(confidence, str) and '%' in confidence else 0.0,
        sources=[], risks=[limitations] if limitations else [],
        model=model, n_rag_queries=n_rag_queries)


# ============================================================
# INTAKE (Template A)
# ============================================================

INTAKE_TEMPLATE = {
    "topic": "",
    "decision_to_inform": "",
    "decision_owner": "",
    "audience": "Founder",          # Founder | Exec | Board | Operator | Investor
    "risk_tier": 2,                 # 1 | 2 | 3
    "freshness": "last_12m",        # timeless | last_12m | last_90d | last_30d | today
    "browsing": "allowed",          # allowed | not_allowed
    "output_writeback": True,
    "output_length": "extensive",   # standard | extensive
    "output_format_requirements": "",
    "scope_constraints": "",
    "must_include": [],
    "must_not": [],
    "success_criteria": [],
    "what_happens_if_wrong": "",
}


def create_intake(topic: str, **kwargs) -> Dict:
    """Create a filled intake from template."""
    intake = INTAKE_TEMPLATE.copy()
    intake["topic"] = topic
    intake.update(kwargs)
    return intake


# ============================================================
# STAGE 1: RESEARCH REPORT (Templates A-H)
# ============================================================

def load_standard(name: str) -> str:
    """Load a standard file."""
    path = STANDARDS / name
    if path.exists():
        return path.read_text()
    return ""


def load_context_package(topic: str) -> str:
    """Load ACP (Agent Context Package) for topic."""
    # Try topic-specific ACP first
    acp_path = RESEARCH_BASE / topic / "acp.md"
    if acp_path.exists():
        return acp_path.read_text()

    # Fallback: generate from CRT + corrections
    parts = []
    if CRT_PATH.exists():
        crt_data = json.loads(CRT_PATH.read_text())
        # Handle both flat list and {truths: [...]} format
        if isinstance(crt_data, dict):
            crts = crt_data.get("truths", [])
        elif isinstance(crt_data, list):
            crts = crt_data
        else:
            crts = []
        active = [c for c in crts if isinstance(c, dict) and c.get("status") == "active"]
        if active:
            parts.append(f"## Active CRTs ({len(active)} truths)")
            for c in active[:30]:
                parts.append(f"- {c['id']}: {c['claim']} [{c.get('confidence','?')}]")

    if CORRECTIONS_PATH.exists():
        corr_data = json.loads(CORRECTIONS_PATH.read_text())
        if isinstance(corr_data, dict):
            corrections = corr_data.get("corrections", [])
        elif isinstance(corr_data, list):
            corrections = corr_data
        else:
            corrections = []
        corrections = [c for c in corrections if isinstance(c, dict)]
        if corrections:
            parts.append(f"\n## Known Corrections ({len(corrections)})")
            for c in corrections:
                parts.append(f"- {c.get('id','?')}: {c.get('original','')} → {c.get('corrected','')}")

    return "\n".join(parts) if parts else ""


def _load_reference_library() -> str:
    """Load compact reference library for producer prompt."""
    ref_path = RESEARCH_BASE / "reference-library.json"
    if not ref_path.exists():
        return ""
    refs = json.loads(ref_path.read_text())
    lines = []
    for r in refs:
        tier = f"T{r['tier']}"
        caveat = f" ⚠ {r['caveat']}" if r.get('caveat') else ""
        lines.append(f"[{r['id']}] {r['title']} ({r['venue']}, {tier}): {r['key_finding']}{caveat}")
    return "\n".join(lines)


def build_producer_prompt(intake: Dict, context: str, dossier: str = "") -> str:
    """Build the Stage 1 Producer prompt. V2: compact, no refusals."""
    ref_library = _load_reference_library()

    # Compact dossier: only key findings, not full text
    compact_dossier = dossier[:6000] if dossier else ""

    prompt = f"""You are a research analyst writing an executive brief.

## TOPIC
{intake.get('topic', 'Unknown')}

## SCOPE
{intake.get('scope', 'Comprehensive analysis')}

## VERIFIED REFERENCES (use [S#] to cite these)
{ref_library}

## ADDITIONAL EVIDENCE (from web search + RAG)
{compact_dossier if compact_dossier else "None."}

## VERIFIED TRUTHS (do NOT contradict)
{context[:2000]}

## RULES
1. Cite EVERY claim with [S#] or mark as "author estimate"
2. Only Tier 1 (peer-reviewed, standards) and Tier 2 (arXiv, lab reports — flag as "preprint")
3. NO: landscape, tapestry, delve, synergy, cutting-edge, game-changer
4. Lead with something an expert DOESN'T already know
5. Honest: what works, what doesn't, what to combine
6. Include: Assumption Register, "Do Not Deploy If" section
7. LABEL EVERY SENTENCE with [E], [I], [J], or [A]:
   [E] Evidenced — peer-reviewed, primary data, cites [S#]
   [I] Interpreted — derived from evidence, explain logic
   [J] Judged — pattern recognition, state assumptions
   [A] Actionable — recommendation, reference supporting E/I/J, include "If wrong:"

## STRUCTURE
1. Beipackzettel (metadata table)
2. Executive Summary (SCR: Situation → Complication → Resolution)
3. Key Takeaways (5-7 bullets with [S#])
4. Main Analysis (3-5 sections, each: Finding → Evidence → Caveat → Implication)
5. Case Studies (2-3 real, sourced)
6. Appendix A: Source Log (every [S#] with title, venue, key finding)
7. Appendix B: Claim Ledger (12 claims, each with [S#], confidence, what would change it)

Write 3000-5000 words. Be direct. No filler.
"""
    return prompt


def build_reviewer_prompt(report: str) -> str:
    """Build the Stage 1 Reviewer prompt (canonical ERF v1)."""
    reviewer_prompt = load_standard("ERF-REVIEWER-PROMPT-v1.md")

    return f"""{reviewer_prompt}

## REPORT TO REVIEW

{report}

## REQUIRED OUTPUT FORMAT (JSON + text)
Return a JSON block with scores, then text sections for failures/claims/fixes.

```json
{{
  "scores": {{
    "decision_alignment": 0-2,
    "evidence_discipline": 0-2,
    "uncertainty_integrity": 0-2,
    "contradictions_handled": 0-2,
    "actionability": 0-2,
    "structure_compliance": 0-2,
    "failure_modes_realism": 0-2,
    "risk_mitigation": 0-2
  }},
  "total": X,
  "max": 16,
  "top_5_failures": [
    {{"location": "Section X", "issue": "...", "severity": "HIGH|MED|LOW"}}
  ],
  "fix_requests": [
    {{"section": "...", "instruction": "..."}}
  ],
  "blockers": []
}}
```

## REPORT TO REVIEW
{report}
"""


def stage1_produce(intake: Dict, dossier: str = "",
                   client: Optional[anthropic.Anthropic] = None) -> Dict[str, str]:
    """
    Stage 1: Produce research report + review.

    Returns:
        {"report": str, "review": json_str, "score": int}
    """
    if client is None:
        client = init_client()

    context = load_context_package(intake.get("topic", ""))

    # Step 1: Producer writes report
    print("[Stage 1.1] Producer writing report...")
    producer_prompt = build_producer_prompt(intake, context, dossier)
    report = llm_call(client, MODELS["stage1_producer"], producer_prompt, max_tokens=16000)

    # Step 2: Reviewer scores report
    print("[Stage 1.2] Reviewer scoring...")
    reviewer_prompt = build_reviewer_prompt(report)
    review = llm_call(client, MODELS["stage1_reviewer"], reviewer_prompt, max_tokens=2000)

    # Extract score
    score = 0
    try:
        review_json = json.loads(re.search(r'\{.*\}', review, re.DOTALL).group())
        score = review_json.get("total", 0)
    except Exception:
        review_json = {"error": "Could not parse review"}

    return {
        "report": report,
        "review": json.dumps(review_json, indent=2),
        "score": score,
    }


# ============================================================
# STAGE 2: ASSET BUILDER
# ============================================================

def build_asset_prompt(report: str) -> str:
    """Build the Stage 2 Asset Builder prompt (v2 — full system)."""
    # Load the professional Asset Builder system prompt + templates + schema
    system_prompt = load_standard("ASSET-BUILDER-SYSTEM-PROMPT.md")
    templates = load_standard("ASSET-BUILDER-TEMPLATES.md")
    rag_schema = load_standard("ASSET-BUILDER-RAG-SCHEMA.md")

    return f"""{system_prompt}

## ASSET TEMPLATES (use these exact structures)
{templates}

## RAG JSON SCHEMA (output must conform)
{rag_schema}

## REPORT TO CONVERT
{report}

## CONSTRAINTS
- Max 20 assets (fewer, higher-quality preferred)
- Target: Obsidian vault + RAG pipeline
- Audience: Founder + Researcher
- IDs: AB-[topicslug]-[TYPE]-[0001]
- Every asset: classification (Evidenced/Derived/Operational) + confidence + sources
- Dedupe aggressively
- Carry forward contradictions as "Known Conflicts"
- NO new facts beyond the report

## OUTPUT
1. Asset Index (counts + coverage map)
2. Atomic Notes
3. Playbooks (with Trigger/Goal/Inputs/Steps/Outputs/Failure modes/Mitigations/Acceptance criteria)
4. Templates (with When to use/Copy-paste block/Pitfalls)
5. Quality Checks (coverage, dedupe, traceability, actionability, JSON integrity)
6. RAG JSON array
"""


def stage2_assets(report: str,
                  client: Optional[anthropic.Anthropic] = None) -> str:
    """
    Stage 2: Build Asset Pack from report.

    Returns: Asset Pack markdown string.
    """
    if client is None:
        client = init_client()

    print("[Stage 2] Asset Builder extracting...")
    prompt = build_asset_prompt(report)
    return llm_call(client, MODELS["stage2_assets"], prompt, max_tokens=12000)


# ============================================================
# STAGE 3: KNOWLEDGE INTEGRATION
# ============================================================

def build_integration_prompt(report: str, assets: str,
                             existing_crts: str) -> str:
    """Build the Stage 3 Knowledge Integration prompt."""
    return f"""You are the Knowledge Integrator.

## TASK
Given a research report and its asset pack, produce:
1. CRT_UPDATES: New or updated Compounding Research Truths (JSON array)
2. VAULT_NOTES: Obsidian note suggestions (title + content + links)
3. CROSS_REFS: Entity links to existing vault content

## RULES
- New CRTs MUST have external source (no circular reasoning from own reports)
- Update existing CRTs if new evidence changes confidence
- Expire CRTs if contradicted by new evidence
- Each CRT: id, claim, source, confidence (High/Med/Low), category, expiry_date

## EXISTING CRTs
{existing_crts}

## REPORT
{report[:8000]}

## ASSET PACK
{assets[:4000]}

## OUTPUT FORMAT (JSON)
```json
{{
  "crt_updates": [
    {{
      "action": "add|update|expire",
      "id": "CT-XXX",
      "claim": "...",
      "source": "...",
      "confidence": "High|Med|Low",
      "category": "...",
      "reason": "why this update"
    }}
  ],
  "vault_notes": [
    {{
      "title": "...",
      "content": "...",
      "links": ["[[Related Note]]"]
    }}
  ],
  "cross_refs": [
    {{
      "entity": "...",
      "related_to": ["..."],
      "relationship": "supports|contradicts|extends"
    }}
  ]
}}
```
"""


def stage3_integrate(report: str, assets: str,
                     client: Optional[anthropic.Anthropic] = None) -> Dict:
    """
    Stage 3: Knowledge Integration.

    Returns: Dict with crt_updates, vault_notes, cross_refs.
    """
    if client is None:
        client = init_client()

    existing_crts = ""
    if CRT_PATH.exists():
        existing_crts = CRT_PATH.read_text()[:5000]

    print("[Stage 3] Knowledge Integration...")
    prompt = build_integration_prompt(report, assets, existing_crts)
    text = llm_call(client, MODELS["stage3_integrate"], prompt, max_tokens=4000)

    try:
        result = json.loads(re.search(r'\{.*\}', text, re.DOTALL).group())
    except Exception:
        result = {"raw": text, "error": "Could not parse integration output"}

    return result


# ============================================================
# HYPOTHESIS GENERATION
# ============================================================

def generate_hypotheses(intake: Dict, dossier: str = "", n: int = 5,
                        client: Optional[anthropic.Anthropic] = None) -> List[Dict]:
    """
    Generate N competing hypotheses from an intake + dossier.

    Each hypothesis is a focused claim that can be confirmed or refuted.
    At least 1 must be contrarian. At least 1 must be "null hypothesis" (status quo is fine).

    Returns: List of hypothesis dicts with id, claim, counter_claim, focus_areas
    """
    if client is None:
        client = init_client()

    context = load_context_package(intake.get("topic", ""))

    prompt = f"""You are a research architect. Generate exactly {n} competing hypotheses
for this research topic. These will each become a separate focused research report.

## RULES
1. Each hypothesis must be a TESTABLE claim (confirmable or refutable with evidence)
2. At least 1 must be CONTRARIAN (challenges conventional wisdom)
3. At least 1 must be the NULL HYPOTHESIS (status quo / "do nothing" is fine)
4. Hypotheses must be NON-OVERLAPPING (each covers different ground)
5. Each hypothesis must have a COUNTER-CLAIM (what the opposing view says)
6. Together they must COVER the full decision space for the intake question

## INTAKE
{json.dumps(intake, indent=2)}

## CONTEXT (existing knowledge — build on this, don't repeat it)
{context[:3000]}

## DOSSIER SUMMARY
{dossier[:5000] if dossier else "No dossier."}

## OUTPUT FORMAT (JSON array, exactly {n} items)
```json
[
  {{
    "id": "H1",
    "claim": "The testable hypothesis statement",
    "counter_claim": "What the opposing view argues",
    "type": "contrarian|null|exploratory|confirmatory",
    "focus_areas": ["area1", "area2"],
    "key_question": "The single question this report must answer",
    "expected_evidence": "What evidence would confirm this",
    "disconfirming_evidence": "What evidence would refute this"
  }}
]
```
Return ONLY the JSON array.
"""

    print(f"[Hypotheses] Generating {n} competing hypotheses...")
    resp_text = llm_call(client, MODELS["hypothesis_gen"], prompt, max_tokens=4000)
    try:
        hypotheses = json.loads(re.search(r'\[.*\]', resp_text, re.DOTALL).group())
    except Exception:
        print(f"[ERROR] Could not parse hypotheses. Raw output saved.")
        hypotheses = [{"id": f"H{i+1}", "claim": f"Hypothesis {i+1} (parse error)",
                       "raw": resp_text} for i in range(n)]

    for h in hypotheses:
        print(f"  {h['id']}: {h['claim']}")
        if h.get('type'):
            print(f"       Type: {h['type']}")

    return hypotheses


def hypothesis_to_intake(base_intake: Dict, hypothesis: Dict) -> Dict:
    """Convert a hypothesis into a focused intake for Stage 1."""
    focused = base_intake.copy()
    focused["topic"] = f"{base_intake['topic']} — {hypothesis['id']}: {hypothesis['claim']}"
    focused["hypothesis"] = hypothesis["claim"]
    focused["counter_claim"] = hypothesis.get("counter_claim", "")
    focused["success_criteria"] = [
        f"Confirm or refute: {hypothesis['claim']}",
        f"Address counter-claim: {hypothesis.get('counter_claim', 'N/A')}",
        f"Answer: {hypothesis.get('key_question', 'N/A')}",
        "Honest comparison: what's better, worse, what to combine",
        "If evidence is insufficient: say so explicitly",
    ]
    focused["must_include"] = hypothesis.get("focus_areas", [])
    focused["scope_constraints"] = f"Focus on hypothesis: {hypothesis['claim']}"
    return focused


# ============================================================
# SYNTHESIS (combines N reports + N asset packs → 1 master)
# ============================================================

def build_synthesis_prompt(hypotheses: List[Dict], reports: List[str],
                           assets: List[str], intake: Dict) -> str:
    """Build the synthesis prompt that combines N hypothesis reports."""

    h_summary = "\n".join(
        f"  {h['id']}: {h['claim']} (type: {h.get('type', '?')})"
        for h in hypotheses
    )

    # Truncate each report to fit context
    max_per_report = 12000
    report_blocks = "\n\n".join(
        f"### REPORT {h['id']}\n{r[:max_per_report]}"
        for h, r in zip(hypotheses, reports)
    )

    asset_blocks = "\n\n".join(
        f"### ASSETS {h['id']}\n{a[:4000]}"
        for h, a in zip(hypotheses, assets)
    )

    return f"""You are the Synthesis Judge in an Exec Research Factory.

## TASK
You have {len(hypotheses)} hypothesis reports, each investigating a different angle of the same topic.
Synthesize them into ONE master report + ONE master asset pack.

## HYPOTHESES TESTED
{h_summary}

## ORIGINAL INTAKE
{json.dumps(intake, indent=2)}

## SYNTHESIS RULES (NON-NEGOTIABLE)
1. HONEST VERDICT per hypothesis: Confirmed / Partially Confirmed / Refuted / Insufficient Evidence
2. COMPARATIVE TABLE: Which hypothesis had strongest evidence? Weakest? Most surprising?
3. Where hypotheses CONTRADICT: explain why, pick the better-evidenced position, note uncertainty
4. Where hypotheses AGREE: this is high-confidence knowledge (combine into single claim)
5. SIMPLICITY > COMPLEXITY: if a simple explanation covers the evidence, prefer it
6. The synthesis must answer the ORIGINAL intake question, not just summarize sub-reports
7. Include a "What We Still Don't Know" section (honest gaps)
8. NO LLM phrases: landscape, tapestry, delve, synergy, cutting-edge, game-changer
9. Every claim references the hypothesis report [H#] and original source [S#] where possible
10. Lead with the MOST SURPRISING finding, not the most expected one

## OUTPUT FORMAT
Write a FULL report in Template C format (Exec Research Factory standard):
- Beipackzettel
- Assumption Register
- Executive Summary (lead with surprise)
- Hypothesis Verdicts (table: H#, Claim, Verdict, Confidence, Key Evidence)
- Key Takeaways (standalone, from ACROSS all hypotheses)
- Detailed Findings (grouped by theme, not by hypothesis)
- Comparative Analysis (hypothesis vs hypothesis)
- What We Still Don't Know
- Recommendations
- Claim Ledger (merged, 15-25 claims, with formula-ready fields)
- Contradiction Register
- Source Log (merged, deduplicated)
- Reviewer Rubric (self-assessed)

Then write a MASTER ASSET PACK:
- Deduplicated across all 5 hypothesis asset packs
- Coverage map references all hypotheses
- Merged entities + relations

## REPORTS
{report_blocks}

## ASSET PACKS
{asset_blocks}
"""


def stage_synthesis(hypotheses: List[Dict], reports: List[str],
                    assets: List[str], intake: Dict,
                    client: Optional[anthropic.Anthropic] = None) -> Dict[str, str]:
    """
    Synthesis stage: Combine N hypothesis reports into master outputs.

    Returns: {"report": str, "assets": str}
    """
    if client is None:
        client = init_client()

    print(f"[Synthesis] Combining {len(reports)} hypothesis reports...")
    prompt = build_synthesis_prompt(hypotheses, reports, assets, intake)

    text = llm_call(client, MODELS["synthesis"], prompt, max_tokens=16000)

    # Split into report and assets if both are present
    # Look for "# Asset Pack" or "## Master Asset Pack" as separator
    asset_split = re.split(r'\n#+\s*(?:Master\s+)?Asset\s+Pack', text, maxsplit=1, flags=re.IGNORECASE)
    if len(asset_split) == 2:
        report = asset_split[0].rstrip()
        assets_text = "# Master Asset Pack" + asset_split[1]
    else:
        report = text
        assets_text = ""

    return {"report": report, "assets": assets_text}


# ============================================================
# FULL PIPELINE
# ============================================================

def run_pipeline(intake: Dict, dossier: str = "",
                 stages: str = "1,2,3",
                 output_dir: Optional[Path] = None) -> Dict:
    """
    Run the full Exec Research Factory pipeline.

    Args:
        intake: Filled Template A
        dossier: Optional research dossier text
        stages: Comma-separated stages to run ("1", "1,2", "1,2,3")
        output_dir: Where to write outputs

    Returns:
        Dict with all outputs + metadata
    """
    client = init_client()
    topic_slug = re.sub(r'[^a-z0-9]+', '-', intake["topic"].lower()).strip('-')
    stages_list = [int(s.strip()) for s in stages.split(",")]

    if output_dir is None:
        output_dir = RESEARCH_DIR / topic_slug
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    result = {
        "topic": intake["topic"],
        "topic_slug": topic_slug,
        "timestamp": datetime.now().isoformat(),
        "stages_run": stages_list,
    }

    # Save intake
    intake_path = output_dir / "intake.json"
    intake_path.write_text(json.dumps(intake, indent=2))
    print(f"[Intake] Saved to {intake_path}")

    # Stage 1: Research Report
    report = ""
    if 1 in stages_list:
        s1 = stage1_produce(intake, dossier, client)
        report = s1["report"]

        report_path = output_dir / "report.md"
        report_path.write_text(report)

        review_path = output_dir / "review.json"
        review_path.write_text(s1["review"])

        result["stage1"] = {
            "report_path": str(report_path),
            "review_path": str(review_path),
            "rubric_score": s1["score"],
            "report_length": len(report),
        }
        print(f"[Stage 1] Report: {report_path} ({len(report)} chars, score {s1['score']}/16)")

    # Load existing report if skipping stage 1
    if not report:
        existing = output_dir / "report.md"
        if existing.exists():
            report = existing.read_text()
        else:
            print("[ERROR] No report found. Run stage 1 first.")
            sys.exit(1)

    # Stage 2: Asset Pack
    assets = ""
    if 2 in stages_list:
        assets = stage2_assets(report, client)

        assets_path = output_dir / "assets.md"
        assets_path.write_text(assets)

        result["stage2"] = {
            "assets_path": str(assets_path),
            "assets_length": len(assets),
        }
        print(f"[Stage 2] Assets: {assets_path} ({len(assets)} chars)")

    # Load existing assets if skipping stage 2
    if not assets and 3 in stages_list:
        existing = output_dir / "assets.md"
        if existing.exists():
            assets = existing.read_text()

    # Stage 3: Knowledge Integration
    if 3 in stages_list:
        integration = stage3_integrate(report, assets, client)

        integration_path = output_dir / "integration.json"
        integration_path.write_text(json.dumps(integration, indent=2))

        n_crt = len(integration.get("crt_updates", []))
        n_notes = len(integration.get("vault_notes", []))
        n_refs = len(integration.get("cross_refs", []))

        result["stage3"] = {
            "integration_path": str(integration_path),
            "crt_updates": n_crt,
            "vault_notes": n_notes,
            "cross_refs": n_refs,
        }
        print(f"[Stage 3] Integration: {n_crt} CRT updates, {n_notes} vault notes, {n_refs} cross-refs")

    # Compute confidence if claim ledger exists
    claims_path = output_dir / "claims.json"
    if claims_path.exists():
        claims = load_claims_from_json(claims_path)
        conf = compute_report_confidence(claims)
        result["confidence"] = conf
        print(f"[Confidence] {conf['confidence_pct']}% ({conf['n_claims']} claims)")

    # Save pipeline result
    result_path = output_dir / "pipeline-result.json"
    result_path.write_text(json.dumps(result, indent=2))
    print(f"\n[Done] Pipeline result: {result_path}")

    return result


def generate_targeted_queries(contradictions: str, open_questions: str,
                              client: Optional[anthropic.Anthropic] = None) -> List[str]:
    """
    Generate targeted search queries from contradictions + open questions.
    Used between rounds to find NEW evidence the previous round didn't have.
    """
    if client is None:
        client = init_client()

    prompt = f"""Given these contradictions and open questions from a research round,
generate 5-8 targeted academic search queries to find NEW evidence.

Rules:
- Queries should find papers that RESOLVE contradictions (not confirm either side)
- Include cross-domain queries (adjacent fields that might have answers)
- Be specific enough to find relevant papers, broad enough to catch surprises
- At least 1 query must be from a DIFFERENT field than the main topic

## CONTRADICTIONS
{contradictions[:3000]}

## OPEN QUESTIONS
{open_questions[:2000]}

Return ONLY a JSON array of query strings.
"""
    resp_text = llm_call(client, MODELS["stage3_integrate"], prompt, max_tokens=1000)
    try:
        return json.loads(re.search(r'\[.*\]', resp_text, re.DOTALL).group())
    except Exception:
        return []


def run_prepare(topic: str, queries: Optional[List[str]] = None,
                max_papers: int = 30, output_dir: Optional[Path] = None) -> str:
    """
    Run prepare.py to build/update a research dossier.

    Args:
        topic: Search topic (broad for Round 0, ignored if queries given)
        queries: Targeted queries (for Re-Prepare rounds)
        max_papers: Max papers to fetch
        output_dir: Where to find/store dossier

    Returns: Dossier text
    """
    prepare_script = Path(__file__).parent / "prepare.py"
    if not prepare_script.exists():
        print(f"[WARN] prepare.py not found at {prepare_script}, skipping RAG")
        return ""

    import subprocess

    if queries:
        # Targeted mode: run prepare.py for each query, merge results
        all_dossier = []
        for q in queries[:8]:
            print(f"  [RAG] Searching: {q}")
            cmd = [sys.executable, str(prepare_script), q,
                   "--papers", str(max_papers // len(queries))]
            if output_dir:
                cmd.extend(["--output", str(output_dir)])
            try:
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
                if result.returncode == 0:
                    all_dossier.append(f"### Query: {q}\n{result.stdout[-2000:]}")
            except Exception as e:
                print(f"  [WARN] Query failed: {e}")
        return "\n\n".join(all_dossier)
    else:
        # Broad mode: single topic search
        print(f"  [RAG] Broad search: {topic}")
        cmd = [sys.executable, str(prepare_script), topic,
               "--papers", str(max_papers)]
        if output_dir:
            cmd.extend(["--output", str(output_dir)])
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            # Load dossier file if it was written
            dossier_path = (output_dir or RESEARCH_BASE / re.sub(r'[^a-z0-9]+', '-',
                           topic.lower()).strip('-')) / "DOSSIER.md"
            if dossier_path.exists():
                return dossier_path.read_text()
            return result.stdout[-5000:] if result.returncode == 0 else ""
        except Exception as e:
            print(f"  [WARN] Prepare failed: {e}")
            return ""


PAPERS_DIR = RESEARCH_BASE / "llm-trust-calibration" / "papers"

def _brave_fetch_and_store(url: str, title: str, snippet: str) -> Optional[str]:
    """Fetch a URL, summarize, store in research-base/papers/. Returns summary or None."""
    import urllib.request, hashlib

    # Skip non-research URLs
    skip = ["youtube.com", "twitter.com", "reddit.com", "linkedin.com", "facebook.com"]
    if any(s in url.lower() for s in skip):
        return None

    # Deduplicate by URL hash
    url_hash = hashlib.md5(url.encode()).hexdigest()[:10]
    slug = re.sub(r'[^a-z0-9]+', '-', title.lower().strip())[:60].strip('-')
    paper_path = PAPERS_DIR / f"web-{url_hash}-{slug}.md"

    if paper_path.exists():
        return paper_path.read_text()[:500]  # Already stored

    # Fetch content
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (research-bot)"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            raw = resp.read(50000).decode("utf-8", errors="ignore")
        # Strip HTML tags for a rough text extraction
        text = re.sub(r'<[^>]+>', ' ', raw)
        text = re.sub(r'\s+', ' ', text).strip()[:5000]
    except Exception:
        text = snippet  # Fallback to Brave snippet

    if len(text) < 100:
        return None

    # Store as markdown
    PAPERS_DIR.mkdir(parents=True, exist_ok=True)
    md = f"""---
title: "{title[:120]}"
url: "{url}"
fetched: "{datetime.now().strftime('%Y-%m-%d')}"
source: "brave-search"
tier: "{'tier1' if 'arxiv.org' in url or 'doi.org' in url else 'tier2' if any(d in url for d in ['springer', 'frontiers', 'ieee', 'acm', 'ncbi', 'pmc']) else 'tier3'}"
---

# {title}

**URL:** {url}
**Snippet:** {snippet}

## Content (auto-extracted)

{text[:3000]}
"""
    paper_path.write_text(md)
    return text[:500]


def web_search_brave(queries: List[str], max_results: int = 5) -> str:
    """Search the web via Brave Search API and return aggregated snippets."""
    import subprocess
    results = []
    for q in queries[:6]:
        try:
            # Use openclaw's built-in brave search via CLI
            cmd = [
                "node", "-e",
                f"""const https = require('https');
const key = process.env.BRAVE_API_KEY || '';
const q = {json.dumps(q)};
const url = `https://api.search.brave.com/res/v1/web/search?q=${{encodeURIComponent(q)}}&count={max_results}`;
https.get(url, {{headers: {{'X-Subscription-Token': key, 'Accept': 'application/json'}}}}, res => {{
  let d=''; res.on('data', c => d+=c); res.on('end', () => {{
    try {{
      const r = JSON.parse(d);
      (r.web?.results || []).forEach(w => console.log(`- ${{w.title}}: ${{w.description}} (${{w.url}})`));
    }} catch(e) {{ console.error(e); }}
  }});
}});"""
            ]
            r = subprocess.run(cmd, capture_output=True, text=True, timeout=15,
                             env={**os.environ})
            if r.stdout.strip():
                results.append(f"### {q}\n{r.stdout.strip()}")
        except Exception as e:
            print(f"  [WARN] Brave search failed for '{q[:40]}': {e}")

    if not results:
        # Fallback: use curl directly
        brave_key = os.environ.get("BRAVE_API_KEY", "")
        if not brave_key:
            # Try to get from openclaw config
            try:
                import subprocess as sp
                r = sp.run(["grep", "-r", "BRAVE", str(Path.home() / ".openclaw/openclaw.json")],
                          capture_output=True, text=True, timeout=5)
                # Extract key from config
                for line in r.stdout.split("\n"):
                    if "braveApiKey" in line or "BRAVE_API_KEY" in line:
                        brave_key = re.search(r'["\']([A-Za-z0-9_-]{20,})["\']', line)
                        if brave_key:
                            brave_key = brave_key.group(1)
                            break
            except Exception:
                pass

        if brave_key:
            import urllib.request, urllib.parse
            for q in queries[:6]:
                try:
                    url = f"https://api.search.brave.com/res/v1/web/search?q={urllib.parse.quote(q)}&count={max_results}"
                    req = urllib.request.Request(url, headers={
                        "X-Subscription-Token": brave_key,
                        "Accept": "application/json"
                    })
                    with urllib.request.urlopen(req, timeout=15) as resp:
                        data = json.loads(resp.read())
                        snippets = [f"- {w['title']}: {w.get('description','')} ({w['url']})"
                                   for w in data.get("web", {}).get("results", [])]
                        if snippets:
                            results.append(f"### {q}\n" + "\n".join(snippets))
                except Exception as e:
                    print(f"  [WARN] Brave fallback failed: {e}")

    return "\n\n".join(results) if results else ""


def web_enrich_dossier(topic: str, weak_claims: List[str] = None) -> str:
    """Use Brave Search to find web evidence, fetch top URLs, store in papers/."""
    if weak_claims:
        queries = [f"{topic} {claim[:60]} academic research" for claim in weak_claims[:3]]
        queries += [f"{topic} empirical evidence {claim[:40]}" for claim in weak_claims[:2]]
    else:
        queries = [
            f"{topic} peer-reviewed research 2024 2025",
            f"{topic} empirical study results",
            f"{topic} systematic review meta-analysis",
            f"{topic} benchmark evaluation",
        ]

    print(f"  [WEB] {len(queries)} Brave searches...")
    web_results = web_search_brave(queries)
    n_results = web_results.count(chr(10)) + 1 if web_results else 0

    # Fetch + store top URLs in research-base/papers/
    stored = 0
    if web_results:
        for line in web_results.split("\n"):
            m = re.search(r'\(([^)]+)\)\s*$', line)
            title_m = re.match(r'- (.+?):', line)
            if m and title_m:
                url = m.group(1)
                title = title_m.group(1)
                snippet = line[len(title_m.group(0)):].strip()
                snippet = re.sub(r'\s*\([^)]+\)\s*$', '', snippet)
                summary = _brave_fetch_and_store(url, title, snippet)
                if summary:
                    stored += 1
                if stored >= 5:  # Max 5 full fetches per iteration
                    break

    print(f"  [WEB] Found {n_results} results, stored {stored} papers")
    return web_results


def extract_contradictions_and_questions(reports: List[str],
                                          client: Optional[anthropic.Anthropic] = None) -> Dict:
    """
    Extract contradictions + open questions from a set of reports.
    Used to drive Re-Prepare between rounds.
    """
    if client is None:
        client = init_client()

    combined = "\n\n---\n\n".join(r[:5000] for r in reports)

    prompt = f"""Analyze these {len(reports)} research reports and extract:

1. CONTRADICTIONS: Where do the reports disagree? What claims conflict?
2. OPEN QUESTIONS: What important questions remain unanswered?
3. ANOMALIES: What findings are surprising or don't fit the overall pattern?

## REPORTS
{combined}

## OUTPUT FORMAT (JSON)
```json
{{
  "contradictions": [
    {{"claim_a": "...", "claim_b": "...", "why_they_differ": "...", "importance": "HIGH|MED|LOW"}}
  ],
  "open_questions": [
    {{"question": "...", "why_it_matters": "...", "what_would_answer_it": "..."}}
  ],
  "anomalies": [
    {{"finding": "...", "why_surprising": "...", "source_report": "H#"}}
  ]
}}
```
"""
    resp_text = llm_call(client, MODELS["stage1_reviewer"], prompt, max_tokens=3000)
    try:
        return json.loads(re.search(r'\{.*\}', resp_text, re.DOTALL).group())
    except Exception:
        return {"contradictions": [], "open_questions": [], "anomalies": [],
                "raw": resp_text}


def compute_claims_diff(prev_claims: List[Dict], curr_claims: List[Dict]) -> Dict:
    """
    Compute what changed between two rounds' claim ledgers.

    Returns: {added, removed, strengthened, weakened}
    """
    prev_texts = {c.get("text", c.get("claim", "")): c for c in prev_claims}
    curr_texts = {c.get("text", c.get("claim", "")): c for c in curr_claims}

    prev_set = set(prev_texts.keys())
    curr_set = set(curr_texts.keys())

    added = [curr_texts[t] for t in curr_set - prev_set]
    removed = [prev_texts[t] for t in prev_set - curr_set]

    # Check confidence changes for shared claims
    strengthened = []
    weakened = []
    for t in prev_set & curr_set:
        p_conf = prev_texts[t].get("confidence", "Med")
        c_conf = curr_texts[t].get("confidence", "Med")
        conf_order = {"Low": 0, "Med": 1, "High": 2}
        if conf_order.get(c_conf, 1) > conf_order.get(p_conf, 1):
            strengthened.append({"claim": t, "was": p_conf, "now": c_conf})
        elif conf_order.get(c_conf, 1) < conf_order.get(p_conf, 1):
            weakened.append({"claim": t, "was": p_conf, "now": c_conf})

    return {
        "added": len(added),
        "removed": len(removed),
        "strengthened": len(strengthened),
        "weakened": len(weakened),
        "details": {
            "added": added,
            "removed": removed,
            "strengthened": strengthened,
            "weakened": weakened,
        }
    }


def check_convergence(diffs: List[Dict], scores: List[List[int]]) -> Dict:
    """
    Check if the dialectic has converged (should we stop iterating?).

    Convergence criteria:
      - Claim Ledger delta < 10% (few new/removed claims)
      - No new HIGH-importance contradictions
      - Rubric scores plateaued (R_n ≈ R_n-1)
    """
    if len(diffs) < 2:
        return {"converged": False, "reason": "Need at least 2 rounds to check"}

    latest = diffs[-1]
    total_changes = latest["added"] + latest["removed"]
    total_claims = total_changes + latest["strengthened"] + latest["weakened"] + 10  # baseline

    change_rate = total_changes / max(total_claims, 1)

    # Score convergence
    score_converged = False
    if len(scores) >= 2:
        prev_avg = sum(scores[-2]) / max(len(scores[-2]), 1)
        curr_avg = sum(scores[-1]) / max(len(scores[-1]), 1)
        score_converged = abs(curr_avg - prev_avg) < 1.0

    converged = change_rate < 0.10 and score_converged

    return {
        "converged": converged,
        "change_rate": round(change_rate, 3),
        "score_converged": score_converged,
        "reason": "Low change rate + stable scores" if converged else "Still evolving",
    }


def run_dialectic_pipeline(intake: Dict, n_hypotheses: int = 5,
                           max_rounds: int = 3, output_dir: Optional[Path] = None) -> Dict:
    """
    Dialectic Pipeline: Iterative These → Antithese → Synthese with RAG at every step.

    Phase 0: PREPARE (broad) → Dossier₀
    Round 1: N Thesen → Reports + Assets → Contradictions
             RE-PREPARE (targeted on contradictions) → Dossier₁
    Round 2: Gegenthesen → Reports + Assets → Claims Diff
             RE-PREPARE (targeted on open questions) → Dossier₂
    Round 3: Synthese-Thesen → Reports + Assets
             CONVERGENCE CHECK
    Final:   Merged Assets + Synthesis Report + Evolution Trail
    """
    client = init_client()
    topic_slug = re.sub(r'[^a-z0-9]+', '-', intake["topic"].lower()).strip('-')

    if output_dir is None:
        output_dir = RESEARCH_DIR / topic_slug / "dialectic-run"
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    result = {
        "topic": intake["topic"],
        "timestamp": datetime.now().isoformat(),
        "mode": "dialectic-pipeline",
        "max_rounds": max_rounds,
        "rounds": [],
    }

    # Save intake
    (output_dir / "intake.json").write_text(json.dumps(intake, indent=2))

    # Phase 0: BROAD PREPARE
    print("=" * 60)
    print("[Phase 0] BROAD RAG PREPARATION")
    print("=" * 60)
    rag_dir = output_dir / "rag"
    rag_dir.mkdir(exist_ok=True)
    dossier = run_prepare(intake["topic"], max_papers=50, output_dir=rag_dir)
    (rag_dir / "dossier-r0.md").write_text(dossier) if dossier else None
    print(f"  Dossier: {len(dossier)} chars")

    all_round_scores = []
    all_diffs = []
    prev_claims = []
    all_reports_all_rounds = []
    all_assets_all_rounds = []
    all_hypotheses_all_rounds = []

    for round_num in range(1, max_rounds + 1):
        round_dir = output_dir / f"round-{round_num}"
        round_dir.mkdir(exist_ok=True)

        print(f"\n{'=' * 60}")
        print(f"[Round {round_num}] {'THESEN' if round_num == 1 else 'GEGENTHESEN' if round_num == 2 else 'SYNTHESE-THESEN'}")
        print(f"{'=' * 60}")

        # Determine N for this round (trichter: 5 → 3 → 2)
        n = max(2, n_hypotheses - (round_num - 1) * 1)
        if round_num > 1:
            n = min(n, 3)

        # Generate hypotheses
        if round_num == 1:
            hypotheses = generate_hypotheses(intake, dossier, n, client)
        else:
            # Gegenthesen: driven by contradictions from previous round
            prev_analysis = extract_contradictions_and_questions(
                all_reports_all_rounds[-n_hypotheses:], client)
            (round_dir / "analysis.json").write_text(json.dumps(prev_analysis, indent=2))

            contra_text = json.dumps(prev_analysis.get("contradictions", []))
            questions_text = json.dumps(prev_analysis.get("open_questions", []))

            # Modify intake to focus on contradictions
            counter_intake = intake.copy()
            counter_intake["scope_constraints"] = (
                f"Round {round_num}: Address these contradictions and open questions "
                f"from Round {round_num-1}. Generate COUNTER-theses that challenge "
                f"the strongest claims. Contradictions: {contra_text[:1000]}"
            )
            hypotheses = generate_hypotheses(counter_intake, dossier, n, client)

        (round_dir / "hypotheses.json").write_text(json.dumps(hypotheses, indent=2))
        all_hypotheses_all_rounds.extend(hypotheses)

        # Run Factory for each hypothesis
        round_reports = []
        round_assets = []
        round_scores = []

        for h in hypotheses:
            h_dir = round_dir / h["id"].lower()
            h_dir.mkdir(exist_ok=True)

            print(f"\n  [{h['id']}] {h['claim']}")

            h_intake = hypothesis_to_intake(intake, h)
            s1 = stage1_produce(h_intake, dossier, client)
            (h_dir / "report.md").write_text(s1["report"])
            (h_dir / "review.json").write_text(s1["review"])
            round_reports.append(s1["report"])
            round_scores.append(s1["score"])
            all_reports_all_rounds.append(s1["report"])

            assets = stage2_assets(s1["report"], client)
            (h_dir / "assets.md").write_text(assets)
            round_assets.append(assets)
            all_assets_all_rounds.append(assets)

            print(f"    Report: {len(s1['report'])} chars, score {s1['score']}/16")

        all_round_scores.append(round_scores)

        # Claims diff
        # (simplified: extract claim counts from reports since we don't have structured claims yet)
        round_result = {
            "round": round_num,
            "n_hypotheses": len(hypotheses),
            "scores": round_scores,
            "avg_score": sum(round_scores) / max(len(round_scores), 1),
        }

        # RE-PREPARE for next round (targeted)
        if round_num < max_rounds:
            print(f"\n  [RE-PREPARE] Targeted RAG for Round {round_num + 1}...")
            analysis = extract_contradictions_and_questions(round_reports, client)
            contra_text = json.dumps(analysis.get("contradictions", []))
            questions_text = json.dumps(analysis.get("open_questions", []))

            targeted_queries = generate_targeted_queries(contra_text, questions_text, client)
            if targeted_queries:
                print(f"  [RAG] {len(targeted_queries)} targeted queries")
                new_dossier = run_prepare(
                    intake["topic"], queries=targeted_queries,
                    max_papers=20, output_dir=rag_dir
                )
                if new_dossier:
                    dossier = dossier + "\n\n## ROUND {round_num} TARGETED FINDINGS\n" + new_dossier
                    (rag_dir / f"dossier-r{round_num}.md").write_text(new_dossier)
                    print(f"  Dossier updated: +{len(new_dossier)} chars")

            round_result["targeted_queries"] = targeted_queries
            round_result["new_papers"] = len(new_dossier) if new_dossier else 0

            # Convergence check
            if round_num >= 2:
                conv = check_convergence(all_diffs, all_round_scores)
                round_result["convergence"] = conv
                if conv["converged"]:
                    print(f"\n  [CONVERGED] {conv['reason']}")
                    result["rounds"].append(round_result)
                    break

        result["rounds"].append(round_result)

    # FINAL SYNTHESIS
    print(f"\n{'=' * 60}")
    print("[FINAL] SYNTHESIS")
    print(f"{'=' * 60}")

    synth = stage_synthesis(
        all_hypotheses_all_rounds,
        all_reports_all_rounds,
        all_assets_all_rounds,
        intake, client
    )

    (output_dir / "synthesis-report.md").write_text(synth["report"])
    if synth["assets"]:
        (output_dir / "synthesis-assets.md").write_text(synth["assets"])

    # Evolution trail
    evolution = {
        "total_rounds": len(result["rounds"]),
        "total_hypotheses": len(all_hypotheses_all_rounds),
        "total_reports": len(all_reports_all_rounds),
        "score_evolution": all_round_scores,
        "hypotheses_evolution": [
            {"id": h["id"], "claim": h["claim"], "type": h.get("type", "?")}
            for h in all_hypotheses_all_rounds
        ],
    }
    (output_dir / "evolution-trail.json").write_text(json.dumps(evolution, indent=2))

    result["synthesis"] = {
        "report_path": str(output_dir / "synthesis-report.md"),
        "report_length": len(synth["report"]),
    }
    result["evolution"] = evolution

    result_path = output_dir / "pipeline-result.json"
    result_path.write_text(json.dumps(result, indent=2))

    print(f"\n{'=' * 60}")
    print(f"[DONE] Dialectic Pipeline Complete")
    print(f"  Rounds: {len(result['rounds'])}")
    print(f"  Total hypotheses tested: {len(all_hypotheses_all_rounds)}")
    print(f"  Total reports: {len(all_reports_all_rounds)}")
    print(f"  Synthesis: {output_dir / 'synthesis-report.md'}")
    print(f"  Evolution: {output_dir / 'evolution-trail.json'}")
    print(f"{'=' * 60}")

    return result


def run_single_agent_pipeline(intake: Dict, max_rounds: int = 3,
                              output_dir: Optional[Path] = None) -> Dict:
    """
    Experiment B: Single deep agent, iterative with RAG after every stage.

    Instead of N parallel hypotheses, ONE agent goes deep:
      Round 1: PREPARE → Report → Assets → RE-PREPARE (on gaps)
      Round 2: Updated Report → Updated Assets → RE-PREPARE (on contradictions)
      Round 3: Final Report → Final Assets
      + Convergence check between rounds

    Same total compute, different architecture.
    Hypothesis: depth > breadth for well-defined topics.
    """
    client = init_client()
    topic_slug = re.sub(r'[^a-z0-9]+', '-', intake["topic"].lower()).strip('-')

    if output_dir is None:
        output_dir = RESEARCH_DIR / topic_slug / "single-agent-run"
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    result = {
        "topic": intake["topic"],
        "timestamp": datetime.now().isoformat(),
        "mode": "single-agent (experiment B)",
        "max_rounds": max_rounds,
        "rounds": [],
    }

    (output_dir / "intake.json").write_text(json.dumps(intake, indent=2))

    dossier = ""
    prev_report = ""
    prev_assets = ""
    all_scores = []

    for round_num in range(1, max_rounds + 1):
        round_dir = output_dir / f"round-{round_num}"
        round_dir.mkdir(exist_ok=True)

        print(f"\n{'=' * 60}")
        print(f"[Round {round_num}/{max_rounds}] Single Agent — Deep Iteration")
        print(f"{'=' * 60}")

        # PREPARE (every round)
        if round_num == 1:
            print(f"  [RAG] Broad preparation...")
            dossier = run_prepare(intake["topic"], max_papers=50,
                                  output_dir=round_dir)
            rag_queries = 1
        else:
            print(f"  [RAG] Targeted preparation (gaps from round {round_num-1})...")
            analysis = extract_contradictions_and_questions([prev_report], client)
            (round_dir / "gaps-analysis.json").write_text(json.dumps(analysis, indent=2))

            contra_text = json.dumps(analysis.get("contradictions", []))
            questions_text = json.dumps(analysis.get("open_questions", []))
            targeted_queries = generate_targeted_queries(contra_text, questions_text, client)

            if targeted_queries:
                new_dossier = run_prepare(intake["topic"], queries=targeted_queries,
                                          max_papers=15, output_dir=round_dir)
                if new_dossier:
                    dossier = dossier + f"\n\n## ROUND {round_num} NEW EVIDENCE\n" + new_dossier
                rag_queries = len(targeted_queries)
            else:
                rag_queries = 0

        # Enhance intake with previous round context
        round_intake = intake.copy()
        if prev_report:
            round_intake["scope_constraints"] = (
                f"Round {round_num}: This is an ITERATIVE improvement. "
                f"Your previous report had these issues (fix them):\n"
                f"Previous gaps: see analysis. Previous score: {all_scores[-1]}/16.\n"
                f"DO NOT start from scratch. IMPROVE the previous report.\n"
                f"New evidence is available in the dossier — USE IT."
            )
            round_intake["must_include"] = [
                "Address ALL gaps from previous round",
                "Integrate new RAG evidence",
                "Improve weakest claims",
            ]

        # Stage 1: Report
        bz = make_beipackzettel(
            output_id=f"R{round_num}-report",
            output_type="Research Report",
            topic=intake["topic"],
            stage="Stage 1: Report",
            round_num=round_num,
            parent_id=f"R{round_num-1}-report" if round_num > 1 else "intake",
            research_type="Expert Synthesis" if round_num == 1 else "Dialectic Synthesis",
            data_source="Secondary",
            model=MODELS["stage1_producer"],
            n_rag_queries=rag_queries,
        )

        # If iterating, include previous report for reference
        full_dossier = dossier
        if prev_report:
            full_dossier += f"\n\n## PREVIOUS REPORT (improve this, don't restart)\n{prev_report[:10000]}"

        s1 = stage1_produce(round_intake, full_dossier, client)
        report_with_bz = bz + "\n\n" + s1["report"]
        (round_dir / "report.md").write_text(report_with_bz)
        (round_dir / "review.json").write_text(s1["review"])
        all_scores.append(s1["score"])

        print(f"  Report: {len(s1['report'])} chars, score {s1['score']}/16")

        # Stage 2: Assets (with beipackzettel)
        assets = stage2_assets(s1["report"], client)
        assets_bz = make_beipackzettel(
            output_id=f"R{round_num}-assets",
            output_type="Asset Pack",
            topic=intake["topic"],
            stage="Stage 2: Assets",
            round_num=round_num,
            parent_id=f"R{round_num}-report",
            model=MODELS["stage2_assets"],
        )
        assets_with_bz = assets_bz + "\n\n" + assets
        (round_dir / "assets.md").write_text(assets_with_bz)

        print(f"  Assets: {len(assets)} chars")

        prev_report = s1["report"]
        prev_assets = assets

        round_result = {
            "round": round_num,
            "score": s1["score"],
            "report_length": len(s1["report"]),
            "assets_length": len(assets),
            "rag_queries": rag_queries,
        }

        # Convergence check (after round 2+)
        if round_num >= 2:
            score_delta = abs(all_scores[-1] - all_scores[-2])
            converged = score_delta < 1
            round_result["convergence"] = {
                "score_delta": score_delta,
                "converged": converged,
            }
            if converged:
                print(f"  [CONVERGED] Score delta {score_delta} < 1")
                result["rounds"].append(round_result)
                break

        result["rounds"].append(round_result)

    # Final Beipackzettel on synthesis
    final_bz = make_beipackzettel(
        output_id=f"final-report",
        output_type="Final Research Report",
        topic=intake["topic"],
        stage="Final",
        round_num=len(result["rounds"]),
        parent_id=f"R{len(result['rounds'])}-report",
        research_type="Dialectic Synthesis",
        data_source="Secondary",
        confidence=f"Rubric {all_scores[-1]}/16",
        model=MODELS["stage1_producer"],
        limitations="Single-agent iterative (Experiment B). No multi-hypothesis testing.",
    )

    # Copy final round as the definitive output
    final_report = final_bz + "\n\n" + prev_report
    (output_dir / "final-report.md").write_text(final_report)
    (output_dir / "final-assets.md").write_text(prev_assets)

    result["final"] = {
        "report_path": str(output_dir / "final-report.md"),
        "score_evolution": all_scores,
        "total_rounds": len(result["rounds"]),
    }

    result_path = output_dir / "pipeline-result.json"
    result_path.write_text(json.dumps(result, indent=2))

    print(f"\n{'=' * 60}")
    print(f"[DONE] Single Agent Pipeline (Experiment B)")
    print(f"  Rounds: {len(result['rounds'])}")
    print(f"  Score evolution: {' → '.join(str(s) for s in all_scores)}/16")
    print(f"  Final: {output_dir / 'final-report.md'}")
    print(f"{'=' * 60}")

    return result


def run_confidence_target_pipeline(intake: Dict, target_confidence: float = 0.90,
                                    max_iterations: int = 10,
                                    output_dir: Optional[Path] = None) -> Dict:
    """
    Confidence-Target Pipeline: Iterate until report hits target confidence.

    Each iteration:
      1. PREPARE (targeted on weak claims)
      2. Produce report
      3. Extract claims → compute confidence
      4. If confidence < target: identify weakest claims → RE-PREPARE → iterate
      5. If confidence >= target or max_iterations: stop

    Returns: Dict with all iterations + final confidence + comparison data
    """
    client = init_client()
    topic_slug = re.sub(r'[^a-z0-9]+', '-', intake["topic"].lower()).strip('-')

    if output_dir is None:
        output_dir = RESEARCH_DIR / topic_slug / "confidence-target-run"
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    result = {
        "topic": intake["topic"],
        "timestamp": datetime.now().isoformat(),
        "mode": "confidence-target",
        "target_confidence": target_confidence,
        "max_iterations": max_iterations,
        "iterations": [],
    }

    (output_dir / "intake.json").write_text(json.dumps(intake, indent=2))

    # Initial broad prepare
    print(f"{'=' * 60}")
    print(f"[CONFIDENCE TARGET] Target: {target_confidence:.0%} | Max iterations: {max_iterations}")
    print(f"{'=' * 60}")

    dossier = run_prepare(intake["topic"], max_papers=50, output_dir=output_dir)
    prev_report = ""
    prev_claims_data = []

    for iteration in range(1, max_iterations + 1):
        iter_dir = output_dir / f"iter-{iteration:02d}"
        iter_dir.mkdir(parents=True, exist_ok=True)

        print(f"\n{'=' * 60}")
        print(f"[Iteration {iteration}/{max_iterations}]")
        print(f"{'=' * 60}")

        # Enhance intake with previous iteration context
        iter_intake = intake.copy()
        if prev_report and prev_claims_data:
            weak_claims = sorted(prev_claims_data, key=lambda c: c.get("claim_confidence", 1.0))[:5]
            weak_text = "\n".join(f"- {c.get('text', c.get('claim',''))[:100]} (conf: {c.get('claim_confidence','?')})" for c in weak_claims)

            iter_intake["must_include"] = [
                "Strengthen or remove these weak claims:",
                weak_text,
                "Add stronger sources (Tier 1 preferred)",
                "Remove any claim that cannot be verified",
            ]
            iter_intake["scope_constraints"] = (
                f"Iteration {iteration}: Previous confidence was {prev_confidence:.1%}. "
                f"Target is {target_confidence:.0%}. Focus on strengthening evidence "
                f"for weak claims or removing unverifiable ones."
            )

        # RE-PREPARE (targeted on weak claims) if iteration > 1
        rag_queries_count = 0
        if iteration > 1 and prev_claims_data:
            weak_claims_text = json.dumps([c.get("text", "") for c in weak_claims[:3]])
            targeted_queries = generate_targeted_queries(
                weak_claims_text, "Strengthen evidence for these claims", client)
            if targeted_queries:
                rag_queries_count = len(targeted_queries)
                print(f"  [RAG] {rag_queries_count} targeted queries for weak claims")
                new_dossier = run_prepare(
                    intake["topic"], queries=targeted_queries,
                    max_papers=15, output_dir=iter_dir)
                if new_dossier:
                    dossier = dossier + f"\n\n## ITERATION {iteration} — NEW EVIDENCE\n" + new_dossier

        # Web enrichment (Brave Search) — every iteration
        weak_claim_texts = [c.get("text", "") for c in (prev_claims_data or [])
                           if c.get("claim_confidence", 1) < 0.5][:3]
        web_evidence = web_enrich_dossier(intake["topic"], weak_claim_texts or None)
        if web_evidence:
            dossier = dossier + f"\n\n## WEB EVIDENCE (Iteration {iteration})\n{web_evidence}"

        # Include previous report for iterative improvement (truncated to avoid prompt overflow)
        full_dossier = dossier[:12000] if len(dossier) > 12000 else dossier
        if prev_report:
            full_dossier += f"\n\n## PREVIOUS REPORT (improve, don't restart)\n{prev_report[:5000]}"

        # Stage 1: Report
        s1 = stage1_produce(iter_intake, full_dossier, client)
        report = s1["report"]

        bz = make_beipackzettel(
            output_id=f"iter-{iteration:02d}-report",
            output_type="Research Report",
            topic=intake["topic"],
            stage=f"Iteration {iteration}",
            round_num=iteration,
            parent_id=f"iter-{iteration-1:02d}-report" if iteration > 1 else "intake",
            research_type="Dialectic Synthesis",
            data_source="Secondary",
            model=MODELS["stage1_producer"],
            n_rag_queries=rag_queries_count,
        )
        (iter_dir / "report.md").write_text(bz + "\n\n" + report)
        (iter_dir / "review.json").write_text(s1["review"])

        print(f"  Report: {len(report)} chars, rubric {s1['score']}/16")

        # Extract claims and compute confidence
        claims_prompt = f"""You are a skeptical research auditor. Extract the 15-20 most important factual claims from this report.

For each claim, provide:
- text: the claim (verbatim)
- has_source: true/false (does it cite a specific source [S#] with URL or DOI?)
- source_quality: "tier1" (peer-reviewed with DOI), "tier2" (preprint/vendor with URL), "tier3" (blog/unknown), "none"
- verification: "verified" ONLY if a specific DOI or URL is cited AND you can confirm the claim matches the source. "partial" if a source is cited but you cannot verify the match. "unverifiable" if no specific source.
- admiralty: Admiralty rating. DEFAULTS:
  * No source at all → D4
  * Source cited but no DOI/URL → C3  
  * URL but no DOI → B2
  * DOI/peer-reviewed → A1 or A2
  * "Author estimate" or opinion → E2
  Most claims should be B2-C3. A1 is RARE (requires specific DOI).
- recency_year: year of the evidence (default 2024)
- weight: "load-bearing" (conclusion depends on this), "supporting", "contextual"

Be HARSH. If in doubt, rate lower. A report with all A1/verified is a red flag.
Extract EXACTLY 12 claims. Not more, not less. Pick the 12 most important ones.
Output as JSON array only, no explanation.

REPORT:
{report[:15000]}"""

        claims_text = llm_call(client, MODELS["stage1_reviewer"], claims_prompt, max_tokens=4000)
        try:
            claims_data = json.loads(re.search(r'\[.*\]', claims_text, re.DOTALL).group())
        except Exception:
            claims_data = []

        (iter_dir / "claims.json").write_text(json.dumps(claims_data, indent=2))

        # Compute confidence using AgentTrust-enhanced formula
        # Three signals: SOURCE (50%) + CONSISTENCY (30%) + STRUCTURAL (20%)
        computed_claims = []
        for c in claims_data:
            adm = c.get("admiralty", "C3")
            ver = c.get("verification", "partial")
            rec = c.get("recency_year", 2024)
            wgt = c.get("weight", "supporting")
            text = c.get("text", "")

            # Signal 1: SOURCE (Admiralty × Verification × Recency)
            source_q = ADMIRALTY_SCORES.get(adm, 0.4)
            ver_score = VERIFICATION_SCORES.get(ver, 0.3)
            recency = max(0.5, 1.0 - (datetime.now().year - rec) * 0.1)
            source_signal = source_q * ver_score * recency

            # Signal 2: CONSISTENCY (Budget-CoCoA proxy)
            # Without 3x LLM calls, we approximate from evaluator metadata:
            # - "verified" = high consistency (evaluator confident) → 0.85
            # - "partial" = medium → 0.60
            # - "unverifiable" = low → 0.30
            consistency_map = {"verified": 0.85, "partial": 0.60, "unverifiable": 0.30}
            consistency_signal = consistency_map.get(ver, 0.40)

            # Signal 3: STRUCTURAL (deterministic checks on the claim text)
            structural = 0.0
            if re.search(r'10\.\d{4,}/', text):  # DOI pattern
                structural += 0.3
            elif re.search(r'https?://', text):   # URL
                structural += 0.15
            if re.search(r'\d{1,3}(\.\d+)?%', text):  # Specific percentage
                structural += 0.1
            if re.search(r'(19|20)\d{2}', text):      # Specific year
                structural += 0.05
            if c.get("has_source"):
                structural += 0.1
            structural = min(structural, 0.5)  # Cap at 0.5

            # Combined: 50% source + 30% consistency + 20% structural
            claim_conf = 0.5 * source_signal + 0.3 * consistency_signal + 0.2 * structural
            claim_weight = WEIGHT_SCORES.get(wgt, 0.5)

            computed_claims.append({
                "text": text,
                "claim_confidence": round(claim_conf, 4),
                "weight": wgt,
                "claim_weight": claim_weight,
                "factors": {
                    "source": round(source_signal, 4),
                    "consistency": round(consistency_signal, 4),
                    "structural": round(structural, 4),
                    "admiralty": adm, "verification": ver,
                },
            })

        # Overall confidence
        if computed_claims:
            weighted_sum = sum(c["claim_confidence"] * c["claim_weight"] for c in computed_claims)
            weight_sum = sum(c["claim_weight"] for c in computed_claims)
            confidence = weighted_sum / weight_sum if weight_sum > 0 else 0
        else:
            confidence = 0

        prev_confidence = confidence
        prev_report = report
        prev_claims_data = computed_claims

        # Stage 2: Assets
        assets = stage2_assets(report, client)
        (iter_dir / "assets.md").write_text(assets)

        iter_result = {
            "iteration": iteration,
            "rubric_score": s1["score"],
            "report_length": len(report),
            "n_claims": len(computed_claims),
            "confidence": round(confidence, 4),
            "confidence_pct": round(confidence * 100, 1),
            "rag_queries": rag_queries_count,
            "weakest_3": sorted(computed_claims, key=lambda c: c["claim_confidence"])[:3],
        }
        result["iterations"].append(iter_result)

        print(f"  Confidence: {confidence:.1%} ({len(computed_claims)} claims)")
        print(f"  Weakest: {', '.join(c['text'][:50] for c in iter_result['weakest_3'])}")

        # Check if we hit target
        if confidence >= target_confidence:
            print(f"\n  [TARGET HIT] {confidence:.1%} >= {target_confidence:.0%}")
            break

        # Plateau detection: stop if delta < 2% between iterations
        if iteration >= 2:
            prev_conf = result["iterations"][-2]["confidence"]
            delta = abs(confidence - prev_conf)
            if delta < 0.02:
                print(f"\n  [PLATEAU] Delta {delta:.1%} < 2%. Stopping.")
                break

        if iteration < max_iterations:
            gap = target_confidence - confidence
            print(f"  [GAP] {gap:.1%} to target. Iterating...")

    # Final output with AgentTrust Beipackzettel
    # Extract sources, uncertainties, risks from claims
    final_sources = list(set(
        c.get("text", "")[:80] + f" [{c['factors']['admiralty']}/{c['factors']['verification']}]"
        for c in prev_claims_data if c["factors"]["verification"] != "unverifiable"
    ))
    final_uncertainties = [
        c["text"][:80] for c in prev_claims_data
        if c["factors"]["verification"] == "unverifiable"
    ]
    final_risks = [
        f"Claim '{c['text'][:50]}...' has low confidence ({c['claim_confidence']:.0%})"
        for c in sorted(prev_claims_data, key=lambda x: x["claim_confidence"])[:3]
    ]
    final_not_checked = [
        c["text"][:80] for c in prev_claims_data
        if c["factors"]["admiralty"] in ("D4", "E2")
    ]

    final_bz = make_beipackzettel(
        output_id=f"final-{intake['topic'][:30]}",
        output_type="Research Report (Confidence Target Pipeline)",
        topic=intake["topic"],
        stage=f"Final (after {len(result['iterations'])} iterations)",
        round_num=len(result["iterations"]),
        research_type="Dialectic Synthesis",
        data_source="Mixed (RAG + Web + LLM)",
        confidence=confidence * 100,
        sources=final_sources,
        uncertainties=final_uncertainties,
        risks=final_risks,
        not_checked=final_not_checked,
        n_rag_queries=sum(i.get("rag_queries", 0) for i in result["iterations"]),
        model=f"{MODELS['stage1_producer']} (producer) + {MODELS['stage1_reviewer']} (evaluator)",
    )

    # Also save as JSON (compatible with agenttrust.Beipackzettel.to_dict)
    bpz_json = beipackzettel_to_json(
        final_bz, output_id=f"final-{intake['topic'][:30]}",
        confidence=confidence * 100, sources=final_sources,
        uncertainties=final_uncertainties, risks=final_risks,
        not_checked=final_not_checked,
        model=f"{MODELS['stage1_producer']}+{MODELS['stage1_reviewer']}",
    )
    (output_dir / "beipackzettel.json").write_text(json.dumps(bpz_json, indent=2))

    final_report = final_bz + "\n\n" + prev_report
    (output_dir / "final-report.md").write_text(final_report)
    (output_dir / "final-assets.md").write_text(assets)

    # Confidence evolution
    conf_evolution = [i["confidence_pct"] for i in result["iterations"]]
    result["final"] = {
        "confidence": round(confidence, 4),
        "confidence_pct": round(confidence * 100, 1),
        "target_hit": confidence >= target_confidence,
        "iterations_used": len(result["iterations"]),
        "confidence_evolution": conf_evolution,
        "report_path": str(output_dir / "final-report.md"),
    }

    result_path = output_dir / "pipeline-result.json"
    result_path.write_text(json.dumps(result, indent=2))

    print(f"\n{'=' * 60}")
    print(f"[DONE] Confidence Target Pipeline")
    print(f"  Target: {target_confidence:.0%} | Achieved: {confidence:.1%}")
    print(f"  Iterations: {len(result['iterations'])}/{max_iterations}")
    print(f"  Evolution: {' → '.join(f'{c:.1f}%' for c in conf_evolution)}")
    print(f"  Final: {output_dir / 'final-report.md'}")
    print(f"{'=' * 60}")

    return result


def run_hypothesis_pipeline(intake: Dict, dossier: str = "",
                            n_hypotheses: int = 5,
                            output_dir: Optional[Path] = None) -> Dict:
    """
    Hypothesis Pipeline: Phase 0 → Phase 1 (N× Factory) → Phase 2 (Synthesis)

    This is the v7 architecture:
      1. Generate N competing hypotheses from intake
      2. Run Stage 1 + Stage 2 for EACH hypothesis (parallel-ready)
      3. Synthesize all N reports + assets into 1 master output

    Args:
        intake: Filled Template A
        dossier: Research dossier text (from prepare.py)
        n_hypotheses: Number of hypotheses (default 5)
        output_dir: Where to write outputs

    Returns:
        Dict with all outputs + comparison metrics
    """
    client = init_client()
    topic_slug = re.sub(r'[^a-z0-9]+', '-', intake["topic"].lower()).strip('-')

    if output_dir is None:
        output_dir = RESEARCH_DIR / topic_slug / "hypothesis-run"
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    result = {
        "topic": intake["topic"],
        "topic_slug": topic_slug,
        "timestamp": datetime.now().isoformat(),
        "mode": "hypothesis-pipeline",
        "n_hypotheses": n_hypotheses,
    }

    # Save intake
    (output_dir / "intake.json").write_text(json.dumps(intake, indent=2))

    # Phase 0: Generate hypotheses
    hypotheses = generate_hypotheses(intake, dossier, n_hypotheses, client)
    (output_dir / "hypotheses.json").write_text(json.dumps(hypotheses, indent=2))
    result["hypotheses"] = [{"id": h["id"], "claim": h["claim"],
                             "type": h.get("type", "?")} for h in hypotheses]

    # Phase 1: Run Factory for each hypothesis
    all_reports = []
    all_assets = []
    all_scores = []

    for i, h in enumerate(hypotheses):
        h_dir = output_dir / h["id"].lower()
        h_dir.mkdir(exist_ok=True)

        print(f"\n{'='*60}")
        print(f"[{h['id']}] {h['claim']}")
        print(f"{'='*60}")

        # Create focused intake
        h_intake = hypothesis_to_intake(intake, h)
        (h_dir / "intake.json").write_text(json.dumps(h_intake, indent=2))

        # Stage 1: Report
        s1 = stage1_produce(h_intake, dossier, client)
        (h_dir / "report.md").write_text(s1["report"])
        (h_dir / "review.json").write_text(s1["review"])
        all_reports.append(s1["report"])
        all_scores.append(s1["score"])

        print(f"  Report: {len(s1['report'])} chars, score {s1['score']}/16")

        # Stage 2: Assets
        assets = stage2_assets(s1["report"], client)
        (h_dir / "assets.md").write_text(assets)
        all_assets.append(assets)

        print(f"  Assets: {len(assets)} chars")

    result["hypothesis_scores"] = {
        h["id"]: score for h, score in zip(hypotheses, all_scores)
    }
    avg_score = sum(all_scores) / len(all_scores) if all_scores else 0
    print(f"\n[Phase 1 Done] Avg rubric score: {avg_score:.1f}/16")

    # Phase 2: Synthesis
    print(f"\n{'='*60}")
    print("[Phase 2] SYNTHESIS")
    print(f"{'='*60}")

    synth = stage_synthesis(hypotheses, all_reports, all_assets, intake, client)

    (output_dir / "synthesis-report.md").write_text(synth["report"])
    if synth["assets"]:
        (output_dir / "synthesis-assets.md").write_text(synth["assets"])

    result["synthesis"] = {
        "report_path": str(output_dir / "synthesis-report.md"),
        "report_length": len(synth["report"]),
        "assets_length": len(synth.get("assets", "")),
    }

    # Save pipeline result
    result_path = output_dir / "pipeline-result.json"
    result_path.write_text(json.dumps(result, indent=2))

    print(f"\n{'='*60}")
    print(f"[DONE] Hypothesis Pipeline Complete")
    print(f"  Hypotheses: {n_hypotheses}")
    print(f"  Reports: {len(all_reports)}")
    print(f"  Avg Score: {avg_score:.1f}/16")
    print(f"  Synthesis: {output_dir / 'synthesis-report.md'}")
    print(f"  Result: {result_path}")
    print(f"{'='*60}")

    return result


# ============================================================
# CLI
# ============================================================

def print_agenda():
    """Print the research agenda (hardcoded + open slots)."""
    print("=" * 60)
    print("EXEC RESEARCH FACTORY — RESEARCH AGENDA")
    print("=" * 60)
    print()
    print("HARDCODED TOPICS (refreshed on schedule):")
    print("-" * 50)
    for t in HARDCODED_TOPICS:
        status = t["status"].upper()
        refs = ", ".join(t["cross_refs"])
        print(f"  [{t['report_id']}] {t['name']}")
        print(f"         Status: {status} | Refresh: {t['refresh']}")
        print(f"         CRT Pool: {t['crt_pool']} | Cross-refs: {refs}")
        if t.get("note"):
            print(f"         Note: {t['note']}")
        print()

    print(f"OPEN SLOTS: {OPEN_SLOTS} available")
    print("  Use --intake to fill a slot with a new topic.")
    print()


def print_confidence(path: str):
    """Compute and print confidence from claims JSON."""
    claims = load_claims_from_json(Path(path))
    result = compute_report_confidence(claims)

    print(f"\nREPORT CONFIDENCE: {result['confidence_pct']}%")
    print(f"Claims: {result['n_claims']}")
    print(f"Formula: sum(claim_conf * weight) / sum(weight)")
    print()

    if result["weakest"]:
        print("WEAKEST CLAIMS (address these to raise confidence):")
        for w in result["weakest"]:
            f = w["factors"]
            print(f"  {w['id']}: {w['text']}")
            print(f"    Confidence: {w['confidence']:.1%} | Weight: {w['weight']}")
            print(f"    Source: {f['source_quality']} | Verified: {f['verification']} | "
                  f"Consensus: {f['consensus']} | Recency: {f['recency']}")
            print()


def main():
    parser = argparse.ArgumentParser(
        description="Exec Research Factory — 3-Stage Pipeline",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --agenda                          # Show research agenda
  %(prog)s --confidence claims.json          # Compute confidence
  %(prog)s --topic "Trust Calibration"       # Full pipeline
  %(prog)s --topic "X" --stage 2 --input r.md  # Asset Builder only
        """,
    )
    parser.add_argument("--topic", help="Research topic")
    parser.add_argument("--intake", help="Path to intake JSON file")
    parser.add_argument("--stage", help="Run specific stage(s): 1, 2, 3, or 1,2,3")
    parser.add_argument("--input", help="Input file (report.md for stage 2/3)")
    parser.add_argument("--dossier", help="Path to research dossier")
    parser.add_argument("--output", help="Output directory")
    parser.add_argument("--hypotheses", type=int, metavar="N",
                        help="Run hypothesis pipeline with N competing hypotheses (v7 mode)")
    parser.add_argument("--dialectic", type=int, metavar="N",
                        help="Run dialectic pipeline: N theses × 3 rounds with RAG between rounds")
    parser.add_argument("--single-agent", action="store_true",
                        help="Experiment B: single deep agent, iterative with RAG after every stage")
    parser.add_argument("--confidence-target", type=float, metavar="PCT",
                        help="Iterate until confidence >= PCT (e.g. 0.90 for 90%%). Max iterations via --max-rounds")
    parser.add_argument("--max-rounds", type=int, default=3,
                        help="Max rounds for dialectic/single-agent mode (default 3)")
    parser.add_argument("--agenda", action="store_true", help="Print research agenda")
    parser.add_argument("--confidence", help="Compute confidence from claims JSON")

    args = parser.parse_args()

    if args.agenda:
        print_agenda()
        return

    if args.confidence:
        print_confidence(args.confidence)
        return

    if not args.topic:
        parser.print_help()
        return

    # Build intake
    if args.intake:
        with open(args.intake) as f:
            intake = json.load(f)
    else:
        intake = create_intake(args.topic)

    # Load dossier if provided
    dossier = ""
    if args.dossier:
        dossier = Path(args.dossier).read_text()

    # Output directory
    output_dir = Path(args.output) if args.output else None

    # Confidence-target pipeline
    if args.confidence_target:
        run_confidence_target_pipeline(intake, args.confidence_target, args.max_rounds, output_dir)
        return

    # Dialectic pipeline (multi-agent)
    if args.dialectic:
        run_dialectic_pipeline(intake, args.dialectic, args.max_rounds, output_dir)
        return

    # Single-agent pipeline (Experiment B)
    if args.single_agent:
        run_single_agent_pipeline(intake, args.max_rounds, output_dir)
        return

    # Hypothesis pipeline (v7 mode)
    if args.hypotheses:
        run_hypothesis_pipeline(intake, dossier, args.hypotheses, output_dir)
        return

    # Standard pipeline
    stages = args.stage or "1,2,3"
    run_pipeline(intake, dossier, stages, output_dir)


if __name__ == "__main__":
    main()
