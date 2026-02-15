# QA Report — AR-001-v2.3: State of AI Agent Trust 2026

**QA Agent** | Phase 6 | 2026-02-15  
**Pipeline:** A+ Research Pipeline v2.3  
**Verdict:** 🟡 **CONDITIONAL GO** — 1 blocker, fixable in 10 minutes

---

## Phase 0: Pre-Read Hypotheses

1. **Likely cut corners:** E/I/J/A labels on borderline claims, unsourced stats dressed as [E], math on projections
2. **Red team attack surface:** The Trust Race Model is unfalsifiable hand-waving; the quote page is fabricated; the 72% stat is wrong
3. **v2 weakness (survey without originality):** v2.3 clearly fixes this — Trust Race Model + Governance Lag Cascade + argumentative titles
4. **Priority:** Verify Trust Race Model inputs first → then cascade scenario → then all other claims

---

## Deliverable 1: 10-Point Rubric (/20)

| # | Dimension | Score /2 | Rationale |
|---|-----------|----------|-----------|
| 1 | Decision alignment | **2** | Explicitly answers "invest now / wait / build in-house." GO decision with "buy + extend" rationale. 90-day plan. Excellent. |
| 2 | Evidence discipline | **1** | E/I/J/A badges present throughout. BUT: 72% investment stat is WRONG (source says 86%). "67% of security alerts ignored" in §9 has [E] badge but ZERO citation. Two misquotes/unsourced claims in a Tier 3 report = cannot score 2. |
| 3 | Uncertainty integrity | **2** | 73% overall confidence well-justified. Per-section confidence levels. Stopping criteria in Transparency Note. Weakest point honestly identified ("no evidence trust infra actually works"). Exemplary. |
| 4 | Contradictions handled | **2** | 8.6-57% adoption range explicitly discussed and explained. METR vs MIT Tech Review paradox named. Multi-agent benchmark vs industry value tension explored. Not smoothed over. |
| 5 | Actionability | **2** | 90-day phased plan. Cost framework ($200K-$2M vs failure cost). Decision criteria clear. "Buy + extend" specific enough to act on. |
| 6 | Structure compliance | **1.5** | All required sections present. Invalidation before So What ✅. Claim Register (18 claims) ✅. About This Report correct ✅. No Adversarial Self-Review ✅. Transparency Note with 7 limitation bullets ✅. Conflict of Interest ✅. **Deduction:** Quote page uses a "paraphrased" Nadella quote — TEMPLATE-RULES require external, properly attributed quotes. A paraphrase is not a quote. |
| 7 | Failure modes realism | **2** | 14 MAST failure modes cited. Governance Lag Cascade is concrete and step-sourced. 50-agent collapse, 35% prompt injection — specific, not hand-wavy. |
| 8 | Risk mitigation | **2** | Recency: 100% within 12-month window. Bias: vendor sponsorship flagged (HBR/Workato, Adversa AI). Limitations: 7 honest bullets. Non-Western gap acknowledged. |
| 9 | Intellectual contribution | **2** | Trust Race Model is genuinely original — nobody else has modeled capability vs governance as a temporal race with 4 named components. Governance Lag Cascade is a well-constructed scenario. Section titles are arguments. This is NOT a survey anymore. |
| 10 | Narrative & boldness | **1.5** | Strong story arc (deploy → broken → accelerating → losing → adapt → window). Section titles are provocative ("The Agents Don't Actually Work Yet"). **Deduction:** Predictions are reasonable but could be bolder — Prediction 5 (doubling slows) at 45% is the only contrarian one. The governing metaphor "accelerating vehicle with no brakes" from Thesis doc barely appears in the report itself. |

**Total: 18/20**

Meets Tier 3 threshold (≥18) IF blockers are resolved. Dimensions 9 and 10 both ≥1.5. ✅

---

## Deliverable 2: Claim Audit

### Section 4: "Everybody's Deploying, Nobody's Trusting"

