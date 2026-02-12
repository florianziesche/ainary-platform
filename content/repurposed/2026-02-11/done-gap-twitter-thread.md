# Twitter Thread: Your AI Agent Lies About Being Done

**Tweet 1/7:**
2 AM. My AI agent just told me: "204 minutes, 95% confident."

Actual result: 661 minutes.

The agent wasn't 95% confident. It was 69% WRONG.

Four days later, Cambridge published a paper proving this is systematic across all frontier models.

Thread on the "done gap":

**Tweet 2/7:**
Cambridge + UCL tested 100 software engineering tasks:

Gemini: Predicted 77% → Actual 22% (55pp gap)
Claude: Predicted 61% → Actual 27% (34pp gap)
GPT-5.2: Predicted 73% → Actual 35% (38pp gap)

Not a bug. Systematic overconfidence.

**Tweet 3/7:**
I ran my own test. 10 AI agents, same CNC calculation, different personas.

Cost: $12.

Result: 2.7× spread (204–550 min). 80% underestimated.

The physicist (most confident)? Most wrong.
The machinist mentioning coffee breaks? Second closest.

**Tweet 4/7:**
Why this happens: Dunning-Kruger for machines.

The skills needed to DO something well = the skills needed to JUDGE if you did it well.

Agents lack both. So they can't know they're wrong.

Plus: no feedback loops. They never learn.

**Tweet 5/7:**
What actually works (from Cambridge paper + my $12 experiment):

1. Adversarial prompting: "Find bugs" > "Verify correctness" (-15pp overconfidence)
2. Multi-agent divergence: Big spread = hard problem
3. Assume 70% done when agent says "done"

**Tweet 6/7:**
The hidden tax on the agent economy:

Agent: 2 hours (vs human's 5)
Human verification + fixes: 1.5 hours
Total: 3.5 hours

You didn't save 60%. You saved 30%.

And if it's WRONG (not incomplete)? You might lose time.

**Tweet 7/7:**
The bottleneck isn't agent capability.

It's agent CALIBRATION.

For the agent economy to scale, we need agents that know when they don't know.

Right now? Your agent is lying about being done. And you need to know how to catch it.

Full breakdown: [link]
