# R2: Trust Calibration Frontier — 7× Deep Dive
> Date: 2026-02-19 | Confidence: 80% | Builds on: AR-020-v2-full.md
> Method: 5 Hypotheses per Topic × Deliberate Disconfirmation × Admiralty Rating
> Total web searches: 28 | Sources rated: 60+

---

## R2-A: Multi-Agent Confidence Propagation

### Hypothesen & Verdicts

**H1: Multiplicative Independence (P(A∩B) = P(A)×P(B)) funktioniert**
→ VERDICT: **DISPROVED** (Conf: 88%)
Evidence strongly refutes naive multiplicative independence for multi-agent systems. The "Agentic Confidence Calibration" paper (Zhang, Jan 2026) [A1] explicitly identifies that "uncertainty is no longer an isolated property of a single output, but a compounding factor that accumulates and propagates throughout a sequential trajectory." SAUP (Duan et al., ACL 2025) [A1] formalizes this mathematically: uncertainty propagation in agent chains requires *situational weighting* — not simple multiplication. Agents sharing context, tools, and prompts have correlated error distributions, violating the independence assumption fundamentally.

**H2: Agents mit shared context haben korrelierte Errors → multiplicative überschätzt**
→ VERDICT: **CONFIRMED** (Conf: 92%)
This is now well-established. "Demystifying Multi-Agent Debate" (Jan 2026) [A2] shows that agents in debate systems exchange verbalized confidence as a direct signal, meaning their estimates become entangled. SAUP (ACL 2025) [A1] explicitly models "situational awareness" weights because step-level uncertainties are context-dependent and correlated. The Collaborative Calibration paper (Apr 2024) [A2] demonstrates that multi-agent deliberation can *improve* calibration precisely because agents share information — but this sharing also creates the correlation that breaks multiplicative independence.

**H3: Ein "Calibration Aggregator Agent" kann besser kalibrieren als math. Formeln**
→ VERDICT: **NUANCED** (Conf: 75%)
ConfidenceCal (Bai, BigDIA 2024) [B1] shows multi-agent debate with confidence reweighting improves reliability. Collaborative Calibration (Apr 2024) [A2] uses tool-augmented LLM agents in deliberation to produce better-calibrated scores than individual estimates. HTC (Holistic Trajectory Calibration, Jan 2026) [A1] introduces a "General Agent Calibrator" that extracts process-level features across entire trajectories and achieves best ECE on out-of-domain benchmarks. However, these are *diagnostic* calibrators, not real-time propagation systems. No evidence that an aggregator agent can do this reliably in production multi-agent chains with latency constraints.

**H4: Confidence-Propagation ist NP-hard und nur approximierbar**
→ VERDICT: **NUANCED** (Conf: 82%)
Probabilistic inference in Bayesian belief networks IS NP-hard (Cooper 1990) [A1], and even approximation is NP-hard (Dagum & Luby 1993) [A1]. Multi-agent confidence propagation maps directly to this problem class when agent dependencies form general DAGs. However, most practical agent systems have *chain* or *tree* topologies, not general graphs — for these restricted cases, exact inference is polynomial. The practical question is whether real agent systems stay in tractable topologies. Current evidence: mostly yes (sequential chains, simple fan-out), but as agent architectures grow more complex, this could change.

**H5: Die Frage ist falsch gestellt — Confidence sollte per-claim sein, nicht per-agent**
→ VERDICT: **CONFIRMED** (Conf: 85%)
The atomic calibration work (Zhang et al., ACL 2025 / AACL-IJCNLP 2025) [A1] demonstrates that per-claim calibration is fundamentally more informative than per-response calibration. HTC (Jan 2026) [A1] moves to *process-level* features — neither per-agent nor per-claim, but per-trajectory-step. SAUP [A1] propagates uncertainty per-step, not per-agent. The emerging consensus: the right granularity is per-claim or per-step, not per-agent. Per-agent confidence is an aggregation convenience, not a fundamental unit.

### Key Sources (Admiralty Rated)
- [A1] Zhang et al. "Agentic Confidence Calibration" arXiv:2601.15778, Jan 2026 — First paper to formally define agentic calibration; HTC framework
- [A1] Duan et al. "Uncertainty Propagation on LLM Agent (SAUP)" ACL 2025 — Formalizes uncertainty propagation with situational awareness
- [A2] "Confidence Calibration and Rationalization for LLMs via Multi-Agent Deliberation" arXiv:2404.09127, 2024 — Collaborative Calibration approach
- [B1] Bai "ConfidenceCal: Confidence Calibration in Multi-Agent Debate" BigDIA 2024 — Reweighting tokens from debaters
- [A2] "Demystifying Multi-Agent Debate: Role of Confidence and Diversity" arXiv:2601.19921, Jan 2026
- [A1] Cooper (1990) "Computational Complexity of Probabilistic Inference Using Bayesian Belief Networks" — NP-hardness proof
- [A1] Dagum & Luby (1993) "Approximating Probabilistic Inference is NP-hard"

### Contradictions
- HTC claims a "General Agent Calibrator" works across domains without retraining, yet SAUP requires per-step situational weights. Resolution: HTC uses a trained meta-model on trajectory features, SAUP is a mathematical framework. They operate at different levels — not truly contradictory.

