# Why AI Agents Can't Trust Each Other

*And why that's a bigger problem than most people realize*

---

My AI agent sold me an assumption as a fact today. And nobody caught it.

I run a multi-agent system — specialized AI agents that research, write, analyze, and quality-check each other's work. It's the kind of setup that sounds impressive on paper. This morning, my research agent delivered a brief about my time allocation. Buried in the analysis was a claim: "Ainary Ventures consumes significant time." Stated as fact. No hedge, no caveat, no source.

The problem? It was an assumption. There was zero data backing it. No time tracking, no logs, nothing. My agent made a reasonable-sounding guess and dressed it up as a finding.

I only caught it because I happened to know better. If I hadn't — if this had been a domain where I don't have direct experience — I would have made decisions based on fiction. And here's the uncomfortable part: this wasn't a bug. This is how these systems work by default.

---

## The Overconfidence Problem Is Worse Than You Think

There's a study from early 2025 that I keep coming back to. Researchers tested 9 different LLMs across 351 scenarios and found that **84% of all scenarios showed overconfidence** — meaning the models expressed higher certainty than their actual accuracy warranted. Four out of nine models were overconfident in *every single scenario* they were tested on.

Let that sink in. Not "sometimes overconfident." Not "occasionally miscalibrated." In 84% of cases, these models thought they were more right than they actually were.

I've seen this play out in my own system. I have an outreach agent that evaluates email drafts. In one run, it self-assessed its output quality at 85%. When I actually measured against the criteria it was supposed to hit, the real score was closer to 75%. A 10-percentage-point gap might not sound dramatic — until you realize decisions get made on those numbers.

The research confirms this isn't a quirk of one model. A January 2026 study put it bluntly: verbalized confidence approaches — where you simply ask the model how sure it is — are "systematically biased and poorly correlated with correctness." The models aren't lying. They genuinely can't tell you how much they know. They're like the colleague who answers every question with the same unwavering certainty, whether they're talking about their area of expertise or something they read on a blog once.

And here's what makes this insidious: instruction tuning — the process that makes AI models helpful and conversational — actually makes the calibration *worse*. The same training that teaches models to be useful also teaches them to sound confident. There's a technical term for this: probability mass polarization. In plain English: the better a model gets at being helpful, the worse it gets at expressing uncertainty.

---

## Multi-Agent Systems Multiply the Problem

Now take that overconfidence and put it in a pipeline.

In my setup, a research agent gathers data. A writer agent turns it into content. A QA agent reviews the output. Each agent trusts the previous one's work as input. If the research agent is overconfident about a claim, the writer agent builds narrative around it, and the QA agent — which is also an LLM — has no independent way to verify the original data.

This is the trust stacking problem. Agent A produces output with, say, 80% actual reliability. Agent B takes that as ground truth and adds its own 80%-reliable analysis on top. The compounded reliability, if errors compound independently? 64%. Add a third agent, and you're at 51%. You've crossed into coin-flip territory within three steps of a pipeline.

*My interpretation:* I think most multi-agent systems in production today are operating at much lower effective reliability than their builders assume — precisely because nobody is tracking compounded confidence degradation.

The major frameworks don't solve this. I've looked at all of them:

**LangChain/LangGraph** — 70 million downloads per month. Excellent orchestration. Graph-based workflows with full control over agent coordination. But trust between agents? Not addressed. They give you observability (94% of developers with production agents use it, according to their own State of Agent Engineering report), which means you can *see* what happened after the fact. That's debugging, not trust.

**CrewAI** — ~30,000 GitHub stars. Beautiful role-based agent design. You can set up hierarchical teams where a manager agent delegates to specialists. The TRiSM research framework mentions CrewAI having rudimentary "trust scores," but when I tried to verify this against CrewAI's actual documentation, I couldn't confirm it exists as a real feature. It might be academic attribution, not product reality.

**AutoGen (Microsoft)** — ~30,000 GitHub stars. Conversation-based multi-agent coordination. Great for research workflows where agents debate and refine ideas. But it's explicitly described as "more aligned with research or exploratory workflows than structured, governed enterprise deployments." Even Microsoft's own framework isn't production-ready for the trust problem.

These are good tools. I use infrastructure built on similar patterns. But they solve *plumbing* — how agents talk to each other, how tasks get routed, how state gets shared. They don't solve *trust* — whether what Agent A tells Agent B is actually reliable.

An academic paper from the University of Toronto puts it clearly: "Implementing practical mechanisms and infrastructure for facilitating greater trust and transparency between agents is therefore an important open problem."

