# Intelligence Architecture — The Template IS the Product

## Core Insight

> "Palantir doesn't sell data. They sell an **ontology** — a model of the world
> that makes data useful. When the ontology improves, every deployment improves."

Our system works the same way. We have ONE template (`dossier.html` + `SCHEMA.json`).
When the template adds a new capability, ALL cities automatically:
1. Get flagged for the gap (auto_enrich.py)
2. Get concrete search queries to fill it
3. Get the new rendering for free (dossier.html already handles it)

**This is why it works: Improvements are multiplicative, not additive.**

## The Stack

```
┌─────────────────────────────────────────────────────────────────┐
│  PRESENTATION LAYER (dossier.html)                              │
│  One template renders ALL cities. Change once → affects all.    │
├─────────────────────────────────────────────────────────────────┤
│  SCHEMA LAYER (SCHEMA.json)                                     │
│  Defines what "complete" means. 11 sections, entity model.      │
│  Change schema → all cities re-validated → gaps queued.         │
├─────────────────────────────────────────────────────────────────┤
│  DATA LAYER (data/cities/*.json)                                │
│  N independent datasets. Each must comply with schema.          │
│  Score tracked over time. Can only improve, never regress.      │
├─────────────────────────────────────────────────────────────────┤
│  INTELLIGENCE LAYER (rag/*.py)                                  │
│  auto_enrich.py — Autonomous gap detection + fill              │
│  enrich_city.py — Delta merge + quality ratchet                │
│  validate_city.py — Pass/fail gate                              │
│  reflect.py — Self-improvement + hypothesis generation          │
│  build_index.py — RAG embedding pipeline                        │
│  query.py — Cross-city semantic search                          │
├─────────────────────────────────────────────────────────────────┤
│  KNOWLEDGE LAYER (learning-journal.json)                        │
│  Compound meta-knowledge: what works, what doesn't,             │
│  which patterns transfer, which hypotheses confirmed.           │
└─────────────────────────────────────────────────────────────────┘
```

## Why Palantir Works — And Why This Does

### 1. Ontology Over Data

**Palantir:** The Foundry Ontology defines objects (people, events, places),
properties (name, role, date), and relationships (works-for, opposes, funds).
Data without ontology is noise. Ontology makes data queryable, comparable, actionable.

**Our system:** `SCHEMA.json` defines entities (candidates, incumbents),
properties (5+ per entity), relationships (connections, graph links),
and meta-properties (trust score, freshness, confidence).

**Why it works:** When we add "themen" to the schema, auto_enrich.py
immediately flags all 4 other cities as non-compliant. The system
*knows what it doesn't know*. That's the foundation of intelligence.

### 2. Feedback Loops (Not Just Data Collection)

**Palantir:** Every analyst interaction feeds back into the model.
Click a link → relationship strengthened. Flag an error → model corrected.
The system doesn't just accumulate data; it accumulates *judgment*.

**Our system:** 
- `reflect.py` generates hypotheses after each run
- `learning-journal.json` records what worked
- Score history tracks improvement over time
- Cross-city patterns transfer tested knowledge

**Why it works:** Run 1 we built Passau in 30 minutes. Run 50 we'll build
a city in 5 minutes — not because we have more data, but because we have
better *strategies* for finding data.

### 3. Cross-Deployment Transfer

**Palantir:** What they learned building intelligence systems for the US Army
transferred to CIA → FBI → NHS → Airbus → BP. Each deployment made the
platform smarter, not just that client's instance.

**Our system:**
- Bamberg taught us: "SPD-Ära ends → CSU-Favorit + progressive splitting"
- Passau confirmed: Same pattern. Now it's a predictive model.
- Next 3 cities: We TEST this hypothesis. If it holds → it's a RULE.

```
City 1 (Bamberg):    Observation    "SPD-OB retires, CSU favorite emerges"
City 2 (Passau):     Confirmation   Same pattern → hypothesis formulated
City 3-5:            Test           Apply hypothesis → predict → validate
City 6+:             Rule           Known pattern → auto-apply to new cities
```

**Why it works:** Knowledge compounds. Each city makes the model better.
The 50th city benefits from everything we learned in the first 49.

### 4. The Template Propagation Mechanism

When we added `themen` and `social` sections to Passau, here's what happened:

```
1. SCHEMA.json updated → themen + social now required
2. auto_enrich.py scanned all cities → 8 CRITICAL gaps detected
3. For each gap → concrete search query generated
4. dossier.html already renders both sections → zero per-city work
5. Agent executes queries → merges results → validates → deploys
```

**The key:** Adding a capability to ONE city creates work for ALL cities.
But the work is **automatically scoped, prioritized, and queryable**.
An agent (or human) just executes the queue top-to-bottom.

### 5. Autonomous Self-Improvement

The system improves itself through three loops:

**Loop 1 — Data Quality (per run)**
```
enrich_city.py --report → see gaps → fill gaps → validate → score↑
```

**Loop 2 — Strategic Learning (per reflection)**
```
reflect.py → generate hypotheses → test next run → confirm/reject → update journal
```

**Loop 3 — Template Evolution (per schema change)**
```
SCHEMA.json change → auto_enrich.py → ALL cities re-validated → queue generated
```

Each loop operates at a different timescale:
- Loop 1: Every enrichment run (minutes)
- Loop 2: Every few runs (hours)
- Loop 3: When we discover a new intelligence dimension (days)

## Current State (2026-02-25)

| Metric | Value |
|--------|-------|
| Cities tracked | 5 (Bamberg, Regensburg, Ottobrunn, Passau, Internal) |
| Schema sections | 11 |
| Total gaps detected | 106 |
| Auto-fillable | 100 (94%) |
| Gold-standard city | Passau (100/100, 11/11 sections) |
| Active hypotheses | 3 (tracked in learning-journal.json) |
| Cross-city patterns | 1 confirmed (Retiring-OB → CSU shift) |

## What Competitors See vs. What We See

**Competitors (static PDF reports):**
- Collected data → formatted → delivered → done
- No feedback loop, no improvement, no cross-client transfer
- Each report is independent work

**Our system:**
- Collected data → structured in ontology → validated → improved next run
- Each city makes every other city better
- Template changes propagate instantly
- Gaps are auto-detected and auto-fillable
- The system tells you what it doesn't know

This is the difference between a consulting deliverable and an intelligence platform.
The deliverable is done when delivered. The platform is never done — it compounds.

## File Inventory

| File | Role | Palantir Equivalent |
|------|------|---------------------|
| `SCHEMA.json` | Master ontology | Foundry Ontology |
| `auto_enrich.py` | Autonomous gap detector | Pipeline Health Monitor |
| `enrich_city.py` | Delta merge + quality gate | Data Pipeline |
| `validate_city.py` | Pass/fail enforcement | Data Quality Rules |
| `reflect.py` | Self-improvement engine | AIP Hypothesis Engine |
| `learning-journal.json` | Compound meta-knowledge | Cross-deployment learnings |
| `build_index.py` | Embedding pipeline | Foundry Transforms |
| `query.py` | Semantic search | AIP Search |
| `dossier.html` | Presentation template | Foundry Workshop App |
| `data/cities/*.json` | City datasets | Foundry Datasets |
| `ENRICHMENT-LOOP.md` | Process documentation | Foundry Documentation |
