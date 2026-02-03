# CNC Planner Pro — Deployment Guide

## Overview

CNC Planner Pro is a static web application that can be deployed to any static hosting provider.

---

## Quick Deploy Options

### Option 1: Vercel (Recommended)

1. **Install Vercel CLI:**
   ```bash
   npm i -g vercel
   ```

2. **Deploy:**
   ```bash
   cd products/cnc-planner
   vercel
   ```

3. **Production Deploy:**
   ```bash
   vercel --prod
   ```

**Automatic Deploys:** Connect your GitHub repo in Vercel dashboard for automatic deploys on push.

---

### Option 2: Netlify

1. **Install Netlify CLI:**
   ```bash
   npm i -g netlify-cli
   ```

2. **Deploy:**
   ```bash
   cd products/cnc-planner
   netlify deploy
   ```

3. **Production Deploy:**
   ```bash
   netlify deploy --prod
   ```

---

### Option 3: GitHub Pages

1. Create a new repo or use existing
2. Push the `products/cnc-planner` folder
3. Enable GitHub Pages in Settings → Pages
4. Select branch and folder

---

### Option 4: Traditional Hosting

Upload these files to your web server:
- `landing-page.html` → `index.html`
- `app.html` or `v14/app.html` → `/app/index.html`
- All assets and documentation

---

## File Structure for Deployment

```
public/
├── index.html          ← Landing Page
├── app/
│   └── index.html      ← Main Application (v14)
├── demo/
│   └── index.html      ← Demo Version
├── docs/
│   ├── manual.html     ← User Manual
│   ├── datenschutz.html
│   └── agb.html
├── sales/
│   └── presentation.html
├── assets/
│   └── (images, if any)
└── robots.txt
```

---

## Configuration Files

### vercel.json

```json
{
  "version": 2,
  "builds": [
    { "src": "**/*.html", "use": "@vercel/static" }
  ],
  "routes": [
    { "src": "/app", "dest": "/app/index.html" },
    { "src": "/demo", "dest": "/demo/index.html" },
    { "src": "/", "dest": "/index.html" }
  ],
  "headers": [
    {
      "source": "/(.*)",
      "headers": [
        { "key": "X-Content-Type-Options", "value": "nosniff" },
        { "key": "X-Frame-Options", "value": "DENY" },
        { "key": "X-XSS-Protection", "value": "1; mode=block" },
        { "key": "Referrer-Policy", "value": "strict-origin-when-cross-origin" }
      ]
    }
  ]
}
```

### netlify.toml

```toml
[build]
  publish = "."

[[redirects]]
  from = "/app"
  to = "/app/index.html"
  status = 200

[[redirects]]
  from = "/demo"
  to = "/demo/index.html"
  status = 200

[[headers]]
  for = "/*"
  [headers.values]
    X-Content-Type-Options = "nosniff"
    X-Frame-Options = "DENY"
    X-XSS-Protection = "1; mode=block"
```

---

## Environment Variables

No environment variables required for basic deployment.

For future backend integration:

```env
# .env.example
API_URL=https://api.cncplanner.de
STRIPE_PUBLIC_KEY=pk_live_xxx
ANALYTICS_ID=G-XXXXXXXXXX
```

---

## Domain Setup

### Custom Domain on Vercel

1. Go to Project Settings → Domains
2. Add your domain: `cncplanner.de`
3. Configure DNS:
   - A Record: `76.76.21.21`
   - Or CNAME: `cname.vercel-dns.com`

### SSL Certificate

Vercel and Netlify provide free SSL certificates automatically.

---

## Pre-Deployment Checklist

- [ ] Test landing page in multiple browsers
- [ ] Test app functionality (create project, calculate, export)
- [ ] Verify all links work
- [ ] Check mobile responsiveness
- [ ] Update contact email addresses
- [ ] Remove demo credentials from documentation
- [ ] Set up error tracking (optional: Sentry)
- [ ] Configure analytics (optional: Plausible, Fathom)

---

## Post-Deployment

1. **Verify deployment:**
   - Visit the live URL
   - Test all pages
   - Check console for errors

2. **Submit to search engines:**
   - Google Search Console
   - Bing Webmaster Tools

3. **Set up monitoring:**
   - Uptime monitoring (e.g., UptimeRobot)
   - Error tracking

---

## Rollback

### Vercel
```bash
vercel rollback
```

### Netlify
Use the Netlify dashboard to restore a previous deploy.

---

## Support

For deployment issues, contact: dev@cncplanner.de
