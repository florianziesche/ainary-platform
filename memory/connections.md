# Connections — Knowledge Graph
*Jede Erkenntnis mit 2-3 Verbindungen zu bestehendem Wissen. Isolierte Fakten = wertlos.*

## C-001: AgentTrust × Glasswing Five-Stage Framework
- **Fakten:** T-001 (95% AI pilots fail), T-002 (Fund III $200M)
- **Insight:** AgentTrust löst das Stage 2→3 Problem das Glasswing beschreibt — Calibration ist der fehlende Mechanismus für Adaptive Orchestration
- **Implikation:** Dieser Angle funktioniert bei JEDEM AI-Fund, nicht nur Glasswing
- **Angewandt:** Cover Letter Glasswing (2026-02-17)
- **Next:** Gleichen Hook für Radical Ventures + Conviction testen

## C-002: Context Engineering × Agent Performance
- **Fakten:** T-003 (3K token degradation), T-004 (Lost-in-the-Middle)
- **Insight:** Weniger System Prompt = bessere Antworten. Nicht linear — exponentiell. Jede neue Zeile hat negativen Marginalwert für alle anderen.
- **Implikation:** SOUL.md Compression (80→28) verbessert nicht nur Token-Budget sondern die Qualität ALLER Regeln
- **Next:** Messen ob Trust Score nach Compression steigt (Baseline: 4/100)

## C-003: Eat-Your-Own-Dogfood × Credibility
- **Fakten:** AgentTrust Python Repo existiert, Mia nutzte es nicht selbst
- **Insight:** Wer Trust-Infra baut und nicht selbst nutzt hat keine Credibility. Jetzt integriert: trust_score.py, 8-Dim Rubric, Trust Levels
- **Implikation:** Jeder VC-Pitch kann jetzt sagen "wir nutzen das selbst, hier sind die Daten" — Demo statt Theorie
- **Next:** Trust Score in Glasswing Cover Letter als Live-Beispiel referenzieren?

## C-004: Compound Intelligence × Flat Architecture Problem
- **Fakten:** 30+ Memory-Files, alle gleichwertig, keine Verbindungen
- **Insight:** Flat Architecture = Notizbuch. Layered Graph = Gehirn. Verbindungen SIND der Wert, nicht die einzelnen Fakten.
- **Implikation:** Diese Datei (connections.md) ist das wertvollste Memory-File — sie macht alle anderen Files wertvoller
- **Next:** Jede Session sollte mindestens 1 Connection hinzufügen

## C-005: Seligman Ventures × Public/Private Market Convergence
- **Fakten:** T-015 ($500M fund Feb 12), T-016 (Padval+Wick team), T-017 (early-stage infra focus)
- **Insight:** Seligman ist der EINZIGE Fund der aktiv die Public/Private Grenze überbrückt — Padval (early-stage VC) + Wick (Public Markets CIO bei $30B Seligman). Problem: Spät-stage VCs pumpen Valuations, IPOs fallen flach → LÖSUNG: Früh rein, public market discipline von Tag 1.
- **Implikation:** Florians Story (36ZERO raised €5.5M, saw the scaling gap, now solves it operationally) ist PERFEKT für Seligman — Public-Market Mindset + Operator Background
- **Angle:** "You bridge public/private. I bridge pilot/production. Both gaps kill 90%+ of companies."
- **Next:** Custom cover letter für Seligman mit diesem Angle

## C-006: Glasswing Portfolio Depth × AgentTrust Fit
- **Fakten:** T-019 (60+ portfolio cos), T-001 (95% AI pilots fail to scale)
- **Insight:** Glasswing hat SECHZIG Portfolio-Firmen die alle im Stage 2→3 Gap stecken. Cydelphi (DFIR), Verusen (MRO Inventory), Base Operations (Threat Intel) — alle bauen Agents, keiner hat Calibration Infra.
- **Implikation:** AgentTrust ist nicht nur Thesis-fit, es ist ein **Multiplier für das gesamte Portfolio**. 1 Platform × 60 Unternehmen = sofortiger Wertzuwachs über die gesamte Portfoliobreite.
- **Next:** Cover Letter Glasswing — "AgentTrust doesn't just fit your thesis, it upgrades your entire portfolio"

