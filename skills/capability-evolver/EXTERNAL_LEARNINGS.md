# External Learnings — Gesammelte Best Practices

*Quellen die Atlas regelmäßig scannt um besser zu werden.*

---

## 📚 Source: Alex Finn's Claude Code Power User Workflow

**Repo:** https://github.com/angelor888/claude-code-project
**Gelernt am:** 2026-02-02

### Die 7 Regeln (für task-basiertes Denken)

1. **Erst denken** — Problem durchdenken, Codebase lesen, Plan in tasks/todo.md schreiben
2. **Todo-Liste** — Plan sollte abhakbare Items haben
3. **Check-in** — Vor Arbeitsbeginn Plan verifizieren lassen
4. **Abhaken** — Todo items als erledigt markieren während der Arbeit
5. **High-Level Updates** — Bei jedem Schritt kurze Erklärung geben
6. **Simplicity** — Jede Änderung so einfach wie möglich, minimaler Impact
7. **Review Section** — Am Ende Summary der Änderungen in todo.md

### Die 8 Produktivitäts-Tricks

| Trick | Beschreibung |
|-------|-------------|
| **Rules First** | Regeln als erstes Message in jeder Session |
| **Plan Mode Overuse** | IMMER erst planen (Shift+Tab) |
| **Git Checkpoints** | Nach JEDEM erfolgreichen Schritt committen |
| **Image Input** | Bilder für UI Inspiration & Debugging |
| **Context Clearing** | /clear nach Tasks |
| **Security Checks** | Mandatory Review nach Features |
| **Learning Prompts** | Code erklären lassen |
| **Productive Breaks** | Während AI arbeitet produktiv sein |

### Der Workflow

```
PLAN (Opus) → BUILD (Sonnet) → COMMIT (Git) → SECURITY → LEARN → CLEAR
```

### Key Insight

> "You want to OVERUSE plan mode. Never fire from the hip."

---

## 🔍 GitHub Repos to Monitor

| Repo | Warum relevant |
|------|----------------|
| angelor888/claude-code-project | Claude Code Best Practices |
| anthropics/claude-code | Official Claude Code |
| openclaw/openclaw | OpenClaw Core |
| steipete/peekaboo | macOS Automation |

---

## 📅 Scan Schedule

- **Alle 24h:** Neue Repos/Updates suchen
- **Fokus:** OpenClaw, Claude Code, AI Agents, Automation
- **Keywords:** "claude code", "openclaw", "ai agent workflow", "coding agent"

---

## 📚 Source: OpenClaw Ecosystem Scan — 2026-02-04

### Architecture Insights

1. **AgentSkills Spec** — Open standard (Anthropic → Linux Foundation, Dec 2025)
   - Skills work across: Claude Code, Cursor, VS Code, OpenAI Codex, Gemini CLI, GitHub Copilot
   - Format: SKILL.md + helper scripts in one directory
   - **Implication:** Skills wir bauen sind PORTABEL. Investment in Skills = cross-platform value.

2. **ClawHub** — clawhub.com, 700+ community skills
   - Official skill marketplace
   - Skills installierbar via `openclaw skills install`
   - **Action:** Prüfen ob unsere Custom Skills dort publishable sind (CNC-related? VC Research?)

3. **Multi-Machine Agent Orchestration**
   - Power users laufen 15+ Agents auf 3+ Maschinen
   - Daily "roll call" pattern für Agent Health Checks
   - Discord als Agent-Koordinations-Channel

4. **Local Model Support (Mac Mini Guide)**
   - Mac Mini M4 + Ollama → Kimi K2, Qwen3 lokal
   - Zero cloud costs, 100% privacy
   - Relevant für: CNC Planner Kunden die "Daten bleiben bei uns" wollen

### Workflow Patterns

| Pattern | Beschreibung | Relevanz |
|---------|-------------|----------|
| **Mobile-first ops** | Telegram/WhatsApp als primäres Interface | 🔴 High |
| **Voice conversations** | Custom voice models für Agent-Calls | 🟡 Medium |
| **Invoice automation** | Generate invoices from work summaries | 🔴 High (Freelance) |
| **Meal/life planning** | Structured Notion templates für Alltag | 🟢 Low |
| **Agent impersonation** | Agent responds as user in group chats | ⚠️ Risky |

### Community Patterns (Discord/Reddit)

- **Quick setup tools** — Reddit user built "openclaw setup in under a minute" (Claude Code integration)
- **exe.dev hosting** — New hosting option für Discord-connected OpenClaw instances
- **Beeper integration** — Unified messaging (all messengers in one) + OpenClaw
- **Homey integration** — Smart home automation

### Media Landscape

OpenClaw hat den **mainstream crossing point** erreicht:
- IBM, DataCamp, DigitalOcean, Vultr = Enterprise/Dev tools
- Shelly Palmer = mainstream tech columnists
- Multiple Substacks = creator economy
- DEV Community = developer adoption

