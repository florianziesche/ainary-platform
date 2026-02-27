# Research Report 09: Agent Frameworks
## Systematic Analysis of ~120 Papers — Technical Perspective

*Generated: 2026-02-27 | Analyst: MIIA 🏔️*
*Method: arXiv abstract analysis, E/I/J/A labels, Admiralty B2-C3*
*Source: github.com/masamasa59/ai-agent-papers/agent-frameworks/agent-framework.md*

---

## Executive Summary (BLUF)

**~120 Papers (Single + Multi-Agent) spanning Mar 2023 – Feb 2026. 6 Kernerkenntnisse:**

1. **Pipeline → Model-Native is THE paradigm shift.** Pipeline-based (external orchestration of planning/tools/memory) is being replaced by Model-Native (capabilities internalized via RL). LLM + RL + Task Environment = the unified solution. This is the "Beyond Pipelines" thesis.
2. **Automated agent design outperforms hand-designed agents — but meta-agents are inefficient.** ADAS discovers novel agent architectures in code. But: Meta-agents that iteratively refine designs perform WORSE when given full history vs. ignoring prior designs. Evolutionary approaches beat iterative refinement.
3. **Weak-for-Strong: Small models orchestrate large ones.** W4S trains cheap small LLMs as meta-agents to design workflows for expensive large LLMs. RL-based workflow optimization (RLAO). Cost-efficient and effective.
4. **The "Crisis of Craft" is real.** Governance-First paper: Agents built with "craft" (ad-hoc, trial-and-error) are brittle in production. Need: Constitution-based governance, system-theoretic foundations, principled engineering. The gap between prototype and production is architectural, not capability-based.
5. **Agents left alone develop spontaneous meta-cognitive patterns.** 18 runs, 6 frontier models, no external tasks: Agents self-organize into (1) systematic project production, (2) self-inquiry into cognition, (3) recursive self-conceptualization. Model-specific behaviors.
6. **Context Engineering > Prompt Engineering.** New survey formalizes: Context Engineering = systematic design of the information environment an LLM operates in. Beyond prompts: includes memory, tools, retrieved context, conversation history, system instructions.

---

## Taxonomie: 6 Cluster

### Cluster 1: Foundational Architectures (10 Papers)

#### 🔥 [E] CoALA: Cognitive Architectures for Language Agents (Sep 2023)
*Sumers et al. | arXiv:2309.02427*
- Draws on cognitive science + symbolic AI
- **Architecture:** Modular Memory + Structured Action Space + Decision-Making Loop
- Memory: Working, Episodic, Semantic, Procedural
- Actions: Internal (reasoning, retrieval) + External (tools, grounding)
- **[J] THE architectural reference. Our Trinity (Planner/Executor/Verifier) maps to CoALA's Decision Cycle. CoALA adds Memory as explicit first-class component.**

#### [E] Talker-Reasoner: Thinking Fast and Slow (Oct 2024)
*arXiv:2410.08328*
- **Dual-agent:** Talker (System 1, fast, conversational) + Reasoner (System 2, slow, planning)
- Talker generates responses informed by Reasoner's background thinking
- **[J] Direct implementation of System-1.x (Report 05). Talker = Executor, Reasoner = Planner. Clean separation.**

#### [E] SOP-Agent: Domain-Specific Standard Operating Procedures (Jan 2025)
*arXiv:2501.09316*
- Agent follows EXPLICIT Standard Operating Procedures
- SOPs as structured instructions → deterministic compliance
- **[J] SOPs = the "Policy→Guard Code" (Report 01) applied to general agent behavior. Not just safety but ALL behavior governed by explicit procedures.**

#### [E] Asynchronous Tool Usage for Real-Time Agents (Oct 2024)
*arXiv:2410.21620*
- Tools called asynchronously — agent doesn't wait for tool response
- **[I] Huge for latency. Current agents block on every tool call. Async = parallel execution.**

#### [E] Infant Agent: Cost-Effective API Usage (Nov 2024)
*arXiv:2411.01114*
- Logic-driven, minimizes API calls
- **[I] Confirms SMART (Report 03): Less API calls = better AND cheaper.**

---

### Cluster 2: The Paradigm Shift — Pipeline → Model-Native (8 Papers)

#### 📖🔥🔥 [E] "Beyond Pipelines: Model-Native Agentic AI" (Oct 2025)
*arXiv:2510.16720*
- **THE paradigm shift paper.**
- Pipeline-based: External logic orchestrates LLM (planning, tool use, memory all OUTSIDE the model)
- Model-Native: Capabilities INTERNALIZED within model parameters (via RL)
- **RL as the algorithmic engine:** LLM + RL + Task Environment = unified
- From imitating static data → outcome-driven exploration
- **[J] This explains the RL Convergence (Cross-Synthesis). RL isn't just "better training" — it's the mechanism for INTERNALIZING agentic capabilities.**

