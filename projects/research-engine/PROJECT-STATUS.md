# Research Engine — Project Status & Knowledge Base
*Letzte Aktualisierung: 2026-02-12 09:20 CET*
*Zweck: Single Source of Truth für Research Engine — Early Warning System für AI/Tech Trends*

---

## 🎯 Was ist das?

Ein **Frühwarnsystem für bleeding-edge AI/Tech Ideen** — scannt 5 Quellen täglich/wöchentlich und generiert einen Intelligence Brief BEVOR Trends Mainstream werden.

**Ziel:** Florian (und später andere) sehen neue Signale bevor sie in VentureBeat/TechCrunch landen.

---

## 📁 Dateistruktur

```
projects/research-engine/
├── PROJECT-STATUS.md      # DIESE DATEI — immer zuerst lesen
├── package.json           # Dependencies: openai, axios, cheerio, rss-parser, xml2js
├── engine.js              # Main Orchestrator (4 Phasen)
├── analyzer.js            # GPT-4o Synthesis
├── renderer.js            # JSON → HTML Renderer
├── template.html          # Dark Mode HTML Template (Emerald Accent)
├── sources/
│   ├── arxiv.js           # ArXiv Atom Feed (cs.AI, cs.CL, cs.MA, cs.LG)
│   ├── hackernews.js      # HN Firebase API (Top + Show HN, AI/ML filtered)
│   ├── reddit.js          # Reddit JSON API (r/MachineLearning, r/LocalLLaMA, r/artificial)
│   ├── github.js          # GitHub Trending Scraper (Cheerio)
│   └── rss.js             # VC Blogs RSS (a16z, Sequoia, Benchmark, NFX, First Round)
└── output/
    ├── research-YYYY-MM-DD.html
    └── research-YYYY-MM-DD.json
```

---

## 🔧 Technische Details

### Pipeline (4 Phasen)
```
Phase 1: Fetch Data (ALL sources in PARALLEL) → ~5-10s
Phase 2: AI Analysis (GPT-4o Synthesis) → ~15-30s
Phase 3: Render HTML (JSON → Template) → instant
Phase 4: Save + Open → instant
TOTAL: ~20-40s
```

### Data Sources (No Auth Needed!)
| Source | API/Method | Categories | Items/Run |
|--------|-----------|------------|-----------|
| **ArXiv** | Atom Feed | cs.AI, cs.CL, cs.MA, cs.LG | ~20-50 papers |
| **Hacker News** | Firebase API | Top + Show HN (AI/ML keywords) | ~20-30 stories |
| **Reddit** | JSON API | r/MachineLearning, r/LocalLLaMA, r/artificial | ~20-30 posts |
| **GitHub** | HTML Scraping | Trending (daily/weekly) | ~15-20 repos |
| **VC Blogs** | RSS Feeds | a16z, Sequoia, Benchmark, NFX, First Round | ~5-15 posts |

### API Requirements
- **OpenAI Key:** `process.env.OPENAI_API_KEY` (GPT-4o for analysis)
- **No other keys needed** — All sources use public APIs or scraping

### CLI Usage
```bash
node engine.js                    # Scan all sources, last 2 days
node engine.js --source arxiv     # Only ArXiv
node engine.js --days 7           # Last 7 days
npm start                         # Alias for node engine.js
npm test                          # Alias for --days=2
```

### Output Format
- **HTML:** `output/research-YYYY-MM-DD.html` (Dark Mode, opens in browser)
- **JSON:** `output/research-YYYY-MM-DD.json` (Raw data + analysis for debugging)

---

## 📊 Analysis Sections

GPT-4o creates 4 key sections:

1. **Top 5 "Emerging Signals"**
   - What's appearing NOW that most people haven't noticed
   - Signal Strength indicator (1-5)
   - Sources where it appeared

2. **Top 3 "Deep Dives"**
   - Technical breakthroughs worth investigating
   - Products/companies gaining momentum
   - Contrarian takes that might be right

3. **"Contrarian Corner"**
   - What everyone is IGNORING that could matter
   - Unpopular opinions with strong reasoning
   - Risks/limitations nobody talks about

4. **Cross-Source Patterns**
   - Themes appearing in 2+ sources
   - Academic research → startup application
   - VC interest matching GitHub activity

---

## 🎨 Design-System

### Colors
- **Background:** #0a0a0f (almost black)
- **Cards:** #12121a (dark grey with Glassmorphism)
- **Primary Accent:** #10b981 (Emerald) ← **DIFFERENTIATOR**
- **Secondary Accent:** #14b8a6 (Teal)
- **Contrarian:** #ef4444 (Red) + #f97316 (Orange)
- **Font:** Inter (Google Fonts)

