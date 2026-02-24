#!/usr/bin/env python3
"""
Momentum Index — Composite score from multiple signals.
Combines: Google Trends + Instagram Engagement Trend + Press Mentions.

Usage:
  python3 momentum_index.py                  # All known candidates
  python3 momentum_index.py --city nuernberg # Single city

Output: data/momentum.json + console report
"""

import json, sys, os, re
from datetime import datetime
from pathlib import Path

SOCIAL_DIR = Path("data/social")
MOMENTUM_FILE = Path("data/momentum.json")

# Candidates with known data
CANDIDATES = {
    "nuernberg": {
        "Marcus König": {"party": "CSU", "role": "OB", "ig_handle": "marcuskoenignbg",
            "ig_followers": 33323, "ig_engagement": 3.57, "ig_trend": 170,
            "google_trend_avg": 1.2, "google_trend_recent": 0},
        "Nasser Ahmed": {"party": "SPD", "role": "Herausforderer", "ig_handle": "nasser.spd",
            "ig_followers": 12023, "ig_engagement": 5.07, "ig_trend": 6,
            "google_trend_avg": 2.1, "google_trend_recent": 0},
    },
}


def calculate_momentum(candidate, city_context=None):
    """
    Momentum Index (0-100):
    - 30% Instagram Engagement Efficiency (engagement rate relative to followers)
    - 20% Instagram Growth Trend
    - 20% Google Trends (search interest)
    - 15% Posting Frequency (campaign activity)
    - 15% Cross-platform presence (FB, X, YouTube, TikTok, Website)
    """
    scores = {}
    
    # 1. Engagement Efficiency (30%)
    eng = candidate.get("ig_engagement", 0)
    # 1-2% = average, 3-5% = good, 5%+ = excellent
    if eng >= 5: scores["engagement"] = 100
    elif eng >= 3: scores["engagement"] = 70 + (eng - 3) * 15
    elif eng >= 1: scores["engagement"] = 30 + (eng - 1) * 20
    else: scores["engagement"] = eng * 30
    
    # 2. Growth Trend (20%)
    trend = candidate.get("ig_trend", 0)
    # Normalize: +100% = score 80, +50% = 60, 0% = 40, -50% = 20
    scores["growth"] = min(100, max(0, 40 + trend * 0.4))
    
    # 3. Google Trends (20%)
    gt = candidate.get("google_trend_avg", 0)
    # Relative within city — higher = more searched
    scores["search_interest"] = min(100, gt * 20)
    
    # 4. Posting Frequency (15%) — estimated from engagement data
    posts_per_week = candidate.get("posts_per_week", 3)  # default estimate
    if posts_per_week >= 7: scores["activity"] = 100
    elif posts_per_week >= 4: scores["activity"] = 70
    elif posts_per_week >= 2: scores["activity"] = 40
    else: scores["activity"] = 20
    
    # 5. Cross-platform (15%)
    platforms = 0
    if candidate.get("ig_followers", 0) > 0: platforms += 1
    if candidate.get("fb_followers", 0) > 0: platforms += 1
    if candidate.get("x_followers", 0) > 0: platforms += 1
    if candidate.get("youtube", False): platforms += 1
    if candidate.get("website", False): platforms += 1
    scores["cross_platform"] = min(100, platforms * 25)
    
    # Weighted composite
    momentum = (
        scores["engagement"] * 0.30 +
        scores["growth"] * 0.20 +
        scores["search_interest"] * 0.20 +
        scores["activity"] * 0.15 +
        scores["cross_platform"] * 0.15
    )
    
    return {
        "momentum_index": round(momentum, 1),
        "components": scores,
        "computed_at": datetime.now().isoformat(),
    }


def generate_report(city, candidates):
    """Generate momentum comparison for a city."""
    print(f"\n{'='*60}")
    print(f"📊 MOMENTUM INDEX — {city.upper()}")
    print(f"{'='*60}")
    
    results = []
    for name, data in candidates.items():
        m = calculate_momentum(data)
        results.append((name, data, m))
    
    # Sort by momentum
    results.sort(key=lambda x: x[2]["momentum_index"], reverse=True)
    
    for name, data, m in results:
        mi = m["momentum_index"]
        bar = "█" * int(mi / 5) + "░" * (20 - int(mi / 5))
        print(f"\n  {name} ({data['party']}, {data['role']})")
        print(f"  Momentum: [{bar}] {mi:.0f}/100")
        for comp, score in m["components"].items():
            mini_bar = "█" * int(score / 10)
            print(f"    {comp:20s} {mini_bar:10s} {score:.0f}")
    
    # Head-to-head
    if len(results) >= 2:
        r1, r2 = results[0], results[1]
        diff = r1[2]["momentum_index"] - r2[2]["momentum_index"]
        print(f"\n  ⚔️ {r1[0]} vs {r2[0]}: Momentum-Vorteil {diff:+.1f} Punkte")
        
        # Component comparison
        print(f"\n  Detailvergleich:")
        for comp in r1[2]["components"]:
            s1 = r1[2]["components"][comp]
            s2 = r2[2]["components"][comp]
            winner = "←" if s1 > s2 else "→" if s2 > s1 else "="
            print(f"    {comp:20s} {s1:5.0f} {winner} {s2:.0f}")
    
    return results


def main():
    all_results = {}
    
    if "--city" in sys.argv:
        city = sys.argv[sys.argv.index("--city") + 1]
        if city in CANDIDATES:
            all_results[city] = generate_report(city, CANDIDATES[city])
    else:
        for city, candidates in CANDIDATES.items():
            all_results[city] = generate_report(city, candidates)
    
    # Save
    output = {
        "_meta": {
            "generated": datetime.now().isoformat(),
            "method": "Composite: 30% IG Engagement + 20% IG Trend + 20% Google Trends + 15% Activity + 15% Cross-Platform",
            "cities": len(all_results),
        },
        "results": {}
    }
    
    for city, results in all_results.items():
        output["results"][city] = {
            name: {
                "momentum": m["momentum_index"],
                "party": data["party"],
                "components": m["components"],
            }
            for name, data, m in results
        }
    
    with open(MOMENTUM_FILE, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    
    print(f"\n💾 Saved: {MOMENTUM_FILE}")


if __name__ == "__main__":
    main()
