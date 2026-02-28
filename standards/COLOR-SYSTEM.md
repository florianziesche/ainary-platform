# COLOR-SYSTEM.md — Ainary Design Tokens (NOT NEGOTIABLE)

*Inspired by Linear (monochrom) + Blueprint (semantic intent). No decorative colors.*

## Background & Surfaces
| Token | Hex | Usage |
|---|---|---|
| `--bg-page` | `#08080c` | Page background, everywhere |
| `--bg-surface` | `#111116` | Cards, boxes, elevated surfaces |
| `--border-default` | `rgba(255,255,255,0.06)` | Borders, dividers |

## Typography
| Token | Hex | Usage |
|---|---|---|
| `--text-primary` | `#ededf0` | H1, H2, H3, bold, headings |
| `--text-secondary` | `#8b8b95` | Body text (p, li, spans) |
| `--text-muted` | `#55555e` | Captions, footnotes, timestamps, meta |

## Brand
| Token | Hex | Usage |
|---|---|---|
| `--accent` | `#c8aa50` | CTAs, KPIs, our system in charts, brand dot |

Gold is reserved for: CTA buttons/links, KPI numbers, "our system" line in comparison charts, the Ainary dot. Nothing else.

## Semantic Intent (EIJA only)
| Token | Hex | Intent | EIJA |
|---|---|---|---|
| `--green` | `#238551` | Evidenced, verified | E badge |
| `--blue` | `#2D72D2` | Interpretation, analytical | I badge, category tags |
| `--orange` | `#C87619` | Judgment, caution | J badge |
| `--red` | `#CD4246` | Assumption, unverified | A badge |

These 4 colors appear ONLY in EIJA badges. Not in grid borders, card decorations, or arbitrary groupings.

## UI Elements
| Element | Color | Rule |
|---|---|---|
| Category tag (EI-001, CI-001) | `--blue` | Always blue, no background, uppercase mono |
| "Human + AI" badge | `--green` + green border | Always green, small mono text |
| Card borders | `--border-default` | Grey only. No colored top-borders. |
| Section dividers | Gold dot or `--border-default` | Subtle |
| Links | `--accent` or underline | Interactive = gold |
| Hover states | opacity or lighter shade | No new colors |

## Rules
1. **No color without semantic meaning.** If a color doesn't map to this table, it's wrong.
2. **No meaning with two colors.** Each concept = one color everywhere.
3. **Grey is the default.** When in doubt, use grey tones.
4. **Gold is scarce.** Max 3-5 gold elements per viewport. Overuse kills impact.
5. **No page-level :root overrides.** All colors come from shared/styles.css.
6. **EIJA colors never used decoratively.** Green border on a card ≠ "looks nice". Green = Evidenced.

## Fonts
| Token | Value | Usage |
|---|---|---|
| `--font-body` | `Inter, -apple-system, system-ui, sans-serif` | All body text |
| `--font-mono` | `JetBrains Mono, monospace` | Code, badges, category tags, meta |

No other fonts. No font-size overrides per page.

## Box System (2 types only)

### 1. Blockquote
```css
border-left: 2px solid var(--accent);  /* #c8aa50 */
padding-left: 24px;
background: none;
```
**When:** Quotes, metaphors, pulled text. Always italic.

### 2. Data Box
```css
background: var(--bg-surface);  /* #111116 */
border: 1px solid rgba(255,255,255,0.06);
border-radius: 8px;
padding: 20px 24px;
```
**When:** Tables, KPIs, legends, grids, code — anything structurally different from prose.

### Rules
- **One left-border color: gold (`#c8aa50`).** No blue, no green, no red. Always gold, always consistent.
- **No box without different information.** If the content is just another paragraph, leave it as text.
- **Max 3 boxes per article.** More = noise. If you need a 4th, one of the first 3 is wrong.
- **No repeated box patterns.** If the same box template appears 3+ times, it's visual noise.
- **Blockquote ≠ Data Box.** Don't mix: italic quoted text never goes in a surface box.

## Border Radius
| Value | When |
|---|---|
| `8px` | All content boxes, cards, data boxes |
| `50%` | Circles only (dots, avatars) |
| `3px` | Small inline badges (EIJA, tags) |
| `6px` | Buttons |

No `12px`, `16px`, `100px` on content boxes. No mixing.

## Gradient Blobs (ambient background)
Gold blob uses `#c8aa50 → #a08030 → transparent`. Allowed exception: gradient spectrum uses intermediate values. These are NOT design tokens — they're render artifacts.

## macOS Traffic Lights
`#ff5f57` / `#ffbd2e` / `#28c840` — allowed ONLY inside monitor mockup chrome. Nowhere else.

## Labels (PROBLEM, OUR APPROACH, etc.)
Use `--text-muted` (#55555e). NOT gold. Labels are structural, not decorative.

## What This Replaces
- No more `--text: #F6F7F9` overrides (use `#ededf0`)
- No more `--bg: #111418` or `#1C2127` surfaces (use `#111116`)
- No more colored EIJA badges (all grey)
- No more colored left-borders (all gold)
- No more inconsistent white values
- No more arbitrary color groupings
- No more per-page `:root` overrides
