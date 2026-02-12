# AI X-Ray Platform — Project Status & Knowledge Base
*Letzte Aktualisierung: 2026-02-12 03:25 CET*
*Zweck: Alles was Mia braucht um in JEDER Session sofort weiterzuarbeiten*

---

## 🎯 Was ist das?

Eine Plattform die AI-powered strategische Reports generiert. Zwei Produkte:

1. **Corporate X-Ray** — AI Strategy Audit für Unternehmen (McKinsey-Replacement)
2. **Startup X-Ray** — AI Due Diligence für VCs (Associate-Replacement)

**Geschäftsmodell:** Free Tool → Email Capture → Qualified Lead → Consulting/Fund

---

## 📁 Dateistruktur

```
projects/
├── ai-company-xray/          # Corporate X-Ray (GEBAUT ✅)
│   ├── ARCHITECTURE.md        # Technische Architektur
│   ├── GTM-STRATEGY.md        # Go-to-Market Plan
│   ├── PROJECT-STATUS.md      # DIESE DATEI — immer zuerst lesen
│   ├── package.json           # Dependencies: openai, puppeteer
│   ├── xray.js                # Main Orchestrator (5 Phasen)
│   ├── utils.js               # OpenAI Wrapper, slugify, log
│   ├── hyperthink.js          # 3-Round Synthesis (Synthesize → Critique → Finalize)
│   ├── renderer.js            # JSON → HTML (SVG Charts, Platzhalter-Replace)
│   ├── pdf-generator.js       # Puppeteer PDF (Cover, TOC, Header/Footer)
│   ├── template.html          # Dark Mode HTML Template (~1650 Zeilen)
│   ├── index.html             # MOCKUP Version (statisch, erste Version)
│   ├── agents/
│   │   ├── scanner.js         # Company Intelligence Gathering
│   │   ├── industry.js        # Industry Benchmarking
│   │   ├── strategist.js      # McKinsey-Style Strategic Analysis
│   │   ├── financier.js       # Financial Modeling & ROI
│   │   └── provocateur.js     # Contrarian "What McKinsey Won't Say"
│   └── output/
│       ├── siemens-xray.html  # Letzter generierter Report
│       └── siemens-xray.pdf   # Letztes generiertes PDF
│
├── startup-xray/              # Startup X-Ray (IN ARBEIT 🔨)
│   ├── [gleiche Struktur wie corporate]
│   ├── agents/
│   │   ├── scanner.js         # Startup Intelligence + Confidence Scores
│   │   ├── market.js          # TAM/SAM/SOM + Market Timing
│   │   ├── investor.js        # Deal Score + Investment Thesis
│   │   ├── financier.js       # Startup Valuation + Unit Economics
│   │   └── devils-advocate.js # Red Flags + Kill Shots
│   └── template.html          # Purple accent (#8b5cf6) statt Indigo
│
└── ga4-agent-dashboard/       # GA4 Demo (deployed auf GitHub Pages)
    └── index.html
```

---

## 🔧 Technische Details

### Pipeline (Corporate X-Ray)
```
Phase 1: Scanner + Industry (PARALLEL) → ~20-40s
Phase 2: Strategist + Financier + Provocateur (PARALLEL) → ~20-30s  
Phase 3: Hyperthink 3 Rounds (SEQUENTIAL) → ~120-230s
Phase 4: Renderer (JSON → HTML) → instant
Phase 5: PDF Generator (Puppeteer) → ~6s
TOTAL: ~3-5 Minuten
```

### API
- **Model:** GPT-4o (OpenAI)
- **Key:** `process.env.OPENAI_API_KEY` (existiert auf Florians Mac)
- **Kosten pro Report:** ~$0.15-$0.30 (8 API Calls)
- **KEIN Anthropic Key** auf dem System verfügbar

