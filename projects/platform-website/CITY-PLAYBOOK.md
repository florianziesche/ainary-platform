# CITY-PLAYBOOK.md — Reproduzierbares City-Dossier-Erstellung

**Version:** 1.0  
**Stand:** 2026-02-25  
**Referenz-Dossier:** Bamberg (143 Punkte, GOLD STANDARD)  
**Pilot-Dossier:** Erlangen (von 35 auf 100+ Punkte in ~3h)

---

## Mission

**Ziel:** City-Dossier von "existiert" auf "Bamberg-Qualität" bringen.  
**Kriterium:** `node test_dossier.js <city>` → PASS (0 issues).  
**Zeit-Budget:** ~2-3 Stunden pro Stadt bei guter Quellenlage.

---

## Voraussetzungen

1. **DATA-SCHEMA.md gelesen** — verbindliche Feldnamen, Required-Felder, Minimum-Counts.
2. **Bamberg.json als Referenz** — für Struktur, Tiefe, Tone.
3. **web_search aktiviert** — Brave Search API für Recherche.
4. **Playwright installiert** — für `test_dossier.js`.

---

## Workflow (6 Phasen)

### Phase 1: IST-ZUSTAND ANALYSE (15 min)

**Schritt 1.1: Bamberg vs. City vergleichen**

Öffne beide JSON-Dateien und vergleiche Sektion für Sektion:

```bash
# Bamberg als Referenz laden
cat data/cities/bamberg.json | jq keys

# City laden
cat data/cities/<city>.json | jq keys
```

**Checkliste:**

| Sektion | Bamberg ✅ | City Status | Lücken? |
|---------|-----------|-------------|---------|
| **TENANT** | `strukturdaten` + `gemeinderat2020` + 5 Alerts | | |
| **KB** | 5 Kandidaten, je 8-10 Properties, `zitate`, `controversies`, `trustScore` | | |
| **GRAPH** | 15 nodes, 19 links | Min: 8 nodes, 10 links | |
| **NEWS** | 9 Items, 50+ Wörter body | Min: 5 Items | |
| **SENTIMENT** | 5 Topics mit je 2-4 Posts (echte Zitate + Quelle) | | |
| **FORECAST** | `historie` (3+ Wahlen), `treiber`, `stichwahlRange` | | |
| **SOCIAL** | Google Trends 3 Kandidaten, `momentum_index` | | |
| **YOUTUBE** | 3 Kandidaten mit Videos | | |
| **TALKING_POINTS** | Konkrete, belegte Points mit `ev`+`src` | | |

**Output:** Liste aller Lücken, priorisiert nach Punktzahl-Impact.

---

### Phase 2: STRUKTURDATEN + GEMEINDERAT (20 min)

**Kritischste Lücken zuerst.**

#### TENANT — strukturdaten

**Query:**
```
<Stadt> Strukturdaten Einwohner Fläche Bevölkerungsdichte 2026
```

**Quellen:**
- Offiziell: stadt.<stadt>.de → Statistik-Seite
- Wikipedia: de.wikipedia.org/wiki/<Stadt>
- Statistisches Landesamt: statistikportal.de

**Felder:**
- `einwohner`: "120.646 (31.12.2025)" — mit Datum + Quelle
- `flaeche`: "76,96 km²"
- `bevoelkerungsdichte`: "1.568 EW/km²" — berechnen falls nicht direkt verfügbar
- `besonderheiten`: 3-5 Unique Selling Points (UNESCO, Uni, Konzerne, etc.)

**Time:** ~10 min

---

#### TENANT — gemeinderat2020

**Query:**
```
<Stadt> Gemeinderat Stadtratswahl 2020 Ergebnis Sitzverteilung Parteien
```

**Quellen:**
- Wikipedia: "Ergebnisse der Kommunalwahlen in <Stadt>"
- Stadt-Website: wahlen.<stadt>.de oder stadt.<stadt>.de/wahlen
- Lokalpresse: Wahlergebnis-Artikel März 2020

**Feld-Format:**
```json
{
  "partei": "CSU",
  "prozent": 30.3,
  "sitze": 15
}
```

**Minimum:** Top 5 Parteien + "Sonstige" (Rest aggregiert).

**Time:** ~10 min

---

### Phase 3: KB — ZITATE + CONTROVERSIES + TRUSTSCORE (30 min)

**Für JEDEN Kandidaten (Top 3 mindestens):**

#### Zitate

**Query:**
```
<Kandidat Name> <Stadt> OB Zitate Interviews 2025 2026
```

