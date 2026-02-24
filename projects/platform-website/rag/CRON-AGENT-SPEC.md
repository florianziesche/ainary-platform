# CRON AGENT: Autonomous Intelligence Loop
## Spec für den Mia Intelligence Agent

### Trigger
- **Täglich 08:00 CET** (Mo-Fr) — Full Loop
- **Stündlich** ab 01.03.2026 (7 Tage vor Wahl) — Hot Loop
- **08.03.2026 18:00-23:00** — Election Night Mode (alle 15 min)
- **09.03-22.03** — Stichwahl-Mode (täglich + bei Breaking News)

### Daily Loop (08:00 CET)

```
STEP 1: SCAN
  python3 rag/auto_enrich.py --execute --propagate
  → Liest SCHEMA.json, scannt ALLE Städte, generiert Gap-Queue

STEP 2: FILL (Top 20 Gaps)
  Für jeden auto-fillable Gap mit Severity HIGH/CRITICAL:
    → web_search(gap.query)
    → Ergebnis in patch.json strukturieren
    → python3 rag/enrich_city.py data/cities/{city}.json --merge patch.json

STEP 3: VALIDATE
  Für jede geänderte Stadt:
    → python3 rag/validate_city.py data/cities/{city}.json
    → Nur wenn PASS: weiter. Sonst: revert.

STEP 4: REFLECT
  python3 rag/reflect.py data/cities/{changed_city}.json --full
  → Hypothesen updaten
  → Cross-City Patterns prüfen

STEP 5: DEPLOY
  git add data/cities/*.json rag/learning-journal.json
  git commit -m "auto: Daily enrichment [date] — {n} gaps filled, {m} cities updated"
  git push && vercel --prod --yes

STEP 6: REPORT
  Telegram-Nachricht an Florian:
  "🔄 Daily Enrichment: {n} Gaps gefüllt, {m} Städte updated.
   Score: Bamberg {x}, Passau {y}, Regensburg {z}.
   Top Finding: {best_new_insight}"
```

### News Monitor (Parallel-Cron, alle 4h)

```
Für jede Stadt:
  web_search("{city} OB-Wahl Kommunalwahl 2026", freshness="pd")
  → Vergleich mit news[] Array im JSON
  → Neue Meldung? → Append zu news[], update sentiment
  → Breaking? → Sofort-Alert an Florian via Telegram
```

### New City Generator (On-Demand, triggered by Florian oder Radar)

```
Input: Stadt-Name
  1. web_search("{stadt} OB-Wahl Kommunalwahl 2026 Kandidaten")
  2. web_search("{stadt} Stadtrat Gemeinderat 2020 Ergebnis Sitze")
  3. web_search("{stadt} Kommunalwahl Themen Wahlkampf")
  4. Für jeden Kandidaten: web_search("{name} Instagram")
  5. Strukturiere in SCHEMA.json Format
  6. python3 rag/validate_city.py → PASS?
  7. python3 rag/reflect.py --full → Cross-City Patterns anwenden
  8. Commit + Deploy
  9. Report: "Neue Stadt: {name}, Score {x}/100, {n} Entities, {m} Cross-City Matches"
```

### Election Night Mode (08.03.2026, 18:00-23:00)

```
Alle 15 Minuten:
  Für jede Stadt:
    web_search("{stadt} OB-Wahl Ergebnis 2026 live")
    → Ergebnis gefunden?
      → forecast.ergebnis_1wg updaten
      → Hypothesen validieren (H1 confirmed/rejected)
      → Stichwahl ja/nein?
      → Sofort Telegram: "🗳️ {stadt}: {gewinner} {prozent}% — Stichwahl: {ja/nein}"
```

### Autonomie-Level

| Level | Was | Wann |
|-------|-----|------|
| **L1: Report** | Scan + Report an Florian, kein Auto-Fill | JETZT möglich |
| **L2: Fill + Ask** | Scan + Fill + "Soll ich deployen?" | JETZT möglich |
| **L3: Auto-Deploy** | Scan + Fill + Deploy + Report | Nach 1 Woche L2 ohne Fehler |
| **L4: Full Auto** | + News Monitor + New City Generator | Nach Wahltag-Validation |

### Empfehlung: Starte mit L2

Ich mache den Daily Loop, fülle Gaps, und schicke dir morgens eine Telegram-Message:
"3 Städte enriched, 12 Gaps gefüllt. Bamberg hat jetzt Social Media. Deploy?"
Du sagst "go" → ich deploye. Oder "stop" → ich warte.

Nach einer Woche ohne Fehler → L3 (Auto-Deploy).
Nach Wahltag (08.03) → wir validieren meine Prognosen gegen echte Ergebnisse → L4.
