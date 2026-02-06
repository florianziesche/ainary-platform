# Tables - Component Documentation

**Component:** Professional Tables  
**Based on:** Bootstrap 5.3 + MBS Angebot  
**Version:** 1.0  
**Research:** [`RESEARCH-TABELLEN-STYLING.md`](../../RESEARCH-TABELLEN-STYLING.md)

---

## 🎯 Purpose

Display data in structured, scannable rows and columns.

**Usage:**
- Quote positions table
- Operations table (Fertigungsanweisung)
- Material lists
- Calculation breakdowns

---

## 📐 Specifications

### Header:
- Background: `#f8f9fa` (hellgrau)
- Text: 13px, uppercase, 600 weight, 0.05em letter-spacing
- Padding: 8px 12px
- Border-bottom: 2px solid `#D1D5DB`

### Body:
- Text: 14px, 400 weight
- Padding: 8px 12px
- Border-bottom: 1px solid `#E5E7EB`
- Hover: `rgba(0, 0, 0, 0.025)` background

### Borders:
- **Horizontal only** (between rows)
- NO vertical borders (cleaner look)

---

## 💻 Basic Table

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
    <tr>
      <td>2</td>
      <td>Welle</td>
      <td class="right">EUR 45,10</td>
    </tr>
  </tbody>
</table>
```

---

## 🎨 CSS

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

/* Utility Classes */
.table .right {
  text-align: right;
}

.table .center {
  text-align: center;
}

.table .mono {
  font-family: var(--font-mono);
  font-size: var(--text-sm);
}
```

---

## 🧩 Variants

### Quote Table (6 Spalten)

```html
<table class="table">
  <thead>
    <tr>
      <th style="width: 50px;">Pos</th>
      <th style="width: 100px;">Artikelnr.</th>
      <th>Bezeichnung</th>
      <th class="right" style="width: 80px;">Menge</th>
      <th class="right" style="width: 100px;">Einzelpreis</th>
      <th class="right" style="width: 100px;">Gesamtpreis</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class="position-nr">1</td>
      <td class="mono">E-CNC-0001</td>
      <td>
        <div class="part-name">Verbindungsplatte</div>
        <div class="drawing-number">2500473.01.11.02.00.001</div>
        <div class="material">Werkstoff S235JR</div>
      </td>
      <td class="right mono">29 Stck.</td>
      <td class="right mono">EUR 26,30</td>
      <td class="right mono">EUR 762,70</td>
    </tr>
  </tbody>
</table>
```

**Additional CSS:**
```css
.position-nr {
  width: 50px;
  text-align: right;
  font-weight: normal;
  font-variant-numeric: tabular-nums;
}

.part-name {
  font-weight: 600;
  font-size: 14px;
  color: #000;
}

.drawing-number {
  font-size: 13px;
  color: #374151;
  font-family: var(--font-mono);
  margin-top: 2px;
}

.material {
  font-size: 13px;
  color: #6B7280;
  margin-top: 2px;
}
```

---

### Operations Table

```html
<table class="table">
  <thead>
    <tr>
      <th>OP</th>
      <th>Arbeitsgang</th>
      <th class="right">Hauptzeit</th>
      <th class="right">Nebenzeit</th>
      <th class="right">Gesamt</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>OP10</strong></td>
      <td>Rohteil sägen</td>
      <td class="right mono">2,5 min</td>
      <td class="right mono">1,0 min</td>
      <td class="right mono">3,5 min</td>
    </tr>
    <tr>
      <td><strong>OP20</strong></td>
      <td>Planfräsen Oberseite</td>
      <td class="right mono">4,2 min</td>
      <td class="right mono">0,8 min</td>
      <td class="right mono">5,0 min</td>
    </tr>
  </tbody>
</table>
```

---

## 🔢 Numeric Alignment

For columns with numbers, use `font-variant-numeric: tabular-nums` for perfect alignment:

```css
.table .numeric {
  font-variant-numeric: tabular-nums;
  text-align: right;
}
```

**Apply to:**
- Preise
- Mengen
- Zeiten
- Positionen

---

## ⚠️ Don'ts

❌ **Zebra-Stripes by default:**
```css
/* NICHT nutzen außer >6 Spalten! */
.table tbody tr:nth-child(even) {
  background: #f9fafb;
}
```

❌ **Vertical Borders:**
```css
/* NIEMALS! */
.table td {
  border-right: 1px solid #ddd;
}
```

❌ **Zu kleine Padding:**
```css
/* Zu eng! */
.table td {
  padding: 4px;
}
```

---

## 📏 Column Width Guidelines

**Fixed Widths:**
- Position: 50px
- Artikelnummer: 100px
- Menge: 80px
- Preise: 100px

**Flexible:**
- Bezeichnung: Rest (fluid)

**Implementation:**
```html
<th style="width: 50px;">Pos</th>
<th style="width: 100px;">Artikelnr.</th>
<th>Bezeichnung</th>  <!-- Fluid -->
<th class="right" style="width: 100px;">Preis</th>
```

---

## 🧪 Testing Checklist

- [ ] Header background `#f8f9fa`
- [ ] Header text uppercase
- [ ] Padding 8px 12px
- [ ] Hover effect works
- [ ] Numbers align right
- [ ] Long text doesn't break layout
- [ ] Print-friendly (no background on print)

---

## 📚 Examples in Code

**Used in:**
- `demo-v16-complete.html` (Fertigungsanweisung)
- `REQUIREMENTS-V18-FINAL.md` (Quote Template)
- `cnc-planner-pro-v18-industrial.html` (WIP)

---

## 🔗 Related

- [Design System](../DESIGN-SYSTEM.md)
- [RESEARCH-TABELLEN-STYLING.md](../../RESEARCH-TABELLEN-STYLING.md)
- [MBS-ANGEBOT-LINE-BY-LINE.md](../../research/MBS-ANGEBOT-LINE-BY-LINE.md)

---

*Last Updated: 2026-02-06*
