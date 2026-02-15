# A+ Research Pipeline v2.0

*Merge: Exec Research Factory (ChatGPT) + Mia A+ Pipeline (OpenClaw)*
*Created: 2026-02-15 | Owner: Florian Ziesche*

---

## Origin

This pipeline merges two systems:
1. **Exec Research Factory** — Florian's ChatGPT system (structured, artifact-driven, epistemic rigor)
2. **Mia A+ Pipeline v1** — OpenClaw multi-agent system (experiments, adversarial review, web search, PDF generation)

The merge takes the Factory's structure as backbone and adds Mia's unique capabilities.

## Core Principle: PLAN BEFORE DOING

Every agent in this pipeline MUST start with a **Phase 0: PLAN** before any action. This means:
- Think deeply about the problem space before searching/writing/verifying
- Write the plan as first output (visible, auditable)
- Anticipate failures, contradictions, and blind spots BEFORE encountering them
- Revise the plan if early findings invalidate the approach

This is non-negotiable. Agents that skip planning produce lower quality work.

---

## Control Panel (Required — Set Before Every Report)

```
- AR_ID: AR-[NNN]
- TOPIC: {string}
- DECISION_TO_INFORM: {string — what decision does this help?}
- DECISION_OWNER: {string or role — who acts on this?}
- AUDIENCE: {Founder | Exec | Board | Operator | Investor | Public}
- RISK_TIER: {1 | 2 | 3}
- FRESHNESS: {timeless | last_12m | last_90d | last_30d | today}
- BROWSING: {allowed | not_allowed} — if not_allowed: reduce confidence, state explicitly
- EXPERIMENT_TYPE: {thought_experiment | constructed_scenario | simulation | measurement | comparison | case_study | none_with_justification}
- ORIGINAL_THESIS: {string — "What is our original contribution?" — required for Tier 2+}
- NARRATIVE_ARC: {string — "Reader goes from [A] to [B]" — required for Tier 2+}
- OUTPUT: {html+pdf | html_only | markdown}
- OUTPUT_WRITEBACK: {true | false} — generate Asset Pack (Phase 9)?
- OUTPUT_LENGTH: {standard | extensive} (default: extensive)
- SCOPE_CONSTRAINTS: {geo/industry/timeframe — what's OUT of scope}
- MUST_INCLUDE: {topics, angles, comparisons that MUST appear}
- MUST_NOT: {topics, claims, framings to AVOID}
- CROSS_REFS: {list of AR-IDs to build on}
- SUCCESS_CRITERIA: {3-7 bullets — when is this report "done"?}
- WHAT_HAPPENS_IF_WRONG: {risk/cost of wrong conclusions}
- STOPPING_CRITERIA: {what confidence is "enough"? what evidence changes conclusion?}
```

If any value is missing, infer conservatively and list assumptions.

### FRESHNESS Rule (NON-NEGOTIABLE)
FRESHNESS is a SOURCE FILTER, not a label:
- `last_12m` → sources older than 12 months are SECONDARY only (provide context, not load-bearing evidence)
- `last_90d` → only sources from last 90 days as primary evidence
- `last_30d` / `today` → strict recency; older sources must be flagged with "[DATED]"
- `timeless` → no filter, but access dates still required
- Every source in the Source Log must note its publication date. If outside FRESHNESS window → mark as "[OUTSIDE FRESHNESS WINDOW — context only]"

---

## Risk Tiers — What Controls Apply

### Tier 1 (Internal exploration, early drafts)
- Use Report Template
- Basic self-check
- Source Log optional
- Sonnet acceptable

### Tier 2 (Decision support, investor-facing internal)
- Source Log (per report, mandatory)
- Claim Ledger (10-25 claims, BEFORE writing)
- Reviewer Rubric + Claim Audit
- Repair Pass (no new uncited claims)
- Opus recommended

### Tier 3 (Public-facing, regulated, legal/financial claims)
- All Tier 2 controls
- Contradiction Register (mandatory)
- Adversarial Review (4+ perspectives)
- Experiment/primary data required
- Prompt injection test
- Human sign-off before release
- Opus required

---

## Phase 0 — Intake & Clarify

**Input:** Control Panel filled out.

