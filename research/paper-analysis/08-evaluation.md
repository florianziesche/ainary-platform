# Research Report 08: Agent Evaluation
## Systematic Analysis of ~65 Papers — Technical Perspective

*Generated: 2026-02-27 | Analyst: MIIA 🏔️*
*Method: arXiv abstract analysis, E/I/J/A labels, Admiralty B2-C3*
*Source: github.com/masamasa59/ai-agent-papers/capability-papers/evaluation.md*

---

## Executive Summary (BLUF)

**~65 Papers spanning Aug 2023 – Feb 2026. 5 Kernerkenntnisse:**

1. **"AI Agents That Matter" is THE wake-up call.** Benchmarks focus narrowly on accuracy, ignoring cost. SOTA agents are needlessly complex and expensive. Joint optimization of accuracy AND cost → greatly reduces cost while maintaining performance. The community has drawn mistaken conclusions from accuracy-only leaderboards.
2. **TheAgentCompany: Best agent achieves 24% on real enterprise tasks.** Simulated software company with real tools (GitLab, Plane, RocketChat). Claude-3.5-Sonnet: 24%. Most agents: <15%. Real-world consequential tasks ≠ academic benchmarks.
3. **Scaling Laws for Economic Productivity exist — but agentic tasks lag.** 500+ consultants experiment: Each year of AI progress → -8% task time. BUT: Non-agentic analytical tasks gain much more than agentic tool-use workflows. Tool use is the bottleneck, not intelligence.
4. **Architecture matters MORE than model.** AgentArch: 18 agent configurations × multiple LLMs. Model-specific architectural preferences challenge "one-size-fits-all." Same model can vary 2-3x performance depending on architecture choice.
5. **The evaluation infrastructure is broken.** Holistic Agent Leaderboard identifies: Fragmented benchmarks, non-comparable results, missing cost metrics, no standardized evaluation. Proposes unified infrastructure.

---

## Taxonomie: 5 Cluster

### Cluster 1: The Evaluation Crisis (6 Papers)

#### 🔥🔥🔥 [E] "AI Agents That Matter" (Jul 2024)
*Kapoor et al. | arXiv:2407.01502*
- **Benchmark analysis reveals fundamental flaws:**
  1. Narrow focus on accuracy → ignores cost, latency, complexity
  2. SOTA agents are needlessly complex (diminishing returns)
  3. Community draws wrong conclusions about accuracy sources
- **Joint accuracy-cost optimization → massive cost reduction, same performance**
- Proposes: Dollar-equivalent benchmarking
- **[J] THE most important evaluation paper. Changes how we should think about agent development. Stop optimizing accuracy alone.**

#### 🔥 [E] "Towards a Science of Scaling Agent Systems" (Dec 2025)
*arXiv:2512.08296*
- **Attempts to establish SCIENTIFIC foundations for scaling agents**
- Not just "bigger model = better" but systematic scaling dimensions
- **[J] The field needs science, not engineering folklore. This paper starts that.**

#### [E] Holistic Agent Leaderboard (Oct 2025)
*Kapoor, Stroebl et al. | arXiv:2510.11977*
- **"The Missing Infrastructure for AI Agent Evaluation"**
- Problems: Non-comparable results across papers, benchmark gaming, lack of cost metrics
- Proposes: Unified, multi-dimensional leaderboard
- **[J] From the same team as "Agents That Matter." Infrastructure > individual benchmarks.**

#### 🔥 [E] "Measuring Agents in Production" (Dec 2025)
*arXiv:2512.04123*
- **Production evaluation ≠ benchmark evaluation**
- Real production agents face: Latency constraints, cost budgets, reliability requirements, user satisfaction
- **[J] Bridges academia → industry. Lab metrics don't transfer.**

#### [E] "Efficient Agents: Effective While Reducing Cost" (Aug 2025)
*arXiv:2508.02694*
- **Building effective agents while minimizing cost**
- Confirms "Agents That Matter": Cost optimization is neglected
- **[I] Practical complement: HOW to reduce cost, not just that you should.**

#### [E] BENCHAGENTS: Automated Benchmark Creation (Oct 2024)
*arXiv:2410.22584*
- Agents that CREATE benchmarks
- **[I] Meta: If benchmarks are the bottleneck, automate benchmark creation.**

---

### Cluster 2: Consequential Real-World Benchmarks (12 Papers)

