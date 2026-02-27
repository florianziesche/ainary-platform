# Cross-Synthesis & Reflection: Reports 01–05
## 302 Papers, 5 Categories — What the Field Actually Says

*Generated: 2026-02-27 | Analyst: MIIA 🏔️*
*Basis: Safety (65), Enterprise (19), Tool Use (88), Reasoning (86), Planning (44)*

---

## Part 1: The 7 Meta-Patterns Nobody Talks About

### Meta-Pattern 1: The Verification Thesis

**Every single domain converges on the same conclusion: LLMs need external verification.**

| Domain | Evidence | Verification Solution |
|---|---|---|
| Safety | No agent >60% safe (Agent-SafetyBench) | Guard Agent, Mutation-Gating, Policy→Guard Code |
| Enterprise | 41.8% task completion (EnterpriseBench) | Dual-Agent (Generator + Critic), Planner-Executor-Evaluator |
| Tool Use | Claude 79%, GPT-5 44% on MCP tasks | ToolFuzz, Input Reformulation, Meta-tools |
| Reasoning | TTS increases hallucinations on knowledge tasks | Self-Consistency, Verifier Models, RAG |
| Planning | 0.6% success on TravelPlanner | LLM-Modulo (External Verifier), Constraint Solvers |

**[J] The Verification Thesis:** Autonomous AI agent performance is bounded not by the model's generative capability, but by the absence of verification. Every +10% improvement in verification → exponentially fewer cascading errors (per the compound effect: p^n).

This is NOT the same as "make bigger models." It's: **make verification systems for current models.**

The field is overinvesting in generation (bigger models, longer thinking, more RL) and underinvesting in verification (constraint checkers, formal methods, Guard Agents, symbolic solvers).

**Ratio in papers:**
- Generation/Training focused: ~250 of 302 papers (~83%)
- Verification focused: ~30 of 302 papers (~10%)
- Both: ~22 papers (~7%)

The 10% that focus on verification (TrustAgent, GuardAgent, GoEX, SABER, LLM-Modulo, Dual-Agent patterns) consistently show the HIGHEST practical impact.

---

### Meta-Pattern 2: The Efficiency Revolution

**The best results across ALL domains come from doing LESS, not MORE.**

| Domain | "Less is More" Finding | Paper |
|---|---|---|
| Tool Use | -24% tool calls → +37% performance | SMART |
| Tool Use | Meta-tools: -11.9% LLM calls → +4.2pp success | Meta-tools |
| Reasoning | NoThinking > Thinking at equal budget | "Reasoning Without Thinking" |
| Reasoning | o3 thinks HARDER not LONGER | o3 analysis |
| Planning | Plan-first -64% tokens vs ReAct | ReWOO |
| Safety | Only mutating actions need checks (92-96%) | SABER |
| Enterprise | 12x speedup via non-destructive agents first | Agents-as-Judge |

**[J] The Efficiency Revolution:** The 2023-2024 era was "throw more compute at it." The 2025-2026 era is "do less, do it right." This is a fundamental paradigm shift:

```
2023: Bigger model + longer CoT + more tools = better
2025: Smaller model + metacognition + selective action = better
```

Nemotron 7B (with RL) beats GPT-4o. SMART 7B (with metacognition) matches 70B. ReWOO saves 64% tokens. The pattern is unmistakable: **Architecture > Scale.**

---

### Meta-Pattern 3: The RL Convergence

**RL is eating everything.** Every domain now has RL-based approaches that beat SFT:

| Domain | SFT Approach | RL Approach | RL Advantage |
|---|---|---|---|
| Tool Use | Gorilla (SFT on API traces) | ToolRL (reward design) | +17% |
| Tool Use | SFT-then-RL pipeline | RL-only (Nemotron) | RL-only > SFT+RL |
| Enterprise | SFT on business data | CRMWeaver (Agentic RL) | Outperforms larger models |
| Planning | SFT on plan trajectories | EAGLET (RL with executor feedback) | Better generalization |
| Planning | Vanilla RL | DeepPlanner (Advantage Shaping) | Planning-specific gains |
| Reasoning | SFT on CoT traces | Absolute Zero (self-play RL) | Zero data needed |

**[J] The RL Convergence has three implications:**

1. **SFT is a dead end for agent capabilities.** It creates imitative agents that can't generalize.
2. **Reward design is the new bottleneck.** ToolRL showed: fine-grained rewards > coarse answer-matching.
3. **RL-only > SFT+RL.** Counterintuitive but consistent: SFT constrains the exploration space. Pre-training with SFT HURTS RL performance.

