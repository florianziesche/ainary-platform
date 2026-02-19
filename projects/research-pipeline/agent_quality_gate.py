#!/usr/bin/env python3
"""
Research Report Quality Gate — Stage 2 (Multi-Agent)
4 LLM stages, each with Beipackzettel.
Usage: python3 agent_quality_gate.py <report.md> [--stage 1-4|all] [--audience expert|ceo|student]
Requires: ANTHROPIC_API_KEY and/or OPENAI_API_KEY
"""

import argparse
import hashlib
import json
import os
import re
import sys
import time
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional


# === BEIPACKZETTEL ===

@dataclass
class Beipackzettel:
    agent: str
    model: str
    timestamp: str
    report_file: str
    input_hash: str
    verdict: str
    confidence: float
    cost_usd: float
    duration_seconds: float
    checks: dict = field(default_factory=dict)
    issues: list = field(default_factory=list)
    recommendation: str = ""

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


# === SYSTEM PROMPTS ===

FACT_CHECKER_PROMPT = """You are a fact-checker for research reports. Your ONLY job is to verify:
1. Do cited papers actually exist? Check: Is the title plausible? Is the year reasonable?
2. Do quantitative claims match their cited sources?
3. Are there claims presented as fact without any source?

For each claim you check, respond with a JSON array of objects:
[{"claim_text": "...", "source_cited": "...", "verdict": "VERIFIED|UNVERIFIABLE|SUSPICIOUS|NO_SOURCE", "reason": "..."}]

Be STRICT. If you cannot verify a claim, mark it UNVERIFIABLE, not VERIFIED.
Do NOT hallucinate verification. If unsure, say unsure.
Return ONLY valid JSON."""

INSIGHT_JUDGE_PROMPT = """You are an expert judge evaluating research report insights.
Audience: {audience}

For each section's key finding, classify as:
- NOVEL: An expert would learn something new
- SYNTHESIS: Combines known facts in a new way
- KNOWN: Any expert already knows this
- OBVIOUS: Even a non-expert knows this

Respond with JSON:
{{"sections": [{{"section": "...", "opener": "...", "rating": "NOVEL|SYNTHESIS|KNOWN|OBVIOUS", "reason": "..."}}],
  "executive_summary_opener_rating": "...",
  "executive_summary_opener_text": "...",
  "executive_summary_recommendation": "...",
  "novel_count": 0, "synthesis_count": 0, "known_count": 0, "obvious_count": 0}}

Be BRUTAL. "RLHF makes models overconfident" is KNOWN for experts.
"BaseCal recovers 42.9% ECE by projecting RLHF hidden states back to base model space" is NOVEL.
Return ONLY valid JSON."""

ADVERSARIAL_REVIEWER_PROMPT = """You are an adversarial peer reviewer. Your job is to DESTROY this report.
Find every:
- Logical fallacy or non-sequitur
- Claim contradicting another claim in the report
- Missing important counterargument
- Survivorship bias or cherry-picked evidence
- Conclusions not supported by evidence
- Recommendations without sufficient justification

Respond with JSON:
{{"weaknesses": [{{"severity": "CRITICAL|MAJOR|MINOR", "section": "...", "description": "...", "suggestion": "..."}}],
  "critical_count": 0, "major_count": 0, "minor_count": 0}}

If you find ZERO weaknesses, your review is REJECTED. Every report has weaknesses.
Return ONLY valid JSON."""

READABILITY_AUDITOR_PROMPT = """You are a readability auditor. Evaluate for audience: {audience}

Respond with JSON:
{{"exec_summary_clear": true/false,
  "jargon_unexplained": [{{"term": "...", "first_use_context": "..."}}],
  "section_balance": "...",
  "actionability_score": 1-5,
  "actionability_note": "...",
  "overall_assessment": "..."}}

Return ONLY valid JSON."""


# === DETERMINISTIC READABILITY METRICS ===

