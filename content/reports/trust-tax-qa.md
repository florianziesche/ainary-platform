# QA Review — "The Trust Tax" (Report #2)

**QA Agent** | Date: 2026-02-14  
**Report reviewed:** `/content/reports/trust-tax-2026.md`  
**Research brief:** `/experiments/agent-test/research-trust-tax.md`  
**Standards:** `/agents/context-packs/pipeline-pack.md`

---

## GESAMTSCORE: 88/100

---

## SECTION SCORES

| Section | Score | Notes |
|---|---|---|
| 1. Factual Accuracy | 90/100 | All major claims match research brief. One minor sample-size inconsistency (see below). |
| 2. Source Attribution | 95/100 | Every number has a source + confidence level. Claim Register is excellent (25 claims). Best-in-class. |
| 3. Evidence vs Interpretation | 88/100 | Consistently separated with "So What?" boxes and Section Confidence labels. Slight blurring in Section 6 (Opportunity Tax) where correlation is presented close to causation. |
| 4. Internal Consistency | 85/100 | One inconsistency: EY Work Reimagined sample is "15,000 employees + 1,500 employers" in text (Section 2) but "n=16.5K" in Claim Register. Also, Section 2 calls it "n=15,000 employees and 1,500 employers, 29 countries" but the EY source page says the same — fine in text, just pick one format for the register. |
| 5. Narrative Coherence | 92/100 | Excellent flow: already paying → 5 line items → compounding → alternative → decision. The "invoice" metaphor is sustained throughout. Strong narrative arc. |
| 6. Voice | 85/100 | Good solo founder voice ("I call it..."). A few borderline LLM-ish constructions: "Here's the part that makes this particularly painful" (Section 2), "This is a paradox that most AI strategies don't account for" (Section 4). Not dealbreakers but could be tightened. |
| 7. Completeness | 90/100 | All outline sections present. Missing: explicit "What would invalidate this?" per section (only in Beipackzettel). Pipeline-pack QA rubric requires it for key claims. |
| 8. Actionability | 90/100 | "Three Steps for Monday Morning" is strong and specific. "Mein Vote" is clear. CFO/CISO can act on this. |

---

## TOP ISSUES (must fix)

1. **EY Work Reimagined sample size inconsistency** — Text says "n=15,000 employees and 1,500 employers" but Claim Register #10 says "n=16.5K". Pick one consistent representation. The 16.5K is the combined total and technically correct but should match the text.

2. **EY 40% productivity claim — nuance needed** — The report says companies are "missing up to 40% of projected AI productivity gains." The actual EY source says "productivity benefits lag by over 40%" specifically "when new technology lands on fragile talent foundations." The report's framing implies this is universal; the source ties it to companies with weak talent strategy. Section 2 should add "for organizations with weak talent foundations" or similar qualifier. Currently Medium-High; this qualifier would make it High confidence.

3. **"What would invalidate this?" missing from body** — Pipeline-pack QA rubric item #6 requires this for key claims. It exists in the Beipackzettel but not inline. Add at least one sentence per major section or a dedicated "Limitations" paragraph.

---

## MINOR ISSUES

1. **Section 6 (Opportunity Tax)** — The 34%/65% EY correlation (governance → revenue/savings) is presented without the standard "correlation ≠ causation" caveat. The Section Confidence note acknowledges it but the main text doesn't. One sentence would suffice.

2. **Voice nits** — "Here's the part that makes this particularly painful" and "This is a paradox that most AI strategies don't account for" are slightly generic. Could be sharper.

3. **$0.005/check framing** — The report attributes this to "Budget-CoCoA pricing, verified against Anthropic API costs." This is Florian's own product/methodology — should be disclosed more explicitly (e.g., "our calibration layer" or "the approach I'm building"). Currently reads like an independent market price. Transparency strengthens credibility with the [KUNDE] audience.

4. **Compliance cost source** — The $2-5M compliance setup figure cites "axis-intelligence.com" (Medium confidence). For a [KUNDE] audience, this is the weakest-sourced number in the comparison table. Consider adding a second source or flagging it more prominently.

5. **ROI math** — "880:1" ratio ($4.4M ÷ $5K) compares annual average loss against calibration cost only, excluding the $2-5M governance setup. The 333x-3,333x range is more honest. The 880:1 in Section 9 could mislead; clarify it's calibration-only cost.

6. **Word count** — Beipackzettel says ~4,800 words. Actual is closer to ~5,500. Minor but update for accuracy.

---

## CALIBRATION RESULTS

| # | Claim | Report Value | Source Check | Confidence |
|---|---|---|---|---|
| 1 | Orgs with AI losses | 99% | ✅ **Bestätigt** — EY.com, Reuters, Insurance Journal all confirm 99%, n=975 | High |
| 2 | Average AI loss per company | $4.4M | ✅ **Bestätigt** — EY primary source confirms. IBM report separately cites $4.44M global average breach cost (different metric but corroborative) | High |
| 3 | Shadow AI breach cost | $4.63M ($670K premium) | ✅ **Bestätigt** — Kiteworks analysis of IBM report, exact figures match | High |
| 4 | AI confidence collapse | Usage +13%, confidence -18% | ✅ **Bestätigt** — ManpowerGroup investor page and press release confirm exact figures | High |
| 5 | Deloitte trust fell 31% | -31% May-Jul 2025 | ✅ **Bestätigt** — HBR article confirms exact figure and timeframe | High |
| 6 | Workslop $186/employee/month | $186/mo, 2h per incident | ✅ **Bestätigt** — Forbes (2 articles), leadwithai.co all cite same figure. Note: traces to single underlying study (Stanford/HBR). | Medium-High |
| 7 | 40% missed AI productivity gains | Up to 40% | ⚠️ **Plausibel mit Einschränkung** — EY confirms "lag by over 40%" but specifically for companies with "fragile talent foundations," not universally. Report should qualify. | Medium-High |
| 8 | Arup deepfake | $25.6M, 15 transactions | ✅ **Bestätigt** — Fortune, MIT, multiple outlets confirm $25.6M (HK$200M) and deepfake video call | High |
| 9 | Zillow AI loss | $881M | ✅ **Bestätigt** — Full Stack Economics, re-brokerage.com confirm $881M loss on Zillow Offers in 2021 | High |
| 10 | Knight Capital | $440M in 45 min | ✅ **Bestätigt** — Wikipedia, case studies confirm $440M pre-tax loss in ~45 minutes | High |

**Calibration Summary:** 9/10 claims fully verified, 1/10 plausible with needed qualifier. Zero claims widerlegt. Excellent factual foundation.

---

## VERDICT: CONDITIONAL PASS ✅

**Conditions for PASS:**
1. Fix EY 40% claim qualifier (add "for organizations with weak talent foundations")
2. Fix sample size inconsistency (n=16.5K vs n=15K+1.5K)
3. Add "what would invalidate this" inline or as brief Limitations section

**Estimated fix time:** 15-20 minutes.

**Overall Assessment:** This is a strong, well-sourced report with an effective narrative arc. The Claim Register and Beipackzettel are excellent quality controls. The "invoice" metaphor works well for the CFO audience. The three conditions above are straightforward fixes that would bring this to a clear PASS.

---

*QA Review completed 2026-02-14*
