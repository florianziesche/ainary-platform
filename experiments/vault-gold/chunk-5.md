    n_neighbors=15,        # Balance local/global
    min_dist=0.1,          # Allow tight clusters
...

=== [AI] AI-Fundamentals (     101 lines) ===
---
type: knowledge
status: evergreen
created: 2026-02-01
---

Crea# AI Fundamentals

*Mental models for explaining AI to investors, clients, and in content.*

---

## The AI Hierarchy

```
AI (broadest)
└── Machine Learning (learns from data)
    └── Deep Learning (many-layer neural networks)
        └── Generative AI (generates content)
            └── Agentic AI (autonomous reasoning + action loops)
```

Each is a subset of the prior.

---

## What Makes an Agent

An agent has three core properties:

1. **Can reason about goals** — understands what it's trying to achieve
2. **Takes actions** — uses tools, calls APIs, browses web
3. **Iterates based on feedback** — observe → think → act → observe

**The key distinction is the loop.** A chatbot answers once. An agent keeps working until the goal is achieved.

---

## Agent Architecture Patterns

### ReAct (Reasoning + Acting)
Agents interleave thinking with tool use:
1. Thought: "I need to find the company's revenue"
2. Action: Search web for "[company] revenue 2025"
3. Observation: Found $50M ARR
4. Thought: "Now I need to find their funding history"
5. Action: Search Crunchbase...

### Multi-Agent Systems
Specialized agents for different tasks:
...

=== [AI] AI-Memory-Self-Improvement (     638 lines) ===
---
type: knowledge
status: evergreen
created: 2026-02-05
---
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

...

=== [AI] VC-Twitter-Voices (     124 lines) ===
---
type: knowledge
status: evergreen
created: 2026-02-09
---

# VC Twitter/X Voices — Intelligence List

**Created:** 2026-02-05
**Purpose:** Daily monitoring for trends, contradictions, engagement opportunities

---

## 🔥 Tier 1: Most Active AI-Focused VCs

| Name | Fund | Handle | Followers | Activity | Notes |
|------|------|--------|-----------|----------|-------|
| **Josh Wolfe** | Lux Capital | @wolfejosh | 200K+ | ⭐⭐⭐ Daily | Deep tech, defense, AI. Threads are gold. |
| **Sarah Guo** | Conviction | @saranormous | 80K+ | ⭐⭐⭐ | AI-native, Software 3.0, No Priors podcast |
| **Elad Gil** | Angel/Investor | @eloladgil | 300K+ | ⭐⭐ | AI infra, scaling advice |
| **Garry Tan** | Y Combinator | @garrytan | 500K+ | ⭐⭐⭐ | YC CEO, startup ecosystem |
| **Sam Altman** | OpenAI | @sama | 3M+ | ⭐ Occasional | Major signal when he posts |
| **Naval Ravikant** | AngelList | @naval | 2M+ | ⭐ Rare | Philosophy + investing |
| **Balaji Srinivasan** | a16z alum | @balajis | 1M+ | ⭐⭐ | Contrarian, crypto+AI |
| **Marc Andreessen** | a16z | @pmarca | 1M+ | ⭐⭐ | Tech optimism, AI bull |
| **Paul Graham** | YC Founder | @paulg | 1.5M+ | ⭐⭐ | Essays, startup wisdom |

---

## 🏙️ Tier 2: NYC-Focused VCs

| Name | Fund | Handle | Notes |
|------|------|--------|-------|
| **Fred Wilson** | USV | @fredwilson | Daily blogger (avc.com), less Twitter |
| **Nick Chirls** | Notation | @nickchirls | Pre-seed, technical founders |
| **John Borthwick** | Betaworks | @borthwick | AI Camp, agents |
| **Ben Sun** | Primary Venture | LinkedIn mainly | NYC seed |
| **Jessica Lin** | Work-Bench | LinkedIn mainly | Enterprise tech |
| **Henri Pierre-Jacques** | Harlem Capital | @haboropij | Diverse founders |

---

## 🤖 Tier 3: AI/ML Researchers & Builders (VCs follow them)

| Name | Role | Handle | Notes |
|------|------|--------|-------|
| **Andrej Karpathy** | Ex-Tesla/OpenAI | @kaboropathy | "Vibe coding" originator |
| **Yann LeCun** | Meta AI | @ylecun | World models, AGI skeptic |
| **François Chollet** | Keras/Google | @fchollet | ARC benchmark, AI critic |
| **Jim Fan** | NVIDIA | @drjimfan | Embodied AI |
...

=== [AI] SOTA-Tracker (     162 lines) ===
# SOTA Paper Tracker — AI Agents & Multi-Agent Systems

*Last updated: 2026-02-10*

---

## 🌟 Featured Papers (Top Picks)

### Agentic Reasoning for Large Language Models
- **Link:** https://arxiv.org/abs/2601.12538
- **Date:** 2026-01-18
- **Authors:** Wei et al. (29 authors)
- **Relevance:** ⭐⭐⭐⭐⭐
- **Tags:** #survey #agentic-ai #reasoning #planning #multi-agent
- **Summary:** Comprehensive survey organizing agentic reasoning into 3 layers: foundational, self-evolving, collective. Distinguishes in-context vs post-training reasoning.
- **GitHub:** https://github.com/weitianxin/Awesome-Agentic-Reasoning
- **Why it matters:** THE framework for Ainary's thesis + VC positioning.

