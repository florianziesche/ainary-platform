#!/usr/bin/env python3
"""
Research Quality Measurement System (v1.0)

4-level measurement for research reports:
  Level 1: Deterministic (automated, $0, <1s)
  Level 2: LLM Evaluator (automated, ~$0.50, <60s)
  Level 3: Human Evaluation (manual, prompts + stores)
  Level 4: Source Verification (automated, ~$0.10, <120s)

Usage:
    # Full measurement (all 4 levels, Level 3 = prompts for human input)
    python3 measure.py report.md --full

    # Deterministic only (free, instant)
    python3 measure.py report.md --level 1

    # Compare two reports
    python3 measure.py report_a.md report_b.md --compare

    # Measure all reports in a directory
    python3 measure.py experiments/runs/ --batch

    # Show correlation matrix (after enough data)
    python3 measure.py --correlations

All measurements stored in measurements.jsonl (append-only, never overwritten).
One line per measurement. Enables longitudinal analysis.
"""

import argparse
import hashlib
import json
import os
import re
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any
from urllib.parse import urlparse

# --- Paths ---
WORKSPACE = Path(os.path.expanduser("~/.openclaw/workspace"))
MEASUREMENTS_FILE = WORKSPACE / "research" / "experiments" / "measurements.jsonl"

# --- LLM Phrases (banned) ---
LLM_PHRASES = [
    "landscape", "tapestry", "delve", "synergy", "cutting-edge",
    "game-changer", "it's worth noting", "in today's world",
    "revolutionize", "paradigm shift", "holistic", "leverage",
    "best-in-class", "robust", "scalable", "innovative",
    "state-of-the-art", "groundbreaking", "transformative",
]

# --- Required Sections ---
REQUIRED_SECTIONS = [
    "beipackzettel", "executive summary", "key takeaway",
    "methodology", "finding", "recommendation",
]

OPTIONAL_SECTIONS = [
    "assumption register", "claim ledger", "contradiction register",
    "source log", "reviewer rubric", "asset",
]


# ============================================================
# LEVEL 1: DETERMINISTIC METRICS ($0, <1s)
# ============================================================

