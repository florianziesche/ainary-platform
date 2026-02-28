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