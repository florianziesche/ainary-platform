# Production Guardrails — Domain Knowledge
*Auto-consolidated: 2026-02-18 22:36 | 7 findings | avg conf: 9043% | 0 verified*

## Verified Claims (conf ≥80%)

**RF-067** [9300%]: Production Failure: Free-Form LLM Outputs ohne Validation halluzinieren. Structured Outputs (JSON Schema Validation) sind Pflicht für alle production-critical outputs.
Source: conversation
Tags: failure-mode, production, guardrails, engineering

**RF-064** [9200%]: Production Failure: Fully Autonomous Agents ohne Human-Oversight scheitern. Agents machen Fehler die eskalieren. HITL Checkpoints für alle irreversiblen Actions (delete, send, deploy) sind Pflicht.
Source: conversation
Tags: failure-mode, production, guardrails, engineering

**RF-070** [9200%]: Production Failure: Tool-Use ohne Whitelisting ist Security-Risiko. Prompt Injection kann Agents manipulieren. Least-Privilege Principle: Whitelisting > Blacklisting. Sandbox Environments für Tests. Human-Approval für High-Risk Actions.
Source: conversation
Tags: failure-mode, production, security, guardrails, engineering

**RF-065** [9000%]: Production Failure: Set-and-Forget Agents brauchen kontinuierliches Monitoring. Ohne Logging+Alerting degradieren Agents still. Circuit Breakers und Cost Budgets ($X/day hard limit) sind Pflicht.
Source: conversation
Tags: failure-mode, production, guardrails, engineering

**RF-068** [9000%]: Production Failure: RAG ohne gute Retrieval-Qualität = Garbage-In/Garbage-Out. Chunking (300-500 tokens, 50-100 overlap), Embedding-Qualität und Metadata-Filtering sind kritisch. Schlechte Embeddings → schlechte Chunks → schlechte Antworten.
Source: conversation
Tags: failure-mode, production, memory, rag, engineering

**RF-066** [8800%]: Production Failure: Multi-Agent ohne klare Rollen-Definition = Chaos. Jeder Agent braucht ONE job, well-defined Inputs/Outputs, strukturierte Messages. Debugging ist schwierig (wer hat den Fehler gemacht?).
Source: conversation
Tags: failure-mode, production, multi-agent, engineering

**RF-069** [8800%]: Production Failure: Reflexion/Self-Refine ohne Iteration-Limits geraten in Endlos-Loops. Max 3 Attempts für Reflexion, 2-3 Iterationen für Self-Refine. Zu viele Iterationen können Output verschlechtern (Overfitting).
Source: conversation
Tags: failure-mode, production, self-improvement, engineering

## Emergent Patterns

**engineering × production** (9 findings): Production Failure: Free-Form LLM Outputs ohne Validation ha; Production Failure: Fully Autonomous Agents ohne Human-Overs; Production Failure: Tool-Use ohne Whitelisting ist Security-
