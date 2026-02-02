# CNC Planner Pro — Changelog

*Complete version history and change documentation.*

---

## Version Overview

| Version | Date | Design Style | Status |
|---------|------|--------------|--------|
| v1-v4 | Jan 2026 | Early iterations | 🗄️ Archived |
| v5 | 2026-02-01 | Dark theme app | 🗄️ Archived |
| v6 | 2026-02-02 | Light theme app | 🗄️ Archived |
| demo-final | 2026-02-02 | Sidebar app + enhancements | ⏸️ Superseded |
| demo-enhanced | 2026-02-02 | New sidebar design | ❌ Rejected |
| **v7** | **2026-02-02** | **Landing page document** | ✅ **Current** |

---

## [v7] — 2026-02-02 (CURRENT)

**File:** `demo-v7.html`
**Design:** Landing page style (clean cards, no sidebar)
**Status:** ✅ Active

### Overview
Complete redesign to match the landing page aesthetic. The demo is now a **document-style Fertigungsanweisung** rather than an app interface. Optimized for printing and presentation.

### Added
- ✅ **Document Header** — Gradient header with metadata grid and QR code
- ✅ **Feedback Panel** — Operator feedback with star ratings and tags
- ✅ **Progress Bar** — Visual time distribution across all 10 operations
- ✅ **Stats Grid** — 4-column key metrics (Zeit, Teile/Schicht, Schnittzeit%, Rüstzeit)
- ✅ **Werkstückübersicht** — Technical drawing (SVG) + critical dimensions
- ✅ **Material Card** — Material info with Chargen-Nr. input field
- ✅ **Zeitberechnung Table** — Complete with formulas and mini progress bars
- ✅ **Werkzeugliste** — Full tool data with Tool Life Bars (good/warning/critical)
- ✅ **Bearbeitungsablauf** — Operation cards with params and time badges
- ✅ **Checklisten** — Interactive "Vor dem Start" + "Prüfintervalle"
- ✅ **Safety Box** — Kaltverfestigung warning for 1.4571
- ✅ **Korrekturwerte Grid** — Correction values for Ø120, Ø26, Ø44
- ✅ **Troubleshooting Table** — Problem → Cause → Solution
- ✅ **NC-Code Block** — Syntax-highlighted with Copy/Download buttons
- ✅ **Print Optimization** — @media print rules for clean output

### Design System
- Colors match `landing-page.html` exactly
- Card-based layout (no sidebar)
- Inter + JetBrains Mono fonts
- Responsive grid (collapses on mobile)

### Files
```
projects/cnc-planner/demo-v7.html (68.7 KB)
```

---

## [demo-enhanced] — 2026-02-02

