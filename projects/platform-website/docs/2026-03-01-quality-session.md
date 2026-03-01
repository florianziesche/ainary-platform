# Session Log: Quality Pipeline Overhaul — 1. März 2026

**Dauer:** ~3.5 Stunden (07:00–10:45 CET)
**Kontext:** Ainary Platform — 50 Bayerische Kommunalwahl-Dossiers
**Teilnehmer:** Florian Ziesche + Mia (AI Co-Founder)

---

## Ausgangslage

50 Stadt-Dossiers für die Bayerische Kommunalwahl am 08.03.2026. Alle 50 JSONs waren vom Research-Agent generiert und über `validate_city.py` als "100/100" bewertet. Die Website (dossier.html) rendert ein einziges Template mit N Datensätzen.

**Das Problem:** Die "100/100" Scores waren Format-Scores — sie prüften ob JSON-Keys existieren, nicht ob die Inhalte stimmen.

---

## Phase 1: Format-Fixes (Symptombekämpfung)

### Was Florian gemeldet hat
> "Bei allen Seiten fehlen Informationen, bei einigen wird null angezeigt"

### Was ich gemacht habe
- Systematischer Audit aller 50 Städte auf leere/falsche Felder
- **41 von 50 Städten hatten Issues:**
  - `kb[].role` enthielt "Kandidat" nicht → Template-Filter zeigte keine Kandidaten
  - `forecast.kandidaten` ohne ID → Forecast-Bars zeigten "?-?%"
  - `kb[].properties` hatte `k/v` statt `key/val` → "undefined" im UI
  - `kb[].karriere` hatte `jahr/text` statt `year/label`
  - `kb[].controversies` ohne `text`-Feld
  - `tenant.wahl` war Objekt statt String → JS crash (`wahlStr.match is not a function`)
  - JURISDIKTIONEN zeigte "undefined" → `TENANT.landkreis` existierte nicht

### Fixes
1. `enrich_template.py` überarbeitet — Role-Filter, Forecast-ID-Matching (Nachname), Topics-Threshold
2. Daten-Migration: `k→key`, `v→val`, `jahr→year`, `text→label`
3. Template: Fallback-Chain für JURISDIKTIONEN, Safety-Guard für `wahlStr`
4. 4 Deploys über Vercel

### Das eigentliche Problem (erst später erkannt)
**Ich hab Format-Fehler gefixed und "0 Audit-Fehler" als Erfolg gewertet. Zu keinem Zeitpunkt habe ich geprüft ob die INHALTE stimmen.**

---

## Phase 2: Florians Intervention — "Hast du validiert?"

### Florians Frage
> "How did you apply the entire pipeline without validating the results? Would a Palantir engineer work this way?"

### Screenshot: André Bart Verification Report
Florian zeigte einen Verification Report mit:
- "3. Buergermeister vs. Zweiter Buergermeister" — Impact: HOCH
- "Strafbefehl akzeptiert Nov. 2023 vs. erlassen Juli 2022" — Impact: MITTEL
- "37 oder 38 Jahre vs. 38 Jahre (seit Jan 2026)" — Impact: GERING
- "1975 oder 1976 vs. Geb. 26.06.1976" — Impact: GERING

**Jeder Datenpunkt gegen Quellen geprüft. Widersprüche aufgedeckt. Impact bewertet. Korrigiert.**

### Content Quality Audit — Die Wahrheit

```
42/299 Kandidaten:  LEERES Kurzprofil
114/299 Kandidaten: NUR Template-Defaults (Partei/Rolle/Status)
68/299 Kandidaten:  KEINE Karriere-Daten
252/299 Kandidaten: KEINE Controversies
6 Städte:           Kaputte Forecast-Summen
Regensburg:         Forecast addiert sich auf 205% (!)
0 Quellen-URLs:     Verifiziert als erreichbar
```

**Fazit:** Der Enricher hat FORMAT gefüllt, nicht SUBSTANZ. 38% der KB-Entries waren Hohlkörper — sie sahen auf der Website "gefüllt" aus, enthielten aber null Information.

---

## Phase 3: Verification Layer gebaut

