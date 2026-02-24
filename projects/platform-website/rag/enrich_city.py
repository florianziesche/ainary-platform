#!/usr/bin/env python3
"""
enrich_city.py — Compound Dossier Enrichment Engine
=====================================================

Philosophy: Every run makes the dossier BETTER, never worse.
- ACCUMULATE: New sources add, never overwrite
- DECAY: Old data loses confidence over time
- GAP: Missing fields generate targeted research queries
- DELTA: Only changed fields update; changelog tracks everything
- SCORE: Quality score becomes a time series

Usage:
  python3 rag/enrich_city.py data/cities/passau.json [--dry-run] [--report]

Architecture:
  1. LOAD current JSON
  2. ANALYZE gaps (missing fields, thin entities, stale sources)
  3. GENERATE search queries for gaps
  4. MERGE new data (additive, never destructive)
  5. VALIDATE via quality gate
  6. TRACK score evolution (score_history in JSON)

The enrichment is designed to be run by:
  a) Human (manual research + paste)
  b) Cron agent (web_search + auto-merge)
  c) Sub-agent (deep research on specific entity)
"""

import json, sys, os
from datetime import datetime, timedelta
from pathlib import Path

# ─── Schema: What a COMPLETE entity looks like ─────────────────────
ENTITY_SCHEMA = {
    "required": ["name", "role", "party", "summary", "properties", "connections",
                 "quellen", "trustScore", "steckbrief", "karriere"],
    "summary_min_words": 50,
    "properties_min": 5,
    "connections_min": 2,
    "quellen_min": 3,
    "karriere_min": 3,
    "zitate_min": 1,
    "steckbrief_fields": ["alter", "beruf", "familienstand", "wohnort", "partei", "ausbildung"],
}

TENANT_SCHEMA = {
    "required_fields": ["gemeinderat2020", "strukturdaten", "alerts", "organisationen"],
    "alerts_min": 3,
    "organisationen_min": 3,
}

DOSSIER_SCHEMA = {
    "sections": ["tenant", "kb", "graph", "news", "hypotheses", "sentiment",
                 "patterns", "actions", "forecast", "themen", "social"],
    "news_min": 5,
    "hypotheses_min": 2,
    "patterns_min": 2,
    "actions_min": 2,
    "themen_min": 5,
    "social_kandidaten_min": 3,
}

# ─── Freshness Decay ───────────────────────────────────────────────
FRESHNESS_THRESHOLDS = {
    "CURRENT":  0,    # < 7 days
    "FRESH":    7,    # 7-30 days
    "AGING":   30,    # 30-90 days
    "STALE":   90,    # > 90 days → triggers re-research
}

def days_since(date_str):
    """Parse various date formats and return days since."""
    now = datetime.now()
    for fmt in ["%Y-%m-%d", "%Y-%m-%dT%H:%M:%S", "%b %Y", "%B %Y"]:
        try:
            dt = datetime.strptime(date_str, fmt)
            return (now - dt).days
        except (ValueError, TypeError):
            continue
    return 999  # Unknown = treat as stale


def freshness_label(days):
    if days < 7: return "CURRENT"
    if days < 30: return "FRESH"
    if days < 90: return "AGING"
    return "STALE"


