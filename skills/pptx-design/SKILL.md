# SKILL: python-pptx Presentation Design

**Zweck:** Professionelle PowerPoint-Decks mit python-pptx. Agentur-Level. Keine hässlichen Grafiken.

---

## Slide Dimensions (16:9)

```
Width:  13.333 inches (33.867 cm)
Height:  7.500 inches (19.050 cm)
```

## Grid System

```
Safe Area (Margins):
  Left:   0.8 inches (2.03 cm)
  Right:  0.8 inches
  Top:    1.0 inches (inkl. Slide-Titel)
  Bottom: 0.6 inches (Slide-Nummer, Footer)

Content Area:
  Width:  11.733 inches (13.333 - 2×0.8)
  Height:  5.900 inches (7.5 - 1.0 - 0.6)
```

## Element Proportions — KRITISCH

### Minimum Sizes (alles in Inches)

| Element | Min Width | Min Height | Empfohlen |
|---------|-----------|------------|-----------|
| Shape/Box | 1.5 | 0.8 | 2.0+ × 1.0+ |
| Arrow (connector) | 1.0 lang | 0.15 dick | 1.5+ × 0.2 |
| Arrow (shape) | 1.5 | 0.6 | 2.0 × 0.8 |
| Icon-Placeholder | 0.5 × 0.5 | — | 0.6 × 0.6 |
| Stat-Card | 2.5 | 1.5 | 3.0 × 1.8 |
| Process-Step Box | 2.0 | 1.2 | 2.5 × 1.5 |
| Bar (horizontal) | 2.0 | 0.35 | Proportional zu Wert |
| Circle badge | 0.7 × 0.7 | — | 0.8 × 0.8 |

### REGEL: Verhältnis Pfeil zu Box

```
Pfeil-Länge  >= 40% der Box-Breite
Pfeil-Dicke  >= 15% der Box-Höhe
Abstand Pfeil ↔ Box >= 0.15 inches

FALSCH:  [████████████]→[████████████]   (Pfeil zu klein)
RICHTIG: [████████████] ══▶ [████████████]  (Pfeil prominent)
```

### REGEL: Abstand zwischen Elementen

```
Minimum Gap:    0.2 inches (0.5 cm)
Standard Gap:   0.3 inches (0.76 cm)
Section Gap:    0.5 inches (1.27 cm)

Nie zwei Shapes direkt aneinander ohne Gap.
```

## Typography

```python
# Slide Title
font.size = Pt(28)    # Minimum 24, Maximum 32
font.bold = True
font.color.rgb = RGBColor(10, 15, 30)  # #0A0F1E

# Subtitle / Section Header
font.size = Pt(20)
font.bold = True

# Body Text
font.size = Pt(14)    # Minimum 12, Maximum 16
font.color.rgb = RGBColor(55, 65, 81)   # #374151

# Stat Number (große Zahlen)
font.size = Pt(36)    # Minimum 28, Maximum 48
font.bold = True
font.color.rgb = RGBColor(37, 99, 235)  # Primary Blue

# Caption / Source
font.size = Pt(10)
font.color.rgb = RGBColor(100, 116, 139)  # Midgray

# Slide Number
font.size = Pt(10)
```

## Color System

```python
COLORS = {
    'dark':      RGBColor(10, 15, 30),      # #0A0F1E - Hintergrund dunkel
    'primary':   RGBColor(37, 99, 235),      # #2563EB - Akzent
    'accent':    RGBColor(96, 165, 250),     # #60A5FA - Sekundär
    'white':     RGBColor(255, 255, 255),
    'light_bg':  RGBColor(241, 245, 249),    # #F1F5F9 - Heller Hintergrund
    'text_dark': RGBColor(55, 65, 81),       # #374151
    'text_mid':  RGBColor(100, 116, 139),    # #64748B
    'green':     RGBColor(21, 128, 61),      # #15803D
    'red':       RGBColor(185, 28, 28),      # #B91C1C
    'yellow':    RGBColor(234, 179, 8),      # #EAB308
}
```

## Layout Patterns

### Pattern 1: Stat Cards (3er oder 4er Reihe)

```python
# 3 Stat Cards nebeneinander
card_width = Inches(3.5)
card_height = Inches(1.8)
gap = Inches(0.35)
start_x = Inches(0.8)
start_y = Inches(2.0)

for i in range(3):
    x = start_x + i * (card_width + gap)
    # Hintergrund-Rechteck
    shape = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, x, start_y, 
        card_width, card_height
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = COLORS['light_bg']
    shape.line.fill.background()  # Kein Rahmen
```

### Pattern 2: Process Flow (Pfeile zwischen Boxen)

