#!/usr/bin/env python3
"""
Ainary Quality Gate — Validates city JSON against quality standard.
Usage: python3 rag/validate_city.py data/cities/bamberg.json
       python3 rag/validate_city.py data/cities/*.json  (batch mode)

Score has NO CAP. 90 = minimum PASS. Every improvement adds +1.
100 is not perfect — it's "current baseline". Gotham-level = 115+.

Returns exit code 0 (PASS) or 1 (FAIL).
"""

import json, sys, os, glob

# ── Minimum thresholds (gate) ──
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
MIN_PASS_SCORE = 90


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
        return errors, warnings, 0

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

    score = calculate_score(data)
    return errors, warnings, score


def calculate_score(data):
    """
    Uncapped score. 90 = minimum PASS baseline. No maximum.
    
    Base (0-90): meeting all minimums = 90.
    Bonus (+1 each): every unit above minimum adds +1.
    """
    tenant = data.get("tenant", {})
    kb = data.get("kb", {})
    graph = data.get("graph", {})
    news = data.get("news", [])
    hypotheses = data.get("hypotheses", [])
    patterns = data.get("patterns", [])
    actions = data.get("actions", [])
    themen = data.get("themen", {})
    social = data.get("social", {})
    sentiment = data.get("sentiment", {})
    forecast = data.get("forecast", {})

    score = 0

    # ── BASE SCORE (max 90 = meeting all minimums) ──

    # Quellen-Dichte (0-15)
    quellen = tenant.get("quellen", 0)
    score += min(quellen / MIN_QUELLEN, 1.0) * 15

    # Entity completeness (0-20)
    entity_avg = 0
    for eid, e in kb.items():
        props = len(e.get("properties", []))
        sources = len(e.get("quellen", []))
        summary_words = len(e.get("summary", "").split())
        e_score = (
            min(props / MIN_PROPERTIES, 1.0) * 0.4 +
            min(sources / MIN_SOURCES_PER_ENTITY, 1.0) * 0.3 +
            min(summary_words / MIN_SUMMARY_WORDS, 1.0) * 0.3
        )
        entity_avg += e_score
    entity_avg = entity_avg / max(len(kb), 1)
    score += entity_avg * 20

    # Graph (0-10)
    nodes = graph.get("nodes", [])
    links = graph.get("links", [])
    score += min(len(nodes) / MIN_NODES, 1.0) * 5
    score += min(len(links) / MIN_LINKS, 1.0) * 5

    # News (0-10)
    score += min(len(news) / MIN_NEWS, 1.0) * 10

    # Hypotheses + Patterns (0-10)
    score += min(len(hypotheses) / MIN_HYPOTHESES, 1.0) * 5
    score += min(len(patterns) / MIN_PATTERNS, 1.0) * 5

    # Source diversity (0-10)
    source_types = set()
    for eid, e in kb.items():
        for q in e.get("quellen", []):
            source_types.add(q.get("typ", "Unknown"))
    score += min(len(source_types) / 3, 1.0) * 10

    # Forecast quality (0-5)
    kandidaten = forecast.get("kandidaten", [])
    szenarien = forecast.get("szenarien", [])
    score += min(len(kandidaten) / 2, 1.0) * 2.5
    score += min(len(szenarien) / 2, 1.0) * 2.5

    # Sentiment + Actions (0-10)
    topics = sentiment.get("topics", [])
    score += min(len(topics) / 3, 1.0) * 5
    score += min(len(actions) / MIN_ACTIONS, 1.0) * 5

    base = round(score)  # max ~90 if all minimums met

    # ── BONUS POINTS (uncapped, +1 each) ──
    bonus = 0

    # +1 per entity above minimum
    bonus += max(0, len(kb) - MIN_ENTITIES)

    # +1 per thema above 5
    radar = themen.get("radar", [])
    bonus += max(0, len(radar) - 5)

    # +1 per social insight above 3
    insights = social.get("insights", [])
    bonus += max(0, len(insights) - 3)

    # +1 per cross-city pattern
    for p in patterns:
        cross = p.get("cross_city", [])
        if len(cross) > 0:
            bonus += 1

    # +1 per verified quote above 3 (across all entities)
    total_quotes = sum(len(e.get("zitate", [])) for e in kb.values())
    bonus += max(0, total_quotes - 3)

    # +1 for forecast with historical data
    for k in kandidaten:
        if "2020" in str(k) or "historisch" in str(k).lower():
            bonus += 1
            break

    # +1 per controversy documented
    for e in kb.values():
        for p in e.get("properties", []):
            if "kontroverse" in p.get("key", "").lower() or "kontroverse" in str(p.get("val", "")).lower():
                bonus += 1

    # +1 per karriere entry above 3 (across all entities)
    total_karriere = sum(len(e.get("karriere", [])) for e in kb.values())
    bonus += max(0, total_karriere - 3 * len(kb))

    # +1 if themen section exists with leitmedium
    if themen.get("leitmedium"):
        bonus += 1

    # +1 per news item above minimum
    bonus += max(0, len(news) - MIN_NEWS)

    # +1 per hypothesis above minimum
    bonus += max(0, len(hypotheses) - MIN_HYPOTHESES)

    # +1 per scenario above 2
    bonus += max(0, len(szenarien) - 2)

    # +1 per graph node above minimum
    bonus += max(0, len(nodes) - MIN_NODES)

    # +1 per graph link above minimum
    bonus += max(0, len(links) - MIN_LINKS)

    # YouTube Intelligence bonus
    youtube = data.get("youtube", {})
    yt_candidates = youtube.get("candidates", [])
    if yt_candidates:
        bonus += 2  # +2 for having YouTube data
        bonus += min(len(yt_candidates), 3)  # +1 per candidate, max 3
        if youtube.get("insight"):
            bonus += 1  # +1 for Red Diamond insight
        if youtube.get("cross_platform_gap"):
            bonus += 1  # +1 for cross-platform analysis
        if any(c.get("has_own_channel") for c in yt_candidates):
            bonus += 1  # +1 if any candidate has own channel

    return base + bonus


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 rag/validate_city.py data/cities/{city}.json")
        print("       python3 rag/validate_city.py data/cities/*.json")
        sys.exit(1)

    files = []
    for arg in sys.argv[1:]:
        files.extend(glob.glob(arg))

    if not files:
        print("No files found")
        sys.exit(1)

    all_pass = True
    results = []

    for filepath in sorted(files):
        if not filepath.endswith('.json'):
            continue
        errors, warnings, score = validate(filepath)
        city = os.path.basename(filepath).replace(".json", "")
        passed = len(errors) == 0 and score >= MIN_PASS_SCORE

        if not passed:
            all_pass = False

        results.append((city, score, passed, errors, warnings))

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
            print(f"\nScore: {score} (minimum PASS: {MIN_PASS_SCORE})")
            print(f"Result: ❌ FAIL")
        else:
            print(f"\nScore: {score} (minimum PASS: {MIN_PASS_SCORE})")
            print(f"Result: ✅ PASS")

    # Leaderboard if multiple files
    if len(results) > 1:
        print(f"\n{'='*50}")
        print("LEADERBOARD")
        print(f"{'='*50}")
        for city, score, passed, _, _ in sorted(results, key=lambda x: -x[1]):
            status = "✅" if passed else "❌"
            print(f"  {status} {city:20s} {score:>4d}")
        print(f"\n  Total: {sum(1 for r in results if r[2])}/{len(results)} PASS")

    sys.exit(0 if all_pass else 1)


if __name__ == "__main__":
    main()
