---
tags: [concept, calibration]
---
# K-002: Calibration

The process of aligning AI confidence with actual accuracy. 84% of LLMs are overconfident. VCE is biased 20-30pp upward.

Five methods: Temperature Scaling (gold standard), Conformal Prediction (guaranteed coverage), Sample Consistency (black-box, $0.003/check), Budget-CoCoA (SOTA, $0.005/check), Selective Prediction (requires retraining).

Calibration is the cheapest intervention with the highest ROI: $0.005/check vs $4.4M losses. ROI ratio 1:1,500,000.

**Appears in:** AR-001, AR-002, AR-004, AR-005, AR-009
