# TOOLS.md - Available Tools & Local Notes

What King has access to and your environment-specific setup.

---

## Core Principle

Check this file before saying "I can't do that." You probably can.

When you need a tool:
1. Check if it's listed here
2. Read the skill's `SKILL.md` if available
3. Use it
4. If it fails, document why and try an alternative

---

## Why This File Exists

**Skills define *how* tools work. This file is for *your* specifics.**

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

Add whatever helps you do your job. This is your cheat sheet.

---

# Part 1: Tool Inventory

## Communication Channels

### 📱 Telegram (Primary)
- **Status:** ✅ Active
- **Use for:** All direct communication with Florian
- **Bot name:** @[your_bot_name]
- **Capabilities:** Text, images, files, voice messages
- **Notes:** Primary channel for heartbeats and alerts

### 💬 Discord
- **Status:** ⬜ Not configured
- **Use for:** Community interactions, group chats
- **Setup:** Add bot token when ready

### 📧 Email (Gmail)
- **Status:** ⬜ Not configured
- **Use for:** Reading inbox, drafting emails
- **Permissions needed:** Gmail API access
- **Rules:** 
  - Can READ freely
  - ASK before sending anything
  - Never auto-reply without permission

### 📅 Google Calendar
- **Status:** ⬜ Not configured
- **Use for:** Checking schedule, upcoming events, meeting prep
- **Permissions needed:** Google Calendar API
- **Rules:**
  - Can READ freely
  - ASK before creating/modifying events

---

## Knowledge & Memory

### 📝 Notion
- **Status:** ⬜ Not configured
- **API Key:** Set in environment
- **Workspaces accessible:**
  - FZ - Compounding AI Engine (main workspace)
  - CEO Framework Template
- **Use for:**
  - Reading tasks, projects, databases
  - Creating/updating tasks
  - Accessing AI Prompts Library
  - Content Pipeline management
- **Key databases:**
  - Tasks: `[database_id]`
  - People: `[database_id]`
  - Content Pipeline: `[database_id]`
  - Leads: `[database_id]`
- **Rules:**
  - Can READ freely
  - Can CREATE tasks and notes
  - ASK before deleting anything

### 🗄️ Obsidian
- **Status:** ✅ Configured
- **Vault location:** `/Users/florianziesche/Library/Mobile Documents/iCloud~md~obsidian/Documents/System_OS/`
- **Vault name:** System_OS (syncs via iCloud)
- **Use for:**
  - Private notes and thinking
  - Prompts library
  - Knowledge base (compounds over time)
  - Lessons learned (your moat)
  - People notes (CRM-lite)
- **Folder structure:**
```
  /00-Inbox          — Quick capture, process weekly
  /01-Daily          — Daily notes
  /10-Projects       — Active work by priority
  /20-Knowledge      — Evergreen reference (AI, VC, Fundraising)
  /30-People         — Notes on people you meet
  /40-Prompts        — Your prompt library
  /50-Tools          — How you use your stack
  /60-Lessons        — Hard-won insights (FEED TO AI)
  /70-Templates      — Reusable structures
  /80-Archive        — Done but worth keeping
  /99-System         — Meta, vault guide
```
- **Rules:**
  - Can READ and WRITE freely
  - This is the private thinking space
  - Knowledge + Lessons = your compound moat

### 🧠 Local Memory
- **Location:** `./memory/`
- **Files:**
  - `YYYY-MM-DD.md` — Daily logs
  - `MEMORY.md` — Long-term curated memory
  - `heartbeat-state.json` — Check tracking
- **Rules:**
  - Update daily files in real-time
  - Curate MEMORY.md during heartbeats
  - Never delete, only append or update

---

## AI & Language Models

### 🤖 Claude (Anthropic)
- **Status:** ✅ Primary model
- **API Key:** `ANTHROPIC_API_KEY`
- **Use for:** Main reasoning, complex tasks
- **Model:** Claude Sonnet/Opus as configured
- **Notes:** Florian's preferred AI

### 🔮 Gemini (Google)
- **Status:** ⬜ Available
- **API Key:** `GEMINI_API_KEY`
- **Use for:** Alternative model, specific tasks
- **Notes:** Good for certain research tasks

### 💬 ChatGPT (OpenAI)
- **Status:** ⬜ Available
- **API Key:** `OPENAI_API_KEY`
- **Use for:** Backup, specific use cases
- **Notes:** Secondary AI in Florian's stack

---

## Voice & Media

### 🎙️ ElevenLabs (TTS)
- **Status:** ⬜ Not configured
- **API Key:** `ELEVENLABS_API_KEY`
- **Use for:**
  - Voice messages
  - Story narration
  - Audio briefings
- **Preferred voice:** [See Local Notes below]
- **Rules:**
  - Use for engaging content (stories, summaries)
  - Don't overuse — text is often better

### 🎨 Midjourney
- **Status:** ⬜ External tool
- **Use for:** Image generation
- **Access:** Via Discord or web
- **Notes:** Florian uses for visuals

---

## Automation & Integration

### ⚡ n8n
- **Status:** ⬜ Not configured
- **Use for:**
  - Complex automation workflows
  - Multi-step integrations
  - Scheduled tasks beyond heartbeats
- **Notes:** Florian's automation platform

### 🔗 Zapier
- **Status:** ⬜ Not configured
- **Use for:** Simple integrations
- **Notes:** Backup to n8n

