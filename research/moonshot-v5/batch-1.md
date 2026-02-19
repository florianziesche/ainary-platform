# MOONSHOT v5 — BATCH 1: Deep Review of AR-020-v4
Generated: 2026-02-19T10:48 | 15 RAG queries executed

---

## 🔴 ROLLE 1: RED TEAM

**Beipackzettel:** Sucht interne Widersprüche, logische Sprünge, Framing Bias, und subtile Fehler die 15 oberflächliche Agents übersehen haben. Prüft gegen CRTs und Volltext-Papers via RAG.

### Finding RT-1: MAJOR — Section 10.1 Complacency Paradox Math Is Misleading

**Problem:** Section 10.1 presents a "paradox" calculation:
- Calibrated: 95% accuracy × 20% human verification → catches 5% × 80% = 4% of errors  
- Uncalibrated: 70% accuracy × 80% human verification → catches 30% × 20% = 6%

This math is **internally inconsistent**. The "catches X% of errors" framing conflates error rate with catch rate. The calibrated system has 5% errors and catches 80% of the 20% it reviews = 0.8% total caught. The uncalibrated system has 30% errors but catches only 20% of the 80% it reviews = 4.8% caught. The actual numbers are different from what's stated, but the qualitative point (better calibration → less vigilance → potentially more missed errors) is valid.

**However:** The bigger issue is the hidden assumption that human verification rates are exogenous. In reality, calibration CHANGES human verification rates — that's the whole point of Tier 3 selective prediction. A well-designed system routes LOW-confidence to humans (high verification rate) and HIGH-confidence away (low verification rate). The paradox only holds if humans randomly verify.

**Fix:** Reframe the paradox as: "Calibration is beneficial only when coupled with intelligent routing. Blanket trust in high-confidence outputs creates complacency risk." Add that Tier 3 selective prediction is the mitigation.

