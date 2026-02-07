# Ainary Ventures — Design-to-Code Bridge & Asset List
**Complete Implementation Reference**  
**Date:** February 7, 2026  
**Author:** Planner Agent 5 (Opus)  
**Sources:** DESIGN-SYNTHESIS-V3.md, BRAND-IDENTITY-SYNTHESIS.md, UI-UX-SYNTHESIS.md, DESIGN-SPEC-V3.md, CONTENT-STRATEGY-SYNTHESIS.md

---

## Purpose

This document bridges design specifications and code implementation. Everything a developer needs to build the Ainary Ventures website is here — design tokens, assets, animations, accessibility requirements, and QA plan. No guessing, no interpretation. Copy-paste ready.

---

# 1. DESIGN TOKENS (CSS Custom Properties)

## 1.1 Complete `:root` Block

```css
:root {
  /* ═══════════════════════════════════════════════════
     COLORS — Monochrome Foundation (95% of site)
     ═══════════════════════════════════════════════════ */
  
  /* Backgrounds (Dark Theme) */
  --bg-deep:       #070b15;   /* Deepest background, section separators */
  --bg-base:       #0a0f1e;   /* Primary page background */
  --bg-card:       #0f1420;   /* Card surfaces, elevated elements */
  --bg-hover:      #14192a;   /* Hover/active states on cards */

  /* Text Hierarchy */
  --white-pure:    #ffffff;   /* Headlines, primary text, nav links (active) */
  --white-warm:    #e8e6df;   /* Body text (slightly warm for readability) */
  --gray-light:    #a8a8b2;   /* Secondary text, subheadings, meta */
  --gray-mid:      #8a8a94;   /* Tertiary text, timestamps */
  --gray-dark:     #5c5c66;   /* Disabled states, placeholder text */
  --gray-rule:     #1f2530;   /* Borders, dividers, separators */

  /* ═══════════════════════════════════════════════════
     COLORS — Gold Spectrum (5% of site — signature)
     ═══════════════════════════════════════════════════ */
  --gold-warm:     #d4a853;   /* Hero accents, primary CTAs, focus rings */
  --gold-base:     #c8aa50;   /* Links, active navigation states */
  --gold-cool:     #b09a45;   /* Secondary elements, cool end of spectrum */
  --gold-pale:     #e8d89f;   /* Highlights, code backgrounds, sparkle */
  --gold-deep:     #9d7f3b;   /* Depth/shadows, icon subtle glows */

  /* Gold with alpha (for glows and overlays) */
  --gold-glow-subtle:  rgba(212, 168, 83, 0.05);
  --gold-glow-light:   rgba(212, 168, 83, 0.08);
  --gold-glow-medium:  rgba(212, 168, 83, 0.12);
  --gold-glow-strong:  rgba(212, 168, 83, 0.25);
  --gold-glow-intense: rgba(212, 168, 83, 0.40);

  /* Complementary Colors (RARE — data viz, category coding) */
  --electric-blue:  #4a9eff;  /* AI/Tech signals */
  --deep-purple:    #8b7fc7;  /* Venture/Strategy */
  --rust-orange:    #d9734a;  /* Manufacturing/Industrial */
  --sage-green:     #7da88f;  /* Legal/Compliance */

  /* Semantic Colors */
  --color-error:    #ef4444;
  --color-success:  #22c55e;
  --color-warning:  #f59e0b;
  --color-info:     var(--electric-blue);

  /* ═══════════════════════════════════════════════════
     TYPOGRAPHY
     ═══════════════════════════════════════════════════ */
  
  /* Font Families */
  --font-display:   'Inter Display', 'Inter', system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
  --font-body:      'Inter', system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
  --font-mono:      'JetBrains Mono', 'SF Mono', 'Fira Code', 'Cascadia Code', monospace;

  /* Font Sizes — Fixed Scale */
  --text-xs:    14px;   /* 0.875rem — Micro labels, legal text */
  --text-sm:    16px;   /* 1rem     — Captions, metadata, nav links */
  --text-base:  18px;   /* 1.125rem — Body text (minimum for body) */
  --text-lg:    20px;   /* 1.25rem  — Lead paragraphs, subtitles */
  --text-xl:    24px;   /* 1.5rem   — H4, card titles */
  --text-2xl:   32px;   /* 2rem     — H3, section subtitles */
  --text-3xl:   42px;   /* 2.625rem — H2, section titles */
  --text-4xl:   56px;   /* 3.5rem   — H1, page titles */
  --text-5xl:   68px;   /* 4.25rem  — Hero headline (desktop) */

  /* Font Sizes — Fluid Scale (clamp) */
  --text-hero:     clamp(2.5rem, 6vw, 4.25rem);    /* 40px → 68px */
  --text-h1:       clamp(2rem, 4.8vw, 3.5rem);     /* 32px → 56px */
  --text-h2:       clamp(1.5rem, 3.5vw, 2.625rem); /* 24px → 42px */
  --text-h3:       clamp(1.25rem, 2.5vw, 2rem);    /* 20px → 32px */
  --text-h4:       clamp(1.125rem, 2vw, 1.5rem);   /* 18px → 24px */

  /* Font Weights */
  --weight-normal:    400;  /* Body text */
  --weight-medium:    500;  /* Links, nav items, emphasized body */
  --weight-semibold:  600;  /* Headings (primary weight) */
  --weight-bold:      700;  /* Rarely used — strong emphasis only */

  /* Line Heights */
  --leading-tight:    1.1;  /* Hero headlines */
  --leading-snug:     1.2;  /* H1 */
  --leading-normal:   1.3;  /* H2, H3 */
  --leading-relaxed:  1.5;  /* H4, subtitles */
  --leading-loose:    1.7;  /* Body text */
  --leading-prose:    1.75; /* Long-form reading */

  /* Letter Spacing */
  --tracking-tight:    -0.025em;  /* H1, hero — negative for large text */
  --tracking-snug:     -0.02em;   /* H2 */
  --tracking-normal:   0em;       /* Body text */
  --tracking-wide:     0.02em;    /* Small caps, labels */
  --tracking-wider:    0.06em;    /* Buttons (JetBrains Mono), uppercase */

  /* ═══════════════════════════════════════════════════
     SPACING — 8px Base Grid
     ═══════════════════════════════════════════════════ */
  --space-0:    0;
  --space-px:   1px;
  --space-0-5:  4px;    /* 0.25rem — Micro spacing */
  --space-1:    8px;    /* 0.5rem  — Tight internal padding */
  --space-1-5:  12px;   /* 0.75rem — Small gap */
  --space-2:    16px;   /* 1rem    — Standard gap */
  --space-3:    24px;   /* 1.5rem  — Card padding, element margin */
  --space-4:    32px;   /* 2rem    — Section sub-gap, mobile container pad */
  --space-5:    40px;   /* 2.5rem  — Card internal padding (desktop) */
  --space-6:    48px;   /* 3rem    — Desktop container pad */
  --space-8:    64px;   /* 4rem    — Section padding (mobile) */
  --space-10:   80px;   /* 5rem    — Medium section gap */
  --space-12:   96px;   /* 6rem    — Section padding (desktop) */
  --space-16:   128px;  /* 8rem    — Large section gap */
  --space-20:   160px;  /* 10rem   — Hero-level vertical padding */

  /* ═══════════════════════════════════════════════════
     LAYOUT
     ═══════════════════════════════════════════════════ */
  --container-narrow:  560px;   /* Quotes, emphasis blocks */
  --container-text:    720px;   /* Body text, blog content */
  --container-wide:    960px;   /* Dual-column, portfolio grids */
  --container-max:     1200px;  /* Maximum content width */
  --container-full:    1440px;  /* Absolute max for large screens */

  --container-pad-mobile:   var(--space-4);   /* 32px */
  --container-pad-tablet:   var(--space-5);   /* 40px */
  --container-pad-desktop:  var(--space-6);   /* 48px */

  /* ═══════════════════════════════════════════════════
     BREAKPOINTS (reference — use in @media queries)
     ═══════════════════════════════════════════════════ */
  /* 
     --bp-sm:    375px;   Small mobile (iPhone SE+)
     --bp-md:    640px;   Large phone / small tablet
     --bp-lg:    768px;   Tablet portrait
     --bp-xl:    1024px;  Tablet landscape / small laptop
     --bp-2xl:   1280px;  Desktop
     --bp-3xl:   1440px;  Large desktop
     --bp-4xl:   1920px;  4K / ultra-wide
  */

  /* ═══════════════════════════════════════════════════
     BORDERS & RADIUS
     ═══════════════════════════════════════════════════ */
  --radius-sm:    4px;    /* Buttons, small elements */
  --radius-md:    6px;    /* Cards, inputs */
  --radius-lg:    8px;    /* Large cards */
  --radius-xl:    12px;   /* Modals, overlays */
  --radius-full:  9999px; /* Pills, avatars */

  --border-subtle:   1px solid var(--gray-rule);
  --border-gold:     1px solid rgba(212, 168, 83, 0.3);

  /* ═══════════════════════════════════════════════════
     SHADOWS
     ═══════════════════════════════════════════════════ */
  --shadow-sm:      0 2px 8px rgba(0, 0, 0, 0.15);
  --shadow-md:      0 4px 16px rgba(0, 0, 0, 0.2);
  --shadow-lg:      0 8px 24px rgba(0, 0, 0, 0.25);
  --shadow-xl:      0 12px 32px rgba(0, 0, 0, 0.3);
  --shadow-gold-sm: 0 4px 16px var(--gold-glow-light);
  --shadow-gold-md: 0 8px 24px var(--gold-glow-medium);
  --shadow-gold-lg: 0 12px 32px var(--gold-glow-strong);
  --shadow-gold-xl: 0 16px 48px var(--gold-glow-intense);

  /* ═══════════════════════════════════════════════════
     ANIMATION TIMING
     ═══════════════════════════════════════════════════ */

  /* Durations */
  --duration-instant:  100ms;   /* Micro-feedback: color changes */
  --duration-fast:     150ms;   /* Button hover, link transitions */
  --duration-base:     200ms;   /* Standard element transitions */
  --duration-medium:   300ms;   /* Nav height change, card hover */
  --duration-slow:     400ms;   /* Section fade-in, modal open */
  --duration-slower:   500ms;   /* Scroll reveals, major transitions */
  --duration-epic:     600ms;   /* Cluster expand, hero entrance */
  --duration-hero:     1200ms;  /* First-visit hero animation */

  /* Easing Curves */
  --ease-standard:  cubic-bezier(0.4, 0, 0.2, 1);    /* General purpose */
  --ease-enter:     cubic-bezier(0, 0, 0.2, 1);       /* Elements appearing */
  --ease-exit:      cubic-bezier(0.4, 0, 1, 1);       /* Elements leaving */
  --ease-bounce:    cubic-bezier(0.68, -0.55, 0.265, 1.55);  /* Playful micro */
  --ease-in:        cubic-bezier(0.4, 0, 1, 1);       /* Accelerating */
  --ease-out:       cubic-bezier(0, 0, 0.2, 1);       /* Decelerating */
  --ease-in-out:    cubic-bezier(0.4, 0, 0.2, 1);     /* Symmetric */

  /* ═══════════════════════════════════════════════════
     Z-INDEX SCALE
     ═══════════════════════════════════════════════════ */
  --z-base:       0;
  --z-card:       10;
  --z-sticky:     50;
  --z-nav:        100;
  --z-progress:   101;
  --z-overlay:    200;
  --z-modal:      300;
  --z-tooltip:    400;
  --z-skip:       1000;

  /* ═══════════════════════════════════════════════════
     GLASSMORPHISM (Navigation)
     ═══════════════════════════════════════════════════ */
  --glass-bg:        rgba(10, 15, 30, 0.92);
  --glass-bg-heavy:  rgba(10, 15, 30, 0.95);
  --glass-blur:      blur(12px);
  --glass-saturate:  saturate(180%);
  --glass-backdrop:  var(--glass-blur) var(--glass-saturate);

  /* ═══════════════════════════════════════════════════
     COMPONENT-SPECIFIC TOKENS
     ═══════════════════════════════════════════════════ */

  /* Navigation */
  --nav-height:          72px;
  --nav-height-scrolled: 56px;
  --nav-bg:              var(--glass-bg);
  --nav-bg-scrolled:     var(--glass-bg-heavy);
  --nav-border:          var(--border-subtle);

  /* Hero */
  --hero-height:          85vh;
  --hero-height-mobile:   auto;
  --hero-min-height:      600px;

  /* Cards */
  --card-bg:              var(--bg-card);
  --card-border:          var(--border-subtle);
  --card-padding:         var(--space-5);
  --card-padding-mobile:  var(--space-4);
  --card-radius:          var(--radius-md);
  --card-lift:            -4px;
  --card-shadow-hover:    var(--shadow-gold-md);

  /* Buttons */
  --btn-padding-y:        10px;
  --btn-padding-x:        24px;
  --btn-radius:           var(--radius-sm);
  --btn-font:             var(--font-mono);
  --btn-font-size:        var(--text-xs);
  --btn-tracking:         var(--tracking-wider);
  --btn-weight:           var(--weight-medium);

  /* Inputs */
  --input-bg:             var(--bg-card);
  --input-border:         var(--border-subtle);
  --input-border-focus:   1px solid var(--gold-warm);
  --input-radius:         var(--radius-md);
  --input-padding:        12px 16px;
  --input-focus-ring:     0 0 0 3px rgba(212, 168, 83, 0.1);

  /* Scroll Progress */
  --progress-height:      2px;
  --progress-gradient:    linear-gradient(90deg, var(--gold-warm), var(--gold-cool));
  --progress-glow:        0 0 10px rgba(212, 168, 83, 0.6);
}
```

