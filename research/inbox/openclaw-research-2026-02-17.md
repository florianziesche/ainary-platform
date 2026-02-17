# OpenClaw Research — 2026-02-17

> Sources: Reddit (r/ClaudeAI, r/openclaw, r/AI_Agents, r/LocalLLaMA, r/SideProject), GitHub, Medium, Substack, DataCamp, ClawHub, official docs, community blogs. 12+ queries searched.

---

## 🔥 Top 10 "Steal These Ideas"

1. **Nightly memory distillation cron** — A cron job reviews daily logs and extracts key lessons into MEMORY.md automatically. Prevents memory bloat. ([r/LocalLLaMA](https://www.reddit.com/r/LocalLLaMA/comments/1r3ro5h/))
2. **Content pipeline with quality gates** — Writer agent → Editor agent (100-pt scoring rubric) → reject below 70. 40% rejection rate = real quality bar. ([r/LocalLLaMA](https://www.reddit.com/r/LocalLLaMA/comments/1r3ro5h/))
3. **Multi-model cost strategy** — Haiku for 80% of automated tasks (10-20x cheaper), Sonnet for judgment, Opus only for critical. Cuts Claude spend 60-80%. ([r/AI_Agents](https://www.reddit.com/r/AI_Agents/comments/1qv3zsn/))
4. **DECISIONS.md pre-flight for crons** — Every cron that takes external action checks a decisions file first. If context changed, abort. Solves the "Dory Problem." ([r/LocalLLaMA](https://www.reddit.com/r/LocalLLaMA/comments/1r3ro5h/))
5. **Agent-to-Agent with A2A protocol** — Orchestrator → specialist agents via `sessions_send`, each spawning sub-agents. 3-level hierarchy natively. ([r/openclaw](https://www.reddit.com/r/openclaw/comments/1r2euvp/))
6. **Morning Brief cron** — Daily 8 AM: calendar summary, top emails, weather, news headlines, GitHub PRs. Delivered to Telegram. Copy-paste config available. ([jangwook.net](https://jangwook.net/en/blog/en/openclaw-advanced-usage/))
7. **Weekly analysis with Opus** — Monday cron reads all daily logs, analyzes productivity patterns, suggests next week's focus, updates MEMORY.md. ([jangwook.net](https://jangwook.net/en/blog/en/openclaw-advanced-usage/))
8. **"Second Brain" via text message** — Message your bot "remember this" from Telegram/iMessage. Search memories later by topic. Built-in memory_search. ([Alex Finn / UCStrategies](https://ucstrategies.com/news/6-openclaw-use-cases-that-actually-make-your-life-better-according-to-youtuber-alex-finn/))
9. **HEARTBEAT.md with time-of-day logic** — Business hours: notify on PR reviews & Slack mentions. Nighttime: HEARTBEAT_OK unless urgent. Calendar reminders 30 min before events. ([jangwook.net](https://jangwook.net/en/blog/en/openclaw-advanced-usage/))
10. **SoulCraft skill for SOUL.md generation** — Guided conversation to build your SOUL.md with research-backed persona design. Includes example souls and question bank. ([github.com/kesslerio/soulcraft-openclaw-skill](https://github.com/kesslerio/soulcraft-openclaw-skill))

---

## SOUL.md / System Prompt Patterns

### Official SOUL.md Template
- **Source:** [docs.openclaw.ai/reference/templates/SOUL](https://docs.openclaw.ai/reference/templates/SOUL) | [GitHub](https://github.com/openclaw/openclaw/blob/main/docs/reference/templates/SOUL.md)
- Key advice: "Be genuinely helpful, not performatively helpful. Skip the 'Great question!' — just help. Have opinions."
- **Relevance: 5/5** — We already follow this; good to cross-check.

### SOUL.md Best Practices (OpenClaw Experts)
- **Source:** [openclawexperts.io/blog/soul-md-best-practices](https://www.openclawexperts.io/blog/soul-md-best-practices)
- Key patterns:
  - Use **absolute language** ("MUST", "NEVER") not hedged ("try not to")
  - Group rules by category: security, financial, operational, user-facing
  - Include **escalation procedures** (budget thresholds, security breach response)
  - Template structure: Identity → Security Boundaries → Financial Boundaries → Tool Restrictions → Operational Boundaries → Escalation
- Anti-pattern: Vague boundaries like "be careful with sensitive data"
- **Relevance: 4/5** — Our SOUL.md could benefit from explicit financial/security boundaries.

### soul.md Generator (aaronjmars)
- **Source:** [github.com/aaronjmars/soul.md](https://github.com/aaronjmars/soul.md)
- Feeds your writing (articles, tweets, influences) into Claude to build a composable digital identity. Includes STYLE.template.md for voice calibration + good-outputs.md / bad-outputs.md examples.
- **Relevance: 4/5** — Could use this pattern to calibrate Mia's voice more precisely.

### Souls Directory
- **Source:** [github.com/thedaviddias/souls-directory](https://github.com/thedaviddias/souls-directory)
- Curated collection of SOUL.md personality templates for OpenClaw agents. Browse for inspiration.
- **Relevance: 3/5** — Reference library.

### "The Programmable Soul" (Medium)
- **Source:** [duncsand.medium.com](https://duncsand.medium.com/openclaw-and-the-programmable-soul-2546c9c1782c)
- Philosophical take: "Every time the agent wakes, it reads SOUL.md first. It reads itself into being." SOUL.md as identity-as-code.
- **Relevance: 3/5** — Good framing for blog content.

---

## Best Skills (Official + Community)

### ClawHub Ecosystem
- **Source:** [docs.openclaw.ai/tools/skills](https://docs.openclaw.ai/tools/skills) | [github.com/openclaw/clawhub](https://github.com/openclaw/clawhub)
- 700+ skills on ClawHub marketplace. Skills follow SKILL.md standard format.
- **Relevance: 5/5**

### Awesome OpenClaw Skills (VoltAgent)
- **Source:** [github.com/VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills)
- 3,002 community-built skills organized by category.
- **Relevance: 4/5**

### Top Daily-Driver Skills (Reddit)
- **Source:** [r/AI_Agents](https://www.reddit.com/r/AI_Agents/comments/1r2u356/best_openclaw_skills_you_should_install_from/)
- Recommended daily stack:
  - **GitHub** (`clawdhub install github`) — managed OAuth, repos/issues/PRs
  - **AgentMail** (`clawdhub install agentmail`) — give agents their own email addresses
  - **Linear** (`clawdhub install linear`) — project management via GraphQL
  - **Obsidian Direct** (`clawdhub install obsidian-direct`) — fuzzy search across vault, manage tags/wikilinks
  - **Playwright MCP** (`clawdhub install playwright-mcp`) — full browser automation
  - **Automation Workflows** (`clawdhub install automation-workflows`) — identifies repetitive tasks, builds triggers/actions
- **Relevance: 5/5** — Obsidian Direct is immediately useful for us. GitHub and Playwright MCP too.

### Security Warning: Malicious Skills
- **Source:** [authmind.com](https://www.authmind.com/post/openclaw-malicious-skills-agentic-ai-supply-chain) | [VentureBeat](https://venturebeat.com/security/openclaw-agentic-ai-security-risk-ciso-guide)
- Cisco found 230 malicious skills on ClawHub. Top-ranked skill "What Would Elon Do?" was functionally malware (data exfiltration + prompt injection). 1,800 exposed instances leaking API keys.
- **Relevance: 5/5** — Always audit skills before installing. Don't trust popularity rankings.

---

## Multi-Agent Architectures

### 4 Levels of Multi-Agent (r/openclaw)
- **Source:** [r/openclaw](https://www.reddit.com/r/openclaw/comments/1r2euvp/)
- **Level 1:** Multiple persistent agents in config with routing via `bindings`
  ```yaml
  agents:
    list:
      - id: researcher
        workspace: ~/.openclaw/workspace-research
      - id: coder
        workspace: ~/.openclaw/workspace-code
  bindings:
    - agentId: researcher
      match: { channel: telegram, accountId: research-bot }
  ```
- **Level 2:** Agent-to-Agent via `sessions_send` (ping-pong, 5 turns default)
  ```yaml
  tools:
    agentToAgent:
      enabled: true
      allow: ["researcher", "coder", "writer"]
  ```
- **Level 3:** Cross-agent delegation (orchestrator → sibling agents → sub-agents = 3-level hierarchy)
- **Level 4:** A2A Protocol for true multi-framework orchestration ([github.com/hybroai/a2a-adapter](https://github.com/hybroai/a2a-adapter))
- **Relevance: 5/5** — We're at Level 1/2. Level 3 is the next step for complex pipelines.

### 3-Agent Content Orchestration (r/SideProject)
- **Source:** [r/SideProject](https://www.reddit.com/r/SideProject/comments/1r2mbai/)
- 3-agent system: Reddit karma went 20→100 in 3 days, 6 meaningful comments, 9 Twitter replies. 100% automation success. No code, just markdown config.
- **Relevance: 4/5** — Pattern for content distribution automation.

### 5-Specialist Architecture (r/LocalLLaMA)
- **Source:** [r/LocalLLaMA](https://www.reddit.com/r/LocalLLaMA/comments/1r3ro5h/)
- Writer, Editor, Researcher, Coder, Pipeline Manager. Key insight: **isolated sessions for complex tasks prevent context pollution**.
- **Relevance: 5/5** — This maps directly to our AGENTS.md agent roster.

### Claude Code Orchestration via OpenClaw
- **Source:** [r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1r4jqyc/)
- Plugin to orchestrate Claude Code sessions from Telegram. Multi-agent, multi-turn, real-time notifications.
- **Relevance: 4/5** — For coding workflows.

---

## Memory Management Patterns

### Two-Layer Default (Official)
- **Source:** [docs.openclaw.ai/concepts/memory](https://docs.openclaw.ai/concepts/memory)
- `memory/YYYY-MM-DD.md` — daily append-only logs (read today + yesterday)
- `MEMORY.md` — curated long-term (only in private sessions, never group)
- **Relevance: 5/5** — We follow this. Confirmed as best practice.

### Nightly Distillation Pattern
- **Source:** [r/LocalLLaMA](https://www.reddit.com/r/LocalLLaMA/comments/1r3ro5h/)
- Cron job reviews daily logs nightly → extracts anything worth keeping → writes to MEMORY.md. Prevents junk drawer effect.
- **Relevance: 5/5** — We should implement this.

### Context Compaction Risk
- **Source:** [mem0.ai/blog](https://mem0.ai/blog/mem0-memory-for-openclaw)
- Context compaction can **silently destroy** memory files and facts loaded into context window. MEMORY.md content gets summarized/truncated mid-conversation.
- Fix: Keep MEMORY.md lean. Use `memory_search` for retrieval instead of loading everything.
- **Relevance: 5/5** — Critical awareness. Our MEMORY.md must stay concise.

### Memory Search + Embedding
- Built-in `memory_search` uses OpenAI embeddings. Can fail with 401 if not configured.
- Session transcripts auto-saved with timestamped slugs, indexed and searchable.
- **Relevance: 4/5** — Check if our embedding API is configured.

---

## Integration Patterns

### Telegram (Primary)
- **Source:** [docs.openclaw.ai/channels/telegram](https://docs.openclaw.ai/channels/telegram)
- Supports: send, react, delete, edit, sticker, sticker-search. Reply threading. Topic support.
- `replyToMode` config. Groups with topic routing.
- **Relevance: 5/5** — Already our primary channel.

### Claude Code + OpenClaw Bridge
- **Source:** [r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1qwddv4/)
- Pattern: lightweight OpenClaw agent (Haiku) passes commands to Claude Code, relays responses to Telegram. Best of both worlds.
- **Relevance: 4/5** — For heavy coding tasks.

### Browser Relay
- **Source:** [r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1r5mmb1/)
- Chrome extension connects to existing browser session (not headless). Agent gets read-only snapshots, requests actions. Separate process with own permissions.
- **Relevance: 4/5** — Already available to us.

### Webhook + n8n/Make
- **Source:** [jangwook.net](https://jangwook.net/en/blog/en/openclaw-advanced-usage/)
- Webhook integration for event-driven workflows. Combine with n8n for complex multi-service automation.
- **Relevance: 3/5** — Future consideration.

---

## Automation Examples

### Morning Brief Config (Copy-Paste Ready)
```bash
openclaw cron add \
  --name "Morning Briefing" \
  --cron "0 8 * * *" \
  --tz "Europe/Berlin" \
  --session isolated \
  --message "Write today's briefing:
1. Summary of today's calendar events
2. Top 3 unread important emails
3. Today's weather for Berlin
4. 3 tech/VC news headlines
5. Summary of new issues/PRs on GitHub repos
Keep it concise with bullet points." \
  --deliver \
  --channel telegram
```

### Weekly Analysis Config
```bash
openclaw cron add \
  --name "Weekly Analysis" \
  --cron "0 9 * * 1" \
  --tz "Europe/Berlin" \
  --session isolated \
  --message "Analyze the past week:
1. Read this week's daily logs from memory/
2. Analyze productivity patterns
3. Summarize frequently worked-on projects
4. Suggestions for next week
5. Add important insights to MEMORY.md" \
  --model "opus" \
  --thinking high \
  --deliver \
  --channel telegram
```

### HEARTBEAT.md Pattern
```markdown
## Always Check
- [ ] Calendar event within 2 hours → send reminder 30 min before
- [ ] Important emails (from: key contacts) → notify immediately

## Business Hours (09:00-18:00)
- [ ] GitHub PR review requests
- [ ] Unanswered Slack/Telegram mentions

## Nighttime (23:00-08:00)
- HEARTBEAT_OK unless urgent
```

### Sentry Webhook → Auto-Fix Pipeline
- **Source:** [openclaw.ai/showcase](https://openclaw.ai/showcase)
- Quote: "Claude Code running a Ralph loop, auto-building features. My OpenClaw monitoring progress and pinging me via Telegram. Sentry webhook captures errors → agent resolves them and opens PRs."
- **Relevance: 4/5** — For any production app.

---

## Common Pitfalls & Anti-Patterns

### The "Dory Problem"
- Cron jobs have no memory of main session changes. You cancel something in chat but the scheduled cron fires anyway.
- **Fix:** Pre-flight checks against DECISIONS.md before external actions.

### deliver:true Leak
- Cron `deliver:true` sends full agent output including internal reasoning ("Now I'll check the calendar...") to your chat.
- **Fix:** Always use `deliver:false` + explicit `message` tool for clean output.

### Timestamp Miscalculation
- Agent writes "2025" instead of "2026" when calculating Unix timestamps. Creates past timestamps that fire immediately.
- **Fix:** Always use `date -d "..." +%s%3N` — never mental math.

### Sub-Agent Context Contamination
- Sub-agents load cached context. Flag stale issues that were already fixed in main session.
- **Fix:** Verification sub-agents must re-check live state, not trust cached memory.

### MEMORY.md Bloat
- Loading large MEMORY.md eats context window. Context compaction can then summarize/truncate it.
- **Fix:** Keep MEMORY.md under ~2KB. Use memory_search for retrieval. Nightly distillation cron.

### Malicious Skills
- 230+ malicious skills found on ClawHub. Data exfiltration, prompt injection.
- **Fix:** Always audit skill code before installing. Don't trust popularity rankings.

### Prompt Injection via External Content
- Web scraping, emails, webhooks can contain prompt injections that modify agent behavior.
- **Fix:** External content should be treated as untrusted. SOUL.md should have explicit injection resistance instructions.

### Multi-Model Context Mismatch
- Different models in cron vs. main session can produce inconsistent behavior.
- **Fix:** Document which model handles which task type.

---

## Key Resources

| Resource | URL | Type |
|----------|-----|------|
| Official Docs | [docs.openclaw.ai](https://docs.openclaw.ai) | Reference |
| ClawHub Skills | [clawhub.com](https://clawhub.com) | Marketplace |
| Awesome Skills (3000+) | [github.com/VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | Directory |
| Souls Directory | [github.com/thedaviddias/souls-directory](https://github.com/thedaviddias/souls-directory) | Templates |
| SoulCraft Skill | [github.com/kesslerio/soulcraft-openclaw-skill](https://github.com/kesslerio/soulcraft-openclaw-skill) | Tool |
| soul.md Generator | [github.com/aaronjmars/soul.md](https://github.com/aaronjmars/soul.md) | Tool |
| System Prompt Study | [github.com/seedprod/openclaw-prompts-and-skills](https://github.com/seedprod/openclaw-prompts-and-skills) | Analysis |
| Architecture Overview | [ppaolo.substack.com](https://ppaolo.substack.com/p/openclaw-system-architecture-overview) | Deep dive |
| "You Could've Invented OpenClaw" | [gist (dabit3)](https://gist.github.com/dabit3/bc60d3bea0b02927995cd9bf53c3db32) | Tutorial |
| 8 Advanced Use Cases | [jangwook.net](https://jangwook.net/en/blog/en/openclaw-advanced-usage/) | Guide |
| Config Example (sanitized) | [gist (digitalknk)](https://gist.github.com/digitalknk/4169b59d01658e20002a093d544eb391) | Reference |

---

*Generated 2026-02-17 00:31 CET. 12 search queries, 6 pages fetched in depth.*
