# CNC Planer Pro - Design System Documentation

**Version:** 1.0  
**Created:** 2026-02-06  
**Purpose:** Prevent 30x iteration loops through documented standards

---

## 📚 Documentation Index

### 🎨 Core Design System
- **[DESIGN-SYSTEM.md](../DESIGN-SYSTEM.md)** - Master design document (tokens, principles, all components)

### 🏗️ Development Process
- **[DEVELOPMENT-PROCESS.md](../DEVELOPMENT-PROCESS.md)** - How we build features (research → requirements → build → test)

---

## 🧱 Components

### Data Display
- **[TABLES.md](components/TABLES.md)** - Professional tables (Bootstrap-based, MBS-compatible)
- **[CARDS.md](components/CARDS.md)** - Content cards with headers (5 variants: primary, info, success, warning, error)

### Forms (TODO)
- **FORMS.md** - Input fields, labels, validation
- **BUTTONS.md** - Button styles and states

---

## 🎭 Patterns

### Layouts
- **[QUOTE-LAYOUT.md](patterns/QUOTE-LAYOUT.md)** - Complete quote/angebot layout (DIN 5008, 8 sections)

### Features (TODO)
- **CALCULATION-DISPLAY.md** - How to display calculation results
- **OPERATIONS-TABLE.md** - Operations table pattern (Fertigungsanweisung)

---

## 🎨 Design Tokens

### Colors (TODO)
- **COLORS.md** - Complete color palette with usage guidelines

### Typography (TODO)
- **TYPOGRAPHY.md** - Font scales, weights, line heights

### Spacing (TODO)
- **SPACING.md** - 8pt grid system, margins, paddings

---

## 🔬 Research

All design decisions based on real-world analysis:

### Golden Standards
- **[MBS-ANGEBOT-LINE-BY-LINE.md](../research/MBS-ANGEBOT-LINE-BY-LINE.md)** - Real Maschinenbau quote (34KB, 8 pages analyzed)
- **[MBS-DESIGN-ANALYSE.md](../research/MBS-DESIGN-ANALYSE.md)** - Design principles extracted

### Feature Research
- **[RESEARCH-TABELLEN-STYLING.md](../RESEARCH-TABELLEN-STYLING.md)** - Bootstrap table standards
- **[RESEARCH-ZEICHNUNGSNUMMER.md](../RESEARCH-ZEICHNUNGSNUMMER.md)** - Drawing number format & display
- **[RESEARCH-POSITION-NUMMERIERUNG.md](../RESEARCH-POSITION-NUMMERIERUNG.md)** - Position numbering (1,2,3 vs 10,20,30)
- **[RESEARCH-PREIS-FORMATIERUNG.md](../RESEARCH-PREIS-FORMATIERUNG.md)** - EUR X.XXX,XX format
- **[RESEARCH-GÜLTIGKEIT.md](../RESEARCH-GÜLTIGKEIT.md)** - Offer validity (4 weeks standard)
- **[RESEARCH-BEDINGUNGEN-TEXT.md](../RESEARCH-BEDINGUNGEN-TEXT.md)** - Terms & conditions text
- **[RESEARCH-DEUTSCHE-FORMATIERUNG.md](../RESEARCH-DEUTSCHE-FORMATIERUNG.md)** - Complete German formatting library
- **[RESEARCH-FOOTER-RECHTLICHES.md](../RESEARCH-FOOTER-RECHTLICHES.md)** - Legal footer requirements (GmbH § 35a)

---

## 🚀 Quick Start

### Starting a New Feature?

1. **Read the Process:** [DEVELOPMENT-PROCESS.md](../DEVELOPMENT-PROCESS.md)
2. **Find Golden Standard:** Check `research/` for similar features
3. **Check Design System:** [DESIGN-SYSTEM.md](../DESIGN-SYSTEM.md) - Use existing components
4. **Write Requirements:** See `REQUIREMENTS-V18-FINAL.md` as template
5. **Get Approval:** Florian must say "GO" before coding
6. **Build:** Follow documented standards (NO inline styles!)
7. **Test:** Complete checklist in requirements
8. **Document:** Update relevant docs

---

## ⚠️ Rules

### DO:
✅ Use CSS classes from Design System  
✅ Use CSS variables for colors/spacing  
✅ Follow 8pt grid system  
✅ System fonts only (no Google Fonts)  
✅ Research before building  
✅ Document everything  

### DON'T:
❌ Inline styles  
❌ Direct hex codes  
❌ Direct pixel values  
❌ Google Fonts  
❌ Build without research  
❌ Skip documentation  

---

## 📊 Component Usage

| Component | Used In | Count |
|-----------|---------|-------|
| Cards | Calculation section | 4 |
| Cards | Instructions | 1 |
| Cards | Quote | 1 |
| Tables | Operations table | 1 |
| Tables | Quote table | 1 |
| Forms | Parameter inputs | 8+ |
| Buttons | Navigation | 10+ |

---

## 🔄 Version History

- **v1.0** (2026-02-06) - Initial design system documentation
  - Components: Tables, Cards
  - Patterns: Quote Layout
  - Research: 8 complete analyses
  - Process: Development workflow defined

---

## 📞 Questions?

**Not sure which component to use?**  
→ Check [DESIGN-SYSTEM.md](../DESIGN-SYSTEM.md)

**Need a new component?**  
→ Follow [DEVELOPMENT-PROCESS.md](../DEVELOPMENT-PROCESS.md) Phase 1-2 (Research + Design System Update)

**Component doesn't exist?**  
→ Find golden standard → Analyze → Document → Build

---

## 🎯 Next Steps

**TODOs for complete Design System:**

- [ ] FORMS.md component doc
- [ ] BUTTONS.md component doc
- [ ] COLORS.md token doc
- [ ] SPACING.md token doc
- [ ] TYPOGRAPHY.md token doc
- [ ] CALCULATION-DISPLAY.md pattern
- [ ] OPERATIONS-TABLE.md pattern

**Priority:** Build as needed, document immediately.

---

*Maintainer: Mia*  
*Last Updated: 2026-02-06*  
*Living Document: Update after every new component*
