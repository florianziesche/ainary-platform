# BCG & Bain Slide Layout Measurements

> **Date:** 2026-02-21
> **Method:** Downloaded 6 public PDFs from BCG and Bain, extracted exact text element positions using PyMuPDF. Supplemented with ex-consultant sources (Slideworks, Deckary, Analyst Academy).
> **Confidence:** 85% — measurements from real PDFs; Bain uses report format more than slide format publicly.

---

## Source Documents Analyzed

| # | Document | Format | Pages | Slide Size (pt) | Slide Size (in) |
|---|----------|--------|-------|-----------------|-----------------|
| 1 | BCG AI at Work 2024 | Widescreen 16:9 | 22 | 1200 × 628 | 16.67" × 8.72" |
| 2 | BCG CEO GenAI Roadmap 2023 | Widescreen 16:9 | 34 | 960 × 540 | 13.33" × 7.50" |
| 3 | BCG Cost & Growth 2025 | Widescreen 16:9 | 24 | 960 × 540 | 13.33" × 7.50" |
| 4 | BCG NYC Media 2012 | 4:3 | 42 | 756 × 540 | 10.50" × 7.50" |
| 5 | Bain Management Tools & Trends 2018 | Portrait/Report | 16 | 612 × 792 | 8.50" × 11.00" |
| 6 | Bain Luxury Goods 2016 | Portrait/Report | 40 | 612 × 792 | 8.50" × 11.00" |

**Key finding:** BCG publishes in landscape slide format (16:9 or 4:3). Bain's public materials are predominantly portrait report-style PDFs, not slide decks.

---

## BCG Slide Measurements (Content Slides, not covers)

### Slide Canvas
| Property | BCG Modern (2023-2025) | BCG Legacy (2012) |
|----------|----------------------|-------------------|
| Canvas size | 960 × 540 pt (13.33" × 7.50") | 756 × 540 pt (10.50" × 7.50") |
| Aspect ratio | 16:9 | ~4:3 (1.4:1) |
| Note | Some decks use 1200×628 (super-wide 16:9) | Standard consulting 4:3 |

