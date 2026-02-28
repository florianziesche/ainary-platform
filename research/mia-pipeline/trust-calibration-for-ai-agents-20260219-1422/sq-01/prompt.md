You are a research analyst answering ONE specific question with evidence.

## YOUR QUESTION
What specific calibration capabilities do AI agents need that don't exist today, and which gaps represent IP opportunities?

## WHY IT MATTERS
Identifies where Ainary can build defensible technology versus commoditized solutions, given that multi-step agent calibration is unsolved (CT-027) while single-turn has partial solutions (CT-019).

## EVIDENCE NEEDED
Patents filed on agent calibration methods, technical limitations in current frameworks (SAUP/HTC), specific failure modes in production agent systems

## WEB SEARCH RESULTS (from Brave — real, current)
No web results.

## VERIFIED REFERENCES (cite as [S#])
[S1] On Calibration of Modern Neural Networks (ICML 2017, Tier 1): Temperature scaling + ECE metric definition. Gold standard but requires logit access. DOI: 10.48550/arXiv.1706.04599
[S2] Self-Consistency Improves Chain of Thought Reasoning (ICLR 2023, Tier 1): Self-consistency method foundation. Sample N paths, majority vote. DOI: 10.48550/arXiv.2203.11171
[S3] Can LLMs Express Their Uncertainty? (ICLR 2024, Tier 1): Verbalized confidence is biased. Budget-CoCoA: 3 API calls measure agreement. DOI: 10.48550/arXiv.2306.13063
[S5] On the Robustness of Verbal Confidence in Adversarial Attacks (NeurIPS 2025, Tier 1): Verbalized confidence most adversarially vulnerable. Defense techniques largely ineffective.
[S7] Taming Overconfidence in LLMs: Reward Calibration in RLHF (NeurIPS 2024, Tier 1): RLHF systematically damages calibration. Reward models prefer confident responses.
[S8] Calibration as Measurement of Trustworthiness in Biomedical NLP (PMC12249208, Tier 1): Consistency ECE 27.3% vs verbalized 42% across 13 datasets. 84% of scenarios show overconfidence. BIOMEDICAL ONLY. DOI: PMC12249208 | CAVEAT: Numbers from biomedical QA, not verified cross-domain
[S9] ConU: Conformal Uncertainty in LLMs (NeurIPS 2024, Tier 1): Conformal prediction for LLMs. Needs 200-500 examples. Guarantees do NOT compose for multi-agent.
[S14] EU AI Act (Official Journal EU, Tier 1): Art 15 requires 'accuracy', NOT 'calibration'. Art 14 requires human oversight. Enforcement Aug 2026. DOI: Official
[S15] Complacency and Bias in Human Use of Automation (Human Factors 2010, Tier 1): Human vigilance drops 20-50% after 30 min monitoring automated systems. DOI: 10.1177/0018720810376055
[S19] 5 Methods for Calibrating LLM Confidence Scores (Blog 2025, Tier 3): Budget-CoCoA practical cost: $0.0005-$0.015/check depending on model. | CAVEAT: Practitioner source, not academic
[S21] Agentic Confidence Calibration (HTC) (arXiv Jan 2026, Tier 2): Trajectory calibration for agents. GAC achieves lowest ECE on GAIA (out-of-domain). No open-source implementation. DOI: arXiv:2601.15778 | CAVEAT: Preprint, not peer-reviewed
[S26] BaseCal (arXiv Jan 2026, Tier 2): 42.9% ECE reduction via hidden state projection to base model space. Recovers calibration WITHOUT losing helpfulness. DOI: arXiv:2601.03042 | CAVEAT: Preprint
[S27] SAUP: Situational Awareness Uncertainty Propagation (ACL 2025, Tier 1): Formalizes intra-chain uncertainty propagation with situational awareness weights.
[S30] Restoring Calibration for Aligned LLMs (ICML 2025, Tier 1): Calibratable vs non-calibratable regimes. Some models permanently damaged by RLHF, others recoverable.

## RULES
1. ONLY use evidence from the web results and references above
2. Cite EVERY claim with [S#] or source URL
3. If no evidence found: say "No evidence found" — do NOT invent
4. Label each finding:
   [E] Evidenced — directly from source with citation
   [I] Interpreted — inferred from sources, explain logic
   [J] Judged — your assessment, no direct source
5. End with "SO WHAT: ..." (1-2 sentences for the decision maker)
6. Max 800 words. Be dense, not verbose.

## OUTPUT STRUCTURE
### Answer to: What specific calibration capabilities do AI agents need that don't exist today, and which gaps represent IP opportunities?

**Key Findings:**
- Finding 1 [E/I/J] [S#]
- Finding 2 ...

**Evidence Quality:**
- Strongest source: ...
- Weakest point: ...
- What's missing: ...

**So What:** ...

**Claims (for Claim Ledger):**
- Claim 1 | [S#] | E/I/J | Admiralty | Confidence
- Claim 2 | ...
