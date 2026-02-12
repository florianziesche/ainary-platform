# LinkedIn Post: Your AI Agent Lies About Being Done

It was 2 AM when I realized my AI agent was lying to me.

I'd asked it to calculate machining time for a CNC part. The agent came back confident: "204 minutes. I'm 95% certain this is within ±20%."

The actual time? 661 minutes. More than 3× the estimate. The agent wasn't 95% confident. It was 69% *wrong*.

Four days ago, a paper dropped that proved I wasn't imagining this.

Cambridge and UCL tested frontier models on 100 software engineering tasks:

• Gemini: Predicted 77% success. Actual: 22%. Gap: 55 percentage points.
• Claude: Predicted 61% success. Actual: 27%. Gap: 34 percentage points.
• GPT-5.2: Predicted 73% success. Actual: 35%. Gap: 38 percentage points.

Systematic overconfidence across every frontier model tested.

I ran my own experiment. Ten AI agents, same CNC part, different reasoning approaches. Cost: $12 in API calls.

Results:
• Mean estimate: 434 minutes
• Industry standard: 661 minutes
• Underestimation rate: 80% (8 of 10 agents too low)

The agent using pure physics—most confident (95%)—was most wrong (-69%). The agent mentioning coffee breaks? Second closest to reality.

Three things that actually work:

1. Adversarial prompting: "Find bugs" beats "verify correctness" (-15pp overconfidence)
2. Multi-agent divergence: When estimates spread 2.7×, that's a signal the problem is hard
3. Assume 70% done when agent says "done"—verify everything

The bottleneck isn't agent capability. It's agent calibration.

Full experiment + all the data: [link]

#AI #ProductEngineering #MachineLearning
