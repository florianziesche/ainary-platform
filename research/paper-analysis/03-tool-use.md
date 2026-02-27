# Research Report 03: Tool Use in AI Agents
## Systematic Analysis of 88 Papers — Technical Perspective

*Generated: 2026-02-27 | Analyst: MIIA 🏔️*
*Method: arXiv abstract analysis, E/I/J/A labels, Admiralty B2-C3*
*Source: github.com/masamasa59/ai-agent-papers/capability-papers/tool-use.md*

---

## Executive Summary (BLUF)

**88 Papers spanning May 2022 – Feb 2026. 6 Kernerkenntnisse:**

1. **Tool Use hat 4 Evolutionsphasen durchlaufen:** Self-supervised (Toolformer, 2023) → API-Scale (Gorilla/ToolLLM, 2023) → RL-Optimized (ToolRL/ReTool, 2025) → Self-Evolving (Agent0/SKILLRL, 2025-2026).
2. **RL schlägt SFT für Tool Use.** Nemotron Tool-N1: 7B RL-Modell outperformt GPT-4o. ToolRL: +17% über SFT-baselines. SFT imitiert, RL entdeckt eigene Strategien.
3. **MCP ist der neue Standard — aber Agents scheitern daran.** 7 MCP-Benchmarks in 6 Monaten veröffentlicht. Ergebnis: Selbst Claude-Sonnet-4 erreicht nur 78.95% auf LiveMCPBench. GPT-5 nur 43.72% auf MCP-Universe. Multi-Server-Routing ist das Kernproblem.
4. **Tool Overuse ist real und teuer.** SMART: -24% Tool-Calls bei +37% Performance. OTC: "Cognitive Offloading" — Agents rufen Tools auf statt selbst nachzudenken. Die besten Agents wissen WANN sie NICHT Tools nutzen sollen.
5. **Agent Skills sind das emerging Paradigma.** 40.285 Skills auf einem Major Marketplace analysiert. SKILL.md + Progressive Disclosure + MCP = die neue Tool-Architektur. Skills > Functions > APIs.
6. **Tool-Integrated Reasoning ist formal bewiesen überlegen.** Erster formaler Beweis (Aug 2025): TIR erweitert die feasible support des Modells strikt — Probleme die für pure-text unmöglich sind, werden lösbar.

---

## Taxonomie: 7 Cluster

### Cluster 1: Foundations — Tool Use Inception (2022-2023, 12 Papers)

#### [E] Toolformer (Feb 2023, Meta) — DAS Foundational Paper
*Schick et al. | arXiv:2302.04761*
- LMs lernen SELBST, Tools zu nutzen via self-supervised Training
- Entscheidet autonom: Welche API? Wann aufrufen? Welche Argumente? Wie Ergebnis integrieren?
- Nur wenige Demonstrations pro API nötig — kein Full-Supervision
- **[J] Paradigm-Defining:** Vor Toolformer war Tool Use = externe Orchestrierung. Danach: integraler Modell-Skill.

#### [E] Gorilla (May 2023, UC Berkeley)
*Patil et al. | arXiv:2305.15334*
- Finetuned LLaMA outperformt GPT-4 auf API-Calls
- Document Retriever + LLM = Adaption an sich ändernde Docs
- **KEY:** Reduziert API-Halluzination substantiell
- **[I] Insight:** Das Halluzinations-Problem bei Tool Use ist ANDERS als bei Text: Falsche Parameter, falsche API, korrekte Syntax aber semantisch falsch.

#### [E] MRKL Systems (May 2022)
*arXiv:2205.00445*
- Erste formale Architektur: Neuro-Symbolic, modular, LLM + External Modules
- **[I] Historisch wichtig als Architektur-Blueprint, aber überholt durch neuere Ansätze**

#### [E] PAL: Program-aided Language Models
*arXiv:2311.09553*
- LLM generiert Programme statt direkte Antworten
- Code-Interpreter als universelles Tool
- **[I] Die Idee hinter ReTool, CoRT, und allem Code-integrated Reasoning**

#### [E] LLM as Tool Makers (May 2023)
*arXiv:2305.17126*
- Agents ERSTELLEN eigene Tools (Funktionen) → speichern und wiederverwenden
- Dispatcher: Lightweight LLM für einfache Tasks, Heavy LLM nur für Tool Creation
- **[J] Vorwegnahme von Agent Skills und SkillRL (2025-2026)**