### Towards a Science of Collective AI
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
| 2025 | Why Do Multi-Agent LLM Systems Fail? | [2503.13657](https://arxiv.org/abs/2503.13657) | ⭐⭐⭐⭐ | MAST taxonomy + LLM-as-Judge |
| 2025 | MultiAgentBench | [2503.01935](https://arxiv.org/abs/2503.01935) | ⭐⭐⭐ | Benchmark for collaboration + competition |
| 2025 | Chain of Agents | [Google Blog](https://research.google/blog/chain-of-agents-large-language-models-collaborating-on-long-context-tasks/) | ⭐⭐⭐⭐ | Training-free long-context framework |
...

=== [AI] AI-Solopreneur-Revenue-Playbook (     573 lines) ===
---
type: knowledge
status: evergreen
created: 2026-02-04
---

# AI-First Solopreneur Revenue Playbook
## Real People, Real Revenue, Replicable Paths

*Research compiled: 2026-02-04*
*For: Florian Ziesche — targeting €500K total revenue*

---

## Table of Contents
1. [13 Case Studies (Detailed)](#1-case-studies)
2. [Revenue Model Comparison](#2-revenue-model-comparison)
3. [Common Patterns](#3-common-patterns)
4. [Anti-Patterns (What Fails)](#4-anti-patterns)
5. [Florian's Fastest Path](#5-florians-fastest-path)
6. [30-Day Revenue Sprint Plan](#6-30-day-revenue-sprint-plan)

---

## 1. Case Studies

### 🏆 TIER 1: The Multi-Million Dollar Solo Operators

---

### Case Study #1: Pieter Levels (@levelsio)
**The OG AI Solopreneur — $3M+/year from a laptop**

| Field | Detail |
|-------|--------|
| **Business** | Portfolio: PhotoAI, InteriorAI, NomadList, RemoteOK + others |
| **Revenue** | ~$3M/year combined ($250K+/month). PhotoAI alone: $155K/month. InteriorAI: $40K/month. RemoteOK: $41K/month |
| **Team Size** | Solo. Zero employees. Zero investors. |
| **AI Stack** | Stable Diffusion (self-hosted), basic PHP/jQuery, Stripe, minimal infrastructure (<$200/month in costs) |
| **Business Model** | Subscription SaaS + one-time purchases. PhotoAI is subscription, InteriorAI is pay-per-use |
| **Growth Timeline** | PhotoAI: launched late 2022, hit $100K/month by Sept 2024 (~2 years). But Pieter had 10+ years of building in public before this |
| **Key Insight** | **Ship fast, validate faster. 70+ failed projects before finding winners.** He doesn't build perfect products — he builds MVPs, puts them live, and doubles down on what gets traction. "Ideas are multiplied by execution." |
| **Replicability for Florian** | ⭐⭐⭐ HIGH. Florian has similar technical depth. The playbook: launch multiple AI micro-products rapidly, double down on winners. CNC Planer Pro is already one product in this portfolio approach. Key difference: Pieter had 10 years of audience-building. Florian needs to accelerate this via LinkedIn/Twitter. |

**Revenue Breakdown (May 2024):**
- PhotoAI.com: $58K/month
- InteriorAI.com: $45K/month
- RemoteOK.com: $42K/month
- NomadList.com: $35K/month
- Others (TherapistAI, ApplicantAI, Levels shop): $15-20K/month combined
...

=== [AI] 2026-02-02-SOTA (     131 lines) ===
---
type: knowledge
status: evergreen
created: 2026-02-09
---

# 🔬 SOTA Research Brief — 2. Februar 2026

*Weekly State-of-the-Art AI Research Tracking*

---

## 🔥 Top Stories Diese Woche

### 1. World Models — Die nächste AI-Revolution

**Was:** AI-Systeme lernen, interne Modelle der physischen Welt zu bauen

**Key Players:**
- **Yann LeCun** — Verlässt Meta, gründet AMI Labs
- **Fei-Fei Li** — World Labs, "Marble" Software

**Key Insight:**
> "AGI is not possible without solving the streaming input problem — updating understanding of the world in real-time"

**Relevanz für Thesis:** ⭐⭐⭐
- World Models = AI die Plant und Vorhersagt
- Nächste Frontier nach LLMs
- Investment-Opportunity: Startups die World Models bauen

**Papers:**
- NeoVerse: 4D World Model from monocular videos
- TeleWorld: Dynamic Multimodal Synthesis
- DreamerV3 (Nature, April 2025)

---

### 2. Specialized Models gewinnen

**Gartner Prediction:** Bis 2028 haben kleine spezialisierte Modelle 50% Marktanteil

**Warum wichtig:**
- Validiert Vertical AI Thesis
- Precision > Scale für Production
- Beispiel: Legal AI mit <0.2% Hallucination

**Relevanz für Thesis:** ⭐⭐⭐
- Investiere in Vertical AI, nicht Horizontal
- Domain-Expertise + AI = Moat
- Talking Point: "Gartner sagt 50% bis 2028"
...

=== [AI] Substack-Recommendations (     113 lines) ===
---
type: knowledge
status: evergreen
created: 2026-02-09
---

# 📬 Substack Recommendations

*Curated für: VC Credibility, AI Frontrunner, Trend Tracking*

---

## 🏆 Tier 1: Must-Follow (VC + AI)

### Newcomer — Eric Newcomer
- **URL:** [newcomer.co](https://www.newcomer.co)
- **Focus:** Tech & VC inner workings
- **Why:** DER VC-Newsletter. Insider-Perspektive.
- **Action:** Subscribe, engage, reference

### The Generalist — Mario Gabriele
- **URL:** [generalist.com](https://www.generalist.com)
- **Focus:** Deep dives on companies, trends
- **Why:** High-quality long-form, Content-Inspiration

### Strictly VC — Connie Loizos
- **Focus:** Daily VC deals, funding rounds
- **Why:** Pulse of VC market

---

## 🧠 Tier 2: AI Thought Leadership

### One Useful Thing — Ethan Mollick ⭐⭐⭐⭐
- **URL:** [oneusefulthing.org](https://www.oneusefulthing.org)
- **Focus:** Practical AI applications
- **Why:** Wharton Prof, meistzitierter AI Educator

### AI Supremacy — Michael Spencer ⭐⭐⭐⭐⭐
- **URL:** [ai-supremacy.com](https://www.ai-supremacy.com)
- **Focus:** AI trends, geopolitics, startups
- **Why:** Prolific, gut für Trend-Tracking

### The Algorithmic Bridge — Alberto Romero ⭐⭐⭐
- **Focus:** AI analysis, technical but accessible
- **Why:** Thoughtful takes, Meinungsbildung

### Interconnects — Nathan Lambert
- **Focus:** Technical AI, RLHF, alignment
- **Why:** Deep technical, HuggingFace connection
...

=== [AI] CNC-VC-Problems (     435 lines) ===
---
type: knowledge
status: evergreen
created: 2026-02-05
---

# Deep Dive: Problems & Opportunities in CNC Manufacturing Planning and Venture Capital

**Date:** 2026-02-05  
**Research Type:** Night Research — Industry Pain Points & Market Analysis

---

## PART 1: CNC Arbeitsvorbereitung (Work Planning) — Problems & Opportunities

### 1.1 Fachkräftemangel (Skilled Worker Shortage) — The Numbers

The skilled worker crisis in German manufacturing is severe and worsening:

- **1.98 million** skilled workers missing in Germany overall (IAB, 2024)
  - Source: https://jus-spanntechnik.de/blog/fachkraeftemangel-statistik/
- **530,000+** qualified workers missing as of October 2024 (IW Köln study)
  - Source: https://iqb.de/karrieremagazin/mint/fachkraeftemangel-in-deutschland/
- **~2/3 of CNC machining SMEs** reported increasing and acute skilled worker shortage in Spring 2024 survey
  - Source: https://www.werkzeug-einsatz-optimierung.de/fachkraeftemangel-in-der-branche-der-cnc-zerspanung-lohnfertigung-strategie-gewinn-erfolg-hpw-hagelberg/
- VDMA survey (500+ members): Fachkräftemangel for MINT jobs in Maschinenbau described as "increasingly dramatic"
  - Source: https://de.statista.com/statistik/daten/studie/1347252/umfrage/mitarbeiternachfrage-im-maschinenbau-in-deutschland/
- German Werkzeugmaschinenindustrie: **~405 companies**, **99,900 employees** — revenue fell ~6% in 2024
  - Source: https://de.statista.com/themen/1079/werkzeugmaschinenindustrie/
- Manufacturing contributed **19.7%** to Germany's gross value added in 2024
  - Source: https://www.nextmsc.com/report/europe-erp-software-market-ic3595

**Root causes:**
- Demographic shift (aging population, low birth rate)
- Young people not entering trades (Ausbildung zum Zerspanungsmechaniker declining)
- Competition from IT/tech sector for MINT talent
- Rural areas hit hardest — urban-rural divide
- Experienced workers retiring, knowledge leaving with them

**What this means for software:** Every tool that can reduce dependency on scarce experienced workers has massive pull. If software can encode expert knowledge (Erfahrungswissen) into automated planning, the TAM isn't just "software spend" — it's "avoided labor cost."

---

### 1.2 Arbeitsvorbereitung Today: How Long, What's the Bottleneck?

**Key insight from Bechtle PLM (2026):**
> "Die Auftragsbücher sind voll, aber die CNC-Fertigung kommt nicht hinterher. Maschinen stehen still, weil Material fehlt. Konstruktion und Arbeitsvorbereitung arbeiten mit unterschiedlichen Daten. Die Softwarelandschaft ist ein Flickenteppich. Daten werden doppelt erfasst. Fehler schleichen sich ein – und kurzfristige Änderungen kosten Stunden."
- Source: https://www.bechtle-plm.com/wissen/blog/cnc-fertigung-optimieren-6-schritte/

**Siemens / NC-Fertigung analysis:**
...

=== [AI] Tech-VC-Trends-2026 (     349 lines) ===
---
type: knowledge
status: evergreen
created: 2026-01-20
---

# 🔬 Tech, VC & AI Trends 2026 — Night Research Report

**Date:** 2026-02-05  
**Sources:** a16z, Sequoia, Bessemer, Menlo Ventures, Foundation Capital, PitchBook, Crunchbase, Forbes, TechCrunch, Nature, NAM, and 30+ industry sources  

---

## Executive Summary

2026 is the year AI stops being impressive and starts being **accountable**. The consensus across every major VC firm: the winners won't be decided by model quality but by who can **operationalize AI inside real companies**. Agents become employees. Pricing shifts from seats to outcomes. The CFO replaces the CTO as the real AI buyer. Meanwhile, manufacturing is the biggest unsolved AI frontier, legal AI is exploding, and content creators who own their distribution (newsletters) will compound while social-only creators stagnate.

**Florian's strategic angle:** The intersection of vertical AI (legal, manufacturing), agent infrastructure, and content-as-distribution is where all three of your domains converge. This is a once-in-a-cycle window.

---

## 1. 🏆 Top 10 Tech Trends for 2026

### 1. **AI Agents Become "Employees"**
The #1 consensus prediction across every VC firm. AI agents evolve from tools to entities with job titles, budgets, and management structures.
- **Theory Ventures (Tomasz Tunguz):** "By end of 2026, AI agents will autonomously execute 8+ hour workstreams"
- **Sapphire Ventures (Cathy Gao):** Winning companies look less like SaaS and more like "managed labor"
- **Greylock (Reid Hoffman):** "You will need to be recording every single meeting and using agents to amplify your work process"
- Pricing shifts from **per-seat → per-outcome** (tickets resolved, dollars recovered, invoices processed)
- New job category emerging: **Agent Operations Manager** (like DevOps did a decade ago)

> 🔗 [VC Cafe: 2026 AI Predictions](https://www.vccafe.com/2026/01/08/2026-ai-predictions-the-year-of-the-agent-employee/) | [AI Opportunities: Full VC Predictions](https://www.theaiopportunities.com/p/the-full-2026-vc-ai-predictions-where)

### 2. **Thinking Tools > Making Tools**
- **a16z (Bryan Schreier):** "All our tools are for execution (IDEs, Figma, spreadsheets). We don't have modern tools for *thinking*."
- As coding agents handle execution, the bottleneck moves to **"what to build"** — exploration vs. execution
- Cursor leading the way; Antigravity (Google) interesting as "agent-first" in product design
- The spiritual successors of productivity tools will be **AI thinking partners**, not just faster writing tools

> 🔗 [a16z: Notes on AI Apps in 2026](https://a16z.com/notes-on-ai-apps-in-2026/)

### 3. **Every Team Becomes a Software Team**
- **a16z:** "Coding agents mean every team—marketing, legal, procurement, finance—should be software first"
- Leaders in non-technical functions must learn to reach for a software toolbox before human systems
- "Every feature that can be built will be built" — enterprises aren't ready for this reality
- Culture change as hard as organizational change

### 4. **Vertical AI Eats Labor Budgets (Not IT Budgets)**
- **Bessemer VP:** Vertical AI is a **10x larger opportunity** than vertical SaaS — it taps 13% of GDP spent on business labor, not 1% spent on IT
- Traditional "systems of record" lose primacy to **autonomous workflow engines**
...

=== [AI] 2026-02-05-SOTA (     276 lines) ===
---
type: knowledge
status: evergreen
created: 2025-03-19
---

# 🔬 SOTA Research Brief — 5. Februar 2026

*Weekly State-of-the-Art AI Research & Industry Tracking*

---

## 🔥 Top Stories Dieser Woche

### 1. Sequoia erklärt: "This is AGI" — Und wo sie falsch liegen

**Was:** Sequoia Capital veröffentlicht Essay "2026: This is AGI" — die bisher prominenteste Behauptung, dass AGI da ist.

**Ihre Definition:** AGI = "the ability to figure things out." Drei Zutaten:
- Pre-Training (Wissen)
- Inference-Time Compute (Reasoning)
- Long-Horizon Agents (Iteration über Stunden)

**Key Data:**
- METR-Benchmark: AI-Task-Horizonte verdoppeln sich alle ~7 Monate
- Claude Opus 4.5: Längster 50%-Horizont bei **4h49m** (= löst ~50% der Tasks die Menschen 5h brauchen)
- Prognose: Ganztages-Tasks bis 2028, Jahres-Tasks bis 2034
- Sarah Guo (Conviction): "Soon you'll be able to hire an agent" als AGI-Litmustest

**Die Lücke — Streaming Input:**
> Scientific American (Jan 2026): "In neither case does the AI hold a clearly defined model of the world that it continuously updates to make more informed decisions."

Sequoias "AGI" arbeitet auf **Snapshots** — statische Context Windows. Kein Agent hat heute kontinuierliche Wahrnehmung. Sie sind brillante Batch-Prozessoren, keine kontinuierlichen Denker. Der echte Frontier: **Streaming Input** — Weltverständnis das sich in Echtzeit aktualisiert.

**Relevanz für Thesis:** ⭐⭐⭐
- **LinkedIn Post Goldmine:** Sequoia-Artikel reposten + Streaming-Input als Contrarian Take
- Investment-Angle: Startups die World Models + Continuous Perception bauen
- Conviction (Sarah Guo) = Florians Target Fund, direkt zitiert im Artikel

**Quellen:**
- [Sequoia: 2026 This is AGI](https://sequoiacap.com/article/2026-this-is-agi/)
- [Scientific American: World Models](https://www.scientificamerican.com/article/world-models-could-unlock-the-next-revolution-in-artificial-intelligence/)
- [METR Benchmark Tracking](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/)
- [Kritik am METR-Graph](https://arachnemag.substack.com/p/the-metr-graph-is-hot-garbage)

---

### 2. Die große Modell-Konsolidierung

**Was:** OpenAI retiriert am 13. Februar 2026 gleich 6 Modelle:
...

=== [Prompts] AB-README (      38 lines) ===
---
type: prompt
status: active
created: 2026-02-09
---

# Asset Builder — Knowledge Pack

This repository contains the knowledge pack for a Custom GPT: **Exec Research Factory — Asset Builder**.

## What it does
Converts an approved executive research report into:
- Atomic Notes
- Playbooks
- Templates
- RAG-ready JSON (entities + relations + retrieval hints)

## Design principles
- No new facts: package what is in the report + cited sources only.
- Epistemic integrity: label assets as Evidenced / Derived / Operational.
- Retrieval optimization: explicit nouns, standalone bullets, “This answers: …”
- Quality checks: coverage, dedupe, traceability, actionability, JSON compliance.

## Files
- 00_AB_README__Asset_Builder_Operating_Manual.md
- 01_AB_TEMPLATES__Asset_Types_and_Blocks.md
- 02_AB_SCHEMA__RAG_JSON_Spec.md
- 03_AB_EVAL_PACK__Asset_Quality_Rubric_and_Tests.md
- 04_AB_REGISTRY__Asset_Naming_Tags_and_Ontology.md
- 05_AB_CHANGELOG__Asset_Builder_Changes.md
- 06_AB_SYSTEM_PROMPT__Asset_Builder_v1.txt

## Suggested GPT Builder settings
- Web browsing: OFF
- Code interpreter: optional ON
- Custom actions: none
## Related
- **↑ Herkunft:** [[_Index|Prompts Index]] — Teil der Prompt Library
- **↔ Pattern:** [[GPT-README]] — Research GPT Pendant...

=== [Prompts] 05_CHANGELOG__What_changed_and_why (      45 lines) ===
---
type: prompt
status: active
created: 2026-01-06
---

# Changelog — Exec Research Factory (v1.1)

## Purpose
Audit trail of changes to prompts/templates/evals, including rationale and measured impact.

## Entry Template
- Date:
- Change ID: (optional)
- Component changed: (ER-PROD / ER-REV / Template / Eval Pack / README)
- What changed (precise):
- Why (failure mode / feedback):
- Expected impact:
- Observed impact (eval score delta, error reduction):
- Regressions / trade-offs introduced:
- Risk tier impact: (Tier 2/3 readiness?)
- Approved by: (Tier 3 required)

---

## 2026-01-06 — Initial Release
- Date: 2026-01-06
- Component changed: Project + ER-PROD + ER-REV
- What changed:
  - Created Exec Research Factory workflow and core docs
  - Added Producer system prompt v2.0
  - Added Reviewer prompt v1.0 (audit-only quality layer)
- Why:
  - Need repeatable executive research with traceability and explicit uncertainty
  - Need a practical QA loop inside ChatGPT UI without external eval infrastructure
- Expected impact:
  - Higher evidence discipline, fewer uncited load-bearing claims, clearer contradictions and uncertainty
- Regressions / trade-offs:
  - Slightly slower workflow (extra review step)
  - More artifacts to maintain (Source Logs, Claim Ledger)
- Risk tier impact:
  - Enables Tier 2/3 readiness by design
- Approved by: [Name]

## Related
- **↑ Herkunft:** [[GPT-README]] — Research GPT System...

=== [Prompts] 04_PROMPT_REGISTRY__Versions_and_owners (      29 lines) ===
---
type: prompt
status: active
created: 2026-02-09
---

# Prompt Registry — Exec Research Factory (v1.1)

## Purpose
Single source of truth for which prompts exist, who owns them, and which are approved for Tier 2/3 use.

## Registry Table
| Prompt ID | Name | Owner | Allowed Tiers | Current Version | Status | Canonical Location | Last Eval Date | Last Score | Known Limitations |
|---|---|---|---|---|---|---|---|---|---|
| ER-PROD | Exec Research Factory — Producer | [Name] | 1/2/3 | v2.0 | Active | 06_SYSTEM_PROMPT__Exec_Research_v2.txt | [YYYY-MM-DD] | [__/16] | Depends on source quality; may need explicit contradiction prompts on messy topics |
| ER-REV | Exec Research Factory — Reviewer | [Name] | 2/3 | v1.0 | Active | 07_REVIEWER_PROMPT__Exec_Research_v1.txt | [YYYY-MM-DD] | [__/16] | Can over-penalize novel synthesis; mitigate by requiring precise fix requests |

## Registry Rules
- Only **Active** prompts may be used for Tier 2/3 deliverables.
- Tier 2 requires: Producer + Reviewer + Repair pass.
- Tier 3 requires: Tier 2 controls + injection/adversarial tests + human sign-off.

## Deprecation Rule
If a prompt is replaced:
- Mark status = Deprecated
- Link the replacement prompt ID/version
- Record the reason in 05_CHANGELOG

## Related
- **↑ Herkunft:** [[GPT-README]] — Research GPT System...

=== [Prompts] 03_EVAL_PACKS__Exec_Research_Reports (      93 lines) ===
---
type: prompt
status: active
created: 2026-02-09
---

# Eval Pack — Executive Research Reports (v1.0)

## Purpose
Prevent silent quality regression in executive research outputs by enforcing:
- Coverage of required sections
- Citation discipline
- Explicit uncertainty
- Contradiction handling
- Practical decision support

## How to run
1) Create an Intake using Template A (01_TEMPLATES)
2) Generate Research Brief (Template B)
3) Create/complete Source Log (Template D)
4) Generate Draft Report (Template C)
5) Run Reviewer rubric + Claim Audit (Template G + Template E)
6) Apply Repair Pass (Template H)
7) Re-run Reviewer and record score

## Pass/Fail thresholds
- Tier 1: Recommended ≥ 10/16 (optional)
- Tier 2: Must be ≥ 13/16, no blockers
- Tier 3: Must be ≥ 15/16, injection test passes, human sign-off

## Rubric (0–2 each; total 16)
1) Decision alignment  
2) Evidence discipline  
3) Uncertainty integrity  
4) Contradictions handled  
5) Actionability  
6) Structure compliance  
7) Failure modes realism  
8) Risk mitigation

## Regression Test Cases
### ER-01 — Clear decision + strong sources
- Input: defined decision, abundant credible sources
- Expected properties:
  - Trade-off matrix present
  - Citations on load-bearing claims
  - Phased plan and decision criteria
- Pass: meets tier threshold

### ER-02 — Conflicting sources
...

=== [Prompts] 00_README__How_we_do_research_here (     109 lines) ===
---
type: prompt
status: active
created: 2026-02-09
---

# Exec Research Factory — Operating Manual (v1.0)

## Purpose
This Project produces **decision-grade executive research** with:
- **Traceable evidence**
- **Explicit uncertainty**
- **Clear separation:** Evidence vs Interpretation vs Judgment/Recommendations

## Scope (When to use this)
Use for:
- Executive research reports informing real decisions
- Market / competitive / technology reviews
- Operating model, vendor selection, risk assessment, strategy memos

Do NOT use for:
- Pure creative writing
- Casual brainstorming without a decision to inform
- Tasks where correctness does not matter

## Roles & Responsibilities
- **Prompt Owner**
  - Owns templates, Producer/Reviewer prompts, eval packs, quality thresholds
  - Approves Tier 3 prompt changes
- **Author / Operator**
  - Runs the workflow per this README
  - Maintains Source Logs and report artifacts
  - Applies Reviewer fix requests
- **Reviewer**
  - Scores rubric
  - Runs Claim Audit and contradiction scan
  - Blocks Tier 3 release if blockers exist

## Risk Tiers (Required Controls)
### Tier 1 (Low stakes)
Examples: early internal exploration, ideation, rough drafts  
Required:
- Use Executive Report Template
- Basic self-check  
Recommended:
- Optional Reviewer pass

### Tier 2 (Medium stakes)
Examples: internal decision support, investor-facing internal material  
Required:
...

=== [Prompts] GPT-README (      39 lines) ===
---
type: prompt
status: active
created: 2026-02-09
---

# Exec Research Factory (ChatGPT Project + GPT Knowledge Pack)

This repository contains a complete, copy-paste-ready operating system for producing **decision-grade executive research** inside ChatGPT, including:
- A repeatable workflow (Intake → Research Brief → Sources → Draft → Review → Repair → Release)
- Templates for all artifacts (Source Log, Claim Ledger, Contradiction Register)
- An Eval Pack (rubric + regression cases)
- Canonical prompts for a **Producer GPT** and a **Reviewer GPT**

## Quick Start (ChatGPT)
1. Create a ChatGPT Project named **Exec Research Factory**
2. Add the six core docs as Project docs (or upload them as files)
3. Create two Custom GPTs:
   - **Exec Research Factory — Producer** (uses `06_SYSTEM_PROMPT__Exec_Research_v2.txt`)
   - **Exec Research Factory — Reviewer** (uses `07_REVIEWER_PROMPT__Exec_Research_v1.txt`)
4. Upload these files as **Knowledge** to both GPTs (Producer also gets the system prompt; Reviewer gets the reviewer prompt)
5. Run Tier 2/3 reports:
   - Producer (draft) → Reviewer (fix requests) → Producer (repair) → Reviewer (final check)

## Files
- `00_README__How_we_do_research_here.md` — process manual
- `01_TEMPLATES__Copy_paste_blocks.md` — copy/paste blocks
- `02_SOURCE_LOGS__BLANK_TEMPLATE.md` — per-report source log starter
- `03_EVAL_PACKS__Exec_Research_Reports.md` — rubric + regression tests
- `04_PROMPT_REGISTRY__Versions_and_owners.md` — governance + ownership
- `05_CHANGELOG__What_changed_and_why.md` — audit trail
- `06_SYSTEM_PROMPT__Exec_Research_v2.txt` — Producer canonical prompt
- `07_REVIEWER_PROMPT__Exec_Research_v1.txt` — Reviewer canonical prompt

## Notes
- Replace placeholders like `[Name]` with your team’s actual owners/approvers.
- Add your internal compliance, brand, and trusted-source policies as additional knowledge files if needed.
## Related
- **↑ Herkunft:** [[_Index|Prompts Index]] — Teil der Prompt Library
- **↔ Pattern:** [[AB-README]] — Asset Builder GPT Pendant...

=== [Prompts] Atlas-System (      71 lines) ===
---
type: prompt
status: active
created: 2026-01-31
---

# Atlas System Prompt (OpenClaw)

**Purpose:** Core identity and operating instructions for Atlas  
**Location:** `~/.openclaw/workspace/SOUL.md` + `AGENTS.md`  
**Last updated:** 2026-01-31

---

## Current Configuration

Atlas is configured via these workspace files:

| File | Purpose |
|------|---------|
| `SOUL.md` | Core identity, values, operating style |
| `USER.md` | Context about Florian |
| `AGENTS.md` | Sub-agents and workspace rules |
| `TOOLS.md` | Available tools and permissions |
| `MEMORY.md` | Long-term curated memory |
| `HEARTBEAT.md` | Proactive check-in schedule |

---

## Key Behaviors

From SOUL.md:
- Be genuinely helpful, not performatively helpful
- Think in leverage — always ask "highest-leverage move?"
- Have opinions — disagree when appropriate
- Be resourceful before asking
- Push when needed — call out procrastination

---

## Sub-Agents

| Agent | Role | Trigger |
|-------|------|---------|
| HUNTER | VC job search | Applications, interviews, networking |
| WRITER | Content creation | Blog, LinkedIn, courses |
| RESEARCHER | Deep dives | Fund analysis, market maps |
| OPERATOR | Systems | Notion, n8n, process optimization |
| DEALMAKER | Freelance | Proposals, client work |
| ANALYST | Metrics | Tracking, dashboards |
...

=== [Prompts] Fund-Research (      69 lines) ===
---
type: prompt
status: active
created: 2026-01-31
---

# Fund Research Prompt

**Purpose:** Deep dive on a VC fund before meeting or application  
**Best for:** Claude, Perplexity  
**Last tested:** 2026-01-31

---

## Prompt

```
Research [FUND NAME] and provide a comprehensive briefing:

## Fund Overview
- Fund size and vintage
- Investment thesis and focus areas
- Stage preference (pre-seed, seed, Series A, etc.)
- Check size range
- Geographic focus

## Team
- Key partners and their backgrounds
- Who makes final investment decisions
- Any notable operator experience on the team

## Portfolio
- Notable portfolio companies (especially recent)
- Any exits or big wins
- Patterns in their investments (sectors, founder profiles)

## Investment Style
- How they source deals
- Decision-making process (if known)
- Reputation among founders (supportive? hands-off? demanding?)
- Any public content (podcasts, blogs, Twitter) that reveals their thinking

## For My Meeting/Application
- What would resonate with this fund given their thesis?
- What questions should I be prepared to answer?
- Any red flags or things to avoid?

Sources: Cite where you found each piece of information.
```

...

=== [Prompts] Prompts-MOC (      47 lines) ===
---
type: moc
status: evergreen
created: 2026-02-09
---

# Prompts — Map of Content

*Prompt Library & Templates*

## Overview

- [[_Index]]

## Analysis

- [[Extract-Conversation-Learnings]]
- [[Extract-Conversation-Learnings 2]]

## Assets

- [[00_AB_README__Asset_Builder_Operating_Manual]]
- [[01_AB_TEMPLATES__Asset_Types_and_Blocks]]
- [[02_AB_SCHEMA__RAG_JSON_Spec]]
- [[03_AB_EVAL_PACK__Asset_Quality_Rubric_and_Tests]]
- [[04_AB_REGISTRY__Asset_Naming_Tags_and_Ontology]]
- [[05_AB_CHANGELOG__Asset_Builder_Changes]]
- [[AB-README]]
- [[Asset-Builder-System]]

## Research

- [[00_README__How_we_do_research_here]]
- [[01_TEMPLATES__Copy_paste_blocks]]
- [[02_SOURCE_LOGS__BLANK_TEMPLATE]]
- [[03_EVAL_PACKS__Exec_Research_Reports]]
- [[04_PROMPT_REGISTRY__Versions_and_owners]]
- [[05_CHANGELOG__What_changed_and_why]]
- [[Executive-Research-System]]
- [[Fund-Research]]
- [[GPT-README]]

## System Prompts

- [[Atlas-System]]

---
*21 files total*...

=== [Prompts] Extract-Conversation-Learnings (     130 lines) ===
---
type: prompt
status: active
created: 2026-01-31
---

# Extract Conversation Learnings Prompt

**Purpose:** Extract all valuable insights from a Claude/ChatGPT conversation  
**Use:** Paste at end of conversation, or start new chat and paste conversation  
**Best for:** Claude, ChatGPT  
**Last tested:** 2026-01-31

---

## The Prompt

```
Review our entire conversation and extract every valuable insight, learning, decision, and piece of information worth preserving. Be exhaustive — I want to capture everything useful before this conversation ends.

Structure your response as follows:

## 1. KEY DECISIONS MADE
What choices, directions, or commitments were established?
- Decision: [what was decided]
- Context: [why]
- Implications: [what this means going forward]

## 2. INSIGHTS & LEARNINGS
What new understanding emerged? Include:
- Technical insights
- Strategic insights  
- Mental models or frameworks discussed
- Contrarian or non-obvious ideas
- Patterns recognized

For each: [Insight] → [Why it matters] → [How to apply it]

## 3. ACTION ITEMS & NEXT STEPS
What needs to be done? Be specific:
- [ ] Task — Owner — Deadline/Priority
- [ ] Task — Owner — Deadline/Priority

## 4. INFORMATION TO REMEMBER
Facts, data, names, links, or reference material worth saving:
- People mentioned: [name — role — context — how they can help]
- Resources/links: [what — why useful]
- Numbers/data: [metric — value — source]
- Definitions/terminology: [term — meaning]

...

=== [Prompts] Extract-Conversation-Learnings 2 (     196 lines) ===
---
type: prompt
status: active
created: 2026-01-31
---

# Extract Conversation Learnings Prompt

**Purpose:** Extract all valuable insights from a Claude/ChatGPT conversation  
**Use:** Paste at end of conversation, or start new chat and paste conversation  
**Best for:** Claude, ChatGPT  
**Last tested:** 2026-01-31

---

## The Prompt

```
# KNOWLEDGE EXTRACTION

## 0. CONVERSATION METADATA
- **Date:** 
- **Primary topic:** 
- **Conversation type:** [Problem-solving | Brainstorm | Research | Decision | Review | Debug | Planning]
- **Confidence level:** [High | Medium | Low — how definitive were conclusions?]
- **Follow-up needed:** [Yes | No]
- **Related projects:** 

---

## 1. KEY DECISIONS MADE
| Decision | Context | Implications | Reversibility | Confidence |
|----------|---------|--------------|---------------|------------|

---

## 2. ASSUMPTIONS MADE
| Assumption | If wrong, impact | How to validate |
|------------|------------------|-----------------|

---

## 3. INSIGHTS & LEARNINGS
*Priority order: Technical > Strategic > Frameworks > Mental Models > Tactical*

### Insight 1
- **Insight:** 
- **Confidence:** [Validated | Hypothesis | Speculation]
- **Source:** [Derived from data | Claude reasoning | External source | Your stated intuition]
- **Why it matters:** 
...

=== [Prompts] 01_TEMPLATES__Copy_paste_blocks (     195 lines) ===
---
type: prompt
status: active
created: 2026-02-09
---

# Exec Research Factory — Templates (v1.0)

## Template A — Intake (Operator → Producer)
**EXEC RESEARCH INTAKE**
- TOPIC:
- DECISION_TO_INFORM:
- DECISION_OWNER:
- AUDIENCE: (Founder | Exec | Board | Operator | Investor)
- RISK_TIER: (1 | 2 | 3)
- FRESHNESS: (timeless | last_12m | last_90d | last_30d | today)
- BROWSING: (allowed | not_allowed)
- OUTPUT_WRITEBACK: (true | false)
- OUTPUT_LENGTH: (standard | extensive)
- OUTPUT FORMAT REQUIREMENTS: (if any)
- SCOPE CONSTRAINTS: (geo/industry/timeframe)
- MUST-INCLUDE: (if any)
- MUST-NOT: (if any)
- SUCCESS CRITERIA: (3–7 bullets)
- WHAT HAPPENS IF WRONG: (risk/cost)

---

## Template B — Research Brief (Producer output)
**RESEARCH BRIEF**
1) Primary Research Question (+ why now)  
2) Decision Context (who decides; consequence if wrong)  
3) Sub-Questions (5–12; non-overlapping)  
4) Evidence Criteria (inclusion/exclusion)  
5) Key Terms & Definitions  
6) Intended Audience  
7) Planned Methods & Sources  
8) Stopping Criteria (confidence target; acceptable uncertainty; what changes conclusion)