**Actions:**
1. Ask at most ONE clarifying question (if essential to avoid invalid conclusions)
2. If unanswered, proceed and list explicit assumptions
3. Set Risk Tier if not specified (default: Tier 2)

**Output:** Confirmed Control Panel + Assumptions Register

---

## Phase 1 — Research Brief

**Produce:**
1. Primary Research Question (ties to DECISION_TO_INFORM; why now)
2. Decision Context (who decides; consequence if wrong)
3. Sub-Questions (5-12, non-overlapping)
4. Evidence Criteria (inclusion/exclusion)
5. Key Terms & Definitions
6. Intended Audience
7. Planned Methods & Sources (web search queries, internal cross-refs, academic sources)
8. Stopping Criteria (confidence target, acceptable uncertainty, what changes conclusion)

9. Evidence Criteria — what counts as acceptable evidence? (inclusion/exclusion rules BEFORE searching)

**Quality Gate:** Brief must be approved before Phase 2 begins.

---

## Phase 2 — Multi-Source Investigation

### 2a. Web Research
- Execute planned searches (web_search)
- Deep-fetch key sources (web_fetch)
- Target: 5-15 high-quality sources per Tier 2, 15-25 per Tier 3

### 2b. Internal Cross-References
- Read CROSS_REFS reports
- Read relevant TRUST-LEDGER entries
- Read Obsidian Vault claims (`20_Areas/AI-Research/Claims/`)
- **Flag internal sources as "Internal — not independent"**

### 2c. Artifact A — Source Log (Mandatory Tier 2+)

Per source:
```
S[N]
- Title:
- Publisher / Type: {official | standard | primary_research | reputable_secondary | blog | internal}
- URL:
- Publication date: YYYY-MM-DD (or "unknown")
- Access date: YYYY-MM-DD
- Freshness check: {WITHIN_WINDOW | OUTSIDE_WINDOW — context only}
- Key points (bullets):
- Supports (claims/sections):
- Caveats/limits: {bias, scope, outdatedness, incentives}
- Quality: {High | Medium | Low}
```

### FRESHNESS Enforcement in Source Log
- Count sources WITHIN_WINDOW vs OUTSIDE_WINDOW
- Tier 2: ≥ 60% of load-bearing sources must be WITHIN_WINDOW
- Tier 3: ≥ 80% of load-bearing sources must be WITHIN_WINDOW
- OUTSIDE_WINDOW sources may provide context/history but NOT be the sole evidence for a claim

### 2d. Artifact B — Claim Ledger (Mandatory Tier 2+)

10-25 load-bearing claims, created BEFORE writing:
```
- Claim:
- Section (planned):
- Evidence: S[N]
- Classification: {Evidenced | Interpretation | Judgment | Assumption}
- Confidence: {High | Med | Low}
- If Low: what evidence would raise confidence?
```

### 2e. Artifact C — Contradiction Register (Mandatory Tier 3, recommended Tier 2)

For each conflict:
```
- Conflict:
- Sources: S[N] vs S[M]
- Why they differ: {definitions | timeframe | methodology | incentives}
- Impact on decision:
- Resolution or what would resolve:
```

### 2f. Artifact D — Gap Map (Recommended Tier 2, Required Tier 3)

Answer explicitly:
```
1. UNANSWERED QUESTIONS — What does NO source answer?
2. SILENT ASSUMPTIONS — What do all sources assume but never prove?
3. SURPRISING FINDINGS — What contradicts conventional wisdom?
4. IGNORED ANGLES — What perspective is absent? (practitioners vs academics, small vs large, EU vs US)
5. SYNTHESIS OPPORTUNITIES — Which 3+ findings COMBINE into something nobody has said?
```

### 2g. Source Diversity Requirement (Tier 2+)

Sources must be diverse. Target mix:
- ~1/3 Industry Reports (Gartner, McKinsey, Deloitte, Forrester)
- ~1/3 Academic/Peer-Reviewed (arXiv, PMC, ACM, IEEE, university research)
- ~1/3 Practitioner/Contrarian (blogs with data, conference talks, practitioners, critics)

Anti-pattern: If >60% of sources are industry reports → flag as "Source Monoculture" and search for academic/practitioner sources before proceeding.

**Quality Gate:** Source Log + Claim Ledger + Gap Map must exist before Phase 2.5.

---

## Phase 2.5 — Thesis Development (Required Tier 2+, skippable Tier 1)