def compute_readability(text: str) -> dict[str, Any]:
    """Compute deterministic readability metrics."""
    sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip() and len(s.strip()) > 5]
    words = text.split()
    paragraphs = [p for p in text.split("\n\n") if p.strip()]

    total_words = len(words)
    total_sentences = max(len(sentences), 1)
    total_syllables = sum(_count_syllables(w) for w in words)

    avg_sentence_len = total_words / total_sentences
    avg_word_len = sum(len(w) for w in words) / max(total_words, 1)

    # Flesch Reading Ease
    flesch = 206.835 - 1.015 * avg_sentence_len - 84.6 * (total_syllables / max(total_words, 1))
    # Flesch-Kincaid Grade Level
    grade = 0.39 * avg_sentence_len + 11.8 * (total_syllables / max(total_words, 1)) - 15.59

    return {
        "total_words": total_words,
        "total_sentences": total_sentences,
        "total_paragraphs": len(paragraphs),
        "avg_sentence_length": round(avg_sentence_len, 1),
        "avg_word_length": round(avg_word_len, 1),
        "flesch_reading_ease": round(flesch, 1),
        "flesch_kincaid_grade": round(grade, 1),
    }


def _count_syllables(word: str) -> int:
    """Rough syllable count."""
    word = word.lower().strip(".,!?;:'\"()-")
    if not word:
        return 1
    count = 0
    vowels = "aeiouy"
    prev_vowel = False
    for ch in word:
        is_vowel = ch in vowels
        if is_vowel and not prev_vowel:
            count += 1
        prev_vowel = is_vowel
    if word.endswith("e") and count > 1:
        count -= 1
    return max(count, 1)


# === API CALLS ===

def call_anthropic(system: str, user: str, model: str = "claude-haiku-4-5-20250514") -> tuple[str, float]:
    """Call Anthropic API. Returns (response_text, cost_usd)."""
    try:
        import anthropic
    except ImportError:
        raise RuntimeError("anthropic package not installed")

    key = os.environ.get("ANTHROPIC_API_KEY")
    if not key:
        raise RuntimeError("ANTHROPIC_API_KEY not set")

    client = anthropic.Anthropic(api_key=key)
    response = client.messages.create(
        model=model,
        max_tokens=4096,
        system=system,
        messages=[{"role": "user", "content": user}],
    )

    text = response.content[0].text
    input_tokens = response.usage.input_tokens
    output_tokens = response.usage.output_tokens

    # Pricing (approximate, Feb 2026)
    prices = {
        "claude-haiku-4-5-20250514": (0.80 / 1e6, 4.0 / 1e6),
        "claude-sonnet-4-20250514": (3.0 / 1e6, 15.0 / 1e6),
    }
    ip, op = prices.get(model, (1.0 / 1e6, 5.0 / 1e6))
    cost = input_tokens * ip + output_tokens * op

    return text, cost


def parse_json_response(text: str) -> Any:
    """Extract JSON from LLM response, handling markdown code blocks."""
    text = text.strip()
    # Try to extract from code block
    m = re.search(r'```(?:json)?\s*\n?(.*?)\n?```', text, re.DOTALL)
    if m:
        text = m.group(1).strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        # Try to find first { or [
        for i, ch in enumerate(text):
            if ch in ('{', '['):
                try:
                    return json.loads(text[i:])
                except json.JSONDecodeError:
                    continue
        return {"error": "Failed to parse JSON", "raw": text[:500]}


# === STAGES ===

