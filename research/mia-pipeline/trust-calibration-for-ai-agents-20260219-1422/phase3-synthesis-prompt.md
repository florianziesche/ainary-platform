You are MIA, synthesizing multiple research sub-reports into one executive report.

## THE REAL QUESTION
Can Ainary create defensible IP in calibration infrastructure that becomes the de facto standard before EU regulations crystallize, thereby capturing market share and regulatory influence?

## WHY NOW
The EU AI Act enforcement begins August 2026, but technical standards won't arrive until 2027-2028 (CT-016). This 12-24 month gap represents a rare window where first-movers can shape both market expectations and regulatory interpretation of 'accuracy metrics' (CT-015).

## SUB-REPORTS (each independently researched — DO NOT add claims not in these reports)
### SQ-1: What specific calibration capabilities do AI agents need that don't exist today, and which gaps represent IP opportunities?

### Answer to: What specific calibration capabilities do AI agents need that don't exist today, and which gaps represent IP opportunities?

**Key Findings:**

- **Finding 1 [E]**: Current calibration methods like temperature scaling require access to model logits, which is not always feasible in production environments [S1]. This represents a gap where new methods that do not require logit access could be developed.

- **Finding 2 [E]**: Multi-step agent calibration is unsolved, as current methods like Conformal Uncertainty (ConU) do not compose well for multi-agent systems [S9]. This indicates an opportunity for developing calibration methods that can handle multi-agent interactions effectively.

- **Finding 3 [E]**: Reinforcement Learning from Human Feedback (RLHF) can damage calibration, with some models being permanently affected while others can recover [S30]. This suggests a need for calibration methods that can either prevent this damage or restore calibration post-RLHF.

- **Finding 4 [E]**: Verbalized confidence is biased and vulnerable to adversarial attacks, with current defense techniques being largely ineffective [S3, S5]. This highlights a need for robust verbal confidence calibration methods.

- **Finding 5 [I]**: The EU AI Act requires accuracy but not calibration, which could lead to regulatory gaps that innovative calibration methods might fill, especially in high-stakes applications [S14].

- **Finding 6 [E]**: Situational Awareness Uncertainty Propagation (SAUP) formalizes intra-chain uncertainty propagation but does not address multi-step calibration [S27]. This suggests a need for methods that can propagate uncertainty across multiple steps in a decision-making process.

**Evidence Quality:**

- **Strongest source**: [S1] provides a foundational understanding of calibration methods and their limitations, making it a critical reference for identifying gaps.
  
- **Weakest point**: [S21] is a preprint and not peer-reviewed, which weakens its reliability as evidence for trajectory calibration methods.

- **What's missing**: There is a lack of detailed exploration into the specific technical limitations of current frameworks like SAUP and HTC in multi-step calibration scenarios.

**So What:** The identified gaps in AI agent calibration, particularly in multi-step scenarios and post-RLHF environments, represent significant IP opportunities. Ainary can focus on developing methods that do not require logit access, can handle multi-agent interactions, and are robust against adversarial attacks, thereby creating defensible technology in a largely unsolved area.

**Claims (for Claim Ledger):**

- Claim 1 | [S1] | E | Admiralty: High | Confidence: High
- Claim 2 | [S9] | E | Admiralty: High | Confidence: High
- Claim 3 | [S30] | E | Admiralty: High | Confidence: High
- Claim 4 | [S3, S5] | E | Admiralty: High | Confidence: High
- Claim 5 | [S14] | I | Admiralty: Medium | Confidence: Medium
- Claim 6 | [S27] | E | Admiralty: High | Confidence: High

### SQ-2: Which enterprise sectors will face EU AI Act compliance pressure first, and what are their calibration readiness levels?

### Answer to: Which enterprise sectors will face EU AI Act compliance pressure first, and what are their calibration readiness levels?

**Key Findings:**

- **Finding 1 [E] [S14]:** The EU AI Act, effective August 2026, mandates compliance with specific requirements such as accuracy and human oversight, which will impact sectors heavily reliant on AI, including healthcare, finance, and hiring. These sectors are likely to face compliance pressure first due to their high-risk nature and the critical role AI plays in their operations.

- **Finding 2 [I] [S8]:** The healthcare sector, specifically in biomedical applications, shows significant calibration challenges, with an Expected Calibration Error (ECE) of 27.3% in consistency and 42% in verbalized confidence. This indicates a readiness gap in meeting the EU AI Act's accuracy requirements, suggesting that healthcare may face substantial compliance challenges.

- **Finding 3 [I] [S19]:** The cost of implementing calibration methods like Budget-CoCoA is relatively low, suggesting that sectors with higher AI integration, such as finance and hiring, might be more prepared to invest in compliance infrastructure. However, the effectiveness of these methods in achieving the required calibration levels remains uncertain.

- **Finding 4 [J]:** Given the lack of direct evidence on sector-specific calibration readiness, it is reasonable to judge that sectors with existing regulatory frameworks and compliance experience, such as finance, may have a head start in preparing for the EU AI Act. However, the specific calibration readiness levels across sectors remain unclear.

**Evidence Quality:**

- **Strongest source:** [S14] provides direct information on the EU AI Act's requirements and timeline, establishing a clear framework for compliance pressure.
  
- **Weakest point:** The lack of direct evidence on sector-specific calibration readiness and enterprise spending on AI compliance infrastructure limits the ability to assess readiness accurately.

- **What's missing:** Detailed industry surveys or reports on AI Act preparedness and specific enterprise spending data on AI compliance infrastructure would provide a clearer picture of sector readiness.

**So What:** The healthcare, finance, and hiring sectors are likely to face the most immediate compliance pressure under the EU AI Act due to their high-risk profiles and reliance on AI. However, the readiness levels, particularly in terms of calibration, are uncertain, with healthcare showing significant challenges. Ainary should prioritize developing solutions for these sectors, focusing on improving calibration and compliance infrastructure to meet the August 2026 deadline.

**Claims (for Claim Ledger):**

- Claim 1 | [S14] | E | The EU AI Act mandates compliance by August 2026, impacting high-risk sectors like healthcare, finance, and hiring.
- Claim 2 | [S8] | I | The healthcare sector shows significant calibration challenges, indicating a readiness gap for EU AI Act compliance.
- Claim 3 | [S19] | I | The cost of calibration methods is low, suggesting potential readiness in sectors with high AI integration.
- Claim 4 | [J] | J | Sectors with existing regulatory frameworks, like finance, may be more prepared for EU AI Act compliance.

### SQ-3: How are competitors (IBM, Microsoft, Google) positioning their calibration offerings, and where are they leaving gaps?

### Answer to: How are competitors (IBM, Microsoft, Google) positioning their calibration offerings, and where are they leaving gaps?

**Key Findings:**

- Finding 1 [E] [S1]: Temperature scaling is a widely recognized method for calibration, requiring access to model logits. This method is foundational in the industry but may not be directly offered as a standalone feature by IBM, Microsoft, or Google, as it requires internal model access.

- Finding 2 [E] [S3]: Budget-CoCoA, a method for measuring agreement through multiple API calls, is a practical approach for calibration but is not explicitly mentioned as a feature in the offerings of IBM, Microsoft, or Google. This suggests a potential gap in providing accessible calibration tools that do not require deep model access.

- Finding 3 [I] [S7]: Reinforcement Learning from Human Feedback (RLHF) can damage calibration by favoring confident responses. This indicates that if IBM, Microsoft, or Google use RLHF in their models, they might face challenges in maintaining calibration, especially if they do not offer specific calibration tools to counteract this effect.

- Finding 4 [E] [S9]: Conformal prediction requires a significant number of examples (200-500) and does not compose well for multi-agent systems. This method is not highlighted in the calibration offerings of IBM, Microsoft, or Google, indicating a gap in providing robust, scalable calibration solutions.

- Finding 5 [I] [S30]: Some models are permanently damaged by RLHF, while others are recoverable. This suggests that IBM, Microsoft, and Google need to carefully manage their model training processes to ensure calibration can be restored, which may not be explicitly addressed in their current offerings.

**Evidence Quality:**

- Strongest source: [S1] provides a foundational understanding of calibration methods like temperature scaling, which is critical for evaluating the offerings of IBM, Microsoft, and Google.

- Weakest point: The lack of direct product announcements or API documentation from IBM, Microsoft, and Google regarding specific calibration features limits the ability to assess their current positioning accurately.

- What's missing: Direct evidence from IBM, Microsoft, and Google about their calibration offerings, such as product announcements or detailed API documentation, is missing. This information would provide a clearer picture of their strategies and any existing gaps.

**So What:** Ainary should consider building standalone calibration infrastructure, as current offerings from IBM, Microsoft, and Google may not adequately address calibration needs, especially in scenarios where auxiliary models outperform native LLM calibration. This approach could fill existing gaps in the market and provide a competitive advantage.

**Claims (for Claim Ledger):**

- Claim 1 | [S1] | E | Temperature scaling is a foundational calibration method requiring logit access.
- Claim 2 | [S3] | E | Budget-CoCoA is a practical calibration method not explicitly offered by IBM, Microsoft, or Google.
- Claim 3 | [S7] | I | RLHF can damage calibration, posing a challenge for IBM, Microsoft, and Google if not addressed.
- Claim 4 | [S9] | E | Conformal prediction's scalability issues indicate a gap in IBM, Microsoft, and Google's offerings.
- Claim 5 | [S30] | I | Models damaged by RLHF highlight the need for careful calibration management by IBM, Microsoft, and Google.

### SQ-4: What is the actual implementation cost and complexity for enterprises to adopt calibration infrastructure?

### Answer to: What is the actual implementation cost and complexity for enterprises to adopt calibration infrastructure?

**Key Findings:**

- Finding 1 [E] [S1]: Implementing temperature scaling, a common calibration method, requires access to model logits, which implies a need for technical expertise in handling neural network outputs. This suggests a moderate level of complexity in integration with existing ML pipelines.
  
- Finding 2 [E] [S19]: The practical cost of using Budget-CoCoA, a calibration method, ranges from $0.0005 to $0.015 per check, depending on the model. This indicates a relatively low operational cost for calibration once the infrastructure is in place.

- Finding 3 [I] [S9]: Conformal prediction for LLMs requires 200-500 examples for effective calibration. This suggests a significant initial data requirement, which could increase the complexity and time needed for implementation.

- Finding 4 [I] [S30]: Some models may be permanently damaged by RLHF, while others are recoverable, indicating that the complexity of calibration can vary significantly depending on the model's prior training and alignment processes.

- Finding 5 [J]: The lack of open-source implementations for some advanced calibration methods like GAC [S21] implies that enterprises may need to invest in custom development or rely on proprietary solutions, increasing both cost and complexity.

**Evidence Quality:**

- Strongest source: [S1] provides a well-established method (temperature scaling) with clear requirements, making it a reliable reference for understanding the technical needs of calibration.

- Weakest point: [S21] discusses a preprint method without open-source implementation, which limits its practical applicability and reliability.

- What's missing: Detailed TCO analyses and specific engineering time estimates for implementing calibration infrastructure in various enterprise contexts are not available.

**So What:** The implementation of calibration infrastructure in enterprises involves moderate complexity due to the need for technical expertise and initial data requirements. While operational costs can be low, the variability in model recoverability and the potential need for custom solutions suggest that enterprises should prepare for a potentially significant initial investment in both time and resources.

**Claims (for Claim Ledger):**

- Claim 1 | [S1] | E | Admiralty | High
- Claim 2 | [S19] | E | Admiralty | Medium
- Claim 3 | [S9] | I | Admiralty | Medium
- Claim 4 | [S30] | I | Admiralty | Medium
- Claim 5 | [S21] | J | Admiralty | Low

### SQ-5: How can Ainary influence the 2027-2028 CEN/CENELEC standards to favor its calibration approach?

### Answer to: How can Ainary influence the 2027-2028 CEN/CENELEC standards to favor its calibration approach?

**Key Findings:**

- **Finding 1 [E] [S14]:** The EU AI Act, which will be enforced starting August 2026, requires AI systems to meet certain standards of 'accuracy' and 'human oversight' but does not explicitly mention 'calibration'. This suggests that influencing standards to include calibration as a requirement could be a strategic move for Ainary.

- **Finding 2 [I] [S1, S8]:** Calibration is a critical component in AI systems for ensuring trustworthiness and reducing overconfidence, as evidenced by the effectiveness of temperature scaling and ECE metrics in neural networks [S1], and the high ECE in biomedical NLP models [S8]. Ainary could leverage these findings to argue for the inclusion of calibration in standards.

