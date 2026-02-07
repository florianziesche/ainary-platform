# Sequoia "2026: This is AGI" — Deep Analysis Research Brief

**Research Date:** February 7, 2026  
**Author:** Mia (Research Agent)  
**Purpose:** Comprehensive analysis for high-quality article on Sequoia's AGI thesis and the streaming input gap

---

## Executive Summary

Sequoia Capital's January 2026 essay "2026: This is AGI" (Pat Grady & Sonya Huang) declares that AGI has arrived, defined functionally as "the ability to figure things out." Their thesis rests on three ingredients: pre-training (knowledge), inference-time compute (reasoning), and **long-horizon agents** (iteration). The essay cites METR benchmark data showing AI task horizons doubling every ~7 months, with Claude Opus 4.5 achieving a 4h49m time horizon.

**The Critical Gap:** Current AI agents operate on **static context windows** (batch processing), not continuous, streaming perception of the world. They're snapshot processors, not continuous thinkers. This fundamental architectural limitation creates a chasm between benchmark performance and real-world deployment in manufacturing, media, legal work, and other domains requiring persistent awareness.

**Key Tension:** Sequoia's functional definition sidesteps the hard technical problem — AGI may arrive by their definition while still being fundamentally limited in ways that matter for the most valuable applications.

---

## 1. Summary of Sequoia's Argument

### Core Definition
**"AGI is the ability to figure things out. That's it."**

Sequoia explicitly disclaims technical authority ("we are investors") and offers a **functional** definition focused on business impact, not philosophical correctness.

### Three Ingredients of AGI

| Ingredient | What It Provides | When It Arrived |
|------------|------------------|-----------------|
| **Pre-training** | Baseline knowledge | 2022 (ChatGPT) |
| **Inference-time compute** | Reasoning over knowledge | Late 2024 (OpenAI o1) |
| **Long-horizon agents** | Iterative problem-solving | Early 2026 (Claude Code, etc.) |

### From Talkers to Doers
- **2023-2024 AI:** Conversationalists with limited impact
- **2026-2027 AI:** Colleagues you can "hire" — specialists that execute multi-step tasks autonomously

### The "Hire an Agent" Test (Sarah Guo / Conviction)
Sequoia credits Sarah Guo with the litmus test: **"Soon you'll be able to hire an agent."**

**Examples of hireable agents:**
- **Medicine:** OpenEvidence's Deep Consult (specialist)
- **Law:** Harvey (associate)
- **Cybersecurity:** XBOW (pen-tester)
- **DevOps:** Traversal (SRE)
- **GTM:** Day AI (BDR, SE, Rev Ops)
- **Recruiting:** Juicebox (recruiter)
- **Math:** Harmonic's Aristotle (mathematician)
- **Chip Design:** Ricursive (chip designers)
- **AI Research:** GPT-5.2, Claude (AI researchers)

### Example Use Case: DevRel Recruiting
Sequoia provides a detailed scenario where an agent:
1. Starts with LinkedIn searches (obvious)
2. Pivots to **signal over credentials** (YouTube talks)
3. Cross-references with Twitter engagement
4. Filters for reduced activity (potential disengagement)
5. Researches three finalists
6. Drafts personalized outreach

**Time:** 31 minutes (vs. traditional job board posting)

This demonstrates **navigating ambiguity** — forming hypotheses, testing, hitting dead ends, pivoting. Not following a script.

### Key Quote
> "Generally intelligent people can work autonomously for hours at a time, making and fixing their mistakes and figuring out what to do next without being told. Generally intelligent agents can do the same thing. This is new."

---

## 2. Key Data Points: METR Benchmarks & Projections

### METR Time Horizon Methodology

**What is "Time Horizon"?**
METR (Model Evaluation & Threat Research) measures AI performance by **the length of tasks AI agents can complete**, measured by how long tasks take human experts.

- **50% time horizon:** The length of task where a model succeeds 50% of the time
- **Tasks:** Software engineering and research tasks requiring multi-step reasoning