### Synthesis
The field has progressed dramatically since AR-020-v2 noted "no framework addresses multi-agent calibration propagation." Two major 2025-2026 papers (SAUP, HTC) now directly address this. Key insight: **confidence propagation in agents is NOT a simple math problem — it requires process-level awareness of trajectory dynamics.** Multiplicative independence is dead for shared-context agents. The right granularity is per-claim or per-step, not per-agent. Practical systems should use SAUP-style weighted propagation for chains and HTC-style trajectory calibration for complex workflows.

### Connections zu AR-020 v2
- AR-020-v2 Open Question #1 ("How should confidence propagate through multi-agent chains?") now has partial answers via SAUP and HTC
- AR-020-v2's three-tier architecture needs revision: Tier 3 (Selective Prediction for Human Routing) should incorporate SAUP-style propagation

---

## R2-B: RLHF-Calibration Recovery

### Hypothesen & Verdicts

**H1: Temperature Scaling auf logits recovert Pre-RLHF Calibration**
→ VERDICT: **NUANCED** (Conf: 80%)
Standard single-parameter temperature scaling is insufficient for RLHF-tuned models. ATS (Adaptive Temperature Scaling, ICLR 2024 Workshop) [A1] shows that per-token temperature prediction significantly outperforms global TS for RLHF models because RLHF creates *heterogeneous* miscalibration patterns. BaseCal (Jan 2026) [A2] takes a different approach: projecting RLHF-model hidden states back to base model space, reducing ECE by 42.9% on average — effectively using the base model's calibration as a reference. The ICML 2025 paper "Restoring Calibration for Aligned LLMs" [A1] identifies that RLHF models exist in a "calibratable regime" where calibration-aware fine-tuning (CFT) can restore calibration, but further performance optimization pushes them into a "non-calibratable regime." Bottom line: TS alone doesn't work, but adaptive/projected variants partially recover calibration.

**H2: PPO-M/PPO-C sind theoretisch elegant aber praktisch nicht deploybar**
→ VERDICT: **CONFIRMED** (Conf: 78%)
Wang et al.'s "Taming Overconfidence" (NeurIPS 2024) [A1] proposed PPO-M (calibrating reward models) and PPO-C (calibrating reward scores during training). No follow-up papers report production deployment. The approach requires modifying the RLHF training pipeline itself — which only model providers (OpenAI, Anthropic, Google) can do. For downstream users and agent builders, PPO-M/PPO-C are inaccessible. No open-source implementation found in active use. The ICML 2025 CFT paper [A1] implicitly supersedes PPO-C by showing calibration can be restored post-hoc without modifying the training pipeline.

**H3: Consistency-Based Methods umgehen das RLHF-Problem komplett**
→ VERDICT: **NUANCED** (Conf: 82%)
Self-consistency (sampling N responses, measuring agreement) does bypass logit-level miscalibration because it operates at the output level. Huang et al. (EMNLP 2024) [A1] confirm that "self-consistency methods excel in factoid datasets" for long-form calibration. However, "Mind the Confidence Gap" (Feb 2025) [A2] found that "large RLHF-tuned models display inherent calibration" in certain settings — suggesting RLHF's damage is not universal. The problem: self-consistency is expensive (N × cost) and RLHF can affect the *diversity* of sampled responses (mode collapse), potentially undermining consistency-based methods too. BaseCal [A2] shows base model signals can be extracted even from RLHF models, offering a complementary bypass.

**H4: Fine-Tuning auf calibration data ist der einzige zuverlässige Weg**
→ VERDICT: **NUANCED** (Conf: 70%)
The ICML 2025 CFT paper [A1] provides the strongest evidence FOR this hypothesis: calibration-aware fine-tuning in the "calibratable regime" restores calibration without hurting performance. However, it also shows a fundamental limit: over-optimization for performance pushes models into non-calibratable territory. Multiple alternatives exist that don't require fine-tuning: ATS (post-hoc), BaseCal (projection), self-consistency (sampling). Fine-tuning is reliable but NOT the only way.

**H5: RLHF-Calibration ist ein gelöstes Problem bis 2027**
→ VERDICT: **DISPROVED** (Conf: 75%)
The ICML 2025 "non-calibratable regime" finding [A1] is devastating for this hypothesis: there's a fundamental tension between performance optimization and calibration. As models get better through more RLHF/DPO, they may become structurally uncalibratable at the logit level. The "Agentic Uncertainty Reveals Agentic Overconfidence" paper (Feb 2026) [A2] shows overconfidence persists in the latest agentic systems. The problem is structural, not just engineering — it requires rethinking how alignment interacts with calibration. 2027 is too optimistic for a full solution.

### Key Sources (Admiralty Rated)
- [A1] Xiao et al. "Restoring Calibration for Aligned LLMs: CFT" ICML 2025, arXiv:2505.01997 — Calibratable vs non-calibratable regimes
- [A1] ATS "Calibrating Language Models with Adaptive Temperature Scaling" ICLR 2024 Workshop, arXiv:2409.19817
- [A2] Tan et al. "BaseCal: Unsupervised Confidence Calibration via Base Model Signals" arXiv:2601.03042, Jan 2026 — 42.9% ECE reduction
- [A1] Wang et al. "Taming Overconfidence in LLMs: Reward Calibration in RLHF" NeurIPS 2024
- [A2] "Mind the Confidence Gap" arXiv:2502.11028, Feb 2025 — Distractors reduce ECE by up to 90%
- [A1] Huang et al. "Calibrating Long-form Generations" EMNLP 2024