---

## Web & Research

### 🌐 Web Search
- **Status:** ✅ Available
- **Use for:**
  - Research
  - Fact-checking
  - Current information
- **Rules:**
  - Search freely for research tasks
  - Cite sources when relevant

### 🔍 Perplexity
- **Status:** ⬜ External tool
- **Use for:** Deep research, fact grounding
- **Notes:** Florian uses for research

---

## Development & Code

### 💻 Terminal/Shell
- **Status:** ✅ Available
- **Use for:**
  - File operations
  - Git commands
  - Running scripts
- **Rules:**
  - `trash` > `rm` (always)
  - ASK before destructive commands
  - Can freely: read, list, navigate, git status

### 📂 File System
- **Status:** ✅ Available
- **Location:** Workspace root + configured paths
- **Rules:**
  - Can READ freely
  - Can WRITE to workspace and memory
  - ASK before writing outside workspace

### 🐙 GitHub
- **Status:** ⬜ Not configured
- **Use for:**
  - Code repositories
  - Project tracking
  - Commits and PRs
- **Repos to track:**
  - Legal AI Platform: `[repo_url]`
  - Manufacturing Software: `[repo_url]`

---

## Location & Environment

### 📍 Google Places
- **Status:** ⬜ Not configured
- **API Key:** `GOOGLE_PLACES_API_KEY`
- **Use for:**
  - Location lookups
  - Meeting venue info
  - Travel planning

### 🌤️ Weather
- **Status:** ⬜ Not configured
- **Use for:** Daily briefings, travel planning
- **Location:** NYC (default)

---

# Part 2: Local Notes (Your Setup)

*Environment-specific details that don't belong in shared skills.*

### TTS Voices
- **Preferred voice:** [To be set — e.g., "Nova" (warm, slightly British)]
- **Default speaker:** [To be set]
- **Backup voice:** [To be set]

### SSH Hosts
```
[alias] → [IP], user: [username]
```

### Cameras
```
[name] → [location], [notes]
```

### Device Nicknames
```
[nickname] → [actual device/service]
```

### Locations
- **Home:** [address]
- **Office/Coworking:** [address]
- **Gym:** [address]

### Network
- **Home WiFi:** [network name]
- **Server IP:** [if applicable]

### Other Environment Notes
```
[Add as needed]
```

---

# Part 3: Quick Reference

## Tool Status Legend

| Symbol | Meaning |
|--------|---------|
| ✅ | Active and configured |
| ⬜ | Available but not configured |
| ❌ | Not available |
| 🔒 | Restricted access |

## Tool Preferences (Florian's Stack)

| Category | Primary | Secondary |
|----------|---------|-----------|
| AI | Claude | ChatGPT, Gemini |
| Notes (Public) | Notion | — |
| Notes (Private) | Obsidian | — |
| Automation | n8n | Zapier |
| Communication | Telegram | Email |
| Research | Web + Perplexity | — |
| Voice | ElevenLabs | — |
| Images | Midjourney | — |

## Credentials Location

All API keys stored in environment variables. Never log or expose them.
```
ANTHROPIC_API_KEY=***
OPENAI_API_KEY=***
GEMINI_API_KEY=***
ELEVENLABS_API_KEY=***
GOOGLE_PLACES_API_KEY=***
TELEGRAM_BOT_TOKEN=***
NOTION_API_KEY=***
```

## Permission Quick Reference

| Action | Permission |
|--------|------------|
| Read files | ✅ Freely |
| Write to workspace | ✅ Freely |
| Search web | ✅ Freely |
| Read Notion | ✅ Freely |
| Create Notion tasks | ✅ Freely |
| Read calendar | ✅ Freely |
| Read email | ✅ Freely |
| Send Telegram | ✅ Freely |
| Send email | ⚠️ Ask first |
| Create calendar events | ⚠️ Ask first |
| Delete anything | ⚠️ Ask first |
| Post to social media | ⚠️ Ask first |
| Run destructive commands | ⚠️ Ask first |

---

## Adding New Tools

When a new tool is added:
1. Document it in Part 1 with status, use case, and rules
2. Add environment-specific details to Part 2
3. Create skill file if complex: `skills/[tool]/SKILL.md`
4. Test it works
5. Update status (⬜ → ✅)

---

*Last updated: 2026-01-31*
*Update this file as tools are configured and local details are learned*
---

## 📁 Local File System (~/FZ/)

- **Status:** ✅ Configured
- **Location:** `~/FZ/`
- **Use for:**
  - Heavy files (PDFs, code archives, exports)
  - AI conversation exports
  - Project assets that don't fit in Obsidian
- **Structure:**
```
  /AI-Conversations    — ChatGPT, Claude exports
  /Projects            — Mirrors Obsidian 10-Projects (heavy files)
  /Resources           — CVs, contracts, templates, reference docs
  /Inbox               — Temporary landing zone
```
- **Rules:**
  - Can READ and WRITE freely
  - Process Inbox weekly
  - Heavy files here, notes in Obsidian

### TTS Voice (DECIDED 2026-02-14)
- **Mia's Stimme:** Matilda — Knowledgeable, Professional (XrExE9yKIg1WjnnlVkGX)
- **API Key:** ELEVENLABS_API_KEY in ~/.zshrc
- **Backup für Floriana-Geschichten:** Lily (warm, samtig)
