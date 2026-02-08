# Sequoia Says AGI Is Here. They're Right — And They're Not.

**Subtitle:** The world's sharpest VCs got the milestone right but named the wrong finish line.

**Category:** AI Intelligence

**Status:** DRAFT for Substack

---

Sequoia Capital just published "2026: This is AGI." Not "getting close." Not "almost there." **This is AGI.**

Coming from one of the most sophisticated technology investors on the planet, this isn't hype — it's a thesis. And the data is genuinely impressive.

METR benchmarks show AI task horizons doubling every ~7 months — and accelerating. Claude Opus 4.5 now solves roughly 50% of tasks that take human experts five hours. These systems chain reasoning, use tools, debug their own errors, and persist through multi-hour assignments. Sequoia's definition: AGI is "the ability to figure things out." Three ingredients — pre-training (knowledge), inference-time compute (reasoning), long-horizon agents (iteration).

I want to respect this argument. When Sequoia stakes a claim this bold, it deserves serious engagement, not a hot take.

But as someone who ships AI into factories and enterprises daily, I see something their framework misses. Not because they're wrong about what AI can do today — but because their definition obscures what it still can't.

**The gap isn't streaming input. It's world models.**

---

## What They Got Right

Let's be honest: the agents arriving right now are qualitatively different from the chatbots of 2023.

Sarah Guo's framing nails it: "Soon you'll be able to hire an agent." Not prompt one. *Hire* one. Give it a problem, walk away, come back to results. Sequoia's recruiting example — where an agent autonomously pivots from LinkedIn to YouTube talks to Twitter engagement to draft personalized outreach in 31 minutes — that's real. I've seen my own AI agent produce research briefs, draft technical documents, and run multi-step analyses that would have taken me days.

The METR data is hard to argue with: six years of consistent exponential growth in task horizons. Recent models are revising *upward*. The doubling time is compressing from 7 months to 3. If you believe the trend, full-day tasks by 2028 and year-long tasks by 2034 aren't unreasonable extrapolations.

So yes — something genuinely new is here. Sequoia isn't wrong about the milestone.

They're wrong about what it means.

---

## The World Model Gap

Here's what current AI actually does, no matter how sophisticated the agent scaffold:

1. Receives a context window (a snapshot of the world)
2. Processes that snapshot
3. Returns output
4. Waits for the next snapshot

You can make this loop faster. You can make the context window larger (Gemini does 1M+ tokens). You can add tool use so the model queries databases and APIs between steps. OpenAI's Realtime API even processes streaming audio with <200ms latency.

But none of this solves the fundamental problem: **current AI doesn't maintain a predictive model of the world that continuously updates.**

A human working on a complex task doesn't just process information — they *anticipate*. You watch a cup sliding toward a table edge and reach for it *before* it falls. You sense a negotiation shifting and adjust your strategy *as* it happens, not after someone summarizes the meeting for you. You build causal models from continuous observation: "the line is running hot today," "this client seems distracted," "the market tone shifted this week."

Current AI — even Sequoia's "generally intelligent agents" — reacts to what happened. It doesn't anticipate what's about to happen.

As Angjoo Kanazawa at UC Berkeley put it: "How do you develop an intelligent system that can actually have streaming input and update its understanding of the world? That's a big open problem. I think AGI is not possible without actually solving this problem."

---

## Where This Shows Up in Production

The gap is invisible on benchmarks. It's obvious in deployment.

**On a manufacturing floor:** We shipped computer vision to automotive OEMs — BMW, Siemens, Bosch. The models were excellent on static images. But manufacturing is continuous: lighting shifts, material batches vary, operators adjust settings. A snapshot-based system processes Frame 1, returns a verdict, processes Frame 2. Each judgment is isolated. It never builds a model of "this shift is running differently than yesterday." The operators know. The AI doesn't.

**In a newsroom:** AI can draft articles from briefs. But a reporter working a breaking story continuously integrates new signals — a source texts back, another outlet publishes an angle, a livestream reveals something unexpected. The reporter's mental model updates in real-time. Current AI requires you to re-prompt: "Here's the update, regenerate." It's a writing tool, not a colleague tracking the story alongside you.

