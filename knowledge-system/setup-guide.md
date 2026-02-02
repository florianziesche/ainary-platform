# Knowledge Extraction System - Setup Guide

Step-by-step instructions to get the full system running.

---

## Phase 1: RSS Feeds with blogwatcher ✅ Ready Now

### 1.1 Verify Installation
```bash
which blogwatcher
# Should output: /opt/homebrew/bin/blogwatcher
```

### 1.2 Add All Verified Feeds

Run these commands to add all working feeds:

```bash
# VC Firm Blogs
blogwatcher add "Sequoia Capital" https://sequoiacap.com/
blogwatcher add "Y Combinator" https://www.ycombinator.com/blog/
blogwatcher add "Greylock Partners" https://greylock.com/
blogwatcher add "Tomasz Tunguz" https://tomtunguz.com/

# Newsletters (Substack)
blogwatcher add "Not Boring" https://www.notboring.co/
blogwatcher add "Lenny's Newsletter" https://www.lennysnewsletter.com/
blogwatcher add "Stratechery" https://stratechery.com/
blogwatcher add "Newcomer" https://www.newcomer.co/
blogwatcher add "The Generalist" https://www.generalist.com/

# Personal blogs
blogwatcher add "Sam Altman" https://blog.samaltman.com/
```

### 1.3 Verify Feeds Added
```bash
blogwatcher blogs
```

### 1.4 Initial Scan
```bash
blogwatcher scan
```

### 1.5 View New Articles
```bash
blogwatcher articles
```

### 1.6 Set Up Daily Automation

**Option A: Via OpenClaw cron (Recommended)**

Add to your OpenClaw cron schedule:
```
Daily 7:00 AM: Run blogwatcher scan and summarize new articles to Obsidian inbox
```

**Option B: Via system crontab**
```bash
crontab -e
# Add:
0 7 * * * /opt/homebrew/bin/blogwatcher scan >> ~/.openclaw/logs/blogwatcher.log 2>&1
```

---

## Phase 2: Twitter/X with bird CLI

### 2.1 Install bird

```bash
# Via Homebrew (recommended for macOS)
brew install steipete/tap/bird

# Or via npm
npm install -g @steipete/bird
```

### 2.2 Verify Installation
```bash
bird --help
bird check  # Shows auth status
```

### 2.3 Configure Authentication

bird uses browser cookie authentication. Choose your method:

**Method A: Use Chrome cookies (if logged into X in Chrome)**
```bash
bird whoami --cookie-source chrome
```

**Method B: Use Arc browser cookies**
```bash
# Find your Arc profile directory
bird whoami --chrome-profile-dir "/Users/florianziesche/Library/Application Support/Arc/User Data/Default"
```

**Method C: Manual cookie setup**
1. Open X.com in browser
2. Open DevTools → Application → Cookies
3. Copy `auth_token` and `ct0` values
4. Run:
```bash
bird whoami --auth-token "YOUR_AUTH_TOKEN" --ct0 "YOUR_CT0"
```

**Method D: Config file (persistent)**
Create `~/.config/bird/config.json5`:
```json5
{
  cookieSource: ["chrome"],
  // or for Arc:
  // chromeProfileDir: "/Users/florianziesche/Library/Application Support/Arc/User Data/Default",
  timeoutMs: 20000
}
```

### 2.4 Test Commands
```bash
bird whoami           # Should show your account
bird home -n 10       # Get 10 recent home timeline tweets
bird mentions         # Check mentions
```

### 2.5 Create Lists for Monitoring

```bash
# Note: bird reads from lists, you create them in Twitter UI
# Go to twitter.com → Lists → Create new list

# Then read from them:
bird lists                    # Show your lists
bird list-timeline <list_id> -n 20
```

### 2.6 Useful Commands for Intel Gathering

```bash
# Morning feed check
bird home --following -n 50

# Search for funding news
bird search "raising OR funded OR seed round" -n 20

# Check specific accounts
bird user-tweets @sama -n 10
bird user-tweets @paulg -n 10

# Get trending/news
bird news -n 10
bird news --ai-only  # AI-curated news
```

### 2.7 Automation Setup

Add to OpenClaw cron:
```
Daily 8:00 AM: Run bird home --following -n 50 --json > /tmp/twitter-morning.json, then summarize
Daily 6:00 PM: Run bird home --following -n 50 --json > /tmp/twitter-evening.json, then summarize
```

---

## Phase 3: Discord Monitoring

### 3.1 OpenClaw Discord Configuration

Discord monitoring is built into OpenClaw. Requirements:
1. OpenClaw bot must be added to the Discord server
2. Channels must be configured in `~/.openclaw/config.yaml`

### 3.2 Check Discord Status
```bash
openclaw status  # Should show Discord connection status
```

### 3.3 Configure Channel Monitoring

