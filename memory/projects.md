<!-- temporal: stable | decay: monthly | last-reviewed: 2026-02-13 -->
# Projects — Was läuft

## 🔴 Aktiv

### AgentTrust Framework (NEU 2026-02-14)
- Open Source Trust Framework für AI Agents — "so groß wie LangChain"
- Core: Calibration (Budget-CoCoA), Trust Scores, Beipackzettel, QA Pipeline
- Integrations: LangChain, CrewAI, AutoGen, OpenAI/Anthropic
- Optional: Blockchain Trust Verification (on-chain Scores)
- Revenue: Open Source + SaaS Dashboard + Enterprise
- Prototyp existiert (unsere Agent Pipeline), Repo noch nicht erstellt
- Research bestätigt: KEINE Konkurrenz in Production
- Content Flywheel: 5 Artikel → Repo → Credibility → Repeat

### Execution Platform / CKE (v0.12.7, 2026-02-19)
- **Version:** v0.12.7, 85 API endpoints, 27 DB tables, 56 tests
- **GitHub:** github.com/florianziesche/ainary-platform (PRIVATE)
- **Stack:** Bottle + SQLite + vanilla JS, localhost:8080, launchctl auto-restart
- **Features:** Executive Board (CEO/COO Tabs, KPIs, Impact Summary), Pipeline View (Kanban), Evidence Gates (E/I/J/A), Stage Views (Research/Systems/Content/Revenue), Activity Feed (14-day chart), Backlog, Decisions Log, Daily Standup Scoring, Mia Bridge (SSE), Pre-Flight Gate, Trust per Skill (9 skills), Quality Gate, So What AI-generation, Command Palette (Cmd+K), Principles View (Cmd+I)
- **Documentation:** 13 docs (README, ARCHITECTURE, DOCUMENTATION, DB-SCHEMA, FORMULAS, CHANGELOG, DEPENDENCIES, DESIGN-DOC, ROADMAP, PLATFORM-SPEC, SECURITY, TESTING, RUNBOOK)
- **Standards:** R2 Deep Dive Research, S1 Ersttermin-Prep, Agent Context Package
- **Decisions:** D-151 to D-187
- **Done-Def v1:** Fehlerfrei + Live AI + Trust System + 5 VC Emails durch Platform gesendet
- **Key Insight:** Platform IST das Produkt. AI Workforce Management System. Dogfooding → Pilot → Scale.
- **Pilot-Kunden:** Bürgermeister Glashütte (Mo 23.02), Andreas (Maschinenbau)
- **Tech Stack für Piloten:** OpenClaw + Obsidian + Dashboard
- **Issue:** main.sqlite = 14 GB, disk 6.1 GB free

### Ainary Platform Website
- **Status:** LIVE https://platform-website-lilac.vercel.app
- **GitHub:** https://github.com/fziescheus-alt/ainary-platform (private)
- **Stack:** Static HTML, Vercel, shared-cta.js Footer
- **Design:** Black + White + Gold (#c8aa50) ONLY
- **Seiten:** 18+ EN, 12 DE. Hamburger mobile nav. Full bilingual.
- **Deploy:** `cd projects/platform-website && cp landing.html index.html && git add . && git commit && vercel --prod --yes`
- **TODO:** Custom domain, Stripe, Mobile polish

### Python Research Pipeline (NEU 2026-02-17)
- **Pfad:** `projects/research-pipeline/pipeline.py`
- **Stack:** Multi-model routing (Haiku→Sonnet→Opus), ~$1.34/report
- **Budget:** $200 = ~149 reports
- **Needs:** ANTHROPIC_API_KEY env var

### AI Company X-Ray
- **Status:** Funktioniert. BMW, Siemens, MBS Reports generiert.
- **Pfad:** `projects/ai-company-xray/xray.js`
- **Usage:** `node xray.js "Company Name"` → HTML + PDF
- **Cost:** ~$0.15/report, 5 Agents, 3 Hyperthink Rounds

### Startup X-Ray
- **Status:** v3 gebaut. Stripe Report generiert.
- **Pfad:** `projects/startup-xray/xray.js`

### Content Engine
- **6 Artikel reviewed** in Vault (ready to publish!)
- **3 Artikel** auf Website (EN + DE)
- **Content-Queue** in Vault mit Posting-Schedule
- **Substack:** https://finitematter.substack.com/

### VC Job Search
- **Primary Venture Partners:** SUBMITTED 18.02 ✅ (OIR: Agents, Primary Labs)
  - Brian Schechter (Partner), $125K-$175K, NYC/SF
  - CV v2 custom (monochromatic, Primary brand match)
  - Campaign "Project BSchech": 7-channel approach (portal + VC Lab + intros + Twitter + LinkedIn + physical + Etched)
- **HOF Capital:** SUBMITTED 13.02 ✅
- **Betaworks, Leonis, Wingspan:** Ready, not submitted
- **50-Fund Pipeline** (2026-02-17): `research/inbox/vc-pipeline-50-funds-2026-02-17.md`
- Top: Glasswing, Radical ($1.8B), Earlybird/HV/La Famiglia, Conviction, Nyca
- NEW: FutureSight (EIR NYC), Seligman ($500M, launched Feb 12!), Innovate.VC (EIR)
- **5 cold outreach drafts** ready, not sent

### Freelance / CNC
- **MBS:** X-Ray Report generiert 13.02. Andreas Email pending seit 06.02.
- **Funkwerk:** Email-Draft TODO
- **19 Outreach Emails** ready (15 alt + 4 Bayern)
- **Case Study MBS:** 92% Zeitersparnis

### Fundraising Lessons (NEU 13.02)
- **Interview-Format:** 5/10 Fragen beantwortet
- **Vault:** 60_Resources/Lessons/Fundraising-Mistakes.md
- **Unique Content** für Blog + Vault

## 🟡 Paused
- Freie Presse KI (Daniel Daum called, waiting)
- BM Glashütte (WhatsApp gesendet 17.02, Terminvorschläge Mi-Fr ab 15h, Mo-Di 9-14h)
- Bürgergeld/ALG1 (Restanspruch unklar)

## 🔵 Infrastructure (nicht Revenue)
- Research Engine v2
- AI Advisory Board v2
- Daily Brief Page
- Vault PARA Struktur (Bulk fix done: 79→13 orphans)

### AgentTrust Key Numbers (Consulting-Ammo)
- Budget-CoCoA: **$0.005 pro Check** (3× Haiku)
- Agent-Fehler: **$5K-$50K+ pro Incident** (Air Canada, McDonald's, VW)
- **ROI: 333x-3.333x** — Break-Even ab dem ERSTEN verhinderten Fehler
- Hallucination Rates: 0.7%-30% je nach Modell (Vectara Index)
- Cases: Air Canada (Halluzination→Klage), McDonald's (Compounding→Programm beendet), Replit (Agent lügt aktiv), VW ($7.5B)

### TrustCheck as Ainary Service — BACKLOG (2026-02-14)
- Concept: Claim-level fact-checking als Service
- Format: Traffic-Light System (Verified/Partially/False) pro Claim
- Input: URL oder Text → Output: PDF Report mit Claim Register
- Monetarisierung: Free (1/Tag) → Pro ($X/Monat)
- Demo existiert bereits (TrustCheck, QA 88/100)
- Priority: NACH Reports + Launch
