# MIA Pipeline — Flowchart (v1.0, 2026-02-19)

```
╔══════════════════════════════════════════════════════════════════════╗
║                        MIA PIPELINE                                 ║
║          Opus = Brain · Sonnet = Worker · Python = Truth            ║
╚══════════════════════════════════════════════════════════════════════╝

┌─────────────────────────────────────────────────────────────────────┐
│ INPUT                                                               │
│                                                                     │
│  Topic ──→ Decision Context                                         │
│  CRTs (27 verified truths)                                          │
│  Corrections (7 past mistakes)                                      │
│  Reference Library (14 papers, DOIs)                                │
│  Vault (631 files, proprietary)                                     │
│  Best Previous Report (AR-020 v5)                                   │
└───────────────────────────┬─────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────────┐
│ PHASE 1: FRAME                                          Opus, 10m  │
│                                                                     │
│  Input:  Topic + CRTs + Corrections + Decisions                     │
│  Task:   Find the REAL question. Decompose into sub-questions.      │
│  Output: Research Brief (JSON)                                      │
│          ├── Real Question (1 sentence)                             │
│          ├── Why Now                                                │
│          ├── 5 Sub-Questions (MECE)                                 │
│          │   ├── SQ-1: question + why + evidence needed             │
│          │   ├── SQ-2: ...                                          │
│          │   ├── SQ-3: ...                                          │
│          │   ├── SQ-4: ...                                          │
│          │   └── SQ-5: ...                                          │
│          └── Brave Search Queries per SQ (2-3 each)                 │
│                                                                     │
│  Risk:   Opus frames wrong question → everything downstream wrong   │
│  Mitigation: CRTs + Corrections constrain framing                   │
└───────────────────────────┬─────────────────────────────────────────┘
                            │
              ┌─────────────┼─────────────┐
              │             │             │
              ▼             ▼             ▼
┌─────────────────────────────────────────────────────────────────────┐
│ PHASE 2a: RESEARCH (parallel)                    Sonnet ×5, 10m    │
│                                                                     │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ │
│  │  SQ-1    │ │  SQ-2    │ │  SQ-3    │ │  SQ-4    │ │  SQ-5    │ │
│  │          │ │          │ │          │ │          │ │          │ │
│  │ Brave ─→ │ │ Brave ─→ │ │ Brave ─→ │ │ Brave ─→ │ │ Brave ─→ │ │
│  │ Fetch ─→ │ │ Fetch ─→ │ │ Fetch ─→ │ │ Fetch ─→ │ │ Fetch ─→ │ │
│  │ Sonnet   │ │ Sonnet   │ │ Sonnet   │ │ Sonnet   │ │ Sonnet   │ │
│  │  ↓       │ │  ↓       │ │  ↓       │ │  ↓       │ │  ↓       │ │
│  │ E/I/J    │ │ E/I/J    │ │ E/I/J    │ │ E/I/J    │ │ E/I/J    │ │
│  │ Findings │ │ Findings │ │ Findings │ │ Findings │ │ Findings │ │
│  │ [S#]     │ │ [S#]     │ │ [S#]     │ │ [S#]     │ │ [S#]     │ │
│  └────┬─────┘ └────┬─────┘ └────┬─────┘ └────┬─────┘ └────┬─────┘ │
│       │            │            │            │            │        │
│       └────────────┴─────┬──────┴────────────┴────────────┘        │
│                          │                                          │
│  Python: Brave API calls + Fetch URLs → papers/web-*.md             │
│                                                                     │
│  Risk:   Sonnet hallucination per SQ (isolated, not propagated)     │
│  Mitigation: Each SQ grounded by Brave results + Reference Library  │
└──────────────────────────┬──────────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────────┐
│ PHASE 2b: EXTRACT + COMPARE + REVIEW                Sonnet, 12m    │
│                                                                     │
│  ┌─────────────────────────────────────────────┐                    │
│  │ CLAIM EXTRACTOR (Sonnet ×5, parallel)       │                    │
│  │ Input:  Each sub-report (text)              │                    │
│  │ Task:   Extract 3 claims VERBATIM           │                    │
│  │ Output: 15 claims with E/I/J + [S#]         │                    │
│  │ Risk:   None (extraction, not generation)   │                    │
│  └─────────────────────┬───────────────────────┘                    │
│                        │                                            │
│  ┌─────────────────────┴───────────────────────┐                    │
│  │ CONTRADICTION FINDER (Sonnet ×1)            │                    │
│  │ Input:  All 5 sub-reports                   │                    │
│  │ Task:   Find claims that contradict each    │                    │
│  │         other across different SQs          │                    │
│  │ Output: Contradiction Register              │                    │
│  │ Risk:   None (comparison, not generation)   │                    │
│  └─────────────────────┬───────────────────────┘                    │
│                        │                                            │
│  ┌─────────────────────┴───────────────────────┐                    │
│  │ REVIEWER (Sonnet ×5, parallel)              │                    │
│  │ Input:  Each sub-report                     │                    │
│  │ Task:   Score evidence/uncertainty/action    │                    │
│  │ Output: 0-6 per sub-report + top issue      │                    │
│  │ Risk:   None (scoring, not generation)      │                    │
│  └─────────────────────┬───────────────────────┘                    │
│                        │                                            │
│  Python: Count E/I/J per report, sources, GOOD/WEAK labels         │
│                                                                     │
└──────────────────────────┬──────────────────────────────────────────┘
                           │
                           │  All data saved as Files:
                           │  ├── sq-01/report.md ... sq-05/report.md
                           │  ├── all-claims.json (15 claims)
                           │  ├── contradictions.json
                           │  ├── sub-reviews.json (5 scores)
                           │  └── sub-validations.json (GOOD/WEAK)
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────────┐
│ PHASE 3: SYNTHESIZE                                  Opus, 10m     │
│                                                                     │
│  Input (alles, 1M Context):                                         │
│  ├── 5 Sub-Reports (from Sonnet)                                    │
│  ├── 15 Extracted Claims (from Sonnet)                              │
│  ├── Contradictions (from Sonnet)                                   │
│  ├── Review Scores (from Sonnet)                                    │
│  ├── GOOD/WEAK Labels (from Python)                                 │
│  ├── CRTs + Corrections (proprietary)                               │
│  ├── Vault Knowledge (proprietary)                                  │
│  ├── Papers (full text)                                             │
│  └── Best Previous Report (AR-020 v5)                               │
│                                                                     │
│  Task: Write A+++ report. V3 narrative + V5 sources.                │
│  ├── Custom Framework (original, drawable)                          │
│  ├── 5-7 Findings (E/I/J/A, Section Confidence, "So What")         │
│  ├── Case Studies (inline, real, sourced)                           │
│  ├── Recommendations (Phased Plan, "Do Not Deploy If")              │
│  ├── Self-Calibrating (applies methods to itself)                   │
│  └── Beipackzettel (AgentTrust format)                              │
│                                                                     │
│  Rules for WEAK sub-reports:                                        │
│  "Use findings only if corroborated by another SQ or CRT"          │
│                                                                     │
│  Risk:   Opus ignores WEAK labels, treats everything as GOOD        │
│  Mitigation: Python validates output in Phase 3.5                   │
└───────────────────────────┬─────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────────┐
│ PHASE 3.5: VALIDATE                                  Python, 5s    │
│                                                                     │
│  ├── Count E/I/J/A distribution in final report                     │
│  │   → E>50%? J<20%? Healthy/Warning/Red Flag                      │
│  ├── Count [S#] references                                          │
│  ├── CRT Cross-Check (does report contradict CRTs?)                 │
│  └── Save validation.json                                           │
│                                                                     │
│  Risk:   None (deterministic)                                       │
└───────────────────────────┬─────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────────┐
│ PHASE 4: ASSETS                                      Opus, 10m     │
│                                                                     │
│  Input:                                                             │
│  ├── Final Report                                                   │
│  ├── Vault Knowledge (for cross-references)                         │
│  └── CRTs (link assets to verified truths)                          │
│                                                                     │
│  Output:                                                            │
│  ├── Atomic Notes (10-15, with "This answers:")                     │
│  ├── Playbooks (2-3, with Trigger/Steps/Failure modes)              │
│  ├── Templates (1-2, copy/paste ready)                              │
│  └── RAG JSON (entities + relations + retrieval hints)              │
│                                                                     │
│  Risk:   Opus invents new facts not in the report                   │
│  Mitigation: Prompt says "NO NEW FACTS beyond the report"           │
└───────────────────────────┬─────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────────┐
│ PHASE 5: QUALITY GATE                                Python, 5s    │
│                                                                     │
│  ├── Rubric score (from report self-assessment)                     │
│  ├── E/I/J/A health check                                          │
│  ├── Beipackzettel completeness                                     │
│  ├── Custom Framework present?                                      │
│  ├── "Do Not Deploy If" present?                                    │
│  │                                                                  │
│  ├── A+++ : ≥15/16, E>50%, J<15%, Framework, Self-Calibrating      │
│  ├── A+   : ≥13/16, E>40%                                          │
│  ├── B    : ≥10/16                                                  │
│  └── C    : <10/16 → REJECT                                        │
│                                                                     │
│  Decision: SHIP / REVISE / REJECT                                   │
│                                                                     │
│  If REVISE:                                                         │
│  └──→ Back to Phase 3 with specific fix requests                    │
│                                                                     │
│  Risk:   None (deterministic)                                       │
└───────────────────────────┬─────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────────┐
│ OUTPUT                                                              │
│                                                                     │
│  final-report.md          ← A+++ Report                             │
│  assets.md                ← Atomic Notes + Playbooks + Templates    │
│  pipeline.json            ← Metadata (timing, models, phases)       │
│  beipackzettel.json       ← AgentTrust-compatible                   │
│  quality-gate.json        ← Grade + Decision                        │
│  all-claims.json          ← 15 claims with E/I/J + Admiralty        │
│  contradictions.json      ← Cross-SQ contradictions                 │
│  sub-validations.json     ← GOOD/WEAK per sub-report               │
│  sub-reviews.json         ← Sonnet review scores                    │
│  validation.json          ← E/I/J/A distribution                    │
│  sq-01/ ... sq-05/        ← Individual sub-research                 │
│  │  ├── prompt.md                                                   │
│  │  └── report.md                                                   │
│  papers/web-*.md          ← Brave-fetched, stored for RAG           │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘


RESOURCE SUMMARY
═══════════════════════════════════════════════════════
 Phase    │ Model    │ Calls │ Time   │ Cost │ Risk
──────────┼──────────┼───────┼────────┼──────┼──────────
 1 Frame  │ Opus     │   1   │ 10 min │ $0   │ Low
 2a Rsrch │ Sonnet   │   5   │ 10 min │ $0   │ Med (grounded)
    Brave │ Python   │  10+  │  30s   │ $0   │ None
 2b Extr. │ Sonnet   │  11   │ 12 min │ $0   │ None (extraction)
    Valid. │ Python   │   -   │   5s   │ $0   │ None
 3 Synth  │ Opus     │   1   │ 10 min │ $0   │ Low
 3.5 Val  │ Python   │   -   │   5s   │ $0   │ None
 4 Assets │ Opus     │   1   │ 10 min │ $0   │ Low
 5 QGate  │ Python   │   -   │   5s   │ $0   │ None
──────────┼──────────┼───────┼────────┼──────┼──────────
 TOTAL    │          │  19   │ ~40min │ $0   │
═══════════════════════════════════════════════════════
```
