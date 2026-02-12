# Research Engine 🔬

**Early Warning System for Bleeding-Edge AI/Tech Trends**

Scans 5 sources daily/weekly and generates an Intelligence Brief BEFORE trends go mainstream.

---

## 🚀 Quick Start

### 1. Install Dependencies
```bash
npm install
```

### 2. Set OpenAI API Key
```bash
export OPENAI_API_KEY="sk-..."  # Your actual OpenAI key
```

Or add to `~/.zshrc` (permanent):
```bash
echo 'export OPENAI_API_KEY="sk-..."' >> ~/.zshrc
source ~/.zshrc
```

### 3. Run
```bash
node engine.js                    # Scan all sources, last 2 days
node engine.js --source arxiv     # Only ArXiv
node engine.js --days 7           # Last 7 days
```

### 4. View Report
Opens automatically in browser (macOS). Or open:
```
output/research-YYYY-MM-DD.html
```

---

## 📊 Data Sources

| Source | What It Tracks | Items/Run |
|--------|----------------|-----------|
| **ArXiv** | cs.AI, cs.CL, cs.MA, cs.LG papers | 50-200 |
| **Hacker News** | Top + Show HN (AI/ML filtered) | 30-50 |
| **Reddit** | r/MachineLearning, r/LocalLLaMA, r/artificial | 50-100 |
| **GitHub** | Trending repos | 20-40 |
| **VC Blogs** | a16z, Sequoia, Benchmark, NFX, First Round | 5-15 |

**All sources use public APIs — no auth needed except OpenAI for analysis.**

---

## 📄 Output

### Intelligence Brief Sections:

1. **Emerging Signals** — Top 5 trends appearing NOW
2. **Deep Dives** — Top 3 topics worth investigating
3. **Contrarian Corner** — What everyone is ignoring
4. **Cross-Source Patterns** — Themes appearing in 2+ sources

### Files Generated:
- `output/research-YYYY-MM-DD.html` — Beautiful dark mode report
- `output/research-YYYY-MM-DD.json` — Raw data + analysis (for debugging)

---

## 🎨 Design

- **Dark Mode** by default
- **Emerald accent** (#10b981) — differentiates from other X-Ray products
- **Glassmorphism cards** with SVG icons
- **Signal Strength indicators** (1-5 bars)
- **Source tags** for cross-referencing

---

## 💰 Cost

~$0.05-$0.15 per run (OpenAI GPT-4o analysis only)

**Daily:** ~$3/month  
**Weekly:** ~$0.50/month

---

## 🐛 Known Issues

### RSS Feeds Return 404
**Status:** ⚠️ Needs fixing  
**Fix:** Update feed URLs in `sources/rss.js`

Some VC blogs changed their RSS URLs or disabled feeds. Need to:
1. Find current RSS URLs
2. Or scrape blog pages directly
3. Or use alternative sources

### Rate Limits
- **ArXiv:** Max 1 req/3s (currently safe, but add delays if scaling)
- **Reddit:** User-Agent header prevents most 429s
- **GitHub:** Scraping can be fragile (HTML structure changes)

---

## 📋 TODO

- [ ] Fix RSS feed URLs (a16z, Benchmark, NFX, First Round)
- [ ] Add Twitter source (needs API access)
- [ ] Add Discord source (key servers: Eleuther, LAION, Stability)
- [ ] Email/Telegram delivery
- [ ] Cron job (daily auto-run)
- [ ] Web UI for historical reports

---

## 📚 Architecture

See [PROJECT-STATUS.md](./PROJECT-STATUS.md) for full technical details.

**Pipeline:**
1. **Fetch** — Parallel data collection from 5 sources (~10s)
2. **Analyze** — GPT-4o synthesis (~20-30s)
3. **Render** — JSON → HTML template (instant)
4. **Save + Open** — Write files + open in browser (instant)

**Total runtime:** ~30-40s per report

---

## 🤝 Integration

This is part of a **shared data layer** strategy:

- **blogwatcher** → RSS feeds (future)
- **Content X-Ray** → ArXiv papers (future)
- **IC Co-Pilot** → GitHub repos (future)

Each product makes the data more valuable for all others.

---

Built by **Florian Ziesche** | Part of the X-Ray Platform Suite
