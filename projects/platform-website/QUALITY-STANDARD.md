# Ainary Quality Standard — Dossier Generation

**Version:** 1.0
**Date:** 2026-02-24
**Status:** ENFORCED — kein Dossier ohne Compliance

---

## Minimum Quality Gate (NICHT OPTIONAL)

Jedes Stadt-Dossier MUSS folgende Kriterien erfüllen bevor es veröffentlicht oder versendet wird:

### 1. Schema Compliance
```json
{
  "tenant": {
    "gemeinde": "REQUIRED — String",
    "landkreis": "REQUIRED — String", 
    "typ": "REQUIRED — z.B. OB-Wahl, BM-Wahl",
    "wahl": "REQUIRED — TT.MM.JJJJ oder '—'",
    "ew": "REQUIRED — String mit Einwohnerzahl",
    "quellen": "REQUIRED — Integer ≥ 30",
    "password": "REQUIRED — String"
  },
  "kb": {
    "[entity_id]": {
      "name": "REQUIRED",
      "role": "REQUIRED",
      "party": "REQUIRED",
      "summary": "REQUIRED — ≥ 50 Wörter",
      "properties": "REQUIRED — ≥ 5 Einträge, jeder mit src",
      "connections": "REQUIRED — ≥ 1 Eintrag",
      "controversies": "OPTIONAL aber MUSS geprüft sein",
      "timeline": "REQUIRED — ≥ 3 Einträge",
      "quellen": "REQUIRED — ≥ 3 Einträge mit trust-Score"
    }
  },
  "graph": {
    "nodes": "REQUIRED — ≥ 8 Nodes",
    "links": "REQUIRED — ≥ 10 Links"
  },
  "news": "REQUIRED — ≥ 5 Einträge mit Datum + Quelle",
  "hypotheses": "REQUIRED — ≥ 2 Einträge mit Confidence",
  "sentiment": "REQUIRED — overall + ≥ 3 Topics",
  "patterns": "REQUIRED — ≥ 2 mit Confidence",
  "actions": "REQUIRED — ≥ 3 mit Priority",
  "forecast": "REQUIRED — ≥ 2 Kandidaten + ≥ 2 Szenarien"
}
```

### 2. Source Requirements (Palantir-Standard)
- **Minimum 30 Quellen pro Stadt** (tenant.quellen ≥ 30)
- Jede Property MUSS `src` haben (keine leeren Quellen)
- Jede Quelle MUSS `trust` Score haben (1-10)
- Mindestens 3 verschiedene Quelltypen: Medien, Offiziell, Analyse
- Keine Quelle älter als 12 Monate (außer historische Karrieredaten)

### 3. Entity Requirements
- **Minimum 3 KB-Entities pro Stadt** (Haupt-Kandidaten)
- Jede Entity: ≥ 5 Properties, ≥ 1 Connection, ≥ 3 Quellen
- Summary: ≥ 50 Wörter, keine generischen Phrasen
- Controversy-Check: MUSS durchgeführt sein (auch wenn Ergebnis = keine)

### 4. Graph Requirements  
- Alle KB-Entities als Nodes im Graph
- Jede Connection in KB = Link im Graph
- Defensive Schema: `n.r = n.r || n.size || 12; n.group = n.group || n.type || "neutral"`

### 5. Freshness
- News: mindestens 1 Eintrag aus den letzten 30 Tagen
- Forecast: `confidence` muss begründet sein
- Patterns: jeder Pattern hat `invalidateIf` (wann ist er falsch?)

---

## Validation Script

`python3 rag/validate_city.py data/cities/{id}.json`

Returns: PASS / FAIL + Liste aller Violations.
Kein Deploy ohne PASS.

---

## Quality Degradation Prevention

### Problem: Qualität sinkt bei Volume
### Lösung: Automated Checks + Human Spot-Check

```
GENERATION PIPELINE:
  
  1. kommune-generator.py generiert Rohdaten (GPT-4o, 30 Sek)
                ↓
  2. validate_city.py prüft Schema (0.5 Sek)
     → FAIL? → Zurück zu Schritt 1 mit Fehler-Feedback
                ↓
  3. build_index.py embeddet (2 Sek)
                ↓
  4. quality_score.py berechnet Score (1 Sek)
     → Score < 70? → Flag für Human Review
                ↓
  5. Deploy ODER Human Review Queue
```

### Quality Score Berechnung
```
score = (
  (quellen_count / 30) * 25      # Quellen-Dichte (max 25)
  + (entity_count / 5) * 20       # Entity-Tiefe (max 20)  
  + (news_freshness) * 15         # Aktualität (max 15)
  + (graph_density) * 15          # Vernetzung (max 15)
  + (source_diversity) * 15       # Quellen-Vielfalt (max 15)
  + (controversy_check) * 10      # Skandal-Check done (max 10)
)
# Minimum: 70 für Auto-Deploy, <70 = Human Review
```
