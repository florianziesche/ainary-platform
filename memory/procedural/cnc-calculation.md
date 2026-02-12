# CNC Time Estimation - Procedural Memory

**Purpose:** How to calculate CNC machining times accurately (process knowledge)

---

## Overview

**Goal:** Estimate CNC machining time for a part within ±10-15% accuracy  
**Manual Time:** 30-60 minutes (industry standard)  
**CNC Planner Pro Time:** ~15 minutes  
**Manual Accuracy:** ±20-30%  
**Our Target Accuracy:** ±10-15%

---

## 1. Part Analysis Phase

### 1.1 Extract Dimensions
- **Inputs:** Technical drawing (PDF/DWG)
- **Required:**
  - Overall dimensions (length × width × height in mm)
  - Material specification (e.g., S355, GJS-700, AlMg3)
  - Quantity (affects setup amortization)
  - Tolerances (ISO 2768 or specific callouts)

### 1.2 Identify Features
- **Feature Types:**
  - Facing (flat surfaces)
  - Milling pockets (depth, area, corners)
  - Drilling holes (diameter, depth, count)
  - Boring operations (precision holes)
  - Threading (thread size, depth)
  - Contouring (complex profiles)
  - Engraving (text, part numbers)

- **For Each Feature:**
  - Dimensions (length, width, depth, diameter)
  - Tolerance requirements
  - Surface finish (Ra value if specified)
  - Accessibility (requires rotation/re-setup?)

---

## 2. Material Properties

### 2.1 Material Database
**Common Materials:**

| Material | Cutting Speed (vc) | Feed (fz) | Density | Cost/kg |
|----------|-------------------|-----------|---------|---------|
| AlMg3 (Aluminum) | 400-600 m/min | 0.15 mm | 2.7 kg/dm³ | €2.50 |
| S355 (Structural Steel) | 180-220 m/min | 0.12 mm | 7.85 kg/dm³ | €3.00 |
| GJS-700 (Ductile Iron) | 100-150 m/min | 0.10 mm | 7.10 kg/dm³ | €2.80 |
| GJS-400 | 120-180 m/min | 0.12 mm | 7.10 kg/dm³ | €2.50 |
| GJL-250 (Gray Cast Iron) | 150-200 m/min | 0.10 mm | 7.20 kg/dm³ | €2.30 |

**Source:** Industry standards + machining handbooks + verified web research (2026-02-10)

### 2.2 Material Factors
- **Machinability:** Cast iron > Aluminum > Steel (affects tool wear, speeds)
- **Chip Formation:** Continuous (aluminum) vs Brittle (cast iron)
- **Coolant:** Required for steel, optional for cast iron, essential for aluminum

---

## 3. Operation Planning (Arbeitsgang = AG)

### 3.1 Define Operations
**For each feature → create operation(s):**

**Example: Lagerungstraverse (Bearing Crossbeam)**
1. **AG 10:** Sägen (Sawing) — Cut raw stock to length
2. **AG 20:** Planfräsen Seite 1 (Face milling side 1)
3. **AG 30:** Planfräsen Seite 2 (Face milling side 2)
4. **AG 40:** Taschen fräsen (Pocket milling)
5. **AG 50:** Bohren (Drilling) — Mounting holes
6. **AG 60:** Senken (Countersinking)
7. **AG 70:** Gewinde schneiden (Threading)
8. **AG 80:** Konturfräsen (Contour milling)
9. **AG 90:** Gravieren (Engraving) — Part number
10. **AG 100:** Entgraten (Deburring)
11. **AG 110:** Qualitätskontrolle (Quality inspection)

### 3.2 Assign Cost Centers (Kostenstellen)
- **Sägen:** €45/hour (band saw, lower rate)
- **CNC Fräsen:** €70/hour (5-axis machining center)
- **Entgraten/QS:** €31/hour (manual work, lower skilled)

---

## 4. Time Calculation Formulas

### 4.1 Machining Time (Bearbeitungszeit)

