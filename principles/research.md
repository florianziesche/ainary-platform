# Research Principles
*Domain: Research, analysis, multi-agent experiments*
*Extracted from: 31 papers + own experiments (2026-02-10)*

## P-RE-01: Adversarial Review = Mandatory
- **Score:** 90
- **Source:** Agentic Overconfidence Paper (arXiv:2602.06948) + CNC Experiment Agent H
- **Rule:** Every non-trivial output gets adversarial self-check. "Was ist falsch? Was fehlt?"
- **Evidence:** 15x correction (47→698 min). Paper shows -15pp overconfidence.
- **Validates:** 2x (paper + own experiment)
- **Violates:** 0x

## P-RE-02: Capacity Limit ~80-90
- **Score:** 75
- **Source:** Single vs Multi-Agent (arXiv:2601.04748), Cross-Paper Synthesis
- **Rule:** Don't exceed ~80-90 items per flat structure. Use hierarchy.
- **Evidence:** Phase transition in skills at 80-90. Mem0 optimal at ~88 memories. Miller's 7±2.
- **Validates:** 3x (3 independent sources)
- **Violates:** 0x

## P-RE-03: Diversity > Depth for Exploration
- **Score:** 85
- **Source:** 100-agent experiment, 10-agent CNC, 5-agent Vault, Google DeepMind
- **Rule:** For exploration: maximize diverse perspectives. For execution: use single best agent.
- **Evidence:** 3.4x variance from persona. Unique nuggets only from divergence.
- **Validates:** 4x (4 independent experiments)
- **Violates:** 0x

## P-RE-04: Pre-Execution Estimate > Post-Execution Review
- **Score:** 70
- **Source:** Agentic Overconfidence Paper (arXiv:2602.06948)
- **Rule:** Estimate difficulty/time BEFORE starting. Post-hoc review anchors on sunk cost.
- **Evidence:** Paper shows pre-exec discrimination better than post-exec across all models.
- **Validates:** 1x
- **Violates:** 0x

## P-RE-05: Organisation > Kapazität
- **Score:** 80
- **Source:** Mem0, Memory-R1, EvolveR, all Evolution papers
- **Rule:** Bottleneck is never reasoning — always knowledge representation. Improve files, not prompts.
- **Evidence:** 26% improvement from better memory org (Mem0). 28% from RL-based management (Memory-R1).
- **Validates:** 2x
- **Violates:** 0x

## P-RE-06: Controller Persona > Expert Persona
- **Score:** 70
- **Source:** CNC 10-agent calibration experiment
- **Rule:** For estimation tasks: use loss-averse/conservative personas, not "domain expert" personas.
- **Evidence:** Controller (684 min, +3.5%) beat REFA-Meister (433 min, -35%) against 661 min target.
- **Validates:** 1x
- **Violates:** 0x
