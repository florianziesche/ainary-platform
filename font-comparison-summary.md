# Font Size Analysis: Executive Summary

## Quick Comparison

| Element | Linear | ElevenLabs | McKinsey | Ainary | Recommended |
|---------|--------|------------|----------|--------|-------------|
| **Hero** | 64px | 48px | 52-72px | 60px ✅ | **60px** (keep) |
| **Section Headers** | 48px | 32-36px | 44-52px | 32px ⚠️ | **44px** (+12px) |
| **Body Text** | 15-16px | 14-18px | 16px | 14.4px ⚠️ | **16px** (+1.6px) |
| **Small/Caption** | 13-14px | 12-13px | 12-14px | 13.6px ✅ | **14px** (+0.4px) |
| **Button Text** | 13px | 14px | 16px | — | **14px** (new) |
| **Mono/Data** | — | 10px | — | 10.4px | **12px** (+1.6px) |

---

## Key Issues with Current Ainary Sizes

❌ **Section headers (32px) are 25-37% smaller than competitors**
- Makes content hierarchy weak
- Reduces scannability
- Below industry standard (40-52px)

❌ **Body text (14.4px) is below modern accessibility standards**
- WCAG recommends 16px minimum
- All competitors use 15-16px+
- Hurts readability on modern high-DPI screens

✅ **Hero headline (60px) is well-positioned**
- In the sweet spot (48-72px range)
- No changes needed

✅ **Small text (13.6px) is appropriate**
- Matches industry standard (12-14px)
- Minimal adjustment needed (round to 14px)

---

## Recommended Changes

### **CRITICAL (Do Now)**
```css
Section Headers: 32px → 44px  (+37.5% increase)
Body Text:      14.4px → 16px  (+11% increase)
```

### **Important (Do Soon)**
```css
Add H3 Headers:  24px (new level for subsections)
Small Text:     13.6px → 14px (clean rounding)
Mono/Data:      10.4px → 12px (better readability)
Button Text:    Define at 14px
```

---

## New Type Scale (CSS Variables)

```css
:root {
  /* UPDATED SCALE */
  --font-hero: 3.75rem;      /* 60px - unchanged ✅ */
  --font-h2: 2.75rem;        /* 44px - increased 🎯 */
  --font-h3: 1.5rem;         /* 24px - new level 🎯 */
  --font-body: 1rem;         /* 16px - increased 🎯 */
  --font-small: 0.875rem;    /* 14px - rounded 🎯 */
  --font-mono: 0.75rem;      /* 12px - increased 🎯 */
  --font-button: 0.875rem;   /* 14px - defined 🎯 */
}
```

---

## Visual Impact

**Before (Current):**
```
60px ███████████████   Hero ✅
32px ████████          Section headers (too small)
     [gap - no H3]
14px ███               Body (too small)
13px ███               Small ✅
10px ██                Mono (too small)
```

**After (Recommended):**
```
60px ███████████████   Hero ✅
44px ███████████       Section headers (stronger hierarchy) 🎯
24px ██████            Subsection headers (new level) 🎯
16px ████              Body (modern standard) 🎯
14px ███               Small (clean) 🎯
12px ███               Mono (more readable) 🎯
```

---

## Why This Matters

1. **Readability** — 16px body text is the modern web standard
2. **Accessibility** — Meets WCAG guidelines
3. **Hierarchy** — Stronger visual structure with 44px headers
4. **Competitive** — Aligns with industry leaders (Linear, McKinsey)
5. **User Experience** — Easier scanning and content comprehension

---

**Bottom Line:** Ainary's current type scale is too small for modern web standards. Increasing section headers and body text will dramatically improve readability and user experience while maintaining the clean aesthetic.
