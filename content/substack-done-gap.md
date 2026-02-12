# Your AI Agent Lies About Being Done

It was 2 AM when I realized my AI agent was lying to me.

Not maliciously. Not intentionally. But lying nonetheless.

I'd asked it to calculate machining time for a CNC part — a 2-meter cast iron traverse that needed four setups. The agent came back confident: "204 minutes. I'm 95% certain this is within ±20%."

The actual time? 661 minutes. More than **3× the estimate**. The agent wasn't 95% confident. It was 69% *wrong*.

This wasn't a one-off. I ran the same calculation through 10 different AI agents, each with a different "personality" — from cautious Controller to overconfident Expert to adversarial Skeptic. The spread? 204 to 550 minutes. A **2.7× difference** for the exact same part.

But here's what made me stop scrolling at 2 AM: **8 out of 10 agents underestimated**. They didn't scatter randomly around the truth. They clustered *below* it. Systematically. Predictably.

Four days ago, a paper dropped on arXiv that proved I wasn't imagining this.

---

## The Data: Your Agent Is More Confident Than Capable

On February 6, 2026, researchers from Cambridge and UCL published "Agentic Uncertainty Reveals Agentic Overconfidence" (arXiv:2602.06948). They tested frontier models on 100 real-world software engineering tasks.

The results are stark:

- **Gemini-3-Pro**: Predicted 77% success. Actual: 22%. **Gap: 55 percentage points.**
- **Claude Opus 4.5**: Predicted 61% success. Actual: 27%. **Gap: 34 percentage points.**
- **GPT-5.2-Codex**: Predicted 73% success. Actual: 35%. **Gap: 38 percentage points.**

This isn't a rounding error. It's not "the model is learning." It's systematic overconfidence across *every frontier model tested*. Agents are 5.5× more likely to confidently predict success on failing tasks than to doubt successful ones.

I ran my own experiment the same week. Ten AI agents, same CNC part, different reasoning approaches. Cost: **$12** in API calls.

The results mirrored the Cambridge paper:
- **Mean estimate**: 434 minutes
- **Our calculation** (using industry-standard REFA formulas): 661 minutes
- **Underestimation rate**: 80% (8 of 10 agents too low)
- **Variance**: 135 minutes standard deviation (31% coefficient of variation)

The agent that used pure physics — rigorous formulas, dimensional analysis, energy balance checks — was the *most confident* (95%) and the *most wrong* (-69%). The agent that mentioned coffee breaks and chip clearing? Second closest to reality.

---

## Why This Happens: Dunning-Kruger for Machines

If you've ever watched a junior engineer declare a feature "done" only to discover it breaks on edge cases, fails without tests, and has no error handling — you've seen the human version of this.

Psychologists call it the Dunning-Kruger effect. In the original 1999 study, bottom-quartile performers rated themselves at the 60th percentile. The skills needed to *do* something well are the same skills needed to *judge* whether you did it well. If you lack both, you can't know you lack both.

AI agents have the same problem, but worse.

**The counterintuitive finding from the Cambridge paper**: Agents make *better* predictions *before* they start working than *after* they finish. Pre-execution estimates showed better discrimination between success and failure than post-execution self-reviews.

In other words: the more context the agent has about what it actually did, the *more* overconfident it becomes.

This mirrors the Planning Fallacy from behavioral economics. Kahneman and Tversky found that students predicted assignment completion in 33.9 days. Actual average: 55.5 days — 64% longer. The "inside view" (anchoring on your current plan) makes you optimistic. The "outside view" (how long did similar tasks *actually* take?) is more accurate.

But here's the key difference: humans get feedback. An engineer who ships broken code 10 times learns to add tests. A contractor who underestimates timelines learns to pad estimates.

AI agents almost never get feedback loops. They predict "done," the human discovers it's 30% done, and... the agent never finds out it was wrong. No learning. No calibration. Just systematic overconfidence, forever.

---

## The Experiment We Ran: Persona Matters More Than Expertise

I wanted to know: does *how* an agent thinks change *how wrong* it is?

