# AI Company X-Ray

CLI tool that generates McKinsey-grade AI strategy reports for any company in minutes.

## Features

- **Multi-Agent Analysis**: 5 specialized AI agents (Scanner, Industry Analyst, Strategist, Financier, Provocateur)
- **Hyperthink Synthesis**: 3-round quality control (Synthesize → Critique → Finalize)
- **Beautiful Reports**: Dark-mode HTML with SVG charts (radar, donut, risk matrix, timeline)
- **Specific & Actionable**: Department-by-department ROI, strategic recommendations, implementation roadmaps
- **Provocative Insights**: "What McKinsey won't tell you" - uncomfortable truths and blind spots

## Installation

```bash
npm install
```

## Usage

### Set OpenAI API Key

```bash
export OPENAI_API_KEY="sk-..."
```

### Run Analysis

```bash
node xray.js "Company Name"
```

**Examples:**
```bash
node xray.js "Siemens"
node xray.js "Tesla"
node xray.js "Joe's Coffee Shop"
```

### Output

The tool generates two files in `output/`:
- `{company-slug}-xray.html` — Beautiful interactive report
- `{company-slug}-xray.json` — Raw structured data

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│ PHASE 1: Data Collection (Parallel)                    │
├─────────────────────────────────────────────────────────┤
│  • Scanner Agent      → Company intelligence            │
│  • Industry Analyst   → Industry benchmarks & trends    │
└─────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────┐
│ PHASE 2: Analysis (Parallel)                           │
├─────────────────────────────────────────────────────────┤
│  • Strategist         → SWOT, competitive position      │
│  • Financier          → ROI models, investment analysis │
│  • Provocateur        → Blind spots, uncomfortable truths│
└─────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────┐
│ PHASE 3: Hyperthink (Sequential)                       │
├─────────────────────────────────────────────────────────┤
│  Round 1: Synthesize  → Coherent draft                 │
│  Round 2: Critique    → Hostile review                 │
│  Round 3: Finalize    → Incorporate feedback           │
└─────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────┐
│ PHASE 4: Render                                         │
├─────────────────────────────────────────────────────────┤
│  • JSON → HTML with SVG charts                         │
│  • Dark mode responsive design                         │
└─────────────────────────────────────────────────────────┘
```

## Report Structure

The final report includes:

1. **Executive Summary** — 3-4 paragraph overview
2. **AI Readiness Assessment** — 5 dimension scoring (0-100)
3. **Competitive Position** — Radar chart vs competitors
4. **Department Opportunities** — 4-6 specific use cases with ROI
5. **Strategic Recommendations** — Top 3 priorities with timelines
6. **Implementation Roadmap** — 3 phase plan (0-6mo, 6-12mo, 12-24mo)
7. **Risk Assessment** — Risk matrix with mitigation strategies
8. **Provocateur Insights** — Blind spots and uncomfortable truths
9. **Bottom Line** — Total opportunity, investment, payback

## Example Output

```bash
$ node xray.js "Siemens"

================================================================================
🔬 AI COMPANY X-RAY — Analyzing Siemens
================================================================================

[02:45:12] SCANNER         │ Scanning Siemens...
[02:45:15] INDUSTRY        │ Analyzing industry context for Siemens...
[02:45:18] PHASE 1         │ ✓ Data collection complete

[02:45:19] STRATEGIST      │ Developing strategy for Siemens...
[02:45:22] FINANCIER       │ Calculating financials for Siemens...
[02:45:24] PROVOCATEUR     │ Analyzing blind spots for Siemens...
[02:45:27] PHASE 2         │ ✓ Analysis complete

[02:45:28] HYPERTHINK      │ Starting 3-round synthesis...
[02:45:30] HYPERTHINK      │ Round 1: Synthesizing all agent outputs...
[02:45:35] HYPERTHINK      │ ✓ Round 1 complete: Draft synthesized
[02:45:36] HYPERTHINK      │ Round 2: Hostile review...
[02:45:40] HYPERTHINK      │ ✓ Round 2 complete: Critique generated
[02:45:41] HYPERTHINK      │ Round 3: Finalizing report...
[02:45:48] HYPERTHINK      │ ✓ Round 3 complete: Final report ready
[02:45:49] PHASE 3         │ ✓ Hyperthink complete

[02:45:50] RENDERER        │ Generating HTML report...
[02:45:51] RENDERER        │ ✓ HTML generation complete
[02:45:51] PHASE 4         │ ✓ Report generation complete

================================================================================
✅ ANALYSIS COMPLETE
================================================================================

📊 Company: Siemens
📄 HTML Report: ./output/siemens-xray.html
📄 JSON Data: ./output/siemens-xray.json
⏱️  Duration: 39.2s
🔢 Total Tokens: 42,157
💰 Estimated Cost: $0.83

Key Findings:
  • AI Readiness Score: 72/100
  • Total Opportunity: $12.4M annually
  • Investment Required: $850K-$1.2M
  • Payback Period: 14 months
  • Strategic Recommendations: 3
  • Department Opportunities: 6
```

## Cost Estimation

Typical run (mid-size company):
- **Tokens**: ~40,000-60,000
- **Cost**: $0.80-$1.20 per report
- **Duration**: 30-60 seconds

## Files

```
ai-company-xray/
├── package.json            # Dependencies
├── xray.js                 # Main orchestrator (CLI entry point)
├── utils.js                # OpenAI wrapper + helpers
├── hyperthink.js           # 3-round synthesis engine
├── renderer.js             # JSON → HTML + SVG charts
├── agents/
│   ├── scanner.js          # Company intelligence gathering
│   ├── industry.js         # Industry benchmarking
│   ├── strategist.js       # Strategic analysis (McKinsey-style)
│   ├── financier.js        # Financial modeling & ROI
│   └── provocateur.js      # Contrarian insights
└── output/                 # Generated reports
```

## Quality Principles

1. **Specific > Generic** — No "improve culture" platitudes. Real initiatives.
2. **Realistic Numbers** — ROI ranges, not aspirational marketing fluff.
3. **Company-Specific** — Works for Siemens AND Joe's Coffee Shop.
4. **Error Handling** — Retry logic, graceful degradation.
5. **Transparent Assumptions** — Data quality & caveats explicitly stated.

## Future Enhancements

- [ ] Brave Search API integration for real-time web data
- [ ] Company size detection for auto-scaled recommendations
- [ ] Industry templates (Manufacturing, Healthcare, Retail, etc.)
- [ ] Multi-language support
- [ ] PDF export option
- [ ] Historical tracking (compare reports over time)

## License

MIT

---

Built with OpenAI GPT-4o | Dark mode design inspired by modern dev tools