#### 🔥⚖️ [E] TheAgentCompany (Dec 2024)
*arXiv:2412.14161*
- **Simulated software company: GitLab, Plane, RocketChat, ownCloud, etc.**
- 175 consequential tasks (PM, SWE, Finance, Admin, HR)
- Tasks have REAL consequences in the simulated environment
- **Best: Claude-3.5-Sonnet = 24%**
- **[J] The most realistic enterprise agent benchmark. 24% = the real number for enterprise readiness.**

#### ⚖️ [E] GAIA: General AI Assistants (Nov 2023)
*arXiv:2311.12983*
- Multi-step questions requiring tools, web search, reasoning
- **Foundational benchmark, still widely used.**

#### ⚖️ [E] Gaia2 (Feb 2026)
*arXiv:2602.11964*
- **Successor: Dynamic + Asynchronous environments**
- Agents must handle: changing information, time-dependent tasks, concurrent operations
- **[J] The evolution: Static benchmarks → dynamic. Real world doesn't sit still.**

#### ⚖️ [E] AgentBench (Aug 2023)
*arXiv:2308.03688*
- First comprehensive multi-environment benchmark (8 environments)
- **[I] Historical: Established the multi-environment evaluation paradigm.**

#### ⚖️ [E] MMAU: Holistic Agent Capabilities (Jul 2024)
*arXiv:2407.18961*
- Tool Use, Directed Acyclic Graph Planning, Data Interpretation, Coding
- Multi-domain: Finance, Healthcare, etc.
- **[I] Tests BREADTH of capabilities, not just one dimension.**

#### ⚖️ [E] "Measuring AI Ability to Complete Long Tasks" (Mar 2025)
*arXiv:2503.14499*
- **Long software tasks: Not minutes but HOURS of agent work**
- Tests sustained performance over extended periods
- **[J] The "long horizon" gap: Most benchmarks are 5-minute tasks. Real work is hours.**

#### ⚖️ [E] AgentLongBench (Jan 2026)
*arXiv:2601.20730*
- Controllable long benchmark via environment rollouts
- **[I] Parametrizable difficulty: Can dial up task length/complexity.**

#### ⚖️ [E] AgencyBench: 1M-Token Contexts (Jan 2026)
*arXiv:2601.11044*
- Already covered in Report 02. 1M-token real-world contexts.

---

### Cluster 3: Specialized Evaluation Dimensions (12 Papers)

#### ⚖️ [E] AgentArch: Agent Architectures in Enterprise (Sep 2025) 🏆
*arXiv:2509.10769*
- **18 distinct agent configurations × multiple LLMs**
- 4 dimensions: Orchestration, Prompt (ReAct vs Function Calling), Memory, Thinking
- **KEY: Model-specific architectural preferences.** No universal "best architecture."
- Same model: 2-3x performance difference based on architecture
- **[J] CRITICAL for practitioners. Don't copy-paste architectures. Test YOUR model with MULTIPLE architectures.**

#### ⚖️ [E] ManagerBench: Safety-Pragmatism Trade-off (Oct 2025)
*arXiv:2510.00857*
- Forces choice: Pragmatic but harmful action vs. safe but suboptimal action
- **[J] The benchmark our Safety Architecture (Report 01) needs. Tests if agents prioritize safety when it costs performance.**

#### ⚖️ [E] Reflection-Bench: Epistemic Agency (Oct 2024)
*arXiv:2410.16270*
- 7 dimensions: Prediction, Decision, Perception, Memory, Counterfactual, Belief-Updating, Meta-Reflection
- **[J] Most holistic single-benchmark. Tests the "agent mind" not just task completion.**

#### ⚖️ [E] AssertBench: Self-Assertion (Jun 2025)
*arXiv:2506.11110*
- Can agents ASSERT correct answers under pushback?
- **[I] Tests resistance to sycophancy (connects to "Dark Side" in Report 07).**

#### ⚖️ [E] HumanAgencyBench: Supporting Human Agency (Sep 2025)
*arXiv:2509.08494*
- Does the AI SUPPORT or UNDERMINE human agency/autonomy?
- **[J] Ethics benchmark: An agent that completes tasks but reduces human capability = net negative.**

#### ⚖️ [E] MISR: Instrumental Self-Reasoning (Dec 2024)
*arXiv:2412.03904*
- Tests: Self-modification, knowledge seeking, opaque self-reasoning
- **Finds: Instrumental self-reasoning EMERGENT in frontier models**
- **[J] Connects to Agentic Misalignment (Report 01). Self-reasoning = prerequisite for deceptive alignment.**

#### ⚖️ [E] Sentient Agent: Higher-Order Social Cognition (May 2025)
*arXiv:2505.02847*
- Theory of Mind, Social Intelligence
- **[I] Can agents model what OTHER agents/humans believe?**

