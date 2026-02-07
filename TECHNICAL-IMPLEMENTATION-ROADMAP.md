# Technical Implementation Roadmap v1
**Planner Agent 4 — Opus**  
**Date:** February 7, 2026  
**Inputs:** Brand Identity Synthesis, UI/UX Synthesis, Content Strategy Synthesis, Design Trends Research, Color Validation, Competitive Analysis, Current Codebase Review

---

## Executive Summary

This document is the build plan for florianziesche.com → Ainary Ventures website. It turns the brand, UX, and content syntheses into a concrete technical blueprint: which tools, which architecture, which order, how long.

**The Decision:** Astro + Tailwind CSS v4 + MDX, deployed on Vercel. Static-first, zero JavaScript by default, progressive enhancement for interactions. Markdown blog with frontmatter CMS. Target: Lighthouse 100/100/100/100.

**Why This Stack:**
- Astro ships zero JS by default → fastest possible site
- Tailwind v4 uses CSS-native layers → zero runtime, ~15KB total CSS
- MDX for blog → Markdown simplicity + component embedding
- Vercel already hosts the site → zero migration friction
- No React runtime on the client → performance ceiling is the network, not the framework

---

## I. Technology Stack Decisions

### Framework: Astro 5.x

**Choice:** Astro (Static Site Generator with Islands Architecture)

**Why Astro over alternatives:**

| Option | Pros | Cons | Verdict |
|--------|------|------|---------|
| **Astro** | Zero JS default, .astro components, MDX native, Vercel deploy, islands for interactivity | Smaller ecosystem than Next.js | ✅ **CHOSEN** |
| **Next.js** | Massive ecosystem, React, app router | Overkill — ships React runtime (~90KB), SSR complexity for a mostly-static site | ❌ Too heavy |
| **Vanilla HTML** | Maximum control, no build step | Unmaintainable at scale (20+ pages), no component reuse, no MDX | ❌ Current approach — doesn't scale |
| **11ty** | Simple, fast builds | Less ergonomic components, weaker TypeScript, smaller community in 2026 | ❌ Outdated DX |
| **Hugo** | Blazing builds | Go templating is painful, no JSX-like components, poor MDX | ❌ Bad DX |

**Astro Key Features Used:**
- **Zero JS by default** — HTML/CSS only unless we opt in
- **Islands Architecture** — Interactive components (mobile nav, tabs) hydrate independently
- **MDX integration** — Blog posts in Markdown with embedded components
- **Content Collections** — Type-safe frontmatter for blog, portfolio, services
- **View Transitions API** — Native page transitions (no SPA needed)
- **Image optimization** — Built-in `<Image>` component with AVIF/WebP
- **Vercel adapter** — First-class deployment support

**When We Need JS (Islands):**
- Mobile hamburger menu toggle
- Homepage section scroll observer (sticky nav highlighting)
- Contact form submission
- Portfolio logo hover (grayscale → color, CSS-only fallback)
- Optional: Gold shimmer (CSS animation, no JS needed)

Everything else: pure HTML + CSS. No framework runtime shipped to the client.

---

### CSS: Tailwind CSS v4

**Choice:** Tailwind CSS v4 (CSS-native, no PostCSS config needed)

**Why Tailwind v4:**
- **CSS-native engine** — Uses `@layer`, `@property`, CSS nesting. No JavaScript at build time.
- **~15KB gzipped** — After purge, total CSS is tiny
- **Design token system** — Maps directly to our brand tokens (gold spectrum, monochrome, spacing)
- **Dark mode native** — `dark:` variant built in (for future light mode toggle)
- **Responsive utilities** — Mobile-first breakpoints match UX synthesis exactly
- **@apply** — Extract component classes without leaving Tailwind
- **No CSS-in-JS runtime** — Zero cost on client

**Why not vanilla CSS:**
- Brand has 30+ design tokens (colors, spacing, typography). Tailwind makes them ergonomic.
- Responsive breakpoints need consistent application across 20+ pages. Utility classes prevent drift.
- Speed of development. Tailwind is 2-3× faster for component styling.

**Why not CSS Modules / styled-components:**
- CSS Modules: Unnecessary with Astro's scoped styles
- styled-components: Ships JS runtime. Absolutely not for a performance-first site.

**Custom Configuration:**

```css
/* tailwind.config.css (v4 native) */
@theme {
  /* Monochrome Foundation */
  --color-bg-deep: #070b15;
  --color-bg-base: #0a0f1e;
  --color-bg-card: #0f1420;
  --color-bg-hover: #14192a;
  
  --color-white-pure: #ffffff;
  --color-white-warm: #e8e6df;
  --color-gray-light: #a8a8b2;
  --color-gray-mid: #8a8a94;
  --color-gray-dark: #5c5c66;
  --color-gray-rule: #1f2530;
  
  /* Gold Spectrum */
  --color-gold-warm: #d4a853;
  --color-gold-base: #c8aa50;
  --color-gold-cool: #b09a45;
  --color-gold-pale: #e8d89f;
  --color-gold-deep: #9d7f3b;
  
  /* Typography */
  --font-display: 'Inter Display Variable', system-ui, sans-serif;
  --font-body: 'Inter Variable', system-ui, sans-serif;
  --font-mono: 'JetBrains Mono Variable', monospace;
  
  /* Spacing (8px base) */
  --spacing-section: 120px;
  --spacing-section-mobile: 60px;
  
  /* Breakpoints */
  --breakpoint-sm: 375px;
  --breakpoint-md: 768px;
  --breakpoint-lg: 1024px;
  --breakpoint-xl: 1440px;
  --breakpoint-2xl: 1920px;
}
```