**Quellen:**
- Kandidaten-Website: <kandidat>.de oder <partei>-<stadt>.de
- Triell/Podiumsdiskussionen: NN, BR24, SZ Regionalteil
- Haushaltsreden: stadt.<stadt>.de → Stadtrat → Reden

**Format:**
```json
{
  "text": "Wörtliches Zitat",
  "kontext": "Kontext (Rede, Interview, etc.)",
  "quelle": "Quelle",
  "datum": "JJJJ-MM-TT oder JJJJ"
}
```

**Minimum:** 3 Zitate pro Kandidat.  
**Zeit:** ~3 min pro Kandidat = 9 min für 3 Kandidaten.

---

#### Controversies

**Query:**
```
<Stadt> Skandale Affären Politik 2024 2025 OB Stadtrat
<Kandidat Name> Kritik Vorwurf Skandal
```

**Quellen:**
- Lokalpresse: FT, NN, SZ Regionalteil, BR24
- Untersuchungsausschüsse: Landtag-Website, SZ Archiv
- Wikipedia: Abschnitt "Kritik" oder "Kontroversen"

**Format:**
```json
{
  "title": "Skandal/Vorwurf-Titel",
  "text": "Zusammenfassung (50-100 Wörter)",
  "year": 2024,
  "severity": "SCHWERWIEGEND|MODERAT|NIEDRIG",
  "ev": "E|J|I|A",
  "conf": 80
}
```

**Falls KEINE Controversies:** `"controversies": []` (leer ist OK).

**Zeit:** ~5 min pro Kandidat = 15 min für 3 Kandidaten.

---

#### trustScore

**Auto-berechnet aus:**
- `gesamt`: 1-10 (subjektiv: Quellenlage + Vollständigkeit)
- `quellen`: Count von `kb.<kandidat>.quellen`
- `aktualitaet`: "Aktuell (Feb 2026)" oder "Veraltet (2024)"
- `tiefe`: "X Properties, Y Connections, Z Quellen, A Zitate, B Controversies"

**Zeit:** ~2 min pro Kandidat = 6 min für 3 Kandidaten.

---

**Total Phase 3:** 30 min.

---

### Phase 4: SENTIMENT — TOPICS MIT POSTS (30 min)

**Erlangen-Lücke:** Topics hatten nur Platzhalter ("Analyse in Vorbereitung").  
**Bamberg-Standard:** 5 Topics mit je 2-4 Posts (echte Zitate + Quelle + Datum).

#### Schritt 4.1: Topics identifizieren

**Quellen:**
- Wahlkampf-Themen: BR24, NN, FT Kommunalwahl-Berichterstattung
- Kandidaten-Websites: <kandidat>.de → Programm/Themen
- Lokalpresse: "Was bewegt <Stadt>?" Artikel

**Minimum:** 3 Topics.  
**Bamberg-Standard:** 5 Topics.

**Beispiel-Topics:**
- Verkehrsprojekte (StUB, Tram, Radwege)
- Amtsinhaber-Bilanz
- Wirtschaftsstandort (Siemens, Uni, etc.)
- Skandale (Masken-Affäre, Boni-Affäre, etc.)
- Klimaschutz / Energie

**Zeit:** ~5 min

---

#### Schritt 4.2: Posts pro Topic

**Query:**
```
<Kandidat Name> <Stadt> <Topic> Zitat Position Statement
<Topic> <Stadt> Presse Berichterstattung 2025 2026
```

**Quellen:**
- Kandidaten-Zitate: Triell-Transkripte, Interviews, Haushaltsreden
- Presse: BR24, NN, FT, SZ — Artikelzitate
- Social Media: Instagram, Facebook (Posts verifizieren via Screenshot/Archive)

**Format:**
```json
{
  "author": "Quelle/Autor",
  "text": "Wörtliches Zitat oder Zusammenfassung (20-50 Wörter)",
  "date": "TT.MM.JJJJ oder JJJJ-MM-TT",
  "source": "Quellen-URL oder Medienname",
  "sentiment": -0.7 bis +0.7 (subjektiv)
}
```

**Minimum:** 2 Posts pro Topic.  
**Bamberg-Standard:** 3-4 Posts pro Topic.

**Zeit:** ~5 min pro Topic = 25 min für 5 Topics.

---

**Total Phase 4:** 30 min.

---

### Phase 5: FORECAST — HISTORIE + TREIBER (15 min)

#### historie