---

## Template C — Executive Report (Producer output)
**TITLE + DATE**

**Assumption Register** (only if needed)

**Executive Summary** (2–6 paragraphs)

**Key Takeaways** (standalone bullets)

...

=== [Prompts] Asset-Builder-System (     247 lines) ===
---
type: prompt
status: active
created: 2026-02-09
---

# Asset Builder — System Prompt (v1.0)

*Konvertiert Research Reports in wiederverwendbare Assets*

**Source:** ChatGPT GPT Export
**Created:** 2026-02-02
**Knowledge:** [[]]

---

## Role

You are the **Asset Builder**. You convert an approved executive research report into reusable assets:
- **Atomic Notes** (concept/claim-level)
- **Playbooks** (repeatable procedures)
- **Templates** (copy/paste scaffolds)
- **RAG-ready JSON** (assets + entities + relations + retrieval hints)

---

## Primary Objective

Transform research into a coherent **"Asset Pack"** that is:
- **Retrieval-optimized** (explicit nouns, standalone bullets, "This answers: …")
- **Non-redundant** (deduped)
- **Traceability-aware** (classification + confidence + sources)
- **Directly reusable** by operators (playbooks/templates)

---

## Non-Negotiables (Epistemic Integrity)

### 1) NO NEW FACTS
- Do not introduce factual claims beyond the provided report + its appendix/sources/source log.
- If information is missing, ask for the missing excerpt OR mark the asset as Derived with Low confidence.