def measure_level1(text: str, filepath: str = "") -> Dict[str, Any]:
    """
    Deterministic quality metrics. No LLM needed.

    Returns dict with all Level 1 metrics.
    """
    lines = text.split("\n")
    words = text.split()
    lower = text.lower()

    # --- Basic stats ---
    word_count = len(words)
    line_count = len(lines)
    char_count = len(text)

    # --- Structure ---
    headings = [l for l in lines if l.startswith("#")]
    h1_count = sum(1 for h in headings if h.startswith("# ") and not h.startswith("## "))
    h2_count = sum(1 for h in headings if h.startswith("## ") and not h.startswith("### "))
    h3_count = sum(1 for h in headings if h.startswith("### "))

    # --- Required sections present ---
    sections_found = {}
    for section in REQUIRED_SECTIONS:
        sections_found[section] = section in lower
    required_present = sum(sections_found.values())
    required_total = len(REQUIRED_SECTIONS)

    optional_found = {}
    for section in OPTIONAL_SECTIONS:
        optional_found[section] = section in lower
    optional_present = sum(optional_found.values())

    # --- Citations ---
    # [S1], [S2], [1], [2], etc.
    citation_refs = re.findall(r'\[S?\d+\]', text)
    unique_citations = len(set(citation_refs))
    total_citations = len(citation_refs)
    citation_density = total_citations / max(word_count / 1000, 1)  # per 1000 words

    # --- Source URLs ---
    urls = re.findall(r'https?://[^\s\)]+', text)
    unique_urls = len(set(urls))

    # --- LLM phrases ---
    llm_phrases_found = []
    for phrase in LLM_PHRASES:
        count = lower.count(phrase)
        if count > 0:
            llm_phrases_found.append({"phrase": phrase, "count": count})
    llm_phrase_count = sum(p["count"] for p in llm_phrases_found)

    # --- Confidence markers ---
    confidence_pattern = r'confidence[:\s]+(\d{1,3})\s*%'
    confidence_matches = re.findall(confidence_pattern, lower)
    has_confidence = len(confidence_matches) > 0
    confidence_values = [int(c) for c in confidence_matches]

    # --- Hedging language (good — shows uncertainty awareness) ---
    hedges = ["may ", "might ", "could ", "approximately", "estimated",
              "uncertain", "caveat", "limitation", "unclear", "unverified",
              "author estimate"]
    hedge_count = sum(lower.count(h) for h in hedges)

    # --- Beipackzettel ---
    has_beipackzettel = "beipackzettel" in lower
    has_assumption_register = "assumption register" in lower or "assumption" in lower
    has_claim_ledger = "claim ledger" in lower
    has_contradiction_register = "contradiction register" in lower or "contradiction" in lower
    has_source_log = "source log" in lower

    # --- Finding/Evidence/Caveat/Implication pattern ---
    finding_count = lower.count("**finding")
    evidence_count = lower.count("**evidence")
    caveat_count = lower.count("**caveat")
    implication_count = lower.count("**implication")
    feci_completeness = min(finding_count, evidence_count, caveat_count, implication_count)

    # --- Claims without sources ---
    # Simple heuristic: sentences with numbers but no [S#] reference
    sentences = re.split(r'[.!?]\s', text)
    claims_with_numbers = [s for s in sentences if re.search(r'\d+\.?\d*%|\$\d+|\d+\.\d+', s)]
    claims_without_source = [s for s in claims_with_numbers
                             if not re.search(r'\[S?\d+\]', s)]
    unsourced_claim_rate = (len(claims_without_source) / max(len(claims_with_numbers), 1))

    # --- Encoding issues ---
    apple_chars = len(re.findall(r'[\uf000-\uf8ff]', text))  # Private Use Area
    non_ascii_issues = len(re.findall(r'[^\x00-\x7f\xc0-\xff\u00a0-\u024f\u2000-\u206f\u2190-\u21ff\u2200-\u22ff\u2500-\u257f]', text))

    # --- Composite score (0-100) ---
    score = 0
    score += min(required_present / required_total * 30, 30)  # Structure: 30pts
    score += min(citation_density / 5 * 20, 20)               # Citations: 20pts
    score += max(0, 15 - llm_phrase_count * 3)                 # LLM phrases: 15pts (penalty)
    score += min(feci_completeness / 3 * 15, 15)               # FECI pattern: 15pts
    score += (10 if has_beipackzettel else 0)                  # Beipackzettel: 10pts
    score += max(0, 10 - unsourced_claim_rate * 20)            # Sourced claims: 10pts

    return {
        "level": 1,
        "timestamp": datetime.now().isoformat(),
        "filepath": filepath,
        "file_hash": hashlib.md5(text.encode()).hexdigest()[:12],

        # Basic stats
        "word_count": word_count,
        "line_count": line_count,
        "char_count": char_count,
        "heading_count": len(headings),

        # Structure
        "required_sections_present": required_present,
        "required_sections_total": required_total,
        "optional_sections_present": optional_present,
        "sections_found": sections_found,
        "has_beipackzettel": has_beipackzettel,
        "has_assumption_register": has_assumption_register,
        "has_claim_ledger": has_claim_ledger,
        "has_contradiction_register": has_contradiction_register,
        "has_source_log": has_source_log,

        # Citations
        "unique_citations": unique_citations,
        "total_citation_refs": total_citations,
        "citation_density_per_1k": round(citation_density, 1),
        "unique_urls": unique_urls,

        # Quality signals
        "llm_phrase_count": llm_phrase_count,
        "llm_phrases_found": llm_phrases_found,
        "unsourced_claim_rate": round(unsourced_claim_rate, 3),
        "hedge_count": hedge_count,
        "has_confidence": has_confidence,
        "confidence_values": confidence_values,

        # FECI pattern
        "feci_finding_count": finding_count,
        "feci_evidence_count": evidence_count,
        "feci_caveat_count": caveat_count,
        "feci_implication_count": implication_count,
        "feci_completeness": feci_completeness,

        # Encoding
        "apple_char_count": apple_chars,
        "encoding_issues": non_ascii_issues,

        # Composite
        "l1_score": round(score, 1),
    }


