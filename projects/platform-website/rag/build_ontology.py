#!/usr/bin/env python3
"""
Builds a unified ontology from all city JSONs.
Single source of truth for cross-city queries.

Usage: python3 rag/build_ontology.py
Output: data/ontology.json
"""

import json, glob, os
from datetime import datetime

CITY_DIR = "data/cities"
OUTPUT = "data/ontology.json"


def load_cities():
    cities = {}
    for path in sorted(glob.glob(f"{CITY_DIR}/*.json")):
        slug = os.path.basename(path).replace(".json", "")
        if slug == "internal":
            continue  # deprecated
        with open(path) as f:
            cities[slug] = json.load(f)
    return cities


def build_entities(cities):
    """Extract all entities across all cities into flat graph."""
    entities = {}
    for city_slug, data in cities.items():
        kb = data.get("kb", {})
        tenant = data.get("tenant", {})
        city_name = tenant.get("gemeinde", city_slug)
        city_ew = tenant.get("ew", "?")

        for eid, e in kb.items():
            global_id = f"{city_slug}/{eid}"
            entities[global_id] = {
                "id": global_id,
                "local_id": eid,
                "city": city_slug,
                "city_name": city_name,
                "city_ew": city_ew,
                "name": e.get("name", ""),
                "party": e.get("party", ""),
                "role": e.get("role", ""),
                "summary": e.get("summary", ""),
                "instagram": extract_ig(e, data, eid),
                "properties_count": len(e.get("properties", [])),
                "sources_count": len(e.get("quellen", [])),
                "karriere_count": len(e.get("karriere", [])),
                "zitate_count": len(e.get("zitate", [])),
                "trust": e.get("trustScore", {}).get("gesamt", 0),
            }
    return entities


def extract_ig(entity, city_data=None, eid=None):
    """Extract Instagram followers from properties OR social section."""
    import re
    # 1. Try properties
    for p in entity.get("properties", []):
        if "instagram" in p.get("key", "").lower():
            val = p.get("val", "")
            nums = re.findall(r'[\d.]+', val.replace(".", ""))
            if nums:
                try:
                    return int(nums[0])
                except:
                    pass
    # 2. Try summary text (e.g. "3.067 Instagram-Follower")
    summary = entity.get("summary", "")
    ig_matches = re.findall(r'([\d.]+)\s*(?:Instagram|IG)[- ]?(?:Follower)?', summary, re.IGNORECASE)
    if ig_matches:
        try:
            return int(ig_matches[0].replace(".", ""))
        except:
            pass
    # Also try "X Follower" pattern
    ig_matches2 = re.findall(r'([\d.]+)\s*Follower', summary)
    if ig_matches2:
        try:
            return int(ig_matches2[0].replace(".", ""))
        except:
            pass
    # 3. Try social.kandidaten section
    if city_data and eid:
        social = city_data.get("social", {})
        for k in social.get("kandidaten", []):
            if k.get("id") == eid:
                ig = k.get("instagram", {})
                followers = ig.get("followers", 0)
                if followers and isinstance(followers, (int, float)):
                    return int(followers)
    return 0


def build_relationships(cities):
    """Extract all entity connections + cross-city links."""
    rels = []
    for city_slug, data in cities.items():
        kb = data.get("kb", {})
        for eid, e in kb.items():
            for conn in e.get("connections", []):
                rels.append({
                    "source": f"{city_slug}/{eid}",
                    "target_local": conn.get("to", ""),
                    "target": f"{city_slug}/{conn.get('to', '')}",
                    "type": conn.get("type", ""),
                    "context": conn.get("context", ""),
                    "city": city_slug,
                })

        # Cross-city pattern links
        for p in data.get("patterns", []):
            for cross in p.get("cross_city", []):
                rels.append({
                    "source": city_slug,
                    "target": cross,
                    "type": "CROSS_CITY_PATTERN",
                    "context": p.get("titel", ""),
                    "city": city_slug,
                })
    return rels


def build_patterns(cities):
    """Aggregate all patterns with cross-city evidence."""
    patterns = []
    seen = set()
    for city_slug, data in cities.items():
        for p in data.get("patterns", []):
            key = p.get("id", "") or p.get("titel", "")
            patterns.append({
                "id": f"{city_slug}/{key}",
                "city": city_slug,
                "titel": p.get("titel", ""),
                "beschreibung": p.get("beschreibung", ""),
                "confidence": p.get("confidence", 0),
                "cross_city": p.get("cross_city", []),
                "evidence_cities": len(p.get("cross_city", [])) + 1,
            })
    return patterns