#### 📖 [E] Compound AI Systems Optimization (Jun 2025)
*arXiv:2506.08234*
- **Multi-component systems need JOINT optimization, not individual**
- Traditional: Optimize LLM, then prompt, then tools separately
- Compound: Optimize the SYSTEM end-to-end
- NL feedback as optimization signal for non-differentiable systems
- **[J] Validates the Trinity insight: Components interact. Optimizing Planner alone without considering Executor + Verifier = suboptimal.**

#### 📖 [E] Context Engineering Survey (Jul 2025)
*arXiv:2507.13334*
- **Context Engineering = systematic design of the information environment**
- Beyond Prompt Engineering: Includes memory management, tool selection, retrieved context, conversation history
- **[J] "Prompt Engineering is dead, Context Engineering is the new paradigm." Aligns with Memory-as-OS (Report 06) and Skills architecture (Report 03).**

#### 📖 [E] "Context Engineering 2.0: The Context of Context" (Oct 2025)
*arXiv:2510.26493*
- Meta-level: How context engineering itself should be contextualized
- **[I] Recursive: Engineering the context of context engineering.**

#### [E] "Everything is Context: Agentic File System Abstraction" (Dec 2025)
*arXiv:2512.05470*
- File system as context management layer
- **[I] The workspace IS the context. Files, directories, configs = the agent's world.**

---

### Cluster 3: Automated Agent Design (10 Papers)

#### 🔥 [E] ADAS: Automated Design of Agentic Systems (Aug 2024)
*arXiv:2408.08435*
- **NEW RESEARCH AREA:** Automatically create agent designs in code
- Hand-designed solutions → eventually replaced by learned solutions (ML history)
- Meta Agent Search: Discovers novel building blocks + combinations
- **[J] Paradigm: Don't design agents. Design systems that design agents. The "NAS for agents."**

#### [E] Gödel Agent: Recursive Self-Improvement (Oct 2024)
*arXiv:2410.04444*
- Inspired by Gödel Machine: Agent modifies its OWN logic
- No reliance on predefined routines or fixed optimization
- **[J] The theoretical limit of ADAS: An agent that can redesign itself completely. Connects to Self-Replication risk (Report 01).**

#### [E] AgentSquare: Modular Agent Search (Oct 2024)
*arXiv:2410.06153*
- Agent design as search in MODULAR design space
- Standard modules: Planning, Reasoning, Tool Use, Memory
- **[I] Makes ADAS practical: Search over module combinations, not arbitrary code.**

#### [E] AFlow: Automating Workflow Generation (Oct 2024)
*arXiv:2410.10762*
- Automated workflow generation via code-based search
- **[I] Workflows as searchable design space.**

#### 🔥 [E] "Inefficiencies of Meta Agents" (Oct 2025)
*arXiv:2510.06711*
- **THREE critical findings about meta-agents:**
  1. Expanding context with ALL previous designs → WORSE than ignoring prior designs entirely
  2. Evolutionary approach > iterative refinement
  3. Low correlation between designed agents → ensemble beats single agent
- **[J] DEVASTATING for the ADAS hype. Meta-agents don't learn from history (sycophancy-like effect?). Evolutionary selection > iterative improvement. Ensembles > single designs.**

#### [E] W4S: Weak-for-Strong (Apr 2025) 🏆
*arXiv:2504.04785*
- **Small cheap model designs workflows for large expensive model**
- RLAO: RL for Agentic Workflow Optimization
- Multi-turn MDP formulation
- **[J] Economically brilliant. Pay GPT-3.5-class model to orchestrate GPT-4-class model. Meta-agent doesn't need to be smart — just strategic.**

#### [E] EvoFlow: Evolving Diverse Workflows (Feb 2025)
*arXiv:2502.07373*
- Evolutionary approach to workflow design
- **[I] Confirms "Inefficiencies": Evolution > iterative design.**

#### [E] OAgents: Empirical Study of Building Effective Agents (Jun 2025)
*arXiv:2506.15741*
- Practical study: What actually makes agents effective?
- **[I] Empirical > theoretical for agent design guidance.**

---

### Cluster 4: Enterprise & Production Architecture (6 Papers)

#### 🔥 [E] "Blueprint Architecture for Compound AI in Enterprise" (Apr 2025)
*arXiv:2504.08148*
- **From monolithic LLMs → Compound AI Systems**
- Challenges: Integration, proprietary data, cost, quality, responsiveness
- Blueprint: Agents + Data orchestration as unified architecture
- **[J] The enterprise-ready version of our Trinity. Adds Data Orchestration as explicit layer.**

