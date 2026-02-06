# Signal Sources: Deep Dive

**A comprehensive catalog of data sources for detecting stealth startup signals, with access methods, costs, and limitations.**

---

## Table of Contents

1. [Free Public Sources](#free-public-sources)
2. [Paid Data Providers](#paid-data-providers)
3. [Creative/Alternative Sources](#creativealternative-sources)
4. [Technical Infrastructure](#technical-infrastructure)
5. [API Reference](#api-reference)
6. [Cost Analysis](#cost-analysis)

---

## Free Public Sources

### 1. LinkedIn (Public Profiles)

**What you can access:**
- Public profile information (name, title, company, location, bio)
- Connection count (not full list without login)
- Recent activity posts (limited without login)
- Profile changes (via scraping/archiving)

**Access methods:**

**A. Public Profile URLs (No auth required)**
```
https://www.linkedin.com/in/[username]
```
- Can scrape with curl/puppeteer
- Rate limit: ~50-100 requests/hour before soft-block
- Requires user-agent rotation
- Use residential proxies to avoid blocks

**B. LinkedIn API (Official)**
- **Status:** Heavily restricted since 2019
- **Access:** Requires partnership approval (nearly impossible)
- **Reality:** Not viable for most users

**C. Scraping with Puppeteer/Playwright**
```javascript
// Headless browser approach
const page = await browser.newPage();
await page.goto(`https://linkedin.com/in/${username}`);
const title = await page.$eval('.top-card-layout__title', el => el.textContent);
```
- Requires cookie/session management
- Can detect: title changes, company changes, bio updates
- Store snapshots in DB, compare weekly

**D. Third-party scrapers**
- **Bright Data (formerly Luminati):** $500-2000/month
- **ScraperAPI:** $49-250/month
- **Apify LinkedIn scrapers:** $49+/month

**Rate limits:**
- Public scraping: ~100 profiles/hour safely
- With proxies: 500+/hour
- With Bright Data: 10,000+/hour

**Limitations:**
- No access to connection lists (need login)
- Limited activity feed visibility
- Frequent HTML structure changes
- Risk of IP blocks

**Best for:**
- Title/company change detection
- Bio monitoring for keywords ("stealth", "building")

**Cost:** Free (DIY) to $500+/month (commercial scrapers)

---

### 2. Twitter/X (Public API & Scraping)

**What you can access:**
- Public profile bios
- Tweet history
- Following/follower lists (with limits)
- Engagement metrics (likes, retweets, replies)

**Access methods:**

**A. Twitter API v2 (Official)**

**Free Tier:**
- 500,000 tweets/month read
- 1,500 tweets/month write
- Good enough for 100-200 founders

**Basic ($100/month):**
- 10M tweets read/month
- 50,000 tweets write/month
- Full archive search

**API endpoints:**
```bash
# Get user by username
GET https://api.twitter.com/2/users/by/username/:username
# Includes: bio, location, created_at, profile_image

# Get user's recent tweets
GET https://api.twitter.com/2/users/:id/tweets
# Max 100 tweets per request

# Get following list
GET https://api.twitter.com/2/users/:id/following
# Max 1000 per request, paginated
```

**B. Nitter (Twitter scraper frontend)**
```
https://nitter.net/[username]
```
- Free, no API key needed
- Can scrape with curl
- Less stable (dependent on Nitter instance availability)

**C. Tweet Capture via RSS**
- Use services like `nitter.net/[user]/rss`
- Monitor with RSS reader
- Detect new tweets, bio changes

**Rate limits:**
- API Free: 50 requests/15 min per user endpoint
- API Basic: 300 requests/15 min
- Scraping: Variable, use proxies

**Detection capabilities:**
- **Bio changes:** Compare weekly snapshots
- **Following analysis:** Track new follows in sectors (e.g., starts following climate VCs)
- **Tweet topics:** NLP to detect interest shifts
- **Engagement patterns:** Who they're replying to, RTing

**Best for:**
- Real-time bio monitoring
- Following graph analysis
- Behavioral pattern detection

**Cost:** Free (500k tweets/month) to $100/month (10M tweets)

---

### 3. GitHub (Public API)

**What you can access:**
- Public repositories
- User activity (commits, PRs, stars)
- Organization memberships
- New org creation
- Repository topics/languages

**Access methods:**

**A. GitHub REST API**

**Authentication:**
- No auth: 60 requests/hour
- Personal access token: 5,000 requests/hour (FREE)
- GitHub App: 15,000 requests/hour

**Key endpoints:**
```bash
# Get user events (public activity)
GET https://api.github.com/users/:username/events

# Get user organizations
GET https://api.github.com/users/:username/orgs

# Get user repos
GET https://api.github.com/users/:username/repos
```

**B. GitHub GraphQL API**
- More efficient for complex queries
- Same rate limits as REST
- Can batch queries

**Example detection:**
```bash
# Check for new orgs weekly
curl -H "Authorization: token $GITHUB_TOKEN" \
  https://api.github.com/users/username/orgs \
  | jq '.[] | {login, created_at}'
```

**Signals to track:**
- **New organization created** (Strong signal)
- **Invited to private org** (visible if org is later public)
- **Activity spike on new repo**
- **Tech stack changes** (e.g., crypto founder starts Rust repos)

**Rate limits:**
- 5,000 requests/hour with token (free)
- GraphQL: 5,000 points/hour (complex queries cost more points)

**Best for:**
- Tracking technical founders
- Detecting "something is being built"
- Tech stack signals

**Cost:** Free (5k requests/hour is plenty)

---

### 4. SEC EDGAR (US Company Filings)

**What you can access:**
- Form D filings (fundraising notifications)
- S-1 filings (IPO registrations)
- Entity formations (indirect via filings)
- Beneficial ownership reports

**Access methods:**

**A. EDGAR Search (Web)**
```
https://www.sec.gov/edgar/search/
```
- Can search by name, CIK, filing type
- Free, unlimited

**B. EDGAR RSS Feeds**
```
https://www.sec.gov/cgi-bin/browse-edgar?action=getcurrent&type=D&output=atom
```
- Real-time Form D filings
- Can monitor via RSS reader or script

**C. EDGAR API (Unofficial)**
```bash
# Search filings by CIK or name
curl "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&company=Acme&type=D&output=xml"
```

**D. sec-api.io (Paid, structured)**
- $49-249/month
- JSON API, historical search
- Real-time streams

**Signals:**
- **Form D filing:** Company raised money (STRONG signal, but late)
- **Entity in founder's name:** Check for CIK registrations

**Rate limits:**
- SEC.gov: 10 requests/second (very generous)
- No authentication needed

**Best for:**
- Confirmed funding events
- Legal entity tracking

**Cost:** Free (SEC.gov) or $49+/month (sec-api.io)

---

### 5. USPTO (Patent & Trademark Filings)

**What you can access:**
- Patent applications
- Trademark applications
- Assignee/inventor information

**Access methods:**

**A. USPTO Patent Search**
```
https://ppubs.uspto.gov/pubwebapp/
```
- Free, public database
- Search by inventor name, assignee

**B. Google Patents**
```
https://patents.google.com/
```
- Better search UX than USPTO
- Can filter by inventor, date, status

**C. USPTO Trademark Search (TESS)**
```
https://tmsearch.uspto.gov/
```
- Search by owner name
- Shows pending and registered marks

**D. Patent APIs**
- **PatentsView API:** Free, bulk data
- **EPO OPS API:** Free for European patents

**Signals:**
- **New patent by known founder** (Medium signal, 6-12 month lead time)
- **Trademark application** (Strong signal, 1-3 month lead)

**Rate limits:**
- USPTO: No official limit, but slow
- Google Patents: No API, scrape-friendly

**Best for:**
- Long lead time signals (patents)
- Brand/company name detection (trademarks)

**Cost:** Free

---

### 6. State Business Registrations

**What you can access:**
- New LLC/Corp formations
- Registered agents
- Filing dates
- Business addresses

**Access methods:**

**A. Delaware Division of Corporations**
```
https://icis.corp.delaware.gov/Ecorp/EntitySearch/NameSearch.aspx
```
- Free entity search
- Can search by entity name or file number
- No API, must scrape

**B. California Secretary of State**
```
https://bizfileonline.sos.ca.gov/search/business
```
- Free business entity search
- JSON responses (unofficial API)

**C. Wyoming Secretary of State**
```
https://wyobiz.wyo.gov/Business/FilingSearch.aspx
```
- Free search
- Popular for crypto/DAOs

**D. OpenCorporates (Aggregator)**
```
https://opencorporates.com/
```
- **Free tier:** 500 API calls/month
- **Paid:** $99-999/month
- Aggregates 200+ jurisdictions worldwide

**API Example:**
```bash
curl "https://api.opencorporates.com/v0.4/companies/search?q=Acme&jurisdiction_code=us_de"
```

**Signals:**
- **New entity in founder's name** (Very strong, 1-6 month lead)
- **Delaware C-corp** (most startups)
- **Registered agent** (often reveals law firm/accelerator connections)

**Rate limits:**
- State sites: No official API, scrape carefully
- OpenCorporates: 50 calls/month (free), 10,000/month (paid)

**Best for:**
- Definitive confirmation of new company
- Early detection (entities often formed before hiring/domains)

**Cost:** Free (scraping) or $99+/month (OpenCorporates)

---

## Paid Data Providers

### 7. Crunchbase

**What you can access:**
- Company profiles (funding, team, investors)
- People profiles (current/past roles)
- Funding announcements
- News mentions

**Access methods:**

**A. Crunchbase Pro (Web)**
- $29-99/month per user
- Search, filters, saved searches
- Manual monitoring

**B. Crunchbase API**
- **Starter:** $199/month, 1,000 calls/month
- **Pro:** $499/month, 10,000 calls/month
- **Enterprise:** Custom pricing

**API endpoints:**
```bash
# Search for person
GET https://api.crunchbase.com/api/v4/entities/people/[permalink]

# Search organizations
GET https://api.crunchbase.com/api/v4/searches/organizations
```

**Signals:**
- **New company appears** (Medium-late signal, often after public launch)
- **Founder listed as "Former" at old company** (Medium signal)

**Limitations:**
- Data is crowd-sourced, often lags reality
- Most valuable for *after* public announcement

**Best for:**
- Backfilling company info after detection
- Competitive analysis

**Cost:** $29-499/month

---

### 8. PitchBook

**What you can access:**
- Private company data (funding, valuations)
- LP/GP data
- People/movement tracking
- Deal flow signals

**Access methods:**

**Licensing:**
- **Cost:** $30,000-60,000/year (institutional only)
- **Access:** Desktop app + web platform
- No public API

**Signals:**
- **Founder profile updates** (PitchBook tracks movements)
- **New entity appears** (late signal, usually post-announcement)

**Best for:**
- Institutional investors with budget
- Post-detection research

**Cost:** $30k-60k/year (not practical for individuals)

---

### 9. People Data Labs

**What you can access:**
- 3+ billion person profiles
- Employment history
- Social profiles
- Contact information

**Access methods:**

**API:**
- **Free tier:** 1,000 credits (very limited)
- **Growth:** $199/month, 10,000 credits
- **Scale:** Custom pricing

**Endpoints:**
```bash
# Enrich person by LinkedIn URL
POST https://api.peopledatalabs.com/v5/person/enrich
{
  "profile": "linkedin.com/in/username"
}
```

**Signals:**
- **Job changes** (updated in their database, often before public)
- **Contact info** (email, phone for outreach)

**Best for:**
- Enriching founder profiles
- Finding contact info after signal detection

**Cost:** $199+/month

---

### 10. Clearbit (HG Insights)

**What you can access:**
- Company data (tech stack, employee count)
- Person data (role, email)
- Website monitoring

**Access methods:**

**API:**
- **Free tier:** 50 requests/month
- **Paid:** $99-999+/month

**Endpoints:**
```bash
# Enrich company by domain
GET https://company.clearbit.com/v2/companies/find?domain=example.com
```

**Signals:**
- **New domain appears** (if monitoring domain registrations)
- **Tech stack signals** (after website is live)

**Best for:**
- Post-detection enrichment
- Finding founder emails

**Cost:** $99+/month

---

### 11. ZoomInfo

**What you can access:**
- B2B contact data
- Company info, org charts
- Intent signals (website visits, keyword searches)

**Access methods:**

**Licensing:**
- **Cost:** $15,000-30,000/year
- **Access:** Web platform + API
- Enterprise-focused

**Best for:**
- Large VC firms with budget
- Post-detection outreach

**Cost:** $15k-30k/year

---

## Creative/Alternative Sources

### 12. Wayback Machine (Archive.org)

**What you can access:**
- Historical snapshots of websites
- Detect when personal sites change
- Compare founder bios over time

**Access methods:**

**A. Wayback Machine CDX API**
```bash
# Get all snapshots of a URL
curl "http://web.archive.org/cdx/search/cdx?url=example.com&output=json"
```

**B. Save API**
```bash
# Archive a page now
curl "https://web.archive.org/save/https://example.com"
```

**Use case:**
- Monitor founder personal websites
- Detect bio changes: "CTO at X" → "Building something new"
- Compare snapshots for subtle signals

**Rate limits:**
- CDX API: Generous, no official limit
- Save API: ~5 requests/minute

**Cost:** Free

---

### 13. DNS/WHOIS Monitoring

**What you can access:**
- Domain registration records
- Registrant name/email (if not private)
- Registration date
- Name server changes

**Access methods:**

**A. WHOIS Command Line**
```bash
whois example.com
```

**B. WHOIS APIs**
- **WhoisXML API:** $0.0005-0.002/query
- **DomainTools:** $99-499/month
- **WhoisAPI:** $49-299/month

**C. Certificate Transparency Logs**
```
https://crt.sh/?q=example.com
```
- Shows all SSL certificates issued
- Detect subdomains, new domains

**D. DNS Dumpster**
```
https://dnsdumpster.com/
```
- Free DNS reconnaissance
- Find related domains

**Signals:**
- **New domain registered to founder email** (Very strong)
- **Domain privacy registration with timing correlation** (Medium)
- **SSL cert issued** (Website setup imminent)

**Best for:**
- Early detection (domains registered months ahead)

**Cost:** Free (crt.sh, whois) to $99+/month (DomainTools)

---

### 14. Job Board Scraping

**What you can access:**
- Job postings by "stealth" companies
- Email domains in postings (reveals company)
- Role types (founding engineer = very early)

**Sources to monitor:**

**A. AngelList/Wellfound**
```
https://angel.co/company/[slug]/jobs
```
- Stealth companies often post here
- Scrape daily for new postings

**B. LinkedIn Jobs**
```
https://www.linkedin.com/jobs/search/?keywords=stealth
```
- Search "stealth startup"
- Filter by posted date (last 24 hours)

**C. Y Combinator Work at a Startup**
```
https://www.ycombinator.com/companies
```
- New YC companies appear here first
- Can scrape for batch-to-batch changes

**D. Hacker News "Who's Hiring"**
- Monthly thread, search for founder names
- Stealth companies often post here

**Detection method:**
```bash
# Example: Scrape AngelList daily
curl -s "https://angel.co/jobs" | grep -i "stealth"
```

**Signals:**
- **Stealth company posting jobs** (Strong, 1-2 months ahead)
- **Email domain reveals founder** (Cross-reference watchlist)

**Cost:** Free (scraping) or use services like **JobDataFeeds** ($99+/month)

---

### 15. Conference Agendas & Speaker Bios

**What you can access:**
- Speaker lineups at major conferences
- Speaker bios (often updated with new ventures)
- Panel topics (reveals focus area)

**Conferences to monitor:**

**Tech:**
- TechCrunch Disrupt
- Web Summit
- Collision
- SXSW

**VC/Startup:**
- YC Startup School
- SaaStr Annual
- Industry conferences (fintech, climate, etc.)

**Access method:**
```bash
# Scrape conference speaker page
curl https://techcrunch.com/events/disrupt-2024/speakers/
# Parse for founder names, compare bios to last year
```

**Signals:**
- **Bio changes from "CEO at X" to "Founder at [New Co]"** (Medium)
- **Speaking in new sector** (e.g., fintech founder speaking at climate conference)

**Best for:**
- Cross-sector moves
- Established founders pivoting

**Cost:** Free (scraping)

---

### 16. Podcast Appearance Tracking

**What you can access:**
- Podcast episodes featuring founders
- Topics discussed (reveals interests)
- Mentions of "what's next"

**Sources:**

**A. Podcast RSS Feeds**
- Subscribe to major startup podcasts
- Search transcripts for founder names

**B. Podcast Databases**
- **Listen Notes API:** $49-499/month
- Search episodes by guest name

**Example:**
```bash
# Search Listen Notes for founder
curl -X GET 'https://listen-api.listennotes.com/api/v2/search?q=Patrick%20Collison' \
  -H 'X-ListenAPI-Key: YOUR_KEY'
```

**Signals:**
- **Founder on podcast talking about new space** (Medium)
- **"Exploring opportunities in X"** (Weak-medium)

**Cost:** Free (RSS) or $49+/month (Listen Notes)

---

### 17. News Monitoring & Alerts

**What you can access:**
- News mentions of founders
- "Leaving company X" announcements
- "Starting something new" hints

**Tools:**

**A. Google Alerts**
```
https://www.google.com/alerts
```
- Free, email-based
- Set alert for "[Founder Name] + stealth OR startup OR new company"

**B. Feedly + RSS**
- Aggregate tech news sources
- Create boards for founders/companies

**C. News APIs**
- **NewsAPI:** $0-449/month
- **Bing News API:** $5/1000 queries
- **Google News API (unofficial):** Free

**Best for:**
- Catching blog posts, interviews
- Public hints about next moves

**Cost:** Free (Google Alerts) to $50+/month (APIs)

---

### 18. AngelList/Wellfound Monitoring

**What you can access:**
- Founder profiles
- New company pages (even if minimal info)
- Fundraising status

**Access method:**
- No official API
- Scrape profile pages
- Monitor RSS if available

**Signals:**
- **New company page created** (Strong, 1-2 months ahead)
- **"Actively Fundraising" status** (Late but confirmed)

**Cost:** Free (scraping)

---

### 19. Product Hunt & Hacker News

**What you can access:**
- New product launches
- "Show HN" posts
- Founder comments revealing projects

**Access methods:**

**Product Hunt API:**
```bash
# Get today's posts
curl https://api.producthunt.com/v2/api/graphql \
  -H "Authorization: Bearer $PH_TOKEN"
```

**Hacker News API:**
```bash
# Get new stories
curl https://hacker-news.firebaseio.com/v0/newstories.json
```

**Signals:**
- **Founder posts "Show HN: [Project]"** (Confirmed, but late)
- **Comments about "working on something"** (Medium)

**Cost:** Free

---

### 20. Email Signature Scraping (Ethical Gray)

**What you can access:**
- Email signatures from public mailing lists
- New domain in signature = new company

**Sources:**
- Public mailing list archives (e.g., Y Combinator list, industry forums)
- Conference attendee lists (if emails visible)

**Method:**
```bash
# Search mailing list archive for founder
curl https://groups.google.com/forum/#!searchin/listname/founder-name
```

**Signals:**
- **New email domain** (Strong)

**Ethical note:** Only monitor public mailing lists.

**Cost:** Free

---

## Technical Infrastructure

### Scraping Best Practices

**1. Proxies & Rotation**
- **Residential proxies:** Bright Data, Smartproxy ($50-500/month)
- **Datacenter proxies:** Cheaper but easier to detect
- Rotate user-agents, headers
- Respect robots.txt (or don't, if you're feeling spicy)

**2. Storage & Diffing**
- Store historical snapshots in SQLite or PostgreSQL
- Use `diff` to detect changes
- Example schema:
```sql
CREATE TABLE profile_snapshots (
  id SERIAL PRIMARY KEY,
  founder_id INT,
  source VARCHAR(50), -- 'linkedin', 'twitter', etc.
  snapshot_date TIMESTAMP,
  data JSONB,
  diff JSONB -- store changes from previous snapshot
);
```

**3. Rate Limiting**
- Use queues (Redis, RabbitMQ)
- Exponential backoff on failures
- Spread requests over time (don't hammer APIs)

**4. Alerting**
- Trigger on significant changes:
  - Job title change
  - New domain registration
  - GitHub new org
- Send to Telegram/Slack via webhook

---

## API Reference

### Quick Access Table

| Source | API? | Cost | Rate Limit | Auth Required |
|--------|------|------|------------|---------------|
| LinkedIn | ❌ (scrape) | Free-$500/mo | 100/hr | No |
| Twitter | ✅ | Free-$100/mo | 50/15min | Yes (token) |
| GitHub | ✅ | Free | 5k/hr | Yes (token) |
| SEC EDGAR | ✅ | Free | 10/sec | No |
| USPTO | ✅ | Free | N/A | No |
| Delaware SoS | ❌ (scrape) | Free | N/A | No |
| OpenCorporates | ✅ | $99+/mo | 50-10k/mo | Yes (API key) |
| Crunchbase | ✅ | $199+/mo | 1k-10k/mo | Yes (API key) |
| People Data Labs | ✅ | $199+/mo | 10k credits/mo | Yes (API key) |
| Clearbit | ✅ | $99+/mo | 50 free/mo | Yes (API key) |
| WhoisXML | ✅ | $10+/mo | Varies | Yes (API key) |
| NewsAPI | ✅ | Free-$449/mo | 100-250k/day | Yes (API key) |

---

## Cost Analysis

### Budget Tiers

**Tier 1: Free (DIY Monitoring)**
- **Cost:** $0/month
- **Sources:** Twitter API (free), GitHub, SEC EDGAR, state registries, Google Alerts
- **Coverage:** 100 founders, weekly checks
- **Effort:** 5 hours/week manual + script maintenance

**Tier 2: Basic Automation**
- **Cost:** $100-200/month
- **Add:** Twitter API Basic ($100), domain monitoring ($50)
- **Coverage:** 200 founders, daily checks
- **Effort:** 1 hour/week review

**Tier 3: Professional**
- **Cost:** $500-1000/month
- **Add:** Crunchbase API ($199), People Data Labs ($199), scraping proxies ($100), OpenCorporates ($99)
- **Coverage:** 500+ founders, real-time monitoring
- **Effort:** 2 hours/week (mostly strategy)

**Tier 4: Institutional**
- **Cost:** $2000+/month (or $30k+/year)
- **Add:** PitchBook ($30k/yr), ZoomInfo ($15k/yr), custom scraping infrastructure
- **Coverage:** Unlimited, production-grade
- **Effort:** Full-time analyst

---

## Recommendations by Founder Type

### Technical Founders (Eng, Product)
**Primary sources:**
- GitHub (new orgs, activity)
- LinkedIn (title changes)
- Job boards (stealth postings)

**Budget:** $100/month (Twitter API, domain monitoring)

---

### Operator Founders (ex-FAANG, ex-unicorns)
**Primary sources:**
- LinkedIn (profile changes)
- Twitter (network shifts)
- Conference bios (speaking at new events)

**Budget:** $200/month (add People Data Labs for enrichment)

---

### Serial Entrepreneurs (Multiple exits)
**Primary sources:**
- Domain registrations (new domains)
- Entity formations (Delaware, Wyoming)
- SEC filings (Form D)
- Job postings (AngelList)

**Budget:** $500/month (add Crunchbase, OpenCorporates)

---

## Next Steps

1. **Start free:** GitHub, Twitter free tier, SEC EDGAR, Google Alerts
2. **Add one paid source per month** based on founder type
3. **Build historical database** to improve pattern detection
4. **Automate everything** (see `monitor.sh` and `n8n-workflow.md`)

---

## Final Thoughts

**Data is abundant. Signals are rare. Insights are priceless.**

The hard part isn't accessing data—it's knowing *which* signals matter and *how* to act on them.

This guide gives you the data. The README gives you the system. Now go find some unicorns before anyone else does.

---

**Version:** 1.0  
**Last Updated:** 2026-02-06  
**Maintained by:** Ainary Ventures Intelligence Team
