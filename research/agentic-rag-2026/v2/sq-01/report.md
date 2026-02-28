### Answer to: What are the technical breakthroughs in 2024-2025 that enable production-ready confidence propagation for multi-step agentic RAG systems?

**Key Findings:**

- **HTC Framework for Trajectory Calibration [E]** [S21]: Holistic Trajectory Calibration (HTC) introduced in 2025 extracts "rich process-level features ranging from macro dynamics to micro stability across an agent's entire trajectory" and "consistently surpasses strong baselines in both calibration and discrimination, across eight benchmarks, multiple LLMs, and diverse agent frameworks" (https://arxiv.org/abs/2601.15778).

- **SAUP for Intra-Chain Uncertainty Propagation [E]** [S27]: SAUP formalizes uncertainty propagation within agent chains using "situational awareness by assigning situational weights to each step's uncertainty during the propagation" and employs Hidden Markov Models to estimate situational weights (https://arxiv.org/html/2412.01033).

- **MA-COPP for Multi-Agent Conformal Prediction [E]** (https://arxiv.org/abs/2403.16871): MA-COPP represents "the first conformal prediction method to solve OPP problems involving multi-agent systems" and derives "joint prediction regions for all agents' trajectories when one or more ego agents change their policies."

- **BaseCal for Calibration Recovery [E]** [S26]: BaseCal achieves "42.9% ECE reduction via hidden state projection to base model space" and "recovers calibration WITHOUT losing helpfulness," addressing RLHF-damaged calibration identified in [S7].

- **Production Implementation Gap [J]**: While SAUP shows "practical implementation" with "normalized entropy" adaptations for ReAct pipelines, no evidence found for full production deployments or 5+ step benchmarks specifically requested.

- **Compositional Guarantees Missing [I]**: MA-COPP addresses multi-agent prediction but doesn't demonstrate compositional conformal guarantees for dependent pipeline stages. Previous work [S9] established that conformal "guarantees do NOT compose for multi-agent" systems.

**Evidence Quality:**
- **Strongest source**: HTC framework [S21] with comprehensive benchmarking across 8 datasets and multiple LLMs, though preprint status limits confidence
- **Weakest point**: Production readiness claims lack concrete deployment evidence or detailed performance metrics under real-world conditions  
- **What's missing**: (1) Benchmarks demonstrating calibration preservation across 5+ agent steps, (2) Production implementation details beyond proof-of-concept, (3) Compositional conformal prediction for dependent RAG pipeline stages

**So What:** The 2024-2025 period shows significant theoretical advances in agentic confidence propagation (HTC, SAUP, MA-COPP) but lacks production-ready implementations with proven 5+ step calibration preservation required for EU AI Act compliance. Organizations should pilot these frameworks but expect additional engineering work for production deployment.

**Claims (for Claim Ledger):**
- HTC achieves superior calibration across 8 benchmarks | [S21] | E | B3 | Medium (preprint)
- SAUP formalizes situational uncertainty propagation | [S27] | E | A3 | High (peer-reviewed)
- MA-COPP enables multi-agent conformal prediction | MA-COPP source | E | B4 | Medium (novel method)
- No production 5+ step benchmarks found | Search results | J | A1 | High (absence of evidence)
- Compositional guarantees remain unproven | [S9] + current sources | I | B3 | Medium (inference from limitations)