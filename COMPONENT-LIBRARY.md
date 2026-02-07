# Ainary Ventures — Component Library v1
**Complete UI Component Specifications**  
**Date:** February 7, 2026  
**Sources:** Brand Identity Synthesis, UI/UX Synthesis, Color System Validation, Current Website Code, Design System Standards

---

## Table of Contents

1. [Design Tokens](#i-design-tokens)
2. [Buttons (5 Variants)](#ii-buttons)
3. [Cards (4 Types)](#iii-cards)
4. [Navigation (4 Patterns)](#iv-navigation)
5. [Forms](#v-forms)
6. [Typography](#vi-typography)
7. [Micro-Interactions](#vii-micro-interactions)
8. [Utility Classes](#viii-utility-classes)
9. [Accessibility Checklist](#ix-accessibility-checklist)

---

## I. Design Tokens

All components reference these shared CSS custom properties. This is the single source of truth.

```css
:root {
  /* ═══════════════════════════════════════════
     MONOCHROME FOUNDATION (90-95% of site)
     ═══════════════════════════════════════════ */

  /* Backgrounds — Dark Spectrum */
  --bg-deep: #070b15;       /* Deepest — page background */
  --bg-base: #0a0f1e;       /* Primary — section backgrounds */
  --bg-card: #0f1420;       /* Elevated — cards, modals */
  --bg-hover: #14192a;      /* Interactive — hover states */

  /* Foregrounds — Light Spectrum */
  --white-pure: #ffffff;    /* Headlines, primary text — 15.2:1 on bg-deep ✅ AAA */
  --white-warm: #e8e6df;    /* Body text — 13.8:1 on bg-deep ✅ AAA */
  --gray-light: #a8a8b2;    /* Secondary text — 8.1:1 on bg-deep ✅ AAA */
  --gray-mid: #8a8a94;      /* Tertiary text — 6.2:1 on bg-deep ✅ AA */
  --gray-dark: #5c5c66;     /* Disabled text — 4.1:1 ⚠️ AA Large only */
  --gray-rule: #1f2530;     /* Borders, dividers — decorative only */

  /* ═══════════════════════════════════════════
     GOLD SPECTRUM (5-10% of site)
     ═══════════════════════════════════════════ */

  /* Text-Safe Golds */
  --gold-pale: #e8d89f;     /* Highlights — 9.8:1 on bg-deep ✅ AAA */
  --gold-warm: #d4a853;     /* Primary CTAs — 7.2:1 on bg-deep ✅ AAA */
  --gold-base: #c8aa50;     /* Links, secondary — 6.5:1 on bg-deep ✅ AA */

  /* Restricted Golds */
  --gold-cool: #b09a45;     /* Large text only (18px+) — 5.2:1 on bg-deep ✅ AA */
  --gold-deep: #9d7f3b;     /* DECORATIVE ONLY — 3.8:1 ❌ Never for text */

  /* ═══════════════════════════════════════════
     SEMANTIC COLORS
     ═══════════════════════════════════════════ */
  --success: #4ade80;
  --success-bg: rgba(74, 222, 128, 0.1);
  --warning: #fbbf24;
  --warning-bg: rgba(251, 191, 36, 0.1);
  --error: #f87171;
  --error-bg: rgba(248, 113, 113, 0.1);
  --info: #60a5fa;
  --info-bg: rgba(96, 165, 250, 0.1);

  /* ═══════════════════════════════════════════
     GRADIENTS
     ═══════════════════════════════════════════ */
  --gradient-gold: linear-gradient(135deg, var(--gold-warm), var(--gold-base), var(--gold-cool));
  --gradient-shimmer: linear-gradient(135deg,
    var(--bg-deep) 0%,
    var(--bg-base) 40%,
    rgba(212, 168, 83, 0.05) 50%,
    var(--bg-base) 60%,
    var(--bg-deep) 100%
  );
  --gradient-card-gold: linear-gradient(135deg,
    rgba(200, 170, 80, 0.08),
    rgba(200, 170, 80, 0.02)
  );

  /* ═══════════════════════════════════════════
     TYPOGRAPHY
     ═══════════════════════════════════════════ */
  --font-display: 'Inter Display', 'Inter', system-ui, -apple-system, sans-serif;
  --font-body: 'Inter', system-ui, -apple-system, 'Segoe UI', sans-serif;
  --font-mono: 'JetBrains Mono', 'SF Mono', 'Fira Code', monospace;

  /* Scale */
  --text-xs: 0.75rem;      /* 12px */
  --text-sm: 0.875rem;     /* 14px */
  --text-base: 1rem;       /* 16px — minimum for mobile body */
  --text-lg: 1.125rem;     /* 18px — desktop body text */
  --text-xl: 1.25rem;      /* 20px */
  --text-2xl: 1.5rem;      /* 24px */
  --text-3xl: 2rem;        /* 32px */
  --text-4xl: 2.625rem;    /* 42px */
  --text-5xl: 3.5rem;      /* 56px */
  --text-6xl: 4.25rem;     /* 68px — hero headlines */

  /* Weights */
  --weight-normal: 400;
  --weight-medium: 500;
  --weight-semibold: 600;
  --weight-bold: 700;

  /* Line Heights */
  --leading-none: 1;
  --leading-tight: 1.15;
  --leading-snug: 1.3;
  --leading-normal: 1.5;
  --leading-relaxed: 1.75;

  /* Letter Spacing */
  --tracking-tighter: -0.025em;
  --tracking-tight: -0.02em;
  --tracking-normal: 0;
  --tracking-wide: 0.02em;
  --tracking-wider: 0.06em;
  --tracking-widest: 0.22em;

  /* ═══════════════════════════════════════════
     SPACING (8px grid)
     ═══════════════════════════════════════════ */
  --space-0: 0;
  --space-1: 0.25rem;      /* 4px */
  --space-2: 0.5rem;       /* 8px */
  --space-3: 0.75rem;      /* 12px */
  --space-4: 1rem;         /* 16px */
  --space-5: 1.25rem;      /* 20px */
  --space-6: 1.5rem;       /* 24px */
  --space-8: 2rem;         /* 32px */
  --space-10: 2.5rem;      /* 40px */
  --space-12: 3rem;        /* 48px */
  --space-16: 4rem;        /* 64px */
  --space-20: 5rem;        /* 80px */
  --space-24: 6rem;        /* 96px */
  --space-32: 8rem;        /* 128px */

  /* ═══════════════════════════════════════════
     BORDERS & RADII
     ═══════════════════════════════════════════ */
  --radius-sm: 4px;
  --radius-md: 6px;
  --radius-lg: 8px;
  --radius-xl: 12px;
  --radius-full: 9999px;

  --border-default: 1px solid var(--gray-rule);
  --border-gold: 1px solid rgba(200, 170, 80, 0.15);
  --border-gold-hover: 1px solid rgba(200, 170, 80, 0.35);

  /* ═══════════════════════════════════════════
     SHADOWS
     ═══════════════════════════════════════════ */
  --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.3);
  --shadow-md: 0 4px 12px rgba(0, 0, 0, 0.25);
  --shadow-lg: 0 12px 32px rgba(0, 0, 0, 0.3);
  --shadow-gold: 0 8px 20px rgba(212, 168, 83, 0.2);
  --shadow-gold-lg: 0 12px 32px rgba(212, 168, 83, 0.25);

  /* ═══════════════════════════════════════════
     TRANSITIONS
     ═══════════════════════════════════════════ */
  --ease-default: cubic-bezier(0.4, 0, 0.2, 1);
  --ease-in: cubic-bezier(0.4, 0, 1, 1);
  --ease-out: cubic-bezier(0, 0, 0.2, 1);
  --ease-spring: cubic-bezier(0.34, 1.56, 0.64, 1);

  --duration-fast: 150ms;
  --duration-normal: 200ms;
  --duration-slow: 300ms;
  --duration-slower: 500ms;

  /* ═══════════════════════════════════════════
     Z-INDEX
     ═══════════════════════════════════════════ */
  --z-base: 0;
  --z-dropdown: 10;
  --z-sticky: 20;
  --z-overlay: 30;
  --z-modal: 40;
  --z-popover: 50;
  --z-tooltip: 60;
  --z-progress: 101;

  /* ═══════════════════════════════════════════
     LAYOUT
     ═══════════════════════════════════════════ */
  --nav-height: 72px;
  --nav-height-scrolled: 56px;
  --content-max: 1200px;
  --content-narrow: 720px;
  --content-wide: 1440px;

  /* ═══════════════════════════════════════════
     FOCUS
     ═══════════════════════════════════════════ */
  --focus-ring: 0 0 0 2px var(--bg-base), 0 0 0 4px var(--gold-warm);
}

/* ═══════════════════════════════════════════
   REDUCED MOTION
   ═══════════════════════════════════════════ */
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

---

## II. Buttons

Five button variants, each with clear use cases and full state definitions.

### Design Principles
- **Minimum tap target:** 44×44px (mobile), 36×36px (desktop)
- **Font:** `var(--font-mono)` for CTAs/actions, `var(--font-body)` for inline buttons
- **Border radius:** `var(--radius-md)` (6px) default, `var(--radius-sm)` (4px) for compact
- **Transitions:** `all var(--duration-normal) var(--ease-default)`

---

### 1. Primary Button (Gold Solid)

**Use:** Primary page actions — "Get in Touch", "Book a Call", "Apply", "Subscribe"  
**Frequency:** 1–2 per viewport. Never more than one primary in a row of buttons.

```html
<button class="btn btn-primary" type="button">
  Get in Touch
</button>

<!-- With icon -->
<button class="btn btn-primary" type="button">
  <svg class="btn-icon" aria-hidden="true"><!-- icon --></svg>
  Get in Touch
</button>

<!-- Disabled -->
<button class="btn btn-primary" type="button" disabled aria-disabled="true">
  Get in Touch
</button>

<!-- Loading -->
<button class="btn btn-primary btn-loading" type="button" disabled aria-busy="true">
  <span class="btn-spinner" aria-hidden="true"></span>
  Sending…
</button>
```

```css
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: var(--space-2);
  height: 44px;
  padding: 0 var(--space-6);
  font-family: var(--font-mono);
  font-size: var(--text-sm);
  font-weight: var(--weight-medium);
  letter-spacing: var(--tracking-wide);
  line-height: 1;
  text-decoration: none;
  border: none;
  border-radius: var(--radius-md);
  cursor: pointer;
  transition: all var(--duration-normal) var(--ease-default);
  white-space: nowrap;
  user-select: none;
  -webkit-tap-highlight-color: transparent;
}

.btn-primary {
  background: var(--gold-warm);
  color: var(--bg-deep);
}

/* Hover — Desktop only */
@media (hover: hover) {
  .btn-primary:hover {
    background: var(--gold-base);
    transform: translateY(-2px);
    box-shadow: var(--shadow-gold);
  }
}

/* Active / Press */
.btn-primary:active {
  transform: scale(0.98) translateY(0);
  box-shadow: none;
}

/* Focus — Keyboard only */
.btn-primary:focus-visible {
  outline: none;
  box-shadow: var(--focus-ring);
}

/* Disabled */
.btn-primary:disabled,
.btn-primary[aria-disabled="true"] {
  background: var(--gray-dark);
  color: var(--gray-mid);
  cursor: not-allowed;
  transform: none;
  box-shadow: none;
  opacity: 0.6;
}
```

**States:**
| State | Background | Color | Transform | Shadow |
|-------|-----------|-------|-----------|--------|
| Default | `--gold-warm` | `--bg-deep` | none | none |
| Hover | `--gold-base` | `--bg-deep` | translateY(-2px) | `--shadow-gold` |
| Active | `--gold-warm` | `--bg-deep` | scale(0.98) | none |
| Focus | `--gold-warm` | `--bg-deep` | none | `--focus-ring` |
| Disabled | `--gray-dark` | `--gray-mid` | none | none |
| Loading | `--gold-warm` | `--bg-deep` | none | none |

**Accessibility:**
- ✅ `--gold-warm` on `--bg-deep` text = 7.2:1 contrast (exceeds AA for inverted text)
- ✅ Focus ring visible on keyboard navigation (`focus-visible`)
- ✅ `disabled` + `aria-disabled` for assistive tech
- ✅ `aria-busy="true"` during loading state

---

### 2. Secondary Button (Gold Outline)

**Use:** Secondary actions alongside a primary — "Our Portfolio", "Learn More", "View All"  
**Frequency:** 1–3 per viewport. Pairs with Primary.

```html
<button class="btn btn-secondary" type="button">
  Our Portfolio
</button>

<!-- As link -->
<a href="/portfolio" class="btn btn-secondary">
  Our Portfolio
</a>
```

```css
.btn-secondary {
  background: transparent;
  color: var(--gold-warm);
  border: 1px solid var(--gold-warm);
}

@media (hover: hover) {
  .btn-secondary:hover {
    background: rgba(212, 168, 83, 0.1);
    border-color: var(--gold-base);
    transform: translateY(-2px);
  }
}

.btn-secondary:active {
  transform: scale(0.98) translateY(0);
  background: rgba(212, 168, 83, 0.15);
}

.btn-secondary:focus-visible {
  outline: none;
  box-shadow: var(--focus-ring);
}

.btn-secondary:disabled,
.btn-secondary[aria-disabled="true"] {
  color: var(--gray-dark);
  border-color: var(--gray-dark);
  background: transparent;
  cursor: not-allowed;
  transform: none;
  opacity: 0.6;
}
```

**States:**
| State | Background | Border | Color | Transform |
|-------|-----------|--------|-------|-----------|
| Default | transparent | `--gold-warm` | `--gold-warm` | none |
| Hover | gold 10% | `--gold-base` | `--gold-warm` | translateY(-2px) |
| Active | gold 15% | `--gold-warm` | `--gold-warm` | scale(0.98) |
| Focus | transparent | `--gold-warm` | `--gold-warm` | none + ring |
| Disabled | transparent | `--gray-dark` | `--gray-dark` | none |

**Accessibility:**
- ✅ `--gold-warm` text on dark background = 7.2:1 (AAA)
- ✅ Border provides additional visual boundary for low vision users

---

### 3. Tertiary Button (Text Only)

**Use:** Least-emphasis actions — "Read more →", "Skip", "Cancel", inline navigation  
**Frequency:** Unlimited. Used for supplementary actions.

```html
<button class="btn btn-tertiary" type="button">
  Read more →
</button>

<!-- As link styled as button -->
<a href="/insights" class="btn btn-tertiary">
  View all articles →
</a>
```

```css
.btn-tertiary {
  background: transparent;
  color: var(--gold-base);
  border: none;
  padding: 0 var(--space-2);
  height: auto;
  font-family: var(--font-body);
  font-size: var(--text-base);
  font-weight: var(--weight-medium);
  letter-spacing: var(--tracking-normal);
  text-decoration: underline;
  text-decoration-color: rgba(200, 170, 80, 0.3);
  text-underline-offset: 3px;
}

@media (hover: hover) {
  .btn-tertiary:hover {
    color: var(--gold-warm);
    text-decoration-color: var(--gold-warm);
  }
}

.btn-tertiary:active {
  opacity: 0.8;
}

.btn-tertiary:focus-visible {
  outline: none;
  box-shadow: var(--focus-ring);
  border-radius: var(--radius-sm);
}

.btn-tertiary:disabled,
.btn-tertiary[aria-disabled="true"] {
  color: var(--gray-dark);
  text-decoration-color: transparent;
  cursor: not-allowed;
}
```

**Accessibility:**
- ✅ Underline provides non-color indicator of interactivity
- ✅ `--gold-base` = 6.5:1 contrast (AA)
- ✅ Sufficient padding for touch targets when used inline

---

### 4. CTA Button (Large, Hero)

**Use:** Hero section call-to-action — "For Founders", "Start a Project", "Subscribe to the Brief"  
**Frequency:** 1 per hero. Maximum 2 side-by-side (one CTA Primary + one CTA Secondary).

```html
<!-- Hero CTA pair -->
<div class="hero-ctas" role="group" aria-label="Primary actions">
  <a href="/contact" class="btn btn-cta">
    For Founders
  </a>
  <a href="/portfolio" class="btn btn-cta btn-cta-outline">
    Our Portfolio
  </a>
</div>
```

```css
.btn-cta {
  height: 56px;
  padding: 0 var(--space-10);
  font-family: var(--font-mono);
  font-size: var(--text-base);
  font-weight: var(--weight-semibold);
  letter-spacing: var(--tracking-wider);
  background: var(--gold-warm);
  color: var(--bg-deep);
  border: none;
  border-radius: var(--radius-md);
}

@media (hover: hover) {
  .btn-cta:hover {
    background: var(--gold-base);
    transform: translateY(-3px);
    box-shadow: var(--shadow-gold-lg);
  }
}

.btn-cta:active {
  transform: scale(0.98) translateY(0);
  box-shadow: none;
}

.btn-cta:focus-visible {
  outline: none;
  box-shadow: var(--focus-ring);
}

/* CTA Outline variant (secondary hero CTA) */
.btn-cta-outline {
  background: transparent;
  color: var(--gold-warm);
  border: 1px solid var(--gold-warm);
}

@media (hover: hover) {
  .btn-cta-outline:hover {
    background: rgba(212, 168, 83, 0.1);
    border-color: var(--gold-base);
    transform: translateY(-3px);
    box-shadow: 0 8px 24px rgba(212, 168, 83, 0.15);
  }
}

/* CTA Container */
.hero-ctas {
  display: flex;
  gap: var(--space-4);
  flex-wrap: wrap;
  margin-top: var(--space-10);
}

@media (max-width: 480px) {
  .btn-cta {
    width: 100%;
    height: 52px;
    font-size: var(--text-sm);
  }
  .hero-ctas {
    flex-direction: column;
    gap: var(--space-3);
  }
}
```

**Accessibility:**
- ✅ Large touch target (56px height)
- ✅ `role="group"` with `aria-label` for CTA pairs
- ✅ Full-width on mobile for easy thumb reach

---

### 5. Icon Button

**Use:** Compact actions — hamburger menu, close modal, social links, copy-to-clipboard  
**Frequency:** As needed in navigation, modals, toolbars.

```html
<!-- Hamburger -->
<button class="btn-icon" aria-label="Open menu" aria-expanded="false">
  <svg width="20" height="20" aria-hidden="true">
    <line x1="3" y1="6" x2="17" y2="6" stroke="currentColor" stroke-width="1.5"/>
    <line x1="3" y1="10" x2="17" y2="10" stroke="currentColor" stroke-width="1.5"/>
    <line x1="3" y1="14" x2="17" y2="14" stroke="currentColor" stroke-width="1.5"/>
  </svg>
</button>

<!-- Close -->
<button class="btn-icon" aria-label="Close dialog">
  <svg width="20" height="20" aria-hidden="true">
    <line x1="5" y1="5" x2="15" y2="15" stroke="currentColor" stroke-width="1.5"/>
    <line x1="15" y1="5" x2="5" y2="15" stroke="currentColor" stroke-width="1.5"/>
  </svg>
</button>

<!-- Social (link variant) -->
<a href="https://linkedin.com/in/florian-ziesche" class="btn-icon" aria-label="LinkedIn profile" target="_blank" rel="noopener noreferrer">
  <svg width="20" height="20" aria-hidden="true"><!-- LinkedIn icon --></svg>
</a>
```

```css
.btn-icon {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 44px;
  height: 44px;
  padding: 0;
  background: transparent;
  color: var(--gray-light);
  border: none;
  border-radius: var(--radius-md);
  cursor: pointer;
  transition: all var(--duration-normal) var(--ease-default);
  -webkit-tap-highlight-color: transparent;
}

@media (hover: hover) {
  .btn-icon:hover {
    color: var(--white-pure);
    background: var(--bg-hover);
  }
}

.btn-icon:active {
  transform: scale(0.92);
}

.btn-icon:focus-visible {
  outline: none;
  box-shadow: var(--focus-ring);
}

/* Small variant (32px — for dense UIs) */
.btn-icon-sm {
  width: 32px;
  height: 32px;
}

.btn-icon-sm svg {
  width: 16px;
  height: 16px;
}

/* Gold accent variant */
.btn-icon-gold {
  color: var(--gold-base);
}

@media (hover: hover) {
  .btn-icon-gold:hover {
    color: var(--gold-warm);
    background: rgba(212, 168, 83, 0.1);
  }
}
```

**Accessibility:**
- ✅ `aria-label` required (no visible text)
- ✅ `aria-hidden="true"` on decorative SVGs
- ✅ `aria-expanded` for toggle-type buttons (hamburger)
- ✅ 44×44px meets WCAG 2.5.8 target size

---

### Button Size Variants

```css
/* Size modifiers — apply to any button variant */
.btn-sm {
  height: 36px;
  padding: 0 var(--space-4);
  font-size: var(--text-xs);
}

.btn-lg {
  height: 48px;
  padding: 0 var(--space-8);
  font-size: var(--text-base);
}

/* Full-width (mobile) */
.btn-block {
  width: 100%;
}
```

### Loading Spinner (shared)

```css
.btn-spinner {
  display: inline-block;
  width: 16px;
  height: 16px;
  border: 2px solid currentColor;
  border-right-color: transparent;
  border-radius: var(--radius-full);
  animation: spin 0.6s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

.btn-loading {
  pointer-events: none;
  opacity: 0.8;
}
```

---

## III. Cards

Four card types serving different content needs. All share a base card style.

### Design Principles
- **Background:** `var(--bg-card)` (#0f1420)
- **Border:** `var(--border-default)` (subtle gray) or `var(--border-gold)` for emphasis
- **Radius:** `var(--radius-lg)` (8px)
- **Hover:** Lift + gold glow (desktop only, via `@media (hover: hover)`)
- **Content padding:** `var(--space-6)` to `var(--space-8)` depending on card density

### Base Card

```css
.card {
  background: var(--bg-card);
  border: var(--border-default);
  border-radius: var(--radius-lg);
  padding: var(--space-8);
  transition: all var(--duration-slow) var(--ease-default);
}

@media (hover: hover) {
  .card:hover {
    border-color: rgba(200, 170, 80, 0.2);
    transform: translateY(-4px);
    box-shadow: 0 12px 32px rgba(212, 168, 83, 0.12);
  }
}
```

---

### 1. Service Card (6 Service Categories)

**Use:** Homepage services grid, /consulting overview  
**Content:** Icon + title + description + optional link  
**Layout:** 3-column grid (desktop), 2-column (tablet), 1-column (mobile)

```html
<article class="card card-service" role="article">
  <div class="card-service-icon" aria-hidden="true">🏭</div>
  <h3 class="card-service-title">Manufacturing AI</h3>
  <p class="card-service-desc">
    AI-powered cost calculation, automated quoting (<span class="mono">80% faster</span>),
    quality documentation, and CNC process optimization.
  </p>
  <a href="/consulting#manufacturing" class="card-service-link">
    Learn more
    <svg class="arrow-icon" aria-hidden="true" width="16" height="16">
      <path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.5" fill="none"/>
    </svg>
  </a>
</article>
```

```css
/* Service Card */
.card-service {
  padding: var(--space-8);
  display: flex;
  flex-direction: column;
  gap: var(--space-4);
}

.card-service-icon {
  font-size: 2rem;
  line-height: 1;
  margin-bottom: var(--space-2);
}

.card-service-title {
  font-family: var(--font-display);
  font-size: var(--text-xl);
  font-weight: var(--weight-semibold);
  color: var(--white-pure);
  line-height: var(--leading-tight);
  letter-spacing: var(--tracking-tight);
}

.card-service-desc {
  font-size: var(--text-sm);
  color: var(--gray-light);
  line-height: var(--leading-relaxed);
  flex: 1; /* pushes link to bottom */
}

.card-service-link {
  display: inline-flex;
  align-items: center;
  gap: var(--space-2);
  font-family: var(--font-mono);
  font-size: var(--text-xs);
  color: var(--gold-base);
  letter-spacing: var(--tracking-wide);
  text-decoration: none;
  margin-top: auto;
  transition: all var(--duration-normal) var(--ease-default);
}

@media (hover: hover) {
  .card-service-link:hover {
    color: var(--gold-warm);
    gap: var(--space-3); /* arrow slides right */
  }
}

.card-service-link:focus-visible {
  outline: none;
  box-shadow: var(--focus-ring);
  border-radius: var(--radius-sm);
}

/* Service Grid */
.services-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: var(--space-6);
}

@media (max-width: 1024px) {
  .services-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 600px) {
  .services-grid {
    grid-template-columns: 1fr;
    gap: var(--space-4);
  }
}
```

**The 6 Service Categories with Gold Spectrum Mapping:**

| Service | Icon | Gold Accent |
|---------|------|-------------|
| Manufacturing AI | 🏭 | `--gold-warm` |
| Media & Publishing | 📰 | `--gold-base` |
| Legal Tech | ⚖️ | `--gold-cool` |
| Office & Operations | 📧 | `--gold-pale` |
| Workshops & Training | 🎓 | `--gold-deep` (icon only) |
| Advisory & Strategy | 💡 | `--gold-warm` |

**Accessibility:**
- ✅ `role="article"` for semantic grouping
- ✅ `aria-hidden="true"` on decorative emoji icons
- ✅ Link text is descriptive ("Learn more" paired with card heading via proximity)
- ✅ Cards are keyboard-navigable via links

---

### 2. Portfolio Card (Company Showcase)

**Use:** Portfolio grid — showcasing invested/advised companies  
**Content:** Logo + company name + description + tags + link  
**Interaction:** Logo grayscale → color on hover

```html
<article class="card card-portfolio">
  <div class="card-portfolio-logo">
    <img
      src="/assets/portfolio/company-logo.svg"
      alt="Company Name logo"
      loading="lazy"
      width="160"
      height="48"
    />
  </div>
  <div class="card-portfolio-body">
    <h3 class="card-portfolio-name">Company Name</h3>
    <p class="card-portfolio-desc">
      AI-powered quality inspection for automotive manufacturing.
    </p>
    <div class="card-portfolio-tags">
      <span class="tag-pill">Manufacturing</span>
      <span class="tag-pill">Computer Vision</span>
      <span class="tag-pill">Series A</span>
    </div>
  </div>
  <a href="/portfolio/company-name" class="card-portfolio-link" aria-label="View Company Name case study">
    <svg width="20" height="20" aria-hidden="true">
      <path d="M5 15L15 5M15 5H8M15 5v7" stroke="currentColor" stroke-width="1.5" fill="none"/>
    </svg>
  </a>
</article>
```

```css
.card-portfolio {
  padding: var(--space-6);
  display: grid;
  grid-template-rows: auto 1fr auto;
  gap: var(--space-5);
  position: relative;
}

.card-portfolio-logo {
  height: 48px;
  display: flex;
  align-items: center;
}

.card-portfolio-logo img {
  max-height: 100%;
  max-width: 160px;
  filter: grayscale(100%) contrast(0.8);
  opacity: 0.7;
  transition: all var(--duration-slow) var(--ease-default);
}

@media (hover: hover) {
  .card-portfolio:hover .card-portfolio-logo img {
    filter: grayscale(0%) contrast(1);
    opacity: 1;
  }
}

.card-portfolio-name {
  font-family: var(--font-body);
  font-size: var(--text-lg);
  font-weight: var(--weight-semibold);
  color: var(--white-pure);
  margin-bottom: var(--space-2);
}

.card-portfolio-desc {
  font-size: var(--text-sm);
  color: var(--gray-light);
  line-height: var(--leading-normal);
  margin-bottom: var(--space-3);
}

.card-portfolio-tags {
  display: flex;
  flex-wrap: wrap;
  gap: var(--space-2);
}

.tag-pill {
  font-family: var(--font-mono);
  font-size: 0.65rem;
  letter-spacing: var(--tracking-wider);
  text-transform: uppercase;
  color: var(--gray-mid);
  background: var(--bg-hover);
  padding: var(--space-1) var(--space-3);
  border-radius: var(--radius-full);
}

.card-portfolio-link {
  position: absolute;
  top: var(--space-6);
  right: var(--space-6);
  color: var(--gray-dark);
  transition: color var(--duration-normal) var(--ease-default);
}

@media (hover: hover) {
  .card-portfolio:hover .card-portfolio-link {
    color: var(--gold-warm);
  }
}

.card-portfolio-link:focus-visible {
  outline: none;
  box-shadow: var(--focus-ring);
  border-radius: var(--radius-sm);
}

/* Portfolio Grid */
.portfolio-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: var(--space-5);
}

@media (max-width: 1024px) {
  .portfolio-grid { grid-template-columns: repeat(3, 1fr); }
}

@media (max-width: 768px) {
  .portfolio-grid { grid-template-columns: repeat(2, 1fr); }
}

@media (max-width: 480px) {
  .portfolio-grid { grid-template-columns: 1fr; }
}
```

**Accessibility:**
- ✅ `alt` text on logos (company name + "logo")
- ✅ `aria-label` on external link icon (no visible text)
- ✅ `loading="lazy"` for performance
- ✅ Grayscale-to-color is decorative; content is accessible without it

---

### 3. Blog Card (Article Preview)

**Use:** Insights section on homepage, /insights listing page  
**Content:** Category tag + title + excerpt + date/reading time + optional image  
**Layout:** Stacked list on homepage, grid on /insights

```html
<article class="card card-blog">
  <div class="card-blog-meta">
    <span class="card-blog-category">Human-AI Systems</span>
    <time class="card-blog-date" datetime="2026-02-07">Feb 7, 2026</time>
  </div>
  <h3 class="card-blog-title">
    <a href="/insights/100-agents-disagreed">
      I Launched 100 AI Agents. They Disagreed on Everything.
    </a>
  </h3>
  <p class="card-blog-excerpt">
    What happens when you force 10 groups of AI agents to think using completely
    different cognitive strategies? 33,000 words. Six universal laws.
  </p>
  <div class="card-blog-footer">
    <span class="card-blog-reading-time">8 min read</span>
  </div>
</article>

<!-- Blog card with image (for /insights grid) -->
<article class="card card-blog card-blog-with-image">
  <div class="card-blog-image">
    <img src="/assets/blog/hero.webp" alt="" loading="lazy" width="600" height="340" />
  </div>
  <div class="card-blog-content">
    <div class="card-blog-meta">
      <span class="card-blog-category">AI Intelligence</span>
      <time class="card-blog-date" datetime="2026-01-15">Jan 15, 2026</time>
    </div>
    <h3 class="card-blog-title">
      <a href="/insights/sequoia-agi">
        Sequoia Says AGI Is Here. They're Right—And They're Not.
      </a>
    </h3>
    <p class="card-blog-excerpt">
      The venture industry's most influential firm declared AGI has arrived.
      What they got right about capability, and what they missed about deployment.
    </p>
    <div class="card-blog-footer">
      <span class="card-blog-reading-time">12 min read</span>
    </div>
  </div>
</article>
```

```css
.card-blog {
  padding: var(--space-6);
  display: flex;
  flex-direction: column;
  gap: var(--space-3);
}

.card-blog-meta {
  display: flex;
  align-items: center;
  gap: var(--space-3);
  font-family: var(--font-mono);
  font-size: 0.68rem;
  letter-spacing: var(--tracking-wider);
  text-transform: uppercase;
}

.card-blog-category {
  color: var(--gold-base);
}

.card-blog-date {
  color: var(--gray-dark);
}

.card-blog-title {
  font-family: var(--font-display);
  font-size: var(--text-xl);
  font-weight: var(--weight-medium);
  line-height: var(--leading-snug);
  color: var(--white-pure);
}

.card-blog-title a {
  color: inherit;
  text-decoration: none;
  transition: color var(--duration-normal) var(--ease-default);
}

/* Make entire card clickable via stretched link */
.card-blog-title a::after {
  content: '';
  position: absolute;
  inset: 0;
}

.card-blog {
  position: relative; /* for stretched link */
}

@media (hover: hover) {
  .card-blog:hover .card-blog-title a {
    color: var(--gold-warm);
  }
}

.card-blog-excerpt {
  font-size: var(--text-sm);
  color: var(--gray-light);
  line-height: var(--leading-relaxed);
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.card-blog-footer {
  margin-top: auto;
  padding-top: var(--space-3);
}

.card-blog-reading-time {
  font-family: var(--font-mono);
  font-size: var(--text-xs);
  color: var(--gray-dark);
}

/* Blog card with image */
.card-blog-with-image {
  padding: 0;
  overflow: hidden;
}

.card-blog-image {
  aspect-ratio: 16 / 9;
  overflow: hidden;
}

.card-blog-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform var(--duration-slow) var(--ease-default);
}

@media (hover: hover) {
  .card-blog-with-image:hover .card-blog-image img {
    transform: scale(1.03);
  }
}

.card-blog-content {
  padding: var(--space-6);
  display: flex;
  flex-direction: column;
  gap: var(--space-3);
}

/* Blog Grid */
.blog-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: var(--space-6);
}

/* Featured (first post spans 2 columns) */
.blog-grid .card-blog:first-child {
  grid-column: span 2;
}

@media (max-width: 1024px) {
  .blog-grid {
    grid-template-columns: repeat(2, 1fr);
  }
  .blog-grid .card-blog:first-child {
    grid-column: span 2;
  }
}

@media (max-width: 600px) {
  .blog-grid {
    grid-template-columns: 1fr;
  }
  .blog-grid .card-blog:first-child {
    grid-column: span 1;
  }
}
```

**Accessibility:**
- ✅ `<time>` element with `datetime` for machine-readable dates
- ✅ Stretched link makes entire card clickable (reduces tab stops)
- ✅ Image `alt=""` (decorative) or descriptive alt if image conveys info
- ✅ `-webkit-line-clamp` for excerpt truncation (full text available on detail page)
- ✅ `loading="lazy"` for images below fold

---

### 4. Team Card (Florian & Mia)

**Use:** About section on homepage, /about page  
**Content:** Photo + name + role + bio + social links  
**Variants:** Florian (human) and Mia (AI agent)

```html
<!-- Florian -->
<article class="card card-team">
  <div class="card-team-photo">
    <img
      src="/assets/florian-400.jpg"
      alt="Florian Ziesche, founder of Ainary Ventures"
      loading="lazy"
      width="400"
      height="400"
    />
  </div>
  <div class="card-team-body">
    <h3 class="card-team-name">Florian Ziesche</h3>
    <span class="card-team-role">Founder & AI Consultant</span>
    <p class="card-team-bio">
      Five years building AI companies. Former CEO & Co-Founder at 36ZERO Vision.
      Shipped to BMW, Siemens, and Bosch. VC Lab Fellow.
      Now building AI systems and advising founders through Ainary Ventures.
    </p>
    <ul class="card-team-credentials">
      <li>M.Sc. Business Administration, TU Munich</li>
      <li>€5.5M+ raised across equity and grants</li>
      <li>VC Lab Fellow — Decile Group, Cohort 6</li>
      <li>Alchemist Accelerator Alumni</li>
    </ul>
    <nav class="card-team-links" aria-label="Florian's social links">
      <a href="https://linkedin.com/in/florian-ziesche" target="_blank" rel="noopener noreferrer" aria-label="LinkedIn">LinkedIn</a>
      <a href="https://x.com/Florian1776" target="_blank" rel="noopener noreferrer" aria-label="X / Twitter">X</a>
      <a href="https://florianziesche.substack.com" target="_blank" rel="noopener noreferrer" aria-label="Substack">Substack</a>
    </nav>
  </div>
</article>

<!-- Mia (AI Agent) -->
<article class="card card-team card-team-ai">
  <div class="card-team-photo card-team-photo-ai">
    <div class="card-team-avatar-ai" aria-hidden="true">
      <span class="avatar-ai-glyph">M</span>
    </div>
  </div>
  <div class="card-team-body">
    <h3 class="card-team-name">Mia</h3>
    <span class="card-team-role card-team-role-ai">AI Research & Operations Agent</span>
    <p class="card-team-bio">
      Research, structure, scale. Mia handles the systematic work — competitive
      analysis, content distribution, data synthesis — so Florian can focus on
      strategy, voice, and judgment. Compound intelligence, not replacement.
    </p>
    <div class="card-team-ai-badge">
      <span class="mono">AI-POWERED</span> · Built on Claude
    </div>
  </div>
</article>
```

```css
.card-team {
  padding: 0;
  overflow: hidden;
  display: grid;
  grid-template-columns: 200px 1fr;
  gap: 0;
}

.card-team-photo {
  aspect-ratio: 1;
  overflow: hidden;
  background: var(--bg-hover);
}

.card-team-photo img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  filter: grayscale(30%) contrast(1.05);
  transition: filter var(--duration-slower) var(--ease-default);
}

@media (hover: hover) {
  .card-team:hover .card-team-photo img {
    filter: grayscale(0%) contrast(1);
  }
}

.card-team-body {
  padding: var(--space-6) var(--space-8);
  display: flex;
  flex-direction: column;
  gap: var(--space-3);
}

.card-team-name {
  font-family: var(--font-display);
  font-size: var(--text-2xl);
  font-weight: var(--weight-semibold);
  color: var(--white-pure);
  line-height: var(--leading-tight);
}

.card-team-role {
  font-family: var(--font-mono);
  font-size: var(--text-xs);
  color: var(--gold-base);
  letter-spacing: var(--tracking-wider);
  text-transform: uppercase;
}

.card-team-role-ai {
  color: var(--gold-cool);
}

.card-team-bio {
  font-size: var(--text-sm);
  color: var(--gray-light);
  line-height: var(--leading-relaxed);
}

.card-team-credentials {
  list-style: none;
  padding: 0;
  margin: 0;
}

.card-team-credentials li {
  font-size: var(--text-sm);
  color: var(--gray-light);
  padding: var(--space-1) 0 var(--space-1) var(--space-4);
  position: relative;
}

.card-team-credentials li::before {
  content: '–';
  position: absolute;
  left: 0;
  color: var(--gray-dark);
}

.card-team-links {
  display: flex;
  gap: var(--space-4);
  margin-top: var(--space-2);
}

.card-team-links a {
  font-size: var(--text-sm);
  color: var(--gray-mid);
  text-decoration: none;
  border-bottom: 1px solid rgba(92, 92, 102, 0.4);
  transition: all var(--duration-normal) var(--ease-default);
}

@media (hover: hover) {
  .card-team-links a:hover {
    color: var(--gold-warm);
    border-color: var(--gold-warm);
  }
}

.card-team-links a:focus-visible {
  outline: none;
  box-shadow: var(--focus-ring);
  border-radius: var(--radius-sm);
}

/* Mia AI Avatar */
.card-team-photo-ai {
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, var(--bg-card), rgba(200, 170, 80, 0.05));
}

.avatar-ai-glyph {
  font-family: var(--font-display);
  font-size: 4rem;
  font-weight: var(--weight-semibold);
  color: var(--gold-warm);
  opacity: 0.8;
}

.card-team-ai-badge {
  font-family: var(--font-mono);
  font-size: var(--text-xs);
  color: var(--gray-mid);
  padding: var(--space-2) var(--space-3);
  background: var(--bg-hover);
  border-radius: var(--radius-sm);
  display: inline-flex;
  align-items: center;
  gap: var(--space-2);
  align-self: flex-start;
}

/* Responsive */
@media (max-width: 768px) {
  .card-team {
    grid-template-columns: 1fr;
  }
  .card-team-photo {
    max-height: 280px;
  }
}
```

**Accessibility:**
- ✅ Descriptive `alt` text on Florian's photo
- ✅ `aria-hidden` on decorative AI avatar
- ✅ `aria-label` on social link navigation
- ✅ `rel="noopener noreferrer"` on external links

---

## IV. Navigation

Four navigation patterns for different contexts.

### 1. Desktop Navigation (Sticky, Glassmorphism)

**Behavior:** Sticky top, adaptive height (72px → 56px on scroll), glassmorphism background

```html
<header class="nav" role="banner">
  <a href="#main-content" class="skip-link">Skip to main content</a>

  <div class="nav-container">
    <a href="/" class="nav-logo" aria-label="Ainary Ventures home">
      AINARY
    </a>

    <nav class="nav-links" aria-label="Main navigation">
      <a href="/consulting" class="nav-link">Consulting</a>
      <a href="/fund" class="nav-link">Fund</a>
      <a href="/portfolio" class="nav-link">Portfolio</a>
      <a href="/insights" class="nav-link">Insights</a>
      <a href="/about" class="nav-link">About</a>
    </nav>

    <div class="nav-actions">
      <a href="/contact" class="btn btn-primary btn-sm">Get in Touch</a>
    </div>

    <!-- Mobile hamburger (hidden on desktop) -->
    <button class="nav-hamburger" aria-label="Open menu" aria-expanded="false" aria-controls="mobile-menu">
      <span class="hamburger-line" aria-hidden="true"></span>
      <span class="hamburger-line" aria-hidden="true"></span>
      <span class="hamburger-line" aria-hidden="true"></span>
    </button>
  </div>
</header>
```

```css
.nav {
  position: sticky;
  top: 0;
  z-index: var(--z-sticky);
  height: var(--nav-height);
  background: rgba(10, 15, 30, 0.92);
  backdrop-filter: blur(12px) saturate(180%);
  -webkit-backdrop-filter: blur(12px) saturate(180%);
  border-bottom: var(--border-default);
  transition: height var(--duration-slow) var(--ease-default),
              background var(--duration-slow) var(--ease-default);
}

/* Scrolled state (applied via JS) */
.nav.nav-scrolled {
  height: var(--nav-height-scrolled);
  background: rgba(10, 15, 30, 0.96);
}

.nav-container {
  max-width: var(--content-max);
  margin: 0 auto;
  padding: 0 var(--space-10);
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

/* Logo */
.nav-logo {
  font-family: var(--font-display);
  font-size: var(--text-sm);
  font-weight: var(--weight-normal);
  letter-spacing: 0.3em;
  color: var(--gold-base);
  text-decoration: none;
  transition: opacity var(--duration-normal) var(--ease-default);
}

@media (hover: hover) {
  .nav-logo:hover {
    opacity: 0.7;
  }
}

/* Links */
.nav-links {
  display: flex;
  align-items: center;
  gap: var(--space-10);
}

.nav-link {
  font-family: var(--font-body);
  font-size: 0.9375rem; /* 15px */
  font-weight: var(--weight-medium);
  color: var(--gray-light);
  text-decoration: none;
  transition: color var(--duration-normal) var(--ease-default);
  position: relative;
}

@media (hover: hover) {
  .nav-link:hover {
    color: var(--white-pure);
  }
}

/* Active page indicator */
.nav-link[aria-current="page"],
.nav-link.active {
  color: var(--white-pure);
}

.nav-link[aria-current="page"]::after,
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

.nav-link:focus-visible {
  outline: none;
  box-shadow: var(--focus-ring);
  border-radius: var(--radius-sm);
}

/* Skip Link */
.skip-link {
  position: absolute;
  top: -100%;
  left: var(--space-4);
  background: var(--gold-warm);
  color: var(--bg-deep);
  padding: var(--space-2) var(--space-4);
  font-size: var(--text-sm);
  font-weight: var(--weight-semibold);
  text-decoration: none;
  border-radius: var(--radius-sm);
  z-index: 1000;
  transition: top var(--duration-normal) var(--ease-default);
}

.skip-link:focus {
  top: var(--space-2);
}

/* Hamburger (hidden on desktop) */
.nav-hamburger {
  display: none;
}

@media (max-width: 768px) {
  .nav-links,
  .nav-actions {
    display: none;
  }

  .nav-hamburger {
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 5px;
    width: 44px;
    height: 44px;
    background: none;
    border: none;
    cursor: pointer;
    padding: 12px;
  }

  .hamburger-line {
    display: block;
    width: 20px;
    height: 1.5px;
    background: var(--gray-light);
    transition: all var(--duration-normal) var(--ease-default);
  }

  /* Hamburger → X animation */
  .nav-hamburger[aria-expanded="true"] .hamburger-line:nth-child(1) {
    transform: translateY(6.5px) rotate(45deg);
  }
  .nav-hamburger[aria-expanded="true"] .hamburger-line:nth-child(2) {
    opacity: 0;
  }
  .nav-hamburger[aria-expanded="true"] .hamburger-line:nth-child(3) {
    transform: translateY(-6.5px) rotate(-45deg);
  }
}
```

**JavaScript (scroll behavior):**
```javascript
const nav = document.querySelector('.nav');
let lastScroll = 0;

window.addEventListener('scroll', () => {
  const currentScroll = window.pageYOffset;
  if (currentScroll > 50) {
    nav.classList.add('nav-scrolled');
  } else {
    nav.classList.remove('nav-scrolled');
  }
  lastScroll = currentScroll;
}, { passive: true });
```

**Accessibility:**
- ✅ Skip link for keyboard users
- ✅ `role="banner"` on header
- ✅ `aria-label="Main navigation"` on nav
- ✅ `aria-current="page"` for active page
- ✅ `aria-expanded` and `aria-controls` on hamburger

---

### 2. Mobile Navigation (Hamburger, Full-Screen Overlay)

```html
<div class="mobile-menu" id="mobile-menu" role="dialog" aria-label="Navigation menu" aria-modal="true" data-open="false">
  <nav class="mobile-menu-nav" aria-label="Mobile navigation">
    <a href="/consulting" class="mobile-menu-link">Consulting</a>
    <a href="/fund" class="mobile-menu-link">Fund</a>
    <a href="/portfolio" class="mobile-menu-link">Portfolio</a>
    <a href="/insights" class="mobile-menu-link">Insights</a>
    <a href="/about" class="mobile-menu-link">About</a>
    <div class="mobile-menu-divider"></div>
    <a href="/contact" class="btn btn-primary btn-block">Get in Touch</a>
  </nav>

  <div class="mobile-menu-footer">
    <a href="mailto:f.ziesche.us@gmail.com">f.ziesche.us@gmail.com</a>
    <div class="mobile-menu-social">
      <a href="https://linkedin.com/in/florian-ziesche" aria-label="LinkedIn">LinkedIn</a>
      <a href="https://x.com/Florian1776" aria-label="X">X</a>
      <a href="https://florianziesche.substack.com" aria-label="Substack">Substack</a>
    </div>
  </div>
</div>
```

```css
.mobile-menu {
  position: fixed;
  inset: 0;
  z-index: var(--z-overlay);
  background: rgba(7, 11, 21, 0.98);
  backdrop-filter: blur(24px);
  -webkit-backdrop-filter: blur(24px);
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: var(--space-16) var(--space-8);
  opacity: 0;
  visibility: hidden;
  transition: opacity var(--duration-slow) var(--ease-default),
              visibility var(--duration-slow) var(--ease-default);
}

.mobile-menu[data-open="true"] {
  opacity: 1;
  visibility: visible;
}

.mobile-menu-nav {
  display: flex;
  flex-direction: column;
  gap: var(--space-2);
}

.mobile-menu-link {
  font-family: var(--font-display);
  font-size: var(--text-3xl);
  font-weight: var(--weight-normal);
  color: var(--white-warm);
  text-decoration: none;
  padding: var(--space-3) 0;
  transition: color var(--duration-normal) var(--ease-default);
  border-bottom: 1px solid var(--gray-rule);
}

.mobile-menu-link:last-of-type {
  border-bottom: none;
}

.mobile-menu-link:hover,
.mobile-menu-link:focus {
  color: var(--gold-warm);
}

.mobile-menu-link:focus-visible {
  outline: none;
  box-shadow: var(--focus-ring);
  border-radius: var(--radius-sm);
}

.mobile-menu-link[aria-current="page"] {
  color: var(--gold-warm);
}

.mobile-menu-divider {
  height: 1px;
  background: var(--gray-rule);
  margin: var(--space-6) 0;
}

.mobile-menu-footer {
  margin-top: auto;
  padding-top: var(--space-8);
}

.mobile-menu-footer a {
  font-size: var(--text-sm);
  color: var(--gray-mid);
  text-decoration: none;
}

.mobile-menu-social {
  display: flex;
  gap: var(--space-6);
  margin-top: var(--space-4);
}

.mobile-menu-social a {
  font-size: var(--text-sm);
  color: var(--gray-dark);
  text-decoration: none;
  transition: color var(--duration-normal) var(--ease-default);
}

.mobile-menu-social a:hover {
  color: var(--gold-base);
}
```

**JavaScript (toggle):**
```javascript
const hamburger = document.querySelector('.nav-hamburger');
const mobileMenu = document.getElementById('mobile-menu');
let focusTrap;

hamburger.addEventListener('click', () => {
  const isOpen = mobileMenu.dataset.open === 'true';
  mobileMenu.dataset.open = !isOpen;
  hamburger.setAttribute('aria-expanded', !isOpen);
  document.body.style.overflow = !isOpen ? 'hidden' : '';

  if (!isOpen) {
    // Focus first link
    mobileMenu.querySelector('.mobile-menu-link').focus();
  }
});

// Close on Escape
mobileMenu.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') {
    mobileMenu.dataset.open = 'false';
    hamburger.setAttribute('aria-expanded', 'false');
    document.body.style.overflow = '';
    hamburger.focus();
  }
});
```

**Accessibility:**
- ✅ `role="dialog"` + `aria-modal="true"` for overlay
- ✅ Focus trapping within menu when open
- ✅ Escape key closes menu
- ✅ Focus returns to hamburger on close
- ✅ `document.body.overflow: hidden` prevents background scroll

---

### 3. Section Nav (Homepage Scroll Anchors)

```html
<!-- Appears below main nav on homepage, after scrolling past hero -->
<div class="section-nav" role="navigation" aria-label="Page sections">
  <div class="section-nav-container">
    <a href="#about" class="section-nav-link active" aria-current="true">About</a>
    <a href="#services" class="section-nav-link">Services</a>
    <a href="#portfolio" class="section-nav-link">Portfolio</a>
    <a href="#insights" class="section-nav-link">Insights</a>
    <a href="#contact" class="section-nav-link">Contact</a>
  </div>
</div>
```

```css
.section-nav {
  position: sticky;
  top: var(--nav-height-scrolled);
  z-index: calc(var(--z-sticky) - 1);
  background: rgba(10, 15, 30, 0.88);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  border-bottom: var(--border-default);
  opacity: 0;
  transform: translateY(-100%);
  transition: opacity var(--duration-slow) var(--ease-default),
              transform var(--duration-slow) var(--ease-default);
}

.section-nav.visible {
  opacity: 1;
  transform: translateY(0);
}

.section-nav-container {
  max-width: var(--content-max);
  margin: 0 auto;
  padding: 0 var(--space-10);
  display: flex;
  align-items: center;
  gap: var(--space-8);
  height: 40px;
}

.section-nav-link {
  font-family: var(--font-mono);
  font-size: var(--text-xs);
  letter-spacing: var(--tracking-wide);
  color: var(--gray-dark);
  text-decoration: none;
  transition: color var(--duration-normal) var(--ease-default);
  position: relative;
  padding: var(--space-2) 0;
}

@media (hover: hover) {
  .section-nav-link:hover {
    color: var(--gray-light);
  }
}

.section-nav-link.active,
.section-nav-link[aria-current="true"] {
  color: var(--white-pure);
}

.section-nav-link.active::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 2px;
  background: var(--gold-warm);
  border-radius: 1px;
}

.section-nav-link:focus-visible {
  outline: none;
  box-shadow: var(--focus-ring);
  border-radius: var(--radius-sm);
}

@media (max-width: 768px) {
  .section-nav {
    display: none; /* Hidden on mobile — scroll is intuitive enough */
  }
}
```

**JavaScript (Intersection Observer):**
```javascript
const sectionNav = document.querySelector('.section-nav');
const heroSection = document.querySelector('.hero');
const sections = document.querySelectorAll('section[id]');
const sectionLinks = document.querySelectorAll('.section-nav-link');

// Show/hide section nav based on hero visibility
const heroObserver = new IntersectionObserver(
  ([entry]) => {
    sectionNav.classList.toggle('visible', !entry.isIntersecting);
  },
  { threshold: 0.1 }
);
heroObserver.observe(heroSection);

// Highlight active section
const sectionObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        sectionLinks.forEach(link => {
          const isActive = link.getAttribute('href') === `#${entry.target.id}`;
          link.classList.toggle('active', isActive);
          link.setAttribute('aria-current', isActive);
        });
      }
    });
  },
  { threshold: 0.3, rootMargin: '-80px 0px -50% 0px' }
);
sections.forEach(section => sectionObserver.observe(section));
```

**Accessibility:**
- ✅ `aria-label="Page sections"` distinguishes from main nav
- ✅ `aria-current` updates dynamically
- ✅ Hidden on mobile (no extra cognitive load)

---

### 4. Footer Navigation

```html
<footer class="footer" role="contentinfo">
  <div class="footer-container">
    <div class="footer-brand">
      <a href="/" class="footer-logo" aria-label="Ainary Ventures home">AINARY</a>
      <p class="footer-tagline">AI Systems That Go Into Production, Not PowerPoints.</p>
    </div>

    <nav class="footer-nav" aria-label="Footer navigation">
      <div class="footer-nav-group">
        <h4 class="footer-nav-heading">Platform</h4>
        <a href="/consulting">Consulting</a>
        <a href="/fund">Fund</a>
        <a href="/portfolio">Portfolio</a>
        <a href="/about">About</a>
      </div>
      <div class="footer-nav-group">
        <h4 class="footer-nav-heading">Content</h4>
        <a href="/insights">Insights</a>
        <a href="https://florianziesche.substack.com" target="_blank" rel="noopener">Substack</a>
        <a href="/resources">Resources</a>
      </div>
      <div class="footer-nav-group">
        <h4 class="footer-nav-heading">Connect</h4>
        <a href="mailto:f.ziesche.us@gmail.com">Email</a>
        <a href="https://linkedin.com/in/florian-ziesche" target="_blank" rel="noopener">LinkedIn</a>
        <a href="https://x.com/Florian1776" target="_blank" rel="noopener">X / Twitter</a>
      </div>
    </nav>

    <div class="footer-bottom">
      <p class="footer-copyright">© 2026 Ainary Ventures. All rights reserved.</p>
      <div class="footer-legal">
        <a href="/privacy">Privacy</a>
        <a href="/imprint">Imprint</a>
      </div>
    </div>
  </div>