---

### Build Tool: Vite (via Astro)

Astro uses Vite internally. No separate configuration needed.

**What Vite Handles:**
- CSS processing (Tailwind v4 native)
- Asset bundling and hashing
- Image optimization pipeline
- MDX compilation
- Hot module replacement in dev
- Production minification (HTML, CSS, JS)

**No additional build tools needed.** No Webpack, no Gulp, no Parcel.

---

### Hosting: Vercel (Keep Current)

**Decision:** Stay on Vercel. Zero migration needed.

**Why:**
- Already deployed (`vercel.json` exists in repo)
- Edge network (CDN in 100+ locations)
- Automatic HTTPS
- Preview deployments per branch
- Analytics built-in (free tier)
- Serverless functions (for contact form, if needed)
- Headers/redirects via `vercel.json`

**Vercel Configuration (Updated):**

```json
{
  "version": 2,
  "framework": "astro",
  "buildCommand": "astro build",
  "outputDirectory": "dist",
  "headers": [
    {
      "source": "/(.*)",
      "headers": [
        { "key": "X-Content-Type-Options", "value": "nosniff" },
        { "key": "X-Frame-Options", "value": "SAMEORIGIN" },
        { "key": "X-XSS-Protection", "value": "1; mode=block" },
        { "key": "Referrer-Policy", "value": "strict-origin-when-cross-origin" },
        { "key": "Permissions-Policy", "value": "camera=(), microphone=(), geolocation=()" }
      ]
    },
    {
      "source": "/fonts/(.*)",
      "headers": [
        { "key": "Cache-Control", "value": "public, max-age=31536000, immutable" }
      ]
    },
    {
      "source": "/_astro/(.*)",
      "headers": [
        { "key": "Cache-Control", "value": "public, max-age=31536000, immutable" }
      ]
    }
  ]
}
```

---

### CMS: Content Collections (Markdown/MDX)

**Decision:** Astro Content Collections with MDX files. No external CMS.

**Why not a headless CMS (Contentful, Sanity, Strapi):**
- Florian is technical — Markdown in VS Code / Obsidian is his natural workflow
- No dependency on third-party service
- Version control (Git) = complete history
- Zero API calls at build time = fastest possible builds
- Free forever

**Why MDX over plain Markdown:**
- Embed interactive components (code demos, calculators)
- Custom callout boxes, image galleries, comparison tables
- Import React/Astro components directly in posts

**Content Schema (Type-Safe):**

```typescript
// src/content/config.ts
import { defineCollection, z } from 'astro:content';

const blog = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string(),
    date: z.date(),
    updated: z.date().optional(),
    author: z.enum(['florian', 'mia']),
    category: z.enum([
      'ai-traditional-industries',
      'operator-to-vc',
      'human-ai-collaboration',
      'systems-thinking',
      'contrarian-takes'
    ]),
    tags: z.array(z.string()),
    image: z.string().optional(),
    imageAlt: z.string().optional(),
    draft: z.boolean().default(false),
    featured: z.boolean().default(false),
    readingTime: z.number().optional(), // auto-calculated
  }),
});

const portfolio = defineCollection({
  type: 'content',
  schema: z.object({
    company: z.string(),
    logo: z.string(),
    sector: z.enum(['manufacturing', 'legal', 'media', 'office']),
    status: z.enum(['active', 'exited', 'stealth']),
    description: z.string(),
    metrics: z.array(z.object({
      label: z.string(),
      value: z.string(),
    })).optional(),
    url: z.string().url().optional(),
    order: z.number(),
  }),
});

const services = defineCollection({
  type: 'data',
  schema: z.object({
    title: z.string(),
    slug: z.string(),
    icon: z.string(),
    tagline: z.string(),
    description: z.string(),
    features: z.array(z.string()),
    caseStudy: z.object({
      client: z.string(),
      result: z.string(),
      metric: z.string(),
    }).optional(),
    goldVariant: z.enum(['warm', 'base', 'cool', 'pale', 'deep']),
    order: z.number(),
  }),
});

export const collections = { blog, portfolio, services };
```

---

## II. File Structure

