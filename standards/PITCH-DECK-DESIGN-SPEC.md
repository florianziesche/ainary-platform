# PITCH-DECK-DESIGN-SPEC.md — McKinsey-Grade HTML Deck Rules

## Anatomie einer Folie (McKinsey Standard)
Jede Folie hat EXAKT 3 Elemente:
1. **Action Title** (oben) — KEIN passiver Titel. Stattdessen das KEY TAKEAWAY als Satz.
   - FALSCH: "Herausforderungen"
   - RICHTIG: "Kleine Gemeinden verlieren den Anschluss — weil ihnen die Kapazität fehlt"
   - Max 2 Zeilen, größere Schrift als Body
2. **Body** (mitte) — Daten/Visualisierung die den Action Title BEWEISEN
   - Charts, Tabellen, KPIs, Vergleiche
   - Nichts im Body was nicht zum Title gehört
3. **So What / Source** (unten) — Quelle + "Was bedeutet das?"
   - Klein, dezent, aber vorhanden

## 5 Design-Prinzipien (aus 300+ Consulting Decks)

### 1. Alignment
- ALLES auf unsichtbarem Grid ausgerichtet
- Feste Margins: links 80px, rechts 80px, oben 60px, unten 60px
- Alle Elemente snappen ans gleiche Grid
- Wenn ein Element 2px daneben ist, sieht es amateurhaft aus

### 2. Contrast
- Dunkler Text auf hellem Hintergrund (cream #faf8f4)
- Key Numbers in Accent-Farbe (#c8aa50 Gold)
- Test: Kann man den Titel aus 3m Entfernung lesen?
- Hierarchie durch Größe UND Gewicht, nicht durch Farbe allein

### 3. Whitespace
- Mindestens 15-20% der Folie ist LEER
- Weite Margins, Platz zwischen Bullet Points
- Weniger Elemente pro Folie = professioneller
- Crowded = amateurhaft

### 4. Consistency
- GLEICHE Schrift überall (Inter 300-600 + JetBrains Mono)
- GLEICHE Margins auf jeder Folie
- GLEICHE Farben (max 3: Text, Accent, Muted)
- GLEICHE Heading-Größen

### 5. Visual Hierarchy
- Title: 1.5-2rem, font-weight 600
- Subtitle/Subheading: 0.85rem, font-weight 500, muted color
- Body: 0.8-0.9rem, regular weight
- Labels: 0.6rem, JetBrains Mono, uppercase, letter-spacing
- Wenn alles gleich groß ist, sticht NICHTS hervor

## Präsentations-Struktur (Consulting Standard)
1. **Frontpage** — Titel (<8 Wörter), Subtitle, Name, Datum
2. **Executive Summary / Situation** — SCR Framework (Situation → Complication → Resolution)
3. **Body Slides** — Jede mit Action Title + Evidence
4. **Recommendation / Next Steps**
5. **Appendix** (optional)

## Adaptiert für BM-Pitch (10 Slides, nicht 50)
1. **Cover** — "KI-Assistenz für Ihre Gemeinde" + Name + Datum
2. **Situation** — Action Title: "6.414 Einwohner, 85 Mitarbeiter, 16 Ortsteile — Glashuette ist typisch"
3. **Complication** — Action Title: "Die Anforderungen steigen, die Ressourcen nicht"
4. **Demo** — Action Title: "In 3 Minuten hat das System 5 Förderprogramme für Glashuette gefunden"
5. **Ergebnisse** — Action Title: "Was Monate dauert, dauert jetzt Minuten"
6. **Vorher/Nachher** — Visuelle Progress Bars
7. **Über mich** — Credentials
8. **Close** — "Wollen wir es ausprobieren?"

## CSS-Spezifika für HTML-Deck

### Typography
```css
--f: 'Inter', -apple-system, sans-serif;
--m: 'JetBrains Mono', monospace;
/* NO font-weight 700. Max 600. */
```

### Farben
```css
--bg: #faf8f4;        /* Cream background */
--surface: #ffffff;    /* Cards */
--s2: #f2efe8;         /* Secondary surface */
--text: #1a1a1a;       /* Primary text */
--t2: #4a4a4a;         /* Secondary text */
--t3: #7a7a7a;         /* Muted text */
--t4: #a0a0a0;         /* Labels */
--accent: #c8aa50;     /* Gold accent — numbers, highlights */
--accent-bg: rgba(200,170,80,0.08);  /* Accent background */
--green: #1a6b3c;      /* Positive/improvement */
--brd: rgba(0,0,0,0.08);  /* Borders */
```

### Spacing System (8px base)
```
8px  = xs
16px = sm  
24px = md
32px = lg
48px = xl
64px = 2xl
80px = 3xl (slide padding)
```

### Grid
- Slide padding: 80px horizontal, 60px vertical
- Mobile: 24px horizontal, 32px vertical
- Content max-width: 1000px, centered
- 2-column grid gap: 48-64px
- 3-column grid gap: 24px

### Visuelle Elemente (Linear-inspiriert, NICHT overdone)
- Subtiler radialer Gradient hinter Key Numbers: `radial-gradient(ellipse, rgba(200,170,80,0.12) 0%, transparent 70%)`
- Box shadows: `0 1px 3px rgba(0,0,0,0.04), 0 4px 24px rgba(0,0,0,0.06)`
- Border-radius: 8-12px für Cards
- Animations: `opacity 0→1, translateY 16px→0, 0.6s ease-out, staggered 80ms`
- Progress bars für Vergleiche statt Text-Tabellen
- Dot-grid Background (optional, sehr subtil): `radial-gradient(circle, rgba(0,0,0,0.03) 1px, transparent 1px) / 24px 24px`

### Action Title Format
```css
.action-title {
  font-size: 1.5rem;
  font-weight: 600;
  letter-spacing: -0.03em;
  line-height: 1.25;
  color: var(--text);
  max-width: 700px;
}
```

### Label Format (Slide-Nummer/Kategorie)
```css
.label {
  font-family: var(--m);
  font-size: 0.55rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--t4);
}
```

### KPI Card Format
```css
.kpi {
  text-align: center;
  padding: 24px;
  background: var(--surface);
  border: 1px solid var(--brd);
  border-radius: 10px;
  position: relative;  /* für Glow */
}
.kpi::before {  /* Subtiler Glow */
  content: '';
  position: absolute;
  inset: -20px;
  background: radial-gradient(ellipse, rgba(200,170,80,0.1) 0%, transparent 70%);
  z-index: -1;
}
.kpi-value {
  font-size: 2rem;
  font-weight: 600;
  color: var(--accent);
}
.kpi-label {
  font-size: 0.7rem;
  color: var(--t3);
  margin-top: 4px;
}
```

## Anti-Patterns (VERMEIDEN)
- ❌ Mehr als 1 Kernbotschaft pro Folie
- ❌ Passive Titel ("Herausforderungen", "Lösung", "Über uns")
- ❌ Text-Wände ohne visuelle Auflockerung
- ❌ Uneinheitliche Margins/Fonts/Farben
- ❌ Konfuse Diagramme die nicht sofort verständlich sind
- ❌ McKinsey/BCG explizit erwähnen ("McKinsey-Grade")
- ❌ Pricing oder konkrete Kosten
- ❌ Überladene Folien — im Zweifel WENIGER
- ❌ AI-generierte Bilder als Füller
- ❌ font-weight: 700 bei Inter
