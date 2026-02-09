# Daily Learnings Log

## 2026-02-09 (Mo) — Automated Research Session

### OpenClaw Updates (v2026.2.6)
- **xAI/Grok provider** added — could use as alternative model
- **Voyage AI native memory support** — better embeddings option (our OpenAI embeddings hit quota limits on 02-08!)
- **Token usage dashboard** in Web UI — useful for cost tracking
- **Cron fixes** — scheduling/reminder delivery regressions fixed; good, we rely on cron heavily
- **Sessions history capped** — reduces context overflow, relevant for our sub-agent patterns

**Action item:** Check if Voyage AI embeddings could replace OpenAI (quota issues on 02-08). Update if needed.

### ClawHub
- Site live at clawhub.ai but minimal content scraped. Check back manually later.

### AI Agent Patterns (Feb 2026 Trends)
- **5 core orchestration patterns** (Redis blog): sequential, concurrent, group chat, handoff, Magentic (plan-first)
  - We use sequential + concurrent (sub-agents). Could explore **handoff** pattern for task routing between agents.
- **MCP servers** gaining traction for tool integration (Gumloop, others)
- **Plan-first execution** (Magentic pattern): Agent creates full plan before executing. We do this partially with pre-flight but could formalize.

### Workflow Analysis (Last 24h: 2026-02-08)
**What went well:**
- Vault structure setup, memory consolidation
- Obsidian deliverables organized

**What went badly:**
- Rate limits hit hard (Anthropic 14:00-20:45, Brave quota 1436/2000, OpenAI embeddings exceeded)
- memory_search broken due to embedding quota → need Voyage AI or local alternative
- 0 sends again (applications, outreach all "ready" but unsent)

**Immediate improvements:**
1. Switch embeddings provider if Voyage AI available (memory_search reliability)
2. Brave search quota awareness — 564 remaining, ~22 days left in month = ~25/day budget
3. Rate limit awareness: heavy work before 14:00 CET

### Open Issues
- FLORIAN.md, INDEX.md, Output-Tracker still not created
- Nancy frustrated about Floriana calls — Florian should address today
- BM presentation needs light theme fix + prices removed