def build_leaderboard(entities):
    """Social media leaderboard across all cities."""
    ranked = sorted(
        [(eid, e) for eid, e in entities.items() if e["instagram"] > 0],
        key=lambda x: -x[1]["instagram"]
    )

    leaderboard = {
        "by_followers": [],
        "by_party": {},
        "by_role_type": {"amtsinhaber": [], "herausforderer": []},
    }

    for eid, e in ranked:
        entry = {
            "id": eid,
            "name": e["name"],
            "party": e["party"],
            "city": e["city_name"],
            "instagram": e["instagram"],
            "role": e["role"],
        }
        leaderboard["by_followers"].append(entry)

        party = e["party"]
        if party not in leaderboard["by_party"]:
            leaderboard["by_party"][party] = []
        leaderboard["by_party"][party].append(entry)

        # Classify as Amtsinhaber or Herausforderer
        role_lower = e["role"].lower()
        if any(w in role_lower for w in ["oberbürgermeister", "bürgermeister", "ob ", "seit 20"]):
            if "kandidat" not in role_lower or "seit" in role_lower:
                leaderboard["by_role_type"]["amtsinhaber"].append(entry)
            else:
                leaderboard["by_role_type"]["herausforderer"].append(entry)
        else:
            leaderboard["by_role_type"]["herausforderer"].append(entry)

    return leaderboard


def build_cross_city_insights(patterns):
    """Identify patterns confirmed across multiple cities."""
    multi_city = [p for p in patterns if p["evidence_cities"] >= 2]
    multi_city.sort(key=lambda x: (-x["evidence_cities"], -x["confidence"]))
    return multi_city


def build_themen_radar(cities):
    """Aggregate themen across all cities."""
    all_themen = {}
    for city_slug, data in cities.items():
        themen = data.get("themen", {})
        for t in themen.get("radar", []):
            label = t.get("label", "").lower()
            # Normalize similar themes
            key = label
            for norm_key, keywords in {
                "wohnen": ["wohnen", "wohnungsbau", "bezahlbar"],
                "verkehr": ["verkehr", "mobilität", "öpnv", "magnetschwebebahn", "stub"],
                "klima": ["klima", "umwelt", "nachhaltigkeit", "fernwärme"],
                "haushalt": ["haushalt", "finanzen", "sozialkosten"],
                "wirtschaft": ["wirtschaft", "arbeitsplätze", "innovation"],
            }.items():
                if any(kw in label for kw in keywords):
                    key = norm_key
                    break

            if key not in all_themen:
                all_themen[key] = {"label": t.get("label", ""), "cities": [], "avg_relevanz": 0, "count": 0}
            all_themen[key]["cities"].append({"city": city_slug, "relevanz": t.get("relevanz", 0)})
            all_themen[key]["count"] += 1

    # Calculate averages
    for k, v in all_themen.items():
        v["avg_relevanz"] = round(sum(c["relevanz"] for c in v["cities"]) / max(len(v["cities"]), 1), 1)

    return dict(sorted(all_themen.items(), key=lambda x: -x[1]["avg_relevanz"]))


def main():
    cities = load_cities()
    entities = build_entities(cities)
    relationships = build_relationships(cities)
    patterns = build_patterns(cities)
    leaderboard = build_leaderboard(entities)
    cross_city = build_cross_city_insights(patterns)
    themen = build_themen_radar(cities)

    # City scores from validate
    city_scores = {}
    for slug in cities:
        meta = cities[slug].get("_meta", {})
        history = meta.get("score_history", [])
        if history:
            last = history[-1]
            city_scores[slug] = last.get("score", 0) if isinstance(last, dict) else last
        else:
            city_scores[slug] = 0

    ontology = {
        "_meta": {
            "version": 1,
            "created": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "description": "Single source of truth — all entities, relationships, patterns across all cities",
            "cities": len(cities),
            "entities": len(entities),
            "relationships": len(relationships),
            "patterns": len(patterns),
            "cross_city_patterns": len(cross_city),
        },
        "city_scores": city_scores,
        "entities": entities,
        "relationships": relationships,
        "patterns": patterns,
        "cross_city_insights": cross_city,
        "leaderboard": leaderboard,
        "themen_radar": themen,
    }

    with open(OUTPUT, "w") as f:
        json.dump(ontology, f, indent=2, ensure_ascii=False)

    print(f"✅ Ontology built: {OUTPUT}")
    print(f"   Cities: {len(cities)}")
    print(f"   Entities: {len(entities)}")
    print(f"   Relationships: {len(relationships)}")
    print(f"   Patterns: {len(patterns)}")
    print(f"   Cross-city patterns: {len(cross_city)}")
    print(f"   Themen clusters: {len(themen)}")
    print(f"\n📊 SOCIAL MEDIA LEADERBOARD (Top 10):")
    for entry in leaderboard["by_followers"][:10]:
        print(f"   {entry['instagram']:>6,} IG  {entry['name']:20s} ({entry['party']}, {entry['city']})")

    print(f"\n📊 BY PARTY:")
    for party, members in sorted(leaderboard["by_party"].items(), key=lambda x: -max(m["instagram"] for m in x[1])):
        top = members[0]
        print(f"   {party:10s}: {len(members)} candidates, top={top['name']} ({top['instagram']:,} IG)")

    print(f"\n📊 THEMEN (cross-city, by avg relevanz):")
    for key, t in list(themen.items())[:8]:
        cities_str = ", ".join(c["city"] for c in t["cities"])
        print(f"   {t['avg_relevanz']:5.1f}  {t['label']:30s} ({t['count']} cities: {cities_str})")


if __name__ == "__main__":
    main()
