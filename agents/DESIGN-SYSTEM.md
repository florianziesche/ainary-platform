# Design System — Mia's Visual Design Rules

*Codifizierte Design-Regeln für alle visuellen Outputs. Lesen vor JEDEM Grafik/HTML-Output.*

---

## Das Grundproblem

Mia (AI) kann Code schreiben, aber Design ist ein SKILL, kein Feature. Bisherige Fehler:
- Substack Banner: Zu viele Elemente, kein Fokus, schlechte Typografie
- Präsentationen: Whitespace komprimiert, Titel redundant mit Content
- OG Images: Generisch, kein Wiedererkennungswert
- Landing Page: Inkonsistente Abstände, kaputte HTML-Tags

**Root Cause:** Design wird als "mach es hübsch" behandelt statt als System mit Regeln.

---

## Die 10 Unverhandelbaren Regeln

### 1. WENIGER IST IMMER MEHR
- Jedes Element muss seinen Platz verdienen
- Frage: "Was kann ich ENTFERNEN?" nicht "Was kann ich HINZUFÜGEN?"
- Wenn ein Slide/Grafik mehr als 5 Elemente hat → zu viel

### 2. WHITESPACE IST DESIGN
- Minimum 20% der Fläche ist leer
- Padding: Lieber zu viel als zu wenig
- Nie Margins komprimieren um "mehr reinzubekommen"
- **Konkret:** padding min 40px, gap min 24px, section-margin min 80px

### 3. EINE SCHRIFTART, ZWEI GEWICHTE
- Font: **Space Grotesk** (Brand) oder **Inter** (UI)
- Gewichte: Bold (700) für Headlines, Regular (400) für Body
- KEINE dritte Schrift. NIE.
- Max 3 Font-Größen pro Grafik (Title, Body, Caption)

### 4. FARBE MIT ABSICHT
- Aus Brand Guide: Navy #1e3a5f + Electric Blue #2563eb + White #ffffff
- 60-30-10 Regel: 60% neutral, 30% primary, 10% accent
- Maximal 3 Farben pro Grafik
- **Keine Gradients** außer in Hero-Bereichen

### 5. ALIGNMENT IST NICHT OPTIONAL
- Alles an einem Grid ausrichten
- Linksbündig ist Standard (nicht zentriert, außer bei einzelnen Headlines)
- Alle Elemente einer Gruppe haben gleichen Abstand
- Wenn 3 Karten: gleiche Höhe, gleicher Abstand, gleiche Padding

### 6. KONTRAST STATT DEKORATION
- Text auf Hintergrund: Minimum 4.5:1 Kontrast
- Kein heller Text auf hellem Hintergrund
- Kein dunkelgrau auf dunkelblau
- Wichtig = Größer + Dunkler, nicht Wichtig = Kleiner + Heller

### 7. KEINE STOCK-DESIGN-MUSTER
- Keine generischen Icons wenn Text reicht
- Keine Schatten-Orgien (max 1 subtle shadow)
- Keine Rounded-Corner-Exzesse (border-radius: 8px oder 12px, fertig)
- Keine Emoji als Design-Elemente in professionellen Grafiken

### 8. RESPONSIVE FIRST
- Mobile zuerst denken (375px Breite)
- Text min 16px auf Mobile
- Touch Targets min 44px
- Bilder max-width: 100%

### 9. JEDE GRAFIK HAT EIN ZIEL
- Was soll der Betrachter TUN nach dem Ansehen?
- Ein Grafik-Element = Eine Message
- Kein "und außerdem noch..."

### 10. TESTEN VOR LIEFERN
- In Browser öffnen und anschauen
- Auf Mobile-Viewport checken (375px)
- Screenshot machen und als Bild betrachten (nicht als Code)
- "Würde das auf einer McKinsey-Slide bestehen?"

---

## Grafik-Typen & Spezifikationen

### LinkedIn Post Image
- **Size:** 1080 × 1080px (Square) oder 1080 × 1350px (Portrait — nimmt mehr Feed-Platz)
- **Safe Zone:** 60px Padding rundrum
- **Text:** Max 6 Wörter Headline, max 15 Wörter Body
- **Font:** Title 48-64px bold, Body 24-32px regular
- **Background:** Solid color oder minimal gradient
- **Branding:** Name + Title dezent unten rechts

**Template CSS:**
```css
.linkedin-graphic {
    width: 1080px;
    height: 1350px; /* Portrait für max Feed-Platz */
    padding: 80px;
    font-family: 'Space Grotesk', sans-serif;
    background: #0f172a;
    color: #ffffff;
    display: flex;
    flex-direction: column;
    justify-content: center;
}
.linkedin-graphic h1 {
    font-size: 64px;
    font-weight: 700;
    line-height: 1.1;
    margin-bottom: 32px;
}
.linkedin-graphic p {
    font-size: 28px;
    font-weight: 400;
    color: #94a3b8;
    line-height: 1.5;
}
.linkedin-graphic .accent {
    color: #2563eb;
}
.linkedin-graphic .branding {
    margin-top: auto;
    font-size: 20px;
    color: #64748b;
}
```

