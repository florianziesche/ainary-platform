# Daily Learnings — Capability Evolver

## 2026-03-04 — OpenClaw v2026.3.2 + Showcase Patterns

### OpenClaw Platform Updates (v2026.3.2, Released March 3)
**Relevant Features:**
- ✅ **First-class PDF tool** — Native Anthropic/Google support, extraction fallback for other models. Config: `agents.defaults.pdfModel`, `pdfMaxBytesMb`, `pdfMaxPages`
- ✅ **sessions_spawn attachments** — Inline file attachments (base64/utf8) for sub-agents. Config: `tools.sessions_spawn.attachments`
- ✅ **Ollama embeddings** — `memorySearch.provider = "ollama"` for local memory embeddings
- ✅ **Telegram streaming** — Defaults to "partial" (live preview) for new setups
- ⚠️ **BREAKING:** tools.profile defaults to "messaging" (not broad coding tools) for new installs
- ⚠️ **BREAKING:** ACP dispatch defaults to enabled

**Not Immediately Relevant:**
- MiniMax-M2.5-highspeed provider
- Zalo Personal plugin rebuild
- Android node capabilities (camera.list, device.permissions, notifications)
- Feishu/Discord/Slack enhancements

### ClawHub Ecosystem
- **2,857+ skills** available (growing)
- No new Florian-specific skills identified (already has 45+ skills installed)

### AI Agent Workflow Patterns 2026
**Emerging Standards:**
1. **ReAct, Reflection, Tool Use, Planning, Multi-Agent Collaboration** — Core design patterns
2. **Full workflow automation** — Move from single-step to end-to-end process ownership
3. **LangGraph stable** — Production-ready multi-agent orchestration
4. **80% workplace embedding** — Prediction for agent penetration

**Showcase Use Case Patterns (50+ examples analyzed):**
1. **Multi-agent orchestration** — 4-5 specialized agents (dev, marketing, business, research) with shared memory + individual contexts
2. **Daily cron workflows** — Email summaries, health tracking, morning briefings, research spawning
3. **Voice-first execution** — Phone → Telegram → actions on VPS/desktop
4. **Coding agent orchestration** — OpenClaw drives Claude Code/Codex, monitors progress, spawns PRs
5. **Overnight experiments** — Cron picks tasks, spawns sub-agents, delivers results in morning
6. **Log → Decision pipeline** — Capture ideas as tasks → overnight research → decision records (ADR-style)
7. **Daily roll call** — 10+ agents report status, coordinate work

### Confidence Analysis — Yesterday's Execution (2026-03-03)
**Strengths:**
- Shipped 7 major features (BLUF, Momentum, Watchlist, Graph filters, Apple emoji removal, Palantir Intelligence Layer)
- Systematic debugging (Graph filter bug: 5 iterations, root cause identified, CSS solution)
- Self-audit discipline (Research Protocol compliance check, confidence ratings)
- Friedberg Production Lock maintained (0 violations)

**Weaknesses:**
- Sentiment bulk-default (85% NEUTRAL = no signal)
- Theme assignment via keyword fallback (55% generic "Kandidaten & Wahlkampf")
- 168 URLs unverified (HTTP 200 status not checked)
- Nürnberg graph density 0.12 vs Friedberg 0.31 (quality gap)

**Confidence Ratings:**
- Friedberg: 85% (manual audit, Stamp-feedback loop, full ACH hypotheses)
- Fürth: 72% (structural parity, sentiment audit done, 4 orphan candidates)
- Nürnberg: 70% (bulk import, sentiment audit done, partial ACH hypotheses)

### Actionable Improvements for Florian's Workflow
1. **PDF tool integration** — Use native PDF analysis for CV/report work (replaces extract-fallback)
2. **Daily cron patterns** — Expand morning briefing: VC news, research summaries, deal flow updates
3. **Multi-agent formalization** — HUNTER/WRITER/RESEARCHER already exist, could add explicit orchestration layer
4. **Overnight experiments** — Spawn research sub-agents for VC thesis work (market analysis, competitor research)
5. **Log → Decision pipeline** — Formalize idea capture → decision records (fits Memory-R1 system)
6. **sessions_spawn attachments** — Pass research docs/PDFs to sub-agents directly

### No Evolver Code Changes Needed
- 0 recurring bugs identified
- System patterns stable
- Yesterday's execution within normal variance
- Graph filter bug = edge case (D3 v7 stale selections), solved with CSS workaround

---
*Next scan: 2026-03-05 05:00 CET*
