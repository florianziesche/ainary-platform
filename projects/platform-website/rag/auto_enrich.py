#!/usr/bin/env python3
"""
auto_enrich.py — Autonomous Gap Detection + Fill Engine
=========================================================

THE TEMPLATE IS THE PRODUCT.
When the schema adds a section, ALL cities must comply.
When one city improves, ALL cities get the same improvement queued.

This script:
1. Loads SCHEMA.json (the master template)
2. Scans ALL city JSONs against the schema
3. Detects gaps (missing sections, thin entities, stale data)
4. Generates CONCRETE fill instructions (not just "research needed")
5. Outputs a queue of auto-fillable tasks

For the agent: run this, then execute the queue top-to-bottom.
Each task has: city, field, search_query, merge_instruction.

Usage:
  python3 rag/auto_enrich.py                    # Scan all cities
  python3 rag/auto_enrich.py --city passau      # Scan one city
  python3 rag/auto_enrich.py --execute          # Scan + print execution plan
  python3 rag/auto_enrich.py --propagate        # Apply cross-city learnings
"""

import json, sys, os, glob
from datetime import datetime
from pathlib import Path

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SCHEMA_PATH = os.path.join(SCRIPT_DIR, 'SCHEMA.json')
CITIES_DIR = os.path.join(SCRIPT_DIR, '..', 'data', 'cities')
JOURNAL_PATH = os.path.join(SCRIPT_DIR, 'learning-journal.json')


def load_schema():
    with open(SCHEMA_PATH) as f:
        return json.load(f)


def load_city(filepath):
    with open(filepath) as f:
        return json.load(f)


def load_all_cities():
    cities = {}
    for f in sorted(glob.glob(os.path.join(CITIES_DIR, '*.json'))):
        if 'index.json' in f:
            continue
        try:
            data = load_city(f)
            city_id = Path(f).stem
            cities[city_id] = {"path": f, "data": data}
        except Exception as e:
            print(f"  ⚠️  Error loading {f}: {e}")
    return cities


# ─── Gap Detection ─────────────────────────────────────────────────

def detect_section_gaps(data, schema):
    """Detect missing or empty required sections."""
    gaps = []
    for section, spec in schema["sections"].items():
        if not spec.get("required"):
            continue
        if section not in data or not data[section]:
            gaps.append({
                "type": "MISSING_SECTION",
                "severity": "CRITICAL",
                "field": section,
                "description": spec["description"],
                "auto_fillable": section in ("themen", "social", "news", "forecast"),
            })
        elif isinstance(data[section], list) and "min_items" in spec:
            if len(data[section]) < spec["min_items"]:
                gaps.append({
                    "type": "THIN_SECTION",
                    "severity": "HIGH",
                    "field": section,
                    "current": len(data[section]),
                    "required": spec["min_items"],
                    "description": f"{section}: {len(data[section])}/{spec['min_items']} items",
                    "auto_fillable": True,
                })
        elif section == "themen" and isinstance(data[section], dict):
            radar = data[section].get("radar", [])
            if len(radar) < spec.get("min_items", 5):
                gaps.append({
                    "type": "THIN_SECTION",
                    "severity": "HIGH",
                    "field": "themen.radar",
                    "current": len(radar),
                    "required": spec.get("min_items", 5),
                    "auto_fillable": True,
                })
        elif section == "social" and isinstance(data[section], dict):
            kands = data[section].get("kandidaten", [])
            if len(kands) < spec.get("min_kandidaten", 3):
                gaps.append({
                    "type": "THIN_SECTION",
                    "severity": "HIGH",
                    "field": "social.kandidaten",
                    "current": len(kands),
                    "required": spec.get("min_kandidaten", 3),
                    "auto_fillable": True,
                })
    return gaps


