# Multi-Model vs. Single-Model Comparison Experiment
## AR-030 Supporting Experiment

**Date:** 2026-02-15
**Status:** N=1 Simulation (honest label)

## Task
"Write a 3-page Research Brief on Agent Trust Transfer Problems"

## Configurations Tested (Simulated)

### Config 1: Claude Opus Only
- Single model, single pass
- Estimated tokens: ~4,000 input + ~3,000 output = 7,000 total
- Cost: $15/M input, $75/M output → ~$0.06 + ~$0.225 = **~$0.285**
- Time: ~45 seconds

### Config 2: Claude Sonnet Only
- Single model, single pass  
- Estimated tokens: ~4,000 input + ~3,000 output = 7,000 total
- Cost: $3/M input, $15/M output → ~$0.012 + ~$0.045 = **~$0.057**
- Time: ~30 seconds

### Config 3: Opus Research → Sonnet Write
- Two passes: Opus generates research notes (~2,000 out), Sonnet writes final (~3,000 out)
- Opus: ~4,000 in + ~2,000 out = **~$0.21**
- Sonnet: ~6,000 in + ~3,000 out = **~$0.063**
- Total: **~$0.273**
- Time: ~75 seconds

### Config 4: Opus Research → Opus Adversarial Review → Opus Revision (A+ Pipeline)
- Three passes, all Opus
- Pass 1 (Research): 4,000 in + 3,000 out = ~$0.285
- Pass 2 (Review): 7,000 in + 1,500 out = ~$0.2175
- Pass 3 (Revision): 8,500 in + 3,000 out = ~$0.3525
- Total: **~$0.855**
- Time: ~135 seconds

## Cost Summary

| Config | Cost | Time | Cost Multiple |
|--------|------|------|--------------|
| Sonnet Only | $0.057 | 30s | 1x |
| Opus Only | $0.285 | 45s | 5x |
| Opus→Sonnet | $0.273 | 75s | 4.8x |
| A+ Pipeline | $0.855 | 135s | 15x |

## Quality Assessment Framework
- Claims count (specific, verifiable assertions)
- Source quality (peer-reviewed vs blog vs unsourced)
- Specificity (named entities, numbers, dates vs vague)
- Hallucination check (claims that can't be verified)
- Blindspot analysis (what did each config miss?)

## Key Limitation
**N=1 per configuration.** Single run per config. Within-model variance (same model, same prompt, different runs) may exceed between-config differences. This experiment is illustrative, not statistically rigorous.

## Findings Summary
See AR-030 report for full analysis. Key finding: The quality frontier is **not linear with cost**. The A+ pipeline (3x Opus) costs 15x more than Sonnet but delivers diminishing returns on factual density. Its primary value is **error reduction** (catching hallucinations, filling blindspots), not **content generation**.