- **Finding 3 [E] [S19]:** Budget-CoCoA, a practical method for calibrating LLM confidence scores, is cost-effective, which could be a selling point for its inclusion in standards. The low cost of implementation could appeal to stakeholders concerned with the economic feasibility of new standards.

- **Finding 4 [I] [S21, S26]:** Emerging methods like GAC and BaseCal show promise in improving calibration without sacrificing model performance [S21, S26]. Ainary could advocate for these methods as part of a standard, emphasizing their potential to enhance AI reliability.

- **Finding 5 [J]:** To influence CEN/CENELEC standards, Ainary should engage with key stakeholders in the standards committees, such as CT-016, and present evidence from leading research to demonstrate the importance and feasibility of calibration in AI systems.

**Evidence Quality:**

- **Strongest source:** The EU AI Act [S14] provides a clear regulatory framework that Ainary can aim to influence by advocating for calibration as a necessary component of AI accuracy and oversight.

- **Weakest point:** There is a lack of direct evidence on the composition of CEN/CENELEC committees and the specific process for influencing standards, which limits the ability to form a detailed strategy.

- **What's missing:** Detailed information on the CEN/CENELEC standards development process and successful case studies of standards influence campaigns would strengthen the strategy.

**So What:** Ainary can strategically position itself to influence the 2027-2028 CEN/CENELEC standards by leveraging existing research on calibration's importance and cost-effectiveness, engaging with key stakeholders, and advocating for the inclusion of calibration as a standard requirement. This could secure a first-mover advantage by aligning industry standards with Ainary's calibration approach.

**Claims (for Claim Ledger):**

- Claim 1 | [S14] | E | Admiralty | High
- Claim 2 | [S1, S8] | I | Admiralty | Medium
- Claim 3 | [S19] | E | Admiralty | High
- Claim 4 | [S21, S26] | I | Admiralty | Medium
- Claim 5 | [J] | J | Admiralty | Medium

## PROPRIETARY KNOWLEDGE
### CRTs (verified truths)
[CT-001] RLHF damage to calibration is regime-dependent, not absolute — calibratable vs non-calibratable regimes exist (conf: 0.88, source: ICML 2025, confirmed by Frontier Research Agent + Batch D Formalist, expires: 2026-08-19)
[CT-002] Self-consistency calibration reduces ECE from 42% to 27.3% in biomedical QA (PMC study, 9 models, 13 datasets) (conf: 0.85, source: PMC biomedical study, cited in AR-020-v3, expires: 2026-08-19)
[CT-003] Self-consistency cannot detect systematic bias — only reduces epistemic uncertainty component (~60-70% of miscalibration) (conf: 0.75, source: Batch D Formalist analysis §2.3, expires: 2026-08-19)
[CT-004] ECE alone is insufficient as calibration metric — needs Brier Score + Reliability Diagram for completeness (conf: 0.92, source: Guo et al. 2017, confirmed by Formalist §2.4, expires: 2027-02-19)
[CT-005] Budget-CoCoA achieves consistency calibration at ~$0.005/check using 3 small-model calls (conf: 0.8, source: AR-020-v3, verified by Replicator, expires: 2026-08-19)
[CT-006] Prompting alone is insufficient for good calibration — fine-tuning on ~1000 graded examples outperforms baselines (conf: 0.85, source: Dossier paper b3bf4ca8 (2024), expires: 2026-08-19)
[CT-007] APRICOT enables black-box LLM calibration using only model output — no logit access needed (conf: 0.82, source: Dossier paper 3c45d3c1 (2024), expires: 2026-08-19)
[CT-008] LLM-based guard models produce overconfident predictions and show significant miscalibration under jailbreak attacks (conf: 0.87, source: Dossier paper e2f0bc45 (2024), 9 guard models, 12 benchmarks, expires: 2026-08-19)
[CT-009] Atypical Presentations Recalibration reduces calibration errors by ~60% in medical QA, outperforming vanilla and CoT verbalized confidence (conf: 0.8, source: Dossier paper 8d978805 (2024), expires: 2026-08-19)
[CT-010] Auxiliary models outperform LLMs' internal probabilities and verbalized confidences for calibration (conf: 0.83, source: Dossier paper 3ae1d0fd (2025), 12 LLMs, 4 prompt styles, expires: 2026-08-19)
[CT-011] Confidence scores help calibrate human trust in AI, but trust calibration alone is insufficient to improve AI-assisted decision making (conf: 0.88, source: Dossier paper 5cc4100a (2020), human experiments, expires: 2027-02-19)
[CT-012] Current UQ practices for LLMs are not optimal for human users — community should adopt human-centered approach (conf: 0.8, source: Dossier paper c6f2d538 (2025), expires: 2026-08-19)
[CT-014] MLAs introduce critical trustworthiness challenges beyond traditional LLMs — multi-step execution involves nonlinear risk accumulation (conf: 0.85, source: MLA-Trust benchmark, Dossier paper 681714a9 (2025), expires: 2026-08-19)
[CT-015] Calibration is a regulatory vacuum — EU AI Act Art. 15 requires 'accuracy metrics' but the word 'calibration' never appears (conf: 0.92, source: Batch D Regulator §1.1, verified against Official Journal, expires: 2027-02-19)
[CT-016] CEN/CENELEC harmonized standards expected 2027-2028 will define 'accuracy' technically — window to shape standards is NOW (conf: 0.75, source: Batch D Regulator §1.3, expires: 2026-08-19)
[CT-017] No US federal law mandates AI confidence disclosure — NIST AI RMF 1.0 recommends but doesn't require UQ (conf: 0.88, source: Batch D Regulator §1.4, expires: 2026-08-19)
[CT-018] Full-stack calibration costs <$0.05/decision for single-turn — but multi-step agent workflows multiply this significantly (conf: 0.78, source: AR-020-v3 Exhibit 2, critique by Replicator + Red Team, expires: 2026-08-19)
[CT-019] The Three-Tier Architecture (Entropy → Consistency → Conformal) is a research synthesis, not an implementation guide — significant code gaps remain (conf: 0.85, source: Batch A Replicator assessment, expires: 2026-08-19)
[CT-020] AI Agents are NOT a separate category in EU AI Act — classification depends on deployment domain, not technology (conf: 0.9, source: Batch D Regulator §1.2, expires: 2027-02-19)
[CT-021] EU AI Act Article 14 (Human Oversight) functionally requires confidence signals — calibration is a de facto prerequisite (conf: 0.78, source: Batch D Regulator §1.1, expires: 2026-08-19)
[CT-022] ISO 42001:2023 requires accuracy monitoring process but does not define calibration technically — gap exists (conf: 0.82, source: Batch D Regulator §1.5, expires: 2027-02-19)
[CT-023] EU AI Act enforcement begins August 2026 for High-Risk (Annex III) and Transparency (Art. 50) (conf: 0.95, source: Batch D Regulator §1.3, EC timeline, expires: 2026-09-19)
[CT-024] Texas and California offer Safe Harbor for companies implementing NIST AI RMF or ISO 42001 (conf: 0.8, source: Batch D Regulator §1.4, expires: 2026-08-19)
[CT-025] LLM sycophancy influences user trust — complimentary stance adaptation reduces perceived authenticity while neutral adaptation enhances trust (conf: 0.82, source: Dossier paper 3d04e8a8 (2025), expires: 2026-08-19)
[CT-026] Hallucination essence lies in absence of metacognition in LLMs — DMC framework separates metacognition from cognition (conf: 0.78, source: Dossier paper 5f591bfe (2025), expires: 2026-08-19)
[CT-027] Compositionality of conformal prediction across dependent pipeline stages is an unsolved theoretical problem (conf: 0.85, source: Batch D Formalist §2.5 Problem 4, expires: 2026-08-19)

### Corrections (past mistakes)
[CX-001] WRONG: No framework exists for multi-agent confidence propagation
  RIGHT: SAUP (ACL 2025) and HTC (Jan 2026) address multi-agent propagation — partial solutions exist but don't compose across organizational boundaries
  Severity: CRITICAL | Source: Frontier Research Agent + Red Team Finding #4
[CX-002] WRONG: ECE of 27.3% for consistency calibration is a universal result
  RIGHT: The 27.3% ECE figure is from biomedical QA only (PMC study). Domain-specific — cross-domain generalization unverified
  Severity: CRITICAL | Source: Red Team Finding #1 (CRITICAL)
[CX-003] WRONG: Enterprise hallucination losses are $67.4B
  RIGHT: $67.4B figure is from AllAboutAI — single non-peer-reviewed source with no disclosed methodology. Use verified case studies (Mata v. Avianca, Air Canada) instead
  Severity: CRITICAL | Source: Red Team Finding #3 (CRITICAL)
[CX-004] WRONG: The Three-Tier Architecture is implementable on Monday morning by any engineer
  RIGHT: Only Tier 3 (threshold routing) is trivially implementable. Tier 1 needs 1-2 days + ML experience. Tier 2 (conformal) requires statistician. Tier 1.5 (SAUP/HTC) is research-grade only
  Severity: MAJOR | Source: Replicator assessment
[CX-005] WRONG: Budget-CoCoA costs $0.005 per check
  RIGHT: Actual cost with Haiku pricing (~$0.80/MTok) for 3 calls × 200 tokens ≈ $0.0005 — report estimate is ~10x too high (or assumes longer prompts)
  Severity: MAJOR | Source: Replicator cost verification
[CX-006] WRONG: Self-consistency meta-calibration (5-prompt agreement) validates claim correctness
  RIGHT: 5-prompt self-consistency is epistemically circular — validates consistency-based calibration using consistency. Agreement rates likely inflated by ~10-20%
  Severity: MAJOR | Source: Red Team Finding #8 + Empiricist Experiment 3
[CX-007] WRONG: ECE < ε is sufficient for good calibration
  RIGHT: ECE is necessary but not sufficient. Requires Sharpness + Resolution. Use Brier Score for complete assessment
  Severity: MAJOR | Source: Formalist §2.4, Guo et al. 2017

### Best Previous Report (improve on this)
# AR-020: Trust Calibration Methods for AI Agents
## v5 — Fifth Edition — February 2026

Ainary Research -- Florian Ziesche

---

## BEIPACKZETTEL

| Field | Value |
|-------|-------|
| Report ID | AR-020 v5 |
| Topic | Trust Calibration for AI Agents |
| Decision to Inform | Build/buy calibration infrastructure for AI agent systems |
| Decision Owner | CTO / VP Engineering |
| Audience | Expert (Technical Leadership + Researchers) |
| Risk Tier | 2 |
| Freshness | last_12m |
| Confidence | 76% (honest, calibrated -- see Section 13) |
| Sources | 30 numbered [S1]-[S30] |
| Load-Bearing Claims | 20 (see Claim Ledger, Appendix B) |
| Contradictions | 4 (see Contradiction Register, Appendix C) |
| Quality Score | 13/16 (self-assessed Reviewer Rubric, Appendix D) |
| Versions | v1 -> v2 -> v3 -> v4 -> v5 |
| Known Limitations | Key headline numbers (84% overconfidence, 27.3% ECE) originate from papers not in our full-text verification corpus. Multi-agent propagation remains illustrative, not empirical. All 14 review agents share the same base model (Claude), creating correlated blind spots. |

---

## ASSUMPTION REGISTER

1. **A1:** We assume readers have access to commercial LLM APIs (OpenAI, Anthropic, Google) and cannot self-host models for logit access. If you self-host, Family 1 (temperature scaling) becomes viable and changes the architecture recommendation.
2. **A2:** Cost estimates use February 2026 API pricing (Haiku ~$0.80/MTok, GPT-4o-mini ~$0.15/MTok). Pricing changes directly affect ROI calculations.
3. **A3:** We assume "agent" means an LLM system that takes actions (tool calls, API writes, multi-step workflows), not a simple chatbot. Simple QA systems need simpler calibration.
4. **A4:** The 27.3% vs 42% ECE comparison (consistency vs verbalized) is from biomedical QA [S8]. We assume the relative ranking (consistency > verbalized) generalizes across domains, but absolute ECE values will differ. This assumption is untested.
5. **A5:** We assume positive error correlation (rho > 0) in same-model multi-agent chains based on shared training data and shared context. This is plausible but not empirically measured in production systems as of February 2026.
6. **A6:** EU AI Act enforcement timeline follows the published schedule. Political delays are possible but not assumed.
7. **A7:** We assume the reader's organization has at least one ML engineer. Organizations without ML expertise need external consulting before implementing Tier 1+.
8. **A8:** The "84% of LLM scenarios show overconfidence" figure [S8] is widely cited but the primary source paper is not in our full-text verification corpus. We treat it as directionally correct but not independently verified.
9. **A9:** HTC, BaseCal, and STeCa are preprints (not peer-reviewed). Their claims may not replicate.
10. **A10:** Human reviewer cost estimates ($40-80K/year FTE) assume US/EU labor markets. Costs differ significantly in other geographies.

