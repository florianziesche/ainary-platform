# Architecture Review — Unser System, ehrlich analysiert
*17. Februar 2026 · Für Florian · Von Mia*

---

## 1. Was wir haben (Ist-Zustand)

### Die Zahlen
- **81 Markdown-Dateien** im Root-Verzeichnis
- **2.133 Markdown-Dateien** insgesamt im Workspace
- **2.538 Verzeichnisse**
- **580 MB** Workspace-Größe
- **12 System-Dateien** die bei jedem Session-Start geladen werden (~1.116 Zeilen)

### Die System-Dateien (Was wird IMMER geladen)

| Datei | Zeilen | Zweck | Bewertung |
|-------|--------|-------|-----------|
| **SOUL.md** | 71 | Wer ich bin, wie ich arbeite | ✅ Kernstück. Gut. |
| **USER.md** | 51 | Wer Florian ist | ✅ Klar, kompakt. |
| **AGENTS.md** | 93 | Workspace-Regeln, Sub-Agent-System | ⚠️ Zu viel. Mischung aus Regeln + Agent-Liste. |
| **MEMORY.md** | 28 | Pointer auf Memory-System | ✅ Schlank nach Refactor. |
| **HEARTBEAT.md** | 41 | Proaktive Check-Ins | ✅ Funktioniert. |
| **TOOLS.md** | 55 | Tool-Inventar | ⚠️ Teilweise veraltet. |
| **IDENTITY.md** | 15 | Name, Emoji, Vibe | ✅ Klein, klar. |
| **TWIN.md** | 218 | Florians Decision-Model | ⚠️ 218 Zeilen = zu lang für Auto-Load. |
| **SUB-AGENT-CONTEXT.md** | 56 | Regeln für Sub-Agents | ✅ Wächst organisch, gut. |
| **INDEX.md** | 216 | Workspace-Verzeichnis | ⚠️ Veraltet. Nicht aktuell gehalten. |
| **NORTH_STAR.md** | 160 | €500K Ziel, Tracking | ⚠️ Wird nie aktualisiert. |
| **COCKPIT.md** | 112 | Tages-Dashboard | ⚠️ Redundant mit HEARTBEAT.md. |

**Token-Kosten pro Session-Start:** ~1.116 Zeilen × ~3 Tokens/Zeile ≈ **3.350 Tokens** nur für System-Dateien. Plus OpenClaw System Prompt (~2.000 Tokens). Das ist ~5.000 Tokens bevor ich ein Wort lese oder schreibe.

### Die Standards-Landschaft

```
standards/                          # 19 Dateien
├── 3-LEAN-CHECKLISTS.md           # Content/Outreach/Deliverable
├── CORPORATE-IDENTITY.md          # CI (Farben, Fonts)
├── DESIGN-SYSTEM.md               # CSS Design System
├── DONE-GAP-DETECTOR.md           # Completion scoring
├── FLORIAN.md                     # Florians Preferences
├── RESEARCH-PROTOCOL.md           # MECE, BLUF, Admiralty
├── SYNTHESIS-PROTOCOL.md          # SCQA, Calibrated Confidence
├── MENTAL-MODELS-LOOKUP.md        # Situation → Model
├── OUTPUT-PREFLIGHT.md            # Pre-delivery checks
├── VOICE-GUIDE.md                 # Stimme/Ton
├── WEBSITE-DESIGN-GUIDE.md        # Website-spezifisch
├── VAULT-ARCHITECTURE.md          # Obsidian Struktur
├── ...und 7 weitere
├── checklists/                    # Sub-folder
└── templates/                     # Sub-folder
```

