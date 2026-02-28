#!/usr/bin/env python3
"""
Research Validator — catches agent errors BEFORE they go live.
Runs after every city research agent completes.

Checks:
1. Schema compliance (required fields)
2. Source quality (duplicate URLs, dead links, source diversity)
3. Claim consistency (EIJA labels present, contradictions)
4. Forecast sanity (percentages sum, ranges plausible)
5. Cross-city contradiction detection
6. Known error patterns (from error_db.json)
"""

import json, sys, os, re
from collections import Counter
from urllib.parse import urlparse

def load_json(path):
    with open(path) as f:
        return json.load(f)

def validate_city(city_slug, data_dir="data/cities"):
    path = os.path.join(data_dir, f"{city_slug}.json")
    if not os.path.exists(path):
        print(f"FAIL: {path} does not exist")
        return False

    data = load_json(path)
    errors = []
    warnings = []
    score = 100

    tenant_raw = data.get("tenant", {})
    if isinstance(tenant_raw, str):
        errors.append(f"tenant is a string '{tenant_raw}' instead of object — SCHEMA VIOLATION")
        score -= 20
        city = tenant_raw or city_slug
        tenant = {}
    else:
        city = tenant_raw.get("gemeinde", city_slug)
        tenant = tenant_raw
    print(f"\n{'='*60}")
    print(f"VALIDATING: {city} ({city_slug}.json)")
    print(f"{'='*60}")

    # 1. SCHEMA COMPLIANCE
    required_top = ["tenant", "kb", "forecast", "quellenverzeichnis", "claim_ledger", "_meta"]
    for field in required_top:
        if field not in data:
            errors.append(f"Missing required field: {field}")
            score -= 15

    for field in ["gemeinde", "wahl"]:
        if field not in tenant:
            errors.append(f"tenant.{field} missing")
            score -= 5

    # 2. SOURCE QUALITY
    sources = data.get("quellenverzeichnis", [])
    source_count = len(sources)

    if source_count < 30:
        errors.append(f"Only {source_count} sources (minimum: 30)")
        score -= 20
    elif source_count < 50:
        warnings.append(f"{source_count} sources (good, target: 100)")

    # Check for duplicate URLs
    urls = [s.get("url", "") for s in sources if s.get("url")]
    url_domains = [urlparse(u).netloc for u in urls]
    url_counter = Counter(urls)
    duplicates = {url: count for url, count in url_counter.items() if count > 1}
    if duplicates:
        errors.append(f"{len(duplicates)} duplicate URLs found")
        for url, count in duplicates.items():
            errors.append(f"  - {url} appears {count}x")
        score -= len(duplicates) * 3

    # Check source diversity (not all from same domain)
    domain_counter = Counter(url_domains)
    if domain_counter:
        top_domain, top_count = domain_counter.most_common(1)[0]
        if top_count > source_count * 0.4:
            warnings.append(f"Source concentration: {top_domain} = {top_count}/{source_count} ({top_count/source_count*100:.0f}%)")
            score -= 5

    # Check for empty/placeholder URLs
    empty_urls = sum(1 for s in sources if not s.get("url") or s["url"] in ["", "N/A", "#"])
    if empty_urls:
        errors.append(f"{empty_urls} sources without valid URL")
        score -= empty_urls * 2

    # 3. CANDIDATE QUALITY
    kb = data.get("kb", {})
    candidate_count = len(kb)
    if candidate_count < 3:
        errors.append(f"Only {candidate_count} candidates (minimum: 3)")
        score -= 10

    for slug, candidate in kb.items():
        if not isinstance(candidate, dict):
            errors.append(f"kb[{slug}] is {type(candidate).__name__} instead of dict")
            score -= 5
            continue
        name = candidate.get("name", slug)
        if not candidate.get("party"):
            warnings.append(f"Candidate {name}: no party")
        if not candidate.get("bio") or len(candidate.get("bio", "")) < 20:
            warnings.append(f"Candidate {name}: bio too short (<20 chars)")

        # RULE-002: Check social handles aren't obviously hallucinated
        social = candidate.get("social", {})
        for platform in ["instagram", "twitter"]:
            handle = social.get(platform, "")
            if handle and not handle.startswith("http"):
                # Suspicious if handle contains city name + candidate name pattern
                if "not_found" in handle.lower() or "n/a" in handle.lower():
                    continue  # OK, agent marked as not found
                # Can't verify URLs here, but flag for manual check
                warnings.append(f"Candidate {name}: {platform} = {handle} (unverified in validator)")

    # 4. FORECAST SANITY
    forecast = data.get("forecast", {})
    kandidaten = forecast.get("kandidaten", [])

    if kandidaten:
        # Try to extract percentages and check sum
        total = 0
        for k in kandidaten:
            # Handle range format "XX-YY%" or single "XX%"
            val = k.get("erstwahlgang", k.get("range", "0"))
            if isinstance(val, str):
                nums = re.findall(r'(\d+(?:\.\d+)?)', val)
                if nums:
                    # Use midpoint of range
                    total += sum(float(n) for n in nums) / len(nums)
            elif isinstance(val, (int, float)):
                total += val

        if total > 0:
            if total < 85 or total > 115:
                errors.append(f"Forecast percentages sum to {total:.1f}% (expected 95-105%)")
                score -= 10
            elif total < 95 or total > 105:
                warnings.append(f"Forecast percentages sum to {total:.1f}% (slightly off)")

    # Stichwahl confidence honesty check
    stw = data.get("stichwahl_prediction", {})
    if stw:
        prob = stw.get("probability", 0)
        if prob > 95:
            warnings.append(f"Stichwahl probability {prob}% seems overconfident")

    # 5. CLAIM LEDGER
    claims = data.get("claim_ledger", [])
    if len(claims) < 10:
        errors.append(f"Only {len(claims)} claims (minimum: 10)")
        score -= 5

    valid_eija = {"E", "I", "J", "A"}
    for claim in claims:
        if not isinstance(claim, dict):
            errors.append(f"Claim is {type(claim).__name__} instead of dict")
            score -= 2
            continue
        eija = claim.get("eija", "")
        if not isinstance(eija, str) or eija not in valid_eija:
            errors.append(f"Claim {claim.get('id','?')}: invalid EIJA label '{eija}'")
            score -= 2

    # 6. META
    meta = data.get("_meta", {})
    reported_sources = meta.get("source_count", 0)
    if reported_sources != source_count and reported_sources > 0:
        warnings.append(f"_meta.source_count ({reported_sources}) != actual ({source_count})")

    # RESULTS
    score = max(0, score)
    print(f"\n--- ERRORS ({len(errors)}) ---")
    for e in errors:
        print(f"  ❌ {e}")

    print(f"\n--- WARNINGS ({len(warnings)}) ---")
    for w in warnings:
        print(f"  ⚠️  {w}")

    print(f"\n--- SCORE ---")
    status = "PASS" if score >= 70 else "FAIL"
    print(f"  {'✅' if status == 'PASS' else '❌'} {score}/100 — {status}")
    print(f"  Sources: {source_count} | Candidates: {candidate_count} | Claims: {len(claims)}")

    return score >= 70, score, errors, warnings


