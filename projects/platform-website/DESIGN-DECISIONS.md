# DESIGN-DECISIONS.md — Ainary Website
*Updated: 2026-02-16 14:50 CET*

## Reference Sites
Check these first when unsure: **Palantir, Linear, McKinsey**

## Design Tokens (CSS Variables)
```css
--bg-page:          #08080c;
--bg-surface:       #111116;
--bg-surface-hover: #18181f;
--bg-input:         #0e0e13;
--border-default:   rgba(255, 255, 255, 0.06);
--border-hover:     rgba(255, 255, 255, 0.10);
--border-active:    rgba(200, 170, 80, 0.30);
--text-primary:     #ededf0;
--text-secondary:   #8b8b95;
--text-muted:       #55555e;
--accent / --gold:  #c8aa50;
--accent-hover:     #d4b85c;
--font-display:     'Inter', -apple-system, sans-serif;
--font-body:        'Inter', -apple-system, sans-serif;
--font-mono:        'JetBrains Mono', monospace;
--space-section:    120px;
```
**No Geist font.** Was never loaded. CDN link removed Feb 16.

## Typography Scale
| Element | Font | Size | Weight | Spacing | Color | Line-height |
|---------|------|------|--------|---------|-------|-------------|
| H1 Hero | Inter | 4.5rem | 600 | -0.035em | white | 1.05 |
| Hero subtitle | Inter | 1.75rem | 400 | -0.01em | text-secondary | 1.4 |
| Hero product label | Mono | 0.75rem | 400 | 0.04em | text-muted | — |
| Section H2 | Inter | 3rem | 500 | -0.035em | text-primary | — |
| Section subtitle | Inter | 1rem | 400 | — | text-secondary | 1.6 |
| Body text | Inter | 1rem | 400 | — | text-secondary | 1.8 |
| Labels (UPPERCASE) | Mono | 0.75rem | 600 | 0.06em | text-secondary | — |
| Finding titles | Inter | 0.875rem | 500 | — | text-primary | — |
| KPI in boxes | Mono | 1.25rem | 600 | — | text-primary | — |
| Big KPI standalone | Mono | 4rem | 600 | -0.03em | text-primary | 1 |
| KPI source citation | Mono | 0.65rem | 400 | — | text-muted (0.7 opacity) | — |
| Sources/badges | Mono | 0.75rem | 400 | — | text-muted | — |
| Footer bar text | Mono | 0.75rem | 400 | — | text-muted | — |
| Card title | Inter | 1.25rem | 500 | — | text-primary | 1.3 |
| Card body | Inter | 1rem | 400 | — | text-secondary | 1.7 |

## CTAs
| Type | Font | Size | Weight | Color | Background |
|------|------|------|--------|-------|------------|
| Action link (gold) | Inter | 1rem | 500 | #c8aa50 | — |
| Footer-bar link | Inter | 0.75rem | 500 | #c8aa50 | — |
| Card "Read →" | Inter | 1rem | 500 | #c8aa50 | — |
| btn-primary | Inter | 0.875rem | 500 | #fff | #c8aa50 |
| btn-secondary | Inter | 0.875rem | 500 | text-primary | transparent, border |
| "Try it yourself ↓" | Inter | 0.875rem | 500 | #000 | #fff |

**Rule:** Action links = Inter, never Mono. Gold = clickable/premium. Grey = non-clickable meta.

## Spacing
- Section padding: `var(--space-section)` = 120px (desktop), 48px (mobile)
- Container max-width: 1440px, padding 0 48px (desktop), 0 16px (mobile)
- Content container (text-heavy pages): max-width 800px
- Section margin-bottom between elements: 40-48px
- Card padding: 32px
- Card gap: 24px (grid), 10px (stacked items)

