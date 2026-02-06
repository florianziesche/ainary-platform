# Stealth Startup Signal Detector

**A deal-sourcing intelligence system that identifies patterns when successful entrepreneurs are about to start something new — BEFORE it becomes public.**

---

## The Core Insight

When a serial entrepreneur is about to start a new company, they leave **digital breadcrumbs** weeks or months before any public announcement. This tool systematically monitors those signals to give you first-mover advantage in deal sourcing.

**The arbitrage:** Most VCs wait for warm intros or public announcements. You can be there *before* the company exists.

---

## Signal Taxonomy

### By Strength

| Level | Description | Examples | Confidence |
|-------|-------------|----------|-----------|
| **Weak** | Suggestive but ambiguous | Following new accounts, minor bio tweaks, liking posts in new sector | 20-40% |
| **Medium** | Clear shift in behavior/focus | Changed title to "Building", new domain registration, conference speaking on new topic | 50-70% |
| **Strong** | Multiple converging signals | Profile change + domain + hiring + GitHub org + unfollowing old company | 75-90% |
| **Confirmed** | Public or semi-public evidence | SEC filing, job postings with company name, blog post announcement | 95-100% |

### By Source Type

| Category | Signal Types | Data Sources |
|----------|--------------|--------------|
| **Social** | Profile changes, bio updates, following patterns, engagement shifts | LinkedIn, Twitter, Instagram |
| **Legal** | Entity formations, trademark filings, patent applications | SEC EDGAR, USPTO, state business registries |
| **Employment** | Job postings, role changes, team departures | LinkedIn Jobs, AngelList, Wellfound, Indeed |
| **Technical** | Domain registrations, GitHub activity, infrastructure setup | WHOIS, GitHub, DNS records |
| **Content** | Blog posts, speaking engagements, newsletter changes | Personal sites, conference agendas, Medium |
| **Network** | Connections with people in new sectors, unfollowing old company | LinkedIn connections, Twitter follows |

### By Timeliness

| Window | Description | Value |
|--------|-------------|-------|
| **3-6 months ahead** | Very early signals (domain, entity, first hires) | 🔥🔥🔥 Highest value |
| **1-3 months ahead** | Medium signals (profile changes, job postings) | 🔥🔥 High value |
| **2-4 weeks ahead** | Late signals (blog posts, speaking) | 🔥 Medium value |
| **<2 weeks** | Confirmation signals (public announcement imminent) | ⚡ Low incremental value |

---

## The Signals (Detailed)

### 1. LinkedIn Profile Changes

**What to monitor:**
- Title changes: "Co-Founder" → "Exploring new opportunities" → "Building something new" → "Stealth"
- Removing current role entirely
- Adding vague titles like "Entrepreneur", "Investor", "Advisor"
- Headline changes to "Open to new opportunities"
- Location changes (SF → NYC, US → Europe)
- Profile activity spikes (posting more, engaging differently)

**Signal strength:** Medium (40-60%)

**Lead time:** 1-4 months

**Detection method:**
- Scrape public profiles weekly
- Compare snapshots for diff detection
- Flag keywords: "stealth", "building", "exploring", "new venture"

---

### 2. Twitter/X Behavior Changes

**What to monitor:**
- Bio changes (similar to LinkedIn)
- Sudden following of people in a new sector (e.g., crypto founder starts following climate tech leaders)
- Engagement pattern shifts (stops engaging with old industry, starts with new)
- Tweet topic analysis (talking about problems in a new space)
- Unfollowing their own company's account
- Following investors/advisors they weren't connected to before
- Posting frequency changes (goes silent, then ramps up)

**Signal strength:** Weak-Medium (30-50%)

**Lead time:** 1-3 months

**Detection method:**
- Monitor following/follower changes via Twitter API
- NLP on recent tweets for topic clustering
- Track engagement patterns over time

---

### 3. Domain Registrations

**What to monitor:**
- New domains registered to known founder's name/email
- Domains registered through privacy services with correlated timing
- Domain patterns (if previous company was "getX.com", look for similar patterns)
- SSL certificate registrations (CT logs)
- DNS configuration changes

**Signal strength:** Strong (70-80%)