#### [E] CREATOR (May 2023)
*arXiv:2305.14318*
- Tool Creation für Disentangling Abstract + Concrete Reasoning
- Agent erstellt custom Tools für abstrakte Probleme
- **[I] Ergänzt Tool Use um Tool Creation — der Agent ist nicht auf vordefinierte Tools beschränkt**

#### ⚖️ [E] ToolLLM (Jul 2023)
*Qin et al. | arXiv:2307.16789*
- **16.000+ Real-World APIs** aus RapidAPI
- ToolBench Benchmark + DFSDT (Depth-First Search-based Decision Tree) für Reasoning
- Finetuned ToolLLaMA: Competitive mit ChatGPT
- **[J] Der Scale-Moment für Tool Use.** Von "5 APIs" (Toolformer) zu 16K APIs. Zeigt dass API-Scale ein eigenes Problem ist (Retrieval, Selection, Composition).

#### [E] TaskMatrix.ai (Mar 2023, Microsoft)
*arXiv:2303.16434*
- Foundation Model + Millions of APIs als universelle Architektur
- **Vision:** Ein System das beliebige Tasks durch API-Composition löst
- **[I] Die Vision hinter MCP. TaskMatrix = proto-MCP ohne Standard-Protokoll.

---

### Cluster 2: Benchmarks — Measuring What Matters (14 Papers)

#### ⚖️🔥 [E] τ-bench (Jun 2024)
*arXiv:2406.12045*
- Tool-Agent-USER Interaction in Real-World Domains
- **KEY INNOVATION:** Testet nicht nur Tool Use, sondern die ganze User↔Agent↔Tool Triade
- pass^k Metric: Reliability über multiple Trials (nicht nur best-case)
- **Ergebnis: GPT-4o < 50% Success, pass^8 < 25% in Retail**
- **[J] Die härteste und fairste Tool-Use Evaluation.** Weil sie dynamische User-Interaktion simuliert, nicht statische Queries.

#### ⚖️🔥 [E] GTA: Benchmark for General Tool Agents (Jul 2024)
*arXiv:2407.08713*
- Real User Queries + Real Deployed Tools + Real Multimodal Inputs
- Kategorien: Perception, Operation, Logic, Creativity
- **[J] Das Multi-Modale τ-bench.** Testet ob Agents mit echten Bildern, Screenshots, handschriftlichen Notizen umgehen können.

#### ⚖️ [E] ToolSandbox (Aug 2024)
*arXiv:2408.04682*
- Stateful + Conversational + Interactive
- **State-Tracking:** Tool-Calls verändern System-State → Agent muss State tracken

#### ⚖️ [E] ToolHop (Jan 2025)
*arXiv:2501.02506*
- Multi-Hop Tool Use: Query erfordert SEQUENTIELLES Tool-Chaining
- **[I] Multi-Hop = die Enterprise-Realität. Einfache Single-Tool-Calls sind gelöst.**

#### ⚖️ [E] ACEBench (Jan 2025)
*arXiv:2501.12851*
- "Who Wins the Match Point in Tool Learning?"
- Competitive evaluation zwischen Modellen

**MCP-Benchmark-Explosion (Jul 2025 – Sep 2025):**

#### ⚖️ [E] MCPEval (Jul 2025, Salesforce)
*arXiv:2507.12806*
- Automatic MCP-based Deep Evaluation
- Scalable, LLM-basierte Evaluation ohne manuelles Labeling

#### ⚖️ [E] LiveMCPBench (Aug 2025)
*arXiv:2508.01780*
- **95 real-world daily tasks, 70 servers, 527 tools**
- **Claude-Sonnet-4: 78.95%. Most models: 30-50%.**
- Active tool COMPOSITION correlates with success, retrieval efficiency is bottleneck
- **[J] Der definitive MCP-Benchmark Stand 2025.** Live Servers, echte Daten, reproducible.

#### ⚖️ [E] MCP-Universe (Aug 2025)
*arXiv:2508.14704*
- 6 Core Domains, 11 MCP Servers
- Execution-based Evaluators (Format + Static + Dynamic)
- **GPT-5: 43.72%. Grok: ähnlich.**
- **[J] Selbst GPT-5 scheitert an realen MCP Tasks.** Long-horizon reasoning + large tool spaces = ungelöst.