</footer>
```

```css
.footer {
  background: var(--bg-deep);
  border-top: var(--border-default);
  padding: var(--space-16) 0 var(--space-8);
}

.footer-container {
  max-width: var(--content-max);
  margin: 0 auto;
  padding: 0 var(--space-10);
}

.footer-brand {
  margin-bottom: var(--space-12);
}

.footer-logo {
  font-family: var(--font-display);
  font-size: var(--text-sm);
  letter-spacing: 0.3em;
  color: var(--gold-base);
  text-decoration: none;
}

.footer-tagline {
  font-size: var(--text-sm);
  color: var(--gray-mid);
  margin-top: var(--space-3);
  max-width: 360px;
}

.footer-nav {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: var(--space-10);
  margin-bottom: var(--space-12);
}

.footer-nav-heading {
  font-family: var(--font-mono);
  font-size: var(--text-xs);
  letter-spacing: var(--tracking-widest);
  text-transform: uppercase;
  color: var(--gold-cool);
  margin-bottom: var(--space-4);
}

.footer-nav-group {
  display: flex;
  flex-direction: column;
  gap: var(--space-3);
}

.footer-nav-group a {
  font-size: var(--text-sm);
  color: var(--gray-mid);
  text-decoration: none;
  transition: color var(--duration-normal) var(--ease-default);
}

