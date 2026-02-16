# Ainary Design System — Rulebook

*Single source of truth for all pages. When in doubt, follow this.*

---

## Colors

| Token | Value | Usage |
|-------|-------|-------|
| `--bg-page` | `#08080c` | Page background |
| `--bg-surface` | `#111116` | Cards, panels, elevated surfaces |
| `--bg-surface-hover` | `#18181f` | Surface hover state |
| `--border-default` | `rgba(255,255,255,0.06)` | Default borders |
| `--border-hover` | `rgba(255,255,255,0.10)` | Hover borders |
| `--text-primary` | `#ededf0` | Headlines, primary text |
| `--text-secondary` | `#8b8b95` | Body text, descriptions |
| `--text-muted` | `#55555e` | Captions, footnotes, timestamps |
| `--accent` / `--gold` | `#c8aa50` | **ONLY**: CTA buttons, key metrics, hover states, agent tags |
| `--accent-hover` | `#d4b85c` | Button hover |

### Gold Rules
- Gold for: CTA buttons, key numbers ($40-60K, 92%), hover accents, agent tags
- **NOT** for: body text, headings, borders (unless interactive)
- Badges (HIGH/MEDIUM): white bg `rgba(255,255,255,0.10)` + white text `#ffffff`

---

## Typography

### Font Stack
| Token | Font | Usage |
|-------|------|-------|
| `--font-display` | `Geist` | Headlines, hero, section headers |
| `--font-body` | `Inter` | Body text, descriptions, UI |
| `--font-mono` | `JetBrains Mono` | Data, metrics, code, timestamps, tags |

### Scale

| Element | Font | Size | Weight | Letter-spacing | Line-height |
|---------|------|------|--------|---------------|-------------|
| Hero headline | Geist | `3.75rem` (60px) | 600 | `-0.025em` | 1.05 |
| Hero subtitle | Geist | `1.6rem` (25.6px) | 600 | `-0.02em` | 1.3 |
| Section heading | Geist | `2.5rem` (40px) | 600 | `-0.025em` | — |
| Card title | Geist | `1.25rem` (20px) | 500 | — | 1.3 |
| Body text | Inter | `1.0625rem` (17px) | 400 | — | 1.6-1.8 |
| Subtitle / desc | Inter | `1rem` (16px) | 400 | — | 1.6 |
| Hero detail | Geist | `1.0625rem` (17px) | 400 | — | 1.6 |
| KPI numbers | JetBrains Mono | `4rem` (64px) | 600 | `-0.03em` | 1 |
| KPI labels | Inter | `1.0625rem` (17px) | 400 | — | — |
| Mono tags | JetBrains Mono | `0.75rem` (12px) | 500 | — | — |
| Mono small | JetBrains Mono | `0.6875rem` (11px) | 400-500 | `0.06em` | — |
| Report meta | JetBrains Mono | `0.75rem` (12px) | 400 | — | — |
| Nav link | Inter | `0.875rem` (14px) | 500 | — | — |
| Button | Inter | `0.875rem` (14px) | 500 | — | — |
| Footer link | Inter | `0.875rem` (14px) | 400 | — | — |

### 5-Step Scale (simplified)
1. **Hero** — 3.75rem (60px)
2. **Section Header** — 2.5rem (40px)
3. **Subtitle / Card Title** — 1.25-1.6rem (20-25px)
4. **Body** — 1.0625rem (17px) — ONE size for all body text
5. **Small / Mono** — 0.75rem (12px) — ONE size for all small text

### Rules
1. **Headlines always Geist**, body always Inter, data always JetBrains Mono
2. **Letter-spacing on large text**: Always `-0.02em` or tighter on anything >1.5rem
3. **No font mixing within a block** — pick one family per element
4. Mobile: Hero shrinks to `2rem`, section heads stay `2rem`

---

## Spacing

| Token | Value | Usage |
|-------|-------|-------|
| `--space-section` | `120px` | Vertical padding between sections (`padding: 120px 0`) |
| Container max-width | `1440px` | Outer container |
| Container padding | `48px` horizontal | Desktop side padding |
| Card padding | `32px` | Inside cards |
| Card gap | `24-32px` | Between grid cards |
| Hero padding | `160px top, 120px bottom` | Hero section |
| Element gap (small) | `8-12px` | Between tags, small elements |
| Element gap (medium) | `16-24px` | Between cards, form elements |
| Element gap (large) | `40-48px` | Between heading and content |

