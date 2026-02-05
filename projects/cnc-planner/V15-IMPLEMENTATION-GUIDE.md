# CNC Planner Pro v15 — Implementation Guide

*Golden Standards → Implementation*

---

## 🎯 Ziel

Eine professionelle, Enterprise-grade Version von CNC Planner Pro mit:
- Sidebar-Navigation
- Klarem Design-System
- Alle v14 Features
- Verbesserte UX

---

## 📐 Architektur

### File Structure
```
demo-v15.html (Single File)
├── <head>
│   ├── Meta + Title
│   ├── Google Fonts (Inter, JetBrains Mono)
│   └── <style> (CSS Variables + Components)
├── <body>
│   ├── .app (Flex Container)
│   │   ├── .sidebar (260px, fixed)
│   │   │   ├── .sidebar-header (Logo)
│   │   │   ├── .sidebar-nav (Sections)
│   │   │   └── .sidebar-footer (Settings)
│   │   └── .main (flex: 1)
│   │       ├── .main-header (Title + Actions)
│   │       └── .main-content (Sections)
│   └── <script>
│       ├── Data (MATERIALS, PROJECTS, RATES)
│       ├── State (currentProject, settings)
│       └── Functions (calculate, render, export)
```

---

## 🎨 CSS Variables (Final)

```css
:root {
    /* Colors - Primary */
    --color-primary: #1E3A5F;
    --color-primary-hover: #152A45;
    --color-primary-light: #2D5A8A;
    
    /* Colors - Semantic */
    --color-success: #059669;
    --color-warning: #D97706;
    --color-error: #DC2626;
    
    /* Colors - Neutrals */
    --color-bg: #F8FAFC;
    --color-surface: #FFFFFF;
    --color-border: #E2E8F0;
    --color-border-light: #F1F5F9;
    
    /* Colors - Text */
    --color-text: #1E293B;
    --color-text-secondary: #64748B;
    --color-text-muted: #94A3B8;
    
    /* Typography */
    --font-sans: 'Inter', -apple-system, sans-serif;
    --font-mono: 'JetBrains Mono', monospace;
    
    /* Spacing (8px base) */
    --space-1: 4px;
    --space-2: 8px;
    --space-3: 12px;
    --space-4: 16px;
    --space-5: 20px;
    --space-6: 24px;
    --space-8: 32px;
    
    /* Sizes */
    --sidebar-width: 260px;
    --header-height: 56px;
    --input-height: 40px;
    --btn-height: 36px;
    
    /* Radius */
    --radius-sm: 4px;
    --radius-md: 6px;
    --radius-lg: 8px;
    
    /* Shadows */
    --shadow-sm: 0 1px 2px rgba(0,0,0,0.05);
    --shadow-md: 0 4px 6px rgba(0,0,0,0.07);
}
```

---

## 🏗️ Component Specifications

### 1. Sidebar

**Dimensions:**
- Width: 260px
- Logo height: 56px
- Nav item height: 36px
- Nav item padding: 8px 12px
- Icon size: 20px

**States:**
- Default: `--color-text-secondary`
- Hover: `--color-bg`, `--color-text`
- Active: `--color-primary`, `white`

### 2. Form Inputs

**Dimensions:**
- Height: 40px
- Padding: 0 12px
- Border-radius: 6px
- Font-size: 14px

**With Unit:**
- Padding-right: 40px
- Unit: 13px, `--color-text-muted`

### 3. Price Hero

**Dimensions:**
- Padding: 32px
- Border-radius: 12px
- Price font: 48px, 700 weight
- Label: 14px
- Detail: 13px

### 4. Cost Breakdown

**Dimensions:**
- Row padding: 12px 16px
- Label: 14px
- Formula: 12px, `--font-mono`, muted
- Value: 14px, 500 weight, `--font-mono`

### 5. Cards

**Dimensions:**
- Padding: 20px (compact) / 24px (standard)
- Border-radius: 8px
- Header padding-bottom: 12px
- Header border: 1px solid `--color-border-light`

---

## 📱 Sections (Sidebar → Content)

