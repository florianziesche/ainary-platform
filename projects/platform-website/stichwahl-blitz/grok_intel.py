#!/usr/bin/env python3
"""
Grok Intelligence — Real-time X/Twitter analysis via xAI API.
Grok has LIVE access to X posts — no other LLM can do this.

Usage:
  python3 grok_intel.py "Kommunalwahl Nürnberg"
  python3 grok_intel.py --candidates nuernberg
  python3 grok_intel.py --wahlnacht          # Live monitoring mode

Requires: XAI_API_KEY environment variable
"""

import json, sys, os
from datetime import datetime
from pathlib import Path

API_KEY = os.environ.get("XAI_API_KEY", "")
API_URL = "https://api.x.ai/v1/chat/completions"
MODEL = "grok-4-1-fast-non-reasoning"  # Cheapest: $0.20/M in, $0.50/M out
OUTPUT_DIR = Path("data/grok-intel")


def query_grok(prompt, system_prompt=None):
    """Query Grok API — returns response text."""
    import urllib.request
    
    if not API_KEY:
        print("❌ XAI_API_KEY not set. Run: export XAI_API_KEY=xai-YOUR_KEY")
        return None
    
    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": prompt})
    
    payload = json.dumps({
        "model": MODEL,
        "messages": messages,
        "temperature": 0.3,
    }).encode()
    
    req = urllib.request.Request(
        API_URL,
        data=payload,
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        },
    )
    
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read())
            return data["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"❌ Grok API error: {e}")
        return None


SYSTEM_PROMPT = """Du bist ein politischer Daten-Analyst. Du hast Zugang zu Echtzeit-X/Twitter-Daten.
Antworte strukturiert in JSON-Format. Keine Prosa. Nur Fakten + Quellen.
Wenn du keine Daten findest, sag "NO_DATA" statt zu halluzinieren."""


def analyze_candidate_mentions(city, candidates):
    """Ask Grok about recent X mentions of candidates."""
    prompt = f"""Analysiere die aktuellen X/Twitter-Erwähnungen für die Kommunalwahl in {city}:

Kandidaten: {', '.join(candidates)}

Beantworte als JSON:
{{
  "city": "{city}",
  "analyzed_at": "jetzt",
  "candidates": [
    {{
      "name": "...",
      "x_mentions_24h": <Anzahl Erwähnungen in den letzten 24h>,
      "sentiment": "positiv/neutral/negativ/gemischt",
      "top_topics": ["...", "..."],
      "notable_tweets": [
        {{"author": "@...", "text": "...", "likes": X, "retweets": X}}
      ],
      "trending_hashtags": ["..."]
    }}
  ],
  "overall_buzz": <1-100>,
  "key_narratives": ["..."],
  "prediction_signal": "..."
}}"""
    
    result = query_grok(prompt, SYSTEM_PROMPT)
    if result:
        print(f"\n📊 GROK INTELLIGENCE: {city}")
        print(result)
        
        # Save
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        outfile = OUTPUT_DIR / f"{city.lower()}-{datetime.now().strftime('%Y%m%d-%H%M')}.json"
        with open(outfile, "w") as f:
            f.write(result)
        print(f"\n💾 Saved: {outfile}")
    
    return result


def search_election_discourse(query):
    """Free-form search of election-related X discourse."""
    prompt = f"""Durchsuche aktuelle X/Twitter-Posts nach: "{query}"

Finde die relevantesten Posts der letzten 7 Tage. Beantworte als JSON:
{{
  "query": "{query}",
  "total_posts_estimated": <Schätzung>,
  "sentiment_breakdown": {{"positiv": X, "neutral": X, "negativ": X}},
  "top_posts": [
    {{"author": "@...", "text": "...", "likes": X, "date": "...", "url": "..."}}
  ],
  "key_themes": ["..."],
  "influencers_discussing": ["@...", "@..."],
  "momentum": "steigend/fallend/stabil"
}}"""
    
    result = query_grok(prompt, SYSTEM_PROMPT)
    if result:
        print(f"\n🔍 GROK SEARCH: \"{query}\"")
        print(result)
    return result


def wahlnacht_monitor(cities):
    """Live monitoring mode for election night."""
    prompt = f"""LIVE-ANALYSE: Kommunalwahl Bayern 2026

Durchsuche X/Twitter nach ALLEN aktuellen Posts über die Kommunalwahl in diesen Städten:
{', '.join(cities)}

Beantworte als JSON:
{{
  "timestamp": "jetzt",
  "cities": [
    {{
      "name": "...",
      "buzz_level": <1-100>,
      "latest_results_mentioned": "...",
      "stichwahl_mentioned": true/false,
      "candidate_mentions": [{{"name": "...", "count": X, "sentiment": "..."}}],
      "notable_posts": [{{"text": "...", "author": "@...", "likes": X}}]
    }}
  ],
  "overall_narrative": "...",
  "trending_hashtags": ["..."]
}}"""
    
    result = query_grok(prompt, SYSTEM_PROMPT)
    if result:
        print(f"\n🗳️ WAHLNACHT LIVE MONITOR")
        print(result)
    return result


# City-candidate mapping
CITY_CANDIDATES = {
    "Nürnberg": ["Marcus König CSU", "Nasser Ahmed SPD", "Britta Walthelm Grüne"],
    "Bamberg": ["Melanie Huml CSU", "Jonas Glüsenkamp Grüne", "Jonas Niedermaier SPD"],
    "Augsburg": ["Eva Weber CSU", "Martina Wild Grüne", "Florian Freund SPD"],
    "Regensburg": ["Astrid Freudenstein CSU", "Gertrud Maltz-Schwarzfischer SPD"],
    "Erlangen": ["Jörg Volleth CSU", "Nora Linhart Grüne"],
    "Fürth": ["Thomas Jung SPD", "Ammon CSU"],
    "Passau": ["Stefanie Auer Grüne", "Armin Dickl CSU"],
    "Landshut": ["Thomas Haslinger CSU", "diverse Kandidaten"],
}


def main():
    if not API_KEY:
        print("❌ XAI_API_KEY not set.")
        print("   1. Go to https://console.x.ai")
        print("   2. Create API Key")
        print("   3. export XAI_API_KEY=xai-YOUR_KEY")
        return
    
    if "--wahlnacht" in sys.argv:
        wahlnacht_monitor(list(CITY_CANDIDATES.keys()))
    elif "--candidates" in sys.argv:
        city = sys.argv[sys.argv.index("--candidates") + 1]
        for c, cands in CITY_CANDIDATES.items():
            if city.lower() in c.lower():
                analyze_candidate_mentions(c, cands)
                break
    elif len(sys.argv) > 1:
        query = " ".join(sys.argv[1:])
        search_election_discourse(query)
    else:
        print("Usage:")
        print('  python3 grok_intel.py "Kommunalwahl Nürnberg"')
        print("  python3 grok_intel.py --candidates nuernberg")
        print("  python3 grok_intel.py --wahlnacht")
        print(f"\nCities: {', '.join(CITY_CANDIDATES.keys())}")
        print(f"Model: {MODEL} (${0.20}/M in, ${0.50}/M out)")


if __name__ == "__main__":
    main()
