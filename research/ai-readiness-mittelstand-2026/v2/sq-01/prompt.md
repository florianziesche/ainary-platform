You are a research analyst answering ONE specific question with evidence.

## YOUR QUESTION
Which German Mittelstand sectors deploy AI systems that fall under EU AI Act high-risk categories (Annex III) or transparency requirements (Art. 50)?

## WHY IT MATTERS
Determines addressable market size and urgency of compliance needs by August 2026.

## EVIDENCE NEEDED
Industry reports on AI adoption by German SMEs, EU AI Act applicability analyses for manufacturing/logistics/healthcare, BDI/VDMA position papers on AI regulation impact

## WEB SEARCH RESULTS (from Brave — real, current)
### BDI VDMA "künstliche intelligenz" regulierung mittelstand 2024
- Künstliche Intelligenz: Chancen für Wirtschaft und Gesellschaft: Der BDI setzt sich seit dem Legislativvorschlag der Europäischen Kommission im April 2021 <strong>bis zum Inkrafttreten des Acts voraussichtlich im Juni 2024 (und teilweise darüber hinaus) für die Industriebedarfe bei der Regulierung von KI ein</strong>, indem ... (https://bdi.eu/artikel/news/kuenstliche-intelligenz-bedrohungsszenario-oder-chance)
- Künstliche Intelligenz - BDI: Künstliche Intelligenz (KI) ist eine zentrale Schlüsseltechnologie der Industrie, mit der ein hohes Wertschöpfungspotenzial verbunden ist. Um dieses Potenzial ausschöpfen zu können, sind die Unternehmen zum einen auf innovationsfreundliche rechtliche Rahmenbedingungen für den Einsatz von KI in Europa angewiesen. (https://bdi.eu/themenfelder/digitalisierung/kuenstliche-intelligenz)
- in Kooperation mit Leitfaden Künstliche Intelligenz –: und deutschen Mittelstands erhalten und sogar ausbauen. Der vorliegende Leitfaden hat zum Ziel, ein gemeinsames Verständnis zu Künstlicher · Intelligenz und deren Umsetzung im Unternehmen zu schaffen. (https://www.vdma.eu/documents/34570/1052572/Leitfaden+K%C3%BCnstliche+Intelligenz-Potenziale+und+Umsetzungen+im+Mittelstand.pdf/ce38a591-68cb-9775-101e-d7cad064b149?t=1615364023575)
- Künstliche Intelligenz - vdma.org - VDMA: Kleinteilige Regulierungen dürfen hier nicht im Wege stehen. ... In turbulenten Zeiten sind gute Handelsbeziehungen ebenso wichtig wie Innovationen. Mit dem Gastland Kanada und dem Fokus auf den Einsatz von Künstlicher Intelligenz in der Produktion hat die Hannover Messe 2025 die richtigen Signale gesetzt. ... Die KI-Verordnung ist am 2. August 2024 in Kraft getreten. (https://ki.vdma.org/)
- Mittelstand fordert Planungssicherheit für Investitionen in Künstliche Intelligenz - Einigung im AI-Act: BVMW e. V. und BVDW setzen sich ... und Innovationen für KMU zu ermöglichen. <strong>Eine rasche Einigung vor der Europawahl 2024 ist wichtig, um Unsicherheit zu vermeiden</strong>.... (https://www.verbandsbuero.de/mittelstand-fordert-planungssicherheit-fuer-investitionen-in-kuenstliche-intelligenz-einigung-im-ai-act/)

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
### Answer to: Which German Mittelstand sectors deploy AI systems that fall under EU AI Act high-risk categories (Annex III) or transparency requirements (Art. 50)?

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
