# Knowledge Extraction System Architecture

> Competitive intelligence pipeline for VC career + blog content creation

## Overview

This system aggregates insights from multiple sources—VC blogs, newsletters, Twitter/X, and Discord communities—and synthesizes them into actionable intelligence stored in Florian's Obsidian vault.

```
┌─────────────────────────────────────────────────────────────────────┐
│                        KNOWLEDGE SOURCES                            │
├─────────────────┬──────────────────┬────────────────┬──────────────┤
│   RSS Feeds     │   Newsletters    │   Twitter/X    │   Discord    │
│   (blogwatcher) │   (via RSS)      │   (bird CLI)   │   (OpenClaw) │
└────────┬────────┴────────┬─────────┴───────┬────────┴──────┬───────┘
         │                 │                 │               │
         ▼                 ▼                 ▼               ▼
┌─────────────────────────────────────────────────────────────────────┐
│                     INGESTION LAYER                                  │
│  • blogwatcher scan (cron/heartbeat)                                │
│  • bird home/search/lists (cron)                                    │
│  • Discord message monitoring (OpenClaw)                            │
└────────────────────────────┬────────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────────┐
│                     PROCESSING LAYER                                 │
│  • AI summarization (Claude via OpenClaw)                           │
│  • Tagging & categorization                                         │
│  • Trend detection                                                  │
│  • Source attribution                                               │
└────────────────────────────┬────────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────────┐
│                      OUTPUT LAYER                                    │
│  Obsidian Vault: ~/Library/Mobile Documents/iCloud~md~obsidian/     │
│                  Documents/System_OS/                                │
├─────────────────────────────────────────────────────────────────────┤
│  /20-Knowledge/                                                     │
│    /VC-Intelligence/                                                │
│      /Weekly-Digests/          ← Weekly synthesis reports           │
│      /Fund-Research/           ← Individual fund deep-dives         │
│      /Trend-Analysis/          ← Emerging patterns & themes         │
│      /People-Notes/            ← Notable VCs & founders             │
│    /AI-Landscape/                                                   │
│      /Model-Updates/           ← AI model releases & capabilities   │
│      /Startup-Tracker/         ← AI companies to watch              │
│  /00-Inbox/                                                         │
│    /Raw-Captures/              ← Unprocessed interesting items      │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Source Categories

### 1. VC Firm Blogs (via RSS/blogwatcher)

**Tier 1 - Major Funds (Daily monitoring)**
| Source | RSS Feed | Focus |
|--------|----------|-------|
| Sequoia Capital | https://sequoiacap.com/feed/ | Company building, market insights |
| Y Combinator | https://www.ycombinator.com/blog/rss/ | Startup advice, batch updates |
| Greylock | https://greylock.com/feed/ | Enterprise, consumer, crypto |
| a16z Future | https://future.com/feed/ | Tech trends (note: stale since 2022) |

**Tier 2 - Other VCs (Weekly check)**
| Source | RSS Feed | Focus |
|--------|----------|-------|
| Tomasz Tunguz | https://tomtunguz.com/index.xml | SaaS metrics, data analysis |

### 2. Substacks & Newsletters (via RSS)

**Must-Read (Daily)**
| Newsletter | RSS Feed | Author | Focus |
|------------|----------|--------|-------|
| Not Boring | https://www.notboring.co/feed | Packy McCormick | Tech optimism, deep dives |
| Lenny's Newsletter | https://www.lennysnewsletter.com/feed | Lenny Rachitsky | Product, growth |
| Stratechery | https://stratechery.com/feed/ | Ben Thompson | Tech strategy |
| Newcomer | https://www.newcomer.co/feed | Eric Newcomer | VC industry news |
| The Generalist | https://www.generalist.com/feed | Mario Gabriele | Company deep dives |

### 3. Twitter/X (via bird CLI)

**Lists to Create & Monitor:**
- `vc-partners` - Top VC partners (a16z, Sequoia, Benchmark partners)
- `ai-founders` - AI startup founders
- `tech-journalists` - Eric Newcomer, Kate Clark, Connie Loizos
- `thought-leaders` - Naval, Sam Altman, etc.

**Search Queries:**
- `"raising" OR "funding" OR "seed round" filter:follows`
- `"AI" "startup" "launch" filter:verified`
- `from:sama OR from:naval OR from:paulg`

### 4. Discord Communities (via OpenClaw)

**Channels to Monitor:**
- OpenClaw Discord (once joined)
- AI-focused servers
- Founder communities

---

## Implementation Plan

### Phase 1: RSS Feeds (Immediate)
1. ✅ `blogwatcher` installed and ready
2. Add all verified RSS feeds
3. Set up daily scan via cron or heartbeat
4. Create Obsidian template for captured articles

### Phase 2: Twitter/X Integration (Requires Setup)
1. Install `bird` CLI (via brew or npm)
2. Configure cookie authentication
3. Create curated lists
4. Set up scheduled timeline pulls

### Phase 3: Processing Pipeline (After Sources Active)
1. Daily digest generation (AI summarization)
2. Weekly trend synthesis
3. Auto-tagging by topic (AI, Fundraising, SaaS, etc.)
4. People mention extraction → link to `/30-People/`

### Phase 4: Discord Monitoring (After Channel Access)
1. Configure OpenClaw Discord integration
2. Set up keyword alerts
3. Weekly community insights digest

---

## Automation Schedule

```
DAILY (via cron or heartbeat)
├── 07:00  blogwatcher scan → new articles
├── 08:00  bird home --following -n 50 → morning feed
├── 12:00  Process morning captures → Obsidian inbox
└── 18:00  bird home --following -n 50 → evening feed