**In legal negotiations:** AI reads contracts and flags risks brilliantly — on static documents. But during a live deal, terms shift across emails, calls, and side conversations. A human negotiator maintains a living model of "where we stand right now." An AI agent processes each update as a separate batch.

Factory.ai identified the deeper technical constraint: even million-token context windows suffer "context rot" — models don't use their context uniformly, and performance degrades as input grows. Bigger windows aren't the answer. Better world models are.

---

## The Honest Counter-Argument

I want to steelman Sequoia's position, because the strongest version of their argument has teeth:

**"Does continuous world modeling actually matter for knowledge work?"**

Maybe not — for most tasks. Writing code, analyzing data, conducting research, drafting documents — these are deliberative tasks where batch processing is genuinely sufficient. You don't need real-time perception to debug a function or write a legal brief.

Even human cognition is more "chunked" than we like to admit. We experience attentional blinks, change blindness, saccadic suppression. Our perception isn't truly continuous either — it's just faster and more integrated than current AI loops.

And the engineering is converging on something that *approximates* streaming: fast inference + tool use + long context + MCP creates observation loops that run at seconds-level frequency. For many applications, that's good enough.

This is why Sequoia's definition works *for knowledge work AGI*. If you define the problem as "automate economically valuable cognitive tasks," then yes — snapshot-based agents with tight iteration loops will capture most of the value.

**But Sequoia didn't say "Knowledge Work AGI." They said "AGI."**

And general intelligence requires something these systems fundamentally lack: a persistent, predictive model of the world that updates in real-time. The kind of understanding that lets you walk into a room and immediately sense that something is off. The kind that lets a master craftsman feel when a machine is about to fail. The kind that makes a great investor read a founder's micro-expressions and adjust their thesis mid-conversation.

---

## What This Means

**For builders:** The biggest opportunity is closing the world model gap. Not just faster loops — genuine continuous understanding. Persistent state, predictive models, anticipatory behavior. The interfaces of the future won't be prompt-and-response; they'll be AI that's *present* — maintaining awareness and surfacing insights without being asked.

**For investors:** Sequoia's "hire an agent" framing will drive massive value creation in knowledge work over the next 24 months. That's the obvious bet. The asymmetric bet is in persistent world models — the companies building AI that doesn't just process the world but genuinely understands its state in real-time. Embodied AI, ambient computing, continuous monitoring systems. That's where the next platform shift lives.

**For enterprises:** Deploy current agents aggressively for well-defined cognitive tasks. They're ready. But temper expectations for roles that require continuous situational awareness. Your AI can analyze the quarterly results. It can't yet walk the factory floor and sense what's different today.

---

## The Gold in the Cracks

Sequoia's essay will be directionally right in retrospect. The milestone they're naming is real. The agents arriving now will reshape industries and create enormous value.

But calling this AGI — without qualification — papers over the most important frontier in AI. We've built brilliant batch processors. We have not yet built systems that maintain continuous understanding of the world.

The distinction matters because **the next breakthrough isn't bigger context windows or deeper reasoning on static problems. It's persistent world models — AI that doesn't just process snapshots of reality but genuinely inhabits time.**

If that sounds abstract, here's a concrete test: Can an AI watch a 10-minute video and predict what happens next — not from pattern matching, but from understanding the physics, intentions, and dynamics at play? Can it maintain object permanence when things move off-screen? Can it detect a change in mood from watching a conversation unfold?

Today, the answer is no. When the answer is yes, we'll have something worth calling AGI.

Until then, we have something remarkable, transformative, and genuinely new. Just not quite what Sequoia named it.

The gold is in the cracks between what we've built and what we're building next.

---

*Florian Ziesche is a former startup CEO (€5.5M+ raised, shipped AI to BMW, Siemens, and Bosch) and now works as an AI consultant and VC Lab Fellow. He writes about applied AI, venture capital, and the future of human-AI collaboration at [ainaryventures.com](https://ainaryventures.com).*