def detect_entity_gaps(data, schema):
    """Detect gaps in entity dossiers."""
    gaps = []
    es = schema["entity_schema"]
    kb = data.get("kb", {})
    city = data.get("tenant", {}).get("gemeinde", "?")

    for eid, entity in kb.items():
        name = entity.get("name", eid)
        party = entity.get("party", "?")

        # Summary
        words = len(entity.get("summary", "").split())
        if words < es["summary_min_words"]:
            gaps.append({
                "type": "ENTITY_GAP",
                "severity": "HIGH",
                "entity": eid,
                "field": "summary",
                "current": f"{words} words",
                "required": f"{es['summary_min_words']}+ words",
                "query": schema["auto_fill_queries"]["entity_summary"].format(
                    name=name, party=party, city=city),
                "auto_fillable": True,
            })

        # Properties
        if len(entity.get("properties", [])) < es["properties_min"]:
            gaps.append({
                "type": "ENTITY_GAP",
                "severity": "HIGH",
                "entity": eid,
                "field": "properties",
                "current": len(entity.get("properties", [])),
                "required": es["properties_min"],
                "query": schema["auto_fill_queries"]["entity_steckbrief"].format(
                    name=name),
                "auto_fillable": True,
            })

        # Connections
        if len(entity.get("connections", [])) < es["connections_min"]:
            gaps.append({
                "type": "ENTITY_GAP",
                "severity": "MEDIUM",
                "entity": eid,
                "field": "connections",
                "current": len(entity.get("connections", [])),
                "required": es["connections_min"],
                "query": schema["auto_fill_queries"]["entity_connections"].format(
                    name=name),
                "auto_fillable": True,
            })

        # Sources
        if len(entity.get("quellen", [])) < es["quellen_min"]:
            gaps.append({
                "type": "ENTITY_GAP",
                "severity": "HIGH",
                "entity": eid,
                "field": "quellen",
                "current": len(entity.get("quellen", [])),
                "required": es["quellen_min"],
                "auto_fillable": False,
            })

        # Karriere
        if len(entity.get("karriere", [])) < es["karriere_min"]:
            gaps.append({
                "type": "ENTITY_GAP",
                "severity": "MEDIUM",
                "entity": eid,
                "field": "karriere",
                "current": len(entity.get("karriere", [])),
                "required": es["karriere_min"],
                "query": schema["auto_fill_queries"]["entity_karriere"].format(
                    name=name),
                "auto_fillable": True,
            })

        # Zitate
        if len(entity.get("zitate", [])) < es["zitate_min"]:
            gaps.append({
                "type": "ENTITY_GAP",
                "severity": "LOW",
                "entity": eid,
                "field": "zitate",
                "current": len(entity.get("zitate", [])),
                "required": es["zitate_min"],
                "query": schema["auto_fill_queries"]["entity_zitate"].format(
                    name=name),
                "auto_fillable": True,
            })

        # Steckbrief
        steckbrief = entity.get("steckbrief", {})
        filled = sum(1 for v in steckbrief.values() if v != "—" and v)
        if filled < es.get("steckbrief_required_filled", 4):
            missing = [k for k, v in steckbrief.items() if v == "—" or not v]
            gaps.append({
                "type": "ENTITY_GAP",
                "severity": "LOW",
                "entity": eid,
                "field": "steckbrief",
                "current": f"{filled}/{len(steckbrief)} filled",
                "missing_fields": missing,
                "query": schema["auto_fill_queries"]["entity_steckbrief"].format(
                    name=name),
                "auto_fillable": True,
            })

    return gaps