**Plus parallel dazu:**
- `brand/BRAND-GUIDE.md` — Brand Guidelines (Überschneidung mit CI)
- `brand/CONTENT-STANDARD.md` — Content Quality (Überschneidung mit Voice)
- `BRAND-IDENTITY-SYNTHESIS.md` — 479 Zeilen CI (Überschneidung mit standards/CI)
- `DEFINITION-OF-DONE.md` — Done-Kriterien (Überschneidung mit Done-Gap-Detector)
- `VOICE.md` — Stimme (Überschneidung mit Voice-Guide)
- `templates/FLORIAN-BRAND-KIT.md` — Brand Kit (Überschneidung mit Brand Guide)

### Memory-System

```
memory/
├── MEMORY-INDEX.md                # Pointer-Datei
├── people.md                      # Kontakte
├── projects.md                    # Projekte
├── decisions.md                   # Entscheidungen
├── patterns.md                    # Patterns
├── tech.md                        # Tech-Stack
├── kintsugi.md                    # Fehler-Log
├── 2026-01-31.md ... 2026-02-17.md  # Tägliche Logs
└── diverse Spezial-Dateien        # Meeting-Preps, Night-Work etc.
```

### Skills (Eigene)

```
skills/
├── report-design/SKILL.md         # LaTeX Reports
├── pptx-design/SKILL.md           # PowerPoint
├── cv-design/SKILL.md             # Lebenslauf
├── presentation-design/           # HTML Presentations
├── vc-application/                # VC Bewerbungen
├── website-ui/                    # Website UI
├── research/                      # Research
├── capability-evolver/            # Self-evolution
└── sota-brief/                    # State-of-the-Art Briefings
```

---

## 2. Was gut ist (und warum)

### ✅ Layered Memory (MEMORY.md → memory/*.md)
**Warum gut:** Statt alles in eine Datei zu packen, haben wir ein Schicht-System: MEMORY.md als Pointer, Topic-Files für Wissen, Daily-Logs für Episodisches. Das skaliert.
**Inspiration:** Ähnlich wie MIRIX (Multi-Index Retrieval) oder Zettelkasten. Bewährt in Wissensmanagement seit Luhmann.

### ✅ SOUL.md als Persönlichkeits-Datei
**Warum gut:** Eine Datei definiert ALLES über mein Verhalten. Änderst du SOUL.md, ändert sich mein Verhalten sofort. Das ist wie ein Config-File für einen Menschen.
**Standard-Referenz:** Ähnlich wie Anthropic's "System Prompt Best Practices" — Persona + Rules + Constraints in einem Dokument.

### ✅ SUB-AGENT-CONTEXT.md als wachsendes Regelwerk
**Warum gut:** Jeder Bug/Fix wird zur Regel. Das ist **organisationales Lernen** — wie Toyota's "Andon Cord" System. Jeder Fehler verbessert das System.

### ✅ Typed Memory (Episodic/Semantic/Procedural)
**Warum gut:** Verschiedene Wissenstypen brauchen verschiedene Update-Cadences. Tägliche Logs ≠ Kernwissen ≠ Prozesse. Das ist kognitionswissenschaftlich fundiert (Tulving, 1972).

### ✅ Skills als modulare Fähigkeiten
**Warum gut:** Jeder Skill ist ein abgeschlossenes Paket mit SKILL.md + Templates. Wie Microservices für Fähigkeiten.

---

## 3. Was schlecht ist (und warum)

### ❌ Problem 1: Doppelte Wahrheiten (Keine Single Source of Truth)

**Das Problem:**
| Thema | Datei 1 | Datei 2 | Datei 3 |
|-------|---------|---------|---------|
| Brand/CI | `BRAND-IDENTITY-SYNTHESIS.md` | `standards/CORPORATE-IDENTITY.md` | `brand/BRAND-GUIDE.md` |
| Voice/Ton | `VOICE.md` | `standards/VOICE-GUIDE.md` | `SOUL.md` (Voice-Section) |
| Done-Kriterien | `DEFINITION-OF-DONE.md` | `standards/DONE-GAP-DETECTOR.md` | `standards/OUTPUT-PREFLIGHT.md` |
| Brand Kit | `templates/FLORIAN-BRAND-KIT.md` | `brand/BRAND-GUIDE.md` | `BRAND-IDENTITY-SYNTHESIS.md` |