**Formula:** `t_cut = (L_cut × n_passes) / (f × n)`

Where:
- `L_cut` = cutting length (mm)
- `n_passes` = number of passes
- `f` = feed rate (mm/min) = fz × z × n
- `n` = spindle speed (RPM) = (vc × 1000) / (π × D)
- `fz` = feed per tooth (mm)
- `z` = number of teeth (cutter)
- `D` = tool diameter (mm)

**Typical Values:**
- Face milling: 80-120% of part width per pass
- Pockets: 50-70% tool diameter stepover
- Drilling: depth/feed rate

### 4.2 Setup Time (Rüstzeit)

**Components:**
1. **First Setup (Initial):** 30-60 min
   - Part fixturing
   - Tool loading
   - Program verification
   - First article inspection

2. **Re-Setup (Rotation):** 15-30 min
   - Flip part to new orientation
   - Re-clamp
   - Probe/touch-off

3. **Tool Changes:** 1-2 min per tool (automatic tool changer)

**Formula:** `t_setup = t_initial + (n_setups × t_reSetup) + (n_tools × t_toolChange)`

**Batch Amortization:**
- Setup time is ONE-TIME per batch
- Amortize over quantity: `t_setup_per_part = t_setup / quantity`

---

## 5. Confidence Scoring

### 5.1 Confidence Factors

**Increase Confidence (+):**
- ✅ Complete drawing with all dimensions
- ✅ Standard materials in database
- ✅ Simple geometry (boxes, flat surfaces)
- ✅ Similar parts calculated before
- ✅ Standard tolerances (ISO 2768-m or coarser)

**Decrease Confidence (-):**
- ❌ Incomplete drawing (missing dimensions, vague specs)
- ❌ Exotic materials (not in database)
- ❌ Complex geometry (undercuts, thin walls, deep pockets)
- ❌ Tight tolerances (<0.05mm)
- ❌ First-time feature types

### 5.2 Confidence Scale

| Score | Meaning | Typical Error |
|-------|---------|---------------|
| 90-95% | Nearly certain (verified similar part) | ±5% |
| 75-89% | High confidence (standard work) | ±10-15% |
| 60-74% | Moderate (some unknowns) | ±20% |
| 40-59% | Low (significant gaps) | ±30%+ |
| <40% | Guess (insufficient data) | ±50%+ |

**Lagerungstraverse Example:** 75% confidence
- Reasoning: Complete drawing, material in database, but complex geometry (11 operations) and first-time calculating this specific part.

---

## 6. Cost Calculation (Zuschlagskalkulation)

### 6.1 Direct Costs
1. **Material Cost:** Weight × €/kg (include scrap allowance 5-10%)
2. **Machining Cost:** Time × Rate per cost center
3. **Setup Cost:** Setup time × Rate (amortized over batch)

### 6.2 Overhead Cascade (REFA Method)

**Formula Chain:**
1. **Material + Machining = Fertigungskosten (Manufacturing Cost)**
2. **+ MGK (Materialgemeinkosten, Material Overhead):** 10-15%
3. **+ Fertigungsgemeinkosten (Manufacturing Overhead, FGK):** = Material + Machining + MGK
4. **+ AV (Außenvertriebskosten, External Sales):** 5-10%
5. **+ VwGK (Verwaltungsgemeinkosten, Admin Overhead):** 8-12%
6. **+ VtGK (Vertriebsgemeinkosten, Sales/Marketing):** 3-5%
7. **+ Gewinn (Profit Margin):** 10-20%
8. **= Angebotspreis (Quote Price)**

**Each step cascades:**
- MGK is applied to Material
- FGK is applied to (Material + Machining + MGK)
- AV is applied to (Material + Machining + MGK + FGK)
- etc.

**Example Percentages (CNC Planner Defaults):**
- MGK: 12%
- AV: 8%
- VwGK: 10%
- VtGK: 4%
- Gewinn: 15%
- Verschnitt (Scrap): 5%
- MwSt (VAT): 19%

