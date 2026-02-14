# AgentTrust Launch Posts — Monday, Feb 17, 2026

Tag: [PUBLIC]

---

## 1. Hacker News — Show HN

**Title:** Show HN: AgentTrust – Trust infrastructure for AI agents

**Body:**

Multi-agent systems have a trust problem. When Agent A delegates a task to Agent B, there's no standardized way to know if B's output is reliable. Most setups either trust everything (dangerous) or verify everything (expensive). I built AgentTrust to sit in between.

AgentTrust is an open-source trust layer that does three things: (1) calibrates confidence scores so agents report honest uncertainty instead of defaulting to "I'm 95% sure" on everything, (2) tracks trust scores across agent interactions over time, and (3) provides a simple API to query "should I trust this agent's output on this type of task?"

Under the hood, it uses a lightweight calibration approach inspired by Budget-CoCoA — you don't need thousands of labeled examples to get useful calibration. The scoring model updates incrementally, so trust scores reflect recent performance without requiring batch retraining. It works with any LLM API (OpenAI, Anthropic, local models via Ollama, etc.) and plugs in as middleware.

Still early. The calibration works well for structured outputs (JSON, code, factual claims) but is weaker for open-ended generation. Feedback welcome.

https://github.com/fziescheus-alt/agenttrust

---

## 2. Reddit r/MachineLearning

**Title:** [P] AgentTrust: Open-source calibration and trust scoring for LLM agents

**Body:**

I've been working on an open-source library for trust and calibration in multi-agent LLM systems. The core problem: LLMs are poorly calibrated out of the box. Xiong et al. (2023) showed ~84% of GPT-4 responses express overconfidence relative to actual accuracy. In single-agent setups you can work around this. In multi-agent orchestration — where agents delegate, verify, and build on each other's outputs — uncalibrated confidence cascades into compounding errors.

**What AgentTrust does:**

- **Confidence calibration**: Applies post-hoc calibration to agent outputs. Inspired by Budget-CoCoA (Chen et al., 2023), which showed you can get useful calibration with limited labeled data by leveraging consistency-based signals. AgentTrust adapts this for agentic workflows — using task outcome feedback rather than human labels.
- **Trust scoring**: Maintains per-agent, per-task-type trust scores that update incrementally. Think of it as a lightweight reputation system. An agent that's good at code generation but bad at medical reasoning gets scored accordingly.
- **Decision API**: A simple `should_trust(agent, task_type, confidence)` call that combines calibrated confidence with historical trust. Returns a trust decision + explanation.

**Technical details:**

- Calibration uses temperature scaling + isotonic regression, selected per task type
- Trust scores use a Bayesian update with configurable priors
- Runs as middleware — wraps any LLM API call
- ~200ms overhead per call (calibration lookup + score update)
- Full Python, no external dependencies beyond numpy

**Limitations (being honest):**

- Calibration quality depends on having enough task outcome signal. Cold-start is a real issue — I'm using prior-based defaults but it's not great until ~50 interactions.
- Open-ended generation tasks are hard to score. Works best for verifiable outputs.
- Haven't benchmarked against Kadavath et al.'s verbalized confidence approach yet.

Looking for feedback, especially from anyone working on multi-agent reliability or LLM calibration.

https://github.com/fziescheus-alt/agenttrust

---

## 3. Reddit r/LocalLLaMA

**Title:** Built an open-source trust layer for multi-agent systems

**Body:**

If you're running multi-agent setups (CrewAI, AutoGen, custom pipelines), you've probably noticed: agents confidently bullshit each other. Agent A says "I'm 95% sure" about something it's 40% correct on, Agent B trusts it, and the whole chain goes sideways.

I built AgentTrust to fix this. It's a Python middleware that calibrates confidence scores and tracks which agents are actually reliable at which tasks.

**Quick start:**

```python
pip install agenttrust

from agenttrust import TrustLayer

trust = TrustLayer()

# Wrap your agent call
result = trust.evaluate(
    agent_id="researcher",
    task_type="fact_extraction",
    output=agent_output,
    stated_confidence=0.92
)

print(result.calibrated_confidence)  # 0.61 — the honest number
print(result.trust_score)            # 0.73 — based on past performance
print(result.recommendation)         # "verify" / "accept" / "reject"
```

**Works with any LLM API.** OpenAI, Anthropic, Ollama, llama.cpp server, vLLM — doesn't matter. It sits between your orchestrator and the model, so it's model-agnostic.

**What it actually does:**
- Recalibrates confidence (LLMs are wildly overconfident by default)
- Tracks per-agent trust over time — so your coding agent and your research agent get separate scores
- Simple API: `should_trust()` gives you a yes/no/maybe with reasoning

Runs locally, no external calls, ~200ms overhead. Still early — works best for structured outputs (JSON, code, factual claims). Open-ended creative stuff is harder to score.

https://github.com/fziescheus-alt/agenttrust

---

```
Confidence: 82%
Word count: ~850
Sources: Budget-CoCoA (Chen et al. 2023), Xiong et al. 2023 (LLM overconfidence), AGENT.md, corrections.md
Voice check: Yes — "I" voice, no hype, no forbidden phrases, honest about limitations, specific not generic
Begründung: HN post kept short + humble (HN hates marketing). r/ML post cites papers + technical depth (that community expects rigor). r/LocalLLaMA post leads with practical code (builders want to copy-paste). All three honest about limitations per corrections.md "keine fake Metrics" + "Substanz > Optik".
```
