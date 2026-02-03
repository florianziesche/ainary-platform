# n8n Workflow: Substack Automation

## Overview
Automate Substack content publishing and branding updates.

---

## Workflow 1: Profile & Branding Setup (One-Time)

### Trigger
Manual trigger

### Steps
1. **HTTP Request** — Upload profile image
   - URL: Substack API or direct upload
   - File: `profile-logo.png`

2. **HTTP Request** — Update publication settings
   - Name: "Finite Matter" 
   - Tagline: "AI, Startups & the Future of Work"
   - Bio: [from substack-setup.md]

---

## Workflow 2: Auto-Publish Posts

### Trigger
- Webhook from OpenClaw
- OR: Watch folder for new .md files
- OR: Schedule (e.g., Tuesday/Thursday 10:00 CET)

### Steps
1. **Read File** — Get markdown content
2. **Markdown to HTML** — Convert
3. **HTTP Request** — Create draft on Substack
4. **IF** auto-publish enabled → Publish
5. **HTTP Request** — Post to LinkedIn
6. **HTTP Request** — Post to Twitter

---

## Workflow 3: Header Image Generator

### Trigger
Webhook with title + subtitle

### Steps
1. **Code Node** — Generate HTML from template
2. **HTTP Request** — Screenshot API (or Puppeteer)
3. **Return** — PNG URL for Substack post

---

## Substack API Notes

Substack doesn't have official API, but options:
1. **Browser automation** (Puppeteer in n8n)
2. **Email-to-post** (send formatted email)
3. **Unofficial API** (reverse-engineered endpoints)

### Recommended: Puppeteer Node
```javascript
// n8n Puppeteer workflow
const browser = await puppeteer.launch();
const page = await browser.newPage();
await page.goto('https://finitematter.substack.com/publish/post');
// Login via cookies
// Fill form
// Upload image
// Save/Publish
```

---

## Required Credentials

- [ ] Substack login cookies (export from browser)
- [ ] LinkedIn API token
- [ ] Twitter API keys
- [ ] Screenshot API key (optional)

---

## Files Ready

| File | Location | Purpose |
|------|----------|---------|
| Profile Logo | `content/substack-branding/exports/individual/profile-logo.png` | 400x400 avatar |
| All Templates | `content/substack-branding/exports/all-templates.png` | Reference |
| Header HTML | `content/substack-branding/header-template.html` | Generate headers |
| Setup Guide | `content/substack-branding/substack-setup.md` | Bio, links, colors |

---

## Implementation Order

1. **Export Substack cookies** from Chrome
2. **Create n8n workflow** with Puppeteer
3. **Test profile update** (logo + bio)
4. **Test post creation** (draft first)
5. **Add LinkedIn/Twitter** cross-posting
6. **Schedule** regular runs

---

## Quick Start After Onkel

```bash
# 1. Export cookies
# Chrome → finitematter.substack.com → F12 → Application → Cookies → Export

# 2. Open n8n
open http://localhost:5678

# 3. Import workflow template (create in n8n UI)
```
