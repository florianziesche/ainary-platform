# Ainary Typography System — Quick Reference

**Verdict: KEEP INTER** (with strategic implementation)

---

## Font Stack

```
Display (Headlines): Inter Display Variable
Body & UI: Inter Variable  
Monospace (Code): JetBrains Mono Variable
```

All fonts: Free (OFL), self-hosted, variable format

---

## Why Inter?

✅ **Operator Signal** — Font of product companies (Notion, Linear, Vercel)  
✅ **Performance** — Variable font = 1 file, infinite weights  
✅ **Readability** — Optimized for 18px body text  
✅ **Cost** — Free, budget goes to content/dev  
✅ **Positioning** — "We build" not "we design"

Inter is NOT overused — it's infrastructure (like Helvetica in the 1960s). The association with product companies is **positive** for AI-native VC positioning.

---

## Differentiation Strategy

We differentiate through **implementation**, not font choice:

1. **Gold spectrum** (5 golds: warm → cool)
2. **Kinetic behavior** (variable font weight transitions)
3. **Scale & spacing** (18px body, 64px headlines, 120px padding)
4. **Negative tracking** (-0.025em on large text)
5. **Monospace accents** (technical depth)

---

## Typography Scale

```
H1: 56-64px, weight 600, Inter Display, -0.025em tracking
H2: 42px, weight 600, Inter Display
H3: 28px, weight 600, Inter Display
Body: 18px, weight 400, Inter, 1.7 line-height
UI: 16px, weight 500, Inter
Small: 15px, weight 400, Inter
Code: 16px, weight 400, JetBrains Mono
```

---

## Implementation Notes

**Self-host** (not Google Fonts CDN):
- Full control over subsetting (~60KB per font)
- No third-party dependencies
- Better privacy/performance

**Variable fonts enable:**
- Kinetic typography (weight shifts on hover/scroll)
- Responsive typography (adjust weight by viewport)
- Performance (1 file vs. 12 static weights)

**Fallback stack:**
```css
font-family: 'Inter', -apple-system, BlinkMacSystemFont, 
             'Segoe UI', 'Helvetica Neue', Arial, sans-serif;
```

---

## Alternative: Söhne (If Differentiation > Operator Signal)

**Söhne by Klim Type Foundry**
- Cost: ~$1000 license
- Character: Warm, material, analog heritage
- Signal: "Design-conscious VC"
- Trade-off: Not variable font, larger file size

**Only choose if:** Differentiation from product companies is critical.

**Otherwise:** Stick with Inter.

---

## Files to Download

1. [Inter Variable](https://rsms.me/inter) — WOFF2 format
2. [Inter Display Variable](https://rsms.me/inter) — WOFF2 format  
3. [JetBrains Mono Variable](https://www.jetbrains.com/lp/mono/) — WOFF2 format

Subset to Latin glyphs using `pyftsubset` (fonttools).

---

## Next Steps

- [ ] Download fonts (Inter, Inter Display, JetBrains Mono)
- [ ] Subset to Latin (~60KB each)
- [ ] Set up font-face declarations
- [ ] Implement kinetic weight transitions
- [ ] Apply gold gradient to hero headline
- [ ] Test performance (Lighthouse)

---

**Full analysis:** See `TYPOGRAPHY-RESEARCH.md`
