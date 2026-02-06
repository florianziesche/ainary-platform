# CNC Planner MVP — Codex Build Spec

**Goal:** Functioning React app with core calculation logic (v16 → TypeScript)

---

## SCOPE (MVP Only)

**In Scope:**
- ✅ React + TypeScript + Vite setup
- ✅ TailwindCSS styling
- ✅ Single-page calculator form
- ✅ Port v16 calculation logic to TypeScript
- ✅ Display results (Zeiten + Kosten)
- ✅ localStorage for persistence
- ✅ Responsive design

**Out of Scope (Later):**
- ❌ Authentication
- ❌ Backend/Database
- ❌ File upload
- ❌ Payment
- ❌ Multi-page navigation

**Timeline:** 1-2 hours

---

## REQUIREMENTS

### 1. PROJECT SETUP

```bash
# Create new Vite + React + TypeScript project
npm create vite@latest cnc-planner-mvp -- --template react-ts
cd cnc-planner-mvp
npm install

# Add TailwindCSS
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p

# Add dependencies
npm install zustand        # State management
npm install react-hook-form @hookform/resolvers zod  # Forms
```

### 2. CALCULATION LOGIC (Port from v16)

**Source:** `demo-v16-complete.html` → `calculate()` function

**Target:** `src/lib/calculator.ts`

**Extract and port:**
```typescript
// Types
interface PartData {
  material: string;
  length: number;
  width: number;
  height: number;
  weight: number;
  holes: Hole[];
  // ... other fields
}

interface CalculationResult {
  totalTime: number;
  totalCost: number;
  sellingPrice: number;
  operations: Operation[];
  // ... detailed breakdown
}

// Main function
export function calculate(data: PartData): CalculationResult {
  // Port all v16 formulas here
  // - REFA time calculations
  // - VDI 3321 cutting parameters
  // - Zuschlagskalkulation (MGK, AV, VwGK, VtGK, Gewinn)
  // - OP details
}
```

### 3. UI COMPONENTS

**Layout:**
```
App.tsx
├── Header (Logo, Title)
├── CalculatorForm (Input fields)
├── ResultsDisplay (Output)
└── Footer
```

**Form Fields (from v16):**
- Material (dropdown: Stahl, Aluminium, etc.)
- Dimensions: Länge, Breite, Höhe (mm)
- Gewicht (kg)
- Anzahl Bohrungen (number)
- Stückzahl (number)
- CNC-Typ (3-Achs, 5-Achs)

**Results Display:**
- Gesamtzeit (Min)
- Materialkosten (€)
- Fertigungskosten (€)
- Verkaufspreis (€)
- OP-Details (Tabelle)

### 4. STATE MANAGEMENT

**Zustand Store:**
```typescript
// src/store/calculator.ts
interface CalculatorState {
  formData: PartData;
  result: CalculationResult | null;
  setFormData: (data: PartData) => void;
  calculate: () => void;
}
```

### 5. PERSISTENCE

**localStorage:**
```typescript
// Save form data on change
localStorage.setItem('cnc-calculator-data', JSON.stringify(formData));

// Load on mount
const saved = localStorage.getItem('cnc-calculator-data');
if (saved) setFormData(JSON.parse(saved));
```

### 6. STYLING

**TailwindCSS:**
- Clean, modern UI
- Card-based layout
- Responsive (mobile-friendly)
- Form inputs: styled consistently
- Results: clear hierarchy

---

## SUCCESS CRITERIA

**MVP is done when:**
- [ ] User can enter part data (Material, L×B×H, etc.)
- [ ] Click "Berechnen" → Shows results
- [ ] Results match v16 accuracy (within 5%)
- [ ] Form data persists (localStorage)
- [ ] UI looks professional (TailwindCSS)
- [ ] No console errors
- [ ] Responsive on mobile

---

## REFERENCE FILES

**Read these:**
1. `demo-v16-complete.html` — Current calculator (line ~500-1500: calculate() function)
2. `FUNKTIONSBESCHREIBUNG.md` — Feature documentation
3. `DESIGN-STANDARD.md` — Design patterns

**Key Formula Locations in v16:**
- Line 614: `calculate()` function start
- Line 650: Material price calculation
- Line 690: REFA time structure
- Line 750: Zuschlagskalkulation (MGK, AV, etc.)
- Line 850: OP details generation

---

## FILE STRUCTURE (Target)

```
cnc-planner-mvp/
├── src/
│   ├── components/
│   │   ├── Header.tsx
│   │   ├── CalculatorForm.tsx
│   │   ├── ResultsDisplay.tsx
│   │   └── Footer.tsx
│   ├── lib/
│   │   ├── calculator.ts       # Core logic (from v16)
│   │   └── types.ts            # TypeScript interfaces
│   ├── store/
│   │   └── calculator.ts       # Zustand state
│   ├── App.tsx
│   ├── main.tsx
│   └── index.css
├── public/
├── package.json
├── vite.config.ts
├── tailwind.config.js
└── tsconfig.json
```

---

## TESTING CHECKLIST

**Before marking done:**
- [ ] Enter test data: Steel, 100×50×20mm, 2.2kg, 5 holes, 10 Stück
- [ ] Calculate → Results appear
- [ ] Check: Total time ~45 Min (expected from v16)
- [ ] Check: Selling price ~€850 (expected from v16)
- [ ] Refresh page → Form data persists
- [ ] Resize to mobile → UI still usable

---

## DELIVERABLES

1. Working React app (`npm run dev`)
2. Calculation accuracy matches v16
3. Clean, styled UI
4. Git commits (logical steps)
5. README with setup instructions

**Timeline:** 1-2 hours

---

## NOTES FOR CODEX

- **Read v16 carefully:** The `calculate()` function is complex (800+ lines)
- **Port, don't rewrite:** Keep formulas identical to v16
- **Test with v16 data:** Use same inputs, compare outputs
- **TypeScript strict:** Enable strict mode, no `any` types
- **Comments:** Explain formula sources (REFA, VDI 3321, DIN 6584)

---

**START BUILDING.**