**RAG:** Queried "Parasuraman Manzey automation complacency vigilance" — paper not in dossier full-text corpus (it's from 2010, outside LLM trust scope). The 20-50% vigilance drop claim is **not verifiable from our corpus** and should be labeled as "external source, not independently verified."

### Finding RT-2: MAJOR — Section 5 Correlation Formula Incomplete

**Problem:** Section 5 gives the two-agent correlation formula:
> P(both correct) = p_1 * p_2 + rho * sqrt(p_1(1-p_1) * p_2(1-p_2))

This is correct for Bernoulli variables (the standard covariance-to-joint-probability conversion). But the report then makes a leap: "rho > 0 (typical for same-model agents): multiplicative is pessimistic for 'all correct'."

This is mathematically correct but **the report never addresses the more dangerous implication**: rho > 0 also means P(both WRONG) > (1-p_1)(1-p_2). The report mentions "bimodal failure risk" in Exhibit 3's notes but doesn't integrate this into the architecture recommendations. Section 6 (Three-Tier Architecture) doesn't mention correlation-adjusted thresholds at all.

**Internal contradiction:** Section 5 warns about correlated failures. Section 6 recommends fixed thresholds (30%/60%/80%) that assume independent errors. Section 7's Step 5 says "set thresholds" without mentioning correlation. The architecture doesn't practice what the theory preaches.

**Fix:** Add a note in Section 6/Tier 3 that thresholds should be higher for same-model multi-agent chains due to correlated failures.

### Finding RT-3: MINOR — Executive Summary Overstates "First Practical Architecture"

**Problem:** The Exec Summary says "the first practical architecture for agent confidence calibration." But Section 2 Family 7 acknowledges HTC/GAC already provide architectures (from January 2026). The report's Three-Tier Architecture is a synthesis/recommendation, not the "first" architecture. 

**Fix:** Change to "a practical architecture synthesizing current methods" or "the first production-oriented integration guide."

### Finding RT-4: MINOR — Framing Bias in ROI Section

**Problem:** Section 4.1 ROI table shows legal research at 99x ROI and customer support at 250x ROI, but content moderation at -19x. The two positive examples use "author estimates" for damage/error that are extremely favorable. $755K damage per legal error seems high (Mata v. Avianca resulted in $5K sanctions, not $755K). The ROI case may be overstated.

**Fix:** Label the legal damage figure source explicitly. $755K seems to include opportunity cost/reputational damage beyond direct sanctions — if so, state that. If it's an estimate, say "author estimate including reputational damage."

### Finding RT-5: MINOR — Section 1.1 Evidence Chain Mixes Timeframes

**Problem:** The evidence chain for "RLHF destroys calibration" mixes NeurIPS 2024, Dec 2025, ICLR 2024, and ICML 2025. The ICML 2025 paper ("calibratable vs non-calibratable regimes") actually WEAKENS the blanket claim. The report acknowledges this but the Section 1.1 title "RLHF Systematically Destroys Calibration" still overstates. Per CT-001 (conf: 88%), it's regime-dependent.

**Fix:** Change title to "RLHF Systematically Damages Calibration" (not "destroys").

### CRT Check
- CT-001 (RLHF regime-dependent): Report acknowledges but title overstates → minor tension
- CT-003 (consistency can't detect systematic bias): Report covers this well in §2.8
- CT-013 (multiplicative underestimates compound confidence): Report covers but doesn't integrate into architecture
- CT-011 (trust calibration alone insufficient for decision-making): Section 10 covers complacency but doesn't reference this CRT directly

### RAG Queries (5):
1. "Parasuraman Manzey automation complacency vigilance" → not in corpus
2. "multiplicative confidence propagation correlated agents" → no direct paper match
3. "Wang NeurIPS 2024 taming overconfidence RLHF reward" → found Influences on LLM Calibration paper, not the Wang paper itself
4. "resisting correction conversational overconfidence bias rho 0.036" → not in corpus
5. "adversarial attack verbal confidence robustness" → found guard model paper tangentially

### NEUE CRTs:
- **CT-028 (proposed, conf: 80%):** Fixed calibration thresholds (30%/60%/80%) are inappropriate for correlated multi-agent chains — thresholds should be adjusted upward proportional to inter-agent correlation. Source: RT-2 analysis of Section 5 vs Section 6 inconsistency.

---

## 🔬 ROLLE 2: EMPIRICIST

**Beipackzettel:** Prüft JEDE Zahl im Report gegen Papers via RAG. Identifiziert nicht-verifizierbare Claims. Designed Verifikations-Experimente.

### Finding EM-1: CRITICAL — "84% overconfidence" Source Cannot Be Verified in Corpus

**Problem:** The Key Numbers table says "LLM scenarios showing overconfidence | 84% | PMC study, 9 models, 351 scenarios | 90% (5/5 prompts)."

RAG query for this specific claim returned NO matching paper in the full-text corpus. The PMC study (paper 8d978805 — "Enhancing Healthcare LLM Trust with Atypical Presentations Recalibration") discusses overconfidence but its abstract doesn't mention "84%" or "351 scenarios" or "9 models." The referenced "PMC 2024" study with 13 datasets appears to be a DIFFERENT paper (PMC12249208, referenced as [8]) that may not be in our downloaded corpus.

**Status:** The 84% figure, 9 models, 351 scenarios, and 13 datasets are attributed to a PMC study but **we cannot verify the exact numbers from our RAG corpus**. The paper may use different phrasing or the numbers may be from supplementary materials we don't have.

**Recommendation:** Either (a) access PMC12249208 full text to verify, or (b) label as "reported in [8], not independently verified by this review."

### Finding EM-2: MAJOR — "$0.005 per check" vs "$0.0005 per check" Contradiction Persists

**Problem:** The report now shows BOTH numbers:
- Key Numbers table: "~$0.005" 
- Exhibit 1: "$0.0005-0.015"
- Exhibit 2: "$0.0005-0.005"

v4 partially fixed this by adding ranges, but the Key Numbers table still shows the single point estimate "$0.005" which CX-005 flagged as ~10x too high for Haiku pricing. The range in Exhibit 1/2 is correct; the Key Numbers table is the stale artifact.

**Fix:** Change Key Numbers table to "~$0.0005-$0.015 (model-dependent)" to match the body text.

### Finding EM-3: MAJOR — "42.9% ECE reduction" (BaseCal) Not Verifiable

**Problem:** Section 2 Family 7 says "BaseCal achieves 42.9% average ECE reduction." RAG query returned no BaseCal paper in our corpus (it's arXiv:2601.03042, January 2026 — likely too new for our download). This number is cited from a preprint abstract and cannot be independently verified from our full-text papers.

**Status:** Label as "per preprint abstract, not peer-reviewed, not independently verified."

### Finding EM-4: MINOR — "46% calibration error reduction" (Amazon Ensembles) Source Vague

**Problem:** Section 2 Family 5: "Amazon's cascading ensembles reduced calibration error by 46% on credit-risk classification." The source is [17] "Amazon Science 2024." RAG returned no Amazon Science paper in our corpus. This appears to be an industry blog post/whitepaper, not peer-reviewed.

**Status:** Should note "industry publication, not peer-reviewed."

### Finding EM-5: MINOR — "rho = 0.036" (Resisting Correction) Not in Corpus

**Problem:** Section 1.1 cites "Resisting Correction" (Dec 2025) with rho = 0.036 for conversational overconfidence bias. RAG query returned no match. This paper is not in our downloaded corpus.

**Status:** Number is unverifiable from our sources. Not critical (it's a small effect size supporting a larger argument), but should be flagged.

### Zahlen-Audit Gesamtergebnis

| Claim | Value | Verifiable from RAG? | Status |
|-------|-------|---------------------|--------|
| 84% overconfidence | 84%, 9 models, 351 scenarios | ❌ PMC paper not in corpus | NEEDS SOURCE ACCESS |
| ECE 27.3% vs 42% | PMC 2024 | ❌ Paper not in corpus | NEEDS SOURCE ACCESS |
| $0.005/check | Budget-CoCoA | ❌ Not in corpus | PARTIALLY FIXED (range added) |
| 42.9% ECE reduction | BaseCal preprint | ❌ Not in corpus | LABEL AS PREPRINT |
| 46% ensemble reduction | Amazon Science | ❌ Not in corpus | LABEL AS INDUSTRY |
| rho = 0.036 | Resisting Correction | ❌ Not in corpus | LOW PRIORITY |
| 0.25% ECE temp scaling | Guo et al. 2017 | ❌ Not in corpus | CLASSIC REFERENCE |
| 20-50% vigilance drop | Parasuraman & Manzey 2010 | ❌ Not in corpus | EXTERNAL FIELD |
| Guard model miscalibration | 9 models, 12 benchmarks | ✅ e2f0bc45 abstract confirms | VERIFIED |
| APRICOT black-box | Single auxiliary model | ✅ 3c45d3c1 abstract confirms | VERIFIED |
| Fine-tuning > prompting | ~1000 graded examples | ✅ b3bf4ca8 abstract confirms | VERIFIED |
| Auxiliary > internal probs | 12 LLMs, 4 prompt styles | ✅ 3ae1d0fd abstract confirms | VERIFIED |

**Key insight:** Of the 6 "Key Numbers" in the executive summary, NONE are directly verifiable from our downloaded paper corpus. The 4 verified claims are supporting evidence, not headline numbers. This is a structural weakness — the report's most prominent claims rely on papers we haven't fully downloaded.

### Experiment Design 1: Cross-Domain ECE Validation ($2.50)

**Hypothesis:** Consistency-based calibration outperforms verbalized confidence across domains (not just biomedical QA).

**Protocol:**
1. Sample 50 questions each from: TriviaQA (factual), HumanEval (code), LegalBench (legal), MMLU-Medical (medical baseline)
2. For each question, collect: (a) verbalized confidence (single call), (b) 3-sample consistency score
3. Use GPT-4o-mini (~$0.15/1M input tokens)
4. Ground truth from benchmark answer keys
5. Calculate ECE (15 bins) per domain per method

**Cost:** 200 questions × (1 verbalized + 3 consistency) = 800 API calls × ~200 tokens × $0.15/1M ≈ $0.024. Add 200 ground-truth lookups. Total: **~$0.05**.

**Value:** Would validate or invalidate the report's central recommendation across 4 domains. If consistency loses in any domain, the "consistency > verbalized" ranking needs domain caveats.

### Experiment Design 2: Correlation Measurement in Agent Chains ($2.50)

**Hypothesis:** Same-model agent chains exhibit positive error correlation (rho > 0.1).

**Protocol:**
1. 100 MMLU questions, 5 domains
2. 3-agent chain: Agent A (answer question), Agent B (summarize A's answer), Agent C (verify B's summary against original question)
3. Run all 3 agents with GPT-4o-mini, record correctness at each step
4. Calculate pairwise error correlation (phi coefficient for binary correct/incorrect)
5. Compare: same-model chain vs. mixed-model chain (GPT-4o-mini → Claude-Haiku → Gemini-Flash)

**Cost:** 100 questions × 6 agents (3 same + 3 mixed) × ~500 tokens ≈ $0.045. Total: **~$0.05**.

**Value:** Would produce the FIRST empirical measurement of rho in agent chains. Directly fills the "UNSOLVED" gap identified in Section 5. Even a small study (n=100) would replace Exhibit 3's "illustrative" label with actual data.

### RAG Queries (6):
1. "self-consistency ECE 27.3% 42% biomedical 13 datasets" → no direct match
2. "Budget-CoCoA cost per check 0.005 three API calls" → no match (low score 0.242)
3. "BaseCal 42.9% ECE reduction RLHF hidden states" → no match
4. "APRICOT auxiliary prediction confidence targets" → ✅ found paper 3c45d3c1 (score 0.675)
5. "guard model overconfident jailbreak miscalibration" → ✅ found paper e2f0bc45 (score 0.503)
6. "fine-tuning 1000 graded examples calibration" → ✅ found paper b3bf4ca8 (score 0.512)

### NEUE CRTs:
- **CT-029 (proposed, conf: 75%):** The 6 "Key Numbers" in AR-020's executive summary all originate from papers NOT in the RAG corpus — creating an unverifiable citation chain. Future reports must ensure headline numbers come from papers with full-text in the verification corpus. Source: EM audit of all key claims.

---

## 📐 ROLLE 3: FORMALIST

**Beipackzettel:** Prüft mathematische Aussagen auf Korrektheit, fehlende Caveats, und ob "proofs" tatsächlich Beweise sind.

### Finding FM-1: MAJOR — "Provably Wrong" Is Not Proven in the Report

**Problem:** The Executive Summary claims: "The standard multiplicative confidence model (C = product of individual confidences) is provably wrong under positive correlation."

Section 5 provides the formula: P(both correct) = p_1 * p_2 + rho * sqrt(p_1(1-p_1) * p_2(1-p_2))

This is a **definition** of the correlation structure for Bernoulli variables, not a proof. The statement "multiplicative is wrong under positive correlation" follows trivially from rho > 0 ⟹ P(joint) > P(product), which is just the definition of positive correlation.

**The problem:** The report says "provably wrong" as if this is a deep result. It's actually a tautology: "If errors are correlated, then assuming independence gives the wrong answer." This is like saying "assuming the earth is flat is provably wrong if the earth is round."

What would be a real proof: showing that rho > 0 in ACTUAL multi-agent systems (empirically), or proving that same-model agents MUST have rho > 0 (theoretically from shared training data). The report does neither — it assumes rho > 0 based on intuition (shared priors, shared context).

**Fix:** Replace "provably wrong" with "wrong under positive correlation, which we expect based on shared training data and context but have not empirically measured." Or keep "provably wrong" but add: "The proof is trivial given the assumption rho > 0; the open question is whether this assumption holds in practice."

### Finding FM-2: MAJOR — ECE Bounds in Section 2.8 Are Author Estimates, Not Formal Bounds

**Problem:** Section 2.8 presents:
> ECE_consistency ≈ ECE_aleatoric + ECE_systematic_bias
> ECE_aleatoric shrinks as O(1/√N)

This is labeled "author estimate, not peer-reviewed" which is honest. But calling it a "Theoretical bound" in the heading while simultaneously disclaiming it is contradictory. 

**Mathematical issues:**
1. ECE is not decomposable into aleatoric + systematic components in general. ECE measures binned calibration error, not uncertainty decomposition. The decomposition ECE = f(epistemic) + f(systematic) is a conceptual analogy, not a mathematical identity.
2. The O(1/√N) convergence for aleatoric component assumes i.i.d. sampling, which Section 2 Family 2 explicitly notes may not hold (model may answer incorrectly the same way).
3. The "60-70% of miscalibration is epistemic" claim has no derivation, no empirical support, and no source. It's presented as if it follows from the bound, but it doesn't.

**Fix:** Rename "Formal Bounds" to "Conceptual Model" or "Heuristic Analysis." Keep the insight (consistency reduces epistemic but not systematic error) but don't dress it as formal mathematics.

### Finding FM-3: MINOR — Conformal Prediction n ≥ 1/α Is Oversimplified

**Problem:** Section 2 Family 4 says "minimum n >= 1/alpha ≈ 200 examples" for 90% coverage at 95% confidence. The actual requirement from Vovk et al. (2005) is more nuanced:
- For marginal coverage: n ≥ 1/(1-α) - 1 (so for α=0.1: n ≥ 9). This gives valid coverage but potentially large prediction sets.
- For meaningful prediction sets with desired width: sample size depends on the complexity of the score function.
- The 200 figure likely comes from practical recommendations for stable calibration, not the theoretical minimum.

**Fix:** Clarify: "Theoretical minimum for valid coverage is ~10 examples, but practical recommendations suggest 200-500 for useful prediction set sizes."

### Finding FM-4: MINOR — Two-Agent Formula Doesn't Scale to N Agents

**Problem:** Section 5 gives the two-agent formula but then shows a table for 3, 5, 10 agents. The n-agent version of the correlation formula requires specifying the full joint distribution, not just pairwise rho. For n agents with pairwise correlation rho, the joint probability depends on the specific copula or multivariate distribution assumed.

The report implicitly assumes a common correlation model where all pairs have the same rho, but doesn't state this. For heterogeneous chains (different models at each step), rho varies per pair, and the formula becomes significantly more complex.

**Fix:** Add caveat: "The pairwise formula extends to n agents only under simplifying assumptions (exchangeable errors, common correlation). Real multi-agent systems have heterogeneous correlation structures."

### Finding FM-5: MINOR — "Best ECE on GAIA" (HTC/GAC) Metric Confusion

**Problem:** Section 2 Family 7 says HTC/GAC "achieves best ECE on out-of-domain GAIA benchmark." ECE is a scalar metric (lower = better). "Best ECE" is ambiguous — lowest ECE? Best calibrated? The statement should specify direction and magnitude.

**Fix:** "Achieves lowest ECE on out-of-domain GAIA benchmark (X.X% vs Y.Y% for baseline)" — if numbers available from preprint.

### RAG Queries (5):
1. "conformal prediction coverage guarantee compositionality pipeline" → found APRICOT + Trust or Escalate papers tangentially, no direct CP composition results
2. "HTC holistic trajectory calibration general agent calibrator GAIA" → found STeCa paper (trajectory calibration), not HTC directly
3. "temperature scaling ECE 0.25% vision models Guo" → not in corpus (Guo 2017 predates LLM focus)
4. "SAUP situational awareness uncertainty propagation" → found SAGIN paper (different SAUP), not the ACL 2025 paper
5. "multiplicative confidence propagation correlated agents proof" → no formal proof in corpus

### Critical RAG Observation

The RAG corpus contains 30 papers focused on LLM trust calibration, but **key referenced papers are missing**:
- PMC biomedical study (the source of the report's central 27.3% vs 42% claim)
- Wang et al. NeurIPS 2024 ("Taming Overconfidence")
- BaseCal (arXiv:2601.03042)
- HTC (arXiv:2601.15778)
- SAUP (ACL 2025)
- Guo et al. 2017

This means the report's most important mathematical and empirical claims CANNOT be verified against full-text sources in our current pipeline. The pipeline's 30 papers are mostly about human-AI trust interaction, not calibration methodology.

### NEUE CRTs:
- **CT-030 (proposed, conf: 85%):** The decomposition ECE = ECE_aleatoric + ECE_systematic is a conceptual analogy, not a mathematical identity — ECE is not formally decomposable into epistemic and aleatoric components. Source: FM-2 analysis.
- **CT-031 (proposed, conf: 90%):** "Provably wrong under positive correlation" for multiplicative confidence is a tautology (follows from the definition of correlation), not a substantive proof — the substantive question is whether rho > 0 empirically. Source: FM-1 analysis.

---

## SUMMARY TABLE

| ID | Severity | Role | Finding | Action Required |
|----|----------|------|---------|-----------------|
| RT-1 | MAJOR | Red Team | Complacency paradox math misleading; doesn't account for intelligent routing | Reframe with Tier 3 context |
| RT-2 | MAJOR | Red Team | Section 5 correlation theory not integrated into Section 6 architecture | Add correlation-adjusted thresholds |
| RT-3 | MINOR | Red Team | "First practical architecture" overstated | Soften language |
| RT-4 | MINOR | Red Team | $755K legal damage figure unsourced | Label as author estimate |
| RT-5 | MINOR | Red Team | "Destroys" calibration overstates regime-dependent finding | Change to "Damages" |
| EM-1 | CRITICAL | Empiricist | 84% overconfidence figure unverifiable from corpus | Access PMC12249208 or relabel |
| EM-2 | MAJOR | Empiricist | $0.005 in Key Numbers table contradicts body text ranges | Update table to show range |
| EM-3 | MAJOR | Empiricist | 42.9% BaseCal ECE reduction unverifiable | Label as preprint-only |
| EM-4 | MINOR | Empiricist | 46% Amazon ensemble reduction unverifiable | Label as industry source |
| EM-5 | MINOR | Empiricist | rho=0.036 unverifiable | Low priority |
| FM-1 | MAJOR | Formalist | "Provably wrong" is tautological, not a proof | Reframe or add empirical rho |
| FM-2 | MAJOR | Formalist | Section 2.8 "bounds" are conceptual, not formal | Rename section |
| FM-3 | MINOR | Formalist | CP n≥200 oversimplified | Add theoretical vs practical distinction |
| FM-4 | MINOR | Formalist | Two-agent formula doesn't scale without distributional assumptions | Add caveat |
| FM-5 | MINOR | Formalist | "Best ECE on GAIA" ambiguous | Specify direction and magnitude |

**Totals:** 1 CRITICAL, 6 MAJOR, 8 MINOR

### NEW CRTs PROPOSED (all roles):
| ID | Claim | Confidence | Source |
|----|-------|------------|--------|
| CT-028 | Fixed thresholds inappropriate for correlated multi-agent chains | 80% | RT-2 |
| CT-029 | Headline numbers rely on papers outside verification corpus — structural vulnerability | 75% | EM audit |
| CT-030 | ECE not formally decomposable into epistemic + aleatoric | 85% | FM-2 |
| CT-031 | "Provably wrong under correlation" is tautological, not substantive | 90% | FM-1 |