**Lead time:** 2-6 months

**Detection method:**
- WHOIS monitoring services
- Certificate Transparency log monitoring
- Reverse WHOIS lookup on known founder emails

---

### 4. Job Postings

**What to monitor:**
- New company name appears on LinkedIn/AngelList/Wellfound
- "Stealth startup" postings by known founders
- Postings with vague company names but founder-linked email domains
- Role types (founding engineer, first designer = very early)
- Job description language clues

**Signal strength:** Strong (75-85%)

**Lead time:** 1-3 months

**Detection method:**
- Scrape job boards daily
- Match email domains to founder watch list
- Flag "stealth" or founder names in postings

---

### 5. AngelList/Wellfound Activity

**What to monitor:**
- New company profiles (even if minimal info)
- Founder creating new company page
- Early team members joining
- Funding status changes

**Signal strength:** Strong (70-80%)

**Lead time:** 1-2 months

**Detection method:**
- Monitor founder profiles for new company links
- Track new company creations with founder tags

---

### 6. GitHub Activity

**What to monitor:**
- Creating a new organization
- Inviting team members to private repos
- Activity spikes on new projects
- Repository naming patterns
- Tech stack signals (Stripe founder using crypto libraries = signal)

**Signal strength:** Medium-Strong (60-75%)

**Lead time:** 1-4 months

**Detection method:**
- GitHub API: monitor user events
- Track org creation, membership changes
- Public repo analysis for topic/tech signals

---

### 7. SEC Filings & Entity Formations

**What to monitor:**
- New Delaware/C-corp formations
- Form D filings (fundraising)
- Trademark applications
- State-level business registrations (DE, CA, WY, NY)

**Signal strength:** Very Strong (85-95%)

**Lead time:** 1-6 months

**Detection method:**
- SEC EDGAR RSS/API
- State business registry APIs
- USPTO trademark monitoring

---

### 8. Patent Filings

**What to monitor:**
- New patent applications by known founders
- Patent topics shifting to new domains
- Provisional patents (earlier signal)

**Signal strength:** Medium (50-65%)

**Lead time:** 3-12 months (patents are slow)

**Detection method:**
- USPTO patent database
- Google Patents monitoring
- PatentScopeAPI

---

### 9. Conference Speaker Bios

**What to monitor:**
- Speaker bio changes from old company to "Founder at [New Co]"
- Speaking at conferences in new sectors
- Panel topics shifting
- Bio says "Building in [space]"

**Signal strength:** Medium (50-60%)

**Lead time:** 1-3 months

**Detection method:**
- Scrape major conference sites (YC Startup School, SaaStr, TechCrunch)
- Track speaker lineup changes
- Archive and diff speaker bios

---

### 10. Blog Posts & Content

**What to monitor:**
- "What I learned building X" (post-exit reflection often precedes new start)
- "What I'm excited about in [new space]"
- Newsletter topic shifts
- Guest posts on new-sector blogs
- Podcast appearances discussing new interests

**Signal strength:** Medium (45-60%)

**Lead time:** 1-4 months

**Detection method:**
- RSS monitoring of founder blogs
- Podcast episode tracking
- Medium/Substack monitoring
- NLP topic analysis

---

### 11. Network Signals

**What to monitor:**
- LinkedIn: New connections with people in a different sector
- LinkedIn: Sudden connections with lawyers, accountants, designers (team building)
- Twitter: Following VCs they weren't following before
- Unfollowing their old company's social accounts (clean break)
- Mutual connection patterns (founder + known co-founder both connect to same designer)

**Signal strength:** Weak-Medium (30-50%)

**Lead time:** 1-3 months

**Detection method:**
- LinkedIn connection scraping (difficult, TOS issues)
- Twitter follow graph monitoring (easier)
- Mutual connection analysis

---

### 12. Email & Communication

**What to monitor (if accessible):**
- New email domain in signature
- Email patterns (if using Gmail plugin approach)
- Calendar invites with investors/advisors

**Signal strength:** Very Strong (80-90%)

**Lead time:** 1-4 months

**Detection method:**
- Gmail plugin (requires user permission)
- Email tracking tools (ethically gray)

