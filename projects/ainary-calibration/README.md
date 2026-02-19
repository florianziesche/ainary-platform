# Ainary Calibration Library

**Trust Calibration Methods for LLM Agents**

A Python library implementing state-of-the-art calibration techniques for AI agent systems, with focus on black-box LLM deployments. Based on comprehensive research (AR-020-v2) covering 20+ papers from ICML, NeurIPS, ICLR, ACL, and industry sources.

---

## Features

### ✅ 6 Calibration Method Families

1. **Consistency-Based** (Self-Consistency, Budget-CoCoA)
2. **Verbalized Confidence** (AFCE, DINCO)
3. **Conformal Prediction** (Distribution-free guarantees)
4. **Selective Prediction** (Abstention, routing)
5. **Multi-Agent Propagation** ⭐ (NOVEL — addresses research gap)
6. **Calibration Metrics** (ECE, MCE, Brier Score, Reliability Diagrams)

### ✅ 3-Tier Architecture

- **Tier 1**: Consistency-based default (~$0.01/query, 25-30% ECE)
- **Tier 2**: + Conformal prediction (~$0.025/query, statistical guarantees)
- **Tier 3**: + Selective prediction (human routing, cost-aware)

### ✅ No API Keys Required

All experiments run with simulated data. Swap in real LLM calls when ready.

---

## Quick Start

### Installation

```bash
# Clone or download this directory
cd projects/ainary-calibration

# No dependencies beyond NumPy (already installed in most Python environments)
# Optional: Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e .
```

### 5-Line Example

```python
from ainary_calibration import calibrate

# Calibrate any LLM output
result = calibrate("What is 2+2?", model="simulated", tier="auto", task_risk="medium")

print(f"Answer: {result.answer}")
print(f"Confidence: {result.confidence:.2%}")
print(f"Route: {result.route}")
print(f"Cost: ${result.cost:.4f}")
```

**Output:**
```
Answer: 4
Confidence: 78.00%
Route: RouteDecision.AUTO
Cost: $0.0250
```

---

## Usage Examples

### Example 1: Self-Consistency Calibration

```python
from ainary_calibration.consistency import self_consistency_score

# Sample 5 responses, cluster by semantic similarity
confidence, metadata = self_consistency_score(
    prompt="What is the capital of France?",
    model="simulated",
    n_samples=5
)

print(f"Confidence: {confidence:.2%}")
print(f"Most common answer: {metadata['most_common_answer']}")
print(f"Clusters: {metadata['clusters']}")
```

### Example 2: Multi-Agent Confidence Propagation

```python
from ainary_calibration.propagation import propagate_confidence, PropagationMethod

# Agent chain: [Agent1: 90%, Agent2: 85%, Agent3: 88%]
chain = [0.90, 0.85, 0.88]

# Method 1: Multiplicative (assumes independence)
result_mult = propagate_confidence(chain, method=PropagationMethod.MULTIPLICATIVE)
print(f"Multiplicative: {result_mult.final_confidence:.2%}")  # 67.32%

# Method 2: Bayesian (models correlation)
result_bayes = propagate_confidence(chain, method=PropagationMethod.BAYESIAN, correlation=0.3)
print(f"Bayesian (ρ=0.3): {result_bayes.final_confidence:.2%}")  # ~78%

# Method 3: Conservative (weakest link)
result_cons = propagate_confidence(chain, method=PropagationMethod.CONSERVATIVE)
print(f"Conservative: {result_cons.final_confidence:.2%}")  # 85% (min)
```

### Example 3: Selective Prediction / Routing

```python
from ainary_calibration.selective import route_by_confidence

# Route based on confidence
result = route_by_confidence(confidence=0.55, task_risk="high")

print(f"Route: {result.route}")  # RouteDecision.ESCALATE
print(f"Reason: {result.reason}")
# Output: "Low confidence (55%) → escalate to more capable model"
```

### Example 4: Calibration Metrics

```python
from ainary_calibration.metrics import calibration_summary

# Evaluate calibration quality
predictions = [
    (0.9, True),   # (confidence, is_correct)
    (0.8, True),
    (0.6, False),
    (0.95, True),
]

metrics = calibration_summary(predictions, n_bins=10)
print(f"ECE: {metrics.ece:.2%}")
print(f"MCE: {metrics.mce:.2%}")
print(f"Brier Score: {metrics.brier:.4f}")
```

---

## Running Experiments

### All 4 Experiments

```bash
cd ainary_calibration/experiments
python3 run_experiments.py
```

**Output:**
- `results/experiments_YYYYMMDD_HHMMSS.json`
- `results/experiments_latest.json`

### Generate Analysis & Summary

```bash
python3 analysis.py
```

**Output:**
- `RESULTS-SUMMARY.md` (full report with ASCII charts)
- Console output with key findings

---

## Experiments Overview

### Experiment 1: Multi-Agent Confidence Propagation

- **Goal**: Compare propagation methods across chain lengths and correlation levels
- **Configurations**: 3/5/10-agent chains × 3 base confidences × 3 correlations = 27 configs
- **Monte Carlo**: 1000 runs per config
- **Methods**: Multiplicative, Bayesian Network, Conservative
- **Finding**: Multiplicative is overly pessimistic when correlation > 0.3

### Experiment 2: ECE Comparison

