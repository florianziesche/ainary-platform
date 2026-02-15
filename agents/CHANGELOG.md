# Changelog — Research Pipeline

*Audit trail of all changes to pipeline, templates, evals, and systems.*

---

## Entry Template
```
## YYYY-MM-DD — [Title]
- **Change ID:** CL-[NNN]
- **Component:** [Pipeline | SP-XXX | Eval Pack | Systems | Registry]
- **What changed:**
- **Why (failure mode / feedback):**
- **Expected impact:**
- **Observed impact:** [fill after 3 reports]
- **Regressions / trade-offs:**
- **Approved by:** [Florian | Mia]
```

---

## 2026-02-15 — Initial Pipeline v1.0 (Mia ad-hoc)
- **Change ID:** CL-001
- **Component:** Pipeline
- **What changed:** Created 6-phase pipeline (Research → Experiment → Synthese → Adversarial → Revision → Polish). No formal templates.
- **Why:** Needed structure for A+ reports (AR-026 to AR-030)
- **Expected impact:** Better quality than B+ pipeline
- **Observed impact:** QA found real errors in ALL 5 reports: math errors (AR-026), cost inconsistencies (AR-027), percentage mistakes (AR-028), cherry-picked citations (AR-029), data discrepancies (AR-030). Pipeline worked but had no consistency enforcement.
- **Regressions:** Ad-hoc prompts → each agent got different quality of instructions
- **Approved by:** Florian (implicit — approved A+ approach)

## 2026-02-15 — Pipeline v2.0 (Merge with Exec Research Factory)
- **Change ID:** CL-002
- **Component:** Pipeline + All spawn templates + Systems
- **What changed:**
  - Merged ChatGPT Exec Research Factory structure with Mia pipeline
  - Added: Control Panel, Risk Tiers, Source Log, Claim Ledger, Contradiction Register
  - Added: E/I/J/A claim classification (Evidence/Interpretation/Judgment/Assumption)
  - Added: 16-point Rubric (replacing free-form scores)
  - Added: "No new claims in Repair" rule
  - Added: Asset Builder as Phase 9
  - Created 7 canonical spawn templates
  - Created 8 supporting systems (Prediction Scorecard, Freshness Decay, Claim Lifecycle, Knowledge Graph, Topic Selection, Feedback Loop, Orchestrator Checklist, Consistency Enforcement)
  - Created Prompt Registry + this Changelog
  - Created Eval Pack with 10 regression tests
- **Why:**
  - 30 reports produced with v1 showed systematic issues: math errors, confidence clustering, circular citations, no asset building, no external feedback
  - ChatGPT system had better structure (artifacts, rubric, governance) but lacked multi-agent execution and experiments
  - Merge combines structural rigor with execution capability
- **Expected impact:**
  - Fewer math errors (mandatory verification step)
  - More honest confidence ratings (rubric forces justification)
  - No circular self-citation (mandatory internal labeling)
  - Reusable knowledge (Asset Builder)
  - Consistent agent behavior (spawn templates vs ad-hoc)
- **Observed impact:** [PENDING — first v2 report not yet produced]
- **Regressions / trade-offs:**
  - More overhead per report (Source Log + Claim Ledger + more phases)
  - Longer pipeline (7 agents vs 3-4)
  - Higher cost per report (~$20-30 vs $15-20)
  - Risk: templates become bureaucratic checkbox exercise instead of quality driver
- **Approved by:** Florian (explicit — "Ja, mach das")

---

*Next entry after first v2 report is produced and QA'd.*
