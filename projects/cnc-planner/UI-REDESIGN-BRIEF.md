# UI Redesign Brief — CNC Planer Pro v18

## Problem
The current UI looks like a developer prototype, not a production SaaS tool. Spacing is inconsistent, elements feel loose, and the overall impression is "broken" rather than "professional industrial software."

## Target Aesthetic
**Reference:** Linear.app, Vercel Dashboard, Raycast — clean, tight, modern SaaS.
**Industry twist:** Industrial/engineering gravitas. No playful colors. Serious tool for serious people.

## Specific Issues to Fix

### 1. SPACING — Too Loose Everywhere
- Card padding: reduce from 16px to 12px
- Section gaps: reduce from 20-24px to 12-16px
- Form group margins: reduce from 16px to 10px
- Page padding: reduce from 32px to 24px
- Header height: reduce if possible
- **Rule:** Nothing should feel "floating in space"

### 2. TYPOGRAPHY — Needs Hierarchy
- Page title: 20px semibold (not 24px)
- Card headers: 13px semibold uppercase, letter-spacing 0.5px
- Body text: 13px (not 14px)
- Metadata: 11px
- Monospace values: 12px
- **Rule:** Tighter line-heights (1.3 for headings, 1.5 for body)

### 3. CARDS — Too Plain
- Add subtle background to card headers: #F8F9FA
- Tighter border: 1px solid #E5E7EB
- Border-radius: 6px (not 4px — slightly softer)
- Card header: 10px 12px padding, border-bottom
- No box-shadow on cards (flat design)

### 4. SIDEBAR — Needs Polish
- Active item: solid background with subtle left border accent
- Items: 10px vertical padding (tighter)
- Section titles: 10px, uppercase, muted color, letter-spacing
- Logo area: tighter padding

### 5. PART CARDS — Need to Feel Clickable
- Slight shadow on hover
- Border highlight on selected (2px primary)
- Thumbnail: 140px height (not 160px)
- Info section: 10px padding, tighter
- Price: right-aligned, bold, dark

### 6. FORM INPUTS — Modern Look
- Height: 36px (not browser default)
- Border-radius: 4px
- Border: 1px solid #D1D5DB
- Focus: primary color outline, no box-shadow
- Font-size: 13px
- Padding: 0 10px
- Background: white (not gray)

### 7. BUTTONS — Consistent System
- Primary: dark background (#1F2937), white text, 36px height
- Secondary: white background, border, dark text
- Small: 28px height, 12px font
- Border-radius: 4px
- No uppercase on buttons

### 8. TABLES — Professional Data Display
- Header: #F8F9FA background, 12px semibold uppercase, letter-spacing
- Cells: 10px padding vertical, 12px horizontal
- Borders: only horizontal (no vertical lines)
- Alternating rows: very subtle #FAFAFA
- Monospace for numbers

### 9. COLORS — Industrial Palette
- Primary: #1F2937 (dark gray, not blue)
- Accent (sparingly): #D97706 (warm amber for CTA)
- Success: #059669
- Error: #DC2626
- Background: pure #FFFFFF
- Surface: #FFFFFF
- Borders: #E5E7EB
- **Rule:** Almost monochrome. Color = meaning, not decoration.

### 10. OVERALL FEEL
- Dense but not cramped (like Linear.app)
- Every pixel intentional
- No decorative elements
- Information-first
- Feels like a tool built by engineers for engineers

## Implementation Order
1. CSS variables (spacing, sizes, colors)
2. Base elements (inputs, buttons, selects, tables)
3. Cards + headers
4. Sidebar
5. Part grid
6. Section-specific fixes
7. Final verification screenshot

## Success Criteria
"Would an Arbeitsvorbereiter at a CNC shop think this was made by a real software company?"
If yes → done. If no → iterate.