### Section: Teil auswählen
```
┌─────────────────────────────────────────┐
│ TEIL AUSWÄHLEN                          │
├─────────────────────────────────────────┤
│ ┌─────────────┐ ┌─────────────┐        │
│ │ [Thumbnail] │ │ [Thumbnail] │        │
│ │ Verbindungs │ │ Adapter-    │        │
│ │ platte      │ │ platte      │        │
│ │ S235JR      │ │ AlMg3       │        │
│ │ €28,40      │ │ €52,15      │        │
│ └─────────────┘ └─────────────┘        │
│                                         │
│ ℹ️ Anwendungsbereich: Prismatische...   │
└─────────────────────────────────────────┘
```

### Section: Parameter
```
┌─────────────────────────────────────────┐
│ PARAMETER                               │
├─────────────────────────────────────────┤
│ ┌─────────────────────────────────────┐ │
│ │ WERKSTÜCK                           │ │
│ │ Werkstoff: [Dropdown          ▼]    │ │
│ │ Länge × Breite × Höhe               │ │
│ │ [440]mm × [50]mm × [20]mm           │ │
│ │ Stückzahl: [1]                      │ │
│ └─────────────────────────────────────┘ │
│                                         │
│ ┌─────────────────────────────────────┐ │
│ │ FERTIGUNG                           │ │
│ │ Spannung: [Schraubstock       ▼]    │ │
│ │ Aufspannungen: [2             ▼]    │ │
│ │ Einrichtzeit: 25 min = €35,42       │ │
│ │                                     │ │
│ │ ☑ Entgraten [5] min                │ │
│ │ ☐ Sägen     [3] min                │ │
│ └─────────────────────────────────────┘ │
└─────────────────────────────────────────┘
```

### Section: Ergebnis
```
┌─────────────────────────────────────────┐
│ ERGEBNIS                                │
├─────────────────────────────────────────┤
│ ┌─────────────────────────────────────┐ │
│ │ ░░░░░░░░ STÜCKPREIS ░░░░░░░░       │ │
│ │ ░░░░░░░░ €64,89     ░░░░░░░░       │ │
│ │ ░░░░ inkl. Material & Fertigung ░░░ │ │
│ └─────────────────────────────────────┘ │
│                                         │
│ ┌──────────────────┐ ┌────────────────┐ │
│ │ KOSTENAUFSCHL.   │ │ MENGENSTAFFEL  │ │
│ │ Material  €14,93 │ │ 1 Stk  €64,89  │ │
│ │ Bearbeit. €18,96 │ │ 5 Stk  €45,23  │ │
│ │ Einricht. €22,75 │ │ 10 Stk €38,45  │ │
│ │ Werkzeug  €20,74 │ │                │ │
│ │ ────────────────│ │                │ │
│ │ GESAMT    €64,89 │ │                │ │
│ └──────────────────┘ └────────────────┘ │
└─────────────────────────────────────────┘
```

### Section: Angebot
```
┌─────────────────────────────────────────┐
│ ANGEBOT                [PDF] [E-Mail]   │
├─────────────────────────────────────────┤
│ ┌─────────────────────────────────────┐ │
│ │ ANGEBOT ANG-2026-0042               │ │
│ │ ─────────────────────────────────── │ │
│ │ Pos │ Beschreibung    │ Menge │ GP  │ │
│ │ ──────────────────────────────────  │ │
│ │  1  │ Verbindungs...  │    1  │€65  │ │
│ │ ──────────────────────────────────  │ │
│ │                   Summe │ €64,89    │ │
│ │                 + MwSt. │ €12,33    │ │
│ │                  GESAMT │ €77,22    │ │
│ └─────────────────────────────────────┘ │
└─────────────────────────────────────────┘
```

