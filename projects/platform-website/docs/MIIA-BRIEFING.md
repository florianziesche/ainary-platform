# Ainary Election Intelligence Platform — Research Briefing

> This document provides context for research agents working on the Ainary election analysis platform. The more precisely you understand what we build, the more relevant your research output will be.

## What We Build

Ainary Ventures operates a **Palantir-grade election intelligence platform** for German municipal elections (Kommunalwahlen). We analyze candidates, predict runoff elections (Stichwahlen), and deliver actionable intelligence to political campaigns, media, and party organizations.

**Live product:** https://ainaryventures.com
**Current scope:** Bayern Kommunalwahl 2026 (March 8, 2026)
**Coverage:** 9 deep city dossiers, 31 cities scouted, 213 municipalities identified

## Architecture

### Three-Level Navigation
1. **Radar** — Overview of all cities with priority scores, election dates, candidate counts
2. **Briefing** — 5-block executive summary per city (Lage, Entwicklungen, Kandidaten, Themen, Szenarien)
3. **Dossier** — Deep intelligence per city with 18 data sections

### ADR-005: One Template, N Datasets
- Single `dossier.html` template renders ALL cities
- City data in `data/cities/{city}.json` (separate from presentation)
- Schema defined in `DATA-SCHEMA.md` (18 sections, exact field names)
- `normalizeCity()` function provides defaults for all fields
- Scale path: JSON files (0-50 cities) → Firebase (50-200) → API (200+)

### Tech Stack
- Static HTML/CSS/JS on Vercel
- Voyage AI embeddings for RAG pipeline (voyage-3-lite for index, voyage-4-large for memory)
- No backend — all intelligence pre-computed in JSON
- Tracking via Upstash Redis

## Data Model (18 Sections per City)

Each city dossier contains:

1. **meta** — City name, state, population, election date, type
2. **kandidaten** — All candidates with: name, party, age, role, profession, properties (array of key-value), social media, sources, image
3. **sentiment** — Topic analysis with direction (positive/negative/neutral) and relevance scores
4. **wahlhistorie** — Historical election results (year, candidates, percentages, turnout)
5. **prognose** — Forecast with probabilities, method description, confidence, gaps
6. **machtanalyse** — Power structure analysis (Stadtrat composition, coalitions, key players)
7. **dempigraphy** — Population structure, age distribution, migration patterns
8. **wirtschaft** — Economic indicators, employment, major employers
9. **infrastruktur** — Key infrastructure projects, urban development
10. **digitalstrategie** — OZG implementation, digital services status
11. **news** — Recent relevant news items with dates, sources, EIJA labels
12. **youtube** — YouTube presence analysis per candidate
13. **patterns** — Cross-city analytical patterns with confidence scores, evidence, soWhat (actionable insight), invalidateIf (conditions that would falsify)
14. **controversies** — Risk signals per candidate (not "Kontroversen" — neutral language) with severity, source, date
15. **scenarios** — Election outcome scenarios with probability, trigger conditions, implications
16. **talkingPoints** — Key campaign talking points per candidate
17. **graph** — Network graph data (nodes + edges for relationship visualization)
18. **quellen** — Source registry with name, URL, type, trust rating

## Analytical Frameworks

### EIJA Trust System
Every claim in the platform is labeled:
- **E** (Evidence) — Documented fact, source available, verifiable
- **I** (Interpretation) — Our reading of data, other readings possible
- **J** (Judgment) — Assessment based on experience, can be wrong
- **A** (Assumption) — Not documented, necessary for analysis

### Composite Risk Score
Auto-calculated per candidate:
```
Risk = Kontroversen (0-30) + Quellenlage (0-10) + Erfahrung (0-15) + Partei-Risiko (0-25)
```

### Stichwahl Probability
Per-city differentiated based on: candidate count, historical patterns, structural analysis. Not copy-paste across cities.