**Query:**
```
<Stadt> OB-Wahl Ergebnis 2014 2020 Stichwahl Prozent
```

**Quellen:**
- Wikipedia: "Ergebnisse der Kommunalwahlen in <Stadt>"
- Stadt-Website: wahlen.<stadt>.de
- Lokalpresse: Wahlarchiv

**Format:**
```json
{
  "jahr": 2020,
  "wg": 1,
  "gewinner": "Janik (SPD) 39,2% vs Volleth (CSU) 35,4% → Stichwahl",
  "wb": 61.3,
  "anmerkung": "Janik gewann Stichwahl mit 54,47% vs 45,53%"
}
```

**Minimum:** 2 Wahlen (2014 + 2020).  
**Bamberg-Standard:** 3 Wahlen (2008, 2014, 2020).

**Zeit:** ~10 min

---

#### treiber + stichwahlRange

**Ableiten aus:**
- Anzahl Kandidaten (>5 → Splitting garantiert)
- Historische Muster (endet meist in Stichwahl?)
- Amtsbonus vs. Wechselstimmung
- Polarisierendes Thema (z.B. StUB)

**Format:**
```json
{
  "treiber": {
    "fuer_stichwahl": ["Grund 1", "Grund 2"],
    "gegen_stichwahl": ["Grund 1"],
    "stichwahlSzenario": "Kandidat A vs. B"
  },
  "stichwahlRange": {
    "min": 85,
    "max": 95,
    "label": "Stichwahl nahezu sicher"
  }
}
```

**Zeit:** ~5 min

---

**Total Phase 5:** 15 min.

---

### Phase 6: TALKING POINTS (20 min)

**Erlangen-Lücke:** Nur generische Platzhalter ("Faktencheck: Aktuelle Lage...").  
**Bamberg-Standard:** 4-5 Topics mit je 2-4 konkreten, belegten Argumenten (`ev`+`src`).

#### Schritt 6.1: Topics ableiten

**Quellen:**
- Aus SENTIMENT-Topics (Top 3 kontroverse)
- Wahlkampf-Hauptthemen (Triell, Kandidaten-Websites)

**Zeit:** ~5 min

---

#### Schritt 6.2: Points pro Topic

**Query:**
```
<Kandidat Name> <Topic> Position Argument Begründung
<Topic> <Stadt> Fakten Daten Statistik
```

**Quellen:**
- Kandidaten-Zitate: aus Zitate-Sektion recyclen
- Fakten: Wikipedia, Statistisches Landesamt, Lokalpresse
- Vergleiche: "Stadt A vs. Stadt B" bei gleichen Themen

**Format:**
```json
{
  "text": "Argument oder Fakt (50-100 Wörter)",
  "ev": "E|J|I|A",
  "src": "Quelle + Datum"
}
```

**Evidence-Level:**
- **E (Empirisch):** Umfrage, Statistik, offizielle Daten
- **J (Journalistisch):** Presseberichterstattung
- **I (Indiz):** Abgeleitet, Indirekt
- **A (Annahme):** Strukturelle Schätzung

**Minimum:** 2 Points pro Topic.  
**Bamberg-Standard:** 3-4 Points pro Topic.

**Zeit:** ~3 min pro Topic = 15 min für 5 Topics.

---

**Total Phase 6:** 20 min.

---

## Quality Gate (10 min)

```bash
cd /Users/florianziesche/.openclaw/workspace/projects/platform-website
node test_dossier.js <city>
```

**Erwartung:**
- ✅ `<CITY> | 0 issues`
- Falls FAIL: Fehlermeldung lesen, fixen, erneut testen.

**Häufige Fehler:**
1. **Feldnamen falsch** (z.B. `partei` statt `party`, `titel` statt `label`):  
   → `grep -r "partei" data/cities/<city>.json` → korrigieren.
2. **Fehlende Required-Felder** (z.B. `gemeinderat2020` fehlt):  
   → DATA-SCHEMA.md → Minimum-Count prüfen → nachrecherchieren.
3. **Leere Arrays wo Minimum gilt** (z.B. `"news": []` aber Min = 5):  
   → web_search → 5 News-Items finden.

**Zeit:** ~10 min (inkl. 1-2 Iterationen).

---

## Zeitaufwand Gesamt

