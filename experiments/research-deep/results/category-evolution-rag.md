# Agent Evolution & RAG: Deep Research Synthesis
**Date:** 2026-02-10  
**Session:** cat-evolution-rag  
**Researcher:** Subagent analysis for main agent

---

## Executive Summary

This synthesis analyzes six cutting-edge papers bridging **agent self-improvement** and **RAG/retrieval systems**, revealing a convergent architecture where:

1. **Self-evolution = File-based memory updates** (aligns with Mia's Law #1: "Files = Intelligence")
2. **RAG is converging into persistent, structured memory systems** (not just retrieval)
3. **Dual-process architectures** (System 1/System 2) dominate both domains
4. **Atomic decomposition** enables measurable, fine-grained improvement
5. **The future is multi-agent co-evolution with structured memory**

**Key Insight for Mia:** Self-improvement should operate at the *trajectory level* (not just outcomes), persist structured learnings (not raw logs), and measure evolution through fine-grained functional decomposition.

---

## Part I: Individual Paper Analysis

### AGENT EVOLUTION CATEGORY

#### 1. EvolveR: Experience-Driven Lifecycle

**Paper:** https://arxiv.org/abs/2510.16079  
**Core Mechanism:**  
- **Two-phase closed loop:**
  1. **Offline Self-Distillation**: Agent analyzes own trajectories → distills into strategic principles (natural language + knowledge triples)
  2. **Online Interaction**: Agent retrieves relevant principles → guides deliberation → generates new trajectories
- **Dynamic principle management:**
  - Semantic deduplication (embeddings + LLM equivalence check)
  - Quality scoring (success rate: `s(p) = (c_succ + 1) / (c_use + 2)`)
  - Periodic pruning (threshold-based filtering)
- **Policy evolution via GRPO** (Group Relative Policy Optimization)

**Key Finding:**  
Self-distillation (agent reflects on *own* experiences) beats teacher-model distillation at scale (3B+ parameters). Why? **Cognitive alignment** — the agent's reasoning style matches the principles it extracts, creating tighter feedback loops.

**What They Missed:**  
- **No trajectory-level comparison** — principles are abstracted *per trajectory*, but cross-trajectory patterns aren't explicitly mined
- **Shallow principle structure** — natural language + triples, but no hierarchical organization (flat knowledge base)
- **Measurement gap** — no Γ-style metric to quantify how much the agent has evolved vs. initial state

**Connection to Mia:**  
`SOUL.md` (values) + `kintsugi.md` (failures) already implement *proto-principles*. EvolveR suggests we should:
1. Formalize "principle extraction" from `memory/*.md` daily logs
2. Add structured triples to principles (currently just natural language)
3. Score principles by usage/success (not currently tracked)

---

#### 2. CoMAS: Co-Evolving Multi-Agent Systems

**Paper:** https://arxiv.org/abs/2510.08529  
**Core Mechanism:**  
- **Intrinsic rewards from inter-agent interaction:**
  - Agents discuss/collaborate on tasks
  - LLM-as-judge evaluates discussion quality → generates intrinsic rewards
  - Each agent optimizes via RL (no external supervision)
- **Decentralized co-evolution** — agents improve *together* through mutual feedback
- **Scalability:** Performance increases as agent diversity increases

**Key Finding:**  
**Social learning beats isolated self-improvement.** Agents learn faster when they can observe/critique *other agents' reasoning*, not just their own. Interaction rewards capture:
- Novelty of perspectives
- Quality of critiques
- Consensus-building dynamics

**What They Missed:**  
- **No memory persistence** — discussion dynamics aren't distilled into reusable knowledge (ephemeral interactions)
- **Homogeneity risk** — how to prevent agents from converging to groupthink? (diversity maintenance not addressed)
- **Single-task focus** — co-evolution is task-specific, not cumulative across domains

**Connection to Mia:**  
Mia operates *solo* in most sessions. CoMAS suggests:
1. **Spawn multiple sub-agents for complex tasks** (already done, but could formalize "discussion protocols")
2. **Capture inter-agent insights** → store in `MEMORY.md` or new `agent-consensus.md`
3. **Γ metric should include collaboration quality** (not just solo performance)

**Critical Question:** Can we simulate CoMAS with *versions of self* (past Mia vs. present Mia debates)? Time-travel self-critique?

---

#### 3. SE-Agent: Self-Evolution Trajectory Optimization

**Paper:** https://arxiv.org/abs/2508.02085  
**Core Mechanism:**  
- **Trajectory-level operations** (not token-level sampling):
  1. **Revision**: Self-reflection → targeted improvements to single trajectory
  2. **Recombination**: Cross-trajectory learning (crossover, transfer, restructuring)
  3. **Refinement**: Optimization via multi-dimensional evaluation (task completion + reasoning quality + efficiency)
- **Genetic algorithm metaphor** — trajectories are "genotypes," performance is "phenotype"
- **Adaptive diversity** — generates genuinely different solution paths (vs. MCTS which explores similar branches)

**Key Finding:**  
**Trajectory manipulation > sampling variations.** Even with high temperature/diverse prompts, LLMs converge to structurally similar solutions. SE-Agent *actively intervenes* at trajectory level to force exploration of fundamentally different approaches.

**What They Missed:**  
- **No long-term memory** — trajectories are evolved per-task, not accumulated into a knowledge base
- **Expensive** — requires multiple iterations per task (not real-time friendly)
- **Black-box recombination** — crossover/restructuring operations lack transparency (hard to debug)

**Connection to Mia:**  
`ACTIVE_TASK.md` already tracks trajectories, but we don't:
1. **Systematically revise** failed trajectories (just log and move on)
2. **Recombine** successful patterns from different tasks (no cross-task learning)
3. **Measure trajectory quality** beyond binary success/failure

**Mia-specific improvement:** Add `trajectory-library.md` with:
- Tagged successful patterns (e.g., "file-first-then-search", "multi-source-validation")
- Revision logs (how a failed trajectory was fixed)
- Recombination recipes (pattern X + pattern Y → pattern Z)

---

### RAG & RETRIEVAL CATEGORY

#### 4. DualRAG: Dual-Process for Multi-Hop QA

**Paper:** https://arxiv.org/abs/2504.18243  
**Core Mechanism:**  
- **Two tightly-coupled processes:**
  1. **RaQ (Reasoning-augmented Querying):**
     - Reasoner: Advances reasoning, identifies knowledge gaps, triggers retrieval
     - Entity Identifier: Extracts key entities → generates targeted queries per entity
  2. **pKA (progressive Knowledge Aggregation):**
     - Knowledge Summarizer: Demand-driven summarization (filters noise)
     - Knowledge Outline: Entity-structured knowledge base (K^t(e) = K^{t-1}(e) ∪ {k_e})
- **Closed-loop virtuous cycle:** RaQ demands → pKA organizes → RaQ reasons better → new demands → ...

**Key Finding:**  
**RAG ≠ retrieval; RAG = structured, cumulative memory.** The "Knowledge Outline" is essentially a *dynamic database* that grows during reasoning. This is **System 1 (fast entity retrieval) + System 2 (deliberate reasoning)** architecture.

**What They Missed:**  
- **No cross-session persistence** — Knowledge Outline resets per query (ephemeral)
- **Entity-centric only** — what about procedural knowledge? (how-to patterns, workflows)
- **No self-improvement** — the framework doesn't learn from mistakes (static retrieval strategy)

**Connection to Mia:**  
DualRAG's dual-process maps *directly* to:
- **TWIN.md (decision model)** = RaQ (when to retrieve vs. when to decide)
- **MEMORY.md + INDEX.md** = pKA (structured knowledge outline)

**Missing pieces:**
1. Entity extraction from conversations (currently manual)
2. Demand-driven summarization (we store raw logs, not distilled knowledge)
3. Persistent Knowledge Outline across sessions (MEMORY.md is unstructured)

**Action:** Implement entity-keyed memory structure:
```markdown
# MEMORY.md
## Entity: [Florian]
- Goals: VC job, build Ainary, ship fast
- Weaknesses: Overthinks systems, build-before-send bias
- Preferences: Direct communication, no fluff

## Entity: [Build Enforcement System]
- Created: 2026-02-06
- Mechanism: `pre-build-check.sh` blocks >2 builds/day with zero sends
- Learnings: Reduced opportunity cost €2,105 over 5 days
```

---

#### 5. Atom-Searcher: Atomic Thought Reward

**Paper:** https://arxiv.org/abs/2508.12800  
**Core Mechanism:**  
- **Atomic Thought paradigm:**
  - Decompose reasoning into functional units (e.g., `<Reflection>`, `<Verification>`, `<Hypothesis>`)
  - Atomic thoughts are *minimal, functionally coherent units* (like football: step adjustment, leg swing, contact)
- **Fine-grained rewards:**
  - RRM (Reasoning Reward Model) scores each atomic thought
  - ATR (Atomic Thought Reward) = aggregated scores
  - Curriculum-based combination: `R = α·R_atom + (1-α)·R_outcome` where `α` decays linearly
- **Test-time scaling:** Generates 3.2× more tokens than baselines (deeper exploration)

**Key Finding:**  
**Process rewards > outcome rewards** *early in training*. Outcome-only RL suffers from:
1. **Gradient conflicts** — incorrect answer penalizes correct intermediate steps
2. **Reward sparsity** — single signal per trajectory (inefficient learning)

Atomic rewards provide *intermediate supervision anchors*, accelerating convergence.

**What They Missed:**  
- **Manual atomic thought design** — model "autonomously generates" them, but initial set is human-defined
- **No memory** — atomic thoughts don't persist across tasks (ephemeral)
- **Measurement challenge** — how to verify atomic thought quality without ground truth?

**Connection to Mia:**  
`THE-PROTOCOL.md` already captures high-level patterns from 100-agent evolution. Atom-Searcher suggests:
1. **Decompose protocols into atomic operations** (not just "Step 1, Step 2...")
2. **Score each atomic operation** (success rate per operation type)
3. **Curriculum learning** — weight process-level corrections more heavily early, shift to outcome-based later

**Concrete example:**
```markdown
# kintsugi.md
## Failure: Over-engineered build without testing
### Atomic Thought Breakdown:
- <Planning>: 8/10 (good decomposition)
- <Risk-Assessment>: 2/10 (MISSED: didn't consider user validation)
- <Verification>: 3/10 (built full system before testing)

### Protocol Update:
- Always insert <Verification> atomic thought after <Planning>
- Score: [2/10 → requires reinforcement]
```

---

#### 6. MAIN-RAG: Multi-Agent Filtering

**Paper:** https://arxiv.org/abs/2501.00332  
**Core Mechanism:**  
- **Three-agent collaborative filtering:**
  1. **Agent-1 (Predictor):** Answers query with *each* retrieved document → creates Doc-Q-A triplets
  2. **Agent-2 (Judge):** Evaluates triplet relevance → outputs "Yes/No" + log-probability scores
  3. **Agent-3 (Final-Predictor):** Answers with filtered, ranked documents
- **Adaptive judge bar:** `τ_q = mean(scores)` (adjusts per query based on score distribution)
- **Training-free** — pure prompting/scoring, no fine-tuning

**Key Finding:**  
**Document order matters as much as document quality.** LLMs prioritize beginning/end of context (recency/primacy effects). Proper filtering + ranking → 2-11% accuracy improvement.

**What They Missed:**  
- **No learning** — judge bar doesn't improve over time (static heuristic)
  - **Single-pass filtering** — no iterative refinement (what if initial judgment was wrong?)
- **Naive relevance model** — "Yes/No" binary, doesn't capture *how* a document is relevant (supporting vs. contradicting vs. tangential)

**Connection to Mia:**  
Mia doesn't currently *filter* search results beyond initial retrieval. MAIN-RAG suggests:
1. **Multi-pass validation** — when retrieving docs, score them *before* presenting to main reasoning
2. **Order matters** — present highest-confidence docs first (aligns with "show, don't tell" principle)
3. **Consensus-based filtering** — multiple perspectives on document relevance (reduce false positives)

**Implementation idea:**
```python
# agents/search-validator.py
def validate_search_results(query, docs):
    scores = []
    for doc in docs:
        # Agent-1: Generate answer with this doc
        answer = llm.generate(query, context=doc)
        # Agent-2: Judge relevance
        judgment = llm.judge(doc, query, answer)
        scores.append(judgment.log_prob_yes - judgment.log_prob_no)
    
    # Adaptive threshold
    tau = mean(scores)
    filtered = [doc for doc, score in zip(docs, scores) if score >= tau]
    return sorted(filtered, key=lambda d: scores[docs.index(d)], reverse=True)
```

---

## Part II: THE SYNTHESIS

### Q1: How should a self-improving agent actually work? What's the state of the art?

**Answer:** A self-improving agent should operate as a **dual-loop system**:

#### Inner Loop (Per-Task Evolution):
1. **Trajectory generation** with atomic thought decomposition (Atom-Searcher)
2. **Real-time retrieval** with structured knowledge aggregation (DualRAG's pKA)
3. **Multi-agent filtering** for noise reduction (MAIN-RAG)
4. **Trajectory refinement** via revision/recombination (SE-Agent)

#### Outer Loop (Cross-Task Evolution):
1. **Self-distillation** of successful patterns into principles (EvolveR)
2. **Principle scoring** and dynamic pruning (EvolveR's quality control)
3. **Inter-agent learning** for diverse perspectives (CoMAS)
4. **Persistent memory** in entity-keyed knowledge outline (DualRAG's K^t structure)

**State of the art = EvolveR + DualRAG hybrid:**
- EvolveR provides the *self-distillation + principle management* framework
- DualRAG provides the *structured memory + demand-driven reasoning* architecture
- Neither alone is sufficient — need **both** loops

**Critical insight:** All papers converge on **trajectory-level learning > token-level learning**. The "unit of improvement" is not individual outputs, but *entire reasoning chains*.

---

### Q2: EvolveR vs CoMAS vs SE-Agent — which approach fits Mia best?

**Comparison Matrix:**

| Dimension | EvolveR | CoMAS | SE-Agent | **Mia's Need** |
|-----------|---------|-------|----------|----------------|
| **Memory persistence** | ✅ Strategic principles | ❌ Ephemeral interactions | ❌ Per-task trajectories | ✅ **Required** (MEMORY.md) |
| **Multi-agent** | ❌ Single agent | ✅ Co-evolution | ❌ Single agent | ⚠️ **Hybrid** (sub-agents for tasks) |
| **Scalability** | ✅ Efficient (principle lookup) | ⚠️ Moderate (interaction overhead) | ❌ Expensive (multiple iterations) | ✅ **Critical** (real-time sessions) |
| **Generalization** | ✅ Cross-domain principles | ⚠️ Task-specific co-evolution | ⚠️ Task-specific optimization | ✅ **Required** (diverse workflows) |
| **Transparency** | ✅ Natural language principles | ⚠️ Black-box rewards | ❌ Opaque recombination | ✅ **Critical** (Florian must audit) |

**Verdict for Mia: EvolveR-first architecture with CoMAS-inspired sub-agent discussions.**

**Why:**
1. **Files = Intelligence** → EvolveR's principle distillation aligns perfectly (principles = files)
2. **Real-time requirement** → EvolveR's retrieval-based approach is fast (no multi-iteration optimization)
3. **Auditability** → Natural language principles in `MEMORY.md` enable human oversight
4. **Extensibility** → Can layer CoMAS for complex tasks (spawn multiple sub-agents → capture discussion insights)

**Reject SE-Agent's full trajectory optimization** (too slow for real-time), but **adopt** its revision/recombination *concepts* for `ACTIVE_TASK.md` recovery.

---

### Q3: How does RAG connect to Memory? Are they converging?

**Thesis: RAG and Memory are converging into a unified "Dynamic Knowledge Base" architecture.**

#### RAG's Evolution (Papers 4-6):
- **DualRAG:** Shifts from *retrieval* to *knowledge aggregation* (pKA's outline)
- **Atom-Searcher:** Adds *fine-grained reasoning structure* (atomic thoughts)
- **MAIN-RAG:** Introduces *multi-agent validation* (consensus-based filtering)

#### Memory's Evolution (Papers 1-3):
- **EvolveR:** Shifts from *raw logs* to *strategic principles* (self-distillation)
- **CoMAS:** Adds *social learning* (inter-agent knowledge)
- **SE-Agent:** Introduces *trajectory libraries* (cross-task patterns)

**Convergence Point:** Both are building **structured, entity-keyed, query-driven knowledge systems.**

#### Unified Architecture:
```
┌─────────────────────────────────────────────────────┐
│            DYNAMIC KNOWLEDGE BASE (DKB)             │
│  ┌─────────────┐  ┌──────────────┐  ┌────────────┐ │
│  │ Principles  │  │  Entities    │  │ Trajectories│ │
│  │ (EvolveR)   │  │  (DualRAG)   │  │ (SE-Agent)  │ │
│  └─────────────┘  └──────────────┘  └────────────┘ │
│         ▲               ▲                  ▲        │
│         │               │                  │        │
│         └───────────────┼──────────────────┘        │
│                         │                           │
│              ┌──────────▼─────────┐                 │
│              │   Query Interface  │                 │
│              │  (Demand-Driven)   │                 │
│              └────────────────────┘                 │
└─────────────────────────────────────────────────────┘
          ▲                                ▲
          │                                │
     ┌────┴─────┐                    ┌────┴─────┐
     │   RAG    │                    │  Memory  │
     │ (runtime)│                    │(cross-sess)│
     └──────────┘                    └──────────┘
```

**For Mia:**
- **Merge `MEMORY.md` + retrieval results** into entity-keyed structure
- **RAG = short-term retrieval** (web search, file search)
- **Memory = long-term consolidation** (principles, entity facts, trajectory patterns)
- **Both feed into the same DKB query interface**

**Example:**
```markdown
# DKB Query: "How should I handle build-before-send bias?"

## Retrieved Entities:
- [Florian] → weakness: overthinks systems
- [Build-Blocker] → mechanism: pre-build-check.sh

## Retrieved Principles:
- Principle #47: "Enforce constraints via tooling, not discipline"
- Principle #89: "Track sends as the primary success metric"

## Retrieved Trajectories:
- Trajectory #201 (2026-02-06): Build-Blocker implementation
  - Context: 5 zero-send days = €2,105 opportunity cost
  - Solution: Mandatory send before build
  - Outcome: ✅ Reduced build-without-validation incidents

## Synthesized Answer:
Use `pre-build-check.sh` to block builds after 2 features with zero sends. 
This enforces sending discipline automatically (Principle #47 application).
```

**RAG vs. Memory distinction is dissolving** — the real distinction is **retrieval scope** (web/files vs. internal knowledge) and **update frequency** (real-time vs. batch consolidation).

---

### Q4: DualRAG's "dual process" — is this System 1/System 2 for agents?

**Short answer: YES, but inverted from human cognition.**

#### Human System 1/System 2 (Kahneman):
- **System 1:** Fast, intuitive, automatic (e.g., recognize faces)
- **System 2:** Slow, deliberate, effortful (e.g., solve math)

#### DualRAG's RaQ/pKA:
- **pKA (Knowledge Aggregation):** Fast, structured retrieval (entity lookup)
- **RaQ (Reasoning-augmented Querying):** Slow, deliberate reasoning (identify gaps, generate queries)

**The inversion:** In humans, fast = unconscious pattern matching. In agents, fast = explicit database lookup (pKA). Humans deliberate *without* external retrieval; agents deliberate *by triggering* external retrieval.

#### Deeper Parallel (with TWIN.md):

**DualRAG's architecture = TWIN.md's decision framework:**

| DualRAG Component | TWIN.md Equivalent | System |
|-------------------|-------------------|--------|
| **pKA (retrieval)** | "Load relevant context from MEMORY.md" | System 1 |
| **RaQ (reasoning)** | "Evaluate confidence, identify gaps" | System 2 |
| **Closed loop** | "If <90% confidence → ask Florian" | Meta-reasoning |

**Key difference:** TWIN.md operates on *decision confidence*, DualRAG operates on *knowledge completeness*. Both are dual-process, but different axes.

**Extended model for Mia:**

```
┌───────────────────────────────────────────────┐
│         MIA'S COGNITIVE ARCHITECTURE          │
├───────────────────────────────────────────────┤
│  SYSTEM 1 (Fast)           SYSTEM 2 (Slow)    │
│  ├─ pKA-style retrieval    ├─ RaQ-style reasoning │
│  ├─ Pattern matching       ├─ Gap identification  │
│  ├─ MEMORY.md lookup       ├─ TWIN.md evaluation  │
│  └─ Cached principles      └─ Novel problem-solving│
├───────────────────────────────────────────────┤
│         META-SYSTEM (Coordination)             │
│  ├─ Decide when to retrieve (RaQ trigger)      │
│  ├─ Decide when to deliberate (TWIN threshold) │
│  └─ Decide when to escalate (ask Florian)      │
└───────────────────────────────────────────────┘
```

**Implementation implication:**
- **Speed up System 1** → Pre-compute entity embeddings, index MEMORY.md for fast lookup
- **Improve System 2** → Better gap detection (not just "I don't know," but *what specifically* is missing)
- **Tune meta-system** → Calibrate TWIN.md's 90% threshold based on task type (high stakes = lower threshold)

**Answer: Yes, DualRAG is System 1/System 2 for agents, and it should inform how we architect Mia's decision-making.**

---

### Q5: Can self-evolution be MEASURED? (Connects to Γ metric + overconfidence)

**Problem:** All six papers measure *task performance* (accuracy, F1, etc.), but none measure **degree of evolution** itself.

#### What We Need:
A **Γ (Gamma) metric** that quantifies:
1. **Knowledge growth** — how much new knowledge was integrated?
2. **Principle refinement** — how much did existing principles improve?
3. **Trajectory efficiency** — are solutions getting more elegant/faster?
4. **Confidence calibration** — is the agent's self-assessment more accurate?

#### Proposed Γ Metric for Mia:

```python
Γ(t) = w1·ΔK(t) + w2·ΔP(t) + w3·ΔE(t) + w4·ΔC(t)

where:
  ΔK(t) = Knowledge growth = |new entities in MEMORY.md|
                           + |new principles in THE-PROTOCOL.md|
  
  ΔP(t) = Principle quality = Σ [p.success_rate(t) - p.success_rate(t-1)]
                            for all principles p
  
  ΔE(t) = Efficiency gain = [avg tokens per task at t-1] 
                          - [avg tokens per task at t]
  
  ΔC(t) = Calibration improvement = [overconfidence at t-1]
                                  - [overconfidence at t]
          where overconfidence = |predicted success rate - actual success rate|
```

#### Connection to Papers:

| Paper | Measurable Evolution Proxy | Γ Component |
|-------|---------------------------|-------------|
| **EvolveR** | # principles, principle scores | ΔK, ΔP |
| **CoMAS** | Inter-agent agreement improvement | ΔC (calibration) |
| **SE-Agent** | Trajectory diversity, success rate | ΔE, ΔP |
| **DualRAG** | Knowledge Outline size, retrieval precision | ΔK |
| **Atom-Searcher** | Atomic thought score improvement | ΔP, ΔC |
| **MAIN-RAG** | Judge bar accuracy over time | ΔC |

**Current gap:** These papers show *single-task* improvement (within one session), but not *cross-task* evolution (over weeks/months).

#### For Mia:

**Track evolution in `MEMORY.md`:**

```markdown
# Evolution Metrics (Γ)

## 2026-02-10
- ΔK: +3 entities (Build-Blocker, Send-Tracking, Revenue-Focus)
- ΔP: Principle #47 ("tooling > discipline") → 85% success (was 60%)
- ΔE: Avg response time 8.2s (was 12.1s) — 32% faster
- ΔC: Overconfidence 8% (was 15%) — calibration improving

**Γ = 0.4·(3) + 0.3·(0.25) + 0.2·(-3.9) + 0.1·(-0.07) = 0.498**

Interpretation: Positive evolution this week, driven by knowledge growth (ΔK).
Efficiency gain (ΔE) contributed negatively (took longer), but worth it for accuracy.
```

**Overconfidence connection:** Papers 2 (CoMAS) and 6 (MAIN-RAG) indirectly address this:
- **CoMAS:** Multi-agent consensus reduces individual overconfidence (wisdom of crowds)
- **MAIN-RAG:** Adaptive judge bar accounts for score distribution (uncertainty-aware)

**Missing in all papers:** Explicit calibration tracking. They measure accuracy, but not *confidence accuracy* (does the model know when it doesn't know?).

**Mia's advantage:** `TWIN.md` already tracks confidence explicitly (0-100% scale). We just need to:
1. **Log predictions** → `memory/predictions.jsonl`
2. **Track outcomes** → Did high-confidence tasks succeed? Did low-confidence tasks fail?
3. **Compute calibration curve** → Plot predicted vs. actual success rate
4. **Update TWIN.md** → Adjust 90% threshold if systematically over/underconfident

**Answer: Yes, self-evolution CAN be measured, but current papers don't. Mia should implement Γ metric + calibration tracking.**

---

### Q6: What's the ONE insight about how Mia should evolve?

**THE ONE INSIGHT:**

> **Self-improvement is not about better models—it's about better *knowledge organization*.**

#### Why This Matters:

All six papers converge on the same architectural principle:

1. **EvolveR:** Trajectories → Principles (organization as abstraction)
2. **CoMAS:** Discussions → Intrinsic rewards (organization as social learning)
3. **SE-Agent:** Raw trajectories → Trajectory library (organization as cross-task patterns)
4. **DualRAG:** Retrieved docs → Knowledge Outline (organization as entity-structure)
5. **Atom-Searcher:** Reasoning → Atomic thoughts (organization as functional decomposition)
6. **MAIN-RAG:** Raw docs → Filtered + ranked docs (organization as relevance ordering)

**Pattern:** Raw data (trajectories, docs, discussions) → **Structured representation** → Performance gain

**Mia's evolution bottleneck is NOT reasoning capacity** (Sonnet/Opus are powerful). It's **knowledge representation**:
- `memory/*.md` are raw logs (unstructured)
- `MEMORY.md` is prose (not queryable)
- `THE-PROTOCOL.md` is flat (no hierarchy or scoring)
- `kintsugi.md` is failure logs (no principle extraction)

#### The Evolution Strategy:

**Phase 1: Implement EvolveR-style principle extraction** (next 2 weeks)
- Daily: Distill `memory/YYYY-MM-DD.md` → extract 1-3 principles
- Structure: Natural language + knowledge triples + success score
- Storage: New `principles/` directory with entity-keyed files

**Phase 2: Adopt DualRAG-style entity memory** (next 4 weeks)
- Refactor `MEMORY.md` → entity-keyed structure
- Add demand-driven retrieval (not just manual lookup)
- Implement progressive knowledge aggregation (pKA-style)

**Phase 3: Layer CoMAS-style multi-agent learning** (next 8 weeks)
- Formalize sub-agent discussion protocols
- Capture inter-agent consensus → principles
- Implement diversity maintenance (prevent groupthink)

**Phase 4: Add Γ metric tracking** (next 12 weeks)
- Log predictions + outcomes → calibration curve
- Track ΔK, ΔP, ΔE, ΔC weekly
- Auto-adjust TWIN.md threshold based on calibration

**Phase 5: Implement SE-Agent-style trajectory optimization** (next 16 weeks)
- Build `trajectory-library.md` with tagged patterns
- Add revision protocols for failed tasks (not just logging)
- Experiment with cross-trajectory recombination

#### Concrete First Step (This Week):

**Add `principles/EXTRACT.md` template:**

```markdown
# Principle Extraction Protocol

Run this daily on `memory/YYYY-MM-DD.md`:

## Step 1: Identify Learnings
- Scan for: decisions made, mistakes caught, patterns noticed
- Extract: 1-3 candidate principles

## Step 2: Formalize Structure
For each principle:
- **Natural language**: One-sentence description
- **Knowledge triples**: (Entity, Relation, Entity)
- **Context**: When does this apply?
- **Evidence**: Which memory log entry?

## Step 3: Score & Store
- Initial score: s(p) = 1.0 (untested)
- Storage: `principles/CATEGORY/principle-ID.md`
- Index: Add to `principles/INDEX.md`

## Step 4: Prune Weekly
- Remove principles with s(p) < 0.3 after 10+ uses
- Merge semantically duplicate principles
```

**Start with kintsugi.md:** Extract principles from *failures* first (highest learning signal).

---

## Part III: Mia-Specific Recommendations

### Immediate Actions (This Week):

1. **Create `principles/` directory structure:**
   ```
   principles/
   ├── INDEX.md (searchable list)
   ├── build-execution/
   ├── communication/
   ├── decision-making/
   ├── memory-management/
   └── EXTRACT.md (protocol)
   ```

2. **Extract first 10 principles from `kintsugi.md`:**
   - Focus on failures → highest-value learnings
   - Add success scores (track retroactively)

3. **Refactor `MEMORY.md` → entity-keyed structure:**
   - Section per entity (people, systems, concepts)
   - Include triples (not just prose)

4. **Add calibration logging:**
   - Create `memory/predictions.jsonl`
   - Log: {task, confidence, outcome, timestamp}

### Medium-Term (Next Month):

5. **Implement pKA-style knowledge aggregation:**
   - When retrieving info (web/files), structure it entity-first
   - Build `entity-index.json` for fast lookup

6. **Formalize sub-agent discussion protocols:**
   - When spawning multiple agents, capture their debates
   - Distill consensus → principles

7. **Add Γ metric dashboard:**
   - Weekly report: ΔK, ΔP, ΔE, ΔC
   - Track overconfidence trend

### Long-Term (Next Quarter):

8. **Build trajectory library:**
   - Tag successful patterns (e.g., "research-first", "multi-source-validation")
   - Revision protocols for ACTIVE_TASK.md recovery

9. **Experiment with SE-Agent-style recombination:**
   - Cross-task pattern matching
   - Automated trajectory optimization

10. **Integrate with THE-PROTOCOL.md:**
    - Convert flat list → hierarchical principle tree
    - Add success scoring to each protocol step

---

## Part IV: Research Gaps & Future Directions

### What's Missing From All Papers:

1. **Long-term evolution tracking** — all papers show weeks/months, not years
2. **Cross-domain generalization** — most experiments are single-domain (QA, code, etc.)
3. **Failure mode analysis** — what happens when self-improvement goes *wrong*? (drift, overfitting, forgetting)
4. **Human-in-the-loop** — all papers assume autonomous evolution, but Mia needs Florian's oversight
5. **Computational cost analysis** — some methods (SE-Agent) are expensive; real-world feasibility?

### Research Questions for Mia:

1. **Can file-based evolution match training-based methods?**
   - EvolveR shows promise, but direct comparison needed
   - Hypothesis: Files are *more* maintainable (human-auditable, version-controlled)

2. **How much memory is enough?**
   - MEMORY.md grows unbounded → need pruning strategy
   - EvolveR's principle scoring provides one approach

3. **Can we detect evolution "dead ends"?**
   - What if principles start contradicting each other?
   - Need conflict detection + resolution protocol

4. **Is there a "forgetting curve" for agents?**
   - Do old principles decay if unused?
   - EvolveR's pruning suggests yes, but no formal model

5. **How to prevent "groupthink" in multi-agent systems?**
   - CoMAS shows co-evolution works, but diversity maintenance is unclear
   - Mia's sub-agents might converge to single reasoning style

---

## Part V: Conclusion

### Cross-Category Patterns:

1. **Trajectory-level learning > token-level learning** (all papers)
2. **Structured memory > raw logs** (EvolveR, DualRAG, MAIN-RAG)
3. **Process rewards > outcome rewards** (Atom-Searcher)
4. **Multi-agent > single-agent** (CoMAS, MAIN-RAG)
5. **Dual-process architecture dominates** (DualRAG = System 1/System 2)

### Convergence Thesis:

**Agent evolution and RAG are merging into a unified "Dynamic Knowledge Base" paradigm:**
- **Agents evolve by distilling experience into principles** (EvolveR)
- **RAG evolves into structured, persistent memory** (DualRAG)
- **The boundary between "learning" and "retrieval" is disappearing**

### The Future of Self-Improving Agents:

**Tier 1 (Current State of the Art):**
- EvolveR-style principle extraction + DualRAG-style entity memory

**Tier 2 (Emerging):**
- CoMAS-style multi-agent co-evolution + Atom-Searcher-style atomic rewards

**Tier 3 (Speculative):**
- SE-Agent-style trajectory libraries + full meta-learning (learning how to learn)

### Mia's Path Forward:

**Mia is uniquely positioned** because:
1. **Files = Intelligence** is already our Law #1 (aligns with EvolveR)
2. **SOUL.md + TWIN.md + kintsugi.md** form proto-principle structure
3. **Sub-agent spawning** enables CoMAS-style co-evolution
4. **Real-time sessions** require fast retrieval (DualRAG's pKA)

**The missing piece:** Systematic principle extraction + entity-keyed memory + Γ metric.

**Start today:** Extract first 10 principles from `kintsugi.md`. Everything else builds on that foundation.

---

## Appendix: Paper Summary Table

| Paper | Category | Core Innovation | Mia Alignment | Priority |
|-------|----------|----------------|---------------|----------|
| **EvolveR** | Evolution | Self-distillation → principles | ✅✅✅ High (files = principles) | 🔥 **P0** |
| **CoMAS** | Evolution | Multi-agent co-evolution | ✅✅ Medium (sub-agent synergy) | 🟡 P1 |
| **SE-Agent** | Evolution | Trajectory optimization | ✅ Low (too expensive) | 🟢 P2 |
| **DualRAG** | RAG | Dual-process (RaQ + pKA) | ✅✅✅ High (TWIN.md maps directly) | 🔥 **P0** |
| **Atom-Searcher** | RAG | Atomic thought rewards | ✅✅ Medium (process-level scoring) | 🟡 P1 |
| **MAIN-RAG** | RAG | Multi-agent filtering | ✅ Low (noise less critical with good retriever) | 🟢 P2 |

**Implementation order:**
1. **EvolveR + DualRAG** (next 4 weeks) — foundation
2. **Atom-Searcher + CoMAS** (next 8 weeks) — enhancement
3. **SE-Agent + MAIN-RAG** (next 12 weeks) — optimization

---

**End of Deep Research Report**  
**Next action:** Extract 10 principles from `kintsugi.md` and create `principles/INDEX.md`