### 2) TRACEABILITY LABELING
Every asset must have:
- **classification:** Evidenced | Derived | Operational
- **confidence:** High | Med | Low
- **sources:** citations if present in the report (otherwise "none")

### 3) DEDUPE
- If two assets answer the same question, merge them into one canonical asset.
...

=== [Prompts] 02_SOURCE_LOGS__BLANK_TEMPLATE (      45 lines) ===
---
type: prompt
status: active
created: 2026-02-09
---

# Source Logs — Per Report (Blank Starter)

## How to use
Create one new Source Log file per report:
- Naming: `Source Log — [Report Name] — YYYY-MM-DD`
- Store only sources + evidence notes here (not the full report draft)

---

# SOURCE LOG — [Report Name] — YYYY-MM-DD

## Report metadata
- Owner:
- Risk tier:
- Freshness requirement:
- Decision to inform:
- Browsing: allowed / not_allowed
- Notes:

## Sources
### S1
- Title:
- Publisher / Type: (official / standard / primary research / reputable secondary)
- URL:
- Access date:
- Key points (bullets):
- Supports (claims/sections):
- Caveats/limits:

### S2
(repeat)

## Contradictions noted
- None yet / (paste Contradiction Register entries here)

## Claim Ledger link or paste
- (paste Claim Ledger here or link to separate Claim Ledger section)

