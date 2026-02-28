# McKinsey Slide Layout — Exact Measurements

> **Source:** Direct PDF measurement (PyMuPDF) of 3 publicly available McKinsey decks + secondary sources (Slideworks, SlideUplift, Piktochart, LinkedIn analysis by ex-consultants).
> **Date:** 2026-02-21

## Decks Analyzed

| # | Deck | Year | Pages | Slide Size (pts) | Slide Size (in) | Aspect Ratio |
|---|------|------|-------|-------------------|------------------|-------------|
| 1 | USPS: Envisioning America's Future Postal Service | 2010 | 9 | 400 × 600 | 5.56 × 8.33 | Portrait (unusual, likely web-converted) |
| 2 | Investment and Industrial Policy (UNCTAD) | 2018 | 23 | 705.6 × 529.2 | 9.80 × 7.35 | 4:3 |
| 3 | Transportation & Warehousing Sector Analysis (DC) | 2020 | 40 | 960 × 540 | 13.33 × 7.50 | 16:9 |

**Note:** Deck 1 appears web-converted (portrait). Decks 2 and 3 are standard presentation formats and most reliable for layout measurements.

---

## Slide Anatomy — Measured Positions

### Standard McKinsey Slide Zones (from Decks 2 & 3)

```
┌─────────────────────────────────────────────────┐
│ [Section Tab]                          0–3% top │  ← Optional section indicator
├─────────────────────────────────────────────────┤
│                                                 │
│  ACTION TITLE (Georgia Bold / Arial)   3–17%    │  ← 2–3 lines max
│  Full-sentence insight headline                 │
│                                                 │
├─────────────────────────────────────────────────┤
│  Subtitle / chart label               17–22%    │  ← Subheading zone
├─────────────────────────────────────────────────┤
│                                                 │
│                                                 │
│  BODY / CHART ZONE                    22–95%    │  ← Main content area
│  (charts, tables, diagrams, text)               │
│                                                 │
│                                                 │
├─────────────────────────────────────────────────┤
│  Source / footnote / page number      95–100%   │  ← Footer
└─────────────────────────────────────────────────┘
```

---

## Exact Measurements Table

### Action Title Position

| Metric | Deck 2 (4:3, 705×529) | Deck 3 (16:9, 960×540) | As % of Slide |
|--------|----------------------|----------------------|---------------|
| **Top edge (Y start)** | 19.4 pt | 12.5–30.0 pt | **2.3–5.4%** from top |
| **Left margin** | 9.4 pt | 43.7 pt | **1.3–4.6%** from left |
| **Right extent** | ~555–605 pt | ~882–891 pt | Title spans **77–92%** of width |
| **Title height** | ~46 pt (2 lines) | ~58–78 pt (2–3 lines) | **8.7–14.5%** of slide height |
| **Title bottom (Y end)** | ~65.8 pt | ~87.6–91.0 pt | **12.4–16.9%** from top |
| **Title font** | ArialMT 20pt | Georgia-Bold 25pt | — |

### Body/Content Zone Start

| Metric | Deck 2 (4:3) | Deck 3 (16:9) | As % of Slide |
|--------|-------------|---------------|---------------|
| **Subtitle/subheading Y** | ~70 pt | ~98 pt | **13–18%** from top |
| **Body content Y start** | ~100 pt | ~115–140 pt | **19–26%** from top |
| **Body left margin** | 9.4 pt | 42–46 pt | **1.3–4.8%** from left |

### Margins

| Margin | Deck 2 (4:3) | Deck 3 (16:9) | As % | Inches |
|--------|-------------|---------------|------|--------|
| **Left** | 9.4 pt | 43.7 pt | **1.3–4.6%** | 0.13–0.61 in |
| **Top** | 19.4 pt | 12.5 pt | **2.3–3.7%** | 0.17–0.27 in |
| **Right** | ~26 pt | ~45 pt | **3.7–4.7%** | 0.36–0.63 in |
| **Bottom (to footer)** | ~7–16 pt | ~15–27 pt | **1.3–5.0%** | 0.10–0.38 in |

### Footer