---

## EXECUTIVE SUMMARY (SCR Framework)

**Situation:** When a multi-agent AI system fails, it fails in clusters. Agents sharing the same base model, training data, and conversation context produce correlated errors. Agent A hallucinates; Agent B, processing A's output, propagates the hallucination with high confidence. The standard multiplicative confidence model (C = product of individual confidences) is mathematically inconsistent under positive correlation [S21, FM-1], yet it remains the implicit assumption in every deployed system. No production framework addresses inter-agent confidence propagation across organizational boundaries.

**Complication:** The training process that makes LLMs helpful -- RLHF -- systematically damages calibration [S7]. Reward models assign higher scores to confident-sounding responses regardless of correctness. The damage is regime-dependent: models exist in either a "calibratable regime" (where post-hoc calibration works) or a "non-calibratable regime" (where aggressive RLHF has structurally destroyed calibratability) [S7, CT-001]. The standard fix (temperature scaling) requires logit access that GPT-4 and Claude do not provide [S1]. Three papers from January 2026 (HTC, BaseCal, SAUP) proved that agent-specific calibration works in research settings [S21, S26, S27], but no open-source implementations exist and none have been peer-reviewed.

**Resolution:** This report presents a production-oriented integration guide synthesizing seven method families into a three-tier architecture. Tier 1 (consistency-based calibration) works today on black-box APIs at $0.0005-$0.015 per check [S8, S19]. Tier 2 (conformal prediction) provides statistical guarantees for high-stakes single-step decisions [S9, S10]. Tier 3 (selective prediction) routes low-confidence outputs to human review. Full-stack automated calibration costs $0.07-$2.24 per query including infrastructure [author estimate]. EU AI Act enforcement begins August 2026; calibration is not legally required but is arguably necessary for Article 14 human oversight compliance [CT-015, CT-021]. The regulatory window for early adoption and standards influence (CEN/CENELEC, expected 2027-2028) is open now.

This is the fifth edition. Version 5 integrates findings from a 6-agent adversarial review (Red Team, Empiricist, Formalist, Practitioner, Writer, Ethicist) that identified 1 critical, 12 major, and 13 minor issues in v4. Key fixes: the "84% overconfidence" figure now carries a verification caveat, "provably wrong" is corrected to "mathematically inconsistent," implementation timelines are honest (6-12 weeks, not "Monday morning"), and a new "Do Not Deploy If" framework addresses when calibration causes more harm than good.

---

## KEY TAKEAWAYS

- Correlated agent failures, not independent errors, are the primary risk in multi-agent systems. Same-model chains amplify errors because agents share systematic biases. No production tool addresses this. [S21, A5]

- RLHF damages calibration in a regime-dependent way. Some models remain calibratable after RLHF; others do not. Assume your model is miscalibrated until measured. [S7, CT-001]

- Consistency-based calibration (3-5 API calls, compare responses) is the best black-box method available today. In biomedical QA, it reduces Expected Calibration Error from 42% to 27% [S8]. Cross-domain generalization is unverified [A4, CX-002].

- Temperature scaling -- the gold standard -- does not work on GPT-4 or Claude because they do not expose logits [S1].

- Full-stack calibration costs $0.07-$2.24 per query including infrastructure and human reviewers. Positive ROI only when damage-per-error exceeds $25-75 depending on volume [author estimate].

- EU AI Act does not mention "calibration," but Article 14 (human oversight) functionally requires confidence signals. Enforcement begins August 2026. [CT-015, CT-021]

- Do NOT deploy calibration if you cannot verify accuracy on your target distribution, cannot monitor for demographic fairness in high-stakes contexts, or if your error cost is below the break-even threshold [E4].

- Implementation takes 6-12 weeks for a team with ML experience, not "Monday morning." Only threshold routing (Tier 3) is trivially implementable. [CX-004]

- ECE alone is an insufficient metric. Combine with Brier Score and reliability diagrams for complete assessment. [CT-004, S1]

- This report is an LLM-assisted research product. All review agents share the same base model, creating correlated blind spots. Independent human expert review remains necessary.

---

## RESEARCH BRIEF (Template B)

### 1) Primary Research Question (why now)
What calibration infrastructure should an organization build or buy to ensure AI agent confidence outputs are trustworthy enough for production decision-making?

**Why now:** Three agent-specific calibration papers appeared in January 2026 (HTC, BaseCal, SAUP) [S21, S26, S27]. EU AI Act high-risk enforcement begins August 2026. Gartner predicts >40% of agentic AI projects will be canceled by 2027 [S22]. The gap between agent deployment velocity and calibration infrastructure is widening.

### 2) Decision Context
**Who decides:** CTO / VP Engineering, with input from Legal (regulatory), Product (UX), and Finance (ROI).
**Consequence if wrong:** Deploy without calibration: liability exposure (EU AI Act penalties up to 35M EUR / 7% revenue), reputational damage (Air Canada, Mata v. Avianca precedents), silent accuracy degradation. Over-invest in calibration: unnecessary infrastructure cost on low-stakes applications.

### 3) Sub-Questions (10, non-overlapping)
1. How does RLHF training damage LLM calibration, and is the damage reversible?
2. Which calibration methods work without logit access (black-box APIs)?
3. How does confidence propagate (or degrade) in multi-agent chains?
4. What does a production calibration architecture look like (tiers, costs, components)?
5. What is the realistic cost and ROI of calibration by use case?
6. What does EU AI Act require for accuracy/calibration, and by when?
7. What are the ethical risks of deploying (or not deploying) calibration?
8. When should an organization NOT deploy calibration?
9. How should calibration be monitored for drift in production?
10. What experiments would validate or invalidate this report's core claims?

### 4) Evidence Criteria
**Include:** Peer-reviewed papers (2023-2026), preprints with methodological rigor, official regulatory text, verified case law, production deployment reports.
**Exclude:** Vendor marketing without technical detail, unverifiable market statistics, pre-2022 LLM calibration work (pre-RLHF era).

### 5) Key Terms & Definitions
- **ECE (Expected Calibration Error):** Measures gap between predicted confidence and actual accuracy, binned. Lower = better. ECE = 0 means perfect calibration. ECE alone is insufficient (needs Brier Score for completeness) [CT-004].
- **Calibration:** The property that when a model says "90% confident," it is correct 90% of the time.
- **RLHF:** Reinforcement Learning from Human Feedback -- training that makes LLMs helpful but damages calibration.
- **Conformal Prediction:** Statistical method producing prediction sets with guaranteed coverage probability.
- **Selective Prediction / Abstention:** Refusing to predict when uncertain; routing to human review.

### 6) Intended Audience
Technical leadership (CTO, VP Engineering, ML leads) at organizations deploying or planning to deploy AI agents. Assumes familiarity with LLM APIs but not with calibration theory.

### 7) Planned Methods & Sources
Literature synthesis of 30+ sources. No new empirical experiments (proposed in Section 11). Sources triangulated across academic (NeurIPS, ICLR, ACL, ICML), regulatory (EU AI Act Official Journal), industry (Amazon Science, Google Cloud), and legal (court records).

### 8) Stopping Criteria
- Core architecture recommendation supported by 3+ independent sources
- All headline numbers traced to primary sources or labeled "author estimate" / "not independently verified"
- All contradictions explicitly registered
- Confidence > 70% overall

---

## METHODOLOGY & SOURCE STRATEGY

### Source Strategy
30 sources spanning academic papers (22), regulatory texts (3), industry publications (3), legal records (2). Full Source Log in Appendix A. Sources weighted by: peer review status, recency, methodological rigor, and relevance to production deployment.

### Validation Approach
- **Tier 1 (Self-Consistency):** 5 key claims tested with 5 different prompts. Agreement rate reported per claim.
- **Tier 2 (Source Verification):** EU AI Act claims verified against Official Journal text. Quantitative claims traced to primary sources where available.
- **Tier 3 (Uncertainty Disclosure):** Claims with <70% confidence marked explicitly.
- **Tier 4 (Circularity Acknowledgment):** This meta-calibration uses self-consistency to validate self-consistency. We acknowledge the epistemic circularity [CX-006]. Source verification (Tier 2) provides the non-circular check.

### Gap Check Results
- **Critical gap:** The 6 headline numbers in the executive summary all originate from papers not in our full-text RAG verification corpus [CT-029]. Citations are to published/preprint sources but we could not cross-check exact figures against full text.
- **Structural gap:** No published study measures error correlation (rho) in production multi-agent chains [A5].
- **Domain gap:** Calibration evidence is concentrated in biomedical QA and factual QA. Code generation, legal reasoning, and creative tasks are underrepresented.
- **Fairness gap:** No published study addresses demographic fairness in LLM calibration [S8, E3].

---

## DOMAIN OVERVIEW

### Definitions

**Trust calibration** is the process of aligning an AI system's expressed confidence with its actual accuracy. A well-calibrated agent saying "90% confident" is correct 90% of the time.

**Overconfidence** is the systematic tendency to express higher confidence than warranted by accuracy. RLHF-trained LLMs are structurally overconfident because reward models score confident-sounding responses higher [S7].

**Expected Calibration Error (ECE)** is the standard metric: partition predictions into bins by confidence, compute |accuracy - confidence| per bin, take the weighted average. ECE = 0 is perfect. ECE alone is insufficient -- it needs Brier Score (combines calibration + sharpness + resolution) and reliability diagrams for complete assessment [S1, CT-004].

### Taxonomy: Seven Method Families

| Family | Access | Key Methods | Typical ECE | Cost/Check | Agent-Ready? |
|--------|--------|-------------|-------------|-----------|--------------|
| 1. Post-Hoc Logit | White-box | Temperature Scaling, ATS, Thermometer | ~0.25% (vision) [S1] | ~$0 | No (API constraint) |
| 2. Consistency-Based | Black-box | Self-Consistency, Budget-CoCoA, PCS, APRICOT | ~27% (biomed QA) [S8] | $0.0005-0.015 | Yes |
| 3. Verbalized Confidence | Black-box | Prompt-based, AFCE, DINCO | ~42% (biomed QA) [S8] | $0.001-0.01 | Partial (biased) |
| 4. Conformal Prediction | Any | ConU, TECP, SConU | N/A (sets) | Variable | Partial (cold start) |
| 5. Ensemble | Any | GETS, BBQ, Cascading | 46% reduction (credit risk) [S17] | High | Partial (cost) |
| 6. Selective Prediction | Any | SelectLLM, Abstention | Abstain ECE | Variable | Yes |
| 7. Agentic (2026) | Any | HTC, GAC, STeCa, SAUP | Research-stage [S21] | Low | Research only |

ECE values are domain-specific. The 27% and 42% figures are from biomedical QA [S8]; absolute ECE will differ in other domains [A4, CX-002].

### Mental Models

1. **The RLHF Tax:** Every instruction-tuned model pays a calibration tax. Measure it before trusting confidence outputs.
2. **Black-Box Reality:** Most production LLMs are black boxes. Architecture must not depend on logit access.
3. **Correlation Amplifier:** Same-model agent chains amplify errors. Treat multi-agent confidence with inherently lower trust than single-agent.

---

## DETAILED FINDINGS

### 1. The RLHF-Calibration Problem

**Finding 1.1:** RLHF systematically damages LLM calibration by rewarding confident-sounding responses regardless of correctness.
**Evidence:** Wang et al. (NeurIPS 2024) demonstrated the mechanism: RLHF reward models assign higher scores to confident responses [S7]. "Resisting Correction" (Dec 2025) found RLHF creates conversational overconfidence bias (rho = 0.036, described as "emergent property of RLHF optimization") [S18]. The effect is widely reported across multiple studies.
**Caveat:** The damage is regime-dependent, not absolute. ICML 2025 demonstrated a "calibratable regime" (post-hoc calibration works) vs "non-calibratable regime" (RLHF has structurally destroyed calibratability) [S7, CT-001]. The rho = 0.036 figure is from a paper not in our full-text verification corpus.
**Implication:** Assume your RLHF-tuned model is miscalibrated. Measure ECE on your target domain before any deployment. Do not trust verbalized confidence without external validation.

**Finding 1.2:** A widely cited figure states 84% of LLM evaluation scenarios show overconfidence (9 models, 351 scenarios) [S8].
**Evidence:** Attributed to PMC biomedical study [S8].
**Caveat:** This figure is widely cited but the primary source paper (PMC12249208) is not in our full-text verification corpus. We cannot independently verify the exact numbers (84%, 9 models, 351 scenarios). Treat as directionally correct. [A8, CT-029]
**Implication:** The direction is clear (LLMs are systematically overconfident) even if the precise magnitude is uncertain.