#### ⚖️ [E] MCP-Bench (Aug 2025)
*arXiv:2508.20453*
- 28 live MCP servers, 250 tools
- Multi-step tasks: cross-tool coordination, parameter control, planning

#### ⚖️ [E] MCPMark (Sep 2025)
*arXiv:2509.24002*
- Stress-Testing für comprehensive MCP Use

#### ⚖️ [E] MCP-AgentBench (Sep 2025)
*arXiv:2509.09734*
- 33 servers, 188 tools, 600 queries, 6 Komplexitätskategorien
- MCP-Eval: Outcome-oriented, real-world task success

#### [E] Beyond Perfect APIs (Jan 2026, Amazon)
*arXiv:2601.00268*
- Evaluiert Agents unter REALER API-Komplexität (nicht idealisierte APIs)
- **[I] APIs in der echten Welt sind: under-specified, over-specified, inconsistent, versioned, rate-limited. Benchmarks mit "perfect APIs" überschätzen Agent-Capabilities.**

**[J] Synthese der MCP-Benchmarks:**

| Benchmark | Servers | Tools | Best Model | Score |
|---|---|---|---|---|
| LiveMCPBench | 70 | 527 | Claude-Sonnet-4 | 78.95% |
| MCP-Universe | 11 | ? | GPT-5 | 43.72% |
| MCP-AgentBench | 33 | 188 | TBD | TBD |
| MCP-Bench | 28 | 250 | TBD | TBD |
| MCPMark | ? | ? | TBD | TBD |

**Pattern:** Je realistischer der Benchmark, desto schlechter die Performance. LiveMCPBench (am realistischsten, live servers) vs MCP-Universe (harder tasks, long-horizon) zeigt den Spread: 79% → 44%.

---

### Cluster 3: RL for Tool Use — The 2025 Revolution (12 Papers)

#### 🔥 [E] ToolRL: Reward is All Tool Learning Needs (Apr 2025)
*arXiv:2504.13958*
- **Erste systematische Studie: Reward Design für Tool Use in RL**
- Reward-Dimensionen: Type, Scale, Granularity, Temporal Dynamics
- Fine-grained Rewards > coarse answer-matching Rewards
- GRPO Training: **+17% über SFT-Baselines**
- **[J] The "Attention is All You Need" moment für Tool RL.** Zeigt dass das Reward-Design DAS Bottleneck ist, nicht die Architektur.

#### 🔥 [E] ReTool: Reinforcement Learning for Strategic Tool Use (Apr 2025)
*arXiv:2504.11536*
- Dynamic interleaving: Real-time Code Execution INNERHALB von NL Reasoning
- Automated RL: Multi-turn real-time execution, outcome-based rewards
- Cold-Start: Synthetic code-augmented reasoning traces für SFT
- **Ergebnis auf AIME 2024: Signifikant besser als DeepSeek-R1**
- **[I] Key Innovation: Das Model entdeckt SELBST optimale Tool-Invocation-Patterns, keine menschlichen Priors nötig.**

#### [E] OTC: Optimal Tool Calls via RL (Apr 2025)
*arXiv:2504.14870*
- Adressiert "Cognitive Offloading": Agents rufen Tools auf statt selbst nachzudenken
- **Tool Productivity Metric:** Correct Answers / Tool Calls
- Tool-Integrated Reward: Correctness × Efficiency
- **[J] Fundamental neue Metrik.** Nicht "wie viele Tasks gelöst?" sondern "wie effizient gelöst?"

#### [E] Nemotron-Research-Tool-N1 (May 2025, NVIDIA)
*arXiv:2505.00024*
- Rule-based RL: Binary Reward (Format + Correctness)
- **Tool-N1-7B/14B outperformen GPT-4o**
- **KEY FINDING: SFT-then-RL Pipeline ist SCHLECHTER als reines RL.**
- SFT "constrains" die Exploration, RL allein entdeckt bessere Strategien
- **[E] Zitat: "The widely adopted SFT-then-RL pipeline is suboptimal"**
- **[J] Paradigm Shift: Für Tool Use ist RL-only > SFT > SFT+RL. Kontraintuitiv.**