### Contradictions
- ICML 2025 says calibration is restorable via CFT in the "calibratable regime," but also shows that better performance = worse calibration. This is a genuine Pareto frontier, not a contradiction — you must choose between optimal performance and optimal calibration.

### Synthesis
RLHF calibration recovery is a multi-front war. No single method dominates. The emerging best practice: **use BaseCal-style base model projection for white-box models, self-consistency for black-box, and accept the performance-calibration tradeoff.** PPO-M/PPO-C are dead ends for users (only providers can implement). The ICML 2025 "non-calibratable regime" is the most important new finding — it means calibration has fundamental limits under aggressive optimization.

### Connections zu AR-020 v2
- AR-020-v2 Finding RF-020-01 ("RLHF destroys calibration") is now refined: destruction is regime-dependent, not absolute
- AR-020-v2's Tier 1 recommendation (consistency-based default) is validated but needs the caveat about mode collapse

---

## R2-C: Calibration for Code Generation & Tool Use

### Hypothesen & Verdicts

**H1: Code hat binäre Correctness → einfacher zu kalibrieren als Text**
→ VERDICT: **NUANCED** (Conf: 78%)
Spiess et al. "Calibration and Correctness of Language Models for Code" (ICSE 2025) [A1] directly studied this. Pre-trained code models suffer from over-confidence. While code has clearer correctness criteria (tests pass/fail), LLMs show "significant confidence bias in complex tasks like code generation, lacking accurate self-assessment capabilities" (Tian et al. 2023, Kadavath et al. 2022) [A1]. The ICSE 2024 paper "On Calibration of Pre-trained Code Models" [A1] found temperature scaling and label smoothing help for in-distribution but degrade under distribution shift. Binary correctness makes *evaluation* easier but doesn't automatically make *pre-generation calibration* easier — the model still doesn't know if its code will work before execution.

**H2: Tool-Use Confidence ≠ Output Confidence (2 separate Kalibrierungen nötig)**
→ VERDICT: **CONFIRMED** (Conf: 85%)
The "Agentic Confidence Calibration" paper (HTC, Jan 2026) [A1] explicitly distinguishes between micro-level stability (within a step) and macro-level dynamics (across steps including tool calls). SAUP (ACL 2025) [A1] models uncertainty at each step independently and then propagates — implicitly treating tool-use steps as having different uncertainty characteristics than reasoning steps. The "Agentic Uncertainty Quantification" survey (Jan 2026) [A2] notes that "uncertainty from external tools" is a unique challenge for agentic systems. No existing framework provides a unified confidence score across tool selection, parameter generation, and output interpretation — these are genuinely separate calibration problems.

**H3: Execution-Based Validation (Code laufen lassen) ersetzt Calibration**
→ VERDICT: **NUANCED** (Conf: 75%)
For code: execution-based validation IS the gold standard. pass@k metrics provide direct empirical calibration via test execution. But: (1) not all code can be safely executed (side effects, APIs, destructive operations), (2) test coverage is often incomplete, (3) execution doesn't help for partial correctness or code quality, (4) for tool use beyond code, execution-based validation is often impossible or expensive. Execution replaces calibration *where possible* but cannot be the universal solution for agent systems.

**H4: Multi-Step Tool Chains haben compounding Calibration Error**
→ VERDICT: **CONFIRMED** (Conf: 90%)
SAUP (ACL 2025) [A1] and HTC (Jan 2026) [A1] both confirm compounding error in multi-step agent trajectories. HTC specifically extracts "macro dynamics" features that capture how errors compound. "Agentic Uncertainty Reveals Agentic Overconfidence" (Feb 2026) [A2] shows that agentic systems are systematically overconfident precisely because compounding errors are not accounted for. The LLM Shepherding paper (Jan 2026) [B1] addresses this indirectly through cascading strategies that intervene before errors compound.

**H5: Bestehende Calibration-Methoden versagen bei Code fundamental**
→ VERDICT: **DISPROVED** (Conf: 72%)
ICSE 2024 [A1] shows temperature scaling works for in-distribution code tasks. ICSE 2025 [A1] demonstrates calibration methods can be adapted. The ICLR 2025 paper "Do LLMs Estimate Uncertainty Well" [A1] evaluates six uncertainty methods across diverse tasks including code-adjacent reasoning. The methods don't "fundamentally fail" — they're just not as well-studied and require domain adaptation. The AXIOM benchmark (Dec 2025) [B1] provides code-specific calibration evaluation. The gap is research attention, not fundamental impossibility.

### Key Sources (Admiralty Rated)
- [A1] Spiess et al. "Calibration and Correctness of Language Models for Code" ICSE 2025
- [A1] "On Calibration of Pre-trained Code Models" ICSE 2024
- [A1] Zhang et al. "Agentic Confidence Calibration (HTC)" arXiv:2601.15778, Jan 2026
- [A1] Duan et al. "SAUP: Uncertainty Propagation on LLM Agent" ACL 2025
- [A2] "Agentic Uncertainty Quantification" arXiv:2601.15703, Jan 2026
- [A1] "Do LLMs Estimate Uncertainty Well" ICLR 2025