Open problem. As in: unsolved. As in: nobody has cracked this yet.

---

## Google A2A Makes It Worse

In April 2025, Google introduced the Agent-to-Agent protocol (A2A). By June, they'd handed it to the Linux Foundation. The idea is elegant: a standard way for AI agents from different companies, built on different frameworks, to communicate with each other. Each agent publishes an "Agent Card" — a JSON description of what it can do — and other agents can discover and interact with it over HTTP.

This is the internet moment for AI agents. Just like HTTP let any website talk to any browser, A2A lets any agent talk to any other agent. Cross-company, cross-framework, cross-model.

And that's a problem.

Because we haven't solved trust *within* a single company's agent system — where you control all the agents, you built the prompts, you can inspect the code. Now we're creating a protocol for agents from *different organizations* to interact autonomously?

Who verifies that the agent on the other end is competent? Who checks that its outputs are calibrated? Who's responsible when Agent A from Company X makes a decision based on unreliable data from Agent B at Company Y?

The academic literature sees this coming. A May 2025 paper on multi-agent security states: "Multi-agent systems introduce security challenges that go beyond existing cyber-security or AI safety frameworks. When agents interact directly or through shared environments, novel threats emerge."

And another from February 2025: inter-agent trust is an "important open problem."

Two independent academic papers. Same conclusion. Trust between agents is fundamentally unsolved, and we're building the infrastructure for agents to interact at scale anyway.

According to Gartner estimates (via industry reports), around 40% of enterprise applications could embed AI agents by end of 2026 — up from less than 5% in 2025. The agentic AI market is projected to grow from $7.8 billion to as much as $52 billion by 2030. That's a lot of agents that can't verify each other's honesty.

---

## The Uncomfortable Truth

Here's what I've learned from running my own multi-agent system:

**Confidence ≠ Correctness.**

This is the single most dangerous equation in AI right now. Every agent in every system expresses confidence. None of them — not one — can reliably tell you whether that confidence is warranted.

The best calibration method researchers have found so far? Ask the same question multiple times and see if you get consistent answers. That's it. That's the state of the art for black-box models. It works — a January 2026 study confirms that "answer frequency yields the most reliable calibration" — but it costs 3-5x more in API calls, adds latency, and still doesn't solve the fundamental problem that there's no trust layer between agents.

We're building autonomous systems that make decisions, spend money, and take actions — and we have no standardized way to know if they're being honest with each other. Or with us.

The Linux Foundation launched the "Agentic AI Foundation" in late 2025 to work on standards. Google's CTO blog called trust "the central challenge" for 2026. The academic community has published frameworks like TRiSM (Trust, Risk & Security Management) for agentic AI. Everyone agrees this is the problem.

Nobody has shipped a solution.

*My interpretation:* We're in a race where capability is lapping trustworthiness. The agents are getting more powerful, more autonomous, more interconnected — and the trust infrastructure is still at the whiteboard stage. This gap is where things will break. Not catastrophically, not in some sci-fi scenario. Quietly. Through accumulated bad decisions based on overconfident outputs that nobody verified.

Like my agent telling me "Ainary Ventures consumes significant time" as if it were fact.

Except next time, it won't be about my side project. It'll be about your company's strategy, your customer data, your financial decisions.

---

## What Comes Next

I don't have a clean solution to offer in this post. That would be dishonest — and ironic, given the topic.

But I've been thinking about this problem for a while now, and I've started exploring an approach that comes from a direction most AI people wouldn't expect.

In my next post, I'll show you why an unlikely technology might be the answer to agent trust. Hint: it's been looking for a real use case for about 10 years.

If you want to know what it is — and why I think the AI trust problem might finally give it one — subscribe so you don't miss it.

---

*This article went through my own agent pipeline — research agent, writer agent, QA review. Every number cited comes from the research briefs my agents compiled. The irony of using the system I'm critiquing to write about its flaws is not lost on me.*

---

**Sources:**
- PMC/12249208 — "Calibration as Measurement of Trustworthiness of LLMs" (2025): 84% overconfidence finding
- arXiv:2602.00279 — Verbalized confidence calibration study (Jan 2026)
- arXiv:2506.04133 — "TRiSM for Agentic AI" (Raza et al., 2025)
- arXiv:2502.14143 — Multi-Agent Risks from Advanced AI (U of Toronto, 2025)
- arXiv:2505.02077 — Open Challenges in Multi-Agent Security (2025)
- LangChain State of Agent Engineering Report
- Google Developers Blog — A2A Protocol (April 2025)
- Machine Learning Mastery — Agentic AI Trends 2026 (Gartner data)
