# Mutation: Multi-Agent Orchestration Pattern

**Date:** 2026-02-10
**Source:** Community Showcase (adam91holt's Dream Team)
**Type:** Architecture Pattern
**Status:** Documented for Future Use

## Pattern Discovery
**Kev's Dream Team:** 14+ agents under one gateway
- **Orchestrator:** Opus 4.5 (high-cost, high-reasoning)
- **Workers:** Codex (specialized, cost-efficient)
- **Flow:** Opus delegates tasks → Codex executes → Opus synthesizes

## Why It Works
1. **Cost optimization:** Opus only for routing/synthesis, Codex for execution
2. **Specialization:** Each Codex agent has domain expertise
3. **Quality control:** Opus validates outputs before delivery
4. **Scalability:** Add new specialists without changing orchestrator

## Current vs. Pattern
**Our current approach:**
- Mia (main) spawns sub-agents ad-hoc
- Sub-agents use same model (Sonnet)
- No formal delegation framework
- Sub-agents report back, Mia relays

**Dream Team approach:**
- Formal roster of specialists
- Orchestrator never executes, only delegates
- Each specialist has explicit domain + tools
- Orchestrator validates + synthesizes
- Clear escalation paths

## Potential Application
Could implement for Florian:
1. **Mia (Orchestrator):** Opus 4.5 — routing + synthesis
2. **HUNTER (VC Job Search):** Codex — research, applications, prep
3. **WRITER (Content):** Codex — blog posts, LinkedIn, repurposing
4. **RESEARCHER (Deep Dive):** Codex — market research, competitive analysis
5. **OPERATOR (Systems):** Codex — Notion, automation, workflows
6. **DEALMAKER (Freelance):** Codex — proposals, client outreach, follow-ups

## Benefits
- **Cost:** Opus only for ~10% of interactions (delegation decisions)
- **Quality:** Specialist agents with domain-specific prompts
- **Speed:** Parallel execution across specialists
- **Clarity:** Clear responsibility boundaries

## Implementation Considerations
1. Requires gateway configuration for multiple agents
2. Needs routing logic (which specialist for which task?)
3. Sub-agent prompts must be highly specialized
4. Orchestrator prompt: "never execute, always delegate"
5. Communication protocol between orchestrator ↔ specialists

## Next Steps
1. Document current sub-agent usage patterns
2. Identify most common delegation categories
3. Design specialist agent prompts
4. Test orchestrator-only mode (Opus delegates everything)
5. Measure cost savings vs current approach

## Resources
- [Dream Team Blog Post](https://adams-ai-journey.ghost.io/2026-the-year-of-the-orchestrator/)
- [Clawdspace](https://github.com/adam91holt/clawdspace) — agent sandboxing
- [GitHub Articles](https://github.com/adam91holt/orchestrated-ai-articles)

## Related
- AGENTS.md (current specialist definitions)
- Sub-agent spawn patterns in memory/
- Cost analysis in session_status
