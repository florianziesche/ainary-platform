# QUALITY RATCHET — Gotham-Ottobrunn als Gold Standard

## Problem
Unsere dossier.html-Dossiers sind "Briefings" (Level 2).
Gotham-Ottobrunn ist ein "Intelligence Dossier" (Level 5).
Die Lücke ist 10x.

## Neuer Standard (ab 2026-02-25)

### Entity-Depth (pro Kandidat)
| Field | Required | Min Count | Source |
|-------|----------|-----------|--------|
| properties[] | ✅ | 8 | key/val/src/type/fresh |
| connections[] | ✅ | 3 | type/target/year/evidence/label |
| controversies[] | 🟡 Amtsinhaber | 2 | title/text/evidence/severity/sources |
| contradictions[] | 🟡 Amtsinhaber | 1 | sagen_vs_tun Format |
| wahlergebnisse[] | ✅ | Letzte 2 Wahlen | ergebnis/details/wahlbeteiligung |
| zitate[] | ✅ | 3 | text/kontext/quelle/datum |
| karriere[] | ✅ | 5 | zeitraum/titel/beschreibung/quelle |
| trustScore{} | ✅ | 1 | gesamt/quellen/aktualitaet/tiefe |
| steckbrief{} | ✅ | 6 fields | alter/beruf/famstand/wohnort/partei/ausbildung |

### Sentiment-Depth
| Field | Required | Min |
|-------|----------|-----|
| topics[] | ✅ | 4 Topics |
| posts per topic | ✅ | 5 Posts |
| entity sentiment | ✅ | sent/trend/mentions/delta per entity |
| overall composite | ✅ | pct/label/n/trend |

### Forecast-Depth
| Field | Required | Min |
|-------|----------|-----|
| kandidaten[] | ✅ | min/max/zentral/conf per candidate |
| historie[] | ✅ | Last 2 elections |
| treiber.fuer/gegen | ✅ | 3 each |
| stichwahlSzenario | ✅ | Narrative text |

## Cross-Learning Rule
When a new city is built:
1. Load Gotham-Ottobrunn schema as reference
2. For every field in reference → check if new city has equivalent
3. Gap = quality deficit → auto-generate research queries
4. Score ONLY increases when fields are filled to Gotham-level

## Propagation
- Schema change here → auto_enrich.py detects gaps in ALL cities
- No city can be deployed below this standard (after grace period)
- Grace period: 7 days for existing cities to reach new standard
- New cities: must pass on first deploy

## Why No Entropy
Palantir's Ontology only grows. A field added to the Ontology is NEVER removed.
Same here:
- Gotham-Ottobrunn added `contradictions` → ALL cities must have it
- Gotham-Ottobrunn has 15 sentiment posts → ALL cities target 15
- Standard is a one-way ratchet: it can only tighten, never loosen

This is the Palantir principle: **the template IS the product.**
Every improvement to one city improves ALL cities.