### `verify_facts.py` — Content-Verifikation (neu)
Prüft nicht ob Felder existieren, sondern ob sie STIMMEN:
1. **Forecast-Plausibilität** — Summen ≤105%, min≤max, Range-Breite
2. **Cross-Field-Konsistenz** — Alter vs Geburtsjahr, Partei über alle Felder
3. **Hollow Shell Detection** — Score 0-10 (kein Kurzprofil + nur Templates = Hohlkörper)
4. **Temporale Konsistenz** — Wahldatum, Karriere-Jahre, News-Freshness
5. **Exit code 1 = Deploy blocked**

### Ergebnisse nach Verification
```
Vorher:  26 HOCH-Issues (Regensburg 205%, 17 Party-Widersprüche, 6 Hohlkörper)
Nachher: 6 HOCH-Issues (alle Friedberg Hohlkörper — brauchen echte Recherche)
```

### Fixes
- Regensburg Forecast: 205-345% → 63-117% (realistische Ranges)
- 17 Party-Inkonsistenzen: HTML-Tags in Partei-Feld, Synonym-Normalisierung ("Grüne" vs "Bündnis 90/Die Grünen")
- `AGENTS.md` als LLM-Projektdokumentation mit Anti-Patterns

---

## Phase 4: Deep Enrichment — Echte Daten statt Template-Fills

### Florians Anforderung
> "2-3x mehr Quellen, auch von X Accounts, Social Media Insights die keiner hat"

### `deep_enrich.py` — Web + X + Institutional Research (neu)
1. **Web-Recherche** — 3 Queries pro Kandidat (Bio, Karriere, Positionen), Top-8 URLs fetchen
2. **Bio-Extraktion** — Relevante Sätze aus Web-Texten extrahieren
3. **Karriere-Extraktion** — Jahr + Kontext Patterns finden
4. **Properties-Extraktion** — Alter, Beruf, Familienstand, Bildung aus Text
5. **Institutionelle Quellen** — Rathaus-Website, Wahlamt, Partei-Seiten
6. **Cleanup** — HTML-Tags, Wikipedia-Boilerplate, Scraping-Müll, Deduplizierung

### Bamberg-Ergebnis (Pilot)
```
VORHER → NACHHER:
  News:    16 → 98 (6x)
  Quellen: 30 → 68 (2.3x)
  Bio:     0 → 20.258 Zeichen

Melanie Huml vorher: 0 Bio, 3 Template-Properties
Melanie Huml nachher: Ärztin, Jg. 1975, MdL seit 2003,
  Gesundheitsministerin 2013-2018, Europaministerium 2018-2022,
  Masken-Affäre, 8 Karriere-Stationen, 15 Quellen
```

### Datenqualitätsprobleme beim Scraping
- AfD Bamberg Bio: ePayment Debug Token (Website-Scraping-Müll)
- Andreas Starke Bio: "Wikipedia Zum Inhalt springen Hauptmenü..." (Boilerplate)
- HTML-Tags in Properties (`<strong>CSU</strong>`)
- Duplizierte Sätze in Bios

→ Cleanup-Step eingebaut der diese Artefakte entfernt.

---

## Phase 5: Social Tracker — RSS + X/Twitter

### `social_tracker.py` (neu)
- **Discover**: X-Accounts automatisch finden (Username-Patterns + Bio-Matching)
- **RSS**: Bayerische Medien-Feeds (inFranken, BR, SZ, Merkur) nach Region gemapped
- **Poll**: Neue Posts holen, nach Stadt/Kandidat filtern, als News einspeisen

### Bamberg Tracking-Quellen
```
✅ @MelanieHuml (Kandidatin, MdL)
✅ @AfDBamberg (Partei)
✅ @SPD_Bamberg (Partei)
✅ @StadtBamberg (Institutional)
✅ SZ Bayern RSS
```

**X Insights:** AfD Bamberg postet Stadtratkandidaten-Vorstellung (Platz 6-10), Infostands in Hallstadt, Memmelsdorf, Lauter. Das sind Wahlkampf-Aktivitäten die in keiner Zeitung stehen.

---

## Phase 6: Batch-Enrichment aller 50 Städte

### Status (laufend)
```
27/50 Städte enriched
1.467 neue Deep-Enrich Items
2.414 total News (vorher ~800)
167.165 Bio-Chars (vorher ~20.000)
```

