# Q1 Build-Verify Standard v1.0
*"Kein Commit ohne Verify. Kein Ship ohne Beweis."*

## Warum dieser Standard existiert
Wir bauen Features und sagen "live" — ohne sie jemals im Browser zu prüfen. Buttons die nicht funktionieren, Views die sich überlappen, Items die spurlos verschwinden. Jeder dieser Bugs wäre in 30 Sekunden aufgefallen. Google's Regel: "Testing is a focus, not a team." Linear's Regel: "Every change gets a preview before merge."

## Geltungsbereich
Jede Änderung an Frontend (HTML/CSS/JS) oder Backend (API Endpoints) der Ainary Platform.

## Der Prozess (9 Schritte, nicht optional)

### 0. FACT VERIFY (VOR Design/Content — NEU ab 2026-02-27)
**Nur bei Content-Tasks (LinkedIn, Emails, Reports, Carousels):**
- [ ] Quelldaten geladen? (Original sources, research notes, verified-truths.md)
- [ ] Namen korrekt? (Cross-check gegen sources)
- [ ] Zahlen korrekt? (Cross-check gegen sources)
- [ ] Affiliationen korrekt? (Partei, Firma, Rolle)
- [ ] Kein Claim ohne Quelle oder "unverified"-Tag

**Why:** Vermeidet "sieht professionell aus, aber Fakten falsch" (Carousel Bug Feb 27).

### 1. SPEC (VOR dem Code)
- Was ändere ich? Welche Buttons/Views sind betroffen?
- Acceptance Criteria: Was muss nachher funktionieren?
- Liste: Welche Elemente muss ich testen?

### 2. IMPLEMENT
- Code schreiben.

### 3. SYNTAX CHECK
```bash
# Python Backend
python3 -c "import app" 2>&1
# Kein Output = OK. Fehler = nicht weitermachen.
```

### 4. SERVER RESTART + HEALTH CHECK
```bash
launchctl kickstart -k gui/$(id -u)/com.ainary.workbench
sleep 3
curl -s http://localhost:8080/api/health
# "healthy" = OK. Fehler = nicht weitermachen.
```

### 5. VISUAL VERIFY (der fehlende Schritt)
```
browser → open http://localhost:8080
browser → screenshot (Gesamtansicht)
browser → snapshot (DOM-Struktur lesen)
```
Prüfen:
- [ ] Sieht die Seite korrekt aus? (kein Layout-Break)
- [ ] Sind alle geänderten Elemente sichtbar?
- [ ] Kein JavaScript-Error in Console?

### 6. FUNCTIONAL VERIFY (jeden geänderten Button klicken)
Für JEDES geänderte UI-Element:
```
browser → act: click [Button/Element]
browser → screenshot (Ergebnis)
```
Prüfen:
- [ ] Hat der Click eine sichtbare Reaktion?
- [ ] Ist das Ergebnis korrekt? (nicht nur "kein Error")
- [ ] Kann ich zurück-navigieren?

### 7. COMMIT + PUSH
Erst JETZT. Nicht vorher. Commit-Message enthält: was geändert, was getestet.

### 8. LLM AS JUDGE (VOR externem Send — NEU ab 2026-02-27)
**Nur bei External Content (LinkedIn, Emails, Reports):**

Run self-audit prompt:
```
You are an expert fact-checker. Evaluate the following content:

[GENERATED CONTENT]

Your task:
1. Accuracy Check: Names, numbers, dates, affiliations correct?
2. Source Verification: Claims sourced or unsourced?
3. Fabrication Detection: Invented statistics or fake data?
4. Confidence Score: Rate overall accuracy (0-100).

Original sources:
[SOURCE DATA]

Return:
- Score: X/100
- Issues Found: [List errors, unsourced claims, fabrications]
- Recommendation: [SHIP / FIX / BLOCK]
```

**Decision Gate:**
- Score ≥ 90 + No fabrications → SHIP
- Score 70-89 OR unsourced claims → FIX
- Score < 70 OR fabrications → BLOCK (manual review)

**Why:** Catches factual errors BEFORE delivery (not after).
**See:** `skills/capability-evolver/llm-as-judge-workflow.md`

