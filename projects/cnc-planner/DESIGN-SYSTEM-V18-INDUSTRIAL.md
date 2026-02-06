# CNC Planer Pro v18 - Industrial Design System

**Status:** 🟡 AWAITING APPROVAL  
**Basis:** Golden Standards + MBS Angebot Analyse  
**Ziel:** Professionelles Maschinenbau-Angebot Design

---

## 📊 Research Quellen

1. **Golden Standards:**
   - `research/golden-standards/design-system.md` ✅
   - `research/golden-standards/price-display.md` ✅

2. **Real-World Reference:**
   - MBS Angebot 20260072 ✅
   - Analysiert in `MBS-DESIGN-ANALYSE.md`

3. **Prinzipien:**
   - DIN 5008 Geschäftsbrief-Standard
   - Industrial/Maschinenbau Ästhetik
   - Maximale Seriosität & Vertrauenswürdigkeit

---

## 🎨 Farbpalette

### Haupt-Farben (MBS-inspiriert, Golden Standard kompatibel)

```css
:root {
    /* Primär - Dunkelgrau statt Blau (wie MBS) */
    --color-primary: #1F2937;           /* Gray-800 - Hauptakzent */
    --color-primary-hover: #111827;     /* Gray-900 */
    --color-primary-light: #374151;     /* Gray-700 */
    
    /* Neutrals - Grauskala */
    --color-text: #000000;              /* Schwarz - Haupttext (wie MBS) */
    --color-text-secondary: #374151;    /* Dunkelgrau - Sekundär */
    --color-text-muted: #6B7280;        /* Grau - Metadaten */
    --color-text-hint: #9CA3AF;         /* Hellgrau - Hints */
    
    /* Backgrounds */
    --color-bg: #FFFFFF;                /* Weiß - Seite */
    --color-surface: #FFFFFF;           /* Weiß - Cards */
    --color-bg-subtle: #F9FAFB;         /* Sehr hellgrau - Alternate rows */
    --color-bg-muted: #F3F4F6;          /* Hellgrau - Table header (wie MBS #F0F0F0) */
    
    /* Borders */
    --color-border: #D1D5DB;            /* Grau - Tabellen-Rahmen (wie MBS #CCC) */
    --color-border-light: #E5E7EB;      /* Hellgrau - Zeilen-Trenner (wie MBS #E5E5E5) */
    
    /* Semantic (minimal, nur wo nötig) */
    --color-success: #059669;           /* Grün - Erfolg */
    --color-warning: #D97706;           /* Amber - Warnung */
    --color-error: #DC2626;             /* Rot - Fehler */
    --color-info: #2563EB;              /* Blau - Info */
}
```

