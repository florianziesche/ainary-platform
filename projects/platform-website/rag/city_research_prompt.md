# City Research Agent Prompt Template

You are researching the city of {CITY} for the Bayern Kommunalwahl 08.03.2026.

## Output
Write a JSON file to: `/Users/florianziesche/.openclaw/workspace/projects/platform-website/data/cities/{CITY_SLUG}.json`

## JSON Schema (mandatory fields)
```json
{
  "tenant": {
    "name": "Kampagnen-Intelligence {CITY}",
    "gemeinde": "{CITY}",
    "landkreis": "{LANDKREIS}",
    "typ": "kreisfrei|kreisangehoerig",
    "wahl": {"typ": "OB-Wahl|BM-Wahl", "datum": "08.03.2026", "stichwahl": "22.03.2026"}
  },
  "kb": {
    "{kandidat_slug}": {
      "name": "Full Name",
      "party": "CSU|SPD|Grüne|FW|AfD|FDP|...",
      "role": "current role",
      "bio": "2-3 sentences",
      "amtsinhaber": true/false,
      "social": {"website": "", "twitter": "", "instagram": "", "facebook": ""},
      "strengths": ["..."],
      "weaknesses": ["..."]
    }
  },
  "forecast": {
    "wahltermin": "08.03.2026",
    "stichwahl": "22.03.2026",
    "stichwahlWahrscheinlichkeit": 0.0-1.0,
    "stichwahlConf": 0-100,
    "kandidaten": [
      {"name": "...", "partei": "...", "erstwahlgang": "XX-YY%", "range": "XX-YY%"}
    ]
  },
  "stichwahl_prediction": {
    "probability": 0-100,
    "likely_matchup": "Name (Partei) vs Name (Partei)",
    "reason": "..."
  },
  "news": [
    {"title": "...", "source": "...", "date": "DD.MM.YYYY", "body": "50 words max"}
  ],
  "scenarios": [
    {"title": "Szenario A: ...", "probability": 0-100, "description": "..."}
  ],
  "quellenverzeichnis": [
    {"id": "S-01", "name": "...", "url": "...", "accessDate": "2026-02-28", "type": "official|media|social|academic"}
  ],
  "claim_ledger": [
    {"id": "CL-001", "claim": "...", "eija": "E|I|J|A", "source": "S-XX", "confidence": 0-100}
  ],
  "_meta": {
    "version": "1.0",
    "last_enriched": "2026-02-28",
    "agent": "research-agent-{CITY_SLUG}",
    "source_count": 0
  }
}
```

## Research Checklist
1. [ ] Official 2020 election results from kommunalwahl2020.bayern.de
2. [ ] Current Amtsinhaber: still running? (RULE-003)
3. [ ] All announced candidates with party affiliation
4. [ ] Social media handles VERIFIED via web_search (RULE-002)
5. [ ] Bürgermeister title verified against official city website (RULE-001)
6. [ ] Local newspaper coverage (min 5 articles)
7. [ ] Stadtrat composition
8. [ ] Population + key demographics
9. [ ] Major local issues/controversies
10. [ ] Google Trends comparison (if available)

## Prevention Rules (from Error Database)
- RULE-001: ALWAYS verify BM/OB title against official city website
- RULE-002: ALL social media handles MUST be verified via web_search. No guessing.
- RULE-003: Check if current Amtsinhaber is running again BEFORE building profile
- RULE-004: 2020 results MUST come from kommunalwahl2020.bayern.de only
- RULE-005: Forecast percentages must sum to 95-105%

## Quality Gate
- Minimum 30 sources in quellenverzeichnis
- Minimum 3 kandidaten in kb
- All claims in claim_ledger have EIJA label
- All sources have URL
- forecast.stichwahlConf is honest (don't inflate)
