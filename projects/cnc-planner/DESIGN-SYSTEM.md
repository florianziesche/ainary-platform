# CNC Planer Pro - Design System

**Version:** 1.0  
**Datum:** 2026-02-06  
**Based on:** MBS Angebot (Real Maschinenbau Company)

---

## 🎯 PHILOSOPHY

**Industrial. Professional. Vertrauenswürdig.**

Dieses Design System basiert auf **echten Maschinenbau-Angeboten** deutscher Unternehmen, nicht auf modernen Web-Trends.

**Prinzipien:**
1. **Weniger ist mehr** - Kein bunter Schnickschnack
2. **Lesbarkeit über Schönheit** - Klarheit gewinnt
3. **System Fonts** - Keine Google Fonts (wie echte Firmen)
4. **Grautöne dominieren** - Schwarz/Grau/Weiß
5. **Standards einhalten** - Folge etablierte Patterns

---

## 🎨 DESIGN TOKENS

### Farben

**Primary Palette:**
```css
:root {
  /* Primär */
  --color-primary: #1F2937;        /* Dunkelgrau - Header, wichtige Elemente */
  
  /* Graustufen */
  --color-black: #000000;          /* Text */
  --color-gray-900: #111827;       /* Sehr dunkler Text */
  --color-gray-700: #374151;       /* Sekundärer Text */
  --color-gray-600: #4B5563;       /* Tertiary Text */
  --color-gray-500: #6B7280;       /* Hints, Labels */
  --color-gray-400: #9CA3AF;       /* Disabled, Footer */
  --color-gray-300: #D1D5DB;       /* Borders */
  --color-gray-200: #E5E7EB;       /* Light Borders */
  --color-gray-100: #F3F4F6;       /* Table Headers */
  --color-gray-50: #F9FAFB;        /* Subtle Backgrounds */
  
  /* Funktionale Farben */
  --color-success: #059669;        /* Grün - Success States */
  --color-warning: #D97706;        /* Orange - Warnings */
  --color-error: #DC2626;          /* Rot - Errors */
  --color-info: #2563EB;           /* Blau - Info (sparsam nutzen!) */
}
```