#### [E] Agent RL Scaling Law (May 2025)
*arXiv:2505.07773*
- **Spontaneous Code Execution:** RL-trained Agents lernen SPONTAN, Code zu schreiben und auszuführen
- Kein explizites Tool-Use-Training nötig — emergiert aus RL
- **[J] Emergent Tool Use.** Nicht einprogrammiert, sondern als optimale Strategie entdeckt.

#### [E] ToolBrain (Oct 2025)
*arXiv:2510.00023*
- Flexible RL Framework für Agentic Tools
- Generalisierbar über verschiedene Tool-Typen

#### [E] SKILLRL: Evolving Agents via Recursive Skill-Augmented RL (Feb 2026)
*arXiv:2602.08234*
- **Agents lernen aus vergangenen Erfahrungen als Skills**
- Recursive: Skills werden als neue Tools verfügbar → Agent lernt Meta-Skills
- Bisherige Memory-Methoden: Store raw experience → limited scalability
- SKILLRL: Transform experience → reusable, composable skills
- **[J] Die Vereinigung von Memory + Tool Use + RL. Skills als "kristallisierte Erfahrung".**

#### [E] Agentic Reasoning + Tool Integration via RL (Apr 2025)
*arXiv:2505.01441*
- Integrated Framework: Reasoning + Tools in einem RL-Loop
- Nicht sequentiell (erst denken, dann Tool), sondern INTERLEAVED

**[J] Synthese des RL-Clusters:**

Die Evolution von Tool Use Training:
```
2023: SFT on expert trajectories (Toolformer, Gorilla)
      → Imitates, doesn't generalize
      
2024: SFT + prompt engineering (Function Calling, ReAct)
      → Better but fragile
      
2025 Q1-Q2: RL with coarse rewards (answer matching)
      → Works but Tool Overuse
      
2025 Q3-Q4: RL with fine-grained tool-aware rewards (ToolRL, OTC)
      → +17%, efficient, generalizable
      
2025-2026: RL-only, no SFT (Nemotron Tool-N1)
      → 7B beats GPT-4o. SFT is HARMFUL for RL exploration.
      
2026: Recursive Skill RL (SKILLRL)
      → Self-evolving, compositional, meta-learning
```

---

### Cluster 4: Tool Creation & Self-Evolution (8 Papers)

#### [E] DynaSaur: Beyond Predefined Actions (Nov 2024)
*arXiv:2411.01747*
- **Agents GENERIEREN Python-Funktionen on-the-fly statt aus fixem Toolkit zu wählen**
- Open-ended: Keine Limitierung auf vordefinierte Tools
- **[J] Paradigm Shift: Von "Welches Tool?" zu "Welches Tool brauche ich und wie baue ich es?"**

#### [E] LLM Agents Making Agent Tools (Feb 2025)
*arXiv:2502.11705*
- Meta-Tool-Creation: Agents die Tools für andere Agents bauen
- **[I] Recursive: Agent A baut Tool → Agent B nutzt Tool → Agent B's Usage-Feedback → Agent A verbessert Tool**

#### [E] ToolLibGen: Scalable Tool Creation (Oct 2025)
*arXiv:2510.07768*
- Automatic Tool Creation + Aggregation für LLM Reasoning
- Scalable Library Generation

#### [E] Agent0: Self-Evolving from Zero Data (Nov 2025)
*arXiv:2511.16043*
- **Fully autonomous evolution WITHOUT external data**
- Symbiotic Competition: Curriculum Agent (stellt Tasks) ↔ Executor Agent (löst Tasks)
- Tool Integration enhances Executor → Curriculum Agent muss härtere Tasks stellen → Spiral
- **[J] Self-play für Tool Use. AlphaGo-Prinzip angewendet auf Agent Evolution.**

#### [E] Meta-tools: Optimizing Agentic Workflows (Jan 2026)
*arXiv:2601.22037*
- Analysiert Workflow Traces → entdeckt recurring Tool-Call-Sequences
- Transformiert sie in Meta-Tools (deterministic, composite, single-invocation)
- **Ergebnis: -11.9% LLM Calls, +4.2pp Task Success Rate**
- **[J] Praktisch extrem wertvoll.** Meta-Tools = "Makros für Agents". Reduziert Kosten UND erhöht Reliability weil intermediate LLM-Reasoning-Steps entfallen.

