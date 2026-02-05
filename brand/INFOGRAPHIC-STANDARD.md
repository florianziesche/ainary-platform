# Infographic & Graphic Design Standard — Finite Matter

*Version 1.0 — 2026-02-05*
*Sources: 36ZERO Vision Guidelines V1.0, Pentagram/Deloitte Insights, McKinsey/Wolff Olins, WCAG 2.1 AA*

---

## 1. Farben

### Primärpalette

| Rolle | Farbe | Hex | Kontrast auf BG |
|-------|-------|-----|-----------------|
| Hintergrund | Warmes Grau | `#EAEBEF` | — |
| Primärtext | Navy (nie schwarz) | `#1E1E2E` | 14.2:1 ✅ |
| Sekundärtext | Slate | `#64748B` | 4.6:1 ✅ |
| Tertiärtext (Captions) | Muted Slate | `#94A3B8` | 3.0:1 ⚠️ nur nicht-essentiell |
| Akzent | Electric Blue | `#2563EB` | 4.1:1 ✅ bold |
| Dark Panels | Dark Navy | `#1E1E2E` | — |
| Text auf Dark | Off-White | `#F8FAFC` | 14.2:1 ✅ |
| Text auf Dark (sekundär) | Muted Slate | `#94A3B8` | 5.8:1 ✅ |

### Verbotene Farben

| Farbe | Hex | Problem |
|-------|-----|---------|
| Reines Schwarz | `#000000` | Zu hart, kein Agentur-Feeling |
| Reines Weiß als BG | `#FFFFFF` | Zu steril |
| Helles Grau auf hellem BG | `#F1F5F9`, `#CBD5E1` | Unsichtbar (Kontrast <2:1) |
| Gelb auf Weiß | `#EAB308` | WCAG 1.9:1 ❌ |

### Regel
**Nichts heller als #94A3B8 auf hellem Hintergrund als Text.**

---

## 2. Typografie

### Font-Familie
**Inter** — Primär und einzige Schrift (vorerst)

### Größen-Skala (für 1100px-breite Infografiken)

| Element | Größe | Weight | Tracking | Farbe |
|---------|-------|--------|----------|-------|
| Title | 36px | 900 | -1px | #1E1E2E |
| Subtitle | 16px | 400 | normal | #64748B |
| Overline | 12px | 700 | 3px | #2563EB |
| Section Label | 11-12px | 700 | 2-2.5px | #94A3B8 |
| Body / Description | 14-15px | 400-500 | normal | #64748B |
| Agent/Item Name | 16-18px | 700-800 | normal | #1E1E2E |
| Metric / KPI | 14px | 600-700 | normal | #2563EB |
| Stat Hero | 40-56px | 900 | -1px | Variabel |
| Source / Brand | 11px | 700 | 1.5px | #94A3B8 |

### Minimum-Größen
- **Body Text:** nie unter 14px
- **Captions/Brand:** nie unter 10px (11px bevorzugt)
- **Overlines:** nie unter 11px (mit 700 weight + uppercase + tracking)

---

## 3. Grafische Elemente

### Erlaubt (diskret, professionell)

| Element | CSS | Zweck |
|---------|-----|-------|
| Accent Bar (3-4px) | `border-left: 4px solid #2563EB` | Key Insight markieren |
| Top-Border Accent | `::before { height: 3px; background: color }` | Karten-Hierarchie |
| Connector Dots (6px) | `width:6px; height:6px; border-radius:50%` | "Look here" Signal |
| Connector Line (2px) | `width:2px; background: gradient` | Flow/Sequenz zeigen |
| Section Dots | Farbige Kreise vor Section Labels | Kategorien unterscheiden |
| Verdict Dots | Kleine Dots neben Bewertungen | Status-Indikator |
| Numbered Circles | `48px circle, 2px border, 18px number` | Sequenz-Schritte |
| Dark Panel | `#1E1E2E mit 12px border-radius` | Abschluss-Statement |

### Verboten

| Element | Warum |
|---------|-------|
| Emojis | Amateur |
| Bunte Hintergründe pro Karte | Unruhig |
| Drop Shadows | Überflüssig bei flachem Design |
| Gradient-Hintergründe auf Karten | Nur für Lines/Accents |
| Mehr als 2 grafische Elemente pro Sektion | Überladung |

### Regel
**Jedes grafische Element muss einen Zweck haben. Dekoration = Amateur.**

---

## 4. Layout

### Canvas-Größen

| Typ | Breite | Höhe | Render-Scale |
|-----|--------|------|-------------|
| Inline Infographic | 1100px | 700-920px | 2x (Retina) |
| Thumbnail / OG | 1200px | 630px | 2x |

### Render-Befehl
```bash
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome \
  --headless --disable-gpu \
  --force-device-scale-factor=2 \
  --screenshot="output.png" \
  --window-size=1200,950 \
  "file://$(pwd)/source.html"
```

### Grid-Prinzipien
- Heading-Block oben: Overline → Title → Subtitle (44-48px margin-bottom)
- Content-Bereich: 920-940px breit (80px padding je Seite)
- Bottom-Bar: 2px solid #1E1E2E border-top, 20px padding-top
- Zwischen Sektionen: 1px solid #E2E8F0 oder #D5D6DA

---

## 5. Branding-Regeln

### Positionierung
- Florian = **Experte, Entdecker, Lehrer**
- Nie: Case Study des Scheiterns, Opfer, Amateur
- **Jede Grafik muss standalone teilbar sein** — wer nur das Bild sieht muss denken: "Von dem will ich lernen"

### Konkret:
- Keine negativen persönlichen Zahlen (0 shipped, fail-ratios)
- Universelle Insights statt persönliche Geständnisse
- Authority Stats: Immer positive Metriken (10 agents, $250/mo, 15-20h saved, 40% quality)
- "FINITE MATTER" als Brand Mark auf jeder Grafik (bottom-right, 11px, uppercase, #94A3B8)

---

## 6. Qualitäts-Checkliste (vor Delivery)

- [ ] Kein Text unter 14px (außer Brand/Source)
- [ ] Kein Text unter #94A3B8 auf hellem Hintergrund
- [ ] Hintergrund ist #EAEBEF, nie #FFFFFF
- [ ] Text ist #1E1E2E, nie #000000
- [ ] Max 2 grafische Elemente pro Sektion
- [ ] Keine Emojis
- [ ] "FINITE MATTER" Brand Mark vorhanden
- [ ] Positives Branding (kein Self-Exposure)
- [ ] 2x Retina gerendert
- [ ] Gesamter Content im Viewport sichtbar
- [ ] Connector-Linien pixel-perfekt zentriert
- [ ] Alle Elemente am Grid ausgerichtet

---

## 7. Cross-References

- `brand/36ZERO-GUIDELINES-ANALYSIS.md` — Source of Truth für Agentur-Qualität
- `agents/DESIGN-SYSTEM.md` — Allgemeines Design System
- `skills/research/SKILL.md` → Appendix: Typography Standards
- `brand/BRAND-GUIDE.md` — Gesamte Brand Identity

---

*Review nach 10 Grafiken mit diesem Standard. Dann messen und updaten.*
*Erstellt: 2026-02-05 02:10 CET*
