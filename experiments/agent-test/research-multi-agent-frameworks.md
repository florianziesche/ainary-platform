# Research Brief: Multi-Agent Frameworks — State of the Art 2025/2026

**Tag: [INTERN]**
**Erstellt:** 2026-02-14
**Agent:** RESEARCHER (Sub-Agent)

---

## Key Findings

1. **Drei Frameworks dominieren:** LangGraph, CrewAI und AutoGen haben sich als die "Big 3" etabliert, jeweils mit ~30k+ GitHub Stars. — Quellen: [Langfuse Blog](https://langfuse.com/blog/2025-03-19-ai-agent-comparison), [Python in Plain English](https://python.plainenglish.io/autogen-vs-crewai-vs-langgraph-2026-comparison-guide-fd8490397977)

2. **Google A2A ist der neue Interoperabilitätsstandard:** Im April 2025 vorgestellt, im Juni 2025 an die Linux Foundation übergeben. Ermöglicht framework-agnostische Agent-zu-Agent-Kommunikation über "Agent Cards" (JSON). — Quelle: [Google Developers Blog](https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/), [Linux Foundation](https://www.linuxfoundation.org/press/linux-foundation-launches-the-agent2agent-protocol-project-to-enable-secure-intelligent-communication-between-ai-agents)

3. **Trust und Safety sind die größten ungelösten Probleme:** Kein Framework hat robustes Trust Scoring zwischen Agents. Akademische Forschung identifiziert inter-agent trust als "important open problem". — Quelle: [arxiv.org/abs/2502.14143](https://arxiv.org/abs/2502.14143), [arxiv.org/abs/2505.02077](https://arxiv.org/abs/2505.02077)

4. **Markt explodiert:** Gartner prognostiziert, dass 40% aller Enterprise-Anwendungen bis Ende 2026 AI Agents einbetten (vs. <5% in 2025). Marktvolumen: $7,8 Mrd. → $52 Mrd. bis 2030. — Quelle: [Machine Learning Mastery](https://machinelearningmastery.com/7-agentic-ai-trends-to-watch-in-2026/)

5. **MCP ≠ A2A:** Anthropics MCP (Nov 2024) ist Agent-to-Tool, Googles A2A (April 2025) ist Agent-to-Agent. Komplementär, nicht konkurrierend. — Quelle: [Semgrep](https://semgrep.dev/blog/2025/a-security-engineers-guide-to-the-a2a-protocol/)

---

## Framework-Übersicht

### Open Source — Die Big 3

| Framework | Stars | Downloads/Monat | Orchestrierung | Stärke | Schwäche |
|-----------|-------|-----------------|----------------|--------|----------|
| **LangGraph** (LangChain) | Teil von LangChain-Ökosystem (70M+ Downloads/Monat) | ~70M (Ökosystem) | Graph-basiert (DAG) | Maximale Kontrolle, Debugging, Production-ready | Steile Lernkurve, viele Imports |
| **CrewAI** | ~30k | ~1M | Role-based, hierarchisch | Einfachster Einstieg, YAML-config, schnell | Weniger Customization bei Scale |
| **AutoGen** (Microsoft) | ~30k | k.A. | Konversations-basiert, async | Forschung, kollaboratives Reasoning | Nicht production-ready für Enterprise |

*Quellen: GitHub Stars und Downloads aus [Python in Plain English (Feb 2026)](https://python.plainenglish.io/autogen-vs-crewai-vs-langgraph-2026-comparison-guide-fd8490397977), LangChain Download-Zahlen aus gleichem Artikel.*

### Weitere relevante Frameworks

| Framework | Ansatz | Notiz |
|-----------|--------|-------|
| **OpenAI Agents SDK** | Leichtgewichtig, OpenAI-native | Noch jung, vendor-locked |
| **Smolagents** (HuggingFace) | Code-zentrisch, minimal | Gut für schnelle Prototypen |
| **Semantic Kernel** (Microsoft) | Enterprise, C#/Python/Java | Merged mit AutoGen → GA Q1 2026 |
| **Google ADK** | Google Cloud-native | Starke Governance |
| **MetaGPT** | Software-Engineering-Rollen | Nischig aber clever |
| **Pydantic AI** | Type-safe, Python-native | Entwickler-freundlich |
| **Agno** | Lightweight wrapper | Einfach, aber Skalierungs-Fragen |

*Quelle: [Langfuse Comparison](https://langfuse.com/blog/2025-03-19-ai-agent-comparison), [Multimodal.dev](https://www.multimodal.dev/post/best-multi-agent-ai-frameworks)*

---

## Orchestrierung-Patterns

### Evidence (aus Quellen belegt)

| Pattern | Beschreibung | Framework-Beispiel |
|---------|-------------|-------------------|
| **Sequential** | Agents arbeiten nacheinander, Output → Input | CrewAI (default), LangGraph |
| **Parallel** | Unabhängige Tasks gleichzeitig | LangGraph (branching), CrewAI |
| **Hierarchical** | Manager-Agent delegiert an Worker | CrewAI (built-in), LangGraph |
| **Graph/DAG** | Beliebige Topologie mit Zyklen & Bedingungen | LangGraph (Kernkonzept) |
| **Conversational** | Agents "debattieren" via Message Passing | AutoGen (Kernkonzept) |

*Quellen: [DEV.to Orchestration Guide](https://dev.to/pockit_tools/langgraph-vs-crewai-vs-autogen-the-complete-multi-agent-ai-orchestration-guide-for-2026-2d63), [ClickIT Multi-Agent Architecture](https://www.clickittech.com/ai/multi-agent-system-architecture/)*

---

## Agent-zu-Agent Kommunikation

### Protokoll-Landschaft

| Protokoll | Wer | Was | Status |
|-----------|-----|-----|--------|
| **A2A** (Agent2Agent) | Google → Linux Foundation | Agent-to-Agent, framework-agnostisch | Open Standard, aktive Entwicklung |
| **MCP** (Model Context Protocol) | Anthropic | Agent-to-Tool | Weit verbreitet |
| **Framework-intern** | Jedes Framework | Eigene Message-Passing-Mechanismen | Fragmentiert |

**Wie A2A funktioniert:** Client Agent sendet Task an Remote Agent. Remote Agent publiziert Capabilities via "Agent Card" (JSON). Kommunikation über HTTP/JSON. — Quelle: [A2A Protocol Docs](https://a2a-protocol.org/latest/)

### Interpretation

Die meisten Frameworks verwenden **proprietäre interne Kommunikation** (shared state, message queues, function calls). A2A adressiert die *Inter-System*-Kommunikation (verschiedene Frameworks/Vendors), nicht die *Intra-System*-Koordination innerhalb eines Frameworks. Adoption ist noch früh — ein [kritischer Artikel von fka.dev](https://blog.fka.dev/blog/2025-09-11-what-happened-to-googles-a2a/) hinterfragt den realen Traction von A2A.

---

## Was fehlt? (Gaps & Unsolved Problems)

### Evidence

1. **Inter-Agent Trust:** "Implementing practical mechanisms and infrastructure for facilitating greater trust and transparency between agents is therefore an important open problem." — [Hammond et al., 2025 (U of Toronto)](https://www.cs.toronto.edu/~nisarg/papers/Multi-Agent-Risks-from-Advanced-AI.pdf)

2. **Security bei Agent-Interaktion:** "Multi-agent systems introduce security challenges that go beyond existing cyber-security or AI safety frameworks. When agents interact directly or through shared environments, novel threats emerge." — [arxiv.org/abs/2505.02077](https://arxiv.org/abs/2505.02077)

3. **Keine Standards für Governance:** Linux Foundation hat Ende 2025 die "Agentic AI Foundation" gegründet — Standards sind noch in Arbeit. — [The Conversation](https://theconversation.com/ai-agents-arrived-in-2025-heres-what-happened-and-the-challenges-ahead-in-2026-272325)

4. **Sim-to-Real Gap:** Algorithmen funktionieren in Simulation, versagen in der echten Welt. Predictability und Safety bei Deployment sind ungelöst. — [Wake Forest / TechXplore](https://techxplore.com/news/2025-12-multi-agent-ai-figure.html)

5. **Production Readiness:** AutoGen wird als "more aligned with research or exploratory workflows than structured, governed enterprise deployments" beschrieben. — [Multimodal.dev](https://www.multimodal.dev/post/best-multi-agent-ai-frameworks)

### Interpretation

Die Lücken clustern um **Trust**, **Safety** und **Governance**. Kein Framework löst heute zuverlässig:
- Wie vertraut Agent A dem Output von Agent B?
- Wie verhindert man cascading failures in Multi-Agent-Pipelines?
- Wie auditiert man Entscheidungsketten über mehrere Agents?

---

## Vergleich: Unser Ansatz (OpenClaw) vs. Markt

| Dimension | Marktstandard | Unser Ansatz | Bewertung |
|-----------|---------------|-------------|-----------|
| **Spezialisierte Agents** | ✅ CrewAI, MetaGPT machen das auch (Role-based) | ✅ Spezialisierte Agents mit eigenen AGENT.md | Parity — kein Differentiator |
| **Trust Scoring** | ❌ Kein Framework hat das | ✅ Trust Level pro Agent (30-100) | **Echte Differenzierung** — adressiert das #1 Open Problem |
| **QA Pipeline** | ⚠️ Rudimentär (Langfuse Tracing, manuelle Reviews) | ✅ Corrections.md, Output-Tracker, Before-Any-Output Checklist | **Differenzierung** — systematischer als jeder Competitor |
| **Orchestrierung** | Graph, Hierarchical, Conversational | Hierarchisch (King → Sub-Agents) | Funktional, aber weniger flexibel als LangGraph |
| **Agent-zu-Agent Protokoll** | A2A (Google), proprietäre Lösungen | File-basiert (AGENT.md, Memory) | Einfacher, aber nicht interoperabel |
| **Memory/State** | Shared state, vector stores | File-basiert (memory/*.md, MEMORY.md) | Transparent & debuggable, aber nicht skalierbar |

### Empfehlung

Unser System hat **zwei echte Differentiators**: Trust Scoring und die QA Pipeline. Beides adressiert die größten Gaps im Markt. Die Schwäche liegt in Interoperabilität (kein A2A-Support) und Skalierung (File-basiert statt programmatisch). 

**Mein Vote:** Nicht auf Framework-Migration setzen. Stattdessen: Trust Scoring und QA Pipeline als **eigenständiges Layer** konzeptualisieren, das *auf* existierenden Frameworks (LangGraph, CrewAI) aufsetzen könnte. Das ist die interessantere Position als "noch ein Framework".

---

## Zahlen (verifiziert)

- **CrewAI:** ~30.000 GitHub Stars, ~1M Downloads/Monat — Quelle: [Python in Plain English, Feb 2026](https://python.plainenglish.io/autogen-vs-crewai-vs-langgraph-2026-comparison-guide-fd8490397977)
- **AutoGen:** ~30.000 GitHub Stars — Quelle: gleiches
- **LangChain Ökosystem:** 70M+ Downloads/Monat — Quelle: gleiches
- **Gartner:** 40% Enterprise-Apps mit AI Agents bis Ende 2026 (vs. <5% 2025) — Quelle: [MLM](https://machinelearningmastery.com/7-agentic-ai-trends-to-watch-in-2026/)
- **Marktgröße:** $7,8 Mrd. (2025) → $52 Mrd. (2030) — Quelle: gleiches (Gartner via MLM)
- **Enterprise Adoption:** 78% Organisationen nutzen AI Agents in Production — Quelle: [Python in Plain English](https://python.plainenglish.io/autogen-vs-crewai-vs-langgraph-2026-comparison-guide-fd8490397977) (⚠️ Primärquelle nicht verifiziert)
- **ROI:** 30% Kostenreduktion, 35% Produktivitätssteigerung nach Implementierung — Quelle: [DEV.to](https://dev.to/eira-wexford/how-to-build-multi-agent-systems-complete-2026-guide-1io6) (⚠️ Primärquelle nicht verifiziert)

---

## Unsicher / Nicht Verifiziert

- Die 78% Enterprise-Adoption-Zahl konnte nicht auf eine Primärquelle zurückgeführt werden (Blog-Artikel ohne Citation)
- Die 30%/35% ROI-Zahlen stammen aus einem Tutorial-Artikel ohne Primärquelle
- Exakte GitHub Stars schwanken — "~30k" für CrewAI und AutoGen sind gerundete Werte aus Sekundärquellen
- LangGraph-spezifische Stars konnten nicht isoliert werden (ist Teil des LangChain-Repos)
- Ob A2A tatsächlich Traction hat, ist umstritten (siehe fka.dev-Artikel)

---

## Quellen

1. [Langfuse Blog — Comparing Open-Source AI Agent Frameworks](https://langfuse.com/blog/2025-03-19-ai-agent-comparison) — März 2025 — Framework-Vergleich mit Tracing-Integration
2. [Python in Plain English — Autogen vs CrewAI vs LangGraph 2026](https://python.plainenglish.io/autogen-vs-crewai-vs-langgraph-2026-comparison-guide-fd8490397977) — Feb 2026 — Aktuellster quantitativer Vergleich
3. [Google Developers Blog — A2A Protocol](https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/) — April 2025 — Primärquelle A2A
4. [arxiv.org — Multi-Agent Risks from Advanced AI](https://arxiv.org/abs/2502.14143) — Feb 2025 — Akademische Analyse Trust/Safety-Gaps
5. [arxiv.org — Open Challenges in Multi-Agent Security](https://arxiv.org/abs/2505.02077) — Mai 2025 — Security-Herausforderungen
6. [Machine Learning Mastery — 7 Agentic AI Trends 2026](https://machinelearningmastery.com/7-agentic-ai-trends-to-watch-in-2026/) — Jan 2026 — Marktdaten (Gartner)
7. [DEV.to — LangGraph vs CrewAI vs AutoGen Guide](https://dev.to/pockit_tools/langgraph-vs-crewai-vs-autogen-the-complete-multi-agent-ai-orchestration-guide-for-2026-2d63) — Feb 2026 — Architektur-Patterns
8. [Multimodal.dev — 8 Best Multi-Agent Frameworks](https://www.multimodal.dev/post/best-multi-agent-ai-frameworks) — Dez 2025 — Breiterer Framework-Überblick
9. [Linux Foundation — A2A Project Launch](https://www.linuxfoundation.org/press/linux-foundation-launches-the-agent2agent-protocol-project-to-enable-secure-intelligent-communication-between-ai-agents) — Juni 2025 — A2A Governance
10. [The Conversation — AI Agents 2025 Retrospective](https://theconversation.com/ai-agents-arrived-in-2025-heres-what-happened-and-the-challenges-ahead-in-2026-272325) — Jan 2026 — Branchenüberblick

---

## Beipackzettel

```
Confidence: 72%
Sources checked: 15+
Verified facts: 12
Unverified claims: 3 (78% Adoption, 30%/35% ROI, exakte Star-Counts)
Search queries used:
  - "multi-agent AI frameworks 2025 comparison open source"
  - "multi-agent framework production usage enterprise 2025 2026"
  - "Google A2A protocol agent-to-agent communication standard 2025"
  - "LangGraph CrewAI AutoGen GitHub stars downloads 2025 2026 traction"
  - "multi-agent AI unsolved problems gaps trust safety 2025"
  - "CrewAI GitHub stars AutoGen stars LangGraph stars February 2026"
Time spent: ~8 Minuten
Tier: 2 (internal decision support)
```

---

*Begründungen inline: Struktur folgt AGENT.md Research Brief Template + Exec Research Factory Trennung (Evidence/Interpretation/Empfehlung). Vergleichstabelle "Unser Ansatz vs. Markt" weil das die eigentliche Decision-relevante Frage ist. Tonalität direkt, keine LLM-Phrasen (corrections.md). Zahlen mit Quellen oder als unverifiziert markiert (AGENT.md Regel).*