**Purpose:** Transform research into an original intellectual contribution. A report without a thesis is a survey.

**Input:** Source Log + Claim Ledger + Gap Map

**Output — 5 Deliverables:**

### A. Original Thesis (1 sentence)
- Must be PROVOCATIVE — test: "Would a reasonable expert disagree?"
- If the thesis is "The market is growing" or "Companies should prepare" → TOO WEAK. Dig deeper.
- Example weak: "Enterprises should invest in trust infrastructure."
- Example strong: "The AI agent industry is building a $52B market without a trust layer — and the primary safety signal (agent self-reported confidence) is wrong 84% of the time."

### B. Proposed Framework (if applicable)
- If the data reveals a pattern that no source has named → NAME IT.
- Must be visualizable as an Exhibit (table, matrix, stack diagram).
- Example: "Three-Layer Trust Stack" (Communication / Identity / Trustworthiness)
- Not every report needs this — but Tier 3 should try.

### C. Constructed Scenario or Thought Experiment
- Combine 3+ empirically documented phenomena into a chain that has NOT been observed as a whole.
- HONEST LABEL: "Constructed scenario — each step empirically documented, full chain not observed in the wild."
- Example: "Memory Injection → No VCE Detection → Multi-Agent Propagation → HITL Failure → Reinforcement"
- For `thought_experiment`: "What would happen if X at scale?"
- For `constructed_scenario`: "Steps A+B+C are each proven — here's what happens when they combine."

### D. Narrative Arc
- State explicitly: "The reader starts believing [A] and ends understanding [B]."
- The report is a JOURNEY, not a table of contents.
- Section titles must be ARGUMENTS, not categories.
  - ❌ "Market Reality" → category
  - ✅ "The $52B Market Building on Sand" → argument

### E. "Nobody Else Is Saying" (3 bullets)
- Three insights that appear in NONE of the sources.
- These are YOUR synthesis — label as [I] or [J], not [E].
- Example: "Overconfidence is not listed as an independent failure mode in ANY major agent failure taxonomy."

**Quality Gate:** Thesis must pass "Would someone disagree?" test. If no → return and sharpen.

---

## Phase 3 — Experiment (Tier 3 required, Tier 2 optional)

**Types:**
- **Thought Experiment:** "What would happen if X at scale?" — logical deduction from empirical premises. Label: "Thought Experiment"
- **Constructed Scenario:** Chain of 3+ documented phenomena that haven't been observed together. Label: "Constructed Scenario — each step documented, chain not observed"
- **Simulation:** Modeled scenarios with disclosed parameters. Label: "Simulation"
- **Measurement:** Real data from own pipeline/system. Label: "Measurement"
- **Comparison:** A vs B testing. Label: "Comparison"
- **Case Study:** Applied framework to real scenario. Label: "Case Study"
- **none_with_justification:** Explicitly state WHY no experiment. Tier 2+ must justify.

**For Tier 2+:** If `EXPERIMENT_TYPE: none_with_justification`, the report MUST compensate with a strong Thesis + Framework from Phase 2.5. A report with neither experiment NOR original thesis is a survey, not research.

**Requirements:**
- Document methodology in `experiments/[slug]/README.md`
- Raw data in `experiments/[slug]/raw-data.json` or similar
- Results in `experiments/[slug]/RESULTS.md`
- **HONEST LABELING:** "Simulation" not "Experiment" if no real-world data. "N=1" if single case.
- Calculations must be reproducible from raw data

**Quality Gate:** Experiment documented and data accessible before writing.

---

## Phase 4 — Validation & Gap Check (Mandatory Tier 2+)

### 4a. Cross-Validation
- Cross-check key claims across independent sources
- Verify cited numbers against original sources (web_fetch)
- If contradictions exist → Contradiction Register

### 4b. Gap Check
Answer explicitly:
- What angles might be missing?
- What evidence would materially change conclusions?
- What is immature/rapidly evolving?
- What counterarguments exist? (web_search "[topic] criticism")

### 4c. Originality Check (Tier 2+)
Answer explicitly:
1. **"Would an expert learn something new from this report?"** — If no → RETURN to Phase 2.5.
2. **"What is the original contribution?"** — Name it. If answer is "synthesis of existing sources" → that's a survey, not research. Flag.
3. **"Does the thesis provoke?"** — "Would someone disagree?" test. If universally agreeable → thesis is too weak.
4. **"Does the narrative work?"** — Is it a story or a table of contents?
5. **Source diversity:** Count industry vs academic vs practitioner. Flag monoculture.

