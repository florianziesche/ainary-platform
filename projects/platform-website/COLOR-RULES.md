# Color Rules — Ainary Design System

## The Rule
**Black, white, and gold. Nothing else.**

## What's Allowed
- `#c8aa50` / `var(--gold)` — THE accent color. For emphasis, key values, highlights, buttons, links, badges
- `rgba(200,170,80,0.12)` — Subtle gold backgrounds for tags, badges
- `rgba(200,170,80,0.20)` — Gold borders for highlighted elements
- `var(--text-primary)` (#ededf0) — All data values, headings
- `var(--text-secondary)` (#8b8b95) — Body text, descriptions
- `var(--text-muted)` (#55555e) — Timestamps, meta info
- `var(--border-default)` — All borders, dividers
- `rgba(255,255,255,0.04-0.15)` — Subtle backgrounds

## What's NOT Allowed
- ❌ `color:#ef4444` (red)
- ❌ `color:#f59e0b` (amber)
- ❌ `color:#10b981` (green/emerald)
- ❌ `color:#8b5cf6` (purple)
- ❌ `color:#06b6d4` (cyan)
- ❌ `color:#6366f1` (indigo) — replace with gold or white
- ❌ Any neon/saturated color
- ❌ Traffic light colors on metrics

## Replacements
| Before | After |
|--------|-------|
| `color:#ef4444` | `color:var(--text-primary)` |
| `color:#f59e0b` | `color:var(--text-primary)` |
| `color:#10b981` | `color:var(--text-primary)` |
| `color:#8b5cf6` | `color:var(--text-secondary)` |
| `color:#06b6d4` | `color:var(--text-secondary)` |
| `color:#6366f1` | `color:#c8aa50` (for emphasis) or `var(--text-secondary)` |
| `background:rgba(99,102,241,0.12)` | `background:rgba(200,170,80,0.12)` or `rgba(255,255,255,0.04)` |
| `background:rgba(139,92,246,0.12)` | `background:rgba(255,255,255,0.04)` |
| `background:rgba(6,182,212,0.12)` | `background:rgba(255,255,255,0.04)` |
| `border:1px solid rgba(99,102,241,0.25)` | `border:1px solid var(--border-default)` |
| `var(--accent)` on buttons | → `#c8aa50` or `var(--gold)` |

## The Palette
```
Background:  #08080c (page), #111116 (surface), #1e1e26 (elevated)
Text:        #ededf0 (primary), #8b8b95 (secondary), #55555e (muted)
Accent:      #c8aa50 (gold) — THE ONLY COLOR
```

## Why
Florian's feedback: "Statt der Neonfarbe lieber mein Gelb-Gold nehmen und sonst mit weiß und schwarz arbeiten."
Black + White + Gold = Professional, premium, brand-consistent.

*Created: 2026-02-13*