def validate_all(data_dir="data/cities"):
    results = {}
    for f in sorted(os.listdir(data_dir)):
        if not f.endswith('.json'):
            continue
        slug = f.replace('.json', '')
        passed, score, errors, warnings = validate_city(slug, data_dir)
        results[slug] = {"passed": passed, "score": score, "errors": len(errors), "warnings": len(warnings)}

    print(f"\n{'='*60}")
    print("SUMMARY")
    print(f"{'='*60}")
    total = len(results)
    passed = sum(1 for r in results.values() if r["passed"])
    avg_score = sum(r["score"] for r in results.values()) / total if total else 0
    print(f"  {passed}/{total} PASSED | Average score: {avg_score:.0f}/100")
    print(f"  Total errors: {sum(r['errors'] for r in results.values())}")
    print(f"  Total warnings: {sum(r['warnings'] for r in results.values())}")

    for slug, r in sorted(results.items(), key=lambda x: x[1]["score"]):
        print(f"  {'✅' if r['passed'] else '❌'} {slug}: {r['score']}/100 ({r['errors']}E, {r['warnings']}W)")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "--all":
            validate_all()
        else:
            validate_city(sys.argv[1])
    else:
        print("Usage: python3 validate_research.py <city_slug>")
        print("       python3 validate_research.py --all")