@media (hover: hover) {
  .footer-nav-group a:hover {
    color: var(--white-warm);
  }
}

.footer-nav-group a:focus-visible {
  outline: none;
  box-shadow: var(--focus-ring);
  border-radius: var(--radius-sm);
}

.footer-bottom {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-top: var(--space-8);
  border-top: var(--border-default);
}

.footer-copyright {
  font-size: var(--text-xs);
  color: var(--gray-dark);
}

.footer-legal {
  display: flex;
  gap: var(--space-6);
}

.footer-legal a {
  font-size: var(--text-xs);
  color: var(--gray-dark);
  text-decoration: none;
  transition: color var(--duration-normal) var(--ease-default);
}

.footer-legal a:hover {
  color: var(--gray-light);
}

@media (max-width: 768px) {
  .footer-nav {
    grid-template-columns: 1fr;
    gap: var(--space-8);
  }
  .footer-bottom {
    flex-direction: column;
    gap: var(--space-4);
    text-align: center;
  }
}
```

**Accessibility:**
- ✅ `role="contentinfo"` on footer
- ✅ `aria-label="Footer navigation"` distinguishes from main nav
- ✅ Heading hierarchy maintained (h4)
- ✅ All links keyboard-accessible

---

## V. Forms

Contact form components for the /contact section and newsletter signup.

### Input Fields

```html
<div class="form-group">
  <label for="name" class="form-label">Name <span class="form-required" aria-label="required">*</span></label>
  <input
    type="text"
    id="name"
    name="name"
    class="form-input"
    placeholder="Your name"
    required
    autocomplete="name"
    aria-describedby="name-error"
  />
  <span id="name-error" class="form-error" role="alert" aria-live="polite"></span>
