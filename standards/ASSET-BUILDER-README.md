# Asset Builder — Operating Manual (v1.0)

## Purpose
Convert approved executive research reports into reusable assets:
- Atomic Notes
- Playbooks
- Templates
- RAG-ready JSON (entities + relations + retrieval hints)

## When to use
Use when:
- A research report is approved (Tier 2 or Tier 3 preferred)
- You want to operationalize research into reusable, searchable building blocks

Do NOT use when:
- The report is unreviewed or missing sources
- You need new research (Asset Builder does not browse by default)

## Inputs
Required:
- Final research report text (including Executive Summary + Key Takeaways + Appendix if available)

Optional:
- Source Log
- Claim Ledger
- Contradiction Register

## Outputs (Asset Pack)
1) Title + Date
2) Asset Index (navigation + coverage map)
3) Atomic Notes
4) Playbooks
5) Templates
6) RAG JSON Writeback (JSON array)

## Quality Gates (mandatory)
- Coverage: each Key Takeaway maps to ≥ 1 asset
- Dedupe: no duplicate assets answering the same question
- Traceability: each asset labeled Evidenced / Derived / Operational, with sources if available
- Actionability: each playbook/template has trigger, steps, failure modes, acceptance criteria
- JSON compliance: output conforms to the schema in `02_AB_SCHEMA__RAG_JSON_Spec.md`

## Asset Types
- Atomic Note: one concept/claim in a reusable unit
- Playbook: repeatable process to achieve a goal
- Template: copy/paste scaffold for consistent execution
- Entity: concept/tool/org/person/method used for RAG graphs

## Definition of Done
Done when:
- Quality gates pass
- IDs are stable and unique within the output
- Coverage map is complete
- No “Evidenced” labels without citations when citations exist/are required