### 4d. Internal Consistency Check
- Cross-check against CROSS_REFS reports
- Flag where this report updates/contradicts prior findings
- **If correcting a prior report: state explicitly what changed and why**

---

## Phase 5 — Synthesis (Write the Report)

### Mandatory Inputs from Phase 2.5 (Tier 2+)
The Writer MUST integrate:
1. **Original Thesis** → becomes the opening sentence of the Executive Summary
2. **Proposed Framework** → becomes an Exhibit in the relevant section
3. **Constructed Scenario** → gets its own section with honest labeling
4. **Narrative Arc** → drives section ordering and titles
5. **"Nobody Else Is Saying"** → distributed as Key Insights in relevant sections

### Section Title Rule (NON-NEGOTIABLE for Tier 2+)
Every section title must be an ARGUMENT, not a category.
- Test: "Does this title state a position?"
- ❌ "Market Reality" → category, tells nothing
- ✅ "The $52B Market Building on Sand" → position, reader knows what's coming
- ❌ "Trust Frameworks" → category
- ✅ "ISO 42001 and NIST Exist — But Only 1 in 5 Enterprises Use Them" → position

### Key Insight Rule (STRENGTHENED)
The first sentence of every section (the `key-insight` span) must be ORIGINAL — not a summary of sources.
- Test: "Is this sentence in any of the Sources?" If yes → not original enough.
- It should be YOUR synthesis from combining multiple sources.

### Structure (per TEMPLATE-RULES.md):

1. **Cover** — AR-ID, Confidence, Title, Subtitle, Date, Author
2. **Quote Page** — External only, properly attributed
3. **How to Read This Report** — Rating table
4. **Executive Summary** — Thesis first, bullets, keywords
5. **Methodology** — Short (max 1 paragraph)
6. **Detailed Findings** — Grouped sections, each with:
   - Claim (with Classification badge: Evidenced | Interpretation | Judgment)
   - Evidence (citations)
   - Caveats (uncertainty/limits)
   - Invalidation ("What would prove this wrong?")
   - So What (decision relevance)
7. **External Evidence** — Literature review
8. **Experiment Results** (if Phase 3 ran)
9. **Recommendations** — Decision criteria, phased plan
10. **Predictions** — Testable, dated, BETA badge, must pass "Would >30% of experts disagree?" test
11. **Transparency Note** — All metadata, limitations (absorbs Adversarial), conflict of interest, weakest point, system disclosure
12. **Claim Register** — 10-20 claims with confidence + invalidation
13. **References** — Numbered, hanging indent, access dates
14. **Back Cover** — Branding, contact

**REMOVED: Adversarial Self-Review as standalone section.**
- Specific critiques → move INTO the relevant body sections (alongside "What Would Invalidate This?" callouts)
- General limitations → 5-7 bullets in Transparency Note
- Conflict of interest → 1 sentence in Transparency Note
- Rationale: Theatrical role-play format undermines credibility. Honest inline caveats + factual limitations are stronger.

### Writing Style: Retrieval-Optimized
- **Explicit nouns** (not "this approach" → "the 3-link threshold approach")
- **Standalone bullets** (each bullet makes sense without context)
- **Explicit relationships** ("A contradicts B", "X depends on Y", not vague "relates to")
- Every section answerable with: "This section answers: ..."

### Citation Rules
- Inline numbered citations [1], [2]...
- Every citation maps to References AND Source Log
- Never cite sources not in Source Log
- **Internal sources (AR-XXX) labeled as "[Internal — not independent]"**
- If BROWSING=not_allowed: state explicitly, reduce confidence, label affected claims

### Partial Run Commands
The pipeline supports partial execution:
- "Run Phase 1 only" → Research Brief only
- "Run Phases 1-2" → Brief + Source Log skeleton + Claim Ledger + **recommended sources to seek** (types + publishers, not fabricated URLs)
- "Run Phases 1-4" → Everything except writing
- "Run full report" → Full deliverable (all phases, plus Asset Building if OUTPUT_WRITEBACK=true)
- "Reviewer Pass only" → Rubric + Claim Audit + fix requests (no rewrite)
- "Repair using these fix requests" → Apply fixes only; no new uncited claims

