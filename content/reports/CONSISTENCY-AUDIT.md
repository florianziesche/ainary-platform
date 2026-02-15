# Cross-Report Consistency Audit

**Date:** 2026-02-15
**Reports Audited:** 35 HTML files (excluding 3 templates), of which ~12 are duplicate/versioned pairs leaving ~23 unique report topics

---

## 📋 Duplicate/Versioned Report Pairs

These reports cover the same content in old vs new template format, or are v1→v2 updates. They should be clearly marked to avoid confusion:

| Old Version | New Version | Notes |
|---|---|---|
| `calibration-2026.html` | `calibration-gap-2026.html` | Same report (AR-009), new template |
| `eu-us-regulation-2026.html` | `eu-vs-us-regulation-2026.html` | Same report (AR-003), new template |
| `financial-services-2026.html` | `financial-services-trust-2026.html` | Same report (AR-005), new template |
| `security-playbook-2026.html` | `security-playbook-2026-v2.html` | Same report (AR-006), new template |
| `maturity-model-2026.html` | `trust-maturity-model-2026.html` | Same report (AR-004), new template |
| `state-of-agent-trust-2026.html` (v1) | `state-of-agent-trust-2026-v2.html` (v2) | Substantive update — v2 changes key claims (see contradictions) |
| `agent-memory-2026.html` | `agent-memory-market-map-2026.html` | Different reports (AR-014 vs AR-019), but overlapping topic |
| `agent-economics-2026.html` | `agent-economics-real-roi-2026.html` | Different reports (AR-016 vs AR-021), overlapping topic |
| `governance-2026.html` / `governance-theater-2026.html` / `governance-framework-vs-reality-2026.html` | Three distinct governance reports (AR-008, AR-022, AR-028) | Different angles, but numbers must align |
| `knowledge-compounding-2026.html` / `knowledge-compounding-flywheel-2026.html` / `knowledge-architecture-effect-2026.html` | AR-015, AR-025, AR-026 | Knowledge trilogy |

---

## 🔴 Direct Contradictions (same claim, different values)

