# Golden Standard: Enterprise SaaS Design System

*Basierend auf Linear, Notion, Stripe, Figma*

---

## 1. Farbpalette

### Primary Colors
```css
--color-primary: #1E3A5F;        /* Deep Navy - Haupt-Akzent */
--color-primary-hover: #152A45;  /* Darker on hover */
--color-primary-light: #2D5A8A; /* Lighter variant */
```

### Neutral Scale (Gray)
```css
/* Von dunkel nach hell */
--color-gray-900: #0F172A;  /* Text primary */
--color-gray-800: #1E293B;  /* Text strong */
--color-gray-700: #334155;  /* Text normal */
--color-gray-600: #475569;  /* Text secondary */
--color-gray-500: #64748B;  /* Text muted */
--color-gray-400: #94A3B8;  /* Placeholder */
--color-gray-300: #CBD5E1;  /* Borders strong */
--color-gray-200: #E2E8F0;  /* Borders */
--color-gray-100: #F1F5F9;  /* Background subtle */
--color-gray-50: #F8FAFC;   /* Background */
```

### Semantic Colors
```css
--color-success: #059669;   /* Green - positive */
--color-warning: #D97706;   /* Amber - attention */
--color-error: #DC2626;     /* Red - negative */
--color-info: #2563EB;      /* Blue - informational */
```

### Backgrounds
```css
--color-bg: #F8FAFC;        /* Page background */
--color-surface: #FFFFFF;   /* Cards, modals */
--color-surface-hover: #F8FAFC;
```

---

## 2. Typografie

### Font Stack
```css
--font-sans: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
--font-mono: 'JetBrains Mono', 'SF Mono', 'Fira Code', monospace;
```

### Type Scale
```css
--text-xs: 0.75rem;    /* 12px - Labels, badges */
--text-sm: 0.875rem;   /* 14px - Secondary text */
--text-base: 1rem;     /* 16px - Body */
--text-lg: 1.125rem;   /* 18px - Large body */
--text-xl: 1.25rem;    /* 20px - Section titles */
--text-2xl: 1.5rem;    /* 24px - Page titles */
--text-3xl: 2rem;      /* 32px - Hero text */
--text-4xl: 2.5rem;    /* 40px - Large numbers */
```

### Font Weights
```css
--font-normal: 400;
--font-medium: 500;
--font-semibold: 600;
--font-bold: 700;
```

### Line Heights
```css
--leading-tight: 1.25;
--leading-normal: 1.5;
--leading-relaxed: 1.75;
```

---

## 3. Spacing

### Spacing Scale (4px base)
```css
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
```

---

## 4. Border Radius

```css
--radius-sm: 4px;     /* Inputs, small elements */
--radius-md: 6px;     /* Buttons, cards */
--radius-lg: 8px;     /* Modals, large cards */
--radius-xl: 12px;    /* Hero sections */
--radius-full: 9999px; /* Pills, avatars */
```

---

## 5. Shadows

```css
--shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05);
--shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.1);
--shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.1);
--shadow-xl: 0 20px 25px -5px rgb(0 0 0 / 0.1);
```

---

## 6. Transitions

```css
--transition-fast: 150ms ease;
--transition-normal: 200ms ease;
--transition-slow: 300ms ease;
```

---

## 7. Layout Constraints

```css
/* Sidebar */
--sidebar-width: 260px;
--sidebar-collapsed: 64px;

/* Content */
--content-max-width: 1200px;
--content-narrow: 800px;

/* Header */
--header-height: 56px;
```

---

## 8. Z-Index Scale

```css
--z-base: 0;
--z-dropdown: 10;
--z-sticky: 20;
--z-overlay: 30;
--z-modal: 40;
--z-popover: 50;
--z-tooltip: 60;
```

---

## 9. Component Standards

### Buttons
```css
.btn {
    height: 36px;              /* Standard */
    padding: 0 16px;
    font-size: 14px;
    font-weight: 500;
    border-radius: 6px;
    transition: all 150ms ease;
}

.btn-sm { height: 32px; padding: 0 12px; font-size: 13px; }
.btn-lg { height: 44px; padding: 0 24px; font-size: 16px; }
```

### Inputs
```css
.input {
    height: 40px;
    padding: 0 12px;
    font-size: 14px;
    border: 1px solid var(--color-gray-300);
    border-radius: 6px;
    background: var(--color-surface);
}

.input:focus {
    border-color: var(--color-primary);
    box-shadow: 0 0 0 3px rgba(30, 58, 95, 0.1);
    outline: none;
}
```

### Cards
```css
.card {
    background: var(--color-surface);
    border: 1px solid var(--color-gray-200);
    border-radius: 8px;
    padding: 24px;
}
```

### Tables
```css
.table th {
    font-size: 12px;
    font-weight: 500;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: var(--color-gray-500);
    padding: 12px 16px;
    background: var(--color-gray-50);
}

.table td {
    padding: 12px 16px;
    border-bottom: 1px solid var(--color-gray-100);
}
```

---

## 10. Golden Rules

1. **8px Grid** — Alle Abstände in Vielfachen von 8px
2. **Konsistente Höhen** — 32/36/40/44/48px für interaktive Elemente
3. **Maximal 3 Grautöne** pro View (Text, Sekundär, Muted)
4. **Primary nur für CTAs** — Nicht für Dekoration
5. **Monospace für Zahlen** — Alle Preise, Zeiten, Maße
6. **Whitespace ist gut** — Nicht alles zustopfen
7. **Progressive Disclosure** — Details erst bei Bedarf
8. **Focus States** — Immer sichtbar für Accessibility

---

*Golden Standard v1.0 — 2026-02-05*