```
florianziesche.com/
├── public/
│   ├── fonts/
│   │   ├── inter-variable.woff2          # Subsetted (~45KB)
│   │   ├── inter-display-variable.woff2  # Subsetted (~45KB)
│   │   └── jetbrains-mono-variable.woff2 # Subsetted (~35KB)
│   ├── images/
│   │   ├── og/                           # Open Graph images (1200×630)
│   │   │   ├── default.jpg
│   │   │   └── blog/                     # Per-post OG images
│   │   ├── portfolio/                    # Company logos (SVG preferred)
│   │   └── favicon/
│   │       ├── favicon.ico
│   │       ├── favicon.svg
│   │       ├── apple-touch-icon.png
│   │       └── manifest.webmanifest
│   ├── robots.txt
│   └── sitemap.xml                       # Auto-generated by Astro
│
├── src/
│   ├── assets/
│   │   └── images/                       # Images processed by Astro (AVIF/WebP)
│   │       ├── hero/
│   │       ├── about/
│   │       └── blog/
│   │
│   ├── components/
│   │   ├── global/
│   │   │   ├── Header.astro              # Sticky nav (72→56px)
│   │   │   ├── Footer.astro              # 3-column footer
│   │   │   ├── SkipToContent.astro       # Accessibility
│   │   │   ├── ScrollProgress.astro      # Gold gradient progress bar
│   │   │   └── SEO.astro                 # Meta tags, OG, JSON-LD
│   │   │
│   │   ├── home/
│   │   │   ├── Hero.astro                # Gold shimmer background
│   │   │   ├── About.astro               # Vision/Mission
│   │   │   ├── Services.astro            # 6-card grid
│   │   │   ├── Portfolio.astro           # Logo showcase
│   │   │   ├── Insights.astro            # Latest 3 articles
│   │   │   └── Contact.astro             # CTA + form
│   │   │
│   │   ├── blog/
│   │   │   ├── PostCard.astro            # Blog list card
│   │   │   ├── PostHeader.astro          # Post title, meta, image
│   │   │   ├── TableOfContents.astro     # Auto-generated TOC
│   │   │   ├── CategoryFilter.astro      # Filter by content pillar
│   │   │   └── ReadingProgress.astro     # Article progress bar
│   │   │
│   │   ├── ui/
│   │   │   ├── Button.astro              # Primary (gold), Secondary (outline)
│   │   │   ├── Card.astro                # Reusable card component
│   │   │   ├── Badge.astro               # Status badges
│   │   │   ├── Callout.astro             # Info/warning/tip boxes (for MDX)
│   │   │   ├── CodeBlock.astro           # Syntax highlighted code
│   │   │   └── Image.astro               # Wrapper around Astro Image
│   │   │
│   │   └── interactive/                  # Client-side islands
│   │       ├── MobileNav.astro           # Hamburger menu (client:visible)
│   │       ├── SectionNav.astro          # Homepage scroll observer
│   │       ├── ContactForm.astro         # Form with validation
│   │       └── ThemeToggle.astro         # Dark/light (future)
│   │
│   ├── content/
│   │   ├── config.ts                     # Content collection schemas
│   │   ├── blog/
│   │   │   ├── ai-agents-overnight.mdx
│   │   │   ├── hallucination-rate.mdx
│   │   │   └── ...
│   │   ├── portfolio/
│   │   │   ├── cnc-planner.md
│   │   │   └── ...
│   │   └── services/
│   │       ├── manufacturing-ai.yaml
│   │       ├── legal-tech.yaml
│   │       ├── media-publishing.yaml
│   │       ├── office-operations.yaml
│   │       ├── workshops.yaml
│   │       └── advisory.yaml
│   │
│   ├── layouts/
│   │   ├── Base.astro                    # HTML shell, fonts, meta
│   │   ├── Page.astro                    # Standard page (nav + footer)
│   │   └── Post.astro                    # Blog post layout (TOC, reading time)
│   │
│   ├── pages/
│   │   ├── index.astro                   # Homepage (single-page scroll)
│   │   ├── consulting/
│   │   │   └── index.astro               # Services with tabs
│   │   ├── fund/
│   │   │   └── index.astro               # VC thesis, team, apply
│   │   ├── portfolio/
│   │   │   ├── index.astro               # Portfolio grid
│   │   │   └── [slug].astro              # Individual case study
│   │   ├── insights/
│   │   │   ├── index.astro               # Blog listing (filterable)
│   │   │   └── [slug].astro              # Individual blog post
│   │   ├── about/
│   │   │   └── index.astro               # Florian, Mia, philosophy
│   │   ├── links/
│   │   │   └── index.astro               # Linktree replacement
│   │   ├── contact.astro                 # Contact page
│   │   ├── 404.astro                     # Custom 404
│   │   └── rss.xml.ts                    # RSS feed
│   │
│   └── styles/
│       ├── global.css                    # Tailwind directives + base styles
│       ├── fonts.css                     # @font-face declarations
│       ├── animations.css                # Gold shimmer, fade-in, etc.
│       └── prose.css                     # Typography for blog content
│
├── astro.config.mjs                      # Astro configuration
├── tailwind.config.ts                    # Tailwind v4 theme
├── tsconfig.json                         # TypeScript config
├── package.json
├── .gitignore
├── vercel.json                           # Deployment config
└── README.md                             # Project documentation
```

### Asset Management Strategy

**Images in `src/assets/`:** Processed by Astro's image pipeline → AVIF/WebP with srcset
**Images in `public/`:** Served as-is (favicons, OG images, fonts)
**Portfolio logos:** SVG in `public/images/portfolio/` (crisp at any size, tiny file)
**Blog images:** In `src/assets/images/blog/` → optimized at build

### CSS Architecture

