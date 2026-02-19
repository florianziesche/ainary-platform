# Q2 Development Intake Standard v1.0
*"Erst denken, dann bauen. Erst Intake, dann Code."*

## Warum dieser Standard existiert
Ohne Intake interpretiert Mia den Auftrag, baut, und Florian sagt "das meinte ich nicht." Rework kostet mehr als 2 Minuten Intake. Google nennt es Design Doc, Linear nennt es Project Brief, Stripe nennt es RFC. Gemeinsam: vor dem Bauen wird geschrieben.

## Geltungsbereich
- **PFLICHT:** Jede Aufgabe >30 Minuten oder >1 View/Feature/Endpoint
- **OPTIONAL:** Quick-Fixes <30min (ein Satz reicht)
- **AUSNAHME:** Florian sagt explizit "mach einfach" oder Aufgabe ist eindeutig (1 Button fixen)

## Der Prozess

### 1. Florian gibt Auftrag
Kann ein Satz sein, ein Screenshot, eine Frage.

### 2. Mia antwortet mit INTAKE (nicht mit Code)
Vorausgefüllt, Florian reviewed.

### 3. Florian bestätigt oder korrigiert
"Go", "Änder X", oder "Nein, ich meinte Y"

### 4. Mia baut NACH Bestätigung
Nicht vorher. Kein "ich fang schon mal an."

## Intake Template

```
INTAKE: [Titel]

WAS:      [Was wird gebaut/geändert — 1-2 Sätze]
WARUM:    [Welches Problem löst es — für wen]
WER:      [Zielgruppe: Florian / Kunde / System]

SCOPE:
✓ [Inkludiert]
✓ [Inkludiert]
✗ [Explizit NICHT inkludiert — verhindert Scope Creep]

OPTIONEN: (nur wenn >1 sinnvoller Weg)
A) [Option] — [Aufwand] — [Pro/Con]
B) [Option] — [Aufwand] — [Pro/Con]
→ Empfehlung: [X], weil [Begründung]

FERTIG WENN:
□ [Acceptance Criterion 1]
□ [Acceptance Criterion 2]
□ Q1 Verify bestanden (bei UI-Änderungen)

AUFWAND: ~[X]h | RISIKO: [niedrig/mittel/hoch]
```

## Regeln

1. **Intake VOR Code.** Kein Build ohne Go. Kein "ich fang schon mal an."
2. **Mia füllt vor.** Florian muss nicht von Null anfangen.
3. **Scope hat ✗.** Was NICHT gebaut wird ist genauso wichtig.
4. **Max 2 Optionen + 1 Empfehlung.** Nicht 5 Optionen ohne Meinung.
5. **"Fertig wenn" ist nicht optional.** Ohne Definition of Done gibt es kein Done.
6. **Aufwand schätzen.** Auch wenn ungenau — kalibriert über Zeit.
7. **Bei Quick-Fixes (<30min):** Ein Satz reicht: "Fix: Backlog Start resettet View. Ändere renderOperationsView() → renderBacklog(). ~15min. Go?"

## Anti-Patterns

| Anti-Pattern | Warum schlecht | Stattdessen |
|---|---|---|
| Intake überspringen weil "ist klar" | 80% der Rework kommt von "war klar" | Immer Intake bei >30min |
| Intake zu detailliert (2 Seiten) | Florian liest es nicht | Max 15 Zeilen |
| Bauen vor Go | Sunk Cost führt zu "mach halt fertig" | Warten auf "Go" |
| Keine ✗ im Scope | Scope Creep, Feature wird 3x so groß | Immer mindestens 1 Ausschluss |
| Optionen ohne Empfehlung | Florian muss selbst recherchieren | Immer 1 klare Empfehlung |

## Integration mit anderen Standards
- **Q1 Build-Verify:** "Q1 Verify bestanden" ist Acceptance Criterion bei UI-Änderungen
- **AGENTS.md Task Loop:** Intake ist Step 0 vor Step 1 (Aktivieren)
- **Sub-Agents:** Intake wird Teil der Sub-Agent Spec (WAS/WARUM/FERTIG WENN)

---
*Standard: Q2-DEVELOPMENT-INTAKE v1.0 | Erstellt: 2026-02-19 | Status: APPROVED*
*Trigger: Jeder Development-Auftrag >30min*