### Hyperthink Schema
Das JSON das Hyperthink Round 3 zurückgibt MUSS diese Felder haben:
```json
{
  "executive_summary": "string (3-4 Absätze)",
  "executive_detail": "string (2-3 Absätze)",
  "ai_readiness": { "overall": N, "data_infrastructure": N, "talent": N, "strategy": N, "culture": N, "percentile": N },
  "readiness_analysis": "string",
  "department_opportunities": [{ "department": "", "current_state": "", "ai_opportunity": "", "estimated_impact": "", "difficulty": "Easy|Medium|Hard" }],
  "department_analysis": "string",
  "competitive_position": { "radar": { "innovation": N, "data_maturity": N, "ai_adoption": N, "talent": N, "investment": N }, "insights": [""] },
  "competitive_narrative": "string",
  "recommendations": [{ "title": "", "why": "", "roi": "", "timeline": "", "difficulty": "Easy|Medium|Hard", "detail": "" }],
  "roadmap": { "phase1": "", "phase2": "", "phase3": "" },
  "roadmap_narrative": "string",
  "risks": [{ "name": "", "likelihood": 1-3, "impact": 1-3, "mitigation": "" }],
  "risk_narrative": "string",
  "provocateur": { "blind_spots": [""], "uncomfortable_truths": [""], "what_mckinsey_wont_say": "", "hidden_risks": [""], "contrarian_bet": "" },
  "critical_questions": [{ "question": "", "why_it_matters": "" }],
  "bottom_line": { "total_opportunity": "", "investment_required": "", "payback_period": "", "summary": "" },
  "bottom_line_detail": "string",
  "sources": { "data_sources": [""], "methodology": "", "limitations": "", "links": [""] }
}
```

### Renderer Platzhalter
Template nutzt `{{variable}}` Syntax. Der Renderer in `renderer.js` macht String-Replace. Wichtige berechnete Platzhalter:
- `{{ai_dasharray_filled}}` / `{{ai_dasharray_empty}}` — SVG Donut Chart (pre-calculated)
- `{{radar_polygon_points}}` — SVG Radar Chart Koordinaten (berechnet aus 5 Scores, cx=100, cy=100, r=75)
- `{{risk_items}}` — SVG Circles für Risk Matrix (likelihood/impact geclampt auf 1-3)
- `{{department_table_rows}}` — Pre-rendered HTML Tabellenzeilen
- `{{critical_questions}}` — Pre-rendered HTML
- `{{sources_section}}` — Pre-rendered HTML
- `{{provocateur_section}}` — Pre-rendered HTML

### Bekannte Bugs & Fixes
| Bug | Status | Fix |
|-----|--------|-----|
| Radar Chart außerhalb ViewBox | ✅ FIXED | cx=100, cy=100, r=75 (war 150,150,120) |
| Risk Matrix Circles außerhalb | ✅ FIXED | Clampe auf 1-3, neue Formel |
| Difficulty CSS Case-Mismatch | ✅ FIXED | Renderer mappt zu lowercase |
| Puppeteer `waitForTimeout` | ✅ FIXED | Replaced mit `setTimeout` Promise |
| Puppeteer SIGKILL | ✅ FIXED | Added `--disable-dev-shm-usage --single-process --no-zygote` |
| Roadmap Streifen | ✅ FIXED | `left: 0; right: 0;` statt 16.666% |
| Apple Emoji in Titles | ✅ FIXED | Replaced mit SVG Icons |

---

## 🎨 Design-System

### Corporate X-Ray
- **Background:** #0a0a0f (fast schwarz)
- **Cards:** #12121a mit Glassmorphism (backdrop-blur, subtle border)
- **Primary Accent:** #6366f1 (Indigo)
- **Secondary Accent:** #10b981 (Emerald)
- **Provocateur:** #ef4444 (Red) + #f97316 (Orange)
- **Font:** Inter (Google Fonts)
- **Icons:** Inline SVG, Heroicons-Style, 24x24

### Startup X-Ray
- **Gleich wie Corporate ABER:**
- **Primary Accent:** #8b5cf6 (Purple) statt Indigo
- **Devil's Advocate:** Gleich wie Provocateur (Red/Orange)
- **Confidence Dots:** ●●●○○ System

