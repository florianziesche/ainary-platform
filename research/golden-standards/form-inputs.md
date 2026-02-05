# Golden Standard: Form Inputs (Industrial Software)

*Basierend auf SAP Fiori, Autodesk, Siemens NX, Paperless Parts*

---

## 1. Input Dimensionen

### Standard Heights
```css
--input-height-sm: 32px;   /* Compact/Tables */
--input-height-md: 40px;   /* Standard */
--input-height-lg: 48px;   /* Hero inputs */
```

### Touch Targets
- Minimum: 44×44px (Apple HIG)
- Desktop: 40px height ist OK
- Mobile: Immer 44px+

---

## 2. Text Input

### Base Styling
```css
.input {
    height: 40px;
    padding: 0 12px;
    font-size: 14px;
    font-family: var(--font-sans);
    color: var(--color-gray-900);
    background: var(--color-surface);
    border: 1px solid var(--color-gray-300);
    border-radius: 6px;
    transition: all 150ms ease;
}

.input::placeholder {
    color: var(--color-gray-400);
}
```

### States
```css
/* Hover */
.input:hover {
    border-color: var(--color-gray-400);
}

/* Focus */
.input:focus {
    outline: none;
    border-color: var(--color-primary);
    box-shadow: 0 0 0 3px rgba(30, 58, 95, 0.1);
}

/* Error */
.input.error {
    border-color: var(--color-error);
}

.input.error:focus {
    box-shadow: 0 0 0 3px rgba(220, 38, 38, 0.1);
}

/* Disabled */
.input:disabled {
    background: var(--color-gray-100);
    color: var(--color-gray-500);
    cursor: not-allowed;
}
```

---

## 3. Number Input (mit Unit)

### Pattern: Input + Unit Suffix
```html
<div class="input-with-unit">
    <input type="number" class="input" value="440">
    <span class="input-unit">mm</span>
</div>
```

```css
.input-with-unit {
    position: relative;
    display: inline-flex;
}

.input-with-unit .input {
    padding-right: 40px;
    font-family: var(--font-mono);
    text-align: right;
}

.input-unit {
    position: absolute;
    right: 12px;
    top: 50%;
    transform: translateY(-50%);
    font-size: 13px;
    color: var(--color-gray-500);
    pointer-events: none;
}
```

### Für CNC Planner: Immer rechts ausrichten
- Zahlen: Monospace
- Unit: Grau, rechts
- Alignment: Right

---

## 4. Select/Dropdown

### Base Styling
```css
.select {
    height: 40px;
    padding: 0 36px 0 12px;
    font-size: 14px;
    color: var(--color-gray-900);
    background: var(--color-surface);
    border: 1px solid var(--color-gray-300);
    border-radius: 6px;
    cursor: pointer;
    appearance: none;
    background-image: url("data:image/svg+xml,...chevron...");
    background-repeat: no-repeat;
    background-position: right 12px center;
    background-size: 16px;
}
```

### Grouped Options
```html
<select class="select">
    <optgroup label="Edelstahl">
        <option value="1.4301">1.4301 (V2A)</option>
        <option value="1.4571">1.4571</option>
    </optgroup>
    <optgroup label="Baustahl">
        <option value="S235JR">S235JR</option>
    </optgroup>
</select>
```

---

## 5. Labels

### Position: OBEN (Standard)
```css
.form-group {
    margin-bottom: 16px;
}

.form-label {
    display: block;
    margin-bottom: 6px;
    font-size: 13px;
    font-weight: 500;
    color: var(--color-gray-700);
}

/* Optional: Uppercase für Categories */
.form-label-caps {
    font-size: 11px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: var(--color-gray-500);
}
```

### Required Indicator
```css
.form-label.required::after {
    content: " *";
    color: var(--color-error);
}
```

---

## 6. Checkbox + Related Input