### Why Emerald?
- Corporate X-Ray: Indigo (#6366f1)
- Startup X-Ray: Purple (#8b5cf6)
- Advisory Board: Gold (#f59e0b)
- **Research Engine: Emerald (#10b981)** ← Unique identity

### UI Components
- **Signal Strength Bar:** 5 vertical bars (like volume indicator)
- **Source Tags:** Pill-shaped tags (arxiv, reddit, github, etc.)
- **Glassmorphism Cards:** Subtle backdrop-blur + border
- **SVG Icons:** Heroicons-style, 24x24 or 32x32

---

## 🧠 Entscheidungen & Kontext

**Warum diese Quellen?**
- ArXiv = Academic bleeding edge (papers publish before peer review)
- Hacker News = Builder community (what hackers care about)
- Reddit = Early adopter community (LocalLLaMA catches OSS trends FAST)
- GitHub = Code speaks louder (trending repos = real traction)
- VC Blogs = Strategic money moving (what VCs write → what they fund)

**Warum NICHT Twitter/Discord/Substack (v1)?**
- Twitter: Needs auth + rate limits + noise-to-signal ratio low
- Discord: Hard to scrape + needs auth per server
- Substack: Individual newsletter RSS — too fragmented for v1

**Roadmap for v2:**
- Twitter via API (if Florian pays for API access)
- Key Discord servers (Eleuther, LAION, Stability) via webhooks
- Curated Substack list (50-100 key writers)

**Shared Data Layer:**
- RSS feeds shared with blogwatcher (future integration)
- ArXiv papers feed Content X-Ray (future product)
- GitHub repos feed IC Co-Pilot (future product)
→ **Compound moat:** Each product makes the data more valuable

**Update Frequency (Recommendation):**
- **Daily:** For fast-moving topics (AI research, OSS releases)
- **Weekly:** For strategic analysis (combine 7 days → bigger patterns)
- **Monthly:** For long-term trend tracking

---

## 📋 Nächste Session — Checkliste

Wenn du diese Datei liest, mache ZUERST:

1. [ ] Lies dieses Dokument komplett
2. [ ] Check `output/` — gibt es neue Reports?
3. [ ] Lies Florians letzte Telegram-Nachrichten für Feedback
4. [ ] Lies `memory/2026-02-12.md` für Tageskontext
5. [ ] `grep -i "research\|engine" memory/*.md` für historischen Kontext

---

## 🚀 Roadmap

| # | Feature | Status | Aufwand | Priorität |
|---|---------|--------|---------|-----------|
| 1 | Core v1 (5 sources) | ✅ GEBAUT | - | DONE |
| 2 | Test-Run + Deploy | 🔨 IN ARBEIT | 10 Min | NOW |
| 3 | Email/Telegram Delivery | ⏳ geplant | 1-2h | HIGH |
| 4 | Twitter Source | ⏳ geplant | 2h | MEDIUM |
| 5 | Discord Source | ⏳ geplant | 3h | MEDIUM |
| 6 | Cron Job (daily run) | ⏳ geplant | 30 Min | HIGH |
| 7 | Web UI (historical reports) | ⏳ geplant | 1 Tag | LOW |
| 8 | Shared DB with blogwatcher | ⏳ geplant | 2-3h | MEDIUM |

---

## 🐛 Known Issues

| Issue | Status | Notes |
|-------|--------|-------|
| ArXiv rate limit | ⚠️  POSSIBLE | Max 1 req/3s — implemented delay between categories |
| GitHub scraping fragile | ⚠️  POSSIBLE | HTML structure can change — backup: GitHub API |
| Reddit rate limit | ⚠️  POSSIBLE | User-Agent header should prevent 429s |
| OpenAI timeout | ⚠️  POSSIBLE | Large prompts (>100 items) might timeout → batch if needed |

---

## 📊 Cost Estimation

**Per Run:**
- ArXiv: Free
- Hacker News: Free
- Reddit: Free
- GitHub: Free
- RSS: Free
- **OpenAI (GPT-4o):** ~$0.05-$0.15 per analysis (1 API call, ~3K tokens)

**Daily Run:** ~$0.10/day = ~$3/month
**Weekly Run:** ~$0.10/week = ~$0.50/month

**Conclusion:** Dirt cheap.

---

*Aktualisiere dieses Dokument nach JEDER Änderung am System.*