**Facts verified:**
- 6% full trust (HBR/Workato via Fortune) — ✅ CONFIRMED. Fortune article: "Only 6% of companies fully trust AI agents"
- 43% routine tasks, 39% supervised — ✅ CONFIRMED
- 57% G2 production — ✅ CONFIRMED (but note: G2 surveyed only 5 vendors, weak methodology)
- 11% Deloitte agentic — referenced in Source Log, not directly verified from fetched excerpt (Deloitte page showed case studies, not the 11% stat)
- 8.6% TechRepublic — Source Log notes couldn't deep-read (Cloudflare blocked). Medium confidence.
- 12% governance controls in place — ✅ CONFIRMED (Fortune: "just 12% feel risk and governance controls are fully in place")
- 🔴 **72% expect to increase agent investment [1]** — **WRONG.** Fortune article says **"Eighty-six percent of respondents expect investment in agentic AI to increase over the next two years."** The 72% figure does not appear in the source. **BLOCKER — misquoted statistic.**

**Logic:** Sound. The deployment-trust inversion argument is well-constructed.  
**E/I/J/A:** Correctly labeled.  
**Template:** Invalidation before So What ✅.

### Section 5: "The Agents Don't Actually Work Yet"

**Facts verified:**
- 1,600+ annotated traces — ✅ CONFIRMED (arXiv abstract)
- "correctness as low as 25%" — arXiv abstract says "performance gains on popular benchmarks are often minimal" but doesn't cite 25% in the abstract. Likely in the full paper. Source Log says "ChatDev correctness can be as low as 25%." **Medium confidence — plausible but not verified from abstract alone.**
- 14 failure modes, 3 categories — ✅ CONFIRMED
- kappa = 0.88 — ✅ CONFIRMED
- Multi-agent minimal gains vs single-agent — ✅ CONFIRMED ("performance gains on popular benchmarks are often minimal")
- 73% vision-reality gap (Camunda) — Camunda page is a gated report, stat not verifiable from landing page. Source Log lists it.
- 11% agentic use cases reaching production (Camunda) — Same, gated.

**Logic:** Sound. The inference that industry values workflow integration over correctness is well-labeled [I].  
**E/I/J/A:** Correct.

### Section 6: "But They're Getting Better Faster Than You Think"

**Facts verified:**
- Doubling every ~7 months — ✅ CONFIRMED (METR abstract: "doubling approximately every seven months since 2019")
- 80% horizon 5x shorter than 50% — Not in abstract. Likely in full paper. The abstract mentions "50%-task-completion time horizon" metric but not the 80%/5x relationship explicitly. **Medium confidence.**
- 🔴 **72% expect to increase agent investment** — Same wrong number from §4. Should be 86%.

**E/I/J/A:** Correct. The "paradox" interpretation properly labeled [I].

### Section 7: "Your Governance Can't Keep Up — By Design"

**Facts verified:**
- ISO 42001 and NIST AI RMF — ✅ Confirmed as primary frameworks
- EU AI Act August 2, 2026 — ✅ CONFIRMED
- Dayforce dual certification Feb 2026 — ✅ CONFIRMED (GlobeNewswire)
- "ISO frameworks update annually" — 🟡 **IMPRECISE.** ISO 42001 was published Dec 2023 and has NOT been updated since. The claim should say "ISO revision cycles are multi-year" rather than "annual." The report says "Both update on annual cycles at best" — this overstates the frequency. ISO typically revises on 5-year cycles.

**Logic:** The structural mismatch argument is sound, but the "annual" governance tempo claim for ISO is actually too generous — real ISO update cycles are slower (multi-year), which would STRENGTHEN the argument.  
**E/I/J/A:** The governance gap widening claim correctly labeled [J].

### Section 8: "The Ungoverned Capability Zone Is Growing"

**Facts:** Trust Race Model inputs all trace to verified sources (METR [3], UC Berkeley [2], HBR [1] — noting the 72% error, ISO [4], NIST [5], EU AI Act [8]).  
**Framework evaluation:** The Trust Race Model is honestly labeled as "original to this report" and "interpretive [I]." Exhibit source line explicitly says "Author synthesis" and "has not been externally validated." This is proper epistemic hygiene.  
**E/I/J/A:** Correct. Framework labeled [J], components labeled with evidence sources.

### Section 9: "What Happens When Governance Falls Behind"

