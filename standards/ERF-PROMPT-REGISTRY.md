# Prompt Registry — Exec Research Factory (v1.1)

## Purpose
Single source of truth for which prompts exist, who owns them, and which are approved for Tier 2/3 use.

## Registry Table
| Prompt ID | Name | Owner | Allowed Tiers | Current Version | Status | Canonical Location | Last Eval Date | Last Score | Known Limitations |
|---|---|---|---|---|---|---|---|---|---|
| ER-PROD | Exec Research Factory — Producer | [Name] | 1/2/3 | v2.0 | Active | 06_SYSTEM_PROMPT__Exec_Research_v2.txt | [YYYY-MM-DD] | [__/16] | Depends on source quality; may need explicit contradiction prompts on messy topics |
| ER-REV | Exec Research Factory — Reviewer | [Name] | 2/3 | v1.0 | Active | 07_REVIEWER_PROMPT__Exec_Research_v1.txt | [YYYY-MM-DD] | [__/16] | Can over-penalize novel synthesis; mitigate by requiring precise fix requests |

## Registry Rules
- Only **Active** prompts may be used for Tier 2/3 deliverables.
- Tier 2 requires: Producer + Reviewer + Repair pass.
- Tier 3 requires: Tier 2 controls + injection/adversarial tests + human sign-off.

## Deprecation Rule
If a prompt is replaced:
- Mark status = Deprecated
- Link the replacement prompt ID/version
- Record the reason in 05_CHANGELOG