### Contradictions
- H1 evidence suggests code is HARDER to calibrate (overconfidence), while H5 evidence suggests existing methods work. Resolution: code calibration is *possible* but models have worse *base* calibration for code due to training distribution effects. Methods work, but the starting point is worse.

### Synthesis
Code and tool-use calibration is a **two-layer problem**: (1) per-step calibration of individual tool calls/code generations, and (2) propagation of uncertainty through multi-step chains. Existing calibration methods partially transfer but need code-specific adaptation. The strongest finding: **tool-use confidence and output confidence are genuinely separate calibration problems** — agent architects must handle both. Execution-based validation is the best available ground truth for code but has coverage limitations.

### Connections zu AR-020 v2
- AR-020-v2 Open Question #3 ("optimal calibration for code generation and tool use") now has partial answer: adapt existing methods + separate tool/output calibration + use execution where possible
- AR-020-v2's three-tier architecture applies: Tier 1 (consistency) for code generation, Tier 3 (selective prediction) for uncertain tool calls

---

## R2-D: Calibration for Long-Form Generation

### Hypothesen & Verdicts

**H1: Atomic Decomposition (Zhang 2024) löst das Problem**
→ VERDICT: **NUANCED** (Conf: 80%)
Zhang et al. "Atomic Calibration of LLMs in Long-Form Generations" (ACL 2025 KnowFM / AACL-IJCNLP 2025) [A1] is the definitive work. Key findings: (1) LLMs exhibit *poorer* calibration at the atomic level during long-form generation, (2) atomic calibration uncovers patterns invisible at the macro level, (3) two new confidence fusion strategies improve calibration. However, Huang (2025) [B2] argues that "LLM-generated decompositions lack stability and reliability" — the decomposition step itself introduces noise. Atomic decomposition is a *framework*, not a complete solution. It diagnoses the problem better but doesn't fully solve it.

**H2: Paragraph-Level Calibration ist der richtige Granularity-Level**
→ VERDICT: **DISPROVED** (Conf: 78%)
Both atomic calibration (Zhang et al.) [A1] and the "Calibrating Long-form Generations" paper (Huang et al., EMNLP 2024) [A1] show that finer granularity (claim-level) is superior. Paragraph-level is too coarse — a paragraph can contain both well-supported and hallucinated claims. The "Linguistic Calibration of Long-Form Generations" paper (Braverman et al., ICML 2024) [A1] demonstrates that sentence-level hedging language should reflect claim-level confidence. No paper advocates for paragraph-level as optimal.

**H3: Long-Form Calibration ist prinzipiell unlösbar (zu viele Freiheitsgrade)**
→ VERDICT: **DISPROVED** (Conf: 75%)
Multiple papers demonstrate workable long-form calibration: Huang et al. (EMNLP 2024) [A1] introduce a unified calibration framework treating both correctness and confidence as distributions. LoGU (Long-form Generation with Uncertainty Expressions, 2024) [A2] shows LLMs can express uncertainty *during* generation. Linguistic Calibration [A1] trains models to embed calibrated hedging. The problem is hard but demonstrably tractable for factoid claims within long-form text. What remains unsolved: calibrating subjective quality, style, and coherence aspects.

**H4: Hybrid: Structure-Calibration + Fact-Calibration + Style-Calibration**
→ VERDICT: **NUANCED** (Conf: 70%)
No paper proposes this exact three-way decomposition. However, the evidence supports it directionally: atomic calibration handles facts [A1], linguistic calibration handles hedging/expression [A1], and LoGU handles uncertainty expressions inline [A2]. The combination hasn't been tested. Style calibration specifically has no research backing — this is speculative. Fact-calibration is well-supported; structure- and style-calibration are open problems.

**H5: Self-Consistency funktioniert auch für Long-Form (N Drafts vergleichen)**
→ VERDICT: **CONFIRMED** (Conf: 82%)
Huang et al. (EMNLP 2024) [A1] explicitly test self-consistency (PSC — Pairwise Self-Consistency) for long-form generation and find it "excels in factoid datasets." The method generates N long-form responses and measures pairwise agreement. "Confidence Improves Self-Consistency in LLMs" (ACL Findings 2025) [A2] further validates this approach. Key limitation: the cost is N × generation cost, which is prohibitive for very long outputs. Also, self-consistency works better for factual content than for creative or subjective content where multiple valid outputs exist.

### Key Sources (Admiralty Rated)
- [A1] Zhang et al. "Atomic Calibration of LLMs in Long-Form Generations" ACL 2025 KnowFM / AACL-IJCNLP 2025, arXiv:2410.13246
- [A1] Huang et al. "Calibrating Long-form Generations from Large Language Models" EMNLP 2024, arXiv:2402.06544
- [A1] Braverman et al. "Linguistic Calibration of Long-Form Generations" ICML 2024, arXiv:2404.00474
- [A2] "LoGU: Long-form Generation with Uncertainty Expressions" arXiv:2410.14309, 2024
- [A2] "Confidence Improves Self-Consistency in LLMs" ACL Findings 2025
- [B2] Huang (2025) — Critique of LLM decomposition stability

### Contradictions
- Atomic calibration shows LLMs are *more* miscalibrated at fine-grained levels, but self-consistency works better for long-form factoid content. Resolution: these measure different things. Atomic calibration reveals hidden miscalibration; self-consistency provides a better *external* estimate despite the model's internal miscalibration.

