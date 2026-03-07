# SOCIAL-MEDIA-DESIGN.md — Visual Content Standard
*Created: 2026-03-07 | Source: [[linkedin-carousel-design-research]]*

## Canvas Sizes

| Platform | Aspect Ratio | Pixels | Status |
|----------|-------------|--------|--------|
| **LinkedIn Carousel** | **4:5 (Portrait)** | **1080 × 1350** | ✅ Gold Standard |
| LinkedIn Carousel | 1:1 (Square) | 1080 × 1080 | ⚠️ Acceptable, 35% less screen |
| LinkedIn Carousel | 16:9 (Landscape) | 1920 × 1080 | ❌ Ineffective on mobile |

**Quelle:** UseVisuals (2026): "The most effective linkedin carousel aspect ratio is 4:5. This vertical format is the standard for mobile-first viewing. It fills the majority of a smartphone screen."
→ https://usevisuals.com/blog/ideal-linkedin-carousel-aspect-ratio-for-mobile

**Warum 4:5:** LinkedIn Mobile = ~90% der Views. 4:5 nimmt 35% mehr vertikalen Screen ein als 1:1 → stärkerer Scroll-Stop → höherer Dwell Time → besseres Engagement.

---

## Font Size Minimum (auf 1080px breitem Canvas)

Die zentrale Frage: **Was ist bei ~375px Viewport (iPhone/Android) noch lesbar?**
Faktor: 1080px / 375px = **2.88× Downscale**.

| Element | Minimum (1080px Canvas) | Effektiv @375px | Quelle |
|---------|------------------------|-----------------|--------|
| **Headlines** | **60px** (ideal: 72-80px) | ~21-28px | UseVisuals (2026) |
| **Body Text** | **36px** (ideal: 30-36px) | ~10-12px | UseVisuals + Lumeo (2026) |
| **Labels / Captions** | **24px** | ~8px | Lumeo (2026): "at least 24pt" |
| **Micro-Labels** | **22px** (absolute Untergrenze) | ~7-8px | Eigene Audit (2026-03-07) |
| **Dekorative Elemente** | Keine Mindestgröße | — | Eigene Analyse |

**Quellen:**
- **UseVisuals (2026):** "Headlines: Use a minimum of 60pt font size (based on a 1080px wide canvas)."
  → https://usevisuals.com/blog/ideal-linkedin-carousel-aspect-ratio-for-mobile
- **Lumeo (2026):** "at least 24pt font size for readability"
  → https://www.lumeo.me/en/blog/linkedin-carousel-size-2026
- **Eigene Audit (2026-03-07):** Vision Model auf exportierte PNGs bei simulierter 375px Viewport. Alles unter 22px auf 1080px Canvas = unleserlich auf Mobile. Stat-Labels bei 9px = "physisch unmöglich zu lesen".

**Warum diese Grenzwerte:**
WCAG/Accessibility-Minimum für Body-Text auf Mobile = **11-12px gerendert**. Bei 2.88× Downscale brauchen wir also ≥32px im Source. Alles darunter fällt unter die Wahrnehmungsschwelle — der Nutzer sieht *etwas*, kann es aber nicht *lesen*.

---

## Readability Checklist (vor jedem Export)

1. [ ] Canvas = 1080 × 1350 (4:5)?
2. [ ] Headlines ≥ 60px?
3. [ ] Body ≥ 30px?
4. [ ] Labels ≥ 22px?
5. [ ] **Vision Model Audit** auf exportierte PNGs (375px Simulation)?
6. [ ] Kontrast: Heller Text auf Dunkel ≥ .35 Opacity? Dunkler Text auf Hell ≥ .4 Opacity?
7. [ ] Lange Labels wie "PREDICTIONS" passen in ihre Container?

---

## Engagement-Daten (Stand März 2026)

| Format | Engagement Rate | Quelle |
|--------|----------------|--------|
| **Carousel** | **6.6%** | GrowLeads (2026) |
| Single Image | 4.85% | GrowLeads (2026) |
| Text-only | ~4% | GrowLeads (2026) |
| Video | ~3.5% | GrowLeads (2026) |
| Eigene Erfahrung (Carousel) | 0.69% (bei ~700 Followern) | Ainary LinkedIn Analytics |