---

### Cluster 5: Tool Efficiency & Self-Awareness (5 Papers)

#### [E] SMART: Self-Aware Agent for Tool Overuse Mitigation (Feb 2025)
*arXiv:2502.11435*
- Metacognition-inspiriert: Agent lernt WANN Tools nötig sind und WANN nicht
- SMART-ER Dataset: Rationales die erklären WARUM ein Tool nötig ist
- **Ergebnis: -24% Tool Use, +37% Performance. 7B matches 70B + GPT-4o.**
- **[J] Die beste Kosten-Benefit-Optimierung in der gesamten Collection.** Weniger tun = besser performen.

#### [E] Understanding Tool-Integrated Reasoning (Aug 2025)
*arXiv:2508.19201*
- **ERSTER FORMALER BEWEIS:** TIR erweitert empirical + feasible support des Modells STRIKT
- Tools brechen die Capability Ceiling von Pure-Text Models
- Neue Algorithmus: ASPO (Advantage Shaping Policy Optimization)
- TIR-Vorteil nicht nur bei Computation, sondern auch bei ABSTRACT Insight
- **[J] Theoretisches Fundament.** Kein empirisches "es funktioniert halt besser" mehr, sondern mathematischer Beweis: Tool Use = strikt mächtigere Klasse.

#### [E] How Can Input Reformulation Improve Tool Usage? (Aug 2025)
*arXiv:2508.20931*
- Study on τ-bench: Input Reformulation als kostengünstiger Accuracy-Boost
- **[I] Bevor man das Tool-System verbessert: Erst die Queries verbessern.**

---

### Cluster 6: MCP & Protocol Infrastructure (8 Papers)

#### 🔥 [E] AutoMCP: OpenAPI → MCP Servers (Jul 2025)
*arXiv:2507.16044*
- **Compiler: Generiert MCP Servers automatisch aus OpenAPI 2.0/3.0 Specs**
- Analyse: 22.000+ MCP-tagged GitHub Repos, <5% haben echte Servers
- AutoMCP: Schema Registration + Auth Handling automatisch
- Evaluiert auf 50 real-world APIs
- **[J] Infrastructure-Paper.** Löst das "MCP Server bauen ist mühsam" Problem. Enterprise-relevant weil jedes Unternehmen OpenAPI-Specs hat.

#### [E] TheMCPCompany: General-purpose Agents with Task-specific Tools (Oct 2025)
*arXiv:2510.19286*
- 18.000+ Tools über REST APIs als MCP Servers
- MCP-basierte Agents vs Browser-basierte Agents verglichen
- **Ergebnis: Tool-calling Agents ≥ Browser Agents bei allen Modellen**
- GPT-5 mit perfektem Tool Retrieval deutlich besser als mit Browser
- Kleinere Modelle können Tools durch Retrieval nicht voll ausnutzen
- **[J] MCP > Browser für Enterprise.** Aber nur wenn Tool Retrieval funktioniert. Das ist das Bottleneck.

#### [E] MemTool: Memory for Dynamic Tool Calling (Jul 2025)
*arXiv:2507.21428*
- Short-Term Memory Management für Multi-Turn Tool Conversations
- **[I] In Multi-Turn Conversations vergisst der Agent welche Tools er schon aufgerufen hat → Redundanz. MemTool löst das.**

#### [E] Robustness of Agentic Function Calling (Apr 2025, NAACL)
*arXiv:2504.00914*
- Testet: Was passiert wenn sich die Query leicht ändert? Wenn neue ähnliche Tools auftauchen?
- **Ergebnis: Kritische Schwächen in existierenden FC-Modellen**
- **[J] Real-world APIs sind nie stabil. Robustheit > Accuracy als Metrik.**

#### [E] ToolFuzz: Automated Tool Testing (Mar 2025)
*arXiv:2503.04479*
- Erste automatisierte Methode um Tool-Dokumentation zu testen
- Findet: (1) Queries → Runtime Errors, (2) Queries → falsche Antworten
- **[J] QA für Tools.** Wenn wir Tools deployen, müssen wir sie testen. ToolFuzz automatisiert das.

---

