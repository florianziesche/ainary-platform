# Ainary Platform — Architecture Decision Record

**Author:** Mia (Co-Founderin, AI)
**Date:** 2026-02-24
**Status:** ACCEPTED
**Confidence:** 85%

---

## ADR-005: One Template, N Datasets

### Context

We have 4 separate Gotham HTML files (bamberg, regensburg, ottobrunn, internal) that share 95% identical code. Each is ~190KB. Adding a new city means copying an HTML file, changing the data, and deploying. This takes 1-3 hours per city.

We also have digi-dashboard.html with hardcoded Bayern data, and radar.html as an internal sales tool.

At 28 cities this is manageable. At 100 cities it's unmaintainable. At 1000 it's impossible.

### Decision

**Separate data from presentation. One template, N JSON files.**

```
platform-website/
├── ARCHITECTURE.md          ← This file
├── radar-scout.md           ← Intelligence collector spec
│
├── data/
│   ├── radar-data.json      ← Lead pipeline (INTERNAL, all cities)
│   └── cities/
│       ├── bamberg.json     ← Per-city intelligence data
│       ├── regensburg.json
│       ├── ottobrunn.json
│       └── ...              ← New cities added by scout or generator
│
├── radar.html               ← INTERNAL: Sales Intelligence Dashboard
│                               Loads: data/radar-data.json
│                               User: Florian (sales lead management)
│                               Question: "Wen kontaktiere ich heute?"
│
├── dashboard.html            ← CUSTOMER-FACING: City Briefing
│                               Loads: data/cities/{id}.json via ?city=X
│                               User: Bürgermeister-Kandidaten, Wahlkampf-Teams
│                               Question: "Was passiert in meiner Stadt?"
│
├── dossier.html              ← CUSTOMER-FACING: Deep Dossier
│                               Loads: data/cities/{id}.json via ?city=X
│                               User: Same as dashboard, power users
│                               Question: "Alles über diese Person/Entität"
│
├── gotham-bamberg.html       ← LEGACY (redirect to dossier.html?city=bamberg)
├── gotham-regensburg.html    ← LEGACY (redirect)
├── gotham-ottobrunn.html     ← LEGACY (redirect)
├── gotham-internal.html      ← LEGACY (redirect)
└── digi-dashboard.html       ← LEGACY (redirect to dashboard.html)
```

### Principles Applied

#### 1. Separation of Concerns (Google)
- **Data** (JSON) is independent of **Presentation** (HTML/JS)
- Internal tools (radar) ≠ Customer tools (dashboard/dossier)
- Sales pipeline ≠ Customer intelligence
- Mixing these creates confusion, security risk, and maintenance hell

#### 2. Single Source of Truth (Palantir Ontology)
- Each city has ONE JSON file. Not 3 copies across 3 HTML files.
- radar-data.json references cities by ID, not by duplicating data
- Change a fact in bamberg.json → reflected everywhere instantly

#### 3. Progressive Disclosure (Palantir Gotham)
- Level 1 (Radar): "Where are my leads?" → Table with scores
- Level 2 (Dashboard): "What's happening in this city?" → Briefing + KPIs
- Level 3 (Dossier): "Everything about this person" → Deep intelligence
- Each level answers ONE question. Not everything at once.

#### 4. URL-Driven State (Google)
- `dashboard.html?city=bamberg` — no server needed, just URL params
- Bookmarkable, shareable, linkable from emails
- Static hosting (Vercel) = $0/month, instant deploys, global CDN

#### 5. Generate, Don't Handcraft (Palantir)
- kommune-generator.py already produces city data in 30 seconds
- Scout agent (cron) searches for new leads automatically
- Human reviews + approves. Machine does the grunt work.

### Why JSON Files, Not a Database

| Approach | Cost | Complexity | Scale Limit | Our Need |
|----------|------|-----------|------------|----------|
| JSON on Vercel | $0 | Zero | ~1000 files | ✅ Now |
| Firebase | $0-25/mo | Low | 100K | When >100 customers |
| Supabase/Postgres | $25/mo | Medium | Unlimited | When >1000 customers |
| Custom API | $50+/mo | High | Unlimited | Never (probably) |

We're at 28 cities. JSON files on a CDN is the right choice until we have a reason to change. Over-engineering is the #1 startup killer.

### Scaling Path

**Now (0-50 customers):**
- JSON files on Vercel
- Shared password per customer
- Manual: `python generate_kommune_report.py "Stadtname" "BL"` → JSON

**Phase 2 (50-200 customers):**
- Per-customer password (simple auth layer)
- Batch generation: `ainary build --bundesland bayern`
- Scout runs daily, auto-enriches existing cities

**Phase 3 (200+ customers):**
- Firebase Auth (Google SSO for Kommunen)
- API gateway for real-time data
- Customer self-service portal

### Migration Plan

1. ✅ radar-data.json created (28 cities)
2. ✅ radar.html loads JSON dynamically
3. ✅ Extract Gotham data → data/cities/{id}.json (bamberg, regensburg, ottobrunn, internal)
4. ✅ Build dossier.html template (replaces 4 gotham-*.html, loads via ?city=X)
5. ⬜ Build dashboard.html template (replaces digi-dashboard.html)
6. ⬜ Legacy redirects (old URLs still work)
7. ⬜ Kommune-generator outputs to data/cities/
8. ⬜ Scout cron writes to radar-data.json

### Risks

- **Data quality:** Scout may produce low-quality leads → mitigated by score threshold + human review
- **JSON size:** At 1000 cities, radar-data.json becomes large (~500KB) → mitigated by lazy loading
- **No auth:** Shared password is weak → acceptable until paying customers exist
- **Stale data:** No auto-refresh → mitigated by scout + manual updates + expiry dates

### What This Enables

1. **New city in 30 seconds:** `python generate_kommune_report.py "Ingolstadt" "BY"` → live
2. **100 cities in 1 hour:** Batch script + auto-deploy
3. **Auto-expanding pipeline:** Scout finds leads while Florian sleeps
4. **Customer demos:** Send URL `dashboard.html?city=bamberg&pw=demo2026` → instant
5. **Pricing per city:** Each JSON can have custom pricing logic
6. **White-label ready:** Same data, different branding per customer

---

*This document follows Google's ADR format and Palantir's architectural documentation standards.*
*Updated: 2026-02-24 10:10 CET*