def stage_fact_checker(report_text: str, report_path: str, input_hash: str) -> Beipackzettel:
    """Stage 1: Fact Checker (Haiku)."""
    print("🔍 Stage 1: Fact Checker (Haiku)...")
    model = "claude-haiku-4-5-20250514"
    start = time.time()

    # Extract claims with numbers/dates
    claims_text = "Check ALL factual claims in this research report. Focus on:\n"
    claims_text += "1. Cited papers and their existence\n2. Quantitative claims\n3. Unsourced claims\n\n"
    claims_text += "REPORT:\n" + report_text[:12000]  # Token budget

    try:
        response, cost = call_anthropic(FACT_CHECKER_PROMPT, claims_text, model)
        data = parse_json_response(response)
    except Exception as e:
        print(f"  ⚠️  Error: {e}")
        return Beipackzettel(
            agent="fact_checker", model=model,
            timestamp=datetime.now(timezone.utc).isoformat(),
            report_file=report_path, input_hash=input_hash,
            verdict="ERROR", confidence=0.0, cost_usd=0.0,
            duration_seconds=time.time() - start,
            recommendation=f"Error: {e}"
        )

    duration = time.time() - start

    if isinstance(data, list):
        claims = data
    elif isinstance(data, dict) and "error" not in data:
        claims = data.get("claims", data.get("results", [data]))
    else:
        claims = []

    verified = sum(1 for c in claims if c.get("verdict") == "VERIFIED")
    unverifiable = sum(1 for c in claims if c.get("verdict") == "UNVERIFIABLE")
    suspicious = sum(1 for c in claims if c.get("verdict") == "SUSPICIOUS")
    no_source = sum(1 for c in claims if c.get("verdict") == "NO_SOURCE")
    total = len(claims)
    pct = (verified / total * 100) if total > 0 else 0

    verdict = "PASS" if pct >= 80 else ("REVISE" if pct >= 60 else "FAIL")

    issues = []
    for c in claims:
        if c.get("verdict") in ("SUSPICIOUS", "NO_SOURCE"):
            issues.append({
                "severity": "MAJOR" if c.get("verdict") == "SUSPICIOUS" else "MINOR",
                "line": 0,
                "description": f"{c.get('verdict')}: {c.get('claim_text', '')[:100]}"
            })

    print(f"  ✅ Done: {verified}/{total} verified ({pct:.0f}%), cost ${cost:.4f}")

    return Beipackzettel(
        agent="fact_checker", model=model,
        timestamp=datetime.now(timezone.utc).isoformat(),
        report_file=report_path, input_hash=input_hash,
        verdict=verdict, confidence=pct / 100,
        cost_usd=cost, duration_seconds=duration,
        checks={"claims_total": total, "verified": verified,
                "unverifiable": unverifiable, "suspicious": suspicious, "no_source": no_source,
                "pct_verified": round(pct, 1)},
        issues=issues,
        recommendation=f"{verified}/{total} claims verified ({pct:.0f}%)"
    )


def stage_insight_judge(report_text: str, report_path: str, input_hash: str, audience: str) -> Beipackzettel:
    """Stage 2: Insight Judge (Sonnet)."""
    print("💡 Stage 2: Insight Judge (Sonnet)...")
    model = "claude-sonnet-4-20250514"
    start = time.time()
    prompt = INSIGHT_JUDGE_PROMPT.format(audience=audience)

    try:
        response, cost = call_anthropic(prompt, "REPORT:\n" + report_text[:15000], model)
        data = parse_json_response(response)
    except Exception as e:
        print(f"  ⚠️  Error: {e}")
        return Beipackzettel(
            agent="insight_judge", model=model,
            timestamp=datetime.now(timezone.utc).isoformat(),
            report_file=report_path, input_hash=input_hash,
            verdict="ERROR", confidence=0.0, cost_usd=0.0,
            duration_seconds=time.time() - start,
            recommendation=f"Error: {e}"
        )

    duration = time.time() - start

    novel = data.get("novel_count", 0)
    synthesis = data.get("synthesis_count", 0)
    known = data.get("known_count", 0)
    obvious = data.get("obvious_count", 0)
    exec_rating = data.get("executive_summary_opener_rating", "UNKNOWN")

    thresholds = {"expert": 5, "ceo": 3, "student": 1}
    needed = thresholds.get(audience, 3)
    verdict = "PASS" if (novel + synthesis) >= needed else "CONDITIONAL"
    if exec_rating in ("KNOWN", "OBVIOUS"):
        verdict = "CONDITIONAL"

    print(f"  ✅ Done: {novel} novel, {synthesis} synthesis, {known} known. Cost ${cost:.4f}")

    return Beipackzettel(
        agent="insight_judge", model=model,
        timestamp=datetime.now(timezone.utc).isoformat(),
        report_file=report_path, input_hash=input_hash,
        verdict=verdict, confidence=0.7,
        cost_usd=cost, duration_seconds=duration,
        checks={"novel": novel, "synthesis": synthesis, "known": known, "obvious": obvious,
                "exec_summary_opener_rating": exec_rating,
                "exec_summary_opener_text": data.get("executive_summary_opener_text", ""),
                "sections": data.get("sections", [])},
        issues=[{"severity": "MAJOR", "line": 0,
                 "description": f"Executive Summary opener rated {exec_rating}"}] if exec_rating in ("KNOWN", "OBVIOUS") else [],
        recommendation=data.get("executive_summary_recommendation", "")
    )