**Finding 1.3:** The black-box constraint eliminates the best calibration method for most production use.
**Evidence:** Temperature scaling (Guo et al. 2017 [S1]) achieves ~0.25% ECE on vision models. GPT-4 provides top-5 logprobs only; Claude provides none; Gemini provides partial access [verified Feb 2026].
**Caveat:** API access changes frequently. Self-hosted models (Llama, Mistral) retain full logit access.
**Implication:** Architecture for calibration must assume black-box APIs. Design for consistency-based methods (Family 2) as default.

---

### 2. Calibration Method Families (6 Production-Relevant)

**Finding 2.1:** Consistency-based calibration outperforms verbalized confidence in biomedical QA.
**Evidence:** Self-consistency achieved mean ECE of 27.3% vs 42.0% for verbalized confidence across 13 biomedical datasets (PMC 2024) [S8]. Budget-CoCoA achieves this with approximately 3 API calls at $0.0005-$0.015/check depending on model and prompt length [S19, CX-005].
**Caveat:** These ECE figures are domain-specific (biomedical QA only). Cross-domain generalization to code, legal, or creative tasks is not validated [CX-002]. The relative ranking (consistency > verbalized) likely generalizes; the absolute numbers will not [A4].
**Implication:** Deploy consistency-based calibration as Tier 1 default. Budget for 3-5 extra API calls per query. Do not cite "27% ECE" as a universal target.

**Finding 2.2:** Consistency methods cannot detect systematic bias.
**Evidence:** If the model answers incorrectly the same way across all samples, consistency reports high confidence for a wrong answer. Self-consistency addresses epistemic uncertainty but not systematic bias [CT-003].
**Caveat:** The "60-70% of miscalibration is epistemic" estimate is an author estimate with no published derivation. The decomposition ECE = epistemic + systematic is a conceptual analogy, not a mathematical identity [CT-030].
**Implication:** Consistency calibration is necessary but not sufficient. Combine with external validation signals (human review, ground-truth comparison) for high-stakes decisions.

**Finding 2.3:** Verbalized confidence is the most adversarially vulnerable method.
**Evidence:** NeurIPS 2025 found "even subtle semantic-preserving modifications can lead to misleading confidence" and "commonly used defence techniques are largely ineffective" [S5]. Prompt injection can inflate verbalized confidence by 15-40 percentage points [author estimate based on S5].
**Caveat:** Consistency-based methods are more resistant but not immune.
**Implication:** Never rely solely on verbalized confidence. Use at minimum 2 independent calibration methods per decision point (defense-in-depth) [S5].

**Finding 2.4:** Conformal prediction provides the only statistical guarantees but requires calibration sets.
**Evidence:** ConU (NeurIPS 2024 [S9]) and SConU (ACL 2025) integrate conformal prediction with LLM calibration. Theoretical minimum for valid coverage is ~10 examples; practical recommendations suggest 200-500 for useful prediction set sizes [S9, FM-3].
**Caveat:** Conformal prediction guarantees do NOT compose across dependent pipeline stages. For multi-agent systems, this is an unsolved theoretical problem [CT-027]. Distribution shift degrades guarantees; partially addressed by Domain-Shift-Aware CP (Lin et al., Oct 2025) [S9].
**Implication:** Deploy con

### Vault Knowledge
### 20_Areas/AI-Research/AR-001 State of Agent Trust.md
---
tags: [ainary-report, ai-trust, agent-security]
report: AR-001
qa-score: 75/100
date: 2026-02-14
audience: [CTO, CISO, AI Product Teams]
---

# AR-001 State of Agent Trust 2026

## Executive Summary

- The [[AI]] agent market will grow from $7.8B to $52B by 2030 (45.8% CAGR), yet 95% of corporate [[AI]] projects fail and 84% of [[LLM]]s are overconfident
- Only 6% of enterprises achieve meaningful EBIT impact from [[AI]] agents (McKinsey, n=1,993)
- Calibration infrastructure costs $0.005 per check vs. $4.4M average [[AI]]-related losses per company (EY, 99% of orgs report losses)
- EU [[AI]] Act enforcement begins August 2026 with €35M penalties; US has no federal framework after rescinding Biden's EO
- Three-layer trust gap: Communication (solved), Identity (emerging), Trustworthiness (missing) — no standardized trust-scoring protocol exists

## Key Insights

- **Overconfidence pandemic:** 84% of [[LLM]] outputs show confidence exceeding actual accuracy (PMC study, 9 models, 351 scenarios)
- **Trust erosion:** [[AI]] usage increased 13% but worker confidence dropped 18% (ManpowerGroup, n=14K)
- **Regulatory trilemma:** Must deploy fast OR compliant OR insured — can't have all three
- **Multi-agent amplification:** Verification chains without external calibration create false consensus, not quality assurance
- **Adversarial memory spiral:** Memory poisoning (>95% success) + no detection + propagation + human failure (67% alerts ignored) = self-reinforcing attack loop

## Sales Angles

- "Every company deploying [[AI]] agents is already paying the Trust Tax — most just haven't read the invoice yet. We help you see the $4.4M you're losing."
- "Your competitors use [[AI]] agents without trust infrastructure. The first major failure will create regulation overnight — be compliant before it's mandatory."
- "Calibration costs half a cent per check. One prevented VW-scale failure ($7.5B) pays for 55,555 years of calibration. The ROI is 1:1,500,000."

## Content Ideas

- LinkedIn: "95% of [[AI]] projects fail. 84% of [[AI]] agents are overconfident. 99% of orgs report [[AI]] losses. The pattern? Everyone's building agents without trust infrastructure. Here's what the 6% who succeed do differently."
- Substack: "The $52 Billion Market Building on Sand" — deep dive on why agent adoption (62% experiment) diverges from production success (<10% enterprise-wide)
- Case Study: "How a $0.005 calibration check prevents $4.4M in [[AI]]-related losses — the economics of trust infrastructure"

## Links

- [[AR-002 Trust Tax]]
- [[AR-003 EU-US Regulation]]
- [[AR-006 Security Playbook]]
- [[AR-007 Orchestration]]
- [[AR-009 Calibration]]
- HTML: content/reports/state-of-agent-trust-2026.html

## Related
- [[AR-001 State of Agent Trust]]
- [[article-1-100-agents]]
- [[article-1-100-agents-de]]
- [[100-agents-48-stunden]]
- [[Content-Ideas-From-Reports]]


### 20_Areas/AI-Research/AR-002 Trust Tax.md
---
tags: [ainary-report, ai-economics, compliance, roi]
report: AR-002
qa-score: 78/100
date: 2026-02-14
audience: [CFO, CISO, CTO]
---

# AR-002 The Trust Tax

## Executive Summary

- 99% of enterprises deploying [[AI]] report financial losses, averaging $4.4M per company (EY RAI Pulse, n=975 C-suite)
- Workslop rework costs $186/employee/month in [[AI]]-heavy workflows — $9M/year at 10K employees (Stanford/HBR)
- Shadow [[AI]] breach premium: $670K above standard breach ($4.63M total, 247 days to detect)
- Organizations with fragile [[AI]] governance miss 40% of projected productivity gains (EY)
- Calibration infrastructure costs $0.005/check vs. €35M EU [[AI]] Act penalties — 333x to 3,333x ROI on prevention

## Key Insights

- **Five hidden line items:** Rework Tax ($186/employee/month), Shadow Tax ($670K breach premium), Confidence Tax (18% trust drop despite 13% usage increase), Compliance Tax ($2-5M EU setup), Opportunity Tax (34% more likely revenue growth with monitoring)
- **Trust Debt compounds:** Like technical debt but worse — retroactive trust infrastructure costs 5-10x proactive deployment
- **Alert fatigue doom loop:** 67% of SOC alerts ignored + 80-99% healthcare false positives = HITL becomes rubber stamp
- **[[AI]] insurance gap:** 99% of enterprises report [[AI]] losses, but insurers exclude [[AI]] liability without clear pricing model
- **Klarna overpivot lesson:** $60M claimed savings, 853 FTEs replaced, then partial rollback — metrics mask quality degradation

## Sales Angles

- "You're already paying $4.4M in [[AI]]-related losses. We help you measure the Trust Tax across 5 hidden line items — then eliminate them for $135/month in calibration infrastructure."
- "The window between 'optional' and 'mandatory' [[AI]] governance closes August 2026. €35M EU penalties vs. $2-5M compliance cost. Build defensibility now."
- "Your [[AI]] transformation ROI is 40% lower than projected because of fragile talent foundations. We fix the foundation — trust infrastructure — so [[AI]] actually delivers."

## Content Ideas

- LinkedIn: "The Trust Tax has 5 line items you can't see: Rework ($186/employee/month), Shadow [[AI]] ($670K breach premium), Confidence Collapse (18% drop), Compliance Gap ($2-5M), Opportunity Loss (40% ROI miss). Here's the invoice."
- Newsletter: "Why Klarna's $60M [[AI]] Savings Required a Partial Rollback" — the hidden cost when metrics don't capture quality degradation
- Case Study: "From $4.4M Losses to Trust Infrastructure: The 90-Day Playbook"

## Links

- [[AR-001 State of Agent Trust]]
- [[AR-003 EU-US Regulation]]
- [[AR-008 Governance for Boards]]
- [[AR-009 Calibration]]
- HTML: content/reports/trust-tax-2026.html

## Related
- [[AR-002 Trust Tax]]
- [[Content-Ideas-From-Reports]]
- [[twitter-ai-agents-employees]]
- [[Publish-Blog-Index]]
- [[Publish-Resources-Index]]


### 20_Areas/AI-Research/AR-003 EU-US Regulation.md
---
tags: [ainary-report, regulation, eu-ai-act, compliance]
report: AR-003
qa-score: 75/100
date: 2026-02-14
audience: [General Counsel, Compliance Officers, CTO]
---

# AR-003 The Transatlantic Divide

## Executive Summary

- EU [[AI]] Act full enforcement August 2026 with €35M or 7% global revenue penalties vs. US has zero federal [[AI]] regulation after rescinding Biden's EO
- EU compliance costs 5-20x higher than US equivalents ($2-5M initial setup)
- Neither framework actually defines or addresses [[AI]] agents specifically — multi-agent liability is a black hole in both jurisdictions
- EU [[AI]] Act has extraterritorial reach — if your [[AI]] system's output is used in the Union, you're in scope regardless of server location
- Pragmatic strategy: Build for EU compliance as floor, use US speed as ceiling

## Key Insights

- **Regulatory trilemma:** Deploy fast (US advantage) → no compliance → no insurance → unlimited liability
- **Agent-shaped hole:** EU [[AI]] Act defines "[[AI]] system" but not autonomous, goal-directed, multi-step agents — provider vs. deployer ambiguity in multi-agent chains
- **HITL paradox:** EU requires "effective human oversight" (Article 14) but 67% of SOC alerts ignored and 80-99% healthcare false positives — regulatory mandate meets empirical failure
- **State-by-state patchwork:** Colorado live Feb 2026, California SB 1047 vetoed, 40+ states with [[AI]] bills — US companies face 50 different compliance regimes
- **ISO 42001 bridge:** AWS first certified (Jan 2026) — voluntary standard that satisfies both EU conformity + US governance without being legally required in either

## Sales Angles

- "EU [[AI]] Act enforcement is 6 months away. €35M penalties vs. $2-5M compliance cost. We build the trust infrastructure that satisfies EU conformity AND makes you insurable in the US."
- "You need one governance framework that works in both markets. ISO 42001 + EU conformity + US state compliance. We deliver all three without triple the cost."
- "Regulatory arbitrage doesn't work anymore — EU extraterritorial reach means if Europeans use your [[AI]], you're in scope. Build compliance as your competitive moat."

## Content Ideas

- LinkedIn: "August 2, 2026: EU [[AI]] Act full enforcement. €35M max penalty. Most US companies don't realize extraterritorial reach means 'just don't sell to Europe' isn't a strategy anymore."
- Substack: "The Munich vs. NYC Experience" — same [[AI]] product, two incompatible regulatory realities, and why 'build fast in US, wrap compliance for EU' is the only viable strategy
- Policy Brief: "The Agent-Shaped Hole in Global [[AI]] Regulation" — why neither EU nor US frameworks address multi-agent liability chains

## Links

- [[AR-001 State of Agent Trust]]
- [[AR-002 Trust Tax]]
- [[AR-008 Governance for Boards]]
- HTML: content/reports/eu-us-regulation-2026.html