---

## Kernprobleme (ungelöst)

### 1. Kein Prozess
Ich reagiere auf Florians Feedback statt einem definierten Workflow zu folgen. Jeder Fix war eine Reaktion, keine Prävention.

### 2. Format ≠ Qualität
`validate_city.py` gibt 100/100 für Dateien die 205% Forecast-Summen und leere Bios haben. Der Score misst das Falsche.

### 3. Kein Quality Ratchet
Es gibt keinen Mechanismus der verhindert dass ein neuer Run die Daten VERSCHLECHTERT. Kein Before/After-Vergleich, kein Score der nur steigen darf.

### 4. Mechanical Enrichment ≠ Verification
`deep_enrich.py` extrahiert Bios aus Web-Texten. Es prüft nicht ob "Jahrgang 1975" stimmt. Es ist bessere Befüllung, nicht Verifikation.

### 5. 6 Friedberg Hohlkörper
6 Kandidaten mit 0 Bio, 0 Karriere, nur Template-Properties. Kein Script kann das fixen — braucht echte Recherche.

### 6. Scraping-Qualität
Web-Extraktion produziert Artefakte (ePayment-Token, Wikipedia-Boilerplate, HTML-Tags). Jeder Run braucht Cleanup.

---

## Gebaute Artefakte (heute)

| Datei | Zweck | Status |
|-------|-------|--------|
| `rag/pipeline/verify_facts.py` | Content-Verifikation (Truth, nicht Format) | ✅ Live |
| `rag/pipeline/deep_enrich.py` | Web + X + Institutional Research | ✅ Live |
| `rag/pipeline/social_tracker.py` | RSS + X/Twitter Tracking | ✅ Live |
| `AGENTS.md` | LLM-Projektdokumentation mit Anti-Patterns | ✅ Live |
| `data/reports/verification-*.json` | Verification Reports | ✅ Generiert |

## CLI-Erweiterungen

```bash
python3 cli.py verify                      # Fact verification
python3 cli.py verify --fix                # Auto-fix deterministic issues
python3 -m pipeline.deep_enrich --city X   # Deep enrich single city
python3 -m pipeline.deep_enrich --all      # All 50 cities
python3 -m pipeline.social_tracker discover --city X  # Find X + RSS
python3 -m pipeline.social_tracker poll --all         # Poll all tracked sources
python3 -m pipeline.social_tracker status             # Tracking overview
```

---

## Offene Fragen für MIIA/AWS

1. **Supabase vs JSON** — Bei 50 Städten reicht JSON. Bei 500+ brauchen wir eine DB mit Schema-Enforcement. Wann migrieren?
2. **Quality Ratchet** — Wie implementiert man einen Score der nur steigen darf in einer CI/CD Pipeline?
3. **Verification at Scale** — `verify_facts.py` prüft Cross-Field-Konsistenz. Aber: Stimmt "Jahrgang 1975" überhaupt? Wie verifiziert man 299 Bios gegen Quellen ohne manuellen Review?
4. **Scraping-Qualität** — `deep_enrich.py` extrahiert aus beliebigen Webseiten. Garbage In = Garbage Out. Brauchen wir LLM-basierte Extraktion statt Regex?
5. **Cron-Readiness** — `social_tracker poll --all` kann als Daily Cron laufen. Aber wer prüft ob die neuen Daten Müll sind?

---

## Lessons Learned

1. **"0 Fehler" ist nicht "gut"** — Es bedeutet nur dass dein Test das Falsche misst
2. **Enrichment ohne Verification = Wallpaper** — Hübsch formatierter Müll ist schlimmer als leere Felder
3. **Der Prozess fehlte, nicht die Tools** — Ich hatte `validate_city.py` seit Wochen. Ich hab es nie als Gate benutzt.
4. **Palantir-Grade = jeder Datenpunkt hat eine Quelle** — Nicht "Bio aus Wikipedia scrapen", sondern "Bio gegen 3 Quellen verifizieren"
5. **Build without ship = 0** — Gilt auch umgekehrt: Ship without verify = negative value

---

*Generiert: 2026-03-01 10:45 CET*
*Commit: platform-website/docs/2026-03-01-quality-session.md*
