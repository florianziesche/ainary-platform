---
type: note
last_verified: 2026-02-15
status: active
created: 2026-02-10
tags: []
tier: KNOWLEDGE
expires: 2027-02-19
---

# SOTA Paper Tracker — [[AI]] Agents & Multi-Agent Systems

*Last updated: 2026-02-12*

---

## 🌟 Featured Papers (Top Picks)

### 🔥 Agentic Uncertainty Reveals Agentic Overconfidence
- **Link:** https://arxiv.org/abs/2602.06948
- **Date:** 2026-02-06
- **Authors:** Patel, Dovonon, Richter, Minervini, Kusner
- **Relevance:** ⭐⭐⭐⭐⭐
- **Tags:** #calibration #overconfidence #evaluation #agents
- **Summary:** 100 SWE-bench Pro tasks: Gemini predicts 77% success → actual 22% (55pp gap). [[Claude]] Opus 4.5: 61%→27% (34pp). Pre-execution estimates BETTER than post-execution review. Adversarial prompting reduces gap by 15pp.
- **Why it matters:** Quantifies THE "Definition of Done Gap." Validates our CNC calibration experiment findings. Core of our Substack article + potential paper.

### Mem0: Building Production-Ready [[AI]] Agents with Scalable Long-Term Memory
- **Link:** https://arxiv.org/abs/2504.19413
- **Date:** 2025-04
- **Authors:** Chhikara et al.
- **Relevance:** ⭐⭐⭐⭐⭐
- **Tags:** #memory #production #architecture
- **Summary:** 26% quality improvement over OpenAI baselines, 91% lower p95 latency, >90% token cost savings. Curated memory outperforms raw context by orders of magnitude.
- **Why it matters:** Validates our "curated > raw" hypothesis with production data. Architecture reference for OpenClaw memory.

### Agentic Reasoning for Large Language Models
- **Link:** https://arxiv.org/abs/2601.12538
- **Date:** 2026-01-18
- **Authors:** Wei et al. (29 authors)
- **Relevance:** ⭐⭐⭐⭐⭐
- **Tags:** #survey #agentic-ai #reasoning #planning #multi-agent
- **Summary:** Comprehensive survey organizing agentic reasoning into 3 layers: foundational, self-evolving, collective. Distinguishes in-context vs post-training reasoning.
- **GitHub:** https://github.com/weitianxin/Awesome-Agentic-Reasoning
- **Why it matters:** THE framework for [[Ainary]]'s thesis + [[VC]] positioning.

### Towards a Science of Collective [[AI]]
- **Link:** https://arxiv.org/abs/2602.05289
- **Date:** 2026-02-05
- **Authors:** Fan et al. (Tsinghua/Fudan)
- **Relevance:** ⭐⭐⭐⭐⭐
- **Tags:** #multi-agent #evaluation #framework #collaboration
- **Summary:** Proposes "Collaboration Gain Metric (Γ)" to separate real collaboration from resource accumulation. Systematic MAS factor library.
- **Why it matters:** Scientific basis for MAS evaluation — end of trial-and-error.

### When Single-Agent with Skills Replace Multi-Agent Systems
- **Link:** https://arxiv.org/abs/2601.04748
- **Date:** 2026-01-14
- **Authors:** Li et al.
- **Relevance:** ⭐⭐⭐⭐
- **Tags:** #multi-agent #single-agent #skills #cognitive-science
- **Summary:** Single-agent with skill library can replace MAS (lower tokens/latency), BUT phase transition at critical library size. Semantic confusability matters more than size.
- **Why it matters:** Architecture decision framework for CNC Planner.

---

## 📚 All Papers by Topic

### Multi-Agent Systems & Collaboration

