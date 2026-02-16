# DESIGN-DECISIONS.md — Ainary Website
*Updated: 2026-02-16*

## Reference Sites
Check these first when unsure: **Palantir, Linear, McKinsey**

## Typography
- **--font-display + --font-body:** Inter (was Geist, never loaded → changed Feb 16)
- **--font-mono:** JetBrains Mono
- H1 Hero: Inter, 4.5rem, 600, -0.035em, white
- Hero subtitle: Inter, 1.75rem, 400, grey (value statement, not features)
- Section H2: Inter, 3rem, 500, -0.035em, left-aligned
- Body: Inter, 1rem, text-secondary, line-height 1.8
- Section labels (UPPERCASE): Mono, 0.75rem, 600, text-secondary, letter-spacing 0.06em
- Finding titles: Inter, 0.875rem, 500, text-primary
- KPI numbers: Mono, 1.25rem, 600, text-primary (in tab boxes)
- Big KPI numbers: Mono, 4rem, 600, -0.03em (standalone section)
- Sources/badges: Mono, 0.75rem, text-muted
- Footer bar text: Mono, 0.75rem, text-muted

## CTAs
- **Action links** (gold text): Inter, 1rem, #c8aa50, weight 500. Never Mono.
- **Footer-bar links**: Inter, 0.75rem, #c8aa50, weight 500
- **"Read →"** on research cards: Inter, 1rem, #c8aa50, weight 500
- **Primary button** (btn-primary): Inter, 0.875rem, 500, gold bg (#c8aa50), white text
- **Secondary button**: Inter, 0.875rem, 500, transparent bg, white text, border
- **"Try it yourself ↓"** hero button: white bg, black text (special)

## Callout Boxes
- Border-left: 2px solid rgba(200,170,80,0.4) — gold tint, ALL callouts
- Background: rgba(255,255,255,0.04)
- Label inside: 0.75rem, 600, text-primary (KEY FINDING, HIDDEN SIGNAL, WHY NOT HIGHER)

## Showcase Tabs
- Header bar: padding 20px 40px. Title = Mono 1rem muted. Badge = Mono 0.75rem secondary, border pill.
- Content: padding 40px. Grid gap 48px.
- Footer bar: padding 16px 40px. Mono 0.75rem muted.
- **Header = Scope** (what: pages, agents, time). **Footer = Process** (how: synthesis rounds, generation time). NO duplicates.
- Tab 1+2: labeled "Example ·". Tab 3: real data (AR-001).
- Summary margin-bottom: 24px (all tabs).
- CTA under tabs: "See use cases →" left-aligned. All 3 tabs consistent.

## Nav
- Logo left, links center, CTA right
- **No language switcher in nav** (moved to footer, like Palantir)
- Links: Use Cases · Daily Briefing · Blog
- Responsive: hide links + auth at ≤768px, show hamburger
- Mobile menu: CSS class toggle (.open), not inline styles

## Footer
- Language: "EN · DE" bottom right (EN=white active, DE=grey link)
- Columns: Ainary logo | Explore | Connect | Legal

## Agent Pills
- Grey border + grey text (not gold). Style matches meta badges.
- Mono, 0.75rem, border rgba(255,255,255,0.08), text-secondary

## KPI Section (standalone)
- Real system stats: < 10 min / +30 pages / 5 agents
- NOT external studies. No footnotes needed.

## Hero
- "Multiply your team." (H1) + "We do 80% of the work. You do the 20% that matters." (subtitle = value statement)
- CTAs: "Try it yourself ↓" (white/black, scrolls to demo) + "Get in touch" (gold)

## Honesty Rules
- No fake company names (use "Series B startup" etc.)
- Tab 1+2 labeled "Example"
- External stats must be attributed, or use own system stats
- "Honest about gaps" = show confidence scores, flag limitations

## Report IDs (verified against live reports)
- AR-001: State of AI Agent Trust 2026
- AR-031: Personal AI Stack Architecture 2026
- AR-032: Knowledge Compounding: Obsidian + Agent
