# META-LEARNINGS — What 30+ Reports Taught Us

*Last updated: 2026-02-19*
*Sources: CHANGELOG.md, Framework-Comparison.md, daily/2026-02-14.md, daily/2026-02-15.md*

---

## Quality Failures (empirical, from QA)

### L1: Every report with calculations had wrong math
- **Source:** 10 Learnings from 30 Reports (CHANGELOG.md CL-002, 2026-02-15)
- **Evidence:** AR-026 had 8/8 Exhibit values wrong ("+45%" → "+54%"), AR-027 ROI 9-53x → 10-18x, AR-028 NIST 50% → 45%, AR-030 SWE-bench 77.2% → 64.8%
- **Implication:** Mandatory math verification step in every pipeline run. Never trust LLM arithmetic.

### L2: Confidence clusters suspiciously at 62-82%
- **Source:** 10 Learnings from 30 Reports (CHANGELOG.md CL-002)
- **Evidence:** Across 30 reports, confidence scores avoid extremes. No report below 60% or above 85%. This is calibration theater.
- **Implication:** Rubric must force justification for confidence. Proposed formula: Evidence Ratio × 0.5 + Source Score × 0.35 + 15% base (D-173, 2026-02-15).

### L3: Cherry-picked citations passed QA undetected
- **Source:** AR-029 QA (CHANGELOG.md CL-001, 2026-02-15)
- **Evidence:** AR-029 cherry-picked Sinha citation to support thesis. QA initially missed it. Only caught in second review.
- **Implication:** QA must audit BEFORE editing. Claim Ledger with E/I/J/A classification on every claim.

### L4: QA scores don't compound — they're flat
- **Source:** 10 Learnings, AR-029 proof (CHANGELOG.md CL-002); AR-015 Knowledge Compounding report (daily/2026-02-15)
- **Evidence:** AR-029 scored 84.8 → 87.6 → 83.4 across iterations. Pipeline QA average ~85.6 across 30 reports. Quality NOT compounding.
- **Implication:** System improvements (templates, rubrics) compound, but individual report QA doesn't auto-improve. Need structural fixes, not more iterations.

### L5: Mia's research scores FAIL on Florian's rubric (8-11/16)
- **Source:** Framework-Comparison.md (Vault, 2026-02-11/15)
- **Evidence:** Top-20-Papers: 8/16, Agent-Developments: 9/16, Cross-Pattern-Insights: 11/16. All below Tier 2 threshold of 13/16. Missing: Intake, Research Brief, Claim Ledger, Contradiction Register.
- **Implication:** Content aggregation ≠ executive research. Need Intake + Top-5 Claims + Contradiction Register (85 min overhead → 13-14/16).

---

## Process Failures (what broke in the pipeline)

### L6: Fix agents introduce unverified new claims
- **Source:** 10 Learnings from 30 Reports (CHANGELOG.md CL-002)
- **Evidence:** Fix agents added new uncited claims during repair passes. "No new claims in Repair" rule created as response.
- **Implication:** Cardinal Rule: Fix agents may only correct existing claims, never introduce new ones. Enforced in SP-FIX template.

### L7: Ad-hoc prompts → inconsistent agent behavior
- **Source:** Pipeline v1.0 → v2.0 transition (CHANGELOG.md CL-001, CL-002)
- **Evidence:** v1 pipeline had no spawn templates. Each agent got different quality instructions. All 5 A+ reports (AR-026-030) had errors despite "A+" designation.
- **Implication:** 7 canonical spawn templates + Prompt Registry. Every agent gets identical structure.

### L8: v2 pipeline kills originality — produces surveys, not thought leadership
- **Source:** AR-001-v2 first run (CHANGELOG.md CL-003, 2026-02-15)
- **Evidence:** v2.2 scored 15/16 on accuracy but 3/10 on originality. v1 had "Overconfidence Pandemic" thesis, "Three-Layer Trust Stack" framework, bold predictions. v2 had none. Root cause: no phase asked "What's our original contribution?"
- **Implication:** v2.3 "Originality Engine" created: Thesis Development Agent (SP-THE), Gap Map in Research Agent, Section Title Rule ("arguments not categories"), QA dimensions expanded to 10/20 with Intellectual Contribution + Narrative & Boldness.

### L9: 30 reports produced zero reusable assets
- **Source:** 10 Learnings (CHANGELOG.md CL-002)
- **Evidence:** No atomic notes, no playbooks, no templates, no RAG JSON created from any report.
- **Implication:** Asset Builder added as Phase 9. Every report must produce reusable knowledge artifacts.

### L10: Cross-references create citation cartel (self-citation as evidence)
- **Source:** 10 Learnings (CHANGELOG.md CL-002); Consistency Audit (daily/2026-02-15)
- **Evidence:** Reports citing other Ainary reports as evidence for claims. 4 critical contradictions found across AR-019, AR-016, AR-028, AR-001.
- **Implication:** Mandatory internal labeling. Self-citations must be explicitly marked [INTERNAL]. Cannot be sole evidence for any claim.

---

## What Works (proven patterns)

### L11: Context Pack = -47% time, -44% tokens, +6 QA points
- **Source:** A/B Test, Reports #1 vs #2 (daily/2026-02-14)
- **Evidence:** Report #1 (no pack): 17 min, 840K tokens, QA 82. Report #2 (with pack): 9 min, 470K tokens, QA 88. Less noise = more focus.
- **Implication:** Context Packs are standard for ALL reports. Dynamic packs (topic-specific) planned as Level 2.