# ============================================================
# LEVEL 2: LLM EVALUATOR (~$0.50, <60s)
# ============================================================

def measure_level2(text: str, client=None) -> Dict[str, Any]:
    """
    LLM-based evaluation. Uses fixed evaluator prompt.
    Requires ANTHROPIC_API_KEY.
    """
    try:
        import anthropic
        if client is None:
            client = anthropic.Anthropic()
    except Exception as e:
        return {"level": 2, "error": f"No API access: {e}"}

    from experiment_runner import evaluate_report, EVALUATOR_MODEL

    result = evaluate_report(text, client)
    result["level"] = 2
    result["timestamp"] = datetime.now().isoformat()
    result["evaluator_model"] = EVALUATOR_MODEL
    return result


# ============================================================
# LEVEL 3: HUMAN EVALUATION (manual)
# ============================================================

def measure_level3_prompt(filepath: str) -> Dict[str, Any]:
    """
    Generate human evaluation prompt. Returns template to fill.
    """
    return {
        "level": 3,
        "timestamp": datetime.now().isoformat(),
        "filepath": filepath,
        "status": "PENDING",
        "questions": {
            "would_send_to_friedl": {
                "question": "Wuerdest du diesen Report an Prof. Friedl senden?",
                "type": "bool",
                "value": None,
            },
            "learned_something_new": {
                "question": "Hast du etwas NEUES gelernt?",
                "type": "bool",
                "value": None,
                "follow_up": "Was?",
                "follow_up_value": None,
            },
            "trust_numbers": {
                "question": "Vertraust du den Zahlen? (1-5)",
                "type": "int",
                "range": [1, 5],
                "value": None,
            },
            "can_decide": {
                "question": "Kannst du basierend auf diesem Report eine Entscheidung treffen?",
                "type": "bool",
                "value": None,
            },
            "seconds_to_first_error": {
                "question": "Lesezeit bis zum ersten Fehler (Sekunden, 0 = kein Fehler gefunden)",
                "type": "int",
                "value": None,
            },
            "overall_grade": {
                "question": "Gesamtnote (1-10, 10 = publishable)",
                "type": "int",
                "range": [1, 10],
                "value": None,
            },
            "notes": {
                "question": "Freitext-Notizen",
                "type": "str",
                "value": None,
            },
        },
    }


def collect_level3_interactive(filepath: str) -> Dict[str, Any]:
    """Collect human evaluation interactively via CLI."""
    template = measure_level3_prompt(filepath)

    print(f"\n{'=' * 50}")
    print(f"HUMAN EVALUATION: {filepath}")
    print(f"{'=' * 50}\n")

    for key, q in template["questions"].items():
        answer = input(f"  {q['question']}: ").strip()

        if q["type"] == "bool":
            q["value"] = answer.lower() in ("ja", "yes", "y", "true", "1")
        elif q["type"] == "int":
            try:
                q["value"] = int(answer)
            except ValueError:
                q["value"] = 0
        else:
            q["value"] = answer

        if q.get("follow_up") and q["value"]:
            follow = input(f"    {q['follow_up']}: ").strip()
            q["follow_up_value"] = follow

    template["status"] = "COMPLETED"
    return template


# ============================================================
# LEVEL 4: SOURCE VERIFICATION (~$0.10, <120s)
# ============================================================