Three layers, loaded in order:

1. **`fonts.css`** — @font-face declarations (loaded first via `<link rel="preload">`)
2. **`global.css`** — Tailwind base + custom utilities + CSS custom properties
3. **`animations.css`** — Keyframes, transitions (deferred loading for non-critical)

Component-specific styles live in `.astro` files (Astro scopes them automatically).

### JS Organization

**Goal: Ship <5KB of JavaScript total.**

All JS lives in island components (`src/components/interactive/`). Astro only hydrates what's needed:

```astro
<!-- Only loads JS when component enters viewport -->
<MobileNav client:visible />

<!-- Only loads JS on media query match -->
<SectionNav client:media="(min-width: 1024px)" />
```

No global JS bundle. No framework runtime. Each island is independent.

---

## III. Performance Strategy

### Performance Budget

| Metric | Target | Strategy |
|--------|--------|----------|
| **Lighthouse Performance** | 100 | Zero JS by default, optimized images |
| **Lighthouse Accessibility** | 100 | Semantic HTML, ARIA, contrast ratios |
| **Lighthouse Best Practices** | 100 | Security headers, HTTPS, no console errors |
| **Lighthouse SEO** | 100 | Meta tags, JSON-LD, sitemap, robots.txt |
| **First Contentful Paint** | <0.8s | Inline critical CSS, preload fonts |
| **Largest Contentful Paint** | <1.5s | Optimized hero image, no render-blocking JS |
| **Cumulative Layout Shift** | <0.05 | Font-display: swap + size hints, fixed image dimensions |
| **Total Blocking Time** | 0ms | No JS on initial render |
| **Total Page Weight** | <300KB | After compression |

### Image Optimization

**Format Priority:** AVIF → WebP → JPEG (Astro handles automatically)

```astro
---
import { Image } from 'astro:assets';
import heroImage from '../assets/images/hero/main.jpg';
---

<Image
  src={heroImage}
  widths={[400, 800, 1200, 1600]}
  sizes="(max-width: 768px) 100vw, (max-width: 1200px) 80vw, 1200px"
  alt="AI systems architecture visualization"
  loading="eager"        <!-- Hero only; all others use lazy -->
  format="avif"
  quality={80}
/>
```

**Rules:**
- Hero image: `loading="eager"`, preloaded in `<head>`
- All other images: `loading="lazy"` (native lazy loading)
- Blog images: Max 1200px wide, AVIF preferred
- Portfolio logos: SVG (vector, infinitely scalable, <5KB each)
- OG images: Pre-generated JPEGs (1200×630, ~80KB)

### Font Loading Strategy

**Goal:** No FOUT, no FOIT. Fonts visible within 100ms.

```css
/* src/styles/fonts.css */

/* Preload critical font */
/* In Base.astro <head>: */
/* <link rel="preload" href="/fonts/inter-variable.woff2" as="font" type="font/woff2" crossorigin> */

@font-face {
  font-family: 'Inter Variable';
  src: url('/fonts/inter-variable.woff2') format('woff2-variations');
  font-weight: 100 900;
  font-display: swap;
  font-style: normal;
  unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6,
    U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+20AC, U+2122,
    U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
}

@font-face {
  font-family: 'Inter Display Variable';
  src: url('/fonts/inter-display-variable.woff2') format('woff2-variations');
  font-weight: 100 900;
  font-display: swap;
  font-style: normal;
  unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6,
    U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+20AC, U+2122,
    U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
}

@font-face {
  font-family: 'JetBrains Mono Variable';
  src: url('/fonts/jetbrains-mono-variable.woff2') format('woff2-variations');
  font-weight: 100 800;
  font-display: swap;
  font-style: normal;
  unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6;
}
```

**Font Subsetting (Build Step):**

```bash
# Subset Inter to Latin characters only
pyftsubset InterVariable.woff2 \
  --output-file=inter-variable.woff2 \
  --flavor=woff2 \
  --layout-features="kern,liga,calt,ss01,ss02,cv01,cv02" \
  --unicodes="U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD"
```

**Expected sizes after subsetting:**
- Inter Variable: ~45KB
- Inter Display Variable: ~45KB
- JetBrains Mono Variable: ~35KB
- **Total fonts: ~125KB** (preloaded, cached forever)

**CLS Prevention:**

```css
/* Fallback font metrics to match Inter */
body {
  font-family: 'Inter Variable', system-ui, -apple-system, sans-serif;
  font-synthesis: none;
  /* size-adjust in fallback prevents layout shift */
}

@font-face {
  font-family: 'Inter Fallback';
  src: local('system-ui'), local('-apple-system'), local('Segoe UI');
  size-adjust: 107%;
  ascent-override: 90%;
  descent-override: 22%;
  line-gap-override: 0%;
}
```

### CSS/JS Minification

**Handled automatically by Astro/Vite in production:**
- CSS: Minified + purged (unused Tailwind classes removed)
- JS: Tree-shaken + minified + code-split per island
- HTML: Minified (whitespace removed)

**Expected output sizes (gzipped):**
- HTML per page: 5-15KB
- CSS (total, all pages): ~15KB
- JS (total, all islands): <5KB
- Fonts: ~125KB (cached after first load)
- **First visit total: ~160-200KB** (well under 300KB budget)

