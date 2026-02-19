# AR-020 v5 — Asset Pack
**Generated:** 2026-02-19 | **Source Report:** AR-020-v5-full.md
**Topic Slug:** trust-cal

---

## Asset Index

| Type | Count |
|------|-------|
| Atomic Notes (NOTE) | 10 |
| Playbooks (PLAY) | 2 |
| Templates (TMPL) | 2 |
| **Total** | **14** |

---

## Coverage Map

| Key Takeaway | Asset IDs |
|-------------|-----------|
| Correlated agent failures are primary multi-agent risk | NOTE-0001, NOTE-0008 |
| RLHF damages calibration (regime-dependent) | NOTE-0002 |
| Consistency-based calibration is best black-box method | NOTE-0003, PLAY-0001 |
| Temperature scaling doesn't work on GPT-4/Claude | NOTE-0004 |
| Full-stack cost $0.07-$2.24/query | NOTE-0005 |
| EU AI Act Article 14 functionally requires confidence signals | NOTE-0006 |
| Do NOT deploy calibration in 5 scenarios | NOTE-0007 |
| Implementation takes 6-12 weeks | PLAY-0001, TMPL-0001 |
| ECE alone is insufficient | NOTE-0009 |
| LLM-assisted review has correlated blind spots | NOTE-0010 |
| Scenario-specific architecture selection | PLAY-0002, TMPL-0002 |

---

## Atomic Notes

