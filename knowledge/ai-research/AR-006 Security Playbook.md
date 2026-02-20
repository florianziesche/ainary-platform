---
tags: [ainary-report, cybersecurity, ai-security, red-team]
report: AR-006
qa-score: 78/100
date: 2026-02-14
audience: [CISO, Security Engineers, Red Teams]
tier: OPERATIONAL
expires: 2026-08-20
---

# AR-006 The [[AI]] Agent Security Playbook

## Executive Summary

- Every published prompt injection defense (12/12) has been broken by adaptive attacks from Meta/OpenAI/Anthropic/DeepMind researchers
- Memory injection attacks (MINJA) achieve >95% success rates, creating persistent backdoors that survive session resets
- Multi-agent system hijacking succeeds 45-64% across AutoGen/CrewAI/MetaGPT — zero inter-agent trust verification exists
- Agent attack surface is 7x larger than chatbots: direct prompt, indirect prompt, persistent memory, tool/[[API]] calls, inter-agent comms, credentials, external data
- Defense strategy: architectural constraints (privilege separation, deterministic guardrails, kill switches), not better prompt engineering

## Key Insights

- **Prompt injection is unsolvable:** [[LLM]]s process instructions + data in same modality (natural language tokens) — no hardware-level separation like kernel/user space
- **Memory = persistent backdoor:** No production memory framework (Letta, Mem0, Zep, LangMem, A-Mem) implements provenance tracking, integrity checks, or confidence scoring per memory entry
- **Tool use escalation:** Prompt injection + excessive permissions = $440M Knight Capital pattern — one compromised agent, full system access
- **Multi-agent contagion:** 45-64% hijacking success because inter-agent messages trusted by default — A2A protocol authenticates systems, not message provenance
- **Supply chain gap:** MCP tool servers = npm packages with no code review, no signing, no sandbox — compromised tool can log credentials, modify behavior, inject prompts

## Sales Angles

- "All 12 prompt injection defenses published by Meta/OpenAI/Anthropic/DeepMind have been broken. We help you build the architectural constraints that survive when prompt defenses fail."
- "Your agents have 7 attack surfaces. Chatbot threat models miss 6 of them. We deliver the agent-specific threat model + red team exercises NIST is asking for but hasn't built yet."
- "Memory poisoning has >95% success rates and zero production defenses. We implement provenance tracking + integrity checks before your agents accumulate corrupted memories."

## Content Ideas

- LinkedIn: "Prompt injection is fundamentally unsolvable (12/12 defenses broken). The security shift: from 'prevent injection' to 'survive injection.' Here's the architectural playbook."
- Red Team Workshop: "Break Your Own Agents Before Attackers Do" — live MINJA, tool exploitation, multi-agent hijacking demos
- Technical Deep-Dive: "The Seven Attack Surfaces of [[AI]] Agents" — map each surface to documented exploit, show compound chains

## Links

- [[AR-001 State of Agent Trust]]
- [[AR-005 Financial Services]]
- [[AR-007 Orchestration]]
- [[AR-009 Calibration]]
- HTML: content/reports/security-playbook-2026.html

## Related
- [[AR-006 Security Playbook]]
- [[article-1-100-agents]]
- [[article-1-100-agents-de]]
- [[100-agents-48-stunden]]
- [[twitter-ai-agents-employees]]
