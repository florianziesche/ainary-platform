# Q3: Verification Pipeline — NICHT VERHANDELBAR

*Stand: 2026-02-27. Gelernt aus Nürnberg: 7 kritische Fehler in kundenreifem Dossier gefunden.*

## Warum

Ein einziger falscher Fakt zerstört Vertrauen. Kaindl (Nürnberg-Insider) hätte sofort gesehen: König ist kein Jurist (Bankkaufmann), nicht 1971 geboren (1980), Walthelm ist keine Bürgermeisterin (Berufsmäßige Stadträtin). Das Dossier wäre wertlos gewesen.

**Regel: Kein Dossier wird geteilt ohne Verification Pipeline.**

## Wann

- VOR jedem Passwort-Share an Externe (Kandidaten, Presse, Kunden)
- VOR jedem Deploy eines neuen City-JSONs
- NACH jedem Deep Research Agent Output

## Pipeline (5 Schritte)

### Schritt 1: Claims extrahieren
```
python3 -c "
import json
with open('data/cities/CITY.json') as f: d=json.load(f)
# Extrahiere ALLE faktischen Aussagen:
# - Patterns (label + meaning)
# - Claim Ledger (claim)
# - Kandidaten (summary, properties, born, role)
# - News (title, source)
# - Hypothesen (label, probability, rationale)
# - Forecast (ranges, keyfactors)
# - Controversies (text, source)
"
```

**Output:** Liste aller Claims mit ID.

### Schritt 2: Opus Verification Agent

Ein einzelner Opus-Agent, sequentiell. KEIN Parallel-Spawning.

**Warum Opus:** Sonnet halluziniert URLs häufiger. Opus markiert Unsicherheit. Ein Agent = ein Context = Widersprüche zwischen Claims werden erkannt.

**Agent Task Template:**
```
VERIFICATION AGENT: [Stadt] Kommunalwahl 2026

METHODIK pro Claim:
1. Claim lesen
2. web_search mit 2-3 unabhängigen Quellen
3. Markieren: ✅ CONFIRMED | ⚠️ CORRECTED (alt → neu) | ❌ UNVERIFIABLE
4. Bei Korrektur: exakte Änderung + Quell-URL

CLAIMS: [Liste aller Claims]

OUTPUT:
1. research/cities/[stadt]/verification-[datum].md
2. research/cities/[stadt]/corrections-[datum].json
   Format: [{path, old, new, source}]
```

**Timeout:** 900s (15 min). 37 Claims ~ 74 web_searches.

### Schritt 3: Corrections anwenden

```python
# Corrections aus JSON laden
# Brute-force replace im gesamten JSON
# KEIN manuelles Editieren einzelner Felder — zu fehleranfällig
# Stattdessen: json.dumps → string replace → json.loads
```

### Schritt 4: Verifikation der Verifikation

```python
# Nach dem Apply: Key-Checks
checks = [
    ('alter_wert' not in raw, 'Alter Wert entfernt'),
    ('neuer_wert' in raw, 'Neuer Wert vorhanden'),
]
```

### Schritt 5: Test + Deploy

```bash
node test_dossier.js  # 8/8 PASS
git add data/cities/CITY.json
git commit -m "Verification: N corrections applied — [wichtigste Korrekturen]"
git push && npx vercel --prod --yes
```

## Typische Fehlerquellen (aus Nürnberg gelernt)

| Fehlertyp | Beispiel | Wie vermeiden |
|-----------|----------|---------------|
| **Geburtsjahr** | König 1971→1980 (9 Jahre daneben) | Wikipedia + offizielle Bio |
| **Beruf** | König Jurist→Bankkaufmann | Nicht aus dem Lebenslauf raten |
| **Amtsbezeichnung** | Walthelm BM→Stadträtin | Offizielles Ratsinfo-System |
| **Ranking falsch zitiert** | Bitkom Nr.1→Nr.8 | Original-Pressemitteilung lesen |
| **Prozentwerte gerundet** | 52,17%→52,20%, 66,4%→66,67% | Offizielle Wahlergebnisse, nicht Sekundärquellen |
| **Datum falsch** | Nominierung 17.05→23.03 | Partei-Pressemitteilung |
| **Kontinuitätsbehauptung** | "75 Jahre SPD" → Scholz CSU 1996-2002 | Vollständige Amtsträgerliste prüfen |
| **Unterstützer verwechselt** | Piraten/Humanisten→Piraten+Volt | Aktuelle Pressemeldung, nicht alte |

## Qualitäts-Metriken

| Metrik | Minimum | Ziel |
|--------|---------|------|
| Claims verifiziert | 100% | 100% |
| Confirmed (✅) | >70% | >85% |
| Corrected (⚠️) | dokumentiert | <15% |
| Unverifiable (❌) | als J/A markiert | <5% |
| Quellen pro Claim | 2 | 3+ |

## Integration mit anderen Standards

- **Q1-BUILD-VERIFY.md**: Verification Pipeline kommt VOR Build-Verify (Schritt 5 = Q1)
- **Q2-DEVELOPMENT-INTAKE.md**: Bei neuem City-JSON: Intake → Research → **Verification** → Build
- **ERF Pipeline**: Research Output → **Q3 Verification** → JSON Conversion → Deploy
- **EIJA Framework**: Unverifiable Claims werden als J (Judgment) oder A (Assumption) gelabelt

## Reihenfolge im Gesamtprozess

```
ERF Research → Opus Deep Analysis → Opus Asset Builder → Q3 VERIFICATION → Test → Deploy → Q1 Build-Verify
```

## Checkliste (Copy-Paste vor jedem Share)

- [ ] Verification Agent gelaufen?
- [ ] Verification Report geschrieben?
- [ ] Corrections JSON erstellt?
- [ ] Alle Corrections angewendet?
- [ ] Key-Checks bestanden?
- [ ] test_dossier.js 8/8 PASS?
- [ ] Live-URL gecurlt und Kernfakten geprüft?
- [ ] Kein "undefined" im gesamten Dossier?
