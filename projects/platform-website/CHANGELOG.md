# Platform Website — Version Changelog

*Jede Version wird archiviert + Learnings dokumentiert. So wird jeder Build besser.*

---

## v1 — 2026-02-12 10:20
**Archiv:** `archive/v1-2026-02-12/`
**Dateien:** index.html (erster Landing Page Build), pricing-tier.html, pricing-credits.html, pricing-simple.html

**Was gut war:**
- Grundstruktur stand schnell
- Glassmorphism + Gold sah "cool" aus auf den ersten Blick
- Pricing Credits Calculator war ein guter UX-Touch

**Was nicht gut war:**
- Zu viel Glassmorphism (2023-Ästhetik)
- Bold (700) statt Semibold (600) — wirkt billig
- Zu wenig Spacing — Seite wirkte eng
- Emoji statt Custom SVG Icons
- Design nicht auf Linear-Niveau — zu "template-haft"
- Kein Design System → jeder Build sah anders aus

**Learnings:**
1. IMMER Design System ZUERST, dann bauen
2. Spacing ist wichtiger als Dekoration
3. Glassmorphism weglassen — solide Hintergründe + subtile Borders
4. Max font-weight 600
5. Restraint > Decoration

---

## v2 — 2026-02-12 11:15
**Archiv:** `archive/v2-2026-02-12-landing-iteration/`
**Dateien:** landing.html (nach DESIGN-SYSTEM.md), design-system.html (Component Library)

**Was besser ist vs v1:**
- Design System als Basis → konsistente Farben, Fonts, Spacing
- Geist + Inter + JetBrains Mono statt nur Inter
- Kein Glassmorphism, subtile Borders
- Mehr Text und Kontext (Hero Detail, Why Section, Tool Meta Tags)
- Trend-Words integriert (Agentic AI, Source-grounded, Multi-agent)
- Trusted By entfernt (fake ohne echte Logos)
- Stats: 90sec/243/5 statt $0.15 (Kundenwert statt unsere Kosten)
- Custom SVG Icons (Lucide) statt Emoji

**Was noch fehlt:**
- Noch nicht auf Linear-Niveau (Details: Micro-Interactions, Polish)
- Product Screenshot ist Placeholder
- Keine echten Social Proof Logos
- Mobile noch nicht perfekt getestet
- Pricing Page noch nicht mit neuem Design System

**Learnings:**
1. Mehr Text = mehr Überzeugung (wir müssen ERKLÄREN, Linear muss das nicht)
2. Trend-Words in Tool-Descriptions + Meta-Tags funktionieren gut
3. "Why" Section mit 3 Cards ist stark — zeigt Differenzierung
4. Hero braucht 2 Ebenen: Emotional (Subtitle) + Rational (Detail)
5. Archivieren + Changelog = wir vergessen nichts zwischen Sessions

---

*Nächste Version: v3 — Pricing Page Credits (nach Design System)*