### Caching Strategy

**Vercel Edge CDN + Cache Headers:**

| Asset Type | Cache Strategy | Max-Age |
|------------|---------------|---------|
| HTML pages | `s-maxage=3600, stale-while-revalidate=86400` | 1 hour + stale 24h |
| CSS/JS (hashed) | `immutable` | 1 year |
| Fonts | `immutable` | 1 year |
| Images (hashed) | `immutable` | 1 year |
| OG images | `public, max-age=86400` | 1 day |
| RSS feed | `s-maxage=3600` | 1 hour |

Astro hashes all built assets (`/_astro/styles.abc123.css`), enabling aggressive caching.

### Reduced Motion Support

```css
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

## IV. Development Phases

### Phase 1: Setup + Foundation (Week 1)
**Goal:** Repo initialized, design system operational, CI/CD working.

**Day 1-2: Project Scaffold**
- [ ] Initialize Astro project: `npm create astro@latest`
- [ ] Install dependencies: `@astrojs/tailwind`, `@astrojs/mdx`, `@astrojs/sitemap`, `@astrojs/vercel`
- [ ] Configure TypeScript (strict mode)
- [ ] Set up Git repo with `.gitignore`
- [ ] Connect to Vercel (auto-deploy on push)
- [ ] Configure `vercel.json` with security headers

**Day 3-4: Design System**
- [ ] Download + subset fonts (Inter, Inter Display, JetBrains Mono)
- [ ] Create `fonts.css` with @font-face declarations
- [ ] Configure Tailwind v4 theme (colors, typography, spacing)
- [ ] Create `global.css` (reset, base styles, custom properties)
- [ ] Create `animations.css` (gold shimmer, fade-in, hover effects)
- [ ] Build `Base.astro` layout (HTML shell, head, font preloading)

**Day 5-7: Core Components**
- [ ] Build `Header.astro` (sticky nav, glassmorphism, adaptive height)
- [ ] Build `MobileNav.astro` (hamburger, full-screen overlay — island)
- [ ] Build `Footer.astro` (3-column, minimal)
- [ ] Build `Button.astro` (primary gold, secondary outline, sizes)
- [ ] Build `Card.astro` (reusable, hover states)
- [ ] Build `SEO.astro` (meta tags, OG, JSON-LD structured data)
- [ ] Build `SkipToContent.astro` (accessibility)
- [ ] Deploy foundation to Vercel (empty site with nav + footer)

**Deliverables:** Working skeleton site on Vercel with design system, navigation, and zero content.

---

### Phase 2: Homepage (Week 2)
**Goal:** Complete homepage — the single-page scroll experience.

**Day 8-9: Hero Section**
- [ ] Build `Hero.astro` (gold shimmer CSS animation)
- [ ] Implement headline typography (Inter Display, 56-68px, negative tracking)
- [ ] Dual CTAs (primary gold, secondary outline)
- [ ] Status badge ("Currently: Building + Investing")
- [ ] Responsive: Hero text scales from 38px (mobile) → 68px (desktop)

**Day 10-11: About + Services**
- [ ] Build `About.astro` (Vision/Mission copy, Florian+Mia positioning)
- [ ] Build `Services.astro` (6-card grid, each with gold variant accent)
- [ ] Implement service card hover (lift + gold glow shadow)
- [ ] Each card links to `/consulting#{slug}` for deep dive
- [ ] Responsive: 1 col (mobile) → 2 col (tablet) → 3 col (desktop)

**Day 12-13: Portfolio + Insights + Contact**
- [ ] Build `Portfolio.astro` (logo grid, grayscale → color on hover)
- [ ] Build `Insights.astro` (latest 3 blog cards + "View All" CTA)
- [ ] Build `Contact.astro` (CTA block + contact form or Calendly embed)
- [ ] Build `ContactForm.astro` island (client-side validation + submit)

**Day 14: Homepage Polish**
- [ ] Build `SectionNav.astro` island (scroll observer, sticky below main nav)
- [ ] Build `ScrollProgress.astro` (gold gradient progress bar, top of page)
- [ ] Implement `fade-in` on scroll (Intersection Observer, all sections)
- [ ] Test responsive across breakpoints (375, 768, 1024, 1440, 1920)
- [ ] Deploy v1 homepage to Vercel

**Deliverables:** Complete homepage with all 6 sections, responsive, interactions working.

---

### Phase 3: Detail Pages (Week 3)
**Goal:** All navigation targets have real pages.

**Day 15-16: Consulting Page**
- [ ] Build `/consulting/index.astro` with tabbed service categories
- [ ] Load services from Content Collections (YAML data)
- [ ] Each tab: description, features, case study, CTA
- [ ] Tab interaction (CSS-only with `:target` selector, JS enhancement optional)
- [ ] Responsive: Tabs → accordion on mobile

**Day 17-18: Fund + Portfolio Pages**
- [ ] Build `/fund/index.astro` (thesis, team, portfolio preview, founder apply CTA)
- [ ] Build `/portfolio/index.astro` (filterable grid by sector)
- [ ] Build `/portfolio/[slug].astro` (case study template — metrics, narrative, results)
- [ ] Load portfolio from Content Collections