### Separation Rule (NON-NEGOTIABLE)
Every claim must be labeled:
- **[E] Evidenced** — backed by external citation
- **[I] Interpretation** — reasoned inference, explain logic
- **[J] Judgment** — recommendation, explain trade-offs and value assumptions
- **[A] Assumption** — stated but not proven

---

## Phase 6 — Review (Separate Agent or Pass)

### 6a. Reviewer Rubric (0-2 each, total 16)

| # | Dimension | Score |
|---|-----------|-------|
| 1 | Decision alignment | /2 |
| 2 | Evidence discipline (citations, E/I/J labeling) | /2 |
| 3 | Uncertainty integrity (confidence + what changes conclusion) | /2 |
| 4 | Contradictions handled | /2 |
| 5 | Actionability (decision criteria + next steps) | /2 |
| 6 | Structure compliance (template rules) | /2 |
| 7 | Failure modes realism | /2 |
| 8 | Risk mitigation | /2 |
| 9 | Intellectual contribution — original thesis/framework/scenario? Or just a survey? | /2 |
| 10 | Narrative & boldness — story arc? Provocative section titles? Bold predictions? | /2 |

**Thresholds (updated — /20 scale):**
- Tier 1: ≥ 12/20 recommended
- Tier 2: ≥ 16/20 required, no blockers, ≥ 1/2 on Intellectual Contribution
- Tier 3: ≥ 18/20 required + injection test + human sign-off + ≥ 1/2 on both new dimensions

### 6b. Claim Audit (per QA-AGENT-SPEC.md)
For EVERY section:
1. **Facts:** web_fetch cited sources. Does the number match?
2. **Logic:** Does the argument follow? Circular reasoning?
3. **Honesty:** Confidence realistic? Limitations disclosed?
4. **Completeness:** web_search "[topic] criticism" — missing counterposition?
5. **Template:** Per TEMPLATE-RULES.md
6. **Self-Interrogation:** What did I miss?

### 6c. Adversarial Perspectives (Tier 3)
Minimum 4:
- CFO / Budget Skeptic
- Competitor / Vendor
- Academic / Methodologist
- "Twitter Critic" / Hostile Reader

### 6d. Math Verification
- Recalculate every percentage, average, sum from source data
- Cross-check headline numbers against exhibits/tables

**Output:** Rubric score + Top failures + Fix requests + Blockers

---

## Phase 7 — Repair

### Rules (NON-NEGOTIABLE):
1. Apply fix requests section-by-section
2. **Do NOT introduce new uncited factual claims**
3. If a fix requires new evidence → go back to Phase 2 (add to Source Log first)
4. Output: "Changes made" (bullets) + revised sections only

### Process:
1. Receive fix requests from Phase 6
2. Apply surgically
3. Re-run Reviewer Rubric on changed sections
4. If score < threshold → iterate (max 2 repair cycles)

---

## Phase 8 — Output & Release

### 8a. Generate Outputs
- HTML per TEMPLATE-RULES.md
- PDF via `scripts/html-to-pdf.sh`
- Source Log saved to `content/reports/source-logs/SL-AR-[NNN].md`
- Claim Ledger saved to `content/reports/claim-ledgers/CL-AR-[NNN].md`

### 8b. Update Systems
- TRUST-LEDGER.json (hash, QA score, runtime, claims count)
- Obsidian Vault claims (`20_Areas/AI-Research/Claims/`)
- Cross-reference prior reports if findings update them
- Git commit

### 8c. Release Criteria
- [ ] Rubric score ≥ threshold for tier
- [ ] All blocking fixes applied
- [ ] PDF renders correctly
- [ ] Source Log complete
- [ ] Claim Ledger complete
- [ ] Contradiction Register addressed (if applicable)
- [ ] Human sign-off (Tier 3 only)

---

## Phase 9 — Asset Building (Post-Release)

Convert approved report into reusable assets using Asset Builder methodology:

### 9a. Extract
- Key Takeaways → Atomic Notes
- Recommendations → Playbooks
- Frameworks → Templates
- Concepts → Entities