## Related
- [[multi-agent-production]]
- [[AR-003 EU-US Regulation]]
- [[article-1-100-agents]]
- [[article-1-100-agents-de]]
- [[100-agents-48-stunden]]


### 20_Areas/AI-Research/AR-004 Maturity Model.md
---
tags: [ainary-report, ai-maturity, framework, assessment]
report: AR-004
qa-score: 68/100
date: 2026-02-14
audience: [CTO, CISO, Enterprise Architecture]
---

# AR-004 The [[AI]] Agent Maturity Model

## Executive Summary

- Every major [[AI]] maturity framework (Gartner, McKinsey, Deloitte, Microsoft, IBM, [[Google]] Cloud) measures [[AI]]-as-tool, not agents-as-actors — fundamental blind spot
- 62% experiment with agents, <10% deploy enterprise-wide, only 6% see EBIT impact — the gap is maturity, not technology
- AGENT framework introduces 5 dimensions: Autonomy, Governance, Error Handling, Networked Trust, Team Integration across 5 levels (Ad Hoc → Calibrated → Orchestrated → Autonomous)
- Level 3 (Calibrated) is the survival threshold for August 2026 EU [[AI]] Act enforcement — organizations below Level 3 face $2-5M compliance costs AND regulatory exposure
- 5-minute self-assessment with 10 binary questions — honest answer: 80%+ of organizations are at Level 1

## Key Insights

- **Maturity illusion:** 62% experimentation vs. <10% production deployment = stuck at Level 1, not slowly moving up
- **Five dimensions map to failures:** Autonomy (Knight Capital $440M), Governance (VW $7.5B), Error Handling (84% overconfidence), Networked Trust (45-64% MAS hijacking), Team Integration (67% alert fatigue)
- **Level 3 gatekeepers:** Calibrated confidence (not VCE), dedicated agent credentials (not personal [[API]] keys), memory governance (provenance tracking), measured SLAs (<2% hallucination)
- **Level 1 → 3 playbook:** Inventory (1-3 months, low cost), Calibration ($0.005/check, 3-9 months), Stop using VCE/random sampling
- **Existing models fail:** Gartner (no agent dimensions), McKinsey (no maturity ladder), Deloitte (no agent-specific), Microsoft (infrastructure-focused), [[Google]] Cloud (named Agent Trust but no framework update), IBM (data maturity, not agent)

## Sales Angles

- "You think you're at Level 3 because you have ChatGPT Enterprise. Our 5-minute assessment shows 80% of organizations are at Level 1. We get you to Level 3 before August 2026 enforcement."
- "The gap between 62% experimentation and <10% production isn't technology — it's maturity. We built the only agent-specific maturity model. Use it to diagnose where you're stuck."
- "Level 3 costs $0.005/check for calibration + $2-5M compliance. Level 1 when EU [[AI]] Act hits? Unlimited regulatory exposure. We deliver Level 3 in 9 months."

## Content Ideas

- LinkedIn: "Take the 5-minute Agent Maturity Self-Assessment. 10 binary questions. Be honest. 80% of you are at Level 1. Here's the roadmap to Level 3 before regulators force it."
- Workshop: "Agent Maturity Audit" — bring your architecture, we map you to AGENT framework, deliver Level 1 → 3 roadmap
- Whitepaper: "Why Every [[AI]] Maturity Model Has an Agent-Shaped Blind Spot" — compare Gartner/McKinsey/Deloitte/Microsoft frameworks side-by-side

## Links

- [[AR-001 State of Agent Trust]]
- [[AR-002 Trust Tax]]
- [[AR-007 Orchestration]]
- [[AR-009 Calibration]]
- HTML: content/reports/maturity-model-2026.html

## Related
- [[AR-004 Maturity Model]]
- [[article-1-100-agents]]
- [[sequoia-agi-weltmodell-luecke]]
- [[article-1-100-agents-de]]
- [[100-agents-48-stunden]]


### 20_Areas/AI-Research/AR-005 Financial Services.md
---
tags: [ainary-report, financial-services, banking, fintech]
report: AR-005
qa-score: 68/100
date: 2026-02-14
audience: [Banking CTO, Financial Services CISO, Fintech Founders]
---

# AR-005 The Financial Services Playbook

## Executive Summary

- Financial services deploys [[AI]] agents first: $270B annual compliance costs + 55-65% cost ratios + digital data density = inevitable adoption
- Major banks in production: JPMorgan (2,000+ [[AI]] use cases, $150B+ daily fraud detection), Klarna ($60M savings, 853 FTEs replaced then partial rollback), Morgan Stanley (16,000 advisors using [[AI]] @ MS)
- Regulators (SEC, BaFin, FCA, MAS) signal existing rules apply, but no [[AI]]-agent-specific frameworks exist — legal uncertainty punishes first movers
- Banks solve wrong trust problem: post-hoc explainability for regulators, not pre-decision calibration to prevent failures
- Three agent types = three risk profiles: Trading (highest per-incident loss $100M+), Customer-Facing (precedent risk like Air Canada), Internal (hidden systemic risk)

## Key Insights

- **Structural inevitability:** 73% of banking employee time has [[AI]] impact potential (Accenture) — 39% automation, 34% augmentation
- **Deployment reality check:** "2,000+ [[AI]] use cases" (JPMorgan) ≠ "autonomous agents" — mostly supervised tooling, not agentic
- **Three-layer trust gap in banking:** Communication (solved via A2A/MCP), Identity (early — 23% credential leaks, 10% non-human identity strategy), Trustworthiness (MISSING — no calibration infrastructure)
- **Regulatory maze:** SEC (fiduciary duty applies), BaFin (EU [[AI]] Act high-risk), FCA (firms fully responsible), MAS (most innovation-friendly with FEAT principles)
- **DBS counterexample:** Singapore's DBS deployed customer-facing [[AI]] without public failure by treating MAS FEAT as engineering requirements, not compliance checkboxes

## Sales Angles

- "You're spending $270B on compliance and deploying [[AI]] agents without trust infrastructure. We prevent the Air Canada precedent ($800 direct cost, unlimited liability exposure) for $0.005/check."
- "JPMorgan has 2,000 [[AI]] use cases. You need one thing they don't: calibrated trust scoring. We deliver production-ready agent calibration before August 2026 EU enforcement."
- "Singapore's DBS proves agent deployment without failures is possible — by building trust infrastructure first. We replicate their playbook for Western banks."

## Content Ideas

- LinkedIn: "$270B compliance spend + 55-65% cost ratios + zero trust infrastructure = why banks will deploy [[AI]] agents first AND fail hardest. Here's the playbook DBS used to avoid it."
- Case Study: "From Klarna's $60M Savings to Partial Rollback: What Happens When Metrics Don't Capture Quality Degradation"
- Regulatory Briefing: "SEC/BaFin/FCA/MAS on [[AI]] Agents: A Comparative Framework" — what each regulator requires, where gaps exist, how to comply across all four

## Links

- [[AR-001 State of Agent Trust]]
- [[AR-002 Trust Tax]]
- [[AR-003 EU-US Regulation]]
- [[AR-006 Security Playbook]]
- [[AR-009 Calibration]]
- HTML: content/reports/financial-services-2026.html

## Related
- [[AR-005 Financial Services]]
- [[article-1-100-agents]]
- [[article-1-100-agents-de]]
- [[100-agents-48-stunden]]
- [[twitter-ai-agents-employees]]


### 20_Areas/AI-Research/AR-006 Security Playbook.md
---
tags: [ainary-report, cybersecurity, ai-security, red-team]
report: AR-006
qa-score: 78/100
date: 2026-02-14
audience: [CISO, Security Engineers, Red Teams]
---

# AR-006 The [[AI]] Agent Security Playbook

## Executive Summary

- Every published prompt injection defense (12/12) has been broken by adaptive attacks from Meta/OpenAI/Anthropic/DeepMind researchers
- Memory injection attacks (MINJA) achieve >95% success rates, creating persistent backdoors that survive session resets
- Multi-agent system hijacking succeeds 45-64% across AutoGen/CrewAI/MetaGPT — zero inter-agent trust verification exists
- Agent attack surface is 7x larger than chatbots: direct prompt, indirect prompt, persistent memory, tool/[[API]] calls, inter-agent comms, credentials, external data
- Defense strategy: architectural constraints (privilege separation, deterministic guardrails, kill switches), not better prompt engineering

## Key Insights

- **Prompt injection is unsolvable:** [[LLM]]s process instructions + data in same modality (natural language tokens) — no hardware-level separation like kernel/user space
- **Memory = persistent backdoor:** No production memory framework (Letta, Mem0, Zep, LangMem, A-Mem) implements provenance tracking, integrity checks, or confidence scoring per memory entry
- **Tool use escalation:** Prompt injection + excessive permissions = $440M Knight Capital pattern — one compromised agent, full system access
- **Multi-agent contagion:** 45-64% hijacking success because inter-agent messages trusted by default — A2A protocol authenticates systems, not message provenance
- **Supply chain gap:** MCP tool servers = npm packages with no code review, no signing, no sandbox — compromised tool can log credentials, modify behavior, inject prompts

## Sales Angles

- "All 12 prompt injection defenses published by Meta/OpenAI/Anthropic/DeepMind have been broken. We help you build the architectural constraints that survive when prompt defenses fail."
- "Your agents have 7 attack surfaces. Chatbot threat models miss 6 of them. We deliver the agent-specific threat model + red team exercises NIST is asking for but hasn't built yet."
- "Memory poisoning has >95% success rates and zero production defenses. We implement provenance tracking + integrity checks before your agents accumulate corrupted memories."

## Content Ideas

- LinkedIn: "Prompt injection is fundamentally unsolvable (12/12 defenses broken). The security shift: from 'prevent injection' to 'survive injection.' Here's the architectural playbook."
- Red Team Workshop: "Break Your Own Agents Before Attackers Do" — live MINJA, tool exploitation, multi-agent hijacking demos
- Technical Deep-Dive: "The Seven Attack Surfaces of [[AI]] Agents" — map each surface to documented exploit, show compound chains

## Links

- [[AR-001 State of Agent Trust]]
- [[AR-005 Financial Services]]
- [[AR-007 Orchestration]]
- [[AR-009 Calibration]]
- HTML: content/reports/security-playbook-2026.html

## Related
- [[AR-006 Security Playbook]]
- [[article-1-100-agents]]
- [[article-1-100-agents-de]]
- [[100-agents-48-stunden]]
- [[twitter-ai-agents-employees]]


### 20_Areas/AI-Research/AR-007 Orchestration.md
---
tags: [ainary-report, multi-agent, orchestration, langgraph]
report: AR-007
qa-score: 72/100
date: 2026-02-14
audience: [Engineering Leads, CTOs, AI Architects]
---

# AR-007 The Orchestration Problem

## Executive Summary

- 51% of companies have agents in production, yet >40% of agentic [[AI]] projects will be canceled by 2027 — the gap is orchestration
- Performance quality (not cost or safety) is the #1 barrier to scaling multi-agent systems
- Multi-agent cost scales super-linearly: 5-agent pipeline costs 10-30x a single agent, not 5x
- Inter-agent communication can be hijacked with 58-90% success rates even when individual agents are secure
- The fix: build orchestration layer first, then add agents (opposite of current practice)

## Key Insights

- **Five proven patterns:** Prompt Chaining (sequential), Routing (classifier-based), Parallelization (independent subtasks), Orchestrator-Workers (dynamic decomposition), Evaluator-Optimizer (feedback loop) — all from Anthropic's production deployments
- **Framework landscape (Feb 2026):** LangGraph (most control, steep learning curve), CrewAI (fastest prototype, black-box orchestration), AutoGen (research-focused, not production-hardened), OpenAI Swarm (educational only)
- **Nine failure modes:** Infinite loops, deadlocks, conflicting outputs, blame attribution failure, context overflow, orchestrator hallucination, cascade failures, cost explosion, security hijacking (58-90%)
- **Cost reality:** MoA (3 layers x 3 agents) = 27+ [[LLM]] calls = $0.50-$2.00 per task vs. single agent $0.01-$0.03 — cost multiplier from token duplication + retry logic + orchestration overhead
- **Anthropic's counterintuitive claim:** "Most successful implementations weren't using complex frameworks" — raw [[LLM]] [[API]] calls + simple composable patterns outperform multi-agent complexity for most use cases

## Sales Angles

