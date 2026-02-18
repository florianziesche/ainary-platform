# Resolved Contradictions — Domain Knowledge
*Auto-consolidated: 2026-02-18 22:36 | 3 findings | avg conf: 8567% | 0 verified*

## Verified Claims (conf ≥80%)

**RF-074** [9000%]: CONTRADICTION AUFGELÖST: Fully Autonomous Agents vs. Human-in-the-Loop. Production zeigt: HITL für irreversible Actions (delete, send, deploy), Autonomous für reversible/low-risk (research, draft, analyze). Nicht binär. Unser Guardrails-System (AUTO ≥60 / REVIEW ≥30 / CONFIRM <30) ist die korrekte Implementierung dieses Spektrums.
Source: conversation
Tags: contradiction, autonomy, hitl, guardrails, production, engineering

**RF-072** [8500%]: CONTRADICTION AUFGELÖST: MemGPT Paging vs. 1M Context Windows. Beide valid: Paging für >1M Token (unbegrenzte Konversationen, Langzeit-Memory), Long Context für ≤1M (einzelne Sessions). Use-case dependent, nicht entweder-oder. Implikation: Wir brauchen BEIDES — Long Context für Sessions, Paging für Cross-Session Memory.
Source: conversation
Tags: contradiction, memory, memgpt, architecture, engineering

**RF-073** [8200%]: CONTRADICTION AUFGELÖST: Toolformer (LLMs lernen Tools selbst) vs. MCP (Standard für Tool-Integration). NICHT widersprüchlich: Toolformer = Discovery (welche Tools sind nützlich?), MCP = Integration (wie spreche ich mit dem Tool?). Complementary. Praktisch: MCP zuerst (Standard), Toolformer-Style Discovery später als Optimierung.
Source: conversation
Tags: contradiction, mcp, toolformer, architecture, engineering

## Emergent Patterns

**engineering × production** (9 findings): CONTRADICTION AUFGELÖST: Fully Autonomous Agents vs. Human-i
