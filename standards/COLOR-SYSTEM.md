# COLOR-SYSTEM.md — Ainary Design System (Research-Based)

*Based on: Palantir Blueprint (semantic intent), Linear (monochrome + sparse color), 
60-30-10 Rule (UX Collective), Color Psychology (IxDF, HakunaMatata 2026).*

## The 60-30-10 Rule Applied

| Proportion | Role | Our Implementation |
|---|---|---|
| **60%** | Dominant | `#08080c` background + `#111116` surfaces |
| **30%** | Secondary | `#ededf0` / `#8b8b95` / `#55555e` (grey text hierarchy) |
| **10%** | Accent | `#c8aa50` (gold) + 4 semantic colors (EIJA) |

## Background & Surfaces
| Token | Hex | Usage |
|---|---|---|
| `--bg-page` | `#08080c` | Every page background |
| `--bg-surface` | `#111116` | Cards, boxes, elevated surfaces |
| `--border-default` | `rgba(255,255,255,0.06)` | Borders, dividers |

## Typography Colors
| Token | Hex | Usage |
|---|---|---|
| `--text-primary` | `#ededf0` | H1, H2, H3, bold, headings |
| `--text-secondary` | `#8b8b95` | Body text (p, li) |
| `--text-muted` | `#55555e` | Meta, labels, captions, timestamps |

## Brand Accent
| Token | Hex | Usage |
|---|---|---|
| `--accent` | `#c8aa50` | CTAs, KPIs, our system in charts, brand dot, box left-borders |

Gold appears ONLY on: CTA buttons, KPI numbers, "our system" in comparison charts, 
Ainary dot, left-border on boxes, gradient blobs. **Max 3-5 gold elements per viewport.**

## Semantic Colors (Blueprint Intent Model)

*Source: Palantir Blueprint — "Each core color is mapped to what we call a visual intent."*
*Source: Color Psychology — "Green = trust/verified, Blue = analytical, Orange = caution, Red = danger"*

| Color | Hex | Intent | EIJA | Other Uses |
|---|---|---|---|---|
| **Green** | `#238551` | Success / Verified | E badge | "Human + AI" badge |
| **Blue** | `#2D72D2` | Primary / Analytical | I badge | Category tags (EI-001, CI-001), "More from" tags |
| **Orange** | `#C87619` | Warning / Judgment | J badge | — |
| **Red** | `#CD4246` | Danger / Unverified | A badge | — |

**These 4 colors appear ONLY where they carry semantic meaning.**
Never for decoration, grid borders, icon coloring, or arbitrary grouping.

### EIJA Badge Style
```css
/* All 4 badges: same structure, different color */
display: inline-block;
font: 700 11px/1 var(--font-mono);
width: 22px; height: 22px;
border-radius: 4px;
text-align: center;
line-height: 22px;

/* E */ background: rgba(35,133,81,0.15); color: #238551;
/* I */ background: rgba(45,114,210,0.15); color: #2D72D2;
/* J */ background: rgba(200,118,25,0.15); color: #C87619;
/* A */ background: rgba(205,66,70,0.15); color: #CD4246;
```

## UI Element Rules

| Element | Color | Why |
|---|---|---|
| Category tag (EI-001, CI-001) | Blue `#2D72D2` | Navigational = Blueprint "primary intent" |
| "Human + AI" badge | Green `#238551` + green border | Quality signal = Blueprint "success intent" |
| Box left-border | Gold `#c8aa50` | Brand accent, consistent |
| Card borders | `--border-default` (grey) | Neutral container |
| Links | Gold or underline | Interactive |
| SVG graphics | `rgba(255,255,255,0.1-0.35)` | Monochrome, no semantic color |
| Labels (PROBLEM, OUR APPROACH) | `--text-muted` | Structural, not decorative |

## Typography Scale (all articles)

*Source: Optimal reading width 45-75 chars at 1.05rem ≈ 720px container.*

| Element | Size | Weight | Line-height | Color |
|---|---|---|---|---|
| H1 (article) | `2.2rem` | 600 | 1.2 | `--text-primary` |
| H1 (page, e.g. About) | `3rem` | 600 | 1.1 | `--text-primary` |
| H2 | `1.5rem` | 600 | 1.4 | `--text-primary` |
| Body p | `1.05rem` | 400 | 1.75 | `--text-secondary` |
| Meta/Labels | `0.65-0.75rem` | 500 | 1 | `--text-muted` |
| Badges | `0.55rem` | 700 | 1 | per intent |

**Container max-width: `720px`** for all article content.

**No `font-weight: 300`.** Minimum is 400. 300 is too thin on dark backgrounds.

**Mobile H1: `1.6rem`** (breakpoint 640px).

## Fonts
| Token | Value | Usage |
|---|---|---|
| `--font-body` / `--font-display` | `Inter, -apple-system, system-ui, sans-serif` | All text |
| `--font-mono` | `JetBrains Mono, monospace` | Code, badges, category tags, meta |

## Required Components (every article page)
- Reading progress bar (gold, 2px, fixed top)
- Ambient gradient blobs (gold + silver)
- shared/styles.css + nav.js + footer.js

## Border Radius (from Linear: "8px-spacing scale")
| Value | When |
|---|---|
| `8px` | All content boxes, cards, data boxes |
| `3px-4px` | Small inline badges (EIJA, tags) |
| `6px` | Buttons |
| `50%` | Circles only (dots, avatars) |

No 10px, 12px, 16px, 100px on content boxes.

## Box System (2 types)

### Blockquote
```css
border-left: 2px solid var(--accent); /* gold */
padding-left: 24px;
background: none;
font-style: italic;
```
**When:** Quotes, pulled text.

### Data Box
```css
background: var(--bg-surface);
border: 1px solid rgba(255,255,255,0.06);
border-left: 3px solid var(--accent); /* gold */
border-radius: 8px;
padding: 20px 24px;
```
**When:** Tables, KPIs, legends — structurally different from prose.

### Box Rules
- One left-border color: **gold only**. No blue, green, red borders.
- No box without different information than surrounding text.
- Max 3 boxes per article. More = noise.
- No repeated box pattern 3+ times.

## Article Header Format (all articles)
```
← Building in Public                     (--text-muted, mono, link)
COMPOUND INTELLIGENCE · CI-001            (#2D72D2, mono, uppercase, no border)
Florian Ziesche · Feb 27, 2026 · 12 Min  Human + AI
                                          (#238551 badge with green border)
Article Title                             (H1, --text-primary, LEFT-aligned)
Lead text...                              (--text-secondary)
```

## "More from" Section
- Layout per context: Cards with SVG thumbnails OR list-style — both OK
- Category tags in "More from": Blue `#2D72D2`
- Consistent tokens regardless of layout choice

## Ambient Background
Every page: 2 fixed gradient blobs (Gold `#c8aa50→#a08030→transparent` + 
Silver `#ffffff→#e8f0ff→transparent`), `position:fixed`, `mix-blend-mode:screen`,
`opacity: 0.06-0.1`, drifting animation 90s.

## Shared Components (mandatory on every page)
| Component | File |
|---|---|
| Styles | `shared/styles.css` |
| Nav | `shared/nav.js` → `#site-nav` |
| Footer | `shared/footer.js` → `#site-footer` |

**No page may override `:root` variables from shared/styles.css.**

## Decision Framework
Before adding ANY color to ANY element, ask:
1. Is this color in the table above? → No = don't use it.
2. Does this color carry semantic meaning here? → No = use grey.
3. Would removing this color lose information? → No = remove it.
4. Would Palantir Blueprint assign an "intent" here? → Map to the right intent.