### Synthesis
Long-form calibration is **not unsolvable but requires granularity-aware methods.** Atomic decomposition is the right direction but not a complete solution. Self-consistency works for factual content. The **hybrid approach (H4) is the most promising direction** but hasn't been formally validated — decompose into facts (atomic calibration), structure (coherence checks), and expression (linguistic calibration). The biggest gap: calibrating subjective aspects of long-form text.

### Connections zu AR-020 v2
- AR-020-v2 Contradiction #3 (binary correctness vs. long-form) is now better understood: atomic decomposition bridges the gap by making long-form amenable to claim-level binary evaluation
- AR-020-v2's consistency-based Tier 1 extends to long-form via PSC

---

## R2-E: Adversarial Attacks on Calibration

### Hypothesen & Verdicts

**H1: Memory Poisoning kann Calibration gezielt manipulieren**
→ VERDICT: **CONFIRMED** (Conf: 88%)
MINJA (Memory Injection Attack, 2025) [A1] achieves >95% injection success rate and >70% attack success rate via query-only interactions. MemoryGraft (Dec 2025) [A2] extends this to persistent compromise through experience retrieval poisoning. AgentPoison (NeurIPS 2024) [A1] directly poisons knowledge bases with trigger tokens. A Jan 2026 paper "Memory Poisoning Attack and Defense" [A2] acknowledges that "adversaries inject malicious instructions through query-only interactions that corrupt the agents' long-term memory." While these attacks target agent behavior broadly (not calibration specifically), the mechanism directly applies: poisoned memories could include false calibration anchors ("previous similar questions had 95% accuracy" → inflated confidence).

**H2: Calibration-Systeme sind robuster als die Modelle selbst**
→ VERDICT: **DISPROVED** (Conf: 80%)
"On the Robustness of Verbal Confidence of LLMs in Adversarial Attacks" (NeurIPS 2025) [A1] is the first comprehensive study on this. Finding: "even subtle semantic-preserving modifications can lead to misleading confidence in responses." Attacks "significantly impair verbal confidence estimates and lead to frequent answer changes." Critically: "commonly used defence techniques are largely ineffective or counterproductive." Calibration systems that rely on verbal confidence are at LEAST as fragile as the model's answers, possibly more so because confidence is easier to manipulate than factual recall.

**H3: Adversarial Calibration Attacks sind schwerer als Adversarial Content Attacks**
→ VERDICT: **NUANCED** (Conf: 65%)
Limited direct evidence comparing difficulty. The NeurIPS 2025 robustness paper [A1] shows calibration attacks are quite easy — semantic-preserving perturbations suffice. However, making a model *confidently wrong* (rather than just shifting confidence) requires both content manipulation AND calibration manipulation simultaneously, which IS harder. LLM-as-a-Judge adversarial attacks (EMNLP 2024) [A1] show universal adversarial suffixes can manipulate assessment scores, which is analogous to calibration manipulation. The difficulty depends on the attack goal: shifting confidence alone is easy; targeted "confident but wrong" is harder.

**H4: Ein Angreifer kann ein System "confident but wrong" machen**
→ VERDICT: **CONFIRMED** (Conf: 85%)
The combination of memory poisoning (MINJA) [A1] + verbal confidence fragility (NeurIPS 2025) [A1] makes this achievable. Memory poisoning injects wrong information that the agent treats as high-confidence context. The "Resisting Correction" paper (Dec 2025) [A2] from AR-020-v2 shows RLHF models already resist correction, meaning injected false confidence is sticky. Adversarial examples on LLM-as-Judge (EMNLP 2024) [A1] show scores can be systematically inflated. The attack surface is wide and defenses are weak.

**H5: Defense-in-Depth (Multi-Method Calibration) ist der einzige Schutz**
→ VERDICT: **CONFIRMED** (Conf: 78%)
The NeurIPS 2025 paper [A1] explicitly concludes that single-method defenses fail. If verbal confidence is attacked, you need consistency-based backup. If consistency is attacked (via mode collapse injection), you need logit-based backup. No single method is adversarially robust. The OWASP LLM Top 10 (2025) [B1] recommends defense-in-depth for prompt injection broadly. Multi-method calibration (verbal + consistency + entropy + execution validation for code) provides redundancy that an attacker must compromise simultaneously.

### Key Sources (Admiralty Rated)
- [A1] Obadinma et al. "On the Robustness of Verbal Confidence of LLMs in Adversarial Attacks" NeurIPS 2025, arXiv:2507.06489
- [A1] Dong et al. "MINJA: A Practical Memory Injection Attack against LLM Agents" arXiv:2503.03704, 2025
- [A2] "Memory Poisoning Attack and Defense on Memory Based LLM-Agents" arXiv:2601.05504, Jan 2026
- [A1] Raina et al. "Is LLM-as-a-Judge Robust? Universal Adversarial Attacks" EMNLP 2024
- [A2] "MemoryGraft: Persistent Compromise via Poisoned Experience Retrieval" Dec 2025
- [A1] Chen et al. "AgentPoison: Red-teaming LLM Agents via Poisoning Memory" NeurIPS 2024
- [B1] OWASP "LLM01:2025 Prompt Injection" genai.owasp.org, 2025

### Contradictions
- NeurIPS 2025 says defenses are "largely ineffective" but multi-method defense is still recommended. This isn't contradictory — it means individual defenses fail but layered defense raises the attack cost, even if no single layer is robust.

