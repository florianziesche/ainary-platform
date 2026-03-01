# AGENTS.md — Platform Website Intelligence System

## ⛔ MANDATORY READ before ANY data change

This file governs ALL work on city dossier data. Read it. Follow it. No exceptions.

---

## Golden Rule

> **FORMAT ≠ QUALITY. Filling empty fields is not enrichment. Verification is.**

A field that says "Kandidat/in" is worse than an empty field — it looks correct but carries zero information. Every data change must make the data MORE CORRECT, not just MORE PRESENT.

---

## Pipeline Order (NON-NEGOTIABLE)

```
1. generate_city.py     → Create initial JSON from research
2. normalize_city.py    → Normalize field names, slugs
3. enrich_template.py   → Fill missing TEMPLATE fields (format only)
4. verify_facts.py      → ⛔ VERIFY content correctness
5. validate_city.py     → Score quality (format + content)
6. DEPLOY               → Only if verify_facts.py returns 0
```

**NEVER skip step 4.** If verify_facts.py returns exit code 1, DO NOT DEPLOY.

Steps 3 and 4 are different:
- Step 3 (enrich) = "Does the JSON have the right keys?" → FORMAT
- Step 4 (verify) = "Is the data correct?" → TRUTH

---

## Directory Structure

```
projects/platform-website/
├── AGENTS.md                    ← YOU ARE HERE. Read first.
├── dossier.html                 ← Frontend template (ONE for all cities)
├── data/
│   ├── cities/*.json            ← City dossier data (50 files)
│   ├── reports/                 ← Verification reports (auto-generated)
│   └── ontology.json            ← Shared ontology definitions
├── rag/
│   ├── cli.py                   ← Unified CLI entry point
│   ├── validate_city.py         ← Quality scoring (format)
│   ├── validate_research.py     ← Research quality check
│   ├── normalize_city.py        ← Field normalization
│   ├── enrich_city.py           ← Research enrichment (web)
│   ├── generate_city.py         ← Initial city generation
│   ├── learning_db.py           ← SQLite learning database
│   └── pipeline/
│       ├── enrich_template.py   ← Template field filling (format)
│       ├── verify_facts.py      ← ⛔ Fact verification (truth)
│       ├── eija_auditor.py      ← Evidence classification
│       ├── backtest.py          ← 2020 election validation
│       ├── sentiment.py         ← NLP sentiment scoring
│       ├── demographics.py      ← Population data
│       ├── graph.py             ← Entity relationship graph
│       ├── contradictions.py    ← Cross-claim contradictions
│       └── knowledge_extractor.py ← Pattern extraction
└── CHANGELOG.md
```

---

## Data Schema: What dossier.html Expects

### Template-Required Fields (enrich_template.py fills these)

| Field | Type | Example | Template Reads |
|-------|------|---------|---------------|
| `tenant.name` | string | "Passau" | Header |
| `tenant.wahl` | string | "08.03.2026" | Countdown |
| `kb[].steckbrief` | `{Partei, Position, Kurzprofil}` | | Dossier tab |
| `kb[].properties` | `[{key, val, ev}]` | `{key:"Alter", val:"45", ev:"E"}` | Profil section |
| `kb[].karriere` | `[{year, label, color}]` | `{year:"2020", label:"CEO"}` | Timeline |
| `kb[].controversies` | `[{title, text, severity, ev_tag, conf}]` | | Risikosignale |
| `kb[].quellen` | `[{name, url, typ}]` | | Quellenverzeichnis |
| `kb[].forecast` | `{min, max}` | `{min:20, max:35}` | Forecast bars |
| `kb[].role` | string containing "andidat" or "ürgermeister" | | Candidate filter |
| `graph.nodes` | `[{id, label, type}]` | | Netzwerk tab |
| `graph.links` | `[{source, target}]` | | Netzwerk tab |
| `topics` | `[{label, count, icon}]` | | Themen sidebar |
| `hypotheses` | `[{label, text, confidence}]` | | Hypothesen sidebar |
| `patterns` | `[{id, label, meaning, confidence, severity}]` | | Patterns section |
| `forecast.kandidaten` | `[{id, name, min, max}]` | | Forecast bars |
| `forecast.stichwahl` | int (0-100) | 85 | Stichwahl % |

### Verification-Required (verify_facts.py checks these)

| Check | Rule | Impact if violated |
|-------|------|--------------------|
| Forecast sum min | ≤ 105% | HOCH — mathematically impossible |
| Forecast sum max | ≤ 130% | HOCH — ranges too wide to be useful |
| Forecast min ≤ max | Always | HOCH — data corruption |
| Age vs birth year | Must match ±1 | HOCH — factual error visible to users |
| Party consistency | Same across all fields | HOCH — undermines credibility |
| Hollow shell score | < 5/10 | MITTEL — entry looks filled but is empty |
| Karriere years | 1950-2026 | MITTEL — implausible |
| News freshness | >50% from 2024+ | MITTEL — stale intelligence |

---

## Before/After Rule

Before running ANY pipeline step that modifies data:

```bash
# 1. Snapshot current state
cp -r data/cities /tmp/cities-backup-$(date +%H%M)

# 2. Run verification BEFORE
python3 -m pipeline.verify_facts --report

# 3. Make changes
python3 -m pipeline.enrich_template

# 4. Run verification AFTER
python3 -m pipeline.verify_facts --report

# 5. Compare
diff <(jq '.summary' /tmp/report-before.json) <(jq '.summary' /tmp/report-after.json)
# HOCH issues must decrease or stay same. NEVER increase.
```

If HOCH issues INCREASE after your change → **REVERT. Your change made it worse.**

---

## Anti-Patterns (things that went wrong before)

### ❌ "Format fix = Done"
Changing `k` to `key` in properties is a format fix. It doesn't make the data more correct. It makes incorrect data render without errors.

### ❌ "0 audit errors = ship it"
Audit checks structure. It doesn't check truth. Regensburg had 205% forecast sum and passed all format checks.

### ❌ "Enricher fills 50/50 = success"
The enricher filled 50 cities with template defaults. 114 candidates got only Partei/Rolle/Status. That's not enrichment — that's wallpaper.

### ❌ "Deploy without browser verification"
Screenshots prove rendering. They don't prove correctness. A perfectly rendered "45 Jahre" is wrong if the person is 52.

### ❌ Running enrich_template.py multiple times
Each run can overwrite previous data with template defaults. The `if True: # Always regenerate` pattern is dangerous — it replaces real data with inferred data.

---

## Deploy Checklist

```
[ ] python3 -m pipeline.verify_facts → exit code 0
[ ] No HOCH issues
[ ] Forecast sums checked (all ≤ 105% min, ≤ 130% max)
[ ] Before/after comparison shows improvement or no change
[ ] At least 1 city spot-checked in browser (all 5 tabs)
[ ] git diff reviewed — no unintended overwrites
```

---

## CLI Quick Reference

```bash
# Full pipeline (all 7 analysis modules)
python3 cli.py full-pipeline

# Enrich template fields (FORMAT only)
python3 -m pipeline.enrich_template

# Verify facts (TRUTH) — run before deploy
python3 -m pipeline.verify_facts
python3 -m pipeline.verify_facts --city passau
python3 -m pipeline.verify_facts --fix          # auto-fix deterministic issues
python3 -m pipeline.verify_facts --report       # save JSON report

# Validate quality score
python3 rag/validate_city.py data/cities/*.json

# Single city
python3 rag/validate_city.py data/cities/passau.json
```
