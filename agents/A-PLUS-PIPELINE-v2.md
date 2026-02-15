# A+ Research Pipeline v2.0

*Merge: Exec Research Factory (ChatGPT) + Mia A+ Pipeline (OpenClaw)*
*Created: 2026-02-15 | Owner: Florian Ziesche*

---

## Origin

This pipeline merges two systems:
1. **Exec Research Factory** — Florian's ChatGPT system (structured, artifact-driven, epistemic rigor)
2. **Mia A+ Pipeline v1** — OpenClaw multi-agent system (experiments, adversarial review, web search, PDF generation)

The merge takes the Factory's structure as backbone and adds Mia's unique capabilities.

---

## Control Panel (Required — Set Before Every Report)

```
- AR_ID: AR-[NNN]
- TOPIC: {string}
- DECISION_TO_INFORM: {string — what decision does this help?}
- AUDIENCE: {Founder | Exec | Board | Operator | Investor | Public}
- RISK_TIER: {1 | 2 | 3}
- FRESHNESS: {timeless | last_12m | last_90d | last_30d | today}
- EXPERIMENT_TYPE: {none | simulation | measurement | comparison | case_study}
- OUTPUT: {html+pdf | html_only | markdown}
- CROSS_REFS: {list of AR-IDs to build on}
- STOPPING_CRITERIA: {what confidence is "enough"? what evidence changes conclusion?}
```

If any value is missing, infer conservatively and list assumptions.

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
- Access date:
- Key points (bullets):
- Supports (claims/sections):
- Caveats/limits:
- Quality: {High | Medium | Low}
```

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
- Why they differ:
- Impact on decision:
- Resolution or what would resolve:
```

**Quality Gate:** Source Log + Claim Ledger must exist before Phase 3.

---

## Phase 3 — Experiment (Tier 3 required, Tier 2 optional)

**Types:**
- **Simulation:** Modeled scenarios with disclosed parameters (label: "Simulation")
- **Measurement:** Real data from own pipeline/system (label: "Measurement")
- **Comparison:** A vs B testing (label: "Comparison")
- **Case Study:** Applied framework to real scenario (label: "Case Study")

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

### 4c. Internal Consistency Check
- Cross-check against CROSS_REFS reports
- Flag where this report updates/contradicts prior findings
- **If correcting a prior report: state explicitly what changed and why**

---

## Phase 5 — Synthesis (Write the Report)

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
9. **Adversarial Self-Review** (Tier 3)
10. **Recommendations** — Decision criteria, phased plan
11. **Predictions** — Testable, dated, BETA badge
12. **Transparency Note** — All metadata, limitations, weakest point
13. **Claim Register** — 10-20 claims with confidence + invalidation
14. **References** — Numbered, hanging indent, access dates
15. **Back Cover** — Branding, contact

### Citation Rules
- Inline numbered citations [1], [2]...
- Every citation maps to References
- Never cite sources not used
- **Internal sources (AR-XXX) labeled as "Internal — not independent"**

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

**Thresholds:**
- Tier 1: ≥ 10/16 recommended
- Tier 2: ≥ 13/16 required, no blockers
- Tier 3: ≥ 15/16 required + injection test + human sign-off

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
| 2 | Research Agent | Opus + Search | Source Log + Claim Ledger |
| 3 | Experiment Agent | Opus | Design + Execute + Document |
| 4 | Validation Agent | Opus + Search | Cross-check + Gap Check |
| 5 | Writer Agent | Opus | Synthesis per template |
| 6 | QA Agent | Opus | Rubric + Claim Audit + Adversarial |
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

---

## References

- Exec Research Factory: `Vault/60_Resources/Prompts/Executive-Research-System.md`
- Asset Builder: `Vault/60_Resources/Prompts/Asset-Builder-System.md`
- QA Agent Spec: `agents/QA-AGENT-SPEC.md`
- Template Rules: `content/reports/TEMPLATE-RULES.md`
- Trust Ledger: `TRUST-LEDGER.json`

---

*"The best research system is the one you actually follow." — v2.0 exists because v1.0 was ad-hoc and it showed.*
