# AR-020 Trust Calibration Methods — Asset Pack

**Created:** 2026-02-19
**Source:** AR-020-v2 Deep Dive Research
**Purpose:** Reusable calibration knowledge assets for Ainary agent infrastructure, consulting, content

---

## ATOMIC NOTES

### AB-calibration-NOTE-0001: Consistency-Based Calibration for Black-Box LLMs

**This answers:** "How do you calibrate confidence when you can't access model logits?"

**Content:**
- Self-Consistency (Wang et al. 2023): Sample N responses with temperature >0, cluster by semantic similarity, use cluster frequency as confidence proxy
- Achieves 27.3% mean ECE vs. 42.0% verbal and 44.2% hybrid across 13 biomedical datasets (PMC 2024)
- Budget-CoCoA variant: Only 3 API calls to a small model (~$0.005/check)
- PCS (Perceived Confidence Scoring, 2025): Uses metamorphic relations — perturb input, observe output stability
- Core insight: Agreement across diverse samples is a better proxy for correctness than any single self-assessment
- Works with ANY LLM API — no logits, no fine-tuning, no model modifications needed

**Classification:** EVIDENCED
- Multiple peer-reviewed studies confirm effectiveness
- PMC 2024 comparison across 13 datasets provides robust evidence

**Confidence:** HIGH (85%)

**Sources:**
- Wang et al. ICLR 2023 (Self-Consistency)
- PMC 2024 biomedical calibration study
- PCS arxiv 2502.07186

**Failure Modes:**
- Cost: N samples = N × API cost (mitigated by Budget-CoCoA)
- Latency: N sequential or parallel calls add time
- Semantic clustering quality varies (paraphrase detection is imperfect)
- Low-diversity sampling: If model always produces same answer, consistency appears high regardless of correctness
- Doesn't address epistemic vs. aleatoric uncertainty distinction

**When to Use:**
- Default calibration for all black-box LLM deployments
- Agent confidence scoring for routing decisions
- Quality gates before executing high-stakes actions
- When logit access is unavailable (GPT-4, Claude API)

**When NOT to Use:**
- When logits ARE available (temperature scaling is cheaper and faster)
- Time-critical single-response scenarios where latency of N calls is unacceptable
- Tasks where model always gives identical answers (consistency is uninformative)

**Tags:** #calibration #black-box #self-consistency #confidence #production

---

### AB-calibration-NOTE-0002: RLHF Destroys Calibration

**This answers:** "Why are instruction-tuned LLMs systematically overconfident?"

**Content:**
- Pre-trained LLMs have reasonably calibrated conditional probabilities
- RLHF optimization targets human preference (helpful, harmless, honest) — but "helpful" rewards confident, fluent responses
- Result: Both logit distributions AND verbalized confidence degrade after RLHF
- "Taming Overconfidence" (NeurIPS 2024): Proposes PPO-M (reward model calibration) and PPO-C (reward score calibration)
- "Resisting Correction" (Dec 2025): RLHF creates specific conversational overconfidence bias (ρ=0.036)
- ATS (ICLR 2024): Can partially recover calibration post-RLHF with per-token temperature adjustment
- Implication: EVERY agent built on instruction-tuned models inherits structural overconfidence
- This is not a bug — it's an emergent property of training for conversational fluency

**Classification:** EVIDENCED
- Multiple independent studies (NeurIPS, ICLR, arXiv) confirm the same causal mechanism

**Confidence:** HIGH (90%)

**Sources:**
- Wang et al. "Taming Overconfidence" NeurIPS 2024
- ATS ICLR 2024 Workshop
- "Resisting Correction" arxiv Dec 2025
- Leng et al. 2024

**Failure Modes:**
- Fix at training level (PPO-M/PPO-C) requires model training access
- Post-hoc fixes may not fully recover pre-RLHF calibration quality
- Models continue to evolve — fix for GPT-4 may not apply to GPT-5