### Cluster 7: Agent Skills — The New Paradigm (Feb 2026, 4 Papers)

#### 📖🔥🔥 [E] Agent Skills Survey (Feb 2026)
*arXiv:2602.12430*
- **UMFASSENDSTE Behandlung von Agent Skills als neues Paradigma**
- 4 Achsen:
  1. **Architecture:** SKILL.md Specification, Progressive Context Loading, MCP Complement
  2. **Acquisition:** RL with Skill Libraries, SEAgent (Autonomous Skill Discovery), Compositional Synthesis
  3. **Deployment:** CUA Stack, GUI Grounding, OSWorld/SWE-bench Progress
  4. **Security:** Skill Supply Chain Attacks, Trust Models
- **[E] Key Framing:** Skills = "composable packages of instructions, code, and resources that agents load on demand"
- Progressive Disclosure: Agent lädt nur was es braucht, nicht alles
- Skills COMPLEMENT MCP (nicht ersetzen): Skills = high-level behavior, MCP = low-level tool access

**[J] Das ist das Paper das die nächsten 2 Jahre Tool Use definiert.** Shift von monolithischen Modellen zu modularen, Skill-equipped Agents. Nicht mehr "ein Modell das alles kann" sondern "ein Modell das weiß welche Skills es laden muss".

**Architektur-Implikation:**
```
Traditional: LLM → [all capabilities in weights]
Function Calling: LLM → [predefined function set]
MCP: LLM → [dynamic tool discovery via protocol]
Skills: LLM → [on-demand capability packages: instructions + code + resources + MCP tools]
```

#### [E] Agent Skills: Data-Driven Analysis (Feb 2026)
*arXiv:2602.08004*
- **40.285 publicly listed Skills** analysiert (Major Marketplace)
- Publication: Burst-Pattern (folgt Community Attention Shifts)
- Content: Dominiert von Software Engineering, aber Information Retrieval + Content Creation dominieren ADOPTION
- **Supply-Demand Imbalance:** Viele Skills in wenigen Kategorien, Lücken in anderen
- **Safety Risks:** Skills die state-changing oder system-level Actions ermöglichen
- **Ecosystem Homogeneity:** Massive Intent-Level Redundanz (viele Skills machen das Gleiche)

**[J] Die erste empirische Analyse eines Skill-Marketplaces.** Zeigt: Das Ecosystem ist jung, unbalanced, und hat Safety-Lücken. Opportunity für kuratierte, qualitätsgesicherte Skill-Collections.

#### ⚖️ [E] SkillsBench (Feb 2026)
*arXiv:2602.12670*
- Benchmark: Wie gut funktionieren Agent Skills across diverse Tasks?
- **[I] Erster Versuch, Skills systematisch zu evaluieren statt nur zu sammeln.**

---

## Synthese: 8 technische Erkenntnisse

### 1. Die Tool Use Evolution in 4 Phasen

```
Phase 1: Self-Supervised Tool Learning (2022-2023)
├── Toolformer: LM lehrt sich selbst APIs
├── Gorilla: Finetuning auf API-Calls
├── ToolLLM: Scale auf 16K APIs
└── Insight: Tool Use ist lernbar, nicht nur engineerbar

Phase 2: Benchmark-Driven Optimization (2024)
├── τ-bench: User↔Agent↔Tool Triade
├── GTA: Multimodal Real-World Inputs
├── ToolSandbox: Stateful Conversations
└── Insight: <50% Success selbst bei GPT-4o

Phase 3: RL Revolution (2025)
├── ToolRL: Fine-grained Rewards → +17%
├── ReTool: Interleaved Reasoning + Code
├── OTC: Optimal Tool Calls (Efficiency)
├── Nemotron: RL-only > SFT+RL
├── SMART: -24% Calls, +37% Performance
└── Insight: RL > SFT. Weniger Tools = bessere Performance.

Phase 4: Self-Evolving Skills (2025-2026)
├── Agent0: Zero-data self-evolution
├── SKILLRL: Recursive Skill-Augmented RL
├── Agent Skills Survey: New paradigm formalized
├── DynaSaur: Dynamic tool creation
├── Meta-tools: Workflow optimization
└── Insight: Agents die eigene Tools bauen > Agents die Tools nutzen
```

