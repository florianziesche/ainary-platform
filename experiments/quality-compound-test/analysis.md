# Quality Compounding Experiment — AR-029
## Does AI Quality Actually Compound? A 25-Report Longitudinal Study

**Date:** 2026-02-15
**Analyst:** Opus (self-assessment — bias acknowledged)

---

## 1. TRUST-LEDGER Data Extraction

### Raw QA Scores (from TRUST-LEDGER.json, 15 entries available):
| Report | QA Score | Confidence | Sources | Claims | Words | Runtime(s) |
|--------|----------|------------|---------|--------|-------|------------|
| AR-001 | 82 | 72 | 12 | 15 | 6200 | 420 |
| AR-002 | 88 | 78 | 14 | 18 | 6500 | 380 |
| AR-003 | 82 | 75 | 16 | 22 | 7100 | 340 |
| AR-004 | 87 | 80 | 15 | 20 | 6800 | 410 |
| AR-005 | 85 | 77 | 13 | 19 | 6400 | 365 |
| AR-006 | 92 | 85 | 18 | 24 | 7500 | 450 |
| AR-007 | 79 | 70 | 11 | 16 | 5900 | 310 |
| AR-008 | 91 | 82 | 17 | 21 | 7200 | 425 |
| AR-009 | 91 | 84 | 19 | 23 | 7400 | 440 |
| AR-010 | 85 | 72 | 21 | 27 | 8100 | 395 |
| AR-011 | 85 | 75 | 15 | 20 | 6900 | 405 |
| AR-012 | 83 | 75 | 14 | 18 | 6600 | 385 |
| AR-013 | 80 | 72 | 13 | 17 | 6300 | 355 |
| AR-014 | 84 | 82 | 16 | 19 | 6700 | 415 |
| AR-015 | 85 | 78 | 16 | 12 | — | — |

**Note:** AR-016 through AR-025 are NOT in TRUST-LEDGER. Only 15 entries exist.

### Fact-Check: "Flat at 85.6"?
- TRUST-LEDGER says avg_qa = 85.3 (for builder-sonnet, 15 tasks)
- My calculation: (82+88+82+87+85+92+79+91+91+85+85+83+80+84+85) / 15 = **1279 / 15 = 85.27**
- Close to 85.3, NOT 85.6. The "85.6" claim would be inaccurate.
- **Verdict: Average is 85.3, not 85.6. Minor discrepancy but matters for honesty.**

### Trend Analysis
- Reports 1-5 avg: (82+88+82+87+85)/5 = **84.8**
- Reports 6-10 avg: (92+79+91+91+85)/5 = **87.6**
- Reports 11-15 avg: (85+83+80+84+85)/5 = **83.4**
- **Pattern: Rise then FALL. Not compounding. Regression toward mean.**

### Context Token Savings: "Really 50%?"
- TRUST-LEDGER economics.context_optimization: before=18500, after=9100, reduction=50.8%
- **Verdict: Yes, 50.8% is documented. But this is an architecture change (INDEX.md pattern), not quality compounding.**

---

## 2. Blind Comparison: AR-001 (Original) vs Today's System

### AR-001 Original Assessment
**Title:** State of AI Agent Trust 2026
**QA Score:** 82 | **Confidence:** 72 | **Sources:** 12 | **Claims:** 15

| Criterion | Score (1-10) | Notes |
|-----------|-------------|-------|
| Structure Quality | 8 | Full template compliance: Cover, Quote, TOC, HTR, ExecSum, Methodology, 6 sections, Predictions, Transparency, Claim Register, References, Back Cover |
| Source Quality | 6 | 12 sources. Mix of peer-reviewed (PMC), preprints (arXiv), corporate (McKinsey), media. ~20% peer-reviewed. Recency good (2024-2026). |
| Claim Precision | 7 | Strong specific claims ("84% of scenarios", "$0.005 per check"). Some vague ("95% fail" from secondary source). |
| Honesty | 8 | Confidence scores on every section. Limitations disclosed. Constructed scenario marked as such. Known_issues: "web search limited", "section transitions could be smoother" |
| Template Compliance | 7 | Uses old template elements (quote from "This Report" — violates later rule about external quotes). Section 10 heading says "What Must Change" not "Recommendations". |

**Total: 36/50**

### AR-005 Original Assessment
**Title:** The Financial Services Trust Playbook (AR-005)
**QA Score:** 85 | **Confidence:** 77 | **Sources:** 13 | **Claims:** 19

| Criterion | Score (1-10) | Notes |
|-----------|-------------|-------|
| Structure Quality | 8 | Full template compliance. |
| Source Quality | 6 | 13 sources. Similar mix. |
| Claim Precision | 7 | Financial-sector specific. |
| Honesty | 7 | Confidence badges present. |
| Template Compliance | 8 | Better than AR-001, closer to locked template. |

**Total: 36/50**

### AR-025 Assessment (Latest available)
**Title:** The Knowledge Compounding Flywheel (AR-025)
**QA Score:** — (not in TRUST-LEDGER as redesigned report) | **Confidence:** 72 (cover)

