# Golden Standards: Price Display & Cost Breakdown UI

> Research compiled from Stripe, Xometry, Shopify, AWS Calculator, and QuickBooks patterns.

---

## Hero Price Display

### Font Size Hierarchy

| Element | Mobile | Desktop | Weight |
|---------|--------|---------|--------|
| **Hero Price** | 32-40px | 48-64px | Bold (700) |
| **Currency Symbol** | 60-70% of price | 60-70% of price | Medium (500) |
| **Cents/Decimals** | 50-60% of price | 50-60% of price | Medium (500) |
| **Period Label** (/month) | 14-16px | 16-18px | Regular (400) |
| **Original Price** (strikethrough) | Same as hero | Same as hero | Regular (400) |

**Stripe Pattern:**
```
€2.5% + €0.25
```
- Main percentage: 48px, bold
- Secondary fee: 32px, regular
- Descriptive text: 14px, gray

**Shopify Pattern:**
```
€79/month
```
- Price: 56px, font-weight: 700
- Period: 18px, font-weight: 400, opacity: 0.7

### Currency Symbol Placement

| Convention | Example | Use Case |
|------------|---------|----------|
| **Leading symbol** | $64.89 | US, UK, most English markets |
| **Trailing symbol** | 64,89 € | Germany, France, most EU |
| **Leading with space** | € 64,89 | Netherlands, formal EU |

**Best Practice for EU (Germany):**
```
64,89 €
```
- Symbol follows amount
- Space before symbol
- Comma as decimal separator

### Decimal Handling

| Locale | Format | CSS Implementation |
|--------|--------|-------------------|
| **US/UK** | $64.89 | `font-feature-settings: "tnum"` |
| **Germany/EU** | 64,89 € | Use `Intl.NumberFormat('de-DE')` |
| **No decimals** | €65 | When rounding is acceptable |

**CSS for Tabular Numbers:**
```css
.price {
  font-variant-numeric: tabular-nums;
  font-feature-settings: "tnum";
}
```

### Per-Unit Indicators

**Patterns observed:**
- Stripe: `per transaction`, `per month`, `per screened transaction`
- AWS: `per hour`, `/month`, `12-month total`
- Shopify: `/month`, `per year`

**Styling:**
```css
.per-unit {
  font-size: 0.5em; /* Relative to price */
  font-weight: 400;
  color: #6B7280; /* Gray-500 */
  margin-left: 4px;
}
```

---

## Cost Breakdown

### Row Structure

**Stripe Invoice Pattern:**
```
┌─────────────────────────────────────────────────────────┐
│ Description                      Qty    Rate    Amount  │
├─────────────────────────────────────────────────────────┤
│ CNC Machining - Aluminum 6061    2      €32.45  €64.90  │
│   └ Material cost                              €24.00  │
│   └ Machine time (2.5h)                        €40.90  │
├─────────────────────────────────────────────────────────┤
│                                  Subtotal      €64.90  │
│                                  Tax (19%)     €12.33  │
├─────────────────────────────────────────────────────────┤
│                                  Total         €77.23  │
└─────────────────────────────────────────────────────────┘
```

**AWS Calculator Pattern:**
```
┌─────────────────────────────────────────────────────────┐
│ Service                          Upfront  Monthly  12-mo│
├─────────────────────────────────────────────────────────┤
│ ▼ Amazon EC2                     $0.00    $45.26   $543 │
│    Instance type: t3.medium                             │
│    Region: eu-central-1                                 │
│    Hours: 730/month                                     │
├─────────────────────────────────────────────────────────┤
│ ▼ Amazon S3                      $0.00    $12.50   $150 │
│    Storage: 500 GB                                      │
├─────────────────────────────────────────────────────────┤
│ TOTAL                            $0.00    $57.76   $693 │
└─────────────────────────────────────────────────────────┘
```

### Indentation for Sub-items

```css
/* Parent item */
.line-item {
  padding-left: 0;
}

/* Child/breakdown item */
.line-item--child {
  padding-left: 24px;
  font-size: 14px;
  color: #6B7280;
}

/* Grandchild (rare) */
.line-item--grandchild {
  padding-left: 48px;
  font-size: 13px;
}
```

**Visual indicator options:**
1. **Tree connector:** `└` character (Stripe uses this)
2. **Indentation only:** AWS Calculator approach
3. **Background tint:** Slightly darker bg for children

### Formula Display (Show Calculation)

**Xometry Pattern:**
```
Material: Aluminum 6061
  Stock volume: 150 × 80 × 25 mm = 300 cm³
  Material cost: 300 cm³ × €0.08/cm³ = €24.00

Machine Time:
  Roughing: 45 min
  Finishing: 60 min
  Setup: 15 min
  Total: 2h × €20.45/h = €40.90
```