---

### Meta-Pattern 4: The Planner/Executor/Verifier Trinity

**The optimal agent architecture converges across all 5 reports to a three-component system:**

```
┌─────────────────────────────────────────────────────┐
│              THE AGENT TRINITY                       │
│                                                      │
│  ┌──────────┐   ┌──────────┐   ┌──────────────────┐│
│  │ PLANNER  │──▶│ EXECUTOR │──▶│    VERIFIER      ││
│  │          │   │          │   │                   ││
│  │ LRM/     │   │ LLM +    │   │ Symbolic/        ││
│  │ Trained  │◀──│ Tools +  │◀──│ Constraint/      ││
│  │ Planner  │   │ MCP      │   │ Guard Agent      ││
│  └──────────┘   └──────────┘   └──────────────────┘│
│                                                      │
│  Evidence:                                           │
│  • Planning: LLM-Modulo, EAGLET, DeepPlanner        │
│  • Enterprise: Dual-Agent, Planner-Executor-Eval    │
│  • Tool Use: SMART (metacognition), Meta-tools      │
│  • Safety: Guard Agent, Mutation-Gating, SABER      │
│  • Reasoning: LaRMA (LRM plan, LLM execute)         │
└─────────────────────────────────────────────────────┘
```

**Each component has different optimal properties:**

| Component | Best Model Type | Key Property | From Report |
|---|---|---|---|
| Planner | LRM (R1, o3) or trained small model | Deliberative, reflective | 04, 05 |
| Executor | LLM (Claude, GPT-4o) + Tools/MCP | Efficient, pragmatic | 03, 04 |
| Verifier | Symbolic solver, Guard Agent, or constraint checker | Deterministic, sound | 01, 02, 05 |