### The Exponential Trend

**Finding:** AI task horizons have been **doubling every ~7 months** since 2019 (6+ years of consistent exponential growth)

**Latest Update (TH1.1, Jan 2026):**
- **Doubling time (2019-2025):** 196 days (~6.5 months)
- **Doubling time (2023+):** 131 days (~4.3 months) — **accelerating**
- **Doubling time (2024+):** 89 days (~3 months) — even faster

### Claude Opus 4.5 Performance

**METR Estimate (Dec 2025):**
- **50% time horizon:** 4 hours 49 minutes (289 minutes)
- **95% confidence interval:** 1h49m to 20h25m (109–1,225 min)
- **Updated TH1.1 (Jan 2026):** 320 minutes (~5h20m) [170–729 min]

**What this means:**
Claude Opus 4.5 can **successfully complete tasks that take human experts ~5 hours** with 50% reliability. Not "5 hours of thinking" — tasks requiring the same human-equivalent work as a 5-hour expert session.

### Other Recent Models (TH1.1)

| Model | 50% Time Horizon | Change from TH1 |
|-------|------------------|-----------------|
| GPT-5 | 214 min (~3h34m) | +55% |
| Claude Opus 4 | 101 min (~1h41m) | +18% |
| o3 | 121 min (~2h) | +29% |
| Claude Sonnet 3.7 | 60 min (1h) | +7% |
| GPT-4 (Nov 2023) | 3.6 min | -57% (revised down) |

**Key Insight:** Recent models saw upward revisions; older models revised downward → **steeper acceleration in recent years**

### Sequoia's Extrapolation

If the ~7 month doubling trend continues:

| Year | Capability |
|------|------------|
| **2026** | ~30 min – 1 hour tasks (✅ now) |
| **2028** | Full-day tasks reliably |
| **2034** | Full-year tasks |
| **2037** | Century-long tasks |

**Quote from Sequoia:**
> "What can you achieve when your plans are measured in centuries? A century is 200,000 clinical trials no one's cross-referenced. A century is every customer support ticket ever filed, finally mined for signal. A century is the entire U.S. tax code, refactored for coherence."

### Important Caveats (from METR)

1. **Task distribution sensitivity:** TH1.1 uses 228 tasks (vs. 170 in TH1). Adding more long tasks changed estimates, suggesting results are somewhat dependent on task selection
2. **Confidence intervals are wide:** Opus 4.5's upper bound is 2.3X the point estimate
3. **Only 5 of 31 long tasks (8h+) have human baselines** — rest use estimates
4. **Trend may not extrapolate linearly:** Could hit plateau, could accelerate further

### How They Get Long-Horizon Capabilities

**Two approaches (Sequoia):**

1. **Reinforcement learning (research labs):** Intrinsically teach models to stay on track longer during training
2. **Agent harnesses (application layer):** Engineer scaffolding around known limitations (memory hand-offs, context compaction, error recovery)

**Examples of great agent harnesses:**
- Manus
- Claude Code (Anthropic)
- Factory's Droids

---

## 3. The Streaming Input Gap: The Core Problem

### The Fundamental Architecture

**How current LLM agents work:**
1. Receive input (snapshot of the world)
2. Process in context window (static, finite)
3. Generate output
4. Repeat with *new* snapshot

**What they lack:**
- **Continuous perception** of a changing world
- **Real-time world model updates**
- **Persistent spatial-temporal memory**

### Technical Deep Dive: Context Windows vs. World Models

#### Context Window Limitations (Factory.ai analysis)

**The Problem:**
- Modern LLMs: ~1 million token context windows
- Enterprise monorepo: **several million tokens**
- Relevant organizational context: **millions more tokens** (Slack, Notion, Datadog, etc.)

**"Context Rot" (Chroma Research, 2025):**
> "Models do not use their context uniformly; instead, their performance grows increasingly unreliable as input length grows."

Even with larger windows:
- **Not big enough** for full production codebases
- **Quality degradation** as context grows (attention is non-uniform)
- **Monetary costs** spiral with token count