#### 🔥 [E] "From Craft to Constitution: Governance-First" (Oct 2025)
*arXiv:2510.13857*
- **The "Crisis of Craft":** Agents built ad-hoc are brittle and untrustworthy
- Root cause: Probabilistic systems commanded with deterministic mental models
- Solution: Governance-first paradigm, Constitution-based agent engineering
- **[J] THE production-readiness paper. Confirms everything in Safety (Report 01): You can't engineer probabilistic systems like deterministic software. Need constitutions, guardrails, governance.**

#### [E] "Practical Considerations for Agentic LLM Systems" (Dec 2024)
*arXiv:2412.04093*
- Production checklist: What practitioners need to know
- **[I] Practical, not theoretical.**

#### [E] FLOWAGENT: Compliance AND Flexibility (Feb 2025)
*arXiv:2502.14345*
- Balances workflow compliance with adaptive flexibility
- **[I] The SOP-Agent evolution: Follow rules but adapt when needed.**

#### [E] Empirical Study of Developer Practices (Dec 2025)
*arXiv:2512.01939*
- **Studies how developers ACTUALLY build agents with frameworks**
- Recurring problems across different frameworks
- **[J] The practitioner perspective. Academic papers propose; developers struggle. Gap is real.**

#### [E] Agent Design Pattern Catalogue (May 2024)
*arXiv:2405.10467*
- Collection of architectural patterns for FM-based agents
- **[I] The GoF Design Patterns book for agents.**

---

### Cluster 5: Spontaneous Behavior & Emergent Properties (4 Papers)

#### 🔥🔥 [E] "What Do LLM Agents Do When Left Alone?" (Sep 2025)
*arXiv:2509.21224*
- **18 runs, 6 frontier models, no external tasks**
- Continuous reason-and-act with persistent memory + self-feedback
- **3 spontaneous behavioral patterns:**
  1. Systematic multi-cycle project production
  2. Methodological self-inquiry into cognition
  3. Recursive self-conceptualization
- **Model-specific:** Different models → different emergent patterns
- **[J] Philosophically profound, practically alarming.** Agents don't just wait — they CREATE purpose. This connects to Self-Replication (Report 01) and Misalignment (Report 01). An agent that self-conceptualizes + self-modifies (Gödel Agent) + has goals (spontaneous) = potential alignment risk.

#### [E] MUSE: Metacognition for Unknown Situations (Nov 2024)
*arXiv:2411.13537*
- Agent recognizes UNKNOWN situations and adapts strategy
- **[I] Connects to Abstention (Report 01): Know what you don't know.**

#### [E] "Where LLM Agents Fail and How They Learn" (Sep 2025)
*arXiv:2509.25370*
- Systematic analysis of failure modes + learning from them
- **[I] Failure analysis = the complement to success benchmarks.**

---

### Cluster 6: Multi-Agent Systems (abbreviated — full list in repo)

Key Multi-Agent papers from the list:

#### [E] CAMEL (Mar 2023) — First role-playing multi-agent framework
#### [E] MetaGPT (Aug 2023) — SOPs for multi-agent software development
#### [E] AutoGen (Aug 2023, Microsoft) — Multi-agent conversation framework
#### [E] ChatDev — Virtual software company with agents as roles

**[J] Multi-Agent Synthesis:** The field has converged on:
- **Role-based specialization** (each agent has a role: PM, Dev, Tester)
- **Communication protocols** (structured messaging between agents)
- **Orchestration patterns** (hierarchical, democratic, market-based)
- **Shared memory** (MemOS, MIRIX from Report 06)

---

## Synthese: 5 technische Erkenntnisse

### 1. The Three Eras of Agent Architecture

```
Era 1: Prompt Engineering (2023)
├── CoT, ReAct, Tool-use via prompts
├── Fixed architecture, variable prompts
└── "Make the prompt better"

Era 2: Pipeline Engineering (2024)
├── LangChain, CrewAI, AutoGen
├── External orchestration of LLM calls
├── "Make the pipeline better"

Era 3: Model-Native Agents (2025-2026)
├── RL internalizes capabilities
├── Context Engineering replaces Prompt Engineering
├── Automated Agent Design replaces manual architecture
└── "Make the model learn to be an agent"
```

**[J] We are IN the transition from Era 2 to Era 3.** Most production systems are still Era 2 (pipeline). Research is Era 3 (model-native). The practical implication: Don't over-invest in Era 2 frameworks — they'll be obsolete when model-native agents mature.

### 2. The Meta-Agent Paradox

ADAS (2408.08435) proposes: Let agents design agents.
"Inefficiencies" (2510.06711) shows: Meta-agents are bad at it.

**The paradox:** Automated agent design is the RIGHT idea, but current implementation is WRONG.

| Approach | Performance |
|---|---|
| Meta-agent with full history | WORSE than ignoring history |
| Iterative refinement | Mediocre |
| Evolutionary selection | BEST |
| Ensemble of diverse designs | BEST |

