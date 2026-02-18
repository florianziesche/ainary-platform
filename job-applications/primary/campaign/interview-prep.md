# Interview Prep — Primary OIR: Agents

**Role:** Operator-In-Residence: Agents  
**Interviewer:** Brian Schechter (Partner, ex-CEO)  
**Focus:** Agent-native systems, local AI, evals, translate tech → company concepts

---

## Part 1: 10 Likely Interview Questions from Brian

### 1. "Walk me through a day using your agent system. What does it actually do?"

**Answer:**

I run OpenClaw as my operating system 12 hours a day. This morning:
- 8:30: Agent loads episodic memory (yesterday's work) + semantic knowledge (distilled patterns)
- 9:00: I ask it to research Primary's portfolio companies. It searches, extracts, connects to my existing thesis notes, stores verified facts
- 10:30: I say "draft LinkedIn post about trust scoring." It reads my content voice standards, pulls examples from prior posts, drafts → I edit 20% → publish
- Afternoon: "Build interview prep for this role" — you're reading the output

**What makes it different:**
- It doesn't reset. Every output feeds the next input (episodic + semantic memory)
- It scores its own confidence. <90% on irreversible → it asks. >90% → it acts
- Trust compounds. When outcomes validate confidence, autonomy thresholds adjust

Not a chatbot. A compound execution layer.

---

### 2. "Most people say 'agents aren't reliable yet.' You use one daily. Why does yours work?"

**Answer:**

Three design decisions:

**1. Trust-as-a-currency framework**
- Every output gets a confidence score (self-assessed)
- Threshold-based autonomy: >90% on irreversible → act. <90% → ask
- Outcomes feed back: `agenttrust-score.py update <agent> <conf> <outcome>`
- System calibrates over time

**2. Memory with anti-entropy**
- Episodic: Daily events (memory/YYYY-MM-DD.md)
- Semantic: Distilled patterns (MEMORY.md, weekly)
- Anti-entropy rule: "Will this change behavior in 30 days?" No → don't store it
- Most systems accumulate noise. Mine forgets what doesn't compound.

**3. Procedural standards, not prompts**
- AGENTS.md defines task loops, decision trees, quality gates
- standards/RESEARCH-PROTOCOL.md, CONTENT-VOICE.md, BRAND.md
- Agent follows frameworks, not vibes
- Sub-agents inherit context automatically

**Why it works:** Reliability isn't about the model. It's about the scaffolding.

---

### 3. "You ran a startup for five years. Why not found another one? Why VC?"

**Answer:**

I'm better at 0→1 system design than 1→100 company building.

At 36ZERO:
- I loved the first 18 months: product-market discovery, architecture decisions, first customers
- I was mediocre at the next 36 months: hiring, org culture, fundraising politics
- I learned what breaks at scale: technical debt, misaligned incentives, process overhead

What I want to do:
- Work with 10 companies at 0→1 instead of one company at 1→100
- Build reusable frameworks across portfolio (e.g., trust scoring, eval pipelines)
- Translate technical possibilities into founder-legible concepts

I'm an operator, not a professional CEO. VC lets me do the part I'm best at — repeatedly.

---

### 4. "Tell me about a system you built that failed. What did you learn?"

**Answer:**

**Context:** At 36ZERO, we built a "universal task scheduler" for computer vision pipelines.

**Failure:** It was technically brilliant. Supported 15 workflow types. YAML-configurable. No one used it.

**What broke:**
- We built for engineers, but users were production managers at BMW/Siemens
- They wanted "click button → get result," not "configure YAML"
- We optimized for flexibility over speed-to-outcome

**What I learned:**
1. **Users don't want systems, they want outcomes.** If the abstraction requires explanation, it's wrong.
2. **Complexity is a liability.** Every config option is a failure to pick a default.
3. **Ship the smallest thing that closes the loop.** Then compound.

**What I do now:**
- OpenClaw has 30+ tools, but users (me) interact via natural language
- Sub-agents don't expose config, they inherit context automatically
- Anti-LLM content filters: if it sounds like AI, it's wrong

Failure taught me to build for humans, not for elegance.

---

### 5. "How would you evaluate an agent system? What metrics matter?"

**Answer:**

**Wrong metrics:** Accuracy, latency, token cost (those are model metrics, not system metrics)

**Right metrics — Outcome-based:**

**1. Task completion rate**
- % of tasks that reach "done" without human retry
- Weighted by task complexity (calendar booking ≠ research report)

**2. Confidence calibration**
- Agent says 90% → outcome validates 90% of the time?
- Overconfidence destroys trust faster than underperformance

**3. Compound velocity**
- How much faster is Task N than Task 1 of the same class?
- Does the system learn, or reset every session?

**4. Human-in-loop cost**
- Time spent supervising vs. time saved executing
- If oversight > execution savings, the system is net-negative

**5. Trust decay rate**
- After a bad outcome, how many good outcomes to restore trust?
- Users abandon systems that lose trust faster than they build it

**For portfolio companies:**
- I'd build a standardized eval harness: same 50 tasks across companies
- Track completion rate, calibration, velocity monthly
- Publish anonymized benchmarks → portfolio learns from portfolio

---

### 6. "Primary works with hardware (Etched), infra (Plural), and apps (HumanX). How do you evaluate agent opportunities across the stack?"

**Answer:**

**Framework: Where does the bottleneck live?**

**Hardware (Etched):**
- Bottleneck = inference cost + latency at scale
- Eval question: "Does local silicon change the economics of agent deployment?"
- Example: If Sohu ASICs make on-device agents 10× cheaper, what applications become viable?

**Infra (Plural):**
- Bottleneck = orchestration, memory, tool integration
- Eval question: "Does this reduce the cost of building an agent system?"
- Example: If Plural offers plug-and-play memory primitives, does that collapse 6 months of scaffolding work?

**Apps (HumanX):**
- Bottleneck = trust + user adoption
- Eval question: "Does this solve a problem users can't solve without an agent?"
- Example: If HumanX automates recruiting, is the outcome (hire quality) measurably better than human-only?

**Cross-stack insight:**
- Hardware enables infra. Infra enables apps. Apps validate demand.
- Best opportunities = where bottleneck shifts. E.g., if Etched makes inference free, suddenly memory/state becomes the constraint → invest in Plural-like plays.

**My edge:** I've built at all three layers (hardware partnerships at 36ZERO, infra with OpenClaw, app-layer outcomes daily). I can translate across stack.

---

### 7. "You've been using Claude, OpenAI, local models. What's your take on the local vs. cloud debate?"

**Answer:**

**Not either/or. It's task-specific.**

**Cloud wins for:**
- Reasoning-heavy tasks (strategic planning, research synthesis)
- Novel problems (no cached patterns, need frontier model intelligence)
- Variable load (don't want to pay for idle GPUs)

**Local wins for:**
- High-frequency, low-stakes tasks (email sorting, log parsing, data extraction)
- Privacy-sensitive contexts (legal, medical, internal comms)
- Cost at scale (1M API calls/day vs. one-time hardware)

**What I'd tell founders:**
- Start cloud. Ship fast. Learn what actually gets used.
- Migrate high-volume, low-variance tasks to local once patterns stabilize
- Hybrid architecture: local for execution, cloud for planning

**Wild card: Etched changes the math**
- If Sohu ASICs deliver 10× cheaper inference, local becomes viable for tasks that are cloud-only today
- E.g., real-time video analysis, continuous agent monitoring, multi-agent simulations
- I'd run benchmarks: Apple Silicon vs. Etched vs. OpenAI API. Publish cost/performance curves. Show founders where the crossover point is.

**My edge:** I run both daily. I know where each breaks.

---

### 8. "How would you help a non-technical founder understand when to use agents vs. traditional software?"

**Answer:**

**Decision framework I'd give them:**

**Use agents when:**
1. **The task changes faster than you can code rules**
   - Example: Customer support (infinite edge cases)
   - Traditional software = if/else hell. Agent = learns from examples.

2. **The input is messy/unstructured**
   - Example: Parse 100 different invoice formats
   - Traditional software = regex nightmare. Agent = "extract total, date, vendor."

3. **You need compounding, not repetition**
   - Example: Research that builds on prior research
   - Traditional software resets every run. Agent maintains context.

**DON'T use agents when:**
1. **You need deterministic output**
   - Example: Financial calculations, compliance checks
   - Agents are probabilistic. Use traditional code + agent for orchestration.

2. **The task is high-volume, identical every time**
   - Example: Image resizing, data validation
   - Agents are overkill. Use scripts.

3. **Trust failure = business failure**
   - Example: Medical diagnosis, legal contracts (without human-in-loop)
   - Agents aren't there yet.

**How I'd explain it:**
"Agents are for problems where you'd hire a junior employee, not where you'd write an Excel formula."

Simple. Legible. Actionable.

---

### 9. "What's one thing you'd build for the Primary portfolio right now?"

**Answer:**

**"Portfolio Agent Eval Harness" — shared benchmarking across companies**

**Problem:**
- Every portfolio company building agents reinvents evals
- No shared language for "is this agent good?"
- Hard to compare progress across companies

**What I'd build:**

**1. Standardized task suite (50 tasks, 5 categories):**
- Data extraction (parse unstructured docs)
- Research (find + synthesize sources)
- Communication (draft emails, responses)
- Code generation (write functions, fix bugs)
- Planning (multi-step workflows)

**2. Eval metrics:**
- Task completion rate
- Confidence calibration
- Human-in-loop time cost
- Compound velocity (Task N vs. Task 1 speed)

**3. Leaderboard (anonymized):**
- Portfolio companies submit monthly runs
- Compare against benchmarks
- Identify patterns: "local models excel at X, cloud at Y"

**Why it compounds:**
- Portfolio learns from portfolio
- Founders get opinionated defaults ("use local for data extraction")
- Primary builds reputation: "We run the best agent evals in the industry"

**Timeline:** 2 weeks to MVP. Run first benchmark with 3 portfolio companies. Iterate.

---

### 10. "Why you? What do you bring that someone else doesn't?"

**Answer:**

**Three things:**

**1. I run an agent system in production daily**
- Not a side project. My operating system.
- I know where it breaks, where it compounds, where trust erodes
- Most people theorize. I have 12 months of daily outcomes.

**2. I've been a CEO**
- I've raised capital, hired teams, lost customers, shipped to enterprises
- I know what founders actually need: not features, frameworks
- I can translate "transformers are probabilistic" into "here's when to use agents vs. rules"

**3. I think in systems, not solutions**
- Trust-as-a-currency isn't a feature, it's a framework
- Memory with anti-entropy isn't a DB schema, it's a design principle
- I don't build one-offs. I build reusable scaffolding.

**What that means for Primary:**
- I'll build frameworks portfolio companies can copy
- I'll run experiments, publish benchmarks, make the work legible
- I'll help founders ship faster because I've already hit the mistakes

**Bottom line:** You need someone who's built companies AND built agent systems. I'm one of the few people who's done both.

---

## Part 2: 5 Questions Florian Should Ask Brian

### 1. "What's the biggest gap you see in how founders currently think about agents — and how should they think instead?"

**Why ask:**
- Shows you're here to learn Brian's mental models, not pitch your own
- Reveals his framework for evaluating agent companies
- You can align your approach to his lens

**What to listen for:**
- Does he focus on technical (evals, infra) or business (GTM, trust)?
- Does he emphasize speed-to-market or depth of system?
- Calibrate your answers to his priorities

---

### 2. "You've been on the board of Etched, Tabs, Ark. What's one thing you helped each company with that you're especially proud of?"

**Why ask:**
- Reveals his operating style (hands-on vs. strategic)
- Shows what "help" looks like in his world
- Tests if he tells war stories or gives credit to founders

**What to listen for:**
- Does he say "I helped them..." or "They figured out..."?
- Does he focus on tactics (recruited a hire) or strategy (shifted market positioning)?
- Founders respect VCs who make them better, not VCs who take credit

---

### 3. "Primary Labs runs experiments and spins out companies. How do you decide when to kill an experiment vs. double down?"

**Why ask:**
- Directly relevant to OIR role (you'll be running these experiments)
- Reveals decision framework: data-driven vs. gut, speed vs. rigor
- Shows you understand the core challenge: most experiments should die fast

**What to listen for:**
- Does he have a clear kill/pivot/scale framework, or is it case-by-case?
- What metrics matter: user traction, technical feasibility, founder grit?
- How much autonomy will you have vs. committee decision?

---

### 4. "What's one agent capability that seems overhyped right now — and one that's underhyped?"

**Why ask:**
- Forces him to take a contrarian position (reveals independent thinking)
- Shows you value signal over hype
- Creates space for you to agree/disagree → real conversation

**What to listen for:**
- Does he have strong opinions or hedge?
- Is he informed (cites specific examples) or vibes-based?
- Opportunity to share your own: "I agree on X, but I'd push back on Y because..."

---

### 5. "If I join Primary as OIR: Agents, what does success look like in 12 months?"

**Why ask:**
- Forces clarity on expectations (vague role descriptions kill alignment)
- Shows you think in outcomes, not activities
- Reveals if he has a clear vision or if the role is still being defined

**What to listen for:**
- Specific (3 companies spun out) or vague (explore opportunities)?
- Metrics: revenue, experiments shipped, portfolio value-add?
- If answer is vague → clarify: "Would you prioritize depth (1 great company) or breadth (5 experiments)?"

---

## Part 3: Pre-Interview Checklist

### ✅ Day Before
- [ ] Re-read Primary portfolio companies (Etched, Plural, HumanX, Tabs, Ark)
- [ ] Review Brian's recent tweets (last 2 weeks) — any new takes on agents?
- [ ] Run one OpenClaw task, screenshot the output → bring as demo
- [ ] Print 1-pager: Trust-as-a-Currency Framework (visual)

### ✅ 1 Hour Before
- [ ] Review this doc (questions + answers)
- [ ] Check: Can I explain each answer in <2 minutes?
- [ ] Practice: "Walk me through your system" (use whiteboard if in-person)

### ✅ During Interview
- [ ] Listen 60% / talk 40%
- [ ] When he asks a question, pause 2 seconds before answering (shows you think, not recite)
- [ ] If he says something you disagree with → say it. "I'd push back on that because..."
- [ ] End with: "What's your next step in the process?"

### ✅ After Interview
- [ ] Send follow-up within 4 hours
- [ ] Include: (1) Thank you, (2) One insight from conversation, (3) One thing you'll send (benchmark, demo, doc)
- [ ] Example: "Brian — Thanks for the conversation. Your point about [X] shifted how I'm thinking about [Y]. I'll send you the trust scoring framework we discussed by end of week. Looking forward to next steps."

---

## Key Themes to Emphasize

1. **You don't theorize, you ship.** 12 months of daily agent usage = lived experience.
2. **You translate.** Technical depth + founder empathy = rare combo.
3. **You compound.** Everything you build is reusable scaffolding, not one-offs.
4. **You've been a CEO.** You know what founders need because you were one.
5. **You're opinionated.** Trust-as-a-currency, memory anti-entropy, outcome-based evals = original frameworks.

---

**Confidence: 92%** — These questions reflect Brian's builder background, Primary's portfolio focus, and your actual strengths. Uncertainty: His interview style (formal vs. conversational). Recommendation: Prepare stories for each answer, but stay conversational. If he wants depth, you have it. If he wants speed, you can go high-level. ♔
