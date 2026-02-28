You are a research analyst answering ONE specific question with evidence.

## YOUR QUESTION
What are the technical integration requirements and costs for implementing calibration in typical Mittelstand AI deployments (ERP, MES, quality control)?

## WHY IT MATTERS
Determines feasibility of <€5000/month target pricing and technical support requirements.

## EVIDENCE NEEDED
Technical architectures of common German industrial AI systems, API documentation for SAP/Siemens/KUKA AI modules, implementation case studies from similar markets

## WEB SEARCH RESULTS (from Brave — real, current)
### SAP S/4HANA AI calibration integration API documentation
- APIs | SAP S/4HANA: SAP Business Accelerator Hub - Explore, discover and consume APIs, pre-packaged Integrations, Business Services and sample apps (https://api.sap.com/products/SAPS4HANA/apis/packages)
- Complete Guide to SAP S/4HANA APIs: REST and SOAP Integration Tutorial: <strong>The SAP API Business Hub (https://api.sap.com)</strong> is your single source of truth. This isn&#x27;t just documentation. It&#x27;s an interactive environment where you can test APIs against sandbox systems. (https://www.apideck.com/blog/guide-to-sap-4-hana-rest-and-soap-api)
- Artificial Intelligence and Technologies in SAP S/4HANA Cloud Public Edition 2402: Demo: Joule in SAP S/4HANA Cloud Public Edition (EAC) Joule seamlessly integrates with SAP applications, offering a rich web client compliant with SAP Fiori UI controls. Its out-of-the-box integration with SAP backend systems ensures enterprise readiness while maintaining compliance with AI ethics, GDPR, privacy controls, and SOC-II compliance standards. (https://community.sap.com/t5/enterprise-resource-planning-blog-posts-by-sap/artificial-intelligence-and-technologies-in-sap-s-4hana-cloud-public/ba-p/13596117)
- Overview | SAP S/4HANA: SAP Business Accelerator Hub - Explore, discover and consume APIs, pre-packaged Integrations, Business Services and sample apps (https://api.sap.com/products/SAPS4HANA)
- Understanding SAP S/4 HANA and Its AI capabilities: We help companies transition to SAP S/4HANA based on practical considerations and unlock its advanced AI/ML capabilities to drive automation and efficiency. (https://www.kellton.com/kellton-tech-blog/automating-and-optimizing-business-processes-with-sap-s4-hana)

### mittelstand "AI integration" costs case study manufacturing 2024
- 9 Prominent AI Use Cases in Manufacturing | Svitla Systems: Infineon Technologies Austria: Infineon Technologies Austria, a semiconductor manufacturer, launched the AIMS5.0 project, optimizing supply chain management and resource-efficient manufacturing through AI integration. (https://svitla.com/blog/ai-use-cases-in-manufacturing/)
- AI in Manufacturing: Benefits and 15 Use Cases | NetSuite: AI integration with other advanced technologies, including Internet of Things (IoT) devices, augmented reality (AR) and enterprise resource planning (ERP) systems, provides additional sources of data, empowering managers and other decision-makers to fine-tune every step of the production process. (https://www.netsuite.com/portal/resource/articles/erp/ai-in-manufacturing.shtml)
- AI Manufacturing Automation Roadmap 2026 | Enterprises & SMBs – Performix Business Services: Industrial Automation &amp; Process ... 2025 Louisiana refiner case achieved 28% outage reductions—SMB-scalable via <strong>$5K/month SaaS</strong>.... (https://www.performixbiz.com/ai-driven-automation-revolutionizing-us-manufacturing-in-2026/)
- Industrial transformation: Scaling AI across the manufacturing value chain - Microsoft Industry Blogs: Bridging the divide between OT and IT systems, which frequently function in isolation and adhere to disparate protocol and stands, is essential. By cultivating a more cohesive and consistent data landscape, manufacturers can expedite their AI integration and optimize their use case scalability. (https://www.microsoft.com/en-us/industry/blog/manufacturing-and-mobility/2024/04/09/industrial-transformation-scaling-ai-across-the-manufacturing-value-chain/)

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
### Answer to: What are the technical integration requirements and costs for implementing calibration in typical Mittelstand AI deployments (ERP, MES, quality control)?

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