# ─── Gap Analysis ──────────────────────────────────────────────────
def analyze_entity_gaps(entity_id, entity):
    """Returns list of gaps with severity and suggested search queries."""
    gaps = []

    # Summary check
    summary = entity.get("summary", "")
    word_count = len(summary.split())
    if word_count < ENTITY_SCHEMA["summary_min_words"]:
        gaps.append({
            "field": "summary",
            "severity": "HIGH",
            "current": f"{word_count} words",
            "target": f"{ENTITY_SCHEMA['summary_min_words']}+ words",
            "query": f'"{entity.get("name", entity_id)}" {entity.get("party", "")} Passau Biografie Lebenslauf',
            "action": "EXPAND summary with biographical details, political positions, key achievements"
        })

    # Properties check
    props = entity.get("properties", [])
    if len(props) < ENTITY_SCHEMA["properties_min"]:
        gaps.append({
            "field": "properties",
            "severity": "HIGH",
            "current": f"{len(props)} properties",
            "target": f"{ENTITY_SCHEMA['properties_min']}+",
            "query": f'"{entity.get("name", entity_id)}" Beruf Ausbildung Familie',
            "action": "ADD missing biographical/political properties"
        })

    # Connections check
    conns = entity.get("connections", [])
    if len(conns) < ENTITY_SCHEMA["connections_min"]:
        gaps.append({
            "field": "connections",
            "severity": "MEDIUM",
            "current": f"{len(conns)} connections",
            "target": f"{ENTITY_SCHEMA['connections_min']}+",
            "query": f'"{entity.get("name", entity_id)}" Koalition Bündnis Zusammenarbeit',
            "action": "MAP political alliances and rivalries"
        })

    # Quellen check
    quellen = entity.get("quellen", [])
    if len(quellen) < ENTITY_SCHEMA["quellen_min"]:
        gaps.append({
            "field": "quellen",
            "severity": "HIGH",
            "current": f"{len(quellen)} sources",
            "target": f"{ENTITY_SCHEMA['quellen_min']}+",
            "query": f'"{entity.get("name", entity_id)}" interview Kommunalwahl 2026',
            "action": "ADD more diverse sources (local media, party websites, social media)"
        })

    # Karriere check
    karriere = entity.get("karriere", [])
    if len(karriere) < ENTITY_SCHEMA["karriere_min"]:
        gaps.append({
            "field": "karriere",
            "severity": "MEDIUM",
            "current": f"{len(karriere)} entries",
            "target": f"{ENTITY_SCHEMA['karriere_min']}+",
            "query": f'"{entity.get("name", entity_id)}" Werdegang Karriere Lebenslauf',
            "action": "EXPAND career timeline with education, jobs, political milestones"
        })

    # Zitate check
    zitate = entity.get("zitate", [])
    if len(zitate) < ENTITY_SCHEMA["zitate_min"]:
        gaps.append({
            "field": "zitate",
            "severity": "LOW",
            "current": f"{len(zitate)} quotes",
            "target": f"{ENTITY_SCHEMA['zitate_min']}+",
            "query": f'"{entity.get("name", entity_id)}" sagt erklärt Interview Zitat',
            "action": "FIND direct quotes from interviews, debates, press releases"
        })

    # Steckbrief completeness
    steckbrief = entity.get("steckbrief", {})
    missing_fields = [f for f in ENTITY_SCHEMA["steckbrief_fields"]
                      if steckbrief.get(f, "—") == "—"]
    if missing_fields:
        gaps.append({
            "field": "steckbrief",
            "severity": "LOW",
            "current": f"Missing: {', '.join(missing_fields)}",
            "target": "All fields filled",
            "query": f'"{entity.get("name", entity_id)}" {" ".join(missing_fields)}',
            "action": f"FILL steckbrief fields: {', '.join(missing_fields)}"
        })

    # Source freshness
    stale_sources = []
    for q in quellen:
        zugriff = q.get("zugriff", "")
        days = days_since(zugriff.replace("Feb 2026", "2026-02-01")
                          .replace("Jan 2026", "2026-01-01")
                          .replace("Dez 2025", "2025-12-01"))
        if days > FRESHNESS_THRESHOLDS["STALE"]:
            stale_sources.append(q.get("name", "?"))
    if stale_sources:
        gaps.append({
            "field": "source_freshness",
            "severity": "MEDIUM",
            "current": f"Stale sources: {', '.join(stale_sources)}",
            "target": "All sources < 90 days",
            "query": f'"{entity.get("name", entity_id)}" 2026',
            "action": "RE-VERIFY stale sources with fresh search"
        })

    return gaps


def analyze_dossier_gaps(data):
    """Top-level dossier gap analysis."""
    gaps = []

    # Section presence
    for section in DOSSIER_SCHEMA["sections"]:
        if section not in data:
            gaps.append({
                "field": section,
                "severity": "CRITICAL",
                "current": "MISSING",
                "target": "Present",
                "action": f"CREATE {section} section"
            })

    # News volume
    news = data.get("news", [])
    if len(news) < DOSSIER_SCHEMA["news_min"]:
        gaps.append({
            "field": "news",
            "severity": "MEDIUM",
            "current": f"{len(news)} items",
            "target": f"{DOSSIER_SCHEMA['news_min']}+",
            "action": "ADD more recent news items"
        })

    # Hypotheses
    hyp = data.get("hypotheses", [])
    if len(hyp) < DOSSIER_SCHEMA["hypotheses_min"]:
        gaps.append({
            "field": "hypotheses",
            "severity": "MEDIUM",
            "current": f"{len(hyp)} hypotheses",
            "target": f"{DOSSIER_SCHEMA['hypotheses_min']}+",
            "action": "FORMULATE more testable hypotheses"
        })

    return gaps


def compute_completeness(data):
    """Returns 0-100 completeness score based on gap analysis."""
    total_checks = 0
    passed_checks = 0

    # Dossier level
    for section in DOSSIER_SCHEMA["sections"]:
        total_checks += 1
        if section in data:
            passed_checks += 1

    # Entity level
    kb = data.get("kb", {})
    for eid, entity in kb.items():
        entity_gaps = analyze_entity_gaps(eid, entity)
        entity_checks = len(ENTITY_SCHEMA["required"]) + 3  # +3 for freshness, steckbrief, zitate
        entity_passed = entity_checks - len([g for g in entity_gaps if g["severity"] in ("HIGH", "CRITICAL")])
        total_checks += entity_checks
        passed_checks += max(0, entity_passed)

    return round((passed_checks / max(total_checks, 1)) * 100)