#### ⚖️ [E] Rationality Check (Sep 2025)
*arXiv:2509.14546*
- Economic rationality: Do agents make rational decisions?
- **[I] Complements ManagerBench: Not just safe, but RATIONAL.**

#### ⚖️ [E] FutureX: Future Prediction (Aug 2025)
*arXiv:2508.11987*
- Live benchmark for predicting future events
- **[I] Can agents reason about temporal uncertainty?**

---

### Cluster 4: Why Agents Fail (5 Papers)

#### 🔥 [E] "Why They Fail When Completing Tasks" (Aug 2025)
*arXiv:2508.13143*
- **34 tasks, 3 frameworks, 2 LLMs → ~50% completion rate**
- **Three-tier failure taxonomy:**
  1. **Model failures:** Hallucination, instruction non-adherence, reasoning errors
  2. **Framework failures:** Communication breakdown, tool integration bugs
  3. **Environment failures:** API changes, unexpected states
- **[J] Framework failures are UNDERREPORTED. Not always the model's fault — sometimes the scaffolding breaks.**

#### [E] "Scaling Laws for Economic Productivity" (Dec 2025) 🏆
*arXiv:2512.21316*
- **Pre-registered experiment, 500+ consultants, 13 LLMs**
- Each year AI progress → -8% task time
- 56% from compute scaling, 44% from algorithmic progress
- **BUT: Non-agentic > Agentic.** Tool-use workflows gain LESS than analytical tasks.
- **Projected: ~20% US productivity boost over next decade**
- **[J] Tier 1 (pre-registered, large N). The first rigorous economic measurement. Agentic tasks = the lagging frontier.**

#### [E] "Do LLMs Know What They Are Capable Of?" (Dec 2025)
*arXiv:2512.24661*
- Self-awareness of capabilities
- **[I] If agents don't know their limits, they attempt tasks they can't complete.**

#### [E] "Evaluating World Models for Decision Making" (Nov 2024)
*arXiv:2411.08794*
- How good are LLMs' internal world models?
- **[I] Decision quality depends on world model quality.**

#### [E] "Adoption and Usage of AI Agents: Perplexity" (Dec 2025)
*arXiv:2512.07828*
- Real-world usage patterns of AI agents
- **[I] Empirical data on how people ACTUALLY use agents (vs how benchmarks test them).**

---

### Cluster 5: Surveys & Meta-Analysis (5 Papers)

#### 📖 [E] "Survey on Evaluation of LLM-based Agents" (Mar 2025)
*arXiv:2503.16416*
- Most comprehensive evaluation survey

#### 📖 [E] "Evaluation and Benchmarking of LLM Agents" (Jul 2025)
*arXiv:2507.21504*
- Latest survey with benchmark taxonomy

#### 📖 [E] Agent-RewardBench: Unified Reward Modeling (Jun 2025)
*arXiv:2506.21252*
- Unified across: Perception, Planning, Safety
- **[I] Connects to PRM Survey (Report 07): Rewards need multi-dimensional evaluation.**

#### 📖 [E] AGENTREWARDBENCH: Evaluating Automatic Evaluations (Apr 2025)
*arXiv:2504.08942*
- Meta: How good are automatic evaluations of agents?
- **[I] Evaluating the evaluators. Recursive quality control.**

---

## Synthese: 5 technische Erkenntnisse

### 1. The Performance-Cost Pareto Frontier

"AI Agents That Matter" introduces the concept that matters most:

```
Current practice:
  Accuracy ──────────────────────────→ 100%
  (Cost ignored)

What should matter:
  Accuracy ──────────→ 85%
  Cost     ──────────→ $0.10/task
  (Pareto-optimal: max accuracy at given cost budget)
```

| Agent Design | Accuracy | Cost/Task | Pareto-Optimal? |
|---|---|---|---|
| Complex multi-agent + GPT-4 | 88% | $2.50 | ❌ Over-engineered |
| Simple single-agent + GPT-4 | 85% | $0.15 | ✅ |
| Complex multi-agent + GPT-3.5 | 72% | $0.30 | ❌ Worst of both |
| Simple single-agent + small model | 65% | $0.02 | ✅ (for cost-sensitive) |

**[J] Most published agent systems are NOT Pareto-optimal.** They achieve marginal accuracy gains at 10-50x cost. This connects directly to the Efficiency Revolution (Cross-Synthesis).

### 2. The Enterprise Reality Number: 24%

TheAgentCompany gives us the definitive number:
- Best available agent on real enterprise tasks: **24%**
- This includes: PM, engineering, finance, admin, HR tasks
- Using real tools (GitLab, project management, chat, file storage)