**CSS for formulas:**
```css
.calculation {
  font-family: 'SF Mono', 'Fira Code', monospace;
  font-size: 13px;
  color: #6B7280;
  background: #F9FAFB;
  padding: 8px 12px;
  border-radius: 4px;
  margin: 4px 0 4px 24px;
}

.calculation-operator {
  color: #9CA3AF;
  padding: 0 4px;
}

.calculation-result {
  font-weight: 600;
  color: #111827;
}
```

### Totals vs Subtotals Styling

| Element | Font Size | Weight | Background | Border |
|---------|-----------|--------|------------|--------|
| **Line item** | 14-16px | 400 | transparent | bottom only |
| **Subtotal** | 14-16px | 500 | transparent | top 1px |
| **Tax line** | 14px | 400 | transparent | none |
| **Total** | 18-20px | 700 | #F3F4F6 | top 2px |
| **Grand Total** | 20-24px | 700 | #1F2937 (dark) | none |

**CSS:**
```css
.subtotal-row {
  border-top: 1px solid #E5E7EB;
  padding-top: 12px;
}

.total-row {
  background: #F3F4F6;
  border-top: 2px solid #D1D5DB;
  padding: 16px;
  font-weight: 700;
  font-size: 18px;
}

.grand-total-row {
  background: #1F2937;
  color: white;
  padding: 20px;
  font-weight: 700;
  font-size: 24px;
  border-radius: 0 0 8px 8px;
}
```

---

## Visual Hierarchy

### What's Most Prominent?

**Hierarchy (top to bottom):**
1. **Total price** - Largest, boldest, high contrast
2. **Hero price/main quote** - Nearly as large
3. **Section headers** - Medium weight, clear separation
4. **Line item amounts** - Right-aligned, tabular
5. **Line item descriptions** - Left-aligned, regular
6. **Metadata/timestamps** - Smallest, lowest contrast

**Stripe's attention flow:**
```
TOTAL €77.23 ←── Eye goes here first (48px, bold, dark)
    ↓
Subtotal €64.90 ←── Secondary (16px, medium)
    ↓
Line items ←── Scanning zone (14px, regular)
```

### Progressive Disclosure Patterns

**Pattern 1: Accordion (AWS Calculator)**
```
▼ EC2 Instance Costs         €45.26/mo
  ├─ Compute                 €38.00
  ├─ Storage                 €5.26
  └─ Data transfer           €2.00

▶ S3 Storage Costs           €12.50/mo  [collapsed]
```

**Pattern 2: Expandable Row (Xometry)**
```
┌──────────────────────────────────────┐
│ Part: Bracket-001      €64.89  [▼]   │
├──────────────────────────────────────┤
│ Material               €24.00        │ ← Appears on expand
│ Machine Time           €40.89        │
└──────────────────────────────────────┘
```

**Pattern 3: Tooltip/Popover (Stripe)**
- Hover on price → see calculation
- Click "?" icon → modal with explanation

### Expandable Details Implementation

```css
.expandable-row {
  cursor: pointer;
  transition: background 0.15s ease;
}

.expandable-row:hover {
  background: #F9FAFB;
}

.expandable-row[aria-expanded="true"] .chevron {
  transform: rotate(180deg);
}

.expandable-content {
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.2s ease-out;
}

.expandable-content[data-open="true"] {
  max-height: 500px;
}
```

---

## Trust Elements

### Data Source Indicators

**Stripe pattern:**
```
Pricing based on your account's standard rates
Last updated: Feb 5, 2026
```

**Xometry pattern:**
```
ⓘ Quote generated using Xometry Instant Quoting Engine®
  Based on: 3D model analysis, material database, machine availability
  Accuracy: ±5% for production quantities
```

**Implementation:**
```css
.data-source {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 12px;
  color: #6B7280;
  padding: 8px 12px;
  background: #F9FAFB;
  border-radius: 4px;
  margin-top: 16px;
}

.data-source-icon {
  width: 16px;
  height: 16px;
  color: #9CA3AF;
}
```

### Accuracy Disclaimers

**Patterns observed:**

**AWS:**
> "Estimates are based on the configuration you provided. Actual costs may vary."

**Xometry:**
> "This is an instant quote estimate. Final pricing may change based on design review."

**QuickBooks:**
> "This invoice is for reference only until finalized."

**Styling:**
```css
.disclaimer {
  font-size: 12px;
  color: #6B7280;
  font-style: italic;
  padding: 12px;
  background: #FFFBEB; /* Amber-50 for warnings */
  border-left: 3px solid #F59E0B; /* Amber-500 */
  border-radius: 0 4px 4px 0;
  margin-top: 16px;
}

/* For informational (non-warning) */
.disclaimer--info {
  background: #EFF6FF; /* Blue-50 */
  border-left-color: #3B82F6; /* Blue-500 */
}
```

