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

*Dieses File wird automatisch erweitert wenn neue Learnings gefunden werden.*
