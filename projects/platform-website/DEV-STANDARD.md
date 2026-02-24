# DEV-STANDARD.md — Entwicklungsstandard Platform Website
## Verbindlich für JEDE Änderung. Keine Ausnahmen.

**Version:** 1.0 | **Erstellt:** 2026-02-24 | **Gilt ab sofort.**

---

## 1. Änderungsprozess (NICHT VERHANDELBAR)

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│ 1. SPEC     │ ──→ │ 2. CODE     │ ──→ │ 3. TEST     │ ──→ │ 4. DEPLOY   │
│ §-Nr lesen  │     │ Ändern      │     │ MUSS PASS   │     │ Nur wenn    │
│             │     │             │     │             │     │ 8/8 grün    │
└─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘
                                              │ FAIL?
                                              ▼
                                        Zurück zu 2.
                                        NICHT deployen.
```

### Schritt-für-Schritt:

1. **SPEC LESEN** — Welche §-Nummer in PRODUCT-SPEC.md betrifft die Änderung?
   - Keine Änderung ohne §-Referenz.
   - Wenn keine § passt: Erst PRODUCT-SPEC.md erweitern, dann coden.

2. **CODE ÄNDERN** — In `dossier.html` oder `data/cities/*.json`
   - Daten-Änderungen: Nur im JSON, NIE hardcoded in HTML
   - Schema-Felder: Nur die in PRODUCT-SPEC.md definierten Namen verwenden
   - Neue Felder: Erst in normalizeCity() Default setzen, dann verwenden

3. **TEST LOKAL** — `node test_dossier.js`
   - MUSS 8/8 PASS zeigen
   - 0 Issues
   - Bei FAIL: Fixen, nicht deployen

4. **DEPLOY** — Nur wenn Test grün
   ```bash
   git add <geänderte Dateien>     # NIE git add -A (Mapbox secret!)
   git commit -m "§X.Y: beschreibung"
   vercel --prod --yes
   ```

5. **VERIFY LIVE** — Nach Deploy
   - Die geänderte Sektion im Browser öffnen
   - Funktioniert es? Ja → Done. Nein → Zurück zu 2.

---

## 2. Commit-Konventionen

```
§1.5: fix forecast rendering for cities without historie
§3.3: add soWhat to pattern cards
§6.4: replace remaining Apple emojis
data: enrich bamberg weekly_brief
test: add strategy tab truncation check
arch: refactor normalizeCity for themen field mapping
```

**Regeln:**
- Immer §-Nummer wenn eine Spec-Sektion betroffen
- `data:` Prefix für reine JSON-Änderungen
- `test:` Prefix für Test-Änderungen
- `arch:` Prefix für Architektur-Änderungen
- Keine Commits ohne Test-Run

---

## 3. Datei-Verantwortung

| Datei | Wann ändern | Wie testen |
|-------|------------|------------|
| `dossier.html` | UI/Rendering-Änderungen | `node test_dossier.js` |
| `data/cities/*.json` | Daten-Updates | `node test_dossier.js` |
| `PRODUCT-SPEC.md` | Neue Sektionen, Schema-Änderungen | Manuell reviewen |
| `DEV-STANDARD.md` | Prozess-Änderungen | — |
| `test_dossier.js` | Neue Test-Cases | Test sich selbst |
| `radar.html` | Radar-Seite | Manuell (kein Test) |
| `radar-data.json` | Stadt-Liste | Manuell |

---

## 4. Schema-Regeln

### 4.1 Feld-Namen (NICHT VERHANDELBAR)

| Richtig | FALSCH | Kontext |
|---------|--------|---------|
| `name` | `topic`, `titel`, `label` (bei Sentiment) | Sentiment Topics |
| `label` | `titel`, `name` (bei Patterns) | Patterns |
| `meaning` | `beschreibung` | Pattern Bedeutung |
| `soWhat` | `cross_city`, `action` | Handlungsempfehlung |
| `party` | `partei` | Partei |
| `role` | `rolle` | Rolle |
| `title` + `body` | `type` + `text` | Social Insights |
| `relevanz` | `relevance` | Themen-Radar |
| `beschreibung` | `description`, `soWhat` | Themen-Radar Beschreibung |

### 4.2 normalizeCity() ist der Schema-Vertrag

- **Jedes neue Feld MUSS in normalizeCity() einen Default bekommen**
- Rendering-Code darf NIEMALS auf optionale Felder zugreifen ohne Default
- Wenn Code `x.y` liest, muss normalizeCity `x.y = x.y || default` setzen
- Fallback-Kette: `x.newName || x.oldName || default`

### 4.3 JSON-Schreiben

Beim Erzeugen oder Ändern von City-JSONs:
1. Verwende NUR die Feldnamen aus §4.1
2. Prüfe nach Schreiben: `node test_dossier.js`
3. Bei neuen Feldern: Erst normalizeCity() updaten

---

## 5. Sicherheit

### 5.1 Secrets Management

| Was | Wo | NICHT |
|-----|----|-------|
| Stadt-Passwörter | `tenant.password` im JSON | Akzeptabel für MVP, TODO: hashen |
| API Keys | Environment Variables / .env | NIE im Code oder JSON |
| Mapbox Token | `projects/pitch-deck/map-v2-real.html` | NIE `git add -A` vom Workspace Root |
| Vercel Token | CLI-Session | NIE in Dateien |

### 5.2 Git-Regeln

```bash
# RICHTIG — selective staging
git add dossier.html data/cities/bamberg.json

# FALSCH — fängt Mapbox Secret ein
git add -A
git add .
```

**Vor jedem Push:** `git diff --cached --name-only` — sind nur erwartete Dateien dabei?

### 5.3 URL-Sicherheit

- `?admin` Parameter bypassed Auth-Gate (nur für Entwicklung)
- Production: Passwort-Gate aktiv
- Keine sensiblen Daten in URLs
- Keine API-Keys in Client-Side Code

---

## 6. Daten-Pipeline

### 6.1 Datenquellen → JSON

```
Quelle                  Methode              Frequenz
─────────────────────────────────────────────────────
Pressearchiv            web_search           2x/Woche
Google Trends           Manuell              1x/Woche
Instagram               Scraper/Manuell      1x/Woche
YouTube                 YouTube API          1x/Woche
Ratsinformationssystem  web_fetch            Bei Bedarf
Wikipedia               web_fetch            Einmalig + Updates
```

### 6.2 Daten-Update Ablauf

```
1. Datenquelle abrufen (web_search, API, etc.)
2. In City-JSON einfügen/updaten
3. `node test_dossier.js` → 8/8 PASS
4. Git commit mit `data:` Prefix
5. Deploy
```

### 6.3 Daten-Qualität

- Jeder Datenpunkt braucht eine Quelle
- Keine Schätzungen als Fakten darstellen
- Confidence-Werte bei Prognosen: PFLICHT
- `gaps` Feld bei Forecast: Transparent machen was wir NICHT wissen
- Daten älter als 60 Tage: Als "veraltet" markieren

---

## 7. Skalierung

### 7.1 Aktueller Stand: 8 Cities (JSON-Files)

- Ein Template (`dossier.html`), N Datasets (`data/cities/*.json`)
- Skaliert bis ~50 Cities ohne Architektur-Änderung
- `radar-data.json` enthält City-Index

### 7.2 Nächste Stufe: 50-200 Cities

- JSON → Firebase/Supabase (ADR-005)
- `dossier.html` lädt per API statt per File
- `normalizeCity()` bleibt gleich (nur Datenquelle ändert sich)
- Automated City Generation Pipeline

### 7.3 Langfrist: 200+ Cities

- Full API Backend
- Cron-basierte Daten-Aktualisierung
- Admin-Dashboard für Daten-Pflege
- Automated Quality Gates in CI/CD

---

## 8. Dokumentations-Standard

### 8.1 Wann dokumentieren?

| Ereignis | Wo dokumentieren |
|----------|-----------------|
| Neue Sektion/Feature | PRODUCT-SPEC.md: neue § anlegen |
| Neues JSON-Feld | PRODUCT-SPEC.md: Schema aktualisieren + normalizeCity() |
| Bug gefunden + gefixt | CHANGELOG.md + Test erweitern |
| Architektur-Entscheidung | ARCHITECTURE.md (ADR-Format) |
| Prozess-Änderung | DEV-STANDARD.md (diese Datei) |

### 8.2 Format

- Markdown, keine Word/PDF
- Kurz. Bullets > Prosa.
- Beispiele > Theorie
- §-Nummern für Referenzierbarkeit

### 8.3 Changelog

Jeder Deploy bekommt einen Eintrag in CHANGELOG.md:
```markdown
## 2026-02-24
- §6.4: Alle Apple Emojis durch CSS-Badges ersetzt
- §1.1: Weekly Brief zeigt "0 Prioritäten" nicht mehr
- arch: normalizeCity() — zentralisierte Daten-Defaults
```

---

## 9. Planungs-Standard

### 9.1 Vor jeder Arbeitssession

1. `node test_dossier.js` laufen lassen → Baseline kennen
2. Aufgabe identifizieren → §-Nummer zuordnen
3. Scope definieren: Was ist "fertig"?
4. Schätzen: <30min = direkt machen, >30min = Intake (Q2 Standard)

### 9.2 Priorisierung

```
P0 (SOFORT):  Produkt ist kaputt (JS-Crash, leere Seiten)
P1 (HEUTE):   Feature für nächsten Send/Outreach
P2 (WOCHE):   Daten-Qualität verbessern
P3 (SPRINT):  Architektur, Skalierung, neue Features
```

### 9.3 Kein Scope Creep

- Eine Aufgabe = eine §-Nummer
- Wenn während der Arbeit ein anderer Bug auffällt: NOTIEREN, nicht fixen
- Erst aktuelle Aufgabe abschließen, dann nächste

---

## 10. Anti-Patterns (VERBOTEN)

| Anti-Pattern | Warum schlecht | Stattdessen |
|---|---|---|
| Deploy ohne Test | Bugs in Production | `node test_dossier.js` → 8/8 PASS |
| `git add -A` | Mapbox Secret wird gepusht | Selective `git add` |
| Hardcoded Daten in HTML | Skaliert nicht, Schema-Drift | Daten nur in JSON |
| Apple Emojis | Broken auf Windows/Android | CSS-Badges, Unicode BMP |
| "Schnell fixen" ohne §-Ref | Kein Kontext, kein Test | §-Nummer + Test |
| Schema-Feld erfinden | normalizeCity crasht nicht, aber Rendering zeigt nichts | Erst PRODUCT-SPEC, dann normalizeCity, dann verwenden |
| Mehrere Aufgaben gleichzeitig | Scope Creep, halbe Sachen | Eine §-Nummer pro Commit |
| Schätzen statt nachschauen | "Ich glaube das Feld heißt..." | JSON öffnen, nachschauen |
| Deploy ohne Live-Verify | "Sieht im Test gut aus" ≠ "funktioniert live" | Browser öffnen, klicken |

---

*Dieser Standard wird bei JEDER Session geladen die das Platform-Website Projekt betrifft.*
*Änderungen an diesem Standard: Nur mit Florians Zustimmung.*