## C-007: Glasswing Portfolio × AgentTrust Product-Portfolio Fit
- **Fakten:** T-027 (6 AI agent cos: Asepha, Basetwo, Allure, Beacon, Black Kite, ChaosSearch), C-006 (60+ total portfolio)
- **Insight:** **Asepha** ist die PERFEKTE AgentTrust Beta-Kundin — agentic pharma platform, high-stakes (drug errors = lives), regulatory compliance (FDA), existing system integration. Wenn AgentTrust bei Asepha funktioniert, funktioniert es überall.
- **Implikation:** Cover Letter Glasswing sollte Asepha NAMENTLICH nennen — "I'd love to help Asepha calibrate their pharma agents for FDA compliance."
- **Next:** Glasswing Cover Letter update mit Asepha-Angle

## C-008: AgentTrust Competitive Landscape × Differentiation
- **Fakten:** T-022 (LangSmith observability), T-023 (Arize Phoenix), T-024 (Galileo), T-030 (LangSmith $2.50-$5/1K traces), T-031 (Phoenix FREE-$50/mo)
- **Insight:** "No competition" war FALSCH. Observability existiert (LangSmith, Arize, Galileo). ABER: Sie tracen, sie monitoren, sie alerten — KEINER kalibriert. AgentTrust ist NICHT "better observability", sondern **Calibration Layer ÜBER Observability**. Budget-CoCoA, Trust Scores, Beipackzettel = neues Problem, nicht bessere Lösung für altes Problem.
- **Pricing Gap:** LangSmith $2.50-$5/1K traces (observability) vs AgentTrust $0.005/check (calibration) = 500× billiger, unterschiedliches Problem. AgentTrust ist ADD-ON, nicht Konkurrent.
- **Implikation:** Positioning shift. NICHT "we monitor agents better" sondern "we calibrate agent trust — observability tells you WHAT happened, calibration tells you IF you can trust it".
- **Integration:** LangSmith/Arize = PARTNER, nicht Konkurrent. Sie liefern Traces → AgentTrust berechnet Trust Scores. Phoenix FREE self-hosted + AgentTrust SDK = perfektes Startup-Bundle.
- **Next:** AgentTrust README muss Arize/LangSmith als Integration Partners positionieren

## C-009: Asepha × AgentTrust Perfect Product-Market Fit
- **Fakten:** T-029 (Asepha: Can Uncu ex-AMD MI300X, 96% OCR accuracy, Fortune 50, HIPAA/SOC2), T-027 (Glasswing Portfolio), C-007 (Asepha als Beta-Kundin)
- **Insight:** Can Uncu (CTO) baute AMD MI300X chip (powers OpenAI/Azure) → versteht LLM Stack auf Hardware-Ebene. 96% OCR accuracy + 71% preference vs human = **sie BRAUCHEN Calibration für die restlichen 4%/29%**. Fortune 50 customers in pharma = extreme regulatory pressure (FDA), Fehler = Klagen/Leben. Asepha löst Admin-Bottleneck (70% understaffed), AgentTrust löst Trust-Bottleneck (wie vertraust du dem Agent bei 4% Fehlerrate?).
- **Contact:** CEO Eunice Wu (PharmD), CTO Can Uncu; asepha.ai, linkedin.com/company/asepha; NYC office opening
- **Intro Path:** Glasswing Portfolio → Rudina Seseri (Glasswing Partner, Asepha Lead Investor) → Warm Intro zu Eunice/Can
- **Pitch Angle:** "You automated 96% of pharmacy data entry. AgentTrust calibrates the trust boundary for the other 4% — so you know WHEN to escalate to a human pharmacist vs when the agent is confident enough."
- **Next:** Florian VC application → Glasswing → Name-drop Asepha in cover letter → Get intro after hire
