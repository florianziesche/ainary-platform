# Platform Findings — Curated for RAG (CORE Tier)
> Source: Ainary Execution Platform (localhost:8080), curated 2026-02-19
> Selection: 8 of 106 findings, all unique (not in Vault files), report-relevant

## C-008 (conf: 0.98) — AgentTrust ≠ Observability
AgentTrust is NOT observability. LangSmith, Arize, Galileo trace and monitor — NONE calibrate. AgentTrust is Calibration. The entire observability market ($2B+) solves a different problem than trust calibration.

## RF-074 (conf: 0.98) — HITL for Irreversible Actions (Contradiction Resolved)
Contradiction resolved: Fully Autonomous Agents vs. Human-in-the-Loop. Production evidence shows: HITL required for irreversible actions. Autonomy only safe for reversible, bounded tasks. Source: Production failure patterns across multiple deployments.

## C013 (conf: 0.85) — Air Canada Chatbot Liability
Air Canada held legally liable for chatbot hallucination. Court ruled the company responsible for AI-generated misinformation about bereavement fares. Precedent: organizations cannot disclaim liability for AI outputs. Directly supports calibration-as-legal-necessity argument.

## C014 (conf: 0.85) — Grok RAG Poisoning
Grok RAG poisoning contaminated thousands of responses before detection. Demonstrates that trust in retrieval-augmented systems is not guaranteed — poisoned sources propagate through the entire output chain. Calibration of source reliability is essential.

## C015 (conf: 0.85) — Waymo 7 Collisions Before Recall
Waymo required 7 collisions before issuing recall. Calibration system failed to flag degrading performance early enough. Better confidence calibration could have triggered intervention after 2 incidents, not 7. Physical-world calibration failure case.

## C005 (conf: 0.85) — MemoryGraft Injection Attack
MemoryGraft attack achieves >95% memory injection success rate. Persistent memory systems in AI agents are vulnerable to adversarial manipulation. Trust calibration must account for memory integrity, not just output confidence.

## RF-049 (conf: 0.90) — AI Funding $202B in 2025
AI startup funding reached $202B globally in 2025 (+75% YoY), capturing ~50% of all VC funding. Market context: massive capital deployment with near-zero calibration infrastructure. The gap between investment and trust is widening.

## RF-026 (conf: 0.95) — Weighted Average ≠ Bayesian Update
Gewichteter Durchschnitt (a*0.7 + b*0.3) ist KEIN Bayesian Update. Echte Formel: P(H|E) = P(E|H)*P(H) / [P(E|H)*P(H) + P(E|!H)*P(!H)]. Common implementation error in confidence aggregation systems. Pipeline must use proper Bayesian math, not shortcuts.
