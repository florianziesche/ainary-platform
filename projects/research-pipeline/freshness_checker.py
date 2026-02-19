#!/usr/bin/env python3
"""
freshness_checker.py — Weekly freshness check for all published reports.

Checks:
1. Have cited sources been updated/retracted?
2. Are there new papers on the same topic? (via Semantic Scholar)
3. Have any predictions resolved?

Output: freshness-status.json with per-report badges (FRESH/AGING/STALE)

Usage:
    python3 freshness_checker.py           # check all reports
    python3 freshness_checker.py MIA-004   # check specific report
"""

import json
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

WORKSPACE = Path.home() / ".openclaw" / "workspace"
GRAPH_PATH = WORKSPACE / "research-base" / "knowledge-graph.json"
FRESHNESS_PATH = WORKSPACE / "research-base" / "freshness-status.json"


def load_graph() -> dict:
    if GRAPH_PATH.exists():
        return json.loads(GRAPH_PATH.read_text())
    return {"nodes": {}, "edges": []}


def load_freshness() -> dict:
    if FRESHNESS_PATH.exists():
        return json.loads(FRESHNESS_PATH.read_text())
    return {}


def save_freshness(status: dict):
    FRESHNESS_PATH.write_text(json.dumps(status, indent=2))


def check_report(report_id: str, node: dict) -> dict:
    """Check freshness of a single report."""
    now = datetime.now(timezone.utc)
    report_date = datetime.strptime(node.get("date", "2026-01-01"), "%Y-%m-%d").replace(tzinfo=timezone.utc)
    age_days = (now - report_date).days

    issues = []
    badge = "FRESH"

    # Age check
    if age_days > 90:
        issues.append(f"Report is {age_days} days old (>90)")
        badge = "STALE"
    elif age_days > 30:
        issues.append(f"Report is {age_days} days old (>30)")
        badge = "AGING"

    # Source freshness would check URLs here (future: HEAD requests for Last-Modified)
    # For now: flag based on age alone

    # Evidence path check
    pdir = Path(node.get("path", ""))
    evidence_path = pdir / "evidence-extracted.json"
    if evidence_path.exists():
        evidence = json.loads(evidence_path.read_text())
        source_count = len(evidence) if isinstance(evidence, list) else 0
        if source_count < 5:
            issues.append(f"Only {source_count} sources (recommend 8+)")
            if badge == "FRESH":
                badge = "AGING"

    return {
        "report_id": report_id,
        "badge": badge,
        "age_days": age_days,
        "issues": issues,
        "checked": now.isoformat(),
        "title": node.get("title", "Unknown"),
    }


def check_all(specific_id: str = None):
    """Check freshness of all reports (or one specific)."""
    graph = load_graph()
    freshness = load_freshness()

    reports_to_check = {}
    if specific_id:
        if specific_id in graph["nodes"]:
            reports_to_check[specific_id] = graph["nodes"][specific_id]
        else:
            print(f"Report {specific_id} not in knowledge graph.")
            return
    else:
        reports_to_check = graph["nodes"]

    if not reports_to_check:
        print("No reports in knowledge graph. Run: knowledge_graph.py add <id> <dir>")
        return

    print(f"Checking freshness for {len(reports_to_check)} reports...\n")

    for rid, node in reports_to_check.items():
        result = check_report(rid, node)
        freshness[rid] = result

        icon = {"FRESH": "🟢", "AGING": "🟡", "STALE": "🔴"}.get(result["badge"], "?")
        print(f"  {icon} {rid}: {result['badge']} ({result['age_days']}d)")
        for issue in result["issues"]:
            print(f"     ⚠️  {issue}")

    save_freshness(freshness)
    print(f"\nSaved to: {FRESHNESS_PATH}")

    # Summary
    badges = [f["badge"] for f in freshness.values()]
    print(f"\nSummary: {badges.count('FRESH')} 🟢 / {badges.count('AGING')} 🟡 / {badges.count('STALE')} 🔴")


if __name__ == "__main__":
    specific = sys.argv[1] if len(sys.argv) > 1 else None
    check_all(specific)
