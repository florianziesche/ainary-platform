# Agent Improvements — Backlog
*Created: 2026-02-14 16:35 CET*

## Priority 1 (nach Report #5)

### 1. Antipatterns-Datei
- `agents/context-packs/antipatterns.md`
- Konkrete Negativbeispiele: zu viel Gold, Boxes, generische Story, CV-Hooks
- Agents lernen schneller von "Das war schlecht" als von "Das soll gut sein"

### 2. Report #1 HTML als BUILDER-Referenz
- Report #1 Section 8 (Predictions) = Design-Goldstandard
- BUILDER soll den HTML-Code sehen können, nicht nur Textbeschreibungen

### 3. pipeline-pack aufteilen
- `design-rules.md` — nur CSS/HTML/Layout
- `content-rules.md` — nur Text/Voice/Structure
- pipeline-pack wird zu groß, Agents ertrinken in Kontext

### 4. Feedback-Log strukturieren
- `agents/feedback-log.md`
- Format: Datum | Report-Nr | Gut | Schlecht | Änderung
- Systematisches Lernen statt Freitext

## Priority 2 (nach 10 Reports)

### 5. Cross-Report Consistency Check
- QA prüft nur isoliert → braucht Zugriff auf Claims aus vorherigen Reports
- "Widerspricht das Report #3?" / "Gleiche Zahl anders zitiert?"

### 6. Output-Vergleich System
- Systematisch: Was macht #1 besser als #2?
- Welche Sections sind stärker?
- Feedback-Loop zurück in Writer-Prompt

### 7. Voice Sample statt Voice Rules
- 200 Wörter perfekter Text als Anker
- Verhindert Tonalität-Drift über viele Reports

### 8. Research Quellen-Plan B
- Brave Quota leer → Google Scholar, Semantic Scholar API, ArXiv
- Paywalls blocken Bloomberg, Reuters, FT
- Alternative Datenquellen dokumentieren

## Priority 3 (nach 25 Reports)

### 9. Agent Self-Evaluation
- Jeder Agent bewertet eigenen Output (1-10)
- Vergleich mit QA-Score → Calibration der Selbsteinschätzung

### 10. Automatisches Context Pack Update
- Neue Claims aus jedem Report fließen automatisch in research-pack.md
- Script statt manuell

## Status
- [ ] P1-1: Antipatterns
- [ ] P1-2: HTML-Referenz
- [ ] P1-3: Pack aufteilen
- [ ] P1-4: Feedback-Log
- [ ] P2-5: Cross-Report Check
- [ ] P2-6: Output-Vergleich
- [ ] P2-7: Voice Sample
- [ ] P2-8: Quellen-Plan B
- [ ] P3-9: Self-Evaluation
- [ ] P3-10: Auto Context Update
