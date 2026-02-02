# CNC Planner Pro — Technical Documentation

*Comprehensive technical documentation for all iterations and features.*

---

## Table of Contents

1. [Overview](#overview)
2. [Design System](#design-system)
3. [File Structure](#file-structure)
4. [Version History](#version-history)
5. [Feature Specifications](#feature-specifications)
6. [Calculation Logic](#calculation-logic)
7. [Data Models](#data-models)
8. [Component Reference](#component-reference)

---

## Overview

**CNC Planner Pro** is a web-based manufacturing calculation and documentation tool designed for CNC machining operations. It generates:

- **Fertigungsanweisungen** (Manufacturing Instructions)
- **Zeitberechnungen** (Time Calculations)
- **Angebote** (Quotes)
- **NC-Code** (Machine Code for Heidenhain TNC 640)

### Target Users
- Maschinenbau Schlottwitz (primary pilot customer)
- Small to medium CNC machining shops
- Manufacturing engineers and operators

### Technology Stack
- Pure HTML/CSS/JavaScript (no frameworks)
- Self-contained single-file applications
- Print-optimized CSS
- Responsive design

---

## Design System

### Color Palette (Industrial Theme)

```css
:root {
    /* Primary Colors */
    --primary: #1e3a5f;        /* Dark blue - headers, primary actions */
    --primary-dark: #152a45;   /* Darker blue - hover states */
    --primary-light: #2d5a8a;  /* Lighter blue - gradients */
    
    /* Accent Colors */
    --accent: #2563eb;         /* Bright blue - links, highlights */
    --accent-dark: #1d4ed8;    /* Darker accent */
    
    /* Status Colors */
    --success: #059669;        /* Green - positive, complete */
    --warning: #d97706;        /* Orange - warnings, corrections */
    --danger: #dc2626;         /* Red - critical, errors */
    
    /* Gray Scale (Slate) */
    --gray-50: #f8fafc;
    --gray-100: #f1f5f9;
    --gray-200: #e2e8f0;
    --gray-300: #cbd5e1;
    --gray-400: #94a3b8;
    --gray-500: #64748b;
    --gray-600: #475569;
    --gray-700: #334155;
    --gray-800: #1e293b;
    --gray-900: #0f172a;
}
```

### Typography

```css
/* Primary Font */
font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;

/* Monospace (for code, calculations) */
font-family: 'JetBrains Mono', monospace;

/* Font Sizes */
--text-xs: 0.7rem;    /* Labels, badges */
--text-sm: 0.8rem;    /* Secondary text */
--text-base: 0.9rem;  /* Body text */
--text-lg: 1rem;      /* Headings */
--text-xl: 1.2rem;    /* Section titles */
--text-2xl: 1.5rem;   /* Page titles */
```

### Spacing & Radius

```css
--radius: 8px;        /* Standard border radius */
--radius-lg: 12px;    /* Cards, large elements */
--radius-full: 9999px; /* Pills, badges */

--spacing-xs: 4px;
--spacing-sm: 8px;
--spacing-md: 16px;
--spacing-lg: 24px;
--spacing-xl: 32px;
```

### Shadows

```css
--shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05);
--shadow: 0 1px 3px 0 rgb(0 0 0 / 0.1);
--shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.1);
--shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.1);
```

---

## File Structure

```
products/cnc-planner/
├── app.html              # Reference app design (sidebar UI)
├── landing-page.html     # Marketing landing page
├── PRICING.md            # Pricing tiers documentation
└── ROI-CALCULATOR.md     # ROI calculation logic

projects/cnc-planner/
├── demo-v7.html          # CURRENT - Landing page style FA document
├── demo-final.html       # App-style with enhancements
├── demo-final-backup.html # Backup of demo-final before edits
├── demo-enhanced.html    # Full-featured but wrong design
├── TECHNICAL_DOCS.md     # This file
├── CHANGELOG.md          # Version history
└── [legacy versions]     # app-v1 through app-v6

/tmp/cnc_ref/             # Reference files from zip
├── Fertigungsanweisung_Grundplatte_V3.html
├── Zeitberechnung_mit_Angebot.html
└── GRUNDPLATTE.H
```

---

## Version History

| Version | File | Date | Design | Status |
|---------|------|------|--------|--------|
| v1-v4 | app-v[n].html | Jan 2026 | Various iterations | Archived |
| v5 | app-v5.html | 2026-02-01 | Dark theme, NC code | Archived |
| v6 | app-v6.html | 2026-02-02 | Light theme | Archived |
| Reference | products/app.html | — | Sidebar app UI | Reference |
| demo-final | demo-final.html | 2026-02-02 | Sidebar app + enhancements | Superseded |
| demo-enhanced | demo-enhanced.html | 2026-02-02 | New design (rejected) | Rejected |
| **v7** | **demo-v7.html** | **2026-02-02** | **Landing page style** | **CURRENT** |

### Design Evolution

1. **v1-v4**: Early prototypes, exploring UI patterns
2. **v5**: Added NC code generation, dark theme
3. **v6**: Switched to light theme, attempted Rohmaß calculation
4. **Reference (app.html)**: Established sidebar app design
5. **demo-final**: Enhanced app design with progress bars, feedback
6. **demo-enhanced**: Created new design (didn't match requirements)
7. **v7**: Clean document-style matching landing page aesthetic

---

## Feature Specifications

### 1. Progress Bar

Visual representation of machining time distribution across operations.

```html
<div class="progress-bar">
    <div class="progress-segment" style="width: 6.5%; background: #3b82f6;">10</div>
    <!-- ... more segments ... -->
</div>
```

**Calculation:**
```
segment_width = (operation_time / total_time) * 100%
```

**Colors by Operation:**
- OP10-OP20: Blues (#3b82f6, #2563eb)
- OP30-OP40: Greens (#10b981, #059669)
- OP50-OP60: Reds (#ef4444, #dc2626) — Critical operations
- OP70-OP80: Purples (#8b5cf6, #7c3aed)
- OP90-OP100: Oranges (#f59e0b, #d97706)

### 2. Tool Life Bars

Visual indicator of remaining tool life.

```html
<div class="tool-life">
    <div class="tool-life-fill good" style="width: 85%;">85%</div>
</div>
```

**Status Classes:**
- `.good`: >60% remaining (green gradient)
- `.warning`: 30-60% remaining (yellow/orange gradient)
- `.critical`: <30% remaining (red gradient)

### 3. Operation Cards

Detailed operation information in card format.

```html
<div class="op-card critical">
    <div class="op-num">50</div>
    <div class="op-details">
        <h4>🎯 Schlichten Ø120 h5</h4>
        <p>T3 Ø16 | n=3500 | f=250 | KRITISCH!</p>
    </div>
    <div class="op-params">
        <div class="param-box">
            <div class="param-label">Tol</div>
            <div class="param-value">h5</div>
        </div>
    </div>
    <div class="op-time">
        <div class="op-time-value">5,1</div>
        <div class="op-time-label">min</div>
    </div>
</div>
```

### 4. Feedback Panel

Operator feedback system for continuous improvement.

**Features:**
- Star ratings (1-5)
- Operation tags (OP10, OP50, etc.)
- Timestamp and author
- Category tags (Allgemein, specific OP)

### 5. Checklists

Interactive pre-start and quality checklists.

```html
<li onclick="this.classList.toggle('checked')">
    <span class="check-box">✓</span>
    Werkzeuglängen geprüft
</li>
```

### 6. Correction Values

Recommended tool corrections based on wear patterns.

| Dimension | Correction | Interval | Threshold |
|-----------|------------|----------|-----------|
| Ø120 h5 | -0,005 mm | 5 parts | >119,990 |
| Ø26 H7 | +0,003 mm | 5 parts | <26,010 |
| Ø44 H7 | +0,004 mm | 5 parts | <44,012 |

### 7. NC Code Display

Syntax-highlighted Heidenhain TNC 640 code.

**Syntax Classes:**
- `.comment`: Gray (#718096) — Lines starting with `;`
- `.keyword`: Orange (#f6ad55) — BEGIN PGM, END PGM, TOOL CALL, CYCL DEF
- `.number`: Green (#68d391) — Numeric values
- `.gcode`: Blue (#90cdf4) — L, CC, C, BLK FORM

---

## Calculation Logic

### Time Calculation Formula

```
Hauptzeit (t_h):
t_h = L / v_f = L / (f × n)

Where:
- L = Cutting path length (mm)
- f = Feed rate (mm/rev)
- n = Spindle speed (rpm)
- v_f = Feed velocity (mm/min)

Nebenzeit (t_n):
- Tool change: 0.5 min (VERSA 943 chain magazine)
- Positioning: Calculated from rapid traverse (40 m/min)
- Measurement: 0.3-0.5 min depending on operation

Total Time:
t_total = Σ(t_h + t_n) for all operations
```

### Operation Times (Grundplatte)

| OP | Description | t_h | t_n | Total |
|----|-------------|-----|-----|-------|
| 10 | Planfräsen | 1.9 | 0.8 | 2.7 |
| 20 | Schruppen Außen | 7.2 | 0.8 | 8.0 |
| 30 | Schruppen Innen | 4.0 | 0.8 | 4.8 |
| 40 | Lochkreis | 3.2 | 1.2 | 4.4 |
| 50 | Schlichten Ø120 | 4.3 | 0.8 | 5.1 |
| 60 | Feinbohren Ø26 | 3.3 | 0.8 | 4.1 |
| 70 | Feinbohren Ø44 | 2.3 | 0.8 | 3.1 |
| 80 | Stufenfräsen | 3.1 | 0.8 | 3.9 |
| 90 | Gewindefräsen | 2.4 | 1.0 | 3.4 |
| 100 | Anfasen | 1.5 | 0.8 | 2.3 |
| **Total** | | **33.2** | **8.6** | **41.8** |

### Tool Wear Calculation

```
Kosten/Teil = (Werkzeugpreis / Standzeit) × Einsatzzeit

Example T2 (VHM-Fräser Ø20):
- Price: €120
- Tool life: 180 min
- Usage: 11.2 min/part
→ €120 / 180 × 11.2 = €7.47/part
```

### Material Factors

| Material | Density | vc Factor | Tool Life Factor |
|----------|---------|-----------|------------------|
| 1.4571 | 8.0 kg/dm³ | 0.6 | 0.7 |
| 1.4301 | 7.9 | 0.65 | 0.75 |
| AlMg3 | 2.66 | 2.5 | 1.5 |
| S235 | 7.85 | 1.0 | 1.0 |
| 42CrMo4 | 7.85 | 0.7 | 0.8 |

---

## Data Models

### Project Data

```json
{
  "project": {
    "name": "Grundplatte",
    "number": "WCAD-15-02-2020",
    "description": "Zahnradpumpe",
    "created": "2026-02-02",
    "status": "active"
  },
  "part": {
    "material": "1.4571",
    "raw": { "diameter": 135, "height": 50 },
    "finished": { "diameter": 120, "height": 42 },
    "weight": 1.903,
    "tolerances": [
      { "feature": "Außen-Ø", "nominal": 120, "type": "h5", "upper": 0, "lower": -0.018 },
      { "feature": "Bohrung", "nominal": 26, "type": "H7", "upper": 0.021, "lower": 0 },
      { "feature": "Bohrung", "nominal": 44, "type": "H7", "upper": 0.025, "lower": 0 }
    ]
  },
  "machine": {
    "name": "FEHLMANN VERSA 943",
    "control": "Heidenhain TNC 640",
    "rapidTraverse": 40000,
    "toolChangeTime": 0.5
  },
  "operations": [
    {
      "number": 10,
      "name": "Planfräsen Oberseite",
      "tool": "T1",
      "params": { "n": 800, "f": 300, "ap": 0.5 },
      "time": { "cutting": 1.9, "non_cutting": 0.8 },
      "critical": false
    }
    // ... more operations
  ],
  "tools": [
    {
      "number": "T1",
      "name": "Planfräser (5 WSP)",
      "diameter": 63,
      "price": 45.00,
      "toolLife": 120,
      "currentLife": 85
    }
    // ... more tools
  ],
  "totals": {
    "time": 41.8,
    "setupTime": 30,
    "firstPartTime": 71.8,
    "partsPerShift": 14,
    "cuttingTimeRatio": 0.79
  }
}
```

---

## Component Reference

### Cards

```html
<div class="card">
    <div class="card-header">
        <span class="card-title">📐 Title</span>
        <span class="card-badge">Badge</span>
    </div>
    <div class="card-body">
        <!-- Content -->
    </div>
</div>
```

### Safety Boxes

```html
<div class="safety-box danger|warning|info">
    <span class="safety-icon">🚨|⚠️|ℹ️</span>
    <div class="safety-content">
        <h5>Title</h5>
        <p>Description text</p>
    </div>
</div>
```

### Data Tables

```html
<table class="data-table">
    <thead>
        <tr><th>Column</th></tr>
    </thead>
    <tbody>
        <tr><td class="mono">Monospace value</td></tr>
        <tr class="critical"><td>Critical row</td></tr>
    </tbody>
</table>
```

### Badges

```html
<span class="op-badge">OP10</span>
<span class="op-badge warning">OP50</span>
<span class="card-badge">Label</span>
```

---

## Print Optimization

```css
@media print {
    body { background: white; }
    .container { max-width: 100%; padding: 0; }
    .card { 
        break-inside: avoid; 
        box-shadow: none; 
        border: 1px solid #ddd; 
    }
    .feedback-panel { display: none; }
    .code-container { max-height: none; }
}
```

---

## Future Enhancements

### Planned Features
- [ ] Dynamic Rohmaß → Zeit calculation
- [ ] Multiple project support (Lagerbock, Flansch)
- [ ] PDF export functionality
- [ ] Quote generator integration
- [ ] Real-time tool wear tracking
- [ ] Operator authentication
- [ ] Feedback database backend

### Technical Debt
- [ ] Extract CSS to separate file
- [ ] Add JavaScript bundling
- [ ] Implement state management
- [ ] Add unit tests for calculations

---

*Documentation Version: 1.0*
*Last Updated: 2026-02-02*
*Author: Atlas (OpenClaw)*