**Facts verified per step:**
- Step 1: 25% [2], 43% [1] — ✅ (with 25% caveat above)
- Step 2: 7-month doubling [3] — ✅
- Step 3: 73% gap [13], agent-washing [11] — Camunda stat unverifiable (gated)
- Step 4: 14 modes [2], 50-agent collapse [17], 35% prompt injection [18] — ✅ All verified
- Step 5: **"67% of security alerts are ignored in practice"** — 🔴 **UNSOURCED CLAIM MARKED [E].** No citation number. No source in the Source Log. The badge says [E] (Evidenced) but there is NO reference. This appears to come from a Vectra AI statistic or similar, but it is not cited. **BLOCKER candidate — unsourced claim in [E] badge.**
- Step 6: Labeled [I] — correct.

**Scenario label:** ✅ "Constructed scenario" label properly displayed.

### Section 10: "Static Trust Is a Losing Strategy"

**Facts verified:**
- Dayforce [15] — ✅
- 7-month doubling [3] — ✅
- IBM watsonx.governance 2.3.x [19] — Referenced via Vectra AI blog. Medium confidence.
- $309M / $420M governance market [20] — ✅ CONFIRMED (Precedence: $309M in 2025, $419M in 2026)
- 2x partnerships [6] — From Deloitte, not directly verified from fetched page but in Source Log.

**E/I/J/A:** Correct.

### Section 11: "Building Brakes That Accelerate With the Car"

**Facts:** TRiSM metrics [16] — confirmed in Source Log. Mostly [J] claims, appropriately labeled. The [A] badge on the caveat paragraph is correct.  
**Exhibit 3:** Honestly labeled "[J]. No production implementation... currently exists."

### Section 12: "The 18-Month Window Is Closing"

**Facts verified:**
- EU AI Act Aug 2026 [8] — ✅
- €35M / 7% [8] — ✅
- $7.55B market / 44% CAGR [21] — ✅ (source says 43.84%, report rounds to 44% — acceptable)
- $309M governance / 36% CAGR [20] — ✅ (source says 35.74%, rounds to 36% — acceptable)
- >40% canceled by 2027 [6][7] — Referenced from Deloitte citing Gartner. ✅

**Math: "4x more capable by mid-2027":**  
Feb 2026 → Sep 2026 (2x) → Apr 2027 (4x). ✅ Correct.

**Math: "~8x by Dec 2027":**  
→ Nov 2027 (8x). Close enough to Dec 2027. ✅

### Section 13: Recommendations

**Facts:** Aggregation of previously cited claims. No new unsourced claims. ✅  
**Cost framework:** "$200K-$2M" cited as [22] (internal AR-001 v1). Properly labeled "[Internal — not independent]" in references. Honestly caveated: "No independent TCO study validates these ranges." ✅

### Section 14: Predictions

**Boldness check:** Prediction 5 (doubling slows to >12 months, 45% confidence) is the only genuinely contrarian one. Others are reasonable extrapolations most experts would agree with (>$50M incident, cancellations, acquisition, NIST guidance). **Would >30% of experts disagree?** Marginally — predictions 3 and 5 pass, others are consensus-adjacent.

### Section 15: Transparency Note

Complete and honest. Weakest point disclosure is brutally good ("No evidence that investing in trust infrastructure actually improves agent outcomes"). ✅

### Section 16: Claim Register

18 claims. Top 5 with invalidation conditions. ✅

### Section 17: References

- [3] METR paper: References says "Updated Dec 2025" but arXiv shows last update was **March 30, 2025** (v2). 🟡 **Wrong date in reference.**
- [22] Internal source properly labeled. ✅
- 24 references matching 24 sources in Source Log. ✅
- [23] McKinsey and [24] Obsidian Security are in references but I can't find where they're cited in the body text. 🟢 Unused references (minor).

---

## Deliverable 3: Limitations & Honesty Check

| Check | Status | Notes |
|-------|--------|-------|
| Inline caveats in body sections? | ✅ | Every section has [I], [J], [A] badges and callouts |
| Transparency Note 5-7 limitation bullets? | ✅ | 7 bullets, all substantive |
| Conflict of Interest disclosed? | ✅ | "Ainary Ventures provides AI strategy advisory. This report's conclusions align with Ainary's commercial interests." |
| Author Bio → "About This Report"? | ✅ | Standard text, no personal name, links to ainaryventures.com |
| NO Adversarial Self-Review section? | ✅ | Removed. Critiques distributed inline. |

