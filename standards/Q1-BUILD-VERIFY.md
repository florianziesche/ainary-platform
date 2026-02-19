# Q1 Build-Verify Standard v1.0
*"Kein Commit ohne Verify. Kein Ship ohne Beweis."*

## Warum dieser Standard existiert
Wir bauen Features und sagen "live" — ohne sie jemals im Browser zu prüfen. Buttons die nicht funktionieren, Views die sich überlappen, Items die spurlos verschwinden. Jeder dieser Bugs wäre in 30 Sekunden aufgefallen. Google's Regel: "Testing is a focus, not a team." Linear's Regel: "Every change gets a preview before merge."

## Geltungsbereich
Jede Änderung an Frontend (HTML/CSS/JS) oder Backend (API Endpoints) der Ainary Platform.

## Der Prozess (7 Schritte, nicht optional)

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

## Checkliste (vor jedem Commit)

| # | Check | Methode |
|---|-------|---------|
| 1 | Backend startet fehlerfrei | `python3 -c "import app"` |
| 2 | Health Endpoint antwortet | `curl localhost:8080/api/health` |
| 3 | Geänderte View öffnet korrekt | Browser Screenshot |
| 4 | Jeder neue/geänderte Button funktioniert | Browser Click + Screenshot |
| 5 | Kein JS-Error in Console | Browser Console Check |
| 6 | View-Wechsel funktioniert (switchView) | Hin und zurück navigieren |
| 7 | Context Panel zeigt richtigen Inhalt | In jeder betroffenen View prüfen |

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
- 7/7 Checks bestanden = COMMIT erlaubt
- <7/7 = Fix zuerst, dann erneut durch die Checkliste
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