**Signal:** Wenn IBM darüber schreibt, ist es kein Nischen-Tool mehr. Content über OpenClaw hat jetzt Mainstream-Reach.

---

## 🔍 GitHub Repos to Monitor

| Repo | Warum relevant |
|------|----------------|
| angelor888/claude-code-project | Claude Code Best Practices |
| anthropics/claude-code | Official Claude Code |
| openclaw/openclaw | OpenClaw Core |
| steipete/peekaboo | macOS Automation |
| skillsmp/clawhub | Skills Marketplace |

---

## 📅 Scan Schedule

- **Alle 24h:** Neue Repos/Updates suchen
- **Fokus:** OpenClaw, Claude Code, AI Agents, Automation
- **Keywords:** "claude code", "openclaw", "ai agent workflow", "coding agent"

---

## 📚 Source: SparkryAI — "24 Hours with OpenClaw" (2026-02-03)

### Chief of Staff Pattern

**Core Workflow:**
```
Email arrives → Cron detects → Match against profile → Notify user → User approves → Agent drafts + sends
```

**Key Design Decisions:**
1. **Trust is earned** — Start read-only, expand as confidence builds
2. **Sandbox for dev, full access for exec assistant** — Different risk profiles
3. **Dead-time is prime-time** — Best agent usage in Lyfts, airports, flights
4. **Hourly email cron** — Sweet spot between responsive and cost-efficient

### Setup Notes
- Mac Mini M2/M4 recommended for 24/7
- Cloudflare Moltworker = $5/month hosted alternative (limited capabilities)
- Claude Max subscription works natively (but Anthropic may cancel heavy users)

### Consulting Triage Pattern (Most Relevant for Florian)
```
1. Cron checks email hourly
2. Match against expertise profile (stored in USER.md/SOUL.md)
3. Categorize by fit (high/medium/low)
4. Send Telegram notification with summary
5. User says "yes" → draft response
6. User says "send" → send email
```
**Total user time: ~2 minutes.** Most consulting requests don't convert, but cost to process is near-zero.

---

## 📚 Source: Leonis Newsletter — "AI Threshold Effect" (2026-02-04)

### Thesis: OpenClaw as "Threshold Artifact"

**Pattern repeats:**
| Wave | Model Threshold | Artifact | Outcome |
|------|----------------|----------|---------|
| 2023 | GPT-4 reasoning | AutoGPT | Hype → crash (unreliable) |
| 2026 | Opus 4.5 execution | OpenClaw | Sustainable? (models reliable enough) |

**Key difference this time:** Claude Opus 4.5 can chain tools AND recover from errors. AutoGPT's GPT-4 could chain but not recover.

**Where durable value accrues (VC-relevant):**
1. NOT orchestration layers (commodity, open-source)
2. YES domain-specific skills (expertise moats)
3. YES trust/memory systems (personalization moats)
4. YES enterprise guardrails (compliance, security)

**Anthropic's response to OpenClaw:** Sprint-built "Cowork" (Jan 2026) — non-technical Claude Code for file/folder delegation. This validates the category but threatens the hobbyist layer.

**Content opportunity for Florian:**
- "I've lived through AutoGPT AND OpenClaw. Here's what VCs should know about the agent wave."
- Frame: Threshold artifacts vs durable platforms
- Unique angle: Founder-operator + VC candidate who actually USES the tools

---

## 📚 Source: OpenClaw v2026.2.3 Release Notes (2026-02-05)

### Cron System Overhaul
- **Announce delivery mode** for isolated jobs (results post to main session)
- **One-shot auto-delete** — cron jobs that run once are cleaned up automatically
- **ISO 8601 support** in schedule.at inputs
- Hard migration: all isolated jobs now use announce/none delivery

### Security Hardening (3 fixes)
- Sandboxed media paths for message attachments
- WhatsApp login gated to owner-only
- Gateway URL credential leakage prevention

### New Provider: Cloudflare AI Gateway
- Available in onboarding wizard
- Alternative to direct Anthropic API

### Per-Channel Response Prefix
- Different prefixes per channel/account
- Useful for multi-channel setups (different tone for different contexts)

### Implications for Us
- Our cron jobs should use announce delivery (already do for some)
- One-shot auto-delete means cleaner reminder management
- Security fixes already active in our version

---

## 🔍 GitHub Repos to Monitor

| Repo | Warum relevant |
|------|----------------|
| angelor888/claude-code-project | Claude Code Best Practices |
| anthropics/claude-code | Official Claude Code |
| openclaw/openclaw | OpenClaw Core |
| steipete/peekaboo | macOS Automation |
| skillsmp/clawhub | Skills Marketplace |

---

## 📅 Scan Schedule

- **Alle 24h:** Neue Repos/Updates suchen
- **Fokus:** OpenClaw, Claude Code, AI Agents, Automation
- **Keywords:** "claude code", "openclaw", "ai agent workflow", "coding agent"

---

*Dieses File wird automatisch erweitert wenn neue Learnings gefunden werden.*