### Mobile Overrides
| Element | Mobile Value |
|---------|-------------|
| Container padding | `16px` |
| Section padding | `48px 0` |
| Hero padding | `100px top, 80px bottom` |

---

## Components

### Buttons
| Type | Background | Border | Text Color | Padding | Radius |
|------|-----------|--------|------------|---------|--------|
| Primary | `#c8aa50` | none | `#fff` | `10px 20px` | `8px` |
| Secondary | transparent | `1px solid var(--border-default)` | `--text-primary` | `10px 20px` | `8px` |
| Nav CTA | `#c8aa50` | none | `#fff` | `8px 16px` | `8px` |

### Cards
- Background: `var(--bg-surface)` or `#08080c`
- Border: `1px solid rgba(255,255,255,0.08-0.12)`
- Border-radius: `16px`
- Padding: `32px`
- Hover: `border-color: rgba(200,170,80,0.25); box-shadow: 0 0 30px rgba(200,170,80,0.06)`

### Report Preview Cards (Showcase)
- Background: `#111116`
- Border: `1px solid rgba(255,255,255,0.08)`
- Border-radius: `16px`
- Full-width inside container
- Internal grid: `grid-template-columns: 1fr 1fr` with `gap: 40px`

### Agent Tags
- Font: JetBrains Mono `0.65rem`
- Padding: `3px 8px`
- Border: `1px solid rgba(200,170,80,0.25)`
- Background: `rgba(200,170,80,0.12)`
- Color: `#c8aa50`
- Radius: `5px`

### Research Cards
- Background: `#08080c`
- Border: `1px solid rgba(255,255,255,0.12)`
- Radius: `16px`
- Padding: `32px`
- Grid: `repeat(3, 1fr)` with `gap: 24px`

---

## Effects

### Hero Glow
```css
.hero::before {
  background: radial-gradient(ellipse at 50% 0%, rgba(200,170,80,0.07) 0%, rgba(200,170,80,0.03) 30%, transparent 70%);
}
```

### Dot Grid (on select sections)
```css
.dot-grid::before {
  background-image: radial-gradient(rgba(255,255,255,0.04) 1px, transparent 1px);
  background-size: 32px 32px;
}
```

### Scroll Fade-In
```css
.fade-in { opacity:0; transform:translateY(24px); transition:opacity 0.7s ease-out, transform 0.7s ease-out; }
.fade-in.visible { opacity:1; transform:translateY(0); }
```
Applied via `IntersectionObserver` with `threshold: 0.1`.

### Logo Pulse
```css
@keyframes logo-pulse { 0%,100%{scale(1)} 50%{scale(1.3)} }
```
3 rings: dot (10px), ring1 (18px, 20% opacity), ring2 (26px, 5% opacity, animated).

---

## Grid System

| Layout | Columns | Gap | Usage |
|--------|---------|-----|-------|
| Trust cards | `repeat(3, 1fr)` | `32px` | Why-grid section |
| Research cards | `repeat(3, 1fr)` | `24px` | Published Research |
| Report internal | `1fr 1fr` | `40px` | Inside report previews |
| KPIs | flexbox, `gap: 120px` | — | Centered row |
| Mobile fallback | `1fr` | `16px` | All grids collapse |

---

## Page Structure (index.html)

1. **Nav** (sticky, blur backdrop)
2. **Hero** (glow behind, centered text)
3. **Product Showcase** (3 tabs, report previews)
4. **Terminal Demo** (interactive, tags, animated output)
5. **Multiplier** (centered text + CTA)
6. **Trust Cards + KPIs** (3-col grid + centered metrics)
7. **Published Research** (3-col card grid)
8. **Why I built this** (photo + text, flex layout)
9. **Footer** (via shared/footer.js — CTA + 4-col links + copyright)

---

## Don'ts
- ❌ No white sections/backgrounds — everything is dark
- ❌ No parallax — it's dated
- ❌ No gold for body text or non-interactive elements
- ❌ No font-size above `3.75rem` (hero only)
- ❌ No border-radius above `16px`
- ❌ No shadows except subtle gold glow on hover
- ❌ No letter-spacing > 0 on headlines (always negative or zero)

---

*Last updated: 2026-02-16*
*Source of truth: index.html commit `7c75a0c`*
