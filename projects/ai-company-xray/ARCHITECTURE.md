# AI Company X-Ray — Architecture

## Overview
CLI tool that generates McKinsey-grade AI strategy reports for any company.
`node xray.js "Company Name"` → `output/company-name-xray.html`

## Agent Pipeline

### Phase 1: DATA COLLECTION (Parallel)
```
Agent 1: SCANNER
  - Web search: "{company} AI strategy"
  - Web search: "{company} technology stack"
  - Web search: "{company} hiring AI machine learning jobs"
  - Web search: "{company} recent news AI"
  - Web search: "{company} competitors"
  → Raw data package
  
Agent 2: INDUSTRY ANALYST
  - Web search: "{industry} AI adoption rate 2025 2026"
  - Web search: "{industry} AI use cases enterprise"
  - Web search: "{industry} digital transformation benchmark"
  → Industry context package
```

### Phase 2: ANALYSIS (Parallel, fed by Phase 1)
```
Agent 3: STRATEGIST
  Input: Scanner data + Industry data
  Prompt: "You are a McKinsey senior partner. Analyze {company}'s AI position.
           Generate: SWOT, 3 strategic recommendations with ROI, implementation roadmap."
  → Strategic analysis
  
Agent 4: FINANCIER  
  Input: Scanner data + Industry data
  Prompt: "You are a CFO advisor. Calculate AI investment opportunity for {company}.
           Generate: Department-by-department ROI, total opportunity, investment required, payback."
  → Financial analysis
  
Agent 5: PROVOCATEUR
  Input: ALL previous outputs
  Prompt: "You are the contrarian. What is EVERYONE missing about {company}'s AI strategy?
           What would a $500K McKinsey engagement NEVER tell the CEO because it's politically unsafe?
           What are the hidden risks? The blind spots? The uncomfortable truths?"
  → Provocateur insights
```

### Phase 3: HYPERTHINK (Sequential)
```
Round 1: SYNTHESIZER
  Input: All 5 agent outputs
  Prompt: "Synthesize into a coherent executive report. Resolve contradictions."
  → Draft report

Round 2: CRITIC  
  Input: Draft report
  Prompt: "You are a hostile reviewer. What's wrong? What's missing? What's unsubstantiated?"
  → Critique

Round 3: FINALIZER
  Input: Draft report + Critique
  Prompt: "Incorporate valid criticisms. Produce the final report with these exact sections..."
  → Final structured JSON
```

### Phase 4: RENDER
- Take final JSON → inject into HTML template
- Generate SVG charts from data
- Output static HTML file

## Data Structure (Final JSON)
```json
{
  "company": "Siemens",
  "generated": "2026-02-12T02:45:00Z",
  "executive_summary": "...",
  "ai_readiness": {
    "overall": 72,
    "data_infrastructure": 78,
    "talent": 65,
    "strategy": 71,
    "culture": 68,
    "percentile": 74
  },
  "department_opportunities": [
    { "dept": "Manufacturing", "current": "...", "opportunity": "...", "impact": "$2.4M/yr", "difficulty": "Medium" }
  ],
  "competitive_position": {
    "dimensions": { "innovation": 75, "data_maturity": 80, ... },
    "competitors": [{ "name": "...", "ahead_in": "...", "behind_in": "..." }]
  },
  "recommendations": [
    { "title": "...", "why": "...", "roi": "...", "timeline": "...", "difficulty": "..." }
  ],
  "roadmap": { "phase1": {...}, "phase2": {...}, "phase3": {...} },
  "risks": [
    { "name": "...", "likelihood": 1-3, "impact": 1-3, "mitigation": "..." }
  ],
  "provocateur": {
    "blind_spots": ["..."],
    "uncomfortable_truths": ["..."],
    "what_mckinsey_wont_say": "..."
  },
  "bottom_line": {
    "total_opportunity": "$X.XM",
    "investment": "$XXK-$XXXK",
    "payback": "X months"
  }
}
```

## Tech Stack
- Node.js
- Anthropic Claude API (via SDK)
- Brave Search API (via web_search)
- No external frontend dependencies
- HTML template with inline CSS/JS (same dark mode design)

## Files
- `xray.js` — Main orchestrator
- `agents/scanner.js` — Web search + data collection
- `agents/industry.js` — Industry benchmarking
- `agents/strategist.js` — Strategic analysis
- `agents/financier.js` — Financial modeling
- `agents/provocateur.js` — Contrarian insights
- `hyperthink.js` — 3-round synthesis
- `renderer.js` — JSON → HTML
- `template.html` — Report template