### Pattern für "Sägen: [ ] 3 min"
```html
<label class="checkbox-with-input">
    <input type="checkbox" class="checkbox">
    <span class="checkbox-label">Sägen</span>
    <input type="number" class="input input-sm" value="3">
    <span class="input-unit">min</span>
</label>
```

```css
.checkbox-with-input {
    display: flex;
    align-items: center;
    gap: 8px;
}

.checkbox {
    width: 18px;
    height: 18px;
    accent-color: var(--color-primary);
    cursor: pointer;
}

.checkbox-label {
    font-size: 14px;
    color: var(--color-gray-700);
}

.input-sm {
    width: 64px;
    height: 32px;
    padding: 0 8px;
    font-size: 13px;
}
```

---

## 7. Dimension Input Group

### Pattern für L × B × H
```html
<div class="dimension-group">
    <div class="dimension-input">
        <label class="form-label">Länge</label>
        <div class="input-with-unit">
            <input type="number" class="input" value="440">
            <span class="input-unit">mm</span>
        </div>
    </div>
    <span class="dimension-separator">×</span>
    <div class="dimension-input">
        <label class="form-label">Breite</label>
        <div class="input-with-unit">
            <input type="number" class="input" value="50">
            <span class="input-unit">mm</span>
        </div>
    </div>
    <span class="dimension-separator">×</span>
    <div class="dimension-input">
        <label class="form-label">Höhe</label>
        <div class="input-with-unit">
            <input type="number" class="input" value="20">
            <span class="input-unit">mm</span>
        </div>
    </div>
</div>
```

```css
.dimension-group {
    display: flex;
    align-items: flex-end;
    gap: 8px;
}

.dimension-input {
    flex: 1;
}

.dimension-separator {
    padding-bottom: 10px;
    color: var(--color-gray-400);
    font-size: 16px;
}
```

---

## 8. Validation

### Real-Time (Industrial Standard)
- Validierung bei `oninput` oder `onchange`
- NICHT bei Blur (zu spät)
- Sofortiges Feedback

### Error Display
```css
.input.error {
    border-color: var(--color-error);
}

.form-error {
    font-size: 12px;
    color: var(--color-error);
    margin-top: 4px;
}
```

### Success Indicator (Optional)
```css
.input.success {
    border-color: var(--color-success);
}
```

---

## 9. Grouping: Cards vs. Sections

### Card (für zusammengehörige Inputs)
```css
.form-card {
    background: var(--color-surface);
    border: 1px solid var(--color-gray-200);
    border-radius: 8px;
    padding: 20px;
    margin-bottom: 16px;
}

.form-card-title {
    font-size: 14px;
    font-weight: 600;
    color: var(--color-gray-800);
    margin-bottom: 16px;
    padding-bottom: 12px;
    border-bottom: 1px solid var(--color-gray-100);
}
```

### Section (für logische Gruppen)
```css
.form-section {
    margin-bottom: 32px;
}

.form-section-title {
    font-size: 11px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: var(--color-gray-500);
    margin-bottom: 12px;
}
```

---

## 10. CNC Planner Pro Empfehlungen

### Parameter-Panel
```
┌─────────────────────────────┐
│ WERKSTÜCK                   │ ← Section Title
├─────────────────────────────┤
│ Werkstoff: [Dropdown    ▼]  │
│                             │
│ Maße:                       │
│ [440] mm × [50] mm × [20] mm│
│                             │
│ Stückzahl: [1]              │
└─────────────────────────────┘

┌─────────────────────────────┐
│ FERTIGUNG                   │
├─────────────────────────────┤
│ Spannung: [Schraubstock ▼]  │
│ Aufspannungen: [2       ▼]  │
│                             │
│ ☑ Entgraten [5] min        │
│ ☐ Sägen     [3] min        │
└─────────────────────────────┘
```

### Input Breiten
- Full-width: Dropdowns
- Fixed 80px: Zahlen mit Unit
- Fixed 64px: Kleine Zahlen (Stückzahl)

---

*Golden Standard v1.0*
