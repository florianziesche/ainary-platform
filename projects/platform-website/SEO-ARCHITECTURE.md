# SEO & Site Architecture — Pre-Build Research

---

## SEO-Architektur: Pillar + Cluster Model

Die beste Architektur für ein AI Tools SaaS ist **Topic Clusters mit Pillar Pages**:

```
PILLAR PAGES (Hauptseiten, in Nav):
├── /tools/corporate-xray     — "AI Company Analysis"
├── /tools/startup-xray       — "AI Startup Due Diligence"  
├── /tools/advisory-board     — "AI Strategy Advisor"
├── /daily                    — "Daily AI Intelligence Brief"
└── /blog                     — Blog Hub

CLUSTER PAGES (SEO-Inhalte, verlinkt von Pillars):
├── /blog/ai-agents-credit-cards
├── /blog/manufacturing-ai-blind-spot
├── /blog/5-ai-tools-48-hours
├── /blog/what-is-ai-strategy-audit
├── /blog/how-to-evaluate-startup-with-ai
├── /blog/ai-consulting-for-manufacturing
├── /daily/2026-02-12           — Archiv
├── /daily/2026-02-13
└── ...
```

**Regel:** Jede Pillar Page verlinkt auf 5-10 Cluster Pages. Jede Cluster Page verlinkt zurück zur Pillar. Das baut "Topical Authority" bei Google.

---

## URL-Struktur (SEO-optimiert)

```
/                           — Home (Landing)
/tools                      — Tool Overview
/tools/corporate-xray       — Pillar: Corporate X-Ray
/tools/startup-xray         — Pillar: Startup X-Ray
/tools/advisory-board       — Pillar: Advisory Board (Chat UI)
/daily                      — Daily AI Brief (Latest)
/daily/2026-02-12           — Archiv-Eintrag
/daily/archive              — Alle Daily Briefs
/blog                       — Blog Hub
/blog/[slug]                — Einzelner Artikel
/pricing                    — Pricing
/about                      — Über Florian Ziesche
```

**Keine:** /page1, /tool-3, /post?id=123. Clean slugs, keywords in URL.

---

## Target Keywords (Hypothesen — validieren mit Ahrefs/Semrush)

### Primary (Tool Pages):
| Keyword | Intent | Zielseite |
|---------|--------|-----------|
| "AI company analysis" | Transactional | /tools/corporate-xray |
| "AI strategy audit" | Transactional | /tools/corporate-xray |
| "AI startup due diligence" | Transactional | /tools/startup-xray |
| "AI advisory board" | Informational | /tools/advisory-board |
| "free AI company report" | Transactional | /tools/corporate-xray |

### Secondary (Blog/Content):
| Keyword | Intent | Zielseite |
|---------|--------|-----------|
| "AI consulting for manufacturing" | Informational | /blog/manufacturing-* |
| "AI agents commerce" | Informational | /blog/ai-agents-credit-cards |
| "AI tools for business strategy" | Informational | /blog |
| "daily AI news" | Navigational | /daily |
| "AI trend report" | Informational | /daily |

### Long-tail (Daily Brief):
| Keyword | Zielseite |
|---------|-----------|
| "AI news today [date]" | /daily/YYYY-MM-DD |
| "latest AI research papers" | /daily |
| "AI trend analysis weekly" | /daily/archive |

---

## Technical SEO Checklist

### Must-have vor Launch:
- [ ] **Semantic HTML:** h1 > h2 > h3 Hierarchie pro Seite
- [ ] **Meta Tags:** Unique title + description pro Seite
- [ ] **OG Tags:** Open Graph für Social Sharing (Bild + Titel + Description)
- [ ] **Canonical URLs:** Vermeidet Duplicate Content (Substack cross-posts!)
- [ ] **Sitemap.xml:** Automatisch generiert
- [ ] **robots.txt:** Allow all, disallow /output/ (generierte Reports)
- [ ] **Schema.org Markup:**
  - Article (Blog Posts)
  - SoftwareApplication (Tools)
  - FAQPage (Pricing)
  - Organization (About)
- [ ] **Performance:** <3s Load Time, Core Web Vitals grün
- [ ] **Mobile-First:** Responsive, touch-friendly
- [ ] **Internal Linking:** Jede Seite 3-5 interne Links

### Nice-to-have:
- [ ] **Breadcrumbs** (Schema + Visual)
- [ ] **Table of Contents** in Blog Posts (Jump Links)
- [ ] **FAQ Schema** auf Tool Pages
- [ ] **Hreflang** wenn DE + EN Versionen kommen

---

## SEA (Paid Search) Strategie

### Phase 1: Nicht starten mit Paid
- Erst organischen Content aufbauen (4-6 Wochen)
- Daily Brief + Blog = kostenloser Traffic-Test
- Validiert welche Keywords konvertieren BEVOR wir Geld ausgeben

### Phase 2: Targeted Ads (nach 50+ Daily Brief Posts)
- **Google Ads:** "AI company analysis free" → /tools/corporate-xray
- **LinkedIn Ads:** Targeting C-Suite + Strategy → Advisory Board
- Budget: $10-20/Tag max zum Testen
- Metric: Cost per Email Capture

### Phase 3: Retargeting
- Pixel auf allen Seiten
- Retarget: Besucher die Tool benutzt aber nicht Email gegeben haben
- Platform: LinkedIn (B2B) > Google Display > Meta

---

## Wettbewerb

| Competitor | Was sie machen | Unser Edge |
|-----------|----------------|------------|
| **Competely.ai** | AI Competitive Analysis | Wir machen STRATEGY, nicht nur Competitor Comparison |
| **GAI Insights** | Newsletter + Consulting | Wir haben Self-Service TOOLS + automatisierten Content |
| **Perplexity** | General AI Search | Wir sind SPEZIALISIERT auf Business Strategy |
| **ChatGPT/Claude** | General Chat | Wir liefern STRUCTURED Reports mit Sources |
| **McKinsey/BCG** | Full Consulting | Wir kosten $0-49 statt $200K+ |

**Positioning:** "Consultant-grade AI strategy tools. Free to start. No consultants required."

---

## Content Flywheel (SEO-optimiert)

```
Research Engine (daily)
    ↓
Daily AI Brief (/daily/YYYY-MM-DD)
    ↓ pick best topics
Blog Article (/blog/[slug])
    ↓ link to tools
Tool Page CTA ("Try X-Ray on this company")
    ↓
Email Capture
    ↓
Newsletter (weekly, best of Daily + Blog)
    ↓
Repeat — jeder Cycle stärkt SEO Authority
```

---

## Font-Empfehlung

Inter ist gut aber generic. Für Premium-Differenzierung:

**Option 1:** Inter Display (Headlines) + Inter (Body) + JetBrains Mono (Data)
- Safe, proven, was wir haben

**Option 2:** Geist (Headlines, von Vercel) + Inter (Body) + Geist Mono (Data)
- Modern, tech-credible, differenziert

**Option 3:** Instrument Serif (Headlines) + Inter (Body) + JetBrains Mono (Data)
- Editorial, sophisticated, Anthropic-Vibe

**Mein Vote:** Option 2 (Geist) — modern, tech, differenziert von der Masse, trotzdem lesbar. Vercel benutzt es, Linear-Vibe.

---

*Diese Analyse muss VOR dem Build stehen. Jede Seite wird mit SEO-Architektur geplant.*