### 9. DELIVER
External send (Telegram, Email, LinkedIn). Erst jetzt. Nicht vorher.

## Checkliste (vor jedem Commit/Send)

| # | Check | Methode |
|---|-------|---------|
| 0 | **Fakten verifiziert** (Content only) | Cross-check Namen/Zahlen/Affiliationen gegen sources |
| 1 | Backend startet fehlerfrei | `python3 -c "import app"` |
| 2 | Health Endpoint antwortet | `curl localhost:8080/api/health` |
| 3 | Geänderte View öffnet korrekt | Browser Screenshot |
| 4 | Jeder neue/geänderte Button funktioniert | Browser Click + Screenshot |
| 5 | Kein JS-Error in Console | Browser Console Check |
| 6 | View-Wechsel funktioniert (switchView) | Hin und zurück navigieren |
| 7 | Context Panel zeigt richtigen Inhalt | In jeder betroffenen View prüfen |
| 8 | **LLM Judge Score ≥ 90** (External content only) | Self-audit prompt, score < 90 → FIX |
| 9 | Delivered (External send executed) | Telegram/Email/LinkedIn confirmed |

## Failure Modes (was schief gehen kann)

| # | Failure | Ursache | Prävention |
|---|---------|---------|------------|
| F1 | Button existiert, Funktion fehlt | onclick zeigt auf nicht-existierende Funktion | Step 6: Click test |
| F2 | Item verschwindet nach Aktion | Backend filtert neuen Status aus | Step 6: Ergebnis prüfen, nicht nur "kein Error" |
| F3 | View zeigt gleichzeitig mit anderer View | Kein Hide vor Show | Step 6: View-Wechsel hin und zurück |
| F4 | Dropdown/Select nicht klickbar | Event Propagation (stopPropagation fehlt) | Step 6: Jedes Formular-Element testen |
| F5 | Content leer wo es Daten geben sollte | API liefert leeres Array / falscher Filter | Step 5: Screenshot prüfen auf leere Bereiche |

## Sub-Agent Integration

### QA-Verify nach Sub-Agent Builds
Jeder Sub-Agent der UI-Code ändert MUSS am Ende:
1. Server neu starten
2. Health Check ausführen
3. Browser öffnen + Screenshot der geänderten View
4. Jeden neuen Button klicken + Screenshot des Ergebnisses
5. Ergebnisse im Findings-Report dokumentieren

### Wie das in der Sub-Agent Spec aussieht
```
## AFTER ALL CHANGES — QA VERIFY (MANDATORY)
1. Restart server: `launchctl kickstart -k gui/$(id -u)/com.ainary.workbench`
2. Health check: `curl -s http://localhost:8080/api/health`
3. Open browser: `browser → open http://localhost:8080`
4. Screenshot each changed view
5. Click each new/changed button, screenshot result
6. Report: what works, what doesn't
7. ONLY commit if all checks pass
```

## Quality Gate
**Platform Changes (UI/API):**
- 7/7 Checks (1-7) bestanden = COMMIT erlaubt
- <7/7 = Fix zuerst, dann erneut durch die Checkliste

**External Content (LinkedIn, Email, Reports):**
- 4/4 Checks (0, 8, 9) bestanden = SEND erlaubt
- Step 0 (Fact Verify) skipped → HIGH RISK (Carousel Bug Feb 27)
- Step 8 (LLM Judge) score < 90 → FIX or BLOCK

**Universal Rule:**
- Kein "ich bin sicher dass es geht" — BEWEISEN.

## Metriken
- Bugs die in Verify gefunden werden (vor Commit) = gut
- Bugs die Florian findet (nach Commit) = schlecht → Trust sinkt
- Ziel: 0 UI-Bugs die Florian findet

## Referenzen
- Google Testing Blog: "Testing is a focus, not a team"
- Linear: Preview Deployments vor Merge
- Playwright: Visual Regression via Screenshot-Vergleich
- Vercel: Every PR gets a preview URL

---
*Standard: Q1-BUILD-VERIFY v1.0 | Erstellt: 2026-02-19 | Status: APPROVED*
*Trigger: Jede Frontend- oder Backend-Änderung an der Ainary Platform*