**Factory's solution:** Treat context as a scarce resource (like CPU time or memory):
- Repository overviews (architectural summaries)
- Semantic search (targeted retrieval)
- Hierarchical memory (user + org memory)
- Enterprise integrations (Datadog, Slack, Notion)

#### The World Model Problem (Scientific American, Jan 2026)

**Key Quote from Angjoo Kanazawa (UC Berkeley):**
> "How do you develop an intelligent LLM vision system that can actually have **streaming input and update its understanding of the world and act accordingly**? That's a big open problem. I think **AGI is not possible without actually solving this problem**."

**Current state:**
- LLMs have *implicit* world models from training data
- But they **cannot update in real-time** — "GPT-4 does not learn from experience" (OpenAI technical report)
- They lack "spatial temporal memory" (Kanazawa)

**What "streaming input" means:**
- **Not:** Periodic API calls with fresh context
- **Is:** Continuous updating of an internal model as the world changes

**4D World Models:**
Recent research (NeoVerse, TeleWorld, Fei-Fei Li's World Labs Marble) explores 4D models (3D + time):
- Persistent spatial representation
- Temporal continuity (objects don't disappear/morph when occluded)
- Viewpoint-independent understanding
- Memory of what recently happened

**Vision-language models struggle with basic physics:**
A 2025 benchmark paper found "striking limitations" including **"near-random accuracy when distinguishing motion trajectories"**

### Why This Matters: Real-World Deployment Gaps

#### Manufacturing
**Requirement:** Continuous monitoring of production lines, real-time fault detection, persistent awareness of part locations/quality

**Current AI limitation:** 
- Batch processing of camera feeds (snapshots)
- No persistent spatial awareness
- Cannot track objects across occlusions
- Loses context between processing cycles

**Impact:** AI can analyze images but cannot "supervise" a production line the way a human does

#### Legal Work (Harvey AI example)
**Requirement:** Following evolving case law, tracking multiple concurrent negotiations, maintaining context across weeks/months of document review

**Current AI limitation:**
- Context window size limits (even 1M tokens < entire case file)
- No persistent memory of previous analysis
- Cannot update understanding as new precedents emerge in real-time
- Memory management is manual (RAG retrieval, not continuous integration)

**What works:** Narrow, bounded tasks (draft motion, research specific question)
**What struggles:** Multi-month case strategy with evolving circumstances

#### Media/Content Production
**Requirement:** Maintaining narrative continuity, character consistency, spatial coherence across scenes

**Current AI limitation:**
- Video generation models (pre-world-model): dog's collar disappears, sofa becomes loveseat
- No persistent scene representation
- Predictions are statistically plausible *per frame*, not globally coherent

**Emerging solution:** 4D world models (TeleWorld paper) that maintain spatial-temporal consistency

#### The General Pattern

**Tasks AI handles well (2026):**
- Defined start/end points
- Fits in context window
- Snapshot-based reasoning (code review, document summarization, Q&A)
- Stateless or quasi-stateless

**Tasks AI struggles with:**
- Long-running processes requiring persistent awareness
- Real-time adaptation to changing environments
- Spatial/physical world understanding
- True "always-on" operation (Sequoia's own "Always-On Economy" essay, April 2025)

---

## 4. Counterarguments and Critiques

### Hacker News Skepticism

**Top critique (46640796):**
> "Before we go any further, it's worth acknowledging that we do not have the moral authority to propose a technical definition of AGI. [...] Since they have admitted their technical incompetence on the subject of AI, nor can they substantiate their definition of AGI themselves, you will struggle to take the rest of this article seriously."

**Core argument:**
- VCs are "hijacking and creating narratives through their own biases"
- "AGI" has become a "narrative scam"
- Sequoia's real definition = automation that enables workforce reduction
- Citing WEF 2025 Jobs Report: "40% anticipate reducing their workforce where AI can automate tasks"
- Timeline matches WEF's 2030 projections

**Translation:** Sequoia is redefining AGI to justify investment returns, not describe technical reality

### The Definition Problem

**Sequoia's own admission:**
> "We appreciate that such an imprecise definition will not settle any philosophical debates."

**The tension:**
- **Functional definition** (useful for business) vs. **Technical definition** (useful for understanding limits)
- Sequoia explicitly chooses business utility: "so what?" (Don Valentine question)
- This sidesteps hard questions about what AI *can't* do

**Alternative framing (implicit in critiques):**
AGI ≠ "Can complete some hours-long tasks"
AGI = General intelligence across domains, continuous learning, common-sense reasoning in novel situations

### The Reliability Gap

**Sequoia acknowledges:**
> "To be clear: agents still fail. They hallucinate, lose context, and sometimes charge confidently down exactly the wrong path. But the trajectory is unmistakable, and the failures are increasingly fixable."

**The question:** How long until "failures are increasingly fixable" becomes "failures are rare enough for production deployment in high-stakes domains"?

- **Software engineering:** Already partially there (coding agents)
- **Legal work:** Still requires extensive human review
- **Medicine:** OpenEvidence is advisory, not prescriptive
- **Manufacturing:** Physical world consequences of errors are severe

### The Extrapolation Uncertainty

**METR's own cautions:**
- Wide confidence intervals
- Task selection affects estimates
- No guarantee trend continues
- Could plateau as fundamental limits are hit
- Could accelerate with algorithmic breakthroughs

**Historical precedent:** Many exponential trends in AI have slowed or plateaued (ImageNet accuracy, chess ELO, etc.)

### The Context Window Arms Race

**Factory.ai's perspective:**
Even with 10X larger context windows, fundamental problems remain:
- Attention degrades with length
- Costs scale linearly (or worse)
- Bigger ≠ better reasoning
- Still fundamentally batch processing

**The architectural question:** Is this a scaling problem or a **paradigm problem**?

### Embodiment and Physical Reality

**Yann LeCun's pivot (Nov 2024):**
Left Meta to found AMI Labs focusing on:
> "Systems that understand the physical world, have persistent memory, can reason, and can plan complex action sequences"

**Implication:** Even leading AI researchers believe current LLM-based agents are insufficient for general intelligence

**The gap:** Digital/software tasks vs. physical world tasks
- Software engineering fits the snapshot paradigm (code doesn't move)
- Manufacturing, robotics, autonomous vehicles need continuous world understanding

---

## 5. Unique Article Angles

### Angle 1: "AGI for VCs vs. AGI for Engineers"
**Hook:** Sequoia and technical researchers are talking past each other — they've defined success differently

**Thesis:** 
- VCs optimize for *market timing* and *narrative capture*
- Engineers optimize for *capability boundaries* and *failure modes*
- Sequoia's "2026 is AGI" is correct *for their purposes* (fundraising, exits, talent attraction)
- But it obscures critical technical gaps that will determine which applications actually succeed

**Story structure:**
1. Sequoia's definition (functional, business-focused)
2. What it enables (coding agents, narrow AI "employees")
3. What it misses (streaming input, persistent awareness, physical world)
4. Why the gap matters (manufacturing, robotics, long-term strategic work)
5. Conclusion: Two types of AGI timeline — "good enough for investors" arrived in 2026; "good enough for embodied intelligence" still TBD

**Target audience:** Technical founders, AI engineers, people building in the space (not retail investors)

---

### Angle 2: "The Streaming Input Problem: Why AI Can't Work a Full Day (Yet)"
**Hook:** AI agents can handle 5-hour tasks in benchmarks but struggle with 8-hour workdays. The reason is architectural.

**Thesis:**
- METR benchmarks measure *task length* but assume **bounded, stateless problems**
- Real work requires **persistent awareness** across interruptions, context switches, and environmental changes
- Current architecture: snapshot → process → output (batch mode)
- Required architecture: continuous perception → world model updates → action (streaming mode)

**Story structure:**
1. The METR milestone (5h tasks) and Sequoia's optimism (full-day tasks by 2028)
2. What a "full-day task" actually requires (case study: human knowledge worker's day)
   - Context switches (Slack messages, email, meetings)
   - Persistent state (remembering morning decisions in afternoon)
   - Environmental awareness (noticing when teammates update shared docs)
3. Why current AI fails at this (context window limits, no streaming input, memory is retrieval not integration)
4. What's being built to fix it (4D world models, hierarchical memory, embodied AI research)
5. Conclusion: The next 2X improvement isn't just "longer tasks" — it's a fundamentally different architecture

**Target audience:** AI product managers, founders building agents, tech-savvy operators

---

### Angle 3: "Why Your AI Employee Still Can't Handle Manufacturing (Or Law, Or...)"
**Hook:** Sequoia says you can "hire" AI agents. But only for some jobs. Here's the pattern in what works and what doesn't.

**Thesis:**
Domain-by-domain analysis of where AI agents are deployable vs. where they fail — with a unifying technical explanation

**Story structure:**
1. The "hire an agent" promise (Sequoia/Sarah Guo)
2. **Where it works:** Software engineering, copywriting, research synthesis
   - Pattern: Stateless or bounded-state, digital artifacts, human-in-loop acceptable
3. **Where it struggles:** Legal (long context), Manufacturing (physical world), Media (continuity)
   - Pattern: Requires persistent awareness, real-time adaptation, or high reliability
4. The technical divide: Snapshot vs. streaming processing
5. What each domain needs to cross the threshold (legal: better memory; manufacturing: world models; media: 4D consistency)
6. Conclusion: "Hireable" is domain-dependent, and the pattern reveals fundamental architecture limits

**Target audience:** Business operators, domain experts evaluating AI, investors doing diligence

---

### Angle 4: "2026, 2028, 2034: Reading the AI Timeline Tea Leaves"
**Hook:** Sequoia extrapolates METR's trend to predict year-long tasks by 2034. Should you believe them?

**Thesis:**
Critically examine the forecasting methodology, confidence intervals, and historical precedents for exponential AI trends

**Story structure:**
1. The headline projection (Sequoia: full-day by 2028, year-long by 2034, century by 2037)
2. What the data actually shows (METR's methodology, confidence intervals, caveats)
3. How trend extrapolation works — and fails (case studies: ImageNet, Chess, other AI benchmarks that plateaued)
4. The variables that could break the trend:
   - Architectural shifts required (streaming input, world models)
   - Reliability thresholds for real-world deployment
   - Data/compute scaling limits
   - Regulatory and safety constraints
5. Alternative scenarios:
   - Optimistic: Algorithmic breakthrough accelerates trend (< 2034 for year-long tasks)
   - Baseline: Trend continues but with wider error bars than Sequoia suggests
   - Pessimistic: Plateau at day-long tasks without architectural paradigm shift
6. Conclusion: The trend is real, but extrapolating to decades is hubris. The 2028 milestone is plausible; 2034+ is speculation.

**Target audience:** Forecasters, strategists, long-term planners, researchers

---

### Angle 5: "The Agent Harness Wars: Why Scaffolding Matters More Than Models"
**Hook:** Frontier models are converging in capability. The real differentiation is in the infrastructure around them.

**Thesis:**
Sequoia mentions "agent harnesses" briefly but doesn't emphasize their importance. The scaffolding — context management, memory systems, tool use, error recovery — is where the real product differentiation happens.

**Story structure:**
1. The model plateau: Claude Opus 4.5 (~5h), GPT-5 (~3.5h), o3 (~2h) — all in the same ballpark
2. What makes an agent actually useful: **harness engineering**
   - Factory's context stack (hierarchical memory, semantic search, enterprise integrations)
   - Anthropic's Claude Code (error recovery, iterative debugging)
   - Harvey's legal-specific scaffolding (precedent search, document versioning)
3. Case study: Two agents with the same model, different harnesses
   - One fails at 30-min tasks (poor context management)
   - One succeeds at 3-hour tasks (excellent scaffolding)
4. Why VCs should care: Harnesses are **defensible moats** (models commoditize, scaffolding doesn't)
5. Conclusion: The race isn't "who trains the best model" — it's "who builds the best infrastructure to make models useful"

**Target audience:** AI founders, product builders, technical VCs

---

## 6. Key Quotes with Sources

### Sequoia Capital ("2026: This is AGI")

**On AGI definition:**
> "AGI is the ability to figure things out. That's it."

> "We appreciate that such an imprecise definition will not settle any philosophical debates. Pragmatically speaking, what do you want if you're trying to get something done? An AI that can just figure stuff out."

**On the shift:**
> "The AI applications of 2023 and 2024 were talkers. Some were very sophisticated conversationalists! But their impact was limited. The AI applications of 2026 and 2027 will be doers."

**On long-horizon agents:**
> "Generally intelligent people can work autonomously for hours at a time, making and fixing their mistakes and figuring out what to do next without being told. Generally intelligent agents can do the same thing. This is new."

**On the exponential:**
> "If we trace out the exponential, agents should be able to work reliably to complete tasks that take human experts a full day by 2028, a full year by 2034, and a full century by 2037."

**On failures:**
> "To be clear: agents still fail. They hallucinate, lose context, and sometimes charge confidently down exactly the wrong path. But the trajectory is unmistakable, and the failures are increasingly fixable."

**On what's possible:**
> "What can you achieve when your plans are measured in centuries? A century is 200,000 clinical trials no one's cross-referenced. A century is every customer support ticket ever filed, finally mined for signal. A century is the entire U.S. tax code, refactored for coherence."

**On hiring agents (Sarah Guo attribution):**
> "Soon you'll be able to hire an agent. That's one litmus test for AGI (h/t: Sarah Guo)."

---

### METR (Time Horizon Research)

**On the trend:**
> "The 50% task completion time horizon on our tasks has been growing exponentially from 2019–2025 with a doubling time of approximately seven months."

**On Claude Opus 4.5:**
> "We estimate that, on our tasks, Claude Opus 4.5 has a 50%-time horizon of around 4 hrs 49 mins (95% confidence interval of 1 hr 49 mins to 20 hrs 25 mins)." (Twitter announcement, Dec 2025)

**On implications:**
> "If the trend of the past 6 years continues to the end of this decade, frontier AI systems will be capable of autonomously carrying out month-long projects. This would come with enormous stakes, both in terms of potential benefits and potential risks."

**On limitations:**
> "Current frontier AI models such as Claude 3.7 Sonnet have a 50% time horizon of around 50 minutes. Furthermore, frontier AI time horizon has been doubling approximately every seven months since 2019, though the trend may have [slowed or accelerated]."

---

### Scientific American (Jan 2026, on World Models)

**Angjoo Kanazawa (UC Berkeley):**
> "How do you develop an intelligent LLM vision system that can actually have streaming input and update its understanding of the world and act accordingly? That's a big open problem. I think AGI is not possible without actually solving this problem."

> "In a way, I would say that the LLM already has a very good world model; it's just we don't really understand how it's doing it."

**On current LLM limitations:**
> "These conceptual models, though, aren't a real-time physical understanding of the world because LLMs can't update their training data in real time. Even OpenAI's technical report notes that, once deployed, its model GPT-4 'does not learn from experience.'"

**On the future role of LLMs:**
> "The LLM would act as the layer for 'language and common sense to communicate' [...] it would serve as an 'interface,' whereas a more clearly defined underlying world model would provide the necessary 'spatial temporal memory' that current LLMs lack."

**On vision-language model limitations (2025 benchmark):**
> "Striking limitations in their basic world-modeling abilities, including near-random accuracy when distinguishing motion trajectories."

---

### Factory.ai (Context Window Problem, Aug 2025)

**On the core problem:**
> "Large language models have limited context windows - approximately 1 million tokens. In contrast, a typical enterprise monorepo can span thousands of files and several million tokens."

**On context rot (citing Chroma Research):**
> "Models do not use their context uniformly; instead, their performance grows increasingly unreliable as input length grows."

**On why bigger windows don't solve it:**
> "Larger windows do not eliminate the need for disciplined context management. Rather, they make it easier to degrade output quality without proper curation."

**On treating context as a resource:**
> "Effective agentic systems must treat context the way operating systems treat memory and CPU cycles: as finite resources to be budgeted, compacted, and intelligently paged."

**On future limitations:**
> "Even as we see improvements in these capabilities, certain limitations will persist: Sensitivity to unrelated context — Models will get distracted and become less effective when given large amounts of unrelated context."

---

### Yann LeCun (AMI Labs launch, Nov 2024)

**On his new focus:**
> "Systems that understand the physical world, have persistent memory, can reason, and can plan complex action sequences."

**From his 2022 position paper:**
> "Why humans can act well in situations they've never encountered [...] may lie in the ability to learn world models, internal models of how the world works."

---

### Hacker News Critique

**On Sequoia's authority:**
> "Before we go any further, it's worth acknowledging that we do not have the moral authority to propose a technical definition of AGI. [...] Since they have admitted their technical incompetence on the subject of AI, nor can they substantiate their definition of AGI themselves, you will struggle to take the rest of this article seriously."

**On real motivation:**
> "Their real definition of 'AGI' is by what the WEF have envisioned in their last 2025 Future of Jobs Report which the timeframe is in 5 years, meaning to 2030. [...] 'Finally, half of employers plan to re-orient their business in response to AI, two-thirds plan to hire talent with specific AI skills, while 40% anticipate reducing their workforce where AI can automate tasks.'"

---

## 7. Additional Context & Meta-Analysis

### What Sequoia Gets Right

1. **Long-horizon agents are a breakthrough:** The shift from "talker" to "doer" is real
2. **METR trend is impressive:** 6+ years of exponential growth is significant
3. **Business impact is accelerating:** Coding agents (2026) genuinely feel different from ChatGPT (2022)
4. **Functional definition has value:** For go-to-market and product development, "can it figure things out" matters more than philosophical debates

### What Sequoia Underplays

1. **Reliability gap:** "Failures are increasingly fixable" ≠ "ready for high-stakes deployment"
2. **Architectural limits:** Snapshot processing vs. streaming input is a paradigm issue, not just a scaling issue
3. **Domain boundaries:** "Hireable" for some jobs (software) ≠ hireable for all jobs (manufacturing, medicine)
4. **Extrapolation risk:** Exponential trends often plateau; projecting to 2034+ is speculation

### The Streaming Input Gap: Why It's THE Story

**This is the unifying technical explanation for:**
- Why coding agents work (code is static, stateless)
- Why manufacturing agents struggle (need continuous physical awareness)
- Why legal AI needs heavy scaffolding (context exceeds windows, memory is manual)
- Why video generation has continuity errors (no persistent scene model)

**It's also the frontier research area:**
- 4D world models (Fei-Fei Li, World Labs)
- Embodied AI (Yann LeCun, AMI Labs)
- Hierarchical memory systems (Factory, Anthropic)
- Real-time learning and adaptation (DreamerV3, etc.)

**And it's a timeline inflection point:**
- **Without solving streaming input:** Plateau at day-long digital tasks
- **With solving streaming input:** Path to year-long tasks, physical world capabilities, true "general" intelligence

### Key Tension for an Article

**The paradox:**
- Sequoia is *correct* that long-horizon agents are transformative (2026 *is* a milestone)
- Sequoia is *incomplete* in not addressing the streaming input gap (2034 extrapolation is uncertain)

**The narrative opportunity:**
Tell the story of where we are (impressive), where we're going (Sequoia's timeline), and **what has to change architecturally** to get there (the streaming input problem).

This avoids both:
- ❌ Dismissing Sequoia as "VC hype" (they're right about near-term impact)
- ❌ Accepting extrapolation uncritically (the technical gaps are real)

**The outcome:**
A nuanced, technically grounded piece that:
1. Validates the 2026 breakthrough (long-horizon agents)
2. Explains the architectural frontier (streaming input, world models)
3. Maps the deployment landscape (what works now, what needs more R&D)
4. Critically examines the timeline (2028 plausible, 2034+ speculative)

---

## 8. Recommended Next Steps for Article Development

### Research Gaps to Fill (Optional Deep Dives)

1. **Sarah Guo / Conviction perspective:** Find interviews/essays where she elaborates on "hire an agent" litmus test
2. **Domain-specific deployment data:** Case studies from Harvey (legal), Factory (engineering), OpenEvidence (medicine) on reliability/adoption
3. **World model technical papers:** Deeper dive on DreamerV3, TeleWorld, NeoVerse for mechanistic understanding
4. **Historical AI trend analysis:** Find examples of exponential trends that plateaued (to ground extrapolation skepticism)

### Structural Recommendations

**For any of the 5 angles:**
1. **Lead with the tension:** VCs say AGI is here; engineers say it's architecturally incomplete
2. **Use METR data as narrative anchor:** Concrete, credible, impressive — but contextualize it
3. **Explain streaming input gap *visually*:** Diagram of batch vs. streaming processing
4. **Domain case studies for concreteness:** Manufacturing + Legal + one more
5. **End with timeline nuance:** Near-term optimism (2026-2028), long-term uncertainty (2034+)

### Tone & Positioning

**Avoid:**
- ❌ Dismissive ("VCs don't know what they're talking about")
- ❌ Credulous ("Sequoia is right, AGI is here, century-long tasks by 2037")
- ❌ Purely technical (inaccessible to non-experts)

**Aim for:**
- ✅ Informed skepticism ("Sequoia is right about 2026 milestone, but...")
- ✅ Technical grounding with business implications
- ✅ Accessible to smart generalists, valuable to experts

---

## 9. Final Assessment: Is Sequoia Right?

### On "AGI is here" (functional definition):
**Verdict: Defensible but incomplete**
- ✅ Long-horizon agents can "figure things out" in bounded domains
- ✅ This is economically transformative
- ❌ Still fundamentally limited by snapshot architecture
- ❌ "General" is overstated — works for digital/stateless tasks, not physical/continuous tasks

### On the METR trend:
**Verdict: Real but over-extrapolated**
- ✅ 6+ years of exponential growth is impressive and statistically robust
- ✅ Doubling every 4-7 months has held through multiple model generations
- ⚠️ Confidence intervals are wide (2X-3X error bars)
- ❌ Extrapolating to 2034 ignores potential plateaus, paradigm shifts, or discontinuities

### On "hire an agent" in 2026:
**Verdict: True for specific roles, misleading as general claim**
- ✅ Software engineering agents are genuinely productive (Claude Code, GitHub Copilot, Cursor)
- ✅ Narrow specialist agents work in bounded domains (legal research, medical Q&A)
- ❌ "Hire" implies autonomy + reliability that isn't there yet for most roles
- ❌ Heavy human oversight still required for high-stakes work

### On the 2028-2034 timeline:
**Verdict: 2028 plausible, 2034 speculative**
- ✅ Full-day digital tasks by 2028: Reasonable if trend continues + reliability improves
- ⚠️ Year-long tasks by 2034: Requires solving streaming input / world model problems
- ❌ Century-long tasks by 2037: Pure speculation; ignores unknown unknowns

### The Real Story:
**2026 is a milestone, not the finish line.**

Long-horizon agents are transformative for digital, stateless work (coding, writing, research synthesis). But the next frontier — continuous perception, physical world understanding, true "always-on" operation — requires architectural breakthroughs (streaming input, world models, persistent memory) that are still in research stages.

Sequoia's timeline is aggressive but not absurd *if* those breakthroughs arrive on schedule. The technical community is more cautious because they understand what still needs to be invented.

---

**End of Research Brief**

*This document provides comprehensive source material for a high-quality article. Recommended angle: #2 ("The Streaming Input Problem") for technical depth + business relevance.*
