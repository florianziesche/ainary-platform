You are a research analyst answering ONE specific question with evidence.

## YOUR QUESTION
What are the emergent failure modes of agentic RAG systems when confidence calibration breaks down across organizational boundaries?

## WHY IT MATTERS
SAUP/HTC frameworks don't compose across organizational boundaries (CX-001), creating systemic risks when agents from different vendors interact

## EVIDENCE NEEDED
Research showing: (1) inter-organizational agent communication failures, (2) confidence signal incompatibility incidents, (3) liability precedents for multi-vendor agent failures

## WEB SEARCH RESULTS (from Brave — real, current)
### multi-vendor agent system failures confidence calibration 2024
- Agentic Confidence Calibration: An early, low-confidence decision-such as erroneously selecting a tool, can “poison” the entire subsequent execution path, leading to an agent holding high confidence in a completely incorrect result. Second, agents introduce new, external sources of uncertainty through their interaction with tools and environments (Liu et al., 2024a). API failures, noisy data returned by tools, or the misuse of a tool’s functionality create new reliability bottlenecks independent of the model’s internal knowledge. Finally, the multi-step nature of agentic processes makes failure modes more opaque. (https://arxiv.org/html/2601.15778)
- Refine and Align: Confidence Calibration through Multi-Agent Interaction in VQA: 2024). This over- confidence undermines the reliability and interpretability of (https://arxiv.org/pdf/2511.11169)
- Evaluations for the agentic world | by QuantumBlack, AI by McKinsey | QuantumBlack, AI by McKinsey | Jan, 2026 | Medium: <strong>The potential for risk and failure expands as systems move from single-model responses to multi-step coordination across agents</strong>. Confidence in these systems depends on understanding not only what they produce, but how outcomes emerge over time ... (https://medium.com/quantumblack/evaluations-for-the-agentic-world-c3c150f0dd5a)
- Why Do Multi-Agent LLM Systems Fail?: Detailed definition and example of each failure mode is available in Appendix A. Despite increasing adoption of MAS, <strong>the gain in accuracy or performance remains minimal compared to single agent frameworks</strong> (Xia et al., 2024) or even simple baselines such as best-of-N sampling on popular benchmarks ... (https://arxiv.org/html/2503.13657v1)
- Why Your Multi-Agent System is Failing: Escaping the 17x Error Trap of the “Bag of Agents” | Towards Data Science: In the same way we defined common Agent archetypes, we can undertake a similar exercise for their tools. <strong>Tool archetypes define how that work is grounded, executed, and verified and which failure modes are contained as the system scales</strong>. (https://towardsdatascience.com/why-your-multi-agent-system-is-failing-escaping-the-17x-error-trap-of-the-bag-of-agents/)

### agentic AI liability cross-organizational boundaries
- When AI Acts Independently: Legal Considerations for Agentic AI Systems | Jones Walker LLP: Cross-Border Risk Assessment: <strong>Develop frameworks for managing liability and compliance when agentic systems operate across multiple jurisdictions</strong>, including clear protocols for determining applicable law and regulatory authority. (https://www.joneswalker.com/en/insights/blogs/ai-law-blog/when-ai-acts-independently-legal-considerations-for-agentic-ai-systems.html?id=102kdl4)
- The rise of “agentic” AI: Potential new legal and organizational risks | DLA Piper: Agents act 24/7 at scale: <strong>Agentic AI scales legal and compliance risk by acting around the clock in a distributed manner</strong>. This could increase the potential for unintended consequences and make it more challenging to detect misalignment with ... (https://www.dlapiper.com/en/insights/publications/ai-outlook/2025/the-rise-of-agentic-ai--potential-new-legal-and-organizational-risks)
- AI governance in the agentic era | IAPP: The guardrails may also include recording each system’s intended goals, boundaries, and limitations and incorporate safety features, secure access and internal explainability tools. Organizations should evaluate and revise pre-existing AI guardrails to address the risks agentic AI may introduce. (https://iapp.org/resources/article/ai-governance-in-the-agentic-era)
- Liability Considerations for Developers and Users of Agentic AI Systems - Lathrop GPM: Developers and deployers alike must proactively address the unique risks these systems pose, particularly around autonomy, delegation of authority and liability. Clear contractual terms, robust internal policies, and thoughtful system design – including human oversight and configurable permissions – are essential to mitigating potential harms. As case law continues to develop, organizations that anticipate and plan for these challenges will be better positioned to leverage the benefits of agentic AI while minimizing exposure to legal and reputational risks. (https://www.lathropgpm.com/insights/liability-considerations-for-developers-and-users-of-agentic-ai-systems/)
- A Complete Guide to Agentic AI Governance - Palo Alto Networks: Responsibility may span model providers, platform operators, and deploying organizations. Which is why clear role definition becomes essential. ... Governance has to extend beyond model alignment into runtime action control. AI agents expand the scope of operational risk. They don&#x27;t only generate outputs. They execute actions inside live systems. As authority increases, so does impact. However, not all risk looks the same. Some risks involve execution boundaries. (https://www.paloaltonetworks.com/cyberpedia/what-is-agentic-ai-governance)

### RAG system integration confidence signal compatibility
- Build Custom RAG Systems With Logic & Control | n8n Automation Platform: AI Evaluations let you measure your RAG’s performance by running a test dataset through your workflow. Calculating metric scores for each output gives you the confidence that your RAG agent actually retrieves reliable information. (https://n8n.io/rag/)
- Enterprise RAG: How to Build a RAG System | Guide: Best Practice: Implement backup detection and confidence scoring so the system can gracefully decline when knowledge coverage is missing. Sometimes, the correct answer is in the database, but it doesn’t make into the top K retrieved results. This usually occurs due to embedding mismatches or ranking thresholds. Best Practice: Use dynamic top-K tuning, hybrid (vector + keyword) retrieval, and reranking models to surface the most relevant content even when the signal is weak. (https://azumo.com/artificial-intelligence/ai-insights/build-enterprise-rag-system)
- A Complete Guide to Retrieval-Augmented Generation: This dynamic integration reduces both computational requirements and financial overhead. Improved user trust and transparency: RAG systems provide clear citations and source attribution. This allows the user to verify the information and builds confidence in the AI’s outputs by clearly showing where the data comes from. (https://www.domo.com/blog/a-complete-guide-to-retrieval-augmented-generation)
- RAG Systems Need RAG Quality: When users correct an answer or identify a risky suggestion, those signals should feed back into content curation, retrieval tuning, and prompt patterns. Over time, the system becomes more accurate and more aligned with organizational judgment. From Valutics’ perspective, “RAG quality” sits at the intersection of content integrity, retrieval intelligence, and human-in-the-loop governance. (https://www.valutics.com/post/rag-systems-need-rag-quality)
- Reduced RAG: Stop Stuffing Context Windows and Start Extracting Signals (English): Text is still part of the system - but it becomes evidence, not &quot;whatever we happened to paste into the prompt&quot;. This is the difference between &quot;RAG answers are vibes&quot; and &quot;RAG answers are inspectable&quot;. You don&#x27;t. Not upfront. That&#x27;s the whole point of storing raw signals instead of LLM-processed summaries. (https://mostlylucid.net/blog/reduced-rag)

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
### Answer to: What are the emergent failure modes of agentic RAG systems when confidence calibration breaks down across organizational boundaries?

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
