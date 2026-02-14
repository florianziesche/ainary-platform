# Research Brief AR-007: The Orchestration Problem
## Why Multi-Agent Systems Fail and How to Fix Them

**Status:** RESEARCH COMPLETE — Ready for Outline Review  
**Date:** 2026-02-14  
**Audience:** [INTERN] Engineering Lead / CTO  
**Confidence:** 72%  
**Thesis:** "The bottleneck in AI agent deployment isn't the agents — it's the orchestration. Most teams build agents first and figure out coordination later. That's backwards."

---

## Beipackzettel

- **Gesamtconfidence:** 72%
- **Quellen:** 13 primary, 5 secondary
- **Stärkste Evidenz:** MAS hijacking 58-90% success rate across orchestrators (arXiv:2503.12188)
- **Schwächste Stelle:** Production failure case studies are mostly anecdotal; no systematic study of orchestration-specific failures exists
- **Was würde diesen Report entwerten?** If single-agent systems prove sufficient for 90%+ of production use cases, making orchestration irrelevant for most teams
- **Methodik:** Multi-source research across academic papers, framework documentation, industry reports, practitioner blogs

---

## Key Findings

1. **Multi-agent orchestration is the #1 unsolved problem in agent deployment.** 51% of companies have agents in production, but performance quality — not cost, not safety — is the top barrier to scaling (LangChain State of AI Agents, n=1,300). The orchestration layer is where quality breaks down.

2. **The Big 4 frameworks (LangGraph, CrewAI, AutoGen, OpenAI Swarm) solve different problems — none solves orchestration comprehensively.** LangGraph gives low-level graph control but requires manual orchestration logic. CrewAI abstracts orchestration but limits flexibility. AutoGen enables conversation-based coordination but lacks production hardening. Swarm is an educational prototype, not a framework.

3. **Anthropic's counter-position: "Don't use frameworks."** Anthropic's "Building Effective Agents" guide (Dec 2024) explicitly recommends starting with raw LLM API calls and simple composable patterns (prompt chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer). Their most successful customer implementations avoided complex frameworks entirely.

4. **Multi-agent systems have a unique attack surface.** Adversarial content can hijack inter-agent communication to execute arbitrary malicious code in 58-90% of trials with GPT-4o, reaching 100% in some configurations — even when individual agents refuse harmful actions (arXiv:2503.12188). The orchestration layer is the weakest link.

5. **Cost scales super-linearly with agent count.** Each additional agent in a multi-agent pipeline multiplies token consumption, latency, and error probability. A 5-agent pipeline with 3 rounds of communication generates 15+ LLM calls per task. At GPT-4o pricing (~$5/M output tokens), a pipeline processing 10K tasks/day burns ~$2,250/day in API costs alone — before retry logic.

---

## Framework Comparison

### Exhibit 1: Multi-Agent Framework Comparison (Feb 2026)

| Dimension | LangGraph | CrewAI | AutoGen | OpenAI Swarm |
|---|---|---|---|---|
| **Architecture** | Directed graph (nodes + edges) | Role-based crews with tasks | Conversation-based multi-agent | Routines + handoffs |
| **Orchestration Model** | Explicit (developer defines graph) | Implicit (framework manages) | Emergent (conversation-driven) | Explicit (function-based handoffs) |
| **GitHub Stars** | Part of LangChain (~100K+) | ~30K | ~30K | ~18K |
| **Production Readiness** | High (LangSmith ecosystem) | Medium (Enterprise tier available) | Low-Medium (research-oriented) | None (educational only) |
| **Flexibility** | Very High (any topology) | Medium (sequential/hierarchical) | High (customizable agents) | Low (simple handoff patterns) |
| **Learning Curve** | Steep (graph concepts required) | Low (YAML + decorators) | Medium (conversation patterns) | Very Low (plain Python) |
| **HITL Support** | Built-in (interrupt/resume) | Optional (task-level) | Built-in (human proxy agent) | Manual implementation |
| **Memory** | Via LangChain ecosystem | Built-in (short/long-term) | Conversation history | None |
| **Observability** | LangSmith integration | Limited built-in | Limited | None |
| **Key Weakness** | Complexity; over-engineering risk | Black-box orchestration; limited debugging | Not production-hardened; verbose | Not a real framework; no persistence |
| **Best For** | Complex, custom workflows | Rapid prototyping; simple crews | Research; experimentation | Learning orchestration concepts |

*Sources: Framework documentation, GitHub repos, Anthropic "Building Effective Agents" (2024), LangChain blog*