**Warum Carousel > Text:** Swipe-Interaktion = aktives Engagement. Jeder Swipe = Signal an den Algorithmus. Carousel-Posts mit ≥3 Slides bekommen signifikant mehr Dwell Time (UseVisuals, Reddit r/AskMarketing).

---

## Design-Prinzipien (Research-basiert)

### Typografie als Design-Element
- **Giant Type** (80-120px) für Hooks — wird zum visuellen Anker, nicht nur Text
- **Ghost Numbers** (120px+, 5-8% Opacity) als Data-as-Design Layer
- Quelle: Linear Brand Guidelines ("reduced visual noise, bold typography")

### Farb-Hierarchie: 60-30-10
- **60%** Hintergrund (dominant)
- **30%** Text-Hierarchie (sekundär)
- **10%** Accent (Gold, CTAs, Icons)
- Quelle: HakunaMatata/IxDF (2026), Jacob Tyler Color Psychology

### Graph/Network als visuelles Element
- **Dekorative Node-Labels:** 8-10px OK — erzeugen Authentizität subliminal
- **Informative Labels:** ≥22px — müssen gelesen werden können
- Glow-Halos proportional zu Node-Wichtigkeit
- Quelle: Palantir Blueprint ("Show Don't Tell"), eigene Audit

### Information Gap (Loewenstein 1994)
- "?" Icons und offene Elemente ("Wildcard", "Surprise me") triggern Curiosity
- Graph zeigt genug zum Verstehen, zu wenig zum vollständigen Lesen → Gap → Comment
- Quelle: Loewenstein, G. (1994). "The psychology of curiosity: A review and reinterpretation." Psychological Bulletin, 116(1), 75-98.

---

## Anti-Patterns (gelernt 2026-03-07)

| Anti-Pattern | Problem | Fix |
|-------------|---------|-----|
| Body bei 17px auf 1080 Canvas | 6px auf Mobile = unter WCAG | ≥30px |
| Stat-Labels bei 9px | Zahlen ohne Label = meaningless | ≥22px |
| Brand-Header bei 12px + .15 Opacity | Unsichtbar = verschwendete Pixel | ≥20px + .22 Opacity, oder weglassen |
| 1:1 Aspect Ratio | 35% weniger Screen auf Mobile | 4:5 verwenden |
| 5-Column Stat Row ohne Size-Check | "PREDICTIONS" klemmt | Labels auf Länge prüfen, ggf. abkürzen |

---

## Quellenverzeichnis

| # | Quelle | URL | Typ | Datum |
|---|--------|-----|-----|-------|
| 1 | UseVisuals — LinkedIn Carousel Aspect Ratio | https://usevisuals.com/blog/ideal-linkedin-carousel-aspect-ratio-for-mobile | Fachquelle | 2026 |
| 2 | Lumeo — LinkedIn Carousel Size Guide | https://www.lumeo.me/en/blog/linkedin-carousel-size-2026 | Fachquelle | 2026 |
| 3 | GrowLeads — LinkedIn Engagement Rates | https://growleads.io (via Research 2026-03-07) | Fachquelle | 2026 |
| 4 | Linear Brand Guidelines | https://linear.app/brand | Primärquelle | — |
| 5 | Palantir Blueprint | https://blog.palantir.com | Primärquelle | — |
| 6 | Jacob Tyler — Color Psychology | https://jacobtyler.com/color-psychology | Fachquelle | 2025 |
| 7 | HakunaMatata — 60-30-10 Rule | https://hakunamatata.in (via Research 2026-03-07) | Fachquelle | 2026 |
| 8 | Loewenstein — Information Gap Theory | DOI: 10.1037/0033-2909.116.1.75 | Wissenschaftlich | 1994 |
| 9 | Eigene Audit — Vision Model + Mobile Sim | Intern (2026-03-07, V3→V4→V5 Iteration) | CORE | 2026-03-07 |

---

*Trigger Map: Task enthält "LinkedIn", "Carousel", "Social Media", "Slide", "Visual Content" → diesen Standard laden.*
