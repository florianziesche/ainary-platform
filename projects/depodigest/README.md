# DepoDigest Pro — AI Deposition Intelligence

*Turning depositions into actionable trial intelligence*

---

## Overview

DepoDigest Pro is an AI-powered deposition analysis tool for plaintiff personal injury attorneys. It goes beyond basic summarization to provide settlement impact scoring, contradiction detection, and cross-examination preparation.

## Features

### Core Analysis
- **Smart Summarization** — Narrative and page-line summaries with key quotes
- **Admission Extraction** — Automatic detection of liability and damages admissions
- **Timeline Generation** — Chronological event reconstruction from testimony

### Differentiators
- **Settlement Impact Score** — AI-assessed testimony strength affecting case value
- **Contradiction Detection** — Cross-reference multiple depositions for inconsistencies
- **Discovery Comparison** — Compare testimony to interrogatory responses
- **Cross-Exam Prep** — Generate impeachment points and suggested questions

## Tech Stack

- **Frontend:** Vanilla HTML/CSS/JavaScript (no framework, fast loading)
- **Backend:** Python with Claude API for NLP
- **Analysis Engine:** Multi-stage LLM pipeline with structured output

## Project Structure

```
depodigest/
├── README.md
├── app/
│   ├── index.html          # Main UI
│   ├── styles.css          # Styling
│   └── app.js              # Frontend logic
├── backend/
│   ├── analyzer.py         # Core analysis engine
│   ├── models.py           # Data structures
│   └── prompts.py          # LLM prompts
├── data/
│   ├── sample_depositions/ # Test transcripts
│   └── demo_output/        # Pre-generated results
└── docs/
    ├── ALGORITHM.md        # How it works
    └── DEMO_SCRIPT.md      # Demo walkthrough
```

## Quick Start

```bash
# Run analysis on a deposition
python backend/analyzer.py data/sample_depositions/smith_deposition.txt

# Start local demo
open app/index.html
```

---

*Version: 0.1.0 (Prototype)*
*Last Updated: 2026-02-02*