def detect_propagation_gaps(cities, schema):
    """Find improvements in one city that should propagate to others."""
    gaps = []

    # Find which sections exist in ANY city but not ALL
    section_coverage = {}
    for city_id, city_info in cities.items():
        for section in schema["sections"]:
            section_coverage.setdefault(section, {"has": [], "missing": []})
            if section in city_info["data"] and city_info["data"][section]:
                section_coverage[section]["has"].append(city_id)
            else:
                section_coverage[section]["missing"].append(city_id)

    for section, coverage in section_coverage.items():
        if coverage["has"] and coverage["missing"]:
            # Some cities have it, some don't → propagation gap
            for missing_city in coverage["missing"]:
                example_city = coverage["has"][0]
                gaps.append({
                    "type": "PROPAGATION",
                    "severity": "HIGH",
                    "city": missing_city,
                    "field": section,
                    "description": f"{missing_city} is missing '{section}' — "
                                  f"but {example_city} has it. Template requires it.",
                    "template_city": example_city,
                    "auto_fillable": True,
                })

    # Find entity-level patterns that could transfer
    # e.g., if Passau has themen with positions, check if Bamberg does too
    for city_id, city_info in cities.items():
        themen = city_info["data"].get("themen", {}).get("radar", [])
        if themen:
            has_positions = any(t.get("positionen") for t in themen)
            if not has_positions:
                gaps.append({
                    "type": "QUALITY_PROPAGATION",
                    "severity": "MEDIUM",
                    "city": city_id,
                    "field": "themen.positionen",
                    "description": f"{city_id} has Themen-Radar but no candidate positions. "
                                  f"Add positions to match Passau quality level.",
                    "auto_fillable": True,
                })

    return gaps


# ─── Execution Plan ────────────────────────────────────────────────

def generate_execution_plan(all_gaps, cities):
    """Turn gaps into an ordered, executable task list."""
    plan = []

    # Sort: CRITICAL > HIGH > MEDIUM > LOW
    severity_order = {"CRITICAL": 0, "HIGH": 1, "MEDIUM": 2, "LOW": 3}
    sorted_gaps = sorted(all_gaps, key=lambda g: (
        severity_order.get(g.get("severity", "LOW"), 4),
        g.get("city", ""),
        g.get("field", "")
    ))

    for i, gap in enumerate(sorted_gaps):
        task = {
            "step": i + 1,
            "city": gap.get("city", "—"),
            "type": gap["type"],
            "severity": gap["severity"],
            "field": gap.get("field", "?"),
            "description": gap.get("description", f"{gap.get('field')}: {gap.get('current', '?')}/{gap.get('required', '?')}"),
            "auto_fillable": gap.get("auto_fillable", False),
        }
        if "query" in gap:
            task["search_query"] = gap["query"]
        if "template_city" in gap:
            task["reference"] = f"Use {gap['template_city']} as template"
        if "missing_fields" in gap:
            task["missing_fields"] = gap["missing_fields"]

        plan.append(task)

    return plan


# ─── Main ──────────────────────────────────────────────────────────

