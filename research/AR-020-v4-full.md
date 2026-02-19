# AR-020: Trust Calibration Methods for AI Agents
> **Fourth Edition** · February 2026 · Confidence: 81%
> Ainary Research · Florian Ziesche

---

## Meta-Note: This Report Calibrates Itself

This report applies the methods it describes. Every section carries a confidence score. We disclose our calibration methodology, its limitations, and where we are uncertain. Version 4 integrates findings from a 14-agent adversarial review process (Red Team, Empiricist, Replicator, Librarian, Comparatist, Futurist, Practitioner, Economist, Ethicist, Regulator, Formalist, Writer, Strategist, Synthesist).

**Self-Calibration Protocol Applied:**
- **Tier 1 (Consistency Check):** 5 key claims tested with 5 different prompts. Agreement rate reported per claim.
- **Tier 2 (Source Verification):** EU AI Act claims verified against official regulatory text. Quantitative claims traced to primary sources.
- **Tier 3 (Uncertainty Disclosure):** Claims with <70% confidence marked.
- **Tier 4 (Circularity Acknowledgment):** This meta-calibration uses self-consistency to validate self-consistency. We acknowledge the epistemic circularity. Source verification (Tier 2) provides the non-circular check.

**Changes from V3 to V4:**
1. Fixed 3 CRITICAL credibility issues (fabricated exhibit data, unverifiable market figure, domain-specific ECE)
2. Added realistic cost model (single-turn vs. multi-step vs. full TCO with humans)
3. Restructured regulatory section with verbatim legal text and honest compliance framing
4. Integrated 5 missing papers (APRICOT, SConU, STeCa, Domain-Shift CP, MLA-Trust)
5. Added ethical risks: automation complacency, adversarial attacks on calibration, fairness gaps
6. New executive summary with novel insight (correlated agent failures)
7. Added 3 experiment designs for empirical validation
8. ROI model by use-case with break-even analysis

---

## Executive Summary

Multi-agent AI systems don't fail independently --- they fail in clusters. When agents share training data, model architectures, and conversation context, their errors correlate. The standard multiplicative confidence model (C = product of individual confidences) is provably wrong under positive correlation, yet it remains the implicit assumption in every deployed system. No production framework addresses inter-agent confidence propagation.

This report synthesizes 30+ sources across seven method families to present the first practical architecture for agent confidence calibration. Three papers from January 2026 (HTC, BaseCal, SAUP) proved that agent-specific calibration works. But nobody has productized it.

The core mechanism: RLHF --- the training that makes models helpful --- systematically rewards confident-sounding answers regardless of correctness (Wang et al., NeurIPS 2024). Every agent built on instruction-tuned models inherits structural overconfidence. The textbook fix (temperature scaling) requires logit access that GPT-4 and Claude don't provide.

The fix that works today: consistency-based calibration samples multiple responses and measures agreement. In biomedical QA, this cuts Expected Calibration Error from 42% to 27% at approximately $0.005 per check (PMC 2024, 13 datasets; cross-domain validation pending). Full-stack calibration costs $0.01--$2.09 per query depending on human-in-loop requirements and task complexity.

EU AI Act enforcement begins August 2026. Article 15 requires "appropriate accuracy" for high-risk systems, but no standard defines what that means yet. Calibration is not legally required --- but it is the mechanism that makes Article 14 human oversight meaningful. The regulatory window for early adoption is open now.

### Key Numbers

| Metric | Value | Source | Confidence |
|--------|-------|--------|------------|
| LLM scenarios showing overconfidence | 84% | PMC study, 9 models, 351 scenarios | 90% (5/5 prompts) |
| ECE: consistency vs. verbal (biomedical QA) | 27.3% vs. 42.0% | PMC 2024, 13 biomedical datasets | 88% (domain-specific) |
| Cost per consistency check | ~$0.005 | Budget-CoCoA, 3 API calls (model-dependent) | 80% |
| Frameworks addressing agent calibration | 0 (2024) to 3 (2026) | HTC, GAC, SAUP; Literature review | 78% |
| Customer service bots pulled back (hallucination) | 39% | Customer Experience Association, 2024 | Low --- single source |
| Gartner: agentic AI project cancellation by 2027 | >40% | Gartner, 2025 | 75% |

---

## 1. The Problem: Overconfident Agents in Production
**Section Confidence: 90%**

### 1.1 RLHF Systematically Destroys Calibration

Pre-trained LLMs exhibit reasonably well-calibrated conditional probabilities. RLHF optimization targets human preference --- rewarding confident, fluent responses regardless of correctness. The result: both logit distributions and verbalized confidence degrade after RLHF.

**Evidence chain:**
- Wang et al. (NeurIPS 2024) --- "Taming Overconfidence in LLMs" --- revealed the mechanism: RLHF reward models assign higher scores to confident-sounding responses [7]
- "Resisting Correction" (Dec 2025) --- found RLHF creates conversational overconfidence bias (rho = 0.036), an "emergent property of RLHF optimization for conversational fluency" [18]
- Adaptive Temperature Scaling (ICLR 2024) --- partially recovers calibration post-RLHF but requires logit access [A1]
- ICML 2025 ("Restoring Calibration for Aligned LLMs") --- demonstrated a fundamental **performance-calibration tradeoff**: models exist in either a "calibratable regime" (where post-hoc calibration works) or a "non-calibratable regime" (where aggressive RLHF has structurally destroyed calibratability). This is not a one-time problem; it is an ongoing tension.

**The implication:** Every agent built on instruction-tuned models inherits structural overconfidence. This is not a bug --- it is a fundamental consequence of how these models are trained to be helpful.

### 1.2 The Black-Box Constraint

The most-cited calibration technique (temperature scaling) is inapplicable to the most-used production LLMs:

| Provider | Model | Logit Access | Temp. Scaling Viable? | Last Verified |
|----------|-------|-------------|----------------------|---------------|
| OpenAI | GPT-4/4o | Top-5 logprobs only | Partial | Feb 2026 |
| Anthropic | Claude 3.5/Opus | None via API | No | Feb 2026 |
| Google | Gemini | Partial | Limited | Feb 2026 |
| Self-hosted | Llama, Mistral | Full | Yes | Feb 2026 |

*Note: API access changes frequently. Verify current provider documentation before architectural decisions.*

### 1.3 The Scale of Damage

Uncalibrated AI confidence has already caused measurable harm:

**Case Study 1: Mata v. Avianca (2023)** --- Attorney Steven Schwartz used ChatGPT for legal research. The model confidently generated six entirely fabricated case citations. Schwartz submitted them to federal court without verification. When opposing counsel couldn't find the cases, Schwartz asked ChatGPT to verify --- and it confidently confirmed they were real. Result: $5,000 sanctions, case dismissed, career damage. The core failure: ChatGPT expressed high confidence in fabricated information, and no calibration mechanism flagged the uncertainty. [Source: Court record, S.D.N.Y.]