### L12: Adversarial review = highest ROI pipeline step
- **Source:** 10 Learnings (CHANGELOG.md CL-002)
- **Evidence:** Consistently catches errors that Writer and Fix agents miss. QA found real errors in ALL 5 A+ reports.
- **Implication:** QA is non-negotiable. But the theatrical "adversarial self-review" section was removed (D-161) — inline caveats + Transparency Note are stronger.

### L13: Reports correcting other reports are most valuable
- **Source:** 10 Learnings (CHANGELOG.md CL-002)
- **Evidence:** Cross-report corrections propagate knowledge. AR-015 used own data as evidence — strongest report.
- **Implication:** Build correction chains. When a claim is updated, trace all reports using that claim.

### L14: Sonnet for QA/Builder = same quality, 40% cheaper
- **Source:** Pipeline experiments (daily/2026-02-14)
- **Evidence:** QA Opus 87 vs Sonnet 85 (minimal). Builder Sonnet: 31 sec vs Opus ~6 min. Cost per report: ~$2.50 vs ~$5.13.
- **Implication:** Opus for Writer/Thesis (creativity), Sonnet for QA/Builder/Validation (rule-following). D-110.

### L15: v2.3 Originality Engine restores thesis quality
- **Source:** AR-001-v2.3 first run (CHANGELOG.md CL-005, 2026-02-15)
- **Evidence:** v2.3 scored 82/100 total (v1: 57, v2: 66). Originality 8 (v1:9, v2:3), Methodology 9 (v1:4, v2:9). "Trust Race Model" framework created. 2 blockers found and fixed.
- **Implication:** Thesis Agent is the key innovation. Pipeline now produces both rigor AND originality.

---

## What Doesn't Work (anti-patterns with evidence)

### L16: "Simulation" labeled as "Experiment" — agents exaggerate
- **Source:** 10 Learnings (CHANGELOG.md CL-002)
- **Evidence:** Agents systematically call thought experiments "experiments" and simulations "studies." This inflates perceived rigor.
- **Implication:** Experiment types expanded with strict labels. "none" → "none_with_justification." thought_experiment and constructed_scenario are separate categories.

### L17: Zero external feedback across 30 reports
- **Source:** 10 Learnings (CHANGELOG.md CL-002); KW7 accountability (daily/2026-02-15)
- **Evidence:** 0 external reviews. 0 distribution. 0 revenue. All build, zero validation. Pattern: hiding in systems building.
- **Implication:** Biggest gap. External calibration mandatory for important deliverables. KW8 target: 3 external feedbacks.

### L18: Gold decoration undermines credibility
- **Source:** Florian report feedback (daily/2026-02-14)
- **Evidence:** "Zu viel Gold = verspielt." Gold only for CTAs + 1-2 key numbers. No boxes, no icons, no borders. Print-first. Benchmark: Economist, McKinsey, Nature.
- **Implication:** "Strong content needs no decoration." Restraint = confidence. Anchored in pipeline-pack.md.

### L19: Personal story in research reports doesn't work
- **Source:** Florian feedback (daily/2026-02-14)
- **Evidence:** "KEINE Personal Story in Research Reports." Blog = personal hook. Report = authority through evidence.
- **Implication:** Content type rules: Report (no story), Blog (personal hook), LinkedIn (specific "this week I...").

---

## Open Questions (unresolved)

### Q1: How to measure knowledge compounding quantitatively?
- **Source:** AR-015, Knowledge Compounding discussion (daily/2026-02-15)
- **Evidence:** Nobody has quantitatively measured it. Luhmann, Forte, Matuschak = anecdotal. 3 proxies proposed: Emergence Rate, Self-Reference Ratio, Value per Note.
- **Status:** KCI v2 framework proposed but untested.

### Q2: Should confidence scores use a formula or remain qualitative?
- **Source:** D-173 (daily/2026-02-15)
- **Evidence:** Current scores are "vibes." Proposed: Evidence Ratio × 0.5 + Source Score × 0.35 + 15% base. NOT YET FINALIZED.
- **Status:** Florian to decide.

### Q3: Can QA scores ever compound, or is flat ~85 the ceiling?
- **Source:** AR-015, 10 Learnings (CHANGELOG.md CL-002)
- **Evidence:** QA flat at ~85.6 despite pipeline improvements. Efficiency compounds (tokens -50%, memory 20%→96%), quality doesn't.
- **Status:** Hypothesis: structural changes (v2.3 Thesis Agent) may break the ceiling. Need 10+ v2.3 reports to test.

### Q4: What's the right tier-based rigor model?
- **Source:** Framework-Comparison.md recommendations
- **Evidence:** Proposed: Tier 1 (speed, 5 min overhead), Tier 2 (85 min → 13-14/16), Tier 3 (4-6h → 15-16/16). Not yet validated in practice.
- **Status:** First Tier 2 v2.3 run successful. Need more data.

### Q5: How to prevent "forced originality" — frameworks that don't hold up?
- **Source:** v2.3 risk assessment (CHANGELOG.md CL-004)
- **Evidence:** Thesis Agent may invent frameworks without empirical backing. Mitigation: Validation Agent checks originality quality, not just presence.
- **Status:** Monitoring. AR-001-v2.3 "Trust Race Model" seems solid but untested externally.

---

*Total learnings: 19 + 5 open questions. Each sourced and evidenced.*