def measure_level4(text: str) -> Dict[str, Any]:
    """
    Verify sources in the report.
    Checks: Do URLs exist? Do DOIs resolve?
    Does NOT check if source actually says what report claims (that needs LLM).
    """
    import urllib.request

    urls = re.findall(r'https?://[^\s\)\]>]+', text)
    unique_urls = list(set(urls))

    results = []
    reachable = 0
    unreachable = 0
    checked = 0

    for url in unique_urls[:20]:  # Max 20 to stay fast
        checked += 1
        try:
            req = urllib.request.Request(url, method="HEAD",
                                        headers={"User-Agent": "ResearchVerifier/1.0"})
            resp = urllib.request.urlopen(req, timeout=10)
            status = resp.getcode()
            reachable += 1
            results.append({"url": url, "status": status, "reachable": True})
        except Exception as e:
            unreachable += 1
            results.append({"url": url, "status": str(e)[:100], "reachable": False})

    # DOI check
    dois = re.findall(r'10\.\d{4,}/[^\s\]]+', text)
    unique_dois = list(set(dois))

    doi_results = []
    for doi in unique_dois[:10]:
        try:
            url = f"https://doi.org/{doi}"
            req = urllib.request.Request(url, method="HEAD",
                                        headers={"User-Agent": "ResearchVerifier/1.0"})
            resp = urllib.request.urlopen(req, timeout=10)
            doi_results.append({"doi": doi, "resolves": True})
        except Exception:
            doi_results.append({"doi": doi, "resolves": False})

    reachability_rate = reachable / max(checked, 1)

    return {
        "level": 4,
        "timestamp": datetime.now().isoformat(),
        "urls_found": len(unique_urls),
        "urls_checked": checked,
        "urls_reachable": reachable,
        "urls_unreachable": unreachable,
        "reachability_rate": round(reachability_rate, 3),
        "dois_found": len(unique_dois),
        "dois_resolved": sum(1 for d in doi_results if d["resolves"]),
        "url_details": results,
        "doi_details": doi_results,
    }


# ============================================================
# STORAGE (append-only JSONL)
# ============================================================

def store_measurement(measurement: Dict):
    """Append measurement to JSONL file."""
    MEASUREMENTS_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(MEASUREMENTS_FILE, "a") as f:
        f.write(json.dumps(measurement) + "\n")


def load_measurements() -> List[Dict]:
    """Load all measurements from JSONL."""
    if not MEASUREMENTS_FILE.exists():
        return []
    measurements = []
    with open(MEASUREMENTS_FILE) as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    measurements.append(json.loads(line))
                except json.JSONDecodeError:
                    pass
    return measurements


# ============================================================
# COMPARISON
# ============================================================

def compare_reports(reports: List[Dict[str, Any]]):
    """Compare L1 measurements across reports."""
    if len(reports) < 2:
        print("Need at least 2 reports to compare.")
        return

    # Key metrics to compare
    metrics = [
        ("l1_score", "L1 Score (0-100)"),
        ("word_count", "Words"),
        ("unique_citations", "Unique Citations"),
        ("citation_density_per_1k", "Citations/1K Words"),
        ("llm_phrase_count", "LLM Phrases (lower=better)"),
        ("unsourced_claim_rate", "Unsourced Claims (lower=better)"),
        ("feci_completeness", "FECI Completeness"),
        ("required_sections_present", "Required Sections"),
        ("hedge_count", "Hedging Language"),
        ("has_beipackzettel", "Has Beipackzettel"),
        ("has_claim_ledger", "Has Claim Ledger"),
        ("has_contradiction_register", "Has Contradictions"),
    ]

    # Header
    names = [r.get("filepath", "?").split("/")[-1][:25] for r in reports]
    header = f"{'Metric':<30}" + "".join(f"{n:>28}" for n in names)
    print(f"\n{header}")
    print("-" * (30 + 28 * len(reports)))

    for key, label in metrics:
        values = [r.get(key, "n/a") for r in reports]
        row = f"{label:<30}"
        for v in values:
            if isinstance(v, float):
                row += f"{v:>28.2f}"
            elif isinstance(v, bool):
                row += f"{'Yes' if v else 'No':>28}"
            else:
                row += f"{v!s:>28}"
        print(row)

    # Winner
    scores = [(r.get("l1_score", 0), r.get("filepath", "?")) for r in reports]
    winner = max(scores, key=lambda x: x[0])
    print(f"\nWinner: {winner[1].split('/')[-1]} (L1={winner[0]:.1f})")