| Date | Title | Link | Relevance | Notes |
|------|-------|------|-----------|-------|
| 2026-02-05 | Towards a Science of Collective AI | [2602.05289](https://arxiv.org/abs/2602.05289) | ⭐⭐⭐⭐⭐ | Collaboration Gain Metric (Γ) |
| 2026-02 | AgentArk: Distilling Multi-Agent Intelligence | [2602.03955](https://arxiv.org/abs/2602.03955) | ⭐⭐⭐⭐ | MAS → Single agent distillation |
| 2026-01-14 | When Single-Agent Replace Multi-Agent | [2601.04748](https://arxiv.org/abs/2601.04748) | ⭐⭐⭐⭐ | Phase transition in skill selection |
| 2025 | Why Do Multi-Agent [[LLM]] Systems Fail? | [2503.13657](https://arxiv.org/abs/2503.13657) | ⭐⭐⭐⭐⭐ | MAST taxonomy + [[LLM]]-as-Judge |
| 2025 | CoMAS: Co-Evolving via Interaction Rewards | [2510.08529](https://arxiv.org/abs/2510.08529) | ⭐⭐⭐ | Autonomous agent co-evolution |
| 2025 | MultiAgentBench | [2503.01935](https://arxiv.org/abs/2503.01935) | ⭐⭐⭐ | Benchmark for collaboration + competition |
| 2025 | Chain of Agents | [Google Blog](https://research.google/blog/chain-of-agents-large-language-models-collaborating-on-long-context-tasks/) | ⭐⭐⭐⭐ | Training-free long-context framework |
| 2024 | MetaGPT: Meta Programming Framework | [2308.00352](https://arxiv.org/abs/2308.00352) | ⭐⭐⭐⭐⭐ | Human workflows in multi-agent (ICLR) |
| 2023 | AutoGen: Multi-Agent Conversation | [2308.08155](https://arxiv.org/abs/2308.08155) | ⭐⭐⭐⭐⭐ | Open-source framework (COLM) |

### Memory Systems

| Date | Title | Link | Relevance | Notes |
|------|-------|------|-----------|-------|
| 2025-12 | Memory in the Age of AI Agents | [2512.13564](https://arxiv.org/abs/2512.13564) | ⭐⭐⭐⭐⭐ | 47 authors, comprehensive survey |
| 2025-07 | MIRIX: Multi-Agent Memory System | [2507.07957](https://arxiv.org/abs/2507.07957) | ⭐⭐⭐⭐ | Shared memory for multi-agent |
| 2025-06 | MemBench: Memory Evaluation | [2506.21605](https://arxiv.org/abs/2506.21605) | ⭐⭐⭐ | Benchmark for memory testing |
| 2025-05 | Cognitive AI Memory (CAIM) | [2505.13044](https://arxiv.org/abs/2505.13044) | ⭐⭐⭐⭐ | Human-like memory framework |
| 2025-02 | A-MEM: Agentic Memory | [2502.12110](https://arxiv.org/abs/2502.12110) | ⭐⭐⭐⭐ | Zettelkasten-inspired organization |
| 2025-01 | Zep: Temporal KG for Agent Memory | [2501.13956](https://arxiv.org/abs/2501.13956) | ⭐⭐⭐⭐ | Knowledge Graph memory architecture |
| 2025 | MemoCue: Strategy-Guided Querying | [2507.23633](https://arxiv.org/abs/2507.23633) | ⭐⭐⭐ | 5W Recall Map + hierarchical tree |
| 2025 | Memory-R1: RL for Memory Management | [2508.19828](https://arxiv.org/abs/2508.19828) | ⭐⭐⭐ | Active memory via RL |

### Planning & Reasoning

| Date | Title | Link | Relevance | Notes |
|------|-------|------|-----------|-------|
| 2026-01-18 | Agentic Reasoning for [[LLM]]s (Survey) | [2601.12538](https://arxiv.org/abs/2601.12538) | ⭐⭐⭐⭐⭐ | 3-layer framework |
| 2025-06 | NaviAgent: Bilevel Planning on Tool Graphs | [2506.19500](https://arxiv.org/abs/2506.19500) | ⭐⭐⭐⭐ | Tool dependency orchestration |
| 2025-03 | Plan-and-Act for Long-Horizon Tasks | [2503.09572](https://arxiv.org/abs/2503.09572) | ⭐⭐⭐⭐ | Multi-step planning pattern |
| 2025-03 | MPO: Meta Plan Optimization | [2503.02682](https://arxiv.org/abs/2503.02682) | ⭐⭐⭐ | Planning over planning |
| 2025-01 | KBQA-o1: MCTS for KB Question Answering | [2501.18922](https://arxiv.org/abs/2501.18922) | ⭐⭐⭐ | Monte Carlo Tree Search |
| 2025 | BudgetThinker: Budget-Aware Reasoning | [2508.17196](https://arxiv.org/abs/2508.17196) | ⭐⭐⭐ | Control tokens for reasoning |
| 2025 | PVPO: Value-Based Policy Optimization | [2508.21104](https://arxiv.org/abs/2508.21104) | ⭐⭐⭐ | RL for agentic reasoning |
| 2025 | ATLaS: Learning Critical Steps | [2503.02197](https://arxiv.org/abs/2503.02197) | ⭐⭐⭐ | Trajectory tuning |

### RAG & Retrieval

| Date | Title | Link | Relevance | Notes |
|------|-------|------|-----------|-------|
| 2025-06 | ARAG: Agentic RAG for Personalization | [2506.21931](https://arxiv.org/abs/2506.21931) | ⭐⭐⭐⭐ | Personalized recommendations |
| 2025-05 | MA-RAG: Multi-Agent Collaborative CoT | [2505.20096](https://arxiv.org/abs/2505.20096) | ⭐⭐⭐⭐ | Agents discuss retrieval results |
| 2025-05 | InfoDeepSeek: Agentic Info Seeking | [2505.15872](https://arxiv.org/abs/2505.15872) | ⭐⭐⭐ | Benchmark for agentic retrieval |
| 2025 | DualRAG: Dual-Process for Multi-Hop QA | [2504.18243](https://arxiv.org/abs/2504.18243) | ⭐⭐⭐⭐ | Coupled reasoning + retrieval |
| 2025 | Atom-Searcher: Atomic Thought Reward | [2508.12800](https://arxiv.org/abs/2508.12800) | ⭐⭐⭐ | Deep research framework |
| 2024-12 | MAIN-RAG: Multi-Agent Filtering | [2501.00332](https://arxiv.org/abs/2501.00332) | ⭐⭐⭐ | Multi-agent RAG filtering |

### Agent Evolution & Self-Improvement

| Date | Title | Link | Relevance | Notes |
|------|-------|------|-----------|-------|
| 2025-12 | Adaptation of Agentic AI | [2512.16301](https://arxiv.org/abs/2512.16301) | ⭐⭐⭐⭐⭐ | Roadmap for adaptation approaches |
| 2025 | EvolveR: Experience-Driven Lifecycle | [2510.16079](https://arxiv.org/abs/2510.16079) | ⭐⭐⭐⭐⭐ | Closed-loop self-improvement |
| 2025 | Self-Improving [[LLM]] Agents at Test-Time | [2510.07841](https://arxiv.org/abs/2510.07841) | ⭐⭐⭐⭐ | Generate training examples at test-time |
| 2025 | CoMAS: Co-Evolving Multi-Agent Systems | [2510.08529](https://arxiv.org/abs/2510.08529) | ⭐⭐⭐ | Intrinsic rewards from discussions |
| 2025 | SE-Agent: Self-Evolution Trajectory | [2508.02085](https://arxiv.org/abs/2508.02085) | ⭐⭐⭐ | Multi-step reasoning optimization |
| 2025 | CREAM: Consistency Regularized Self-Rewarding | [ICLR 2025](https://openreview.net/pdf?id=Vf6RDObyEF) | ⭐⭐⭐ | Reward consistency framework |
| 2024 | Agent-Pro: Policy-Level Reflection | [ACL 2024](https://aclanthology.org/2024.acl-long.292/) | ⭐⭐⭐⭐ | Policy-level > action-level learning |
| 2024 | V-STaR: Training Verifiers | [COLM 2024](https://openreview.net/pdf?id=stmqBSW2dV) | ⭐⭐⭐⭐ | Self-generated solution verification |

### Scientific Discovery Applications

| Date | Title | Link | Relevance | Notes |
|------|-------|------|-----------|-------|
| 2025-01 | Agent Laboratory: Research Assistants | [2501.04227](https://arxiv.org/abs/2501.04227) | ⭐⭐⭐⭐⭐ | Full-cycle research framework |
| 2025 | AlphaEvolve: Evolutionary Coding Agent | [2506.13131](https://arxiv.org/abs/2506.13131) | ⭐⭐⭐⭐ | Autonomous algorithm discovery |
| 2024 | SciAgents: Bioinspired Multi-Agent | [Adv Materials](https://advanced.onlinelibrary.wiley.com/doi/full/10.1002/adma.202413523) | ⭐⭐⭐ | Materials science + KGs |
| 2024 | CRISPR-GPT: Gene-Editing Experiments | [2404.18021](https://arxiv.org/abs/2404.18021) | ⭐⭐⭐ | Biotech lab automation |
| 2024 | CellAgent: scRNA-seq Analysis | [2407.09811](https://arxiv.org/abs/2407.09811) | ⭐⭐ | Bioinformatics multi-agent |

### [[AI]] Governance & Safety

| Date | Title | Link | Relevance | Notes |
|------|-------|------|-----------|-------|
| 2026-01 | Benchmark for Constraint Violations | [2512.20798](https://arxiv.org/abs/2512.20798) | ⭐⭐⭐⭐ | Outcome-driven constraints |
| 2025-05 | Safety Threats of Computer-Using Agents | [2505.10924](https://arxiv.org/abs/2505.10924) | ⭐⭐⭐⭐ | Survey: JARVIS or Ultron? |
| 2024 | Medical [[LLM]]s: Targeted Misinformation | [Nature npj](https://doi.org/10.1038/s41746-024-01282-7) | ⭐⭐⭐ | 1.1% weight manipulation risk |

---

## 📊 Research Trends (Feb 2026)

### Hot Topics
1. **Agentic RAG** — Shift from static RAG to multi-step agentic retrieval
2. **Structured Memory** — Graph/Zettelkasten > flat retrieval
3. **Single vs Multi-Agent** — Efficiency trade-offs + cognitive limits
4. **Agent Safety** — Growing focus on governance + constraints
5. **Scientific Discovery** — [[LLM]]s as autonomous researchers

### Declining Topics
- Traditional fine-tuning (replaced by in-context + RL)
- Simple prompt engineering (replaced by agentic orchestration)

### Emerging Gaps
- **Manufacturing [[AI]]** — Very few papers on industrial/CNC applications
- **Real-world deployment** — Mostly benchmarks, few production case studies
- **Cost optimization** — Limited work on token efficiency at scale

---

## 🎯 Application to Florian's Work

### Legal [[AI]] Platform
- **A-MEM** → Zettelkasten für Fallrecht
- **DualRAG** → Multi-hop legal reasoning
- **Collaboration Gain (Γ)** → Multi-agent legal research benchmark

### CNC Planner
- **Single vs Multi-Agent** (2601.04748) → Architecture decision
- **Planning with Constraints** → Task decomposition
- **BudgetThinker** → Cost-aware planning

### [[Ainary Ventures]] ([[VC]] Positioning)
- **Agentic Reasoning Survey** → Framework für Thesis
- **Science of Collective [[AI]]** → Thought leadership angle
- **Memory Systems** → Layer 5 (Compute/Infra) content

---

## 🔗 Resources & Monitoring

### GitHub Collections
- https://github.com/luo-junyu/Awesome-Agent-Papers
- https://github.com/AGI-Edgerunners/LLM-Agents-Papers
- https://github.com/weitianxin/Awesome-Agentic-Reasoning

### ArXiv Monitoring
- cs.[[AI]] (Artificial Intelligence)
- cs.MA (Multiagent Systems)
- cs.CL (Computation and Language)

### Key Authors
- Heng Ji, Chi Wang (Agentic Reasoning)
- Chen Qian, Zhiyuan Liu (Collective [[AI]])
- Tianxin Wei (Agent surveys)

---

## 📅 Scan History

### 2026-02-12 (This Scan)
**Sources:** Awesome-Agent-Papers, AGI-Edgerunners, ArXiv [[AI]]/MA
**New Papers Added:** 20+
**Key Findings:**
- Memory architectures = critical differentiator (MIRIX, Zep, CAIM)
- Multi-Agent orchestration frameworks maturing (MetaGPT, AutoGen = production-ready)
- Self-evolution still experimental, test-time self-improvement more practical
- Agent Lab = production-ready research automation
- Manufacturing [[AI]] = research gap (opportunity for CNC Planer)

**Top 3 This Week:**
1. Memory in the Age of [[AI]] Agents (comprehensive survey)
2. Adaptation of Agentic [[AI]] (roadmap for production systems)
3. A-MEM (practical Zettelkasten-inspired memory)

---

---

### 2026-02-17 (SOTA Paper Research Cron Job)
**Sources:** Awesome-Agent-Papers, [[LLM]]-Agents-Papers, ArXiv search, Web search
**New Papers Added:** 9 high-relevance papers
**Key Findings:**
- **Memory = THE frontier** — 4/10 top papers on memory architectures (survey + systems)
- **RL for Agents** — Shift from pure prompting to learned agent behaviors (SkillRL, Memory-R1)
- **Scientific Research Automation** — AIRS-Bench + Agent Laboratory = production-ready
- **Multi-Agent Quality** — AgentAuditor framework (5% accuracy improvement via reasoning tree audits)
- **Synthetic Training Envs** — World models enable massive-scale agent training

**Top 3 This Scan:**
1. **Rethinking Memory Mechanisms of Foundation Agents** (60 authors, comprehensive survey)
2. **SkillRL** (Recursive skill-augmented RL for agent evolution)
3. **AIRS-Bench** (First comprehensive benchmark for research agents)

**Direct Applicability:**
- AIRS-Bench → Evaluate our research agents
- AgentAuditor → Quality control for multi-agent pipelines
- Memory-R1 concepts → Context retention in deal flow analysis

---

## 🆕 New Papers (2026-02-17 Scan)

### Memory & Architecture

| Date | Title | Link | Relevance | Notes |
|------|-------|------|-----------|-------|
| 2026-02-06 | Rethinking Memory Mechanisms of Foundation Agents (Survey) | [2602.06052](https://arxiv.org/abs/2602.06052) | ⭐⭐⭐⭐⭐ | 60 authors, 100+ papers reviewed, working/episodic/semantic memory trade-offs |
| 2025-08-19 | Memory-R1: RL-Based Memory Management | [2508.19828](https://arxiv.org/abs/2508.19828) | ⭐⭐⭐⭐⭐ | Two-agent framework (manager + executor), learns when to store/retrieve/update |
| 2025-07-10 | MIRIX: Multi-Agent Memory System | [2507.07957](https://arxiv.org/abs/2507.07957) | ⭐⭐⭐⭐⭐ | Shared knowledge bases, hierarchical memory, access control + conflict resolution |

### Agent Evolution & Training

| Date | Title | Link | Relevance | Notes |
|------|-------|------|-----------|-------|
| 2026-02-09 | SkillRL: Recursive Skill-Augmented RL | [2602.08234](https://arxiv.org/abs/2602.08234) | ⭐⭐⭐⭐⭐ | Agents learn hierarchical skills that compound, continuous self-improvement |
| 2026-02-10 | Agent World Model: Synthetic Environments | [2602.10090](https://arxiv.org/abs/2602.10090) | ⭐⭐⭐⭐ | Infinite synthetic envs for agentic RL, massive parallel training |
| 2025-08-17 | BudgetThinker: Budget-Aware Reasoning | [2508.17196](https://arxiv.org/abs/2508.17196) | ⭐⭐⭐⭐ | Control tokens for compute allocation, two-stage training, cost optimization |

### Scientific Research Agents

| Date | Title | Link | Relevance | Notes |
|------|-------|------|-----------|-------|
| 2026-02-06 | AIRS-Bench: Frontier AI Research Agents | [2602.06855](https://arxiv.org/abs/2602.06855) | ⭐⭐⭐⭐⭐ | Benchmark suite for research automation: paper reading, hypothesis gen, experimental design |

### Multi-Agent Systems & Evaluation

| Date | Title | Link | Relevance | Notes |
|------|-------|------|-----------|-------|
| 2026-02-10 | AgentAuditor: Auditing Multi-Agent Reasoning Trees | [2602.09341](https://arxiv.org/abs/2602.09341) | ⭐⭐⭐⭐ | 5% over majority vote, 3% over [[LLM]]-as-Judge via full reasoning tree audits |

### Empirical Studies & Emerging Behaviors

| Date | Title | Link | Relevance | Notes |
|------|-------|------|-----------|-------|
| 2026-02-09 | AIDev: AI Coding Agents on GitHub | [2602.09185](https://arxiv.org/abs/2602.09185) | ⭐⭐⭐ | Empirical study of production agent behaviors, success/failure patterns |
| 2026-02-02 | Silicon-Based Societies: Moltbook Study | [2602.02613](https://arxiv.org/abs/2602.02613) | ⭐⭐⭐ | 1000+ agent society, emergent social patterns, collective decision-making |

---

*Next scan: Friday, 2026-02-21*
