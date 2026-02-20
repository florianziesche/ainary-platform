---
type: knowledge
last_verified: 2026-02-15
status: evergreen
created: 2026-02-01
tier: KNOWLEDGE
expires: 2027-02-19
---

Crea# [[AI]] Fundamentals

*Mental models for explaining [[AI]] to investors, clients, and in content.*

---

## The [[AI]] Hierarchy

```
AI (broadest)
└── Machine Learning (learns from data)
    └── Deep Learning (many-layer neural networks)
        └── Generative AI (generates content)
            └── Agentic AI (autonomous reasoning + action loops)
```

Each is a subset of the prior.

---

## What Makes an Agent

An agent has three core properties:

1. **Can reason about goals** — understands what it's trying to achieve
2. **Takes actions** — uses tools, calls APIs, browses web
3. **Iterates based on feedback** — observe → think → act → observe

**The key distinction is the loop.** A chatbot answers once. An agent keeps working until the goal is achieved.

---

## Agent Architecture Patterns

### ReAct (Reasoning + Acting)
Agents interleave thinking with tool use:
1. Thought: "I need to find the company's revenue"
2. Action: Search web for "[company] revenue 2025"
3. Observation: Found $50M ARR
4. Thought: "Now I need to find their funding history"
5. Action: Search Crunchbase...

### Multi-Agent Systems
Specialized agents for different tasks:
- **Orchestrator** — routes tasks to appropriate agent
- **Researcher** — gathers information
- **Writer** — creates content
- **Validator** — checks accuracy

Your systems (Legal [[AI]], OpenClaw/King) are fundamentally agentic.

---

## RAG (Retrieval-Augmented Generation)

Combines retrieval + generation:

1. **Query** → User asks a question
2. **Retrieve** → Find relevant documents/chunks
3. **Augment** → Add retrieved context to prompt
4. **Generate** → [[LLM]] answers using the context

### Best Practices for Low Hallucination
- Hybrid retrieval (BM25 sparse + dense semantic)
- Cross-encoder re-ranking
- Self-correction loops
- Multi-agent verification
- Full citation tracking

Your Legal [[AI]] achieves <0.2% hallucination using these techniques.

---

## Hot Topics (Jan 2026)

- Reasoning models (o1/o3)
- [[AI]] agents
- Small Language Models (SLMs)
- Multimodal [[AI]]
- Legal [[AI]]
- [[AI]] coding tools
- Defense tech
- Climate tech 2.0
- Humanoid robotics
- [[AI]] pricing models
- Open vs closed model economics

*Review quarterly — fast-moving space.*

---

*Source: [[Claude]] conversation extracts 2026-02-01*

## Connections
AI-Grundlagen. Aufbauend: [[RAG]], [[AI-State-of-Art]]. Relevant für [[CNC-Fertigungsplaner]] AI-Komponente.