def compute_correlations():
    """Compute correlation between L1, L2, L3, L4 scores."""
    measurements = load_measurements()
    if len(measurements) < 5:
        print(f"Need at least 5 measurements, have {len(measurements)}.")
        return

    # Group by file_hash
    by_hash = {}
    for m in measurements:
        h = m.get("file_hash", "")
        if h not in by_hash:
            by_hash[h] = {}
        by_hash[h][m.get("level", 0)] = m

    # Find hashes with both L1 and L2
    pairs = []
    for h, levels in by_hash.items():
        if 1 in levels and 2 in levels:
            pairs.append({
                "l1_score": levels[1].get("l1_score", 0),
                "l2_rubric": levels[2].get("rubric_total", 0),
                "l2_insight": levels[2].get("novel_insight_score", 0),
                "l2_claims": levels[2].get("claim_verification_rate", 0),
            })

    if len(pairs) < 3:
        print(f"Need at least 3 reports with both L1+L2, have {len(pairs)}.")
        return

    # Simple Pearson correlation (stdlib only)
    def pearson(xs, ys):
        n = len(xs)
        if n < 3:
            return 0
        mean_x = sum(xs) / n
        mean_y = sum(ys) / n
        num = sum((x - mean_x) * (y - mean_y) for x, y in zip(xs, ys))
        den_x = sum((x - mean_x) ** 2 for x in xs) ** 0.5
        den_y = sum((y - mean_y) ** 2 for y in ys) ** 0.5
        if den_x == 0 or den_y == 0:
            return 0
        return num / (den_x * den_y)

    l1 = [p["l1_score"] for p in pairs]
    l2r = [p["l2_rubric"] for p in pairs]
    l2i = [p["l2_insight"] for p in pairs]

    print(f"\nCORRELATION MATRIX ({len(pairs)} reports)")
    print(f"  L1 Score ↔ L2 Rubric:  r={pearson(l1, l2r):.3f}")
    print(f"  L1 Score ↔ L2 Insight: r={pearson(l1, l2i):.3f}")
    print(f"  L2 Rubric ↔ L2 Insight: r={pearson(l2r, l2i):.3f}")

    if pearson(l1, l2r) > 0.7:
        print("\n  → L1 and L2 correlate well. L1 (free) is a good proxy for L2 ($0.50).")
    elif pearson(l1, l2r) < 0.3:
        print("\n  → L1 and L2 do NOT correlate. They measure different things.")
    else:
        print("\n  → Moderate correlation. Both metrics add value.")


# ============================================================
# CLI
# ============================================================

