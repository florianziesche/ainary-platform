# Startup X-Ray — VC Due Diligence Engine

AI-powered due diligence reports for venture capital. Generates McKinsey-grade investment analysis with **honest confidence indicators** about data quality.

## What It Does

Analyzes any startup (public or YC) and produces a comprehensive due diligence report covering:
- **Deal Score** (0-100) across Team, Market, Product, Traction, Timing
- **Founder X-Ray** — backgrounds, founder-market fit, red flags
- **Market Opportunity** — TAM/SAM/SOM, timing, dynamics
- **Competitive Landscape** — defensibility analysis, market map
- **Financial Assessment** — valuation estimate, comparables, unit economics
- **Growth Levers** — top 3 opportunities with impact estimates
- **Devil's Advocate** — red flags, kill shots, uncomfortable questions
- **Investment Thesis vs Anti-Thesis** — bull case vs bear case
- **5 Questions for the Founder** — what to ask in the meeting
- **Bottom Line** — INVEST / PASS / DIG_DEEPER recommendation

## Key Feature: Honest Confidence Indicators

Every section has a **confidence indicator** showing data quality:

- **●●●●●** High Confidence — Based on 15+ verified public sources
- **●●●●○** Good Confidence — Based on 8-14 public sources  
- **●●●○○** Moderate — Based on 3-7 public sources, some estimates
- **●●○○○** Low — Limited public data, significant estimation
- **●○○○○** Speculative — Minimal data, educated guess only

**Why this matters:** Most startup data is private. A VC who admits data gaps is more credible than one who bullshits. This system tells you exactly where the analysis is strong and where you need founder conversations.

## Architecture

**5 AI Agents:**
1. **Scanner** — Pre-screening due diligence (company, funding, founders, traction, tech, competitors)
2. **Market Analyst** — Market opportunity, timing, dynamics, defensibility
3. **Investor Analyst** — Deal scoring, founder assessment, growth levers, investment thesis
4. **Financier** — Valuation estimates, comparables, unit economics, exit scenarios
5. **Devil's Advocate** — Red flags, kill shots, contrarian takes

**3-Round Hyperthink Synthesis:**
1. **Synthesize** — Combine all agent outputs into coherent report
2. **Critique** — Hostile review to find weaknesses, data gaps, overly optimistic projections
3. **Finalize** — Incorporate critique, adjust scores, produce final report

**Honest by Design:**
- Agents rate confidence for every data point (VERIFIED / LIKELY / ESTIMATED / UNKNOWN)
- Final report includes Data Confidence section showing what's missing
- Scores reflect data quality — if confidence is LOW, scores are conservative
- No bullshit: "Revenue data not publicly available" > fake precision

## Usage

```bash
node xray.js "Stripe"
node xray.js "Notion"
node xray.js "Any Startup Name"
```

**Output:**
- `output/stripe-xray.html` — Interactive dark mode report
- Console logs show progress through 5 agents + 3 synthesis rounds

## Requirements

- Node.js 18+
- OpenAI API key in environment (`OPENAI_API_KEY`)
- Dependencies: `openai`, `puppeteer` (auto-installed)

## Design

**Dark Mode VC Template:**
- Primary color: **#8b5cf6** (Purple) — differentiated from Corporate X-Ray
- Secondary: **#10b981** (Emerald) for positive metrics
- Devil's Advocate section: **Red/Orange** for warnings
- SVG radar chart for Deal Scorecard (5 dimensions)
- Confidence dots next to every section header
- Side-by-side Bull Case vs Bear Case with color coding
- Deal Score as hero metric (like AI Readiness Score in Corporate version)

**NO emoji** — SVG icons only for clean, professional look.

## Email-Gated Download (Future)

Template includes modal for collecting:
- Full Name
- Email
- Fund Name (optional)
- AUM (optional)

Currently generates HTML directly. PDF generation can be added with same Puppeteer approach as Corporate X-Ray.

## Quality Standards

- **Works with ANY startup** — from Stripe to random YC companies
- **Ehrlichkeit > Bullshit** — If we don't have data, we say so
- **Confidence Indicators are the FEATURE** — not a bug
- Every narrative field is 2-4 paragraphs minimum (no thin sections)
- Scores are realistic and justified by evidence
- Recommendations match confidence level (don't say INVEST if confidence is SPECULATIVE)

## Differences from Corporate X-Ray

| Feature | Corporate X-Ray | Startup X-Ray |
|---------|-----------------|---------------|
| **Use Case** | AI strategy for large companies | VC due diligence for startups |
| **Agents** | Industry + Strategist + Provocateur | Market + Investor + Devil's Advocate |
| **Key Metric** | AI Readiness Score | Deal Score (Team/Market/Product/Traction/Timing) |
| **Data Quality** | Assumed high (public companies) | **Explicit confidence indicators** |
| **Honesty** | Standard consulting | **Transparent about data gaps** |
| **Color** | Indigo | Purple |
| **Output** | Corporate strategy playbook | VC investment memo |

## Example Run

```bash
$ node xray.js "Stripe"

╔══════════════════════════════════════════════╗
║  STARTUP X-RAY — VC Due Diligence Engine    ║
║  5 Agents · 3 Rounds · Honest Confidence     ║
╚══════════════════════════════════════════════╝

Target: Stripe

[HH:MM:SS] ◎ PHASE 1: Data Collection — Scanner + Market Analyst
[HH:MM:SS] ◎ SCANNER: Pre-screening due diligence on Stripe...
[HH:MM:SS] ◎ MARKET: Market opportunity analysis for Stripe...
[HH:MM:SS] ◎ PHASE 1: Complete (XX.Xs)
[HH:MM:SS] ◎ PHASE 2: Deep Analysis — Investor + Financier + Devil's Advocate
[HH:MM:SS] ◎ INVESTOR: Investment evaluation for Stripe...
[HH:MM:SS] ◎ FINANCIER: Financial analysis for Stripe...
[HH:MM:SS] ◎ DEVIL'S ADVOCATE: Finding every reason NOT to invest in Stripe...
[HH:MM:SS] ◎ PHASE 2: Complete (XX.Xs)
[HH:MM:SS] ◎ PHASE 3: Hyperthink — Synthesize → Critique → Finalize
[HH:MM:SS] ◎ HYPERTHINK: Round 1/3: Synthesizing all agent outputs...
[HH:MM:SS] ◎ HYPERTHINK: Round 2/3: Critical review...
[HH:MM:SS] ◎ HYPERTHINK: Round 3/3: Incorporating critique and finalizing...
[HH:MM:SS] ◎ HYPERTHINK: Complete. 3 rounds of synthesis finished.
[HH:MM:SS] ◎ PHASE 3: Complete (XX.Xs)
[HH:MM:SS] ◎ PHASE 4: Rendering HTML report...
[HH:MM:SS] ◎ RENDERER: Loading template...
[HH:MM:SS] ◎ RENDERER: Report saved: output/stripe-xray.html

╔══════════════════════════════════════════════╗
║  ✓ DUE DILIGENCE COMPLETE                    ║
╚══════════════════════════════════════════════╝

  Startup:  Stripe
  Time:     XX.Xs
  Agents:   5 (Scanner, Market, Investor, Financier, Devil's Advocate)
  Rounds:   3 (Synthesize → Critique → Finalize)
  Output:   output/stripe-xray.html
```

## Branding

**Built by:**
- Florian Ziesche
- Ainary Ventures
- AI Due Diligence Engine

## License

Private. For Ainary Ventures use only.

---

**The Rule:** Ehrlichkeit > Bullshit. If you don't have data, say so. VCs respect honesty.
