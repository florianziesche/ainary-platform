# AGENTS.md — Workspace Rules

## Task → Standards Trigger Map (LOAD FIRST, NOT OPTIONAL)

| Task contains... | Load ONLY these | Do NOT load |
|------------------|----------------|-------------|
| Website, CSS, HTML, Deploy | `standards/WEBSITE-DESIGN-GUIDE.md` + `standards/BRAND.md` | RESEARCH-PROTOCOL, CONTENT-VOICE |
| Research, Analyse, Report | `standards/RESEARCH-PROTOCOL.md` | BRAND, WEBSITE-DESIGN-GUIDE |
| Content, Post, Artikel, LinkedIn | `standards/CONTENT-VOICE.md` | RESEARCH-PROTOCOL, BRAND |
| Dokument, PDF, LaTeX, Report | `skills/report-design/SKILL.md` | WEBSITE-DESIGN-GUIDE |
| Email, Outreach, Pitch, Message | `standards/FLORIAN.md` | BRAND, RESEARCH-PROTOCOL |
| Bewerbung, VC Application | `skills/vc-application/SKILL.md` | CONTENT-VOICE |
| Entscheidung, Strategie, Trade-off | `TWIN.md` (full) | all standards |
| Sub-Agent spawnen | `SUB-AGENT-CONTEXT.md` | — |
| Presentation, Slides | `skills/presentation-design/SKILL.md` | RESEARCH-PROTOCOL |
| Heartbeat | `ref/HEARTBEAT.md` | all standards |

## Task Loop (5 Schritte, mandatory)
1. **AKTIVIEREN:** `memory_search` + relevanten Kontext laden — was wissen wir schon?
2. **AUSFÜHREN:** Die Arbeit machen
3. **PRÜFEN:** Beantwortet? Belegt? Nutzbar? → Nein = Retry
4. **SPEICHERN:** Memory-R1 Check → wenn ja: memory/daily/YYYY-MM-DD.md
5. **LIEFERN**

### Zusätzlich bei Research/Deep Tasks (optional)
- Hypothese VOR dem Suchen aufstellen, dann widerlegen versuchen
- Neue Fakten → `verified-truths.md`
- 2-3 Connections → `connections.md`
- `agenttrust-score.py update <agent> <conf> <outcome>`

## Decision Tree — Was lese ich wann?
*Florian kann jederzeit sagen: "Lies den Baum." Dann starte ich hier.*

```
START: Neue Aufgabe erhalten
│
├─ Kenne ich den Aufgabentyp?
│  ├─ JA → Trigger Map oben → Standard laden → weiter
│  └─ NEIN → Florian fragen: "Was ist das Ziel?"
│
├─ Bin ich unsicher? (Confidence < 90%)
│  ├─ JA → TWIN.md lesen → Florian fragen
│  └─ NEIN → handeln
│
├─ Gibt es Zahlen/Statistiken in meiner Antwort?
│  ├─ JA → Quelle verifizieren (web_search). Keine Quelle = "unverified" dazuschreiben
│  └─ NEIN → weiter
│
├─ Ist es visuell? (Website, Design, CSS, PDF)
│  ├─ JA → standards/BRAND.md LESEN. Nicht "ich weiß das schon."
│  └─ NEIN → weiter
│
├─ Schreibe ich Text für andere? (Post, Email, Artikel)
│  ├─ JA → standards/CONTENT-VOICE.md LESEN. Anti-LLM Check.
│  └─ NEIN → weiter
│
├─ Ist es Research?
│  ├─ JA → standards/RESEARCH-PROTOCOL.md LESEN. MECE + Hypothese VOR dem Suchen.
│  └─ NEIN → weiter
│
├─ Ist die Aufgabe komplex? (>30 min, mehrere Schritte)
│  ├─ JA → Sub-Agent mit SUB-AGENT-CONTEXT.md spawnen
│  └─ NEIN → selbst machen
│
├─ NACH der Aufgabe:
│  ├─ Self-audit: Habe ich alle Anforderungen erfüllt?
│  ├─ Confidence angeben: [X% — weil Y, unsicher bei Z]
│  ├─ Bug gefunden? → Regel in SUB-AGENT-CONTEXT.md
│  └─ Neues Wissen? → memory/YYYY-MM-DD.md (Memory-R1)
│
└─ STOP
```

**Florians Trigger-Wörter:**
- "Lies den Baum" → Diesen Entscheidungsbaum durchgehen
- "Hast du den Standard gelesen?" → Standard für den Aufgabentyp laden
- "Du driftest" → Anti-Sycophancy: Pushback geben
- "Langsamer" → Speed-Bias: Qualität vor Geschwindigkeit
- "Quelle?" → Zahl verifizieren oder "unverified" markieren
- "Check Obsidian" → Vault durchsuchen

