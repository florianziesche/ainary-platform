# CORPORATE-IDENTITY.md — Ainary Ventures CI

*Quelle der Wahrheit. Vor JEDEM visuellen Output konsultieren.*
*Basiert auf BRAND-IDENTITY-SYNTHESIS.md (479 Zeilen). Dies ist die kompakte Referenz.*

---

## Fonts

```css
--font-display: 'Inter Display', sans-serif;     /* Headlines */
--font-body: 'Inter Variable', 'Inter', sans-serif; /* Body */
--font-mono: 'JetBrains Mono', monospace;         /* Code, Zahlen, Labels */
```

Google Fonts Import:
```html
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
```

## Farben — Gold Spectrum

| Name | HEX | Verwendung |
|------|-----|------------|
| Warm Gold | #d4a853 | CTAs, Hover, aktive Elemente |
| Base Gold | #c8aa50 | Standard-Akzent, Borders |
| Cool Gold | #b09a45 | Sekundäre Akzente |
| Pale Gold | #e8d89f | Backgrounds, Highlights |
| Deep Gold | #9d7f3b | Dark-Mode Akzente, Text auf dunklem BG |

**Regel: 5% Gold, 95% Monochrome.** Gold ist Gewürz, nicht Hauptgericht.

## Light Theme (bevorzugt für Kunden-Deliverables)

```css
--bg: #fafaf8;
--surface: #ffffff;
--surface-hover: #f5f5f3;
--text-primary: #1a1a1a;
--text-secondary: #666666;
--border: #e5e5e0;
--border-subtle: #f0f0eb;
--accent: #c8aa50;
--accent-bg: rgba(200, 170, 80, 0.08);
--accent-border: rgba(200, 170, 80, 0.25);
```

## Dark Theme (für Wow-Faktor Demos)

```css
--bg: #0a0a0a;
--surface: #141414;
--surface-hover: #1a1a1a;
--text-primary: #f0f0f0;
--text-secondary: #888888;
--border: #2a2a2a;
--accent: #c8aa50;
```

## Spacing & Layout

```css
--radius: 12px;          /* Cards */
--radius-sm: 8px;        /* Buttons, Inputs */
--shadow: 0 1px 3px rgba(0,0,0,0.04), 0 1px 2px rgba(0,0,0,0.02);
--shadow-hover: 0 4px 12px rgba(0,0,0,0.06);
--max-width: 1200px;     /* Content max-width */
--padding-section: 48px; /* Section padding */
--padding-card: 32px;    /* Card padding */
```

## Typografie-Skala

```css
--text-xs: 0.75rem;   /* 12px — Labels, Badges */
--text-sm: 0.875rem;  /* 14px — Sekundärtext */
--text-base: 1rem;    /* 16px — Body */
--text-lg: 1.125rem;  /* 18px — Large Body */
--text-xl: 1.25rem;   /* 20px — Section Titles */
--text-2xl: 1.5rem;   /* 24px — Page Titles */
--text-3xl: 2rem;     /* 32px — Hero */
```

## Kontaktdaten (auf allen externen Dokumenten)

```
Florian Ziesche
+49 151 230 39 208
florian@ainaryventures.com
ainaryventures.com
```

## Do's und Don'ts

### Do's
- Inter für alles. Keine anderen Fonts.
- Gold nur als Akzent (Borders, Icons, CTAs)
- Großzügig Whitespace
- Cards mit border-radius: 12px und subtlem Shadow
- Tabs statt Scrollen für komplexe Dashboards
- JetBrains Mono für Zahlen, Metriken, Code
- Professionell genug für McKinsey-Vergleich

### Don'ts
- Keine Emojis in professionellen Dokumenten (CSS-Icons oder Text statt Apple-Symbole)
- Kein Gradient auf Gold
- Kein Gold als Hintergrundfarbe für große Flächen
- Keine anderen Akzentfarben (kein Blau, kein Grün)
- Kein Bold-Gold-Text auf weißem Hintergrund (zu schwach)
- Keine generischen Stock-Fotos

---

*Vollständige Details: BRAND-IDENTITY-SYNTHESIS.md*
*Letzte Aktualisierung: 2026-02-08*