| Criterion | Score (1-10) | Notes |
|-----------|-------------|-------|
| Structure Quality | 9 | Full locked template. All sections present. Proper ordering (Invalidation before So What). |
| Source Quality | 7 | 21 sources. Internal experiment data. Mix of academic (Edvinsson, Kaplan, Wegner), practitioner, and projections. ~30% peer-reviewed. |
| Claim Precision | 8 | Very specific ("73% higher emergence", "56% of answers", "33-point quality gain"). Claims are hedged ("Internal" confidence tag for own data). |
| Honesty | 9 | N=1 limitations disclosed multiple times. 10x claim explicitly marked as hypothesis. Confidence badges on every section including low ones (60%, 65%). Quote page quote from "This Report" — still violates rule. |
| Template Compliance | 9 | Near-perfect. Minor issue: Quote is from "This Report" not external. |

**Total: 42/50**

---

## 3. Timeline Plot: What Improves, What Doesn't

### IMPROVES ✅
| Dimension | AR-001 | AR-005 | AR-025 | Trend |
|-----------|--------|--------|--------|-------|
| Template Compliance | 7 | 8 | 9 | ↑ Clear improvement |
| Honesty/Limitations | 8 | 7 | 9 | ↑ Better N=1 disclosure |
| Claim Precision | 7 | 7 | 8 | ↑ Slight improvement |
| Structure Quality | 8 | 8 | 9 | ↑ Slight improvement |
| Total Score | 36 | 36 | 42 | ↑ +17% improvement |

### DOES NOT IMPROVE ❌
| Dimension | AR-001 | AR-005 | AR-025 | Trend |
|-----------|--------|--------|--------|-------|
| Source Quality | 6 | 6 | 7 | → Marginal (12→13→21 count, but peer-reviewed % similar) |
| Source Peer-Review % | ~20% | ~20% | ~30% | → Slight improvement but still low |
| Originality | High (novel framing) | Medium | High (own experiment) | ~ Varies by topic |
| QA Scores (TRUST-LEDGER) | 82 | 85 | N/A | → Flat (85.3 avg) |

### GETS WORSE ⚠️
| Dimension | Early | Late | Trend |
|-----------|-------|------|-------|
| QA Score Trajectory | 84.8 avg (1-5) | 83.4 avg (11-15) | ↓ Declining |

---

## 4. The Honest Finding

**Quality does NOT compound in the way the pipeline narrative suggests.**

What actually happens:
1. **Template compliance compounds** — the locked template (D-157) guarantees structural quality floor
2. **Efficiency compounds** — token optimization (50.8%), runtime stabilization
3. **Process discipline compounds** — confidence badges, invalidation-before-sowhat, claim registers
4. **Content quality is FLAT** — QA scores oscillate 79-92, average 85.3, no trend
5. **Source quality is FLAT** — peer-reviewed % stays ~20-30%, source count fluctuates with topic
6. **Originality is RANDOM** — depends on topic, not iteration number

The pipeline is a **formatting machine that got better at formatting**. It did NOT become a better researcher over 25 reports.

### Why?
- The LLM is stateless. Report 25 does not "remember" reports 1-24.
- The template ensures consistency, not depth.
- Source quality depends on what's available via web search, not pipeline maturity.
- Claims are only as good as the research the LLM can access in-session.

### What Would Actually Compound?
- A vector database of prior research → RAG-based self-citation
- A claim registry that prevents re-citing debunked claims
- An external review loop feeding corrections back
- Domain expertise accumulation (which requires persistent memory, not session-based LLMs)

---

## 5. Adversarial Self-Review

### As Scientist: "Is the study design valid?"
**No.** Self-assessment is inherently biased. The same system that produced the reports is grading them. There is no inter-rater reliability. The QA scores in TRUST-LEDGER were assigned by the same pipeline — they are self-reported grades, not external validation. This is like asking a student to grade their own exams.

**H-002 in TRUST-LEDGER literally says:** "Unsere QA-Scores sind overconfident (79-92 Range zu hoch?)" — and suggests external review ($500-1000). That hypothesis remains UNTESTED.

### As Skeptiker: "Misst du wirklich Qualität oder nur Compliance?"
**Mostly compliance.** The QA score measures template adherence, source count, word count, claim count. These are proxies. A perfectly formatted report with shallow analysis would score 80+. A brilliant report with formatting errors would score lower. The metric optimizes for what's easy to measure (format) not what matters (insight).

### As Investor: "Ist 'Effizienz verbessert sich' genug?"
**No.** Efficiency gains are table stakes. Producing reports 50% cheaper is nice but not a moat. If the reports are 85/100 quality whether it's report #1 or #25, the system is a commodity text generator with a nice template — not a compounding intelligence system.

### "Was ist der Unterschied zwischen 'besser werden' und 'anders werden'?"
Critical distinction. The pipeline didn't get better — it got more consistent. The template locked quality FLOOR, not CEILING. The reports became more alike (convergence toward template), not better (improvement toward excellence). Standardization ≠ quality.