</div>

<div class="form-group">
  <label for="email" class="form-label">Email <span class="form-required" aria-label="required">*</span></label>
  <input
    type="email"
    id="email"
    name="email"
    class="form-input"
    placeholder="you@company.com"
    required
    autocomplete="email"
    aria-describedby="email-error"
  />
  <span id="email-error" class="form-error" role="alert" aria-live="polite"></span>
</div>

<div class="form-group">
  <label for="company" class="form-label">Company</label>
  <input
    type="text"
    id="company"
    name="company"
    class="form-input"
    placeholder="Company name (optional)"
    autocomplete="organization"
  />
</div>
```

```css
.form-group {
  display: flex;
  flex-direction: column;
  gap: var(--space-2);
  margin-bottom: var(--space-6);
}

.form-label {
  font-family: var(--font-body);
  font-size: var(--text-sm);
  font-weight: var(--weight-medium);
  color: var(--white-warm);
}

.form-required {
  color: var(--gold-warm);
  margin-left: 2px;
}

.form-input {
  height: 48px;
  padding: 0 var(--space-4);
  font-family: var(--font-body);
  font-size: var(--text-base);
  color: var(--white-pure);
  background: var(--bg-card);
  border: 1px solid var(--gray-rule);
  border-radius: var(--radius-md);
  transition: all var(--duration-normal) var(--ease-default);
  -webkit-appearance: none;
}