**Philosophie:**
- **Schwarz für Haupttext** (nicht Dunkelgrau) — wie MBS
- **Keine bunten Akzente** außer für Status/Warnungen
- **Dunkelgrau (#1F2937) statt Blau** als Primärfarbe
- **Kompatibel mit Golden Standard** (Spacing, Components)

---

## 📝 Typografie

### Schriftarten

```css
:root {
    /* System Fonts - KEINE Web Fonts */
    --font-sans: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, 
                 "Helvetica Neue", Arial, sans-serif;
    --font-mono: "SF Mono", Monaco, "Cascadia Code", Consolas, 
                 "Courier New", monospace;
}
```

**Warum System Fonts:**
- Schneller (kein Download)
- Professioneller (nicht "designed")
- Wie echte Geschäftsbriefe (Arial/Helvetica)
- Kostenlos, keine Lizenz nötig

### Schriftgrößen (wie Golden Standard)

```css
:root {
    --text-xs: 0.6875rem;   /* 11px - Footer Kontaktdaten */
    --text-sm: 0.8125rem;   /* 13px - Metadaten, Zeichnungsnummern */
    --text-base: 0.875rem;  /* 14px - Body, Tabelle */
    --text-lg: 1rem;        /* 16px - Headers */
    --text-xl: 1.125rem;    /* 18px - Totals */
    --text-2xl: 1.25rem;    /* 20px - Angebots-Nummer */
    --text-3xl: 1.5rem;     /* 24px - Titel */
}
```

### Schriftgewichte

```css
:root {
    --font-normal: 400;     /* Standard-Text */
    --font-medium: 500;     /* Subtle emphasis */
    --font-semibold: 600;   /* Table headers, labels */
    --font-bold: 700;       /* Position-Nummern, Summen */
}
```

### Line Heights

```css
:root {
    --leading-tight: 1.25;      /* Zahlen, kompakte Tabellen */
    --leading-normal: 1.5;      /* Fließtext */
    --leading-relaxed: 1.75;    /* Bedingungen-Text */
}
```

---

## 📐 Spacing (wie Golden Standard)

```css
:root {
    --space-1: 0.25rem;   /* 4px */
    --space-2: 0.5rem;    /* 8px */
    --space-3: 0.75rem;   /* 12px */
    --space-4: 1rem;      /* 16px */
    --space-5: 1.25rem;   /* 20px */
    --space-6: 1.5rem;    /* 24px */
    --space-8: 2rem;      /* 32px */
    --space-10: 2.5rem;   /* 40px */
    --space-12: 3rem;     /* 48px */
}
```

**Prinzip:** 8px Grid (alle Abstände Vielfache von 8px)

---

## 🏗️ Layout

### Seiten-Margins

```css
.page {
    max-width: 210mm;      /* A4 Breite */
    margin: 0 auto;
    padding: 2cm;          /* Wie MBS */
    background: white;
}
```

### Sidebar

```css
.sidebar {
    width: 240px;          /* Wie Golden Standard */
    background: var(--color-primary);  /* Dunkelgrau */
    color: white;
}
```

---

## 📊 Komponenten

### 1. Tabellen (Haupt-Element)

**Header:**
```css
.table thead {
    background: var(--color-bg-muted);  /* Hellgrau wie MBS #F0F0F0 */
    border-bottom: 2px solid var(--color-border);
}

.table th {
    padding: var(--space-2) var(--space-3);  /* 8px 12px */
    font-size: var(--text-sm);               /* 13px */
    font-weight: var(--font-semibold);       /* 600 */
    text-align: left;
    color: var(--color-text-secondary);
    text-transform: uppercase;
    letter-spacing: 0.05em;
}

.table th:last-child {
    text-align: right;  /* Preise rechtsbündig */
}
```

**Zeilen:**
```css
.table tbody tr {
    border-bottom: 1px solid var(--color-border-light);
}

.table td {
    padding: var(--space-3) var(--space-3);  /* 12px */
    font-size: var(--text-base);             /* 14px */
    color: var(--color-text);                /* Schwarz */
}

.table td:last-child {
    text-align: right;
    font-variant-numeric: tabular-nums;  /* Zahlen alignment */
    font-weight: var(--font-medium);     /* 500 */
}
```

**Position-Nummer (10, 20, 30...):**
```css
.table .position-nr {
    font-weight: var(--font-bold);  /* 700 */
    width: 40px;
}
```

**Zeichnungsnummer (unter Produktname):**
```css
.table .drawing-nr {
    font-size: var(--text-sm);           /* 13px */
    color: var(--color-text-muted);      /* Grau */
    padding-left: var(--space-3);        /* 12px Einrückung */
    padding-top: var(--space-1);         /* 4px Abstand oben */
}

.table .drawing-nr::before {
    content: "Zchng Nr. ";               /* Wie MBS */
}
```

**Summen-Zeile:**
```css
.table .total-row {
    background: var(--color-bg-muted);
    border-top: 2px solid var(--color-border);
    font-weight: var(--font-bold);
    font-size: var(--text-lg);  /* 16px */
}
```

### 2. Header (Angebotsdaten)

```css
.quote-header {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: var(--space-8);
    margin-bottom: var(--space-8);
}

.quote-meta {
    display: grid;
    grid-template-columns: auto 1fr;
    gap: var(--space-2) var(--space-4);
    font-size: var(--text-sm);
}

.quote-meta dt {
    font-weight: var(--font-semibold);
    color: var(--color-text-secondary);
}

.quote-meta dd {
    color: var(--color-text);
}
```

### 3. Footer (Rechtliche Infos)

```css
.legal-footer {
    margin-top: var(--space-12);
    padding-top: var(--space-6);
    border-top: 1px solid var(--color-border-light);
    font-size: var(--text-xs);       /* 11px */
    color: var(--color-text-muted);  /* Grau */
    line-height: var(--leading-relaxed);
}

.contact-footer {
    margin-top: var(--space-6);
    font-size: var(--text-xs);       /* 11px */
    color: var(--color-text-hint);   /* Hellgrau */
    line-height: var(--leading-tight);
}
```

### 4. Buttons

```css
.btn {
    height: 36px;
    padding: 0 var(--space-4);
    font-size: var(--text-base);
    font-weight: var(--font-medium);
    border-radius: 4px;  /* Minimal */
    border: 1px solid var(--color-border);
    background: white;
    color: var(--color-text);
    transition: all 150ms ease;
}

.btn:hover {
    background: var(--color-bg-subtle);
    border-color: var(--color-primary);
}

.btn-primary {
    background: var(--color-primary);
    color: white;
    border-color: var(--color-primary);
}

.btn-primary:hover {
    background: var(--color-primary-hover);
}
```

### 5. Cards

```css
.card {
    background: white;
    border: 1px solid var(--color-border-light);
    border-radius: 4px;  /* Minimal */
    padding: var(--space-6);
    margin-bottom: var(--space-6);
}

.card-header {
    padding: var(--space-4) var(--space-6);
    background: var(--color-bg-muted);  /* Hellgrau */
    border-bottom: 1px solid var(--color-border-light);
    font-weight: var(--font-semibold);
    font-size: var(--text-base);
    color: var(--color-text);
}

/* KEINE bunten Card-Header mehr */
```

---

## 🎯 Angebot-spezifische Elemente

### Zeichnungsnummer-Display

```html
<div class="part-info">
    <div class="part-name">Platte (Lagerbock)</div>
    <div class="drawing-nr">2500473.01.01.02.01.001</div>
</div>
```

```css
.part-name {
    font-size: var(--text-lg);
    font-weight: var(--font-semibold);
    color: var(--color-text);
}

.drawing-nr {
    font-size: var(--text-sm);
    color: var(--color-text-muted);
    font-family: var(--font-mono);
    margin-top: var(--space-1);
}

.drawing-nr::before {
    content: "Zeichnung-Nr.: ";
    font-family: var(--font-sans);
}
```

### Gültigkeit-Display

```html
<div class="validity">
    Angebot gültig bis: <strong>05.03.2026</strong> (4 Wochen)
</div>
```

```css
.validity {
    font-size: var(--text-sm);
    color: var(--color-text-muted);
    margin-top: var(--space-2);
}

.validity strong {
    color: var(--color-text);
    font-weight: var(--font-semibold);
}
```

### Disclaimer-Box

```html
<div class="disclaimer">
    <strong>Hinweis:</strong> Die Preise basieren auf aktuellen 
    Materialkosten und Standard-Fertigungsparametern (±15% Genauigkeit). 
    Änderungen bei Sonderwünschen oder stark schwankenden Marktpreisen 
    vorbehalten.
</div>
```

```css
.disclaimer {
    padding: var(--space-4);
    background: var(--color-bg-subtle);
    border-left: 3px solid var(--color-border);
    font-size: var(--text-sm);
    color: var(--color-text-secondary);
    line-height: var(--leading-relaxed);
    margin-top: var(--space-6);
}
```

---

## 🚫 Was NICHT mehr verwendet wird

### Emojis/Icons
- ❌ ALLE Emojis entfernen
- ❌ Keine Icon-Fonts
- ❌ Nur Text

### Bunte Farben
- ❌ Keine blauen/grünen/gelben Card-Header
- ❌ Success/Warning/Info nur für Alerts
- ❌ Primärfarbe = Dunkelgrau (nicht Blau)

### Dekorative Elemente
- ❌ Keine Schatten (außer minimal)
- ❌ Keine Gradients
- ❌ Keine Rounded Corners >4px

### Google Fonts
- ❌ Keine externen Fonts
- ✅ System Fonts nur

---

## 📋 Implementierungs-Checklist

### Phase 1: CSS Grundlagen
- [ ] Farbpalette updaten (Dunkelgrau statt Blau)
- [ ] System Fonts setzen
- [ ] Spacing beibehalten (Golden Standard)
- [ ] Emojis aus CSS entfernen

### Phase 2: Komponenten
- [ ] Tabellen-Styling (MBS-Style)
- [ ] Card-Header hellgrau (nicht bunt)
- [ ] Buttons minimal
- [ ] Footer-Komponenten

### Phase 3: Angebot-Tab
- [ ] Zeichnungsnummer prominent
- [ ] Position-Nummerierung (10, 20, 30...)
- [ ] Gültigkeit automatisch
- [ ] Disclaimer-Box
- [ ] Footer mit Rechtlichem

### Phase 4: Fertigungsanweisung-Tab
- [ ] Zeichnungsnummer als Referenz
- [ ] Tabellen wie Angebot-Style
- [ ] Keine bunten Headers

### Phase 5: Validierung
- [ ] Browser-Test
- [ ] Print-Test
- [ ] Vergleich mit MBS Original
- [ ] Florian Approval

---

## 🎯 Erwartetes Ergebnis

**Wenn Florian öffnet, sollte er sehen:**

1. **Seriös & Professionell**
   - Wie ein echtes Maschinenbau-Angebot
   - Keine Spielerei
   - Vertrauenswürdig

2. **Klare Hierarchie**
   - Zeichnungsnummer prominent
   - Preise gut lesbar
   - Tabellen strukturiert

3. **Industrial Look**
   - Schwarz/Grau/Weiß
   - Keine bunten Farben
   - System Fonts

4. **DIN-ähnlich**
   - Geschäftsbrief-Layout
   - Professional Spacing
   - Deutsche Formatierung

---

## ✅ Genehmigung benötigt

**Florian, bitte prüfe:**

1. **Farbpalette:** Dunkelgrau (#1F2937) statt Blau OK?
2. **System Fonts:** Arial/Helvetica statt Inter OK?
3. **Tabellen:** Hellgrauer Header (#F3F4F6) wie MBS OK?
4. **Keine Emojis:** Komplett entfernen OK?
5. **Zeichnungsnummer:** Unter Bauteil-Name anzeigen OK?
6. **Position-Nummern:** 10, 20, 30 statt 1, 2, 3 OK?

**Wenn approved → implementieren in `cnc-planner-pro-v18-industrial.html`**

---

*Erstellt: 2026-02-06 00:45*  
*Status: AWAITING APPROVAL*  
*Next: Implementation nach Genehmigung*
