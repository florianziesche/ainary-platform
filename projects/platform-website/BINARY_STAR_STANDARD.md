# Binary Star Animation — Quality Standard

## What "Premium" Means (Reference: Stripe, Linear, Palantir)
1. **Less is more** — Fewer particles, more intention. Every element has purpose.
2. **Smooth over busy** — No noise, no chaos. Movement should feel like breathing.
3. **Glow over particles** — The connection between stars should be a LIGHT phenomenon, not a particle storm.
4. **The connection** — A soft luminous bridge (like an accretion stream or gravitational lens), NOT scattered dots flying between points.
5. **Speed** — Everything moves SLOWER than you think. Hypnotic, meditative.
6. **Color restraint** — Gold + Silver-white only. No extra colors. Opacity does the work.

## Current Issues (v1 Feedback)
- ❌ Stream particles between stars = too noisy, chaotic
- ❌ Too many particles competing for attention
- ❌ Connection looks like scattered dots, not a luminous bridge

## v2 Requirements
- ✅ Replace stream particles with a **smooth luminous bridge** (gradient arc between stars)
- ✅ Bridge should pulse/breathe subtly (opacity oscillation)
- ✅ Reduce total particle count by 60%
- ✅ Keep orbital trail particles (subtle, small)
- ✅ Keep ambient stars (very few, very subtle)
- ✅ Stars themselves: multi-layer glow (keep, this is good)
- ✅ The bridge = the hero element. Smooth bezier curve with soft gaussian glow.

## Technique for the Bridge
Instead of 250 stream particles: 
- Draw a **bezier curve** between the two stars
- Apply **gaussian blur** via shadow (ctx.shadowBlur)
- Animate control points to create gentle wave motion
- Vary opacity along the curve (brighter near stars, dimmer in middle)
- Add 2-3 thin secondary curves at slight offsets for depth
- Total: 3 curves instead of 250 particles

## Quality Checklist
- [ ] Can you tell it's handcrafted, not a tutorial demo?
- [ ] Does it feel like it belongs on stripe.com?
- [ ] Is the connection between stars SMOOTH (no noise)?
- [ ] Would you show this to a VC in a meeting?
- [ ] Does it enhance the hero text, not distract?