**Day 19-20: Blog Infrastructure**
- [ ] Configure MDX integration
- [ ] Build `/insights/index.astro` (blog listing with category filter)
- [ ] Build `/insights/[slug].astro` (blog post layout)
- [ ] Build `PostCard.astro` (card for listing page)
- [ ] Build `PostHeader.astro` (title, date, reading time, category)
- [ ] Build `TableOfContents.astro` (auto-generated from headings)
- [ ] Build `ReadingProgress.astro` (gold progress bar for articles)
- [ ] Create `prose.css` (typography for long-form content — headings, lists, code, blockquotes)

**Day 21: Supporting Pages**
- [ ] Build `/about/index.astro` (Florian bio, Mia story, Kintsugi philosophy, How We Work)
- [ ] Build `/links/index.astro` (Linktree replacement — migrated from current links.html)
- [ ] Build `/contact.astro` (full contact page)
- [ ] Build `404.astro` (custom error page with gold accent)
- [ ] Build `rss.xml.ts` (RSS feed generation)
- [ ] Deploy all detail pages to Vercel

**Deliverables:** All 8+ pages live, blog infrastructure ready for content.

---

### Phase 4: Content Integration (Week 4)
**Goal:** Real content populates the site. SEO configured. Blog live.

**Day 22-23: Core Content**
- [ ] Write/finalize homepage copy (integrate brand messaging framework)
- [ ] Write consulting page copy (6 service descriptions, proof points)
- [ ] Write fund page copy (thesis, team bios)
- [ ] Write about page copy (Florian narrative, Mia story, philosophy)
- [ ] Populate portfolio Content Collection (3-5 entries minimum)
- [ ] Populate services Content Collection (6 services with YAML data)

**Day 24-25: Blog Content**
- [ ] Publish 3-5 launch blog posts (from content strategy pillars):
  - "AI Systems That Go Into Production, Not PowerPoints" (manifesto)
  - "How I Reduced Hallucinations to <0.2%: A Technical Deep Dive"
  - "Why Manufacturing AI Is a $2.3T Opportunity Silicon Valley Ignores"
  - "What Working With an AI Agent (Mia) Taught Me About Compound Intelligence"
  - "The Operator's Guide to VC: What I Wish I Knew" (if ready)
- [ ] Create OG images for each post (1200×630, branded template)
- [ ] Test MDX rendering (code blocks, callouts, images)

**Day 26-27: SEO + Metadata**
- [ ] Implement JSON-LD structured data (Person, Organization, BlogPosting)
- [ ] Configure per-page meta descriptions
- [ ] Generate sitemap.xml (Astro plugin)
- [ ] Create robots.txt
- [ ] Set up canonical URLs
- [ ] Verify Open Graph tags render correctly (Facebook debugger, Twitter card validator)
- [ ] Submit sitemap to Google Search Console

**Day 28: Lead Generation Setup**
- [ ] Contact form integration (Vercel serverless function → email notification)
- [ ] Newsletter signup CTA (Substack embed or redirect)
- [ ] Lead magnet placeholder ("AI Implementation Playbook" — coming soon)
- [ ] Calendly integration (book a call links)

**Deliverables:** Content-complete site with blog, SEO, and lead capture.

---

### Phase 5: Testing + Launch (Week 5)
**Goal:** Ship. Production-ready, thoroughly tested, zero-downtime launch.

**Day 29-30: Performance Audit**
- [ ] Run Lighthouse (target: 100/100/100/100 on all pages)
- [ ] Test Core Web Vitals (FCP, LCP, CLS, TBT)
- [ ] Verify total page weight <300KB
- [ ] Test on slow 3G (Chrome DevTools throttling)
- [ ] Optimize any images exceeding size budget
- [ ] Verify font loading (no FOUT/FOIT)

**Day 31-32: Accessibility Audit**
- [ ] Keyboard navigation test (Tab through entire site)
- [ ] Screen reader test (VoiceOver on macOS)
- [ ] WCAG AA contrast verification (all text + gold accents)
- [ ] Focus indicator visibility (gold ring on all interactive elements)
- [ ] Alt text on all images
- [ ] ARIA labels on interactive elements
- [ ] Skip to content link functional
- [ ] Reduced motion preference respected

**Day 33-34: Cross-Browser + Device Testing**
- [ ] Chrome (macOS, Windows, Android)
- [ ] Safari (macOS, iOS)
- [ ] Firefox (macOS, Windows)
- [ ] Edge (Windows)
- [ ] iPhone SE (smallest supported viewport)
- [ ] iPhone 15 Pro (standard iOS)
- [ ] iPad (portrait + landscape)
- [ ] Android (Pixel, Samsung Galaxy)
- [ ] 4K display (1920px+ breakpoint)

**Day 35: Launch**
- [ ] Final content review (typos, broken links, placeholder text)
- [ ] Deploy production build to Vercel
- [ ] Execute redirect plan (see Migration section)
- [ ] Verify custom domain working (florianziesche.com + www redirect)
- [ ] Test all forms + CTAs post-launch
- [ ] Monitor Vercel analytics for errors
- [ ] Announce on LinkedIn, Twitter, Substack
- [ ] Submit to Google Search Console for re-indexing