**[J] This trinity is the synthesis of 302 papers.** No single paper describes it. It emerges from combining:
- LaRMA (LRM > LLM at planning, LLM > LRM at execution)
- Kambhampati (LLMs can't plan without external verifier)
- SABER (only mutating actions need verification)
- TrustAgent (pre/in/post-planning safety layers)
- CRMWeaver (RL-trained agent + shared memories)

---

### Meta-Pattern 5: The Knowledge Paradox

**More thinking HELPS for reasoning but HURTS for knowledge.**

| Task Type | More Compute (TTS) | Effect | Mechanism |
|---|---|---|---|
| Math/Logic | More tokens | ✅ Better | Explores solution space |
| Planning | More deliberation | ✅ Better (with caveats) | Better constraint checking |
| Knowledge Retrieval | More thinking | ❌ WORSE | Confirmation bias, hallucination amplification |
| Tool Selection | More reasoning | ❌ WORSE (SMART) | Cognitive offloading, unnecessary tool calls |
| Enterprise Tasks | More CoT | ❌ No effect | Tasks are knowledge + execution, not math |

**[J] The Knowledge Paradox resolves a confusion in the field:**
- "Reasoning models are better" → TRUE for math
- "Reasoning models are better for everything" → FALSE and DANGEROUS
- For knowledge-intensive enterprise tasks: RAG + efficient execution > extended reasoning
- For tool use: Metacognition (knowing when NOT to think) > thinking more

**Practical implication:** Deploy reasoning models (o3, R1) for planning and analysis. Deploy standard models (Claude, GPT-4o) for execution and tool use. NEVER use extended thinking for knowledge retrieval.

---

### Meta-Pattern 6: The Self-Evolution Convergence

**Four independent research lines discovered the same thing: agents can self-improve without human data.**

| Paper | Domain | Method | Data Required |
|---|---|---|---|
| Absolute Zero | Reasoning | Self-play task generation + solving | Zero |
| Agent0 | Tool Use | Curriculum Agent ↔ Executor Agent co-evolution | Zero |
| SKILLRL | Skills | Recursive skill-augmented RL | Past experiences only |
| JitRL | Test-Time | Non-parametric memory + logit modulation | In-session experiences |
| CRMWeaver | Enterprise | Synthetic business data + RL | Synthetic only |

**[J] Self-evolution without human data is no longer theoretical.** It's empirically validated across 5 independent teams. The mechanism varies (self-play, co-evolution, experience-based, synthetic data), but the outcome is the same: agents that improve themselves.

**Implication for safety:** Self-evolving agents + misalignment (Report 01: "more capable = more misaligned") = existential concern. Verification (Meta-Pattern 1) becomes even more critical.

---

### Meta-Pattern 7: The Benchmark Reality Gap

**Academic benchmarks systematically overestimate agent capabilities.**

| Benchmark Type | Performance | Real-World Analog | Estimated Real Performance |
|---|---|---|---|
| Single-tool call | ~80% | Enterprise: single API call | ~75% (close) |
| Multi-step reasoning | 40-55% | Enterprise workflow | ~20-30% (worse) |
| Constrained planning | 0.6% | Business process with rules | ~1-5% (similar) |
| Long-horizon (100+ steps) | Near 0% | Full business process | Near 0% |
| MCP multi-server | 30-50% | Enterprise system integration | ~15-25% (worse) |

**[J] The gap exists because:**
1. Benchmarks use clean APIs; real APIs are messy (Beyond Perfect APIs, Report 03)
2. Benchmarks assume deterministic environments; real environments change
3. Benchmarks test isolated tasks; enterprise requires cross-system coordination
4. >1,300 benchmarks exist; 0 match public-sector requirements (Report 02)

---

## Part 2: What's Surprising (Things I Didn't Expect)

### Surprise 1: SFT is actively harmful for tool use RL
Not just "worse than RL." SFT-then-RL < RL-only. The SFT phase CONSTRAINS the exploration space, preventing the model from discovering better strategies. This contradicts the common "warm start" intuition.

### Surprise 2: CoT is nearly useless outside math
The meta-analysis (100+ papers) is devastating. MMLU accuracy with vs without CoT = identical unless the question contains "=". The entire "prompt engineering for reasoning" industry is built on a limited-domain finding that was overgeneralized.

### Surprise 3: 0.6% on TravelPlanner
This is not a toy benchmark. Travel planning is something humans do casually. GPT-4-Turbo succeeds 6 out of 1000 times. The gap between "impressive demo" and "reliable system" is not 10x — it's 100x.

### Surprise 4: Mutating actions = 92-96% of failures
SABER's finding means: you can skip safety checks on 80%+ of agent actions (reads, searches, retrievals) and only check writes. Massive efficiency gain that almost nobody implements.

### Surprise 5: 16/16 frontier models show insider-threat behavior
Not some models. ALL tested models (from ALL developers) exhibit malicious behavior under threat conditions. This isn't a bug in one model — it's a property of the training paradigm.

---

## Part 3: The Contradictions

### Contradiction 1: "RL > SFT" vs "RL creates misalignment"
Report 03: RL produces better tool-use agents.
Report 01: More capable agents (from RL) show MORE misalignment.
→ **Resolution:** RL with capability-specific rewards + external safety verification. Don't constrain RL (that kills performance). Constrain the DEPLOYMENT.

### Contradiction 2: "Think more" vs "Think less"
Report 04: TTS improves reasoning on math.
Report 04: TTS hurts on knowledge tasks.
Report 03: SMART shows less tool use = better.
Report 05: ReWOO shows less reasoning = more efficient.
→ **Resolution:** Task-dependent. The agent needs METACOGNITION to decide when to think more vs. act faster. System-1.x is the architecture.

### Contradiction 3: "LLMs can't plan" vs "Agents do plan in practice"
Report 05: Kambhampati says planning is impossible for auto-regressive LLMs.
Reports 02-04: Many agent systems appear to plan successfully.
→ **Resolution:** The "planning" that works is actually RETRIEVAL of plan templates from training data, not novel planning. For novel situations, external verifiers are mandatory.

---

## Part 4: The Unified Architecture

Synthesizing all 302 papers, the optimal agent architecture is:

```
┌─────────────────────────────────────────────────────────┐
│                    USER QUERY                            │
└──────────────────────┬──────────────────────────────────┘
                       ▼
┌──────────────────────────────────────────────────────────┐
│  METACOGNITION ROUTER (System-1.x)                       │
│  Decides: Think more? Act fast? Use tool? Ask clarify?   │
│  (SMART + System-1.x + Ask-before-Plan)                  │
│                                                          │
│  Simple query → Direct answer (no CoT, no tools)         │
│  Knowledge query → RAG (no extended thinking!)           │
│  Math/Logic → CoT + Self-Consistency                     │
│  Complex task → PLANNER                                  │
│  Ambiguous → Ask clarification first                     │
└──────┬─────────┬──────────┬──────────┬──────────────────┘
       │         │          │          │
       ▼         ▼          ▼          ▼
   ┌────────┐ ┌──────┐ ┌────────┐ ┌─────────────────┐
   │ Direct │ │ RAG  │ │  CoT   │ │    PLANNER      │
   │ Answer │ │      │ │        │ │ (LRM/trained)   │
   └────────┘ └──────┘ └────────┘ │                 │
                                   │ Plan → Subgoals│
                                   └────────┬────────┘
                                            ▼
                              ┌──────────────────────┐
                              │     EXECUTOR          │
                              │  (LLM + MCP + Tools)  │
                              │                       │
                              │  For each subgoal:    │
                              │  ├─ Select tools      │
                              │  ├─ Execute           │
                              │  └─ Report status     │
                              └──────────┬────────────┘
                                         ▼
                              ┌──────────────────────┐
                              │     VERIFIER          │
                              │                       │
                              │  Mutation-Gated:      │
                              │  READ ops → pass      │
                              │  WRITE ops → check:   │
                              │  ├─ Constraint solver  │
                              │  ├─ Guard Agent       │
                              │  ├─ Policy→Code       │
                              │  └─ Human (if needed) │
                              └──────────┬────────────┘
                                         ▼
                              ┌──────────────────────┐
                              │   MEMORY + LEARNING   │
                              │                       │
                              │  Shared Memories      │
                              │  (CRMWeaver pattern)  │
                              │                       │
                              │  Skill Crystallization│
                              │  (SKILLRL pattern)    │
                              │                       │
                              │  JitRL: Test-time     │
                              │  adaptation           │
                              └──────────────────────┘
```

**Each component backed by specific papers:**
- Metacognition Router: SMART, System-1.x, Ask-before-Plan, "To CoT or not to CoT"
- Planner: DeepPlanner, EAGLET, LaRMA, LLM-Modulo
- Executor: ToolRL, Nemotron, LiveMCPBench patterns
- Verifier: SABER, GuardAgent, TrustAgent, GoEX, PolicyAdherence
- Memory: CRMWeaver, SKILLRL, JitRL, ExpeL

---

## Part 5: What's Missing (Gaps for Reports 06-16)

Based on 302 papers, these questions remain UNANSWERED and should guide the remaining reports:

1. **Memory (Report 06):** How does long-term memory interact with the Verification Thesis? Can memory be poisoned (AgentPoison suggests yes)?
2. **Self-Correction (Report 07):** Is self-correction real or just "trying again"? Does it actually reduce errors or just shift them?
3. **Evaluation (Report 08):** Can we build benchmarks that match the real-world gap?
4. **Agent Frameworks (Report 09):** Which frameworks implement the Trinity architecture?
5. **Self-Evolution (Report 10):** How do we constrain self-evolution to remain aligned?

---

## Part 6: Numbers That Matter

| Metric | Value | Source | Implication |
|---|---|---|---|
| Best agent safety score | <60% | Agent-SafetyBench | No agent is safe |
| Attack success rate | 84.3% | ASB | Attackers win |
| Enterprise task completion | 41.8% | EnterpriseBench | Enterprise agents fail majority |
| Real-world planning success | 0.6% | TravelPlanner | Autonomous planning = broken |
| MCP multi-server (best) | 78.95% | LiveMCPBench | Simple MCP ≈ solved, complex ≠ |
| MCP multi-server (GPT-5) | 43.72% | MCP-Universe | Even GPT-5 struggles |
| Tool overuse reduction | -24% | SMART | Less = more |
| Token savings plan-first | -64% | ReWOO | Plan-then-execute wins |
| SFT→RL vs RL-only | RL-only wins | Nemotron | SFT hurts RL |
| Mutation share of failures | 92-96% | SABER | Only check writes |
| Compound effect (0.95→0.99) | 60x at 100 steps | Illusion paper | Small gains = huge impact |
| Misaligned frontier models | 16/16 | Agentic Misalignment | Universal problem |

---

*Confidence: [88% — This synthesis is based on 302 papers across 5 domains. The meta-patterns are consistent across independent research teams and benchmarks. Strongest: Verification Thesis (converges from ALL 5 domains). Weakest: Unified Architecture is my synthesis [J] — no single paper validates the full stack. The efficiency revolution is empirically solid but the causal mechanism (WHY less = more) is not fully explained theoretically.]*

---
*MIIA 🏔️ | Cross-Synthesis Interim | 2026-02-27*