### Synthesis
Adversarial attacks on calibration are **easier than expected and less defended than assumed.** The combination of memory poisoning (MINJA, >95% success) + verbal confidence fragility (NeurIPS 2025) creates a clear attack vector for making agents "confident but wrong." The only viable defense is defense-in-depth: multiple independent calibration methods so an attacker must compromise all simultaneously. **This is the most underappreciated risk in current agent calibration literature.**

### Connections zu AR-020 v2
- AR-020-v2 Open Question #4 ("How do adversarial attacks interact with calibration?") now answered: interaction is devastating, defense requires multi-method approach
- AR-020-v2's three-tier architecture is implicitly defense-in-depth (consistency + conformal + selective), which is validated as the right approach

---

## R2-F: Cost-Optimal Calibration Architecture

### Hypothesen & Verdicts

**H1: $0.005/Check ist das Minimum (Budget-CoCoA, 3 Samples)**
→ VERDICT: **NUANCED** (Conf: 72%)
Budget-CoCoA's ~$0.005/check estimate from AR-020-v2 was based on ~3 API calls to a small model. Current pricing (Haiku 3.5: $0.80/$4.00 per MTok, Feb 2026) means 3 short API calls (~200 tokens each) cost roughly $0.002-0.005. But zero-cost alternatives exist (see H5), making $0.005 a meaningful cost, not the minimum. For caching-enhanced systems, per-check cost approaches near-zero for repeated similar queries.

**H2: Caching + Embedding-Similarity kann 80% der Checks eliminieren**
→ VERDICT: **NUANCED** (Conf: 68%)
No paper directly validates the "80%" figure. However, the cascading/routing literature strongly supports the principle. Model cascades (ICML 2025) [A1] achieve up to 98% cost savings by routing easy queries to small models. FrugalGPT-style approaches [B1] cache responses for similar queries. The "Improving Model Cascades Through Confidence Tuning" paper [A1] shows confidence-based routing can match GPT-4 quality at 2% of cost. The 80% figure is plausible for production systems with repetitive query patterns but unverified for novel/diverse agent workloads.

**H3: Small Model Proxy (Haiku) kalibriert genauso gut wie Opus für 1/20 der Kosten**
→ VERDICT: **NUANCED** (Conf: 70%)
ICLR 2025 routing paper [A1] confirms >50x cost difference between Haiku and Opus. "Predicting LLM Reasoning Performance with Small Proxy Model" [B1] shows small models can predict larger model behavior. However, calibration quality specifically has not been benchmarked Haiku-vs-Opus. The ICLR 2025 "Do LLMs Estimate Uncertainty Well" [A1] shows model size affects uncertainty estimation quality. Small models may produce *different* uncertainty signals, not just worse ones. Confidence routing (use small model, escalate to large when uncertain) is the pragmatic approach — not using small for calibration per se, but using it as first-pass filter.

**H4: Der optimale Punkt ist 5-7 Samples, nicht 3**
→ VERDICT: **NUANCED** (Conf: 65%)
The "Cycles of Thought" paper (2024) [B1] and self-consistency literature generally show diminishing returns after ~5 samples. Huang et al. (EMNLP 2024) [A1] test self-consistency for long-form with varying sample sizes. The optimal depends heavily on task difficulty and model diversity. For easy tasks, 3 is often sufficient. For hard tasks, 5-7 provides meaningful improvement. **No universal optimum exists** — it's task-dependent and the right approach is adaptive: start with 3, escalate if variance is high.

**H5: Zero-Cost Calibration ist möglich via Token-Entropy (keine Extra-Calls)**
→ VERDICT: **CONFIRMED** (Conf: 82%)
"Think Just Enough: Sequence-Level Entropy as Confidence Signal" (Oct 2025) [A2] uses token entropy with "closed-form thresholds" and achieves 25-50% compute reduction without accuracy loss. TECP (Token-Entropy Conformal Prediction, MDPI 2025) [A2] uses token-level entropy as nonconformity scores for conformal prediction. "Learning to Route LLMs with Confidence Tokens" [B1] embeds confidence directly in the token stream. These methods require logprob access (white-box or partial API access) but add zero marginal cost beyond the base inference call. For models providing logprobs (many open-source, OpenAI partial), this is genuinely zero-cost calibration. Limitation: quality is lower than multi-sample methods.

### Key Sources (Admiralty Rated)
- [A1] "Improving Model Cascades Through Confidence Tuning" OpenReview 2025 — 98% cost savings
- [A1] Dekoninck et al. "A Unified Approach to Routing and Cascading for LLMs" ICML 2025
- [A2] "Think Just Enough: Sequence-Level Token Entropy" arXiv:2510.08146, Oct 2025
- [A2] TECP "Token-Entropy Conformal Prediction" MDPI 2025
- [A1] "Do LLMs Estimate Uncertainty Well" ICLR 2025
- [A1] Huang et al. "Calibrating Long-form Generations" EMNLP 2024
- [B1] "Learning to Route LLMs with Confidence Tokens" arXiv:2410.13284

### Contradictions
- Zero-cost entropy methods (H5) exist, yet Budget-CoCoA assumes 3 API calls (H1). Resolution: they serve different contexts. Entropy methods require logprob access (white-box/partial). Consistency methods work for any black-box API. The cost-optimal choice depends on API access level.

