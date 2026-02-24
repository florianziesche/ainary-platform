#!/usr/bin/env python3
"""
Ainary Quality Gate — Validates city JSON against quality standard.
Usage: python3 rag/validate_city.py data/cities/bamberg.json
Returns exit code 0 (PASS) or 1 (FAIL).
"""

import json, sys, os

REQUIRED_KEYS = ["tenant", "kb", "graph", "news", "hypotheses", "sentiment", "patterns", "actions", "forecast"]
MIN_QUELLEN = 30
MIN_ENTITIES = 3
MIN_PROPERTIES = 5
MIN_CONNECTIONS = 1
MIN_SOURCES_PER_ENTITY = 3
MIN_NODES = 8
MIN_LINKS = 10
MIN_NEWS = 5
MIN_HYPOTHESES = 2
MIN_PATTERNS = 2
MIN_ACTIONS = 3
MIN_SUMMARY_WORDS = 50
MIN_QUALITY_SCORE = 70

def validate(filepath):
    errors = []
    warnings = []
    
    with open(filepath) as f:
        data = json.load(f)
    
    city = os.path.basename(filepath).replace(".json", "")
    
    # 1. Required keys
    for k in REQUIRED_KEYS:
        if k not in data:
            errors.append(f"Missing required key: {k}")
    
    if errors:
        return errors, warnings, 0  # Can't continue without keys
    
    tenant = data.get("tenant", {})
    kb = data.get("kb", {})
    graph = data.get("graph", {})
    
    # 2. Tenant validation
    for field in ["gemeinde", "landkreis", "typ", "wahl", "ew"]:
        if not tenant.get(field):
            errors.append(f"tenant.{field} missing")
    
    quellen = tenant.get("quellen", 0)
    if quellen < MIN_QUELLEN:
        errors.append(f"tenant.quellen = {quellen}, minimum is {MIN_QUELLEN}")
    
    # 3. KB validation
    if len(kb) < MIN_ENTITIES:
        errors.append(f"Only {len(kb)} entities, minimum is {MIN_ENTITIES}")
    
    total_sources = 0
    for eid, entity in kb.items():
        prefix = f"kb.{eid}"
        
        if not entity.get("name"):
            errors.append(f"{prefix}.name missing")
        if not entity.get("role"):
            errors.append(f"{prefix}.role missing")
        if not entity.get("party"):
            warnings.append(f"{prefix}.party missing")
        
        summary = entity.get("summary", "")
        word_count = len(summary.split())
        if word_count < MIN_SUMMARY_WORDS:
            errors.append(f"{prefix}.summary only {word_count} words, minimum {MIN_SUMMARY_WORDS}")
        
        props = entity.get("properties", [])
        if len(props) < MIN_PROPERTIES:
            errors.append(f"{prefix}.properties only {len(props)}, minimum {MIN_PROPERTIES}")
        
        # Check properties have sources
        props_without_src = [p for p in props if not p.get("src")]
        if props_without_src:
            errors.append(f"{prefix}: {len(props_without_src)} properties without src")
        
        conns = entity.get("connections", [])
        if len(conns) < MIN_CONNECTIONS:
            warnings.append(f"{prefix}.connections only {len(conns)}, minimum {MIN_CONNECTIONS}")
        
        sources = entity.get("quellen", [])
        if len(sources) < MIN_SOURCES_PER_ENTITY:
            errors.append(f"{prefix}.quellen only {len(sources)}, minimum {MIN_SOURCES_PER_ENTITY}")
        total_sources += len(sources)
        
        # Check sources have trust scores
        sources_without_trust = [s for s in sources if "trust" not in s]
        if sources_without_trust:
            warnings.append(f"{prefix}: {len(sources_without_trust)} sources without trust score")
    
    # 4. Graph validation
    nodes = graph.get("nodes", [])
    links = graph.get("links", [])
    if len(nodes) < MIN_NODES:
        errors.append(f"graph.nodes only {len(nodes)}, minimum {MIN_NODES}")
    if len(links) < MIN_LINKS:
        errors.append(f"graph.links only {len(links)}, minimum {MIN_LINKS}")
    
    # Check all KB entities are in graph
    for eid in kb:
        node_ids = [n.get("id", "") for n in nodes]
        if eid not in node_ids:
            warnings.append(f"KB entity '{eid}' not found in graph nodes")
    
    # 5. News validation
    news = data.get("news", [])
    if len(news) < MIN_NEWS:
        errors.append(f"news only {len(news)}, minimum {MIN_NEWS}")
    
    # 6. Other sections
    if len(data.get("hypotheses", [])) < MIN_HYPOTHESES:
        errors.append(f"hypotheses below minimum ({MIN_HYPOTHESES})")
    if len(data.get("patterns", [])) < MIN_PATTERNS:
        errors.append(f"patterns below minimum ({MIN_PATTERNS})")
    if len(data.get("actions", [])) < MIN_ACTIONS:
        errors.append(f"actions below minimum ({MIN_ACTIONS})")
    
    sentiment = data.get("sentiment", {})
    if not sentiment.get("overall"):
        errors.append("sentiment.overall missing")
    
    forecast = data.get("forecast", {})
    if len(forecast.get("kandidaten", [])) < 2:
        errors.append("forecast needs ≥ 2 kandidaten")
    
    # Quality Score
    score = calculate_quality_score(data, kb, graph, news, total_sources)
    
    return errors, warnings, score