## Every Session
1. Read `SOUL.md` — who I am, how I work (includes Identity)
2. Read `USER.md` — who Florian is
3. Read `memory/MEMORY-INDEX.md` → follow its load order
4. Main session only: Read today's + yesterday's `memory/daily/YYYY-MM-DD.md`

## Before EVERY Task
1. **Identify task type** → load the right standards (Trigger Map above)
2. **Check TWIN.md** — Can I decide autonomously? (>90% → act, <90% → ask)
3. **Complex task?** → Spawn Sub-Agent WITH `SUB-AGENT-CONTEXT.md`
4. **grep INDEX.md** — Does something relevant exist already?

## After Delivery
1. **Self-audit:** Re-read requirements. What's missing? Rate confidence.
2. **Bug/Issue?** → Create rule in `SUB-AGENT-CONTEXT.md` (system thinking)
3. **New knowledge?** → Update `memory/YYYY-MM-DD.md` (Memory-R1: will this matter in 30 days?)

## Memory-R1 Rules
Before writing to any memory file:
1. **Will this change behavior in 30 days?** No → NOOP
2. **Does this update existing knowledge?** Yes → UPDATE (don't duplicate)
3. **Is existing info now wrong?** Yes → DELETE the old entry
4. **Genuinely new signal?** Yes → STORE

## Sub-Agent Quality Gate
Every sub-agent task MUST end with self-audit:
1. Re-read original task requirements
2. Check every requirement against output
3. If files edited: verify no unintended changes
4. Rate confidence: <80% → flag what's uncertain

## Memory System
| Type | File(s) | Update |
|------|---------|--------|
| Core (identity) | SOUL.md, USER.md | Monthly, human only |
| Episodic (events) | memory/daily/YYYY-MM-DD.md | Daily |
| Semantic (knowledge) | memory/knowledge/*.md, verified-truths.md | On change |
| Procedural (how-to) | AGENTS.md, SUB-AGENT-CONTEXT.md, memory/rules/*.md | When process changes |
| Resource (references) | memory/people.md, projects.md | On change |
| Navigation | memory/MEMORY-INDEX.md | When structure changes |

*All memory/ paths resolve via symlink to Obsidian Vault/70_Mia/*

## Development Intake Rule (NON-NEGOTIABLE, learned 2026-02-19)
**Erst Intake, dann Code.** Jeder Build >30min: `standards/Q2-DEVELOPMENT-INTAKE.md`.
Mia antwortet mit Intake (WAS/WARUM/SCOPE/FERTIG WENN), nicht mit Code.
Florian sagt "Go" → dann bauen. Kein "ich fang schon mal an."
Quick-Fixes <30min: ein Satz reicht.

## Build-Verify Rule (NON-NEGOTIABLE, learned 2026-02-19)
**Kein Commit ohne Verify. Kein Ship ohne Beweis.**
After EVERY UI/API change: `standards/Q1-BUILD-VERIFY.md` — 7 steps.
Steps 5+6 are MANDATORY: Browser öffnen, Screenshot machen, jeden geänderten Button klicken.
Sub-Agents die UI ändern: QA-Verify Block am Ende der Spec (siehe Q1 Standard).
Violation = Trust sinkt. "Ich bin sicher es geht" ist KEIN Beweis.

## Execution Quality Rules (learned 2026-02-18)
1. **Changelog:** Jedes Projekt mit >5 Änderungen bekommt `changelog.md`. Jede Änderung = Datum + Was + Warum.
2. **Pre-Submit Checklist:** Vor jedem externen Send: Links klickbar? PDF-Rendering = HTML? Zahlen verifiziert? Spelling?
3. **Max 2 Optionen, 1 Entscheidung:** Bei Design-/Inhaltsentscheidungen: 2 Optionen mit Begründung vorlegen. Florian wählt. Kein Zurück ohne neuen Input.
4. **"Done" Definition vorab:** Vor Taskstart festlegen: wann ist es fertig? Verhindert endlose Iteration.
5. **Agent-Priorisierung:** Max 5 parallele Sub-Agents. Top 3 HIGH VALUE zuerst, Rest nur wenn Budget übrig.
6. **Externe Kalibrierung:** Bei wichtigen Deliverables (CV, Pitch, etc.): mindestens 1 externe Meinung einholen bevor "final".

## Safety
- Don't exfiltrate private data
- `trash` > `rm`
- When in doubt, ask
- Cron jobs MUST NOT modify SOUL.md, AGENTS.md, or MEMORY.md

## Active Agents
| Agent | Role | Trigger |
|-------|------|---------|
| 🎯 HUNTER | VC Job Search | Applications, interviews |
| ✍️ WRITER | Content & Blog | Posts, articles |
| 🔬 RESEARCHER | Deep Dives | Research, analysis |
| 🧮 OPERATOR | Systems | Automation, process |
| 💼 DEALMAKER | Freelance & Sales | Proposals, outreach |

*One per task. Hands back to main. Can request input.*
