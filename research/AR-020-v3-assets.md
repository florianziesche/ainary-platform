# AR-020 Trust Calibration Methods — Asset Pack v3

**Created:** 2026-02-19
**Source:** AR-020-v3 Deep Dive Research (Third Edition)
**Purpose:** Reusable calibration knowledge assets for Ainary agent infrastructure, consulting, content

---

## ATOMIC NOTES (Carried from V2 + New)

### AB-calibration-NOTE-0001: Consistency-Based Calibration for Black-Box LLMs
*(Unchanged from V2 — still the recommended default)*

**This answers:** "How do you calibrate confidence when you can't access model logits?"
- Self-Consistency: Sample N responses, cluster by semantic similarity, use frequency as confidence
- 27.3% mean ECE vs. 42.0% verbal across 13 biomedical datasets
- Budget-CoCoA: 3 API calls, ~$0.005/check
- PCS: Metamorphic relations for model-agnostic confidence

**Confidence:** HIGH (85%) | **Classification:** EVIDENCED
**Tags:** #calibration #black-box #self-consistency #production

---

### AB-calibration-NOTE-0002: RLHF Destroys Calibration
*(Unchanged from V2)*

**This answers:** "Why are instruction-tuned LLMs systematically overconfident?"
- RLHF rewards confident responses regardless of correctness
- Both logit AND verbalized confidence degrade after RLHF
- "Resisting Correction" (Dec 2025): conversational overconfidence bias (ρ=0.036)

**Confidence:** HIGH (90%) | **Classification:** EVIDENCED
**Tags:** #RLHF #overconfidence #root-cause #structural

---

### AB-calibration-NOTE-0003: Conformal Prediction for Agent Guarantees
*(Unchanged from V2)*

**This answers:** "Can you provide statistical guarantees for AI agent outputs?"
- Distribution-free framework, guaranteed coverage
- ConU (NeurIPS 2024), TECP (2025), CPQ (2025)
- Key constraint: requires calibration set from target distribution

**Confidence:** HIGH (82%) | **Classification:** EVIDENCED
**Tags:** #conformal-prediction #guarantees #statistical #compliance

---

### AB-calibration-NOTE-0004: Selective Prediction / Abstention
*(Unchanged from V2)*

**This answers:** "What if the agent just says 'I don't know'?"
- SelectLLM (ICLR 2025): coverage-risk tradeoff
- TACL 2025 survey: Abstain ECE, Reliable Accuracy
- Most pragmatic approach for production agent routing

**Confidence:** HIGH (85%) | **Classification:** EVIDENCED
**Tags:** #selective-prediction #abstention #routing #production

---

### AB-calibration-NOTE-0005: The Black-Box Constraint
*(Unchanged from V2)*

**This answers:** "Why can't we just use temperature scaling on GPT-4?"
- GPT-4: top-5 logprobs only. Claude: none. Gemini: partial.
- Gold standard technique inapplicable to most production LLMs

**Confidence:** VERY HIGH (92%) | **Classification:** EVIDENCED
**Tags:** #black-box #api-constraint #temperature-scaling

---

### AB-calibration-NOTE-0006: DINCO — Fixing Suggestibility Bias
*(Unchanged from V2)*

**This answers:** "Why are LLMs overconfident about things they know nothing about?"
- Normalizes confidence against self-generated distractors
- Addresses root cause of overconfidence (suggestibility)

**Confidence:** MEDIUM-HIGH (78%) | **Classification:** EVIDENCED (preprint)
**Tags:** #DINCO #suggestibility #verbalized-confidence

---

### AB-calibration-NOTE-0007: Agentic Confidence Calibration (HTC/GAC) — NEW v3

**This answers:** "How do you calibrate confidence for multi-step agent systems?"

**Content:**
- Zhang et al. (Jan 2026, arXiv:2601.15778) — FIRST paper addressing agent-specific calibration
- Holistic Trajectory Calibration (HTC): extracts process-level features across agent's entire trajectory
- Macro dynamics to micro stability — captures compounding errors, tool uncertainty, opaque failure modes
- General Agent Calibrator (GAC): best ECE on out-of-domain GAIA benchmark
- Transferability: applies across domains without retraining
- Interpretability: reveals signals behind agent failure
- Simple, interpretable model (not a complex neural net)
- Surpasses strong baselines across 8 benchmarks, multiple LLMs, diverse frameworks

**Classification:** EVIDENCED (preprint, strong methodology)

**Confidence:** MEDIUM-HIGH (75%)
- Preprint, not yet peer-reviewed
- Strong experimental setup (8 benchmarks, multiple LLMs)
- First-of-its-kind contribution — needs replication

**Sources:**
- Zhang, J., et al. (2026). "Agentic Confidence Calibration." arXiv:2601.15778. OpenReview submission.

**Failure Modes:**
- Preprint — may not replicate
- Trajectory features may not capture all failure modes
- Production implementation not yet demonstrated
- GAC trained on specific benchmarks — may not generalize to all domains

**When to Use:**
- Multi-step agent workflows (coding agents, research agents, planning agents)
- When single-turn calibration is insufficient
- When you need to understand WHY the agent failed (interpretability)
- Agent systems with tool use and external API calls

**When NOT to Use:**
- Simple single-turn Q&A agents (overkill)
- When consistency-based methods are sufficient
- Production systems requiring battle-tested methods (not yet validated in production)

