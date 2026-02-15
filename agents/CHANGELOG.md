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

## 2026-02-15 — Pipeline v2.2 First Run (AR-001-v2)
- **Change ID:** CL-003
- **Component:** Pipeline validation
- **What changed:** First manual v2 run completed. AR-001-v2 produced through full pipeline.
- **Observed impact:** QA 15/16. Math all correct. Camunda source missed (caught by QA, fixed). BUT: report was a survey, not thought leadership. No original thesis, no framework, no narrative arc. v1 had stronger ideas with weaker methodology.
- **Key learning:** Pipeline optimizes for accuracy and verifiability but NOT for originality. Without a thesis phase, agents produce consultant-grade surveys.
- **Approved by:** Florian ("v2.2 ist gut")

## 2026-02-15 — Pipeline v2.3 "Originality Engine"
- **Change ID:** CL-004
- **Component:** Pipeline + SP-RES + SP-THE (NEW) + SP-WRT + SP-QA + SP-VAL + TEMPLATE-RULES + QA-SPEC
- **What changed:**
  1. **NEW Phase 2.5: Thesis Development Agent** (SP-THE v1.0) — transforms research into original thesis, framework, scenario, narrative arc, "nobody else is saying"
  2. **Research Agent:** Added Gap Map (5 sections), Source Diversity Requirement (~1/3 industry + 1/3 academic + 1/3 practitioner), Synthesis Opportunities for Thesis Agent
  3. **Writer Agent:** Thesis document as #2 input (drives everything), Section Title Rule (arguments not categories), Key Insight Rule (must be original), Constructed Scenario integration
  4. **QA Agent:** Rubric expanded from 8→10 dimensions (/20 scale). New: #9 Intellectual Contribution, #10 Narrative & Boldness. Prediction Boldness Check. Source Diversity Check. Thresholds: Tier 2 ≥16/20, Tier 3 ≥18/20
  5. **Validation Agent:** Added 4c Originality Check ("Would an expert learn something new?")
  6. **Experiment types expanded:** Added thought_experiment, constructed_scenario. "none" → "none_with_justification" (must explain why)
  7. **REMOVED: Adversarial Self-Review as standalone section.** Replaced by: inline caveats in body sections + 5-7 limitation bullets in Transparency Note + Conflict of Interest statement
  8. **Author Bio updated:** Factual, no slogans. "Florian Ziesche is the founder of Ainary Ventures and former CEO of 36ZERO Vision, where he raised €5.5M+ and delivered AI solutions for BMW, Siemens, and Bosch."
  9. **Control Panel:** Added ORIGINAL_THESIS and NARRATIVE_ARC fields (required Tier 2+)
  10. **All templates:** Added Phase 0: PLAN section (think before doing)
- **Why (failure mode):**
  - AR-001-v2 scored 15/16 on accuracy but 3/10 on originality
  - v1 had: Three-Layer Trust Stack, Overconfidence Pandemic thesis, HITL Spiral, provocative section titles, bold predictions
  - v2 had: none of this. Pipeline produced a survey, not thought leadership
  - Root cause: no phase asked "What's our original contribution?" and Research Agent optimized for consensus instead of gaps
- **Expected impact:**
  - Reports with original theses that experts would debate
  - Named frameworks where data supports them
  - Constructed scenarios that combine empirical findings into novel chains
  - Section titles that tell a story, not an index
  - Predictions that are actually controversial
  - Honest limitations without theatrical role-play
  - Professional author bio that builds credibility through facts
- **Observed impact:** [PENDING — first v2.3 report not yet produced]
- **Regressions / trade-offs:**
  - One more agent per pipeline run (+$3-5 for Thesis Agent on Opus)
  - Risk: "Forced originality" — agent invents frameworks that don't hold up
  - Mitigation: Validation Agent now checks originality quality, not just presence
  - Adversarial removal risk: less explicit self-criticism → mitigated by inline caveats + Transparency Note expansion
- **Approved by:** Florian (explicit — "Deine empfehlungen + Adversarial und bio heraus")

---

## 2026-02-15 — AR-001-v2.3 First Originality Engine Run
- **Change ID:** CL-005
- **Component:** Pipeline validation (full v2.3 run)
- **What changed:** First v2.3 pipeline run on AR-001 "State of AI Agent Trust 2026"
- **Observed impact:**
  - Thesis Agent produced "Trust Race Model" framework (4 components) + "Governance Lag Cascade" scenario (6 steps)
  - QA scored 18/20 (vs 15/16 on v2.2). New dimensions: Intellectual Contribution 2/2, Narrative & Boldness 2/2
  - 2 Blockers found (misquoted HBR 72→86%, unsourced Vectra claim) — both fixed
  - Source diversity: 3 academic + 3 contrarian added (v2.2 had 0+0)
  - Total score estimate: 82/100 (v1: 57, v2: 66)
  - Pipeline timing: ~20min total (same as v2.2)
- **Regressions:** Originalität 8 not 9 (v1 "Overconfidence Pandemic" was bolder than "Trust Race"). Budget-CoCoA asymmetry lost.
- **Approved by:** Florian (reviewed and sent final edits)

## 2026-02-15 — Template Decisions: System Disclosure, CoI, About This Report
- **Change ID:** CL-006
- **Component:** TEMPLATE-RULES + Pipeline
- **What changed:**
  - System Disclosure section REMOVED (redundant with Methodology Full + About This Report)
  - Conflict of Interest wording finalized (not bold, no service list, covers research+build+advisory)
  - "About This Report" confirmed on last page
- **Why:** Florian reviewed v2.3 output and flagged redundancy + CoI service description issues
- **Approved by:** Florian (explicit — multiple review rounds)

---

*Next: Tuesday Feb 17 — second v2.3 report on Tier 2 topic. Wednesday Feb 18 — pipeline.py orchestrator.*