def calculate_quality_score(data, kb, graph, news, total_sources):
    tenant = data.get("tenant", {})
    quellen = tenant.get("quellen", 0)
    
    # Quellen-Dichte (max 25)
    s1 = min(quellen / MIN_QUELLEN, 1.0) * 25
    
    # Entity-Tiefe (max 20)
    entity_score = 0
    for eid, e in kb.items():
        entity_score += min(len(e.get("properties", [])) / MIN_PROPERTIES, 1.0)
    s2 = min(entity_score / max(len(kb), 1) * 20, 20)
    
    # Aktualität (max 15) — simplified: news count
    s3 = min(len(news) / MIN_NEWS, 1.0) * 15
    
    # Vernetzung (max 15)
    links = graph.get("links", [])
    s4 = min(len(links) / MIN_LINKS, 1.0) * 15
    
    # Quellen-Vielfalt (max 15)
    source_types = set()
    for eid, e in kb.items():
        for q in e.get("quellen", []):
            source_types.add(q.get("typ", "Unknown"))
    s5 = min(len(source_types) / 3, 1.0) * 15
    
    # Controversy Check (max 10)
    has_controversy_check = any(
        "controversies" in e for e in kb.values()
    )
    s6 = 10 if has_controversy_check else 0
    
    return round(s1 + s2 + s3 + s4 + s5 + s6)


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 rag/validate_city.py data/cities/{city}.json")
        sys.exit(1)
    
    filepath = sys.argv[1]
    errors, warnings, score = validate(filepath)
    city = os.path.basename(filepath).replace(".json", "")
    
    print(f"\n{'='*50}")
    print(f"QUALITY GATE: {city}")
    print(f"{'='*50}")
    
    if warnings:
        print(f"\n⚠️  WARNINGS ({len(warnings)}):")
        for w in warnings:
            print(f"  - {w}")
    
    if errors:
        print(f"\n❌ ERRORS ({len(errors)}):")
        for e in errors:
            print(f"  - {e}")
        print(f"\nQuality Score: {score}/100")
        print(f"Result: ❌ FAIL")
        sys.exit(1)
    else:
        print(f"\nQuality Score: {score}/100")
        if score >= MIN_QUALITY_SCORE:
            print(f"Result: ✅ PASS (auto-deploy ready)")
        else:
            print(f"Result: ⚠️  PASS with review (score < {MIN_QUALITY_SCORE})")
        sys.exit(0)


if __name__ == "__main__":
    main()
