# I Built 100 AI Agents in 48 Hours. Here's What I Learned.

**Subtitle:** A sprint experiment in systematic AI deployment — from sub-agent orchestration to quality metrics.

**Category:** Human-AI Systems

**Status:** DRAFT for Substack

---

Last weekend, I ran an experiment: build 100 specialized AI agents in 48 hours. Not as a stunt — as a stress test for systematic agent deployment.

The goal wasn't quantity. It was to find the breaking points in orchestration, quality control, and human-AI collaboration at scale.

Here's what I learned building everything from CNC cost calculators to legal document analyzers to blog content pipelines — and what broke along the way.

---

## Why 100 Agents?

Most people deploy AI like this:
1. Hit a problem
2. Prompt ChatGPT/Claude
3. Copy-paste result
4. Repeat tomorrow

This works — until you want to compound. If every interaction is isolated, you're renting intelligence, not building it.

The alternative: **systematic agent deployment**. Each agent is a reusable unit with:
- Clear scope (what it does, what it doesn't)
- Defined inputs/outputs
- Quality metrics
- Failure modes documented

100 agents forces you to solve problems that don't show up at 5:
- How do you prevent agents from hallucinating?
- How do you orchestrate sub-agents without losing control?
- What's the failure mode when an agent hands off to another agent?
- How do you measure quality when you can't manually review everything?

---

## The Architecture

**Primary Agent (Opus 4.6):** Orchestrator. Receives user request, decides which specialized agents to deploy, synthesizes results.

**Sub-Agents (Sonnet 4.5):** Specialists. Each handles one domain:
- Research (web search, summarization)
- Writing (blog posts, emails, documentation)
- Analysis (data, documents, code)
- Translation (EN ↔ DE)
- Red Team (challenge assumptions, find edge cases)

**Model Selection Rules:**
- Opus for main session, synthesis, strategy (high reasoning)
- Sonnet for sub-agents (fast, reliable, 80% of tasks)
- Haiku for heartbeats, checks, monitoring (ultra-fast)

**Key Insight:** Don't use the most powerful model for everything. Use the *right* model for each task. Sonnet at $3/MTok vs Opus at $15/MTok = 5× cost savings with minimal quality loss on focused tasks.

---

## What Worked

### 1. Parallel Sub-Agent Deployment

For complex tasks, deploy 3-5 agents in parallel, then synthesize.

**Example: Blog Concept Development**
- Agent 1: Research competitive blogs
- Agent 2: Analyze positioning opportunities
- Agent 3: Red team assumptions
- Primary Agent: Synthesize into v2 concept

**Result:** Better than sequential prompting. Each agent explores independently, reducing anchoring bias.

### 2. Red Team Everything

For every output agent, deploy a red team agent.

**Example: VC Application Cover Letter**
- Writer Agent: Drafts letter
- Red Team Agent: "What's weak? What's missing? What will a skeptical reader dismiss?"
- Primary Agent: Integrates feedback into v2

**Result:** Outputs that survive scrutiny. The red team agent caught:
- Vague claims ("extensive experience" → specific metrics)
- Missing context (assumed reader knows background)
- Tone mismatches (too formal for startup, too casual for established fund)

### 3. Structured Output Formats

Every agent returns structured data, not prose.

**Bad:**
> "The CNC planner should probably use REFA time standards and maybe add material costs..."

**Good:**
```json
{
  "recommendation": "Use REFA time standards",
  "confidence": 0.85,
  "alternatives": ["Manual time entry", "ML-predicted times"],
  "trade-offs": "REFA = industry standard but conservative estimates",
  "next_steps": ["Validate against 10 real parts", "Compare to ERP output"]
}
```

**Why:** Structured outputs force clarity. You can't hide uncertainty in prose. And they're composable — one agent's output becomes another's input without parsing ambiguity.

---

## What Broke

### 1. Context Compaction Crashes

**Problem:** Long tasks hit context limits. OpenClaw auto-compacts context by summarizing old tool_use/tool_result pairs.

**Failure Mode:** Sometimes compaction separates a tool_use from its tool_result. Agent crashes because it's waiting for a result that was already compacted away.

**Solution:** ACTIVE_TASK.md. Before any non-trivial task:
1. Update ACTIVE_TASK.md with: Goal, Steps, Status, Intermediate Results
2. Do the work
3. If crash → read ACTIVE_TASK.md and resume
4. On completion → clear ACTIVE_TASK.md

Files survive. Context doesn't.

### 2. Agents Built Structure, Not Design

**Problem:** Deployed 15 sub-agents to build Ainary Ventures website. Agents produced:
- ✅ Semantic HTML
- ✅ Content architecture
- ✅ Responsive layout
- ❌ Actual design (spacing, typography, visual polish)

**Why:** Specs were too abstract. "Implement gold shimmer" → agent writes `.hero-shimmer` class but doesn't define `@keyframes`. "Use design tokens" → agent references `var(--gold-warm)` but doesn't set proper values.

**Solution:** Reference-driven building. "Make Hero like anthropic.com" → screenshot → extract exact CSS → pixel-perfect implementation. Agents are great at matching patterns, bad at inventing aesthetics.

### 3. Prepared:Sent Ratio Explosion

**Problem:** 9 CNC outreach emails ready. 0 sent. 3 VC cover letters polished. 0 submitted. Reports? Perfect. Deck? Beautiful. Revenue? €0.

**Why:** Building feels productive. Sending feels risky. Agents amplify this—they make it trivially easy to build more without forcing you to ship.

**Solution:** Build-blocker script. Before starting ANY new build task:
```bash
./scripts/pre-build-check.sh "Feature Name"
```

If >2 features built today with 0 external sends → BLOCKED. Must send 1 thing first, then resume building.

**Lesson:** Agents make you dangerous at execution. But they won't fix procrastination. You still have to ship.

---

## Quality Metrics That Actually Work

You can't manually review 100 agent outputs. You need automated quality signals.

### 1. Confidence Scores

Every agent returns:
```json
{
  "output": "...",
  "confidence": 0.85,
  "uncertainty": ["Assumption X not validated", "Edge case Y unclear"]
}
```

**Rule:** confidence <0.7 → flag for human review.

### 2. Citation Validation

For research/analysis agents:
- Every claim must cite a source
- Source must be reachable (URL returns 200)
- Quote must exist in source (fuzzy match)

**Example:** Legal AI agent analyzing contracts. <0.2% hallucination rate because every extracted clause includes page number + exact quote.

### 3. Contradiction Detection

Deploy 2 agents for the same task (different approaches). If outputs contradict → flag for review.

**Example:** CNC cost calculation. Agent 1 uses REFA standards. Agent 2 uses historical actuals. If deviation >15% → human decides which is right.

### 4. Changelog Tracking

Every agent logs:
- Input hash
- Output hash
- Model used
- Timestamp
- Parent task

**Why:** When something breaks, you can trace: "This agent produced bad output because it received corrupted input from Agent X at 14:32."

---

## The Compounding Flywheel

100 agents isn't the goal. It's the foundation for compounding intelligence.

**Traditional AI use:**
- Ask question → get answer → forget context
- Tomorrow: start from zero

**Agent-based system:**
- Task → specialized agent → structured output → saved to knowledge base
- Tomorrow: agents reference yesterday's outputs
- Next week: agents learn from patterns across 50 tasks

**Example:** After 20 CNC cost calculations, the system knows:
- Typical deviations per material
- Which suppliers are consistently cheaper
- Seasonal price fluctuations
- Common estimation errors

An isolated ChatGPT session never learns this. A systematic agent system compounds.

---

## What I'd Do Differently

### 1. Start with 10 Core Agents, Not 100

**Better:**
- 3 research agents (web, documents, data)
- 2 writing agents (long-form, short-form)
- 2 analysis agents (technical, business)
- 1 red team agent
- 1 translation agent
- 1 orchestrator

**Then:** Specialize as needed. Don't build 50 niche agents upfront.

### 2. Build Quality Scaffolding First

Before deploying agents at scale:
- Confidence scoring system
- Structured output templates
- Automated citation validation
- Contradiction detection
- Failure logging

**Why:** Fixing quality issues after deploying 100 agents = archaeology. Build the safety net first.

### 3. Enforce Shipping Cadence

**Rule:** Every 3 build tasks → 1 external send.

Don't let agent productivity become a procrastination amplifier.

---

## The Honest Take

Building 100 agents in 48 hours was educational. Would I recommend it? No.

**Better approach:**
- Build 10-15 core agents systematically
- Deploy them on real work for 2 weeks
- Find breaking points
- Fix quality/orchestration issues
- Then scale

**But the experiment proved:**
- Multi-agent systems work at scale (if you build quality scaffolding)
- Opus for synthesis, Sonnet for sub-agents is the right model split
- Structured outputs > prose
- Red teams > reviews
- Files > memory
- Shipping > building

**The meta-lesson:** AI agents amplify your existing patterns. If you build without shipping, agents make you build faster without shipping. If you ship, agents make you ship faster.

The tools are ready. The question is whether you are.

---

*Florian Ziesche is a former startup CEO (€5.5M+ raised) building AI systems for manufacturing and legal AI. He writes about applied AI, systematic agent deployment, and human-AI collaboration at [ainaryventures.com](https://ainaryventures.com).*