**Deliverables:** Live production site. Lighthouse 95+. All tests passing. Announced.

---

## V. Dependencies & Blockers

### What Needs to Be Done First (Prerequisites)

| Dependency | Needed For | Owner | Status |
|------------|-----------|-------|--------|
| **Brand synthesis approved** | Copy, colors, typography | Florian | ⏳ Pending review |
| **Content pillars finalized** | Blog categories, nav labels | Florian | ⏳ Pending review |
| **Self-hosted fonts downloaded** | Font loading, subsetting | Developer | 🔲 Not started |
| **Portfolio data** (companies, logos, metrics) | Portfolio page | Florian | 🔲 Needs gathering |
| **Professional headshot** (optional) | About page, OG images | Florian | 🔲 Nice to have |
| **Substack account live** | Newsletter integration | Florian | ✅ Exists (finitematter) |
| **Calendly link confirmed** | Contact CTAs | Florian | ✅ Exists |
| **Google Search Console access** | SEO verification | Developer | 🔲 Setup needed |

### Blockers to Watch

1. **Content is the bottleneck.** The tech will be ready before the copy. Solution: Build with placeholder content, swap in real content in Phase 4. Don't let copy writing block development.

2. **Gold shimmer performance on mobile.** CSS gradients with `background-size: 200%` can trigger GPU compositing issues on older iOS devices. Solution: Reduce shimmer animation on mobile (fewer keyframes, smaller gradient), test on iPhone SE early.

