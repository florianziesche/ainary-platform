# Research Report 06: Memory in AI Agents
## Systematic Analysis of ~85 Papers — Technical Perspective

*Generated: 2026-02-27 | Analyst: MIIA 🏔️*
*Method: arXiv abstract analysis, E/I/J/A labels, Admiralty B2-C3*
*Source: github.com/masamasa59/ai-agent-papers/capability-papers/memory.md*

---

## Executive Summary (BLUF)

**~85 Papers spanning May 2023 – Oct 2025. 6 Kernerkenntnisse:**

1. **Memory IS the bottleneck for agent self-evolution.** Long-term memory is the foundation that enables planning, learning, and adaptation. Without persistent memory, agents are stateless — every interaction starts from zero.
2. **The OS metaphor won.** MemGPT → MemOS → MemOS 2.0: Memory management as an Operating System with virtual memory, paging, and hierarchical tiers. This is now the dominant architectural paradigm.
3. **Memory has its own hallucination problem.** HaluMem benchmark: Memory systems fabricate, conflict, omit, and error at each operation stage (storage, retrieval, integration). Memory ≠ ground truth.
4. **Memory is attackable.** MINJA: Memory injection via QUERY-ONLY interaction (no direct access needed). Combined with AgentPoison (Report 01): Memory is the #1 attack surface for agents.
5. **RL is learning to manage memory.** MEM1, Memory-R1, Mem-α, MemRL, MemAct: RL-trained agents that autonomously decide WHAT to store, WHEN to retrieve, and HOW to organize. Memory management as a learnable policy, not a fixed architecture.
6. **4 memory types, not 2.** Beyond "short-term / long-term": Episodic (what happened), Semantic (what I know), Procedural (how to do things), Working (what I'm doing now). Procedural memory is the most underexploited.

---

## Taxonomie: 7 Cluster

### Cluster 1: The OS Paradigm — Memory as Infrastructure (6 Papers)

#### 🔥 [E] MemGPT: Towards LLMs as Operating Systems (Oct 2023)
*Packer et al. | arXiv:2310.08560*
- **THE foundational paper.** Virtual Context Management inspired by OS hierarchical memory.
- Main memory (context window) + Disk (external storage) + Paging (intelligent swapping)
- Interrupts for control flow management
- **[J] Paradigm-defining.** Every subsequent memory paper builds on or reacts to this metaphor.

#### [E] AI-native Memory: Pathway from LLMs to AGI (Jun 2024)
*arXiv:2406.18312*
- **Positions memory as THE missing piece for AGI, not just a utility.**
- "Reasoning-in-a-haystack" experiments: Finding info + reasoning simultaneously = nearly impossible with long context alone
- Long context ≠ memory. Effective context << claimed context.
- **[J] Kills the "just make context longer" argument.** 1M tokens doesn't replace proper memory.

#### [E] MemOS: Operating System for Memory-Augmented Generation (May 2025)
*arXiv:2505.22101*
- Full OS formalization: Memory scheduling, allocation, garbage collection
- Memory types as first-class OS objects

#### [E] MemOS 2.0: A Memory OS for AI Systems (Jul 2025)
*arXiv:2507.03724*
- Extended version: Multi-agent memory sharing, memory security layers
- **[I] Memory as shared infrastructure across agents = "memory bus"**

#### [E] AI-native Memory 2.0: Second Me (Mar 2025)
*arXiv:2503.08102*
- Personalized memory → "digital twin" of the user
- **[I] Memory as identity persistence — the agent "becomes" a representation of you.**

---

### Cluster 2: Memory Structures — What to Remember (10 Papers)

#### 📖 [E] Survey on Memory Mechanism (Apr 2024)
*arXiv:2404.13501*
- First systematic review. Categorizes: Sensory, Short-Term, Long-Term.
- Design patterns: Encoding, Storage, Retrieval, Forgetting
- **[J] The reference taxonomy. Still valid as of 2025.**

#### 📖 [E] From Human Memory to AI Memory (Apr 2025)
*arXiv:2504.15965*
- Maps cognitive science to AI: Sensory → Working → Long-Term (Episodic/Semantic/Procedural)
- **[I] Most complete cognitive-AI mapping.**

#### 📖 [E] Memory in the Age of AI Agents (Dec 2025)
*arXiv:2512.13564*
- Survey: Forms, Functions, and Dynamics
- **Most current survey. Treats memory as a dynamic system, not static storage.**

#### [E] On Structural Memory of LLM Agents (Dec 2024)
*arXiv:2412.15266*
- **Compares 4 structures:** Chunks, Knowledge Triples, Atomic Facts, Summaries
- **Mixed memory (combining all) = best on most tasks**
- Memory structure × retrieval method interaction matters more than either alone
- **[J] No single memory structure is universally best. Topology matters (echoes RAG-Topologie-These).**

#### 🔥 [E] Episodic Memory Position Paper (Feb 2025)
*arXiv:2502.06975*
- **"Episodic Memory is the Missing Piece for Long-Term LLM Agents"**
- 5 key properties of episodic memory: Instance-specific, contextual, single-shot, time-aware, emotion-tagged
- Current systems lack all 5
- **[J] Most current memory systems store FACTS. Episodic memory stores EXPERIENCES. The difference matters for learning from past mistakes.**

#### [E] Agent Workflow Memory (Sep 2024)
*arXiv:2409.07429*
- **AWM: Induces reusable WORKFLOWS from past experience**
- Offline: Learn from training data. Online: Learn from interactions.
- Selectively provides relevant workflows to guide future actions
- **[J] Direct precursor to Procedural Memory and SKILLRL. Workflows = crystallized procedures.**

#### [E] Procedural Knowledge Improves Agentic Workflows (Nov 2025)
*arXiv:2511.07568*
- **Procedural memory > episodic memory for repetitive tasks**
- How-to knowledge stored as reusable procedures
- **[J] The "Semantic Data Product" of memory: Not "what happened" but "how to do it."**

#### [E] CodeMem: Dynamic MCP and Procedural Memory (Dec 2025)
*arXiv:2512.15813*
- **Combines MCP + Procedural Memory for reproducible agents**
- References n8n and Zapier as workflow platforms
- Probabilistic instability of LLM agents → Procedural Memory as stabilizer
- **[J] Direct connection to our Mittelstand AI Stack (n8n + Dify). CodeMem validates the pattern.**

#### [E] Synthesizing Procedural Memory (Dec 2025)
*arXiv:2512.20278*
- Challenges in automated workflow generation from experience
- **[I] The "hard part" of procedural memory: How do you EXTRACT reusable procedures from messy experiences?**

---

### Cluster 3: Hierarchical & Working Memory (6 Papers)

#### [E] HiAgent: Hierarchical Working Memory (Aug 2024)
*arXiv:2408.09559*
- Working memory = in-trial memory (during a single task attempt)
- Hierarchical management: Subgoal tracking + relevant context selection
- **[J] Working memory is the MOST NEGLECTED type. Cross-trial (long-term) gets attention. In-trial does not.**

#### [E] H-MEM: Hierarchical Memory for Long-Term Reasoning (Jul 2025)
*arXiv:2507.22925*
- Multi-level hierarchy: Raw → Summary → Abstract
- Efficient retrieval across levels
- **[I] Hierarchical = better retrieval at scale. Flat memory degrades logarithmically.**

#### [E] ACON: Context Compression for Long-Horizon Agents (Oct 2025)
*arXiv:2510.00615*
- Compresses context while preserving reasoning-relevant information
- **[I] Memory compression ≠ information loss. Smart compression > no compression AND full context.**

#### [E] Memory as Action (MemAct, Oct 2025)
*arXiv:2510.12635*
- **Working memory management as LEARNABLE ACTIONS (not fixed heuristics)**
- In-place editing: deletion + insertion as policy actions
- End-to-end RL optimization
- **[J] The "SABER of memory": Only mutating ops (add/delete) matter, reads are free. RL learns when to mutate.**

#### [E] AgentFold: Proactive Context Management (Oct 2025)
*arXiv:2510.24699*
- Proactive: Agent anticipates what it will need and pre-loads into working memory
- **[I] Prefetching for agent memory. OS metaphor applied to anticipatory loading.**

---

### Cluster 4: RL for Memory Management (8 Papers)

#### 🔥🔥 [E] MEM1: Synergize Memory and Reasoning (Jun 2025)
*arXiv:2506.15841*
- **End-to-end RL: Agent operates with CONSTANT memory across long multi-turn tasks**
- Compact shared internal state: jointly supports memory consolidation AND reasoning
- Unbounded memory growth → eliminated
- **[J] The MEM1 insight: Memory should not GROW with interaction length. It should remain CONSTANT, distilling what matters.**

#### [E] Memory-R1: Memory via RL (Aug 2025)
*arXiv:2508.19828*
- RL teaches agents to manage and utilize memories
- Named after DeepSeek-R1 pattern: RL for memory as R1 did for reasoning
- **[I] Memory-R1 = ToolRL (Report 03) applied to memory. RL > heuristics for memory management.**

#### [E] Mem-α: Learning Memory Construction via RL (Sep 2025)
*arXiv:2509.25911*
- **RL trains agent to determine: WHAT to store, HOW to structure, WHEN to update**
- Pre-defined rules fail as memory systems grow complex
- **[J] Answers the key question: How does the agent learn what's worth remembering?**

#### [E] MemRL: Self-Evolving via Runtime RL on Episodic Memory (Jan 2026)
*arXiv:2601.03192*
- **Runtime RL** (not offline training): Agent improves memory management DURING deployment
- Episodic memory as training signal
- **[J] Combines JitRL (Report 04) with memory: Self-evolution at runtime via memory optimization.**

#### [E] Agentic Memory (AgeMem, Jan 2026)
*arXiv:2601.01885*
- **Unified LTM + STM management as tool-based actions**
- Agent autonomously decides store/retrieve/update/summarize/delete
- End-to-end optimization via RL
- **[J] The most complete RL-for-memory framework. Memory ops = tool calls. Unifies memory and tool use.**

#### [E] Memento: Fine-tuning Agents without Fine-tuning LLMs (Aug 2025)
*arXiv:2508.16153*
- **Adapt agent behavior via MEMORY UPDATES, not weight updates**
- No fine-tuning needed — just change what the agent remembers
- **[J] Elegant insight: If memory is powerful enough, you never need to retrain. Memory IS the model's "fine-tuning."**

---

### Cluster 5: Memory Security & Hallucinations (4 Papers)

#### 🔥 [E] MINJA: Memory Injection Attack via Query-Only (Mar 2025)
*arXiv:2503.03704*
- **Attacker injects malicious memories by only QUERYING the agent (no direct memory access)**
- Crafted queries → agent stores malicious reasoning chains → future retrieval produces harmful output
- **[J] DEVASTATING.** Combined with AgentPoison (Report 01): Two independent attack vectors on memory, both requiring zero direct access. Memory is the #1 attack surface.

#### [E] HaluMem: Memory Hallucination Benchmark (Nov 2025)
*arXiv:2511.03506*
- **First operation-level hallucination benchmark for memory systems**
- 4 hallucination types: Fabrication, Errors, Conflicts, Omissions
- Localizes WHERE in the memory pipeline hallucinations arise
- **[J] Memory systems hallucinate INDEPENDENTLY of the LLM. Even with a perfect LLM, memory storage/retrieval introduces errors.**

#### [E] Memory Sharing Security (from MemOS)
- Multi-agent memory sharing introduces new attack surface
- **[I] Shared memory = amplified risk (cf. Agent Smith infectious jailbreak, Report 01)**

#### [E] Controllable Memory Usage (Jan 2026)
*arXiv:2601.05107*
- **Balancing Anchoring and Innovation in long-term interaction**
- Too much memory = anchoring bias (agent can't adapt)
- Too little memory = no continuity
- **[J] The forgetting problem: Agents that remember too much perform WORSE. Selective forgetting = feature, not bug.**

---

### Cluster 6: Self-Evolving Memory (8 Papers)

#### [E] Long-Term Memory: Foundation of AI Self-Evolution (Oct 2024)
*arXiv:2410.15665*
- Position: LTM is the prerequisite for self-evolution
- Without persistent memory, no learning from experience possible
- **[J] Foundational claim. Everything in Cluster 4 validates this.**

#### [E] Self-evolving Agents with Reflective Memory (Sep 2024)
*arXiv:2409.00872*
- Reflection on past actions → stored as refined memories → better future actions
- **[I] Reflection = memory distillation.**

#### [E] MemEvolve: Meta-Evolution of Memory Systems (Dec 2025)
*arXiv:2512.18746*
- **Not just evolving the agent — evolving the MEMORY SYSTEM ITSELF**
- Memory architecture adapts to task context
- Prior work: Fixed memory architecture. MemEvolve: Dynamic memory architecture.
- **[J] Meta-level insight: The memory system is itself a hyperparameter that should be optimized.**

#### [E] ReasoningBank: Scaling with Reasoning Memory (Sep 2025)
*arXiv:2509.25140*
- Store reasoning CHAINS as reusable memory
- **[I] Not just "what happened" but "how I reasoned about it."**

#### [E] MemGen: Generative Latent Memory (Sep 2025)
*arXiv:2509.24704*
- Latent space memory: Compress experiences into generative latent representations
- **[I] Memory as compressed generative model, not raw storage.**

#### [E] MOBIMEM: Self-Evolution via Memory (Dec 2025)
*arXiv:2512.15784*
- Beyond Training: Agents evolve through memory alone, no retraining
- **[J] Confirms Memento pattern: Memory update replaces weight update.**

---

### Cluster 7: Specialized Memory Applications (6 Papers)

#### [E] Mem0: Production-Ready Long-Term Memory (Apr 2025)
*arXiv:2504.19413*
- **Graph-based memory for relational structures in conversation**
- Evaluated on LOCOMO benchmark
- Scalable, production-ready architecture
- **[J] The most deployment-ready memory system. Graph memory > flat memory for conversations.**

#### [E] A-MEM: Agentic Memory with Zettelkasten (Feb 2025)
*arXiv:2502.12110*
- **Zettelkasten method for agent memory: atomic notes + links + dynamic organization**
- Agent SELF-ORGANIZES memory (not pre-defined structure)
- **[J] Beautiful concept: Zettelkasten = the original "knowledge graph" for humans. Applied to agents.**

#### [E] AGENT KB: Cross-Domain Experience (Jul 2025)
*arXiv:2507.06229*
- Knowledge Base for cross-domain experience transfer
- **[I] Memory that transfers between DIFFERENT tasks/domains.**

#### [E] MIRIX: Multi-Agent Memory System (Jul 2025)
*arXiv:2507.07957*
- Multi-agent shared memory with isolation + sharing policies
- **[I] The "enterprise memory bus": Which agents share which memories?**

#### [E] ChemAgent: Self-updating Library (Jan 2025)
*arXiv:2501.06590*
- Domain-specific: Builds reusable chemical reasoning library from experience
- **[I] Procedural memory for a specific domain. Template for any domain-specific agent.**

#### [E] Ella: Embodied Social Agent with Lifelong Memory (Jun 2025)
*arXiv:2506.24019*
- Lifelong memory for social interactions
- **[I] Memory for SOCIAL context — who said what, relationship history, preferences.**

---

## Synthese: 6 technische Erkenntnisse

### 1. The Memory Type Matrix

| Memory Type | What It Stores | Analog | Current State | Key Paper |
|---|---|---|---|---|
| **Working** | Current task context | RAM | Underexploited | HiAgent, MemAct |
| **Episodic** | What happened (experiences) | Event log | Basic implementations | Episodic Position Paper |
| **Semantic** | What I know (facts, relations) | Knowledge base | Mature (via RAG) | Mem0, A-MEM |
| **Procedural** | How to do things (workflows) | Skill library | **MOST UNDEREXPLOITED** | AWM, CodeMem, Procedural Knowledge |

**[J] The field is over-indexed on Semantic memory (RAG/KG) and under-indexed on Procedural memory.** But procedural memory is what makes agents COMPETENT — not just knowledgeable.

Procedural memory = the "SKILL.md" of agents. It's the connection between memory and Agent Skills (Report 03).

### 2. Memory Management = Learnable Policy

The RL-for-memory cluster (MEM1, Memory-R1, Mem-α, MemRL, AgeMem, MemAct) converges:

```
2023: Fixed memory rules (store everything, retrieve by similarity)
2024: Heuristic memory management (summarize, compress, forget old)
2025: RL-learned memory policy (agent decides what/when/how)
2026: Runtime self-evolving memory (MemRL, MemEvolve)
```

**[J] Memory management is the FOURTH domain conquered by RL** (after Tool Use, Reasoning, Planning). The pattern is universal: Heuristics → RL → Self-Evolution.

### 3. The Constant-Memory Insight

MEM1's key finding: Agent operates with CONSTANT memory across arbitrarily long interactions. Memory doesn't grow — it DISTILLS.

**Mathematical analogy:**
- Naive: Memory = O(n) where n = interaction length → unbounded growth
- MEM1: Memory = O(1) → constant, bounded, efficient
- The agent learns to compress and forget

**[J] This mirrors human cognition.** We don't remember every conversation turn. We remember the GIST, the LESSON, the EMOTION. Everything else fades. MEM1 formalizes this.

### 4. Memory as Attack Surface

| Attack | Method | Access Required | Defense |
|---|---|---|---|
| AgentPoison (Report 01) | Poison RAG knowledge base | Indirect (via data) | Anomaly detection on embeddings |
| Agent Smith (Report 01) | Infectious image in memory | One compromised agent | Isolation |
| **MINJA** | Query-only injection | **ZERO — just talk to the agent** | Memory integrity verification |

**[J] MINJA is the most dangerous because it requires ZERO privileged access.** Anyone who can query the agent can poison its memory. And once poisoned, the malicious memory persists and affects all future interactions.

**Cross-reference with Verification Thesis (Cross-Synthesis):** Memory ALSO needs verification. Not just action outputs — memory INPUTS must be verified before storage.

### 5. Procedural Memory + MCP = Agent Skills

The convergence is clear:

```
Procedural Memory (how to do things)
    + MCP (protocol for tool access)
    + Progressive Disclosure (load on demand)
    = Agent Skills (Report 03)
```

CodeMem (2512.15813) explicitly references n8n/Zapier and proposes Procedural Memory + Dynamic MCP as the architecture for reproducible agents. This is EXACTLY our Mittelstand AI Stack.

### 6. The Forgetting Problem

Controllable Memory Usage (2601.05107) identifies a paradox:
- **Anchoring bias:** Too much memory → agent anchors to past patterns, can't adapt
- **Amnesia:** Too little memory → agent can't learn, every interaction is fresh
- **Sweet spot:** Selective forgetting + periodic consolidation

**[J] This is exactly what MEMORY.md maintenance does.** Raw daily logs → periodic review → distill into long-term memory → delete outdated. The cognitive science is clear: Forgetting is a FEATURE, not a bug.

---

## Top 10 Papers (Technical Impact)

| Rang | Paper | Warum |
|------|-------|-------|
| 1 | **MEM1** (2506.15841) | Constant-memory agent via RL. Solves unbounded growth. |
| 2 | **MemGPT** (2310.08560) | OS paradigm. Foundation for everything after. |
| 3 | **MINJA** (2503.03704) | Query-only memory injection. Zero-access attack. |
| 4 | **A-MEM** (2502.12110) | Zettelkasten for agents. Self-organizing memory. |
| 5 | **Episodic Memory Position** (2502.06975) | Identifies the missing piece. 5 key properties. |
| 6 | **Agent Workflow Memory** (2409.07429) | Procedural memory from experience. Precursor to Skills. |
| 7 | **Mem-α** (2509.25911) | RL learns what/when/how to memorize. |
| 8 | **MemEvolve** (2512.18746) | Meta-evolution: memory SYSTEM adapts, not just content. |
| 9 | **HaluMem** (2511.03506) | Memory hallucinations are real and measurable. |
| 10 | **CodeMem** (2512.15813) | MCP + Procedural Memory = reproducible agents. Validates our stack. |

---

## Cross-Report Connections

| Finding (Report 06) | Connects to | Report |
|---|---|---|
| RL for memory (MEM1, Mem-α) | RL Convergence meta-pattern | Cross-Synthesis |
| MINJA query-only attack | Verification Thesis (memory needs verification too) | 01, Cross |
| Procedural Memory + MCP = Skills | Agent Skills paradigm | 03 |
| Constant memory = distillation | SMART efficiency (-24% tools, +37% perf) | 03 |
| Memory structure × task topology | RAG topology thesis | 100-Repo Synthesis |
| Forgetting as feature | Selective action (SABER: only check mutations) | 01 |
| CodeMem references n8n/Zapier | Mittelstand AI Stack | 100-Repo Synthesis |
| MemEvolve (meta-evolution) | Self-Evolution Convergence | Cross-Synthesis |

---

## Open Problems

1. **Memory Verification:** No robust method to verify memory integrity against MINJA-style attacks
2. **Cross-Agent Memory:** How do agents safely share memories without contamination?
3. **Procedural Memory Extraction:** How to reliably extract reusable procedures from messy experiences?
4. **Memory × Privacy:** EU AI Act requires data minimization. How does this interact with persistent agent memory?
5. **Forgetting Policies:** No principled framework for WHEN to forget WHAT
6. **Memory Hallucination Mitigation:** HaluMem identifies the problem but solutions are rudimentary

---

*Confidence: [83% — Strong evidence for OS paradigm (MemGPT → MemOS lineage). RL-for-memory cluster (5 papers, convergent results). MINJA attack is empirically validated. Weakest: MemEvolve is conceptually compelling but empirically early. Memory type matrix is my synthesis [J] from surveys + cognitive science mapping. Procedural memory thesis is strongly supported by AWM + CodeMem but needs more production validation.]*

---
*MIIA 🏔️ | Report 06/16 | 2026-02-27*