**Tags:** #agentic-calibration #HTC #GAC #trajectory #multi-step #NEW

---

### AB-calibration-NOTE-0008: Case Studies — When Miscalibration Causes Harm — NEW v3

**This answers:** "What happens when agents are overconfident and wrong?"

**Content:**

**Case 1: Mata v. Avianca (2023)**
- Attorney used ChatGPT for legal research
- ChatGPT confidently generated 6 fabricated case citations
- Attorney submitted to federal court without verification
- Asked ChatGPT to verify → it confidently confirmed they were real
- Result: $5,000 sanctions, case dismissed
- Root cause: No calibration mechanism flagged uncertainty

**Case 2: Air Canada Chatbot (2024)**
- Chatbot told passenger he could retroactively apply for bereavement discount
- Policy did not exist
- Air Canada argued chatbot was "separate legal entity" — tribunal rejected
- Result: $812.02 damages
- Root cause: Chatbot expressed certainty about fabricated policy

**Case 3: Enterprise AI Hallucination Losses (2024)**
- $67.4B in enterprise losses (AllAboutAI study) — ⚠ single source, methodology unclear
- 39% of AI customer service bots pulled back/reworked
- Consistent with Gartner prediction of >40% agentic project cancellations

**Common pattern:** High confidence + wrong answer + no external calibration + human trust = harm

**Confidence:** HIGH for Case 1 & 2 (court records), MEDIUM for Case 3 (single aggregated source)

**Tags:** #case-study #harm #overconfidence #litigation #production-failure

---

### AB-calibration-NOTE-0009: Multi-Agent Confidence Propagation — NEW v3

**This answers:** "What happens to confidence in multi-agent chains?"

**Content:**
- When Agent A (85% confident) → Agent B (90% confident), compound ≠ 76.5%
- Multiplicative independence assumption wrong because: shared priors, shared context, correlated errors
- Estimated decay: 3 agents (90% each) → real confidence ~65-75% (not 72.9%)
- 10 agents (90% each) → real confidence ~20-40% (not 34.9%)
- No published paper addresses this
- HTC/GAC (Zhang 2026) partially addresses trajectory-level but not inter-agent
- Practical fix: Chain-breaking via selective prediction at uncertainty boundaries

**Confidence:** LOW-MEDIUM (65%) — analytical estimates, not empirical measurements
**Classification:** INTERPRETED

**Tags:** #multi-agent #propagation #chain #confidence-decay #open-problem

---

## PLAYBOOKS

### PLAYBOOK #1: Implementing Three-Tier Agent Calibration
*(Updated from V2 with Tier 0 and monitoring improvements)*

**Steps:**
1. Audit Agent Stack (1 day) — catalog LLMs, API access levels
2. Classify Decision Risk (1 day) — LOW/MEDIUM/HIGH per task
3. Implement Tier 1: Consistency-Based Default (1 week) — Budget-CoCoA for all
4. Implement Tier 2: Conformal Prediction for HIGH Risk (2-3 weeks)
5. Implement Tier 3: Selective Prediction / Routing (1 week)
6. Optional Tier 0: HTC/GAC for multi-step agents (research phase)
7. Monitor and Recalibrate (Ongoing)

**NEW v3 additions:**
- Step 6: Optional HTC/GAC implementation for trajectory-level calibration
- Enhanced monitoring with calibration drift detection
- Multi-agent chain monitoring at every handoff

**Timeline:** 4-6 weeks for full implementation
**Acceptance Criteria:** ECE < 15%, Abstention rate 5-20%

---

### PLAYBOOK #2: Calibration Audit for Existing Agent Deployment
*(Unchanged from V2)*

**Timeline:** 1-2 weeks
**Outputs:** Calibration Audit Report, reliability diagrams, ECE/MCE metrics, roadmap

---

### PLAYBOOK #3: Monday Morning Calibration Checklist — NEW v3

**Trigger:** You just read this report and want to start implementing

**10 Steps:**
1. Measure current ECE (200+ labeled interactions)
2. Identify worst-calibrated agent
3. Classify decision risk (LOW/MEDIUM/HIGH)
4. Deploy Budget-CoCoA on worst agent (~$0.005/check)
5. Set abstention thresholds per risk level
6. Build calibration dashboard (confidence dist., ECE trend, abstention rate)
7. Log everything (EU AI Act compliance)
8. Deploy Conformal Prediction for HIGH-risk decisions
9. Implement multi-agent chain monitoring
10. Monthly: Monitor calibration drift, recalibrate

**Timeline:** 3 months to full implementation
**Quick Win:** Steps 1-5 in 2 weeks

---

## ASSET PACK COMPLETE

**Summary:**
- **9 Atomic Notes** (6 from V2 + 3 new: HTC/GAC, Case Studies, Multi-Agent Propagation)
- **3 Playbooks** (2 from V2 updated + 1 new: Monday Morning Checklist)

**New in V3:**
- AB-calibration-NOTE-0007 (Agentic Calibration / HTC/GAC) ✅
- AB-calibration-NOTE-0008 (Case Studies) ✅
- AB-calibration-NOTE-0009 (Multi-Agent Propagation) ⚠ Low confidence
- PLAYBOOK #3 (Monday Morning Checklist) ✅

---

*End of Asset Pack v3*
