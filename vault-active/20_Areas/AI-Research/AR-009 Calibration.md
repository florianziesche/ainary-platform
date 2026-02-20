---
tags: 
report: AR-009
qa-score: 72/100
date: 2026-02-14
audience: 
tier: OPERATIONAL
expires: 2026-08-20
---

# AR-009 The Calibration Gap

## Executive Summary

- 84% of [[AI]] agents are overconfident — confidence exceeds actual accuracy across 9 models and 351 scenarios
- Verbalized confidence is biased upward by 20-30 percentage points and poorly correlated with correctness (r ≈ 0.3-0.5)
- Multi-agent verification amplifies miscalibration instead of correcting it — identically biased validators create false consensus
- Alert fatigue from overconfident systems causes 67% of security alerts to be ignored
- A calibration check costs $0.005 per decision; not calibrating has cost up to $7.5B in single cases (VW Cariad)

## Key Insights

- **Root cause is training:** RLHF reward signal favors confident answers, instruction tuning trains out "I don't know," sycophancy reinforces user premises — overconfidence is emergent property, not model defect
- **Verbalized confidence expression (VCE) is systematically biased:** [[LLM]]s cluster around round numbers (70%, 80%, 90%, 95%) rather than smooth distribution, upward bias 20-30pp, poor correlation with correctness
- **Multi-agent amplification loop:** Agent A (overconfident) → Agent B verifies (also overconfident) → sycophancy bias toward agreement → anchoring on Agent A's confidence → compound overconfidence approaching 100% in 3-agent chains
- **Trust erosion spiral:** Phase 1 (Overcommitment) → Phase 2 (Discovery — 95% confidence on wrong AND right) → Phase 3 (Alert fatigue — 67% ignored) → Phase 4 (Binary choice: abandon [[AI]] or remove oversight) → Phase 5 (Catastrophe)
- **Five calibration methods:** Temperature Scaling (gold standard, requires logit access), Conformal Prediction (guaranteed coverage, needs set handling), Sample Consistency (black-box, $0.003/check), Budget-CoCoA (SOTA, $0.005/check), Selective Prediction (requires retraining)

## Sales Angles

- "84% of [[AI]] outputs are overconfident. Your agents say '95% sure' when they're 70% accurate. We implement Budget-CoCoA calibration for $135/month (1,000 checks/day) — the ROI is 1:1,500,000."
- "Your multi-agent system uses 'Agent B verifies Agent A' for quality. That creates false consensus, not quality assurance. We redesign for disagreement measurement, not confirmation bias."
- "Alert fatigue kills 67% of security alerts. [[AI]] overconfidence will do the same to your HITL system unless you calibrate. We prevent the trust erosion spiral before Phase 3."

## Content Ideas

- LinkedIn: "Verbalized confidence is 'systematically biased and poorly correlated with correctness' (arXiv:2602.00279). Your agents cluster around 70/80/90/95% regardless of actual accuracy. Here's the $0.005 fix."
- Technical Walkthrough: "Sample Consistency vs. Budget-CoCoA vs. Conformal Prediction" — when to use which calibration method
- Case Study: "How $0.005 Calibration Prevents $7.5B VW-Scale Failures" — the asymmetry between prevention cost and failure cost

## Links

- [[AR-001 State of Agent Trust]]
- [[AR-002 Trust Tax]]
- [[AR-004 Maturity Model]]
- [[AR-007 Orchestration]]
- PDF: content/reports/calibration-2026.pdf
- MD: content/reports/calibration-2026-v2.md

## Related
- [[article-1-100-agents]]
- [[article-1-100-agents-de]]
- [[100-agents-48-stunden]]
- [[twitter-ai-agents-employees]]
- [[100-agents-evolution]]