# ─── Score History ─────────────────────────────────────────────────
def update_score_history(data, new_score, run_type="manual"):
    """Append score to history. Never delete history."""
    if "_meta" not in data:
        data["_meta"] = {}
    if "score_history" not in data["_meta"]:
        data["_meta"]["score_history"] = []

    data["_meta"]["score_history"].append({
        "date": datetime.now().strftime("%Y-%m-%dT%H:%M"),
        "score": new_score,
        "run": run_type,
        "entities": len(data.get("kb", {})),
        "nodes": len(data.get("graph", {}).get("nodes", [])),
        "news": len(data.get("news", [])),
    })

    data["_meta"]["last_enriched"] = datetime.now().strftime("%Y-%m-%dT%H:%M")
    data["_meta"]["version"] = data["_meta"].get("version", 0) + 1

    return data


# ─── Enrichment Report ─────────────────────────────────────────────
def generate_report(data, city_name):
    """Generate human-readable enrichment report."""
    lines = []
    lines.append("=" * 60)
    lines.append(f"ENRICHMENT REPORT: {city_name}")
    lines.append("=" * 60)

    # Overall score
    score = compute_completeness(data)
    lines.append(f"\nCompleteness Score: {score}/100")

    # Score history
    history = data.get("_meta", {}).get("score_history", [])
    if history:
        lines.append(f"Score History: {' → '.join(str(h['score']) for h in history[-5:])}")
        if len(history) >= 2:
            delta = history[-1]["score"] - history[-2]["score"]
            direction = "↑" if delta > 0 else ("↓" if delta < 0 else "→")
            lines.append(f"Trend: {direction} ({delta:+d} since last run)")

    # Entity gaps
    kb = data.get("kb", {})
    lines.append(f"\nEntities: {len(kb)}")
    for eid, entity in kb.items():
        gaps = analyze_entity_gaps(eid, entity)
        status = "✅" if not gaps else f"⚠️  {len(gaps)} gaps"
        lines.append(f"  [{status}] {entity.get('name', eid)} ({entity.get('party', '?')})")
        for gap in gaps:
            sev = {"CRITICAL": "🔴", "HIGH": "🟠", "MEDIUM": "🟡", "LOW": "⚪"}.get(gap["severity"], "?")
            lines.append(f"    {sev} {gap['field']}: {gap['current']} → {gap['target']}")
            if "query" in gap:
                lines.append(f"       Search: {gap['query']}")

    # Dossier gaps
    dossier_gaps = analyze_dossier_gaps(data)
    if dossier_gaps:
        lines.append(f"\nDossier Gaps:")
        for gap in dossier_gaps:
            lines.append(f"  ⚠️  {gap['field']}: {gap['current']} → {gap['target']}")

    # Research queries (prioritized)
    all_gaps = []
    for eid, entity in kb.items():
        for gap in analyze_entity_gaps(eid, entity):
            gap["entity"] = entity.get("name", eid)
            all_gaps.append(gap)

    high_gaps = [g for g in all_gaps if g["severity"] in ("CRITICAL", "HIGH")]
    if high_gaps:
        lines.append(f"\n{'─' * 60}")
        lines.append(f"PRIORITY RESEARCH QUERIES ({len(high_gaps)} high-priority gaps):")
        lines.append(f"{'─' * 60}")
        for i, gap in enumerate(high_gaps[:10], 1):
            lines.append(f"  {i}. [{gap['entity']}] {gap.get('query', gap['action'])}")

    lines.append(f"\n{'─' * 60}")
    lines.append(f"Next: Run web_search on priority queries, then re-run enrich_city.py")
    lines.append(f"{'─' * 60}")

    return "\n".join(lines)