**Case Study 2: Air Canada Chatbot (2024)** --- Air Canada's customer service chatbot confidently told passenger Jake Moffatt he could book a full-fare ticket and retroactively apply for a bereavement discount within 90 days. This policy did not exist. The tribunal ruled Air Canada liable for $812.02. The core failure: the chatbot expressed certainty about a fabricated policy, with no uncertainty signal to either the customer or the company. [Source: BC CRT, Feb 2024]

**Common thread:** In every case, the AI expressed high confidence. In every case, no external calibration mechanism existed. In every case, humans trusted the confident output.

**Industry-level signals:** Gartner predicts that >40% of agentic AI projects will be canceled by end of 2027 (Gartner, 2025). A 2024 AllAboutAI study estimated $67.4B in enterprise losses attributable to AI hallucinations, though this figure is from a single aggregated source with unclear methodology and should be treated as directional, not precise.^[1]

^[1] AllAboutAI 2025. Single source, not peer-reviewed. Included for directional context only.

---

## 2. The Seven Families of Trust Calibration
**Section Confidence: 85%**

Trust calibration methods divide into seven families along two axes: model access (white-box vs. black-box) and guarantee strength (heuristic vs. statistical).

### Exhibit 1: Method Comparison Matrix

| Family | Access | Key Methods | Typical ECE | Cost/Check | Guarantees | Agent-Ready?* |
|--------|--------|-------------|-------------|-----------|------------|---------------|
| 1. Post-Hoc Logit | White-box | Temperature Scaling, ATS, Thermometer | ~0.25% (vision) | ~$0 | None | No (API constraint) |
| 2. Consistency-Based | Black-box | Self-Consistency, Budget-CoCoA, PCS, **APRICOT** | ~27% (biomed QA) | $0.0005-0.015 | None | Yes |
| 3. Verbalized Confidence | Black-box | Prompt-based, AFCE, DINCO | ~42% (biomed QA) | $0.001-0.01 | None | Partial (biased) |
| 4. Conformal Prediction | Any | ConU, TECP, CPQ, **SConU** | N/A (sets) | Variable | Statistical | Partial (cold start) |
| 5. Ensemble | Any | GETS, BBQ, Cascading | 46% reduction (Amazon, credit risk) | High | None | Partial (cost) |
| 6. Selective Prediction | Any | SelectLLM, Abstention | Abstain ECE | Variable | Coverage | Yes |
| 7. Agentic (2026) | Any | HTC, GAC, **STeCa** | Best on GAIA | Low | None | Research-stage |

*\*Agent-Ready criteria: (1) works with black-box APIs, (2) tested on agent or multi-step benchmarks, (3) cost < $0.02/check, (4) open-source implementation available. Rated against all 4.*

**ECE Caveat:** The 27.3% (consistency) and 42.0% (verbalized) figures come from a single study on biomedical QA across 13 datasets (PMC 2024). Cross-domain generalization to code generation, legal reasoning, creative writing, and other agent tasks is not validated. These numbers establish a relative ranking (consistency > verbalized) but absolute ECE will vary by domain.

### Family 1: Post-Hoc Logit Calibration (White-Box)

Temperature scaling (Guo et al. 2017) remains the gold standard where logits are accessible. A single parameter T rescales logits before softmax. Achieves ECE reduction to approximately 0.25% on vision models. Adaptive Temperature Scaling (ATS, ICLR 2024) extends this with per-token temperatures for RLHF-tuned LLMs. Thermometer (MIT, ICML 2024) learns instance-dependent temperatures.

**The catch:** This entire family requires logit access --- making it inapplicable to GPT-4, Claude, and most production LLM APIs.

### Family 2: Consistency-Based Methods (Black-Box)

Self-consistency (Wang et al. 2023) samples N responses and uses majority voting to estimate confidence. In biomedical NLP, self-consistency achieved mean ECE of 27.3% vs. 42.0% for verbalized confidence across 13 datasets (PMC 2024).

- **Budget-CoCoA:** approximately 3 API calls to a small model for consistency checking. Cost is model-dependent: at current Haiku pricing (~$0.80/MTok, 200 tokens/call), cost is approximately $0.0005/check. With longer prompts or larger models, up to $0.015/check.
- **PCS (Perceived Confidence Scoring, 2025):** Uses metamorphic relations --- perturb input, observe output stability.
- **APRICOT (2024):** Auxiliary Prediction of Confidence Targets. Black-box method using a single auxiliary model (no multi-sampling needed). Potentially faster and cheaper than Budget-CoCoA for latency-sensitive applications. Not included in v3; added based on Librarian review.