### Last Updated Timestamps

**Formats used:**
- Stripe: "Pricing effective as of January 2024"
- AWS: "Last updated: 5 minutes ago"
- Xometry: "Quote valid for 30 days from Feb 5, 2026"

**Implementation:**
```css
.timestamp {
  font-size: 11px;
  color: #9CA3AF;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.timestamp--fresh {
  color: #10B981; /* Green when recent */
}

.timestamp--stale {
  color: #F59E0B; /* Amber when old */
}
```

---

## CSS Specifics

### Price Font Sizes

| Context | Size | Line Height | Weight |
|---------|------|-------------|--------|
| **Hero price (landing)** | 48-64px | 1.1 | 700 |
| **Card price (pricing table)** | 36-48px | 1.2 | 700 |
| **Inline price (in text)** | Same as body | 1.5 | 600 |
| **Table price (invoice)** | 14-16px | 1.4 | 500 |
| **Total price** | 20-24px | 1.3 | 700 |
| **Small/meta price** | 12-14px | 1.4 | 400 |

### Monospace vs Proportional

**Use MONOSPACE for:**
- Calculations/formulas
- Code snippets
- Serial numbers/IDs

**Use TABULAR NUMS (proportional with fixed-width digits) for:**
- All prices
- Quantities
- Dates in tables

```css
/* Prices - tabular numerals */
.price {
  font-family: 'Inter', system-ui, sans-serif;
  font-variant-numeric: tabular-nums;
}

/* Calculations - monospace */
.calculation {
  font-family: 'JetBrains Mono', 'Fira Code', monospace;
}
```

### Background Colors for Totals

| Row Type | Background | Text Color |
|----------|------------|------------|
| **Regular row** | `transparent` | `#374151` |
| **Alternating row** | `#F9FAFB` | `#374151` |
| **Subtotal row** | `#F3F4F6` | `#1F2937` |
| **Total row** | `#E5E7EB` | `#111827` |
| **Grand total** | `#1F2937` | `#FFFFFF` |
| **Highlight/selected** | `#EFF6FF` | `#1E40AF` |

### Border/Divider Styles

```css
/* Light separator between rows */
.row-divider {
  border-bottom: 1px solid #E5E7EB;
}

/* Section separator */
.section-divider {
  border-bottom: 1px solid #D1D5DB;
  margin: 16px 0;
}

/* Before totals */
.totals-divider {
  border-top: 2px solid #9CA3AF;
  margin-top: 16px;
  padding-top: 16px;
}

/* Grand total emphasis */
.grand-total-divider {
  border-top: 3px solid #1F2937;
}
```

---

## Recommendation for CNC Planner Pro

### Exact Price Display Component

```tsx
// PriceDisplay.tsx
interface PriceDisplayProps {
  amount: number;
  currency?: string;
  size?: 'hero' | 'card' | 'inline' | 'table';
  showDecimals?: boolean;
  perUnit?: string;
  originalPrice?: number;
}

const sizeStyles = {
  hero: 'text-5xl font-bold', // 48px
  card: 'text-4xl font-bold', // 36px
  inline: 'text-base font-semibold', // 16px
  table: 'text-sm font-medium tabular-nums', // 14px
};
```

**Rendered HTML:**
```html
<div class="price-display price-display--hero">
  <span class="price-amount">64</span>
  <span class="price-decimal">,89</span>
  <span class="price-currency">€</span>
  <span class="price-unit">/Stück</span>
</div>
```

**CSS:**
```css
.price-display {
  font-family: 'Inter', system-ui, sans-serif;
  font-variant-numeric: tabular-nums;
  display: inline-flex;
  align-items: baseline;
  gap: 2px;
}

.price-display--hero {
  font-size: 48px;
  font-weight: 700;
  color: #111827;
  line-height: 1.1;
}

.price-display--hero .price-decimal {
  font-size: 0.6em;
  font-weight: 500;
}

.price-display--hero .price-currency {
  font-size: 0.6em;
  font-weight: 500;
  margin-left: 4px;
}

.price-display--hero .price-unit {
  font-size: 0.35em;
  font-weight: 400;
  color: #6B7280;
  margin-left: 8px;
}
```

### Cost Breakdown Table Styling

```tsx
// CostBreakdownTable.tsx
interface LineItem {
  id: string;
  description: string;
  quantity?: number;
  rate?: number;
  amount: number;
  children?: LineItem[];
  calculation?: string;
}
```