In your OpenClaw config, add channels to monitor:
```yaml
channels:
  discord:
    guilds:
      - id: "YOUR_SERVER_ID"
        channels:
          - id: "CHANNEL_ID"
            name: "general"
```

### 3.4 Message Reading (via OpenClaw)

OpenClaw can:
- Read recent messages: `discord readMessages channelId:xxx limit:20`
- Search messages: `discord searchMessages guildId:xxx content:"AI"`
- React to messages
- Send messages

---

## Phase 4: Obsidian Vault Setup

### 4.1 Create Folder Structure

Run this to create the knowledge folders:

```bash
VAULT_PATH="$HOME/Library/Mobile Documents/iCloud~md~obsidian/Documents/System_OS"

mkdir -p "$VAULT_PATH/20-Knowledge/VC-Intelligence/Weekly-Digests"
mkdir -p "$VAULT_PATH/20-Knowledge/VC-Intelligence/Fund-Research"
mkdir -p "$VAULT_PATH/20-Knowledge/VC-Intelligence/Trend-Analysis"
mkdir -p "$VAULT_PATH/20-Knowledge/VC-Intelligence/People-Notes"
mkdir -p "$VAULT_PATH/20-Knowledge/AI-Landscape/Model-Updates"
mkdir -p "$VAULT_PATH/20-Knowledge/AI-Landscape/Startup-Tracker"
mkdir -p "$VAULT_PATH/00-Inbox/Raw-Captures"
```

### 4.2 Create Article Template

Save this as `$VAULT_PATH/70-Templates/Article-Capture.md`:

```markdown
---
source: {{source}}
url: {{url}}
author: {{author}}
captured: {{date}}
tags: [vc-intel]
status: unprocessed
---

# {{title}}

## Summary


## Key Takeaways
- 
- 

## Relevant For
- [ ] Blog post idea
- [ ] Fund research  
- [ ] Trend tracking

## Source Link
[Original Article]({{url}})
```

### 4.3 Create Weekly Digest Template

Save as `$VAULT_PATH/70-Templates/Weekly-Digest.md`:

```markdown
---
type: weekly-digest
week: {{week}}
date_range: {{start_date}} - {{end_date}}
---

# Week {{week}} Intelligence Digest

## Top Stories

### 1. 
### 2.
### 3.

## Funding & Deals
- 

## AI Updates
- 

## Notable Quotes
> 

## Blog Post Ideas
- [ ] 
- [ ] 

## To Research Further
- 

---
*Generated: {{date}}*
```

---

## Phase 5: Putting It All Together

### 5.1 Daily Workflow (Automated)

Morning (7-8 AM):
1. `blogwatcher scan` runs automatically
2. `bird home --following` captures Twitter feed  
3. OpenClaw summarizes new content → Obsidian inbox

Evening (6 PM):
1. Second Twitter check
2. Process day's captures

### 5.2 Weekly Workflow (Sunday)

1. Review week's captures in `/00-Inbox/Raw-Captures/`
2. Generate weekly digest (Claude via OpenClaw)
3. Move processed items to appropriate folders
4. Update trend analysis if patterns emerge
5. Clean up inbox

### 5.3 Sample OpenClaw Commands

```
# During heartbeat or on demand:
"Scan blogwatcher for new articles and summarize any new ones to my Obsidian inbox"

"Check my Twitter feed and extract any VC/AI news worth noting"

"Generate this week's intelligence digest from my Obsidian inbox captures"
```

---

## Troubleshooting

### blogwatcher issues
```bash
# If feeds aren't updating
blogwatcher remove "Feed Name"
blogwatcher add "Feed Name" https://url/

# Check what's tracked
blogwatcher blogs
```

### bird authentication issues
```bash
# Refresh query IDs if getting 404s
bird query-ids --fresh

# Test auth
bird check
bird whoami
```

### Discord access issues
- Ensure bot has `Read Message History` permission
- Check channel IDs are correct
- Verify guild/server ID

---

## What Florian Needs to Do

### Required Actions:
1. **bird CLI auth** - Log into X/Twitter in Chrome or Arc, then run `bird check`
2. **Create Twitter lists** - Set up curated lists at twitter.com/lists
3. **Join Discord servers** - Join OpenClaw and other relevant communities
4. **Configure Discord in OpenClaw** - Add server/channel IDs once joined

### Optional Enhancements:
- Set up Brave API key for web search: `openclaw configure --section web`
- Add more RSS feeds as discovered
- Customize Obsidian templates

---

## Quick Reference

| Task | Command |
|------|---------|
| Scan RSS feeds | `blogwatcher scan` |
| List articles | `blogwatcher articles` |
| Mark read | `blogwatcher read <id>` |
| Twitter home | `bird home -n 50` |
| Twitter search | `bird search "query" -n 20` |
| Check auth | `bird check` / `bird whoami` |

---

*Setup Guide v1.0 - Created 2026-02-01*
