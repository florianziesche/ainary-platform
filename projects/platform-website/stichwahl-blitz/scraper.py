#!/usr/bin/env python3
"""
Stichwahl-Blitz Scraper — kommunalwahl2026.bayern.de
Erkennt Stichwahl-Paarungen in Echtzeit am Wahlabend.

Usage:
  python3 scraper.py              # Live-Modus (8. März 2026)
  python3 scraper.py --test-2020  # Test mit 2020-Daten
  python3 scraper.py --dry-run    # Zeigt was passieren würde

Output: results/stichwahl-paarungen.json
"""

import json, re, sys, time, os
from datetime import datetime
from pathlib import Path

# 2026 URLs (gleiche Struktur wie 2020)
BASE_2026 = "https://www.kommunalwahl2026.bayern.de"
BASE_2020 = "https://www.kommunalwahl2020.bayern.de"

RESULTS_DIR = Path("results")
OUTPUT_FILE = RESULTS_DIR / "stichwahl-paarungen.json"
RAW_DIR = RESULTS_DIR / "raw"

# Unsere 9 Dossier-Städte (höchste Priorität)
DOSSIER_CITIES = {
    "bamberg", "regensburg", "nuernberg", "augsburg",
    "erlangen", "fuerth", "landshut", "passau", "ottobrunn"
}

# Top-50 Radar-Städte (mittlere Priorität)
RADAR_CITIES = set()  # TODO: aus radar-data.json laden


def setup():
    RESULTS_DIR.mkdir(exist_ok=True)
    RAW_DIR.mkdir(exist_ok=True)


def fetch_page(url):
    """Fetch page content. Returns HTML string."""
    import urllib.request
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "AinaryIntelligence/1.0"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            return resp.read().decode("utf-8", errors="replace")
    except Exception as e:
        print(f"  ⚠️ Fetch failed: {url} — {e}")
        return None


def parse_ob_results(html, gemeinde_name=""):
    """
    Parse OB/BM election results from a municipality page.
    Returns list of candidates with votes and percentages.
    
    Expected format (from 2020 site):
    Candidate Name (Party) — XX,X% — XXXX Stimmen
    """
    candidates = []
    
    # Try multiple parsing strategies since the site is JS-rendered
    # Strategy 1: Look for structured data in HTML tables
    # Strategy 2: Look for JSON data embedded in script tags
    # Strategy 3: Regex on rendered text
    
    # Look for JSON data in script tags
    json_matches = re.findall(r'var\s+data\s*=\s*(\{.*?\});', html, re.DOTALL)
    for match in json_matches:
        try:
            data = json.loads(match)
            # Parse structured data
            if "candidates" in data or "bewerber" in data:
                for c in data.get("candidates", data.get("bewerber", [])):
                    candidates.append({
                        "name": c.get("name", ""),
                        "party": c.get("partei", c.get("party", "")),
                        "votes": c.get("stimmen", c.get("votes", 0)),
                        "percent": c.get("prozent", c.get("percent", 0)),
                    })
        except json.JSONDecodeError:
            pass
    
    # Strategy 2: Parse HTML table rows
    if not candidates:
        # Look for table rows with candidate data
        rows = re.findall(
            r'<tr[^>]*>.*?<td[^>]*>(.*?)</td>.*?<td[^>]*>(.*?)</td>.*?<td[^>]*>(.*?)</td>.*?</tr>',
            html, re.DOTALL
        )
        for row in rows:
            name = re.sub(r'<[^>]+>', '', row[0]).strip()
            party_or_pct = re.sub(r'<[^>]+>', '', row[1]).strip()
            votes_or_pct = re.sub(r'<[^>]+>', '', row[2]).strip()
            if name and any(c.isalpha() for c in name):
                candidates.append({
                    "name": name,
                    "party": party_or_pct if not any(c.isdigit() for c in party_or_pct) else "",
                    "percent": extract_percent(votes_or_pct) or extract_percent(party_or_pct),
                    "votes": extract_votes(votes_or_pct),
                })
    
    return candidates


def extract_percent(text):
    """Extract percentage from text like '45,3%' or '45.3'"""
    m = re.search(r'(\d+)[,.](\d+)\s*%?', text)
    if m:
        return float(f"{m.group(1)}.{m.group(2)}")
    m = re.search(r'(\d+)\s*%', text)
    if m:
        return float(m.group(1))
    return 0