# ─── Delta Merge ───────────────────────────────────────────────────
def merge_patch(data, patch_file):
    """
    Merge a JSON patch into existing dossier. Rules:
    - Arrays: APPEND (deduplicate by key field)
    - Objects: DEEP MERGE (new keys add, existing keys update only if newer)
    - _meta.changelog: auto-generated entry for every merge

    Patch format (example):
    {
      "kb": {
        "dickl": {
          "properties": [{"key": "Ehefrau", "val": "Maria Dickl", "src": "PNP", "type": "official", "fresh": "CURRENT"}],
          "zitate": [{"text": "...", "kontext": "...", "quelle": "...", "datum": "2026-02-25"}]
        }
      },
      "news": [{"title": "...", "source": "...", "date": "...", "body": "..."}]
    }
    """
    with open(patch_file, "r") as f:
        patch = json.load(f)

    changes = []

    # Merge kb entities
    if "kb" in patch:
        for eid, entity_patch in patch["kb"].items():
            if eid not in data.get("kb", {}):
                # New entity
                data.setdefault("kb", {})[eid] = entity_patch
                changes.append(f"NEW entity: {eid}")
                continue

            existing = data["kb"][eid]
            for field, value in entity_patch.items():
                if isinstance(value, list) and isinstance(existing.get(field), list):
                    # Array merge: append + deduplicate
                    existing_keys = set()
                    key_field = _array_key(field)
                    for item in existing[field]:
                        if key_field and key_field in item:
                            existing_keys.add(item[key_field])

                    added = 0
                    for item in value:
                        item_key = item.get(key_field) if key_field else None
                        if item_key and item_key in existing_keys:
                            continue  # Skip duplicate
                        existing[field].append(item)
                        added += 1
                    if added:
                        changes.append(f"  {eid}.{field}: +{added} items")
                elif isinstance(value, dict) and isinstance(existing.get(field), dict):
                    # Dict merge
                    existing[field].update(value)
                    changes.append(f"  {eid}.{field}: updated")
                else:
                    existing[field] = value
                    changes.append(f"  {eid}.{field}: replaced")

    # Merge top-level arrays (news, hypotheses, patterns, actions)
    for arr_key in ["news", "hypotheses", "patterns", "actions"]:
        if arr_key in patch:
            existing_arr = data.setdefault(arr_key, [])
            key_field = _array_key(arr_key)
            existing_titles = {item.get(key_field, "") for item in existing_arr} if key_field else set()
            added = 0
            for item in patch[arr_key]:
                if key_field and item.get(key_field) in existing_titles:
                    continue
                existing_arr.append(item)
                added += 1
            if added:
                changes.append(f"{arr_key}: +{added} items")

    # Merge graph nodes/links
    if "graph" in patch:
        g = data.setdefault("graph", {"nodes": [], "links": []})
        existing_node_ids = {n["id"] for n in g["nodes"]}
        for node in patch["graph"].get("nodes", []):
            if node["id"] not in existing_node_ids:
                g["nodes"].append(node)
                changes.append(f"graph.nodes: +{node['id']}")
        existing_links = {(l["source"], l["target"]) for l in g["links"]}
        for link in patch["graph"].get("links", []):
            if (link["source"], link["target"]) not in existing_links:
                g["links"].append(link)
                changes.append(f"graph.links: +{link['source']}→{link['target']}")

    # Record changelog
    if changes:
        data.setdefault("_meta", {}).setdefault("changelog", []).append({
            "date": datetime.now().strftime("%Y-%m-%dT%H:%M"),
            "patch": os.path.basename(patch_file),
            "changes": changes,
        })

    return data, changes


def _array_key(field_name):
    """Return the deduplication key for a given array field."""
    return {
        "properties": "key",
        "connections": "target",
        "quellen": "name",
        "karriere": "zeitraum",
        "zitate": "text",
        "news": "title",
        "hypotheses": "id",
        "patterns": "id",
        "actions": "title",
    }.get(field_name)


# ─── Main ──────────────────────────────────────────────────────────
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 rag/enrich_city.py data/cities/<city>.json [--dry-run] [--report]")
        sys.exit(1)

    filepath = sys.argv[1]
    dry_run = "--dry-run" in sys.argv
    report_only = "--report" in sys.argv
    merge_file = None
    for i, arg in enumerate(sys.argv):
        if arg == "--merge" and i + 1 < len(sys.argv):
            merge_file = sys.argv[i + 1]

    with open(filepath, "r") as f:
        data = json.load(f)

    city_name = data.get("tenant", {}).get("gemeinde", Path(filepath).stem)

    # Merge patch if provided
    if merge_file:
        old_score = compute_completeness(data)
        data, changes = merge_patch(data, merge_file)
        new_score = compute_completeness(data)
        print(f"Merged {len(changes)} changes from {merge_file}")
        for c in changes:
            print(f"  {c}")
        if new_score < old_score:
            print(f"\n🔴 SCORE REGRESSION: {old_score} → {new_score} — NOT saving!")
            sys.exit(1)
        print(f"\nScore: {old_score} → {new_score} {'↑' if new_score > old_score else '→'}")

    # Compute score + update history
    score = compute_completeness(data)
    if not report_only:
        data = update_score_history(data, score, "enrich")

    # Generate report
    report = generate_report(data, city_name)
    print(report)

    # Write back (unless dry-run)
    if not dry_run and not report_only:
        with open(filepath, "w") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"\n✅ Updated {filepath} (version {data['_meta']['version']})")
    elif dry_run:
        print(f"\n🔍 Dry run — no changes written")


if __name__ == "__main__":
    main()