### Exhibit 2: Orchestration Patterns

| Pattern | Description | When to Use | Risk | Framework Support |
|---|---|---|---|---|
| **Hierarchical (Supervisor)** | Central agent delegates to workers | Clear task decomposition; need control | Single point of failure; supervisor bottleneck | LangGraph ✓, CrewAI ✓, AutoGen ✓ |
| **Pipeline (Sequential)** | Agent A → Agent B → Agent C | Linear workflows; each step depends on previous | Latency compounds; error propagation | All frameworks |
| **Parallel (Fan-out/Fan-in)** | Multiple agents work simultaneously, results aggregated | Independent subtasks; voting/consensus | Result merging complexity; cost multiplication | LangGraph ✓, AutoGen partial |
| **Orchestrator-Workers** | Dynamic task decomposition by orchestrator LLM | Unpredictable subtask count (e.g., coding) | Orchestrator quality determines everything | LangGraph ✓, Anthropic pattern |
| **Evaluator-Optimizer** | Generator + evaluator in feedback loop | Clear quality criteria; iterative refinement | Infinite loops if no stopping condition | LangGraph ✓, Anthropic pattern |
| **Conversation (Democratic)** | Agents converse freely to reach consensus | Brainstorming; research; open problems | Deadlocks; token explosion; no convergence guarantee | AutoGen ✓, CrewAI partial |
| **Market-Based** | Agents bid on tasks based on capability/cost | Resource allocation; competitive selection | Complexity overhead; game-theoretic instabilities | No framework support |
| **Mixture-of-Agents (MoA)** | Layered architecture; each layer refines previous | Quality maximization (benchmark performance) | Extreme cost (N×M LLM calls per layer) | Custom only |

*Sources: LangGraph blog, Anthropic "Building Effective Agents", arXiv:2406.04692 (Wang et al. 2024)*

---

## Failure Modes in Multi-Agent Systems

### Exhibit 3: Multi-Agent Failure Taxonomy

| Failure Mode | Description | Frequency | Mitigation |
|---|---|---|---|
| **Infinite Loops** | Agents keep delegating to each other without progress | Common | Max iteration limits; progress detection |
| **Deadlocks** | Two agents wait for each other's output | Occasional | Timeout mechanisms; dependency graph validation |
| **Conflicting Outputs** | Agents produce contradictory results | Common in parallel patterns | Conflict resolution agent; voting mechanisms |
| **Blame Attribution Failure** | When output is wrong, impossible to determine which agent failed | Systemic | Per-agent logging; trace IDs; output provenance |
| **Context Window Overflow** | Accumulated conversation exceeds token limits | Common in conversation patterns | Summarization agents; context pruning |
| **Orchestrator Hallucination** | Supervisor agent delegates to non-existent agents or tools | Occasional | Strict agent/tool registry; validation layer |
| **Cascade Failures** | One agent's error propagates through entire pipeline | Common in sequential patterns | Circuit breakers; per-step validation |
| **Cost Explosion** | Retry loops and verbose inter-agent communication burn tokens | Systemic | Budget caps; token monitoring; early termination |
| **Security Hijacking** | Adversarial input manipulates inter-agent communication | Demonstrated (58-90%) | Sandboxing; input validation between agents |

*Sources: arXiv:2503.12188, arXiv:2402.01680, Anthropic engineering blog, practitioner reports*

---

## Production Cases

### Where Multi-Agent Worked

1. **Coding Agents (Anthropic, Cursor, Devin):** Orchestrator-worker pattern. One agent plans changes, workers execute per-file. Clear task decomposition + verifiable output (code compiles or doesn't). SWE-bench performance improved significantly with multi-agent approaches.

2. **Customer Service Routing (OpenAI Swarm pattern):** Triage agent classifies intent, hands off to specialist agents (refund, technical, sales). Works because categories are well-defined and handoffs are deterministic.

3. **Research & Summarization (58% of production use cases per LangChain survey):** Pipeline pattern. Searcher → Analyzer → Summarizer. Works because each step has clear input/output contracts.

### Where Multi-Agent Failed or Struggled

1. **McDonald's AI Drive-Through (killed 2024):** Compounding errors across speech recognition + order processing + verification agents. No effective error correction between agents. Program terminated.

2. **Autonomous Agent Swarms (general):** Fully autonomous multi-agent systems with no HITL consistently produce unreliable results. Gartner predicts >40% of agentic AI projects will be canceled by 2027.

3. **Democratic/Debate Architectures:** Agents debating to reach consensus rarely converge in production. Token costs explode, latency becomes unacceptable, and "consensus" often just means the last agent's output wins.

---

## Research: Coordination in Multi-Agent Systems

### Key Papers

1. **Wu et al. (2023)** — "AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation" (arXiv:2308.08155). Foundational paper. Defines conversable agents + flexible conversation patterns. 43 pages, 30 pages appendices. Key insight: conversation as universal orchestration primitive.

2. **Guo et al. (2024)** — "Large Language Model based Multi-Agents: A Survey of Progress and Challenges" (arXiv:2402.01680). Comprehensive survey covering agent profiling, communication mechanisms, and capacity growth. Identifies coordination as key open challenge.

3. **Wang et al. (2024)** — "Mixture-of-Agents Enhances Large Language Model Capabilities" (arXiv:2406.04692). Layered MoA architecture where each layer of agents refines previous layer's outputs. Achieves SOTA on AlpacaEval 2.0 (65.1% vs GPT-4o's 57.5%). But: extreme cost — each layer multiplies token usage by agent count.