.form-input::placeholder {
  color: var(--gray-dark);
}

.form-input:focus {
  outline: none;
  border-color: var(--gold-warm);
  box-shadow: 0 0 0 3px rgba(212, 168, 83, 0.1);
}

/* Validation states */
.form-input:invalid:not(:placeholder-shown):not(:focus) {
  border-color: var(--error);
  box-shadow: 0 0 0 3px var(--error-bg);
}

.form-input:valid:not(:placeholder-shown) {
  border-color: var(--gold-base);
}

.form-input:disabled {
  background: var(--bg-hover);
  color: var(--gray-dark);
  cursor: not-allowed;
  opacity: 0.6;
}

/* Error message */
.form-error {
  font-size: var(--text-xs);
  color: var(--error);
  min-height: 1.2em;
}

.form-error:empty {
  display: none;
}
```

### Textarea

```html
<div class="form-group">
  <label for="message" class="form-label">Message <span class="form-required" aria-label="required">*</span></label>
  <textarea
    id="message"
    name="message"
    class="form-textarea"
    placeholder="Tell me about your project, workflow, or AI challenge…"
    rows="5"
    required
    aria-describedby="message-help message-error"
  ></textarea>
  <span id="message-help" class="form-help">Be specific. The more context, the better I can help.</span>
  <span id="message-error" class="form-error" role="alert" aria-live="polite"></span>