### AB-trust-cal-NOTE-0001
**Title:** Correlated Agent Failures in Multi-Agent Chains
**This answers:** Why do multi-agent AI systems fail in clusters?
**Content:**
- Same-model agents share training data, architecture, and conversation context, producing correlated errors [S21]
- If Agent A hallucinates, Agent B (processing A's output) is more likely to propagate the hallucination
- Multiplicative confidence model (C = product of individual confidences) is mathematically inconsistent under positive correlation [FM-1]
- P(both correct) = p1*p2 + rho*sqrt(p1(1-p1)*p2(1-p2)); when rho > 0, joint accuracy > product but joint failure risk also increases
- No published study has measured rho in production multi-agent chains (Feb 2026)
- Mitigation: diverse models (different providers), correlation-adjusted thresholds, confidence logging at every handoff

**Classification:** Derived
**Confidence:** Med
**Sources:** [S21], [S27], FM-1, CT-031
**Tags:** multi-agent, correlation, failure-modes, propagation

---

### AB-trust-cal-NOTE-0002
**Title:** RLHF Damages Calibration (Regime-Dependent)
**This answers:** Why are LLMs overconfident, and is it fixable?
**Content:**
- RLHF reward models assign higher scores to confident-sounding responses regardless of correctness [S7]
- Damage is regime-dependent: models exist in "calibratable" vs "non-calibratable" regimes [S30, CT-001]
- In calibratable regime: post-hoc methods (temperature scaling, consistency) can recover calibration
- In non-calibratable regime: aggressive RLHF has structurally destroyed calibratability
- Practical implication: assume miscalibrated until measured; measure ECE on your target domain

**Classification:** Evidenced
**Confidence:** High
**Sources:** [S7], [S18], [S30], CT-001
**Tags:** rlhf, overconfidence, calibration, regime

---

### AB-trust-cal-NOTE-0003
**Title:** Consistency-Based Calibration (Best Black-Box Method)
**This answers:** What is the best calibration method for black-box LLM APIs?
**Content:**
- Sample 3-5 responses to the same query, measure agreement via semantic clustering (embedding cosine similarity >0.85)
- ECE: 27.3% vs 42.0% for verbalized confidence in biomedical QA (13 datasets) [S8]
- Cross-domain generalization is NOT verified -- absolute ECE will differ by domain [CX-002]
- Budget-CoCoA: 3 API calls at $0.0005-$0.015/check depending on model [S19, CX-005]
- Cannot detect systematic bias (model consistently wrong = high confidence for wrong answer) [CT-003]
- Not viable for <2s latency; use APRICOT as alternative [S23]

**Classification:** Evidenced
**Confidence:** Med (domain-specific evidence only)
**Sources:** [S2], [S8], [S19], [S23], CT-003, CX-002
**Tags:** consistency, black-box, ece, budget-cocoa, apricot

---

### AB-trust-cal-NOTE-0004
**Title:** Black-Box Constraint (Temperature Scaling Inapplicable)
**This answers:** Why can't we use the best calibration method on production LLMs?
**Content:**
- Temperature scaling (Guo et al. 2017) achieves ~0.25% ECE on vision models -- gold standard [S1]
- Requires logit access: GPT-4 provides top-5 logprobs only; Claude provides none; Gemini partial [verified Feb 2026]
- Self-hosted models (Llama, Mistral) retain full access -- temperature scaling viable there
- API access terms change; verify current provider docs before architectural decisions

**Classification:** Evidenced
**Confidence:** High
**Sources:** [S1], API documentation
**Tags:** temperature-scaling, logits, black-box, api

---

### AB-trust-cal-NOTE-0005
**Title:** Calibration Cost Waterfall ($0.001 to $2.24/query)
**This answers:** How much does calibration cost in production?
**Content:**
- Single-turn automated: $0.001-$0.05/query
- Multi-step agent (5-10 steps): costs multiply 10-40x
- Full TCO at 100K queries/month: $88K-544K/year (automated) or $626K-2.69M (with 20% human review)
- Break-even thresholds: $75/error (10K queries/yr), $25/error (100K/yr), $0.60/error (1M/yr)
- All cost figures are author estimates based on Feb 2026 API pricing

**Classification:** Derived
**Confidence:** Low (author estimates)
**Sources:** [S19], author estimates
**Tags:** cost, roi, tco, break-even

---

### AB-trust-cal-NOTE-0006
**Title:** EU AI Act and Calibration (Regulatory Vacuum)
**This answers:** Does the EU AI Act require calibration?
**Content:**
- Article 15 requires "appropriate level of accuracy" and declared metrics -- but "calibration" and "confidence" never appear [S14, CT-015]
- Article 14 requires "effective oversight by natural persons" -- without confidence signals, oversight is performative [CT-021]
- Enforcement timeline: Aug 2026 (high-risk), 2027-2028 (CEN/CENELEC harmonized standards)
- Penalties: up to 35M EUR or 7% global revenue
- No jurisdiction explicitly requires calibration as of Feb 2026
- Window to shape CEN/CENELEC technical standards is open now [CT-016]

**Classification:** Evidenced
**Confidence:** High
**Sources:** [S14], CT-015, CT-021, CT-023
**Tags:** eu-ai-act, regulation, article-14, article-15, compliance

---

### AB-trust-cal-NOTE-0007
**Title:** Do Not Deploy Calibration If (5 Scenarios)
**This answers:** When is calibration harmful or wasteful?
**Content:**
1. Cannot verify accuracy on target distribution (false confidence worse than no calibration)
2. Application faces adversarial users (attackers will inflate scores)
3. Cannot monitor demographic fairness for high-stakes decisions (liability risk)
4. Latency SLA <500ms without APRICOT option
5. Error cost below break-even threshold ($0.60-$75/error depending on volume)

**Classification:** Derived
**Confidence:** Med
**Sources:** E4 (Ethicist analysis), Section 5.2 ROI
**Tags:** do-not-deploy, decision-criteria, risk, fairness

---

### AB-trust-cal-NOTE-0008
**Title:** Conformal Prediction: Single-Step Only
**This answers:** Can conformal prediction provide guarantees for multi-agent systems?
**Content:**
- Conformal prediction provides statistical coverage guarantees (e.g., 90% of prediction sets contain correct answer) [S9]
- Requires 200-500 labeled examples per domain (practical; theoretical min ~10) [S9, FM-3]
- Guarantees do NOT compose across dependent pipeline stages [CT-027]
- For multi-agent systems: coverage degrades under independence assumption; under correlation, behavior is unsolved
- Deploy for high-stakes single-step decisions only

**Classification:** Evidenced
**Confidence:** High
**Sources:** [S9], [S10], CT-027, FM-3
**Tags:** conformal-prediction, guarantees, multi-agent, limitation

---

### AB-trust-cal-NOTE-0009
**Title:** ECE Is Insufficient (Use Brier Score)
**This answers:** Is ECE enough to evaluate calibration quality?
**Content:**
- ECE measures binned calibration error (|accuracy - confidence| per bin, weighted average) [S1]
- A model always predicting 50% on a 50% base-rate task has perfect ECE but is useless
- Complete evaluation requires: ECE + Brier Score (combines calibration + sharpness + resolution) + reliability diagrams [CT-004]
- The decomposition ECE = epistemic + systematic is a conceptual analogy, not a mathematical identity [CT-030]

**Classification:** Evidenced
**Confidence:** High
**Sources:** [S1], CT-004, CT-030
**Tags:** ece, brier-score, metrics, evaluation

---

### AB-trust-cal-NOTE-0010
**Title:** LLM-Assisted Research Has Correlated Blind Spots
**This answers:** Can we trust AI-generated research reviews?
**Content:**
- All 14 review agents (v4) and 6 agents (v5) share the same base model (Claude)
- Shared training data creates correlated blind spots -- errors that no agent catches
- 5-prompt self-consistency is epistemically circular: validates consistency using consistency [CX-006]
- Agreement rates likely inflated by 10-20%
- Independent human expert review remains necessary for any claim treated as established

**Classification:** Derived
**Confidence:** Med
**Sources:** CX-006, Section 13 self-calibration
**Tags:** meta-research, llm-limitation, correlated-bias, review

---

## Playbooks

### AB-trust-cal-PLAY-0001
**Title:** Deploy Tier 1 Calibration (Consistency-Based)
**This answers:** How do I add calibration to my existing LLM agent?

**Trigger:** Agent in production without calibration; damage-per-error > break-even threshold
**Goal:** Reduce ECE by deploying consistency-based calibration for all agent outputs
**Inputs:**
- 200+ labeled agent interactions with ground truth (for ECE measurement)
- Choice of consistency model (Haiku, GPT-4o-mini, or same model)
- Semantic similarity threshold (start: 0.85 cosine)

**Steps:**
1. Measure baseline ECE on 200+ labeled examples (15 bins). If agents don't express confidence, that's your first finding.
2. Identify worst-calibrated agent (highest ECE).
3. Classify all agent tasks by risk level (LOW/MEDIUM/HIGH based on cost-of-being-wrong).
4. Implement consistency wrapper: for each query, sample 3 responses (parallel API calls). Compare via embedding cosine similarity >0.85. Report agreement rate as confidence.
5. Choose semantic clustering: (a) exact string match (simple), (b) embedding similarity >0.85 (recommended), (c) LLM-as-judge (most accurate, adds cost).
6. Set abstention thresholds by risk: LOW 30%, MEDIUM 60%, HIGH 80%. For same-model multi-agent chains: add 10-20 percentage points.
7. Implement caching (Redis, TTL 1-24h depending on drift tolerance). 95% cache hit = 20x cost reduction.
8. Set up monitoring: rolling ECE (7-day window), confidence distribution drift (JSD), abstention rate, human override rate.
9. Run for 2 weeks. Compare ECE before vs after. Adjust thresholds based on data.
10. Add calibration regression test to CI/CD: ECE increase >5 points = block deployment.

**Outputs:** Calibrated confidence scores for all agent outputs; monitoring dashboard; ECE improvement metric
**Failure Modes:**
- No labeled data available (can't measure ECE) -> Start with 50-100 manually labeled examples
- All 3 responses identical (systematic bias) -> Confidence is high but may be wrong; add 10% forced human review
- Latency unacceptable (<2s SLA) -> Switch to APRICOT (single auxiliary call)
- API rate limiting from 3x calls -> Implement key rotation + circuit breaker

**Mitigations:** Cache aggressively; use smallest viable model for consistency; parallel not sequential calls
**Acceptance Criteria:** ECE measurably lower than baseline; monitoring operational; abstention routing working

**Classification:** Operational
**Confidence:** High (for Tier 1 components; lower for threshold tuning)
**Sources:** [S2], [S8], [S19], [S23], F1-F4
**Tags:** implementation, tier-1, consistency, playbook

---

### AB-trust-cal-PLAY-0002
**Title:** Choose Your Calibration Architecture (Scenario Selection)
**This answers:** Which calibration tier should my organization deploy?

**Trigger:** Organization decides to invest in calibration infrastructure
**Goal:** Select the right calibration architecture for your scale, risk profile, and budget
**Inputs:**
- Query volume (monthly)
- Risk classification of agent tasks
- Team composition (ML engineer? Statistician?)
- Budget constraints
- Latency requirements

**Steps:**
1. Calculate damage-per-error for your highest-risk agent task. If < $25/error at your volume, stop (calibration ROI is negative).
2. Check "Do Not Deploy If" conditions (NOTE-0007). If any apply, address them first.
3. Select scenario:
   - **Startup (<10K queries/mo, API-only):** Tier 1 + Tier 3. Cost: $50-500/mo. Timeline: 2-4 weeks.
   - **Enterprise (100K+ queries/mo, mixed risk):** Tier 1 + Tier 2 (high-risk) + Tier 3. Cost: $88K-544K/yr. Timeline: 6-12 weeks.
   - **Regulated (healthcare/finance/legal):** Full stack + human review. Cost: $626K-2.69M/yr. Timeline: 3-6 months.
4. For real-time paths (<2s), use APRICOT instead of consistency. For async/batch, use full consistency.
5. Tier 2 (conformal prediction) requires: statistician on team, 200-500 labeled examples/domain, single-step decisions only.
6. Plan phased rollout: Tier 1 first (Month 1), Tier 3 (Month 1-2), Tier 2 (Month 3+).

**Outputs:** Architecture decision; phased implementation plan; budget estimate
**Failure Modes:**
- Overinvesting in low-stakes applications (negative ROI)
- Deploying Tier 2 for multi-agent chains (guarantees don't compose)
- Insufficient labeled data for Tier 2

**Mitigations:** Start with Tier 1 only; measure ROI before scaling
**Acceptance Criteria:** Clear architecture selection documented; budget approved; team assigned

**Classification:** Operational
**Confidence:** Med
**Sources:** Section 4, Section 5, Comparative Analysis
**Tags:** architecture, decision, scenario, playbook

---

## Templates

### AB-trust-cal-TMPL-0001
**Title:** Calibration Measurement Report Template
**When to use:** When measuring ECE for the first time or reporting calibration drift

```markdown
# Calibration Measurement Report
**Date:** YYYY-MM-DD
**Agent:** [agent name]
**Domain:** [e.g., customer support, legal, medical]
**Model:** [e.g., GPT-4o, Claude 3.5]

## Dataset
- Sample size: [n >= 200]
- Source: [production data / benchmark / manually labeled]
- Time period: [date range]
- Labeling method: [human annotation / ground truth / automated]

## ECE Calculation
- Bins: 15
- Method: [equal-width / equal-count]
- ECE: [X.X%]
- Brier Score: [X.XXX]

## Reliability Diagram
[Insert or describe: x-axis = mean predicted confidence per bin, y-axis = actual accuracy per bin]

## Confidence Distribution
- Mean confidence: [X%]
- Median confidence: [X%]
- Std dev: [X%]
- % of outputs > 90% confidence: [X%]

## Risk Classification
- LOW risk tasks: [X%] of volume
- MEDIUM risk tasks: [X%]
- HIGH risk tasks: [X%]

## Comparison (if applicable)
- Previous ECE: [X%]
- Change: [+/- X points]
- Cause: [distribution shift / model update / prompt change / unknown]

## Recommendation
[Deploy calibration / Adjust thresholds / Investigate drift / No action needed]
```

**Pitfalls:**
- Using fewer than 200 samples (insufficient for 15-bin ECE stability)
- Reporting ECE without Brier Score (ECE alone is insufficient)
- Using stale labeled data (production distributions shift in 2-4 weeks)

**Classification:** Operational
**Confidence:** High
**Sources:** [S1], CT-004
**Tags:** template, measurement, ece, brier-score

---

### AB-trust-cal-TMPL-0002
**Title:** Calibration Architecture Decision Record
**When to use:** When documenting the decision to deploy (or not deploy) calibration

```markdown
# Calibration Architecture Decision Record
**Date:** YYYY-MM-DD
**Decision Owner:** [name, role]
**Status:** [Proposed / Approved / Rejected]

## Context
- Agent(s): [list agents in scope]
- Query volume: [X/month]
- Risk classification: [LOW / MEDIUM / HIGH per agent]
- Current ECE: [X% per agent, or "not measured"]

## Decision
[Deploy Tier 1 + 3 / Deploy full stack / Do not deploy / Defer]

## Rationale
- Damage-per-error estimate: [$X]
- Break-even threshold: [$X at current volume]
- ROI assessment: [positive / negative / uncertain]
- "Do Not Deploy" conditions checked: [none apply / condition X applies]

## Architecture Selected
- Tier 0 (entropy): [yes/no, which models]
- Tier 1 (consistency): [yes/no, model choice, cost estimate]
- Tier 2 (conformal): [yes/no, domains, calibration set plan]
- Tier 3 (human routing): [yes/no, threshold levels, reviewer plan]

## Implementation Plan
- Phase 1: [scope, timeline, owner]
- Phase 2: [scope, timeline, owner]
- Phase 3: [scope, timeline, owner]

## Budget
- Monthly API cost: [$X]
- Infrastructure: [$X]
- Human reviewers: [$X or N/A]
- Engineering: [$X]

## Monitoring Plan
- ECE measurement frequency: [weekly]
- Drift alert threshold: [ECE +5 points, JSD >0.15]
- Review cadence: [quarterly]

## Risks
1. [Risk, probability, mitigation]
2. [Risk, probability, mitigation]
```

**Pitfalls:**
- Not documenting the "do not deploy" check
- Skipping ROI calculation (leads to over-investment)
- No monitoring plan (calibration silently degrades)

**Classification:** Operational
**Confidence:** High
**Sources:** Section 4, Section 8, Recommendations
**Tags:** template, decision-record, architecture

---

## Quality Checks

- [x] Coverage: each Key Takeaway maps to >= 1 asset
- [x] Dedupe: no duplicated "This answers"
- [x] Traceability: every asset has classification/confidence/sources
- [x] Actionability: playbooks have trigger/goal/inputs/steps/outputs/failure modes/mitigations/acceptance criteria
- [x] Templates have when-to-use/copy-paste block/pitfalls
