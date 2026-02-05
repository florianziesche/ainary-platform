# CNC Planner Pro v15 — Design Specification

**Version:** 15.0  
**Date:** 2026-02-05  
**Design Language:** Enterprise SaaS (Linear/Notion/Figma-inspired)

---

## Table of Contents

1. [Design Principles](#design-principles)
2. [Color System](#color-system)
3. [Typography](#typography)
4. [Spacing & Layout](#spacing--layout)
5. [Component Library](#component-library)
6. [Page Layout Structure](#page-layout-structure)
7. [Interaction Patterns](#interaction-patterns)
8. [Responsive Breakpoints](#responsive-breakpoints)
9. [Implementation Notes](#implementation-notes)

---

## Design Principles

1. **Information Density:** Show what matters, hide what doesn't. No wasted space.
2. **Immediate Feedback:** Costs update in real-time as parameters change.
3. **Settings as First-Class:** Rates and materials are always one click away.
4. **Quiet Confidence:** Muted colors, sharp typography, no gradients or shadows abuse.
5. **Mobile-Native:** Touch targets ≥44px, single-column stacking, swipe-friendly.

---

## Color System

### CSS Variables

```css
:root {
  /* === LIGHT MODE (default) === */
  
  /* Background Layers (darkest to lightest) */
  --color-bg-base: #ffffff;
  --color-bg-subtle: #f9fafb;
  --color-bg-muted: #f3f4f6;
  --color-bg-emphasis: #e5e7eb;
  
  /* Surface (cards, modals, dropdowns) */
  --color-surface: #ffffff;
  --color-surface-raised: #ffffff;
  --color-surface-overlay: rgba(255, 255, 255, 0.95);
  
  /* Border */
  --color-border-default: #e5e7eb;
  --color-border-muted: #f3f4f6;
  --color-border-emphasis: #d1d5db;
  
  /* Text */
  --color-text-primary: #111827;
  --color-text-secondary: #6b7280;
  --color-text-tertiary: #9ca3af;
  --color-text-disabled: #d1d5db;
  --color-text-inverse: #ffffff;
  
  /* Brand / Accent */
  --color-accent-primary: #2563eb;
  --color-accent-primary-hover: #1d4ed8;
  --color-accent-primary-subtle: #dbeafe;
  --color-accent-primary-text: #1e40af;
  
  /* Semantic */
  --color-success: #059669;
  --color-success-subtle: #d1fae5;
  --color-warning: #d97706;
  --color-warning-subtle: #fef3c7;
  --color-error: #dc2626;
  --color-error-subtle: #fee2e2;
  --color-info: #0284c7;
  --color-info-subtle: #e0f2fe;
  
  /* Interactive States */
  --color-focus-ring: rgba(37, 99, 235, 0.5);
  --color-hover-overlay: rgba(0, 0, 0, 0.04);
  --color-active-overlay: rgba(0, 0, 0, 0.08);
  
  /* Shadows */
  --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.05);
  --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
  --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
  --shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
  
  /* Animation */
  --transition-fast: 100ms ease;
  --transition-base: 150ms ease;
  --transition-slow: 250ms ease;
}

/* === DARK MODE === */
[data-theme="dark"] {
  /* Background Layers */
  --color-bg-base: #0f0f0f;
  --color-bg-subtle: #171717;
  --color-bg-muted: #262626;
  --color-bg-emphasis: #404040;
  
  /* Surface */
  --color-surface: #1a1a1a;
  --color-surface-raised: #222222;
  --color-surface-overlay: rgba(26, 26, 26, 0.95);
  
  /* Border */
  --color-border-default: #2e2e2e;
  --color-border-muted: #262626;
  --color-border-emphasis: #404040;
  
  /* Text */
  --color-text-primary: #f5f5f5;
  --color-text-secondary: #a3a3a3;
  --color-text-tertiary: #737373;
  --color-text-disabled: #525252;
  --color-text-inverse: #0f0f0f;
  
  /* Brand / Accent (slightly adjusted for dark) */
  --color-accent-primary: #3b82f6;
  --color-accent-primary-hover: #60a5fa;
  --color-accent-primary-subtle: rgba(59, 130, 246, 0.15);
  --color-accent-primary-text: #93c5fd;
  
  /* Semantic (adjusted for dark backgrounds) */
  --color-success: #10b981;
  --color-success-subtle: rgba(16, 185, 129, 0.15);
  --color-warning: #f59e0b;
  --color-warning-subtle: rgba(245, 158, 11, 0.15);
  --color-error: #ef4444;
  --color-error-subtle: rgba(239, 68, 68, 0.15);
  --color-info: #0ea5e9;
  --color-info-subtle: rgba(14, 165, 233, 0.15);
  
  /* Interactive States */
  --color-focus-ring: rgba(59, 130, 246, 0.5);
  --color-hover-overlay: rgba(255, 255, 255, 0.04);
  --color-active-overlay: rgba(255, 255, 255, 0.08);
  
  /* Shadows (more subtle in dark mode) */
  --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.3);
  --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.4);
  --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.5);
  --shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.6);
}
```

### Color Usage Guidelines

| Use Case | Light Mode | Dark Mode |
|----------|------------|-----------|
| Page background | `--color-bg-subtle` | `--color-bg-base` |
| Cards | `--color-surface` | `--color-surface` |
| Input fields | `--color-bg-base` | `--color-bg-subtle` |
| Primary buttons | `--color-accent-primary` | `--color-accent-primary` |
| Cost total | `--color-success` | `--color-success` |
| Validation errors | `--color-error` | `--color-error` |

---

## Typography

### Font Stack

```css
:root {
  --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  --font-mono: 'JetBrains Mono', 'Fira Code', 'SF Mono', Consolas, monospace;
  
  /* Base size for rem calculations */
  font-size: 16px;
}
```

### Type Scale

```css
:root {
  /* Font Sizes */
  --text-xs: 0.75rem;      /* 12px */
  --text-sm: 0.8125rem;    /* 13px */
  --text-base: 0.875rem;   /* 14px — default body */
  --text-md: 1rem;         /* 16px */
  --text-lg: 1.125rem;     /* 18px */
  --text-xl: 1.25rem;      /* 20px */
  --text-2xl: 1.5rem;      /* 24px */
  --text-3xl: 1.875rem;    /* 30px */
  
  /* Line Heights */
  --leading-none: 1;
  --leading-tight: 1.25;
  --leading-snug: 1.375;
  --leading-normal: 1.5;
  --leading-relaxed: 1.625;
  
  /* Font Weights */
  --font-normal: 400;
  --font-medium: 500;
  --font-semibold: 600;
  --font-bold: 700;
  
  /* Letter Spacing */
  --tracking-tight: -0.025em;
  --tracking-normal: 0;
  --tracking-wide: 0.025em;
}
```

### Typography Classes

```css
/* Headings */
.heading-1 {
  font-size: var(--text-2xl);
  font-weight: var(--font-semibold);
  line-height: var(--leading-tight);
  letter-spacing: var(--tracking-tight);
  color: var(--color-text-primary);
}

.heading-2 {
  font-size: var(--text-xl);
  font-weight: var(--font-semibold);
  line-height: var(--leading-tight);
  color: var(--color-text-primary);
}

.heading-3 {
  font-size: var(--text-lg);
  font-weight: var(--font-medium);
  line-height: var(--leading-snug);
  color: var(--color-text-primary);
}

/* Body */
.body-default {
  font-size: var(--text-base);
  font-weight: var(--font-normal);
  line-height: var(--leading-normal);
  color: var(--color-text-primary);
}

.body-secondary {
  font-size: var(--text-base);
  font-weight: var(--font-normal);
  line-height: var(--leading-normal);
  color: var(--color-text-secondary);
}

/* Labels */
.label {
  font-size: var(--text-sm);
  font-weight: var(--font-medium);
  line-height: var(--leading-normal);
  color: var(--color-text-secondary);
  text-transform: uppercase;
  letter-spacing: var(--tracking-wide);
}

/* Captions & Help Text */
.caption {
  font-size: var(--text-xs);
  font-weight: var(--font-normal);
  line-height: var(--leading-normal);
  color: var(--color-text-tertiary);
}

/* Numbers / Costs */
.number-display {
  font-family: var(--font-mono);
  font-size: var(--text-3xl);
  font-weight: var(--font-semibold);
  line-height: var(--leading-none);
  letter-spacing: var(--tracking-tight);
  font-variant-numeric: tabular-nums;
}

.number-inline {
  font-family: var(--font-mono);
  font-variant-numeric: tabular-nums;
}
```

---

## Spacing & Layout

### Spacing Scale

```css
:root {
  --space-0: 0;
  --space-1: 0.25rem;   /* 4px */
  --space-2: 0.5rem;    /* 8px */
  --space-3: 0.75rem;   /* 12px */
  --space-4: 1rem;      /* 16px */
  --space-5: 1.25rem;   /* 20px */
  --space-6: 1.5rem;    /* 24px */
  --space-8: 2rem;      /* 32px */
  --space-10: 2.5rem;   /* 40px */
  --space-12: 3rem;     /* 48px */
  --space-16: 4rem;     /* 64px */
  
  /* Component-specific */
  --radius-sm: 4px;
  --radius-md: 6px;
  --radius-lg: 8px;
  --radius-xl: 12px;
  --radius-full: 9999px;
}
```

### Layout Grid

```css
.container {
  width: 100%;
  max-width: 1400px;
  margin: 0 auto;
  padding: 0 var(--space-4);
}

@media (min-width: 768px) {
  .container {
    padding: 0 var(--space-6);
  }
}

@media (min-width: 1024px) {
  .container {
    padding: 0 var(--space-8);
  }
}
```

---

## Component Library

### 1. Buttons

```css
/* Base Button */
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: var(--space-2);
  padding: var(--space-2) var(--space-4);
  font-family: var(--font-sans);
  font-size: var(--text-sm);
  font-weight: var(--font-medium);
  line-height: var(--leading-tight);
  border-radius: var(--radius-md);
  border: 1px solid transparent;
  cursor: pointer;
  transition: all var(--transition-fast);
  white-space: nowrap;
  min-height: 36px;
}

.btn:focus-visible {
  outline: none;
  box-shadow: 0 0 0 2px var(--color-bg-base), 0 0 0 4px var(--color-focus-ring);
}

.btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

/* Primary Button */
.btn-primary {
  background: var(--color-accent-primary);
  color: var(--color-text-inverse);
}

.btn-primary:hover:not(:disabled) {
  background: var(--color-accent-primary-hover);
}

.btn-primary:active:not(:disabled) {
  transform: translateY(1px);
}

/* Secondary Button */
.btn-secondary {
  background: var(--color-surface);
  color: var(--color-text-primary);
  border-color: var(--color-border-default);
}

.btn-secondary:hover:not(:disabled) {
  background: var(--color-bg-muted);
  border-color: var(--color-border-emphasis);
}

/* Ghost Button */
.btn-ghost {
  background: transparent;
  color: var(--color-text-secondary);
}

.btn-ghost:hover:not(:disabled) {
  background: var(--color-hover-overlay);
  color: var(--color-text-primary);
}

/* Danger Button */
.btn-danger {
  background: var(--color-error);
  color: var(--color-text-inverse);
}

.btn-danger:hover:not(:disabled) {
  background: #b91c1c;
}

/* Button Sizes */
.btn-sm {
  padding: var(--space-1) var(--space-3);
  font-size: var(--text-xs);
  min-height: 28px;
}

.btn-lg {
  padding: var(--space-3) var(--space-6);
  font-size: var(--text-base);
  min-height: 44px;
}

/* Icon Button */
.btn-icon {
  padding: var(--space-2);
  min-width: 36px;
}

.btn-icon.btn-sm {
  padding: var(--space-1);
  min-width: 28px;
  min-height: 28px;
}
```

**Button HTML Structure:**
```html
<button class="btn btn-primary">Calculate Cost</button>
<button class="btn btn-secondary">
  <svg class="icon">...</svg>
  Export Quote
</button>
<button class="btn btn-ghost btn-icon" aria-label="Settings">
  <svg class="icon">...</svg>
</button>
```

---

### 2. Form Inputs

```css
/* Input Base */
.input {
  width: 100%;
  padding: var(--space-2) var(--space-3);
  font-family: var(--font-sans);
  font-size: var(--text-base);
  line-height: var(--leading-normal);
  color: var(--color-text-primary);
  background: var(--color-bg-base);
  border: 1px solid var(--color-border-default);
  border-radius: var(--radius-md);
  transition: border-color var(--transition-fast), box-shadow var(--transition-fast);
  min-height: 40px;
}

.input::placeholder {
  color: var(--color-text-tertiary);
}

.input:hover:not(:disabled) {
  border-color: var(--color-border-emphasis);
}

.input:focus {
  outline: none;
  border-color: var(--color-accent-primary);
  box-shadow: 0 0 0 3px var(--color-focus-ring);
}

.input:disabled {
  background: var(--color-bg-muted);
  color: var(--color-text-disabled);
  cursor: not-allowed;
}

/* Input with Error */
.input-error {
  border-color: var(--color-error);
}

.input-error:focus {
  box-shadow: 0 0 0 3px rgba(220, 38, 38, 0.25);
}

/* Numeric Input (for dimensions, quantities) */
.input-number {
  font-family: var(--font-mono);
  font-variant-numeric: tabular-nums;
  text-align: right;
}

/* Input with Unit Suffix */
.input-group {
  display: flex;
  align-items: stretch;
}

.input-group .input {
  border-top-right-radius: 0;
  border-bottom-right-radius: 0;
  border-right: none;
}

.input-group .input-suffix {
  display: flex;
  align-items: center;
  padding: 0 var(--space-3);
  font-size: var(--text-sm);
  color: var(--color-text-secondary);
  background: var(--color-bg-muted);
  border: 1px solid var(--color-border-default);
  border-left: none;
  border-radius: 0 var(--radius-md) var(--radius-md) 0;
}

/* Select */
.select {
  appearance: none;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 24 24' fill='none' stroke='%236b7280' stroke-width='2'%3E%3Cpath d='M6 9l6 6 6-6'/%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: right var(--space-3) center;
  padding-right: var(--space-10);
}

/* Form Field Container */
.form-field {
  display: flex;
  flex-direction: column;
  gap: var(--space-1);
}

.form-label {
  font-size: var(--text-sm);
  font-weight: var(--font-medium);
  color: var(--color-text-primary);
}

.form-label-optional {
  font-weight: var(--font-normal);
  color: var(--color-text-tertiary);
}

.form-hint {
  font-size: var(--text-xs);
  color: var(--color-text-tertiary);
}

.form-error {
  font-size: var(--text-xs);
  color: var(--color-error);
}
```

**Form HTML Structure:**
```html
<div class="form-field">
  <label class="form-label" for="length">
    Length <span class="form-label-optional">(mm)</span>
  </label>
  <div class="input-group">
    <input type="number" id="length" class="input input-number" value="250">
    <span class="input-suffix">mm</span>
  </div>
  <span class="form-hint">Maximum: 2000mm</span>
</div>
```

---

### 3. Cards

```css
/* Base Card */
.card {
  background: var(--color-surface);
  border: 1px solid var(--color-border-default);
  border-radius: var(--radius-lg);
}

/* Card Sections */
.card-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: var(--space-4);
  border-bottom: 1px solid var(--color-border-muted);
}

.card-title {
  font-size: var(--text-base);
  font-weight: var(--font-semibold);
  color: var(--color-text-primary);
}

.card-body {
  padding: var(--space-4);
}

.card-footer {
  display: flex;
  align-items: center;
  justify-content: flex-end;
  gap: var(--space-3);
  padding: var(--space-4);
  border-top: 1px solid var(--color-border-muted);
  background: var(--color-bg-subtle);
  border-radius: 0 0 var(--radius-lg) var(--radius-lg);
}

/* Elevated Card (for primary content) */
.card-elevated {
  box-shadow: var(--shadow-md);
  border: none;
}

/* Interactive Card */
.card-interactive {
  cursor: pointer;
  transition: box-shadow var(--transition-fast), border-color var(--transition-fast);
}

.card-interactive:hover {
  border-color: var(--color-border-emphasis);
  box-shadow: var(--shadow-sm);
}

.card-interactive:active {
  background: var(--color-bg-subtle);
}

/* Cost Display Card (special) */
.card-cost {
  background: var(--color-success-subtle);
  border-color: var(--color-success);
}

[data-theme="dark"] .card-cost {
  background: var(--color-success-subtle);
}
```

---

### 4. Tables

```css
/* Table Container (for horizontal scroll on mobile) */
.table-container {
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
}

/* Table */
.table {
  width: 100%;
  border-collapse: collapse;
  font-size: var(--text-sm);
}

.table th,
.table td {
  padding: var(--space-3) var(--space-4);
  text-align: left;
  border-bottom: 1px solid var(--color-border-muted);
}

.table th {
  font-weight: var(--font-medium);
  color: var(--color-text-secondary);
  background: var(--color-bg-subtle);
  white-space: nowrap;
}

.table tbody tr:hover {
  background: var(--color-hover-overlay);
}

.table tbody tr:last-child td {
  border-bottom: none;
}

/* Numeric Columns */
.table td.number {
  font-family: var(--font-mono);
  font-variant-numeric: tabular-nums;
  text-align: right;
}

/* Table with Borders */
.table-bordered {
  border: 1px solid var(--color-border-default);
  border-radius: var(--radius-md);
  overflow: hidden;
}

.table-bordered th,
.table-bordered td {
  border-right: 1px solid var(--color-border-muted);
}

.table-bordered th:last-child,
.table-bordered td:last-child {
  border-right: none;
}

/* Compact Table */
.table-compact th,
.table-compact td {
  padding: var(--space-2) var(--space-3);
}
```

**Table HTML Structure:**
```html
<div class="table-container">
  <table class="table table-bordered">
    <thead>
      <tr>
        <th>Material</th>
        <th>Grade</th>
        <th class="number">Price/kg</th>
        <th class="number">Setup Time</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Aluminum</td>
        <td>6061-T6</td>
        <td class="number">€12.50</td>
        <td class="number">15 min</td>
      </tr>
    </tbody>
  </table>
</div>
```

---

### 5. Tabs

```css
/* Tab Container */
.tabs {
  display: flex;
  flex-direction: column;
}

/* Tab List */
.tab-list {
  display: flex;
  gap: var(--space-1);
  border-bottom: 1px solid var(--color-border-default);
  padding: 0 var(--space-4);
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
  scrollbar-width: none;
}

.tab-list::-webkit-scrollbar {
  display: none;
}

/* Tab Button */
.tab {
  position: relative;
  padding: var(--space-3) var(--space-4);
  font-size: var(--text-sm);
  font-weight: var(--font-medium);
  color: var(--color-text-secondary);
  background: none;
  border: none;
  cursor: pointer;
  white-space: nowrap;
  transition: color var(--transition-fast);
}

.tab:hover {
  color: var(--color-text-primary);
}

.tab[aria-selected="true"] {
  color: var(--color-accent-primary);
}

.tab[aria-selected="true"]::after {
  content: '';
  position: absolute;
  bottom: -1px;
  left: 0;
  right: 0;
  height: 2px;
  background: var(--color-accent-primary);
  border-radius: 2px 2px 0 0;
}

.tab:focus-visible {
  outline: none;
  box-shadow: inset 0 0 0 2px var(--color-focus-ring);
  border-radius: var(--radius-sm);
}

/* Tab Panel */
.tab-panel {
  padding: var(--space-4);
}

.tab-panel[hidden] {
  display: none;
}
```

---

### 6. Badges & Tags

```css
.badge {
  display: inline-flex;
  align-items: center;
  gap: var(--space-1);
  padding: var(--space-1) var(--space-2);
  font-size: var(--text-xs);
  font-weight: var(--font-medium);
  line-height: var(--leading-tight);
  border-radius: var(--radius-full);
  white-space: nowrap;
}

.badge-default {
  background: var(--color-bg-muted);
  color: var(--color-text-secondary);
}

.badge-primary {
  background: var(--color-accent-primary-subtle);
  color: var(--color-accent-primary-text);
}

.badge-success {
  background: var(--color-success-subtle);
  color: var(--color-success);
}

.badge-warning {
  background: var(--color-warning-subtle);
  color: var(--color-warning);
}

.badge-error {
  background: var(--color-error-subtle);
  color: var(--color-error);
}
```

---

### 7. Tooltip

```css
.tooltip {
  position: relative;
}

.tooltip-content {
  position: absolute;
  z-index: 50;
  bottom: calc(100% + 8px);
  left: 50%;
  transform: translateX(-50%);
  padding: var(--space-2) var(--space-3);
  font-size: var(--text-xs);
  color: var(--color-text-inverse);
  background: var(--color-text-primary);
  border-radius: var(--radius-md);
  white-space: nowrap;
  opacity: 0;
  visibility: hidden;
  transition: opacity var(--transition-fast), visibility var(--transition-fast);
}

.tooltip-content::after {
  content: '';
  position: absolute;
  top: 100%;
  left: 50%;
  transform: translateX(-50%);
  border: 6px solid transparent;
  border-top-color: var(--color-text-primary);
}

.tooltip:hover .tooltip-content,
.tooltip:focus-within .tooltip-content {
  opacity: 1;
  visibility: visible;
}
```

---

### 8. Modal / Dialog

```css
/* Backdrop */
.modal-backdrop {
  position: fixed;
  inset: 0;
  z-index: 100;
  background: rgba(0, 0, 0, 0.5);
  backdrop-filter: blur(4px);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: var(--space-4);
}

/* Modal */
.modal {
  position: relative;
  width: 100%;
  max-width: 480px;
  max-height: calc(100vh - var(--space-8));
  background: var(--color-surface);
  border-radius: var(--radius-xl);
  box-shadow: var(--shadow-xl);
  overflow: hidden;
  display: flex;
  flex-direction: column;
}

.modal-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: var(--space-4) var(--space-5);
  border-bottom: 1px solid var(--color-border-muted);
}

.modal-title {
  font-size: var(--text-lg);
  font-weight: var(--font-semibold);
  color: var(--color-text-primary);
}

.modal-close {
  padding: var(--space-1);
  color: var(--color-text-secondary);
  background: none;
  border: none;
  border-radius: var(--radius-sm);
  cursor: pointer;
}

.modal-close:hover {
  background: var(--color-hover-overlay);
  color: var(--color-text-primary);
}

.modal-body {
  padding: var(--space-5);
  overflow-y: auto;
}

.modal-footer {
  display: flex;
  justify-content: flex-end;
  gap: var(--space-3);
  padding: var(--space-4) var(--space-5);
  border-top: 1px solid var(--color-border-muted);
  background: var(--color-bg-subtle);
}

/* Large Modal */
.modal-lg {
  max-width: 640px;
}
```

---

## Page Layout Structure

### Recommended: **Split Panel with Persistent Settings**

```
┌─────────────────────────────────────────────────────────────────┐
│  Header: Logo + App Name              [Dark/Light] [Export]     │
├──────────────────────┬──────────────────────────────────────────┤
│                      │                                          │
│   SETTINGS PANEL     │         MAIN WORKSPACE                   │
│   (240px fixed)      │                                          │
│                      │  ┌─────────────────────────────────────┐ │
│   • Machine Rates    │  │  PART SELECTOR                      │ │
│   • Material Prices  │  │  [Grid of part types]               │ │
│   • Labor Costs      │  └─────────────────────────────────────┘ │
│   • Margins          │                                          │
│                      │  ┌─────────────────────────────────────┐ │
│   ─────────────────  │  │  PARAMETERS                         │ │
│                      │  │  Dimensions | Material | Quantity   │ │
│   Quick Presets      │  └─────────────────────────────────────┘ │
│   • Standard Alum    │                                          │
│   • High Volume      │  ┌─────────────────────────────────────┐ │
│   • Prototype        │  │  COST BREAKDOWN          TOTAL      │ │
│                      │  │  Material: €XX.XX       ┌─────────┐ │ │
│                      │  │  Machining: €XX.XX      │ €XXX.XX │ │ │
│                      │  │  Setup: €XX.XX          └─────────┘ │ │
│                      │  │  Finishing: €XX.XX       per unit   │ │
│                      │  └─────────────────────────────────────┘ │
│                      │                                          │
│                      │  [Generate Quote]                        │
│                      │                                          │
└──────────────────────┴──────────────────────────────────────────┘
```

### Layout CSS

```css
/* App Shell */
.app {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  background: var(--color-bg-subtle);
}

/* Header */
.app-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 56px;
  padding: 0 var(--space-4);
  background: var(--color-surface);
  border-bottom: 1px solid var(--color-border-default);
  flex-shrink: 0;
}

.app-logo {
  display: flex;
  align-items: center;
  gap: var(--space-3);
  font-size: var(--text-base);
  font-weight: var(--font-semibold);
  color: var(--color-text-primary);
}

.app-header-actions {
  display: flex;
  align-items: center;
  gap: var(--space-2);
}

/* Main Layout */
.app-layout {
  display: flex;
  flex: 1;
  overflow: hidden;
}

/* Settings Sidebar */
.sidebar {
  width: 280px;
  flex-shrink: 0;
  background: var(--color-surface);
  border-right: 1px solid var(--color-border-default);
  overflow-y: auto;
  display: flex;
  flex-direction: column;
}

.sidebar-header {
  padding: var(--space-4);
  border-bottom: 1px solid var(--color-border-muted);
}

.sidebar-section {
  padding: var(--space-4);
  border-bottom: 1px solid var(--color-border-muted);
}

.sidebar-section:last-child {
  border-bottom: none;
}

.sidebar-section-title {
  font-size: var(--text-xs);
  font-weight: var(--font-semibold);
  color: var(--color-text-tertiary);
  text-transform: uppercase;
  letter-spacing: var(--tracking-wide);
  margin-bottom: var(--space-3);
}

/* Main Content */
.main-content {
  flex: 1;
  overflow-y: auto;
  padding: var(--space-6);
}

/* Content Sections */
.section {
  margin-bottom: var(--space-6);
}

.section:last-child {
  margin-bottom: 0;
}

.section-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: var(--space-4);
}

.section-title {
  font-size: var(--text-lg);
  font-weight: var(--font-semibold);
  color: var(--color-text-primary);
}

/* Cost Display */
.cost-display {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  padding: var(--space-4);
  background: linear-gradient(135deg, var(--color-success-subtle), transparent);
  border: 1px solid var(--color-success);
  border-radius: var(--radius-lg);
}

.cost-label {
  font-size: var(--text-sm);
  color: var(--color-text-secondary);
  margin-bottom: var(--space-1);
}

.cost-value {
  font-family: var(--font-mono);
  font-size: var(--text-3xl);
  font-weight: var(--font-bold);
  color: var(--color-success);
  letter-spacing: var(--tracking-tight);
}

.cost-suffix {
  font-size: var(--text-sm);
  color: var(--color-text-secondary);
  margin-top: var(--space-1);
}

/* Cost Breakdown */
.cost-breakdown {
  display: grid;
  gap: var(--space-2);
}

.cost-line {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: var(--space-2) 0;
}

.cost-line:not(:last-child) {
  border-bottom: 1px solid var(--color-border-muted);
}

.cost-line-label {
  font-size: var(--text-sm);
  color: var(--color-text-secondary);
}

.cost-line-value {
  font-family: var(--font-mono);
  font-size: var(--text-sm);
  font-weight: var(--font-medium);
  color: var(--color-text-primary);
}
```

### Mobile Layout (Collapsible Sidebar)

```css
/* Mobile: Stack layout */
@media (max-width: 767px) {
  .app-layout {
    flex-direction: column;
  }
  
  .sidebar {
    position: fixed;
    top: 56px;
    left: 0;
    bottom: 0;
    width: 100%;
    max-width: 320px;
    z-index: 50;
    transform: translateX(-100%);
    transition: transform var(--transition-slow);
    box-shadow: var(--shadow-xl);
  }
  
  .sidebar.is-open {
    transform: translateX(0);
  }
  
  /* Overlay when sidebar is open */
  .sidebar-overlay {
    position: fixed;
    inset: 0;
    top: 56px;
    z-index: 40;
    background: rgba(0, 0, 0, 0.5);
    opacity: 0;
    visibility: hidden;
    transition: opacity var(--transition-slow), visibility var(--transition-slow);
  }
  
  .sidebar-overlay.is-visible {
    opacity: 1;
    visibility: visible;
  }
  
  .main-content {
    padding: var(--space-4);
  }
  
  /* Show settings toggle in header */
  .settings-toggle {
    display: flex;
  }
}

@media (min-width: 768px) {
  .settings-toggle {
    display: none;
  }
  
  .sidebar-overlay {
    display: none;
  }
}
```

---

## Interaction Patterns

### 1. Real-Time Calculation

**Pattern:** Calculate immediately on input change (debounced 150ms)

```javascript
// Debounce pattern for cost updates
const debouncedCalculate = debounce(() => {
  updateCostDisplay();
}, 150);

inputFields.forEach(input => {
  input.addEventListener('input', debouncedCalculate);
});
```

**Visual Feedback:**
- Cost value animates when changing (subtle scale pulse)
- Brief highlight on changed breakdown items
- No loading spinners for instant calculations

```css
.cost-value {
  transition: transform var(--transition-fast);
}

.cost-value.is-updating {
  animation: pulse 200ms ease;
}

@keyframes pulse {
  50% { transform: scale(1.02); }
}
```

---

### 2. Part Selection Grid

**Pattern:** Icon-based grid with visual selection state

```css
.part-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(100px, 1fr));
  gap: var(--space-3);
}

.part-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: var(--space-2);
  padding: var(--space-4);
  background: var(--color-surface);
  border: 2px solid var(--color-border-default);
  border-radius: var(--radius-lg);
  cursor: pointer;
  transition: all var(--transition-fast);
}

.part-card:hover {
  border-color: var(--color-border-emphasis);
  background: var(--color-bg-subtle);
}

.part-card[aria-selected="true"] {
  border-color: var(--color-accent-primary);
  background: var(--color-accent-primary-subtle);
}

.part-card-icon {
  width: 48px;
  height: 48px;
  color: var(--color-text-secondary);
}

.part-card[aria-selected="true"] .part-card-icon {
  color: var(--color-accent-primary);
}

.part-card-label {
  font-size: var(--text-sm);
  font-weight: var(--font-medium);
  color: var(--color-text-primary);
  text-align: center;
}
```

---

### 3. Settings Inline Editing

**Pattern:** Click-to-edit with inline validation

```css
.setting-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: var(--space-2) 0;
  border-bottom: 1px solid var(--color-border-muted);
}

.setting-label {
  font-size: var(--text-sm);
  color: var(--color-text-primary);
}

.setting-value {
  font-family: var(--font-mono);
  font-size: var(--text-sm);
  color: var(--color-text-secondary);
  padding: var(--space-1) var(--space-2);
  border-radius: var(--radius-sm);
  cursor: pointer;
  transition: background var(--transition-fast);
}

.setting-value:hover {
  background: var(--color-hover-overlay);
}

.setting-input {
  width: 80px;
  padding: var(--space-1) var(--space-2);
  font-family: var(--font-mono);
  font-size: var(--text-sm);
  text-align: right;
  border: 1px solid var(--color-accent-primary);
  border-radius: var(--radius-sm);
  outline: none;
}
```

---

### 4. Quote Generation

**Pattern:** Two-step confirmation with preview

```
[Click "Generate Quote"]
        ↓
[Modal: Quote Preview]
  - Summary of part, params, costs
  - Customer info fields (optional)
  - [Cancel] [Download PDF] [Email Quote]
```

---

### 5. Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Tab` | Navigate between inputs |
| `Enter` (in input) | Move to next input |
| `Esc` | Close modal / Cancel edit |
| `Cmd/Ctrl + S` | Save preset (if editing settings) |
| `Cmd/Ctrl + E` | Export quote |

---

## Responsive Breakpoints

```css
/* Mobile First */

/* Small (default): 0 - 639px */
/* Stacked layout, full-width inputs */

/* Medium: 640px+ */
@media (min-width: 640px) {
  /* Two-column form grids */
}

/* Large: 768px+ */
@media (min-width: 768px) {
  /* Sidebar becomes visible */
  /* Side-by-side layout */
}

/* XL: 1024px+ */
@media (min-width: 1024px) {
  /* Wider sidebar */
  /* More horizontal space */
}

/* 2XL: 1280px+ */
@media (min-width: 1280px) {
  /* Max container width applies */
}
```

---

## Implementation Notes

### Accessibility Requirements

1. **Focus States:** All interactive elements must have visible focus indicators
2. **Color Contrast:** Minimum 4.5:1 for text, 3:1 for UI components
3. **Touch Targets:** Minimum 44x44px for mobile
4. **Screen Reader:** Use proper ARIA labels, roles, and live regions
5. **Keyboard Navigation:** Full functionality without mouse

### Performance

1. **CSS Variables:** Enables instant theme switching without repaints
2. **Debounced Calculations:** Prevent excessive recalculations
3. **No Heavy Shadows:** Limited shadow use for GPU efficiency
4. **Font Loading:** Use `font-display: swap` for system font fallback

### Theme Switching

```javascript
// Toggle theme
function toggleTheme() {
  const current = document.documentElement.dataset.theme;
  const next = current === 'dark' ? 'light' : 'dark';
  document.documentElement.dataset.theme = next;
  localStorage.setItem('theme', next);
}

// Init on load
const stored = localStorage.getItem('theme');
const preferred = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
document.documentElement.dataset.theme = stored || preferred;
```

### Recommended Tech Stack

- **CSS:** Native CSS with custom properties (no preprocessor needed)
- **Icons:** Lucide Icons (consistent, MIT licensed, tree-shakeable)
- **Fonts:** Inter (body), JetBrains Mono (numbers)
- **Framework:** Works with vanilla JS, React, Vue, Svelte

---

## File Structure (Suggested)

```
/styles
  /base
    reset.css
    tokens.css      ← CSS variables
    typography.css
  /components
    buttons.css
    inputs.css
    cards.css
    tables.css
    tabs.css
    modal.css
  /layout
    shell.css
    sidebar.css
    content.css
  /utilities
    spacing.css
    visibility.css
  main.css          ← imports all
```

---

## Quick Start Template

```html
<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CNC Planner Pro</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="styles/main.css">
</head>
<body>
  <div class="app">
    <header class="app-header">
      <div class="app-logo">
        <svg class="icon" width="24" height="24"><!-- logo --></svg>
        <span>CNC Planner Pro</span>
      </div>
      <div class="app-header-actions">
        <button class="btn btn-ghost btn-icon settings-toggle" aria-label="Open settings">
          <svg class="icon"><!-- settings icon --></svg>
        </button>
        <button class="btn btn-ghost btn-icon" aria-label="Toggle theme" onclick="toggleTheme()">
          <svg class="icon"><!-- sun/moon icon --></svg>
        </button>
        <button class="btn btn-primary btn-sm">Export</button>
      </div>
    </header>
    
    <div class="app-layout">
      <aside class="sidebar">
        <!-- Settings content -->
      </aside>
      <div class="sidebar-overlay"></div>
      <main class="main-content">
        <!-- Calculator content -->
      </main>
    </div>
  </div>
</body>
</html>
```

---

*End of Design Specification*
