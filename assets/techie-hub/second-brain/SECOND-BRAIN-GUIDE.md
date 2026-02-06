# The Ultimate Obsidian Second Brain Guide

**A complete system to capture, connect, and compound your knowledge.**

---

## Table of Contents

1. [Philosophy: Why a Second Brain?](#philosophy-why-a-second-brain)
2. [Folder Structure](#folder-structure)
3. [Essential Plugins (20 Recommended)](#essential-plugins-20-recommended)
4. [Dataview Dashboards](#dataview-dashboards)
5. [AI Integration](#ai-integration)
6. [Building the Habit](#building-the-habit)
7. [Migration Guide](#migration-guide)
8. [Quick Start Checklist](#quick-start-checklist)

---

## Philosophy: Why a Second Brain?

Your brain is for **having ideas**, not storing them.

A Second Brain is an external system that:
- **Captures** everything worth remembering
- **Connects** ideas across time and contexts
- **Compounds** knowledge into insights
- **Creates** leverage through reusable thinking

**The ROI:**
- Find anything in seconds
- Never lose an idea again
- See patterns you'd otherwise miss
- Build on past thinking instead of starting from scratch

This system is inspired by Tiago Forte's PARA method, Zettelkasten principles, and real-world use by founders, researchers, and operators.

---

## Folder Structure

```
📁 Your Vault/
├── 📁 00-Inbox/              # Quick capture, process weekly
├── 📁 01-Daily/              # Daily notes (auto-generated)
├── 📁 10-Projects/           # Active work (time-bound)
├── 📁 20-Areas/              # Ongoing responsibilities
├── 📁 30-Resources/          # Reference material by topic
├── 📁 40-Archive/            # Completed projects
├── 📁 50-People/             # Notes on people you know
├── 📁 60-Meetings/           # Meeting notes (dated)
├── 📁 70-Books/              # Book notes and highlights
├── 📁 80-Decisions/          # Decision logs
├── 📁 90-Templates/          # Note templates
└── 📁 99-System/             # Meta, dashboards, guides
```

### Folder Purposes

**00-Inbox** — Your capture zone. Anything that doesn't have a home yet lands here. Process weekly.

**01-Daily** — Dated notes (YYYY-MM-DD). Your daily log, scratchpad, and anchor point. Link liberally.

**10-Projects** — Time-bound efforts with a goal and deadline. Examples: "Launch Product," "Write eBook," "Organize Conference." Archive when complete.

**20-Areas** — Ongoing responsibilities without end dates. Examples: "Health," "Finance," "Learning," "Career." Standards to maintain.

**30-Resources** — Evergreen reference organized by topic. Examples: "AI," "Marketing," "Fundraising." Your personal Wikipedia.

**40-Archive** — Completed projects. Keep for reference but out of sight.

**50-People** — One note per person. Context, conversations, and follow-ups. Your private CRM.

**60-Meetings** — Meeting notes with attendees, agenda, decisions, and action items. Dated.

**70-Books** — Book summaries, highlights, and key takeaways. What you actually remember.

**80-Decisions** — Important decisions with context, options, and reasoning. Review yearly.

**90-Templates** — Reusable note templates for consistency.

**99-System** — Dashboards, this guide, and vault documentation.

---

## Essential Plugins (20 Recommended)

### Core Workflow

**1. Dataview** ⭐️  
*Dynamic queries and live databases*  
Why: Turn your notes into a queryable database. Power every dashboard.  
Use case: "Show all tasks due this week from project notes."

**2. Templater** ⭐️  
*Advanced template engine with variables and scripts*  
Why: Auto-fill dates, prompts, and dynamic content in templates.  
Use case: Daily notes with auto-generated headings and weather.

**3. Calendar**  
*Visual monthly calendar for daily notes*  
Why: Navigate daily notes visually. See your consistency.  
Use case: Click a date to create/open that day's note.

**4. Periodic Notes**  
*Auto-create daily, weekly, monthly, yearly notes*  
Why: Never manually create dated notes again.  
Use case: Daily notes appear automatically with your template.

**5. Tasks** ⭐️  
*Advanced task management with queries*  
Why: Track tasks with due dates, priorities, and recurrence.  
Use case: "Show all high-priority tasks not started yet."

### Knowledge Connection

**6. Graph Analysis**  
*Visualize note connections*  
Why: See clusters, orphans, and connection patterns.  
Use case: Discover emerging topics from interconnected notes.

**7. Outgoing Links**  
*Show links and backlinks side by side*  
Why: Quickly see what a note connects to.  
Use case: Understanding context when reviewing old notes.

**8. Tag Wrangler**  
*Rename and organize tags easily*  
Why: Keep your tag system clean as it evolves.  
Use case: Merge `#productivity` and `#gtd` into one.

**9. QuickAdd** ⭐️  
*Rapid capture with one-click templates*  
Why: Capture thoughts in <5 seconds.  
Use case: Hotkey for instant meeting note or person note.

### Writing & Editing

**10. Advanced Tables**  
*Spreadsheet-like table editing*  
Why: Make tables actually usable in Markdown.  
Use case: Competitive analysis, comparison matrices.

**11. Linter**  
*Auto-format notes with rules*  
Why: Consistent formatting without thinking.  
Use case: Auto-fix YAML frontmatter, remove trailing spaces.

**12. Editor Syntax Highlight**  
*Syntax highlighting for code blocks*  
Why: Readable code snippets.  
Use case: Save SQL queries, Python scripts, API examples.

**13. Paste URL into Selection**  
*Turn selected text into a link by pasting URL*  
Why: Faster link creation.  
Use case: Highlight "this article" and paste URL—done.

### Capture & Import

**14. Omnivore** or **Readwise**  
*Import highlights from articles and books*  
Why: Your reading → your Second Brain automatically.  
Use case: Kindle highlights auto-sync to book notes.

**15. Excalidraw**  
*Sketching and diagramming inside Obsidian*  
Why: Visual thinking integrated with notes.  
Use case: System diagrams, wireframes, visual explanations.

**16. Web Clipper** (official)  
*Save web content to Obsidian*  
Why: Capture articles, tweets, and research.  
Use case: Save a blog post as markdown with one click.

### AI & Automation

**17. Smart Connections** ⭐️  
*AI-powered note suggestions and semantic search*  
Why: Surface relevant notes you forgot about.  
Use case: Writing about AI—plugin suggests related past notes.

**18. Text Generator** or **Copilot**  
*AI writing assistance inside Obsidian*  
Why: Generate, expand, or refine text inline.  
Use case: Draft a meeting summary from bullet points.

### Productivity

**19. Commander**  
*Add commands to UI (ribbons, hotkeys, etc.)*  
Why: Customize your workspace for your workflow.  
Use case: Add "Weekly Review" button to sidebar.

**20. Kanban**  
*Task boards inside notes*  
Why: Visual project management.  
Use case: Track blog post pipeline: Idea → Draft → Edit → Published.

### Installation

Settings → Community Plugins → Browse → Search by name → Install → Enable

Start with: **Dataview, Templater, Calendar, Tasks, QuickAdd** — then add as needed.

---

## Dataview Dashboards

Place these in `99-System/Dashboard.md` or within daily notes.

### 1. Task Dashboard

```dataview
TASK
WHERE !completed
GROUP BY file.folder
SORT priority DESC, due ASC
```

**What it does:** Shows all incomplete tasks grouped by folder, sorted by priority and due date.

**Use case:** Morning review—what needs attention today?

---

### 2. Recent Notes

```dataview
TABLE file.mtime AS "Last Modified", summary AS "Summary"
FROM ""
WHERE file.mtime >= date(today) - dur(7 days)
SORT file.mtime DESC
LIMIT 20
```

**What it does:** Shows notes modified in the last 7 days with their summaries.

**Use case:** Quick context on what you've been working on.

---

### 3. Project Overview

```dataview
TABLE status, deadline, priority, progress
FROM "10-Projects"
WHERE status != "archived"
SORT priority DESC, deadline ASC
```

**What it does:** Live project tracker with status, deadlines, and priorities.

**Use case:** Weekly review—what projects need focus?

**Required frontmatter in project notes:**
```yaml
status: active | paused | completed | archived
deadline: 2026-03-15
priority: high | medium | low
progress: 30%
```

---

### 4. Reading List

```dataview
TABLE author, status, rating, dateFinished AS "Finished"
FROM "70-Books"
WHERE status = "reading" OR status = "to-read"
SORT status ASC, dateStarted DESC
```

**What it does:** Shows books you're reading or plan to read.

**Use case:** Pick your next book. Track reading progress.

**Required frontmatter:**
```yaml
author: "Author Name"
status: to-read | reading | finished
rating: 0-5
dateStarted: 2026-01-15
dateFinished: 2026-02-01
```

---

### 5. People Dashboard

```dataview
TABLE lastContact, relationship, nextAction AS "Next Action"
FROM "50-People"
WHERE nextAction
SORT lastContact ASC
```

**What it does:** Shows people you need to follow up with.

**Use case:** Relationship maintenance—who haven't you talked to in a while?

**Required frontmatter:**
```yaml
lastContact: 2026-01-20
relationship: colleague | friend | mentor | client
nextAction: "Send update on project"
```

---

### Bonus: Unlinked Notes (Orphans)

```dataview
TABLE file.inlinks AS "Backlinks", file.outlinks AS "Links"
FROM ""
WHERE length(file.inlinks) = 0 AND length(file.outlinks) = 0
SORT file.name ASC
```

**What it does:** Find isolated notes with no connections.

**Use case:** Weekly cleanup—connect or delete orphans.

---

## AI Integration

Connect your Second Brain to AI for supercharged thinking.

### Option 1: Claude / ChatGPT (API)

**Plugin:** Text Generator or Copilot  
**Setup:**
1. Get API key from Anthropic or OpenAI
2. Install plugin → Settings → Add API key
3. Configure commands (summarize, expand, ask)

**Use cases:**
- "Summarize this meeting note"
- "Expand these bullet points into a blog post"
- "Generate 10 questions about this topic"

**Cost:** ~$5-20/month depending on usage

---

### Option 2: Local LLMs (Privacy-First)

**Tools:** Ollama + Text Generator  
**Setup:**
1. Install Ollama: `https://ollama.ai`
2. Pull a model: `ollama pull llama3` or `mistral`
3. Point Text Generator to `http://localhost:11434`

**Pros:** Free, private, offline  
**Cons:** Slower, requires decent hardware (16GB+ RAM recommended)

---

### Option 3: Smart Connections (Semantic Search)

**Plugin:** Smart Connections  
**What it does:** Uses embeddings to find conceptually similar notes.

**Setup:**
1. Install plugin
2. Choose: OpenAI API or local embeddings
3. Let it index your vault (one-time)

**Use case:** You're writing about "delegation" — it surfaces your notes on "hiring," "trust," and "systems" even if they don't use the word "delegation."

---

### Option 4: ChatGPT with Entire Vault Context

**Workflow:**
1. Export vault to markdown (use Obsidian Markdown Export plugin)
2. Upload to ChatGPT or Claude (Code Interpreter / Projects)
3. Ask: "Based on my notes, what patterns do you see?" or "Help me write a post on X using my past thinking."

**Pros:** Deep context, powerful analysis  
**Cons:** Manual, privacy considerations (don't upload sensitive info)

---

### AI-Powered Workflows

**Daily Summary:**  
Templater script → pull yesterday's note → send to AI → get 3-bullet summary → insert in today's note.

**Meeting Notes → Action Items:**  
Write raw notes → run AI command → extract tasks → auto-create task blocks.

**Book Notes → Twitter Thread:**  
Write book summary → AI command: "Turn this into a 7-tweet thread" → review + post.

**Question Answering:**  
Select text → ask AI: "Explain like I'm 12" or "Give me 3 counterarguments."

---

## Building the Habit

Systems fail without habits. Here's how to make this stick.

### Daily Workflow (10 minutes)

**Morning (5 min):**
1. Open today's daily note (auto-created)
2. Review calendar for the day
3. Check task dashboard — flag 3 priorities
4. Write: "Today's intention: ______"

**Evening (5 min):**
1. Brain dump — capture loose thoughts
2. Link today's note to relevant people/projects
3. Mark tasks as done
4. Write: "One thing I learned today: ______"

**Key:** Do it at the same time daily. Anchor to existing habit (after coffee, before bed).

---

### Weekly Review (30 minutes)

**Friday afternoon or Sunday evening:**

1. **Process Inbox** (10 min)  
   - Go through 00-Inbox/  
   - Move to proper folders  
   - Create links  
   - Delete noise

2. **Review Projects** (10 min)  
   - Check 10-Projects/ dashboard  
   - Update statuses, progress  
   - Archive completed projects  
   - Adjust priorities

3. **Reflect** (10 min)  
   - Review last 7 daily notes  
   - Extract patterns → create resource note if needed  
   - Update people notes (who did you talk to?)  
   - Plan next week's focus

Use `90-Templates/weekly-review.md` for structure.

---

### Monthly Cleanup (1 hour)

**Last Sunday of the month:**

1. **Orphan Audit** — Run orphan query, connect or delete
2. **Tag Cleanup** — Merge redundant tags (use Tag Wrangler)
3. **Archive Sweep** — Move completed projects to 40-Archive/
4. **Template Tune-Up** — Improve templates based on usage
5. **Plugin Review** — Disable unused plugins, try one new one
6. **Backup Check** — Ensure vault is backed up (iCloud, Git, or Obsidian Sync)

---

### Habit-Building Tips

**Start small:** Just daily notes for 2 weeks. Don't touch anything else.  
**Don't over-organize:** Capture first, organize later. Inbox is fine.  
**Link > Tag:** Tags categorize. Links connect. Links compound.  
**Review weekly:** Knowledge decays without review. 10 minutes saves hours.  
**Delete freely:** Not everything is worth keeping. Clarity > completeness.  
**Make it yours:** Adapt this system. Break the rules. Keep what works.

---

## Migration Guide

### From Notion

**What to migrate:**
- Tasks → Use Dataview + Tasks plugin
- Databases → Frontmatter + Dataview tables
- Linked databases → MOCs (Maps of Content) with queries
- Pages → Individual markdown files
- Relations → Wiki links `[[Page Name]]`

**Export process:**
1. Notion: Settings → Export → Markdown & CSV
2. Unzip the export
3. Obsidian: Drag folders into vault
4. Clean up: Remove Notion IDs, fix image paths
5. Use Linter plugin to standardize formatting

**Challenges:**
- Notion's databases → You'll rebuild with frontmatter + Dataview
- Inline databases → Create separate notes + queries
- Formulas → Some can be done with Dataview, others need manual

**Upside:** You own the data. It's future-proof markdown.

---

### From Evernote

**What to migrate:**
- Notes → Markdown files
- Notebooks → Folders
- Tags → Keep tags or convert to folders
- Attachments → Embedded files

**Export process:**
1. Evernote: Select notes → Export → ENEX format
2. Use tool: `https://github.com/wormi4ok/evernote2md`
3. Run: `evernote2md yourfile.enex -o output-folder`
4. Move output into Obsidian vault
5. Review formatting (some cleaning needed)

**Challenges:**
- Web clips may need cleanup
- Rich formatting → simplified in markdown
- Reminders → recreate as tasks

---

### From Apple Notes

**What to migrate:**
- Notes → Markdown
- Folders → Obsidian folders
- Attachments → Manual copy

**Export process:**
1. Use Exporter app: `https://github.com/Automattic/simplenote-macos` or similar
2. Or manual: Copy-paste each note into Obsidian
3. For bulk: Use AppleScript or third-party tool

**Challenges:**
- No official export from Apple Notes
- Drawings/sketches → export as images
- Locked notes → unlock first

**Tip:** If <50 notes, manual migration might be fastest.

---

### From Roam Research

**What to migrate:**
- Pages → Notes
- Daily notes → Keep structure
- Block references → Embed links `![[Note#heading]]`
- Queries → Dataview equivalents

**Export process:**
1. Roam: Settings → Export All → Markdown
2. Unzip into vault
3. Install plugin: "Roam Import Converter"
4. Run converter to fix link syntax

**Challenge:** Roam's outliner style vs. Obsidian's long-form. Adjust as you go.

---

### General Tips

**Don't migrate everything:** Only bring notes worth keeping. Fresh start is okay.  
**Batch by value:** Start with projects, key resources, people. Leave old junk.  
**Accept imperfection:** Some formatting will break. Fix as you encounter it.  
**Set a deadline:** Spend max 2 weekends migrating, then move forward.

---

## Quick Start Checklist

**Week 1: Setup**
- [ ] Install Obsidian
- [ ] Create folder structure (copy from above)
- [ ] Install core plugins: Dataview, Templater, Calendar, Tasks
- [ ] Copy templates from this package to `90-Templates/`
- [ ] Create today's daily note
- [ ] Write one note (anything!) and link it

**Week 2: Habit**
- [ ] Daily note every day (even if short)
- [ ] Capture 5+ thoughts in Inbox
- [ ] Create 3+ resource notes
- [ ] Link notes together (5+ links)
- [ ] Review weekly (use template)

**Week 3: Expand**
- [ ] Add 3 more plugins from recommended list
- [ ] Create a dashboard with 2 Dataview queries
- [ ] Start a project note
- [ ] Create person notes for 5 people
- [ ] Try AI integration (pick one option)

**Week 4: Compound**
- [ ] Monthly cleanup
- [ ] Reflect: What's working? What's not?
- [ ] Customize: Adjust templates, add queries
- [ ] Teach someone: Explaining = understanding
- [ ] Commit: Make this your system for 90 days

---

## What Makes This a $49 System?

**Templated structure:** Plug-and-play, not theory  
**Battle-tested plugins:** Curated from 1000+ available  
**Copy-paste queries:** Working Dataview code, not docs  
**AI integration:** Actual setup steps, not vague ideas  
**Migration paths:** Real export → import workflows  
**Habit playbook:** Not just tools, but how to use them daily

Most guides give you philosophy. This gives you **a working system in <1 hour.**

---

## Support & Community

**Questions?**  
- Obsidian Forum: `https://forum.obsidian.md`
- r/ObsidianMD: `https://reddit.com/r/ObsidianMD`
- Discord: `https://obsidian.md/community`

**Feedback on this guide?**  
Open an issue or PR on GitHub. This is a living document.

---

**Now go build your Second Brain. Your future self will thank you.**

---

*Version 1.0 | Last updated: 2026-02-06*  
*Created by Florian Ziesche for Techie Hub*  
*License: MIT — Use freely, share widely*