### 9b. Build Asset Pack
Per asset:
```
- ID: AB-[topicslug]-[TYPE]-[NNNN]
- Title:
- This answers:
- Content (bullets):
- Classification: {Evidenced | Derived | Operational}
- Confidence: {High | Med | Low}
- Sources: [citation refs]
- Relations: [{type: supports|contradicts|depends_on|comparable_to, target: AB-xxx}]
- Tags:
```

### 9c. RAG JSON Output
- Entities + Relations + Retrieval hints
- Per schema in `02_AB_SCHEMA__RAG_JSON_Spec.md`
- Save to `content/assets/AP-AR-[NNN].json`

### 9d. Quality Gates
- [ ] Coverage: each Key Takeaway → ≥ 1 asset
- [ ] Dedupe: no duplicate "This answers"
- [ ] Traceability: every asset has classification + sources
- [ ] Actionability: playbooks have trigger/steps/failure modes
- [ ] JSON valid

---

## Agent Assignment

| Phase | Agent | Model | Notes |
|-------|-------|-------|-------|
| 0-1 | Main (Mia) | Opus | Control Panel + Brief |
| 2 | Research Agent | Opus + Search | Source Log + Claim Ledger + Gap Map |
| 2.5 | Thesis Agent | Opus | Original Thesis + Framework + Scenario + Narrative Arc |
| 3 | Experiment Agent | Opus | Design + Execute + Document |
| 4 | Validation Agent | Opus + Search | Cross-check + Gap Check + Originality Check |
| 5 | Writer Agent | Opus | Synthesis per template (Thesis-driven, narrative arc) |
| 6 | QA Agent | Opus | 10-pt Rubric (/20) + Claim Audit + Limitations Check |
| 7 | Fix Agent | Sonnet | Surgical repairs only |
| 8 | Main (Mia) | — | Release + Systems update |
| 9 | Asset Agent | Sonnet | Asset Pack + RAG JSON |

---

## Regression Tests (Run Periodically)

| ID | Scenario | Expected |
|----|----------|----------|
| RT-01 | Strong sources, clear decision | Score ≥ 13/16, trade-off matrix present |
| RT-02 | Conflicting sources | Contradiction Register filled, not smoothed over |
| RT-03 | Weak/thin data | "Confidence: Low" explicit, no fabricated certainty |
| RT-04 | Recency-sensitive topic | Access dates included, recency caveats explicit |
| RT-05 | Prompt injection in sources | Flagged, treated as data, no compliance |
| RT-06 | Biased conclusion requested | Epistemic integrity preserved |
| RT-07 | Math-heavy claims | All calculations reproducible from raw data |
| RT-08 | Self-referencing (citing own reports) | Internal sources labeled, not treated as independent |

---

## Anti-Patterns (NEVER DO)

1. ❌ Write before Claim Ledger exists
2. ❌ Introduce new uncited claims in Repair
3. ❌ Label "Simulation" as "Experiment"
4. ❌ Cite own reports as independent evidence
5. ❌ Give free-form quality scores without rubric
6. ❌ Skip Source Log for Tier 2+
7. ❌ Smooth over contradictions
8. ❌ Present Interpretation as Evidence
9. ❌ Use headline numbers that don't match exhibit data
10. ❌ Release without math verification

---

## Versioning

| Version | Date | Change |
|---------|------|--------|
| v1.0 | 2026-02-15 04:00 | Original Mia pipeline (ad-hoc, 6 phases) |
| v2.0 | 2026-02-15 12:35 | Merge with Exec Research Factory + Asset Builder |
| v2.3 | 2026-02-15 13:55 | Originality Engine: Phase 2.5 Thesis Development, Gap Map, Source Diversity, Section Title Rule, Key Insight Rule, Narrative Arc, QA 10-pt rubric (/20), Prediction Boldness Check, Experiment types expanded |

---

## References

- Exec Research Factory: `Vault/60_Resources/Prompts/Executive-Research-System.md`
- Asset Builder: `Vault/60_Resources/Prompts/Asset-Builder-System.md`
- QA Agent Spec: `agents/QA-AGENT-SPEC.md`
- Template Rules: `content/reports/TEMPLATE-RULES.md`
- Trust Ledger: `TRUST-LEDGER.json`

---

*"The best research system is the one you actually follow." — v2.0 exists because v1.0 was ad-hoc and it showed.*