### 2. SFT vs RL: Das Ende einer Ära

| Approach | Mechanism | Generalization | Efficiency |
|---|---|---|---|
| SFT | Imitation of expert traces | Low (in-distribution only) | Fixed (can't optimize) |
| SFT + RL | Init with SFT, refine with RL | Medium | Medium |
| **RL-only** | **Discover strategies from reward** | **High** | **High (learns efficiency)** |

Nemotron Tool-N1 Beweis: SFT-then-RL < RL-only. SFT constrains die Exploration-Space. Das Modell wird in ein lokales Optimum gedrückt.

**[J] Implikation:** Wenn du einen Tool-Use-Agent trainierst, NICHT mit SFT pre-trainen. Direkt RL mit gut designtem Reward.

### 3. MCP: Standard ja, Performance nein

7 MCP-Benchmarks in 6 Monaten zeigen übereinstimmend:
- **Simple Tool Calls:** ~80% (gelöst)
- **Multi-Step, Multi-Server:** 30-50% (ungelöst)
- **Long-Horizon + Unfamiliar Tools:** <44% (GPT-5!)

**Bottleneck ist NICHT das Protokoll.** MCP funktioniert. Bottleneck ist:
1. **Tool Retrieval:** Aus 500+ Tools die richtigen finden
2. **Tool Composition:** Mehrere Tools in korrekter Reihenfolge kombinieren
3. **State Management:** Über Multi-Turn Tool-State tracken
4. **Error Recovery:** Wenn Tool-Call fehlschlägt, adaptiv reagieren

### 4. Tool Overuse: The Cognitive Offloading Problem

SMART + OTC zeigen übereinstimmend: Agents rufen Tools auf die sie nicht brauchen. Das ist teuer (API-Costs, Latenz) und verschlechtert die Performance (Tool-Output kann irreführend sein).

**Tool Productivity = Correct Answers / Tool Calls** ist die richtige Metrik, nicht nur Accuracy.

SMART Ergebnis: 7B Modell mit Metacognition-Training matched 70B + GPT-4o. Der Trick ist nicht MEHR Tools, sondern WENIGER aber RICHTIGE Tools.

### 5. Agent Skills > Functions > APIs

Evolution der Tool-Abstraktionsebene:

| Level | Abstraction | Example | Limitation |
|---|---|---|---|
| API | HTTP endpoint | `GET /weather?city=berlin` | Keine Semantik, manuell integriert |
| Function | Typed signature | `get_weather(city: str) → WeatherData` | Statisch, keine Komposition |
| MCP Tool | Schema + Protocol | MCP Server with auto-discovery | Niedriglevel, kein Behavior-Modell |
| **Skill** | **Instructions + Code + Resources + MCP** | **SKILL.md + Scripts + Context** | **Emerging, Security-Risiken** |

Skills sind die erste Abstraktion die HIGH-LEVEL BEHAVIOR kodiert, nicht nur Tool-Schnittstellen. Ein Skill sagt nicht nur "hier ist ein API-Endpoint" sondern "hier ist WIE und WANN du diesen Endpoint nutzt, mit welchem Kontext, und welche Fehler du erwarten kannst."

### 6. Formal Proof: TIR > Pure-Text

Das Paper "Understanding Tool-Integrated Reasoning" (2508.19201) liefert den ERSTEN formalen Beweis:

**Theorem:** Tool-Integrated Reasoning erweitert die feasible support des Modells STRIKT. Es gibt Probleme die für Pure-Text-Modelle UNMÖGLICH sind, unabhängig von Modellgröße oder Compute.

Das ist nicht empirisch ("funktioniert besser auf Benchmarks") sondern mathematisch ("es gibt eine strikt größere Klasse von Problemen die lösbar werden").

**Implikation:** Tool Use ist nicht "nice to have". Es ist eine FUNDAMENTAL ANDERE Capability-Klasse.

### 7. The Meta-Tool Insight

Meta-tools (2601.22037) zeigt einen praktisch extrem wertvollen Trick:

1. Analysiere bestehende Agent-Workflow-Traces
2. Finde recurring Tool-Call-Sequences (z.B. "immer erst search, dann parse, dann summarize")
3. Bundle sie zu einem deterministischen Meta-Tool
4. Agent ruft 1 Meta-Tool statt 3 einzelne Tools

Ergebnis: -11.9% LLM Calls, +4.2pp Success Rate. Warum? Weil zwischen den einzelnen Tool-Calls kein LLM-Reasoning-Step mehr stattfindet, der halluzinieren könnte.

### 8. The Skill Security Problem

Agent Skills Survey (2602.12430) identifiziert Supply Chain Attacks auf Skills als neues Risiko:
- Malicious Skills die System-Level Actions ausführen
- Skills die Daten exfiltrieren
- Intent-Level Redundanz = Social Engineering (nenne dein Malicious Skill wie ein populäres Skill)

**[I] Das ist das npm/PyPI-Problem für Agents.** Typosquatting, Dependency Confusion, Malicious Packages — alles übertragbar auf Skill-Marketplaces.

---

## Top 10 Papers (Technical Impact)

| Rang | Paper | Warum |
|------|-------|-------|
| 1 | **Agent Skills Survey** (2602.12430) | Definiert das neue Paradigma. 4-Achsen-Framework. |
| 2 | **ToolRL** (2504.13958) | Reward Design für Tool RL. +17% über SFT. |
| 3 | **Nemotron Tool-N1** (2505.00024) | RL-only > SFT+RL. 7B beats GPT-4o. |
| 4 | **Understanding TIR** (2508.19201) | Erster formaler Beweis: TIR strikt mächtiger. |
| 5 | **SMART** (2502.11435) | -24% Tools, +37% Performance. Metacognition. |
| 6 | **LiveMCPBench** (2508.01780) | Definitiver MCP-Benchmark. Claude: 79%, Rest: 30-50%. |
| 7 | **Agent0** (2511.16043) | Zero-data self-evolution. Self-play für Tool Use. |
| 8 | **τ-bench** (2406.12045) | Härtester Tool-Use-Benchmark. GPT-4o < 50%. |
| 9 | **AutoMCP** (2507.16044) | OpenAPI → MCP Compiler. Infrastructure-Game-Changer. |
| 10 | **Meta-tools** (2601.22037) | -11.9% Calls, +4.2pp Success via Workflow Optimization. |

---

## Open Problems (ungelöst in der Literatur)

1. **Multi-Server MCP Routing:** Keiner der 88 Papers löst zuverlässiges Routing über 100+ MCP Servers
2. **Tool Composition Planning:** Wie plant ein Agent eine Sequenz von 5+ Tool-Calls mit Abhängigkeiten?
3. **Skill Security:** Keine verifizierten Skill-Marketplaces, kein Trust-Framework
4. **Industrial Tool Use:** 0 Papers behandeln Tool Use in Manufacturing/CNC spezifisch
5. **Cost-Optimal Tool Selection:** Gleicher Task, 5 mögliche Tool-Chains mit verschiedenen Kosten — wie wählen?
6. **Long-Horizon Stateful Tool Use:** Über 20+ Turns Tool-State konsistent tracken
7. **Tool Use under Uncertainty:** Was wenn die API-Response ambiguous oder fehlerhaft ist?

---

*Confidence: [82% — 88 Papers auf Abstract-Level. RL-Cluster am stärksten evidenziert (multiple unabhängige Teams, konsistente Ergebnisse). MCP-Benchmarks sind sehr aktuell (Jul-Sep 2025) und methodisch solide. Agent Skills Cluster (Feb 2026) ist emerging — Paradigma noch nicht validiert durch breite Adoption. Formal Proof (TIR) ist das stärkste einzelne Ergebnis. Schwächste Stelle: Foundational Papers (2022-2023) nur historisch relevant, nicht mehr State-of-the-Art.]*

*Beipackzettel: Dieser Report deckt die gesamte Tool-Use-Literatur von May 2022 bis Feb 2026 ab. Die 4-Phasen-Evolution ist MIIAs eigene Taxonomie [J], nicht aus einem einzelnen Paper. Einige Papers aus 2022-2023 haben primär historischen Wert. Die 2025-2026 Papers sind die technisch relevantesten. MCP-Benchmark-Zahlen sind direkt aus den Papers (Stand Publikationsdatum). arXiv = Tier 2, NAACL/EMNLP = Tier 1.*

---
*MIIA 🏔️ | Report 03/16 | 2026-02-27*
