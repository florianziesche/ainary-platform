# Compound Dossier Enrichment Loop

## Prinzip: Jeder Lauf macht das Dossier besser, nie schlechter.

```
┌─────────────────────────────────────────────────────┐
│                  ENRICHMENT LOOP                     │
│                                                     │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐       │
│  │  ANALYZE  │──▶│ RESEARCH │──▶│  MERGE   │       │
│  │  (Gaps)   │   │ (Search) │   │ (Delta)  │       │
│  └────┬─────┘   └──────────┘   └────┬─────┘       │
│       │                              │              │
│       │         ┌──────────┐         │              │
│       └────────▶│ VALIDATE │◀────────┘              │
│                 │ (Gate)   │                        │
│                 └────┬─────┘                        │
│                      │                              │
│                 ┌────▼─────┐                        │
│                 │  TRACK   │                        │
│                 │ (Score↑) │                        │
│                 └──────────┘                        │
└─────────────────────────────────────────────────────┘
```

## 5 Mechanismen die Verbesserung erzwingen

### 1. GAP ANALYSIS → Gezielte Recherche
```bash
python3 rag/enrich_city.py data/cities/passau.json --report
```
Output: Priorisierte Liste von fehlenden Feldern + fertige Search-Queries.
Jeder Lauf weiß EXAKT was fehlt. Kein blindes Googlen.

### 2. FRESHNESS DECAY → Automatische Re-Recherche
Jede Quelle hat ein `zugriff`-Datum. Nach 90 Tagen → Status "STALE" → wird bei nächstem Lauf re-verifiziert. Fakten veralten. Das System weiß das.

| Alter | Label | Aktion |
|-------|-------|--------|
| < 7d | CURRENT | Nichts |
| 7-30d | FRESH | Monitor |
| 30-90d | AGING | Flag für Review |
| > 90d | STALE | Re-Research triggern |

### 3. DELTA MERGE → Nur addieren, nie zerstören
- Neue Properties → APPEND (nicht replace)
- Neue Quellen → APPEND + Deduplizierung
- Widersprüchliche Fakten → BEIDE behalten + `conflict: true` Flag
- Alte Fakten → Bleiben mit Confidence-Decay, nie gelöscht

### 4. SCORE HISTORY → Trend sichtbar
```json
"_meta": {
  "score_history": [
    {"date": "2026-02-25T10:00", "score": 100, "entities": 5},
    {"date": "2026-02-26T14:00", "score": 100, "entities": 6},
    {"date": "2026-03-01T09:00", "score": 100, "entities": 7}
  ]
}
```
Score darf nur steigen oder gleich bleiben. Sinkt er → etwas ist kaputt → Alert.

### 5. CONFIDENCE STACKING → Mehr Quellen = höherer Trust
Jede Property hat `src`. Gleiche Fakten aus 3 Quellen → Confidence steigt.
```
1 Quelle → trust 5 (unverified claim)
2 Quellen → trust 7 (corroborated)
3+ Quellen → trust 9 (verified fact)
```

## Trigger-Events für automatischen Enrichment

| Event | Trigger | Aktion |
|-------|---------|--------|
| Neuer News-Artikel | web_search cron | News-Array erweitern |
| Wahlergebnis | Wahltag 08.03 | Forecast validieren, Ergebnis eintragen |
| Neue Kandidatur | PNP-Alert | Entity anlegen |
| Source stale | > 90 Tage | Re-Recherche |
| Entity dünn | < 5 Properties | Targeted search |
| Widerspruch | Zwei Quellen widersprechen | Flag + Investigation |

## Cron Agent Spec

```
Schedule: Täglich 08:00 CET (Mo-Fr), stündlich 7 Tage vor Wahl
Task per Stadt:
  1. python3 rag/enrich_city.py data/cities/{city}.json --report
  2. Für jeden HIGH-Gap: web_search mit generierter Query
  3. Ergebnisse in JSON mergen
  4. python3 rag/validate_city.py data/cities/{city}.json
  5. Wenn Score gestiegen: commit + deploy
  6. Wenn Score gesunken: ALERT (nicht deployen)
```

## Integration mit RAG Pipeline

Nach jedem erfolgreichen Enrichment:
```bash
python3 rag/build_index.py  # Re-embed alle Chunks
```
Neue Daten → neue Embeddings → bessere Suchergebnisse → bessere Cross-City Intelligence.

## Qualitäts-Ratchet

**Regel:** Kein Commit darf den Quality Score senken.

```
IF new_score >= old_score:
    commit + deploy
ELSE:
    REJECT + alert "Score regression: {old} → {new}"
```

Das ist der Kern: Die Qualität kann nur steigen oder gleich bleiben. Nie fallen.