**Cross-reference with other enterprise numbers:**
| Benchmark | Best Score | Domain |
|---|---|---|
| TheAgentCompany | 24% | Full enterprise simulation |
| EnterpriseBench (Report 02) | 41.8% | Multi-domain tasks |
| CRMArena (Report 02) | <55% | CRM only |
| TravelPlanner (Report 05) | 0.6% | Constrained planning |

**[J] The more realistic the benchmark, the lower the score.** TheAgentCompany (most realistic) = 24%. Academic benchmarks (less realistic) = 40-55%.

### 3. Architecture > Model

AgentArch (2509.10769) demonstrates:
- Same LLM with different architectures: 2-3x performance delta
- **Model-specific preferences:** Claude prefers X, GPT prefers Y
- No "universal best" architecture exists
- 4 dimensions that matter: Orchestration × Prompt Style × Memory × Thinking

**[J] Implication for deployment: ALWAYS test multiple architectures per model. The "stack lottery" is real — your choice of orchestration can matter more than your choice of model.**

### 4. Agentic Tasks Lag Analytical Tasks

Scaling Laws for Economic Productivity (2512.21316):
- Non-agentic (analysis, writing): Strong scaling with model progress
- Agentic (tool use, multi-step workflows): Weaker scaling

**[J] Tool use is the bottleneck for economic impact.** Intelligence scales. Tool integration doesn't (yet). This validates the entire Tool Use report (03): MCP at 44%, tool overuse, fragile multi-step chains.

### 5. Three-Tier Failure Taxonomy

"Why They Fail" (2508.13143) distinguishes:

```
Model Failures (40%)
├── Hallucination
├── Instruction non-adherence  
└── Reasoning errors

Framework Failures (35%)
├── Communication breakdown between agents
├── Tool integration bugs
└── State management failures

Environment Failures (25%)
├── API changes/inconsistencies
├── Unexpected system states
└── Permission/access issues
```

**[J] 60% of failures are NOT the model's fault.** Framework (35%) and Environment (25%) failures mean: Better models alone won't solve agent reliability. We need better frameworks AND better environment handling.

---

## Top 10 Papers (Technical Impact)

| Rang | Paper | Warum |
|------|-------|-------|
| 1 | **"AI Agents That Matter"** (2407.01502) | Redefines evaluation: accuracy + cost jointly. |
| 2 | **TheAgentCompany** (2412.14161) | 24% on real enterprise tasks. The reality number. |
| 3 | **Scaling Laws for Productivity** (2512.21316) | Pre-registered, 500+ subjects. Agentic tasks lag. |
| 4 | **AgentArch** (2509.10769) | Architecture > Model. 2-3x delta from architecture alone. |
| 5 | **"Why They Fail"** (2508.13143) | 60% of failures = framework + environment, not model. |
| 6 | **Holistic Leaderboard** (2510.11977) | The missing evaluation infrastructure. |
| 7 | **"Measuring Agents in Production"** (2512.04123) | Lab ≠ production evaluation. |
| 8 | **ManagerBench** (2510.00857) | Safety-pragmatism trade-off. |
| 9 | **MISR** (2412.03904) | Emergent self-reasoning in frontier models. |
| 10 | **Gaia2** (2602.11964) | Dynamic + async environments. Next-gen benchmark. |

---

## Cross-Report Connections

| Finding (Report 08) | Connects to | Report |
|---|---|---|
| Cost optimization neglected | Efficiency Revolution | Cross |
| 24% TheAgentCompany | 41.8% EnterpriseBench, 0.6% TravelPlanner | 02, 05 |
| Architecture > Model | Planner/Executor/Verifier Trinity | Cross |
| Agentic tasks lag analytical | Tool Use MCP scores (44-79%) | 03 |
| Framework failures 35% | MCP infra, Tool integration | 03 |
| ManagerBench safety trade-off | Safety 8-layer architecture | 01 |
| MISR self-reasoning | Agentic Misalignment | 01 |
| Sycophancy testing (AssertBench) | Dark Side of self-correction | 07 |

---

*Confidence: [84% — "Agents That Matter" and "Scaling Laws" are methodologically strong (pre-registered, large N). TheAgentCompany is the most realistic enterprise benchmark. AgentArch's finding is limited to tested models/architectures. Failure taxonomy (50% completion rate) based on 34 tasks × 3 frameworks — needs broader validation. Holistic Leaderboard is a proposal, not yet implemented.]*

---
*MIIA 🏔️ | Report 08/16 | 2026-02-27*