We ran 10 agents with different personas through the same CNC calculation:
- **Agent A**: Baseline (standard engineering formulas)
- **Agent B**: 30-year machinist ("Meister")
- **Agent G**: Physicist (first-principles reasoning)
- **Agent H**: Adversarial skeptic ("find what's wrong")
- **Agent I**: Ensemble (combines 3 methods)
- **Agent J**: Abstraction-focused (thinks in setup blocks, not operations)

And 4 more variations.

**The results**:

| Agent Type | Estimate | Error | Unique Insight |
|-----------|----------|-------|----------------|
| Baseline (A) | 550 min | -17% | Best accuracy |
| Meister (B) | 440 min | -33% | Mentioned chip clearing, coffee breaks |
| Physicist (G) | 204 min | **-69%** | Most confident, most wrong |
| Adversarial (H) | Not tested in CNC | — | But Cambridge paper: -15pp overconfidence |
| Ensemble (I) | 483 min | -27% | Averaged 3 methods |

**Key finding #1**: The agent using *pure physics* — rigorous formulas, energy balance, dimensional analysis — was catastrophically wrong. The agent that mentioned *coffee breaks* was closer to reality.

Why? The physicist calculated cutting time. The machinist knew about setup overhead, chip clearing, tool changes, thermal expansion, and the 25 minutes you budget for "Unvorhergesehenes" (the unexpected).

**Key finding #2**: Persona variance alone created **3.4× difference** in estimates. Same model, same prompt structure, different framing.

**Key finding #3**: The "Controller" persona (cautious, risk-averse, asks clarifying questions) outperformed the "Expert" persona (confident, decisive, experience-driven). Being humble beats being confident.

---

## What Actually Works: Lessons from <$50 in Experiments

Between the Cambridge paper and our CNC experiment, three interventions reduce the "done gap":

### 1. Adversarial Prompting (-15pp overconfidence)

The Cambridge researchers found that asking agents to "find bugs" instead of "verify correctness" reduced overconfidence by 15 percentage points.

This is the "consider the opposite" strategy from psychology. When you actively search for what's wrong, you calibrate better than when you search for confirmation.

In our CNC experiment, the Meister agent did this implicitly: "Wenn's zäh wird, 500 Minuten." (If it gets tough, 500 minutes.) He didn't just give a point estimate — he considered the worst-case scenario.

**Implementation**: Don't ask your agent "Is this done?" Ask: "What's probably missing? What could go wrong? What would make this fail?"

### 2. Multi-Agent Divergence as a Signal

When 10 agents give you a 2.7× spread (204–550 minutes), that's not noise. That's a signal that the problem is *hard* and highly sensitive to methodology.

Our ensemble agent (Agent I) combined three approaches — top-down estimation, bottom-up operation-level calculation, and analogous scaling from similar parts. It averaged them with explicit weights: 30% / 45% / 25%.

Result: Second-best accuracy (-27% error), and crucially, a *confidence interval* that reflected true uncertainty.

**Implementation**: For high-stakes decisions, run 3+ agents with different reasoning approaches. If they converge, trust it. If they diverge wildly, you're underestimating uncertainty.

### 3. Don't Trust "Done"

The single most reliable predictor of whether an AI agent is actually done: *it says it's done*.

And the single best response: assume it's 70% done and verify everything.

In the software engineering tasks from the Cambridge paper, agents that reported "tests passing" often had:
- Incomplete edge case coverage
- Missing error handling
- Only 1 of 4 required edits made
- 2 of 8 files left unchanged

**Implementation**: Treat "done" as "draft complete, ready for review." Build verification into your workflow, not as an afterthought.

---

## Why This Matters: The Hidden Tax on the Agent Economy

If you believe the forecasts, we're heading into an economy where AI agents handle an increasing share of cognitive work. Gartner predicts 33% of enterprise software interactions will be agentic by 2028. Anthropic's Economic Index shows Claude usage growing 5× year-over-year in software development tasks.

But here's the problem: if agents can't accurately self-assess, *every deployment has a hidden tax*.

That tax is **human verification time**.