---

## Stealth Score Model

### Weighted Scoring (0-100)

```
Stealth Score = Σ (Signal_Weight × Signal_Strength × Time_Decay)

Where:
- Signal_Weight: Importance of signal type (see below)
- Signal_Strength: Confidence in detection (0-1)
- Time_Decay: Recency factor (newer = higher)
```

### Signal Weights

| Signal Type | Weight | Rationale |
|-------------|--------|-----------|
| SEC/Entity Formation | 25 | Definitive legal action |
| Domain Registration | 20 | Clear intent, costs money |
| Job Postings | 20 | Actively hiring = real |
| LinkedIn Title Change | 15 | Public signal of transition |
| GitHub New Org | 10 | Building has started |
| Twitter Bio Change | 5 | Easy to fake, but suggestive |
| Network Shifts | 5 | Weak but additive |

**Score Interpretation:**

| Range | Status | Action |
|-------|--------|--------|
| 0-20 | No signal | Continue monitoring |
| 21-40 | Weak signal | Note for review |
| 41-60 | Medium signal | Research deeper |
| 61-80 | Strong signal | Reach out |
| 81-100 | Confirmed | Immediate action |

### Time Decay Function

```
Time_Factor = 1 / (1 + (days_old / 30))

Fresh signal (1 day old) = 0.97
Week old = 0.81
Month old = 0.50
3 months old = 0.25
```

---

## Example: Retrospective Scoring

### Case: Sam Altman → OpenAI (2015)

**Timeline:**

| Date | Signal | Weight | Strength | Score Contribution |
|------|--------|--------|----------|-------------------|
| Aug 2015 | Leaves YC presidency (blog post) | 15 | 0.9 | 13.5 |
| Aug 2015 | Twitter bio change | 5 | 1.0 | 5.0 |
| Sep 2015 | Seen with Elon at AI conference | 5 | 0.6 | 3.0 |
| Oct 2015 | Domain "openai.org" registered | 20 | 1.0 | 20.0 |
| Oct 2015 | Entity formation (Delaware) | 25 | 1.0 | 25.0 |
| Nov 2015 | Job postings appear | 20 | 1.0 | 20.0 |
| Dec 2015 | Public announcement | — | — | — |

**Stealth Score Progression:**
- Aug 2015: 18.5 (Weak — just left YC)
- Oct 2015: 58.5 (Strong — domain + entity)
- Nov 2015: 86.5 (Confirmed — hiring openly)
- Dec 2015: Public

**Earliest actionable signal:** October 2015 (domain + entity) = **2 months ahead**

---

## Implementation Levels

### Level 1: Manual Monitoring (Free)
- Weekly Google/Twitter searches for watchlist founders
- LinkedIn profile checks
- GitHub manual lookups
- Effort: ~5 hours/week
- Coverage: ~20 founders

### Level 2: Basic Automation (Free tools)
- `monitor.sh` cron script
- RSS feeds for blogs
- GitHub API monitoring
- Effort: Setup 10 hours, then 1 hour/week review
- Coverage: ~100 founders

### Level 3: Full Automation (Paid tools)
- n8n workflow with AI classification
- Paid data sources (PitchBook, Clearbit)
- Telegram/Slack alerts
- Effort: Setup 40 hours, then 30 min/week
- Coverage: ~500 founders

### Level 4: Production System (Serious)
- Custom scraping infrastructure
- Machine learning for pattern detection
- Full data lake with historical tracking
- Effort: 200+ hours, ongoing maintenance
- Coverage: Unlimited

---

## Use Cases

### 1. Early Deal Sourcing
**Goal:** Be the first VC to reach out to a founder starting something new

**Workflow:**
1. Signal detected (Stealth Score > 60)
2. Research: What are they building? (Signals from tech stack, hiring, network)
3. Warm intro via mutual connection
4. Coffee/call: "Saw you're exploring something new. Would love to hear about it."

**Edge:** Most VCs wait for intros or demo day. You're there at incorporation.

---

### 2. Competitive Intelligence
**Goal:** Track founders in your portfolio's competitive space