| Metric | Deck 2 | Deck 3 | As % |
|--------|--------|--------|------|
| **Source text Y** | 513 pt | 520+ pt | **96–97%** from top |
| **Font size** | 8 pt | 8 pt | — |
| **Page number position** | Right-aligned, ~83% from left | Right-aligned | — |

---

## Font Sizes — Measured + Corroborated

| Element | Measured (Decks 2 & 3) | SlideUplift Guide | Recommended Range |
|---------|----------------------|-------------------|-------------------|
| **Action Title** | 20–25 pt | 24–28 pt | **20–28 pt** |
| **Title font** | ArialMT or Georgia-Bold | Sans-serif (Arial) | Georgia (titles) or Arial |
| **Subtitle / chart header** | 14–16 pt (Bold) | — | **14–16 pt** |
| **Body text** | 10–14 pt | 16–18 pt | **12–18 pt** |
| **Chart labels** | 10–12 pt | 12–14 pt | **10–14 pt** |
| **Source / footnote** | 8 pt | — | **8 pt** |
| **Section tab** | 8–10 pt | — | **8–10 pt** |

---

## Typography System

| Role | Font (pre-2019) | Font (post-2019 rebrand) | PowerPoint substitute |
|------|----------------|--------------------------|----------------------|
| **Headlines** | Arial Bold | Bower (custom serif) | **Georgia Bold** |
| **Body text** | Arial | McKinsey Sans | **Arial** |
| **Emphasis** | Arial Bold | McKinsey Sans Bold | **Arial Bold** |

> Per Slideworks: McKinsey uses custom fonts Bower + McKinsey Sans internally, but substitutes Georgia + Arial in shared PowerPoint files for compatibility.

---

## Key Design Rules (from multiple sources)

1. **Action title = full sentence** (not a label), max 2 lines
2. **One message per slide**
3. **Title spans ~80–90% of slide width** (generous horizontal space)
4. **Body zone starts at ~18–22% from top** — this is the consistent "content start line"
5. **Left margin: 4.5–5%** for 16:9 slides (narrower ~1.3% in older 4:3 decks)
6. **Minimum 1-inch margins** mentioned in Piktochart analysis of 2016 McKinsey global report
7. **White and dark blue backgrounds** alternated for visual rhythm
8. **Limited color palette**: dark navy, vivid blue (accent), white, grays
9. **Source/footnote always at bottom** in 8pt, right-aligned page numbers

---

## Recommended Template Values (for 16:9, 960×540 pt / 13.33×7.50 in)

For building a McKinsey-style template:

| Element | Position | Size |
|---------|----------|------|
| **Action Title** | Top: 2.5%, Left: 4.5%, Width: 88% | Georgia Bold 24pt |
| **Title max height** | 15% of slide (2 lines) | — |
| **Subtitle line** | Top: 17% | Arial 14pt |
| **Body zone** | Top: 20%, Left: 4.5%, Width: 91%, Height: 73% | Arial 12–14pt |
| **Footer/source** | Top: 96%, Left: 4.5% | Arial 8pt |
| **Page number** | Top: 96%, Right-aligned at 95% | Arial 8pt |
| **Left margin** | 43 pt / 0.60 in / 4.5% | — |
| **Right margin** | 45 pt / 0.63 in / 4.7% | — |
| **Top margin** | 12–20 pt / 0.17–0.28 in / 2.3–3.7% | — |
| **Bottom margin** | 20 pt / 0.28 in / 3.7% | — |

---

## Confidence & Caveats

- **Confidence: 75%** — Measurements are from real McKinsey PDFs, but PDF export can shift positions slightly vs. native PPTX. Font substitution may also affect spacing.
- Deck 1 (USPS) was portrait-oriented and likely a web conversion, so excluded from main measurements.
- Post-2019 rebrand decks use Georgia Bold for titles (confirmed in Deck 3, 2020).
- Pre-2019 decks used Arial throughout (confirmed in Deck 2, 2018).
- No actual .pptx files were available for download; all measurements from PDF renders.
- For pixel-perfect accuracy, measuring a leaked/shared .pptx template would be ideal.