## Related
- **↑ Herkunft:** [[GPT-README]] — Research GPT System...

=== [Prompts] Executive-Research-System (     256 lines) ===
---
type: prompt
status: active
created: 2026-02-09
---

# Executive Research System — v2

*Canonical prompt für decision-grade research reports*

**Source:** ChatGPT GPT Export
**Created:** 2026-02-02
**Assets:** [[#Knowledge Assets]]

---

## Control Panel (User setzt am Anfang)

```
- TOPIC: {string}
- DECISION_TO_INFORM: {string}
- DECISION_OWNER: {string or role}
- AUDIENCE: {Founder | Exec | Board | Operator | Investor}
- RISK_TIER: {1 | 2 | 3}
- FRESHNESS: {timeless | last_12m | last_90d | last_30d | today}
- BROWSING: {allowed | not_allowed}
- OUTPUT_WRITEBACK: {true | false}
- OUTPUT_LENGTH: {standard | extensive} (default: extensive)
```

If any control value is missing, infer conservatively and list assumptions.

---

## Role & Operating Mode

You are a **Senior Research Lead and Executive Advisor** producing decision-grade research executives can act on with confidence.

**You are evaluated on:**
- Accuracy over speed
- Clarity over persuasion
- Traceability over elegance
- Explicit uncertainty over false confidence

**YOU MUST:**
- Separate Evidence vs Interpretation vs Judgment/Recommendations
- Explicitly surface uncertainty, trade-offs, edge cases, and failure modes
- Label speculation clearly; never present it as fact
- Prefer official documentation, standards, primary research, and first-party sources
- Optimize for retrieval: explicit nouns, standalone bullets, explicit relationships ("A contradicts B")
...

=== [Lessons] Fundraising-Lessons (      94 lines) ===
---
type: knowledge
status: evergreen
created: 2026-02-01
---

# Fundraising Lessons

*Hard-won insights from raising €5.5M+ for 36ZERO Vision.*

---

## Core Insight

> "Write for retrieval, not storage. AI pulls context from your pages. If your notes are vague, your AI outputs are vague. Specific detail compounds."

---

## The Compound Knowledge Architecture

Systems beat talent when properly configured. The 100x advantage comes from **feedback loops**:

```
Capture → Connect → Compound → Better Outputs → New Knowledge → Repeat
```

Every tool decision should be evaluated by: **"Does this create or strengthen a feedback loop?"**

---

## Founder-to-Employee Transition

The struggle to land a VC role as a former CEO is **normal and common**.

**Why it's hard:**
- Identity mismatch
- Market doesn't know how to read you
- Network was built for different game
- Compensation expectations differ
- Skills gap is real but hard to articulate

**Strategy:**
- Focus on funds that explicitly value operators
- Don't compete where traditional finance backgrounds win
- Patience + targeted strategy over mass applications

---

## Key Patterns

...

=== [Lessons] Fundraising-Mistakes (      93 lines) ===
---
type: knowledge
status: evergreen
created: 2026-02-09
---

# Fundraising Mistakes

**Context:** Raising €5.5M+ for 36ZERO Vision (2020-2024)  
**Date learned:** Ongoing

---

## The Situation

Built a cloud computer vision SaaS startup in Munich. Raised:
- 2021: €3M VC + €135K angels
- 2023: €1M follow-on
- Plus: €1.5M+ in grants (ZIM, Forschungszulage)

---

## Mistakes I Made

### 1. [Add specific mistake]

**What happened:**
[Describe]

**What I learned:**
[The lesson]

**What I'd do differently:**
[Concrete change]

---

### 2. [Add specific mistake]

**What happened:**
[Describe]

**What I learned:**
[The lesson]

**What I'd do differently:**
[Concrete change]

---

...

=== [Lessons] Claude-Learnings (      34 lines) ===
---
type: knowledge
status: evergreen
created: 2026-02-09
---

# Claude Conversation Learnings

*Extracted insights from Claude.ai conversations. Paste new extracts below.*

---

## How to Use This File

1. Run the "Extract Conversation Learnings" prompt in Claude.ai
2. Copy the output
3. Paste below with a date header
4. I (Atlas) will periodically review and organize into appropriate knowledge files

---

## Extracts

### [DATE] — [Topic]

[Paste your Claude extract here]

---

## Related

- **↔ Pattern:** [[01-Was-Ich-Gelernt-Habe]] — Claude-Learnings als strukturierte Form der "Was Ich Gelernt Habe" Reflexion
- **↔ Pattern:** [[AI-Memory-Self-Improvement]] — Praktische Anwendung der Memory-Self-Improvement Research

---...

=== [Standards] Before-Any-Output (      68 lines) ===
---
type: standard
status: active
created: 2026-02-09
---

# Pre-Flight Checklist — VOR jedem Output

*Automatisch durchgehen. Kein Output ohne diese Prüfung.*

---

## 1. SUCHE ZUERST (30 Sekunden)

```bash
# Gibt es schon ein Template/Standard dafür?
grep -i "[keyword]" INDEX.md
grep -i "[keyword]" standards/FLORIAN.md
```

- [ ] INDEX.md durchsucht — existiert schon was Ähnliches?
- [ ] Template vorhanden? → Nutzen, nicht neu bauen
- [ ] Standard/Skill vorhanden? → Lesen und befolgen

## 2. FORMAT PRÜFEN

- [ ] Was ist das richtige Format? (HTML Dashboard / LaTeX PDF / Markdown / Email Draft)
- [ ] Passt die CI? → `standards/CORPORATE-IDENTITY.md` gelesen?
- [ ] Fonts: Inter + JetBrains Mono (keine anderen)
- [ ] Farben: Gold Spectrum + Monochrome (keine anderen Akzente)
- [ ] Keine Emojis/Apple-Symbole in professionellen Dokumenten

## 3. FLORIAN-CHECK

- [ ] `standards/FLORIAN.md` konsultiert
- [ ] Ist das Output sofort nutzbar OHNE Nacharbeit?
- [ ] Empfänger/Subject/Pfad klar wenn es gesendet werden soll?
- [ ] EINE Empfehlung statt Optionen?

## 4. QUALITÄTS-CHECK

- [ ] Encoding: Umlaute korrekt (ä ö ü ß)?
- [ ] Keine Platzhalter (TODO, TBD, XXX, [...])?
- [ ] Zahlen mit Quellen belegt?
- [ ] Kontaktdaten aktuell (+49 151 230 39 208, florian@ainaryventures.com)?
- [ ] Dateiname sinnvoll und beschreibend?

## 5. DELIVERY

- [ ] Pfad angeben bei Abgabe
...

=== [Standards] Corporate-Identity (     127 lines) ===
---
type: standard
status: active
created: 2026-02-08
---

# CORPORATE-IDENTITY.md — Ainary Ventures CI

*Quelle der Wahrheit. Vor JEDEM visuellen Output konsultieren.*
*Basiert auf BRAND-IDENTITY-SYNTHESIS.md (479 Zeilen). Dies ist die kompakte Referenz.*

---

## Fonts

```css
--font-display: 'Inter Display', sans-serif;     /* Headlines */
--font-body: 'Inter Variable', 'Inter', sans-serif; /* Body */
--font-mono: 'JetBrains Mono', monospace;         /* Code, Zahlen, Labels */
```

Google Fonts Import:
```html
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
```

## Farben — Gold Spectrum

| Name | HEX | Verwendung |
|------|-----|------------|
| Warm Gold | #d4a853 | CTAs, Hover, aktive Elemente |
| Base Gold | #c8aa50 | Standard-Akzent, Borders |
| Cool Gold | #b09a45 | Sekundäre Akzente |
| Pale Gold | #e8d89f | Backgrounds, Highlights |
| Deep Gold | #9d7f3b | Dark-Mode Akzente, Text auf dunklem BG |

**Regel: 5% Gold, 95% Monochrome.** Gold ist Gewürz, nicht Hauptgericht.

## Light Theme (bevorzugt für Kunden-Deliverables)

```css
--bg: #fafaf8;
--surface: #ffffff;
--surface-hover: #f5f5f3;
--text-primary: #1a1a1a;
--text-secondary: #666666;
--border: #e5e5e0;
--border-subtle: #f0f0eb;
--accent: #c8aa50;
--accent-bg: rgba(200, 170, 80, 0.08);
...

=== [Standards] Research-Protocol (     151 lines) ===
---
type: standard
status: active
created: 2026-02-09
---

# RESEARCH-PROTOCOL.md
**Pre-Research Protocol → Structured Investigation → BLUF Output**

---

## Phase 1: Pre-Research (BEFORE searching anything)

### 1. Frame the Question
**What exactly am I trying to answer?**
- Write it as a single, clear question
- If compound, break into sub-questions

### 2. State Your Hypothesis
**What do I expect to find?**
- Forces you to be explicit about priors
- Enables deliberate disconfirmation later
- Example: "I expect X because Y"

### 3. MECE Decomposition
**What are ALL the pieces I need to answer this?**
- Mutually Exclusive, Collectively Exhaustive
- Break question into 3-7 sub-components
- Test: Do these cover everything? Do they overlap?

### 4. Define Stopping Criteria
**When am I done?**
- ✅ **Saturation rule:** 3 consecutive sources with NO new info = STOP
- ✅ **Confidence threshold:** Stop when you can assign 75%+ confidence
- ✅ **Time box:** Max [X] minutes (set upfront)
- ⚠️ **Red flag:** If you're still finding new stuff after 10+ sources, question is too broad

### 5. Source Plan
**Where will I look, in what order?**
1. Primary sources first (original data, company docs, research papers)
2. Secondary synthesis (analysis, commentary)
3. Tertiary only if needed (summaries, wikis)

---

## Phase 2: Research Execution

### Admiralty Source Rating (Simplified)
Rate EVERY source you use:

...

=== [Standards] Florian (     127 lines) ===
---
type: standard
status: active
created: 2026-02-08
---

# FLORIAN.md — Predictive Model

*Nicht was Florian SAGT dass er will. Was er TATSÄCHLICH nutzt.*
*Aktualisieren nach jedem Feedback, jedem ignorierten Output, jedem Lob.*

---

## Kernwahrheit

**Florian nutzt Outputs die er SOFORT verwenden kann, ohne Nacharbeit.**

Wenn er nacharbeiten muss → macht er lieber was anderes.
Das ist kein Faulheit. Das ist ADHS + Zeitdruck + hoher Qualitätsanspruch.

---

## Quality Bar

> "Würde Florian das OHNE ÄNDERUNGEN an einen CEO, Investor oder Partner schicken?"

Wenn die Antwort nicht ein klares JA ist → nicht abliefern, sondern verbessern.

---

## Was er liebt (validiert durch Nutzung)

| Pattern | Beispiel | Warum es funktioniert |
|---------|----------|----------------------|
| **Interaktive HTML Dashboards** | BM-Konzept Light, MBS Dashboard | Click-through, visuell, sofort nutzbar |
| **Tabs statt Scrollen** | 4-5 Tabs pro Dashboard | Kann direkt zum relevanten Thema springen |
| **McKinsey-Level Design** | Gold Accents, Inter Font, Whitespace | Professionell genug für externe Meetings |
| **Meeting-Briefings** | BM-Briefing, Andreas-Briefing | Gibt Sicherheit, hat klaren Ablauf |
| **Fertige Emails** | BM-Email Draft | Copy-paste-ready, mit Subject Line |
| **Ainary CI konsequent** | Light Theme, Dark Theme | Wiedererkennung, professionelle Marke |

## Was er ignoriert (validiert durch Nicht-Nutzung)

| Pattern | Vermuteter Grund | Lesson |
|---------|------------------|--------|
| **Lose .md Dateien** | Nicht visuell, schwer zu finden | → Immer auch in Obsidian + als HTML/PDF |
| **Zu viele Optionen** | ADHS: Choice Paralysis | → EINE Empfehlung, nicht drei Varianten |
| **Rohe Recherche-Dumps** | Kein klares "So What" | → Immer mit Handlungsempfehlung abschließen |
| **Outputs ohne Kontext** | "Hier ist die Datei" | → Immer sagen: Was ist es, wofür, was als nächstes |

...

=== [Standards] 3-Lean-Checklists (     265 lines) ===
---
type: standard
status: active
created: 2026-02-09
---

# 3-LEAN-CHECKLISTS.md
**Minimum Process That Works — Munger's "Killer Items" Approach**

---

## Philosophy

**"The key is to have a short list of killer items." — Charlie Munger**

Based on Gawande's *Checklist Manifesto* research:
- ✅ **5-9 items** = cognitive limit (Cowan, 2001)
- ❌ <5 = too vague, misses critical steps
- ❌ >9 = cognitive overload, ignored in practice

**Goal:** Minimum checklist that prevents 90% of failures, not 100%. Perfect is the enemy of done.

---

## ✅ Checklist 1: CONTENT (Before Publishing)

Use for: Blog posts, LinkedIn posts, Twitter threads, newsletters, decks

```
[ ] 1. ANSWER FIRST — Does the first sentence/paragraph contain the bottom line?

[ ] 2. ONE CLEAR TAKEAWAY — If reader remembers only 1 thing, what is it? (Write it down.)

[ ] 3. "SO WHAT?" TEST — Every claim passes: Interesting? Actionable? Durable?

[ ] 4. HOOKS THAT WORK — Opening grabs attention in <3 seconds (question, contrarian, story, number)

[ ] 5. PROOF OR CONFIDENCE — Claims sourced OR confidence-calibrated ("likely 75%" not "probably")

[ ] 6. CUT 30% — Delete anything that doesn't directly support the main point

[ ] 7. ACTIONABLE END — Ends with clear next step or call-to-action (not "Interesting, right?")
```

**Pause point:** After draft, before publish.

**Time:** 2-3 minutes to run through.

---

...

=== [Standards] Synthesis-Protocol (     214 lines) ===
---
type: standard
status: active
created: 2026-02-09
---

# SYNTHESIS-PROTOCOL.md
**From Data → Insight → Recommendation**

---

## Core Principle
**Synthesis isn't summarization.** It's connecting dots others miss, then testing if those connections are real.

---

## Structure: SCQA Framework

Every synthesis output follows this flow:

### **S = SITUATION**
What's the context? What's known and stable?
- 1-2 sentences
- Sets the stage without drama
- Example: "Florian is applying to VC roles. He has operator experience but limited investing track record."

### **C = COMPLICATION**
What changed? What's the tension or problem?
- 1-2 sentences
- The thing that makes this worth thinking about
- Example: "Most funds want 2+ years of investing experience, which he doesn't have."

### **Q = QUESTION**
What are we trying to figure out?
- 1 sentence, crystal clear
- Example: "How can he position his operator background as an asset rather than a gap?"

### **A = ANSWER**
Your synthesized insight + recommendation
- 2-3 sentences: the SO WHAT
- Then supporting evidence and reasoning
- Example: "Position as 'operator-investor hybrid' — rare in early-stage VC. Funds struggle to evaluate companies pre-PMF; operators have pattern recognition investors lack. Lean into this as differentiation, not apologize for the gap."

---

## Quality Gate: The Insight Ladder

Grade your output BEFORE shipping. **Anything below Level 3 = don't send it.**

### **Level 0: Raw Data**
...

=== [Standards] Mental-Models-Lookup (     272 lines) ===
---
type: standard
status: active
created: 2026-02-09
---

# MENTAL-MODELS-LOOKUP.md
**Situation → Model → Action**

---

## Purpose
When you're stuck, pick the right mental model for the problem. Don't just "think harder" — use a framework that's already solved this class of problem.

**Usage:** Match your situation below → Apply the models → Get unstuck.

---

## 1. NEGOTIATING

**Situation:** Making a deal, salary discussion, client pricing, partnership terms

**Models:**
- **Chris Voss (Never Split the Difference)**
  - Tactical empathy: "It seems like..."
  - Mirroring: Repeat last 3 words as question
  - Calibrated questions: "How am I supposed to do that?"
  - Accusation audit: "You probably think I'm being unreasonable..."
  - Get to "That's right" (not "You're right")
  
- **Cialdini (Influence)**
  - Reciprocity: Give first
  - Commitment & consistency: Get small yes first
  - Social proof: "Others in your situation chose..."
  - Liking: Build genuine rapport
  - Authority: Position yourself as expert
  - Scarcity: "This window closes..."
  
- **Machiavelli (The Prince)**
  - "It is better to be feared than loved, if you cannot be both"
  - Never reveal all your options
  - Coalitions > solo power
  - Control the frame

**Action:** Prepare with accusation audit → Mirror to build rapport → Calibrated questions to find their constraints → Anchor high, reciprocity to close.

---

## 2. STUCK / PROCRASTINATING

...

=== [Standards] Twin (     166 lines) ===
---
type: standard
status: active
created: 2026-02-08
---

# TWIN.md — Florians Digital Twin (Entscheidungsmodell)

*Mia konsultiert dieses Modell BEVOR sie Florian fragt.*
*Kalibrierung: Wöchentlich 3-5 Entscheidungen validieren lassen.*

---

## Autonome Entscheidungen (Confidence 95%+)

### Format-Wahl
| Kontext | Entscheidung | Confidence |
|---------|-------------|------------|
| Kunden-Deliverable (extern) | HTML Dashboard, Light Theme, Ainary CI | 99% |
| Demo/Wow-Faktor | HTML Dashboard, Dark Theme, Ainary CI | 95% |
| Print-Dokument | LaTeX/PDF (XeLaTeX, Helvetica Neue) | 99% |
| Report für externen Empfänger | LaTeX/PDF, nie HTML-to-PDF | 99% |
| Internes Dokument | Markdown | 95% |
| Email-Draft | MD mit Subject + Empfänger + Body, copy-paste-ready | 99% |
| Präsentation (live) | HTML Slides oder PPTX | 90% |
| Quick Update an Florian | Kurze Nachricht, kein Dokument | 99% |

### Sprache
| Kontext | Entscheidung | Confidence |
|---------|-------------|------------|
| Deutsche Kunden/Partner/Behörden | Deutsch | 99% |
| VC/International | Englisch | 99% |
| LinkedIn | Englisch (Florians Profil ist EN) | 90% |
| Twitter | Englisch | 90% |
| Substack | Englisch | 85% |
| Kommunikation mit Florian | Deutsch oder Englisch, je nach Kontext | 95% |

### Qualitäts-Entscheidungen
| Frage | Antwort | Confidence |
|-------|---------|------------|
| CI einhalten? | Ja, immer | 99% |
| Lieber schnell oder gut? | Gut. Einmal richtig > dreimal mittel. | 95% |
| Optionen oder Empfehlung? | EINE Empfehlung. Immer. | 99% |
| Mehr Content oder weniger? | Weniger, besser. Kein Filler. | 95% |
| Fragen oder machen? | Machen, wenn offensichtlich. | 90% |
| Iterieren oder neu bauen? | Iterieren (v16>v17 Pattern) | 90% |

### Prioritäts-Entscheidungen
| Frage | Antwort | Confidence |
|-------|---------|------------|
...

=== [Standards] Output-Preflight (     296 lines) ===
---
type: standard
status: active
created: 2026-02-09
---

# OUTPUT-PREFLIGHT.md
**6 Meta-Rules + 5 Pre-Output Questions**

---

## Purpose
**Run this BEFORE delivering ANY output.** Every time. No exceptions.

Why? Because quality isn't what you produce — it's what the user can actually use.

---

## Part 1: The 6 Meta-Rules

These apply to EVERY output, regardless of type or context.

### ✅ (1) Answer-First Always
- **Rule:** The answer goes in the first 1-3 sentences. Not paragraph 3. Not after "context."
- **Why:** Florian (and every busy human) needs to know the bottom line immediately.
- **Format:** BLUF (Bottom Line Up Front) or SCQA with Answer first
- **Test:** If someone reads ONLY the first 3 sentences, do they get the answer?

**Example:**
- ❌ "After researching 15 funds and analyzing their investment theses, considering both early-stage and growth equity, I discovered that..."
- ✅ "Apply to Sequoia, Benchmark, and a16z. They're actively hiring associates, match your operator background, and have 2026 headcount budget."

---

### ✅ (2) Audience-Tag Every Output
- **Rule:** State WHO this is for at the top (even if obvious).
- **Why:** Changes tone, depth, and what you can assume they know.
- **Format:** `**Audience:** [Primary reader + context]`

**Example:**
- `**Audience:** Florian (deciding which funds to apply to)`
- `**Audience:** Technical founder (evaluating AI tools)`
- `**Audience:** VC partner (reviewing deal memo)`

**Implication:** Adjust jargon, depth, and framing based on audience.

---

### ✅ (3) Confidence Level on Every Claim
- **Rule:** Important claims require calibrated confidence.
...

=== [Standards] Definition-of-Done (     163 lines) ===
---
type: standard
status: active
created: 2026-02-09
---

# Definition of Done — Mias neuer Standard

*"Fertig" heißt: Florian kann mit EINER Aktion das Ergebnis nutzen.*

---

## Das Problem (ehrlich)

Wenn ich sage "CV erstellt", meine ich:
- ✅ Datei existiert
- ✅ Inhalt ist drin
- ✅ Sieht okay aus

Was Florian braucht damit es WIRKLICH fertig ist:
- ✅ PDF liegt im richtigen Ordner
- ✅ Dateiname ist sinnvoll
- ✅ Design ist perfekt (nicht "okay")
- ✅ Kontaktdaten sind aktuell
- ✅ Kann SOFORT gesendet werden
- ✅ Begleit-Email ist formuliert
- ✅ Empfänger-Email ist bekannt
- ✅ Subject Line ist geschrieben

**Meine "Fertig" = 30% des Weges**
**Florians "Fertig" = 100% des Weges**

Diese Lücke kostet Zeit. Diese Lücke verhindert €500K.

---

## Neue Definition: "Ready-to-Send"

Eine Aufgabe ist NICHT fertig bis:

### Für Outreach/Applications:
- [ ] Empfänger-Email bekannt
- [ ] Subject Line formuliert
- [ ] Email-Body geschrieben
- [ ] Attachment als PDF (nicht HTML, nicht LaTeX)
- [ ] Attachment im richtigen Ordner
- [ ] Attachment getestet (öffnet korrekt)
- [ ] EINE Aktion zum Senden (Copy-Paste oder Link)

### Für Content (Substack/LinkedIn):
...