**When to Use (this knowledge):**
- Explaining to customers WHY their agents are overconfident
- Justifying external calibration layer (agents CAN'T self-assess accurately)
- Sales pitch: "The training that makes your AI helpful is the same training that makes it overconfident"

**When NOT to Use:**
- Don't claim RLHF always makes models worse overall — it improves usability
- Don't suggest avoiding RLHF — suggest adding calibration ON TOP

**Tags:** #RLHF #overconfidence #root-cause #training #structural

---

### AB-calibration-NOTE-0003: Conformal Prediction for Agent Guarantees

**This answers:** "Can you provide statistical guarantees for AI agent outputs?"

**Content:**
- Conformal Prediction (CP) is a distribution-free framework that produces prediction sets with guaranteed coverage
- If you want 90% coverage: CP guarantees that 90% of prediction sets contain the correct answer
- ConU (NeurIPS 2024): Integrates self-consistency into CP for LLMs — correctness-aligned uncertainty measure
- TECP (2025): Uses token-entropy as nonconformity score — works at token level
- CPQ (2025): Handles open-ended generation via missing mass estimation
- CP for LLM-as-a-Judge (EMNLP 2025): Provides interval evaluations instead of point estimates
- Key advantage: NO distributional assumptions needed (unlike Bayesian methods)
- Key constraint: Requires exchangeable calibration data from target distribution

**Classification:** EVIDENCED
- Strong theoretical foundations (decades of CP research)
- LLM applications are new but from top venues (NeurIPS, EMNLP, ICML)

**Confidence:** HIGH (82%)

**Sources:**
- ConU NeurIPS 2024
- TECP MDPI Mathematics 2025
- CPQ arxiv 2025
- EMNLP 2025 interval evaluations
- ICML 2025 "Prune 'n Predict"

**Failure Modes:**
- Requires calibration set from target distribution — cold start problem for novel domains
- Prediction sets can be too large to be useful (low informativeness)
- Assumes exchangeability — violated under distribution shift
- Computational cost scales with calibration set size
- Not yet integrated into any agent framework

**When to Use:**
- High-stakes agent decisions (financial, medical, legal)
- When regulatory compliance requires provable guarantees
- Insurance-facing applications (demonstrable risk bounds)
- Evaluating LLM-as-a-Judge reliability

**When NOT to Use:**
- Rapid prototyping (overhead of building calibration sets)
- Low-stakes tasks where approximate confidence suffices
- Domains without sufficient calibration data
- Real-time applications where prediction set computation is too slow

**Tags:** #conformal-prediction #guarantees #statistical #high-stakes #compliance

---

### AB-calibration-NOTE-0004: Selective Prediction / Abstention

**This answers:** "What if instead of calibrating wrong answers, the agent just says 'I don't know'?"

**Content:**
- Selective prediction: Model chooses to answer only when confident, abstains otherwise
- SelectLLM (ICLR 2025): Integrates selective prediction into fine-tuning, optimizes coverage-risk tradeoff
- "Know Your Limits" survey (TACL 2025): Comprehensive taxonomy of abstention methods
  - Reliable Accuracy (R-Acc): Of answers given, how many are correct?
  - Effective Reliability (ER): Balance between reliability and coverage
  - Abstain ECE: Modified ECE including abstention
- Direct application to agent routing: Uncertain → escalate to human or more capable model
- Amazon's cascading ensembles (2024): Route by confidence — high confidence → small cheap model, low confidence → large expensive model
- This is the MOST pragmatic approach for production agent systems

**Classification:** EVIDENCED
- ICLR 2025, TACL 2025, Amazon Science — strong venue quality
- Directly maps to existing agent routing patterns

**Confidence:** HIGH (85%)

**Sources:**
- SelectLLM ICLR 2025
- "Know Your Limits" TACL 2025
- Amazon Science cascading ensembles 2024

**Failure Modes:**
- Over-abstention: System refuses too many queries, frustrating users
- Under-abstention: Threshold too permissive, still outputs bad answers
- Threshold tuning requires labeled validation data
- Different tasks need different thresholds
- "I don't know" is not always acceptable (customer-facing agents)

**When to Use:**
- Multi-agent routing: Route uncertain queries to specialized agents
- Human-in-the-loop: Trigger human review for low-confidence outputs
- Cost optimization: Route by confidence to cheaper models when confident
- Safety-critical applications: Better to not answer than answer wrong

**When NOT to Use:**
- When coverage is paramount (must always give an answer)
- When abstention labels are ambiguous
- Without clear escalation paths for abstained queries

**Tags:** #selective-prediction #abstention #routing #pragmatic #production

---

### AB-calibration-NOTE-0005: The Black-Box Constraint

**This answers:** "Why can't we just use temperature scaling on GPT-4?"

**Content:**
- Temperature scaling (Guo et al. 2017) is the most cited calibration technique
- Requires logit access: Adjust softmax(z/T) where z = logits
- Production reality in 2026:
  - GPT-4/4o: Top-5 logprobs only (since late 2023) — insufficient for full calibration
  - Claude (Anthropic): No logprob access via API
  - Gemini: Partial logprob access
- "A Survey of Calibration Process for Black-Box LLMs" (Dec 2024): First systematic review
- Two approaches for black-box:
  1. Proxy models: Use open-source model as calibration proxy → transform black-box to gray-box
  2. Input-output methods: Operate solely on API responses (consistency, verbalized, metamorphic)
- "Thermometer" (MIT, ICML 2024): Instance-dependent temperature — but still requires logits
- The gap between academic calibration research and production deployment is THE defining challenge

**Classification:** EVIDENCED
- Directly verifiable from API documentation
- Survey from Amazon/Penn State confirms gap

**Confidence:** VERY HIGH (92%)

**Sources:**
- OpenAI API documentation
- Anthropic API documentation
- Xie et al. "Calibration Process for Black-Box LLMs" Dec 2024
- Guo et al. ICML 2017

**Failure Modes:**
- Proxy model approach: Proxy may not mirror black-box model's calibration
- API changes: Providers may add/remove logprob access
- Gray-box methods may violate provider ToS

**When to Use (this knowledge):**
- Explaining to technical audiences why standard ML calibration doesn't apply
- Scoping calibration projects: "Which methods are viable for your model stack?"
- Architectural decisions: Which calibration tier for which LLM provider?

**Tags:** #black-box #api-constraint #temperature-scaling #production #architecture

---

### AB-calibration-NOTE-0006: DINCO — Fixing Suggestibility Bias

**This answers:** "Why are LLMs overconfident about things they know nothing about?"

**Content:**
- DINCO (Distractor-Normalized Coherence, Wang et al. 2025, ICLR 2026 submission)
- Hypothesis: LLM overconfidence stems from heightened suggestibility — when facing claims it has little info about, it still agrees
- Validated: More suggestibility on lower-accuracy claims
- Method: Have LLM verbalize confidence independently across self-generated distractors
  - Generate alternative (distractor) claims
  - Ask LLM to assess confidence in each
  - Normalize target confidence against distractor confidence
  - High confidence in target BUT ALSO in distractors → actually low confidence (suggestible)
  - High confidence in target, LOW in distractors → genuinely confident
- Independent prompting (asking separately) >> Joint prompting (asking together) for calibration
- Addresses a ROOT CAUSE of overconfidence, not just a symptom

**Classification:** EVIDENCED (paper exists, ICLR submission with empirical validation)

**Confidence:** MEDIUM-HIGH (78%)
- Paper is a preprint/submission, not yet peer-reviewed at time of writing
- Method is clever but implementation complexity is non-trivial

**Sources:**
- Wang et al. "Calibrating Verbalized Confidence with Self-Generated Distractors" arXiv:2509.25532

**Failure Modes:**
- Distractor quality matters — bad distractors → bad normalization
- Adds significant latency (multiple independent confidence assessments)
- Cost: Multiple LLM calls per confidence estimate
- May not generalize across all task types

**When to Use:**
- When verbalized confidence is the only option
- When understanding WHY the model is confident matters
- For debugging overconfident agent behaviors
- Research and development of calibration systems

**When NOT to Use:**
- Production latency-sensitive applications (too many calls)
- When consistency-based methods are available and sufficient
- Budget-constrained deployments

**Tags:** #DINCO #suggestibility #verbalized-confidence #root-cause #research

---

## PLAYBOOKS

### PLAYBOOK #1: Implementing Three-Tier Agent Calibration

**Trigger:** Deploying AI agents that need reliable confidence scores for routing, safety, or compliance

**Goal:** Production-ready calibration infrastructure covering all agent outputs with appropriate method per risk level

**Inputs:**
- Agent stack (which LLMs, which frameworks)
- API access level per model (logits? logprobs? black-box only?)
- Risk taxonomy (which agent decisions are high/medium/low stakes)
- Budget for calibration overhead per query

**Steps:**

1. **Audit Agent Stack (1 day)**
   - Catalog all LLMs in use: model, provider, API access level
   - Map: Black-box (Claude, GPT-4 API) vs. Gray-box (OpenAI logprobs) vs. White-box (self-hosted)
   - For each: What calibration methods are viable?
   - Output: API Access Matrix

2. **Classify Decision Risk (1 day)**
   - For each agent task/decision: What's the cost of being wrong AND confident?
   - Risk tiers:
     - LOW: Information retrieval, summarization (wrong answer is annoying, not harmful)
     - MEDIUM: Recommendations, analysis (wrong answer leads to bad decisions)
     - HIGH: Actions (financial transactions, code execution, legal advice)
   - Output: Risk Classification Matrix

3. **Implement Tier 1: Consistency-Based Default (1 week)**
   - For ALL agent outputs:
     - Sample 3-5 responses with temperature 0.7
     - Semantic clustering (embed + cluster)
     - Confidence = largest cluster frequency / N
   - Implementation: Wrapper function around LLM calls
   - Log: Every confidence score alongside output
   - Cost budget: ~$0.005-0.015/check
   - Validate: Compare consistency confidence against held-out correctness labels

4. **Implement Tier 2: Conformal Prediction for HIGH Risk (2-3 weeks)**
   - For HIGH-risk agent decisions:
     - Build calibration set: 200-500 labeled examples per domain
     - Implement split conformal prediction using Tier 1 confidence as nonconformity score
     - Output: Prediction set instead of single answer, with coverage guarantee
   - Integration: Agent returns prediction set + coverage level
   - Human review for sets larger than threshold

5. **Implement Tier 3: Selective Prediction / Routing (1 week)**
   - Set confidence thresholds per risk tier:
     - LOW risk: Abstain below 30% confidence
     - MEDIUM risk: Abstain below 60% confidence
     - HIGH risk: Abstain below 80% confidence
   - Routing:
     - Below threshold → Escalate to human reviewer
     - OR → Route to more capable model (cost-aware cascading)
   - Track: Abstention rate, human override rate, escalation cost

6. **Monitor and Recalibrate (Ongoing)**
   - Weekly: Check ECE across production outputs (requires sampling + labeling)
   - Monthly: Recalibrate conformal prediction sets with fresh data
   - Alert: If abstention rate exceeds 30% → model may be encountering distribution shift
   - Dashboard: Confidence distribution, ECE trend, abstention rate, human override rate

**Outputs:**
- Calibration wrapper library (pip-installable)
- Risk-classified agent inventory
- Monitoring dashboard
- Per-agent ECE scores

**Acceptance Criteria:**
- Tier 1 deployed on 100% of agent outputs
- Tier 2 deployed on all HIGH-risk decisions
- ECE < 15% (down from ~40% uncalibrated)
- Abstention rate between 5-20% (not too conservative, not too permissive)

**Timeline:** 4-6 weeks for full implementation

---

### PLAYBOOK #2: Calibration Audit for Existing Agent Deployment

**Trigger:** Customer has agents in production without calibration, wants to understand their trust gap

**Goal:** Quantified assessment of current calibration quality + roadmap for improvement

**Inputs:**
- Access to agent system (logs, outputs, or live API)
- Sample of 200+ agent interactions with known correct answers (or ability to label them)
- Agent architecture documentation

**Steps:**

1. **Collect Sample (2-3 days)**
   - Extract 500+ recent agent interactions
   - Label correctness (binary or graded)
   - Extract any existing confidence signals (verbalized, logprob-based, or none)

2. **Measure Baseline Calibration (1 day)**
   - Calculate ECE (15-bin) and MCE
   - Generate reliability diagram (predicted confidence vs. actual accuracy)
   - Measure overconfidence ratio (% of cases where confidence > accuracy)
   - If no confidence exists: Run consistency-based estimation retroactively

3. **Identify Failure Patterns (1 day)**
   - Where is miscalibration worst? (Which topics? Which query types?)
   - Is the model consistently overconfident or inconsistently calibrated?
   - Compare across different agent roles if multi-agent

4. **Cost-of-Miscalibration Analysis (1 day)**
   - Map miscalibrated decisions to business impact
   - Calculate: How many wrong-and-confident outputs per month?
   - Estimate: Cost per undetected error (customer impact, legal, reputation)

5. **Recommend Calibration Stack (1 day)**
   - Based on findings: Which tier(s) from Playbook #1 are needed?
   - Quick wins: What can be fixed in 1 week?
   - Structural improvements: What needs 1-3 months?
   - Output: Calibration roadmap with timeline and cost estimates

**Outputs:**
- Calibration Audit Report (10-15 pages)
- Reliability diagrams per agent
- ECE/MCE metrics
- Cost-of-miscalibration estimate
- Improvement roadmap

**Timeline:** 1-2 weeks

**Who This Is For:**
- CTOs deploying agents without confidence infrastructure
- AI product teams pre-launch
- Compliance teams preparing for EU AI Act
- Insurance assessment for agent deployments

---

## ASSET PACK COMPLETE

**Summary:**
- **6 Atomic Notes** (Consistency Calibration, RLHF Destruction, Conformal Prediction, Selective Prediction, Black-Box Constraint, DINCO)
- **2 Playbooks** (Three-Tier Implementation, Calibration Audit)

**High-Confidence Assets (Ready to Use):**
- AB-calibration-NOTE-0001 (Consistency-Based) ✅
- AB-calibration-NOTE-0002 (RLHF Destroys Calibration) ✅
- AB-calibration-NOTE-0004 (Selective Prediction) ✅
- AB-calibration-NOTE-0005 (Black-Box Constraint) ✅
- Playbook #1 (Three-Tier Implementation) ✅
- Playbook #2 (Calibration Audit) ✅

**Medium-Confidence Assets (Use with Caveats):**
- AB-calibration-NOTE-0003 (Conformal Prediction) — Strong theory, nascent LLM practice
- AB-calibration-NOTE-0006 (DINCO) — Preprint, not yet peer-reviewed

---

*End of Asset Pack*