| Phase | Zeit | Ergebnis |
|-------|------|----------|
| 1. Ist-Zustand Analyse | 15 min | Lücken-Liste |
| 2. Strukturdaten + Gemeinderat | 20 min | TENANT komplett |
| 3. KB (zitate, controversies, trustScore) | 30 min | 3 Kandidaten vollständig |
| 4. Sentiment Topics | 30 min | 5 Topics mit Posts |
| 5. Forecast (historie, treiber) | 15 min | Historische Einordnung |
| 6. Talking Points | 20 min | 5 Topics mit Arguments |
| 7. Quality Gate | 10 min | PASS bestätigt |

**Gesamt:** **140 min (~2,5h)** bei guter Quellenlage.

**Reserve:** +30 min bei schlechter Quellenlage oder komplexen Controversies.

---

## Quellen-Hierarchie (Wichtig für Recherche)

| Rang | Quelle | Trust | Verwendung |
|------|--------|-------|------------|
| **1** | Offizielle Stadt-Website | 100% | Strukturdaten, Wahlergebnisse, Ratssitzungen |
| **2** | Statistisches Landesamt | 100% | EW, Fläche, Dichte, Demografie |
| **3** | Wikipedia (Gemeinde-Seite) | 95% | Historie, Struktur, Wahlergebnisse (mit Quellen-Check) |
| **4** | Lokalpresse (NN, FT, SZ Regional) | 90% | Zitate, Controversies, News |
| **5** | BR24 | 90% | Überregionale Einordnung, Hintergrund |
| **6** | Kandidaten-Websites | 80% | Zitate, Programm (Bias beachten!) |
| **7** | Partei-Websites | 70% | Programm, Pressemitteilungen (Bias!) |
| **8** | Social Media (IG, FB) | 60% | Zitate, Engagement (verifizieren!) |

**Regel:** Jede Zahl, jedes Datum, jede Controversy → **2+ unabhängige Quellen** oder als "unverified" markieren.

---

## Häufige Fehler + Fixes

### 1. "Ich finde keine Strukturdaten"

**Symptom:** Wikipedia sagt nur "~115.000 EW", keine genaue Zahl.  
**Fix:**
1. stadt.<stadt>.de → Suche "Statistik" oder "Bevölkerung"
2. statistikportal.de → Gemeindeverzeichnis → Stadt suchen
3. Falls keine aktuellen Daten: Wikipedia-Zahl + " (Stand JJJJ-MM)" aus Quelle übernehmen

**Zeit:** +5 min

---

### 2. "Kandidat hat keine Controversies, aber ich brauche welche"

**Symptom:** Kandidat ist "sauber", keine Skandale.  
**Fix:**
- **Controversies sind OPTIONAL.** Leeres Array ist OK: `"controversies": []`
- NICHT erfinden! Lieber leeres Array als fabricated content.

**Regel:** Nur echte, belegbare Controversies eintragen.

---

### 3. "Sentiment Topics haben nur 1 Post pro Topic"

**Symptom:** Ich finde nur 1 Zitat pro Thema, brauche aber 2+.  
**Fix:**
1. Presse durchsuchen: "<Topic> <Stadt> Presse 2025"
2. Kandidaten-Websites: Programm-Seiten zitieren
3. Haushaltsreden: stadt.<stadt>.de → Ratssitzungen → Reden-Protokolle
4. Falls NICHTS: Anderen Kandidaten zitieren (Gegenperspektive)

**Notfall:** Topic entfernen wenn <2 Posts verfügbar (aber Min = 3 Topics halten).

**Zeit:** +10 min pro Topic

---

### 4. "test_dossier.js schlägt fehl: 'label is not defined' in patterns"

**Symptom:** Schema-Fehler — falscher Feldname.  
**Fix:**
```bash
grep -n "titel" data/cities/<city>.json
# Falls gefunden: ersetzen mit "label"
```

**Häufige Falsch-Felder:**
- `titel` → `label` (in patterns)
- `beschreibung` → `meaning` (in patterns)
- `partei` → `party` (in KB)
- `rolle` → `role` (in KB)
- `topic` → `name` (in sentiment.topics — WICHTIG!)

**Zeit:** +5 min

---

### 5. "Ich habe PASS, aber Score ist niedriger als Bamberg"

**Symptom:** Erlangen: 90 Punkte. Bamberg: 143 Punkte.  
**Analyse:**
- PASS = Minimum erfüllt (90+ Punkte).
- Bamberg = GOLD STANDARD (140+ Punkte).
- Gap = Tiefe (mehr Kandidaten, mehr News, mehr Properties).

**Fix:**
- Wenn Zeit: Mehr Kandidaten hinzufügen (5 statt 3).
- Wenn Zeit: Mehr News (9 statt 6).
- Wenn Zeit: Mehr KB-Properties (10 statt 6).