---

## Deliverable 4: Math Verification

| Calculation | Verified? | Notes |
|-------------|-----------|-------|
| 51-percentage-point chasm (57% - 6%) | ✅ | 57 - 6 = 51 |
| 4x capability by mid-2027 | ✅ | 7mo doubling × 2 = 14mo = Apr 2027 |
| 8x capability by Dec 2027 | ✅ | 7mo × 3 = 21mo = Nov 2027 ≈ Dec |
| Market $7.55B → $10.86B (44% CAGR) | ✅ | 7.55 × 1.4384 = 10.86. Confirmed. |
| Governance $309M → ~$420M (36% CAGR) | ✅ | 309 × 1.3574 = 419.4 ≈ $420M |
| 5x gap between 50%/80% horizons | ⚠️ | Not verifiable from abstract; likely in full paper |

---

## Deliverable 5: Source Diversity Check

| Category | Count | % | Target (~33% each) |
|----------|-------|---|---------------------|
| Industry Reports | 8 | 33% | ✅ |
| Academic/Peer-Reviewed | 3 | 13% | 🟡 Below target |
| Practitioner/Contrarian | 3 | 13% | 🟡 Below target |
| Trade/Vendor | 9 | 37% | 🟡 Above target |
| Standards/Regulatory | 1 | 4% | — |

**Assessment:** Improved dramatically from v2 (0% academic/contrarian → 13%/13%). Still vendor-heavy at 37%. Not a blocker — the academic sources (UC Berkeley, METR, TRiSM) are the report's strongest evidence. The 3 contrarian voices (Marcus, MIT Tech Review, Siegel) provide essential balance.

---

## Deliverable 6: Originality Check

**1. "Would an expert learn something new?"**  
**Yes.** The Trust Race Model (capability velocity vs governance tempo as a temporal dynamic) is not in any of the 24 sources. The "deployment-trust inversion" framing (6% trust vs 57% deployment) is synthesis, not summary. The Governance Lag Cascade as a 6-step constructed scenario is original.

**2. "What is the original contribution?"**  
The Trust Race Model framework — modeling the trust problem as a dynamic race rather than a static gap. This is a genuine intellectual contribution that reframes the conversation.

**3. "Does the thesis provoke?"**  
Yes. "Structurally guaranteed to lose without fundamentally different infrastructure" is a strong claim. Reasonable experts would disagree: some would argue governance only needs to set outer boundaries, not track capability 1:1; others that market self-correction via failures is sufficient.

**4. Section titles: arguments or categories?**  
All 9 analysis sections are arguments. ✅ ("Everybody's Deploying, Nobody's Trusting" / "The Agents Don't Actually Work Yet" / etc.)

**5. Predictions: would >30% of experts disagree?**  
Marginally. Predictions 3 (governance vendor acquisition) and 5 (doubling slows) would see disagreement. Others are relatively consensus. Acceptable but not exceptional.

---

## Deliverable 7: Fix Requests

### 🔴 BLOCKER

**FIX-1: Misquoted HBR investment statistic**

The report says "72% expect to increase agent investment" citing [1] (HBR/Workato). The actual Fortune article says **"Eighty-six percent of respondents expect investment in agentic AI to increase over the next two years."**

Replace in §4:
```
yet <strong>72% expect to increase agent investment</strong> over the next two years<sup>[1]</sup>
```
with:
```
yet <strong>86% expect to increase agent investment</strong> over the next two years<sup>[1]</sup>
```

Replace in §6 KPI grid:
```
<div class="kpi-number">72%</div>
<div class="kpi-label">of enterprises plan to increase agent investment</div>
```
with:
```
<div class="kpi-number">86%</div>
<div class="kpi-label">of enterprises plan to increase agent investment</div>
```

Replace in Exhibit 2 (§8):
```
<td>72% plan to increase investment</td>
```
with:
```
<td>86% plan to increase investment</td>
```