def stage_adversarial_reviewer(report_text: str, report_path: str, input_hash: str) -> Beipackzettel:
    """Stage 3: Adversarial Reviewer (Sonnet)."""
    print("⚔️  Stage 3: Adversarial Reviewer (Sonnet)...")
    model = "claude-sonnet-4-20250514"
    start = time.time()

    try:
        response, cost = call_anthropic(ADVERSARIAL_REVIEWER_PROMPT, "REPORT:\n" + report_text[:15000], model)
        data = parse_json_response(response)
    except Exception as e:
        print(f"  ⚠️  Error: {e}")
        return Beipackzettel(
            agent="adversarial_reviewer", model=model,
            timestamp=datetime.now(timezone.utc).isoformat(),
            report_file=report_path, input_hash=input_hash,
            verdict="ERROR", confidence=0.0, cost_usd=0.0,
            duration_seconds=time.time() - start,
            recommendation=f"Error: {e}"
        )

    duration = time.time() - start

    critical = data.get("critical_count", 0)
    major = data.get("major_count", 0)
    minor = data.get("minor_count", 0)
    weaknesses = data.get("weaknesses", [])

    if critical > 0:
        verdict = "FAIL"
    elif major > 0:
        verdict = "REVISE"
    else:
        verdict = "PASS"

    issues = [{"severity": w.get("severity", "MINOR"), "line": 0,
               "description": w.get("description", "")} for w in weaknesses]

    top_issue = weaknesses[0].get("description", "") if weaknesses else "None"
    print(f"  ✅ Done: {critical} critical, {major} major, {minor} minor. Cost ${cost:.4f}")

    return Beipackzettel(
        agent="adversarial_reviewer", model=model,
        timestamp=datetime.now(timezone.utc).isoformat(),
        report_file=report_path, input_hash=input_hash,
        verdict=verdict, confidence=0.75,
        cost_usd=cost, duration_seconds=duration,
        checks={"critical": critical, "major": major, "minor": minor,
                "weaknesses": weaknesses, "top_issue": top_issue},
        issues=issues,
        recommendation=f"{critical} critical, {major} major, {minor} minor issues"
    )


def stage_readability_auditor(report_text: str, report_path: str, input_hash: str, audience: str) -> Beipackzettel:
    """Stage 4: Readability Auditor (Haiku + deterministic)."""
    print("📖 Stage 4: Readability Auditor (Haiku)...")
    model = "claude-haiku-4-5-20250514"
    start = time.time()

    # Deterministic metrics first
    metrics = compute_readability(report_text)
    prompt = READABILITY_AUDITOR_PROMPT.format(audience=audience)

    try:
        response, cost = call_anthropic(prompt, "REPORT:\n" + report_text[:12000], model)
        data = parse_json_response(response)
    except Exception as e:
        print(f"  ⚠️  Error: {e}")
        data = {}
        cost = 0.0

    duration = time.time() - start

    jargon = data.get("jargon_unexplained", [])
    actionability = data.get("actionability_score", 3)

    verdict = "PASS"
    issues = []
    if len(jargon) > 5:
        issues.append({"severity": "MAJOR", "line": 0, "description": f"{len(jargon)} jargon terms unexplained"})
        verdict = "REVISE"

    checks = {**metrics, "jargon_unexplained": jargon,
              "actionability_score": actionability,
              "llm_assessment": data.get("overall_assessment", "")}

    print(f"  ✅ Done: Flesch {metrics['flesch_reading_ease']}, avg sentence {metrics['avg_sentence_length']} words. Cost ${cost:.4f}")

    return Beipackzettel(
        agent="readability_auditor", model=model,
        timestamp=datetime.now(timezone.utc).isoformat(),
        report_file=report_path, input_hash=input_hash,
        verdict=verdict, confidence=0.8,
        cost_usd=cost, duration_seconds=duration,
        checks=checks, issues=issues,
        recommendation=f"Flesch {metrics['flesch_reading_ease']}, Grade {metrics['flesch_kincaid_grade']}"
    )


