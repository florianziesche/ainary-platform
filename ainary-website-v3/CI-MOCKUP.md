# Ainary Ventures — CI Mockup
**Based on DESIGN-SPEC-V3.md**  
**Date:** February 7, 2026

---

## Visual Identity Overview

### Color Palette

```
MONOCHROME FOUNDATION (95% of design)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

██ #070b15  bg-deep      | Deepest background
██ #0a0f1e  bg-base      | Primary background  
██ #0f1420  bg-card      | Card backgrounds
██ #14192a  bg-hover     | Hover states

██ #ffffff  white-pure   | Headlines, primary text
██ #e8e6df  white-warm   | Body text (slightly warm)
██ #a8a8b2  gray-light   | Secondary text
██ #8a8a94  gray-mid     | Tertiary text
██ #5c5c66  gray-dark    | Disabled states
██ #1f2530  gray-rule    | Borders, dividers


GOLD SPECTRUM (5% strategic accents)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

██ #d4a853  gold-warm    | Hero, primary CTAs
██ #c8aa50  gold-base    | Links, active states
██ #b09a45  gold-cool    | Secondary elements
██ #e8d89f  gold-pale    | Highlights, code backgrounds
██ #9d7f3b  gold-deep    | Depth, shadows, focus
```

---

## Typography System

```
FONT STACK
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Display:   Inter Display Variable (H1, H2)
Body/UI:   Inter Variable (paragraphs, nav, buttons)
Mono:      JetBrains Mono Variable (code, data)


SCALE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

H1 (Hero)       64-68px   600 weight   -0.025em   line-height 1.1
H2 (Section)    42px      600 weight   -0.02em    line-height 1.2
H3 (Subsection) 28px      600 weight   -0.01em    line-height 1.25
Body (Standard) 18px      400 weight   0          line-height 1.7
Body (Small)    16px      400 weight   0          line-height 1.6
Meta/Caps       14px      500 weight   0.06em     line-height 1.5
```

---

## Logo Variations

```
FULL LOGO (Primary)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

╔═══════════════════════════════════╗
║                                   ║
║     ╔═╗╦╔╗╔╔═╗╦═╗╦ ╦             ║
║     ╠═╣║║║║╠═╣╠╦╝╚╦╝             ║
║     ╩ ╩╩╝╚╝╩ ╩╩╚═ ╩              ║
║                                   ║
║     VENTURES                      ║
║                                   ║
╚═══════════════════════════════════╝

Usage: Main site header, documents
Color: White (#ffffff) on dark backgrounds
      Gold-warm (#d4a853) on light backgrounds


MONOGRAM (Icon)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

╔═══════╗
║       ║
║   A   ║     Stylized "A" with gold accent
║  ═══  ║     32×32px minimum
║   V   ║     Used for: Favicon, social avatars
║       ║
╚═══════╝


WORDMARK (Minimal)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

AINARY

Usage: Text-only contexts, email signatures
Font: Inter Display, 700 weight, all caps
```

---

## Component Examples

### Hero Section Mockup

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│                        [Dark bg with gold shimmer]                  │
│                                                                     │
│                                                                     │
│                    ╔══════════════════════╗                         │
│                    ║ ● Currently: Building║  [Status badge]        │
│                    ╚══════════════════════╝                         │
│                                                                     │
│                                                                     │
│               We Build AI Systems                                   │
│               That Go Into Production.      [64px, white-pure]     │
│               Not PowerPoints.              [word "Production"     │
│                                              in gold-warm]          │
│                                                                     │
│         AI-native platform for operators and investors.             │
│         We build, invest, deploy, and teach — compounding           │
│         expertise in manufacturing and legal AI.                    │
│                           [20px, gray-light]                        │
│                                                                     │
│                                                                     │
│           ┌──────────────────┐  ┌──────────────────┐               │
│           │  For Founders →  │  │   Our Work →     │               │
│           └──────────────────┘  └──────────────────┘               │
│              [gold solid]         [gold outline]                    │
│                                                                     │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Service Card Mockup (with Gold Spectrum)

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│    ┌───────────────┐  ┌───────────────┐  ┌───────────────┐        │
│    │               │  │               │  │               │        │
│    │    🏭         │  │    📰         │  │    ⚖️          │        │
│    │ [gold-warm]   │  │ [gold-base]   │  │ [gold-cool]   │        │
│    │               │  │               │  │               │        │
│    │ Manufacturing │  │  Media &      │  │  Legal        │        │
│    │ AI            │  │  Publishing   │  │  Tech         │        │
│    │               │  │               │  │               │        │
│    │ Build AI...   │  │ Transform...  │  │ Deploy AI...  │        │
│    │ [16px text]   │  │ [16px text]   │  │ [16px text]   │        │
│    │               │  │               │  │               │        │
│    │ Learn more →  │  │ Learn more →  │  │ Learn more →  │        │
│    │ [gold-warm]   │  │ [gold-base]   │  │ [gold-cool]   │        │
│    │               │  │               │  │               │        │
│    └───────────────┘  └───────────────┘  └───────────────┘        │
│                                                                     │
│    ┌───────────────┐  ┌───────────────┐  ┌───────────────┐        │
│    │               │  │               │  │               │        │
│    │    🗂️          │  │    🎓         │  │    💼         │        │
│    │ [gold-pale]   │  │ [gold-deep]   │  │ [gold-warm]   │        │
│    │               │  │               │  │               │        │
│    │ Office &      │  │  Workshops    │  │  Advisory     │        │
│    │ Operations    │  │  & Training   │  │  & Strategy   │        │
│    │               │  │               │  │               │        │
│    │ Optimize...   │  │ Learn how...  │  │ Strategic...  │        │
│    │ [16px text]   │  │ [16px text]   │  │ [16px text]   │        │
│    │               │  │               │  │               │        │
│    │ Learn more →  │  │ Learn more →  │  │ Learn more →  │        │
│    │ [gold-pale]   │  │ [gold-deep]   │  │ [gold-warm]   │        │
│    │               │  │               │  │               │        │
│    └───────────────┘  └───────────────┘  └───────────────┘        │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘

Each service card gets a unique gold from the spectrum
Background: bg-card (#0f1420)
Hover: bg-hover (#14192a) + translateY(-4px) + gold glow
```

### Navigation Mockup (Desktop)

```
┌─────────────────────────────────────────────────────────────────────┐
│ [Glassmorphism: rgba(10,15,30,0.92) + backdrop-blur(12px)]         │
│ ─────────────────────────────────────────────────────────────────── │
│                                                                     │
│  AINARY          Consulting  Fund  Portfolio  Insights  About      │
│  [gold-warm]     [gray-light, hover → white-pure]                  │
│                                                                     │
│                                                  ┌──────────────┐   │
│                                                  │ Get in Touch │   │
│                                                  └──────────────┘   │
│                                                   [gold button]     │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘

Height: 72px default → 56px on scroll
Sticky, z-index 100
Border-bottom: 1px solid gray-rule (#1f2530)
```

### Button Variations

```
PRIMARY (Gold Solid)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┌────────────────────┐
│  For Founders →    │  Background: gold-warm (#d4a853)
└────────────────────┘  Text: bg-deep (#070b15)
                        Hover: gold-base + translateY(-2px)
                        Padding: 14px 32px
                        Border-radius: 8px


SECONDARY (Gold Outline)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┌────────────────────┐
│  Our Work →        │  Background: transparent
└────────────────────┘  Border: 2px solid gold-warm
                        Text: white-pure
                        Hover: bg gold-warm/10


TERTIARY (Text Only)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Learn more →            No background
                        Underline: gold-warm
                        Hover: text → gold-base
```

---

## Spacing System (8px Grid)

```
SCALE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0    0px     (none)
xs   8px     Component gaps
sm   16px    Internal spacing
md   24px    Card padding
lg   40px    Section spacing
xl   64px    Large gaps
2xl  96px    Section breaks
3xl  120px   Section vertical padding
4xl  160px   Large section vertical padding


CONTAINER WIDTHS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

narrow    560px   (Text-heavy content)
default   900px   (Homepage sections)
wide      1200px  (Service grids, portfolios)
full      1440px  (Max width, hero backgrounds)
```

---

## Responsive Breakpoints

```
MOBILE FIRST
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Base        320px+   (Mobile portrait)
sm          375px+   (Larger phones)
md          768px+   (Tablet portrait)
lg          1024px+  (Desktop small)
xl          1440px+  (Desktop large)
2xl         1920px+  (4K displays)


LAYOUT CHANGES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

< 768px:  Single column, stacked CTAs, hamburger nav
768-1024: 2-column grids, side-by-side CTAs
> 1024px: 3-column grids, full nav, enhanced spacing
```

---

## Animation Specifications

### Gold Shimmer (Hero Background)

```css
@keyframes goldShimmer {
  0%, 100% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
}

Background:
linear-gradient(
  135deg,
  #070b15 0%,      ← bg-deep
  #0a0f1e 40%,     ← bg-base
  rgba(212,168,83,0.05) 50%,  ← gold-warm at 5% opacity
  #0a0f1e 60%,     ← bg-base
  #070b15 100%     ← bg-deep
)
background-size: 200% 200%
animation: goldShimmer 5s ease-in-out infinite
```

### Scroll Fade-In

```
Element enters viewport:
  opacity: 0 → 1
  transform: translateY(24px) → translateY(0)
  duration: 0.5s
  easing: ease-out
  threshold: 15% visible
```

### Hover States

```
Cards:        translateY(-4px) + gold glow shadow
Buttons:      translateY(-2px) + brightness 1.1
Links:        underline color shift
Portfolio:    grayscale(100%) → grayscale(0%) + scale(1.05)
```

---

## Example Pages

### Homepage Layout

```
┌─────────────────────────────────────────────────────────────────────┐
│ NAVIGATION (sticky, glassmorphism, 72px)                            │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│ HERO (85vh, gold shimmer bg, center-aligned)                        │
│   - Status badge                                                    │
│   - Headline (64px)                                                 │
│   - Subhead (20px)                                                  │
│   - Dual CTAs                                                       │
│                                                                     │
├─────────────────────────────────────────────────────────────────────┤
│ ABOUT (120px vertical padding)                                      │
│   - Vision/Mission                                                  │
│   - Flywheel visual                                                 │
│                                                                     │
├─────────────────────────────────────────────────────────────────────┤
│ SERVICES GRID (120px vertical padding)                              │
│   - 6 service cards in 3×2 grid                                     │
│   - Each with unique gold from spectrum                             │
│                                                                     │
├─────────────────────────────────────────────────────────────────────┤
│ PORTFOLIO SHOWCASE (120px vertical padding)                         │
│   - Logo grid, 4 columns                                            │
│   - Grayscale → color on hover                                      │
│                                                                     │
├─────────────────────────────────────────────────────────────────────┤
│ INSIGHTS PREVIEW (120px vertical padding)                           │
│   - Latest 3 articles                                               │
│   - Category badges                                                 │
│                                                                     │
├─────────────────────────────────────────────────────────────────────┤
│ NOT A FIT (120px vertical padding)                                  │
│   - Transparency section                                            │
│   - 4 cards: "When NOT to hire us"                                  │
│                                                                     │
├─────────────────────────────────────────────────────────────────────┤
│ CONTACT CTA (120px vertical padding)                                │
│   - Email + social links                                            │
│                                                                     │
├─────────────────────────────────────────────────────────────────────┤
│ FOOTER (3-column, 80px vertical padding)                            │
│   - Brand + tagline                                                 │
│   - Navigation                                                      │
│   - Legal links                                                     │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Key Design Principles

1. **Monochrome Restraint (95%) + Strategic Boldness (5%)**
   - Dark backgrounds dominate
   - Gold only for CTAs, links, and accents
   - Never use gold for large areas or backgrounds

2. **Gold Spectrum = Differentiation**
   - Each service category gets unique gold
   - Creates visual hierarchy without color explosion
   - Stays within monochrome restraint philosophy

3. **Generous Whitespace = Luxury Signal**
   - 120px+ section padding
   - Never cramped, always breathing room
   - "We don't need to cram content"

4. **Typography Hierarchy**
   - Large body text (18px minimum)
   - Dramatic heading scales (64px hero)
   - Negative letter-spacing on large text
   - High line-height for readability (1.7)

5. **Restrained Animation**
   - ONE signature effect (gold shimmer)
   - All other animations subtle (fade, lift)
   - Respects prefers-reduced-motion
   - No decorative motion

6. **Accessibility First**
   - WCAG AA minimum
   - All gold/dark contrasts validated
   - Keyboard navigation
   - Screen reader friendly
   - Focus indicators (gold ring)

---

## Usage Guidelines

### ✅ DO

- Use gold sparingly (≤10% per viewport)
- Maintain 120px+ vertical section padding
- Use Inter for all typography
- Keep body text at 18px minimum
- Use monochrome for 95% of design
- Apply gold spectrum to differentiate services
- Generous whitespace between elements
- Dark backgrounds with light text

### ❌ DON'T

- Use gold for backgrounds or large areas
- Mix other accent colors
- Cramped layouts (<80px section padding)
- Small body text (<16px)
- Decorative animations
- Bright or saturated colors
- Light backgrounds (except for accent cards)
- Multiple fonts beyond Inter + JetBrains Mono

---

## File Exports Needed

### Logos
- `logo-full.svg` (primary, white version)
- `logo-full-gold.svg` (gold version for light backgrounds)
- `logo-mono.svg` (monogram icon, 32×32px minimum)
- `logo-wordmark.svg` (text only)

### Fonts
- `inter-var.woff2` (Inter Variable)
- `inter-display-var.woff2` (Inter Display Variable)
- `jetbrains-mono-var.woff2` (JetBrains Mono Variable)

### Icons
- Service icons (🏭 📰 ⚖️ 🗂️ 🎓 💼) as SVGs
- UI icons (menu, close, arrow-right, external-link) as SVGs
- Social icons (Twitter, LinkedIn, GitHub) as SVGs

### Favicons
- `favicon.svg` (scalable)
- `favicon-32x32.png`
- `favicon-16x16.png`
- `apple-touch-icon.png` (180×180px)

---

**CI Mockup Complete**  
**Ready for:** Design review, implementation, brand guidelines

This mockup defines the complete visual identity system for Ainary Ventures based on DESIGN-SPEC-V3.md. All measurements, colors, and specifications are production-ready.