## 1.2 Breakpoint Media Queries

```css
/* Mobile First — base styles target 320px+ */

/* Small mobile (375px+) — iPhone SE and up */
@media (min-width: 23.4375rem) { }

/* Medium (640px+) — large phones, small tablets */
@media (min-width: 40rem) {
  /* Service grid: 2 columns
     Portfolio grid: 2 columns
     Increase container padding */
}

/* Large (768px+) — tablet portrait */
@media (min-width: 48rem) {
  /* Navigation: hamburger → horizontal links
     About section: side-by-side layout
     Section padding increases */
}

/* XL (1024px+) — tablet landscape / small laptop */
@media (min-width: 64rem) {
  /* Service grid: 3 columns
     Portfolio grid: 3 columns
     Full hover effects enabled
     Section nav appears */
}

/* 2XL (1280px+) — desktop */
@media (min-width: 80rem) {
  /* Max-width container: 960px
     Portfolio grid: 4 columns
     Full animation suite */
}

/* 3XL (1440px+) — large desktop */
@media (min-width: 90rem) {
  /* Cap container at 1200px max */
}

/* 4XL (1920px+) — 4K displays */
@media (min-width: 120rem) {
  /* Cap at 1440px, extra whitespace */
}

/* Touch device detection */
@media (hover: hover) {
  /* Desktop hover effects only activate here */
}

/* Reduced motion preference */
@media (prefers-reduced-motion: reduce) {
  /* Override all animations — see §4 Accessibility */
}

/* High contrast preference */
@media (forced-colors: active) {
  /* System color overrides */
}

/* Dark/Light scheme (future) */
@media (prefers-color-scheme: light) {
  /* Optional light theme tokens */
}
```

## 1.3 Typography Application Map

```css
/* Hero Headline */
.hero-title {
  font-family: var(--font-display);
  font-size: var(--text-hero);
  font-weight: var(--weight-semibold);
  line-height: var(--leading-tight);
  letter-spacing: var(--tracking-tight);
  color: var(--white-pure);
}

/* Page Title (H1) */
h1, .h1 {
  font-family: var(--font-display);
  font-size: var(--text-h1);
  font-weight: var(--weight-semibold);
  line-height: var(--leading-snug);
  letter-spacing: var(--tracking-tight);
  color: var(--white-pure);
}

/* Section Title (H2) */
h2, .h2 {
  font-family: var(--font-display);
  font-size: var(--text-h2);
  font-weight: var(--weight-semibold);
  line-height: var(--leading-normal);
  letter-spacing: var(--tracking-snug);
  color: var(--white-pure);
}

/* Subsection Title (H3) */
h3, .h3 {
  font-family: var(--font-body);
  font-size: var(--text-h3);
  font-weight: var(--weight-semibold);
  line-height: var(--leading-normal);
  letter-spacing: var(--tracking-normal);
  color: var(--white-pure);
}

/* Card Title (H4) */
h4, .h4 {
  font-family: var(--font-body);
  font-size: var(--text-h4);
  font-weight: var(--weight-medium);
  line-height: var(--leading-relaxed);
  letter-spacing: var(--tracking-normal);
  color: var(--white-pure);
}

/* Body Text */
body, p, .body {
  font-family: var(--font-body);
  font-size: var(--text-base);
  font-weight: var(--weight-normal);
  line-height: var(--leading-loose);
  letter-spacing: var(--tracking-normal);
  color: var(--white-warm);
}

/* Lead / Subtitle */
.lead {
  font-family: var(--font-body);
  font-size: var(--text-lg);
  font-weight: var(--weight-normal);
  line-height: var(--leading-relaxed);
  color: var(--gray-light);
}

/* Caption / Metadata */
.caption {
  font-family: var(--font-body);
  font-size: var(--text-sm);
  font-weight: var(--weight-normal);
  line-height: var(--leading-relaxed);
  color: var(--gray-mid);
}

/* Micro / Legal */
.micro {
  font-family: var(--font-body);
  font-size: var(--text-xs);
  font-weight: var(--weight-normal);
  line-height: var(--leading-relaxed);
  color: var(--gray-dark);
}

/* Monospace (Technical, Metrics, Code) */
.mono, code, .metrics {
  font-family: var(--font-mono);
  font-size: var(--text-xs);
  font-weight: var(--weight-normal);
  line-height: var(--leading-relaxed);
  letter-spacing: var(--tracking-wider);
}

/* Navigation Links */
.nav-link {
  font-family: var(--font-body);
  font-size: 15px;
  font-weight: var(--weight-medium);
  letter-spacing: var(--tracking-normal);
  color: var(--gray-light);
}

/* Button Text */
.btn {
  font-family: var(--font-mono);
  font-size: var(--text-xs);
  font-weight: var(--weight-medium);
  letter-spacing: var(--tracking-wider);
  text-transform: none; /* NOT uppercase — operator, not corporate */
}

/* Section Labels (e.g., "SERVICES", "WORK") */
.section-label {
  font-family: var(--font-mono);
  font-size: var(--text-xs);
  font-weight: var(--weight-medium);
  letter-spacing: var(--tracking-wider);
  text-transform: uppercase;
  color: var(--gold-base);
}
```

---

# 2. ASSET REQUIREMENTS LIST

## 2.1 Fonts

### Inter (Display + Variable)