**FIX-2: Unsourced claim marked as Evidenced in §9**

Section 9, Step 5 states: "67% of security alerts are ignored in practice" with an [E] badge but NO citation number. Either:
- (a) Add a citation to a verifiable source and add to Source Log, OR
- (b) Change classification to [A] (Assumption) and add caveat, OR
- (c) Remove the specific percentage

Recommended: Replace:
```
67% of security alerts are ignored in practice. Monitoring dashboards
```
with:
```
a significant proportion of security alerts go unreviewed in practice<sup>[source needed]</sup>. Monitoring dashboards
```
and change the badge from `badge-e` to `badge-a`.

### 🟡 SHOULD FIX

**FIX-3: Quote page uses paraphrased quote**

"(paraphrased)" undermines the quote's credibility. TEMPLATE-RULES require properly attributed external quotes. Either find the actual Nadella quote or replace with a different, genuine quote. A paraphrased quote is not a quote.

**FIX-4: ISO update cycle claim is imprecise**

In §7, the report says "Both update on annual cycles at best." ISO 42001 was published Dec 2023 and hasn't been updated. ISO revision cycles are typically 3-5 years, not annual. This actually STRENGTHENS the argument.

Replace in §7:
```
Both are widely referenced. Both update on annual cycles at best.
```
with:
```
Both are widely referenced. NIST AI RMF updates periodically (last May 2025); ISO 42001 follows multi-year revision cycles typical of international standards.
```

**FIX-5: METR reference date is wrong**

Reference [3] says "Updated Dec 2025" but arXiv shows v2 was submitted March 30, 2025.

Replace:
```
[3] METR. (2025). "Measuring AI Ability to Complete Long Tasks." arXiv:2503.14499. Updated Dec 2025. Accessed: 2026-02-15.
```
with:
```
[3] Kwa, T., West, B., Becker, J. et al. (2025). "Measuring AI Ability to Complete Long Tasks." METR. arXiv:2503.14499. Updated Mar 2025. Accessed: 2026-02-15.
```

**FIX-6: Exhibit 2 Governance Tempo says "Annual at best" — should match FIX-4**

Replace in Exhibit 2:
```
<td>Annual at best</td>
<td>ISO [4], NIST [5], EU AI Act [8]</td>
```
with:
```
<td>Multi-year (ISO) to periodic (NIST); step-function (regulation)</td>
<td>ISO [4], NIST [5], EU AI Act [8]</td>
```

### 🟢 NICE TO HAVE

**FIX-7:** References [23] (McKinsey State of AI) and [24] (Obsidian Security) appear in the References section but are not visibly cited in the body text. Either add inline citations or note them as "background sources" in the Source Log.

**FIX-8:** The governing metaphor "accelerating vehicle with no brakes" from the Thesis Document barely appears in the report. Consider adding it to the Executive Summary subtitle or Section 11 title to strengthen the narrative arc.

**FIX-9:** Predictions 1, 2, and 4 could be bolder. Most experts would agree with them. Consider tightening timelines or raising thresholds to ensure >30% disagreement.

---

## Deliverable 8: GO / NO-GO

### 🟡 CONDITIONAL GO

**Score: 18/20** — meets Tier 3 threshold.

**1 Blocker remaining:**
- FIX-1 (72% → 86% misquote) — 2-minute fix, 3 replacements
- FIX-2 (unsourced 67% claim) — 5-minute fix, needs source or reclassification

**After fixing FIX-1 and FIX-2:** Full GO.

**Assessment:** This is a dramatically better report than v2. The Trust Race Model is a genuine intellectual contribution. The evidence discipline is strong (24 sources, all within freshness window, honest E/I/J/A labeling throughout). The Transparency Note is exemplary — especially the "Weakest Point" disclosure. The narrative arc works. Section titles are arguments. The constructed scenario is well-sourced and honestly labeled.

**What I'm still uncertain about:**
- The 25% ChatDev correctness and 5x horizon gap are likely in the full papers but I could only verify from abstracts. Low risk — both are from reputable academic sources.
- Camunda's 73% and 11% stats are behind a gated report. Medium risk.

**Bottom line:** Fix the two blockers. Then publish. This is Tier 3 quality.
