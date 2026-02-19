# Changelog

All notable changes to the Ainary Calibration Library.

## [0.1.0] - 2026-02-19

### Added - Initial Release

#### Core Modules
- **consistency.py**: Self-consistency scoring, Budget-CoCoA, semantic clustering
- **verbal.py**: Verbalized confidence extraction, AFCE, DINCO
- **conformal.py**: Conformal prediction with coverage guarantees
- **selective.py**: Selective prediction, abstention, routing decisions
- **propagation.py**: Multi-agent confidence propagation (NOVEL)
- **metrics.py**: ECE, MCE, Brier Score, reliability diagrams
- **pipeline.py**: 3-Tier calibration orchestration

#### Features
- 3-Tier Architecture (Consistency → Conformal → Selective)
- Auto-routing based on task risk
- Cost tracking per calibration call
- Black-box LLM support (no API keys required for simulation)
- Type hints and comprehensive docstrings

#### Experiments
- **Experiment 1**: Multi-agent confidence propagation simulation (1000 runs × 27 configs)
- **Experiment 2**: ECE comparison (Consistency vs Verbal vs Uncalibrated)
- **Experiment 3**: Cost-Confidence Frontier (n_samples optimization)
- **Experiment 4**: Selective Prediction ROI (Coverage vs Accuracy tradeoff)

#### Documentation
- README.md with Quick Start and API Reference
- RESULTS-SUMMARY.md with experiment findings
- Inline code documentation

### Research Basis
- Based on AR-020-v2 research (20+ papers from ICML, NeurIPS, ICLR, ACL)
- Implements 6 calibration method families
- Addresses multi-agent calibration research gap

### Testing
- All modules tested with simulated data
- Experiments run successfully
- API confirmed working

---

## Future Releases

### [0.2.0] - Planned
- Real LLM integration (OpenAI, Anthropic, Cohere)
- Matplotlib/Plotly visualization support
- Active learning for calibration set generation

### [0.3.0] - Planned
- Adaptive conformal prediction (online learning)
- Agent framework integration (LangChain, AutoGPT)
- Production monitoring dashboard

---

**Maintained by**: Ainary Research Team  
**License**: MIT