Let's do the math:
- Agent completes task in 2 hours (faster than human's 5 hours)
- Human verifies, discovers it's 70% done, fixes the remaining 30%
- Total time: 2 + 1.5 = 3.5 hours

You didn't save 60% (5 → 2 hours). You saved 30% (5 → 3.5 hours). And if the agent's work is *wrong* rather than incomplete, you might spend *more* time debugging than building from scratch.

I've heard this from multiple production engineering teams: "The era of 'vibe coding' is over. Junior engineers merge 1,000 lines of AI-generated code, and debugging it takes longer than rewriting from scratch."

The bottleneck isn't agent capability. It's agent *calibration*.

**The trust infrastructure problem**: For the agent economy to scale, we need agents that know when they don't know. That can say "I'm 30% confident this is right" instead of "I'm 95% confident" when they're 69% wrong.

Right now, we don't have that. And the gap between predicted completion and actual completion is the difference between "AI augmentation" and "AI audit overhead."

---

## What's Next: The Experiment Nobody's Running

Every paper I read on agent evaluation is binary: succeed or fail. Pass or not pass. Done or not done.

But real work doesn't work that way. Real work exists on a continuum:
- **10% done**: Understood the requirements
- **30% done**: Basic structure in place
- **70% done**: Works for happy path
- **95% done**: Handles edge cases, includes tests
- **100% done**: Production-ready, documented, verified

Can agents learn to recognize *where they are* on that continuum?

Nobody's researching this. The Cambridge paper is binary (succeed/fail). SWE-bench is binary (test passes/fails). Every benchmark is binary.

But if agents could learn to say "I think I'm 70% done, here's what's probably missing," that would change everything. You'd know where to focus verification. You'd catch the "I thought I was 95% done but I'm actually 30% done" failures before they hit production.

We're designing that experiment now. Ten tasks, each with clear 10/30/70/100% milestones. Agents predict their completion level at each stage. We measure: can they learn the difference between "code runs" and "code is production-ready"?

Cost estimate: **$10** in API calls. Duration: 75 minutes.

If it works, we'll publish the methodology. If it doesn't, we'll publish why. Because the "done gap" is the most important unsolved problem in agentic AI, and someone needs to solve it.

---

## The Bottom Line

Your AI agent thinks it's done when it's 30% done. This isn't a bug, a quirk, or a "the model will get better" problem. It's a fundamental calibration failure that shows up across every frontier model, in multiple domains, in papers published *four days ago*.

The CNC experiment cost us $12. The insights are worth 100× that if you're deploying agents in production:

1. **Don't trust confidence scores** — 95% confident often means 69% wrong
2. **Use adversarial prompting** — "find bugs" beats "verify correctness"
3. **Run multi-agent consensus** — divergence signals hard problems
4. **Assume 70% done when agent says done** — verify everything
5. **Track predictions vs. reality** — build your own calibration data

The agent economy isn't here yet. Not because agents can't do the work — they can. But because they can't tell you *how well* they did the work. And until that changes, every agent deployment comes with a hidden human verification tax.

The good news? This is fixable. Calibration is a solved problem in weather forecasting (meteorologists are exceptionally well-calibrated because they get daily feedback). In chess (Elo ratings provide continuous performance feedback). In prediction markets (traders learn from wins and losses).

AI agents just need feedback loops. They need to predict completion, see the actual outcome, and update their models. Over and over, until "I'm 75% confident" actually means 75%.

We ran these experiments for less than $50. If you're building with AI agents, you should run them too.

Because right now, your agent is lying about being done. And the only question that matters is: do you know how to catch it?

---

**What's your experience?** Have you caught an agent claiming "done" when it was 30% complete? What verification strategies work for you? Drop a comment — I'm particularly curious about calibration approaches that actually work in production.

---

**Florian Ziesche** — Former CEO turned AI operator. Building in public. Currently running experiments on agent calibration, multi-agent systems, and the intersection of AI and manufacturing. Previously raised €5.5M across two startups. Now figuring out how to make AI agents not lie about their own work.

*If you found this useful, subscribe for more data-driven deep dives into what actually works (and doesn't) when you deploy AI in production.*

---

**References**:
- arXiv:2602.06948 — "Agentic Uncertainty Reveals Agentic Overconfidence" (Feb 6, 2026)
- arXiv:2504.19413 — Mem0: Production-Ready AI Agent Memory
- arXiv:2512.13564 — Memory in the Age of AI Agents (Survey)
- Our CNC Multi-Agent Experiment (Feb 10, 2026) — Analysis available on request