### Section: NC-Code
```
┌─────────────────────────────────────────┐
│ NC-CODE            [Heidenhain][Siemens]│
├─────────────────────────────────────────┤
│ ┌─────────────────────────────────────┐ │
│ │ ; ================================  │ │
│ │ ; VERBINDUNGSPLATTE                 │ │
│ │ ; Werkstoff: S235JR                 │ │
│ │ ; ================================  │ │
│ │ BEGIN PGM VERBINDUNGSPLATTE MM      │ │
│ │                                     │ │
│ │ TOOL CALL 1 Z S1200 F350            │ │
│ │ ...                                 │ │
│ └─────────────────────────────────────┘ │
│                       [Kopieren] [Export]│
└─────────────────────────────────────────┘
```

### Section: Einstellungen
```
┌─────────────────────────────────────────┐
│ EINSTELLUNGEN                           │
├─────────────────────────────────────────┤
│ ┌─────────────────────────────────────┐ │
│ │ STUNDENSÄTZE                        │ │
│ │ Arbeitsgang  │ Lohn  │ Maschine │Sum│ │
│ │ ─────────────────────────────────── │ │
│ │ CNC          │ [49]  │  [42]    │€91│ │
│ │ Sägen        │ [43]  │  [12]    │€55│ │
│ │ Entgraten    │ [32]  │  [4]     │€36│ │
│ └─────────────────────────────────────┘ │
│                                         │
│ ┌─────────────────────────────────────┐ │
│ │ MATERIALPREISE (€/kg)               │ │
│ │ S235JR: [6.79]  1.4301: [8.50]     │ │
│ │ S355J2: [7.50]  1.4571: [14.00]    │ │
│ │ AlMg3:  [6.50]  ...                 │ │
│ └─────────────────────────────────────┘ │
│                                         │
│        [Speichern]  [Zurücksetzen]      │
└─────────────────────────────────────────┘
```

---

## 🔄 JavaScript Structure

```javascript
// ============ CONSTANTS ============
const RATES = { cnc, saegen, entgraten };
const MATERIALS = { /* 18 materials */ };
const PROJECTS = { verbindungsplatte, adapterplatte };
const CLAMPING_TIMES = { schraubstock, tischspannung, nullpunkt };

// ============ STATE ============
let currentProject = null;
let currentSection = 'part';
let settings = loadSettings();

// ============ NAVIGATION ============
function showSection(name) { ... }

// ============ PROJECT ============
function selectProject(id) { ... }

// ============ CALCULATION ============
function calculate() {
    // 1. Material
    const volumeMm3 = ...
    const weightKg = ...
    const materialCost = ...
    
    // 2. Machining
    const machiningTime = ...
    const machineCost = ...
    
    // 3. Setup
    const setupTime = ...
    const setupCost = ...
    
    // 4. Tools
    const toolCost = ...
    
    // 5. Optional Operations
    const additionalCost = ...
    
    // 6. Total
    const totalCost = ...
    const sellPrice = totalCost * (1 + margin);
    
    // 7. Update UI
    updateDisplay();
}

// ============ SETTINGS ============
function saveSettings() { ... }
function loadSettings() { ... }
function resetSettings() { ... }

// ============ EXPORT ============
function generatePDF() { ... }
function exportCSV() { ... }
function copyCode() { ... }

// ============ INIT ============
document.addEventListener('DOMContentLoaded', init);
```

---

## ✅ Implementation Checklist

### Phase 1: Structure
- [ ] HTML skeleton with sidebar + main
- [ ] CSS variables
- [ ] Basic navigation

### Phase 2: Components
- [ ] Sidebar (logo, sections, items)
- [ ] Form inputs (text, number, select, checkbox)
- [ ] Cards
- [ ] Tables
- [ ] Price display

### Phase 3: Sections
- [ ] Teil auswählen
- [ ] Parameter
- [ ] Ergebnis
- [ ] Angebot
- [ ] NC-Code
- [ ] Einstellungen

### Phase 4: Logic
- [ ] Data (Materials, Projects, Rates)
- [ ] Calculation engine
- [ ] Settings persistence
- [ ] Export functions

### Phase 5: Polish
- [ ] Responsive behavior
- [ ] Animations
- [ ] Error handling
- [ ] Documentation

---

## 🚀 Start Implementation

**Command:** Read this guide, then build section by section.

**Rule:** Every component must match the Golden Standard specs.

---

*Guide v1.0 — Ready for Implementation*