```python
# 4 Schritte mit Pfeilen
n_steps = 4
box_w = Inches(2.2)
box_h = Inches(1.4)
arrow_w = Inches(0.8)   # MINDESTENS 0.8!
arrow_h = Inches(0.4)   # MINDESTENS 0.3!
gap = Inches(0.15)

total = n_steps * box_w + (n_steps-1) * (arrow_w + 2*gap)
start_x = (Inches(13.333) - total) / 2  # Zentrieren

for i in range(n_steps):
    x = start_x + i * (box_w + arrow_w + 2*gap)
    y = Inches(3.0)
    
    # Box
    box = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, x, y, box_w, box_h
    )
    
    # Pfeil (NUR zwischen Boxen, nicht nach letzter)
    if i < n_steps - 1:
        ax = x + box_w + gap
        ay = y + box_h/2 - arrow_h/2
        arrow = slide.shapes.add_shape(
            MSO_SHAPE.RIGHT_ARROW, ax, ay, arrow_w, arrow_h
        )
        arrow.fill.solid()
        arrow.fill.fore_color.rgb = COLORS['primary']
        arrow.line.fill.background()
```

### Pattern 3: Two-Column Layout

```python
col_w = Inches(5.5)
gap = Inches(0.7)
left_x = Inches(0.8)
right_x = left_x + col_w + gap
```

### Pattern 4: Dark Section Slide (Trennslide)

```python
bg = slide.background
fill = bg.fill
fill.solid()
fill.fore_color.rgb = COLORS['dark']

# Alle Texte in Weiß!
```

### Pattern 5: Horizontal Bars (Vergleich/Ranking)

```python
max_bar_w = Inches(8.0)
bar_h = Inches(0.4)      # MINDESTENS 0.35!
bar_gap = Inches(0.25)

for i, (label, value, max_val) in enumerate(data):
    y = Inches(2.0) + i * (bar_h + bar_gap)
    w = max_bar_w * (value / max_val)
    
    bar = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE,
        Inches(3.5), y, w, bar_h
    )
```

## Pre-Flight Checklist

Vor jedem `prs.save()`:

- [ ] Alle Shapes innerhalb Safe Area (0.8" Rand)?
- [ ] Kein Element kleiner als Minimum Size?
- [ ] Pfeile proportional zu umgebenden Boxen (≥40% Breite)?
- [ ] Abstände zwischen Elementen ≥0.2"?
- [ ] Font Sizes: Titel ≥24pt, Body ≥12pt, Stat-Numbers ≥28pt?
- [ ] Farben aus dem Color System (keine Freestyle-Farben)?
- [ ] Slide-Nummern auf allen Slides (außer Title)?
- [ ] Dark Slides: Alle Texte in Weiß?
- [ ] Kein Text abgeschnitten (word_wrap=True bei TextFrames)?
- [ ] Maximal 6 Zeilen Text pro Body-Element?

## Anti-Patterns — VERBOTEN

```
❌ Pfeile kleiner als 0.8" Länge oder 0.3" Höhe
❌ Shapes die den Safe Area Rand berühren
❌ Mehr als 7 Elemente auf einem Slide
❌ Font Size < 10pt (außer Quellenangaben)
❌ Gradient Fills (sehen in Export hässlich aus)
❌ Schatten auf Shapes (wirken amateurhaft)
❌ Mehr als 3 Farben pro Slide (+ Schwarz/Weiß)
❌ Text direkt auf Dark Background ohne Box/Padding
❌ Shapes ohne word_wrap (Text läuft über Rand)
```

## Code Template

```python
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)

# Leeres Layout (immer Blank verwenden!)
blank_layout = prs.slide_layouts[6]

def add_text_to_shape(shape, text, size=14, bold=False, 
                      color=RGBColor(55,65,81), align=PP_ALIGN.LEFT):
    """Helper: Text in Shape einfügen."""
    tf = shape.text_frame
    tf.word_wrap = True  # IMMER!
    tf.auto_size = None
    p = tf.paragraphs[0]
    p.text = text
    p.font.size = Pt(size)
    p.font.bold = bold
    p.font.color.rgb = color
    p.alignment = align

def add_slide_number(slide, num, total=None):
    """Slide-Nummer unten rechts."""
    txt = f"{num}" if not total else f"{num}/{total}"
    txBox = slide.shapes.add_textbox(
        Inches(12.2), Inches(7.05), Inches(0.8), Inches(0.3)
    )
    add_text_to_shape(txBox, txt, size=10, 
                      color=RGBColor(100,116,139), 
                      align=PP_ALIGN.RIGHT)

# ... Slides bauen ...

prs.save('output.pptx')
```

## Qualitätskontrolle

Nach dem Erstellen:
1. Datei mit `open` in PowerPoint öffnen
2. Visuell prüfen (Screenshot wenn möglich)
3. Bei Problemen: Koordinaten anpassen, NIE Minimum Sizes unterschreiten

---

*Erstellt: 2026-02-06 auf Basis von McKinsey/BCG Design Principles + python-pptx Docs*
*Bei Problemen: Dieses File updaten, nicht ignorieren.*