- "Your multi-agent pipeline costs 10-30x a single agent, not 5x. We analyze your token flows, identify coordination overhead, and redesign orchestration to cut costs 40-60%."
- "40% of agentic [[AI]] projects will be canceled by 2027. The pattern: teams build agents, then try to connect them. We build the orchestration layer first — your agents plug into a working system."
- "Inter-agent hijacking succeeds 58-90% when agents trust each other's outputs. We implement the trust verification layer that LangGraph/CrewAI/AutoGen don't provide."

## Content Ideas

- LinkedIn: "Multi-agent cost doesn't scale linearly. 5 agents ≠ 5x cost. It's 10-30x because of token duplication, retry logic, and orchestration overhead. Here's the token flow analysis most teams skip."
- Workshop: "Orchestration-First Design" — build the coordination layer, add stub agents, replace stubs one at a time
- Technical Comparison: "LangGraph vs. CrewAI vs. AutoGen vs. Swarm in Production" — framework decision matrix for Feb 2026

## Links

- [[AR-001 State of Agent Trust]]
- [[AR-004 Maturity Model]]
- [[AR-006 Security Playbook]]
- [[AR-009 Calibration]]
- PDF: content/reports/orchestration-2026.pdf
- MD: content/reports/orchestration-2026-v2.md

## Related
- [[multi-agent-production]]
- [[article-1-100-agents]]
- [[article-1-100-agents-de]]
- [[100-agents-48-stunden]]
- [[twitter-ai-agents-employees]]


### 20_Areas/AI-Research/AR-008 Governance for Boards.md
---
tags: [ainary-report, governance, board-oversight, fiduciary-duty]
report: AR-008
qa-score: 72/100
date: 2026-02-14
audience: [Board of Directors, General Counsel, Audit Committee]
---

# AR-008 [[AI]] Governance for Boards

## Executive Summary

- Only 22% of CEOs say their board effectively supports them on [[AI]] challenges — the competence gap is structural and widening
- EU [[AI]] Act high-risk enforcement begins August 2026 with penalties up to €35M or 7% of global revenue
- Caremark duty of oversight is extending to [[AI]] — directors who fail to monitor [[AI]] risk face personal liability under Delaware law
- 99% of enterprises report [[AI]]-related losses (EY 2025), yet most boards lack dedicated [[AI]] risk oversight structures
- The window between optional and mandatory [[AI]] governance is closing — directors who act now build defensibility, those who wait build liability

## Key Insights

- **Board composition gap:** Average director age 59.1 (up from 58.2), new appointments down 8% (lowest since 2016), only 43% of directors have expertise aligned with CEO's pressing issues — boards getting older/more insular as [[AI]] demands new competence
- **Regulatory clock ticking:** Feb 2025 (prohibited [[AI]] enforced), Aug 2025 (GPAI obligations), Aug 2026 (full high-risk enforcement), Aug 2027 (legacy systems must comply)
- **Caremark → [[AI]] extension:** "Mission critical" risks require affirmative board monitoring (Marchand v. Barnhill 2019) — [[AI]] in customer-facing/safety/compliance = mission critical, no monitoring = "utter failure," business judgment rule only protects informed decisions
- **Failure case pattern:** VW/Cariad ($7.5B), Air Canada (tribunal liability), McDonald's (discontinued), Klarna (reversed cuts) — every case = board either didn't ask about [[AI]] risk OR didn't understand answers
- **Seven questions every board must answer:** (1) Where are we deploying [[AI]]? (2) What is our [[AI]] risk taxonomy? (3) How do we validate outputs? (4) Incident response plan? (5) Compliance status? (6) Audit trail? (7) Adequate expertise?

## Sales Angles

- "22% of CEOs say their board supports them on [[AI]]. We train your board to ask the 7 questions that create Caremark defensibility before August 2026 enforcement."
- "€35M EU penalties vs. $2-5M compliance cost. Your D&O insurance has [[AI]] exclusions. We build the governance infrastructure that makes your board defensible AND your company insurable."
- "Every VW/Air Canada/Klarna failure shares one pattern: the board didn't know what to ask. We deliver the [[AI]] Governance Playbook that turns your board from risk to asset."

## Content Ideas

- Board Training: "[[AI]] Governance for Directors" — 90-minute session covering Caremark extension, EU [[AI]] Act timeline, seven essential questions
- LinkedIn: "The Caremark Duty Just Extended to [[AI]]. Delaware courts held food safety (Blue Bell) requires board monitoring. [[AI]] in customer decisions? Same standard. Your board ready?"
- Decision Memo Template: "Board-Level [[AI]] Risk Assessment" — plug-and-play format for Audit/Risk Committee [[AI]] agenda items

## Links

- [[AR-001 State of Agent Trust]]
- [[AR-002 Trust Tax]]
- [[AR-003 EU-US Regulation]]
- [[AR-004 Maturity Model]]
- PDF: content/reports/governance-2026.pdf
- MD: content/reports/governance-2026-v2.md

## Related
- [[AR-008 Governance for Boards]]
- [[post-microsoft-concentration-risk]]
- [[Content-Ideas-From-Reports]]
- [[microsoft-openai-concentration-risk]]
- [[Publish-Blog-Index]]


### 20_Areas/AI-Research/AR-009 Calibration.md
---
tags:
  - calibration
  - overconfidence
  - trust-infrastructure
  - ainary-report
report: AR-009
qa-score: 72/100
date: 2026-02-14
audience:
  - CTO
  - ML Engineering Lead
  - AI Product Managers
---

# AR-009 The Calibration Gap

## Executive Summary

- 84% of [[AI]] agents are overconfident — confidence exceeds actual accuracy across 9 models and 351 scenarios
- Verbalized confidence is biased upward by 20-30 percentage points and poorly correlated with correctness (r ≈ 0.3-0.5)
- Multi-agent verification amplifies miscalibration instead of correcting it — identically biased validators create false consensus
- Alert fatigue from overconfident systems causes 67% of security alerts to be ignored
- A calibration check costs $0.005 per decision; not calibrating has cost up to $7.5B in single cases (VW Cariad)

## Key Insights

- **Root cause is training:** RLHF reward signal favors confident answers, instruction tuning trains out "I don't know," sycophancy reinforces user premises — overconfidence is emergent property, not model defect
- **Verbalized confidence expression (VCE) is systematically biased:** [[LLM]]s cluster around round numbers (70%, 80%, 90%, 95%) rather than smooth distribution, upward bias 20-30pp, poor correlation with correctness
- **Multi-agent amplification loop:** Agent A (overconfident) → Agent B verifies (also overconfident) → sycophancy bias toward agreement → anchoring on Agent A's confidence → compound overconfidence approaching 100% in 3-agent chains
- **Trust erosion spiral:** Phase 1 (Overcommitment) → Phase 2 (Discovery — 95% confidence on wrong AND right) → Phase 3 (Alert fatigue — 67% ignored) → Phase 4 (Binary choice: abandon [[AI]] or remove oversight) → Phase 5 (Catastrophe)
- **Five calibration methods:** Temperature Scaling (gold standard, requires logit access), Conformal Prediction (guaranteed coverage, needs set handling), Sample Consistency (black-box, $0.003/check), Budget-CoCoA (SOTA, $0.005/check), Selective Prediction (requires retraining)

## Sales Angles

- "84% of [[AI]] outputs are overconfident. Your agents say '95% sure' when they're 70% accurate. We implement Budget-CoCoA calibration for $135/month (1,000 checks/day) — the ROI is 1:1,500,000."
- "Your multi-agent system uses 'Agent B verifies Agent A' for quality. That creates false consensus, not quality assurance. We redesign for disagreement measurement, not confirmation bias."
- "Alert fatigue kills 67% of security alerts. [[AI]] overconfidence will do the same to your HITL system unless you calibrate. We prevent the trust erosion spiral before Phase 3."

## Content Ideas

- LinkedIn: "Verbalized confidence is 'systematically biased and poorly correlated with correctness' (arXiv:2602.00279). Your agents cluster around 70/80/90/95% regardless of actual accuracy. Here's the $0.005 fix."
- Technical Walkthrough: "Sample Consistency vs. Budget-CoCoA vs. Conformal Prediction" — when to use which calibration method
- Case Study: "How $0.005 Calibration Prevents $7.5B VW-Scale Failures" — the asymmetry between prevention cost and failure cost

## Links

- [[AR-001 State of Agent Trust]]
- [[AR-002 Trust Tax]]
- [[AR-004 Maturity Model]]
- [[AR-007 Orchestration]]
- PDF: content/reports/calibration-2026.pdf
- MD: content/reports/calibration-2026-v2.md

## Related
- [[article-1-100-agents]]
- [[article-1-100-agents-de]]
- [[100-agents-48-stunden]]
- [[twitter-ai-agents-employees]]
- [[100-agents-evolution]]


### 20_Areas/AI-Research/Claims/C001 — 67% of security alerts are ignored by SOC analysts.md
---
type: claim
id: C001
confidence: HIGH
source: "Vectra 2023 (n=2,000 SOC professionals)"
last_verified: 2026-02-15
cross_referenced: true
tags: [claim, research]
---

# 67% of security alerts are ignored by SOC analysts

**Source:** Vectra 2023 (n=2,000 SOC professionals)
**Confidence:** HIGH
**Verified by:** qa-agent

## Used In
- [[AR-010]]
- [[AR-011]]

## Invalidation Trigger
If contradicting evidence with comparable methodology emerges, flag all linked reports.


### 20_Areas/AI-Research/Claims/C002 — 84% of LLM outputs are overconfident (verbalized confidence .md
---
type: claim
id: C002
confidence: HIGH
source: "PMC/12249208 (9 models, 351 scenarios)"
last_verified: 2026-02-15
cross_referenced: true
tags: [claim, research]
---

# 84% of [[LLM]] outputs are overconfident (verbalized confidence exceeds actual accuracy)

**Source:** PMC/12249208 (9 models, 351 scenarios)
**Confidence:** HIGH
**Verified by:** qa-agent

## Used In
- [[AR-009]]
- [[AR-010]]
- [[AR-011]]

## Invalidation Trigger
If contradicting evidence with comparable methodology emerges, flag all linked reports.


### 20_Areas/AI-Research/Claims/C003 — Tool calling fails 3-15% of the time in production agent sys.md
---
type: claim
id: C003
confidence: MEDIUM
source: "Michael Hannecke practitioner data + McDonald's case study"
last_verified: 2026-02-15
cross_referenced: false
tags: [claim, research]
---

# Tool calling fails 3-15% of the time in production agent systems

**Source:** Michael Hannecke practitioner data + McDonald's case study
**Confidence:** MEDIUM
**Verified by:** qa-agent

## Used In
- [[AR-010]]

## Invalidation Trigger
If contradicting evidence with comparable methodology emerges, flag all linked reports.


### 20_Areas/AI-Research/Claims/C004 — 6% of companies achieve 'AI High Performer' status with 2-3x.md
---
type: claim
id: C004
confidence: HIGH
source: "McKinsey State of AI 2025 (n=1,993 companies)"
last_verified: 2026-02-15
cross_referenced: true
tags: [claim, research]
---

# 6% of companies achieve '[[AI]] High Performer' status with 2-3x productivity gains

**Source:** McKinsey State of [[AI]] 2025 (n=1,993 companies)
**Confidence:** HIGH
**Verified by:** qa-agent

## Used In
- [[AR-012]]
- [[AR-004]]

## Invalidation Trigger
If contradicting evidence with comparable methodology emerges, flag all linked reports.


### 20_Areas/AI-Research/Claims/C005 — MemoryGraft attack achieves >95% memory injection success ra.md
---
type: claim
id: C005
confidence: HIGH
source: "MINJA research (2024)"
last_verified: 2026-02-15
cross_referenced: true
tags: [claim, research]
---

# MemoryGraft attack achieves >95% memory injection success rate

**Source:** MINJA research (2024)
**Confidence:** HIGH
**Verified by:** qa-agent

## Used In
- [[AR-010]]
- [[AR-014]]

## Invalidation Trigger
If contradicting evidence with comparable methodology emerges, flag all linked reports.


### 20_Areas/AI-Research/Claims/C006 — 80-99% false positive rate in healthcare alert systems.md
---
type: claim
id: C006
confidence: MEDIUM
source: "Healthcare IT literature synthesis"
last_verified: 2026-02-15
cross_referenced: false
tags: [claim, research]
---

# 80-99% false positive rate in healthcare alert systems

**Source:** Healthcare IT literature synthesis
**Confidence:** MEDIUM
**Verified by:** qa-agent

## Used In
- [[AR-011]]

## Invalidation Trigger
If contradicting evidence with comparable methodology emerges, flag all linked reports.


### 20_Areas/AI-Research/Claims/C007 — Each reminder reduces response rate by 30% (alert fatigue).md
---
type: claim
id: C007
confidence: MEDIUM
source: "Behavioral economics research"
last_verified: 2026-02-15
cross_referenced: false
tags: [claim, research]
---

