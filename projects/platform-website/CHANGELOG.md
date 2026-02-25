# Changelog — Ainary Platform

## v2.5.0 — 2026-02-25 — Election Intelligence Launch

### Blog
- Neuer Artikel: "Kommunalwahl Bayern 2026: Warum es in 5 von 8 Städten zur Stichwahl kommt" (DE + EN)
- EIJA-Transparenzsystem, Live-Countdown, Share-Bar (Stripe-Pattern), Product Card (full-bleed)
- Social Proof Box (+12% Turnout Harvard, €50K+ Preisanker), Dual CTA, Newsletter via eigene API
- Autorenfoto (echtes JPEG), Status-Badge ("Hohe Nachfrage"), "More from Ainary" Section
- Titel: Curiosity Gap ("Warum") + SEO "2026", Subtitel "10+ Städte, 300+ Quellen"
- Konsistenz mit AgentTrust: Binary Star BG, Reading Progress, Fade-in, JSON-LD, Breadcrumb

### Demo-Modus
- Information Gap: Struktur zeigen, Wert verbergen. Embed-Modus (?embed=1)
- "Kontroverse" → "Risikosignal" (überall)
- Einordnungen, Talking Points, €-Beträge, URLs, Quellenanalyse geblurt
- Themen: nur Name + Score sichtbar

### Blog-Index
- "Election Intelligence" Tab (DE + EN), Stichwahl-Artikel als Featured

### Navigation
- nav.js + footer.js: Blog-Subdir-Routing gefixt
- Alle Links konsistent DE/EN, hreflang Tags, EN/DE Switch Override

### API
- `/api/subscribe`: Email-Sammlung (POST → /tmp JSONL)

### Outreach
- Gmail-Drafts: Freund (SPD Augsburg) + Kramer (Stadt Fürth)

### Assets
- florian-400.jpg + florian.jpg: Korrupte/fehlende Dateien ersetzt
- dashboard-preview.png, bayern-radar-v2.png

---

## 2026-02-24

### Added
- `radar.html` — Sales Intelligence Dashboard (28 Städte, Scores, Prioritäten)
- `radar-data.json` — Externalized city data (dynamic loading)
- `radar-scout.md` — Intelligence Collector Spec für Cron-Agent
- `ARCHITECTURE.md` — ADR-005: One Template, N Datasets
- Breadcrumb navigation across all 3 levels (Radar → Briefing → Dossier)

### Fixed
- Graph crash in digi-dashboard + gotham pages (missing r/group/info fields)
- Defensive schema mapping: `n.r = n.r || n.size || 12`

### Architecture
- Separated data (JSON) from presentation (HTML)
- radar.html loads radar-data.json dynamically, falls back to hardcoded
- Prepared for: dossier.html template, dashboard.html template, legacy redirects
