# Agent Calibration - Prediction Log

**Created:** 2026-02-10  
**Purpose:** Track predictions with confidence levels to measure calibration accuracy over time

---

## Prediction Set #1 - Initial Baseline

**Date:** 2026-02-10

### Prediction 1: Andreas Brand's Lagerungstraverse Calculation
- **Prediction:** Manual calculation result is between 550-750 minutes
- **Confidence:** 70%
- **Status:** ⏳ Unverified (no access to Andreas's actual calculation yet)
- **Notes:** Based on our own calculation of 661 min; assuming human manual calc could vary ±15%

---

### Prediction 2: S355 Steel Plate Price (>100mm thick)
- **Prediction:** €2.50-3.50/kg on Feb 1, 2026
- **Confidence:** 75%
- **Status:** ❌ **WRONG** (overestimated significantly)

**Web Research Results:**
- **Source:** [Midwest Steel Supply - S355 Price Guide 2025](https://midweststeelsupply.org/article/en10025-s355-s355-plate-s355-price/)
- **Actual Data:** €820-1,050 per metric ton for standard thickness (6-40mm) in Europe (2025)
- **Converted:** €0.82-1.05 per kg for standard thickness
- **Thick Plate Adjustment:** Plates >100mm thick typically cost 20-40% more than standard
- **Estimated Actual for >100mm:** ~€1.00-1.40 per kg

**Analysis:** My prediction was **1.8-3.5x too high**. Likely confused structural steel plate with specialty alloys or machined components.

**Calibration Error:** High. A 75% confident prediction should be much closer to actual values.

---

### Prediction 3: Florian's Unread Emails
- **Prediction:** Between 15-40 unread emails right now
- **Confidence:** 60%
- **Status:** ⏳ Unverified (cannot check email currently)
- **Notes:** Medium confidence reflects high variability in email habits

---

### Prediction 4: CNC Planner SaaS Pricing
- **Prediction:** Average CNC Planner SaaS charges €99-299/month
- **Confidence:** 75%
- **Status:** ⚠️ **PARTIALLY CORRECT** (but definition was unclear)

**Web Research Results:**
- **JobBOSS²:** $200/user/month (~€185/user) [Source: Top10ERP](https://www.top10erp.org/products/jobboss%C2%B2/pricing)
- **Cetec ERP:** $40/user/month (manufacturing ERP) [Source: Top10ERP Manufacturing ERP Guide](https://www.top10erp.org/blog/manufacturing-erp)
- **Fusion Operations (formerly Prodsmart):** Pricing not publicly listed
- **Fulcrum:** Pricing not publicly listed (contact sales)

**Analysis:** 
- My range €99-299/month is in the ballpark BUT most CNC software prices **per user**, not as flat SaaS
- If interpreting as "per user" → €99-299 covers the range from Cetec ($40) to JobBOSS ($200+)
- If interpreting as "total monthly cost for small shop" → would need to multiply by ~3-10 users = €300-2,000/month

**Calibration Error:** Medium. Prediction was reasonable but lacked precision on pricing model (per-user vs flat).

---

### Prediction 5: GJS-700 Cutting Speed
- **Prediction:** Recommended cutting speed for face milling GJS-700 with coated carbide is 150-200 m/min
- **Confidence:** 80%
- **Status:** ⚠️ **SLIGHTLY HIGH** (upper bound is optimistic)

**Web Research Results:**
- **Source:** [CastingSR - EN-GJS-700-2 Complete Guide](https://castingsr.com/en-gjs-700-2-complete-technical-guide-for-high-strength-ductile-iron-applications/)
- **Actual Data:** "Cutting speeds: **100-150 m/min** for turning and milling operations"

**Analysis:**
- My prediction: 150-200 m/min
- Actual range: 100-150 m/min
- **Overlap at 150 m/min** but my lower bound was too optimistic
- I overestimated by shifting the entire range ~25-50 m/min too high

**Calibration Error:** Low-Medium. 80% confidence should have been more conservative. The overlap saves it from being completely wrong.

---

## Initial Calibration Score

**Method:** Simple hit rate for verified predictions

| Prediction | Result | Points |
|------------|--------|--------|
| #1 | Unverified | - |
| #2 | Wrong (off by 1.8-3.5x) | 0/1 |
| #3 | Unverified | - |
| #4 | Partially Correct (definition unclear) | 0.5/1 |
| #5 | Slightly High (but overlaps) | 0.7/1 |

**Score: 1.2 / 3.0 verified predictions = 40% accuracy**

---

## Lessons Learned

### Overconfidence Patterns Identified:
1. **Steel pricing:** Confused structural steel with specialty materials - need to ground industrial commodity prices in actual market data
2. **Cutting speeds:** Optimistic bias toward higher performance values - conservative ranges are safer for 80%+ confidence
3. **SaaS pricing:** Failed to specify per-user vs flat pricing model - precision in definition matters

### Calibration Insights:
- **75-80% confidence predictions still had significant errors** → Need to reserve high confidence for truly well-known facts
- **Web research revealed faster than expected** → Should default to "search first, predict second" for verifiable facts
- **Range predictions need wider margins** → Human tendency to anchor on "ideal case" rather than "typical range"

### Action Items:
1. ✅ Create this prediction log for ongoing calibration tracking
2. Create source requirement standard (prevent unsourced facts)
3. Lower confidence levels until calibration improves
4. Always web-search verifiable facts before committing to files

---

## Future Predictions

*New predictions will be added here with timestamps, confidence levels, and verification results*

---

**Next Review:** After 20 predictions or 1 week, whichever comes first