**File:** `demo-enhanced.html`
**Design:** New sidebar app design
**Status:** ❌ Rejected (didn't match requirements)

### Overview
Created as an enhanced version but with a **new design** instead of building on the existing reference. User feedback: "Das passt überhaupt nicht."

### Added
- Complete sidebar navigation
- All 7 tabs (Übersicht, Zeitberechnung, Werkzeuge, Bearbeitung, NC-Code, Angebot, Qualität)
- Full NC code with syntax highlighting
- Quote generator with dynamic calculation
- Tool life bars
- Checklists and troubleshooting

### Why Rejected
- Did not match the established design (`app.html` reference)
- Did not match the landing page aesthetic (user's actual requirement)
- Created a new sidebar design instead of enhancing existing

### Files
```
projects/cnc-planner/demo-enhanced.html (107 KB)
```

---

## [demo-final] — 2026-02-02

**File:** `demo-final.html`
**Design:** Sidebar app (based on reference)
**Status:** ⏸️ Superseded by v7

### Overview
Enhanced version of the reference `app.html` design. Added new features while keeping the sidebar app layout.

### Added (enhancements to reference)
- Progress bar in Übersicht tab
- Feedback panel at top of analysis view
- Tool life bars in Werkzeuge tab
- Full Fertigungsanweisung with all 10 operations
- Checklists (Vor dem Start, Prüfintervalle)
- Correction values grid
- Troubleshooting table
- Safety warnings for 1.4571

### CSS Additions
- `.progress-section`, `.progress-bar`, `.progress-segment`
- `.tool-life-bar`, `.tool-life-fill.good/warning/critical`
- `.feedback-panel`, `.feedback-item`
- `.correction-grid`, `.correction-card`
- `.checklist`, `.checkbox-icon`
- `.safety-box.danger/warning/info`
- `.troubleshoot-table`

### JavaScript Additions
- `toggleCheck(item)` — Checklist interaction
- `showFeedbackForm()` — Feedback modal placeholder

### Files
```
projects/cnc-planner/demo-final.html
projects/cnc-planner/demo-final-backup.html (original before edits)
```

---

## [v6] — 2026-02-02

**File:** `app-v6.html`
**Design:** Light theme sidebar app
**Status:** 🗄️ Archived

### Changes from v5
- Switched from dark to light theme
- Attempted Rohmaß → Zeit calculation (incomplete)
- Refined color palette

### Issues
- Rohmaß calculation not fully implemented
- Only Grundplatte project functional

---

## [v5] — 2026-02-01

**File:** `app-v5.html`
**Design:** Dark theme sidebar app
**Status:** 🗄️ Archived

### Added
- NC code generation for Heidenhain TNC 640
- Dark theme code editor
- Basic syntax highlighting
- 6 tabs structure

### Issues
- Dark theme didn't match industrial aesthetic
- Code display too limited

---

## [v1-v4] — January 2026

**Files:** `app-v1.html` through `app-v4.html`
**Status:** 🗄️ Archived (some lost)

### Evolution
- v1: Initial concept, basic structure
- v2: PDF upload, basic calculation
- v3: Improved UI, better tables
- v4: Enhanced FA with progress bars

### Notes
- v1 file lost during development
- Iterations focused on finding right UI pattern

---

## Reference Files

### products/cnc-planner/app.html
**Purpose:** Reference design for sidebar app UI
**Status:** 🔒 Reference (do not modify)

### Features
- Dashboard with quick stats
- 3 project cards (Grundplatte, Lagerbock, Flansch)
- Upload area (drag-drop STEP/PDF)
- Processing simulation animation
- 6 tabs: Übersicht, Zeitberechnung, Werkzeugkosten, Maschinencode, FA, Angebot
- Complete Grundplatte data

### products/cnc-planner/landing-page.html
**Purpose:** Marketing landing page
**Status:** 🔒 Reference

### Features
- Hero section with gradient
- Feature grid (6 features)
- ROI calculator
- App demo tabs (Quote, Code, Calculation)
- Pricing cards
- Trust badges

---

## External Reference Files

### /tmp/cnc_ref/Fertigungsanweisung_Grundplatte_V3.html
**Source:** claude_anforderungen_cnc_planner.zip
**Content:** Detailed FA with all features

### Key Features Extracted
- Feedback panel with previous operator feedback
- Progress bar with colored segments
- Detailed time table with mini progress
- Technical drawing (SVG)
- Dimension cards with tolerances
- Material card with certification field
- Tool table with life bars
- Operation flow cards
- Correction values
- Troubleshooting table
- Checklists

### /tmp/cnc_ref/Zeitberechnung_mit_Angebot.html
**Source:** claude_anforderungen_cnc_planner.zip
**Content:** Time calculation + quote generator

### Key Features Extracted
- Calculation formulas
- Machine data (FEHLMANN VERSA 943)
- Detailed time breakdown table
- Quote form with editable fields
- Dynamic price calculation
- Summary cards

### /tmp/cnc_ref/GRUNDPLATTE.H
**Source:** Downloads folder
**Content:** Complete Heidenhain TNC 640 NC code

### Operations Included
- BLK FORM (Rohteil Ø135×50)
- OP10-OP100 complete
- CYCL DEF for all operations
- Contour labels (LBL 1, LBL 2)

---

## Migration Guide

### From demo-final to v7
If you had customizations in demo-final:

1. **Content** transfers directly (same data)
2. **Styling** needs CSS class updates:
   - `.instruction-card` → `.op-card`
   - `.tip-icon` → removed (use emoji in text)
   - `.tab-panel` → `.card` sections
3. **JavaScript** — Only `toggleCheck()` and NC copy/download remain

### Printing
- v7 is print-optimized by default
- demo-final requires print CSS additions

---

## Known Issues

### Current (v7)
- NC code is abbreviated (shows key sections only)
- No dynamic Rohmaß → Zeit calculation yet
- Single project only (Grundplatte)
- No backend/database

### Planned Fixes
- [ ] Expand NC code to full version
- [ ] Add all 3 example projects
- [ ] Implement Rohmaß calculation
- [ ] Add quote generator

---

## Contributors

- **Florian Ziesche** — Project owner, requirements
- **Atlas (OpenClaw)** — Development, documentation

---

*Changelog Version: 1.0*
*Last Updated: 2026-02-02*
