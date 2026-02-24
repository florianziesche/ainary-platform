# Changelog — Ainary Platform

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
