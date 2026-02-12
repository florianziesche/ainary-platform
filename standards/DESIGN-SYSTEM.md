# DESIGN-SYSTEM.md — Intelligence Platform CI

*Single Source of Truth. JEDER Build muss diesem Dokument folgen.*
*Referenz-Qualität: Linear.app — unser Benchmark für Craft.*
*Erstellt: 2026-02-12*

---

## Philosophie

**Restraint over decoration.** Weniger ist mehr. Jedes Element muss seinen Platz verdienen. Wenn etwas entfernt werden kann ohne Funktion zu verlieren — entferne es.

**Spacing is the design.** Der leere Raum zwischen Elementen ist wichtiger als die Elemente selbst. Großzügig. Immer.

**Typography carries the weight.** Farbe ist Gewürz (5%). Typografie ist das Gericht (95%). Headline-Gewicht, Letter-Spacing und Größen-Hierarchie definieren die Qualität.

**Two accents, clear roles.** Indigo (#6366f1) = Primary. CTAs, Icons, Links, aktive States. Gold (#c8aa50) = Special. Preise, Badges, Premium-Highlights, "Wow"-Momente. Beide sparsam. Nie als Hintergrundfarbe. Nie für große Flächen.

---

## Farben

### Dark Theme (Primary — alle Seiten)

```css
:root {
  /* Backgrounds */
  --bg-page:          #08080c;    /* Seitengrund — fast schwarz, leicht blau */
  --bg-surface:       #111116;    /* Cards, Panels */
  --bg-surface-hover: #18181f;    /* Hover State */
  --bg-elevated:      #1e1e26;    /* Modals, Dropdowns, Tooltips */
  --bg-input:         #0e0e13;    /* Input Fields */
  
  /* Borders — subtil, fast unsichtbar */
  --border-default:   rgba(255, 255, 255, 0.06);   /* Standard */
  --border-hover:     rgba(255, 255, 255, 0.10);   /* Hover */
  --border-active:    rgba(200, 170, 80, 0.30);    /* Active/Focus — Gold tint */
  
  /* Text */
  --text-primary:     #ededf0;    /* Headlines, wichtiger Text */
  --text-secondary:   #8b8b95;    /* Beschreibungen, Labels */
  --text-muted:       #55555e;    /* Placeholder, deaktiviert */
  
  /* Primary Accent — Indigo (CTAs, Icons, Links, aktive States) */
  --accent:           #6366f1;    /* Primary: CTAs, Icons, Links */
  --accent-hover:     #818cf8;    /* Hover */
  --accent-muted:     rgba(99, 102, 241, 0.12);  /* Subtle BG */
  --accent-border:    rgba(99, 102, 241, 0.20);  /* Border */
  
  /* Special Accent — Gold (Preise, Badges, Premium-Momente) */
  --gold:             #c8aa50;    /* Preise, Badges, "Premium" Highlights */
  --gold-hover:       #d4b85c;
  --gold-muted:       rgba(200, 170, 80, 0.12);
  --gold-border:      rgba(200, 170, 80, 0.20);
  
  /* Status */
  --success:          #34d399;
  --warning:          #fbbf24;
  --error:            #f87171;
}
```

### Dual-Accent System: Indigo + Gold

| Element | Farbe | Beispiel |
|---------|-------|---------|
| CTAs, Buttons | Indigo | "Try X-Ray Free", "Sign up" |
| Icons (aktiv) | Indigo | Navigation, Tool-Icons, Check-Icons |
| Links | Indigo | "Read more →", Nav-Links hover |
| Focus States | Indigo | Input focus ring |
| Preise / Zahlen | Gold | "$29/month", "90 sec", "243" |
| Badges | Gold | "MOST POPULAR", "HOW WE BUILD" |
| Premium Highlights | Gold | Featured Card Border, Special Moments |
| Stats | Gold | Große Zahlen in Stats Section |

**Kein anderer Tech-Anbieter kombiniert Indigo + Gold.** Das ist unser visueller Fingerabdruck.

### Product-Farben (subtile Akzente)
```css
--product-startup:   #8b5cf6;   /* Purple — Startup X-Ray */
--product-research:  #10b981;   /* Emerald — Research Engine */
```
NUR als Tool-Card Icon oder Badge auf der jeweiligen Tool-Seite. Corporate X-Ray und Advisory Board nutzen die Brand-Farben (Indigo/Gold).

---

## Typography

### Font Stack

```css
/* Headlines — Geist (von Vercel, modern, differenziert) */
--font-display: 'Geist', -apple-system, BlinkMacSystemFont, sans-serif;

/* Body — Inter (bewährt, lesbar) */
--font-body: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;

/* Data/Code — JetBrains Mono */
--font-mono: 'JetBrains Mono', 'Fira Code', monospace;
```

Google Fonts Import:
```html
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
```

Geist: Von https://vercel.com/font herunterladen oder CDN:
```html
<link href="https://cdn.jsdelivr.net/npm/geist@1.0.0/dist/fonts/geist-sans/style.css" rel="stylesheet">
```

**Fallback wenn Geist nicht lädt:** Inter für alles. Kein visueller Bruch.

### Type Scale

```css
/* Hierarchie — jede Stufe muss sich KLAR unterscheiden */
--text-hero:    3.5rem;    /* 56px — Landing Page Hero ONLY */
--text-h1:      2.5rem;    /* 40px — Seitentitel */
--text-h2:      1.75rem;   /* 28px — Section Titles */
--text-h3:      1.25rem;   /* 20px — Card Titles, Sub-sections */
--text-body:    1rem;       /* 16px — Body Text */
--text-small:   0.875rem;  /* 14px — Labels, Captions */
--text-xs:      0.75rem;   /* 12px — Badges, Tags, Fine Print */
```

### Font Weights

```css
/* NUR diese 4 Weights verwenden */
--weight-light:    300;    /* Hero Subtitle, große Beschreibungen */
--weight-regular:  400;    /* Body Text */
--weight-medium:   500;    /* Labels, Navigation, Card Titles */
--weight-semibold: 600;    /* Headlines, CTAs, Preise */

/* KEIN 700 (Bold). Semibold ist das Maximum. Bold wirkt "billig". */
```

### Letter Spacing

```css
/* Headlines: leicht enger = Premium-Gefühl */
h1, h2 { letter-spacing: -0.02em; }

/* Small Text: leicht weiter = besser lesbar */
.label, .tag, .badge { letter-spacing: 0.04em; text-transform: uppercase; }

/* Body: default */
p { letter-spacing: 0; }
```

### Line Height

```css
--lh-tight:   1.2;    /* Headlines */
--lh-normal:  1.6;    /* Body */
--lh-relaxed: 1.8;    /* Long-form Blog Text */
```

---

## Spacing System

```css
/* 8px Base Grid — ALLES ist ein Vielfaches von 8 */
--space-1:   4px;     /* Micro — Icon-zu-Text */
--space-2:   8px;     /* Tight — inline Elemente */
--space-3:   12px;    /* Small — innerhalb von Groups */
--space-4:   16px;    /* Default — Padding in Inputs */
--space-5:   24px;    /* Medium — Card Padding intern */
--space-6:   32px;    /* Large — zwischen Sections in Cards */
--space-8:   48px;    /* XL — Section Padding */
--space-10:  64px;    /* XXL — zwischen Sektionen */
--space-12:  80px;    /* Hero — zwischen großen Blöcken */
--space-16:  120px;   /* Page — Top/Bottom Margin */
```

### Regel: Lieber zu viel Platz als zu wenig
Wenn du unsicher bist → eine Stufe größer. Linear hat ~2x so viel Spacing wie "normale" Websites. Das IST der Qualitätsunterschied.

---

## Components

### Cards

```css
.card {
  background: var(--bg-surface);
  border: 1px solid var(--border-default);
  border-radius: 16px;            /* Größer als 12px = moderner */
  padding: 32px;                  /* Großzügig */
  transition: border-color 0.2s ease;
}

.card:hover {
  border-color: var(--border-hover);
  /* KEIN shadow-change. KEIN transform. Subtil. */
}

.card--featured {
  border-color: var(--accent-border);
  background: linear-gradient(
    135deg, 
    rgba(200, 170, 80, 0.04) 0%, 
    transparent 50%
  );
}
```

**KEIN Glassmorphism.** Kein `backdrop-filter: blur()`. Das ist 2023. Linear-Style: Solide Hintergründe, subtile Borders.

### Buttons

```css
/* Primary — Gold, SPARSAM (max 1 pro Screen-Section) */
.btn-primary {
  background: var(--accent);     /* Indigo */
  color: #ffffff;
  font-family: var(--font-body);
  font-weight: 500;
  font-size: 0.875rem;
  padding: 10px 20px;
  border-radius: 8px;
  border: none;
  cursor: pointer;
  transition: background 0.15s ease;
}
.btn-primary:hover { background: var(--accent-hover); }

/* Secondary — Outline, für nicht-primäre Actions */
.btn-secondary {
  background: transparent;
  color: var(--text-primary);
  border: 1px solid var(--border-default);
  font-weight: 500;
  font-size: 0.875rem;
  padding: 10px 20px;
  border-radius: 8px;
  cursor: pointer;
  transition: border-color 0.15s ease;
}
.btn-secondary:hover { border-color: var(--border-hover); }

/* Ghost — Für Navigation, tertiäre Actions */
.btn-ghost {
  background: transparent;
  color: var(--text-secondary);
  border: none;
  padding: 8px 16px;
  font-weight: 500;
  cursor: pointer;
}
.btn-ghost:hover { color: var(--text-primary); }
```

**Regel:** NUR 1 Primary Button pro sichtbarem Bereich. Alles andere = Secondary oder Ghost.

### Navigation (Top-Bar)

```css
.nav {
  position: sticky;
  top: 0;
  z-index: 100;
  background: rgba(8, 8, 12, 0.8);
  backdrop-filter: blur(12px);      /* NUR hier ist blur erlaubt */
  border-bottom: 1px solid var(--border-default);
  padding: 0 24px;
  height: 56px;
  display: flex;
  align-items: center;
}
```

### Input Fields

```css
.input {
  background: var(--bg-input);
  border: 1px solid var(--border-default);
  border-radius: 10px;
  padding: 12px 16px;
  color: var(--text-primary);
  font-family: var(--font-body);
  font-size: 1rem;
  transition: border-color 0.15s ease;
}
.input:focus {
  outline: none;
  border-color: var(--accent-border);
  box-shadow: 0 0 0 3px var(--accent-muted);
}
.input::placeholder { color: var(--text-muted); }
```

### Badges / Tags

```css
.badge {
  font-family: var(--font-mono);
  font-size: 0.7rem;
  font-weight: 500;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  padding: 4px 10px;
  border-radius: 6px;
  background: var(--gold-muted);    /* Gold für Badges */
  color: var(--gold);
  border: 1px solid var(--gold-border);
}
```

### Pricing Cards (spezifisch)

```css
.pricing-card {
  /* Basis Card Styles */
  padding: 40px 32px;
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.pricing-card__name {
  font-family: var(--font-body);
  font-weight: 500;
  font-size: 1rem;
  color: var(--text-primary);
}

.pricing-card__price {
  font-family: var(--font-display);
  font-weight: 600;
  font-size: 2.5rem;
  letter-spacing: -0.03em;
  color: var(--text-primary);
}

.pricing-card__price span.period {
  font-size: 1rem;
  font-weight: 400;
  color: var(--text-muted);
}

.pricing-card__description {
  font-size: 0.875rem;
  color: var(--text-secondary);
  line-height: 1.5;
}

/* Feature List in Pricing */
.feature-list {
  list-style: none;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.feature-list li {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 0.875rem;
  color: var(--text-secondary);
}

.feature-list li svg {
  width: 16px;
  height: 16px;
  color: var(--accent);
  flex-shrink: 0;
}
```

---

## Icons

- **KEINE Emoji.** Nie. Nirgends.
- **SVG Inline** — Custom gezeichnet oder Lucide Icons (https://lucide.dev)
- Stroke-Width: 1.5px (nicht 2px — zu dick)
- Größen: 16px (inline), 20px (in Cards), 24px (Navigation), 32px (Features)
- Farbe: `currentColor` (erbt vom Text) oder `var(--accent)` für aktive States

---

## Animations & Transitions

```css
/* EINZIGE erlaubte Transitions */
transition: color 0.15s ease;
transition: border-color 0.15s ease;
transition: background 0.15s ease;
transition: opacity 0.15s ease;
transition: transform 0.2s ease;

/* VERBOTEN */
/* Kein bounce, kein spring, kein elastic */
/* Kein transform: scale() auf hover (außer Buttons: max 1.02) */
/* Kein box-shadow Animation (zu teuer, sieht billig aus) */
/* Keine Scroll-Animationen die Content verstecken (Kintsugi #7) */
/* KEIN opacity: 0 als Default. NIEMALS. */
```

### Erlaubt:
- Fade-in bei Scroll: `opacity: 1` default, Animation optional als Enhancement
- Subtle parallax auf Hero-Bildern (max 20px Versatz)
- Typing-Animation im Chat UI (Advisory Board)
- Loading Spinner/Skeleton für async Content

---

## Layout

### Max Width
```css
--max-width-page:    1200px;   /* Content-Bereich */
--max-width-text:    680px;    /* Blog-Text, Beschreibungen */
--max-width-narrow:  520px;    /* Formulare, Modals */
```

### Grid
```css
/* Pricing Cards: 4-Column */
.pricing-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1px;                        /* Linear-Style: 1px Gap = gemeinsame Borders */
  background: var(--border-default); /* Border-Farbe sichtbar im Gap */
  border-radius: 16px;
  overflow: hidden;
}

/* Responsive */
@media (max-width: 1024px) { grid-template-columns: repeat(2, 1fr); }
@media (max-width: 640px)  { grid-template-columns: 1fr; }
```

### Sections
```css
.section {
  padding: var(--space-16) 0;   /* 120px oben/unten */
  max-width: var(--max-width-page);
  margin: 0 auto;
  padding-left: 24px;
  padding-right: 24px;
}
```

---

## Social Proof

```css
.social-proof {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 48px;
  padding: 48px 0;
  border-top: 1px solid var(--border-default);
  border-bottom: 1px solid var(--border-default);
}

.social-proof__label {
  font-size: 0.8rem;
  color: var(--text-muted);
  letter-spacing: 0.04em;
  text-transform: uppercase;
}

/* Logos: Grayscale, opacity 0.5, hover full */
.social-proof img {
  height: 24px;
  filter: grayscale(1) brightness(2);
  opacity: 0.4;
  transition: opacity 0.15s ease;
}
.social-proof img:hover { opacity: 0.8; }
```

---

## Responsive Breakpoints

```css
/* Mobile First */
@media (min-width: 640px)  { /* sm — Tablet Portrait */ }
@media (min-width: 768px)  { /* md — Tablet Landscape */ }
@media (min-width: 1024px) { /* lg — Desktop */ }
@media (min-width: 1280px) { /* xl — Wide Desktop */ }
```

---

## Copy & Tone

- **Tagline:** "Human × AI = Compounded Intelligence"
- **"Consultant-grade"** — nie "McKinsey-level"

### Section Anatomy (Mandatory Structure)
Every content section follows the same anatomy:

```
┌─────────────────────────────────────┐
│  Section Title (h2)                 │
│  Section Subtitle (1-2 lines,       │
│    explains WHY this matters)       │
│                                     │
│  ┌─────┐ ┌─────┐ ┌─────┐          │
│  │Card │ │Card │ │Card │  Content  │
│  └─────┘ └─────┘ └─────┘          │
│                                     │
│  Cross-link to related page →       │
└─────────────────────────────────────┘
```

**Rules:**
1. **Title**: `section-title` class. Short. What it is.
2. **Subtitle**: `section-subtitle` class. 1-2 lines. Why it matters to the CUSTOMER. Color: `var(--text-secondary)`. Max-width: 540px. Centered.
3. **Content**: Cards, steps, stats — whatever fits.
4. **Cross-link**: At section bottom. Links to the most relevant other page. Format: descriptive text + `→`. Color: Indigo. Centered.

**Subtitle tone:** Customer benefit, not feature description.
- ✅ "Three products, one engine. Choose the lens that fits your question."
- ❌ "Our suite of AI-powered intelligence tools."

**Cross-link examples:**
- Intelligence Suite → "Explore all tools →" (tools.html)
- Why/How → "See how we build →" (quality.html)
- How It Works → "Try it free →" (tools.html)
- Fresh Intelligence → "Read today's brief →" (#)
- Stats → "See pricing →" (pricing.html)

**Apply to:** Every section on every page. No section without subtitle + cross-link.

### Grid Content Alignment (Horizontal Rhythm)
All sibling cards/items in a grid must have their text elements (titles, descriptions, meta, CTAs) at the **same vertical position**. This creates visual rhythm across columns.

**Rules:**
1. Every card in a grid uses `display: flex; flex-direction: column;`
2. Title: fixed height or `min-height` to align across cards (e.g., `min-height: 2em` for single-line, `min-height: 3.2em` for wrapping titles)
3. Description: use `min-height` based on longest expected text (e.g., `min-height: 5em`)
4. Meta/CTA: pushed to bottom via `margin-top: auto` on the last flexible element
5. When cards have different content lengths, the `min-height` ensures horizontal alignment
6. Test: visually scan each row — titles, descriptions, meta, and CTAs must form horizontal lines

**Apply to:** tool-card grids, step grids, pricing cards, blog article cards, any repeating card pattern.

### Card Content Alignment (Legacy) (Global Rule)
Wenn Cards nebeneinander stehen und variable Textlängen haben:
- Card-Content MUSS `display: flex; flex-direction: column;` sein
- Letztes Element (Meta/Footer) bekommt `margin-top: auto;`
- Titel: Feste max Zeilen via `-webkit-line-clamp` (z.B. 2)
- Excerpt: Feste max Zeilen via `-webkit-line-clamp` (z.B. 2-3)
- Ergebnis: Meta-Zeile steht IMMER auf gleicher Höhe, unabhängig von Textlänge
```css
.card__content {
  display: flex;
  flex-direction: column;
  flex: 1;
}
.card__title {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
.card__excerpt {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
.card__meta {
  margin-top: auto;
}
```
- **"Intelligence"** — nicht "Analysis" oder "Report"
- **Confident but not arrogant** — "Start free." nicht "Try our amazing tool!"
- **Numbers > Adjectives** — "5 AI agents, 3 rounds, $0.15/report" statt "powerful AI platform"
- **Short sentences.** Punkt. Nicht Komma.
- **Tier descriptions:** Kurz, eine Zeile. "For individuals exploring intelligence tools." "For teams making strategic decisions." "For organizations requiring dedicated infrastructure."

---

## Checkliste vor JEDEM Build

- [ ] Dieses Dokument gelesen?
- [ ] Geist + Inter + JetBrains Mono importiert?
- [ ] Farben stimmen mit :root überein?
- [ ] Kein Glassmorphism (kein backdrop-blur außer Nav)?
- [ ] Kein Bold (700)? Maximal Semibold (600)?
- [ ] Letter-Spacing auf Headlines (-0.02em)?
- [ ] Spacing großzügig genug? (Lieber eine Stufe größer)
- [ ] Nur 1 Primary Button pro sichtbarem Bereich?
- [ ] Keine Emoji? Nur SVG Icons (Lucide, Stroke 1.5)?
- [ ] Kein opacity:0 Default?
- [ ] Responsive getestet?

---

*Dieses Dokument ist das Gesetz. Kein Output verlässt das System ohne es zu erfüllen.*