## Cards & Boxes
- Background: `var(--bg-page)` (#08080c)
- Border: `1px solid rgba(255,255,255,0.12)`
- Border-radius: 16px
- Hover: `border-color rgba(255,255,255,0.25)` + `box-shadow 0 0 0 1px rgba(255,255,255,0.06)`
- Content boxes (inside showcase): `background: #111116`, border `rgba(255,255,255,0.08)`

## Callout Boxes
- Border-left: `2px solid rgba(200,170,80,0.4)` — gold tint, ALL callouts
- Background: `rgba(255,255,255,0.04)`
- Padding: 12px 14px
- Label: 0.75rem, 600, text-primary (KEY FINDING, HIDDEN SIGNAL, WHY NOT HIGHER)
- Body: 0.875rem, text-secondary, line-height 1.6

## Showcase Tabs
- Header bar: padding 20px 40px. Title = Mono 1rem muted. Badge = Mono 0.75rem secondary, border pill.
- Content: padding 40px. Grid gap 48px.
- Footer bar: padding 16px 40px. Mono 0.75rem muted.
- **Header = Scope** (what: pages, agents, time). **Footer = Process** (how: synthesis rounds, generation time). NO duplicates.
- Tab order: Real data first (AR-001), then Examples.
- Tab buttons: Mono 0.875rem. Active = white bg, dark text, strong border. Inactive = transparent, grey text, subtle border.
- CTA under tabs: gold link, left-aligned. All tabs consistent.

## Nav
- Logo left (dot + "Ainary"), links center, CTA right
- **No language switcher in nav** (moved to footer, like Palantir)
- **No Use Cases** (page quality gap — re-add when updated)
- Links: Daily Briefing · Blog
- CTA: "Get in touch" btn-primary
- Responsive: hide links + auth at ≤768px, show hamburger
- Mobile menu: CSS class toggle (.open), not inline styles
- **All pages use shared/nav.js** — single source of truth
- Height: 56px, sticky, backdrop-filter blur(12px)

## Footer (shared/footer.js)
- CTA section: "Better decisions start here." + bordered button
- Grid: Ainary logo | Explore | Connect | Legal
- Language: "EN · DE" bottom right (EN=white active, DE=grey link)
- Copyright: left-aligned, 0.7rem, text-muted
- **All pages use shared/footer.js** — single source of truth

## Hero (index.html)
- "Multiply your team." (H1)
- "We do 80% of the work. You do the 20% that matters." (subtitle)
- Product label: Mono, muted (e.g. "Strategic intelligence · Automated research · Ready in minutes")
- CTAs: "Try it yourself ↓" (white/black, scrolls to #try-it) + "Get in touch" (gold)

## KPI Section (standalone, with sources)
- 80% faster (Anthropic Research, 2025)
- ~10 min per report (Ainary system average)
- 2-3× more output (McKinsey State of AI, 2025)
- Source citations: Mono 0.65rem, text-muted, opacity 0.7

## Agent Pills
- Grey border + grey text (not gold). Gold = clickable/premium.
- Mono, 0.75rem, border `rgba(255,255,255,0.08)`, text-secondary

## Signal Items (Daily Brief)
- Border-bottom separation (not cards)
- Source tag: Mono 0.6rem, gold, uppercase
- Time: Mono 0.6rem, text-muted
- Relevance indicator: Mono 0.6rem, color-coded
- Title: Inter, 1rem, 500, text-primary
- Insight body: Inter, 0.875rem, text-secondary, line-height 1.6
- "So What" callout: gold label (Mono 0.65rem uppercase), body 0.85rem text-secondary

## Effects
- Hero glow: radial gradient, gold 0.07 opacity
- Dot grid: 32px spacing, 0.04 opacity
- Scroll fade-in: translateY(24px) → 0, opacity 0→1, 0.7s ease-out
- Card hover glow: border-color + box-shadow transition
- Logo pulse: 3s ease-in-out infinite, ring scale 1→1.3

## Honesty Rules
- No fake company names (use "Series B startup" etc.)
- Example tabs labeled "Example ·"
- External stats must be attributed with source + year
- "Honest about gaps" = show confidence scores, flag limitations
- Report IDs from published URLs, not sequential

## Report IDs (verified)
- AR-001: State of AI Agent Trust 2026
- AR-031: Personal AI Stack Architecture 2026
- AR-032: Knowledge Compounding: Obsidian + Agent

## Easter Eggs
- Console (F12): "★ Ainary — You inspect websites. We inspect industries."
- Demo keyword "trust": agents discuss trust → shows report PDF link
- No hints anywhere. Rewards curiosity.

## Page-Specific Notes
- **index.html**: Inline CSS (has own nav/typography styles) + shared/nav.js + shared/footer.js
- **daily-brief.html**: Inline CSS + shared/nav.js + shared/footer.js + shared/styles.css
- **blog.html**: shared/styles.css + shared/nav.js + shared/footer.js (minimal inline)
- **DE pages**: Outdated — do not update until EN is stable
