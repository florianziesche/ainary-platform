---
name: website-ui
description: Develop, edit, and deploy the Ainary website (HTML/CSS/JS). Use when making visual changes, fixing layout, updating content, or deploying to Vercel.
metadata:
  openclaw:
    emoji: "🎨"
    requires:
      bins: ["git", "npx"]
---

# Website UI Skill

## Project
- **Repo:** `/Users/florianziesche/.openclaw/workspace/projects/platform-website`
- **Live:** https://ainaryventures.com
- **Deploy:** `cd <repo> && git add -A && git commit -m "<msg>" && git push origin main && npx vercel --prod`
- **Languages:** EN (root), DE (`de/`)

## Before ANY Edit
1. Read `DESIGN-SYSTEM.md` in the repo — it's the single source of truth
2. Identify which file(s) to change
3. Never blind-iterate — have a reference or clear spec

## Design System (Quick Reference)

### Typography (5-Step Scale)
| Level | Size | Font | Weight | Spacing |
|-------|------|------|--------|---------|
| Hero | 4.5rem (72px) | Geist | 600 | -0.035em |
| Section Header | 3rem (48px) | Geist | 500 | -0.035em |
| Subtitle/Card Title | 1.25-1.5rem | Geist | 400-500 | -0.01em |
| Body | 1.0625rem (17px) | Inter | 400 | — |
| Small/Mono | 0.75rem (12px) | JetBrains Mono | 400-500 | — |

### Colors
- Page bg: `#08080c` — Surface: `#111116`
- Text: `#ededf0` (primary) / `#8b8b95` (secondary) / `#55555e` (muted)
- Gold: `#c8aa50` — ONLY for CTAs, key metrics, hover states
- Borders: `rgba(255,255,255,0.06-0.12)`

### Layout
- Container: `max-width:1440px; padding:0 48px`
- Section spacing: `120px` vertical
- Cards: `bg-page`, `border:1px solid rgba(255,255,255,0.12)`, `border-radius:16px`, `padding:32px`
- Headers: **left-aligned** (not centered). Hero: centered.
- Mobile: container padding 16px, section padding 48px

### KPI Style (Gold Standard)
```
Numbers: JetBrains Mono, 4rem, weight 600, -0.03em
Labels: Inter, 1.0625rem, --text-muted
Sources: JetBrains Mono, 0.75rem, --text-muted
Divider: 1px rgba(255,255,255,0.08), 64px tall
```

### Don'ts
- No white/light sections — everything dark
- No gold for body text
- No fake clickable elements (buttons that do nothing)
- No parallax
- No border-radius > 16px
- No centered section headers (hero exception)

## Deploy Workflow
```bash
cd /Users/florianziesche/.openclaw/workspace/projects/platform-website
# edit files...
git add -A
git commit -m "descriptive message"
git push origin main
npx vercel --prod
```
Wait for "Aliased: https://ainaryventures.com" confirmation.
Tell user to `Cmd + Shift + R` to see changes.

## Shared Components
- `shared/nav.js` — Navigation (used by all pages)
- `shared/footer.js` — Footer with CTA + links (used by all pages)

## Page Structure (index.html)
1. Nav (sticky, blur)
2. Hero (centered, glow effect)
3. Product Showcase (3 tabs: AI Readiness, Due Diligence, AI Research)
4. Terminal Demo (interactive sim)
5. Multiplier (left-aligned)
6. Trust Cards + KPIs (3-col grid + metrics with sources)
7. Published Research (3-col cards)
8. Why I built this (photo + text)
9. Footer (via shared/footer.js)

## Effects
- Hero glow: radial gold gradient behind headline
- Dot grid: subtle dots on Showcase + Trust sections
- Scroll fade-in: IntersectionObserver, 0.7s ease-out
- Card hover: border brightens to rgba(255,255,255,0.25)

## References
- Linear (linear.app) — left-aligned headers, tight letter-spacing, product-in-hero
- Vercel (vercel.com) — pure black, minimal color, wide spacing
- ElevenLabs (elevenlabs.io) — clean dark theme, readable body text