3. **Font subsetting tooling.** `pyftsubset` requires Python. Alternative: Use [google-webfonts-helper](https://gwfh.mranftl.com/) or download pre-subsetted from fontsource.org. Decision: Try fontsource first.

4. **MDX image optimization.** Images referenced in `.mdx` files need to go through Astro's image pipeline. Ensure `<Image>` imports work inside MDX. Test early in Phase 3.

5. **Vercel serverless cold starts.** Contact form via serverless function may have 200-500ms cold start. Solution: Use edge function instead, or route to external service (Formspree, Formspark) for guaranteed <100ms response.

### Third-Party Services

| Service | Purpose | Cost | Priority |
|---------|---------|------|----------|
| **Vercel** (hosting) | Deploy, CDN, serverless | Free tier (sufficient) | Critical |
| **Google Fonts** (source fonts) | Download only, self-host | Free | Critical |
| **Google Search Console** | SEO monitoring | Free | High |
| **Google Analytics / Plausible** | Traffic analytics | Free / €9/mo | Medium |
| **Formspree / Formspark** | Contact form backend | Free tier | Medium |
| **Calendly** | Meeting scheduling | Free tier | Medium |
| **Substack** | Newsletter (external link) | Free | Low (just link to it) |

**Analytics Recommendation:** Use **Plausible** ($9/mo) over Google Analytics. Reasons:
- Privacy-friendly (no cookies → no consent banner needed in EU)
- Lightweight (~1KB script vs GA's ~45KB)
- GDPR compliant by default
- Simple dashboard (no configuration paralysis)
- Aligns with "operator who respects users" brand

---

## VI. Migration Plan

### Current State

**florianziesche.com** is deployed on Vercel as a static HTML site:
- `index.html` — Simple personal page (Inter font, dark theme, 720px container)
- `links.html` — Linktree-style links page (products, resources, VC resources)
- `vercel.json` — Basic routing config

**Domain:** `florianziesche.com` (Vercel DNS)
**Git:** Presumably connected to a Vercel project

### Migration Strategy: In-Place Replacement

**Approach:** Replace the current static HTML with the Astro project in the same Vercel project. Same domain, same deployment pipeline.

**Why not a separate project:**
- Same domain = no DNS changes
- Same Vercel project = existing analytics/logs preserved
- Zero-downtime (Vercel atomic deploys)

### Step-by-Step Migration

**Step 1: Preserve current site** (Before starting Phase 1)
```bash
# Archive current site
cp -r websites/florianziesche.com websites/florianziesche.com.backup-2026-02
```

**Step 2: Initialize Astro in same directory**
```bash
cd websites/florianziesche.com
# Remove old files (after backup)
rm index.html links.html index-for-links-folder.html links-*.html
# Keep vercel.json (will update)
# Initialize Astro project
npm create astro@latest . -- --template minimal
```

**Step 3: Develop locally on feature branch**
```bash
git checkout -b redesign
# All Phase 1-4 work happens here
# Vercel creates preview deploys for each push
```

**Step 4: Launch = merge to main**
```bash
git checkout main
git merge redesign
# Vercel auto-deploys. Atomic switch. Zero downtime.
```

### URL Redirects

The current site has minimal URLs, so redirect scope is small:

| Old URL | New URL | Type |
|---------|---------|------|
| `/` | `/` | No change (homepage) |
| `/links.html` | `/links/` | 301 redirect |
| `/links-concept-*.html` | — | Remove (dev artifacts) |
| `/index-for-links-folder.html` | — | Remove (dev artifact) |

**Vercel redirect config:**

```json
{
  "redirects": [
    { "source": "/links.html", "destination": "/links/", "permanent": true },
    { "source": "/links", "destination": "/links/", "permanent": true }
  ]
}
```

### DNS / Domain

**No changes needed.** Domain stays on Vercel. SSL auto-renews. CDN continues working.

### Rollback Plan

If something goes wrong after launch:

```bash
# Revert to previous commit
git revert HEAD
git push
# Vercel re-deploys the previous version in ~30 seconds
```

Or use Vercel's instant rollback feature in the dashboard (one click).

---

## VII. Astro Configuration (Reference)

```javascript
// astro.config.mjs
import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';
import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';
import vercel from '@astrojs/vercel';

export default defineConfig({
  site: 'https://florianziesche.com',
  output: 'static',
  adapter: vercel({
    webAnalytics: { enabled: true },
  }),
  
  integrations: [
    tailwind({
      applyBaseStyles: false, // We manage our own base styles
    }),
    mdx(),
    sitemap({
      filter: (page) => !page.includes('/links/'), // Exclude linktree from sitemap
    }),
  ],

  image: {
    service: {
      entrypoint: 'astro/assets/services/sharp',
    },
    domains: [], // No external image domains
  },

  markdown: {
    shikiConfig: {
      theme: 'github-dark', // Code syntax theme (matches dark site)
    },
  },

  vite: {
    build: {
      cssMinify: 'lightningcss', // Fastest CSS minification
    },
  },

  prefetch: {
    defaultStrategy: 'viewport', // Prefetch links when they enter viewport
    prefetchAll: false,
  },
});
```

---

## VIII. Quality Checklist (Pre-Launch Gate)

Every item must pass before launch:

### Performance
- [ ] Lighthouse Performance: ≥95 (target 100)
- [ ] Lighthouse Accessibility: ≥95 (target 100)
- [ ] Lighthouse Best Practices: ≥95 (target 100)
- [ ] Lighthouse SEO: ≥95 (target 100)
- [ ] FCP < 1.0s on desktop, < 1.8s on mobile
- [ ] LCP < 1.5s on desktop, < 2.5s on mobile
- [ ] CLS < 0.05
- [ ] TBT < 50ms
- [ ] Total page weight < 300KB (first load, gzipped)

### Accessibility
- [ ] All pages keyboard-navigable
- [ ] Skip-to-content link works
- [ ] All images have alt text
- [ ] All form inputs have labels
- [ ] Focus indicators visible (gold ring)
- [ ] Color contrast AA minimum (AAA where possible)
- [ ] Reduced motion respected
- [ ] Screen reader tested (VoiceOver)

### SEO
- [ ] Unique `<title>` on every page
- [ ] Unique `<meta name="description">` on every page
- [ ] Open Graph tags on every page
- [ ] JSON-LD structured data (Person, Organization)
- [ ] Canonical URLs set
- [ ] Sitemap.xml generated and submitted
- [ ] Robots.txt allows crawling
- [ ] RSS feed functional

### Cross-Browser
- [ ] Chrome (latest)
- [ ] Safari (latest)
- [ ] Firefox (latest)
- [ ] iOS Safari
- [ ] Chrome Android
- [ ] Edge

### Content
- [ ] No placeholder text remaining
- [ ] No broken links (internal or external)
- [ ] All CTAs functional (Calendly, Substack, email)
- [ ] Contact form sends successfully
- [ ] Legal pages present if needed (privacy policy, imprint for Germany)

### Infrastructure
- [ ] Custom domain working (https://florianziesche.com)
- [ ] www → non-www redirect
- [ ] Old URL redirects active
- [ ] Security headers present
- [ ] Analytics tracking verified

---

## IX. Future Enhancements (Post-Launch Backlog)

**Not in scope for v1 launch, but planned:**

| Enhancement | Priority | Effort | When |
|-------------|----------|--------|------|
| Light mode toggle | Medium | 1 day | Month 2 |
| Blog search (client-side) | Medium | 1 day | When >20 posts |
| Newsletter embed (vs. Substack link) | Low | 0.5 day | When ready |
| Portfolio case study videos | Low | 2 days | When video content exists |
| i18n (German version) | Low | 3 days | If German audience significant |
| View Transitions API | Medium | 1 day | After browser support stabilizes |
| Web Vitals monitoring (SpeedCurve) | Low | 0.5 day | Month 3 |
| A/B testing (Vercel Edge Config) | Low | 1 day | When enough traffic |
| AI-powered site search | Low | 2 days | Month 6 |

---

## X. Summary

**Stack:** Astro 5 + Tailwind CSS v4 + MDX + Vercel  
**Timeline:** 5 weeks (35 working days)  
**Total JS shipped:** <5KB  
**Total CSS shipped:** ~15KB  
**Lighthouse target:** 100/100/100/100  
**Migration risk:** Near zero (same Vercel project, atomic deploy, instant rollback)

**The philosophy mirrors the brand:** Restrained technology choices. Zero excess. Every byte justified. Ship fast, iterate publicly.

---

*Technical Roadmap by Planner Agent 4 (Opus)*  
*Ready for development*  
*Date: February 7, 2026*