### Action Title Zone
| Property | BCG Modern (960×540) | BCG Wide (1200×628) | BCG Legacy (756×540) |
|----------|---------------------|---------------------|---------------------|
| **Font** | HendersonBCGSans-Bold | HendersonBCGSans-Bold / BCGSerif | Arial Bold |
| **Font size** | 24pt | 31pt (action titles), 44pt (key stats) | 24pt |
| **Left margin** | 30–39pt (0.42"–0.54") | 52–54pt (0.72"–0.75") | 36pt (0.50") |
| **Top of title (Y)** | 19–49pt (3.5%–9.1%) | 37–42pt (6.0%–6.6%) | 19–48pt (3.5%–8.8%) |
| **Title Y as %** | ~3.5–9% from top | ~6% from top | ~3.5–9% from top |
| **Right margin** | ~38–190pt (varies with text length) | ~52–58pt | ~33–40pt |
| **Max title width** | ~90% of canvas | ~91% of canvas (1088pt/1200) | ~91% of canvas (688pt/756) |
| **Title lines** | 1–2 lines | 1–2 lines | 1–2 lines |

### Body Zone
| Property | BCG Modern (960×540) | BCG Wide (1200×628) | BCG Legacy (756×540) |
|----------|---------------------|---------------------|---------------------|
| **Body starts at Y** | ~116pt (21.5%) | ~134pt (21.4%) | ~109pt (20.1%) |
| **Subtitle font size** | 16pt (bold) | 20pt (bold) | 16pt (bold) |
| **Body text size** | 14pt | 16pt | 14pt |
| **Small text/labels** | 10–12pt | 10–14pt | 9–12pt |
| **Source line** | 7pt | 7–10pt | 7pt |
| **Left margin (body)** | Same as title (30–39pt) | Same as title (52–55pt) | Same as title (36pt) |

### Summary: BCG Layout Grid (normalized to standard 960×540)

```
┌─────────────────────────────────────────────────────────┐
│ ← 30pt (3.1%) →                          ← 38pt (4%) → │
│                                                          │
│  ACTION TITLE (24pt Bold)           Y = ~20pt (3.5%)    │
│  Full-sentence takeaway, 1-2 lines                      │
│                                                          │
│  ─────────── body zone starts ──────── Y = ~116pt (21%) │
│                                                          │
│  SUBTITLE (16pt Bold)                                    │
│  Body text (14pt), charts, tables                        │
│                                                          │
│                                                          │
│                                                          │
│                                                          │
│  Source: (7pt)                          Y ≈ 520pt (96%) │
│  Page #                                                  │
└─────────────────────────────────────────────────────────┘
```

---

## Bain Report-Style Measurements

Bain's public PDFs are primarily portrait reports (8.5"×11"), not landscape slides. Measurements below reflect this format:

| Property | Bain Report Format |
|----------|-------------------|
| **Page size** | 612 × 792pt (8.50" × 11.00") |
| **Title font** | Futura-Light / Futura-Book, 14–18pt |
| **Body font** | Scala-Regular, 10pt |
| **Header/Running head** | Futura-Book, 9pt |
| **Left margin** | 72–87pt (1.00"–1.21") |
| **Title Y position** | ~95–121pt (12–15% from top) |
| **Body text start** | ~150pt (19% from top) |
| **Figure labels** | Futura-Heavy 12pt |
| **Source/copyright** | 6–7pt |

---

## Font Families

| Firm | Title Font | Body Font | Accent/Label |
|------|-----------|-----------|-------------|
| **BCG (modern)** | HendersonBCGSans-Bold | HendersonBCGSans-Light | HendersonBCGSerif-Regular |
| **BCG (legacy)** | Arial Bold | Arial | Arial |
| **Bain** | Futura-Light / Futura-Heavy | Scala-Regular | Futura-Book |

---

## Key Design Principles (from ex-consultant sources)

| Principle | BCG | Bain |
|-----------|-----|------|
| Action title rule | Mandatory. Full sentence. Max 15 words, 2 lines | Same principle, less strict format |
| Body text sizes | 2 sizes: 16pt headlines + 14pt body (or 14/12) | 14pt headlines + 10pt body |
| Colors | Green accent (BCG brand), black body, gray secondary | Red accent (Bain brand), black body |
| Max fonts per slide | 2 (title + body) | 2 |
| Source citations | Required on every data slide, 7pt bottom | Required, 6-7pt |
| White space | Generous margins, ~3-5% all sides | Wider margins (1"+) in report format |

---

## Practical Takeaways for Slide Design

For a **standard 16:9 slide (960×540pt / 13.33"×7.50")**:

| Element | Position/Size |
|---------|--------------|
| **Left margin** | 30–36pt (0.42"–0.50") = ~3–4% |
| **Right margin** | 30–38pt = ~3–4% |
| **Action title Y** | 18–35pt from top (~3–6%) |
| **Action title font** | 24pt bold sans-serif |
| **Body zone starts** | ~110–120pt from top (~20–22%) |
| **Subtitle font** | 16pt bold |
| **Body text font** | 14pt regular |
| **Source line Y** | ~520pt (~96%), 7pt |
| **Usable content width** | ~890pt (~93% of canvas) |
| **Usable body height** | ~400pt (from 120pt to 520pt = ~74% of canvas) |

---

## Limitations

1. **Bain slide decks not publicly available** — Bain publishes reports in portrait/letter format, not landscape slides. Their internal slide format likely follows similar patterns to BCG but with Futura/Scala fonts and Bain red accent.
2. **BCG uses custom Henderson BCG Sans** — not publicly available; closest substitutes are Helvetica Neue or Arial.
3. **Measurements are from PDF extraction** — actual PowerPoint templates may have slightly different guide positions due to PDF export settings.
4. **Font sizes in PDF may differ from PPT source** — PDF embedding can shift sizes by ±0.5pt.
