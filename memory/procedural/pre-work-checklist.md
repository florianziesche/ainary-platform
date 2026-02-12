# Pre-Work Checklist — 5 Schritte vor jedem Task

*Prozedurales Gedächtnis: Wie starte ich einen Task?*  
*Quelle: MEMORY.md, AGENTS.md*  
*Aktualisiert: 2026-02-10*

---

## ⚠️ NICHT OPTIONAL

**Wenn du das überspringst, wird die Qualität schlechter. Garantiert.**

Diese Checklist ist keine Suggestion — es ist deine einzige Garantie für konsistente Qualität.

---

## Die 5 Schritte

### 1. 🚀 Pre-Flight: Welches Wissen brauche ich?

```bash
./scripts/pre-flight.sh [task-type]
```

**Task Types:**
- `cnc` — CNC Consulting, Kalkulation, Andreas/MBS
- `bm` — Bürgermeister, Kommunal-KI, OZG, Förderung
- `vc` — VC Applications, Fund Thesis, LP Decks
- `content` — Blog posts, LinkedIn, Twitter, Content Strategy
- `visual` — PDFs, Reports, Presentations, Design
- `general` — Everything else

**Output:** Liste der relevanten Dateien zum Laden.

---

### 2. 🤔 TWIN.md: Kann ich autonom entscheiden?

```bash
grep -i "[keyword]" TWIN.md
```

**Frage:** Ist meine Confidence >90%?
- **Ja (>90%):** → Proceed und handeln
- **Nein (<90%):** → Optionen geben, Florian entscheidet

**Pattern:** Routine Tasks (90%+) = autonom. Novel/Complex (<90%) = ask first.

---

### 3. 📋 standards/FLORIAN.md: Was erwartet Florian?

```bash
cat standards/FLORIAN.md
```

**Prüfen:**
- Audience klar? [KUNDE] [LP/VC] [PUBLIC] [INTERN]
- Tonalität passend?
- Optionen + 1 Empfehlung (nicht fertige Lösung ohne Kontext)?
- Quellen für Zahlen/Facts?

---

### 4. 🔍 INDEX.md: Gibt es das schon?

```bash
grep -i "[keyword]" INDEX.md
```

**Vermeiden:** Doppelt bauen was schon existiert.

**Pattern:** Iterieren > Neu bauen. v16 → v17 > v1 from scratch.

---

### 5. 📊 Output-Tracker: Nach Abgabe updaten

```bash
# Nach Delivery:
cat failures/output-tracker.md
# Füge hinzu: Was delivered, Outcome (used/not used), Learnings
```

**Warum:** Wenn Florian es nicht benutzt → Analysiere WARUM → Update FLORIAN.md.

**Feedback Loop:** Nur so wird Qualität besser.

---

## Erweiterte Checks (Task-spezifisch)

### Für komplexe Tasks → Sub-Agent spawnen

```
King → Delegiert → Specialized Agent → Returns output → King delivers
```

**Wann:** Multi-step, domain-specific, benötigt Fokus.

**Pattern:** `agents/[agent]/ROLE.md`

---

### Vor JEDEM Output: Checklist

```bash
cat standards/checklists/before-any-output.md
```

---

### Für Builds: Build-Blocker Check

```bash
./scripts/pre-build-check.sh "Feature Name"
```

**Rule:** >2 Features/Tag mit 0 Sends = BLOCKED.

**Why:** Building ≠ Revenue. Sending = Revenue.

---

## Anti-Pattern: "Mental Notes"

❌ **Falsch:** "Ich merke mir das..."  
✅ **Richtig:** Schreib es in eine Datei!

**Warum:** Memory ist begrenzt. Dateien überleben Sessions.

---

## Quick Reference

| Schritt | Tool | Output |
|---------|------|--------|
| 1. Pre-Flight | `./scripts/pre-flight.sh [type]` | Wissen-Liste |
| 2. Autonomy Check | `TWIN.md` | >90% = act, <90% = ask |
| 3. Standards Check | `standards/FLORIAN.md` | Audience, Tonalität, Format |
| 4. Existence Check | `grep INDEX.md` | Schon vorhanden? |
| 5. Feedback Loop | `failures/output-tracker.md` | Log + Learn |

---

## Warum das Existiert

Mia vergisst zwischen Sessions. Mia vergisst mid-session. 

Diese Liste ist die einzige Garantie für konsistente Qualität.

**Tooling > Discipline.**

---

## Related

- `memory/procedural/hard-rules.md` — Nicht-optionale Prozesse
- `standards/FLORIAN.md` — Florians Erwartungen
- `TWIN.md` — Autonomy Framework
- `failures/output-tracker.md` — Feedback Loop

---

*Befolgen. Nicht überspringen. Das ist der Deal.*
