# Ainary Ventures Website v3 — Design Specification
**Goal:** Transform from "6% of 100%" to state-of-the-art 2026 web design  
**Date:** February 7, 2026  
**Status:** Design Blueprint — Ready for Implementation

---

## Executive Summary

This specification outlines a complete redesign of the Ainary Ventures website, moving from a functional but conservative design to a cutting-edge 2026 web experience that positions Florian as a thought leader at the intersection of AI, manufacturing, and venture capital.

**Core Design Philosophy:**
- **Proprietary, not template:** Custom animations and interactions that feel uniquely "Ainary"
- **Bold color explosion:** Expand from single gold accent to full gold spectrum + complementary colors
- **Guided experience:** Intentional scroll behaviors and wayfinding that tell a story
- **Art meets tech:** Blend craft aesthetics with advanced UI patterns
- **Performance obsessed:** Single HTML file, zero external dependencies, mobile-first

**Target Audience:**
- VCs and fund managers (sophisticated, design-literate)
- Startup founders (looking for strategic guidance)
- German Mittelstand (SME owners, practical but ambitious)

---

## 1. Visual System

### 1.1 Color Palette — The Gold Spectrum Revolution

**Current Problem:** Single gold (#c8aa50) feels flat and predictable.

**Solution:** A living gold spectrum that creates depth, hierarchy, and emotion.

#### Primary Gold Spectrum
```
--gold-warm:     #d4a853   /* Sunset gold — hero, primary CTAs */
--gold-base:     #c8aa50   /* Classic gold — links, accents */
--gold-cool:     #b09a45   /* Bronze gold — secondary elements */
--gold-pale:     #e8d89f   /* Champagne — subtle highlights */
--gold-deep:     #9d7f3b   /* Antique gold — depth, shadows */
```

**Usage Strategy:**
- **Hero section:** Animate between warm → base → cool golds on scroll
- **Service cards:** Each service gets a position on the spectrum (warm = high-touch consulting, cool = self-serve tools)
- **Content clusters:** Icons use different golds to signal category
- **Hover states:** Shift 1-2 steps warmer on interaction

#### Complementary Colors (Strategic Accents)
```
--electric-blue: #4a9eff   /* AI/Tech signals — sparingly */
--deep-purple:   #8b7fc7   /* Venture/Strategy — quotes, emphasis */
--rust-orange:   #d9734a   /* Manufacturing/Industrial — factory icon */
--sage-green:    #7da88f   /* Legal/Compliance — trust signal */
```

**Rules:**
- Never use more than 2 complementary colors per section
- Always anchor with gold spectrum
- Complementary colors at 20-30% opacity for backgrounds/glows

#### Background & Neutrals
```
--bg-deep:       #070b15   /* Deeper than current, more space */
--bg-base:       #0a0f1e   /* Current background */
--bg-card:       #0f1420   /* Card backgrounds, slight lift */
--bg-hover:      #14192a   /* Interactive states */

--white-pure:    #ffffff   /* Headers, key text */
--white-warm:    #e8e6df   /* Current white, body text */
--gray-light:    #a8a8b2   /* De-emphasized text */
--gray-mid:      #8a8a94   /* Current gray */
--gray-dark:     #5c5c66   /* Subtle text */
--gray-rule:     #1f2530   /* Dividers, borders */
```

#### Gradients (Signature Effects)
```css
/* Gold shimmer — hero background */
background: linear-gradient(
  135deg,
  var(--bg-deep) 0%,
  var(--bg-base) 50%,
  rgba(212,168,83,0.03) 100%
);

/* CTA glow */
background: linear-gradient(
  90deg,
  var(--gold-warm),
  var(--gold-base),
  var(--gold-warm)
);
background-size: 200% auto;
animation: shimmer 3s ease-in-out infinite;

/* Section transitions */
background: radial-gradient(
  ellipse at top,
  rgba(74,158,255,0.08) 0%,
  transparent 60%
);
```

---

### 1.2 Typography — Hierarchy That Breathes

**Current Stack:**
- Cormorant Garamond (serif, elegant)
- DM Sans (sans-serif, clean)
- JetBrains Mono (monospace, technical)

**Enhancement Strategy:** Keep fonts, refine usage + add dynamic behaviors.

#### Scale & Hierarchy
```css
/* Display — Hero only */
--text-display: clamp(2.5rem, 6vw, 4rem);
--weight-display: 300;
--line-display: 1.1;

/* H1 — Section headers */
--text-h1: clamp(2rem, 4.8vw, 3rem);
--weight-h1: 300;
--line-h1: 1.2;

/* H2 — Subsections */
--text-h2: clamp(1.4rem, 3vw, 1.9rem);
--weight-h2: 300;
--line-h2: 1.25;

/* H3 — Card titles */
--text-h3: clamp(1.2rem, 2.5vw, 1.5rem);
--weight-h3: 400;
--line-h3: 1.3;

/* Body Large */
--text-body-lg: 1.05rem;
--line-body-lg: 1.7;

/* Body */
--text-body: 0.95rem;
--line-body: 1.75;

/* Body Small */
--text-body-sm: 0.88rem;
--line-body-sm: 1.65;

/* Caption */
--text-caption: 0.78rem;
--line-caption: 1.5;

/* Micro */
--text-micro: 0.68rem;
--line-micro: 1.4;
```

#### Dynamic Typography Behaviors

**1. Kinetic Headers (Hero)**
```css
/* Animate letter-spacing on scroll */
h1.hero-title {
  letter-spacing: 0.02em;
  transition: letter-spacing 0.8s cubic-bezier(0.4, 0, 0.2, 1);
}

h1.hero-title.scrolled {
  letter-spacing: -0.02em; /* Tighten as you scroll */
}
```

**2. Emphasis Animation**
```css
/* Animated underline for key phrases */
.emphasis {
  background: linear-gradient(
    to right,
    var(--gold-warm) 0%,
    var(--gold-cool) 100%
  );
  background-size: 0% 2px;
  background-position: 0 100%;
  background-repeat: no-repeat;
  transition: background-size 0.6s ease-out;
}

.emphasis.in-view {
  background-size: 100% 2px;
}
```

**3. Variable Font Weight on Scroll**
Use CSS custom properties to shift weight dynamically:
```css
h2 {
  font-variation-settings: 'wght' var(--dynamic-weight);
  --dynamic-weight: 300;
}

/* Heavier as element enters viewport */
h2.in-view {
  --dynamic-weight: 400;
  transition: font-variation-settings 0.8s ease;
}
```

---

### 1.3 Spacing System — Rhythm & Breath

**Problem:** Current spacing is functional but lacks rhythm.

**Solution:** 8px base grid with breathing modifiers.

#### Core Scale
```css
--space-1:  0.5rem;   /* 8px */
--space-2:  1rem;     /* 16px */
--space-3:  1.5rem;   /* 24px */
--space-4:  2rem;     /* 32px */
--space-5:  2.5rem;   /* 40px */
--space-6:  3rem;     /* 48px */
--space-8:  4rem;     /* 64px */
--space-10: 5rem;     /* 80px */
--space-12: 6rem;     /* 96px */
--space-16: 8rem;     /* 128px */
--space-20: 10rem;    /* 160px */
```

#### Vertical Rhythm Rules
- **Section padding:** `--space-12` (96px) desktop, `--space-8` (64px) mobile
- **Card internal padding:** `--space-5` (40px) desktop, `--space-4` (32px) mobile
- **Element margin-bottom:** Match line-height (e.g., body text at 1.75 = ~28px ≈ `--space-3`)
- **Breathing space:** Add extra `--space-2` between conceptually distinct groups

#### Horizontal Rhythm
- **Content max-width:** 720px (current, keep)
- **Wide content:** 960px (for dual-column layouts)
- **Narrow content:** 560px (for quotes, emphasis)
- **Container padding:** `--space-4` (32px) mobile, `--space-6` (48px) desktop

---

### 1.4 Animation Principles — Proprietary Motion Language

**Goal:** Animations that feel uniquely "Ainary" — precise, confident, human.

#### Core Easing Curves
```css
/* Ainary Standard — confident, not aggressive */
--ease-ainary: cubic-bezier(0.4, 0, 0.2, 1);

/* Ainary Enter — elements arriving */
--ease-enter: cubic-bezier(0, 0, 0.2, 1);

/* Ainary Exit — elements leaving */
--ease-exit: cubic-bezier(0.4, 0, 1, 1);

/* Ainary Bounce — playful micro-interactions */
--ease-bounce: cubic-bezier(0.68, -0.55, 0.265, 1.55);
```

#### Animation Durations
```css
--duration-instant: 100ms;   /* Micro-feedback (hover color change) */
--duration-fast:    200ms;   /* Button states, small movements */
--duration-base:    400ms;   /* Standard transitions */
--duration-slow:    600ms;   /* Section reveals, large elements */
--duration-epic:    1200ms;  /* Hero entrances, major state changes */
```

#### Signature Animations

**1. Magnetic Cursor**
Large interactive elements (CTA buttons, service cards) subtly pull toward cursor.

**2. Parallax Scroll Layers**
Background elements move at 0.5x speed, creating depth without distraction.

**3. Text Reveal — "Typewriter Shimmer"**
Key phrases reveal with a gold shimmer that flows left→right.

```css
@keyframes shimmer {
  0% { background-position: -200% center; }
  100% { background-position: 200% center; }
}

.shimmer-text {
  background: linear-gradient(
    90deg,
    var(--white-warm) 0%,
    var(--gold-warm) 50%,
    var(--white-warm) 100%
  );
  background-size: 200% auto;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: shimmer 2s ease-in-out infinite;
}
```

**4. Scroll Progress Indicator**
Thin gold line at top of viewport (2px height) fills left→right as user scrolls.

**5. Card Lift on Hover**
```css
.card {
  transform: translateY(0);
  transition: transform var(--duration-base) var(--ease-ainary);
}

.card:hover {
  transform: translateY(-4px);
}
```

**6. Button "Glow Pulse"**
Primary CTAs pulse gently with expanding gold glow on idle.

```css
@keyframes glow-pulse {
  0%, 100% { box-shadow: 0 0 20px rgba(212,168,83,0.3); }
  50% { box-shadow: 0 0 40px rgba(212,168,83,0.6); }
}

.btn-primary {
  animation: glow-pulse 3s ease-in-out infinite;
}
```

---

## 2. Component Patterns

### 2.1 Hero Section — "The Opening Statement"

**Current:** Static headline + subtitle + email.

**V3 Vision:** Dynamic, cinematic, impossible to ignore.

#### Structure
```
┌─────────────────────────────────────────┐
│  [Animated Background Pattern]          │
│                                          │
│  [Scroll Progress Bar — 2px gold line]  │
│                                          │
│        AINARY VENTURES                   │  ← Logo fades in
│                                          │
│     I build AI that replaces             │  ← Display size
│       *workflows*, not tasks.            │  ← "workflows" animates
│                                          │
│   [Rotating Role Labels with Icons]     │  ← Cycles through:
│   🧠 AI Consultant                       │     • AI Consultant
│   🏗️ Builder                             │     • Builder  
│   💼 VC Lab Fellow                       │     • VC Lab Fellow
│                                          │
│   [Short punchy intro — 2 lines max]    │
│                                          │
│   [Primary CTA]  [Secondary CTA]        │  ← Buttons with glow
│                                          │
│          ↓                               │  ← Animated scroll indicator
└─────────────────────────────────────────┘
```

#### Key Behaviors

**Animated Background Pattern:**
Subtle geometric shapes (hexagons, circuit-like lines) in `--gold-deep` at 5% opacity, slowly drifting. Creates "AI network" feeling without cliché.

**Headline Animation:**
- Entire headline fades in with stagger (word by word, 100ms delay)
- Word "workflows" gets shimmer treatment
- Italicized words pulse slightly brighter

**Role Label Rotation:**
3-second intervals, fade out → fade in with icon. Uses complementary colors:
- AI Consultant: `--electric-blue`
- Builder: `--rust-orange`
- VC Lab Fellow: `--deep-purple`

**CTAs:**
```html
<button class="btn-primary">
  See My Work →
</button>
<button class="btn-secondary">
  Read Intelligence Hub
</button>
```

**Scroll Indicator:**
Animated arrow that bounces gently, fades out after 3 seconds or first scroll.

#### Responsive Behavior
- **Desktop:** Full viewport height (100vh), centered content
- **Tablet:** 80vh, slightly smaller text
- **Mobile:** Auto height, stack CTAs vertically

---

### 2.2 Navigation — Sticky & Adaptive

**Current:** Fixed header with logo + links.

**V3 Vision:** Context-aware navigation that adapts to scroll position.

#### States

**State 1: Top of Page (Hero Visible)**
```
┌─────────────────────────────────────────┐
│  AINARY    Services Work Insights About │  ← Full opacity, large
└─────────────────────────────────────────┘
```
- Background: Transparent with blur
- Height: 80px
- Logo: Full "AINARY VENTURES"
- Links: Visible, spaced generously

**State 2: Scrolled (Content Visible)**
```
┌─────────────────────────────────────────┐
│  A  Services Work Insights About  [🔍] │  ← Compact, search icon
└─────────────────────────────────────────┘
```
- Background: `--bg-base` at 95% opacity with heavy blur
- Height: 60px
- Logo: Collapses to "A" monogram
- Links: Slightly smaller, tighter spacing
- Search icon appears (future feature hook)

**State 3: Mobile (Hamburger Menu)**
```
┌─────────────────────────────────────────┐
│  AINARY                             ☰   │
└─────────────────────────────────────────┘
```
- Hamburger menu slides in from right
- Full-screen overlay with large links
- Gold accent for current section

#### Active Section Indicator
- Underline slides beneath current section link (gold shimmer)
- Updates based on scroll position (Intersection Observer)

---

### 2.3 Service Cards — "Memorable Offerings"

**Current:** Simple text list with borders.

**V3 Vision:** Interactive cards with icons, hover effects, and visual hierarchy.

#### Card Structure
```
┌─────────────────────────────────────────┐
│  [Icon]  Service Title                  │  ← Icon uses gold spectrum
│                                          │
│  Short description of the service        │  ← 2-3 lines max
│  and its unique value.                   │
│                                          │
│  Key Metrics:                            │
│  • €61B saved  • 80% faster              │  ← Monospace numbers
│                                          │
│  [Learn More →]                          │  ← Inline link, not button
└─────────────────────────────────────────┘
```

#### Visual Hierarchy
1. **Icon:** 48px, single color from gold spectrum or complementary palette
2. **Title:** H3, `--text-h3`, white
3. **Description:** `--text-body`, gray
4. **Metrics:** `--text-body-sm`, JetBrains Mono, gold
5. **CTA:** `--text-caption`, inline link with arrow

#### Hover Behavior
```css
.service-card {
  background: var(--bg-card);
  border: 1px solid var(--gray-rule);
  transition: all var(--duration-base) var(--ease-ainary);
}

.service-card:hover {
  background: var(--bg-hover);
  border-color: rgba(212,168,83,0.3);
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(212,168,83,0.12);
}

.service-card:hover .icon {
  transform: scale(1.1) rotate(5deg);
}
```

#### Icon Strategy (Emoji + Custom)
- 🏭 Manufacturing (rust-orange glow)
- 📰 Media (electric-blue glow)
- ⚖️ Legal (sage-green glow)
- 📧 Operations (gold-base glow)
- 🎓 Workshops (deep-purple glow)
- 💡 Advisory (gold-warm glow)

Each icon gets a subtle glow (10px blur) in its complementary color.

---

### 2.4 Content Clusters — "Intelligence Hub"

**Current:** Good structure, needs polish + interaction.

**V3 Vision:** Expandable clusters with filter states and visual depth.

#### Cluster Card Enhanced
```
┌─────────────────────────────────────────┐
│  [Icon] Cluster Title          [+]      │  ← Expand/collapse
│                                          │
│  One-line description of cluster theme. │
│                                          │
│  ─────────────────────────────────────  │  ← Subtle divider
│                                          │
│  Article Title                           │
│  Jan 2026 • 5 min read                   │  ← Metadata
│  Preview text for the article...         │
│                                          │
│  ─────────────────────────────────────  │
│                                          │
│  [Another Article]                       │
│                                          │
│  [Show 3 more articles ↓]               │  ← Lazy load
└─────────────────────────────────────────┘
```

#### Interaction Behaviors

**Expand/Collapse:**
- Click anywhere on header to toggle
- Smooth height transition (600ms)
- Icon rotates 180° (+ becomes -)
- Content fades in with stagger (articles appear one by one, 100ms delay)

**Article Hover:**
```css
.cluster-article {
  padding: var(--space-3) 0;
  border-bottom: 1px solid var(--gray-rule);
  transition: padding var(--duration-fast) var(--ease-ainary);
}

.cluster-article:hover {
  padding-left: var(--space-2);
  background: rgba(212,168,83,0.03);
}

.cluster-article:hover .article-title {
  color: var(--gold-warm);
}
```

**Lazy Load ("Show More"):**
- Initially show 3 articles per cluster
- Button reveals 3 more with smooth height expand
- Fades to "All articles shown" after final load

#### Filter Tabs (Above Clusters)
```
[All]  [AI Intelligence]  [Human-AI Systems]  [Manufacturing]  [Legal]  [Venture]
```
- Active tab: gold background, white text
- Inactive: transparent background, gray text
- Click filters clusters (fade out non-matching, 200ms)

---

### 2.5 CTAs — Placement & Micro-Interactions

**Philosophy:** CTAs should feel inevitable, not pushy.

#### CTA Hierarchy

**Primary CTA (High Intent):**
```css
.btn-primary {
  background: linear-gradient(90deg, var(--gold-warm), var(--gold-base));
  background-size: 200% auto;
  color: var(--bg-deep);
  font-family: 'JetBrains Mono', monospace;
  padding: var(--space-3) var(--space-5);
  border: none;
  border-radius: 4px;
  font-size: var(--text-caption);
  letter-spacing: 0.06em;
  font-weight: 500;
  cursor: pointer;
  transition: all var(--duration-base) var(--ease-ainary);
  animation: glow-pulse 3s ease-in-out infinite;
}

.btn-primary:hover {
  background-position: 100% center;
  transform: translateY(-2px);
  box-shadow: 0 12px 32px rgba(212,168,83,0.4);
  animation: none; /* Stop pulse on hover */
}
```

**Secondary CTA (Lower Intent):**
```css
.btn-secondary {
  background: transparent;
  color: var(--gold-base);
  border: 1px solid var(--gold-base);
  padding: var(--space-3) var(--space-5);
  border-radius: 4px;
  font-family: 'JetBrains Mono', monospace;
  font-size: var(--text-caption);
  letter-spacing: 0.06em;
  cursor: pointer;
  transition: all var(--duration-base) var(--ease-ainary);
}

.btn-secondary:hover {
  background: rgba(212,168,83,0.1);
  border-color: var(--gold-warm);
  color: var(--gold-warm);
  transform: translateY(-2px);
}
```

**Inline Link (Contextual):**
```css
a.inline-cta {
  color: var(--gold-base);
  border-bottom: 1px solid rgba(212,168,83,0.3);
  transition: all var(--duration-fast);
}

a.inline-cta::after {
  content: ' →';
  display: inline-block;
  transition: transform var(--duration-fast) var(--ease-ainary);
}

a.inline-cta:hover {
  color: var(--gold-warm);
  border-color: var(--gold-warm);
}

a.inline-cta:hover::after {
  transform: translateX(4px);
}
```

#### CTA Placement Strategy

**Hero Section:**
- Primary: "See My Work"
- Secondary: "Read Intelligence Hub"

**After Services:**
- Primary: "Book a Consultation"
- Secondary: "Download AI Readiness Assessment"

**After Work:**
- Primary: "Explore Case Studies"

**Inside Intelligence Hub:**
- Primary: "Subscribe to the Brief"
- Secondary: "View All Articles"

**Footer:**
- Primary: "Get in Touch"

**Rule:** Never more than 2 CTAs visible at once.

---

## 3. Interaction Design

### 3.1 Scroll Behaviors — Guided Journey

**Philosophy:** The website is a narrative. Scrolling is how you turn the pages.

#### Scroll Progress Bar
```
┌─────────────────────────────────────────┐
│ [████████░░░░░░░░░░░░░░░░░░░░░░░░░░] 30%│  ← 2px gold bar, top of nav
└─────────────────────────────────────────┘
```
- Fixed to top of viewport
- Fills left→right as user scrolls (0% = top, 100% = footer)
- Color gradient: `--gold-warm` → `--gold-cool`
- Subtle glow (4px blur, 30% opacity)

#### Section Reveal Animation
```javascript
// As section enters viewport (Intersection Observer)
section.classList.add('in-view');
```

```css
section {
  opacity: 0;
  transform: translateY(40px);
  transition: opacity var(--duration-slow) var(--ease-enter),
              transform var(--duration-slow) var(--ease-enter);
}

section.in-view {
  opacity: 1;
  transform: translateY(0);
}
```

**Stagger Children:**
For sections with multiple cards/articles, stagger entrance:
```css
section.in-view .card:nth-child(1) { transition-delay: 0ms; }
section.in-view .card:nth-child(2) { transition-delay: 100ms; }
section.in-view .card:nth-child(3) { transition-delay: 200ms; }
/* etc. */
```

#### Parallax Layers
- Background geometric shapes move at 0.5x scroll speed
- Creates depth without distraction
- Limited to hero + about sections (don't overuse)

#### Smooth Scroll Anchors
Clicking nav links smoothly scrolls to section (800ms duration).

```javascript
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function(e) {
    e.preventDefault();
    const target = document.querySelector(this.getAttribute('href'));
    target.scrollIntoView({ behavior: 'smooth', block: 'start' });
  });
});
```

---

### 3.2 Hover States — Tactile Feedback

**Goal:** Every interactive element responds to cursor in a unique way.

#### Card Hover Matrix

| Element | Transform | Shadow | Border | Other |
|---------|-----------|--------|--------|-------|
| Service Card | translateY(-4px) | 0 8px 24px gold 12% | gold 30% | Icon scales + rotates |
| Content Cluster | translateY(-2px) | 0 4px 16px gold 8% | gold 20% | — |
| Article Link | translateX(8px) | None | None | Title color → gold-warm |
| Button Primary | translateY(-2px) | 0 12px 32px gold 40% | None | Stop glow pulse |
| Button Secondary | translateY(-2px) | None | gold-warm | Background tint |

#### Link Underline Animation
```css
a {
  background: linear-gradient(var(--gold-base), var(--gold-base));
  background-size: 0% 1px;
  background-position: 0 100%;
  background-repeat: no-repeat;
  transition: background-size var(--duration-fast) var(--ease-ainary);
}

a:hover {
  background-size: 100% 1px;
}
```

#### Image Hover (About Photo)
```css
.photo img {
  filter: grayscale(30%) contrast(1.05);
  transition: filter var(--duration-slow) var(--ease-ainary);
}

.photo:hover img {
  filter: grayscale(0%) contrast(1.1);
  transform: scale(1.02);
}
```

---

### 3.3 Loading States — First Impression Matters

**Page Load Sequence (First Visit):**

1. **Immediate (0ms):** Background color `--bg-deep` fills screen
2. **100ms:** Logo fades in at center (large, then shrinks to nav position)
3. **400ms:** Hero headline fades in, word by word stagger
4. **800ms:** Role labels + CTAs fade in
5. **1200ms:** Scroll indicator appears
6. **Background:** Geometric pattern animates in over 2000ms

**Return Visit (Cached):**
Skip logo animation, jump straight to hero content (400ms).

```javascript
// Detect if user has visited before
const hasVisited = localStorage.getItem('ainary-visited');

if (!hasVisited) {
  // First visit animation
  document.body.classList.add('first-visit');
  localStorage.setItem('ainary-visited', 'true');
} else {
  // Skip intro
  document.body.classList.add('return-visit');
}
```

---

### 3.4 Transitions Between Sections — Seamless Flow

**Problem:** Current hard dividers (`<hr>`) feel abrupt.

**Solution:** Gradient fade zones.

```css
section {
  position: relative;
  padding: var(--space-12) 0;
}

/* Optional: Add gradient overlay at section boundaries */
section::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 120px;
  background: linear-gradient(
    to bottom,
    transparent 0%,
    var(--bg-deep) 100%
  );
  pointer-events: none;
}
```

**Alternative:** Keep `<hr>` but animate on reveal:
```css
hr {
  border: none;
  height: 1px;
  background: linear-gradient(
    90deg,
    transparent 0%,
    var(--gold-base) 50%,
    transparent 100%
  );
  opacity: 0;
  transform: scaleX(0);
  transition: opacity var(--duration-slow) var(--ease-enter),
              transform var(--duration-slow) var(--ease-enter);
}

hr.in-view {
  opacity: 1;
  transform: scaleX(1);
}
```

---

## 4. Layout & Wireframe

### 4.1 Overall Structure

```
┌───────────────────────────────────────────────────────────┐
│ FIXED NAV: [Logo] [Services] [Work] [Insights] [About]   │ ← Sticky, adaptive
├───────────────────────────────────────────────────────────┤
│ PROGRESS BAR: [████░░░░░░░░░░░░░░░░░░░░░░░░░░░]          │ ← 2px gold line
└───────────────────────────────────────────────────────────┘

┌───────────────────────────────────────────────────────────┐
│                                                             │
│                     HERO SECTION                            │ ← 100vh
│              [Animated background pattern]                  │   Full viewport
│                                                             │   Centered content
│                  Display Headline                           │
│                  Rotating Role Labels                       │
│                  [CTA] [CTA]                                │
│                      ↓                                      │
│                                                             │
└───────────────────────────────────────────────────────────┘

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ← Gradient fade

┌───────────────────────────────────────────────────────────┐
│ SERVICES                                                    │
│ ─────                                                       │ ← Tag (gold monospace)
│                                                             │
│ [Card] [Card] [Card]                                        │ ← 3 columns desktop
│ [Card] [Card] [Card]                                        │   Stack mobile
│                                                             │
│                    [CTA]                                    │ ← Primary: Book consult
└───────────────────────────────────────────────────────────┘

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┌───────────────────────────────────────────────────────────┐
│ WORK                                                        │
│ ────                                                        │
│                                                             │
│ [Project Card]                                              │ ← Single column
│ [Project Card]                                              │   Full width
│ [Project Card]                                              │
│                                                             │
└───────────────────────────────────────────────────────────┘

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┌───────────────────────────────────────────────────────────┐
│ INTELLIGENCE HUB                                            │
│ ────────────────                                           │
│                                                             │
│ [Filter Tabs: All | AI | Systems | Mfg | Legal | VC]       │
│                                                             │
│ ┌─────────────────────────────────────────────────────┐   │
│ │ [Icon] AI Intelligence                          [+] │   │ ← Cluster (expandable)
│ │ ─────────────────────────────────────────────────── │   │
│ │ Article • Article • Article                         │   │
│ └─────────────────────────────────────────────────────┘   │
│                                                             │
│ [4 more clusters...]                                        │
│                                                             │
│         ┌───────────────────────────────┐                  │
│         │  Newsletter CTA (centered)    │                  │ ← Gold gradient bg
│         │  [Subscribe Button]           │                  │
│         └───────────────────────────────┘                  │
│                                                             │
│ LINKS & COMMENTARY                                          │
│ [Link card] [Link card] [Link card]                        │
│                                                             │
│ QUOTES THAT HIT                                             │
│ [Quote block]                                               │
│ [Quote block]                                               │
│                                                             │
└───────────────────────────────────────────────────────────┘

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┌───────────────────────────────────────────────────────────┐
│ ABOUT                                                       │
│ ─────                                                       │
│                                                             │
│ ┌─────────┐ Florian Ziesche                                │ ← Photo + bio
│ │ [Photo] │ Founder, Ainary Ventures                       │   Side by side
│ └─────────┘                                                 │   Desktop
│             Bio text, credentials, links...                 │   Stack mobile
│                                                             │
└───────────────────────────────────────────────────────────┘

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┌───────────────────────────────────────────────────────────┐
│ FOOTER                                                      │
│ ──────                                                      │
│                                                             │
│ © 2026 Ainary Ventures                                      │ ← Centered, minimal
│ [Link] [Link] [Link]                                        │
│                                                             │
└───────────────────────────────────────────────────────────┘
```

---

### 4.2 Responsive Breakpoints

```css
/* Mobile First */
:root {
  --container-padding: var(--space-4); /* 32px */
}

/* Tablet (640px+) */
@media (min-width: 40rem) {
  :root {
    --container-padding: var(--space-5); /* 40px */
  }
  
  /* Services grid: 2 columns */
  .services-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

/* Desktop (960px+) */
@media (min-width: 60rem) {
  :root {
    --container-padding: var(--space-6); /* 48px */
  }
  
  /* Services grid: 3 columns */
  .services-grid {
    grid-template-columns: repeat(3, 1fr);
  }
  
  /* About section: side by side */
  .about-wrap {
    grid-template-columns: 200px 1fr;
  }
}

/* Large Desktop (1280px+) */
@media (min-width: 80rem) {
  /* Wider max-width for content */
  .w {
    max-width: 960px;
  }
}
```

---

### 4.3 Content Hierarchy Map

**Priority 1 (Critical Path — User must see):**
1. Hero headline + role labels
2. Primary CTA
3. Services (first 3 cards visible)
4. About section (photo + bio)

**Priority 2 (High Value):**
5. Work section (project cards)
6. Intelligence Hub (first 2 clusters)
7. Newsletter CTA

**Priority 3 (Nice to Have):**
8. Full Intelligence Hub (all clusters)
9. Links, Quotes, Notes
10. Resources section

**Mobile Strategy:**
- Load Priority 1 immediately
- Lazy load Priority 2 as user scrolls
- Defer Priority 3 until user expands sections

---

## 5. Comparison Analysis: Top-Tier Websites

### 5.1 What They Do Well

| Site | Navigation | Color | Typography | Animation | Layout |
|------|------------|-------|------------|-----------|--------|
| **Anthropic** | Minimal, clean | Muted neutrals, orange accent | Sans-serif, readable | Subtle scroll effects | Spacious, lots of whitespace |
| **Linear** | Sticky, adaptive | Dark base, purple accent | Modern sans, tight hierarchy | Smooth transitions, product demos | Grid-based, product-first |
| **Stripe** | Multi-tier (products + resources) | Blue accent, professional | Clear hierarchy, data-heavy | Minimal, purposeful | Content-dense but organized |
| **Vercel** | Developer-focused | Black + bright accents | Code-friendly, technical | Fast, snappy | Terminal aesthetic, modular |
| **Framer** | Embedded nav in canvas | Playful gradients | Bold display type | Showcases tool capability | Meta (site built in Framer) |

### 5.2 What Ainary Should Adopt

**From Anthropic:**
- Confidence in whitespace
- Single accent color used sparingly (we'll do gold spectrum instead)
- Clear narrative flow

**From Linear:**
- Sticky nav that adapts to scroll
- Purposeful animation (every transition has meaning)
- "Made for [audience]" positioning

**From Stripe:**
- Data-forward (our metrics: €5.5M raised, 80% faster, etc.)
- Multi-tier content (Services → Work → Insights hierarchy)
- Professional but not corporate

**From Vercel:**
- Developer/operator credibility signals
- Fast, snappy interactions
- Code snippets / technical depth where relevant

**From Framer:**
- Showcasing capability through design itself
- Playful without being unprofessional
- Bold typography treatments

### 5.3 What Ainary Should Avoid

**From Anthropic:**
- Too minimal (we need more personality)

**From Linear:**
- Product screenshot overload (we're service-first, not SaaS)

**From Stripe:**
- Corporate blandness (we're a solo operator, not an enterprise)

**From Vercel:**
- Too technical (we serve SMEs, not just devs)

**From Framer:**
- Meta-ness (don't just show off design, show substance)

---

## 6. Implementation Roadmap

### Phase 1: Foundation (Week 1)
- [ ] Set up new color system (CSS variables)
- [ ] Implement typography scale + dynamic behaviors
- [ ] Build spacing system
- [ ] Create animation library (easing curves, keyframes)

### Phase 2: Core Components (Week 2)
- [ ] Hero section with background animation
- [ ] Adaptive navigation
- [ ] Service cards with hover states
- [ ] Content clusters (expandable)

### Phase 3: Interactions (Week 3)
- [ ] Scroll progress bar
- [ ] Section reveal animations
- [ ] Hover states for all interactive elements
- [ ] Loading sequence

### Phase 4: Polish (Week 4)
- [ ] Micro-animations (shimmer text, glow pulse, etc.)
- [ ] Parallax layers
- [ ] Magnetic cursor effects
- [ ] Performance optimization

### Phase 5: Testing & Launch (Week 5)
- [ ] Cross-browser testing (Chrome, Safari, Firefox)
- [ ] Mobile responsiveness
- [ ] Accessibility audit (WCAG AA)
- [ ] Performance audit (Lighthouse score >90)
- [ ] Launch 🚀

---

## 7. Success Metrics

**Quantitative:**
- Time on site: +50% (from ~2min to ~3min)
- Scroll depth: +30% (more users reach About section)
- CTA click-through: +40% (better conversion on "Book consultation")
- Return visits: +25% (memorable = returnable)

**Qualitative:**
- "This doesn't look like a consultant website" (in a good way)
- "I can tell you know what you're doing" (credibility signal)
- "This feels premium" (perceived value)

**Peer Feedback:**
- Designer reaction: "This is 2026-level"
- Developer reaction: "How is this a single HTML file?"
- User reaction: "I want to work with this person"

---

## 8. Design Principles Recap

1. **Proprietary, not template:** Every animation and interaction should feel uniquely Ainary
2. **Gold is the hero:** Spectrum, not single shade
3. **Motion with purpose:** Every animation tells part of the story
4. **Confidence > decoration:** Bold choices, not busy design
5. **Performance is design:** Fast = professional
6. **Mobile is default:** Desktop is the enhancement
7. **Accessibility is non-negotiable:** WCAG AA minimum
8. **Content is king:** Design serves the message, not the other way around

---

## 9. Brand Voice in Design

**How the design communicates Florian's personality:**

- **Precise:** Clean typography, intentional spacing
- **Confident:** Bold color choices, large headlines
- **Technical:** Monospace accents, code-like details
- **Human:** Warmth in gold spectrum, not cold blues
- **Operator:** Action-oriented CTAs, metrics-forward
- **European depth + American scale:** Sophisticated without being flashy

**Design should say:**
"I ship. I don't just theorize. And I do it with craft."

---

## 10. Next Steps

**For Florian:**
1. Review this spec — approve/revise design direction
2. Prioritize: What must launch v3, what's v3.1?
3. Provide high-res logo (if upgrading from text-based "AINARY")
4. Gather any additional content (project case studies, testimonials)

**For Implementation:**
1. Start with Phase 1 (foundation)
2. Build one component at a time, test in isolation
3. Progressive enhancement (site works without JS, enhanced with it)
4. Document custom animations for future maintenance

**Decision Points:**
- Should services be filterable (like content clusters)?
- Do we need a search feature (currently hinted in nav state 2)?
- Should we add a "Dark Factory" AI agent demo (interactive showcase)?

---

## Appendix A: Code Snippets Reference

### A.1 Shimmer Text Effect
```css
.shimmer-text {
  background: linear-gradient(
    90deg,
    var(--white-warm) 0%,
    var(--gold-warm) 50%,
    var(--white-warm) 100%
  );
  background-size: 200% auto;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: shimmer 2s ease-in-out infinite;
}

@keyframes shimmer {
  0% { background-position: -200% center; }
  100% { background-position: 200% center; }
}
```

### A.2 Scroll Progress Bar
```html
<div class="scroll-progress-bar"></div>
```

```css
.scroll-progress-bar {
  position: fixed;
  top: 0;
  left: 0;
  height: 2px;
  background: linear-gradient(
    90deg,
    var(--gold-warm),
    var(--gold-cool)
  );
  width: 0%;
  z-index: 100;
  box-shadow: 0 0 10px rgba(212,168,83,0.6);
  transition: width 0.1s linear;
}
```

```javascript
window.addEventListener('scroll', () => {
  const scrollTop = window.pageYOffset;
  const docHeight = document.documentElement.scrollHeight - window.innerHeight;
  const scrollPercent = (scrollTop / docHeight) * 100;
  document.querySelector('.scroll-progress-bar').style.width = scrollPercent + '%';
});
```

### A.3 Section Reveal with Intersection Observer
```javascript
const observerOptions = {
  threshold: 0.15,
  rootMargin: '0px 0px -10% 0px'
};

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('in-view');
    }
  });
}, observerOptions);

document.querySelectorAll('section, .cluster, .card').forEach(el => {
  observer.observe(el);
});
```

---

## Appendix B: Inspiration Library

**Reference Sites (Beyond Top 5):**
- [Studio Freight](https://www.studiofreight.com/) — Parallax mastery
- [Active Theory](https://activetheory.net/) — WebGL excellence
- [Awwwards Site of the Year Winners](https://www.awwwards.com/websites/sotd/) — Cutting edge
- [Godly](https://godly.website/) — Curated design inspiration

**Motion Design:**
- [Loom](https://www.loom.com/) — Purposeful micro-animations
- [Pitch](https://pitch.com/) — Smooth transitions
- [Raycast](https://www.raycast.com/) — Snappy interactions

**Typography:**
- [Stripe Press](https://press.stripe.com/) — Beautiful book layouts
- [The Margins](https://themargins.substack.com/) — Editorial hierarchy
- [Typewolf](https://www.typewolf.com/) — Font inspiration

---

## Document Control

**Version:** 1.0  
**Date:** February 7, 2026  
**Author:** AI Research Agent (Subagent)  
**Status:** Complete — Ready for Review  
**Next Review:** Upon implementation feedback

**Changelog:**
- v1.0 (Feb 7, 2026): Initial comprehensive specification based on competitive research + 2026 trends

---

**End of Design Specification**

This document is the blueprint. Now it's time to build.
