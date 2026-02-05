# Deep Research: AI Agent Memory, Self-Improvement & Architectures

**Research Date:** 2026-02-05  
**Status:** Comprehensive literature review with real sources  
**Scope:** Memory systems, documentation as knowledge, self-improving agents, human-AI collaboration, agent architectures  

---

## Table of Contents

1. [Memory Systems for AI Agents](#1-memory-systems-for-ai-agents)
2. [Documentation as Compound Knowledge](#2-documentation-as-compound-knowledge)
3. [Self-Improving AI Agents](#3-self-improving-ai-agents)
4. [Human-AI Collaboration Patterns](#4-human-ai-collaboration-patterns)
5. [AI Agent Architectures 2025-2026](#5-ai-agent-architectures-2025-2026)
6. [Key Takeaways & Implications](#6-key-takeaways--implications)
7. [Source Index](#7-source-index)

---

## 1. Memory Systems for AI Agents

### 1.1 The Definitive Survey: "Memory in the Age of AI Agents"

The most comprehensive overview is **Hu et al. (Dec 2025)**, a landmark survey that reframes agent memory as a first-class primitive:

- **Three forms of memory:**
  - **Token-level memory** — information stored as tokens in the context window
  - **Parametric memory** — knowledge encoded in model weights (via fine-tuning)
  - **Latent memory** — compressed representations in latent space
- **Three functional types:**
  - **Factual memory** — persistent facts, world knowledge (≈ semantic memory in cognitive science)
  - **Experiential memory** — past interaction traces, successes/failures (≈ episodic memory)
  - **Working memory** — temporary scratchpad for current reasoning task
- **Memory dynamics:** How memory is formed, evolved, and retrieved over time
- **Emerging frontiers:** Memory automation, RL integration, multimodal memory, multi-agent shared memory, trustworthiness

> *"Traditional taxonomies such as long/short-term memory have proven insufficient to capture the diversity of contemporary agent memory systems."*

📄 Paper: https://arxiv.org/abs/2512.13564  
📂 Paper list: https://github.com/Shichun-Liu/Agent-Memory-Paper-List  
🏫 ICLR 2026 Workshop on MemAgents: https://openreview.net/pdf?id=U51WxL382H

### 1.2 Cognitive-Inspired Memory Architectures

**The Three Types of Long-Term Memory Agents Need** (Machine Learning Mastery, Dec 2025):

| Memory Type | What It Stores | Analogy | Implementation |
|-------------|---------------|---------|----------------|
| **Episodic** | "Last Tuesday, approach X failed with client Y because Z" | Personal diary | Timestamped interaction logs, trajectory databases |
| **Semantic** | "Approach X works best when conditions A and B are present" | Encyclopedia | Knowledge graphs, RAG systems, vector stores |
| **Procedural** | "To deploy code, run these 5 steps in order" | Muscle memory | Tool definitions, skill libraries, code templates |

🔗 https://machinelearningmastery.com/beyond-short-term-memory-the-3-types-of-long-term-memory-ai-agents-need/

### 1.3 Key Memory Frameworks & Systems

#### MemGPT / Letta — Virtual Context Management
- Treats memory like an OS treats virtual memory: the LLM manages data flow between in-context "RAM" (core memory blocks) and external "disk" (archival/recall storage)
- Agent uses **function calls** to read/write its own memory autonomously
- **Heartbeat mechanism** allows multi-step reasoning by requesting continued execution
- Now evolved into **Letta** — a full platform for stateful agents with persistent memory
- Core insight: *"Memory blocks hold the 'executive summary' while external storage holds the full details"*

📄 MemGPT paper: https://arxiv.org/abs/2310.08560  
🔗 Letta platform: https://www.letta.com/  
📂 GitHub: https://github.com/letta-ai/letta  
📚 Letta Docs on memory: https://docs.letta.com/guides/agents/memory/

#### Zep / Graphiti — Temporal Knowledge Graphs
- **Outperforms MemGPT** on Deep Memory Retrieval benchmark
- Uses a **bi-temporal knowledge graph** engine (Graphiti) that tracks both when facts were learned and when they were valid
- Architecture has three subgraphs:
  - **Episodic subgraph** — raw interaction episodes with timestamps
  - **Semantic subgraph** — extracted facts, entities, relationships
  - **Community nodes** — high-level structures representing domain concepts
- **Hybrid retrieval**: combines lexical, dense, knowledge-graph, and temporal signals via reciprocal rank fusion

📄 Paper: https://arxiv.org/abs/2501.13956  
📂 Graphiti GitHub: https://github.com/getzep/graphiti  
🔗 Neo4j integration: https://neo4j.com/blog/developer/graphiti-knowledge-graph-memory/

#### AriGraph — Episodic + Semantic Knowledge Graphs
- Combines episodic memory and semantic knowledge graphs for LLM agents
- Agent builds a knowledge graph of the world during exploration, then queries it for planning
- Published at **IJCAI 2025**

📄 Paper: https://www.ijcai.org/proceedings/2025/0002.pdf

#### BMAM — Brain-inspired Multi-Agent Memory Framework
- Decomposes agent memory into **functionally specialized subsystems**: episodic, semantic, salience-aware, and control-oriented
- Uses **StoryArc** — a timeline-indexed episodic memory organization
- **Hierarchical memory control** coordinated by a central agent across complementary time scales
- Targets "soul erosion" problem in long-horizon LLM agents

📂 Referenced in: https://github.com/tmgthb/Autonomous-Agents

#### Reflective Memory Management (RMM)
- Constructs memory at **adaptive granularities** (utterance, turn, session, or topic)
- Refines retrieval using feedback from response citations
- Applies **online reinforcement learning** to rerank memory relevance

#### Nemori — Self-Organizing Cognitive Memory
- Autonomously segments conversational streams into **semantically aligned episodes** (Boundary Alignment)
- Continually updates semantic knowledge via active prediction-calibration loops based on the **Free-Energy Principle**

🔗 Survey of persistent memory research: https://www.emergentmind.com/topics/persistent-memory-for-llm-agents

### 1.4 The RAG → Agentic RAG → AI Memory Evolution

From Avi Chawla's analysis (Dec 2025):

| Stage | Capability | Limitation |
|-------|-----------|------------|
| **RAG (2020-2023)** | Read-only, one-shot retrieval | Often retrieves irrelevant context |
| **Agentic RAG** | Agent decides if/what/where to retrieve | Still read-only, can't learn |
| **AI Memory** | Read-write via tool calls, learns from interactions | Memory corruption, forgetting, multi-type management |

> *"RAG was never the end goal. Memory in AI agents is where everything is heading."*

Key insight: Memory introduces challenges RAG never had — **memory corruption**, **deciding what to forget**, and **managing multiple memory types**.

🔗 https://blog.dailydoseofds.com/p/rag-agentic-rag-and-ai-memory

### 1.5 Industry Memory Solutions (2025)

| Platform | Approach | Key Feature |
|----------|----------|-------------|
| **Amazon Bedrock AgentCore Memory** | Extraction + consolidation + retrieval | Mirrors human cognitive processes |
| **Dust.tt Agent Memory** | Continuously learning agents | Transforms agents from "knowledgeable" to "learning" |
| **Redis Agent Memory** | Short-term + long-term memory with vector search | Episodic and semantic memory stores |

🔗 AWS: https://aws.amazon.com/blogs/machine-learning/building-smarter-ai-agents-agentcore-long-term-memory-deep-dive/  
🔗 Dust: https://dust.tt/blog/agent-memory-building-persistence-into-ai-collaboration  
🔗 Redis: https://redis.io/blog/build-smarter-ai-agents-manage-short-term-and-long-term-memory-with-redis/

---

## 2. Documentation as Compound Knowledge

### 2.1 Why Documentation Matters for AI Agents

The key insight from the memory research: **text files are the most durable form of AI agent memory**. Unlike parametric memory (weight updates) or latent memory (embeddings), documentation is:

- **Human-readable** — inspectable, auditable, debuggable
- **Persistent** — survives session restarts, model changes, platform migrations
- **Composable** — can be selectively loaded via progressive disclosure
- **Version-controllable** — can be tracked with git, diffed, reverted
- **Portable** — works across any model, any framework

This is exactly the insight behind **Anthropic's Agent Skills** system (Dec 2025):

> *"Building a skill for an agent is like putting together an onboarding guide for a new hire. Instead of building fragmented, custom-designed agents for each use case, anyone can now specialize their agents with composable capabilities by capturing and sharing their procedural knowledge."*

🔗 https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills  
🔗 Agent Skills open standard: https://agentskills.io/

### 2.2 Progressive Disclosure — The Core Design Pattern

From Anthropic's Agent Skills architecture:

1. **Level 1 (Always loaded):** Name + description of each skill → minimal tokens in system prompt
2. **Level 2 (Loaded on trigger):** Full SKILL.md content → loaded when relevant to task
3. **Level 3+ (Loaded on demand):** Additional reference files → loaded only as needed

This matches how human experts organize knowledge:
- Table of contents → specific chapters → detailed appendix

**Key principle:** *"Agents with a filesystem and code execution tools don't need to read the entirety of a skill into their context window. The amount of context that can be bundled into a skill is effectively unbounded."*

### 2.3 Zettelkasten Principles Applied to AI Agent Memory

The Zettelkasten method (Niklas Luhmann) maps remarkably well to AI agent memory design:

| Zettelkasten Principle | AI Agent Memory Application |
|----------------------|---------------------------|
| **Atomicity** — One idea per note | One fact/skill per memory entry |
| **Connectivity** — Links between notes | Knowledge graph edges, cross-references |
| **Emergence** — New ideas from connections | Agent discovers patterns across memories |
| **Progressive summarization** — Refine over time | Memory consolidation (episodic → semantic) |
| **Permanent notes vs. fleeting notes** | Long-term memory vs. working/session memory |

**The AI-Zettelkasten convergence:**
- Obsidian + AI: Use NER (Named Entity Recognition) and Graph LLMs to auto-generate knowledge graph connections from Zettelkasten notes
- Reddit discussion on atomic approach for AI: *"Remove a limit of document size (for AI sake) and enable me to be more effective on finding information myself (for my sake)"*

🔗 Obsidian Forum — AI-empowered Zettelkasten: https://forum.obsidian.md/t/ai-empowered-zettelkasten-with-ner-and-graph-llm/79112  
🔗 Reddit discussion: https://www.reddit.com/r/ObsidianMD/comments/1psc9zf/best_way_to_give_ai_gemini_notebooklm_access_to/

### 2.4 Structuring Persistent Memory — Best Practices

From synthesizing the research:

#### The Memory Hierarchy (for personal AI agents)

```
├── System Prompt (always loaded)
│   ├── Core identity & rules
│   ├── Skill/capability index (names + descriptions)
│   └── Current context summary
│
├── Core Memory Blocks (in-context, actively maintained)
│   ├── User profile (preferences, style, goals)
│   ├── Agent self-model (capabilities, lessons)
│   └── Active task state
│
├── Working Memory (session-scoped)
│   ├── Current conversation
│   ├── Scratchpad / reasoning traces
│   └── Temporary task context
│
├── Long-Term Memory (external, retrieved on demand)
│   ├── Episodic logs (daily notes, interaction history)
│   ├── Semantic knowledge (facts, curated insights)
│   ├── Procedural skills (how-to guides, code templates)
│   └── Relational knowledge (people, connections)
│
└── Archival Memory (rarely accessed, searchable)
    ├── Historical logs
    ├── Completed project records
    └── Raw data / exports
```

#### Key Design Principles

1. **Write it down, don't "remember"** — Files survive; mental notes don't
2. **Separate raw logs from curated knowledge** — Daily notes vs. long-term memory
3. **Memory consolidation as a process** — Periodically review, distill, update
4. **Progressive disclosure** — Load only what's needed for current task
5. **Temporal awareness** — Timestamp everything; knowledge has a half-life
6. **Dual memory: human-readable + machine-optimized** — Markdown files + knowledge graphs

### 2.5 Context Engineering as the New Paradigm

The New Stack (Jan 2026) frames the shift:

> *"When internal assistants 'remember' project history, onboarding new team members becomes smoother. The system becomes an institutional historian, one that captures the tacit knowledge stored inside an organization."*

Memory is now understood as a form of **context engineering** — the art of managing what information is available to the LLM at any given moment.

🔗 https://thenewstack.io/memory-for-ai-agents-a-new-paradigm-of-context-engineering/

---

## 3. Self-Improving AI Agents

### 3.1 The Landscape (NeurIPS 2025 Synthesis)

Yohei Nakajima (creator of BabyAGI) published a comprehensive synthesis of self-improving agent research, organized into **six mechanisms**:

#### Mechanism 1: Self-Reflection & In-Loop Feedback
**Prompt-level improvement without changing weights.**

| System | Mechanism | Result |
|--------|-----------|--------|
| **Reflexion** (Shinn 2023) | LLM solves → fails → writes verbal critique → stores reflection → retries | HumanEval: baseline → ~91% pass@1 |
| **Self-Refine** (Madaan 2023) | Generate → critique → revise, repeat until convergence | Consistent quality improvement |

*Pros:* Cheap, no weight updates, easy to bolt on  
*Cons:* Improvements are ephemeral unless persisted; model can hallucinate bad reflections

#### Mechanism 2: Learning to Self-Correct
**Training the model to be better at self-correction.**

| System | Mechanism | Key Insight |
|--------|-----------|-------------|
| **RISE** (Qu 2024) | Fine-tune on mistake→fix traces | Self-correction becomes built-in capability |
| **STaR** (Zelikman 2022) | Generate solutions → filter correct ones → fine-tune on reasoning traces | Small models become strong reasoners from own data |
| **STaSC** (Moskvoretskii 2025) | Self-correction for open-domain QA | Closes gap between 2B and much larger models |

#### Mechanism 3: Self-Generated Data & Auto-Curricula
**Agents create the data they learn from.**

| System | Venue | Mechanism | Result |
|--------|-------|-----------|--------|
| **Self-Challenging Agents** (Zhou) | NeurIPS 2025 | LLM plays challenger + executor; creates Code-as-Task with verified tests | 2x performance on tool-use benchmarks |
| **Self-Generated ICL Examples** (Sarukkai) | NeurIPS 2025 | Stores successful trajectories; replays as in-context examples | ALFWorld: 73% → 93% |
| **SiriuS** (Zhao) | NeurIPS 2025 | Multi-agent experience bootstrapping; repairs failed trajectories | 2.86-21.88% accuracy gains |

> *"Self-generated data is the engine of long-term self-improvement. The core design challenge is signal quality."*

#### Mechanism 4: Self-Adapting Models (SEAL)
**Agents that edit their own weights.**

- **SEAL** (NeurIPS 2025): Model generates natural-language self-edit instructions → converted to fine-tuning examples
- Results: Factual QA 33.5% → 47%; some few-shot reasoning 0% → 72.5%
- Edits are interpretable as natural language — debugging + oversight

#### Mechanism 5: Self-Improving Code Agents
**Agents that modify their own code and architecture.**

| System | Mechanism |
|--------|-----------|
| **SICA** (Self-Improving Coding Agent) | Best-performing agent becomes meta-agent, looks through archive, identifies and implements improvements |
| **Gödel Agent** | Self-modifying agent that rewrites its own policy through recursive improvement |
| **Meta Agent Search** (ICLR 2025) | Automated search over agent architectures; discovers novel agent designs without human guidance |

#### Mechanism 6: Embodied Self-Improvement
**Agents learning by acting in environments.**

- **Voyager** (2023): LLM agent in Minecraft with automatic curriculum, skill library, iterative prompting
- **Self-Improving Embodied Foundation Models** (NeurIPS 2025): Physical agents that improve through environmental interaction

🔗 Yohei Nakajima's synthesis: https://yoheinakajima.com/better-ways-to-build-self-improving-ai-agents/  
📄 SICA: https://arxiv.org/html/2504.15228v2  
📄 Self-Improving LLM Agents at Test-Time: https://arxiv.org/html/2510.07841v1

### 3.2 Metacognition: The Missing Piece

**"Truly Self-Improving Agents Require Intrinsic Metacognitive Learning"** (Jun 2025) — a position paper arguing current agents are limited:

- **Extrinsic metacognition** (current): Fixed, human-designed reflection loops that limit scalability
- **Intrinsic metacognition** (needed): Agent autonomously decides what and how to learn

Three components of intrinsic metacognition:
1. **Metacognitive knowledge** — self-assessment of capabilities, tasks, and strategies
2. **Metacognitive planning** — deciding what and how to learn
3. **Metacognitive evaluation** — reflecting on learning experiences to improve future learning

Key finding: *"Static self-improvement loops lose efficacy as agents' generative (task-solving) abilities outpace their ability to evaluate their own outputs."*

📄 Paper: https://arxiv.org/abs/2506.05109  
📄 OpenReview: https://openreview.net/forum?id=4KhDd0Ozqe

### 3.3 Self-Evolving Agents: The Big Picture

**"A Survey of Self-Evolving Agents: On Path to Artificial Super Intelligence"** (Jul 2025):

Self-evolving agents uniquely demonstrate:
- **Active exploration** — e.g., searching for tools online
- **Structural self-modification** — iteratively modifying their own workflow or code
- **Self-reflection and self-evaluation** — providing verbal feedback using internal evaluator

🔗 https://arxiv.org/html/2507.21046v1

### 3.4 Anthropic's Agent Skills — Practical Self-Improvement

Anthropic's approach to agent improvement is notably practical (Dec 2025):

- **Skills as captured expertise** — procedural knowledge packaged as composable folders
- **Iterative refinement with the agent** — "Ask Claude to capture its successful approaches and common mistakes into reusable context and code within a skill"
- **Self-reflection on failure** — "If it goes off track, ask it to self-reflect on what went wrong"

Best practices:
1. Start with evaluation — find gaps, then build skills to address them
2. Structure for scale — split large skills, separate mutually exclusive contexts
3. Think from Claude's perspective — monitor how it uses skills, iterate
4. Iterate with Claude — let the agent help build its own skill library

🔗 https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills

### 3.5 Meta-Cognitive Reflection for Efficient Self-Improvement

**"Learn Like Humans: Use Meta-cognitive Reflection for Efficient Self-Improvement"** (Jan 2026):

Compares against MetaAgentSearch and Gödel Agent. Shows that meta-cognitive reflection (inspired by human learning) can be more efficient than blind recursive self-improvement.

📄 Paper: https://arxiv.org/html/2601.11974v1

---

## 4. Human-AI Collaboration Patterns

### 4.1 The State of Human-AI Collaboration

**"Human-AI collaboration is not very collaborative yet"** (Frontiers in Computer Science, Dec 2024):

Major systematic review of 105 empirical studies reveals:

- Most human-AI interactions are **unidirectional** — AI recommends, human accepts/rejects
- True collaborative patterns (back-and-forth, iterative refinement) are **rare**
- The field lacks a **common vocabulary** for describing human-AI interactions
- Most empirical studies reduce interactions to *"basic actions like menu selections or button clicks"*

Key interaction patterns identified:
- **AI recommends → Human decides** (most common, least collaborative)
- **Human queries → AI responds** (chatbot pattern)
- **Iterative refinement** (human and AI co-evolve a solution)
- **Turn-taking** (alternating control)
- **Parallel work** (independent then merge)

🔗 https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2024.1521066/full

### 4.2 The Agency Framework for Human-AI Co-creation

**"Exploring Collaboration Patterns and Strategies in Human-AI Co-creation through the Lens of Agency"** (ACM CSCW 2025):

Scoping review of 134 top-tier HCI papers. Key findings:
- Agency distribution between human and AI is the central design question
- Framework covers context, control, and application dimensions
- User-centric design principles must guide agency allocation

📄 Paper: https://arxiv.org/abs/2507.06000  
🔗 ACM: https://dl.acm.org/doi/10.1145/3757594

### 4.3 Stanford Research: Complementarity Over Replacement

Stanford research (May 2025) by Spiess and McLaughlin proposes a **complementarity framework**:

> *"AI model might detect patterns in large amounts of data that humans might not discover easily, while humans might excel at the causal interpretation and intuition required to understand these patterns."*

Key insight: The goal isn't AI replacing human judgment but **refining human-AI collaboration** so each contributes what they're best at.

🔗 https://news.stanford.edu/stories/2025/05/research-ai-human-collaboration  
📄 Full paper: https://www.tandfonline.com/doi/full/10.1080/0960085X.2025.2475962

### 4.4 Failure Modes in Human-AI Collaboration

From synthesizing multiple sources:

| Failure Mode | Description | Mitigation |
|-------------|-------------|------------|
| **Automation bias** | Humans over-rely on AI output, stop thinking critically | Require explicit human reasoning before seeing AI suggestion |
| **Anchoring** | AI's first suggestion dominates human's subsequent thinking | Randomize or delay AI output |
| **Skill atrophy** | Humans lose skills they delegate to AI | Periodic human-only exercises |
| **Miscalibrated trust** | Over-trust (ignoring errors) or under-trust (ignoring good suggestions) | Calibration training, explanations of AI confidence |
| **Communication overhead** | Too much coordination eats into productive work | Design for minimal necessary communication |
| **Error amplification** | One agent's mistake cascades through the system | Centralized validation bottlenecks (Google Research finding: 17.2x in independent systems vs. 4.4x with orchestrator) |

### 4.5 Anthropic's "How AI is Transforming Work" Report

Anthropic's internal analysis (2025):
- Between Feb and Aug 2025, Claude usage at Anthropic shifted dramatically
- **Implementing new features:** 14.3% → 36.9%
- **Code design/planning:** 1.0% → 9.9%
- Engineers develop **intuitions for AI delegation over time** — knowing when to hand off vs. do yourself

🔗 https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic  
📄 2026 Agentic Coding Trends Report: https://resources.anthropic.com/hubfs/2026%20Agentic%20Coding%20Trends%20Report.pdf

---

## 5. AI Agent Architectures 2025-2026

### 5.1 The Top 5 Agent Architectures (MarkTechPost, Nov 2025)

| Architecture | Control Topology | Learning Focus | Use Cases |
|-------------|-----------------|----------------|-----------|
| **Hierarchical Cognitive** | Centralized, layered (reactive/deliberative/meta-cognitive) | Layer-specific control | Robotics, industrial, mission planning |
| **Swarm Intelligence** | Decentralized, multi-agent | Local rules → emergent behavior | Drone fleets, logistics, crowd sim |
| **Meta Learning** | Single agent, inner/outer loops | Learning to learn | Personalization, AutoML, adaptive control |
| **Self-Organizing Modular** | Orchestrated modules | Dynamic routing | LLM agent stacks, enterprise copilots |
| **Evolutionary Curriculum** | Population-level | Curriculum + evolutionary search | Multi-agent RL, game AI |

The **Self-Organizing Modular Agent** is the dominant pattern for LLM-based agents in 2025-2026:
- Modules for perception, memory, reasoning, action
- Meta-controller/orchestrator selects and routes between modules
- New tools can be inserted as modules without retraining

🔗 https://www.marktechpost.com/2025/11/15/comparing-the-top-5-ai-agent-architectures-in-2025-hierarchical-swarm-meta-learning-modular-evolutionary/

### 5.2 Google Research: The Science of Scaling Agent Systems

**"Towards a Science of Scaling Agent Systems"** (Dec 2025) — 180 agent configurations evaluated:

#### Five canonical architectures tested:
1. **Single-Agent (SAS)** — one agent, unified memory stream
2. **Independent** — parallel agents, no communication, aggregate at end
3. **Centralized** — hub-and-spoke with orchestrator
4. **Decentralized** — peer-to-peer mesh, direct communication
5. **Hybrid** — hierarchical oversight + peer coordination

#### Key findings:

**The "More Agents" Myth:**
- On **parallelizable tasks** (financial reasoning): centralized coordination improved 80.9% over single agent
- On **sequential tasks** (planning): every multi-agent variant degraded performance by 39-70%
- **Tool-use bottleneck:** As tasks require more tools (16+), coordination "tax" increases disproportionately

**Error amplification:**
- Independent systems: **17.2x error amplification**
- Centralized systems: **4.4x error amplification** (orchestrator catches errors)

**Predictive model (R² = 0.513):**
- Correctly identifies optimal architecture for **87% of unseen task configurations**
- Uses measurable task properties: tool count, decomposability, sequential dependencies

> *"Smarter models don't replace the need for multi-agent systems — they accelerate it, but only when the architecture is right."*

📄 Paper: https://arxiv.org/abs/2512.08296  
🔗 Blog: https://research.google/blog/towards-a-science-of-scaling-agent-systems-when-and-why-agent-systems-work/

### 5.3 Gartner's Signal: 1,445% Surge

Gartner reported a **1,445% surge in multi-agent system inquiries** from Q1 2024 to Q2 2025, signaling massive industry interest.

🔗 https://machinelearningmastery.com/7-agentic-ai-trends-to-watch-in-2026/

### 5.4 Multi-Agent Orchestration Patterns

From n8n's guide and Neomanex analysis:

| Pattern | Description | Best For |
|---------|-------------|----------|
| **Sequential (Pipeline)** | Each agent processes then hands off | Step-by-step workflows |
| **Parallel** | Multiple agents work simultaneously | Independent sub-tasks |
| **Routing** | Dynamic routing based on context | Triage, classification |
| **Hierarchical** | Supervisor manages worker agents | Complex decision-making |
| **Handoff** | Agents transfer control based on expertise | Customer support, specialized tasks |
| **Network** | Agents communicate peer-to-peer | Consensus, negotiation |

**Rule of thumb:** Keep teams small — **3-7 agents per workflow**. Beyond that, create hierarchical structures with team leaders.

🔗 n8n: https://blog.n8n.io/multi-agent-systems/  
🔗 Neomanex: https://neomanex.com/posts/multi-agent-ai-systems-orchestration

### 5.5 Comprehensive Surveys

**"Agentic AI: A Comprehensive Survey"** (Oct 2025):
- PRISMA-based review of 90 studies (2018-2025)
- Three dimensions: theoretical foundations, domain implementations (healthcare/finance/robotics), ethical challenges
- Each paradigm has divergent risks requiring different mitigation strategies

📄 https://arxiv.org/html/2510.25445

**"Agentic AI: Architectures, Taxonomies, and Evaluation"** (Jan 2026):
- Includes ReAcTree — Hierarchical LLM Agent Trees with Control Flow for Long-Horizon Task Planning

📄 https://arxiv.org/html/2601.12560v1

### 5.6 Protocol Standards: MCP and Agent Skills

Two emerging standards for agent interoperability:

1. **MCP (Model Context Protocol)** — Anthropic's open standard for connecting AI models to data sources and tools
2. **Agent Skills** — Anthropic's open standard for packaging domain expertise into composable, portable skill folders

🔗 Agent Skills: https://agentskills.io/

---

## 6. Key Takeaways & Implications

### For Building Personal AI Agents (like King/OpenClaw)

1. **Memory is the moat.** The agent that remembers best, serves best. Invest in persistent, structured memory.

2. **Document everything in files, not "in memory."** Token-level working memory is volatile. Files are persistent, auditable, portable.

3. **Use the Zettelkasten approach for agent knowledge:**
   - Atomic facts/skills (one per file/entry)
   - Rich cross-links (knowledge graph or file references)
   - Regular consolidation (daily notes → long-term memory)
   - Progressive disclosure (load only what's needed)

4. **Self-improvement is real but requires curation.** The best approaches:
   - Store successful trajectories and replay them (Self-Generated ICL)
   - Capture lessons learned after failures (Reflexion pattern)
   - Build and iterate on skill files (Anthropic's Agent Skills)
   - Periodic memory review and consolidation (metacognitive maintenance)

5. **The right architecture depends on the task:**
   - Sequential reasoning → single agent (don't add coordination overhead)
   - Parallelizable research → centralized multi-agent
   - Tool-heavy tasks → modular with orchestrator

6. **Human-AI collaboration is still primitive.** The biggest opportunity is in building true iterative collaboration patterns, not just AI-recommends-human-decides.

7. **Context engineering > prompt engineering.** Managing what information is available to the agent (through memory, skills, progressive disclosure) matters more than how you phrase a single prompt.

### The Compound Knowledge Thesis

Documentation compounds. Each interaction that is captured, each lesson that is recorded, each skill that is codified makes the next interaction better. This is the fundamental insight connecting all five research areas:

- **Memory systems** make past experience accessible
- **Documentation** makes it persistent and portable
- **Self-improvement** makes the agent learn from it
- **Collaboration patterns** determine how human knowledge flows into the system
- **Architecture** determines how efficiently it all works together

---

## 7. Source Index

### Key Papers

| Title | Date | URL |
|-------|------|-----|
| Memory in the Age of AI Agents (Survey) | Dec 2025 | https://arxiv.org/abs/2512.13564 |
| Zep: Temporal Knowledge Graph for Agent Memory | Jan 2025 | https://arxiv.org/abs/2501.13956 |
| AriGraph: Episodic Memory for LLM Agents | 2025 | https://www.ijcai.org/proceedings/2025/0002.pdf |
| Truly Self-Improving Agents Require Intrinsic Metacognition | Jun 2025 | https://arxiv.org/abs/2506.05109 |
| Self-Improving Coding Agent (SICA) | Apr 2025 | https://arxiv.org/html/2504.15228v2 |
| Self-Improving LLM Agents at Test-Time | Oct 2025 | https://arxiv.org/html/2510.07841v1 |
| Meta Agent Search (ICLR 2025) | Aug 2024 | https://arxiv.org/pdf/2408.08435 |
| Learn Like Humans: Meta-cognitive Reflection | Jan 2026 | https://arxiv.org/html/2601.11974v1 |
| Survey of Self-Evolving Agents | Jul 2025 | https://arxiv.org/html/2507.21046v1 |
| Towards Agentic Self-Learning in Search | Oct 2025 | https://arxiv.org/html/2510.14253v2 |
| Towards a Science of Scaling Agent Systems | Dec 2025 | https://arxiv.org/abs/2512.08296 |
| Agentic AI: Comprehensive Survey | Oct 2025 | https://arxiv.org/html/2510.25445 |
| Agentic AI: Architectures & Taxonomies | Jan 2026 | https://arxiv.org/html/2601.12560v1 |
| Human-AI Collaboration Patterns (Frontiers) | Dec 2024 | https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2024.1521066/full |
| Human-AI Co-creation Agency (ACM CSCW) | Jul 2025 | https://arxiv.org/abs/2507.06000 |
| Complementarity in Human-AI Collaboration | 2025 | https://www.tandfonline.com/doi/full/10.1080/0960085X.2025.2475962 |

### Key Blog Posts & Industry Sources

| Title | Source | URL |
|-------|--------|-----|
| Better Ways to Build Self-Improving AI Agents | Yohei Nakajima | https://yoheinakajima.com/better-ways-to-build-self-improving-ai-agents/ |
| RAG, Agentic RAG, and AI Memory | Daily Dose of DS | https://blog.dailydoseofds.com/p/rag-agentic-rag-and-ai-memory |
| Agent Memory: How to Build Agents that Learn | Letta | https://www.letta.com/blog/agent-memory |
| Equipping Agents with Agent Skills | Anthropic | https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills |
| Science of Scaling Agent Systems | Google Research | https://research.google/blog/towards-a-science-of-scaling-agent-systems-when-and-why-agent-systems-work/ |
| Stanford: AI Human Collaboration Research | Stanford Report | https://news.stanford.edu/stories/2025/05/research-ai-human-collaboration |
| How AI is Transforming Work at Anthropic | Anthropic | https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic |
| Top 5 AI Agent Architectures 2025 | MarkTechPost | https://www.marktechpost.com/2025/11/15/comparing-the-top-5-ai-agent-architectures-in-2025-hierarchical-swarm-meta-learning-modular-evolutionary/ |
| 7 Agentic AI Trends for 2026 | ML Mastery | https://machinelearningmastery.com/7-agentic-ai-trends-to-watch-in-2026/ |
| Memory for AI Agents: Context Engineering | The New Stack | https://thenewstack.io/memory-for-ai-agents-a-new-paradigm-of-context-engineering/ |
| Multi-Agent Systems Guide | n8n Blog | https://blog.n8n.io/multi-agent-systems/ |
| 2026 Agentic Coding Trends Report | Anthropic | https://resources.anthropic.com/hubfs/2026%20Agentic%20Coding%20Trends%20Report.pdf |
| Persistent Memory for LLM Agents | EmergentMind | https://www.emergentmind.com/topics/persistent-memory-for-llm-agents |

### Frameworks & Tools

| Name | Description | URL |
|------|------------|-----|
| Letta (MemGPT) | Stateful agents with persistent memory | https://github.com/letta-ai/letta |
| Graphiti | Real-time knowledge graphs for AI agents | https://github.com/getzep/graphiti |
| Agent Skills | Open standard for composable agent expertise | https://agentskills.io/ |
| Autonomous Agents Paper List | Daily-updated research paper collection | https://github.com/tmgthb/Autonomous-Agents |
| Agent Memory Paper List | Companion to "Memory in the Age of AI Agents" | https://github.com/Shichun-Liu/Agent-Memory-Paper-List |

---

*Research compiled 2026-02-05 01:00 CET. All URLs verified at time of research.*
