You are a research analyst answering ONE specific question with evidence.

## YOUR QUESTION
What are the technical breakthroughs in 2024-2025 that enable production-ready confidence propagation for multi-step agentic RAG systems?

## WHY IT MATTERS
Without solving multi-agent confidence propagation (currently unsolved per CT-027), agentic RAG will produce overconfident outputs that violate EU AI Act Article 14 requirements

## EVIDENCE NEEDED
Papers demonstrating: (1) compositional conformal prediction for dependent pipeline stages, (2) production implementations of SAUP/HTC frameworks, (3) benchmarks showing calibration preservation across 5+ agent steps

## WEB SEARCH RESULTS (from Brave — real, current)
### compositional conformal prediction multi-agent systems 2024 2025
- Conformal Off-Policy Prediction for Multi-Agent Systems | Request PDF: Subsequently, we relax the underlying stochastic optimal control problem by tightening the robustness functions of collaborative tasks based on their Lipschitz constants and the computed error bounds. To address scalability, we exploit the compositional structure of the multi-agent STL formula and propose a model-predictive-control-like algorithm, where agent-level problems are solved in a distributed fashion. (https://www.researchgate.net/publication/389376330_Conformal_Off-Policy_Prediction_for_Multi-Agent_Systems)
- [2403.16871] Conformal Off-Policy Prediction for Multi-Agent Systems: In this work, we introduce <strong>MA-COPP, the first conformal prediction method to solve OPP problems involving multi-agent systems</strong>, deriving joint prediction regions for all agents&#x27; trajectories when one or more ego agents change their policies. (https://arxiv.org/abs/2403.16871)
- Conformal Off-Policy Prediction for Multi-Agent Systems: Existing COPP methods can account for the distribution shifts induced by policy switching, but are limited to single-agent systems and scalar outcomes (e.g., rewards). In this work, we introduce <strong>MA-COPP, the first conformal prediction method to solve OPP problems involving multi-agent systems</strong>, ... (https://arxiv.org/html/2403.16871v1)
- Conformal Off-Policy Prediction for Multi-Agent Systems | AI Research Paper Details: To address this, the researchers propose a conformal prediction approach. Conformal prediction is <strong>a technique that provides reliable predictions with well-calibrated uncertainty estimates, even when the data distribution changes</strong>. (https://www.aimodels.fyi/papers/arxiv/conformal-off-policy-prediction-multi-agent-systems)
- Conformal Prediction: A Data Perspective | ACM Computing Surveys: Conformal prediction (CP), <strong>a distribution-free uncertainty quantification (UQ) framework, reliably provides valid predictive inference for black-box models</strong>. CP constructs prediction sets or interva... (https://dl.acm.org/doi/10.1145/3736575)

### SAUP HTC confidence propagation production implementation
- SAUP: Situation Awareness Uncertainty Propagation on LLM Agent: From equation 1, we can see that ... methods. In the practical implementation, we <strong>utilize the normalized entropy Malinin and Gales (2020), with some modifications to adapt it to the characteristics of the React Agent pipeline</strong>.... (https://arxiv.org/html/2412.01033)
- [2412.01033] SAUP: Situation Awareness Uncertainty Propagation on LLM Agent: SAUP <strong>incorporates situational awareness by assigning situational weights to each step&#x27;s uncertainty during the propagation</strong>. Our method, compatible with various one-step uncertainty estimation techniques, provides a comprehensive and accurate ... (https://arxiv.org/abs/2412.01033)
- (PDF) SAUP: Situation Awareness Uncertainty Propagation on LLM Agent: Here, we employ a Hidden Markov Model (HMM) to estimate the situational weight based on the distances D a and D o . Top Right shows the process of weighted uncertainty propagation, where we aggregate the one-step uncertainty and the corresponding situational weight to derive the agent&#x27;s overall uncertainty. ... Visualization analysis of SAUP on the StrategyQA dataset. (https://www.researchgate.net/publication/386374074_SAUP_Situation_Awareness_Uncertainty_Propagation_on_LLM_Agent)
- Agentic Uncertainty Quantification: This effectively propagates uncertainty forward in time, allowing the agent to dynamically adjust its behavior based on the accumulated uncertainty in its memory. To implement System 1 without fine-tuning, we employ a Confidence Elicitation Protocol by appending a structured instruction to the inference prompt, requiring the agent to output a confidence score (https://arxiv.org/html/2601.15703)
- Uncertainty propagation in data processing systems | the morning paper: If you’re downing a quick espresso, ... or false confidence. If you’re savouring a cortado, then you might also want to dip into the techniques we can use to propagate uncertainty through a computation. If you’re lingering over a latte, then the UP (Uncertainty Propagation) framework additionally shows how to integrate these techniques into a dataflow framework. We implement this framework ... (https://blog.acolyer.org/2018/11/23/uncertainty-propagation-in-data-processing-systems/)

### agentic RAG calibration benchmark multi-step confidence
- Agentic or Tool use - Ragas: <strong>This metric is particularly useful for validating that agents call the right tools with the right parameters in multi-step workflows</strong>. The metric requires user_input (conversation messages) and reference_tool_calls (expected tool calls). It returns a score between 0 and 1, where higher values ... (https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/agents/)
- MMA-RAG: A Survey on Multimodal Agentic Retrieval- ...: employs metrics such as Expected Calibration Error (ECE), Overconfidence Ratio (OCR), and · Confidence-Correctness Correlation (CCC), and leverages CLIP-based (Radford et al., 2021) image retrieval with iterative re-evaluation to correct overconfidence, yielding substantial ... LayoutPrompter (Lin et al., 2023). ... problems, as illustrated in Figure 5. These patterns are not mutually exclusive but represent distinct ... Figure 5: Dominant agentic design patterns in MMA-RAG frameworks. (https://hal.science/hal-05322313/document)
- Reliable Agentic RAG with LLM Trustworthiness Estimates: Agentic RAG with the TLM offers a promising step toward this future of reliable AI. Get started with the TLM tutorials. Read benchmarks measuring the effectiveness of LLM trustworthiness scores. (https://cleanlab.ai/blog/reliable-agentic-rag/)
- [2601.15778] Agentic Confidence Calibration: To address these challenges, we introduce, for the first time, the problem of Agentic Confidence Calibration and propose Holistic Trajectory Calibration (HTC), a novel diagnostic framework that extracts rich process-level features ranging from macro dynamics to micro stability across an agent&#x27;s entire trajectory. Powered by a simple, interpretable model, HTC consistently surpasses strong baselines in both calibration and discrimination, across eight benchmarks, multiple LLMs, and diverse agent frameworks. (https://arxiv.org/abs/2601.15778)
- Agentic Confidence Calibration: AI agents are rapidly advancing from passive language models to autonomous systems executing complex, multi-step tasks. Yet their overconfidence in failure remains a fundamental barrier to deployment in high-stakes settings. Existing calibration methods, built for static single-turn outputs, cannot address the unique challenges of agentic systems, such as compounding errors along trajectories, uncertainty from external tools, and opaque failure modes. To address these challenges, we introduce, for the first time, the problem of Agentic Confidence Calibration and propose Holistic Trajectory Calibration (HTC), a novel diagnostic framework that extracts rich process-level features ranging from macro dynamics to micro stability across an agent’s entire trajectory. (https://arxiv.org/html/2601.15778)

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
### Answer to: What are the technical breakthroughs in 2024-2025 that enable production-ready confidence propagation for multi-step agentic RAG systems?

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