WEEKLY (Sunday evening)
├── Synthesize week's captures into digest
├── Update trend analysis
├── Archive processed inbox items
└── Review/prune RSS feeds
```

---

## Obsidian Integration

### Folder Structure (to create)
```
System_OS/
├── 20-Knowledge/
│   ├── VC-Intelligence/
│   │   ├── Weekly-Digests/
│   │   │   └── 2026-W05-Digest.md
│   │   ├── Fund-Research/
│   │   │   └── Sequoia-Notes.md
│   │   └── Trend-Analysis/
│   │       └── AI-Infrastructure-Q1-2026.md
│   └── AI-Landscape/
│       ├── Model-Updates/
│       └── Startup-Tracker/
└── 00-Inbox/
    └── Raw-Captures/
        └── 2026-02-01-captures.md
```

### Article Template
```markdown
---
source: {{source}}
url: {{url}}
author: {{author}}
captured: {{date}}
tags: [vc-intel, {{topic}}]
status: unprocessed
---

# {{title}}

## Summary
{{AI-generated summary}}

## Key Takeaways
- 
- 
- 

## Relevant For
- [ ] Blog post idea
- [ ] Fund research
- [ ] Trend tracking

## Raw Content
{{excerpt or link}}
```

---

## Tools Summary

| Tool | Purpose | Status |
|------|---------|--------|
| `blogwatcher` | RSS/Atom feed monitoring | ✅ Installed |
| `bird` | Twitter/X CLI | ⬜ Needs install + auth |
| Discord (OpenClaw) | Discord monitoring | ⬜ Needs channel config |
| Claude (OpenClaw) | Summarization & synthesis | ✅ Available |
| Obsidian | Knowledge storage | ✅ Vault configured |

---

## Success Metrics

**Weekly:**
- 50+ articles captured and categorized
- 1 weekly digest generated
- 3+ blog post ideas identified

**Monthly:**
- 2+ deep-dive fund research notes
- 1 trend analysis piece
- Growing network of linked notes in Obsidian

---

## Next Steps

See `setup-guide.md` for step-by-step implementation instructions.

---

*Architecture v1.0 - Created 2026-02-01*
