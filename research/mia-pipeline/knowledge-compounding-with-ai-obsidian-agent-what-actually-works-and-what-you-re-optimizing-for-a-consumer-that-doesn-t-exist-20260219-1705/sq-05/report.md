### Answer to: Which user segments actually need calibrated AI outputs (per CT-011, CT-012) vs. those satisfied with 'good enough' responses?

**Key Findings:**
- **High-stakes domains require calibration but evidence is domain-limited** [E] [S8]: Biomedical NLP shows 84% of scenarios exhibit overconfidence with 42% ECE for verbalized confidence vs 27.3% for consistency-based methods, indicating critical need for calibration in medical applications
- **Regulatory requirements don't mandate calibration** [E] [S14]: EU AI Act Art 15 requires 'accuracy', NOT 'calibration', with enforcement beginning Aug 2026, suggesting regulatory pressure may not drive calibration adoption
- **Human oversight degrades over time** [E] [S15]: Human vigilance drops 20-50% after 30 minutes monitoring automated systems, indicating users in monitoring roles need calibrated confidence to maintain appropriate skepticism
- **RLHF-aligned models systematically damage calibration** [E] [S7]: RLHF systematically damages calibration because reward models prefer confident responses, meaning mass-market models optimized for user satisfaction inherently provide poor calibration
- **Cost barriers exist for calibration** [E] [S19]: Budget-CoCoA practical implementation costs $0.0005-$0.015 per confidence check, creating economic friction for high-volume applications
- **Some models permanently uncalibratable** [E] [S30]: Research identifies "calibratable vs non-calibratable regimes" where some RLHF-aligned models are permanently damaged and others recoverable

**Evidence Quality:**
- **Strongest source**: [S8] provides concrete quantitative evidence from biomedical domain with 84% overconfidence scenarios and specific ECE measurements
- **Weakest point**: No direct user research on willingness-to-pay or demand segmentation; evidence is primarily technical rather than market-focused
- **What's missing**: Cross-domain validation beyond biomedical, user preference studies, market size data for high-stakes vs mass-market segments, actual regulatory enforcement patterns

**So What:** [I] The evidence suggests a bifurcated market: high-stakes domains (medical confirmed, likely legal/financial) demonstrate clear technical need for calibration due to overconfidence risks, but mass-market users appear satisfied with confident-but-miscalibrated responses that RLHF optimizes for. [J] The technical complexity may only be justified for specialized high-stakes applications rather than general consumer AI.

**Claims (for Claim Ledger):**
- Biomedical AI shows 84% overconfidence scenarios | [S8] | E | High | Strong quantitative evidence
- EU AI Act requires accuracy not calibration | [S14] | E | High | Official regulatory text  
- Human vigilance drops 20-50% after 30min automation monitoring | [S15] | E | High | Peer-reviewed human factors research
- RLHF systematically damages calibration via confident response preference | [S7] | E | High | NeurIPS 2024 Tier 1 source
- Budget-CoCoA costs $0.0005-$0.015 per confidence check | [S19] | E | Medium | Practitioner blog source
- Some RLHF models permanently uncalibratable | [S30] | E | Medium | ICML 2025 but recent
- High-stakes users need calibration, mass-market satisfied with confidence | No source | J | Low | Inference from technical evidence