**CSS:**
```css
.cost-breakdown {
  width: 100%;
  border-collapse: collapse;
  font-size: 14px;
}

.cost-breakdown th {
  text-align: left;
  font-weight: 500;
  color: #6B7280;
  font-size: 12px;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  padding: 12px 16px;
  border-bottom: 2px solid #E5E7EB;
}

.cost-breakdown th:last-child {
  text-align: right;
}

.cost-breakdown td {
  padding: 12px 16px;
  border-bottom: 1px solid #F3F4F6;
  color: #374151;
}

.cost-breakdown td:last-child {
  text-align: right;
  font-variant-numeric: tabular-nums;
  font-weight: 500;
}

/* Child row (indented) */
.cost-breakdown tr.child-row td:first-child {
  padding-left: 40px;
  color: #6B7280;
  font-size: 13px;
}

.cost-breakdown tr.child-row td:first-child::before {
  content: "└ ";
  color: #D1D5DB;
}

/* Subtotal row */
.cost-breakdown tr.subtotal-row {
  background: #F9FAFB;
}

.cost-breakdown tr.subtotal-row td {
  font-weight: 500;
  border-top: 1px solid #E5E7EB;
}

/* Total row */
.cost-breakdown tr.total-row {
  background: #F3F4F6;
}

.cost-breakdown tr.total-row td {
  font-weight: 700;
  font-size: 16px;
  color: #111827;
  border-top: 2px solid #D1D5DB;
  padding: 16px;
}

/* Grand total row */
.cost-breakdown tr.grand-total-row {
  background: #1F2937;
}

.cost-breakdown tr.grand-total-row td {
  color: white;
  font-weight: 700;
  font-size: 18px;
  padding: 20px 16px;
}
```

### Complete Example

```html
<table class="cost-breakdown">
  <thead>
    <tr>
      <th>Beschreibung</th>
      <th>Menge</th>
      <th>Einzelpreis</th>
      <th>Betrag</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CNC-Fräsen - Aluminium 6061</td>
      <td>2</td>
      <td>32,45 €</td>
      <td>64,90 €</td>
    </tr>
    <tr class="child-row">
      <td>Materialkosten</td>
      <td></td>
      <td></td>
      <td>24,00 €</td>
    </tr>
    <tr class="child-row">
      <td>Maschinenzeit (2,5h)</td>
      <td></td>
      <td></td>
      <td>40,90 €</td>
    </tr>
    <tr class="subtotal-row">
      <td colspan="3">Zwischensumme</td>
      <td>64,90 €</td>
    </tr>
    <tr>
      <td colspan="3">MwSt. (19%)</td>
      <td>12,33 €</td>
    </tr>
    <tr class="total-row">
      <td colspan="3">Gesamtbetrag</td>
      <td>77,23 €</td>
    </tr>
  </tbody>
</table>
```

### Color Palette Summary

```css
:root {
  /* Text colors */
  --text-primary: #111827;    /* Headings, totals */
  --text-secondary: #374151;  /* Body text */
  --text-tertiary: #6B7280;   /* Captions, labels */
  --text-muted: #9CA3AF;      /* Timestamps, hints */
  
  /* Backgrounds */
  --bg-white: #FFFFFF;
  --bg-subtle: #F9FAFB;       /* Alternating rows */
  --bg-muted: #F3F4F6;        /* Subtotals */
  --bg-emphasis: #E5E7EB;     /* Totals */
  --bg-inverse: #1F2937;      /* Grand total */
  
  /* Borders */
  --border-light: #F3F4F6;    /* Row dividers */
  --border-default: #E5E7EB;  /* Section dividers */
  --border-strong: #D1D5DB;   /* Before totals */
  
  /* Accents */
  --accent-info: #3B82F6;     /* Blue for info */
  --accent-warning: #F59E0B;  /* Amber for warnings */
  --accent-success: #10B981;  /* Green for fresh data */
}
```

---

## Quick Reference Card

| Element | Font | Size | Weight | Color |
|---------|------|------|--------|-------|
| Hero price | Inter | 48px | 700 | #111827 |
| Card price | Inter | 36px | 700 | #111827 |
| Table amount | Inter | 14px | 500 | #374151 |
| Total | Inter | 18px | 700 | #111827 |
| Grand total | Inter | 20px | 700 | #FFFFFF |
| Description | Inter | 14px | 400 | #374151 |
| Child item | Inter | 13px | 400 | #6B7280 |
| Header | Inter | 12px | 500 | #6B7280 |
| Timestamp | Inter | 11px | 400 | #9CA3AF |

---

*Last updated: 2026-02-05*
*Sources: Stripe, AWS Calculator, Shopify, Xometry, QuickBooks*