def main():
    parser = argparse.ArgumentParser(
        description="Research Quality Measurement System",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Levels:
  1 = Deterministic ($0, <1s): structure, citations, LLM phrases
  2 = LLM Evaluator (~$0.50): rubric, insight, claims
  3 = Human (manual): trust, utility, errors
  4 = Source Verification (~$0.10): URL reachability, DOI resolution

Examples:
  %(prog)s report.md                    # Level 1 only (default)
  %(prog)s report.md --full             # All 4 levels
  %(prog)s report.md --level 1 4        # Specific levels
  %(prog)s a.md b.md --compare          # Side-by-side comparison
  %(prog)s --correlations               # Check if metrics correlate
        """,
    )
    parser.add_argument("files", nargs="*", help="Report file(s) to measure")
    parser.add_argument("--full", action="store_true",
                        help="Run all 4 measurement levels")
    parser.add_argument("--level", nargs="+", type=int, default=[1],
                        help="Which levels to run (1-4)")
    parser.add_argument("--compare", action="store_true",
                        help="Compare multiple reports side-by-side")
    parser.add_argument("--batch", action="store_true",
                        help="Measure all .md files in directory")
    parser.add_argument("--correlations", action="store_true",
                        help="Show correlation matrix between levels")
    parser.add_argument("--human", action="store_true",
                        help="Collect human evaluation interactively")
    parser.add_argument("--store", action="store_true", default=True,
                        help="Store measurements to JSONL (default: true)")
    parser.add_argument("--no-store", action="store_true",
                        help="Don't store measurements")

    args = parser.parse_args()

    if args.correlations:
        compute_correlations()
        return

    if args.full:
        args.level = [1, 2, 3, 4]

    # Collect files
    files = []
    for f in args.files:
        p = Path(f)
        if p.is_dir() or args.batch:
            files.extend(sorted(p.glob("**/*.md")))
        elif p.exists():
            files.append(p)
        else:
            print(f"[WARN] Not found: {f}")

    if not files and not args.correlations:
        parser.print_help()
        return

    # Measure
    all_l1 = []
    for filepath in files:
        text = filepath.read_text()
        print(f"\n{'=' * 60}")
        print(f"MEASURING: {filepath.name} ({len(text)} chars)")
        print(f"{'=' * 60}")

        # Level 1: Always
        if 1 in args.level:
            l1 = measure_level1(text, str(filepath))
            all_l1.append(l1)
            print(f"\n  L1 Score: {l1['l1_score']}/100")
            print(f"  Words: {l1['word_count']} | Citations: {l1['unique_citations']} "
                  f"({l1['citation_density_per_1k']}/1K)")
            print(f"  LLM Phrases: {l1['llm_phrase_count']} | "
                  f"Unsourced Claims: {l1['unsourced_claim_rate']:.0%}")
            print(f"  Structure: {l1['required_sections_present']}/{l1['required_sections_total']} required | "
                  f"FECI: {l1['feci_completeness']}")
            print(f"  Beipackzettel: {'Yes' if l1['has_beipackzettel'] else 'No'} | "
                  f"Claim Ledger: {'Yes' if l1['has_claim_ledger'] else 'No'} | "
                  f"Contradictions: {'Yes' if l1['has_contradiction_register'] else 'No'}")
            if l1['llm_phrases_found']:
                print(f"  LLM phrases: {', '.join(p['phrase'] for p in l1['llm_phrases_found'])}")
            if not args.no_store:
                store_measurement(l1)

        # Level 2: LLM
        if 2 in args.level:
            print(f"\n  [L2] LLM Evaluator...")
            l2 = measure_level2(text)
            if "error" not in l2:
                print(f"  L2 Rubric: {l2.get('rubric_total', '?')}/16 | "
                      f"Insight: {l2.get('novel_insight_score', '?')}/5 | "
                      f"Claims: {l2.get('claim_verification_rate', '?')}")
            else:
                print(f"  L2 Error: {l2['error']}")
            if not args.no_store:
                l2["filepath"] = str(filepath)
                store_measurement(l2)

        # Level 3: Human
        if 3 in args.level:
            if args.human:
                l3 = collect_level3_interactive(str(filepath))
            else:
                l3 = measure_level3_prompt(str(filepath))
                print(f"\n  [L3] Human evaluation template saved. "
                      f"Run with --human to fill interactively.")
            if not args.no_store:
                store_measurement(l3)

        # Level 4: Source verification
        if 4 in args.level:
            print(f"\n  [L4] Verifying sources...")
            l4 = measure_level4(text)
            print(f"  URLs: {l4['urls_reachable']}/{l4['urls_checked']} reachable "
                  f"({l4['reachability_rate']:.0%}) | "
                  f"DOIs: {l4['dois_resolved']}/{l4['dois_found']} resolved")
            if not args.no_store:
                l4["filepath"] = str(filepath)
                store_measurement(l4)

    # Compare mode
    if args.compare and len(all_l1) >= 2:
        compare_reports(all_l1)


if __name__ == "__main__":
    main()
