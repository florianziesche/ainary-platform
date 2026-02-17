# Ainary Research Pipeline

Automated research report generation using Anthropic API.
Optimized for $200 budget = ~3.3M Opus input tokens or ~60M Haiku input tokens.

## Strategy: Multi-Model Routing
- **Haiku** ($0.25/MTok in, $1.25/MTok out): Paper fetching, summarization, source extraction
- **Sonnet** ($3/MTok in, $15/MTok out): Synthesis, pattern recognition, cross-referencing  
- **Opus** ($15/MTok in, $75/MTok out): Final report writing, quality gate, opinionated analysis

## Pipeline Stages
1. **Intake** — Fetch papers from arxiv, RSS, web search (Haiku)
2. **Extract** — Pull key findings, methods, results from each paper (Haiku)
3. **Synthesize** — Cross-reference findings, identify patterns (Sonnet)
4. **Write** — Generate report HTML from template (Opus)
5. **Quality Gate** — Self-audit, source verification (Sonnet)
6. **Publish** — Git push + Vercel deploy

## Cost Estimate per Report
- Intake: ~50K Haiku tokens = $0.01
- Extract (10 papers): ~500K Haiku tokens = $0.13
- Synthesize: ~100K Sonnet tokens = $0.30
- Write: ~50K Opus tokens = $0.75
- Quality: ~50K Sonnet tokens = $0.15
- **Total per report: ~$1.34**
- **$200 budget = ~149 reports**
