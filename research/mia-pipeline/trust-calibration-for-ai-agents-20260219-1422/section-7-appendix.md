## Appendix

### Claim Ledger

| ID | Claim | Label | Admiralty | Sources |
|----|-------|-------|-----------|---------|
| CL-01 | Current calibration methods require logit access and don't compose for multi-agent systems | [E] | A1 | S1, S9 |
| CL-02 | RLHF can permanently damage some models' calibration while others are recoverable | [E] | A1 | S30 |
| CL-03 | EU AI Act requires 'accuracy' but never mentions 'calibration', creating regulatory vacuum | [E] | A1 | S14 |
| CL-04 | Healthcare sector shows 27.3% ECE with consistency calibration vs 42% verbalized | [E] | A1 | S8 |
| CL-05 | Budget-CoCoA calibration costs $0.0005-$0.015 per check | [E] | B2 | S19 |
| CL-06 | Temperature scaling requires model logit access, limiting production deployment | [E] | A1 | S1 |
| CL-07 | Conformal Uncertainty (ConU) methods fail to compose in multi-agent systems | [E] | A1 | S9 |
| CL-08 | Healthcare, finance, and hiring sectors face immediate EU AI Act compliance pressure by August 2026 | [E] | A1 | S14 |
| CL-09 | No major cloud provider explicitly offers multi-agent calibration infrastructure | [I] | B2 | S3, S19 |
| CL-10 | Conformal prediction requires 200-500 calibration examples per model | [E] | A1 | S9 |
| CL-11 | Sectors with existing regulatory frameworks may have calibration readiness advantage | [J] | C3 | - |
| CL-12 | CEN/CENELEC standards development window provides opportunity for calibration requirement inclusion | [I] | B2 | S14 |

### Source Log

| ID | Title | Type | Admiralty | URL/Reference |
|----|-------|------|-----------|---------------|
| S1 | On Calibration of Modern Neural Networks | Peer-reviewed paper | A1 | 10.48550/arXiv.1706.04599 |
| S3 | Budget-CoCoA: Practical Calibration Methods | Technical documentation | B2 | Industry source |
| S8 | Calibration as Measurement of Trustworthiness in Biomedical NLP | Peer-reviewed paper | A1 | PMC12249208 |
| S9 | ConU: Conformal Uncertainty in LLMs | Conference paper | A1 | NeurIPS 2024 |
| S14 | EU AI Act | Official regulation | A1 | Official Journal EU |
| S19 | 5 Methods for Calibrating LLM Confidence Scores | Industry blog | C3 | Latitude.so Blog |
| S30 | Restoring Calibration for Aligned LLMs | Conference paper | A1 | ICML 2025 |

### Research Confidence Assessment

**High Confidence Areas (85-90%)**
- Technical gaps in multi-agent calibration methods
- EU AI Act requirements and timeline
- Current calibration method limitations

**Medium Confidence Areas (70-80%)**
- Sector-specific calibration readiness levels
- Implementation costs at scale
- RLHF damage permanence patterns

**Low Confidence Areas (50-65%)**
- Competitor positioning specifics (limited public documentation)
- CEN/CENELEC influence pathways
- Multi-agent composability solutions

### Critical Uncertainties

1. **Multi-agent calibration composability**: No proven methods exist for calibrating decisions across multiple interacting AI agents
2. **RLHF damage reversibility**: Limited evidence on which model architectures can recover from calibration damage
3. **Competitor capabilities**: Major cloud providers' internal calibration R&D remains opaque
4. **Regulatory interpretation**: How EU regulators will interpret "accuracy" requirements in practice

**For the decision maker:** The claim ledger demonstrates strong evidence for a technical gap in multi-agent calibration that aligns with imminent EU regulatory requirements, but competitor positioning remains the largest intelligence gap.

Section Confidence: 85%