# Each reminder reduces response rate by 30% (alert fatigue)

**Source:** Behavioral economics research
**Confidence:** MEDIUM
**Verified by:** qa-agent

## Used In
- [[AR-011]]

## Invalidation Trigger
If contradicting evidence with comparable methodology emerges, flag all linked reports.


### 20_Areas/AI-Research/Claims/C008 — Klarna saved $60M with AI agents but reversed deployment due.md
---
type: claim
id: C008
confidence: MEDIUM
source: "Public company statements + media reporting"
last_verified: 2026-02-15
cross_referenced: false
tags: [claim, research]
---

# Klarna saved $60M with [[AI]] agents but reversed deployment due to trust failures

**Source:** Public company statements + media reporting
**Confidence:** MEDIUM
**Verified by:** qa-agent

## Used In
- [[AR-012]]

## Invalidation Trigger
If contradicting evidence with comparable methodology emerges, flag all linked reports.


### 20_Areas/AI-Research/Claims/C009 — VW Cariad $7.5B loss attributed to AI orchestration complexi.md
---
type: claim
id: C009
confidence: MEDIUM
source: "Industry reporting + company announcements"
last_verified: 2026-02-15
cross_referenced: true
tags: [claim, research]
---

# VW Cariad $7.5B loss attributed to [[AI]] orchestration complexity

**Source:** Industry reporting + company announcements
**Confidence:** MEDIUM
**Verified by:** qa-agent

## Used In
- [[AR-007]]
- [[AR-010]]

## Invalidation Trigger
If contradicting evidence with comparable methodology emerges, flag all linked reports.


### 20_Areas/AI-Research/Claims/C010 — 96% of security breaches are disclosed by the attacker, not .md
---
type: claim
id: C010
confidence: MEDIUM
source: "Cybersecurity industry reports"
last_verified: 2026-02-15
cross_referenced: false
tags: [claim, research]
---

# 96% of security breaches are disclosed by the attacker, not internal detection

**Source:** Cybersecurity industry reports
**Confidence:** MEDIUM
**Verified by:** qa-agent

## Used In
- [[AR-010]]

## Invalidation Trigger
If contradicting evidence with comparable methodology emerges, flag all linked reports.


### 20_Areas/AI-Research/Claims/C011 — LangChain grew from 0 to 100k GitHub stars in approximately .md
---
type: claim
id: C011
confidence: MEDIUM
source: "GitHub star history (approximation)"
last_verified: 2026-02-15
cross_referenced: false
tags: [claim, research]
---

# LangChain grew from 0 to 100k GitHub stars in approximately 1 year

**Source:** GitHub star history (approximation)
**Confidence:** MEDIUM
**Verified by:** qa-agent

## Used In
- [[AR-013]]

## Invalidation Trigger
If contradicting evidence with comparable methodology emerges, flag all linked reports.


### 20_Areas/AI-Research/Claims/C012 — Vercel achieved $200M ARR via DX-first design philosophy.md
---
type: claim
id: C012
confidence: MEDIUM
source: "Public announcements + funding rounds"
last_verified: 2026-02-15
cross_referenced: false
tags: [claim, research]
---

# Vercel achieved $200M ARR via DX-first design philosophy

**Source:** Public announcements + funding rounds
**Confidence:** MEDIUM
**Verified by:** qa-agent

## Used In
- [[AR-013]]

## Invalidation Trigger
If contradicting evidence with comparable methodology emerges, flag all linked reports.


### 20_Areas/AI-Research/Claims/C013 — Air Canada held legally liable for chatbot hallucination.md
---
type: claim
id: C013
confidence: HIGH
source: "Court ruling 2024"
last_verified: 2026-02-15
cross_referenced: true
tags: [claim, research]
---

# Air Canada held legally liable for chatbot hallucination

**Source:** Court ruling 2024
**Confidence:** HIGH
**Verified by:** qa-agent

## Used In
- [[AR-010]]
- [[AR-001]]

## Invalidation Trigger
If contradicting evidence with comparable methodology emerges, flag all linked reports.


### 20_Areas/AI-Research/Claims/C014 — Grok RAG poisoning contaminated thousands of responses befor.md
---
type: claim
id: C014
confidence: HIGH
source: "Security disclosure 2024"
last_verified: 2026-02-15
cross_referenced: false
tags: [claim, research]
---

# Grok RAG poisoning contaminated thousands of responses before detection

**Source:** Security disclosure 2024
**Confidence:** HIGH
**Verified by:** qa-agent

## Used In
- [[AR-010]]

## Invalidation Trigger
If contradicting evidence with comparable methodology emerges, flag all linked reports.


### 20_Areas/AI-Research/Claims/C015 — Waymo required 7 collisions before issuing recall.md
---
type: claim
id: C015
confidence: HIGH
source: "NHTSA reporting + media"
last_verified: 2026-02-15
cross_referenced: false
tags: [claim, research]
---

# Waymo required 7 collisions before issuing recall

**Source:** NHTSA reporting + media
**Confidence:** HIGH
**Verified by:** qa-agent

## Used In
- [[AR-010]]

## Invalidation Trigger
If contradicting evidence with comparable methodology emerges, flag all linked reports.


### 20_Areas/AI-Research/Claims/Claims-Ledger.md
---
version: 1.0.1
status: current
review_date: 2026-03-19
owner: florian
type: claims-ledger
created: 2026-02-19
last_updated: 2026-02-19
total_claims: 15
---

# Claims Ledger

**Purpose:** Central repository for all research claims used across [[AI]] research reports and articles. Each claim is independently verified and cross-referenced to ensure factual accuracy and allow for systematic invalidation when contradicting evidence emerges.

**Version:** 1.0.1  
**Status:** Current  
**Owner:** Florian Ziesche  
**Review Date:** 2026-03-19

---

## Source Files (Consolidated)

This ledger consolidates the following 15 original claim files:

1. `C001 — 67% of security alerts are ignored by SOC analysts.md`
2. `C002 — 84% of [[LLM]] outputs are overconfident (verbalized confidence .md`
3. `C003 — Tool calling fails 3-15% of the time in production agent sys.md`
4. `C004 — 6% of companies achieve '[[AI]] High Performer' status with 2-3x.md`
5. `C005 — MemoryGraft attack achieves >95% memory injection success ra.md`
6. `C006 — 80-99% false positive rate in healthcare alert systems.md`
7. `C007 — Each reminder reduces response rate by 30% (alert fatigue).md`
8. `C008 — Klarna saved $60M with [[AI]] agents but reversed deployment due.md`
9. `C009 — VW Cariad $7.5B loss attributed to [[AI]] orchestration complexi.md`
10. `C010 — 96% of security breaches are disclosed by the attacker, not .md`
11. `C011 — LangChain grew from 0 to 100k GitHub stars in approximately .md`
12. `C012 — Vercel achieved $200M ARR via DX-first design philosophy.md`
13. `C013 — Air Canada held legally liable for chatbot hallucination.md`
14. `C014 — Grok RAG poisoning contaminated thousands of responses befor.md`
15. `C015 — Waymo required 7 collisions before issuing recall.md`

**Location:** `20_Areas/[[AI]]-Research/Claims/`  
**Original files:** Preserved (not deleted) for reference

---

## Table of Contents