### Palantir Principles Applied
- **Every element clickable** — every data point is an entry point, not an endpoint
- **Three-layer rendering** — DATEN (fact) → INTERPRETATION (so what) → AKTION (what to do)
- **Blueprint exact colors** — #111418, #1C2127, #252A31, #2D72D2, #CD4246, #238551, #C87619
- **Trust System in Command Header** — transparent data coverage score
- **Interactive simulations** — Stichwahl-Simulator with sliders, Scatter-Plot, Wählerfluss-Projektion

## Quality Standards

### Minimum Requirements
- 30+ sources per city (target: 50-60)
- 50-word summaries minimum
- 5+ properties per candidate
- All external claims source-backed
- Q3 Verification Pipeline before any customer/media share (Opus agent verifies all claims with 2-3 web searches)

### Research Protocol (ERF Pipeline)
All research follows: RESEARCH-PROTOCOL.md → ERF-SYSTEM-PROMPT → ERF-TEMPLATES → SYNTHESIS-PROTOCOL → ERF-EVAL-PACK (Score ≥ 80 or retry)

### Memory-R1 Gate
Before storing any knowledge: "Will this change behavior in 30 days?" If no → don't store.

## Pricing & Market

| Segment | Price | Target |
|---------|-------|--------|
| City >50K population | €5,000 | OB candidates, campaign managers |
| City 20-50K | €2,500 | BM candidates |
| City <20K | €990 | Smaller municipalities |
| Party-level (all cities) | €15,000-50,000 | Party HQs, state organizations |

### Competitive Differentiation
- Political consultancies charge €20,000-50,000+ for comparable scope
- We deliver in 48 hours, continuously updatable
- AI-first, scalable (template = product, not custom reports)
- EIJA transparency system (no competitor labels fact vs interpretation)
- 300+ sources across 10+ cities (not per city)

## Current Pipeline (Feb 2026)

### Replies Received (6 of 23 outreach emails)
1. **Jonas Glüsenkamp** — Grünes Bamberg, 3. Bürgermeister
2. **Dr. Florian Freund** — SPD Augsburg, OB-Kandidat
3. **Stadt Fürth** — Pressestelle (Susanne Kramer)
4. **Egon Stamp** — Grüne Friedberg, Stadtrat (had call, offered interview + press article)
5. **Constantin Kaindl** — wirdenkenlokal / deinNämberch.de (media partner)
6. **Dr. Stefan Christoph** — Grüne Regensburg, Stadtrat

### Key Dates
- **March 8, 2026** — Bayern Kommunalwahl (Wahltag)
- **March 9-22, 2026** — Stichwahl window (14-day goldrush for opponent analysis)

## Research Priorities for miia

When conducting research for this platform, prioritize:

1. **Candidate backgrounds** — Professional history, political positions, public statements, social media presence
2. **Election history** — Previous results in the city, turnout trends, party strength over time
3. **Local issues** — Key topics in the city (housing, infrastructure, migration, economy)
4. **Power structures** — Stadtrat composition, coalition dynamics, key alliances
5. **Cross-city patterns** — Structural similarities between cities that predict outcomes
6. **Source verification** — Every claim needs 2+ independent sources. Typical errors: birth years (±5-10 years), professional titles, party positions, election percentages

### What NOT to include
- Private addresses or phone numbers from candidate replies
- Unverified social media rumors
- Percentage bars or fake poll data (legally problematic in Germany)
- Em dashes (—) — use periods, commas, colons instead

## Schema Field Names (CRITICAL)

When producing city JSON data, use EXACTLY these field names:
- `party` not `partei`
- `role` not `rolle`
- `properties` (array of objects) not `steckbrief`
- `name` not `topic` or `label` (for sentiment topics)
- `title` + `body` not `type` + `text` (for social insights)
- `label` not `titel` (for patterns)
- `meaning` not `beschreibung`
- `soWhat` not `ableitung` (for "Für Sie" boxes)
- `invalidateIf` not `invalidation`

---

*Last updated: 2026-02-27. This document is the single source of truth for research agents working on Ainary election intelligence.*