def main():
    schema = load_schema()
    target_city = None
    execute = "--execute" in sys.argv
    propagate = "--propagate" in sys.argv

    for i, arg in enumerate(sys.argv):
        if arg == "--city" and i + 1 < len(sys.argv):
            target_city = sys.argv[i + 1]

    # Load cities
    cities = load_all_cities()
    if not cities:
        print("No city JSONs found in data/cities/")
        sys.exit(1)

    if target_city:
        if target_city not in cities:
            print(f"City '{target_city}' not found. Available: {', '.join(cities.keys())}")
            sys.exit(1)
        cities = {target_city: cities[target_city]}

    print("=" * 70)
    print(f"AUTO-ENRICH SCAN — Schema v{schema['_version']} · {len(cities)} cities")
    print(f"Template: {len(schema['sections'])} required sections · "
          f"{len(schema['entity_schema']['required_fields'])} entity fields")
    print("=" * 70)

    all_gaps = []

    for city_id, city_info in sorted(cities.items()):
        data = city_info["data"]
        city_name = data.get("tenant", {}).get("gemeinde", city_id)

        # Section gaps
        s_gaps = detect_section_gaps(data, schema)
        for g in s_gaps:
            g["city"] = city_id

        # Entity gaps
        e_gaps = detect_entity_gaps(data, schema)
        for g in e_gaps:
            g["city"] = city_id

        city_gaps = s_gaps + e_gaps
        all_gaps.extend(city_gaps)

        # City summary
        crit = len([g for g in city_gaps if g["severity"] == "CRITICAL"])
        high = len([g for g in city_gaps if g["severity"] == "HIGH"])
        med = len([g for g in city_gaps if g["severity"] == "MEDIUM"])
        low = len([g for g in city_gaps if g["severity"] == "LOW"])
        auto = len([g for g in city_gaps if g.get("auto_fillable")])

        status = "✅ COMPLIANT" if not city_gaps else f"⚠️  {len(city_gaps)} gaps"
        if crit > 0:
            status = f"🔴 {crit} CRITICAL"

        sections_present = len(detect_section_gaps(data, schema))
        total_sections = len(schema["sections"])

        print(f"\n{'─' * 70}")
        print(f"📁 {city_name} ({city_id}.json) — {status}")
        print(f"   Sections: {total_sections - len(s_gaps)}/{total_sections} · "
              f"Entities: {len(data.get('kb', {}))} · "
              f"Gaps: 🔴{crit} 🟠{high} 🟡{med} ⚪{low} · Auto-fillable: {auto}")

        if city_gaps:
            for g in city_gaps[:8]:
                sev_icon = {"CRITICAL": "🔴", "HIGH": "🟠", "MEDIUM": "🟡", "LOW": "⚪"}.get(g["severity"], "?")
                auto_icon = "🤖" if g.get("auto_fillable") else "👤"
                entity_str = f" [{g['entity']}]" if "entity" in g else ""
                print(f"   {sev_icon}{auto_icon}{entity_str} {g.get('field', '?')}: "
                      f"{g.get('current', 'MISSING')} → {g.get('required', 'required')}")
                if "query" in g:
                    print(f"      🔍 {g['query'][:80]}")
            if len(city_gaps) > 8:
                print(f"   ... +{len(city_gaps) - 8} more gaps")

    # Propagation gaps
    if propagate and len(cities) >= 2:
        p_gaps = detect_propagation_gaps(cities, schema)
        all_gaps.extend(p_gaps)
        if p_gaps:
            print(f"\n{'─' * 70}")
            print(f"🌐 PROPAGATION GAPS ({len(p_gaps)} cross-city issues):")
            for g in p_gaps:
                print(f"   → {g['city']}: {g['description'][:80]}")

    # Summary
    total = len(all_gaps)
    auto_fillable = len([g for g in all_gaps if g.get("auto_fillable")])
    manual = total - auto_fillable

    print(f"\n{'=' * 70}")
    print(f"TOTAL: {total} gaps across {len(cities)} cities")
    print(f"  🤖 Auto-fillable: {auto_fillable} ({round(auto_fillable/max(total,1)*100)}%)")
    print(f"  👤 Manual:        {manual}")

    # Execution plan
    if execute and all_gaps:
        plan = generate_execution_plan(all_gaps, cities)
        print(f"\n{'=' * 70}")
        print(f"EXECUTION PLAN ({len(plan)} tasks)")
        print(f"{'=' * 70}")
        for task in plan[:20]:
            auto_icon = "🤖" if task["auto_fillable"] else "👤"
            sev_icon = {"CRITICAL": "🔴", "HIGH": "🟠", "MEDIUM": "🟡", "LOW": "⚪"}.get(task["severity"], "?")
            print(f"\n  [{task['step']:02d}] {sev_icon}{auto_icon} {task['city']} → {task['field']}")
            print(f"       {task['description'][:80]}")
            if "search_query" in task:
                print(f"       🔍 web_search: {task['search_query'][:70]}")
            if "reference" in task:
                print(f"       📋 {task['reference']}")
        if len(plan) > 20:
            print(f"\n  ... +{len(plan) - 20} more tasks")

    print(f"\n{'─' * 70}")
    print(f"Next: python3 rag/auto_enrich.py --execute --propagate")
    print(f"Then: Execute search queries for 🤖 tasks, merge results, re-validate")
    print(f"{'─' * 70}")

    return all_gaps


if __name__ == "__main__":
    main()