# === GATE LOGIC ===

def final_verdict(beipackzettel_list: list[Beipackzettel]) -> dict[str, Any]:
    """Compute aggregated verdict from all stages."""
    has_critical = any(
        any(i.get("severity") == "CRITICAL" for i in b.issues)
        for b in beipackzettel_list
    )
    has_fail = any(b.verdict == "FAIL" for b in beipackzettel_list)
    has_revise = any(b.verdict == "REVISE" for b in beipackzettel_list)
    has_conditional = any(b.verdict == "CONDITIONAL" for b in beipackzettel_list)

    if has_critical or has_fail:
        verdict = "FAIL"
    elif has_revise:
        verdict = "REVISE"
    elif has_conditional:
        verdict = "CONDITIONAL"
    else:
        verdict = "PASS"

    total_cost = sum(b.cost_usd for b in beipackzettel_list)
    total_time = sum(b.duration_seconds for b in beipackzettel_list)

    return {
        "verdict": verdict,
        "total_cost_usd": round(total_cost, 4),
        "total_time_seconds": round(total_time, 1),
        "stages": [b.to_dict() for b in beipackzettel_list],
    }


def write_qa_report(result: dict[str, Any], report_path: str) -> tuple[Path, Path]:
    """Write QA report as JSON and Markdown."""
    qa_dir = Path(report_path).parent / "qa"
    qa_dir.mkdir(exist_ok=True)

    stem = Path(report_path).stem
    json_path = qa_dir / f"{stem}-qa.json"
    md_path = qa_dir / f"{stem}-qa.md"

    json_path.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")

    # Markdown
    verdict_icon = {"PASS": "✅", "FAIL": "❌", "REVISE": "⚠️", "CONDITIONAL": "⚠️", "ERROR": "💥"}
    v = result["verdict"]
    md = f"# Quality Assurance Report: {stem}\n\n"
    md += f"## Verdict: {verdict_icon.get(v, '?')} {v}\n\n"

    stage_names = {
        "fact_checker": "Fact Checker (Haiku)",
        "insight_judge": "Insight Judge (Sonnet)",
        "adversarial_reviewer": "Adversarial Reviewer (Sonnet)",
        "readability_auditor": "Readability Auditor (Haiku)",
    }

    for s in result["stages"]:
        name = stage_names.get(s["agent"], s["agent"])
        sv = s["verdict"]
        md += f"### Stage: {name}\n"
        md += f"- **Verdict:** {verdict_icon.get(sv, '?')} {sv}\n"
        md += f"- **Cost:** ${s['cost_usd']:.4f}\n"
        md += f"- **Duration:** {s['duration_seconds']:.1f}s\n"

        checks = s.get("checks", {})
        if s["agent"] == "fact_checker":
            md += f"- **Claims checked:** {checks.get('claims_total', '?')}\n"
            md += f"- **Verified:** {checks.get('verified', '?')} | **Unverifiable:** {checks.get('unverifiable', '?')} | **Suspicious:** {checks.get('suspicious', '?')}\n"
        elif s["agent"] == "insight_judge":
            md += f"- **Novel:** {checks.get('novel', '?')} | **Synthesis:** {checks.get('synthesis', '?')} | **Known:** {checks.get('known', '?')}\n"
            md += f"- **Executive Summary opener:** {checks.get('exec_summary_opener_rating', '?')} — \"{checks.get('exec_summary_opener_text', '')[:80]}\"\n"
        elif s["agent"] == "adversarial_reviewer":
            md += f"- **Critical:** {checks.get('critical', '?')} | **Major:** {checks.get('major', '?')} | **Minor:** {checks.get('minor', '?')}\n"
            md += f"- **Top issue:** {checks.get('top_issue', 'None')[:100]}\n"
        elif s["agent"] == "readability_auditor":
            md += f"- **Flesch Score:** {checks.get('flesch_reading_ease', '?')}\n"
            md += f"- **Avg sentence length:** {checks.get('avg_sentence_length', '?')} words\n"
            md += f"- **Jargon unexplained:** {len(checks.get('jargon_unexplained', []))} terms\n"

        if s.get("recommendation"):
            md += f"- **Recommendation:** {s['recommendation']}\n"
        md += "\n"

    md += f"### Total QA Cost: ${result['total_cost_usd']:.4f}\n"
    md += f"### Total QA Time: {result['total_time_seconds']:.1f} seconds\n\n"
    md += "### Aggregated Beipackzettel\n```json\n"
    md += json.dumps(result["stages"], indent=2, ensure_ascii=False)
    md += "\n```\n"

    md_path.write_text(md, encoding="utf-8")
    return json_path, md_path


