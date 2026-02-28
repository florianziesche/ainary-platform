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

## Box/Callout Rule
A bordered box is justified ONLY when it contains **different information** than the surrounding text:
- ✅ KPI numbers (300+, 750, 4 of 8) — scannable, different from prose
- ✅ One-time callouts (self-assessment, important note) — unique, singular
- ✅ Code blocks — structurally different
- ❌ Repeated "What it improves" boxes — just another paragraph in a frame
- ❌ Any box that appears 3+ times with the same pattern — becomes noise

**If the box has no information the text doesn't already have, leave it away. Cleaner.**

## What This Replaces
- No more `--text: #F6F7F9` overrides in articles
- No more `--bg: #111418` overrides
- No more colored grid card borders
- No more inconsistent white values (#ededf0 vs #F6F7F9)
- No more arbitrary color groupings in grids/cards
