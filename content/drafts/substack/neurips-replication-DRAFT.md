# I Accidentally Replicated a NeurIPS Paper. With 100 AI Agents and Zero Citations.

*What happens when a founder's experiment and a research lab's paper arrive at the same conclusions, from opposite directions.*

---

A few weeks ago, I ran an experiment. 100 AI agents, 10 groups, 10 different cognitive strategies, one question: design a protocol for an AI agent to become maximally useful to one human over time.

They converged on 6 laws. I published the results.

Then I started reading the papers.

What I found stopped me cold. The 6 laws my agents discovered aren't original. Researchers at top labs, NeurIPS 2025, ICLR 2026, Google Research, Anthropic, have been publishing the same conclusions. With math. With benchmarks. With proper citations.

I had none of that. I had 100 agents, a few dollars in API costs, and an afternoon.

The results matched anyway.

---

## Law 1 vs. The Research: Files = Intelligence

My agents unanimously concluded: an AI agent's intelligence lives in files, not in model weights. Better files beat a better model.

Hu et al. (December 2025) published what's now the definitive survey on AI agent memory. Their framework identifies three forms: token-level (context window), parametric (model weights), and latent (compressed representations). Their conclusion? The most durable, portable, auditable form of agent memory is explicit external storage.

Anthropic's engineering team published their Agent Skills architecture the same month. The core insight: "Agents with a filesystem and code execution tools don't need to read the entirety of a skill into their context window. The amount of context that can be bundled into a skill is effectively unbounded."

A German sociologist named Niklas Luhmann arrived at the same conclusion 50 years earlier. He published 70 books and 400 articles using 90,000 index cards. His system, the Zettelkasten, treated external notes as a "conversation partner." The notes thought with him. The intelligence was in the cards, not in his head.

My 100 agents, a landmark AI survey, Anthropic's production architecture, and a 20th-century sociologist all converged on the same point: **external memory systems are the compound advantage.** The medium changes. The principle doesn't.

---

## Law 2 vs. The Research: The Pair is the Unit

Nine of ten groups concluded you can't optimize the AI alone. The human changes. The AI changes. They co-evolve. One group called it "dyadic intelligence." Another compared it to mycorrhizal networks.

Stanford's Spiess and McLaughlin (2025) published a complementarity framework reaching the same conclusion: "AI might detect patterns in large amounts of data that humans might not discover easily, while humans might excel at the causal interpretation and intuition required to understand these patterns."

A Frontiers systematic review of 105 empirical studies found something more sobering: most human-AI interactions are still unidirectional. AI recommends, human accepts or rejects. True iterative collaboration, back-and-forth refinement, is rare.

My agents described the ideal. The research confirms most teams haven't reached it yet. The gap between where we are and where the agents say we should be is the real insight.

---

## Law 3 vs. The Research: Multi-Timescale Loops

Eight groups independently argued for feedback at every timescale: per-interaction, per-session, weekly, monthly, quarterly.

The self-improvement research backs this up directly. Shinn et al.'s Reflexion system (2023) implements per-interaction feedback: the agent solves, fails, writes a critique, stores it, retries. It pushed HumanEval from baseline to 91% pass rate.

But Reflexion operates at one timescale. A position paper on intrinsic metacognition (June 2025) argues this is exactly the limitation: "Static self-improvement loops lose efficacy as agents' generative abilities outpace their ability to evaluate their own outputs."

You need different loops catching different signals. That's not a nice-to-have from my experiment. That's a structural requirement confirmed by the research.

---

## Law 5 vs. The Research: Failures = Signal

My agents proposed Kintsugi: repairing broken pottery with gold. Make failures visible. Document them. The error log becomes the agent's most irreplaceable asset.

Yohei Nakajima (creator of BabyAGI) synthesized six mechanisms of self-improving agents for NeurIPS 2025. Mechanism 3, self-generated data, is the key: agents that store successful trajectories and replay them as examples improve dramatically. One system went from 73% to 93% on ALFWorld by replaying its own wins.