**Workflow:**
1. Monitor founders who exited from competitors
2. Track if they're starting in the same space again
3. Alert portfolio companies of emerging threats

**Edge:** Forewarned is forearmed. Portfolio can move faster.

---

### 3. Talent Scouting
**Goal:** Identify top operators leaving big companies to start things

**Workflow:**
1. Monitor senior folks at FAANG/unicorns
2. Detect when they "go dark" (leave LinkedIn role, Twitter goes quiet)
3. Reach out for advisory/angel/early check

**Edge:** Best founders don't announce on Twitter. They just leave and start.

---

### 4. Market Mapping
**Goal:** Understand founder flow between sectors

**Workflow:**
1. Track 1000+ founders over 12 months
2. Analyze: Which sectors are hot? (Where are fintech founders going? AI to climate?)
3. Aggregate patterns for thesis development

**Edge:** Founder migration is a leading indicator of where innovation is going.

---

## Ethical Considerations

### ✅ Acceptable:
- Monitoring public profile changes
- Tracking public business registrations
- Analyzing public GitHub activity
- Reading public blog posts and conference bios

### ⚠️ Gray Area:
- Scraping LinkedIn at scale (violates TOS, but everyone does it)
- Domain WHOIS lookups (public but feels invasive)
- Monitoring network connections (creepy but public)

### ❌ Not Acceptable:
- Hacking private accounts
- Impersonating people to get info
- Bribing insiders for tips
- Stalking physical movements

**Guiding principle:** If it's public and you're not deceptive about who you are, it's fair game. If you'd be embarrassed to explain how you found out, don't do it.

---

## Success Metrics

### Leading Indicators
- **Signal detection rate:** % of founders on watchlist with at least one signal/month
- **False positive rate:** Signals that don't lead to a new company
- **Lead time:** Days between first signal and public announcement

### Lagging Indicators
- **Deals sourced:** New companies you reached before they were announced
- **Response rate:** Do founders reply when you reach out?
- **Investment conversion:** Deals sourced → deals done

### Target Benchmarks (Year 1)
- Monitor: 200 founders
- Detect: 20 new companies before public announcement
- Reach out: 15 of those 20
- Meeting: 10 founders
- Investment: 2-3 deals

**If you source ONE unicorn this way, this system paid for itself 1000x.**

---

## Roadmap

### Phase 1: Manual MVP (Week 1-2)
- Create watchlist of 50 founders
- Manual weekly checks
- Document signals in Notion
- Validate signal quality

### Phase 2: Basic Automation (Week 3-4)
- `monitor.sh` for free sources
- n8n workflow for alerts
- Weekly digest email
- Expand to 100 founders

### Phase 3: Scale (Month 2-3)
- Add paid data sources
- Build historical database
- ML for pattern detection
- 200+ founders monitored

### Phase 4: Production (Month 4+)
- Custom scraping infrastructure
- Real-time alerts
- Portfolio integration
- Public API for LPs?

---

## Getting Started

1. **Read this README** (you are here)
2. **Review `signal-sources.md`** — Understand data sources
3. **Load `watchlist-founders.md`** — Pick 20-50 to start
4. **Study `historical-analysis.md`** — Learn from past examples
5. **Run `monitor.sh`** — Start collecting data
6. **Deploy `n8n-workflow.md`** — Automate alerts

**First milestone:** Detect ONE founder starting something new before they announce it publicly. Then reach out and have coffee.

That's the whole game.

---

## Why This Matters

**The VC game is relationship-driven.** The best deals never hit the market. They're pre-empted by investors who were "in the room" early.

**How do you get in the room?** Be there before there *is* a room.

This system makes that possible at scale.

Traditional VC: Wait for intros → React to inbound → Compete in rounds

Stealth Signal Detection: Proactive → Early → Exclusive conversations

**One early catch beats a hundred warm intros.**

---

## Next Steps

Build it. Use it. Refine it.

Then decide: Keep it secret (moat) or share it (brand).

Either way, this is the kind of edge that defines careers.

---

*"The best time to invest in a company is before it exists. The second best time is now."*

---

**Version:** 1.0  
**Last Updated:** 2026-02-06  
**Maintained by:** Ainary Ventures Intelligence Team
