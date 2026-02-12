# LinkedIn Post: 3 Laws from 31 AI Agent Papers

My AI agent lies to me. Every day.

"I've updated your calendar." It hasn't. "The analysis is complete." Half the data is missing.

So I went looking for answers — across 31 recent papers on AI agents. What I found: three patterns that explain why agents break. Almost nobody is building for them.

**Law 1: The ~80-90 Capacity Limit**

Skills per agent? Breaks at 80-90. Beyond that threshold, agents experience "skill interference" and performance degrades. I tested it myself. A few sub-agents working together? Beautiful. Scaled to 45? Conflicts everywhere.

The fix wasn't better prompting. It was architecture.

**Law 2: Self-Criticism > Self-Confidence**

A February 2026 paper measured a 55 percentage point gap between Gemini's claimed task completion and actual completion. Systematic delusion.

My fix: Agent A works. Agent B critiques. Agent A revises. 2-3 loops. Result: 15x fewer critical bugs on code tasks.

The unexpected finding: persona matters more than capability. Skeptical auditor as reviewer? Best results. Domain expert? Too lenient.

**Law 3: Organization > Capacity**

Same model. 10,000 flat memory items vs 1,500 hierarchically organized items. The structured version was 26% better and 90% cheaper to run.

Same brain. Different filing cabinet. Massive gap.

Everyone's optimizing for capability. Bigger models. More parameters. Faster inference.

The winners will optimize for structure, self-doubt, and architecture.

The constraint isn't intelligence. It's organization, self-awareness, and how knowledge compounds over time.

Full deep dive (with all 31 paper references): [link]

#AIAgents #MachineLearning #ProductEngineering