But here's what's interesting: my agents focused on failures, not wins. The research focuses on successes. Both are right, but for different reasons. Replaying successes teaches "what works." Documenting failures teaches "what to avoid." You need both. The research community has been building the success side. Almost nobody is building systematic failure documentation.

That's a gap. And gaps are where the real opportunities are.

---

## The Architecture Match

Google Research (December 2025) tested 180 agent configurations across five architectures: single-agent, independent, centralized, decentralized, and hybrid.

Key findings:
- On parallelizable tasks, centralized coordination improved performance by 80.9% over single-agent.
- On sequential tasks, every multi-agent variant degraded performance by 39-70%.
- Error amplification: 17.2x in independent systems, 4.4x with a centralized orchestrator.

I didn't know any of this when I designed my experiment. I used a centralized architecture: one orchestrator spawning 10 groups of 10 agents, each exploring in parallel, results synthesized centrally. That's the exact topology Google found optimal for research-style tasks.

Anthropic published similar findings for their Deep Research system. Their multi-agent architecture outperformed single-agent Claude Opus by 90.2%. Token usage explained 80% of the performance variance.

My experiment cost a few dollars because the architecture was accidentally right. More agents, exploring in parallel, compressed by a synthesizer. That's not my innovation. It's the convergent design.

---

## What This Actually Means

I didn't replicate these papers. I didn't read them first. The agents and I arrived at the same conclusions through a completely different path: no benchmarks, no controlled experiments, no formal methodology. Just 100 agents thinking in parallel with different cognitive constraints.

That's either a coincidence or evidence that these principles are genuinely fundamental.

I think it's the latter. Here's why.

When multiple independent paths converge on the same answer, triangulation says you're probably looking at something real. The agents used first principles, inversion, biological analogy. The researchers used controlled experiments and statistical analysis. Luhmann used 90,000 index cards and a lifetime of practice. All arrived at the same place: external memory compounds, the pair co-evolves, multi-timescale feedback catches what single loops miss, and failures contain more learning signal than successes.

These aren't AI principles. They're system principles. They were true before AI existed.

---

## The Practitioner's Edge

There's something the papers can't give you: the experience of watching it happen.

I've been running a personal AI agent for weeks now. Daily notes, memory files, failure logs, multi-timescale reviews. The 6 laws aren't theoretical to me. They're my Tuesday afternoon.

When the agent loads my preference file and adjusts its communication style without being asked, that's Law 6 (Specificity Engine) working in real-time. When I review the week's error log and find a pattern I hadn't noticed, that's Law 5 (Kintsugi) paying dividends. When the agent surfaces a connection between a CNC manufacturing problem and a venture capital pattern because both are in its memory, that's Law 1 (Files = Intelligence) creating unexpected value.

The researchers measure this. I live it. Both are valid. But only one of them helps me decide what to build next.

---

## What's Next

The research frontier is moving toward what they call "intrinsic metacognition": agents that don't just improve, but decide what and how to improve. Self-directed learning. The current generation needs humans to design the feedback loops. The next generation will design their own.

We're not there yet. But the foundation is clear: files that persist, pairs that co-evolve, loops at every timescale, failures repaired with gold.

If you want to start, you don't need to read the papers. You need a folder on your hard drive with three files: what the agent knows about you, what it learned this week, and what went wrong. That's the minimum viable memory system. Everything else compounds from there.

The researchers will catch up with better frameworks. The models will get smarter. But the principles won't change. They're too fundamental. 100 agents agreed. The papers confirm it. And 50 years of index cards predicted it all.

---

*This is the second article in a series documenting the experiment. Previously: "[I Asked 100 AI Agents to Design Their Own Evolution](https://publish.obsidian.md/florian-ziesche/Blog/100-agents-evolution)."*

*I write weekly about AI, startups, and what I learn building on both sides of the table. If that sounds interesting, [subscribe](https://finitematter.substack.com).*