# === MAIN ===

def main() -> None:
    """CLI entry point."""
    parser = argparse.ArgumentParser(description="Research Report Quality Gate — Stage 2 (Multi-Agent)")
    parser.add_argument("report", help="Path to report file (.md)")
    parser.add_argument("--stage", default="all", help="Stage to run: 1-4 or 'all'")
    parser.add_argument("--audience", default="expert", choices=["expert", "ceo", "student"])
    args = parser.parse_args()

    path = Path(args.report)
    if not path.exists():
        print(f"ERROR: File not found: {args.report}", file=sys.stderr)
        sys.exit(1)

    content = path.read_text(encoding="utf-8", errors="replace")
    # Strip HTML tags for analysis if HTML
    if path.suffix.lower() in (".html", ".htm"):
        text = re.sub(r'<[^>]+>', ' ', content)
        text = re.sub(r'\s+', ' ', text)
    else:
        text = content

    input_hash = hashlib.sha256(content.encode()).hexdigest()[:16]
    report_path = str(path)

    stages_to_run: list[int] = []
    if args.stage == "all":
        stages_to_run = [1, 2, 3, 4]
    else:
        stages_to_run = [int(args.stage)]

    print(f"\n🚀 Quality Gate Stage 2 — {path.name}")
    print(f"   Audience: {args.audience} | Stages: {stages_to_run}\n")

    results: list[Beipackzettel] = []

    stage_funcs = {
        1: lambda: stage_fact_checker(text, report_path, input_hash),
        2: lambda: stage_insight_judge(text, report_path, input_hash, args.audience),
        3: lambda: stage_adversarial_reviewer(text, report_path, input_hash),
        4: lambda: stage_readability_auditor(text, report_path, input_hash, args.audience),
    }

    for s in stages_to_run:
        if s in stage_funcs:
            results.append(stage_funcs[s]())

    combined = final_verdict(results)
    json_path, md_path = write_qa_report(combined, report_path)

    print(f"\n{'='*50}")
    print(f"📋 VERDICT: {combined['verdict']}")
    print(f"💰 Total cost: ${combined['total_cost_usd']:.4f}")
    print(f"⏱️  Total time: {combined['total_time_seconds']:.1f}s")
    print(f"📁 JSON: {json_path}")
    print(f"📁 MD:   {md_path}")

    if combined["verdict"] == "FAIL":
        sys.exit(1)
    elif combined["verdict"] in ("REVISE", "CONDITIONAL"):
        sys.exit(2)
    sys.exit(0)


if __name__ == "__main__":
    main()