| # | Claim | Report A | Value A | Report B | Value B | Resolution |
|---|---|---|---|---|---|---|
| 1 | **$52B market — AI agents or agent memory?** | `state-of-agent-trust-2026` (AR-001) | "$52 billion AI agent market by 2030 at 45.8% CAGR" | `agent-memory-market-map-2026` (AR-019) | "Agent memory market projected at $52.62B by 2030 (46.3% CAGR)" | 🚨 **CRITICAL.** AR-019 appears to cite the same MarketsandMarkets figure for the *overall* AI agent market but frames it as the "agent memory market." A memory sub-segment cannot equal the total market. Either AR-019 mislabels the market scope, or the source is different. Fix AR-019 to clarify this is the broader AI agent market, or find a memory-specific figure. |
| 2 | **CAGR for $52B market** | `state-of-agent-trust-2026` (AR-001) | 45.8% CAGR | `agent-memory-market-map-2026` (AR-019) | 46.3% CAGR | Minor but sloppy. Same market, different CAGR. One source says 45.8%, the other 46.3%. Pick one and standardize. |
| 3 | **Multi-agent hijacking success rate** | `security-playbook-2026-v2` (AR-006) | "45–64% of the time across AutoGen, CrewAI, and MetaGPT" | `orchestration-2026` (AR-007) | "Inter-agent communication can be hijacked with 58–90% success rates" | Different ranges for overlapping phenomena. AR-006 cites a specific study; AR-007's 58-90% range is broader and possibly aggregates multiple attack types. **Reconcile:** specify which attack vector each refers to. The ranges don't overlap cleanly (45-64% vs 58-90%). |
| 4 | **Number of production reports (own data)** | `agent-economics-2026` (AR-016) | "14 production-grade research outputs" / "$38.50 total cost" | `agent-economics-real-roi-2026` (AR-021) | "18 research reports at $2.75 average" | AR-016 was written when 14 reports existed; AR-021 when 18 existed. Not a true contradiction but **confusing to readers.** The $38.50 total (14×$2.75) vs 18×$2.75=$49.50 are both internally consistent. Note: `quality-compound-study` (AR-029) references 25 reports. **Fix:** Add temporal context ("as of report date") or update older reports. |
| 5 | **181× ROI vs honest cost** | `agent-economics-2026` (AR-016) | "181× ROI — $38.50 total cost, ~$7,000 market value" | `real-cost-ai-agents-2026` (AR-027) | "honest TCO is $70-80/report… still 10-18× cheaper than human-only" | 🚨 **CRITICAL.** AR-016 claims 181× ROI based on API cost only. AR-027 explicitly debunks this, showing the honest cost is $70-80/report (25-29× higher than API cost). AR-027 is the more honest analysis. **AR-016's 181× claim is misleading and should be flagged or retracted.** |
| 6 | **Enterprise AI agent adoption rate** | `state-of-agent-trust-v2` (AR-001-v2) | "8–14% in production" | `orchestration-2026` (AR-007) | "51% of companies have AI agents in production" | Different sources with different definitions. AR-001-v2 uses TechRepublic (8.6%) and Deloitte (11-14%). AR-007 uses LangChain survey (n=1,300). The LangChain survey likely has selection bias (surveying their own users). **Both should note the range explicitly.** Additionally, `governance-theater` (AR-022) claims "98% of enterprises deploy agentic AI" — an even wider gap. |
| 7 | **NIST AI RMF catch rate (INTERNAL to AR-028)** | `governance-framework-vs-reality` exec summary | "NIST AI RMF caught 45%" | Same report, section title | "NIST AI RMF: 50% of Failure Modes Caught" | 🔴 **Internal contradiction within AR-028.** The exec summary says 45%, the section heading says 50%. Combined is stated as 55% in both places. Fix the inconsistent number. |
| 8 | **Hidden cost multiplier** | `agent-economics-2026` (AR-016) | "monitoring, error correction, and human oversight can exceed direct API costs by 3-5×" | `agent-economics-real-roi` (AR-021) | "Actual deployment costs are 3-7× initial estimates" | Different framing (3-5× of API costs vs 3-7× of initial estimates) but could confuse readers. AR-021's range is wider. These measure different bases, but should be reconciled. |
| 9 | **Governance framework operationalization** | `governance-theater` (AR-022) | "only 18% have fully implemented" / "Fewer than 25% have operationalized" (Deloitte) | `governance-framework-vs-reality` (AR-028) | "75% have NOT operationalized" / "only 12% describe governance as mature" (Cisco) | Different sources (Deloitte vs Cisco) with directionally consistent but numerically different figures: 18% implemented vs 12% mature vs 25% operationalized. Not a hard contradiction but messy. **Pick one anchor stat and cite others as supporting range.** |
| 10 | **State of Agent Trust v1 vs v2 — subtitle claim** | `state-of-agent-trust-2026` (v1) | "95% of projects fail" (subtitle) | `state-of-agent-trust-v2` | "Over 40% of projects will be canceled" (subtitle) | v1 used "95% fail" (MIT via secondary, low confidence) as a headline claim. v2 dropped this and uses the more defensible Gartner "40% canceled." **v1 should be deprecated or removed from distribution.** |

---

## 🟡 Tensions (different emphasis, potentially reconcilable)

| # | Tension | Reports | Notes |
|---|---|---|---|
| 1 | **HITL: essential vs. failing** | `hitl-illusion-2026` (AR-011) argues HITL fails at scale. `governance-2026` (AR-008) and EU AI Act reports recommend human oversight. `governance-theater` (AR-022) says mandated HITL doesn't work. | Actually internally consistent — AR-011 says HITL works in *specific* conditions (low frequency, high impact), not universally. But the tension could confuse readers who skim. |
| 2 | **Trust infrastructure: cost or moat?** | `trust-tax-2026` (AR-002) frames trust as a hidden cost. `trust-moat-2026` (AR-012) frames it as competitive advantage. | Complementary, not contradictory — but readers encountering one without the other might get opposite impressions. |
| 3 | **Agent quality: compounds or doesn't?** | `knowledge-compounding-2026` (AR-015) argues knowledge compounds. `quality-compound-study` (AR-029) finds "Quality does not compound. Efficiency does." | AR-015 proposes the framework; AR-029 tests it and finds the answer is nuanced. Consistent in spirit but the headlines are in tension. |
| 4 | **Build vs buy vs wait** | `state-of-agent-trust-v2` recommends "buy + extend now." `build-buy-compose` (AR-017) recommends the compose pattern. | Different decision levels — trust infrastructure vs. agent stack. But "buy" vs "compose" framing could confuse. |
| 5 | **Governance: theater vs. necessary** | AR-022 ("governance is theater") vs AR-008 ("boards need governance now") vs AR-028 ("frameworks catch 40-55%") | AR-022 is contrarian; AR-008 is prescriptive; AR-028 provides empirical middle ground. The trilogy works together but AR-022's title is provocative enough to seem anti-governance when it's actually pro-*operational* governance. |
| 6 | **89% never reach production vs 40% canceled** | AR-021 cites "89% of enterprise AI agents never reach production." AR-001/AR-004/AR-007 cite Gartner's "40% canceled by 2027." | Different claims from different sources (single vendor vs Gartner). 89% is flagged as low confidence. They're measuring different things but could seem contradictory. |