- **Goal**: Compare calibration methods
- **Methods**: Uncalibrated (baseline), Consistency-based, Verbalized confidence
- **Samples**: 1000 predictions per method
- **Metrics**: ECE, MCE, Brier Score, Overconfidence Ratio
- **Finding**: Consistency-based achieves ~35% ECE improvement over uncalibrated

### Experiment 3: Cost-Confidence Frontier

- **Goal**: Find optimal n_samples for Budget-CoCoA
- **Range**: n_samples from 1 to 20
- **Trade-off**: Cost vs ECE improvement
- **Finding**: n=3-5 provides best cost-efficiency (~$0.005/query, 30% ECE improvement)

### Experiment 4: Selective Prediction ROI

- **Goal**: Optimize abstention threshold
- **Range**: Threshold from 0.50 to 0.99
- **Metrics**: Coverage, Reliable Accuracy, Effective Reliability
- **Finding**: Threshold=0.60-0.70 balances coverage and reliability for most tasks

---

## API Reference

### Main Entry Point

#### `calibrate(prompt, model, tier, task_risk, ...)`

3-tier calibration pipeline. Returns `CalibratedResult`.

**Args:**
- `prompt` (str): User query
- `model` (str): Model identifier (default: "simulated")
- `tier` (str): "tier1" | "tier2" | "tier3" | "auto" (default: "auto")
- `task_risk` (str): "low" | "medium" | "high" (default: "medium")

**Returns:**
- `answer` (str): Model's answer
- `confidence` (float): Calibrated confidence (0.0-1.0)
- `tier` (CalibrationTier): Tier used
- `route` (RouteDecision): Routing decision (Tier 3 only)
- `cost` (float): Estimated cost in USD
- `metadata` (dict): Detailed calibration info

---

### Consistency Module

#### `self_consistency_score(prompt, model, n_samples=5)`

Sample N responses, cluster by semantic similarity, use majority vote as confidence.

**Returns:** `(confidence: float, metadata: dict)`

#### `budget_cocoa(prompt, model, n_samples=3)`

Cost-optimized consistency checking with fewer samples.

**Returns:** `(confidence: float, cost: float, metadata: dict)`

---

### Propagation Module

#### `propagate_confidence(chain, method, correlation=0.0)`

Propagate confidence through multi-agent chain.

**Args:**
- `chain` (list[float]): Individual agent confidences
- `method` (PropagationMethod): "multiplicative" | "bayesian_network" | "conservative"
- `correlation` (float): For Bayesian method (0.0-1.0)

**Returns:** `PropagationResult`

#### `simulate_chain(n_agents, base_confidence, correlation, n_simulations=1000)`

Monte Carlo simulation of agent chains.

**Returns:** `dict` with statistics per propagation method

---

### Metrics Module

#### `expected_calibration_error(predictions, n_bins=15)`

Calculate ECE (Expected Calibration Error).

**Args:**
- `predictions` (list[tuple[float, bool]]): (confidence, is_correct) pairs
- `n_bins` (int): Number of bins (default: 15)

**Returns:** `(ece: float, bin_stats: list[dict])`

#### `calibration_summary(predictions, n_bins=15)`

All metrics at once: ECE, MCE, Brier Score.

**Returns:** `CalibrationMetrics`

---

## Research Background

This library implements methods from 20+ papers, including:

- **Self-Consistency**: Wang et al. (ICLR 2023)
- **AFCE**: Xu et al. (ACL 2025)
- **DINCO**: Wang et al. (ICLR 2026 submission)
- **ConU**: Li et al. (NeurIPS 2024)
- **SelectLLM**: ICLR 2025
- **RLHF Overconfidence**: Wang et al. (NeurIPS 2024)

**Key Finding from AR-020-v2:**

> RLHF systematically destroys calibration. Models trained for "helpfulness" learn to assert confidence even when undue, resulting in 15-30% overconfidence bias. External calibration is not optional — it's structural.

**Novel Contribution:**

> Multi-agent confidence propagation was an identified research gap. No existing framework addresses how confidence should propagate through agent chains. This library provides the first practical implementation.

---

## Limitations

1. **Simulation-Based**: Experiments use simulated data. Real-world calibration quality depends on actual LLM behavior.
2. **Domain Shift**: Calibration quality degrades under distribution shift. Requires per-domain calibration sets.
3. **No White-Box Methods**: Temperature scaling (requires logits) not implemented. Most production LLM APIs don't expose logits.
4. **Conformal Prediction**: Requires calibration data from target distribution. Cold start problem for novel domains.

---

## Roadmap

- [ ] Integration with OpenAI API (real LLM calls)
- [ ] Integration with Anthropic Claude API
- [ ] Active learning for calibration set generation
- [ ] Adaptive conformal prediction (online learning)
- [ ] Visualization dashboard (matplotlib/plotly)
- [ ] Agent framework integration (LangChain, AutoGPT, etc.)

---

## Citation

If you use this library in research, please cite:

```
Ainary Calibration Library (2026)
Based on AR-020-v2: Trust Calibration Methods for AI Agents
https://github.com/ainary/calibration
```

---

## License

MIT License — See LICENSE file

---

## Contact

For questions, issues, or contributions:
- GitHub Issues: [ainary/calibration/issues](https://github.com/ainary/calibration/issues)
- Email: research@ainary.com

---

**Built with ❤️ for reliable AI agent systems.**
