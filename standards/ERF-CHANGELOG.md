# Changelog — Exec Research Factory (v1.1)

## Purpose
Audit trail of changes to prompts/templates/evals, including rationale and measured impact.

## Entry Template
- Date:
- Change ID: (optional)
- Component changed: (ER-PROD / ER-REV / Template / Eval Pack / README)
- What changed (precise):
- Why (failure mode / feedback):
- Expected impact:
- Observed impact (eval score delta, error reduction):
- Regressions / trade-offs introduced:
- Risk tier impact: (Tier 2/3 readiness?)
- Approved by: (Tier 3 required)

---

## 2026-01-06 — Initial Release
- Date: 2026-01-06
- Component changed: Project + ER-PROD + ER-REV
- What changed:
  - Created Exec Research Factory workflow and core docs
  - Added Producer system prompt v2.0
  - Added Reviewer prompt v1.0 (audit-only quality layer)
- Why:
  - Need repeatable executive research with traceability and explicit uncertainty
  - Need a practical QA loop inside ChatGPT UI without external eval infrastructure
- Expected impact:
  - Higher evidence discipline, fewer uncited load-bearing claims, clearer contradictions and uncertainty
- Regressions / trade-offs:
  - Slightly slower workflow (extra review step)
  - More artifacts to maintain (Source Logs, Claim Ledger)
- Risk tier impact:
  - Enables Tier 2/3 readiness by design
- Approved by: [Name]