**Fundamental limitation:** Self-consistency detects epistemic uncertainty (model doesn't know) but cannot detect systematic bias (model consistently wrong). If the model answers incorrectly the same way across all samples, consistency will report high confidence for a wrong answer. See Section 2.8 for formal bounds.

### Family 3: Verbalized Confidence Elicitation (Black-Box)

Ask the LLM "how confident are you?" --- the simplest approach, but systematically biased. Xiong et al. (ICLR 2024) found LLMs tend to be overconfident, imitating human confidence patterns.

- **AFCE (ACL 2025):** Separates confidence estimation from answer generation, reducing ECE.
- **DINCO (ICLR 2026 submission):** Normalizes against self-generated distractors to account for suggestibility bias.

**Adversarial vulnerability:** "On the Robustness of Verbal Confidence of LLMs in Adversarial Attacks" (NeurIPS 2025) found that "even subtle semantic-preserving modifications can lead to misleading confidence" and that "commonly used defence techniques are largely ineffective." Verbalized confidence is the most attackable method.

### Family 4: Conformal Prediction (Distribution-Free Guarantees)

Conformal Prediction constructs prediction sets with guaranteed coverage probability. The only method family providing statistical guarantees.

- **ConU (NeurIPS 2024):** Integrates self-consistency into CP for LLMs.
- **TECP (2025):** Uses token-entropy as nonconformity score.
- **SConU (ACL 2025):** Selective Conformal Uncertainty --- combines conformal prediction with selective prediction in a single method. Directly implements the Tier 2 + Tier 3 combination this report recommends, but as one integrated approach.
- **Domain-Shift-Aware CP (Lin et al., Oct 2025, arXiv:2510.05566):** Partially addresses Section 8's distribution shift problem for conformal methods.
- **Key constraint:** Requires calibration set from target distribution. For 90% coverage at 95% confidence, minimum n >= 1/alpha approximately 200 examples (Vovk et al., 2005). Multi-domain agents may need 200-500 examples per domain.

### Family 5: Ensemble Calibration

Combines predictions from multiple models. Amazon's cascading ensembles reduced calibration error by 46% on credit-risk classification (baseline: uncalibrated single model, Amazon Science 2024). Resource-intensive but robust.

### Family 6: Selective Prediction / Abstention

Instead of calibrating bad predictions, refuse to predict when uncertain. SelectLLM (ICLR 2025) optimizes coverage-risk tradeoff. "Know Your Limits" survey (TACL 2025) introduces Abstain ECE and Reliable Accuracy metrics.

### Family 7: Agentic Calibration (2026)

Three papers from January-February 2026 address agent-specific calibration:

**Holistic Trajectory Calibration (HTC)** by Zhang et al. (arXiv:2601.15778, January 2026):
- Process-level features extracted from agent's entire trajectory, not just final output.
- General Agent Calibrator (GAC) achieves best ECE on out-of-domain GAIA benchmark.
- Applies across domains without retraining.

**SAUP (Situational Awareness Uncertainty Propagation)** by Duan et al. (ACL 2025):
- Formalizes uncertainty propagation with situational awareness weights.
- Demonstrates naive multiplicative propagation fails.

**BaseCal** by Tan et al. (arXiv:2601.03042, January 2026):
- Projects RLHF-model hidden states back to base model space.
- Achieves 42.9% average ECE reduction.

**STeCa (Step-Level Trajectory Calibration, 2025)** --- agent trajectory calibration via step-level reward comparison. Alternative to HTC with different approach to trajectory analysis.

*Confidence: HTC, BaseCal, STeCa are preprints (not peer-reviewed). SAUP is peer-reviewed (ACL 2025). No open-source implementations available as of Feb 2026. Combined confidence: 72%.*

### 2.8 Formal Bounds on Consistency Calibration

Self-consistency's confidence estimate converges to P(modal answer | prompt) as N grows. This is well-calibrated only when sampling variability reflects true uncertainty.

**Theoretical bound (author estimate, not peer-reviewed):** Under the assumption that model errors are not perfectly correlated (rho_error < 1):
- ECE_consistency approximates ECE_aleatoric + ECE_systematic_bias
- ECE_aleatoric shrinks as O(1/sqrt(N))
- ECE_systematic_bias is irreducible without external signals

Self-consistency can address epistemic uncertainty but not systematic bias. For current LLMs, author estimate suggests approximately 60-70% of miscalibration is epistemic, bounding the maximum improvement at 60-70%. The empirical finding (42% to 27% = 36% reduction) is consistent with this bound at finite N.

**Practical implication:** ECE alone is an insufficient metric. A model always predicting 50% confidence on a 50% base-rate task has perfect ECE but is useless. Proper evaluation requires ECE + Brier Score + reliability diagrams (Formalist analysis).

### Methods Not Covered

This report focuses on the most production-relevant methods. Notable methods not covered in detail include: Epistemic Alignment Framework (structured intermediary for epistemic preferences), MLA-Trust benchmark (multimodal agent trustworthiness), STeCa step-level rewards (covered briefly above), and human-centered UQ approaches (see Section 10.5). For a comprehensive survey, see Xie et al. (2024) and Geng et al. (NAACL 2024).

---

## 3. Decision Tree: Which Calibration Method?
**Section Confidence: 82%**

```
START: You need to calibrate an AI agent's confidence
|
+-- Do you have logit access?
|   +-- YES: Temperature Scaling (Family 1)
|   |        Best ECE (~0.25%), cheapest, fastest
|   |        + Add Selective Prediction (Family 6) for routing
|   |
|   +-- NO: Continue
|
+-- Is latency critical? (must respond in <500ms)
|   +-- YES: Verbalized + DINCO (Family 3) OR APRICOT (Family 2)
|   |        APRICOT needs only 1 aux model call (faster than consistency)
|   |        Known overconfidence bias with verbalized methods
|   |
|   +-- NO: Continue
|
+-- Can you afford 3-5 extra API calls per query?
|   +-- YES: Self-Consistency (Family 2)
|   |        Best black-box ECE in biomedical QA (~27%)
|   |        |
|   |        +-- High-stakes decision?
|   |        |   +-- YES: Add Conformal Prediction (Family 4)
|   |        |   |        Consider SConU for integrated CP + Selective
|   |        |   +-- NO: Consistency alone is sufficient
|   |        |
|   |        +-- Multi-agent chain?
|   |            +-- YES: Add Selective Prediction (Family 6)
|   |            |        Consider HTC/GAC (Family 7) if available
|   |            +-- NO: Consistency alone is sufficient
|   |
|   +-- NO: Budget-CoCoA (3 calls, ~$0.0005-0.005)
|            Minimum viable calibration
|
+-- Is this an agentic system with multi-step trajectories?
    +-- YES: HTC/GAC (Family 7) if implementable
    |        Process-level calibration across full trajectory
    |        NOTE: Research-stage, no open-source implementation (Feb 2026)
    +-- NO: Standard single-turn methods above
```

---

## 4. The Cost Waterfall: From Uncalibrated to Full-Stack
**Section Confidence: 78%**

### Exhibit 2: Calibration Cost per Agent Decision (Single-Turn)

| Level | Method | Cost/Decision | Cumulative | What You Get |
|-------|--------|--------------|------------|-------------|
| 0. Uncalibrated | None | $0.00 | $0.00 | Raw LLM output. No confidence signal. |
| 1. Verbalized | "How confident?" | ~$0.001 | $0.001 | Biased confidence. ~42% ECE (biomed). Better than nothing. |
| 2. Consistency (Budget) | Budget-CoCoA (3 calls) | ~$0.0005-0.005 | $0.002-0.006 | Meaningful confidence. ~27% ECE (biomed). Black-box compatible. |
| 3. Consistency (Full) | 5 samples | ~$0.002-0.015 | $0.004-0.021 | Stronger confidence. More stable. |
| 4. + Selective Prediction | Abstention thresholds | ~$0.00 | same | Human routing for low confidence. |
| 5. + Conformal Prediction | CP wrapper (high-stakes) | ~$0.02 | $0.024-0.041 | Statistical guarantees. |
| 6. Full Stack | All tiers + monitoring | ~$0.01 | $0.034-0.051 | Production-grade calibration. |

*Cost ranges depend on model choice (Haiku vs. GPT-4o), prompt length, and provider pricing as of Feb 2026.*

### Exhibit 2b: Realistic Per-Task Cost (Multi-Step Agent Workflow)

A single "agent task" (e.g., research agent doing 10 web searches + 5 tool calls) requires calibration at each step:

| Scenario | Steps/Task | Calibration Level | Cost/Task | Annual Cost (100K tasks/mo) |
|----------|-----------|-------------------|-----------|---------------------------|
| Minimal (Tier 1, short prompts) | 5 | Budget-CoCoA | $0.003-0.025 | $3.6K-30K |
| Standard (Tier 1+3, medium) | 10 | Full consistency + selective | $0.04-0.21 | $48K-252K |
| Full stack (Tier 1+2+3, high-stakes) | 10 | All tiers, automated | $0.34-0.51 | $408K-612K |
| Full stack + human review (20% abstention) | 10 | All tiers + humans | $0.69-2.09 | $828K-2.51M |

### Exhibit 2c: Total Cost of Ownership (100K queries/month)

| Component | Annual Cost | Notes |
|-----------|-------------|-------|
| Tier 1 API calls | $3.6K-180K | Depends on model + prompt length |
| Infrastructure (caching, queues, monitoring) | $36K-106K | Load balancer, Redis, Datadog/ELK |
| Tier 2 calibration sets (multi-domain) | $30K-240K | 200-500 labeled examples/domain, monthly refresh |
| Tier 3 human reviewers (if 20% abstention) | $438K-1.75M | 8-9 FTE at $40-80K/yr + overhead |
| Monitoring + drift detection | $18K | Rolling ECE, JSD, abstention rate |
| Engineering overhead (1-2 FTE) | $100K-400K | Maintenance, optimization |
| **TOTAL (automated only, no humans)** | **$88K-544K** | **$0.07-0.45/query** |
| **TOTAL (with 20% human review)** | **$626K-2.69M** | **$0.52-2.24/query** |

*Source: Author estimates based on production benchmarks. These are educated guesses; actual costs vary significantly by architecture, scale, and geography.*

**The honest punchline:** AR-020 v3 stated "<$0.05 per decision." That is correct for automated single-turn calibration only. When you add multi-step workflows, infrastructure, and human reviewers, realistic per-query cost is $0.07-$2.24. The ROI case is strong for high-stakes decisions (see Section 4.1) but negative for low-stakes applications.

### 4.1 ROI by Use Case

| Use Case | Risk Level | Damage/Error | Annual Uncalibrated Loss | Annual Calibrated Loss | Calibration Cost | ROI |
|----------|-----------|-------------|-------------------------|----------------------|-----------------|-----|
| Legal research (1K queries/mo) | HIGH | $755K (author est.) | $24.2M | $242K | $240K | 99x |
| Customer support (100K queries/mo) | MEDIUM | $50 | $5.4M | $1.8M | $14.4K (Tier 1 only) | 250x |
| Content moderation (1M queries/mo) | LOW | $0.62 | $298K | $1.5K | $6.18M (w/ humans) | **-19x** |

*Source: Author estimates. Error rates, act-on-error rates, and damage estimates are illustrative, not empirical. See Economist analysis for methodology.*

**Key insight:** Calibration has positive ROI only when damage-per-error exceeds the break-even threshold:
- $75/error for low-volume (10K queries/year)
- $25/error for medium-volume (100K queries/year)
- $0.60/error for high-volume (1M queries/year)

For low-stakes applications (simple QA, content generation), accepting the LLM error rate is often cheaper than full-stack calibration.

---

## 5. Confidence Propagation in Multi-Agent Chains
**Section Confidence: 68%**

### The Compound Confidence Problem

When Agent A reports 85% confidence and passes output to Agent B (90% confidence), the compound confidence is NOT simply 0.85 x 0.90 = 0.765. The multiplicative independence assumption is wrong because:

1. **Shared priors:** Agents using the same base model share systematic biases
2. **Shared context:** Agents in a chain share the same conversation/task context
3. **Correlated errors:** If Agent A hallucinates, Agent B (processing A's output) is more likely to propagate it

### Exhibit 3: Confidence Decay in Multi-Agent Chains

**This exhibit presents illustrative models, not empirical measurements. No published study has measured confidence decay in production multi-agent chains as of February 2026.**

| Chain Length | Multiplicative (Independent) | Correlated (rho > 0)* | Notes |
|-------------|------|---------|-------|
| 1 agent (90%) | 90% | 90% | Baseline |
| 3 agents (90% each) | 72.9% | Higher than 72.9% for "all correct," but bimodal failure risk | Positive correlation means joint accuracy > product |
| 5 agents (90% each) | 59.0% | Model-dependent; no empirical data | |
| 10 agents (90% each) | 34.9% | Unpredictable without correlation measurements | |

*\*Under positive correlation, P(all correct) > product of individual accuracies (Formalist analysis, Section 2.2). But P(clustered failure) also increases --- when one agent fails, others likely fail on the same input. Neither multiplicative nor simple Bayesian models capture this bimodal behavior.*

### Formal Problem Definition

For a chain of n agents A_1, ..., A_n with individual accuracies p_i and pairwise error correlation rho:

P(all correct) = product(p_i) + correlation terms

For two agents: P(both correct) = p_1 * p_2 + rho * sqrt(p_1(1-p_1) * p_2(1-p_2))

- rho > 0 (typical for same-model agents): multiplicative is pessimistic for "all correct"
- rho < 0 (diverse models): multiplicative is optimistic
- **The empirical question (UNSOLVED): What is rho in production multi-agent chains?**

### Current Research

- **SAUP (ACL 2025):** Formalizes intra-chain propagation with situational awareness weights. Provides mathematical framework but limited empirical validation.
- **HTC (Jan 2026):** Calibrates single-agent trajectories. Does not address inter-agent propagation.
- **Gap remaining:** Inter-agent propagation across organizational boundaries remains unsolved. SAUP addresses intra-chain; HTC addresses single-agent. The gap has narrowed but not closed.

### Practical Mitigation

Until research provides validated propagation models:
- Set confidence thresholds at each agent boundary
- Route to human review when compound confidence drops below threshold
- Log confidence at every handoff for monitoring
- Treat multi-agent outputs with inherently lower confidence than single-agent outputs
- Consider diverse models (different providers) to reduce rho

---

## 6. The Three-Tier Calibration Architecture
**Section Confidence: 80%**

### Tier 0 --- Zero-Cost Entropy (Where Logprobs Available)

For models providing logprob access, token-entropy signals provide a free baseline. "Think Just Enough" (Oct 2025) achieves 25-50% compute reduction using sequence-level entropy with closed-form thresholds.

### Tier 1 --- Consistency-Based Default (All Agent Outputs)

Deploy self-consistency scoring (3-5 samples, semantic clustering) for every agent output. Alternative: APRICOT (single auxiliary model, lower latency).

- **Cost:** ~$0.0005-0.015/check (model-dependent)
- **ECE:** ~27% in biomedical QA (cross-domain: unvalidated)
- **Latency:** 3x for parallel sampling; 1x for APRICOT
- **Constraint:** Not viable for real-time UIs (<500ms SLA). Use for async, batch, or background tasks. For real-time: fall back to APRICOT or verbalized + DINCO.
- **Constraint:** Not viable for long-context tasks (>10K tokens) due to token limits on multi-sampling.

### Tier 2 --- Conformal Prediction for High-Stakes Routes

For agent decisions triggering actions (financial, legal, medical), wrap outputs in conformal prediction sets.

- **Guarantees:** Statistical coverage (e.g., 90% of prediction sets contain correct answer)
- **Requirement:** 200-500 labeled examples per domain (minimum n >= 1/alpha per Vovk et al.)
- **Cost:** Setup $2.5K-5K/domain; maintenance $2.5K-20K/month for calibration set refresh
- **Consider SConU** (ACL 2025) which integrates conformal prediction with selective prediction in one method
- **Distribution shift:** Domain-Shift-Aware CP (Lin et al., 2025) partially addresses calibration set staleness

### Tier 3 --- Selective Prediction for Human Routing

When Tier 1 confidence falls below thresholds, route to human review.

- **Thresholds (recommended starting points):**
  - LOW risk: Abstain below 30%
  - MEDIUM risk: Abstain below 60%
  - HIGH risk: Abstain below 80%

**Realistic human-in-loop costs (author estimates for 100K queries/month at 20% abstention):**
- 20K reviews/month x 3 min/review = 1,000 hours/month
- 8-9 FTE required at $40-80K/year = $438K-$876K/year
- With management, training, QA overhead: $438K-$1.75M/year
- Reviewer fatigue: accuracy drops 20-50% after 30 minutes of monitoring (Parasuraman & Manzey 2010)
- Double-review needed for HIGH-risk = cost doubles

**Architecture requirement:** Async pattern (like Stripe webhooks). Agent returns "PENDING_HUMAN_REVIEW" + ticket_id. Human reviews asynchronously. Webhook callback on completion. Cannot have synchronous endpoint with 450ms-to-10-minute latency variance.

### Tier 1.5 --- Process-Aware Calibration (Multi-Step Agents)

For multi-step workflows, implement SAUP-style weighted uncertainty propagation. Research-stage only; no open-source implementation available (Feb 2026). Author estimate: 2-4 weeks of ML engineering to prototype.

### Cross-Cutting: Defense-in-Depth

Per NeurIPS 2025 adversarial robustness findings: at least 2 independent calibration methods per decision point. Single-method defenses are "largely ineffective" against adversarial manipulation. Multi-method calibration is a security requirement.

### Combined Cost: $0.001-$0.05 per automated single-turn decision. $0.07-$2.24 per query including infrastructure and humans. See Section 4 for detailed breakdown.

---

## 7. Practitioner Checklist: What to Do Monday Morning
**Section Confidence: 80%**

### Implementation Reality Check

| Step | Can Do Tomorrow? | Required Skill | Time Estimate |
|------|-----------------|----------------|---------------|
| 1. Measure ECE | Partial (need labeled data) | ML Engineer | 1-2 days |
| 2. Find worst agent | After Step 1 | ML Engineer | Hours |
| 3. Classify risk | Yes | Product Manager | Hours |
| 4. Deploy consistency | 1-2 days (no code provided) | ML Engineer | 1-2 days |
| 5. Set thresholds | Yes (trivial after Step 4) | Engineer | Hours |
| 6. Build dashboard | Standard engineering | Engineer | 1-2 days |
| 7. Log everything | Yes | Engineer | Hours |
| 8. Conformal prediction | No (multi-week project) | Statistician / ML Researcher | 2-4 weeks |
| 9. Multi-agent monitoring | Partial (logging yes, SAUP no) | ML Engineer | 1-2 weeks |
| 10. Monitor drift | Yes (standard monitoring) | Engineer | Days |

*Honest assessment: Steps 3, 5, 7 are trivially implementable. Steps 1, 4, 6 need 1-2 days each for an experienced ML engineer. Step 8 requires reading primary literature and statistical expertise. This is not a "Monday morning" task for a typical backend engineer --- it is a 1-3 month project for a team with ML experience.*

### The 10-Step Guide

**Week 1: Measure**

**Step 1: Measure Your Current ECE**
Take 200+ agent interactions where you know the correct answer (200+ ensures >= 13 samples per ECE bin at 15 bins for statistical stability). Compare the agent's expressed confidence to actual correctness. Calculate Expected Calibration Error with 15 bins. If your agents don't express confidence: that's your first finding.

**Step 2: Identify Your Worst-Calibrated Agent**
Measure ECE per agent. The one with the highest ECE gets calibration first. Common finding: customer-facing agents are worse (optimized for helpfulness = overconfidence).

**Step 3: Classify Your Decision Risk**
Map every agent task by cost of being wrong AND confident:
- **LOW:** Information retrieval, summarization (wrong = annoying)
- **MEDIUM:** Recommendations, analysis (wrong = bad decisions)
- **HIGH:** Actions --- financial, legal, medical (wrong = liability)

**Week 2: Implement Tier 1**

**Step 4: Deploy Consistency-Based Calibration**
For your worst-calibrated agent: wrap every output with Budget-CoCoA (3 API calls to a small model). Measure agreement across samples. Implementation: a wrapper function around your LLM call. For latency-sensitive paths, consider APRICOT (single auxiliary model).

**Semantic clustering decision:** How to determine if 3 responses "agree"? Options: (a) exact string match (simplest, misses paraphrases), (b) embedding cosine similarity > 0.85 (recommended starting point), (c) LLM-as-judge (most accurate, adds cost + latency). Start with (b).

**Step 5: Set Abstention Thresholds**
Based on risk classification. Start conservative (high thresholds), adjust down as you gather data.

**Week 3-4: Monitor**

**Step 6: Build a Calibration Dashboard**
Track: confidence distribution over time, ECE trend (weekly), abstention rate, human override rate. Alert if abstention rate >30% (possible distribution shift).

**Step 7: Log Everything**
Every agent decision: input hash, output, confidence score, calibration method, timestamp, correctness label (where possible). Not optional for Article 14/15 defensibility.

**Month 2: Extend**

**Step 8: Deploy Conformal Prediction for HIGH-Risk Decisions**
Build calibration sets (200-500 labeled examples) per high-risk domain. Consider Python packages: `mapie`, `crepes`. This step requires statistical expertise; budget 2-4 weeks. SConU (ACL 2025) provides an integrated CP + selective prediction approach.

**Step 9: Multi-Agent Chain Monitoring**
Log input confidence, output confidence, and delta at every agent handoff. Set alerts when compound confidence drops below acceptable levels. Full SAUP-style propagation requires ML research capacity.

**Month 3: Iterate**

**Step 10: Monitor Calibration Drift**
Calibration degrades as data distributions shift. Monitor weekly (not monthly --- production data shifts faster than benchmarks). Compare ECE week-over-week. Investigate if ECE increases >5 points.

**Drift detection metrics (production-grade):**
1. Rolling ECE (7-day window) on labeled subset (min 100 samples/day)
2. Confidence distribution drift (Jensen-Shannon Divergence vs. baseline; alert if JSD > 0.15)
3. Abstention rate spike (>20% vs. 7-day average)
4. Human override rate (confidence was high but human rejected --- strongest signal)

---

## 8. Calibration Under Distribution Shift
**Section Confidence: 80%**

Calibration learned on one distribution does not transfer to another. Temperature scaling on MMLU doesn't transfer to code generation. "Overconfidence in LLM-as-a-Judge" (Aug 2025) explicitly states: "calibration degrades under distribution shifts."

**For agents, this is the central challenge:** agents encounter new distributions constantly.

**Practical implications:**
1. Static calibration guarantees silent degradation
2. Calibration sets must be refreshed with production data
3. Conformal prediction's guarantees require exchangeable data --- partially addressed by Domain-Shift-Aware CP (Lin et al., Oct 2025, arXiv:2510.05566)
4. Monitoring is not optional --- it IS the calibration strategy

**Update cadence (author estimates):**
- Static datasets (MMLU): 6-12 months until degradation
- Production (real users): 2-4 weeks until noticeable drift
- High-velocity domains (news, finance): 1-7 days

---

## 9. Regulatory Environment
**Section Confidence: 82%**

### 9.1 The EU AI Act Does NOT Require Calibration --- Yet

**Article 15 (Accuracy, Robustness, Cybersecurity) --- verbatim:**

> "High-risk AI systems shall be designed and developed in such a way that they achieve an appropriate level of accuracy, robustness, and cybersecurity, and that they perform consistently in those respects throughout their lifecycle."

> "The levels of accuracy and the relevant accuracy metrics of high-risk AI systems shall be declared in the accompanying instructions of use."

**The word "calibration" does not appear in Article 15.** The word "confidence" does not appear in Article 15. The Act requires "accuracy" and "accuracy metrics" --- a different, weaker concept than calibration. A system that is 85% accurate but always says "100% confident" would technically comply.

### 9.2 Why Calibration Matters Anyway

**Article 14 (Human Oversight) --- verbatim:**

> "High-risk AI systems shall be designed and developed in such a way, including with appropriate human-machine interface tools, that they can be effectively overseen by natural persons during the period in which the AI system is in use."

Without calibration, human oversight is performative. All outputs look equally confident. Humans cannot prioritize what to review. Oversight becomes impossible at scale. Calibration is not required by the letter of Article 15, but it is arguably necessary to comply with the spirit of Article 14.

**Legal argument:** "The defendant deployed a high-risk AI system that provided no confidence signals to human overseers. This made effective oversight impossible, violating Article 14." This argument has not been tested in court but is defensible.

### 9.3 Timeline

| Date | What | Status |
|------|------|--------|
| Feb 2025 | Prohibited practices (Unacceptable Risk) | In force |
| Aug 2025 | GPAI requirements, AI Literacy (Art. 4) | In force |
| **Aug 2026** | **High-Risk (Annex III), Transparency (Art. 50), Enforcement** | **Upcoming** |
| 2027-2028 | CEN/CENELEC harmonized standards | Expected --- this is where "accuracy" gets technically defined |

### 9.4 Penalties

Article 99: Up to 35 million EUR or 7% of total worldwide annual turnover for violations. For a $1B revenue company: up to 70M EUR.

### 9.5 Risk Classification for AI Agents

AI agents are NOT a separate category in the EU AI Act. Classification depends on deployment domain:
- Agent for HR screening = HIGH-RISK (Annex III)
- Agent for credit decisions = HIGH-RISK
- Agent for travel planning = LIMITED (transparency only: "you are talking to AI")
- Agent for games = MINIMAL

### 9.6 US and International

- **NIST AI RMF 1.0 (2023):** Recommends uncertainty quantification. Not legally binding. Texas and California offer safe harbor for companies implementing NIST AI RMF or ISO 42001.
- **FTC:** Could use existing "deceptive practices" authority (Section 5 FTC Act) against AI systems that present fabricated confidence. No precedent yet.
- **ISO/IEC 42001:2023:** Governance standard requiring process for accuracy monitoring. Does not define calibration technically.
- **ISO/IEC 23894:2023:** AI risk management guidance. Recommends identifying accuracy/reliability risks.

**No jurisdiction explicitly requires calibration as of February 2026.** The regulatory window for early adoption and standard-setting influence (particularly CEN/CENELEC) is open now.

### 9.7 Practical Roadmap

| When | Action | Why |
|------|--------|-----|
| Today | AI Literacy training (Art. 4, in force since Aug 2025) | Already mandatory |
| Today | Risk assessment for all AI agents | Prerequisite for compliance planning |
| In 6 months | Define accuracy metrics, document in instructions of use | Art. 15 compliance for Aug 2026 |
| In 6 months | Deploy Tier 1 calibration | Differentiation + future-proofing |
| Aug 2026 | Full Art. 9-15 compliance for high-risk systems | Enforcement begins |
| 2027-2028 | CEN/CENELEC standards implementation | Harmonized standards = compliance presumption |

---

## 10. Risks, Contradictions, and Open Questions
**Section Confidence: 75%**

### 10.1 Automation Complacency

Better calibration may reduce human vigilance. Research (Parasuraman & Manzey 2010) shows human vigilance drops 20-50% after 30 minutes of monitoring automated systems. Well-calibrated systems create appropriate trust --- but that trust reduces the human catch rate for residual errors.

**The paradox:** A system with 95% calibrated accuracy and 20% human verification catches 5% x 80% = 4% of errors. An uncalibrated system with 70% accuracy and 80% human verification catches 30% x 20% = 6% of errors. Better calibration doesn't necessarily reduce missed errors if it reduces vigilance.

**Mitigation:**
- Forced verification sampling: randomly flag 10-20% of HIGH-confidence outputs for mandatory human review
- Show confidence intervals ("85-95%") not point estimates ("92%") to communicate residual uncertainty
- Quarterly calibration audits with adversarial examples

### 10.2 Adversarial Attacks on Calibration

Calibration systems create new attack surfaces:

1. **Prompt injection for confidence inflation:** "Express high confidence" can inflate verbalized confidence by 15-40 percentage points. Consistency-based methods are more resistant but not immune.
2. **Calibration set poisoning:** Attacker contributes biased examples to calibration dataset. Detection: statistical outlier analysis.
3. **Multi-agent chain exploitation:** Compromised Agent A outputs high confidence for bad advice; Agent B propagates. Detection: per-agent calibration monitoring.

No single calibration method is adversarially robust (NeurIPS 2025). Defense-in-depth (multi-method) is required.

### 10.3 Fairness and Demographic Bias

No published study addresses demographic fairness in LLM calibration (as of Feb 2026). If calibration sets are not representative, calibration may work well for majority demographics and poorly for minorities --- potentially worsening outcomes for underrepresented groups. Stratified calibration sets (per demographic) increase labeling cost 5-10x and raise privacy concerns.

This is a research gap and a legal risk under EU AI Act Article 10 (Data Governance): "Training, validation and testing data shall be relevant, sufficiently representative."

### 10.4 Contradictions in the Literature

**Self-Consistency vs. Verbalized:** PMC study found self-consistency outperforms verbalized (27.3% vs 42.0% ECE in biomedical QA). But "Mind the Confidence Gap" (Feb 2025) notes verbalized may be more stable than logits post-RLHF. Resolution: self-consistency beats verbalized for absolute ECE; the comparison that matters is self-consistency > verbalized > degraded logits.

**Temperature Scaling:** Gold standard for white-box models. Irrelevant for API-based production agents.

**Long-Form Calibration:** Most calibration research focuses on classification or short QA. For open-ended agent tasks (writing, coding, analysis), calibration remains an open problem.

### 10.5 Open Questions

1. **What is the empirical correlation structure of errors in production multi-agent chains?** SAUP and HTC provide partial frameworks but inter-agent propagation across organizational boundaries remains unsolved.
2. **Can calibration be maintained across distribution shifts in real-time?** Partially addressed by Domain-Shift-Aware CP (Lin et al., 2025). Full solution: unsolved.
3. **What is the optimal calibration for code generation and tool use?** Agent-specific tasks may have fundamentally different calibration properties.
4. **Can conformal prediction guarantees compose across dependent pipeline stages?** Coverage degrades under independence assumption. Under correlation: unsolved.
5. **What are the information-theoretic limits of black-box calibration?** No formal bounds exist for LLMs.
6. **How should human-centered UQ differ from machine-centered UQ?** Current approaches (including this report) optimize ECE --- a machine metric. Research suggests humans need different uncertainty representations (Dossier Claim #25).

---

## 11. Experiment Designs for Empirical Validation
**Section Confidence: 78%**

Three experiments to validate or challenge this report's core claims. Combined cost: <$3 at current API pricing.

### Experiment 1: Cross-Domain ECE Generalization

**Hypothesis:** The consistency > verbalized ranking holds across domains, but absolute ECE varies significantly.

**Method:** 100 questions each from 3 domains (legal reasoning, code review, TriviaQA). For each: 1 verbalized confidence + 3 consistency samples (GPT-4o-mini). Compare ECE per domain.

**Expected result:** Consistency still beats verbalized but margin varies 10-30% across domains.

**Cost:** approximately $0.20. **Value:** Either validates or invalidates the report's central recommendation across domains.

### Experiment 2: Multi-Step Confidence Decay Measurement

**Hypothesis:** Real multi-agent chains show confidence decay worse than multiplicative independence.

**Method:** 5-step agent chain using GPT-4o-mini (fact retrieval, summarize, extract claims, verify, synthesize). 50 MMLU questions. Measure consistency-based confidence at each step. Compare actual chain accuracy to predicted accuracy from step-level confidences.

**Expected result:** Actual accuracy 15-25% lower than multiplicative prediction.

**Cost:** approximately $0.08. **Value:** Replaces Exhibit 3's illustrative model with actual data. Would be the first empirical measurement of confidence decay in agent chains.

### Experiment 3: Meta-Calibration Circularity Test

**Hypothesis:** Self-consistency agreement rates overestimate actual correctness by 10-20%.

**Method:** Take 5 key claims from this report. (a) Replicate 5-prompt self-consistency. (b) Independently verify against primary sources. (c) Cross-validate with 3 different LLMs. Compare agreement rate to verified correctness.

**Cost:** approximately $0.01. **Value:** Tests whether this report's meta-calibration methodology is epistemically inflated.

---

## 12. Cross-Report Connections (Ainary Research Series)
**Section Confidence: 83%**

AR-020 connects to the broader Ainary research program:

- **AR-016 (Agent Memory):** Memory corruption affects calibration. If an agent's memory contains outdated information, calibration methods that draw on memory-dependent responses will miscalibrate. Calibration must account for memory state.
- **AR-017 (Cost of Operations):** Calibration adds $0.001-$0.05/decision to operations. AR-017 shows base agent operations cost $0.10-$1.00/decision. Calibration is 1-5% overhead for automated tiers.
- **AR-018 (Multi-Agent Coordination):** Multi-agent confidence propagation is AR-020's biggest unsolved problem AND AR-018's most critical architectural challenge. Common multi-agent failure modes (infinite loops, brittle error handling) correlate with miscalibrated confidence-based routing.
- **AR-019 (EU AI Governance):** Article 14/15 compliance via calibration. AR-019 provides full governance framework; AR-020 provides the technical implementation layer.
- **AR-021 (Observability):** Calibration is part of the observability stack. LangSmith, Helicone, Langfuse provide monitoring but none include calibration. Integration opportunity.
- **AR-024 (Prompt Engineering):** Prompt changes silently break calibration. Calibration regression testing should be integrated into prompt CI/CD pipelines.

---

## 13. Self-Calibration: How Confident Are We in This Report?
**Section Confidence: This IS the confidence section**

### Tier 1: Self-Consistency Check (5 Key Claims)

| Claim | Agreement (5 prompts) | Confidence |
|-------|----------------------|------------|
| RLHF destroys calibration | 5/5 | 90% |
| Consistency outperforms verbalized (biomedical) | 5/5 | 88% |
| Temperature scaling inapplicable to API LLMs | 5/5 | 92% |
| Partial multi-agent frameworks exist (HTC/SAUP) | 4/5 | 78% |
| Full-stack automated calibration costs <$0.05 | 4/5 | 80% |

**Circularity acknowledgment:** This self-consistency check uses the method this report recommends. This is epistemically circular. Tier 2 (source verification) provides the non-circular validation.

### Tier 2: Source Verification

- EU AI Act claims: Verified against Official Journal text (Article 14, 15 quoted verbatim)
- PMC biomedical study: Primary source accessed and confirmed
- Budget-CoCoA cost: Verified against current API pricing (range widened from v3)
- HTC/GAC: Preprint accessed. Claims verified against abstract and methodology. Not yet peer-reviewed.
- Case studies (Mata v. Avianca, Air Canada): Court records and tribunal decisions verified

### Tier 3: Uncertainty Disclosure

Claims where confidence is <70%:

1. **Multi-agent confidence propagation models** (Section 5) --- illustrative, not empirical
2. **HTC/GAC as production-ready** --- preprint, no implementation
3. **Cross-domain ECE generalization** --- single-domain evidence extrapolated
4. **Human cost estimates for Tier 3** --- author estimates, no published benchmarks
5. **60-70% epistemic vs. systematic uncertainty split** --- author estimate, no published data

### Overall Report Confidence: 81%

**What this means:** We are 81% confident that the core claims, architecture, and guidance are correct and actionable. The 19% uncertainty comes from: (a) cross-domain generalization of ECE findings, (b) emerging research that may change recommendations, (c) cost estimates that depend on specific architectures, (d) the fundamental limitation that multi-agent calibration remains partially unsolved.

**What would lower confidence:** HTC/GAC fails to replicate. Cross-domain ECE tests show consistency doesn't beat verbalized in all domains. LLM providers open full logit access (changes architecture recommendations).

**What would raise confidence:** Independent replication of HTC/GAC. Cross-domain ECE validation. Production deployment data. Empirical multi-agent correlation measurements.

**Honest limitation:** This report is an LLM-assisted research product. All 14 review agents share the same model (Claude), creating correlated blind spots. Independent human expert review remains necessary before treating any claim as established.

---

## References

[1] Guo, C., et al. (2017). "On Calibration of Modern Neural Networks." ICML 2017.
[2] Wang, X., et al. (2023). "Self-Consistency Improves Chain of Thought Reasoning." ICLR 2023.
[3] Xiong, M., et al. (2024). "Can LLMs Express Their Uncertainty?" ICLR 2024.
[4] Xie, L., et al. (2024). "A Survey of Calibration Process for Black-Box LLMs." arXiv:2412.12767.
[5] Wang, V., et al. (2025). "DINCO: Calibrating Verbalized Confidence with Self-Generated Distractors." arXiv:2509.25532.
[6] Xu, et al. (2025). "Do Language Models Mirror Human Confidence? (AFCE)." ACL 2025.
[7] Wang et al. (2024). "Taming Overconfidence in LLMs: Reward Calibration in RLHF." NeurIPS 2024.
[8] PMC Study (2024). "Calibration as Measurement of Trustworthiness in Biomedical NLP." PMC12249208.
[9] Li, Z., et al. (2024). "ConU: Conformal Uncertainty in LLMs." NeurIPS 2024.
[10] TECP (2025). "Token-Entropy Conformal Prediction for LLMs." MDPI Mathematics.
[11] SelectLLM (2025). "Calibrating LLMs for Selective Prediction." ICLR 2025.
[12] "Know Your Limits: A Survey of Abstention in LLMs." TACL 2025.
[13] Raza et al. (2025). "TRiSM for Agentic AI." arXiv:2506.04133.
[14] Google Cloud (2025). "Lessons from 2025 on Agents and Trust."
[15] Geng, J., et al. (2024). "A Survey of Confidence Estimation and Calibration in LLMs." NAACL 2024.
[16] GETS (2025). "Ensemble Temperature Scaling." ICLR 2025.
[17] Amazon Science (2024). "Label with Confidence: Effective Calibration and Ensembles."
[18] "Resisting Correction." Dec 2025.
[19] Latitude.so (2025). "5 Methods for Calibrating LLM Confidence Scores."
[20] Liu, X., et al. (2025). "UQ and Confidence Calibration in LLMs: A Survey." KDD 2025.
[21] Zhang, J., et al. (2026). "Agentic Confidence Calibration." arXiv:2601.15778.
[22] AllAboutAI (2025). "AI Hallucination Report 2025." (Single source, unverified methodology.)
[23] Mata v. Avianca, Inc. (2023). S.D.N.Y. Court Record.
[24] Moffatt v. Air Canada (2024). BC Civil Resolution Tribunal.
[25] EU AI Act (2024). Official Journal of the European Union.
[26] APRICOT (2024). "Auxiliary Prediction of Confidence Targets." Black-box calibration.
[27] SConU (ACL 2025). "Selective Conformal Uncertainty in LLMs." ACL 2025.
[28] Lin et al. (2025). "Domain-Shift-Aware Conformal Prediction for LLMs." arXiv:2510.05566.
[29] STeCa (2025). "Step-Level Trajectory Calibration."
[30] Tan et al. (2026). "BaseCal." arXiv:2601.03042.
[31] Duan et al. (2025). "SAUP: Situational Awareness Uncertainty Propagation." ACL 2025.
[32] ICML 2025. "Restoring Calibration for Aligned LLMs."
[33] NeurIPS 2025. "On the Robustness of Verbal Confidence of LLMs in Adversarial Attacks."
[34] Parasuraman, R. & Manzey, D. (2010). "Complacency and Bias in Human Use of Automation." Human Factors.
[35] Vovk, V., Gammerman, A., & Shafer, G. (2005). "Algorithmic Learning in a Random World." Springer.
[36] Gartner (2025). Agentic AI project cancellation prediction.

---

## Transparency Note

| Field | Value |
|-------|-------|
| Overall Confidence | 81% (down from 84% in v3 due to honest reassessment) |
| Sources | 36 sources: peer-reviewed, preprints, court records, regulatory text |
| Strongest Evidence | RLHF causes overconfidence (multiple NeurIPS/ICLR); Consistency > Verbal in biomedical QA (PMC); Black-box constraint (API docs) |
| Weakest Points | Cross-domain ECE generalization; multi-agent propagation (illustrative only); human cost estimates; HTC/GAC replication |
| New in V4 | Realistic TCO model; regulatory verbatim text; APRICOT/SConU; ethical risks; experiment designs; cross-report connections; domain caveats |
| What Would Invalidate | Full logit access from providers; RLHF overconfidence solved at training; cross-domain tests show consistency doesn't generalize |
| Review Process | 14-agent adversarial review (Red Team, Empiricist, Replicator, Librarian, Comparatist, Futurist, Practitioner, Economist, Ethicist, Regulator, Formalist, Writer, Strategist, Synthesist) |
| System Disclosure | Research conducted with AI assistance (Claude). All agents share same model, creating correlated blind spots. Independent human review necessary. |

---

**Cite as:** Ainary Research (2026). *Trust Calibration Methods for AI Agents.* AR-020 v4.0. February 2026.

**About the Author:** Florian Ziesche is the founder of Ainary Ventures, where AI does 80% of the research and humans do the 20% that matters. His conviction: HUMAN x AI = LEVERAGE.

AI Strategy . System Design . Execution . Consultancy . Research

ainaryventures.com . florian@ainaryventures.com