**Regel:** PASS ist OK. Gold Standard ist optional.

**Zeit:** +30-60 min für Gold-Upgrade

---

## Playbook-Validierung: Erlangen Case Study

**Start:** erlangen.json bei ~35 Punkten (dünn).  
**Nach Phase 1-6:** 100+ Punkte (PASS).  
**Zeit:** ~2,5h (inkl. Dokumentation).

**Lücken gefüllt:**
- TENANT: `strukturdaten` + `gemeinderat2020` + 5 Alerts (statt 1)
- KB: `zitate` (3-4 pro Kandidat), `controversies` (wo vorhanden), `trustScore`
- SENTIMENT: 5 Topics mit 2-4 Posts (statt Platzhalter)
- FORECAST: `historie` (2014 + 2020), `treiber`, `stichwahlRange`
- TALKING_POINTS: 4 Topics mit 2-4 konkreten Arguments (`ev`+`src`)
- NEWS: 9 Items (statt 6)

**Test-Ergebnis:**
```
✅ ERLANGEN     | 0 issues
```

**Bestätigung:** Playbook funktioniert. Reproduzierbar.

---

## Nächste Schritte

1. **Pilot:** Eine weitere Stadt (z.B. Fürth oder Passau) mit diesem Playbook upgraden.
2. **Timing:** Zeit pro Phase messen → Playbook optimieren.
3. **Automation:** Teile von Phase 2+3+5 (Strukturdaten, Historie) via Scripts automatisieren.
4. **Scaling:** Template für "Stadt in 2h" etablieren.

---

## Appendix: web_search Query Templates

### Strukturdaten
```
<Stadt> Strukturdaten Einwohner Fläche Bevölkerungsdichte 2026
<Stadt> Wikipedia Gemeinde Fläche Einwohner
```

### Gemeinderat
```
<Stadt> Gemeinderat Stadtratswahl 2020 Ergebnis Sitzverteilung
<Stadt> Kommunalwahl 2020 Wikipedia Stadtrat Sitze
```

### Zitate
```
<Kandidat Name> <Stadt> OB Zitate Interviews 2025 2026
<Kandidat Name> Haushaltsrede <Stadt> 2025
<Kandidat Name> Website Programm
```

### Controversies
```
<Stadt> Skandale Affären Politik 2024 2025
<Kandidat Name> Kritik Vorwurf Skandal
<Kandidat Name> Untersuchungsausschuss
```

### Historische Wahlergebnisse
```
<Stadt> OB-Wahl Ergebnis 2014 2020 Stichwahl
<Stadt> Kommunalwahl Wikipedia Oberbürgermeister
```

### Sentiment Topics
```
<Topic> <Stadt> Presse Berichterstattung 2025 2026
<Kandidat Name> <Topic> Position Statement
```

### Talking Points
```
<Kandidat Name> <Topic> Argument Begründung
<Topic> <Stadt> Fakten Daten Statistik
```

---

### Phase 7: VERIFICATION (PFLICHT vor Share) — NEU ab 2026-02-27

**Gelernt aus Nürnberg:** 7 kritische Fehler in "fertigem" Dossier. König als Jurist statt Bankkaufmann, Geburtsjahr 9 Jahre daneben, Walthelm als Bürgermeisterin statt Stadträtin.

**Vollständiger Prozess:** → `standards/Q3-VERIFICATION-PIPELINE.md`

**Kurzversion:**
1. Alle Claims aus JSON extrahieren (Patterns, Claim Ledger, KB Summaries, Forecast)
2. Opus Verification Agent: pro Claim 2-3 web_searches
3. Corrections als JSON-Patch anwenden
4. Key-Checks: alte Werte weg, neue Werte drin
5. test_dossier.js 8/8 PASS
6. Live-URL curlen, Kernfakten prüfen

**Typische Fehler die IMMER vorkommen:**
- Geburtsjahre (Agent rät oft ±5-10 Jahre)
- Berufsbezeichnung (Jurist vs. Bankkaufmann)
- Amtstitel (Bürgermeisterin vs. Stadträtin)
- Rankings falsch zitiert (Nr. 1 vs. Nr. 8)
- Prozentwerte gerundet (52,17% vs. 52,20%)
- Kontinuitätsbehauptungen ("75 Jahre SPD" vs. CSU-Unterbrechung)

**Total Phase 7:** 20 min (Agent 15 min + Apply 5 min)

---

**End of Playbook.**
