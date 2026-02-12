# Technical Setup — Tools, Pfade, Konfiguration

*Semantisches Gedächtnis: Technisches Environment*  
*Quelle: MEMORY.md, TOOLS.md*  
*Aktualisiert: 2026-02-10*

---

## LaTeX Setup

- **Distribution:** TinyTeX
- **Engine:** XeLaTeX
- **PATH:** `$HOME/Library/TinyTeX/bin/universal-darwin`
- **Use Case:** Print-PDFs, Reports (LaTeX > HTML für Print!)

**Installierte Packages:**
```bash
tlmgr list --only-installed
```

**Pattern:** LaTeX für alles was gedruckt werden soll. HTML für Dashboards/Web.

---

## Obsidian Vault

- **Vault Name:** System_OS
- **Location:** `~/Library/Mobile Documents/iCloud~md~obsidian/Documents/System_OS/`
- **Sync:** iCloud
- **Structure:** PARA (Projects / Areas / Resources / Archive)

**Key Folders:**
```
00-Inbox          — Quick capture
01-Daily          — Daily notes (YYYY-MM-DD.md)
10-Projects       — Active work
20-Areas          — Areas of responsibility
60-Resources      — Reference, Knowledge
70-Templates      — Reusable structures
80-Archive        — Done but worth keeping
99-System         — Meta, vault guide
```

**Plugins Installed (2026-02-10):**
- **Smart Connections v4.1.8** — Semantic search, local embeddings
  - Model: Multilingual E5 Small (free, local, handles DE/EN mix)
  - Settings: Result Limit 20, Lookup 50, Heading-level blocks ON
  - Exclude: Templates, System folders
  - Status: ✅ Active, configured by Florian

**Wikilinks Rule:** NUR Filename `[[Datei]]`, NIEMALS `[[Ordner/Datei]]`

---

## Sub-Agents

- **Max parallel:** 5
- **Model:** Sonnet (default für Sub-Agents)
- **Use Case:** Spezialisierte, fokussierte Tasks
- **Pattern:** Delegate → Agent arbeitet → Returns output → Main agent delivers

---

## Desktop-Ordner (~/FZ/)

```
01-Dashboards     — HTML Dashboards mit Ainary CI
02-Active         — Aktive Projekte, Deliverables
03-Mia-Brand      — Mia-spezifische Assets
AI-Conversations  — ChatGPT, Claude exports
Projects          — Heavy files (mirrors Obsidian)
Resources         — CVs, Contracts, Templates, Reference
Inbox             — Temporary landing zone (process weekly)
```

**Rule:** Heavy files → ~/FZ/, Notes → Obsidian

---

## Workspace

- **Location:** `/Users/florianziesche/.openclaw/workspace/`
- **Use:** Primary working directory für Mia
- **Structure:**
```
agents/           — Agent roles, skills
board/            — Board Advisors (6 people)
content/          — Content strategy, ideas
memory/           — Daily logs, MEMORY.md, semantic/, procedural/
research/         — VC landscape, market research
skills/           — Tool skills (report-design, pptx-design, etc.)
standards/        — FLORIAN.md, CORPORATE-IDENTITY.md, checklists
failures/         — output-tracker.md, lessons learned
scripts/          — pre-flight.sh, pre-build-check.sh, log-send.sh
```

---

## Key Scripts

### pre-flight.sh
```bash
./scripts/pre-flight.sh [task-type]
# task-type: cnc|bm|vc|content|visual|general
```
**Use:** IMMER vor jedem Task → Zeigt welches Wissen laden

### pre-build-check.sh
```bash
./scripts/pre-build-check.sh "Feature Name"
```
**Use:** Build-Blocker System (>2 features/day mit 0 sends = blocked)

### log-send.sh
```bash
./scripts/log-send.sh "Description"
```
**Use:** Send logged → unblocks building

---

## Tools Status

| Tool | Status | Use For |
|------|--------|---------|
| Telegram | ✅ Active | Primary communication |
| Discord | ⬜ Not configured | Community, group chats |
| Gmail | ⬜ Not configured | Email (READ only, ASK before send) |
| Google Calendar | ⬜ Not configured | Schedule, meeting prep |
| Notion | ⬜ Not configured | Tasks, databases |
| ElevenLabs | ⬜ Not configured | TTS, voice messages |
| n8n | ⬜ Not configured | Automation workflows |
| Perplexity | ⬜ External | Deep research |
| Midjourney | ⬜ External | Image generation |

**Details:** See `TOOLS.md`

---

## Git Workflow

```bash
git status               # Check state
git add [file]           # Stage changes
git commit -m "msg"      # Commit
git push                 # Push to remote
```

**Rule:** Commit memory updates, deliverables. Don't commit Obsidian vault (syncs via iCloud).

---

## Research Tools

### PaperQA2
- **Status:** ⬜ Parked (not usable)
- **Issue:** OpenAI Tier 1 RPM Limit (500/min) insufficient
- **Requirement:** Needs Tier 2 ($50+ spend) or Anthropic backend
- **Alternative:** Smart Connections + Mia Scanner work well enough
- **Decision:** Not worth the cost for now (2026-02-10)

### SOTA Paper Scanner
- **Status:** ✅ Active (Cron job)
- **Schedule:** Monday + Thursday 04:00
- **Session ID:** `1dda7cb3`
- **Delivery:** Telegram announcement
- **First Run:** 47 papers scanned (2026-02-10)

### Daily Agent Research
- **Status:** ✅ Active (Cron job)
- **Schedule:** Daily 05:00
- **Session ID:** `5ada58d2`
- **Delivery:** Telegram announcement with cross-learnings
- **Note:** Only suggests, Florian confirms vault changes

---

## Related

- `TOOLS.md` — Vollständige Tool-Dokumentation
- `skills/*/SKILL.md` — Spezifische Tool-Skills
- `memory/procedural/vault-rules.md` — Obsidian-Regeln
- `memory/procedural/research-methodology.md` — Research experiments

---

*Update this file when tools are configured or paths change*
