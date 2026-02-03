# Brand Guide — Florian Ziesche

*Version 1.0 | 3. Februar 2026*

---

## Übersicht

Diese Corporate Identity gilt für alle Marken und Produkte unter dem Dach von Florian Ziesche:

- **FZ** — Florian Ziesche (Personal Brand / Dachmarke)
- **CP** — CNC Planner Pro (SaaS Produkt)
- **LT** — Legal Tech AI (Enterprise Platform)

---

## Farbpalette

### Primärfarben

| Name | Hex | RGB | Verwendung |
|------|-----|-----|------------|
| **Primary (Navy)** | `#1e3a5f` | 30, 58, 95 | Logos, Headlines, primäre Elemente |
| **Primary Dark** | `#152a45` | 21, 42, 69 | Hover-States, Schatten |
| **Primary Light** | `#2d5a8a` | 45, 90, 138 | Gradients, sekundäre Elemente |

### Akzentfarben

| Name | Hex | RGB | Verwendung |
|------|-----|-----|------------|
| **Accent (Electric Blue)** | `#2563eb` | 37, 99, 235 | CTAs, Links, Highlights |
| **Accent Light** | `#60a5fa` | 96, 165, 250 | Hover, helle Akzente |
| **Success (Grün)** | `#059669` | 5, 150, 105 | Erfolg, positive Werte |

### Neutrale Farben

| Name | Hex | Verwendung |
|------|-----|------------|
| **Dark** | `#0f172a` | Dunkle Hintergründe, Text auf Hell |
| **Gray 800** | `#1e293b` | Karten auf dunklem Hintergrund |
| **Gray 600** | `#475569` | Sekundärer Text |
| **Gray 400** | `#94a3b8` | Tertiärer Text, Placeholder |
| **Light** | `#f8fafc` | Helle Hintergründe |
| **White** | `#ffffff` | Reinweiß |

### CSS Variables

```css
:root {
    --primary: #1e3a5f;
    --primary-dark: #152a45;
    --primary-light: #2d5a8a;
    --accent: #2563eb;
    --accent-light: #60a5fa;
    --success: #059669;
    --dark: #0f172a;
    --gray-800: #1e293b;
    --gray-600: #475569;
    --gray-400: #94a3b8;
    --light: #f8fafc;
    --white: #ffffff;
}
```

---

## Typografie

### Logo-Schrift

**Space Grotesk Bold**
- Verwendung: Logo-Initialen (FZ, CP, LT)
- Gewicht: 700 (Bold)
- Charakter: Geometrisch, tech, clean

```css
font-family: 'Space Grotesk', sans-serif;
font-weight: 700;
```

### Body-Schrift

**Inter**
- Verwendung: Alle anderen Texte
- Gewichte: 400 (Regular), 500 (Medium), 600 (SemiBold), 700 (Bold)

```css
font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
```

### Typografie-Hierarchie

| Element | Font | Gewicht | Größe |
|---------|------|---------|-------|
| H1 | Inter | 800 | 2.5rem |
| H2 | Inter | 700 | 1.75rem |
| H3 | Inter | 600 | 1.25rem |
| Body | Inter | 400 | 1rem |
| Small | Inter | 400 | 0.875rem |
| Caption | Inter | 400 | 0.75rem |

---

## Logo-System

### Logo-Konstruktion

Alle Logos folgen dem gleichen Muster:
- **Box**: 2-Buchstaben-Initialen in quadratischer Box
- **Gradient**: `linear-gradient(135deg, #1e3a5f, #2d5a8a)`
- **Border-Radius**: 16px (groß), 12px (mittel), 8px (klein)
- **Schrift**: Space Grotesk Bold

### Logo-Varianten

#### Florian Ziesche (FZ)
```
[FZ] Florian Ziesche
```
- Box: Navy Gradient mit weißem "FZ"
- Text: "Florian" schwarz/weiß, "Ziesche" in Accent Blue

#### CNC Planner Pro (CP)
```
[CP] CNC Planner Pro
```
- Box: Navy Gradient mit weißem "CP"
- Text: "CNC" + "Pro" normal, "Planner" in Primary

#### Legal Tech AI (LT)
```
[LT] Legal Tech AI
```
- Box: Navy Gradient mit weißem "LT"
- Text: "Legal" + "AI" normal, "Tech" in Accent Blue

### Logo-Größen

| Kontext | Box-Größe | Schriftgröße |
|---------|-----------|--------------|
| Hero/Header | 80px | 2rem |
| Navigation | 36-48px | 1.1rem |
| Favicon | 32px | - |
| Email Signatur | 40px | 1rem |

---

## Anwendungen

### Website Header
- Hintergrund: Weiß
- Logo links, Navigation mitte, CTA rechts
- CTA Button: Primary Navy

### Dark Mode
- Hintergrund: `#0f172a`
- Karten: `#1e293b`
- Text: `#e2e8f0` (hell)
- Accent bleibt: `#2563eb`

### Light Mode
- Hintergrund: `#f8fafc` oder weiß
- Text: `#0f172a`
- Accent bleibt: `#2563eb`

### Email Signatur
- Navy Linie als Trenner
- Logo-Box klein (40px)
- Sub-Brands (CP, LT) als kleine Icons

---

## Dateien

### Finale Dateien
- `/brand/final/corporate-identity-mockup.html` — Komplette CI-Übersicht

### Konzept-Dateien (Archiv)
- `/brand/concepts/color-concepts.html` — 5 Farbvarianten
- `/brand/concepts/logo-concepts.html` — 3 Schrift-Varianten

### Assets (zu erstellen)
- `/brand/assets/` — SVG Logos, PNG Exports

---

## Entscheidungen

| Datum | Entscheidung | Status |
|-------|--------------|--------|
| 2026-02-03 | Primary: Navy #1e3a5f | ✅ Final |
| 2026-02-03 | Accent: Electric Blue #2563eb | ✅ Final |
| 2026-02-03 | Logo-Schrift: Space Grotesk | ✅ Final |
| 2026-02-03 | Body-Schrift: Inter | ✅ Final |
| 2026-02-03 | Logo-Stil: Gradient Box + Initialen | ✅ Final |

---

*Erstellt von Mia | Aktualisiert: 2026-02-03*
