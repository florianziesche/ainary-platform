# Foundational Research — Domain Knowledge
*Auto-consolidated: 2026-02-20 22:02 | 6 findings | avg conf: 92% | 0 verified*

## Verified Claims (conf ≥80%)

**RF-059** [95%]: ReAct (Think→Act→Observe→Repeat) ist das Fundament für Agent-Architekturen. Score 100/100 (Buildability 10 × Relevance 10). 5000+ Zitationen. Alle modernen Frameworks (AutoGPT, LangChain, OpenClaw) nutzen ReAct-Loops. Known Failure: Endlos-Loops ohne Max-Iteration-Limit.
Source: conversation
Tags: paper-ranking, architecture, foundational, sofort-nutzen, engineering

**RF-063** [92%]: Production Agentic Workflows: 4 Core Patterns funktionieren (Reflection, Tool Use/ReAct, Planning, Multi-Agent). Score 100/100. Was funktioniert: HITL Checkpoints, Whitelists, Structured Outputs, Logging, Graceful Degradation. Was NICHT funktioniert: Fully Autonomous, Set-and-Forget, Multi-Agent ohne klare Rollen, Free-Form Outputs.
Source: conversation
Tags: paper-ranking, production, foundational, sofort-nutzen, engineering

**RF-082** [92%]: MaxRL paper: Maximum Likelihood via RL (arXiv 2602.02710)
Source: arxiv 2602.02710
Tags: maxrl, calibration, rlhf, paper

**RF-060** [90%]: MemGPT (Context-Window als Virtual Memory mit Main/Storage/Paging) ist ESSENTIAL für Long-Running Agents. Score 80/100. Agent entscheidet selbst was in/aus Context gepaged wird. Known Failure: Suboptimale Paging-Decisions. Widerspruch zu 1M Context Windows: Paging für >1M nötig, Long Context für ≤1M.
Source: conversation
Tags: paper-ranking, memory, foundational, sofort-nutzen, engineering

**RF-061** [90%]: Reflexion (verbales Reinforcement Learning: Execute→Feedback→Reflect→Retry) ermöglicht Agents aus Fehlern zu lernen OHNE menschliches Feedback. Score 64/100. Episodisches Memory speichert Reflections. Known Failure: Endlose Reflection-Loops ohne Max-Iteration-Limit (3 Attempts empfohlen).
Source: conversation
Tags: paper-ranking, self-improvement, foundational, sofort-nutzen, engineering

**RF-062** [90%]: MCP (Model Context Protocol) ist der offene Standard für Agent-Tool-Integration. Score 90/100. Linux Foundation Agentic AI Foundation. Members: Anthropic, OpenAI, Google, Microsoft, AWS. 10k+ Server, 97M+ SDK Downloads. Windows 11 wird MCP nativ unterstützen. Wie USB für AI Agents.
Source: conversation
Tags: paper-ranking, infrastructure, foundational, sofort-nutzen, vc-ammo

## Emergent Patterns

**production × engineering** (9 findings): Production Agentic Workflows: 4 Core Patterns funktionieren 

**engineering × sofort-nutzen** (9 findings): ReAct (Think→Act→Observe→Repeat) ist das Fundament für Agent; Production Agentic Workflows: 4 Core Patterns funktionieren ; MemGPT (Context-Window als Virtual Memory mit Main/Storage/P