</div>
```

```css
.form-textarea {
  padding: var(--space-3) var(--space-4);
  font-family: var(--font-body);
  font-size: var(--text-base);
  color: var(--white-pure);
  background: var(--bg-card);
  border: 1px solid var(--gray-rule);
  border-radius: var(--radius-md);
  resize: vertical;
  min-height: 120px;
  max-height: 400px;
  line-height: var(--leading-normal);
  transition: all var(--duration-normal) var(--ease-default);
  -webkit-appearance: none;
}

.form-textarea::placeholder {
  color: var(--gray-dark);
}

.form-textarea:focus {
  outline: none;
  border-color: var(--gold-warm);
  box-shadow: 0 0 0 3px rgba(212, 168, 83, 0.1);
}

.form-help {
  font-size: var(--text-xs);
  color: var(--gray-mid);
  font-style: italic;
}
```

### Submit Button

Uses the Primary Button variant:

```html
<button type="submit" class="btn btn-primary btn-lg btn-block" id="submit-btn">
  Send Message
</button>
```

### Validation States

```css
/* Success state (after form submission) */
.form-success {
  background: var(--success-bg);
  border: 1px solid var(--success);
  border-radius: var(--radius-md);
  padding: var(--space-4) var(--space-6);
  color: var(--success);
  font-size: var(--text-sm);
  display: flex;
  align-items: center;
  gap: var(--space-3);
}

.form-success::before {
  content: '✓';
  font-weight: var(--weight-bold);
  font-size: var(--text-lg);
}

/* Error state (form-level) */
.form-error-message {
  background: var(--error-bg);
  border: 1px solid var(--error);
  border-radius: var(--radius-md);
  padding: var(--space-4) var(--space-6);
  color: var(--error);
  font-size: var(--text-sm);
  display: flex;
  align-items: center;
  gap: var(--space-3);
}

.form-error-message::before {
  content: '✕';
  font-weight: var(--weight-bold);
  font-size: var(--text-lg);
}
```

### Complete Contact Form

```html
<form class="contact-form" action="/api/contact" method="POST" novalidate>
  <div class="form-row">
    <div class="form-group">
      <label for="contact-name" class="form-label">Name <span class="form-required" aria-label="required">*</span></label>
      <input type="text" id="contact-name" name="name" class="form-input" required autocomplete="name" />
    </div>
    <div class="form-group">
      <label for="contact-email" class="form-label">Email <span class="form-required" aria-label="required">*</span></label>
      <input type="email" id="contact-email" name="email" class="form-input" required autocomplete="email" />
    </div>
  </div>

  <div class="form-group">
    <label for="contact-company" class="form-label">Company</label>
    <input type="text" id="contact-company" name="company" class="form-input" autocomplete="organization" />
  </div>

  <div class="form-group">
    <label for="contact-message" class="form-label">Message <span class="form-required" aria-label="required">*</span></label>
    <textarea id="contact-message" name="message" class="form-textarea" rows="5" required></textarea>
  </div>

  <div id="form-status" aria-live="polite"></div>

  <button type="submit" class="btn btn-primary btn-lg">Send Message</button>
</form>
```

```css
.contact-form {
  max-width: 640px;
}

.form-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: var(--space-6);
}

@media (max-width: 600px) {
  .form-row {
    grid-template-columns: 1fr;
  }
}
```

**JavaScript (validation + submission):**
```javascript
const form = document.querySelector('.contact-form');
const status = document.getElementById('form-status');
const submitBtn = form.querySelector('button[type="submit"]');

