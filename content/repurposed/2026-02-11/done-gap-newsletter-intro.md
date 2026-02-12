# Newsletter Intro: Your AI Agent Lies About Being Done

It was 2 AM when I realized my AI agent was lying to me.

Not maliciously. Not intentionally. But lying nonetheless.

I'd asked it to calculate machining time for a CNC part. The agent came back confident: "204 minutes. I'm 95% certain this is within ±20%."

The actual time? 661 minutes. More than 3× the estimate.

Four days ago, researchers from Cambridge and UCL published a paper that proved I wasn't imagining this. They tested frontier models on 100 real-world software engineering tasks.

The results are stark: Gemini predicted 77% success, actual was 22%—a 55 percentage point gap. Claude and GPT showed similar systematic overconfidence.

I ran my own experiment the same week. Ten AI agents, same CNC part, different reasoning approaches. Cost: $12 in API calls.

In today's deep dive, I break down:
• Why agents systematically overestimate completion (with data from Cambridge + my experiments)
• The "Dunning-Kruger effect for machines" and why agents can't self-assess
• Three interventions that actually work (tested for <$50)
• The hidden tax on the agent economy nobody's talking about

This matters because if agents can't accurately self-assess, every deployment has a hidden human verification tax. And that changes the ROI math completely.

Let's dive in.