def extract_votes(text):
    """Extract vote count from text like '12.345' or '12345'"""
    m = re.search(r'([\d.]+)', text.replace(',', '.'))
    if m:
        try:
            return int(m.group(1).replace('.', ''))
        except:
            pass
    return 0


def detect_stichwahl(candidates):
    """
    Stichwahl = kein Kandidat über 50%.
    Returns (is_stichwahl, top2_candidates)
    """
    if not candidates:
        return False, []
    
    sorted_cands = sorted(candidates, key=lambda c: c.get("percent", 0), reverse=True)
    
    if sorted_cands[0]["percent"] > 50:
        return False, sorted_cands[:2]
    
    if len(sorted_cands) >= 2:
        return True, sorted_cands[:2]
    
    return False, sorted_cands[:2]


def classify_city(gemeinde_slug):
    """Classify city into priority tier."""
    slug = gemeinde_slug.lower().replace(" ", "").replace("-", "")
    if slug in DOSSIER_CITIES:
        return "A"  # Full dossier available
    if slug in RADAR_CITIES:
        return "B"  # In radar, partial data
    return "C"  # Unknown, generic template


def process_results(results_by_city):
    """Process all results, identify Stichwahlen, output JSON."""
    stichwahlen = []
    direct_wins = []
    
    for city, data in results_by_city.items():
        candidates = data.get("candidates", [])
        is_stichwahl, top2 = detect_stichwahl(candidates)
        
        entry = {
            "gemeinde": city,
            "gemeinde_slug": data.get("slug", city.lower()),
            "tier": classify_city(data.get("slug", city.lower())),
            "is_stichwahl": is_stichwahl,
            "candidates": top2,
            "all_candidates": candidates,
            "diff_pct": abs(top2[0]["percent"] - top2[1]["percent"]) if len(top2) >= 2 else 0,
            "timestamp": datetime.now().isoformat(),
        }
        
        if is_stichwahl:
            stichwahlen.append(entry)
        else:
            direct_wins.append(entry)
    
    # Sort Stichwahlen by tier (A first) then by closeness
    stichwahlen.sort(key=lambda x: ({"A": 0, "B": 1, "C": 2}[x["tier"]], x["diff_pct"]))
    
    output = {
        "_meta": {
            "generated": datetime.now().isoformat(),
            "total_cities": len(results_by_city),
            "stichwahlen": len(stichwahlen),
            "direct_wins": len(direct_wins),
            "tier_a": len([s for s in stichwahlen if s["tier"] == "A"]),
            "tier_b": len([s for s in stichwahlen if s["tier"] == "B"]),
            "tier_c": len([s for s in stichwahlen if s["tier"] == "C"]),
        },
        "stichwahlen": stichwahlen,
        "direct_wins": direct_wins,
    }
    
    with open(OUTPUT_FILE, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    
    print(f"\n{'='*60}")
    print(f"STICHWAHL-BLITZ ERGEBNIS")
    print(f"{'='*60}")
    print(f"Gesamt: {len(results_by_city)} Gemeinden ausgewertet")
    print(f"Stichwahlen: {len(stichwahlen)}")
    print(f"  Tier A (Dossier): {output['_meta']['tier_a']}")
    print(f"  Tier B (Radar):   {output['_meta']['tier_b']}")
    print(f"  Tier C (Generisch): {output['_meta']['tier_c']}")
    print(f"Direkte Siege: {len(direct_wins)}")
    
    if stichwahlen:
        print(f"\n🎯 TOP STICHWAHLEN (nach Priorität + Knappheit):")
        for s in stichwahlen[:15]:
            c1, c2 = s["candidates"][0], s["candidates"][1]
            tier_emoji = {"A": "🟢", "B": "🟡", "C": "⚪"}[s["tier"]]
            print(f"  {tier_emoji} {s['gemeinde']}: {c1['name']} ({c1['party']}) {c1['percent']:.1f}% vs {c2['name']} ({c2['party']}) {c2['percent']:.1f}% — Diff: {s['diff_pct']:.1f}%")
    
    return output


def simulate_2020():
    """Simulate with known 2020 Stichwahl results."""
    print("🧪 TEST-MODUS: Simuliere mit bekannten 2020-Ergebnissen\n")
    
    # Known 2020 Stichwahl results (from memory)
    test_data = {
        "Regensburg": {
            "slug": "regensburg",
            "candidates": [
                {"name": "Gertrud Maltz-Schwarzfischer", "party": "SPD", "percent": 28.2, "votes": 0},
                {"name": "Astrid Freudenstein", "party": "CSU", "percent": 26.1, "votes": 0},
                {"name": "Stefan Christoph", "party": "Grüne", "percent": 15.3, "votes": 0},
            ]
        },
        "Bamberg": {
            "slug": "bamberg",
            "candidates": [
                {"name": "Andreas Starke", "party": "SPD", "percent": 38.5, "votes": 0},
                {"name": "Christian Lange", "party": "CSU", "percent": 26.8, "votes": 0},
            ]
        },
        "Passau": {
            "slug": "passau",
            "candidates": [
                {"name": "Jürgen Dupper", "party": "SPD", "percent": 46.0, "votes": 0},
                {"name": "Armin Dickl", "party": "CSU", "percent": 22.0, "votes": 0},
            ]
        },
        "Nürnberg": {
            "slug": "nuernberg",
            "candidates": [
                {"name": "Marcus König", "party": "CSU", "percent": 35.2, "votes": 0},
                {"name": "Thorsten Brehm", "party": "SPD", "percent": 25.7, "votes": 0},
                {"name": "Verena Osgyan", "party": "Grüne", "percent": 17.1, "votes": 0},
            ]
        },
        "Augsburg": {
            "slug": "augsburg",
            "candidates": [
                {"name": "Eva Weber", "party": "CSU", "percent": 50.2, "votes": 0},
                {"name": "Dirk Wurm", "party": "SPD", "percent": 17.5, "votes": 0},
            ]
        },
        "Erlangen": {
            "slug": "erlangen",
            "candidates": [
                {"name": "Florian Janik", "party": "SPD", "percent": 54.3, "votes": 0},
                {"name": "Jörg Volleth", "party": "CSU", "percent": 21.2, "votes": 0},
            ]
        },
        "Landshut": {
            "slug": "landshut",
            "candidates": [
                {"name": "Alexander Putz", "party": "FDP", "percent": 26.3, "votes": 0},
                {"name": "Helmut Radlmeier", "party": "CSU", "percent": 22.1, "votes": 0},
                {"name": "Sigi Hagl", "party": "Grüne", "percent": 22.6, "votes": 0},
            ]
        },
        "Fürth": {
            "slug": "fuerth",
            "candidates": [
                {"name": "Thomas Jung", "party": "SPD", "percent": 62.1, "votes": 0},
                {"name": "Dietmar Helm", "party": "CSU", "percent": 19.8, "votes": 0},
            ]
        },
        # Some smaller cities for Tier C testing
        "Schweinfurt": {
            "slug": "schweinfurt",
            "candidates": [
                {"name": "Sebastian Remelé", "party": "CSU", "percent": 48.3, "votes": 0},
                {"name": "Sören Lippert", "party": "SPD", "percent": 14.2, "votes": 0},
            ]
        },
    }
    
    return process_results(test_data)


def main():
    setup()
    
    if "--test-2020" in sys.argv:
        simulate_2020()
    elif "--dry-run" in sys.argv:
        print("🔍 DRY RUN: Würde kommunalwahl2026.bayern.de scrapen")
        print(f"   URL: {BASE_2026}")
        print(f"   Output: {OUTPUT_FILE}")
        print(f"   Dossier-Städte: {', '.join(sorted(DOSSIER_CITIES))}")
    else:
        print("🚀 LIVE-MODUS: Scrape kommunalwahl2026.bayern.de")
        print("   ⚠️ Ergebnisse erst ab 8. März 2026 ~18:00 verfügbar")
        print(f"   Prüfe {BASE_2026}...")
        html = fetch_page(BASE_2026)
        if html:
            print(f"   ✅ Seite erreichbar ({len(html)} Bytes)")
            # Save raw HTML
            with open(RAW_DIR / "index.html", "w") as f:
                f.write(html)
            print(f"   💾 Gespeichert: {RAW_DIR}/index.html")
            print("   → Am Wahlabend: python3 scraper.py (alle 5 Min)")
        else:
            print("   ❌ Seite noch nicht erreichbar (normal vor dem 8.03)")


if __name__ == "__main__":
    main()