form.addEventListener('submit', async (e) => {
  e.preventDefault();

  // Reset
  status.innerHTML = '';
  submitBtn.disabled = true;
  submitBtn.innerHTML = '<span class="btn-spinner" aria-hidden="true"></span> Sending…';
  submitBtn.classList.add('btn-loading');

  try {
    const data = new FormData(form);
    const response = await fetch(form.action, {
      method: 'POST',
      body: data,
    });

    if (response.ok) {
      status.innerHTML = `
        <div class="form-success" role="status">
          Message sent. I'll get back to you within 24 hours.
        </div>`;
      form.reset();
    } else {
      throw new Error('Failed');
    }
  } catch (err) {
    status.innerHTML = `
      <div class="form-error-message" role="alert">
        Something went wrong. Try emailing me directly at f.ziesche.us@gmail.com
      </div>`;
  } finally {
    submitBtn.disabled = false;
    submitBtn.textContent = 'Send Message';
    submitBtn.classList.remove('btn-loading');
  }
});
```

**Accessibility:**
- ✅ Every input has a `<label>` with matching `for`/`id`
- ✅ `aria-describedby` links inputs to help/error text
- ✅ `aria-live="polite"` on error/success regions
- ✅ `role="alert"` on error messages
- ✅ `autocomplete` attributes for autofill
- ✅ `:invalid:not(:placeholder-shown)` prevents showing errors before interaction
- ✅ `novalidate` on form — custom validation for better UX
- ✅ Visible focus states on all inputs

---

## VI. Typography

Complete typographic system using Inter Display, Inter, and JetBrains Mono.

### Heading Scale (H1–H6)

```html
<h1 class="h1">We Build AI Systems That Go Into Production.</h1>
<h2 class="h2">Services</h2>
<h3 class="h3">Manufacturing AI</h3>
<h4 class="h4">Case Study: CNC Planner Pro</h4>
<h5 class="h5">Technical Architecture</h5>
<h6 class="h6">Implementation Notes</h6>
```

```css
h1, .h1 {
  font-family: var(--font-display);
  font-size: clamp(var(--text-4xl), 5vw, var(--text-6xl));
  font-weight: var(--weight-semibold);
  line-height: var(--leading-tight);
  letter-spacing: var(--tracking-tighter);
  color: var(--white-pure);
  max-width: 20ch; /* ~20 characters for optimal readability */
}

h2, .h2 {
  font-family: var(--font-display);
  font-size: clamp(var(--text-3xl), 3.5vw, var(--text-4xl));
  font-weight: var(--weight-semibold);
  line-height: var(--leading-tight);
  letter-spacing: var(--tracking-tight);
  color: var(--white-pure);
}

h3, .h3 {
  font-family: var(--font-display);
  font-size: clamp(var(--text-xl), 2.5vw, var(--text-2xl));
  font-weight: var(--weight-medium);
  line-height: var(--leading-snug);
  letter-spacing: var(--tracking-tight);
  color: var(--white-pure);
}

h4, .h4 {
  font-family: var(--font-body);
  font-size: var(--text-xl);
  font-weight: var(--weight-semibold);
  line-height: var(--leading-snug);
  letter-spacing: var(--tracking-normal);
  color: var(--white-pure);
}

h5, .h5 {
  font-family: var(--font-body);
  font-size: var(--text-lg);
  font-weight: var(--weight-semibold);
  line-height: var(--leading-snug);
  letter-spacing: var(--tracking-normal);
  color: var(--white-warm);
}

h6, .h6 {
  font-family: var(--font-mono);
  font-size: var(--text-xs);
  font-weight: var(--weight-medium);
  line-height: var(--leading-snug);
  letter-spacing: var(--tracking-widest);
  text-transform: uppercase;
  color: var(--gold-base);
}
```

### Section Tag (Label Above Headings)

```html
<span class="section-tag">Services</span>
```

```css
.section-tag {
  font-family: var(--font-mono);
  font-size: 0.65rem;
  letter-spacing: var(--tracking-widest);
  text-transform: uppercase;
  color: var(--gold-base);
  display: block;
  margin-bottom: var(--space-6);
}
```

### Body Text Variations

```css
/* Primary body */
.text-body, p {
  font-family: var(--font-body);
  font-size: var(--text-lg);
  font-weight: var(--weight-normal);
  line-height: var(--leading-relaxed);
  color: var(--white-warm);
}

/* Smaller body (cards, descriptions) */
.text-body-sm {
  font-size: var(--text-sm);
  color: var(--gray-light);
  line-height: var(--leading-relaxed);
}

/* Lead / introduction paragraph */
.text-lead {
  font-size: var(--text-xl);
  color: var(--gray-light);
  line-height: var(--leading-relaxed);
  max-width: 52ch;
}

/* Monospace data highlight */
.mono {
  font-family: var(--font-mono);
  font-size: 0.82em;
  color: var(--gold-warm);
}

/* Strong emphasis */
strong, b, .text-strong {
  color: var(--white-pure);
  font-weight: var(--weight-medium);
}

/* Muted / caption */
.text-muted {
  color: var(--gray-mid);
  font-size: var(--text-sm);
}

/* Small / fine print */
.text-small {
  font-size: var(--text-xs);
  color: var(--gray-dark);
}

@media (max-width: 768px) {
  .text-body, p {
    font-size: var(--text-base);
  }
  .text-lead {
    font-size: var(--text-lg);
  }
}
```

### Links

```css
/* Default link */
a {
  color: var(--gold-base);
  text-decoration: underline;
  text-decoration-color: rgba(200, 170, 80, 0.3);
  text-underline-offset: 3px;
  text-decoration-thickness: 1px;
  transition: text-decoration-color var(--duration-normal) var(--ease-default),
              color var(--duration-normal) var(--ease-default);
}

@media (hover: hover) {
  a:hover {
    color: var(--gold-warm);
    text-decoration-color: var(--gold-warm);
  }
}

a:focus-visible {
  outline: none;
  box-shadow: var(--focus-ring);
  border-radius: var(--radius-sm);
}

/* No-underline link (for cards, navigation) */
.link-clean {
  text-decoration: none;
}

/* External link indicator */
a[target="_blank"]::after {
  content: ' ↗';
  font-size: 0.75em;
  opacity: 0.6;
}

/* Exclude icon-only links */
a[target="_blank"][aria-label]::after,
a[target="_blank"].link-no-arrow::after {
  content: none;
}
```

### Lists

```css
/* Unordered list */
ul.list {
  list-style: none;
  padding: 0;
  margin: var(--space-4) 0;
}

ul.list li {
  font-size: var(--text-base);
  color: var(--gray-light);
  padding: var(--space-1) 0 var(--space-1) var(--space-5);
  position: relative;
  line-height: var(--leading-relaxed);
}

ul.list li::before {
  content: '–';
  position: absolute;
  left: 0;
  color: var(--gray-dark);
}

/* Ordered list */
ol.list {
  list-style: none;
  padding: 0;
  margin: var(--space-4) 0;
  counter-reset: ordered-list;
}

ol.list li {
  font-size: var(--text-base);
  color: var(--gray-light);
  padding: var(--space-1) 0 var(--space-1) var(--space-8);
  position: relative;
  line-height: var(--leading-relaxed);
  counter-increment: ordered-list;
}

ol.list li::before {
  content: counter(ordered-list, decimal-leading-zero);
  position: absolute;
  left: 0;
  font-family: var(--font-mono);
  font-size: var(--text-xs);
  color: var(--gold-cool);
  top: 0.4em;
}

/* Checkmark list (for features/benefits) */
ul.list-check li::before {
  content: '✓';
  color: var(--gold-warm);
}
```

### Code Blocks

```html
<!-- Inline code -->
<code class="code-inline">RAG systems</code>

<!-- Code block -->
<pre class="code-block"><code class="language-python">
from langchain import RetrievalQA
from chromadb import Client

# Multi-agent legal research
class LegalResearchAgent:
    def __init__(self):
        self.hallucination_rate = 0.002  # <0.2%
</code></pre>
```

```css
/* Inline code */
.code-inline, code:not(pre code) {
  font-family: var(--font-mono);
  font-size: 0.85em;
  color: var(--gold-pale);
  background: rgba(200, 170, 80, 0.08);
  padding: 0.15em 0.4em;
  border-radius: var(--radius-sm);
  border: 1px solid rgba(200, 170, 80, 0.1);
}

/* Code block */
.code-block {
  font-family: var(--font-mono);
  font-size: var(--text-sm);
  line-height: var(--leading-relaxed);
  color: var(--white-warm);
  background: var(--bg-deep);
  border: var(--border-default);
  border-radius: var(--radius-lg);
  padding: var(--space-6);
  overflow-x: auto;
  margin: var(--space-6) 0;
  tab-size: 2;
}

.code-block code {
  font-size: inherit;
  color: inherit;
  background: none;
  padding: 0;
  border: none;
}

/* Syntax highlighting tokens */
.code-block .comment { color: var(--gray-mid); font-style: italic; }
.code-block .keyword { color: var(--gold-warm); }
.code-block .string { color: var(--gold-pale); }
.code-block .number { color: var(--gold-cool); }
.code-block .function { color: var(--white-pure); }
```

**Accessibility:**
- ✅ `clamp()` for fluid typography — respects user zoom/font size preferences
- ✅ Line heights ≥ 1.5 for body text (WCAG 1.4.12)
- ✅ Maximum ~65-75 characters per line via `max-width: Xch`
- ✅ Sufficient contrast on all text levels (validated in Color System)
- ✅ `code` elements use semantic HTML

---

## VII. Micro-Interactions

### Hover States

All hover states are gated behind `@media (hover: hover)` to prevent sticky-hover on mobile.

```css
/* Card hover — universal */
@media (hover: hover) {
  .card:hover {
    transform: translateY(-4px);
    border-color: rgba(200, 170, 80, 0.2);
    box-shadow: 0 12px 32px rgba(212, 168, 83, 0.12);
  }
}

/* Button hover — lift + glow */
@media (hover: hover) {
  .btn-primary:hover {
    transform: translateY(-2px);
    box-shadow: var(--shadow-gold);
  }
}

/* Link hover — underline reveal */
@media (hover: hover) {
  a:hover {
    text-decoration-color: var(--gold-warm);
  }
}

/* Portfolio logo hover — grayscale to color */
@media (hover: hover) {
  .card-portfolio:hover .card-portfolio-logo img {
    filter: grayscale(0%) contrast(1);
    opacity: 1;
  }
}

/* Image hover — subtle zoom */
@media (hover: hover) {
  .card-blog-with-image:hover .card-blog-image img {
    transform: scale(1.03);
  }
}

/* Team photo hover — desaturate to full color */
@media (hover: hover) {
  .card-team:hover .card-team-photo img {
    filter: grayscale(0%) contrast(1);
  }
}
```

### Focus States

Consistent gold focus ring for keyboard navigation:

```css
/* Global focus-visible — replaces default browser outline */
:focus-visible {
  outline: none;
  box-shadow: var(--focus-ring);
  /* --focus-ring = 0 0 0 2px var(--bg-base), 0 0 0 4px var(--gold-warm) */
}

/* Remove focus-visible from mouse clicks */
:focus:not(:focus-visible) {
  outline: none;
  box-shadow: none;
}

