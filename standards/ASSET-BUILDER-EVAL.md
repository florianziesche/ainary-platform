# Asset Builder — Eval Pack (v1.0)

## Rubric (0–2 each; total 12)
1) Coverage of Key Takeaways
2) Dedupe quality (no redundant assets)
3) Retrieval quality (this_answers, explicit nouns, tags)
4) Traceability labeling (classification + sources)
5) Playbook actionability (trigger/steps/failure modes/criteria)
6) JSON schema compliance (fields present, IDs stable, references valid)

## Pass thresholds
- Tier 1 packaging: ≥ 8/12
- Tier 2 packaging: ≥ 10/12
- Tier 3 packaging: ≥ 11/12 and no “uncited but labeled Evidenced” issues

## Test Cases
AB-01: Short report → 10–20 atomic notes, 1–2 playbooks, 2–5 templates
AB-02: Contradictory report → contradiction assets + explicit caveats
AB-03: Highly procedural report → strong playbooks + templates, fewer notes
AB-04: Poorly sourced report → many Derived/Operational labels; confidence reduced
AB-05: Duplicate-heavy extraction → dedupe merges into canonical assets + aliases