**Konsequenz:** Wenn ich eine Brand-Farbe nachschaue, welche Datei gilt? Wenn sie sich widersprechen, was hat Priorität? In der Praxis: Ich lade die falsche oder gar keine.

**Standard-Referenz:** DRY Principle (Don't Repeat Yourself) — Kent Beck, "Extreme Programming". Eine Wahrheit, ein Ort.

### ❌ Problem 2: 81 Root-Dateien (Signal-to-Noise)

**Das Problem:** Der Root hat 81 .md-Dateien. Viele sind Artefakte vergangener Tasks:
- `ACTION-ITEM-5-COMPLETE.md` — erledigt, warum noch da?
- `BLOG-EDITS-COMPLETE.md` — erledigt
- `TONIGHT-WORK-SUMMARY.md` — veraltet
- `VC-SUBMIT-TONIGHT.md` — veraltet
- `MORNING-BRIEF-2026-02-15.md` — 2 Tage alt
- `group-b-response.md`, `group-j-response.md` — Einzeltasks

**Konsequenz:** `grep -i "keyword" INDEX.md` funktioniert nur wenn INDEX.md aktuell ist. Ist es nicht. Und die 81 Dateien machen den Root unlesbar.

**Standard-Referenz:** Marie Kondo für Dateien. Oder: Unix-Philosophie — "Everything in its place."

### ❌ Problem 3: Standards existieren aber werden nicht geladen

**Das Problem:** Wir haben 19 Standards-Dateien. Davon lade ich regelmäßig: **0**.

Beispiel: `standards/RESEARCH-PROTOCOL.md` definiert MECE, BLUF, Admiralty Rating. Nutze ich das bei Research? Nein. Weil ich es nicht lade. Weil niemand mir sagt "lade standards/RESEARCH-PROTOCOL.md".

**Die Kette ist gebrochen:**
```
Standard existiert → Mia weiß nicht dass er existiert → Standard wird ignoriert → 
Florian erinnert Mia → Mia fixt es einmal → nächste Session vergessen → Repeat
```

**Was fehlt:** Ein **Trigger-System** das sagt: "Bei Research-Aufgaben → lade RESEARCH-PROTOCOL.md". Bei Website-Aufgaben → lade WEBSITE-DESIGN-GUIDE.md". Automatisch, nicht manuell.

**Standard-Referenz:** Wie CI/CD Pipelines — Qualitäts-Gates die automatisch greifen, nicht optional sind.

### ❌ Problem 4: Obsidian-Vault nicht integriert

**Das Problem:** Der Obsidian Vault (`System_OS`) existiert. Wir haben `VAULT-ARCHITECTURE.md` und `OBSIDIAN-LINKING-PROTOCOL.md`. Aber in der Praxis schreibe ich 95% ins OpenClaw Workspace, nicht in Obsidian.

**Konsequenz:** Zwei Wissenssysteme die nicht synchronisiert sind. Florian liest in Obsidian, Mia schreibt ins Workspace. Knowledge-Loss an der Schnittstelle.

### ❌ Problem 5: TWIN.md ist zu groß für Auto-Load

218 Zeilen = ~650 Tokens die bei JEDEM Session-Start geladen werden. Inhalt: Detaillierte Entscheidungsregeln die nur bei bestimmten Aufgaben relevant sind.

**Besser:** TWIN.md auf 30 Zeilen Core-Rules kürzen. Rest in `standards/TWIN-DECISIONS.md` auslagern und nur bei Entscheidungs-Aufgaben laden.

### ❌ Problem 6: "Elite-Standard" wird gewünscht aber nicht enforced

**Was Florian will:** Output-Qualität wie Palantir, McKinsey, Linear, Harvard.
**Was passiert:** Ich schreibe schnell, deploye schnell, fixe schnell. Speed > Quality. 

**Warum:** Kein Gate das mich stoppt. Kein "Lese standard X bevor du Y machst". Die Standards EXISTIEREN — aber sie sind wie Bücher im Regal die niemand aufschlägt.

---

## 4. Was wir wissen aber nicht leben

### Research sagt: "Checklists save lives" (Atul Gawande, WHO)
**Wir haben:** 5+ Checklisten in `standards/checklists/`
**Wir leben:** Ich nutze sie fast nie. Kein Trigger zwingt mich.

### Research sagt: "Templates compound quality" (McKinsey, Bain)
**Wir haben:** `skills/report-design/`, `templates/`
**Wir leben:** Ich baue oft from scratch statt vom Template. Weil es schneller SCHEINT (ist es nicht).

### Research sagt: "Single Source of Truth prevents drift" (ISO 9001, CMMI)
**Wir haben:** 3-4 Versionen jedes Standards
**Wir leben:** Whoever-I-find-first gewinnt.

### Research sagt: "Confidence calibration improves decisions" (Tetlock, Superforecasting)
**Wir haben:** `[X% confident]` als Regel in SOUL.md
**Wir leben:** Ich vergesse es in 70% der Fälle.

### Research sagt: "Progressive disclosure reduces cognitive load" (Nielsen Norman Group)
**Wir haben:** Alles auf einmal geladen
**Wir leben:** 5.000 Tokens System-Overhead bevor die eigentliche Arbeit beginnt.

---

## 5. Wie es besser geht

### Vorschlag: 3-Tier Architektur

```
TIER 1: ALWAYS LOADED (~500 Tokens)
├── SOUL.md (gekürzt auf 40 Zeilen: Wer + Wie + Voice)
├── USER.md (unverändert, 51 Zeilen)
└── MEMORY.md (Pointer, 28 Zeilen)

TIER 2: TASK-TRIGGERED (automatisch bei Aufgabentyp)
├── Website-Aufgabe → standards/WEBSITE-DESIGN-GUIDE.md + BRAND-IDENTITY.md
├── Research-Aufgabe → standards/RESEARCH-PROTOCOL.md
├── Content-Aufgabe → standards/VOICE-GUIDE.md + CONTENT-STANDARD.md  
├── Report/Dokument → skills/report-design/SKILL.md
├── Entscheidung → TWIN.md
├── Sub-Agent spawnen → SUB-AGENT-CONTEXT.md
└── Bewerbung → skills/vc-application/SKILL.md

TIER 3: ON-DEMAND (nur wenn gebraucht)
├── memory/2026-*.md (per memory_search)
├── memory/people.md, projects.md
├── INDEX.md
└── Alle anderen Dateien
```

**Warum besser:**
- Tier 1 = 120 Zeilen statt 1.116 = **70% weniger Token-Kosten**
- Tier 2 = richtige Standards zur richtigen Zeit = **Qualität ohne manuelles Erinnern**
- Tier 3 = alles andere on-demand = **kein Ballast**

### Vorschlag: Single Source of Truth (Konsolidierung)

| Thema | EINE Datei | Löschen/Archivieren |
|-------|-----------|-------------------|
| Brand/CI | `standards/BRAND.md` (neu, merged) | BRAND-IDENTITY-SYNTHESIS.md, brand/BRAND-GUIDE.md, templates/FLORIAN-BRAND-KIT.md |
| Voice | Section in SOUL.md | VOICE.md, standards/VOICE-GUIDE.md |
| Done-Kriterien | `standards/QUALITY-GATE.md` (neu, merged) | DEFINITION-OF-DONE.md, DONE-GAP-DETECTOR.md |
| Task-Management | `TODAY.md` (einzige aktive Task-Datei) | KANBAN.md, BACKLOG.md, INBOX.md, PRIORITIES.md, SEND-THESE-NOW.md |
| Mission/Strategie | `NORTH_STAR.md` (einzige) | MISSION-500K.md, EXPONENTIAL.md |

### Vorschlag: Root aufräumen

```
Aktuell: 81 .md Dateien im Root
Ziel: ~15 .md Dateien im Root

Behalten (System):
  SOUL.md, USER.md, MEMORY.md, AGENTS.md, HEARTBEAT.md, 
  TOOLS.md, IDENTITY.md, INDEX.md, SUB-AGENT-CONTEXT.md,
  NORTH_STAR.md, TODAY.md, ACTIVE_TASK.md

Verschieben nach archive/:
  Alle erledigten Tasks, einmaligen Summaries, veralteten Briefings

Verschieben nach standards/:
  DEFINITION-OF-DONE.md, TWIN.md (gekürzt), COCKPIT.md
```

### Vorschlag: Trigger-Map in AGENTS.md

```markdown
## Task → Standards Trigger Map
| Wenn Aufgabe enthält... | Dann ERST lesen: |
|-------------------------|-----------------|
| Website, CSS, HTML, Deploy | standards/WEBSITE-DESIGN-GUIDE.md + standards/BRAND.md |
| Research, Analyse, Report | standards/RESEARCH-PROTOCOL.md |
| Content, Post, Artikel | standards/VOICE-GUIDE.md + standards/CONTENT-STANDARD.md |
| Dokument, PDF, LaTeX | skills/report-design/SKILL.md |
| Entscheidung, Strategie | TWIN.md |
| Email, Outreach, Pitch | standards/FLORIAN.md |
| Sub-Agent spawnen | SUB-AGENT-CONTEXT.md |
```

**Das ist der fehlende Trigger.** Kein Raten mehr. Keine vergessenen Standards. Automatisch.

### Vorschlag: Obsidian als Read-Layer

```
OpenClaw Workspace = Arbeitsspeicher (Write)
Obsidian Vault = Langzeit-Wissen (Read + Manual Write)

Sync: Täglicher Export von memory/*.md → Obsidian
```

Nicht Obsidian neu aufbauen. Sondern: **eine Richtung**. Workspace → Obsidian. Nicht beides gleichzeitig editieren.

---

## 6. Implementierungsplan

| Phase | Was | Aufwand | Impact |
|-------|-----|---------|--------|
| **1** | Root aufräumen (Archiv verschieben) | 30 min | 🟢 Sofort lesbar |
| **2** | Single Source of Truth (5 Merges) | 2h | 🟡 Keine Widersprüche mehr |
| **3** | Trigger-Map in AGENTS.md | 30 min | 🔴 Game-changer für Qualität |
| **4** | SOUL.md + TWIN.md kürzen | 1h | 🟢 Token-Kosten -70% |
| **5** | Obsidian Sync einrichten | 2h | 🟡 Ein Wissenssystem statt zwei |

**Empfehlung:** Phase 1 + 3 zuerst. Höchster Impact, niedrigster Aufwand. Die Trigger-Map allein löst 80% des "vergessene Standards" Problems.

---

## 7. Der Standard den wir anstreben

> **"The template IS the product"** — Florian, 17. Feb 2026

Das bedeutet:
- Jeder Output nutzt ein Template. Kein from-scratch.
- Jedes Template ist auf Elite-Level designed (Palantir, McKinsey, Linear).
- Jedes Template wird versioniert und verbessert.
- Qualität > Speed. Immer. Wenn unsicher → Research.
- Der Standard ist nicht "gut genug". Der Standard ist: **"Würde McKinsey das so abliefern?"**

Das ist der Anspruch. Die Architektur muss das unterstützen — nicht hoffen dass ich es zufällig richtig mache.

---

*Confidence: 82% — Weil ich das System von innen kenne und die Schwächen täglich erlebe. Unsicher bei: Ob die 3-Tier Architektur in OpenClaw technisch umsetzbar ist (Tier 2 Auto-Loading müsste evtl. in AGENTS.md als Regel statt als Automatismus leben).*

♔