---

## ✅ Consistent Threads (same claim, same value across reports)

| # | Claim | Reports Citing It | Confidence |
|---|---|---|---|
| 1 | **84% of LLM responses show overconfidence** (9 models, 351 scenarios) | AR-001, AR-005, AR-009, AR-011, AR-018 (5+ reports) | High |
| 2 | **67% of security alerts ignored** (Vectra, n=2,000) | AR-009, AR-011, AR-018, AR-022 (4 reports) | High |
| 3 | **EU AI Act enforcement August 2, 2026** | AR-001, AR-002, AR-003, AR-004, AR-005, AR-008, AR-022, AR-028 (8+ reports) | High |
| 4 | **EU AI Act penalties up to €35M or 7% revenue** | AR-002, AR-003, AR-005, AR-008, AR-022 (5+ reports) | High |
| 5 | **$0.005 per calibration check** | AR-001, AR-005, AR-009 (3 reports) | High |
| 6 | **Memory injection attacks >95% success rate** | AR-006, AR-014, AR-018 (3 reports) | High |
| 7 | **No production memory framework has provenance tracking** | AR-006, AR-014, AR-018, AR-019 (4 reports) | High |
| 8 | **Tool calling fails 3–15% in production** | AR-001, AR-006, AR-010, AR-018 (4 reports) | Medium |
| 9 | **40% of agentic AI projects canceled by 2027** (Gartner) | AR-001, AR-004, AR-007, AR-012 (4 reports) | High |
| 10 | **Klarna saved $60M but returned to human oversight** | AR-005, AR-012, AR-027 (3 reports) | Medium (CEO claim, not audited) |

---

## Recommendations

### 🚨 Must Fix Before External Distribution

1. **AR-019 ($52B memory market)** — The $52.62B figure is almost certainly the *total AI agent market*, not the memory sub-segment. This is the single most embarrassing error if a reader notices. Add clarifying language or find a memory-specific figure.

2. **AR-016 (181× ROI)** — This claim is directly contradicted by AR-027's honest accounting ($70-80/report). Either add a prominent caveat to AR-016 ("API cost only — see AR-027 for full TCO") or retract the 181× figure.

3. **AR-028 (NIST 45% vs 50%)** — Internal contradiction. Pick one number.

4. **AR-001 v1 ("95% fail")** — This headline claim was dropped in v2 for good reason. Remove v1 from distribution or mark it clearly superseded.

### ⚠️ Should Fix

5. **Standardize CAGR** — 45.8% vs 46.3%. Pick one.

6. **Multi-agent hijacking ranges** — AR-006 (45-64%) and AR-007 (58-90%) should specify which attack type each refers to.

7. **Adoption rate chaos** — 8-14% vs 51% vs 98% across reports. Add a note to each explaining the definition used. Consider a canonical "adoption landscape" sidebar for all reports.

8. **Deprecate old-template duplicates** — Either remove old versions or add "SUPERSEDED BY [new version]" headers. Having both live is confusing.

### 💡 Observations

- The **core trust thesis is rock-solid** across all reports: 84% overconfidence, no provenance tracking, 67% alert fatigue, EU AI Act August 2026. These numbers are well-sourced and consistent.
- **Cost claims are the weakest chain** — the $2.75 API cost is accurate but the ROI framing varies wildly (181× vs 10-18×) depending on what you include. AR-027 is the honest version; earlier reports should reference it.
- The **governance trilogy** (AR-008, AR-022, AR-028) works well together but needs clearer cross-referencing so readers understand the progression: governance matters → most governance is theater → here's empirical data on what works.
- **12 duplicate/versioned reports** create significant confusion. A canonical report index marking which version is current would help enormously.
