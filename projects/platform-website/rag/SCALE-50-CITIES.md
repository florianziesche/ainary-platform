# 50-City Scale Architecture
*Target: 50 Städte, 5000+ Quellen, Error-Learning Database*
*Created: 2026-02-28*

## Why This Works

### Math
- 10 cities × 30 sources = 300 (current)
- 50 cities × 100 sources = 5,000 (target)
- Each city: ~45min agent time = 50 × 45min = 37.5 hours agent time
- With 10 parallel agents: ~4 hours wall clock
- Cost: ~$15-25 in API calls (Sonnet for research, Haiku for extraction)

### Compound Intelligence Loop
```
City N research
    → finds pattern P
        → P gets tested against City N+1...N+10
            → if P holds: verified-truth (weight 2x)
            → if P fails: contradiction registered
                → contradiction triggers re-research on original city
                    → system gets DENSER not LARGER
```

### Error-Learning Database (from "100 Agents" article)
Every agent run produces:
1. **Claims** with EIJA labels
2. **Sources** with Admiralty ratings (A1-C3)
3. **Errors** (contradictions, failed verifications, stale data)
4. **Patterns** (cross-city insights)

Errors are NOT deleted. They become training data:
- Error Type → Prevention Rule → Applied to all future runs
- Example: "Agent hallucinated Instagram handle" → Rule: "Verify ALL social handles via web_search before including" → Injected into every agent's context

## 5-Ring Architecture

### Ring 1: City Core (per city, ~30 sources)
- Kandidaten-Profile (bio, party, history, social)
- Wahlergebnisse 2020 (official Statistik Bayern)
- Lokale Medienlandschaft (Zeitungen, TV, Radio)
- Stadtrat-Zusammensetzung
- Bevölkerungsstruktur

### Ring 2: Deep Context (per city, ~40 sources)
- Kontroversen/Risikosignale (Zeitungsarchive)
- Finanzlage der Kommune (Haushalt, Schulden)
- Infrastrukturprojekte (was bewegt die Stadt?)
- Google Trends (Kandidaten-Vergleich)
- Social Media Präsenz (verifiziert!)

### Ring 3: Cross-City Patterns (shared, ~30 sources)
- CSU vs SPD vs Grüne Amtsinhaber-Verteidigungsrate
- Stichwahl-Wahrscheinlichkeit nach Kandidatenzahl
- Wahlbeteiligung als Funktion von Wetter + Briefwahl
- Medien-Effekt auf Ergebnisse
- BAFA/Fördermittel-Korrelation mit Amtsinhaber-Bonus

### Ring 4: National Context (shared, ~20 sources)
- Bundestrend-Effekt auf Kommunalwahlen
- Partei-Umfragen als Proxy
- Medienzyklus-Effekte
- Demografie-Shifts

### Ring 5: Meta/Quality (system-level)
- Error-Learning Database
- Source Quality Rankings
- Agent Performance Scores
- Prediction Accuracy Tracking

## Error-Learning Database Schema

```json
{
  "error_id": "ERR-2026-0042",
  "timestamp": "2026-02-28T19:00:00Z",
  "city": "bamberg",
  "agent_id": "research-agent-bamberg-v3",
  "error_type": "HALLUCINATION|STALE_DATA|WRONG_ATTRIBUTION|MISSING_SOURCE|CONTRADICTION",
  "severity": "HIGH|MEDIUM|LOW",
  "claim": "Glüsenkamp ist 2. Bürgermeister",
  "actual": "Glüsenkamp ist 3. Bürgermeister",
  "source_that_caught_it": "stadt.bamberg.de",
  "prevention_rule": "Always verify Bürgermeister title against official city website",
  "rule_applied_to": ["ALL_CITIES"],
  "status": "ACTIVE",
  "prevented_count": 0
}
```

## Execution Plan

### Wave 1: Bayern Kommunalwahl (40 cities) — Priority
All cities with OB/BM elections on 08.03.2026.
Source: Statistik Bayern PDF (already parsed, 213 Gemeinden >10K)
Filter: Focus on kreisfreie Städte + Große Kreisstädte = ~40

### Wave 2: Sachsen + NRW (10 cities) — Expansion
Prove the system works beyond Bayern.

### Agent Prompt Template
Each agent gets:
1. City name + basic data
2. Ring 1-2 research checklist (what to find)
3. Error-Learning Rules (all active prevention rules)
4. Output Schema (city JSON format)
5. Quality Gate (minimum 30 sources, 5+ properties per entity)

### Quality Pipeline
1. Agent researches → produces city JSON
2. Validator checks schema compliance
3. Cross-reference against error database
4. Contradiction check against existing cities
5. Source verification (are URLs real?)
6. Human spot-check (Florian reviews 3-5 cities)
7. Deploy to platform

## Metrics
- Sources per city: target 100, minimum 30
- Error rate: track per agent run, target <5%
- Prevention rule effectiveness: how many errors prevented
- Cross-city pattern confidence: weighted by city count
- Prediction accuracy: verified post-election
