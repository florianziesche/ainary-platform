# Palantir Investor Presentation — Design Measurements

**Sources analyzed:**
- Palantir Q1 2025 Investor Presentation (40 pages) — [PDF](https://investors.palantir.com/files/Palantir%20-%20Q1%202025%20Investor%20Presentation.pdf)
- Palantir Q4 2025 Investor Presentation (39 pages) — [PDF](https://investors.palantir.com/files/Palantir%20-%20Q4%202025%20Investor%20Presentation.pdf)

**Date:** 2026-02-21

---

## Canvas & Grid

| Property | Value | Notes |
|----------|-------|-------|
| Slide dimensions | **1600 × 900 pt** (16:9) | Both decks identical |
| Pixel equivalent | 1600 × 900 px at 1× | PDF pts = px at 72dpi |
| Aspect ratio | 16:9 | Standard widescreen |

---

## Margins & Positioning

| Property | Q1 2025 | Q4 2025 | Consensus |
|----------|---------|---------|-----------|
| **Left margin (content start)** | 49.9 pt | 49.9–50.3 pt | **~50 pt (3.1%)** |
| **Left margin (nav pill)** | 61.9 pt | 61.9 pt | **62 pt (3.9%)** |
| **Top margin (nav pill Y)** | 53.1–53.4 pt | 53.1–53.4 pt | **~53 pt (5.9%)** |
| **Headline Y start (content pages)** | 88.6 pt | 88.6 pt | **~89 pt (9.9%)** |
| **Headline Y start (story pages)** | 102–125 pt | 98–120 pt | **~100–120 pt (11–13%)** |
| **Right margin** | ~63–100 pt | ~53–113 pt | **~60 pt minimum (3.8%)** |
| **Bottom copyright Y** | 845.1 pt | 845.1 pt | **845 pt (55 pt bottom margin, 6.1%)** |
| **Footer text margin left** | 47.9 pt | 47.9 pt | **48 pt** |
| **Bullet indent (→ items)** | 110 pt | 110 pt | **110 pt (6.9%)** |
| **Content right edge (text)** | ~1540 pt | ~1550 pt | **~1550 pt (96.9% of width)** |

---

## Typography System

### Font Family
**Alliance No.2** — exclusive Palantir brand typeface (custom, not publicly available)

| Weight | Usage | Frequency |
|--------|-------|-----------|
| **Alliance No.2 Regular** | ~97% of all text | Primary workhorse |
| **Alliance No.2 Medium** | Sparse emphasis | Rare |
| **Alliance No.2 SemiBold** | Minimal | Very rare |
| **Alliance No.1 SemiBold** | Q4 deck only, metric callouts | Accent |
| **Alliance No.1 Medium** | Q4 deck only | Very rare |

### Type Scale (measured from PDF spans)

| Role | Size (pt) | Usage | Frequency |
|------|-----------|-------|-----------|
| **Hero display** | 119–150 pt | Cover/section divider titles ("TITAN dominates") | Rare, impact pages |
| **Section title (large)** | 66 pt | Story headlines ("Rebuilding American Seapower") | Q4 story pages |
| **Page headline** | 52 pt | Statement headlines ("Skip the Debt.") | Story/narrative pages |
| **Section headline** | 39 pt | Financial page titles, key statements | Common on data pages |
| **Sub-headline / body large** | 32.9 pt | "Q1 2025 Highlights" section headers | Section openers |
| **Body / narrative** | 28–35 pt | Supporting body text, quotes | Story pages |
| **Key metric callout** | 60 pt | "+137% Y/Y" large stat numbers | Q4 metric pages |
| **Bullet text** | 22 pt | Highlight bullet items (→ lines) | Very common |
| **Chart data labels** | 20 pt | Data point values on charts | Common |
| **Body / axis labels** | 14–15 pt | Chart labels, axis text, fine detail | Most frequent size |
| **Small body / chart ticks** | 12–13.3 pt | Axis labels, nav text, disclaimers | Very common |
| **Legal / footnotes** | 9–9.9 pt | Copyright, fine print, footnotes | Footer/disclaimer |
| **Chart micro-labels** | 8 pt | Tiny chart annotations | Q4 scatter plots |

### Dominant sizes by span count:
1. **15 pt** (~250 spans) — axis labels, small body
2. **14 pt** (~150 spans) — chart labels
3. **12 pt** (~100 spans) — nav text, disclaimers
4. **22 pt** (~75 spans) — bullet items
5. **13.3 pt** (~70 spans) — secondary labels

---

## Color System

### Q1 2025 Palette

| Color | Hex | Usage | Frequency |
|-------|-----|-------|-----------|
| **Light gray** | `#E0E0E0` | Primary text on dark bg, nav, bullets | ~70% of spans |
| **White** | `#FFFFFF` | Headlines on dark bg, hero text | ~12% |
| **Near-black** | `#212428` | Headlines on light bg, body on light | ~11% |
| **Medium gray** | `#6D6F71` | Secondary text, annotations, muted | ~7% |

### Q4 2025 Palette

| Color | Hex | Usage | Frequency |
|-------|-----|-------|-----------|
| **Light gray** | `#DBDBDB` | Primary text on dark bg | ~66% of spans |
| **White** | `#FFFFFF` | Headlines, hero text | ~12% |
| **Near-black** | `#1D2124` | Headlines/body on light bg | ~11% |
| **Medium gray** | `#626466` | Secondary text, annotations | ~6% |
| **Accent light blue** | `#D3F1FF` | Chart highlight fills | ~3% |
| **Teal accent** | `#39919B` | Special metric callouts | <1% |
| **Neon green accent** | `#00FFAD` | Single standout metric ("PLTR: 127%") | 1 instance |

### Background
- **Dark background:** Near-black (`#1D2124` / `#212428`) — used on ~90% of slide area
- **Light panel:** Light gray (`#E0E0E0` / `#DBDBDB`) — left sidebar or full-page variant
- **Split layout:** ~50/50 light-left / dark-right on financial pages

---

## Layout Patterns

### Pattern 1: Highlights / Bullet List Page
```
┌──────────────────────────────────────────────┐
│ [Q1] [Business Update]          (nav @ 53pt) │
│                                              │
│ Q1 2025 Highlights        (title @ 89pt, 33pt) │
│                                              │
│  → Bullet item 1          (@ 110pt indent, 22pt) │
│  → Bullet item 2          (alternating dark rows) │
│  → Bullet item 3                             │
│  → ...                                       │
│                                              │
│ © 2025 Palantir...         (footer @ 845pt)  │
└──────────────────────────────────────────────┘
```
- Bullet spacing: ~54–58 pt between bullet baselines
- Alternating row backgrounds (subtle dark stripe)

### Pattern 2: Split Financial Page (Text + Chart)
```
┌─────────────────┬────────────────────────────┐
│  LIGHT BG       │  DARK BG                   │
│                 │                             │
│  Statement text │  Chart Title     (39pt)     │
│  (39pt)         │                             │
│                 │  [Chart / Graph]            │
│                 │                             │
│  © + footnotes  │                             │
└─────────────────┴────────────────────────────┘
```
- Split at ~862 pt from left (53.9% of width)
- Left panel: light gray bg with dark text
- Right panel: dark bg with chart + light text
- Chart title at Y ≈ 76 pt

### Pattern 3: Full-bleed Story/Impact Page
```
┌──────────────────────────────────────────────┐
│ [Q1] [Business Update]                       │
│                                              │
│ BIG HEADLINE           (52–66pt, white)      │
│ on 2-4 lines                                 │
│                                              │
│ Supporting body text   (28–35pt)             │
│                                              │
│                          [optional image]     │
│                                              │
│ © 2025 Palantir...                           │
└──────────────────────────────────────────────┘
```
- Full dark background
- Content left-aligned at 50pt
- Text rarely exceeds 40% of slide width (~640pt)
- Massive white space on right (often 50–60% empty)

### Pattern 4: Section Divider
```
┌──────────────────────────────────────────────┐
│ [Q1]                                         │
│                                              │
│              Q1                (124pt hero)   │
│              2025                             │
│              Business Update                  │
│                                              │
└──────────────────────────────────────────────┘
```
- Hero text at 124pt
- Centered or left-aligned at 86pt from left

---

## Navigation System

| Element | Position | Style |
|---------|----------|-------|
| Quarter label ("Q1"/"Q4") | x=62, y=53 | 12pt, pill/rounded rect |
| Section label ("Business Update" / "Financials") | x=96, y=53 | 12pt, same row |
| Combined nav height | ~20pt tall | Minimal, top-left corner |

---

## White Space Analysis

| Metric | Value |
|--------|-------|
| **Top margin to nav** | 53 pt (5.9% of height) |
| **Nav to first content** | 36 pt gap (nav at 53 → content at 89) |
| **Left margin** | 50 pt (3.1% of width) |
| **Right margin (minimum)** | ~50–60 pt (3.1–3.8%) |
| **Bottom margin (to copyright)** | 55 pt (6.1% of height) |
| **Bullet line spacing** | ~54–58 pt between baselines (~2.5× font size) |
| **Story pages: text width** | ~600 pt max (37.5% of slide) |
| **Story pages: empty space** | ~60% of slide area |
| **Financial split: left panel** | 0–862 pt (53.9%) |
| **Financial split: right panel** | 862–1600 pt (46.1%) |

---

## Key Design Principles (Derived)

1. **Extreme restraint:** One typeface family (Alliance No.2), one weight dominates (Regular)
2. **Dark-first:** Near-black backgrounds with light gray/white text — cinematic feel
3. **Massive white space:** Story pages use only 35–40% of slide for text
4. **Clear hierarchy:** 5–6 distinct size tiers (hero → headline → sub → body → label → legal)
5. **Minimal color:** 4-color system (near-black, light gray, white, medium gray) + 1 rare accent
6. **Consistent grid:** Nav always at (62, 53), content always starts at ~50pt left, ~89pt top
7. **No gradients, no shadows, no decorative elements** — pure typography + data
8. **Alternating row stripes** on bullet lists for readability (subtle dark/darker alternation)
9. **Split layouts** for data pages: narrative left, visualization right
10. **Footer locked** at Y=845, copyright + legal footnotes in 9pt gray

---

## Cross-Deck Consistency (Q1 vs Q4 2025)

| Element | Q1 2025 | Q4 2025 | Identical? |
|---------|---------|---------|------------|
| Slide size | 1600×900 | 1600×900 | ✅ |
| Font family | Alliance No.2 | Alliance No.2 + No.1 | ⚠️ Q4 adds No.1 |
| Primary text color | #E0E0E0 | #DBDBDB | ⚠️ Slightly different gray |
| Dark bg color | #212428 | #1D2124 | ⚠️ Slightly different |
| Nav position | (62, 53) | (62, 53) | ✅ |
| Left margin | 50pt | 50pt | ✅ |
| Headline Y | 89pt | 89pt | ✅ |
| Bullet indent | 110pt | 110pt | ✅ |
| Copyright Y | 845pt | 845pt | ✅ |
| Footer left | 48pt | 48pt | ✅ |
| Hero type size | 124pt | 124pt | ✅ |
| Accent colors | None | Teal + Neon green | ⚠️ Q4 bolder |

**Conclusion:** Layout grid is virtually identical. Q4 slightly evolves the palette (warmer darks, adds accent colors, introduces Alliance No.1 for metric emphasis).