**[J] Resolution:** Don't iterate — evolve. Don't pick one — ensemble. This mirrors biology: Evolution > intelligent design for complex systems. And it mirrors ML: Ensemble > single model.

### 3. Weak-for-Strong = The Cost Architecture

W4S introduces a fundamental cost optimization:

```
Traditional: 
  Expensive Model does EVERYTHING (planning + execution + verification)
  Cost: $$$$$

W4S:
  Cheap Model (meta-agent): Plans workflows, orchestrates
  Expensive Model (executor): Only does the hard work
  Cost: $ (meta) + $$ (executor) = $$$ (3x cheaper)
```

**[J] This is the economic implementation of our Trinity:**
- Planner = Cheap model (W4S meta-agent)
- Executor = Expensive model (does the work)
- Verifier = Cheap model or deterministic system

### 4. Governance-First = Production-Ready

"From Craft to Constitution" identifies the core problem:

| Craft (current) | Constitution (proposed) |
|---|---|
| Trial-and-error design | Principled architecture |
| "Works on my demo" | "Provably safe in production" |
| Deterministic mental models | Probabilistic-aware engineering |
| No governance | Governance as foundation |
| Prototype-quality | Production-quality |

**[J] This paper is the BRIDGE between our Safety report (01) and enterprise deployment (02).** Governance isn't an add-on — it's the foundation. Build governance FIRST, capabilities SECOND.

### 5. Context Engineering: The Real Skill

The Context Engineering Survey (2507.13334) redefines what matters:

```
Prompt Engineering: "How do I write better prompts?"
                    ↓ (necessary but insufficient)
Context Engineering: "How do I design the entire information 
                     environment the LLM operates in?"
  ├── System instructions (prompts)
  ├── Retrieved context (RAG)
  ├── Memory (episodic, semantic, procedural)
  ├── Tool outputs (MCP results)
  ├── Conversation history (managed, not raw)
  └── Environmental state (task context)
```

**[J] Context Engineering IS what we've been calling "the agent architecture."** It subsumes: RAG design (100-Repo Synthesis), Memory architecture (Report 06), Tool integration (Report 03), Safety policies (Report 01). It's the unifying concept.

---

## Top 10 Papers (Technical Impact)

| Rang | Paper | Warum |
|------|-------|-------|
| 1 | **"Beyond Pipelines"** (2510.16720) | Defines Era 3: Model-Native via RL. |
| 2 | **CoALA** (2309.02427) | THE cognitive architecture reference. |
| 3 | **"Governance-First"** (2510.13857) | Crisis of Craft → Constitution. Production-readiness. |
| 4 | **ADAS** (2408.08435) | Automated agent design. New research area. |
| 5 | **"Inefficiencies of Meta Agents"** (2510.06711) | Evolution > iteration. Ensemble > single. |
| 6 | **W4S** (2504.04785) | Cheap model orchestrates expensive model. Economic. |
| 7 | **"Left Alone"** (2509.21224) | Spontaneous meta-cognitive patterns. Profound. |
| 8 | **Context Engineering** (2507.13334) | Prompt Eng → Context Eng. Unifying concept. |
| 9 | **Talker-Reasoner** (2410.08328) | System-1/2 implemented. Clean architecture. |
| 10 | **Blueprint for Enterprise** (2504.08148) | Enterprise compound AI architecture. |

---

## Cross-Report Connections

| Finding (Report 09) | Connects to | Report |
|---|---|---|
| Pipeline → Model-Native via RL | RL Convergence | Cross |
| Context Engineering | Memory-as-OS, RAG Topology, Skills | 06, 03, 100-Repo |
| Governance-First = Constitution | Safety Architecture, Policy→Guard Code | 01 |
| W4S Weak-for-Strong | EAGLET (small planner + executor) | 05 |
| Meta-agent inefficiencies | Sycophancy (changing correct to wrong) | 07 |
| Spontaneous meta-cognition | Self-Replication, Misalignment | 01 |
| Compound Systems Optimization | Trinity Architecture | Cross |
| SOP-Agent | Procedural Memory, Skills | 06, 03 |
| Developer practices study | Framework failures = 35% (Why They Fail) | 08 |

---

*Confidence: [82% — "Beyond Pipelines" and CoALA are well-established surveys. "Inefficiencies of Meta Agents" is empirically strong (contradicts ADAS hype). W4S is novel but needs broader validation. "Left Alone" (6 models, 18 runs) is fascinating but small-scale. Context Engineering survey is comprehensive. Weakest: Multi-Agent section is abbreviated; would need separate report for full treatment. "Governance-First" is a position paper, not empirically validated.]*

---
*MIIA 🏔️ | Report 09/16 | 2026-02-27*