---

## 7. Quality Checks (Prüfprotokoll)

**Before finalizing quote, ask:**

1. **Is the drawing complete?** (all dimensions clear?)
2. **Material availability?** (standard stock or special order?)
3. **Tolerance feasibility?** (can we hit spec with our machines?)
4. **Special tooling needed?** (custom cutters, long reach tools?)
5. **Raw material form?** (plate, bar, casting, forging?)
6. **Surface finish requirements?** (cosmetic, functional, or standard?)
7. **Inspection requirements?** (CMM, calipers, or visual?)
8. **Delivery timeline realistic?** (1 week, 2 weeks, rush?)

**If any answer is uncertain:**
- Flag in quote as assumption
- Lower confidence score
- Add contingency buffer (time +10-20%)

---

## 8. Documentation Output

### 8.1 Fertigungsanweisung (Work Instructions)
**Includes:**
- Part details (drawing number, material, quantity)
- Setup plan (4 setups with orientation diagrams)
- Operations table:
  - AG number
  - Description
  - Tool (diameter, type)
  - Cutting parameters (vc, feed, depth)
  - Time (setup + machining)
- Change protocol (if AI recommendations were modified)
- Signatures (programmer, operator, QC)

### 8.2 Kalkulation (Costing Report)
**Includes:**
- Material cost breakdown
- Time breakdown per operation
- Overhead cascade (MGK → Gewinn)
- Final quote price
- Confidence score + assumptions

### 8.3 Risikoanalyse (Risk Analysis) — Optional for Complex Parts
**Includes:**
- Risk matrix (Probability × Impact)
- Scenario analysis (Best/Expected/Worst case)
- Price drivers (what if material costs rise? tight tolerance?)
- Decision matrix (bid options: aggressive, standard, conservative)
- Mitigation strategies

---

## 9. Lessons Learned (From Practice)

### Lesson 1: Rüstzeit Matters for Small Batches
- 1 part: Setup dominates cost (661 min machining + 164 min setup = 825 min total)
- 10 parts: Setup amortizes (661×10 + 164 = 6,774 min total = 677 min/part average)
- **Implication:** Always show batch pricing (1, 5, 10, 25, 50 pcs)

### Lesson 2: Material Costs Can Mislead
- S355 steel plate (standard): €0.82-1.05/kg
- S355 steel plate (>100mm thick): ~€1.20-1.40/kg (20-40% premium)
- GJS-700 casting (complex): Beistellung (customer supplies)
- **Implication:** Always verify material form (plate, bar, casting) and thickness

### Lesson 3: Cutting Speeds Are Material-Specific
- GJS-700 (ductile iron): 100-150 m/min [Source: CastingSR Guide | 2026-02-10]
- S355 (steel): 180-220 m/min
- AlMg3 (aluminum): 400-600 m/min
- **Implication:** Don't use generic "steel" speeds — specify grade

### Lesson 4: AI Recommendations Need Human Check
- AI might suggest faster speeds (optimistic)
- Always validate against material database
- Confidence score should reflect uncertainty
- **Implication:** Build AI assist, not AI replace

---

## 10. Continuous Improvement

**Track Actual vs Estimated:**
- After part completion, log actual time
- Calculate error: `(actual - estimated) / actual × 100%`
- Update database if systematic bias found

**Refine Material Database:**
- Add new materials as encountered
- Update cutting speeds based on tooling (coated vs uncoated)
- Source from tool manufacturer catalogs (Sandvik, Kennametal, etc.)

**Build Part Library:**
- Save calculations for common geometries
- Reuse time estimates for similar features
- Analogous estimating: "This is like Part X but 20% larger"

---

**Last Updated:** 2026-02-10  
**Source:** Extracted from CNC Planner v19 implementation + REFA methodology + daily session logs  
**Key Reference:** Lagerungstraverse calculation (661 min, 11 AGs, GJS-700, 75% confidence)
