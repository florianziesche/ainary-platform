# E/I/J/A Framework — Epistemic Labeling Standard (v1.0)

## Purpose
Every sentence in a research output must be labeled with its epistemic status.
This is non-negotiable for Tier 2+ reports.

## The Four Labels

### E — Evidenced
Backed by peer-reviewed research, primary data, official standards, or verified first-party sources.
- MUST cite [S#]
- MUST have DOI, URL, or official reference
- Confidence floor: 70%

**Example:**
> [E] Self-consistency calibration reduces ECE from 42% to 27.3% in biomedical QA [S8].

### I — Interpreted
Derived from evidence through logical inference. The evidence exists, but the conclusion requires reasoning.
- MUST reference which evidence it's derived from
- MUST explain the logic chain
- Confidence floor: 40%

**Example:**
> [I] If RLHF damages calibration [S7] and most deployed models use RLHF, then most deployed models are likely miscalibrated. This has not been directly measured in production.

### J — Judged
Assessment based on pattern recognition, expert experience, or qualitative reasoning. No direct evidence.
- MUST state it's a judgment
- MUST explain what assumptions underlie it
- Confidence floor: 20%
- If confidence < 50%: mark "NEEDS HUMAN REVIEW"

**Example:**
> [J] Based on adoption patterns in enterprise AI, we estimate 12-24 months before calibration becomes a competitive requirement. This is a judgment based on EU AI Act timeline [S14] and Gartner predictions [S22], not empirical measurement.

### A — Actionable
Recommendation based on a combination of E + I + J. The label shows the reader exactly what the recommendation rests on.
- MUST reference which E, I, and J findings support it
- MUST include "If wrong:" — what happens if this recommendation is wrong
- MUST include phased implementation (not just "do X")

**Example:**
> [A] Implement consistency-based calibration (3 API calls per decision) as Tier 1 baseline.
> Based on: [E] 27.3% ECE reduction [S8], [I] likely generalizes to non-biomedical domains, [J] cost of $0.0005-$0.015/check is acceptable for most enterprise use cases.
> If wrong: Worst case is 3x API cost increase with no calibration benefit in your specific domain. Reversible within 1 sprint.

## Self-Calibrating Protocol

Every report that uses E/I/J/A MUST calibrate itself:

1. **Section Confidence**: Each major section carries a confidence % with explanation
2. **Label Distribution**: Report must disclose its E/I/J/A ratio
   - Healthy: >50% E, <20% J
   - Warning: <30% E or >30% J
   - Red flag: >50% J (opinion piece, not research)
3. **Consistency Check**: 3-5 key claims tested with rephrased prompts (Budget-CoCoA)
4. **Cross-CRT Check**: Claims validated against Compounding Research Truths
5. **Correction Check**: Claims checked against corrections.json
6. **Meta-Note**: Report states which calibration methods it applied to itself

## Integration with AgentTrust

| EIJA Label | Admiralty Rating | Typical Confidence |
|---|---|---|
| E (Evidenced) | A1-A2 | 70-95% |
| I (Interpreted) | B2-C3 | 40-70% |
| J (Judged) | C3-D4 | 20-50% |
| A (Actionable) | Composite | Weighted avg of supporting E/I/J |

## Integration with Beipackzettel

The Beipackzettel MUST include:
- E/I/J/A distribution (e.g., "E: 14, I: 8, J: 3, A: 5")
- Weakest label category (e.g., "Most judgments are in Section 5 — cost estimates")
- Self-calibration results (e.g., "3/5 key claims passed consistency check")

## RAG Integration Point

RAG outputs are ALWAYS labeled:
- RAG hit with DOI → E (Evidenced)
- RAG hit without DOI → I (Interpreted, source exists but unverified)
- RAG miss (no relevant hit) → J (Judged, must state "no RAG evidence found")
- Recommendation from RAG-supported analysis → A (Actionable)

## Anti-Patterns
- ❌ Unlabeled claims in body text
- ❌ "A" recommendations without supporting E/I/J references
- ❌ "E" labels on blog posts or LLM outputs
- ❌ Section Confidence > 90% with >30% J-labeled claims
- ❌ Self-calibrating protocol skipped for Tier 2+
