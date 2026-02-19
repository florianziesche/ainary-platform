# Research Pipeline Architecture — Stand 19.02.2026

## System Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                    RESEARCH FACTORY                              │
│                  research_factory.py                              │
│                                                                  │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐     │
│  │  INTAKE  │──→│ STAGE 1  │──→│ STAGE 2  │──→│ STAGE 3  │     │
│  │          │   │ Report   │   │ Assets   │   │ Knowledge│     │
│  └──────────┘   └──────────┘   └──────────┘   └──────────┘     │
│                      │                              │            │
│              ┌───────┴───────┐              ┌──────┴──────┐     │
│              │   REVIEWER    │              │  CRT Update │     │
│              │  (Sonnet)     │              │  Vault Notes│     │
│              └───────────────┘              └─────────────┘     │
└─────────────────────────────────────────────────────────────────┘
```

## Hybrid Model Routing

```
┌─────────────────────────────────────────────────┐
│              llm_call() Router                   │
│                                                  │
│   Model name starts with...                      │
│                                                  │
│   "gpt-*"  ──→  OpenAI API  ──→  GPT-4o         │
│                  (OPENAI_API_KEY)                 │
│                  22s, $0.01/call                  │
│                  + 3x Retry on refusal           │
│                                                  │
│   "claude-*" ──→  Anthropic OAuth  ──→  Sonnet   │
│                   (Bearer token from              │
│                    auth-profiles.json)            │
│                   60s, $0/call (Pro plan)         │
│                                                  │
│   Fallback ──→  init_client() default            │
└─────────────────────────────────────────────────┘

Default Model Assignment:
  Producer (Report)    = gpt-4o       ← Fast, cheap
  Reviewer (Rubric)    = claude-sonnet ← Skeptical, honest
  Assets               = gpt-4o       ← Structured extraction
  Knowledge Integ.     = gpt-4o       ← Fast
  Claims Evaluator     = claude-sonnet ← Harsh, calibrated
  Synthesis            = claude-sonnet ← Quality
```

## Confidence-Target Pipeline

```
                    ┌─────────────┐
                    │   INTAKE    │
                    │  Topic +    │
                    │  Target %   │
                    └──────┬──────┘
                           │
                    ┌──────▼──────┐
                    │ BRAVE SEARCH│──→ research-base/papers/web-*.md
                    │ 4 queries   │    (Top 5 URLs fetched + stored)
                    │ 20-30 hits  │
                    └──────┬──────┘
                           │
              ┌────────────▼────────────┐
              │     ITERATION LOOP      │
              │     (max N rounds)      │
              │                         │
              │  ┌───────────────────┐  │
              │  │ 1. WEB ENRICH     │  │
              │  │    Brave Search   │  │
              │  │    + fetch URLs   │  │
              │  │    + store papers │  │
              │  └────────┬──────────┘  │
              │           │             │
              │  ┌────────▼──────────┐  │
              │  │ 2. PRODUCE (GPT4o)│  │
              │  │    Report ~10K ch  │  │
              │  │    Rubric 16/16   │  │
              │  └────────┬──────────┘  │
              │           │             │
              │  ┌────────▼──────────┐  │
              │  │ 3. REVIEW (Sonnet)│  │
              │  │    Rubric scoring  │  │
              │  └────────┬──────────┘  │
              │           │             │
              │  ┌────────▼──────────┐  │
              │  │ 4. EXTRACT CLAIMS │  │
              │  │    (Sonnet, 12x)  │  │
              │  │    Admiralty rated │  │
              │  └────────┬──────────┘  │
              │           │             │
              │  ┌────────▼──────────┐  │
              │  │ 5. CONFIDENCE     │  │
              │  │    AgentTrust     │  │
              │  │    Formula        │  │
              │  └────────┬──────────┘  │
              │           │             │
              │      conf >= target?    │
              │       │YES     │NO      │
              │       │    ┌───▼─────┐  │
              │       │    │ PRUNE   │  │
              │       │    │ weak    │  │
              │       │    │ claims  │  │
              │       │    │ + RAG   │  │
              │       │    │ targeted│  │
              │       │    └───┬─────┘  │
              │       │        │        │
              │       │   plateau <2%?  │
              │       │    │YES   │NO   │
              │       │    │      └──→ LOOP
              │       │    │            │
              └───────┼────┼────────────┘
                      │    │
               ┌──────▼────▼──────┐
               │   FINAL OUTPUT   │
               │  final-report.md │
               │  final-assets.md │
               │  claims.json     │
               │  pipeline.json   │
               └──────────────────┘