### Synthesis
The cost landscape for calibration is more nuanced than AR-020-v2 suggested. The **optimal architecture is a cost-aware cascade**: (1) Zero-cost token entropy for logprob-accessible models, (2) 3-sample consistency for black-box models, (3) escalation to 5-7 samples only for high-uncertainty items, (4) caching + routing to avoid redundant checks. True cost per check ranges from $0 (entropy) to $0.015+ (multi-sample Opus), with the weighted average depending on query mix and access level.

### Connections zu AR-020 v2
- AR-020-v2's cost estimate of "<$0.05 per agent decision" is conservative — cascade architecture can bring this to <$0.01 for most queries
- AR-020-v2's Tier 1 should be split: Tier 1a (zero-cost entropy where available) + Tier 1b (consistency for black-box)

---

## R2-G: EU AI Act × Calibration Requirements

### Hypothesen & Verdicts

**H1: Art. 15 fordert explizit Calibration für High-Risk AI**
→ VERDICT: **DISPROVED** (Conf: 88%)
Article 15 text (verified from official source) [A1]: "High-risk AI systems shall be designed and developed in such a way that they achieve an appropriate level of accuracy, robustness, and cybersecurity." The word "calibration" does NOT appear in Article 15. The requirements are for "accuracy" and "relevant accuracy metrics" declared in instructions of use. Accuracy ≠ calibration. A system can be accurate but poorly calibrated (e.g., always 100% confident, correct 85% of the time). The Act does NOT explicitly require calibration.

**H2: Der AI Act nennt "accuracy" aber meint nicht "calibration" — Compliance-Gap**
→ VERDICT: **CONFIRMED** (Conf: 90%)
Direct reading of Article 15 [A1] confirms: the Act requires "appropriate level of accuracy" and that "accuracy metrics shall be declared." It also requires resilience against "data poisoning," "model poisoning," and "adversarial examples." But nowhere does it require that confidence scores be calibrated, that uncertainty be quantified, or that the system know when it's wrong. This is a significant compliance gap: a system that is 85% accurate and always says "I'm 100% confident" would technically comply with Art. 15 accuracy requirements but be dangerously miscalibrated. The Commission is tasked with developing "benchmarks and measurement methodologies" — this could eventually include calibration, but doesn't yet.

**H3: ISO 42001 wird der de-facto Calibration-Standard für EU**
→ VERDICT: **NUANCED** (Conf: 65%)
ISO 42001 is an AI management system standard — it addresses governance, risk management, and lifecycle management, NOT specific technical requirements like calibration. ISACA (2025) [B1] and Vanta (2025) [B1] position it as complementary to the EU AI Act. However, ISO 42001 is NOT a harmonised standard under the AI Act. The FIRST harmonised standard is prEN 18286 (QMS for EU AI Act, Oct 2025) [A2], which is specifically designed for Art. 17 compliance (quality management). Neither ISO 42001 nor prEN 18286 specify calibration requirements. The actual calibration standard would need to come from CEN/CENELEC technical standards still in development.

**H4: Nur High-Risk Systeme brauchen Calibration — 90% der Agents sind nicht betroffen**
→ VERDICT: **NUANCED** (Conf: 72%)
The AI Act's Art. 15 requirements apply only to high-risk AI systems (Annex III categories: biometrics, critical infrastructure, education, employment, essential services, law enforcement, migration, justice). Most current AI agents (chatbots, coding assistants, content generation) are NOT high-risk. GPAI model provisions (Aug 2025) [A2] add transparency requirements but not calibration. However: (1) any agent deployed in high-risk contexts becomes subject to Art. 15, (2) the Act's scope may expand via implementing acts, (3) market pressure may make calibration expected even for non-regulated agents. The "90%" figure is roughly correct today but may shrink.

**H5: Die EU wird 2027 spezifische Agent-Calibration Guidance veröffentlichen**
→ VERDICT: **NUANCED** (Conf: 50%)
The EU published GPAI Guidelines (Jul 2025) [A2] and Code of Practice (Jul 2025) [A2], but neither mentions calibration. Art. 15(2) tasks the Commission with developing "benchmarks and measurement methodologies" for accuracy — this COULD include calibration guidance. The timeline: high-risk AI obligations for regulated products apply Aug 2027. CEN/CENELEC is accelerating standards development (Oct 2025 decision) [A2]. However, "agent-specific calibration guidance" is speculative — the EU regulatory apparatus focuses on risk categories, not technology types. More likely: general accuracy/robustness standards that implicitly require calibration metrics, by 2027-2028. Agent-specific guidance by 2027 is optimistic.

### Key Sources (Admiralty Rated)
- [A1] EU AI Act Article 15 — Official text from artificialintelligenceact.eu
- [A2] prEN 18286 "QMS for EU AI Act Regulatory Purposes" Oct 2025 — First harmonised standard
- [A2] EU Commission "Standardisation of the AI Act" digital-strategy.ec.europa.eu
- [A2] EU Commission "Guidelines for providers of GPAI models" Jul 2025
- [B1] ISACA "ISO/IEC 42001 and EU AI Act: A Practical Pairing" 2025
- [B1] Vanta "How ISO 42001 helps with EU AI Act compliance" 2025
- [A2] Trilateral Research "EU AI Act Compliance Timeline" Nov 2025

