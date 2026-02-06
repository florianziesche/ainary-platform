# Cards - Component Documentation

**Component:** Cards  
**Based on:** v16 Design Standard  
**Version:** 1.0

---

## 🎯 Purpose

Group related content into distinct sections with headers and bodies.

**Usage:**
- Calculation results (Maschinenkalkulation, Materialkalkulation)
- Instructions (Fertigungsanweisung)
- Settings panels
- Data displays

---

## 💻 Basic Card

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

---

## 🎨 CSS

```css
.card {
  background: white;
  border: var(--border-light);
  border-radius: var(--radius-sm);
  margin-bottom: var(--space-6);
  overflow: hidden;
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

.card-header-success {
  background: var(--color-success);
  color: white;
  padding: var(--space-4) var(--space-6);
  font-weight: var(--weight-semibold);
  font-size: var(--text-base);
}

.card-header-warning {
  background: var(--color-warning);
  color: white;
  padding: var(--space-4) var(--space-6);
  font-weight: var(--weight-semibold);
  font-size: var(--text-base);
}

.card-header-error {
  background: var(--color-error);
  color: white;
  padding: var(--space-4) var(--space-6);
  font-weight: var(--weight-semibold);
  font-size: var(--text-base);
}

.card-body {
  padding: var(--space-6);
}
```

---

## 🧩 Header Variants

### Primary (Dunkelgrau)
```html
<div class="card-header-primary">
  <h3>Maschinenzeitkalkulation</h3>
</div>
```
**When:** Wichtige Berechnungen, Hauptinformationen

### Info (Hellgrau)
```html
<div class="card-header-info">
  <h3>Berechnungsgrundlagen</h3>
</div>
```
**When:** Sekundäre Infos, Erklärungen

### Success (Grün)
```html
<div class="card-header-success">
  <h3>Berechnung erfolgreich</h3>
</div>
```
**When:** Erfolgsmeldungen, positive States

### Warning (Orange)
```html
<div class="card-header-warning">
  <h3>Achtung: Grenzwert</h3>
</div>
```
**When:** Warnungen, Hinweise

### Error (Rot)
```html
<div class="card-header-error">
  <h3>Fehler bei Berechnung</h3>
</div>
```
**When:** Fehlermeldungen, kritische States

---

## 📏 Body Variations

### Simple Body
```html
<div class="card-body">
  <p>Einfacher Text.</p>
</div>
```

### With Grid
```html
<div class="card-body">
  <div class="info-grid">
    <div class="info-item">
      <span class="info-label">Maschinenstundensatz:</span>
      <span class="info-value">EUR 91,00/h</span>
    </div>
    <div class="info-item">
      <span class="info-label">Hauptzeit:</span>
      <span class="info-value">16,7 min</span>
    </div>
  </div>
</div>
```

**CSS for Grid:**
```css
.info-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: var(--space-3);
}

.info-item {
  display: flex;
  justify-content: space-between;
  padding: var(--space-2) 0;
  border-bottom: 1px solid var(--color-gray-200);
}

.info-item:last-child {
  border-bottom: none;
}

.info-label {
  color: var(--color-gray-700);
  font-size: var(--text-sm);
}

.info-value {
  font-family: var(--font-mono);
  font-size: var(--text-sm);
  font-weight: var(--weight-semibold);
  color: var(--color-black);
}
```

---

## 🔢 Data Display Card (Calculation)

```html
<div class="card">
  <div class="card-header-primary">
    <h3>Maschinenzeitkalkulation</h3>
  </div>
  <div class="card-body">
    <div class="info-grid">
      <div class="info-item">
        <span class="info-label">Hauptzeit (th):</span>
        <span class="info-value">16,7 min</span>
      </div>
      <div class="info-item">
        <span class="info-label">Nebenzeit (tn):</span>
        <span class="info-value">3,5 min</span>
      </div>
      <div class="info-item">
        <span class="info-label">Gesamtzeit (tges):</span>
        <span class="info-value">20,2 min</span>
      </div>
      <div class="info-item total">
        <span class="info-label"><strong>Maschinenkosten:</strong></span>
        <span class="info-value"><strong>EUR 30,63</strong></span>
      </div>
    </div>
  </div>
</div>
```

**Additional CSS:**
```css
.info-item.total {
  border-top: 2px solid var(--color-gray-300);
  padding-top: var(--space-4);
  margin-top: var(--space-2);
}

.info-item.total .info-label,
.info-item.total .info-value {
  font-size: var(--text-base);
  color: var(--color-black);
}
```

---

## ⚠️ Don'ts

❌ **Inline Styles:**
```html
<!-- NIEMALS! -->
<div style="padding: 24px; background: #f9fafb;">
```

❌ **Nested Cards ohne Grund:**
```html
<!-- Vermeide! -->
<div class="card">
  <div class="card">
    <div class="card">...</div>
  </div>
</div>
```

❌ **Zu viele Header-Varianten:**
- Nutze maximal 2-3 pro Page
- Primary für Haupt-Cards
- Info für Details

---

## 📐 Spacing Rules

- **Card margin-bottom:** `var(--space-6)` (24px)
- **Header padding:** `var(--space-4)` vertical, `var(--space-6)` horizontal
- **Body padding:** `var(--space-6)` (24px) alle Seiten

---

## 🧪 Testing Checklist

- [ ] Header hat richtige Farbe (primary/info/etc)
- [ ] Body padding 24px
- [ ] Border-radius 4px
- [ ] Margin-bottom zwischen Cards
- [ ] Text lesbar (contrast check)
- [ ] Print-friendly (keine zu dunklen Backgrounds)

---

## 📚 Examples in Code

**Used in:**
- `demo-v16-complete.html` - Alle Kalkulations-Cards
- Section: `section-calculation` (4 Cards)
- Section: `section-instructions` (1 Card)

---

## 🔗 Related

- [Design System](../DESIGN-SYSTEM.md)
- [DESIGN-STANDARD.md](../../DESIGN-STANDARD.md)
- [TABLES.md](TABLES.md) (Cards oft combined mit Tables)

---

*Last Updated: 2026-02-06*