```

## AgentTrust Confidence Formula

```
claim_confidence = 0.5 × SOURCE + 0.3 × CONSISTENCY + 0.2 × STRUCTURAL

Where:

  SOURCE = admiralty_score × verification_score × recency
  ├── admiralty_score:   A1=0.95  B2=0.70  C3=0.40  D4=0.20  E2=0.10
  ├── verification:     verified=1.0  partial=0.5  unverifiable=0.1
  └── recency:          max(0.5, 1.0 - (current_year - evidence_year) × 0.1)

  CONSISTENCY = Budget-CoCoA proxy (from verification rating)
  ├── verified     → 0.85  (high agreement)
  ├── partial      → 0.60  (medium)
  └── unverifiable → 0.30  (low)

  STRUCTURAL = deterministic checks on claim text
  ├── DOI pattern (10.xxxx/)  → +0.30
  ├── URL present             → +0.15
  ├── Specific percentage     → +0.10
  ├── Specific year           → +0.05
  ├── Source reference [S#]   → +0.10
  └── Cap at 0.50

report_confidence = Σ(claim_conf × claim_weight) / Σ(claim_weight)

  claim_weight:  load-bearing=1.0  supporting=0.6  contextual=0.3
```

## Data Flow

```
Brave Search API ──→ web_search_brave() ──→ snippets
      │                                        │
      └──→ _brave_fetch_and_store() ──→ research-base/papers/web-*.md
                                              │
                                       build-embeddings.py (cron 03:00)
                                              │
                                       embeddings.json (RAG index)
                                              │
                                       query_papers.py / prepare.py
                                              │
                                       DOSSIER.md ──→ Producer Prompt
```

## File Locations

```
~/.openclaw/workspace/
├── projects/research-pipeline/
│   ├── research_factory.py      # Main pipeline (~2400 LOC)
│   ├── ab_test.py               # A/B model comparison
│   ├── experiment_runner.py     # 50-run controlled experiments
│   ├── measure.py               # 4-level quality measurement
│   ├── prepare.py               # 12-step research prep (1070 LOC)
│   ├── quality_gate.py          # Deterministic QA
│   ├── track_openclaw_ecosystem.py  # Weekly GitHub tracker
│   └── context_package.py       # Agent Context Package
├── research/
│   ├── experiments/
│   │   ├── ab-test/             # GPT-4o vs Sonnet results
│   │   ├── compare-confidence/  # Confidence formula A/B tests
│   │   └── pipeline-optimization/  # Phase 1 experiment runs
│   ├── AR-020-v5-full.md        # Current best report
│   └── AR-020-v5.pdf            # PDF version
├── research-base/
│   ├── llm-trust-calibration/
│   │   ├── papers/              # Stored papers (incl. web-*.md from Brave)
│   │   ├── embeddings.json      # RAG vector index
│   │   └── DOSSIER.md           # Compiled research dossier
│   ├── compounding-research-truths.json  # 27 CRTs
│   └── corrections.json         # 7 corrections
└── memory/knowledge/
    └── openclaw-ecosystem-tracker.json  # Weekly GitHub stats
```

## Empirical Results (19.02.2026)

| Setup | Producer | Evaluator | Formula | Peak Conf | Plateau | Iterations |
|-------|----------|-----------|---------|-----------|---------|------------|
| GPT-4o only | GPT-4o | GPT-4o | Old | 100% (inflated) | — | 2 |
| Sonnet only | Sonnet | Sonnet | Old | 14.6% | — | 1 |
| Hybrid v1 | GPT-4o | Sonnet | Old | 91.8% | — | 1 |
| Hybrid v2 (skeptical) | GPT-4o | Sonnet | Old | 37.8% | 25% | 4 |
| **AgentTrust** | **GPT-4o** | **Sonnet** | **New** | **65.1%** | **35.5%** | **8** |

Key insight: GPT-4o self-evaluates too generously (100%).
Sonnet is a harder evaluator. New formula adds ~10% to plateau via Consistency signal.