1. [C001 — 67% of security alerts are ignored by SOC analysts](#c001--67-of-security-alerts-are-ignored-by-soc-analysts)
2. [C002 — 84% of [[LLM]] outputs are overconfident](#c002--84-of-[[LLM]]-outputs-are-overconfident)
3. [C003 — Tool calling fails 3-15% of the time in production](#c003--tool-calling-fails-3-15-of-the-time-in-production)
4. [C004 — 6% of companies achieve [[AI]] High Performer status](#c004--6-of-companies-achieve-ai-high-performer-status)
5. [C005 — MemoryGraft attack achieves >95% success rate](#c005--memorygraft-attack-achieves-95-success-rate)
6. [C006 — 80-99% false positive rate in healthcare alert systems](#c006--80-99-false-positive-rate-in-healthcare-alert-systems)
7. [C007 — Each reminder reduces response rate by 30%](#c007--each-reminder-reduces-response-rate-by-30)
8. [C008 — Klarna saved $60M but reversed [[AI]] agent deployment](#c008--klarna-saved-60m-but-reversed-ai-agent-deployment)
9. [C009 — VW Cariad $7.5B loss attributed to [[AI]] orchestration complexity](#c009--vw-cariad-75b-loss-attributed-to-ai-orchestration-complexity)
10. [C010 — 96% of security breaches disclosed by attacker](#c010--96-of-security-breaches-disclosed-by-attacker)
11. [C011 — LangChain grew to 100k GitHub stars in ~1 year](#c011--langchain-grew-to-100k-github-stars-in-1-year)
12. [C012 — Vercel achieved $200M ARR via DX-first philosophy](#c012--vercel-achieved-200m-arr-via-dx-first-philosophy)
13. [C013 — Air Canada held legally liable for chatbot hallucination](#c013--air-canada-held-legally-liable-for-chatbot-hallucination)
14. [C014 — Grok RAG poisoning contaminated thousands of responses](#c014--grok-rag-poisoning-contaminated-thousands-of-responses)
15. [C015 — Waymo required 7 collisions before issuing recall](#c015--waymo-required-7-collisions-before-issuing-recall)

---

## C001 — 67% of security alerts are ignored by SOC analysts

**Confidence:** HIGH  
**Source:** Vectra 2023 (n=2,000 SOC professionals)  
**Last Verified:** 2026-02-15  
**Verified By:** qa-agent  
**Cross-Referenced:** Yes

### Used In
- [[AR-010]]
- [[AR-011]]

### Invalidation Trigger
If contradicting evidence with comparable methodology emerges, flag all linked reports.

---

## C002 — 84% of [[LLM]] outputs are overconfident

**Full Claim:** 84% of [[LLM]] outputs are overconfident (verbalized confidence exceeds actual accuracy)

**Confidence:** HIGH  
**Source:** PMC/12249208 (9 models, 351 scenarios)  
**Last Verified:** 2026-02-15  
**Verified By:** qa-agent  
**Cross-Referenced:** Yes

### Used In
- [[AR-009]]
- [[AR-010]]
- [[AR-011]]

### Invalidation Trigger
If contradicting evidence with comparable methodology emerges, flag all linked reports.

---

## C003 — Tool calling fails 3-15% of the time in production

**Full Claim:** Tool calling fails 3-15% of the time in production agent systems

**Confidence:** MEDIUM  
**Source:** Michael Hannecke practitioner data + McDonald's case study  
**Last Verified:** 2026-02-15  
**Verified By:** qa-agent  
**Cross-Referenced:** No

### Used In
- [[AR-010]]

### Invalidation Trigger
If contradic

### 20_Areas/AI-Research/Findings-Snapshot.md
---
type: meta
status: current
updated: 2026-02-19
owner: mia
source: platform-api
---

# Findings Snapshot (Auto-Sync)

> Auto-generated from localhost:8080 on 2026-02-19. Do not edit manually.

**Total Findings:** 106

## High Confidence (≥0.85) (48)

- **RF-001** (conf: 0.90): Pre-Flight mit Regex fängt 80% der Output-Fehler bei 0 Kosten und <50ms
- **C002** (conf: 0.85): 84% of [[LLM]] outputs are overconfident (verbalized confidence exceeds actual accuracy)
- **C001** (conf: 0.85): 67% of security alerts are ignored by SOC analysts
- **C004** (conf: 0.85): 6% of companies achieve '[[AI]] High Performer' status with 2-3x productivity gains
- **C005** (conf: 0.85): MemoryGraft attack achieves >95% memory injection success rate
- **C013** (conf: 0.85): Air Canada held legally liable for chatbot hallucination
- **C014** (conf: 0.85): Grok RAG poisoning contaminated thousands of responses before detection
- **C015** (conf: 0.85): Waymo required 7 collisions before issuing recall
- **RF-074** (conf: 0.98): CONTRADICTION AUFGELÖST: Fully Autonomous Agents vs. Human-in-the-Loop. Production zeigt: HITL für irreversible Actions 
- **C-008** (conf: 0.98): AgentTrust ≠ Observability. LangSmith/Arize/Galileo tracen und monitoren — KEINER kalibriert. AgentTrust ist Calibration
- **RF-026** (conf: 0.95): Gewichteter Durchschnitt (a*0.7 + b*0.3) ist KEIN Bayesian Update. Echte Formel: P(H|E) = P(E|H)·P(H) / [P(E|H)·P(H) + P
- **RF-059** (conf: 0.95): ReAct (Think→Act→Observe→Repeat) ist das Fundament für Agent-Architekturen. Score 100/100 (Buildability 10 × Relevance 1
- **RF-075** (conf: 0.95): ReAct Implementation Pattern: while not task_complete: thought → action → observation → context.add(). Max-Iteration-Lim
- **RF-078** (conf: 0.95): RAG Implementation Pattern: Index (docs → embeddings → vector DB) → Retrieve (query → top-K chunks) → Augment (chunks + 
- **RF-067** (conf: 0.93): Production Failure: Free-Form [[LLM]] Outputs ohne Validation halluzinieren. Structured Outputs (JSON Schema Validation) sin
- **RF-063** (conf: 0.92): Production Agentic Workflows: 4 Core Patterns funktionieren (Reflection, Tool Use/ReAct, Planning, Multi-Agent). Score 1
- **RF-064** (conf: 0.92): Production Failure: Fully Autonomous Agents ohne Human-Oversight scheitern. Agents machen Fehler die eskalieren. HITL Ch
- **RF-070** (conf: 0.92): Production Failure: Tool-Use ohne Whitelisting ist Security-Risiko. Prompt Injection kann Agents manipulieren. Least-Pri
- **RF-025** (conf: 0.90): Native browser prompt() zerstört UX-Flow und signalisiert Amateur-Level. Inline Modal mit Fokus-Management ist Standard.
- **RF-029** (conf: 0.90): Research VOR Implementierung ist nicht optional. 15min Research hätte 40min Rework gespart (fake Bayesian, prompt() stat
- **RF-031** (conf: 0.90): Ein Wissens-System das vom Erbauer nicht benutzt wird, wird von niemandem benutzt. Dogfooding ist der erste Test. Wenn i
- **RF-046** (conf: 0.90): MCP (Model Context Protocol) has 10,000+ active public servers and 97M+ monthly SDK downloads — de facto standard for ag
- **RF-048** (conf: 0.90): Full autonomous software engineering still not here — agents need human-in-the-loop for complex decisions
- **RF-049** (conf: 0.90): [[AI]] startup funding reached $202B globally in 2025 (+75% YoY), capturing ~50% of all [[VC]] funding
- **RF-053** (conf: 0.90): Agent Teams für Investigative Journalism: Parallele Agents ([[Claude]] Opus 4.6) koordinieren autonome Recherche — Agent 1: 
- **RF-054** (conf: 0.90): Workflow Memory für CNC-Kalkulation: Wang et al. Workflow Memory Paper (Sept 2024) auf Fertigungskalkulation anwenden — 
- **RF-055** (conf: 0.90): Browser Use für OZG-Automatisierung: Open-source Browser Use Framework für OZG-Integration ohne APIs — Agent bedient leg
- **RF-060** (conf: 0.90): MemGPT (Context-Window als Virtual Memory mit Main/Storage/Paging) ist ESSENTIAL für Long-Running Agents. Score 80/100. 
- **RF-061** (conf: 0.90): Reflexion (verbales Reinforcement Learning: Execute→Feedback→Reflect→Retry) ermöglicht Agents aus Fehlern zu lernen OHNE
- **RF-062** (conf: 0.90): MCP (Model Context Protocol) ist der offene Standard für Agent-Tool-Integration. Score 90/100. Linux Foundation Agentic 
- ... and 18 more

## Medium (0.60-0.84) (36)

- **RF-002** (conf: 0.73): Bayesian Trust Scoring konvergiert schneller als lineares +2/-3 bei kleinen Stichproben
- **C009** (conf: 0.60): VW Cariad $7.5B loss attributed to [[AI]] orchestration complexity
- **C003** (conf: 0.60): Tool calling fails 3-15% of the time in production agent systems
- **C006** (conf: 0.60): 80-99% false positive rate in healthcare alert systems
- **C007** (conf: 0.60): Each reminder reduces response rate by 30% (alert fatigue)
- **C008** (conf: 0.60): Klarna saved $60M with [[AI]] agents but reversed deployment due to trust failures
- **C010** (conf: 0.60): 96% of security breaches are disclosed by the attacker, not internal detection
- **C011** (conf: 0.60): LangChain grew from 0 to 100k G

### 20_Areas/AI-Research/Paper-Tracker.md
---
type: tracker
status: active
created: 2026-02-19
review_date: 2026-03-19
tags: [research, papers, sota, agent-trust]
---

# AI Research Paper Tracker

**Purpose:** Track papers relevant to AgentTrust, Ainary, and AI agent development.  
**Review Cycle:** Monthly (next review: 2026-03-19)  
**Tagging:** Papers move through Reading Queue → In Progress → Completed

---

## Reading Queue

Papers identified but not yet read in full.

### Memory in the Age of AI Agents
- **Status:** 📥 Queued  
- **Link:** https://arxiv.org/abs/2512.13564  
- **Authors:** Yuyang Hu, Shichun Liu, Guibin Zhang et al.  
- **Date:** Dec 2025 (updated Jan 2026)  
- **Type:** Survey  
- **Why relevant:** Comprehensive memory taxonomy (token/parametric/latent), identifies trustworthiness as research frontier  
- **Priority:** HIGH — Informs AgentTrust memory tracking architecture  
- **Added:** 2026-02-19

### Agentic Memory (AgeMem)
- **Status:** 📥 Queued  
- **Link:** https://arxiv.org/abs/2601.01885  
- **Authors:** Yi Yu et al.  
- **Date:** Jan 2026  
- **Type:** Implementation (code available)  
- **Why relevant:** Unified LTM+STM management via RL, memory as tool-based actions  
- **Priority:** HIGH — Implementation pattern for Ainary agent memory  
- **Added:** 2026-02-19

### OpenSec: Incident Response Agent Calibration
- **Status:** 📥 Queued  
- **Link:** https://arxiv.org/abs/2601.21083  
- **Authors:** Jarrod Barnes et al.  
- **Date:** Jan 2026 (updated Feb 2026)  
- **Type:** Benchmark + Code (https://github.com/jbarnes850/opensec-env)  
- **Why relevant:** DIRECTLY measures trust calibration under adversarial conditions — our core problem  
- **Priority:** CRITICAL — Potential validation benchmark for AgentTrust  
- **Added:** 2026-02-19  
- **Action:** Contact author for collaboration

### TRiSM for Agentic AI
- **Status:** 📥 Queued  
- **Link:** https://arxiv.org/html/2506.04133v5  

## YOUR TASK
Synthesize the sub-reports into ONE report. Rules:

1. **NO NEW FACTS** — only combine what's in the sub-reports + CRTs. If it's not sourced, mark [J].
2. **DESIGN A CUSTOM FRAMEWORK** — one original model that shows relationships across sub-questions.
   Name it. Make it drawable. Map findings to it.
3. **E/I/J/A LABELS** — in the Claim Ledger (appendix). Prose must flow narratively.
4. **NARRATIVE STYLE** — like V3 (engaging opener, case studies inline, section confidence).
   Start with something an expert DOESN'T already know.
5. **"SO WHAT" per section** — every section ends with "For the decision maker: ..."
6. **RECOMMENDATIONS** — phased (Week 1 / Month 1 / Quarter 1). Specific.
   Include "Do Not Deploy If" (5 conditions). Include "If Wrong:" for each recommendation.
7. **SELF-CALIBRATING** — apply the trust methods this report describes to itself.

## STRUCTURE
1. Beipackzettel (confidence, risk level, E/I/J/A distribution, sources, uncertainties, risks)
2. Executive Summary (SCR, 3 paragraphs + "If you read nothing else" bullets)
3. Custom Framework (describe so reader can draw it)
4. Key Findings (5-7, narrative, case studies woven in, section confidence %)
5. Recommendations (Decision Matrix + Phased Plan + "Do Not Deploy If")
6. Risks & "What Would Change This"
7. Appendix: Claim Ledger (12 claims, E/I/J/A, [S#], confidence) + Source Log + Contradictions

## QUALITY CHECK (verify before output)
- [ ] Opener: would an expert learn something new?
- [ ] Every section has "So What"
- [ ] Custom Framework is original (not from any source)
- [ ] >50% E labels, <20% J labels
- [ ] Phased plan: reader can start Monday
- [ ] No claims without [S#] or [J] label
- [ ] Self-calibration applied

NO: landscape, tapestry, delve, synergy, cutting-edge, game-changer
Target: 5000-8000 words.


## DOCUMENTED BLINDSPOTS (include in Appendix)
- **What if calibration becomes a commodity feature that cloud providers bundle for free, making standalone infrastructure unsellable?**
  Why overlooked: We're assuming calibration remains specialized enough to command premium pricing, but AWS/Azure might commoditize it like they did with ML monitoring - especially since basic methods cost <$0.05/decision (CT-018).
  Confidence: 85% | YES — priority 2
- **Could the insurance industry's approach to AI liability make technical calibration irrelevant compared to legal/financial risk transfer mechanisms?**
  Why overlooked: We're focused on technical accuracy while insurers might solve the trust problem through financial products - similar to how cyber insurance evolved separately from security technology.
  Confidence: 70% | YES — priority 2
- **What if human users systematically ignore or misuse calibration signals, making technical accuracy improvements meaningless for actual decision outcomes?**
  Why overlooked: CT-011 shows confidence scores alone don't improve decision-making, and CT-012 highlights the gap between technical UQ and human needs. We might be solving the wrong layer of the problem.
  Confidence: 75% | MAYBE


## PYTHON VALIDATION RESULTS (trust GOOD reports more, be skeptical of WEAK ones)
- SQ-1: GOOD (E:5 I:1 J:0, 6 sources)
- SQ-2: WEAK — fewer sources, more judgments (E:1 I:2 J:2, 3 sources)
- SQ-3: GOOD (E:3 I:2 J:0, 5 sources)
- SQ-4: GOOD (E:2 I:2 J:1, 5 sources)
- SQ-5: GOOD (E:2 I:2 J:2, 4 sources)

## EXTRACTED CLAIMS (verified by Sonnet)
- [E] Current calibration methods like temperature scaling require access to model log ([S1], A1)
- [E] Multi-step agent calibration is unsolved, as current methods like Conformal Unce ([S9], A1)
- [E] Reinforcement Learning from Human Feedback (RLHF) can damage calibration, with s ([S30], A1)
- [E] The EU AI Act mandates compliance by August 2026, impacting high-risk sectors li ([S14], A1)
- [I] The healthcare sector shows significant calibration challenges, indicating a rea ([S8], A1)
- [I] The cost of calibration methods is low, suggesting potential readiness in sector ([S19], A1)
- [E] Temperature scaling is a foundational calibration method requiring logit access. ([S1], A1)
- [E] Budget-CoCoA is a practical calibration method not explicitly offered by IBM, Mi ([S3], A1)
- [I] RLHF can damage calibration, posing a challenge for IBM, Microsoft, and Google i ([S7], A1)
- [E] Implementing temperature scaling, a common calibration method, requires access t ([S1], A1)
- [E] The practical cost of using Budget-CoCoA, a calibration method, ranges from $0.0 ([S19], B2)
- [I] Conformal prediction for LLMs requires 200-500 examples for effective calibratio ([S9], C3)
- [E] The EU AI Act, which will be enforced starting August 2026, requires AI systems  ([S14], C3)
- [I] Calibration is a critical component in AI systems for ensuring trustworthiness a ([S1, S8], C3)
- [E] Budget-CoCoA, a practical method for calibrating LLM confidence scores, is cost- ([S19], C3)

## CONTRADICTIONS FOUND
- The EU AI Act requires accuracy but not calibratio VS The EU AI Act, effective August 2026, mandates com — Claim A suggests a gap in the EU AI Act regarding calibration, while Claim B implies comprehensive compliance requirements, including accuracy and oversight, without mentioning calibration as a gap.
- Temperature scaling is a foundational calibration  VS Implementing temperature scaling, a common calibra — Claim A presents temperature scaling as a foundational method without discussing complexity, while Claim B highlights the technical expertise required for its implementation.

## SUB-REPORT REVIEWS
- SQ-1: 4/6 | Issue: Inconsistency in evidence quality and lack of context about 
- SQ-2: 5/6 | Issue: The sub-report lacks sufficient direct evidence to support c
- SQ-3: 0/6 | Issue: parse error
- SQ-4: 3/6 | Issue: Lack of detailed context and clarity regarding sources and e
- SQ-5: 5/6 | Issue: Lack of detailed information on the CEN/CENELEC standards de


If a sub-report is marked WEAK: use its findings only if corroborated by another sub-report or CRT.
If a sub-report is marked GOOD: trust its [E] labeled findings.
