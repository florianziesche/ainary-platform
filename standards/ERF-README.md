# Exec Research Factory — Operating Manual (v1.0)

## Purpose
This Project produces **decision-grade executive research** with:
- **Traceable evidence**
- **Explicit uncertainty**
- **Clear separation:** Evidence vs Interpretation vs Judgment/Recommendations

## Scope (When to use this)
Use for:
- Executive research reports informing real decisions
- Market / competitive / technology reviews
- Operating model, vendor selection, risk assessment, strategy memos

Do NOT use for:
- Pure creative writing
- Casual brainstorming without a decision to inform
- Tasks where correctness does not matter

## Roles & Responsibilities
- **Prompt Owner**
  - Owns templates, Producer/Reviewer prompts, eval packs, quality thresholds
  - Approves Tier 3 prompt changes
- **Author / Operator**
  - Runs the workflow per this README
  - Maintains Source Logs and report artifacts
  - Applies Reviewer fix requests
- **Reviewer**
  - Scores rubric
  - Runs Claim Audit and contradiction scan
  - Blocks Tier 3 release if blockers exist

## Risk Tiers (Required Controls)
### Tier 1 (Low stakes)
Examples: early internal exploration, ideation, rough drafts  
Required:
- Use Executive Report Template
- Basic self-check  
Recommended:
- Optional Reviewer pass

### Tier 2 (Medium stakes)
Examples: internal decision support, investor-facing internal material  
Required:
- Source Log (per report)
- Reviewer rubric score + Claim Audit
- Repair pass using fix requests

### Tier 3 (High stakes)
Examples: public-facing, regulated domains, legal/medical/financial claims, actions/agents/tools  
Required:
- All Tier 2 controls
- Prompt injection / adversarial tests
- Stricter provenance: citations for every load-bearing claim
- Human sign-off before release

## Standard Workflow (Always follow this order)
1) **Intake** (use template in `01_TEMPLATES__Copy_paste_blocks.md`)
2) **Research Brief** (Producer)
3) **Source Log** (Operator fills; Producer may help create skeleton)
4) **Draft Report** (Producer)
5) **Review** (Reviewer rubric + Claim Audit + contradiction scan)
6) **Repair** (Producer applies fix requests; no new uncited factual claims)
7) **Release** (final report + archive artifacts + log any changes)

## Definition of “Done”
A report is done when:
- All required sections exist (Executive Report Template)
- Every load-bearing claim is either:
  - **Cited**, or
  - Labeled **Assumption**, or
  - Labeled **Interpretation** with reasoning
- Contradictions are resolved or explicitly presented with implications
- Uncertainty is explicit (confidence labels + what evidence would change conclusions)

## Minimum Quality Thresholds
- Tier 1: Recommended Reviewer score ≥ 10/16 (optional)
- Tier 2: Required Reviewer score ≥ 13/16 and no blockers
- Tier 3: Required Reviewer score ≥ 15/16 + injection test passes + human sign-off

## House Rules (Non-negotiable)
- No invented sources, quotes, metrics, or consensus.
- Separate Evidence vs Interpretation vs Judgment.
- If evidence is weak, state low confidence and explain why.
- Use retrieval-first writing: explicit nouns, standalone bullets, explicit relationships.

## Escalation Rules
Escalate to Tier 3 controls if:
- External/public distribution
- Regulated or compliance-sensitive topic
- Material impact on reputation, revenue, compliance, or security

## How to Start a New Report (Operator Checklist)
- Create a new chat in this Project
- Paste and fill the Intake Template
- Generate Research Brief
- Create a new Source Log file (copy the blank template)
- Generate Draft Report
- Run Reviewer pass
- Repair and re-run Reviewer if Tier 2/3
- Archive artifacts and update changelog if process/prompt changed