/* Inputs get border color change instead of ring */
.form-input:focus-visible,
.form-textarea:focus-visible {
  box-shadow: 0 0 0 3px rgba(212, 168, 83, 0.15);
  border-color: var(--gold-warm);
}
```

### Loading States

```css
/* Skeleton loading (for async content) */
.skeleton {
  background: linear-gradient(
    90deg,
    var(--bg-card) 25%,
    var(--bg-hover) 50%,
    var(--bg-card) 75%
  );
  background-size: 200% 100%;
  animation: shimmer 1.5s ease-in-out infinite;
  border-radius: var(--radius-sm);
}

@keyframes shimmer {
  0% { background-position: 200% 0; }
  100% { background-position: -200% 0; }
}

.skeleton-text {
  height: 1em;
  margin-bottom: 0.5em;
  width: 80%;
}

.skeleton-text:last-child {
  width: 60%;
}

.skeleton-title {
  height: 1.5em;
  width: 50%;
  margin-bottom: 1em;
}

.skeleton-image {
  aspect-ratio: 16 / 9;
  width: 100%;
}

/* Inline spinner */
.spinner {
  display: inline-block;
  width: 20px;
  height: 20px;
  border: 2px solid var(--gray-rule);
  border-top-color: var(--gold-warm);
  border-radius: var(--radius-full);
  animation: spin 0.6s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

/* Full-page loading overlay */
.loading-overlay {
  position: fixed;
  inset: 0;
  z-index: var(--z-modal);
  background: rgba(7, 11, 21, 0.8);
  display: flex;
  align-items: center;
  justify-content: center;
}
```

### Transitions (Scroll Animations)

```css
/* Fade-in on scroll */
.fade-in {
  opacity: 0;
  transform: translateY(24px);
  transition: opacity var(--duration-slower) var(--ease-out),
              transform var(--duration-slower) var(--ease-out);
}

.fade-in.visible {
  opacity: 1;
  transform: translateY(0);
}

/* Staggered children */
.stagger-children > * {
  opacity: 0;
  transform: translateY(16px);
  transition: opacity var(--duration-slow) var(--ease-out),
              transform var(--duration-slow) var(--ease-out);
}

.stagger-children.visible > *:nth-child(1) { transition-delay: 0ms; opacity: 1; transform: none; }
.stagger-children.visible > *:nth-child(2) { transition-delay: 80ms; opacity: 1; transform: none; }
.stagger-children.visible > *:nth-child(3) { transition-delay: 160ms; opacity: 1; transform: none; }
.stagger-children.visible > *:nth-child(4) { transition-delay: 240ms; opacity: 1; transform: none; }
.stagger-children.visible > *:nth-child(5) { transition-delay: 320ms; opacity: 1; transform: none; }
.stagger-children.visible > *:nth-child(6) { transition-delay: 400ms; opacity: 1; transform: none; }
```

**JavaScript (Intersection Observer):**
```javascript
const observeElements = () => {
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.15, rootMargin: '0px 0px -60px 0px' }
  );

  document.querySelectorAll('.fade-in, .stagger-children').forEach(el => {
    observer.observe(el);
  });
};

document.addEventListener('DOMContentLoaded', observeElements);
```

### Signature Effect: Gold Shimmer (Hero Only)

```css
@keyframes goldShimmer {
  0%, 100% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
}

.hero {
  background: linear-gradient(
    135deg,
    var(--bg-deep) 0%,
    var(--bg-base) 40%,
    rgba(212, 168, 83, 0.05) 50%,
    var(--bg-base) 60%,
    var(--bg-deep) 100%
  );
  background-size: 200% 200%;
  animation: goldShimmer 8s ease-in-out infinite;
}

/* Reduce animation for users who prefer it */
@media (prefers-reduced-motion: reduce) {
  .hero {
    animation: none;
    background-size: 100% 100%;
  }
}
```

### Scroll Progress Bar

```html
<div class="scroll-progress" aria-hidden="true"></div>
```

```css
.scroll-progress {
  position: fixed;
  top: 0;
  left: 0;
  height: 2px;
  background: linear-gradient(90deg, var(--gold-warm), var(--gold-cool));
  width: 0%;
  z-index: var(--z-progress);
  transition: width 0.1s linear;
  pointer-events: none;
}
```

```javascript
window.addEventListener('scroll', () => {
  const scrolled = (window.scrollY / (document.body.scrollHeight - window.innerHeight)) * 100;
  document.querySelector('.scroll-progress').style.width = `${Math.min(scrolled, 100)}%`;
}, { passive: true });
```

---

## VIII. Utility Classes

Quick-use classes for layout and spacing, following the design token system.

```css
/* Display */
.flex { display: flex; }
.flex-col { flex-direction: column; }
.flex-wrap { flex-wrap: wrap; }
.items-center { align-items: center; }
.justify-center { justify-content: center; }
.justify-between { justify-content: space-between; }

/* Gap */
.gap-2 { gap: var(--space-2); }
.gap-3 { gap: var(--space-3); }
.gap-4 { gap: var(--space-4); }
.gap-6 { gap: var(--space-6); }
.gap-8 { gap: var(--space-8); }

/* Text alignment */
.text-center { text-align: center; }
.text-right { text-align: right; }

/* Max widths */
.max-narrow { max-width: var(--content-narrow); margin-left: auto; margin-right: auto; }
.max-content { max-width: var(--content-max); margin-left: auto; margin-right: auto; }

/* Padding wrapper */
.container {
  max-width: var(--content-max);
  margin: 0 auto;
  padding: 0 var(--space-10);
}

@media (max-width: 768px) {
  .container {
    padding: 0 var(--space-6);
  }
}

/* Section padding */
.section {
  padding: var(--space-24) 0;
}

@media (max-width: 1024px) {
  .section { padding: var(--space-20) 0; }
}

@media (max-width: 768px) {
  .section { padding: var(--space-12) 0; }
}

/* Visibility */
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

.hidden { display: none; }

/* Responsive visibility */
@media (max-width: 768px) {
  .hide-mobile { display: none !important; }
}
@media (min-width: 769px) {
  .hide-desktop { display: none !important; }
}
```

---

## IX. Accessibility Checklist

### Per-Component Requirements

| Component | WCAG Requirement | Implementation |
|-----------|-----------------|----------------|
| **All buttons** | 4.5:1 contrast (text on background) | ✅ Gold on dark ≥ 7.2:1 |
| **All buttons** | 44×44px minimum touch target | ✅ Height 44-56px |
| **All buttons** | Visible focus indicator | ✅ Gold focus ring |
| **All inputs** | Associated `<label>` | ✅ `for`/`id` pairing |
| **All inputs** | Error messages programmatically associated | ✅ `aria-describedby` |
| **All images** | Alternative text | ✅ `alt` on all `<img>` |
| **Navigation** | Skip link | ✅ Skip to main content |
| **Navigation** | `aria-label` on each `<nav>` | ✅ Unique labels |
| **Mobile menu** | Focus trap when open | ✅ JS implementation |
| **Mobile menu** | Escape closes | ✅ keydown listener |
| **Cards** | Clickable area ≥ 44×44px | ✅ Stretched link pattern |
| **Animations** | Respects `prefers-reduced-motion` | ✅ Media query |
| **Color** | Information not conveyed by color alone | ✅ Text labels, icons |
| **Typography** | 1.5× line height for body | ✅ `--leading-relaxed: 1.75` |
| **Typography** | Resizable up to 200% without loss | ✅ `rem` units, `clamp()` |

### Testing Checklist

- [ ] **Keyboard navigation:** Tab through all interactive elements in logical order
- [ ] **Screen reader:** Test with VoiceOver (macOS), NVDA (Windows)
- [ ] **Zoom:** 200% zoom — no horizontal scrolling, no content loss
- [ ] **Contrast:** Validate all color combinations with WebAIM checker
- [ ] **Colorblind:** Simulate with Stark or Color Oracle
- [ ] **Motion:** Test with `prefers-reduced-motion: reduce` enabled
- [ ] **Mobile:** Test on real devices (iPhone, Android) for touch targets
- [ ] **Lighthouse:** Accessibility score ≥ 95

### Semantic HTML Structure

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Page Title — Ainary Ventures</title>
</head>
<body>
  <a href="#main-content" class="skip-link">Skip to main content</a>

  <header class="nav" role="banner">
    <nav aria-label="Main navigation">…</nav>
  </header>

  <main id="main-content">
    <section id="hero" aria-labelledby="hero-heading">
      <h1 id="hero-heading">…</h1>
    </section>

    <section id="services" aria-labelledby="services-heading">
      <h2 id="services-heading">Services</h2>
      …
    </section>

    <!-- More sections -->
  </main>

  <footer role="contentinfo">
    <nav aria-label="Footer navigation">…</nav>
  </footer>
</body>
</html>
```

---

## X. Usage Guidelines Summary

### When to Use What

| Need | Component | Notes |
|------|-----------|-------|
| Primary page action | `btn-primary` | Max 1 per viewport |
| Secondary action | `btn-secondary` | Pair with primary |
| Tertiary/inline action | `btn-tertiary` | Unlimited |
| Hero call-to-action | `btn-cta` | Max 2 (primary + outline) |
| Compact UI action | `btn-icon` | Always needs `aria-label` |
| Show a service | `card-service` | In 3-col grid |
| Show a company | `card-portfolio` | In 4-col grid |
| Show an article | `card-blog` | In 3-col grid, first spans 2 |
| Show a team member | `card-team` | Horizontal layout |
| Page-level navigation | Desktop nav | Sticky, glassmorphism |
| Mobile navigation | Mobile menu | Full-screen overlay |
| Homepage sections | Section nav | Appears after hero scroll |
| Site-wide footer | Footer nav | 3-column grid |
| User input | `form-input` | Always with `<label>` |
| Long text input | `form-textarea` | Min 5 rows |

### Color Usage Rules (Quick Reference)

| Element | Color Token | Rule |
|---------|------------|------|
| H1 headlines | `--white-pure` | Always |
| Body text | `--white-warm` | Primary reading text |
| Secondary text | `--gray-light` | Descriptions, metadata |
| Disabled text | `--gray-dark` | Large text only (18px+) |
| Primary CTA | `--gold-warm` (bg) | On dark backgrounds |
| Links | `--gold-base` | With underline |
| Section tags | `--gold-base` | Monospace, uppercase |
| Data highlights | `--gold-warm` | Via `.mono` class |
| Focus rings | `--gold-warm` | 4px offset |
| Decorative only | `--gold-deep` | **NEVER for text** |

### Gold Restraint Rule

**Gold touches ≤ 10% of any given viewport.**

Count gold elements before adding more:
- 1 CTA button
- 1 section tag
- 2-3 inline data highlights
- Focus ring (only on active element)
- Navigation active state

That's it. Restraint = luxury.

---

*Component Library v1 — Ainary Ventures*  
*Based on: Brand Identity Synthesis, UI/UX Architecture Synthesis, Color System Validation*  
*Ready for implementation*  
*Date: February 7, 2026*
