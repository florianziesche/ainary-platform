# CNC Planner Pro — Project Files

## Quick Reference

| What | File |
|------|------|
| **Current Demo** | `demo-v7.html` |
| **Technical Docs** | `TECHNICAL_DOCS.md` |
| **Version History** | `CHANGELOG.md` |
| **Reference Design** | `../products/cnc-planner/app.html` |
| **Landing Page** | `../products/cnc-planner/landing-page.html` |

## Demo v7 — Current Version

**Open in browser:**
```bash
open demo-v7.html
```

**Features:**
- Landing page design (clean cards, no sidebar)
- Complete Fertigungsanweisung document
- Progress bar with 10 operations
- Tool life bars
- Interactive checklists
- NC code with copy/download
- Print-optimized

## File Structure

```
projects/cnc-planner/
├── README.md              # This file
├── TECHNICAL_DOCS.md      # Full technical documentation
├── CHANGELOG.md           # Version history
├── demo-v7.html           # ✅ CURRENT VERSION
├── demo-final.html        # Sidebar app version (superseded)
├── demo-final-backup.html # Backup
└── demo-enhanced.html     # Rejected design

products/cnc-planner/
├── app.html               # Reference sidebar app
├── landing-page.html      # Marketing page
├── PRICING.md             # Pricing tiers
└── ROI-CALCULATOR.md      # ROI logic
```

## Project Data

**Grundplatte WCAD-15-02-2020**
- Material: 1.4571 (Edelstahl)
- Rohteil: Ø135 × 50 mm
- Fertigmaß: Ø120 × 42 mm
- Gewicht: 1,903 kg
- Bearbeitungszeit: 41,8 min
- 10 Operationen (OP10-OP100)
- Kritische Toleranzen: Ø120 h5, Ø26 H7, Ø44 H7

## Quick Links

- [TECHNICAL_DOCS.md](./TECHNICAL_DOCS.md) — Design system, calculations, components
- [CHANGELOG.md](./CHANGELOG.md) — All versions and changes
- [Landing Page](../products/cnc-planner/landing-page.html) — Design reference

---

*Last Updated: 2026-02-02*