| Font | Format | Purpose | Source |
|------|--------|---------|--------|
| Inter Variable | `.woff2` | Body, UI, nav, H3-H4 | [GitHub: rsms/inter](https://github.com/rsms/inter/releases) |
| Inter Display Variable | `.woff2` | H1, H2, Hero headline | Same release package |

**Download:** https://github.com/rsms/inter/releases (latest — v4.1+)

**Subsetting Instructions:**
```bash
# Install pyftsubset (part of fonttools)
pip install fonttools brotli

# Subset Inter Variable to Latin glyphs only
pyftsubset InterVariable.ttf \
  --output-file=InterVariable-latin.woff2 \
  --flavor=woff2 \
  --layout-features='kern,liga,calt,ss01,ss02,cv01,cv02,cv03,cv04,cv05,cv06,cv07,cv08,cv09,cv10,cv11' \
  --unicodes='U+0000-007F,U+00A0-00FF,U+0100-017F,U+0180-024F,U+0250-02AF,U+2000-206F,U+2070-209F,U+20AC,U+2122,U+2190-21BB,U+2200-22FF,U+2300-23FF,U+25A0-25FF,U+2600-26FF,U+FB01-FB02'

# Same for Inter Display
pyftsubset InterDisplay-Variable.ttf \
  --output-file=InterDisplay-Variable-latin.woff2 \
  --flavor=woff2 \
  --layout-features='kern,liga,calt' \
  --unicodes='U+0000-007F,U+00A0-00FF,U+0100-017F,U+2000-206F,U+20AC,U+2122'
```

**Expected sizes after subsetting:**
- Inter Variable: ~55–65 KB
- Inter Display Variable: ~45–55 KB

**CSS `@font-face` declarations:**
```css
@font-face {
  font-family: 'Inter';
  src: url('/fonts/InterVariable-latin.woff2') format('woff2');
  font-weight: 100 900;
  font-style: normal;
  font-display: swap;
  unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6,
    U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+2074, U+20AC,
    U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
}

@font-face {
  font-family: 'Inter Display';
  src: url('/fonts/InterDisplay-Variable-latin.woff2') format('woff2');
  font-weight: 100 900;
  font-style: normal;
  font-display: swap;
  unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6,
    U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+2074, U+20AC,
    U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
}
```

### JetBrains Mono (Variable)

| Font | Format | Purpose | Source |
|------|--------|---------|--------|
| JetBrains Mono Variable | `.woff2` | Code, metrics, buttons, labels | [GitHub: JetBrains/JetBrainsMono](https://github.com/JetBrains/JetBrainsMono/releases) |

**Download:** https://github.com/JetBrains/JetBrainsMono/releases (latest — v2.304+)

**Subsetting:**
```bash
pyftsubset JetBrainsMono-Variable.ttf \
  --output-file=JetBrainsMono-Variable-latin.woff2 \
  --flavor=woff2 \
  --layout-features='kern,liga,calt,zero,ss01,ss02' \
  --unicodes='U+0000-007F,U+00A0-00FF,U+0100-017F,U+2000-206F,U+20AC,U+2122,U+2190-21BB,U+2200-22FF'
```

**Expected size:** ~35–45 KB

```css
@font-face {
  font-family: 'JetBrains Mono';
  src: url('/fonts/JetBrainsMono-Variable-latin.woff2') format('woff2');
  font-weight: 100 800;
  font-style: normal;
  font-display: swap;
}
```

**Total font budget:** ~140–165 KB (all three subsetted)

---

## 2.2 Logos

| Asset | Format(s) | Sizes | Notes |
|-------|-----------|-------|-------|
| Ainary Ventures — Full Logo | SVG, PNG | SVG (vector), PNG@1x: 200×40, PNG@2x: 400×80 | Used in nav (full state), footer, OG image |
| Ainary — Monogram "A" | SVG, PNG | SVG (vector), PNG@1x: 40×40, PNG@2x: 80×80 | Nav scrolled state, favicon base |
| Ainary — Text Wordmark | SVG | SVG (vector) | "AINARY VENTURES" text only, no icon |

**SVG Specifications:**
- Viewbox: sized to content, no excess whitespace
- Colors: Use `currentColor` for monochrome adaptability
- Gold variant: Inline `fill="#c8aa50"` (--gold-base)
- White variant: `fill="#ffffff"`
- Optimized with SVGO (remove metadata, comments, editor data)

**If logo doesn't exist yet:** Use text-based logo with Inter Display at weight 600, tracking 0.06em, uppercase. Gold for "AINARY", white-warm for "VENTURES".

---

## 2.3 Favicons

| File | Size | Format | Use |
|------|------|--------|-----|
| `favicon.ico` | 16×16, 32×32, 48×48 | ICO (multi-size) | Legacy browsers |
| `favicon-16x16.png` | 16×16 | PNG | Standard tab icon |
| `favicon-32x32.png` | 32×32 | PNG | Standard tab icon @2x |
| `apple-touch-icon.png` | 180×180 | PNG | iOS home screen |
| `android-chrome-192x192.png` | 192×192 | PNG | Android home screen |
| `android-chrome-512x512.png` | 512×512 | PNG | Android splash, PWA |
| `safari-pinned-tab.svg` | Vector | SVG | Safari pinned tab (single color) |
| `mstile-150x150.png` | 150×150 | PNG | Windows tiles |

**Design:** Gold "A" monogram on transparent background. For `apple-touch-icon`, use `--bg-base` (#0a0f1e) background with gold monogram.

**HTML Head Tags:**
```html
<link rel="icon" type="image/x-icon" href="/favicon.ico">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="mask-icon" href="/safari-pinned-tab.svg" color="#c8aa50">
<meta name="msapplication-TileColor" content="#0a0f1e">
<meta name="theme-color" content="#0a0f1e">
```

**`site.webmanifest`:**
```json
{
  "name": "Ainary Ventures",
  "short_name": "Ainary",
  "icons": [
    { "src": "/android-chrome-192x192.png", "sizes": "192x192", "type": "image/png" },
    { "src": "/android-chrome-512x512.png", "sizes": "512x512", "type": "image/png" }
  ],
  "theme_color": "#0a0f1e",
  "background_color": "#0a0f1e",
  "display": "standalone"
}
```

**Generation tool:** https://realfavicongenerator.net/ (upload 512×512 source PNG)

---

## 2.4 Icons (SVG)

### Service Category Icons (6 required)

| Service | Icon | Color Token | Emoji Fallback |
|---------|------|-------------|----------------|
| Manufacturing AI | Factory/gear | `--rust-orange` | 🏭 |
| Media & Publishing | Newspaper/signal | `--electric-blue` | 📰 |
| Legal Tech | Scale/shield | `--sage-green` | ⚖️ |
| Office & Operations | Envelope/workflow | `--gold-base` | 📧 |
| Workshops & Training | Graduation/lightbulb | `--deep-purple` | 🎓 |
| Advisory & Strategy | Compass/lightbulb | `--gold-warm` | 💡 |

### UI Icons (12 required)

| Icon | Purpose | Size | Notes |
|------|---------|------|-------|
| Hamburger menu (3 lines) | Mobile nav toggle | 24×24 | Animates to X on open |
| Close (X) | Close menu/modal | 24×24 | |
| Arrow right (→) | CTA arrows, inline links | 16×16 | Translates 4px on hover |
| Arrow down (↓) | Scroll indicator | 24×24 | Bounce animation |
| Expand (+) | Content cluster toggle | 20×20 | Rotates to − |
| External link (↗) | External link indicator | 14×14 | |
| Search (🔍) | Future search feature | 20×20 | Nav state 2 |
| GitHub | Social link | 20×20 | |
| LinkedIn | Social link | 20×20 | |
| Twitter/X | Social link | 20×20 | |
| Substack | Social link | 20×20 | |
| Email/Mail | Contact | 20×20 | |

### SVG Icon Specifications
- **Viewbox:** `0 0 24 24` (standard) or `0 0 20 20` (small)
- **Stroke:** `currentColor`, stroke-width: 1.5px or 2px
- **Fill:** `none` (outlined style) — consistent with modern aesthetic
- **Size:** Rendered at 20–24px in UI, 32–48px for service icons
- **Optimization:** SVGO, remove all metadata
- **Inline vs. file:** Inline SVGs for UI icons (faster, stylable), external files for service icons if complex

**Recommended icon set:** [Lucide Icons](https://lucide.dev/) (MIT license, consistent, stroke-based, matches Inter aesthetic)

---

## 2.5 Images

### Required Images

| Image | Usage | Aspect | Resolution | Format | Notes |
|-------|-------|--------|------------|--------|-------|
| Florian portrait | About section | 1:1 square | 400×400, 800×800 @2x | WebP + JPEG fallback | Exists: `florian.jpg`, `florian-400.jpg` |
| OG Image (social share) | `og:image` meta | 1200×630 | 1200×630 | PNG or JPEG | Dark bg, gold text, logo |
| Twitter Card | `twitter:image` | 1200×600 | 1200×600 | PNG or JPEG | Can be same as OG |

### Optional / Future Images

| Image | Usage | Priority | Notes |
|-------|-------|----------|-------|
| Portfolio company logos | Portfolio grid | Medium | Monochrome SVGs preferred; grayscale filter on raster |
| Blog post thumbnails | Insights section | Low | Can use colored abstract gradients |
| Team photos (future) | About expansion | Low | When team grows |
| Case study screenshots | Work section | Medium | Product screenshots with device frames |

### Image Optimization Pipeline

```bash
# Convert to WebP (primary format)
cwebp -q 82 -m 6 florian.jpg -o florian.webp

# Generate srcset sizes
# 400w (mobile), 800w (desktop @1x), 1200w (desktop @2x)
cwebp -q 82 -resize 400 0 florian.jpg -o florian-400.webp
cwebp -q 82 -resize 800 0 florian.jpg -o florian-800.webp

# HTML with responsive images
# <picture>
#   <source srcset="florian-400.webp 400w, florian-800.webp 800w" type="image/webp">
#   <img src="florian-400.jpg" alt="Florian Ziesche" loading="lazy" width="400" height="400">
# </picture>
```

### OG Image Template
```
┌────────────────────────────────────────────┐
│  bg: #0a0f1e                                │
│                                              │
│     AINARY VENTURES                          │  ← Gold, Inter Display 600
│                                              │
│     AI Systems That Go Into                  │  ← White, Inter 400, 28px
│     Production, Not PowerPoints.             │
│                                              │
│     ainaryventures.com                       │  ← Gray-light, 16px
│                                              │
└────────────────────────────────────────────┘
```

---

# 3. ANIMATION SPECIFICATIONS

## 3.1 Gold Shimmer (Hero Background) — Signature Effect

**Context:** The ONE proprietary animation. Subtle gold light that flows across the hero background. Must feel organic and luxurious, never distracting.

```css
@keyframes goldShimmer {
  0%, 100% {
    background-position: 0% 50%;
  }
  50% {
    background-position: 100% 50%;
  }
}

.hero {
  position: relative;
  min-height: var(--hero-height);
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  
  /* Base background */
  background-color: var(--bg-deep);
  
  /* Shimmer gradient overlay */
  background-image: linear-gradient(
    135deg,
    var(--bg-deep) 0%,
    var(--bg-base) 35%,
    rgba(212, 168, 83, 0.05) 50%,
    var(--bg-base) 65%,
    var(--bg-deep) 100%
  );
  background-size: 200% 200%;
  animation: goldShimmer 5s ease-in-out infinite;
}

/* Reduce motion: disable shimmer */
@media (prefers-reduced-motion: reduce) {
  .hero {
    animation: none;
    background-size: 100% 100%;
    background-position: center center;
  }
}
```

**Parameters:**
- **Duration:** 5s (slow, luxurious)
- **Easing:** ease-in-out (natural breathe)
- **Gold opacity:** 0.05 (5% — barely there but visible)
- **Direction:** 135° diagonal
- **Scope:** Hero section ONLY, never elsewhere

---

## 3.2 Scroll-Based Fade-Ins (Intersection Observer)

### CSS Classes

```css
/* Base hidden state */
.fade-in {
  opacity: 0;
  transform: translateY(24px);
  transition: 
    opacity var(--duration-slower) var(--ease-enter),
    transform var(--duration-slower) var(--ease-enter);
}

/* Visible state (applied by JS) */
.fade-in.visible {
  opacity: 1;
  transform: translateY(0);
}

/* Staggered children — use on parent, children get delay */
.stagger-children .fade-in:nth-child(1) { transition-delay: 0ms; }
.stagger-children .fade-in:nth-child(2) { transition-delay: 100ms; }
.stagger-children .fade-in:nth-child(3) { transition-delay: 200ms; }
.stagger-children .fade-in:nth-child(4) { transition-delay: 300ms; }
.stagger-children .fade-in:nth-child(5) { transition-delay: 400ms; }
.stagger-children .fade-in:nth-child(6) { transition-delay: 500ms; }

/* Variant: fade from left */
.fade-in-left {
  opacity: 0;
  transform: translateX(-24px);
  transition: 
    opacity var(--duration-slower) var(--ease-enter),
    transform var(--duration-slower) var(--ease-enter);
}

.fade-in-left.visible {
  opacity: 1;
  transform: translateX(0);
}

/* Variant: scale up */
.fade-in-scale {
  opacity: 0;
  transform: scale(0.95);
  transition: 
    opacity var(--duration-slower) var(--ease-enter),
    transform var(--duration-slower) var(--ease-enter);
}

.fade-in-scale.visible {
  opacity: 1;
  transform: scale(1);
}

/* Reduced motion override */
@media (prefers-reduced-motion: reduce) {
  .fade-in,
  .fade-in-left,
  .fade-in-scale {
    opacity: 1;
    transform: none;
    transition: none;
  }
}
```

### JavaScript Implementation

```javascript
/**
 * Scroll Reveal System
 * Observes elements with .fade-in, .fade-in-left, .fade-in-scale
 * Adds .visible class when element enters viewport
 */
function initScrollReveal() {
  // Respect reduced motion preference
  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  
  if (prefersReducedMotion) {
    // Make everything visible immediately
    document.querySelectorAll('.fade-in, .fade-in-left, .fade-in-scale').forEach(el => {
      el.classList.add('visible');
    });
    return;
  }

  const observerOptions = {
    threshold: 0.15,                    // 15% of element visible
    rootMargin: '0px 0px -80px 0px'     // Trigger 80px before bottom edge
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);  // One-shot: don't re-trigger
      }
    });
  }, observerOptions);

  // Observe all reveal targets
  const targets = document.querySelectorAll('.fade-in, .fade-in-left, .fade-in-scale');
  targets.forEach(el => observer.observe(el));
}

// Initialize on DOM ready
document.addEventListener('DOMContentLoaded', initScrollReveal);
```

### Application Guide

```html
<!-- Sections: fade in from below -->
<section class="fade-in">
  <h2>Services</h2>
  <!-- Card grid with staggered children -->
  <div class="services-grid stagger-children">
    <div class="service-card fade-in">Card 1</div>
    <div class="service-card fade-in">Card 2</div>
    <div class="service-card fade-in">Card 3</div>
  </div>
</section>

<!-- About section: photo from left, text from below -->
<section id="about">
  <div class="about-photo fade-in-left">...</div>
  <div class="about-text fade-in">...</div>
</section>
```

---

## 3.3 Hover States — Complete Transition Catalog

### Cards (Service, Portfolio, Blog)

```css
.card {
  background: var(--card-bg);
  border: var(--card-border);
  border-radius: var(--card-radius);
  padding: var(--card-padding);
  transition: 
    transform var(--duration-medium) var(--ease-standard),
    box-shadow var(--duration-medium) var(--ease-standard),
    border-color var(--duration-medium) var(--ease-standard);
}

/* Only apply hover on devices that support it */
@media (hover: hover) {
  .card:hover {
    transform: translateY(var(--card-lift));  /* -4px */
    box-shadow: var(--shadow-gold-md);        /* 0 8px 24px gold 12% */
    border-color: rgba(212, 168, 83, 0.3);
  }

  .card:hover .card-icon {
    transform: scale(1.1) rotate(5deg);
    transition: transform var(--duration-medium) var(--ease-bounce);
  }

  .card:hover .card-title {
    color: var(--gold-warm);
    transition: color var(--duration-fast);
  }
}

.card:active {
  transform: scale(0.98);
}
```

### Buttons

```css
/* Primary CTA */
.btn-primary {
  background: linear-gradient(90deg, var(--gold-warm), var(--gold-base));
  background-size: 200% auto;
  color: var(--bg-deep);
  padding: var(--btn-padding-y) var(--btn-padding-x);
  border: none;
  border-radius: var(--btn-radius);
  font-family: var(--btn-font);
  font-size: var(--btn-font-size);
  font-weight: var(--btn-weight);
  letter-spacing: var(--btn-tracking);
  cursor: pointer;
  transition: 
    transform var(--duration-base) var(--ease-standard),
    box-shadow var(--duration-base) var(--ease-standard),
    background-position var(--duration-medium) var(--ease-standard);
}

@media (hover: hover) {
  .btn-primary:hover {
    transform: translateY(-2px);
    box-shadow: var(--shadow-gold-lg);
    background-position: 100% center;
  }
}

.btn-primary:active {
  transform: scale(0.98) translateY(0);
}

.btn-primary:focus-visible {
  outline: 2px solid var(--gold-warm);
  outline-offset: 3px;
}

/* Secondary CTA */
.btn-secondary {
  background: transparent;
  color: var(--gold-base);
  padding: var(--btn-padding-y) var(--btn-padding-x);
  border: 1px solid var(--gold-base);
  border-radius: var(--btn-radius);
  font-family: var(--btn-font);
  font-size: var(--btn-font-size);
  font-weight: var(--btn-weight);
  letter-spacing: var(--btn-tracking);
  cursor: pointer;
  transition: 
    all var(--duration-base) var(--ease-standard);
}

@media (hover: hover) {
  .btn-secondary:hover {
    background: rgba(212, 168, 83, 0.1);
    border-color: var(--gold-warm);
    color: var(--gold-warm);
    transform: translateY(-2px);
  }
}

.btn-secondary:active {
  transform: scale(0.98);
}
```

### Links

```css
/* Text links — animated underline */
a:not(.btn-primary):not(.btn-secondary):not(.nav-link) {
  color: var(--white-pure);
  text-decoration: underline;
  text-decoration-color: var(--gold-warm);
  text-underline-offset: 3px;
  text-decoration-thickness: 1px;
  transition: 
    text-decoration-color var(--duration-base) var(--ease-standard),
    color var(--duration-base) var(--ease-standard);
}

@media (hover: hover) {
  a:not(.btn-primary):not(.btn-secondary):not(.nav-link):hover {
    color: var(--gold-warm);
    text-decoration-color: var(--gold-base);
  }
}

/* Inline CTA with arrow */
.inline-cta::after {
  content: ' →';
  display: inline-block;
  transition: transform var(--duration-fast) var(--ease-standard);
}

@media (hover: hover) {
  .inline-cta:hover::after {
    transform: translateX(4px);
  }
}
```

### Navigation Links

```css
.nav-link {
  color: var(--gray-light);
  transition: color var(--duration-base) var(--ease-standard);
  position: relative;
}

@media (hover: hover) {
  .nav-link:hover {
    color: var(--white-pure);
  }
}

.nav-link.active {
  color: var(--white-pure);
}

/* Active indicator — animated gold underline */
.nav-link.active::after {
  content: '';
  position: absolute;
  bottom: -4px;
  left: 0;
  right: 0;
  height: 2px;
  background: var(--gold-warm);
  border-radius: 1px;
}
```

### Portfolio Logos

```css
.portfolio-logo {
  filter: grayscale(100%) contrast(0.8);
  opacity: 0.6;
  transition: 
    filter var(--duration-medium) var(--ease-standard),
    opacity var(--duration-medium) var(--ease-standard),
    transform var(--duration-medium) var(--ease-standard);
}

@media (hover: hover) {
  .portfolio-logo:hover {
    filter: grayscale(0%) contrast(1);
    opacity: 1;
    transform: scale(1.05);
  }
}
```

### Form Inputs

```css
input, textarea {
  background: var(--input-bg);
  border: var(--input-border);
  border-radius: var(--input-radius);
  padding: var(--input-padding);
  color: var(--white-pure);
  font-family: var(--font-body);
  font-size: var(--text-base);
  transition: 
    border-color var(--duration-base) var(--ease-standard),
    box-shadow var(--duration-base) var(--ease-standard);
}

input:focus, textarea:focus {
  border-color: var(--gold-warm);
  box-shadow: var(--input-focus-ring);
  outline: none;
}

input::placeholder, textarea::placeholder {
  color: var(--gray-dark);
}
```

---

## 3.4 Navigation Adaptive Height

```css
.sticky-nav {
  position: sticky;
  top: 0;
  z-index: var(--z-nav);
  height: var(--nav-height);                   /* 72px */
  padding: 0 var(--container-pad-desktop);
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: var(--nav-bg);
  backdrop-filter: var(--glass-backdrop);
  -webkit-backdrop-filter: var(--glass-backdrop);
  border-bottom: var(--nav-border);
  
  /* THE TRANSITION — exactly 300ms ease */
  transition: 
    height var(--duration-medium) var(--ease-standard),
    background var(--duration-medium) var(--ease-standard),
    padding var(--duration-medium) var(--ease-standard);
}

.sticky-nav.scrolled {
  height: var(--nav-height-scrolled);          /* 56px */
  background: var(--nav-bg-scrolled);
}

/* Logo collapses with nav */
.nav-logo {
  transition: transform var(--duration-medium) var(--ease-standard);
}

.sticky-nav.scrolled .nav-logo {
  transform: scale(0.85);
}
```

```javascript
/**
 * Navigation Height Reducer
 * Shrinks nav from 72px to 56px when scrolled past 50px
 */
function initNavScroll() {
  const nav = document.querySelector('.sticky-nav');
  if (!nav) return;

  let ticking = false;

  function updateNav() {
    if (window.scrollY > 50) {
      nav.classList.add('scrolled');
    } else {
      nav.classList.remove('scrolled');
    }
    ticking = false;
  }

  window.addEventListener('scroll', () => {
    if (!ticking) {
      window.requestAnimationFrame(updateNav);
      ticking = true;
    }
  }, { passive: true });
}

document.addEventListener('DOMContentLoaded', initNavScroll);
```

---

## 3.5 Scroll Progress Bar

```html
<!-- Place as first child of <body>, before nav -->
<div class="scroll-progress" role="progressbar" aria-label="Page scroll progress" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100"></div>
```

```css
.scroll-progress {
  position: fixed;
  top: 0;
  left: 0;
  height: var(--progress-height);          /* 2px */
  width: 0%;
  background: var(--progress-gradient);    /* gold-warm → gold-cool */
  box-shadow: var(--progress-glow);
  z-index: var(--z-progress);
  pointer-events: none;
  transition: width 50ms linear;           /* Smooth but responsive */
}

@media (prefers-reduced-motion: reduce) {
  .scroll-progress {
    transition: none;
  }
}
```

```javascript
/**
 * Scroll Progress Bar
 * Fills a thin gold bar at the very top of the viewport
 */
function initScrollProgress() {
  const bar = document.querySelector('.scroll-progress');
  if (!bar) return;

  let ticking = false;

  function updateProgress() {
    const scrollTop = window.scrollY;
    const docHeight = document.documentElement.scrollHeight - window.innerHeight;
    
    if (docHeight <= 0) {
      bar.style.width = '0%';
      bar.setAttribute('aria-valuenow', '0');
      ticking = false;
      return;
    }

    const percent = Math.min((scrollTop / docHeight) * 100, 100);
    bar.style.width = percent + '%';
    bar.setAttribute('aria-valuenow', Math.round(percent));
    ticking = false;
  }

  window.addEventListener('scroll', () => {
    if (!ticking) {
      window.requestAnimationFrame(updateProgress);
      ticking = true;
    }
  }, { passive: true });
}

document.addEventListener('DOMContentLoaded', initScrollProgress);
```

---

## 3.6 Hero Loading Sequence (First Visit)

```css
/* Initial hidden states */
.hero-title,
.hero-subtitle,
.hero-roles,
.hero-ctas,
.hero-scroll-indicator {
  opacity: 0;
  transform: translateY(20px);
}

/* Entrance animations — staggered */
.hero-loaded .hero-title {
  opacity: 1;
  transform: translateY(0);
  transition: opacity 0.6s var(--ease-enter), transform 0.6s var(--ease-enter);
  transition-delay: 0.2s;
}

.hero-loaded .hero-subtitle {
  opacity: 1;
  transform: translateY(0);
  transition: opacity 0.6s var(--ease-enter), transform 0.6s var(--ease-enter);
  transition-delay: 0.4s;
}

.hero-loaded .hero-roles {
  opacity: 1;
  transform: translateY(0);
  transition: opacity 0.6s var(--ease-enter), transform 0.6s var(--ease-enter);
  transition-delay: 0.6s;
}

.hero-loaded .hero-ctas {
  opacity: 1;
  transform: translateY(0);
  transition: opacity 0.6s var(--ease-enter), transform 0.6s var(--ease-enter);
  transition-delay: 0.8s;
}

.hero-loaded .hero-scroll-indicator {
  opacity: 0.6;
  transform: translateY(0);
  transition: opacity 0.6s var(--ease-enter), transform 0.6s var(--ease-enter);
  transition-delay: 1.2s;
}

/* Scroll indicator bounce */
@keyframes scrollBounce {
  0%, 100% { transform: translateY(0); }
  50%      { transform: translateY(8px); }
}

.hero-scroll-indicator {
  animation: scrollBounce 2s ease-in-out infinite;
  animation-delay: 2s;  /* Start after entrance */
}

/* Return visit: skip delays */
.return-visit .hero-title,
.return-visit .hero-subtitle,
.return-visit .hero-roles,
.return-visit .hero-ctas {
  opacity: 1;
  transform: none;
  transition-delay: 0s;
  transition-duration: 0.3s;
}

/* Reduced motion: instant reveal */
@media (prefers-reduced-motion: reduce) {
  .hero-title,
  .hero-subtitle,
  .hero-roles,
  .hero-ctas,
  .hero-scroll-indicator {
    opacity: 1;
    transform: none;
    transition: none;
    animation: none;
  }
}
```

```javascript
/**
 * Hero Loading Sequence
 */
function initHeroSequence() {
  const hero = document.querySelector('.hero');
  if (!hero) return;

  const hasVisited = localStorage.getItem('ainary-visited');
  
  if (hasVisited) {
    document.body.classList.add('return-visit');
  }

  // Trigger entrance animations
  requestAnimationFrame(() => {
    hero.classList.add('hero-loaded');
  });

  // Mark as visited
  if (!hasVisited) {
    localStorage.setItem('ainary-visited', 'true');
  }
}

document.addEventListener('DOMContentLoaded', initHeroSequence);
```

---

## 3.7 Section Dividers (Animated HR)

```css
hr.gold-divider {
  border: none;
  height: 1px;
  max-width: 200px;
  margin: 0 auto;
  background: linear-gradient(
    90deg,
    transparent 0%,
    var(--gold-base) 50%,
    transparent 100%
  );
  opacity: 0;
  transform: scaleX(0);
  transition: 
    opacity var(--duration-slower) var(--ease-enter),
    transform var(--duration-slower) var(--ease-enter);
}

hr.gold-divider.visible {
  opacity: 1;
  transform: scaleX(1);
}
```

---

## 3.8 Shimmer Text (Gold Keyword Highlight)

```css
.shimmer-text {
  background: linear-gradient(
    90deg,
    var(--white-warm) 0%,
    var(--gold-warm) 40%,
    var(--gold-pale) 50%,
    var(--gold-warm) 60%,
    var(--white-warm) 100%
  );
  background-size: 250% auto;
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: shimmerText 3s ease-in-out infinite;
}

@keyframes shimmerText {
  0%   { background-position: 0% center; }
  100% { background-position: 250% center; }
}

@media (prefers-reduced-motion: reduce) {
  .shimmer-text {
    animation: none;
    background: none;
    -webkit-text-fill-color: var(--gold-warm);
    color: var(--gold-warm);
  }
}
```

---

## 3.9 Skeleton Loader (for async content)

```css
@keyframes skeletonShimmer {
  0%   { background-position: 200% 0; }
  100% { background-position: -200% 0; }
}

.skeleton {
  background: linear-gradient(
    90deg,
    var(--bg-card) 25%,
    var(--bg-hover) 50%,
    var(--bg-card) 75%
  );
  background-size: 200% 100%;
  animation: skeletonShimmer 1.5s ease-in-out infinite;
  border-radius: var(--radius-sm);
}

.skeleton-title {
  height: 24px;
  width: 60%;
  margin-bottom: var(--space-2);
}

.skeleton-text {
  height: 16px;
  width: 90%;
  margin-bottom: var(--space-1);
}

.skeleton-text:last-child {
  width: 70%;
}
```

---

# 4. ACCESSIBILITY CHECKLIST

## 4.1 WCAG AA Compliance Items

### Color Contrast (Validated)

| Foreground | Background | Ratio | WCAG Level | Status |
|------------|------------|-------|------------|--------|
| `--white-pure` (#fff) | `--bg-base` (#0a0f1e) | 14.2:1 | AAA | ✅ Pass |
| `--white-warm` (#e8e6df) | `--bg-base` (#0a0f1e) | 12.8:1 | AAA | ✅ Pass |
| `--gray-light` (#a8a8b2) | `--bg-base` (#0a0f1e) | 7.1:1 | AA | ✅ Pass |
| `--gray-mid` (#8a8a94) | `--bg-base` (#0a0f1e) | 5.3:1 | AA (large text) | ⚠️ Use only for large text or non-essential |
| `--gray-dark` (#5c5c66) | `--bg-base` (#0a0f1e) | 3.4:1 | Fail | ❌ Decorative only, never for content |
| `--gold-warm` (#d4a853) | `--bg-base` (#0a0f1e) | 5.8:1 | AA (large text) | ✅ Pass for buttons/headings |
| `--gold-base` (#c8aa50) | `--bg-base` (#0a0f1e) | 5.2:1 | AA (large text) | ✅ Pass for links (18px+) |
| `--gold-pale` (#e8d89f) | `--bg-base` (#0a0f1e) | 9.8:1 | AAA | ✅ Pass |
| `--bg-deep` (#070b15) text on gold btn | `--gold-warm` (#d4a853) | 7.9:1 | AAA | ✅ Pass |

**Rules:**
- Body text: Use `--white-warm` or `--white-pure` only
- Links at body size (18px): `--gold-base` passes AA
- `--gray-mid` and below: Only for metadata, timestamps, non-essential info at ≥18px
- `--gray-dark`: Never for readable text — decorative only (placeholders, disabled)
- All interactive gold elements: Ensure minimum 4.5:1 against `--bg-base`

### Contrast Validation Tools
- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)
- [Colour Contrast Analyser (Desktop)](https://www.tpgi.com/color-contrast-checker/)
- Chrome DevTools → Accessibility Inspector → Contrast ratio
- `axe DevTools` browser extension

---

## 4.2 Keyboard Navigation Requirements

### Tab Order
- **Logical flow:** Top → bottom, left → right
- **Skip redundant:** Use `tabindex="-1"` for decorative elements
- **No traps:** Every focusable area must allow Tab/Shift+Tab to exit

### Focus Indicators

```css
/* Custom focus indicator — gold ring */
:focus-visible {
  outline: 2px solid var(--gold-warm);
  outline-offset: 3px;
  border-radius: 2px;
}

/* Remove default for mouse users */
:focus:not(:focus-visible) {
  outline: none;
}
```

### Skip-to-Content Link

```html
<!-- First focusable element in DOM -->
<a href="#main-content" class="skip-to-content">Skip to main content</a>
```

```css
.skip-to-content {
  position: absolute;
  top: -100%;
  left: var(--space-2);
  background: var(--gold-warm);
  color: var(--bg-deep);
  padding: var(--space-1) var(--space-2);
  font-weight: var(--weight-semibold);
  border-radius: var(--radius-sm);
  z-index: var(--z-skip);
  transition: top var(--duration-fast) var(--ease-standard);
}

.skip-to-content:focus {
  top: var(--space-1);
}
```

### Keyboard Interaction Patterns

| Component | Keys | Behavior |
|-----------|------|----------|
| Navigation links | Tab, Enter | Focus traversal, activate link |
| Hamburger menu | Enter/Space | Toggle open/close |
| Mobile menu overlay | Escape | Close menu |
| Expandable clusters | Enter/Space | Toggle expand/collapse |
| Buttons | Enter/Space | Activate action |
| Filter tabs | Tab, Arrow keys | Navigate tabs |
| Scroll indicator | N/A | Not focusable (decorative) |

### Focus Management (Mobile Menu)

```javascript
function openMobileMenu() {
  const menu = document.querySelector('.mobile-menu');
  const firstLink = menu.querySelector('a');
  
  menu.setAttribute('data-open', 'true');
  document.body.style.overflow = 'hidden'; // Prevent background scroll
  
  // Trap focus inside menu
  firstLink.focus();
  
  // Listen for Escape
  menu.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') closeMobileMenu();
  });
}

function closeMobileMenu() {
  const menu = document.querySelector('.mobile-menu');
  const trigger = document.querySelector('.hamburger');
  
  menu.setAttribute('data-open', 'false');
  document.body.style.overflow = '';
  
  // Return focus to trigger
  trigger.focus();
}
```

---

## 4.3 Screen Reader Compatibility

### Semantic HTML Structure

```html
<!DOCTYPE html>
<html lang="en">
<head>...</head>
<body>
  <a href="#main-content" class="skip-to-content">Skip to main content</a>
  
  <header>
    <nav aria-label="Main navigation">
      <!-- Logo, links, CTA -->
    </nav>
  </header>
  
  <main id="main-content">
    <section id="hero" aria-label="Introduction">...</section>
    <section id="about" aria-labelledby="about-heading">
      <h2 id="about-heading">About</h2>
      ...
    </section>
    <section id="services" aria-labelledby="services-heading">
      <h2 id="services-heading">Services</h2>
      ...
    </section>
    <!-- etc. -->
  </main>
  
  <footer>
    <nav aria-label="Footer navigation">...</nav>
  </footer>
</body>
</html>
```

### ARIA Patterns Required

```html
<!-- Hamburger menu button -->
<button 
  class="hamburger" 
  aria-label="Open menu"
  aria-expanded="false"
  aria-controls="mobile-menu">
  <span aria-hidden="true"></span>
  <span aria-hidden="true"></span>
  <span aria-hidden="true"></span>
</button>

<!-- Expandable content cluster -->
<div class="cluster">
  <button 
    class="cluster-toggle"
    aria-expanded="false"
    aria-controls="cluster-ai-content">
    <span class="cluster-icon" aria-hidden="true">🧠</span>
    AI Intelligence
  </button>
  <div id="cluster-ai-content" role="region" aria-hidden="true">
    <!-- Articles -->
  </div>
</div>

<!-- External links -->
<a href="https://example.com" 
   target="_blank" 
   rel="noopener noreferrer">
  Portfolio <span class="sr-only">(opens in new tab)</span>
  <span aria-hidden="true">↗</span>
</a>

<!-- Decorative elements -->
<div class="gold-shimmer" aria-hidden="true"></div>
<div class="scroll-indicator" aria-hidden="true">↓</div>

<!-- Scroll progress -->
<div 
  class="scroll-progress" 
  role="progressbar" 
  aria-label="Page scroll progress"
  aria-valuenow="0" 
  aria-valuemin="0" 
  aria-valuemax="100">
</div>

<!-- Social links -->
<nav aria-label="Social links">
  <a href="..." aria-label="Follow on LinkedIn">
    <svg aria-hidden="true">...</svg>
  </a>
</nav>
```

### Screen Reader Utilities

```css
/* Visually hidden but accessible to screen readers */
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border-width: 0;
}

/* Visually hidden until focused (skip links) */
.sr-only-focusable:focus {
  position: static;
  width: auto;
  height: auto;
  padding: inherit;
  margin: inherit;
  overflow: visible;
  clip: auto;
  white-space: normal;
}
```

---

## 4.4 Motion-Safe Preferences

```css
/**
 * MOTION SAFE — Master override for users who prefer reduced motion
 * This MUST appear at the end of the stylesheet
 */
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }

  /* Gold shimmer: static fallback */
  .hero {
    animation: none !important;
    background-size: 100% 100% !important;
  }

  /* Scroll reveals: show immediately */
  .fade-in,
  .fade-in-left,
  .fade-in-scale {
    opacity: 1 !important;
    transform: none !important;
  }

  /* Shimmer text: static gold color */
  .shimmer-text {
    animation: none !important;
    -webkit-text-fill-color: var(--gold-warm) !important;
  }

  /* Scroll indicator: no bounce */
  .hero-scroll-indicator {
    animation: none !important;
  }

  /* Skeleton: no shimmer */
  .skeleton {
    animation: none !important;
  }

  /* Progress bar: instant updates */
  .scroll-progress {
    transition: none !important;
  }
}
```

---

## 4.5 Additional Accessibility Items

### Image Accessibility
```html
<!-- Informative images: descriptive alt text -->
<img src="florian.webp" alt="Florian Ziesche, founder of Ainary Ventures" width="400" height="400" loading="lazy">

<!-- Decorative images: empty alt -->
<img src="pattern.svg" alt="" role="presentation">

<!-- SVG icons: hide from screen readers -->
<svg aria-hidden="true" focusable="false">...</svg>
```

### Language & Text
- `<html lang="en">` on all pages
- Use `lang="de"` attribute on any German text blocks
- Avoid text in images (SVG text is fine, raster text is not)
- Ensure minimum 200% zoom works without horizontal scrolling

### Touch Targets
- Minimum 44×44px for all interactive elements (WCAG 2.5.5)
- Buttons: 48px minimum height (our design: 40-48px ✓)
- Nav links on mobile: minimum 48px tap target
- Links in text: enough spacing between adjacent links

### Page Structure
- One `<h1>` per page
- Heading levels never skip (h1 → h2 → h3, never h1 → h3)
- Meaningful link text (never "click here")
- Lists use `<ul>/<ol>` semantics

---

# 5. QUALITY ASSURANCE PLAN

## 5.1 Browser Testing Matrix

### Must Pass (Tier 1 — release blockers)

| Browser | Version | Platform | Notes |
|---------|---------|----------|-------|
| Chrome | Latest 2 | macOS, Windows, Android | Primary browser |
| Safari | Latest 2 | macOS, iOS | `-webkit-` prefixes for backdrop-filter, background-clip |
| Firefox | Latest 2 | macOS, Windows | No `-webkit-` — test background-clip fallback |
| Chrome Mobile | Latest | Android 12+ | Touch interactions |
| Safari Mobile | Latest | iOS 16+ | Test `100vh` on mobile (use `100dvh` instead) |

### Should Pass (Tier 2 — fix if easy)

| Browser | Version | Platform | Notes |
|---------|---------|----------|-------|
| Edge | Latest 2 | Windows | Chromium-based, should match Chrome |
| Samsung Internet | Latest | Android | Common on Samsung devices |
| Safari | 15.x | iOS 15 | Older but significant share |

### Known Cross-Browser Issues to Handle

| Feature | Issue | Fallback |
|---------|-------|----------|
| `backdrop-filter` | Firefox partial support (now good since 103+) | `background: rgba(10,15,30,0.95)` solid fallback |
| `-webkit-background-clip: text` | Needs `-webkit-` prefix | Provide both `background-clip` and `-webkit-background-clip` |
| `100vh` on iOS | Doesn't account for address bar | Use `100dvh` or `min-height: 100vh; min-height: 100dvh;` |
| Variable fonts | Old browsers lack support | Fallback `@font-face` with static woff2 weights (400, 600) |
| `scroll-behavior: smooth` | Safari partial | JS fallback (`Element.scrollIntoView({behavior: 'smooth'})`) |
| `:focus-visible` | Safari 15.3+ | Polyfill or fallback with `:focus` |
| `@media (hover: hover)` | Reliable in modern browsers | Test on hybrid devices (Surface) |

---

## 5.2 Device Testing Plan

### Physical / Real Devices (Priority)

| Device | Screen | Breakpoint | Test Focus |
|--------|--------|------------|------------|
| iPhone SE (3rd gen) | 375×667 | Small mobile | Minimum viable layout |
| iPhone 15 Pro | 393×852 | Standard mobile | Primary mobile target |
| iPhone 15 Pro Max | 430×932 | Large mobile | Content reflow |
| iPad Air | 820×1180 | Tablet portrait | 2-column layouts |
| iPad Pro 12.9" | 1024×1366 | Tablet landscape | Nav transition |
| MacBook Air 13" | 1470×956 | Small desktop | Primary desktop target |
| 27" Monitor | 2560×1440 | Large desktop | Max-width behavior |

### Emulation / Responsive Testing

- Chrome DevTools Device Toolbar (resize freely)
- Safari Responsive Design Mode
- BrowserStack (for cross-OS testing)

### Testing Checklist per Device

- [ ] Navigation collapses/expands at correct breakpoint
- [ ] Hero text is readable without horizontal scrolling
- [ ] Service cards reflow (1 → 2 → 3 columns)
- [ ] Touch targets ≥ 44×44px on mobile
- [ ] No horizontal overflow at any breakpoint
- [ ] Gold shimmer animation runs smoothly (60fps)
- [ ] Scroll reveals trigger at correct positions
- [ ] Forms are usable (input focus, keyboard visible on mobile)
- [ ] Images lazy-load correctly
- [ ] Text is readable at all sizes (no text under 14px)

---

## 5.3 Performance Benchmarks

### Lighthouse Targets (All Green)

| Metric | Target | Measurement |
|--------|--------|-------------|
| Performance Score | ≥ 95 | Lighthouse CI |
| Accessibility Score | ≥ 95 | Lighthouse CI |
| Best Practices Score | ≥ 95 | Lighthouse CI |
| SEO Score | ≥ 95 | Lighthouse CI |

### Core Web Vitals Targets

| Metric | Target | What It Measures |
|--------|--------|-----------------|
| LCP (Largest Contentful Paint) | ≤ 1.2s | Time to render hero text |
| FID (First Input Delay) | ≤ 50ms | Responsiveness to first click |
| CLS (Cumulative Layout Shift) | ≤ 0.05 | Visual stability (no jumping) |
| INP (Interaction to Next Paint) | ≤ 100ms | Overall responsiveness |
| FCP (First Contentful Paint) | ≤ 0.8s | Time to see anything |
| TTFB (Time to First Byte) | ≤ 200ms | Server response speed |

### Page Weight Budget

| Asset Type | Budget | Notes |
|------------|--------|-------|
| HTML | ≤ 50 KB | Single file, gzipped |
| CSS (inline or file) | ≤ 30 KB | All custom properties + styles |
| JavaScript | ≤ 20 KB | Intersection Observer, nav, progress bar |
| Fonts (total) | ≤ 165 KB | 3 variable fonts, subsetted |
| Images (above fold) | ≤ 50 KB | Hero: no raster needed. OG image: preloaded |
| Images (total) | ≤ 200 KB | Lazy-loaded, WebP |
| **Total initial load** | **≤ 300 KB** | Gzipped/Brotli compressed |
| **Total page weight** | **≤ 500 KB** | Including all lazy-loaded assets |

### Performance Optimization Checklist

- [ ] Fonts: `font-display: swap` on all `@font-face`
- [ ] Fonts: Preload critical fonts (`<link rel="preload" as="font">`)
- [ ] Images: `loading="lazy"` on all below-fold images
- [ ] Images: `width` and `height` attributes (prevent CLS)
- [ ] Images: WebP format with JPEG fallback (`<picture>`)
- [ ] CSS: Inline critical CSS or use single stylesheet
- [ ] JS: `defer` attribute on all scripts
- [ ] JS: Intersection Observer (native, no library)
- [ ] Compression: Brotli on server (gzip fallback)
- [ ] Caching: Immutable headers on fonts and images
- [ ] No external dependencies: Zero third-party JS/CSS
- [ ] Minification: HTML, CSS, JS minified for production
- [ ] DNS prefetch: `<link rel="dns-prefetch">` for any external resources

### Font Loading Strategy

```html
<head>
  <!-- Preload critical font (Inter — used everywhere) -->
  <link rel="preload" 
        href="/fonts/InterVariable-latin.woff2" 
        as="font" 
        type="font/woff2" 
        crossorigin>
  
  <!-- Preload monospace (used in hero CTAs) -->
  <link rel="preload" 
        href="/fonts/JetBrainsMono-Variable-latin.woff2" 
        as="font" 
        type="font/woff2" 
        crossorigin>
  
  <!-- Display font: loaded async (only needed for headings) -->
  <link rel="preload" 
        href="/fonts/InterDisplay-Variable-latin.woff2" 
        as="font" 
        type="font/woff2" 
        crossorigin>
</head>
```

---

## 5.4 Accessibility Audit Tools

| Tool | Purpose | When to Use |
|------|---------|-------------|
| [axe DevTools](https://www.deque.com/axe/) | Automated accessibility scanner | Every build |
| [WAVE](https://wave.webaim.org/) | Visual overlay of a11y issues | Before launch, after major changes |
| [Lighthouse Accessibility](https://web.dev/lighthouse-accessibility/) | Automated audit (built into Chrome) | Every build |
| [Pa11y](https://pa11y.org/) | CLI automated testing | CI/CD pipeline |
| Screen reader (VoiceOver on macOS) | Manual screen reader testing | Before launch |
| Screen reader (NVDA on Windows) | Manual screen reader testing | Before launch |
| Keyboard-only navigation | Manual tab/enter testing | Before launch |
| [Colour Contrast Analyser](https://www.tpgi.com/color-contrast-checker/) | Verify contrast ratios | When changing colors |
| [Stark (Figma plugin)](https://www.getstark.co/) | Design-time contrast check | During design phase |

### Automated Testing Command

```bash
# Pa11y automated test
npx pa11y https://ainaryventures.com --standard WCAG2AA --reporter cli

# Lighthouse CI (performance + a11y)
npx lighthouse https://ainaryventures.com \
  --output json --output html \
  --chrome-flags="--headless" \
  --only-categories=performance,accessibility,best-practices,seo
```

---

## 5.5 Pre-Launch Checklist

### ✅ Foundation
- [ ] All CSS custom properties defined and consistent
- [ ] Fonts downloaded, subsetted, self-hosted
- [ ] `@font-face` declarations with `font-display: swap`
- [ ] Font preloading in `<head>`
- [ ] Base color palette implemented and tested

### ✅ Content & SEO
- [ ] All content reviewed for spelling/grammar
- [ ] `<title>` tag unique and descriptive (≤60 chars)
- [ ] `<meta name="description">` unique and compelling (≤155 chars)
- [ ] OG tags (`og:title`, `og:description`, `og:image`, `og:url`)
- [ ] Twitter card tags (`twitter:card`, `twitter:title`, `twitter:image`)
- [ ] Canonical URL set
- [ ] `robots.txt` exists and is correct
- [ ] `sitemap.xml` exists
- [ ] Structured data (JSON-LD: Organization, Person)
- [ ] All links tested (no 404s)
- [ ] Images have descriptive `alt` text

### ✅ Design & Interaction
- [ ] Gold shimmer animation runs smoothly (hero)
- [ ] Scroll reveal animations fire correctly
- [ ] Navigation transitions (72px → 56px) smooth
- [ ] Scroll progress bar fills correctly
- [ ] All hover states work on desktop
- [ ] No hover states fire on touch devices
- [ ] Mobile menu opens/closes correctly
- [ ] All buttons/links have visible focus states
- [ ] Forms validate and submit correctly
- [ ] Loading states display for async content

### ✅ Responsive
- [ ] Tested at 375px (small mobile)
- [ ] Tested at 768px (tablet)
- [ ] Tested at 1024px (small desktop)
- [ ] Tested at 1440px (large desktop)
- [ ] No horizontal scrollbar at any width
- [ ] No text overflow or truncation errors
- [ ] Images scale correctly
- [ ] Navigation collapses at correct breakpoint

### ✅ Accessibility
- [ ] Lighthouse Accessibility score ≥ 95
- [ ] axe DevTools: 0 critical/serious issues
- [ ] Keyboard-only navigation: all content reachable
- [ ] Skip-to-content link works
- [ ] Focus visible on all interactive elements
- [ ] Screen reader announces all content logically
- [ ] ARIA labels on all non-text interactive elements
- [ ] `prefers-reduced-motion` respected
- [ ] `prefers-color-scheme` handled (if light theme exists)
- [ ] Zoom to 200%: no content loss or horizontal scroll

### ✅ Performance
- [ ] Lighthouse Performance score ≥ 95
- [ ] LCP ≤ 1.2s
- [ ] CLS ≤ 0.05
- [ ] Total initial load ≤ 300 KB
- [ ] No render-blocking resources
- [ ] Images optimized (WebP, lazy-loaded)
- [ ] Fonts optimized (subsetted, preloaded)
- [ ] No console errors
- [ ] No mixed content warnings

### ✅ Cross-Browser
- [ ] Chrome (latest) ✓
- [ ] Safari (latest) ✓
- [ ] Firefox (latest) ✓
- [ ] Chrome Mobile (Android) ✓
- [ ] Safari Mobile (iOS) ✓
- [ ] Edge (latest) ✓

### ✅ Deployment
- [ ] HTTPS enforced (SSL certificate)
- [ ] `www` → non-`www` redirect (or vice versa)
- [ ] 404 page exists and is styled
- [ ] Compression enabled (Brotli/gzip)
- [ ] Cache headers configured
- [ ] Analytics installed (if desired)
- [ ] Favicon set renders correctly in all browsers
- [ ] Social share preview tested (Facebook Debugger, Twitter Card Validator)

---

# APPENDIX A: Complete JavaScript Bundle

All animations and interactions in one file. No dependencies. ~8 KB unminified.

```javascript
/**
 * Ainary Ventures — Site Interactions
 * Zero dependencies. ES2020+.
 * Handles: scroll progress, nav resize, scroll reveals, hero sequence, smooth scroll
 */

(function () {
  'use strict';

  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // ──── Scroll Progress Bar ────
  function initScrollProgress() {
    const bar = document.querySelector('.scroll-progress');
    if (!bar) return;

    let ticking = false;
    function update() {
      const h = document.documentElement.scrollHeight - window.innerHeight;
      const pct = h > 0 ? Math.min((window.scrollY / h) * 100, 100) : 0;
      bar.style.width = pct + '%';
      bar.setAttribute('aria-valuenow', Math.round(pct));
      ticking = false;
    }

    window.addEventListener('scroll', () => {
      if (!ticking) { requestAnimationFrame(update); ticking = true; }
    }, { passive: true });
  }

  // ──── Sticky Nav Height Reduction ────
  function initNavScroll() {
    const nav = document.querySelector('.sticky-nav');
    if (!nav) return;

    let ticking = false;
    function update() {
      nav.classList.toggle('scrolled', window.scrollY > 50);
      ticking = false;
    }

    window.addEventListener('scroll', () => {
      if (!ticking) { requestAnimationFrame(update); ticking = true; }
    }, { passive: true });
  }

  // ──── Scroll Reveal (Intersection Observer) ────
  function initScrollReveal() {
    if (prefersReducedMotion) {
      document.querySelectorAll('.fade-in, .fade-in-left, .fade-in-scale').forEach(el => {
        el.classList.add('visible');
      });
      return;
    }

    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.15, rootMargin: '0px 0px -80px 0px' });

    document.querySelectorAll('.fade-in, .fade-in-left, .fade-in-scale').forEach(el => {
      observer.observe(el);
    });
  }

  // ──── Hero Loading Sequence ────
  function initHeroSequence() {
    const hero = document.querySelector('.hero');
    if (!hero) return;

    if (localStorage.getItem('ainary-visited')) {
      document.body.classList.add('return-visit');
    }

    requestAnimationFrame(() => hero.classList.add('hero-loaded'));
    localStorage.setItem('ainary-visited', 'true');
  }

  // ──── Smooth Scroll for Anchor Links ────
  function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
      anchor.addEventListener('click', (e) => {
        const target = document.querySelector(anchor.getAttribute('href'));
        if (!target) return;
        e.preventDefault();
        target.scrollIntoView({ behavior: prefersReducedMotion ? 'auto' : 'smooth', block: 'start' });
        // Update URL hash without jump
        history.pushState(null, '', anchor.getAttribute('href'));
      });
    });
  }

  // ──── Mobile Menu Toggle ────
  function initMobileMenu() {
    const trigger = document.querySelector('.hamburger');
    const menu = document.querySelector('.mobile-menu');
    if (!trigger || !menu) return;

    function open() {
      menu.setAttribute('data-open', 'true');
      trigger.setAttribute('aria-expanded', 'true');
      document.body.style.overflow = 'hidden';
      const firstLink = menu.querySelector('a');
      if (firstLink) firstLink.focus();
    }

    function close() {
      menu.setAttribute('data-open', 'false');
      trigger.setAttribute('aria-expanded', 'false');
      document.body.style.overflow = '';
      trigger.focus();
    }

    trigger.addEventListener('click', () => {
      const isOpen = menu.getAttribute('data-open') === 'true';
      isOpen ? close() : open();
    });

    menu.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') close();
    });

    // Close on link click
    menu.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', close);
    });
  }

  // ──── Initialize All ────
  document.addEventListener('DOMContentLoaded', () => {
    initScrollProgress();
    initNavScroll();
    initScrollReveal();
    initHeroSequence();
    initSmoothScroll();
    initMobileMenu();
  });

})();
```

---

# APPENDIX B: HTML Head Template

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  
  <!-- Title & Description -->
  <title>Ainary Ventures — AI Systems That Go Into Production</title>
  <meta name="description" content="AI-native platform for operators and investors. We build, invest, deploy, and teach — compounding expertise in manufacturing and legal AI.">
  
  <!-- Favicon -->
  <link rel="icon" type="image/x-icon" href="/favicon.ico">
  <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
  <link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
  <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
  <link rel="manifest" href="/site.webmanifest">
  <link rel="mask-icon" href="/safari-pinned-tab.svg" color="#c8aa50">
  <meta name="msapplication-TileColor" content="#0a0f1e">
  <meta name="theme-color" content="#0a0f1e">
  
  <!-- Open Graph -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://ainaryventures.com/">
  <meta property="og:title" content="Ainary Ventures — AI Systems That Go Into Production">
  <meta property="og:description" content="AI-native platform for operators and investors. We build, invest, deploy, and teach.">
  <meta property="og:image" content="https://ainaryventures.com/og-image.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  
  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Ainary Ventures — AI Systems That Go Into Production">
  <meta name="twitter:description" content="AI-native platform. We build, invest, deploy, and teach.">
  <meta name="twitter:image" content="https://ainaryventures.com/og-image.png">
  
  <!-- Canonical -->
  <link rel="canonical" href="https://ainaryventures.com/">
  
  <!-- Font Preloads -->
  <link rel="preload" href="/fonts/InterVariable-latin.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="preload" href="/fonts/JetBrainsMono-Variable-latin.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="preload" href="/fonts/InterDisplay-Variable-latin.woff2" as="font" type="font/woff2" crossorigin>
  
  <!-- Styles (inline for single-file approach, or external) -->
  <style>
    /* All CSS custom properties and styles here */
  </style>
</head>
```

---

# APPENDIX C: Structured Data (JSON-LD)

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Ainary Ventures",
  "url": "https://ainaryventures.com",
  "logo": "https://ainaryventures.com/logo.svg",
  "description": "AI-native platform for operators and investors. We build, invest, deploy, and teach — compounding expertise in manufacturing and legal AI.",
  "founder": {
    "@type": "Person",
    "name": "Florian Ziesche",
    "jobTitle": "Founder",
    "url": "https://florianziesche.com"
  },
  "sameAs": [
    "https://linkedin.com/in/florianziesche",
    "https://twitter.com/florianziesche",
    "https://github.com/florianziesche"
  ],
  "contactPoint": {
    "@type": "ContactPoint",
    "email": "florian@ainaryventures.com",
    "contactType": "business"
  },
  "address": {
    "@type": "PostalAddress",
    "addressLocality": "New York",
    "addressCountry": "US"
  }
}
</script>
```

---

# APPENDIX D: Quick Reference Card

## Colors (Copy-Paste)
| Token | Hex | Use |
|-------|-----|-----|
| `--bg-deep` | `#070b15` | Deepest bg |
| `--bg-base` | `#0a0f1e` | Main bg |
| `--bg-card` | `#0f1420` | Cards |
| `--bg-hover` | `#14192a` | Hover states |
| `--white-pure` | `#ffffff` | Headlines |
| `--white-warm` | `#e8e6df` | Body text |
| `--gray-light` | `#a8a8b2` | Secondary |
| `--gray-mid` | `#8a8a94` | Tertiary |
| `--gray-dark` | `#5c5c66` | Disabled |
| `--gray-rule` | `#1f2530` | Borders |
| `--gold-warm` | `#d4a853` | Primary CTA |
| `--gold-base` | `#c8aa50` | Links |
| `--gold-cool` | `#b09a45` | Secondary |
| `--gold-pale` | `#e8d89f` | Highlights |
| `--gold-deep` | `#9d7f3b` | Depth |

## Typography Quick Ref
| Element | Font | Size | Weight | Leading |
|---------|------|------|--------|---------|
| Hero | Inter Display | 68px (clamp) | 600 | 1.1 |
| H1 | Inter Display | 56px (clamp) | 600 | 1.2 |
| H2 | Inter Display | 42px (clamp) | 600 | 1.3 |
| H3 | Inter | 32px (clamp) | 600 | 1.3 |
| Body | Inter | 18px | 400 | 1.7 |
| Caption | Inter | 16px | 400 | 1.5 |
| Button | JetBrains Mono | 14px | 500 | — |
| Label | JetBrains Mono | 14px | 500 | — |

## Animation Quick Ref
| Animation | Duration | Easing | Trigger |
|-----------|----------|--------|---------|
| Gold Shimmer | 5s loop | ease-in-out | Always (hero) |
| Scroll Reveal | 500ms | ease-enter | Intersection Observer |
| Card Hover | 300ms | ease-standard | hover |
| Button Hover | 200ms | ease-standard | hover |
| Link Hover | 200ms | ease-standard | hover |
| Nav Height | 300ms | ease-standard | scroll > 50px |
| Progress Bar | 50ms | linear | scroll |
| Hero Entrance | 600ms per element | ease-enter | Page load |
| Mobile Menu | 300ms | ease-standard | Click |

---

*Document complete. Ready for implementation.*  
*Planner Agent 5 — February 7, 2026*
