# Bayern Kommunalwahl 2026 — Intelligence Pipeline

## Quickstart (für LLMs und Menschen)

```bash
# Status aller 50 Städte
python3 cli.py status

# Eine Stadt validieren
python3 cli.py validate muenchen

# Alle Städte validieren + Dashboard
python3 cli.py validate-all

# Cross-City Analyse
python3 cli.py analyze

# Monte Carlo für eine Stadt
python3 cli.py simulate muenchen

# Neue Stadt researchen (spawnt Sub-Agent)
python3 cli.py research aichach

# Scorecard generieren
python3 cli.py scorecard
```

## Architektur

```
rag/
├── README.md              ← DU BIST HIER
├── cli.py                 ← Einziger Einstiegspunkt (alle Commands)
├── db.py                  ← SQLite Wrapper (Single Source of Truth)
├── normalize_city.py      ← Schema-Fixes (tenant, kb, news)
├── validate_research.py   ← Score 0-100 pro Stadt
├── learning_db.py         ← Legacy DB interface (wird durch db.py ersetzt)
├── intelligence.py        ← Cross-City Analyse + Monte Carlo
├── learning.db            ← SQLite Database
└── BEIPACKZETTEL.md       ← Error Learning (procedural memory)

data/
├── cities/*.json          ← 50 Stadt-Dossiers (Rohdaten + Intelligence)
├── election-scorecard.json← Testbare Predictions
└── ontology.json          ← Entity-Relationships
```

## Datenbank-Schema (learning.db)

```sql
cities          — 50 Einträge (slug, name, typ, wahl_typ, score)
sources         — 1.730 Quellen (id, city, name, url, type, domain)
claims          — 939 Claims (id, city, claim, eija, tier, confidence, source)
candidates      — 299 Kandidaten (id, city, name, party, role, amtsinhaber, result_2020)
errors          — Dokumentierte Fehler
prevention_rules— 13 Regeln (pattern → prevention)
agent_runs      — Audit Trail
patterns        — Auto-detected Cross-City Patterns
```

## EIJA-Labels
- **E** (Evidence): Verifizierter Fakt (Wahlergebnis, offizielle Quelle)
- **I** (Inference): Logische Ableitung aus Fakten
- **J** (Judgment): Einschätzung/Prognose
- **A** (Assumption): Unbelegte Annahme

## Knowledge Tiers
- **CORE**: Amtliche Wahlergebnisse, offizielle Daten
- **VERIFIED**: Kandidaten-Bestätigungen, Partei-Nominierungen
- **INFERRED**: Forecast-Schätzungen, Trend-Analysen
- **EPHEMERAL**: Einzelne News, Tages-Kontext

## Pipeline (3-Step, mandatory nach jedem Agent-Run)
```
Agent Output → normalize_city.py → validate_research.py → db.py ingest
```

## Bekannte Limitationen
- Monte Carlo basiert auf Agent-Schätzungen, nicht auf Umfragen
- 76% Sekundärquellen (Medien), 19% Primär (offiziell), 5% Wikipedia
- EIJA-Labels sind Agent-generiert, nicht manuell verifiziert
- Kein Backtest gegen 2020-Ergebnisse
- "Stichwahl ja/nein" ist die einzige robuste MC-Aussage