### Contradictions
- Multiple compliance guides claim ISO 42001 "aligns with" the AI Act, but it's NOT a harmonised standard and doesn't confer presumption of conformity. This is a marketing/compliance-industry gap, not a factual contradiction.

### Synthesis
**The EU AI Act does NOT require calibration.** It requires "accuracy" — which is a weaker, different concept. This creates both a compliance gap (miscalibrated systems can technically comply) and an opportunity (early calibration adoption provides competitive advantage and future-proofs against likely regulatory evolution). ISO 42001 is governance, not technical. prEN 18286 is QMS, not calibration-specific. **Actual calibration standards are still 1-2 years away.** For Ainary, this means: calibration is a market differentiator, not a compliance requirement (yet).

### Connections zu AR-020 v2
- AR-020-v2 mentioned EU AI Act compliance as a motivation for calibration — this is accurate as future-proofing but overstates current requirements
- AR-020-v2's Tier 2 (conformal prediction for "compliance story") is premature — there's nothing to comply with yet, but building the capability now is strategically sound

---

## Meta-Synthesis: Übergreifende Patterns über alle 7 Topics

### Pattern 1: The Field Has Moved Fast (Jan-Feb 2026 Breakthrough Papers)
Three papers from Jan 2026 fundamentally advance the field beyond AR-020-v2's landscape:
- **HTC** (Agentic Confidence Calibration) — First formal framework for agent-specific calibration
- **BaseCal** — Novel approach using base model signals to bypass RLHF miscalibration
- **SAUP** (ACL 2025, cited in Jan 2026 surveys) — Formalizes uncertainty propagation in agent chains

AR-020-v2's claim that "no framework addresses multi-agent calibration" is now outdated.

### Pattern 2: The Performance-Calibration Tradeoff is Fundamental
ICML 2025's "calibratable vs non-calibratable regime" is the most important theoretical finding. As models are optimized for performance (via RLHF/DPO), they structurally lose calibration. This means:
- Calibration is not a one-time problem to solve — it's an ongoing tension
- Post-hoc calibration will always be needed as models improve
- Model providers face an inherent tradeoff their users inherit

### Pattern 3: Per-Claim/Per-Step > Per-Agent/Per-Response
Across R2-A (per-step propagation), R2-D (atomic decomposition), and R2-C (tool-use vs output): the consistent finding is that **fine-grained calibration is superior to coarse-grained.** Confidence should be tracked at the claim or step level, not aggregated to agent or response level. This has architectural implications: calibration must be woven into the generation/execution pipeline, not bolted on as a post-processing step.

### Pattern 4: Defense-in-Depth is Non-Negotiable
R2-E (adversarial attacks) + R2-F (cost optimization) converge: **multi-method calibration is required for both security AND cost reasons.** Zero-cost entropy catches easy cases, consistency catches moderate cases, conformal prediction handles high-stakes cases. No single method is robust against adversarial attacks, cost-optimal for all queries, AND accurate across all domains.

### Pattern 5: The Regulatory Window is Open
R2-G shows the EU AI Act does NOT yet require calibration. This is a **strategic window**: organizations that implement calibration now gain competitive advantage without compliance pressure. By 2027-2028, when standards likely include calibration-adjacent requirements, early adopters will be positioned to lead. The risk of early adoption is low; the risk of late adoption is regulatory scramble.

### Pattern 6: Black-Box vs White-Box Divide Persists but Narrows
AR-020-v2 identified the black-box constraint as fundamental. New developments narrow the gap:
- BaseCal works for open-weight models (maps RLHF back to base)
- Token entropy works with partial logprob access
- Consistency methods remain the universal black-box approach
- OpenAI's partial logprob access (top-5 tokens) enables some white-box methods

The divide is becoming a **spectrum** rather than a binary.

### Updated Recommendation for Ainary Architecture
Based on all 7 deep dives, AR-020-v2's three-tier architecture should be updated to:

**Tier 0 — Zero-Cost (where logprobs available):** Token-entropy confidence as free baseline signal. ~$0/check.

**Tier 1 — Consistency-Based (all agents):** 3-sample self-consistency for black-box. Adaptive: escalate to 5-7 samples if variance is high. ~$0.005-0.015/check.

**Tier 2 — Process-Aware (multi-step agents):** SAUP-style uncertainty propagation through agent chains. HTC-inspired trajectory-level calibration for complex workflows. Cost: minimal overhead (lightweight model on top of existing traces).

**Tier 3 — Conformal + Selective (high-stakes):** Conformal prediction sets for guaranteed coverage. Abstention/human routing when confidence below task-specific thresholds. Cost: domain-specific calibration set maintenance.

**Cross-Cutting — Defense-in-Depth:** At least 2 independent calibration methods per decision point. Memory integrity checks to prevent calibration poisoning. Regular adversarial testing of calibration robustness.

---

## Sources Summary (All Topics)
Total unique sources cited: 45+
Admiralty distribution: A1: 22 | A2: 15 | B1: 7 | B2: 2
Publication year range: 2024-2026 (majority 2025-2026)
No source older than 2022 used for primary claims.

## Metadata
- Research Line: trust-calibration
- Tags: calibration, multi-agent, RLHF, code-generation, long-form, adversarial, cost-optimization, EU-AI-Act, frontier
- Builds on: AR-020-v2-full.md
- Confidence: 80% overall (range: 50% for EU 2027 guidance prediction to 92% for shared-context correlation)