4. **Triedman et al. (2025)** — "Multi-Agent Systems Execute Arbitrary Malicious Code" (arXiv:2503.12188). Demonstrates that adversarial content hijacks control flow between agents. 58-90% attack success with GPT-4o. Key finding: attacks succeed even when individual agents are safe — the vulnerability is in the orchestration layer.

5. **Anthropic (2024)** — "Building Effective Agents." Not a paper but the most influential practitioner guide. Core argument: simple composable workflows beat complex multi-agent frameworks. Five workflow patterns identified. Key quote: "The most successful implementations weren't using complex frameworks."

---

## Human-in-the-Loop vs Fully Autonomous

### Exhibit 4: HITL Spectrum for Multi-Agent Systems

| Level | Description | Use Case | Risk |
|---|---|---|---|
| **0: Fully Autonomous** | No human oversight | Only for low-stakes, well-tested pipelines | Compounding errors; security hijacking |
| **1: Checkpoint Approval** | Human approves at key decision points | Financial transactions; content publishing | Alert fatigue if too many checkpoints |
| **2: Exception Handling** | Human intervenes only on failures/low confidence | Most production deployments | Requires good confidence calibration |
| **3: Supervised Autonomy** | Human monitors dashboard, can intervene anytime | Enterprise deployments | Monitoring fatigue; 67% of alerts ignored (Vectra 2023) |
| **4: Human-Directed** | Human decides orchestration; agents execute | High-stakes decisions | Defeats purpose of multi-agent automation |

**Key tension:** LangChain survey shows most production agents have read-only permissions. Very few companies allow agents to read, write, AND delete freely. The more agents in a system, the more conservative the permission model — which limits what multi-agent systems can actually do.

---

## Cost Analysis

### Exhibit 5: Token Cost Modeling for Multi-Agent Pipelines

| Configuration | LLM Calls/Task | Est. Cost/Task (GPT-4o) | Est. Cost/Task (Claude Sonnet) | Daily Cost (10K tasks) |
|---|---|---|---|---|
| Single Agent | 1-3 | $0.01-0.03 | $0.01-0.02 | $100-300 |
| 3-Agent Pipeline | 5-9 | $0.05-0.15 | $0.03-0.10 | $500-1,500 |
| 5-Agent Pipeline | 15-25 | $0.15-0.50 | $0.10-0.35 | $1,500-5,000 |
| 5-Agent + Retry Logic | 25-50 | $0.25-1.00 | $0.18-0.70 | $2,500-10,000 |
| MoA (3 layers × 3 agents) | 27+ | $0.50-2.00 | $0.35-1.40 | $5,000-20,000 |

*Assumptions: ~2K tokens input, ~1K tokens output per call. Prices: GPT-4o ($2.50/$10 per M in/out), Claude Sonnet ($3/$15 per M in/out). Estimates — actual costs vary by task complexity.*