### PDF (Print)
- **Background:** White (#ffffff)
- **Text:** #1a1a2e (dark navy)
- **Cards:** #f8f9fa mit #e2e8f0 Border
- **Accent:** #4a5568 (muted grey-blue)
- **Akademisch/Professionell**, nicht bunt
- **Page Breaks:** Jede Section auf eigener Seite

---

## 📊 Florians Feedback (chronologisch)

1. ✅ "Mehr Details wie Provocateur in allen Sections" → Hyperthink Prompts verschärft
2. ✅ "Keine Apple Symbole" → SVG Icons
3. ✅ "Grafiken nicht korrekt" → ViewBox Bugs gefixt
4. ✅ "5 Fragen die du dir noch stellen würdest" → "5 Critical Questions" Section
5. ✅ "Quellenangaben" → "Sources & Methodology" Section
6. ✅ "Download mit Email-Eingabe" → Modal mit Name/Email/Company/Role
7. ✅ "PDF zu farbig, mehr akademisch" → Print CSS komplett überarbeitet
8. 🔨 "Source Links on request" → Noch zu implementieren (Toggle/Accordion)
9. 🔨 "Roadmap Streifen" → CSS gefixt, needs Verify
10. ⏳ "VC Version" → Startup X-Ray wird gebaut
11. ⏳ "News Intelligence Layer" → Noch nicht gestartet

---

## 🚀 GTM Plan (Kurzversion)

**TIMELINE:**
- **Donnerstag 13.02:** Pricing finalisieren
- **Montag 16.02:** LAUNCH 🚀

**Woche 1:** Deploy auf Custom Domain + LinkedIn Post + Substack
**Woche 2:** 5 Consultancies ansprechen + Product Hunt + HN
**Woche 3:** Viral Loop + Weekly Company Spotlights
**Woche 4:** Monetization (Free/Pro $49/Enterprise $499/Custom €5-50K)

**5 Consultancy Targets:** Horváth, MHP, Capgemini Invent DE, Accenture Song DE, Roland Berger

**Revenue Projektion Q1:** ~€67K (konservativ)

Volle Strategie: `GTM-STRATEGY.md`

---

## 🔮 Produkt-Roadmap

| # | Produkt | Status | Aufwand | Priorität |
|---|---------|--------|---------|-----------|
| 1 | Corporate X-Ray | ✅ v2 gebaut | - | DEPLOY |
| 2 | Startup X-Ray | 🔨 wird gebaut | 1 Tag | HIGH |
| 3 | Content X-Ray | ⏳ geplant | 1 Tag | HIGH (Flywheel) |
| 4 | IC Co-Pilot | ⏳ geplant | 2-3 Tage | MEDIUM |
| 5 | Competitor X-Ray | ⏳ geplant | 1 Tag | MEDIUM |
| 6 | News Intelligence | ⏳ geplant | 2 Tage | HIGH (Content Automation) |
| 7 | Live Web-Search (Brave API) | ⏳ | 0.5 Tage | Enhancement |
| 8 | Cloudflare Worker (Web-App) | ⏳ | 1 Tag | Scale |
| 9 | AI Advisory Board | ⏳ geplant | 1-2 Tage | HIGH (proven concept) |
| 10 | Platform Website (alle Tools) | ⏳ geplant | 1 Tag | HIGH (Dach für alles) |

---

## 🧠 Entscheidungen & Kontext

- **OpenAI statt Anthropic:** Kein ANTHROPIC_API_KEY auf dem System. GPT-4o funktioniert gut.
- **CLI statt Web-App:** Schneller zu bauen, bessere Qualität. Web-App kommt als Cloudflare Worker.
- **Puppeteer für PDF:** Volle Kontrolle, Dark Mode bleibt im HTML, Academic Mode im Print.
- **Ehrlichkeit als Feature:** "Weniger Daten aber ehrlich" — Confidence Indicators sind das Alleinstellungsmerkmal.
- **Provocateur/Devil's Advocate:** Die Sektion die NIEMAND sonst hat. McKinsey KANN das nicht, weil der Kunde zahlt.
- **Domain:** Noch zu entscheiden: `xray.florianziesche.com` vs `xray.ainaryventures.com`
- **Branding:** Corporate X-Ray = "Florian Ziesche" (Consulting). Startup X-Ray = kann Ainary sein.

---

## 📋 Nächste Session — Checkliste

Wenn du diese Datei liest, mache ZUERST:

1. [ ] Lies dieses Dokument komplett
2. [ ] Check `output/` — gibt es neue Reports?
3. [ ] Check ob `startup-xray/` existiert und funktioniert
4. [ ] Lies Florians letzte Telegram-Nachrichten
5. [ ] Lies `memory/2026-02-12.md` für Tageskontext
6. [ ] `grep -i "xray\|x-ray" memory/*.md` für historischen Kontext

---

*Aktualisiere dieses Dokument nach JEDER Änderung am System.*