**Usage Guidelines:**
- **Schwarz (#000):** Nur für Haupttext
- **Primär (#1F2937):** Headers, wichtige Labels, Borders
- **Grau 700-500:** Sekundärer Text, Metadaten
- **Grau 400:** Footer, Copyright, Hints
- **Grau 100-50:** Backgrounds, sehr subtile Elemente
- **Funktionale Farben:** NUR wo semantisch sinnvoll (Success = grün, Error = rot)

**Referenz:** `research/MBS-DESIGN-ANALYSE.md`

---

### Typography

**Font Stack:**
```css
:root {
  /* System Fonts (wie echte Firmen) */
  --font-sans: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --font-mono: "SF Mono", Monaco, "Cascadia Code", "Roboto Mono", Consolas, "Courier New", monospace;
  
  /* Font Sizes */
  --text-xs: 11px;      /* Footer, Copyright */
  --text-sm: 13px;      /* Table Content, Labels */
  --text-base: 14px;    /* Body Text */
  --text-lg: 16px;      /* Section Headers */
  --text-xl: 18px;      /* Card Titles */
  --text-2xl: 24px;     /* Page Titles */
  --text-3xl: 32px;     /* Hero Text (selten) */
  
  /* Line Heights */
  --leading-tight: 1.25;
  --leading-normal: 1.5;
  --leading-relaxed: 1.75;
  
  /* Font Weights */
  --weight-normal: 400;
  --weight-medium: 500;
  --weight-semibold: 600;
  --weight-bold: 700;
}
```

**Usage:**
- **Titles:** 600 weight, Grau 900
- **Body:** 400 weight, Schwarz
- **Labels:** 500-600 weight, Grau 700
- **Hints:** 400 weight, Grau 500

**Referenz:** `research/MBS-ANGEBOT-LINE-BY-LINE.md` (Seite 1, Font-Analyse)

---

### Spacing

**8pt Grid System:**
```css
:root {
  --space-1: 4px;
  --space-2: 8px;
  --space-3: 12px;
  --space-4: 16px;
  --space-5: 20px;
  --space-6: 24px;
  --space-8: 32px;
  --space-10: 40px;
  --space-12: 48px;
  --space-16: 64px;
  --space-20: 80px;
  --space-24: 96px;
}
```

**Usage:**
- **Card Padding:** `--space-6` (24px)
- **Section Margins:** `--space-8` bis `--space-12`
- **Element Gaps:** `--space-4` (16px)
- **Tight Spacing:** `--space-2` (8px)

---

### Borders & Shadows

```css
:root {
  /* Borders */
  --border-light: 1px solid var(--color-gray-200);
  --border-medium: 1px solid var(--color-gray-300);
  --border-heavy: 2px solid var(--color-gray-900);
  
  /* Border Radius */
  --radius-sm: 4px;
  --radius-md: 6px;
  --radius-lg: 8px;
  
  /* Shadows (sparsam nutzen!) */
  --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
  --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
  --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
}
```

**Usage:**
- Borders meist `--border-light`
- Shadows NUR für Cards, Modals (nicht für alles!)
- Border-Radius: `--radius-sm` Standard

---

## 🧱 COMPONENTS

### Cards

**Standard Card:**
```html
<div class="card">
  <div class="card-header-primary">
    <h3>Überschrift</h3>
  </div>
  <div class="card-body">
    <p>Content hier...</p>
  </div>
</div>
```

**CSS:**
```css
.card {
  background: white;
  border: var(--border-light);
  border-radius: var(--radius-sm);
  margin-bottom: var(--space-6);
}

.card-header-primary {
  background: var(--color-primary);
  color: white;
  padding: var(--space-4) var(--space-6);
  font-weight: var(--weight-semibold);
  font-size: var(--text-base);
}

.card-header-info {
  background: var(--color-gray-100);
  color: var(--color-gray-900);
  padding: var(--space-4) var(--space-6);
  font-weight: var(--weight-semibold);
  font-size: var(--text-base);
}

.card-body {
  padding: var(--space-6);
}
```

**Variants:**
- `.card-header-primary` - Dunkelgrau, wichtige Cards
- `.card-header-info` - Hellgrau, Info-Cards
- `.card-header-success` - Grün, Erfolgsmeldungen
- `.card-header-warning` - Orange, Warnungen
- `.card-header-error` - Rot, Fehler

**Referenz:** `DESIGN-STANDARD.md`

---

### Tables

**Professional Table (Bootstrap-based):**
```html
<table class="table">
  <thead>
    <tr>
      <th>Position</th>
      <th>Bezeichnung</th>
      <th class="right">Preis</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>Verbindungsplatte</td>
      <td class="right">EUR 26,30</td>
    </tr>
  </tbody>
</table>
```

**CSS:**
```css
.table {
  width: 100%;
  border-collapse: collapse;
  font-size: var(--text-sm);
}

.table thead {
  background: var(--color-gray-100);
}

.table th {
  padding: 8px 12px;
  text-align: left;
  font-weight: var(--weight-semibold);
  color: var(--color-gray-700);
  border-bottom: 2px solid var(--color-gray-300);
  font-size: var(--text-xs);
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.table td {
  padding: 8px 12px;
  border-bottom: 1px solid var(--color-gray-200);
  color: var(--color-black);
}

.table tbody tr:hover {
  background: rgba(0, 0, 0, 0.025);
}

.table .right {
  text-align: right;
}

.table .mono {
  font-family: var(--font-mono);
  font-size: var(--text-sm);
}
```

**Referenz:** `RESEARCH-TABELLEN-STYLING.md`

---

### Buttons

```html
<button class="btn btn-primary">Primär</button>
<button class="btn btn-secondary">Sekundär</button>
<button class="btn btn-text">Text-Button</button>
```

**CSS:**
```css
.btn {
  padding: 10px 16px;
  font-size: var(--text-sm);
  font-weight: var(--weight-medium);
  border-radius: var(--radius-sm);
  border: none;
  cursor: pointer;
  transition: all 0.2s;
}

.btn-primary {
  background: var(--color-primary);
  color: white;
}

.btn-primary:hover {
  background: var(--color-gray-900);
}

.btn-secondary {
  background: white;
  color: var(--color-gray-700);
  border: var(--border-medium);
}

.btn-secondary:hover {
  background: var(--color-gray-50);
}

.btn-text {
  background: transparent;
  color: var(--color-gray-700);
  text-decoration: underline;
}
```

---

### Forms

```html
<div class="form-group">
  <label for="input" class="form-label">Label</label>
  <input type="text" id="input" class="form-input" placeholder="Placeholder...">
  <span class="form-hint">Hilfetext hier</span>
</div>
```

**CSS:**
```css
.form-group {
  margin-bottom: var(--space-4);
}

.form-label {
  display: block;
  font-weight: var(--weight-medium);
  color: var(--color-gray-700);
  font-size: var(--text-sm);
  margin-bottom: var(--space-2);
}

.form-input {
  width: 100%;
  padding: 10px 12px;
  font-size: var(--text-base);
  border: var(--border-medium);
  border-radius: var(--radius-sm);
  font-family: var(--font-sans);
}

.form-input:focus {
  outline: none;
  border-color: var(--color-primary);
  box-shadow: 0 0 0 3px rgba(31, 41, 55, 0.1);
}

.form-hint {
  display: block;
  font-size: var(--text-xs);
  color: var(--color-gray-500);
  margin-top: var(--space-1);
}
```

---

### Info-Boxen

```html
<div class="info-box">
  <strong>Wichtig:</strong> Diese Information ist wichtig.
</div>

<div class="warning-box">
  <strong>Achtung:</strong> Dies ist eine Warnung.
</div>
```

**CSS:**
```css
.info-box {
  background: var(--color-gray-50);
  border-left: 3px solid var(--color-primary);
  padding: var(--space-4);
  font-size: var(--text-sm);
  line-height: var(--leading-relaxed);
  margin: var(--space-6) 0;
}

.warning-box {
  background: #FEF3C7;
  border-left: 3px solid var(--color-warning);
  padding: var(--space-4);
  font-size: var(--text-sm);
  line-height: var(--leading-relaxed);
  margin: var(--space-6) 0;
}

.success-box {
  background: #D1FAE5;
  border-left: 3px solid var(--color-success);
  padding: var(--space-4);
  font-size: var(--text-sm);
  line-height: var(--leading-relaxed);
  margin: var(--space-6) 0;
}
```

---

## 📐 LAYOUT PATTERNS

### 2-Column Layout (Quote Header)

```html
<div class="grid-2col">
  <div>
    <!-- Linke Spalte: Adresse -->
  </div>
  <div>
    <!-- Rechte Spalte: Metadaten -->
  </div>
</div>
```

**CSS:**
```css
.grid-2col {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: var(--space-8);
}

@media (max-width: 768px) {
  .grid-2col {
    grid-template-columns: 1fr;
  }
}
```

**Referenz:** `research/MBS-ANGEBOT-LINE-BY-LINE.md` (Seite 1, Header-Struktur)

---

### Footer Layout

```html
<div class="contact-footer">
  <div class="footer-grid">
    <div>Kontaktdaten</div>
    <div>Rechtliches</div>
  </div>
</div>
```

**CSS:**
```css
.contact-footer {
  margin-top: var(--space-12);
  padding-top: var(--space-6);
  border-top: 1px solid var(--color-gray-200);
  font-size: var(--text-xs);
  color: var(--color-gray-400);
  line-height: var(--leading-relaxed);
}

.footer-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: var(--space-4);
}
```

**Referenz:** `RESEARCH-FOOTER-RECHTLICHES.md`

---

## 🔢 FORMATTING LIBRARY

### Deutsche Formatierung

**Alle Formate in JavaScript:**
```javascript
const DEFormatter = {
  date(date) {
    return date.toLocaleDateString('de-DE', {
      day: '2-digit',
      month: '2-digit',
      year: 'numeric'
    });
  },
  
  price(amount) {
    const formatted = amount.toLocaleString('de-DE', {
      minimumFractionDigits: 2,
      maximumFractionDigits: 2
    });
    return `EUR ${formatted}`;
  },
  
  length(value, unit = 'mm') {
    return `${Math.round(value)} ${unit}`;
  },
  
  weight(value) {
    return `${value.toFixed(2)} kg`;
  },
  
  time(minutes) {
    if (minutes < 60) return `${minutes.toFixed(1)} min`;
    return `${(minutes/60).toFixed(1)} h`;
  },
  
  quantity(num, unit = 'Stck.') {
    return `${Math.round(num)} ${unit}`;
  }
};
```

**Usage:**
```javascript
DEFormatter.price(1234.56);     // "EUR 1.234,56"
DEFormatter.date(new Date());   // "06.02.2026"
DEFormatter.length(440);        // "440 mm"
DEFormatter.weight(2.2);        // "2,20 kg"
DEFormatter.time(75);           // "1,3 h"
DEFormatter.quantity(29);       // "29 Stck."
```

**Referenz:** `RESEARCH-DEUTSCHE-FORMATIERUNG.md`

---

## 🎯 ANWENDUNGSBEISPIELE

### Vollständiges Quote Template

**Siehe:** `REQUIREMENTS-V18-FINAL.md` (Complete HTML Structure)

### Calculation Cards

**Siehe:** `demo-v16-complete.html` (section-calculation)

### Operations Table

**Siehe:** `demo-v16-complete.html` (Fertigungsanweisung)

---

## 🔗 RELATED DOCUMENTS

### Research:
- [`research/MBS-ANGEBOT-LINE-BY-LINE.md`](research/MBS-ANGEBOT-LINE-BY-LINE.md) - Golden Standard Analyse
- [`research/MBS-DESIGN-ANALYSE.md`](research/MBS-DESIGN-ANALYSE.md) - Design-Prinzipien
- [`RESEARCH-TABELLEN-STYLING.md`](RESEARCH-TABELLEN-STYLING.md) - Table Standards
- [`RESEARCH-FOOTER-RECHTLICHES.md`](RESEARCH-FOOTER-RECHTLICHES.md) - Footer Guidelines
- [`RESEARCH-PREIS-FORMATIERUNG.md`](RESEARCH-PREIS-FORMATIERUNG.md) - Price Formatting
- [`RESEARCH-DEUTSCHE-FORMATIERUNG.md`](RESEARCH-DEUTSCHE-FORMATIERUNG.md) - Complete DE Library

### Process:
- [`DEVELOPMENT-PROCESS.md`](DEVELOPMENT-PROCESS.md) - Software Development Process
- [`DESIGN-STANDARD.md`](DESIGN-STANDARD.md) - Legacy Design Standards (v16)

### Implementation:
- [`REQUIREMENTS-V18-FINAL.md`](REQUIREMENTS-V18-FINAL.md) - v18 Requirements
- [`demo-v16-complete.html`](demo-v16-complete.html) - Current Production Version
- [`cnc-planner-pro-v18-industrial.html`](cnc-planner-pro-v18-industrial.html) - v18 WIP

---

## ⚠️ DO NOT

### Verboten:

❌ **Inline-Styles:**
```html
<!-- NIEMALS! -->
<div style="padding: 24px; color: #374151;">
```

❌ **Direkte Hex-Codes:**
```css
/* NIEMALS! */
.card { background: #f9fafb; }
```

❌ **Pixel-Werte direkt:**
```css
/* NIEMALS! */
.card { margin: 24px; }
```

❌ **Google Fonts:**
```html
<!-- NIEMALS! -->
<link href="https://fonts.googleapis.com/css?family=Inter">
```

❌ **Bunte Akzente ohne Grund:**
```css
/* NIEMALS! */
.card-header { background: linear-gradient(45deg, #FF6B6B, #4ECDC4); }
```

### Stattdessen:

✅ **CSS-Klassen:**
```html
<div class="card-body">
```

✅ **CSS-Variablen:**
```css
.card { background: var(--color-gray-50); }
```

✅ **Spacing-System:**
```css
.card { margin: var(--space-6); }
```

✅ **System Fonts:**
```css
font-family: var(--font-sans);
```

✅ **Funktionale Farben:**
```css
.success { color: var(--color-success); }
```

---

## 📊 USAGE TRACKING

**Welche Components werden wo genutzt:**

### Cards:
- Kalkulation (4 Cards: Maschine, Material, Einrichtung, Gesamt)
- Fertigungsanweisung (1 Card)
- Angebot (1 Card)
- Parameter (3 Tabs als Cards)

### Tables:
- Operations-Tabelle (Fertigungsanweisung)
- Quote-Tabelle (Angebot)
- Calculation-Details (optional)

### Forms:
- Parameter-Eingaben (Teil-Tab)
- Materialeingabe
- Maschinenwahl

---

## 🔄 VERSION HISTORY

- **v1.0** (2026-02-06) - Initial Design System basierend auf MBS Research

---

*Maintainer: Mia*  
*Last Updated: 2026-02-06*  
*Next Review: Bei jedem neuen Component*