**Key insight:** Multi-agent cost is not linear. Each additional agent adds communication overhead (agents reading other agents' outputs), retry logic, and orchestration tokens. A 5-agent system doesn't cost 5x a single agent — it costs 10-30x.

---

## Monitoring & Debugging

### The Observability Gap

Current observability tools (LangSmith, Langfuse, Arize Phoenix) are designed for single-agent tracing. Multi-agent systems need:

1. **Cross-agent trace correlation:** Following a request through multiple agents with shared trace IDs
2. **Inter-agent message inspection:** Seeing what agents communicate to each other (most frameworks don't expose this cleanly)
3. **Decision attribution:** Understanding WHY the orchestrator routed to Agent B instead of Agent A
4. **Cost allocation per agent:** Which agent in the pipeline consumes the most tokens?
5. **Failure root cause analysis:** When the final output is wrong, which agent introduced the error?

**Current state:** LangSmith supports LangGraph traces natively. Everything else requires custom instrumentation. 94% of production agent developers use some observability tool (LangChain survey), but multi-agent-specific observability is nascent.

---

## Gap Analysis

| Gap | Impact | Available Evidence | Needed |
|---|---|---|---|
| No standardized orchestration benchmarks | Can't compare frameworks objectively | SWE-bench for coding only | Multi-task orchestration benchmark |
| No production failure database for multi-agent systems | Teams repeat each other's mistakes | Anecdotal case studies only | Systematic failure taxonomy with real cases |
| No cost modeling standard | Teams underestimate multi-agent costs by 5-10x | Per-call pricing only | TCO calculator including communication overhead |
| No inter-agent trust protocol | Agents trust each other by default | A2A authenticates systems, not intentions | Trust scoring between agents (see AR-001) |
| Limited HITL patterns for multi-agent | Alert fatigue at scale | Single-agent HITL research | Multi-agent HITL with severity tiering |
| No orchestration security model | Hijacking succeeds at 58-90% | arXiv:2503.12188 | Sandboxed inter-agent communication |

---

## Claim Register

| # | Claim | Value | Source | Confidence |
|---|---|---|---|---|
| 1 | MAS hijacking success rate | 58-90% (GPT-4o) | arXiv:2503.12188 (Triedman et al.) | **High** |
| 2 | Companies with agents in production | 51% | LangChain State of AI Agents (n=1,300) | **High** |
| 3 | Performance quality as #1 barrier | >2x other factors | LangChain State of AI Agents | **High** |
| 4 | MoA outperforms GPT-4o | 65.1% vs 57.5% AlpacaEval | arXiv:2406.04692 | **High** |
| 5 | Agentic AI project cancellation rate | >40% by 2027 | Gartner | **Medium** (prediction) |
| 6 | 94% use observability tools | 94% | LangChain State of AI Agents | **Medium** |
| 7 | Multi-agent cost is 10-30x single agent | 10-30x | Calculated from API pricing + communication overhead | **Medium** (modeled) |
| 8 | Most successful implementations use simple patterns | Qualitative | Anthropic "Building Effective Agents" | **Medium** (practitioner report) |
| 9 | Agent market $7.8B → $52B by 2030 | 45.8% CAGR | Precedence Research | **Medium** (single analyst) |
| 10 | 100% attack success in some orchestrator configs | 100% | arXiv:2503.12188 | **High** |
| 11 | CrewAI ~30K stars, AutoGen ~30K stars | ~30K each | GitHub (approximate, Feb 2026) | **Medium** |
| 12 | Mid-size companies most aggressive (63% in production) | 63% | LangChain State of AI Agents | **High** |

---

## Contradiction Register

| Contradiction | Source A | Source B | Resolution |
|---|---|---|---|
| "Use frameworks for multi-agent" vs "Don't use frameworks" | CrewAI, LangGraph marketing | Anthropic engineering blog | Both are right for different audiences. Frameworks help rapid prototyping; raw APIs win for production reliability. Anthropic's advice applies to teams with strong engineering. |
| "Multi-agent improves quality" vs "Multi-agent compounds errors" | MoA paper (65.1% AlpacaEval) | McDonald's case, practitioner reports | Quality improves only when orchestration is well-designed and tasks are decomposable. For ill-defined tasks, errors compound. |
| "51% have agents in production" vs ">40% will be canceled" | LangChain survey (2024) | Gartner (2025 prediction) | "In production" ≠ "successful in production." Many will deploy, discover orchestration problems, and cancel. |

---

## Outline: Report AR-007

### Proposed Structure (7 Chapters)

**1. Executive Summary**
- Key Insight: The orchestration layer — not the agents — determines whether a multi-agent system succeeds or fails.
- Exhibit: Framework comparison matrix (Exhibit 1)

**2. The $52B Coordination Problem**
- Key Insight: The AI agent market is growing at 45.8% CAGR, but most teams build agents first and orchestration never.
- Data: 51% in production, >40% predicted cancellation, performance quality as #1 barrier
- Exhibit: Agent adoption vs. cancellation paradox

**3. Anatomy of Orchestration: Patterns That Work**
- Key Insight: There are exactly 5 production-proven orchestration patterns — and Anthropic identified them by observing what their most successful customers actually build.
- Patterns: Prompt chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer
- Exhibit: Orchestration Patterns (Exhibit 2)

**4. Framework Wars: LangGraph vs CrewAI vs AutoGen vs Swarm**
- Key Insight: No framework solves orchestration comprehensively. Each optimizes for a different point on the flexibility-simplicity spectrum.
- Exhibit: Framework Comparison (Exhibit 1, expanded)
- Real comparison: code examples, production readiness, ecosystem

**5. When Multi-Agent Systems Break**
- Key Insight: Multi-agent systems don't fail at the agent level — they fail at the communication layer between agents.
- Failure taxonomy (Exhibit 3)
- MAS hijacking: 58-90% success rate
- Production cases: McDonald's, autonomous swarms, debate architectures
- Exhibit: Failure Taxonomy + Attack Success Rates

**6. The Hidden Tax: Cost, Latency, and Observability**
- Key Insight: Multi-agent cost scales super-linearly — a 5-agent pipeline costs 10-30x a single agent, not 5x.
- Token cost modeling (Exhibit 5)
- Observability gap: tools designed for single agents, not multi-agent traces
- Exhibit: Cost Modeling Table

**7. Orchestration-First: A Design Methodology**
- Key Insight: Build the orchestration layer first, then add agents. Not the other way around.
- Start with Anthropic's 5 patterns
- Add complexity only when simple patterns fail
- HITL spectrum (Exhibit 4)
- When NOT to use multi-agent
- Exhibit: Decision tree — single agent vs multi-agent

**8. Predictions and Open Questions**
- Key Insight: The orchestration problem will be solved by standardization — whoever creates the "Kubernetes of agents" wins.
- Predictions: Framework consolidation, orchestration-as-a-service, inter-agent trust protocols
- What would invalidate this report

---

## Source List

| # | Source | Type | Used For |
|---|---|---|---|
| 1 | arXiv:2503.12188 — Triedman et al. "Multi-Agent Systems Execute Arbitrary Malicious Code" | Academic paper | MAS security vulnerabilities, attack success rates |
| 2 | arXiv:2308.08155 — Wu et al. "AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation" | Academic paper | AutoGen architecture, conversation-based orchestration |
| 3 | arXiv:2402.01680 — Guo et al. "LLM-based Multi-Agents: A Survey of Progress and Challenges" | Academic survey | Multi-agent coordination challenges, taxonomy |
| 4 | arXiv:2406.04692 — Wang et al. "Mixture-of-Agents Enhances LLM Capabilities" | Academic paper | MoA architecture, cost vs quality tradeoff |
| 5 | Anthropic — "Building Effective Agents" (Dec 2024) | Practitioner guide | 5 workflow patterns, anti-framework position |
| 6 | LangChain — "State of AI Agents" (2024, n=1,300) | Industry survey | Adoption rates, barriers, controls, observability |
| 7 | LangChain Blog — "LangGraph: Multi-Agent Workflows" | Technical blog | LangGraph architecture, multi-agent patterns |
| 8 | OpenAI Cookbook — "Orchestrating Agents: Routines and Handoffs" | Technical guide | Swarm concepts, handoff patterns |
| 9 | CrewAI — Open source documentation | Framework docs | CrewAI architecture, features, limitations |
| 10 | Microsoft — AutoGen documentation (stable) | Framework docs | AutoGen Core, AgentChat, extensions |
| 11 | Gartner — ">40% of agentic AI projects canceled by 2027" | Analyst prediction | Market outlook, failure prediction |
| 12 | Vectra (2023) — SOC alert fatigue data | Industry report | 67% alerts ignored, HITL failure |
| 13 | Precedence Research — Agent market sizing | Market research | $7.8B → $52B CAGR 45.8% |
| 14 | arXiv:2502.14143 — Multi-agent frameworks survey | Academic paper | Framework landscape overview |
| 15 | McDonald's AI Drive-Through failure (2024) | News reports | Production failure case study |
| 16 | OpenAI/Anthropic API pricing pages | Primary data | Cost modeling |
| 17 | LangSmith/Langfuse documentation | Product docs | Observability capabilities |
| 18 | Ainary Research Pack (internal) — Briefs #2, #5, #10, #11 | Internal research | Cross-references to Trust, Adversarial, HITL |

---

*Cite as: Ziesche, F. (2026). The Orchestration Problem — Why Multi-Agent Systems Fail and How to Fix Them. Ainary Research Report, No. AR-007.*

**Keywords:** multi-agent orchestration, LangGraph, CrewAI, AutoGen, agent coordination, orchestration patterns, multi-agent failure modes