### Twitter/X Image
- **Size:** 1200 × 675px (16:9) oder 1080 × 1080px
- **Text:** Weniger als LinkedIn — Bild ergänzt Tweet
- **Style:** Bold, eine Zahl oder Statement

### Substack Header/Banner
- **Size:** 1456 × 180px (Newsletter banner) oder 1100 × 110px
- **Cover Image:** 1100 × 550px
- **Style:** Clean, minimal, Brand-Farben
- **KEINE Fotos** — geometrisch, typografisch

### OG Image (Website)
- **Size:** 1200 × 630px
- **Must have:** Logo/Brand, Titel, URL
- **Background:** Brand-Farbe, nicht generisch

### Presentation Slides
- **Size:** 1920 × 1080px (16:9)
- **Padding:** 120px seitlich, 80px oben/unten
- **Max Elemente pro Slide:** 1 Headline + 1 Visual OR 1 Headline + 3-4 Bullet Points
- **TITEL ≠ CONTENT** — Titel fasst zusammen, Content liefert Details
- **Kein Slide mit mehr als 50 Wörtern**

---

## Design-Entscheidungsbaum

```
Brauche ich eine Grafik?
├── Nein → Nur Text-Post (performt auf LinkedIn oft besser!)
└── Ja → Was für eine?
    ├── Daten/Statistik → Chart/Diagramm
    │   └── Simple bar/line, max 5 Datenpunkte, Brand-Farben
    ├── Framework/Konzept → Diagram
    │   └── Boxes + Arrows, max 4 Elemente, viel Whitespace
    ├── Quote/Statement → Text-Grafik
    │   └── Bold Headline + Author, Dark BG, 3 Elemente max
    ├── Vergleich → Split-Screen
    │   └── Links vs Rechts, max 4 Punkte pro Seite
    └── Tutorial/How-To → Screenshot oder Step-Grafik
        └── Nummern + kurze Labels, vertical flow
```

---

## Reusable CSS Components

### Card
```css
.card {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    padding: 32px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
}
```

### Stat Block
```css
.stat {
    text-align: center;
}
.stat-number {
    font-size: 48px;
    font-weight: 700;
    color: #2563eb;
}
.stat-label {
    font-size: 16px;
    color: #64748b;
    margin-top: 4px;
}
```

### Badge
```css
.badge {
    display: inline-block;
    padding: 4px 12px;
    background: #eff6ff;
    color: #2563eb;
    border-radius: 20px;
    font-size: 14px;
    font-weight: 600;
}
```

### Button (Primary)
```css
.btn-primary {
    display: inline-block;
    padding: 14px 28px;
    background: #2563eb;
    color: #ffffff;
    border: none;
    border-radius: 8px;
    font-family: 'Space Grotesk', sans-serif;
    font-size: 16px;
    font-weight: 600;
    cursor: pointer;
    transition: background 0.2s;
}
.btn-primary:hover {
    background: #1d4ed8;
}
```

---

## Deliberate Practice Plan

### Wöchentlich
1. **1 McKinsey/BCG Slide analysieren** — Was macht es gut? Layout, Farben, Whitespace
2. **1 Top-Performer LinkedIn Grafik nachbauen** — Pixel für Pixel in HTML/CSS
3. **Eigene Grafik erstellen → Florian Feedback → LEARNINGS updaten**

### Referenz-Accounts für Design-Inspiration
- **Justin Welsh** — Minimalist LinkedIn graphics, text-only, huge engagement
- **Sahil Bloom** — Framework graphics, clean diagrams
- **Alex Hormozi** — Bold text on dark backgrounds, ultra-simple
- **Chris Donnelly** — Carousel format, consistent branding
- **Packy McCormick** — Not Boring newsletter, clean visuals

### Was ich NICHT kann und wissen muss:
- Ich kann keine Fotos bearbeiten → Text-Grafiken und CSS-Grafiken nur
- Ich kann keine Vektorgrafiken → SVG Basics in HTML ja, aber kein Illustrator
- Ich sehe das Ergebnis nicht "als Mensch" → immer Screenshot + Florian-Check
- Ich neige dazu "mehr reinzupacken" → aktiv entfernen

---

## Pre-Delivery Checklist (Visuals)

- [ ] Maximal 3 Farben (aus Brand Guide)?
- [ ] Maximal 2 Font-Gewichte?
- [ ] Minimum 20% Whitespace?
- [ ] Alignment: Alles am Grid?
- [ ] Text: Lesbar auf Mobile (min 16px)?
- [ ] Korrekte Dimensionen für Plattform?
- [ ] Keine Emojis in professioneller Grafik?
- [ ] Ein klares Ziel/Message?
- [ ] "Würde das auf einem McKinsey-Slide bestehen?"
- [ ] Im Browser geöffnet und angeschaut?

---

## Quellen

- Refactoring UI (Adam Wathan & Steve Schoger) — 20 Key Principles
- Smashing Magazine — Typographic Hierarchies
- Forbes — 5 Types of Viral LinkedIn Posts 2025
- IxDF — Visual Hierarchy Principles
- Toptal — 12 Principles of Design

---

*Erstellt: 2026-02-04 04:37 CET*
*Update: Bei jedem Design-Feedback von Florian*
