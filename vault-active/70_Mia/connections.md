---
tier: KNOWLEDGE
expires: 2027-02-19
---
# Connections — Knowledge Graph
*Jede Erkenntnis mit 2-3 Verbindungen zu bestehendem Wissen. Isolierte Fakten = wertlos.*

## C-001: AgentTrust × Glasswing Five-Stage Framework
- **Fakten:** T-001 (95% [[AI]] pilots fail), T-002 (Fund III $200M)
- **Insight:** AgentTrust löst das Stage 2→3 Problem das Glasswing beschreibt — Calibration ist der fehlende Mechanismus für Adaptive Orchestration
- **Implikation:** Dieser Angle funktioniert bei JEDEM [[AI]]-Fund, nicht nur Glasswing
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
- **Implikation:** Jeder [[VC]]-Pitch kann jetzt sagen "wir nutzen das selbst, hier sind die Daten" — Demo statt Theorie
- **Next:** Trust Score in Glasswing Cover Letter als Live-Beispiel referenzieren?

## C-004: Compound Intelligence × Flat Architecture Problem
- **Fakten:** 30+ Memory-Files, alle gleichwertig, keine Verbindungen
- **Insight:** Flat Architecture = Notizbuch. Layered Graph = Gehirn. Verbindungen SIND der Wert, nicht die einzelnen Fakten.
- **Implikation:** Diese Datei (connections.md) ist das wertvollste Memory-File — sie macht alle anderen Files wertvoller
- **Next:** Jede Session sollte mindestens 1 Connection hinzufügen

## C-005: Seligman Ventures × Public/Private Market Convergence
- **Fakten:** T-015 ($500M fund Feb 12), T-016 (Padval+Wick team), T-017 (early-stage infra focus)
- **Insight:** Seligman ist der EINZIGE Fund der aktiv die Public/Private Grenze überbrückt — Padval (early-stage [[VC]]) + Wick (Public Markets CIO bei $30B Seligman). Problem: Spät-stage VCs pumpen Valuations, IPOs fallen flach → LÖSUNG: Früh rein, public market discipline von Tag 1.
- **Implikation:** Florians Story (36ZERO raised €5.5M, saw the scaling gap, now solves it operationally) ist PERFEKT für Seligman — Public-Market Mindset + Operator Background
- **Angle:** "You bridge public/private. I bridge pilot/production. Both gaps kill 90%+ of companies."
- **Next:** Custom cover letter für Seligman mit diesem Angle

## C-006: Glasswing Portfolio Depth × AgentTrust Fit
- **Fakten:** T-019 (60+ portfolio cos), T-001 (95% [[AI]] pilots fail to scale)
- **Insight:** Glasswing hat SECHZIG Portfolio-Firmen die alle im Stage 2→3 Gap stecken. Cydelphi (DFIR), Verusen (MRO Inventory), Base Operations (Threat Intel) — alle bauen Agents, keiner hat Calibration Infra.
- **Implikation:** AgentTrust ist nicht nur Thesis-fit, es ist ein **Multiplier für das gesamte Portfolio**. 1 Platform × 60 Unternehmen = sofortiger Wertzuwachs über die gesamte Portfoliobreite.
- **Next:** Cover Letter Glasswing — "AgentTrust doesn't just fit your thesis, it upgrades your entire portfolio"

## C-007: Glasswing Portfolio × AgentTrust Product-Portfolio Fit
- **Fakten:** T-027 (6 [[AI]] agent cos: Asepha, Basetwo, Allure, Beacon, Black Kite, ChaosSearch), C-006 (60+ total portfolio)
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
- **Insight:** Can Uncu (CTO) baute AMD MI300X chip (powers OpenAI/Azure) → versteht [[LLM]] Stack auf Hardware-Ebene. 96% OCR accuracy + 71% preference vs human = **sie BRAUCHEN Calibration für die restlichen 4%/29%**. Fortune 50 customers in pharma = extreme regulatory pressure (FDA), Fehler = Klagen/Leben. Asepha löst Admin-Bottleneck (70% understaffed), AgentTrust löst Trust-Bottleneck (wie vertraust du dem Agent bei 4% Fehlerrate?).
- **Contact:** CEO Eunice Wu (PharmD), CTO Can Uncu; asepha.ai, linkedin.com/company/asepha; NYC office opening
- **Intro Path:** Glasswing Portfolio → Rudina Seseri (Glasswing Partner, Asepha Lead Investor) → Warm Intro zu Eunice/Can
- **Pitch Angle:** "You automated 96% of pharmacy data entry. AgentTrust calibrates the trust boundary for the other 4% — so you know WHEN to escalate to a human pharmacist vs when the agent is confident enough."
- **Next:** Florian [[VC]] application → Glasswing → Name-drop Asepha in cover letter → Get intro after hire

## C-010: Platform als Produkt × Consulting Pilots
- **Fakten:** T-038 (Tech Stack: OpenClaw+Obsidian+Dashboard), T-039 (Platform = Firma), D-180 (Multi-Path Revenue)
- **Insight:** Jeder Consulting-Pilot ist gleichzeitig ein Platform-Pilot. Der Bürgermeister kauft nicht "Beratung", er kauft ein Dashboard das seine Verwaltung transparenter macht. Andreas kauft nicht "[[AI]]-Beratung", er kauft ein System das Angebote automatisiert. Das Produkt verkauft sich über den Pilot, nicht über einen Sales-Pitch.
- **Implikation:** Pricing = Pilot-Gebühr (€15-30K) + laufende Platform-Lizenz (€49-499/mo). Pilot refinanziert sich über Förderung, Platform wird recurring revenue.

## C-011: Bürgermeister × OZG × Förderung = Triple Fit
- **Fakten:** T-032 (Glashütte 7K EW), T-033 (OZG <30%), T-034 (Dippoldiswalde weiter), T-035 (EFRE bis 60%), T-037 (20-40% realistisch)
- **Insight:** OZG-Deadline zwingt Kommunen zu handeln. Förderung senkt Risiko auf ~40% Eigenanteil. Dippoldiswalde-Vergleich erzeugt sozialen Druck. Triple Fit: regulatorischer Druck + finanzielle Unterstützung + Wettbewerbsvergleich = idealer Pilot-Kontext.
- **Implikation:** Pitch-Struktur: "Das Gesetz fordert es (OZG), das Land fördert es (EFRE), die Nachbarn machen es schon (Dippoldiswalde). Wir helfen Ihnen dabei."

## C-012: Evidence System (E/I/J/A) × Landing Page × Trust as Currency
- **Fakten:** D-184 (Ehrliche Impact-Metriken), D-187 (50-Jähriger MacBook Test), Landing Page [[Ainary]]ventures.com
- **Insight:** Das Evidence System (E/I/J/A) ist gleichzeitig internes Qualitäts-Tool UND externes Verkaufsargument. "Jeder Claim ist nach Evidenz-Typ getaggt" differenziert von jeder normalen Beratung. Kunden sehen: diese Leute quantifizieren Unsicherheit statt sie zu verstecken. Das IST das Produkt.
- **Implikation:** E/I/J/A muss in der Demo-Ansicht für Kunden prominent sichtbar sein (wie auf der Landing Page).

## C-013: E/I/J/A × GRADE Framework × "Medical Rigor for Business"
- **Fakten:** T-045 (GRADE = CDC/WHO Standard), E/I/J/A System ([[Ainary]])
- **Insight:** GRADE (High/Moderate/Low/Very Low) bewertet CERTAINTY of Evidence (RCT vs Observational). E/I/J/A klassifiziert TYPE of Evidence (Empirical/Inferred/Judgment/Assumption). **Kein Widerspruch — ERGÄNZEND.** GRADE = Studien-Qualität, E/I/J/A = Evidenz-Typ. Beide quantifizieren Unsicherheit, unterschiedliche Achsen.
- **Positionierung:** "GRADE für Consulting" — medizinische Rigorosität für Business-Entscheidungen. Kein anderes Consulting-Framework macht das.
- **Differentiator:** Jeder Berater sagt "datenbasiert". Wir sagen "E/I/J/A-getaggt nach GRADE-Prinzipien". Das ist SPEZIFISCH und VALIDIERBAR.
- **Next:** Landing Page + Pitch Decks sollten GRADE referenzieren: "Wir bringen den Gold-Standard medizinischer Evidenz-Bewertung ins Business."

## C-014: ICP Framework × Platform-Piloten × HUNTER Agent
- **Fakten:** T-044 (ICP 7-Step Framework), T-041 (HUNTER = BDR), C-010 (Platform als Produkt)
- **Insight:** HUNTER braucht systematischen ICP, nicht Ad-hoc-Liste. FullFunnel.io Framework = Industry-Standard (7 Schritte, 5 Pillars). Anwendung auf Platform-Piloten:
  - **Segment:** KMU/Kommunen (Admin-Bottleneck + OZG) ODER Mittelstand (Angebots-Bottleneck)
  - **Firmographics:** €5-50M revenue OR 2-20K EW, 10-200 Mitarbeiter
  - **Buying Committee:** CEO/Bürgermeister (Decision-Maker) + Verwaltungsleiter/Projektleiter (Champion)
  - **Qualification:** Admin-Bottleneck + Förderung verfügbar + Wettbewerbsdruck (OZG/Nachbar-Gemeinde)
  - **Disqualification:** <€3M revenue, >500 Mitarbeiter, keine Förderung, IT-Dienstleister (haben eigene Kapazität)
- **Implikation:** Bürgermeister Glashütte + Andreas = 2 Data Points. Nach Pilot-Validierung → 10 Customer Interviews → ICP v1.0 → HUNTER kann systematisch suchen.
- **Next:** Nach beiden Piloten: Diver Survey Method (6 Fragen-Gruppen) auf Bürgermeister + Andreas anwenden.

## C-015: EFRE Antragsberechtigung × Glashütte Pilot × Förderungs-Strategie
- **Fakten:** T-042 (EFRE nur KMU, Kommunen wenn gewerblich), T-043 (60% bis €10K), T-035 alt (Widerspruch aufgelöst)
- **Insight:** **PROBLEM:** Glashütte ist KEINE KMU, sondern öffentliche Verwaltung. EFRE Digitalisierungszuschuss sagt explizit "KMU + Freiberufler", NICHT Kommunen. Die allgemeine EFRE-Seite sagt "Kommunen können Begünstigte sein", aber die SPEZIFISCHE Richtlinie schließt sie aus.
- **Lösung 1:** Bürgermeister gründet kommunale GmbH (gewerbliche Tätigkeit) → antragsberechtigt. Kompliziert, dauert.
- **Lösung 2:** Andere Förderprogramme prüfen (nicht EFRE Digitalisierung): SAB Innovationsförderung, Kommunalrichtlinie, etc.
- **Lösung 3:** KEIN Zuschuss, Pilot zu 100% bezahlt (€15-30K). Florian argumentiert: "Investment in Modernisierung, refinanziert sich über Effizienz."
- **Implikation:** EFRE war Hypothese (70% Conf → 60% Conf). ERST mit Bürgermeister klären: "Sind Sie bereit, ohne Förderung zu starten?" DANN Förderantrag parallel prüfen.
- **Confidence:** 75% — Rechtslage klar, Lösungswege existieren, Execution-Risiko mittel.
- **Next:** Vor Termin Mo 23.02 → SAB direkt anrufen, Antragsberechtigung Kommunen klären.

## C-016: Primary Venture Partners Application × Follow-up Strategy × Multi-Channel Persistence
- **Fakten:** T-046 (1-2 weeks follow-up best practice), T-047 (immediate LinkedIn DM = top of stack), Primary submitted 18.02 (gestern)
- **Insight:** Primary "7-channel approach" (portal + VC Lab + intros + Twitter + LinkedIn + physical + Etched) ist GUT, ABER timing matters. **Immediate LinkedIn DM > alles andere.** Konsens: Email follow-up 1-2 weeks post-submit, ABER LinkedIn community experts sagen "same day DM = top of stack, shows interest". Multi-channel = OK wenn tiered (Email → Voicemail → Front Desk), nicht parallel spam.
- **Action Plan:**   1. **HEUTE (19.02):** LinkedIn DM an Brian Schechter — kurz, VALUE-focused: "I applied yesterday for the OIR role. My background (36ZERO GTM, AgentTrust framework) maps directly to Primary Labs' portfolio challenges. Happy to discuss how I can accelerate Stage 2→3 transitions across your companies."
  2. **26.02 (1 week):** Email follow-up if no response — same value angle, slightly expanded
  3. **05.03 (2 weeks):** Multi-channel (Twitter DM, physical letter) if total silence
- **Differentiation:** Florian's "7-channel" is AGGRESSIVE but STRATEGIC. Most candidates do 0-1 follow-ups. Florian's persistence = signal of operator mindset.
- **Risk:** Too aggressive = spam. Mitigation: Space out, VALUE in every touch (nicht "checking in"), respect non-response after 3 touches.
- **Confidence:** 90% — Multi-source consensus, Florian has Brian's LinkedIn, timing is NOW.
- **Next:** Draft LinkedIn DM, send heute/morgen.

## C-017: ICP Early-Stage Definition × Florian's 2 Piloten × PostHog Validation Framework
- **Fakten:** T-048 (5 customers = good, 10+ = strong), T-049 (Pre-PMF = JTBD not Firmographics), T-050 (Cold outbound = honest signals), C-014 (HUNTER ICP hypothesis)
- **Insight:** Florian hat 0 paying customers, 2 Piloten geplant (Glashütte, Andreas) → **zu früh für finalen ICP, ABER initial ICP mit 3 Attributen = OK (Lenny Rachitsky).** PostHog sagt "5 customers who look the same = good sign" → Florian's nächster Meilenstein: **5 Piloten in 90 Tagen** (nicht 1-2).
- **Current ICP Hypothesis (v0.1, 3 Attributes):**   1. **Admin-Bottleneck:** 36% founder/Bürgermeister time on admin (Forbes/Time)
  2. **Förderung verfügbar:** EFRE/Bayern Digital/SAB (senkt Risiko auf 40-60%)
  3. **Wettbewerbsdruck:** OZG-Deadline OR Industrie 4.0 OR Nachbar-Gemeinde weiter
- **Validation Path:**   - **2 Piloten (Feb-Mar):** Glashütte + Andreas → Retention + Aktivierung tracken
  - **10 Interviews (Apr):** Discovery Calls mit ähnlichen Profilen (Kommunen + Mittelstand)
  - **ICP v1.0 (Mai):** Firmographics + JTBD + Filters/Signals finalisiert
  - **Cold Outbound (Jun):** HUNTER nutzt ICP v1.0 für systematische Prospektion
- **PostHog Warning:** "Don't jump to conclusions. 1-2 Kunden = Outliers möglich." → Florian MUSS 5-10 erreichen bevor ICP locked.
- **Kalungi Insight:** Pre-PMF (Florian = jetzt) → Psychographics (Bürgermeister Frustration: OZG-Druck, Andreas: Angebots-Bottleneck) wichtiger als Firmographics (Revenue, Mitarbeiter).
- **Confidence:** 85% — PostHog/Kalungi = Industry Standard, aber Florian's execution risk hoch (0 paying yet).
- **Next:** Nach Piloten: 6-Fragen Diver Survey auf Glashütte + Andreas → Pattern finden → ICP v1.0 draft.

## C-018: Primary Labs Incubation × AgentTrust × Stage 0→1 vs Stage 2→3
- **Fakten:** T-052 (Primary Labs = Incubation, Brian Schechter manages, Snowflake/Palo Alto successes), T-001 (95% AI pilots fail Stage 2→3), C-001 (AgentTrust = Stage 2→3 solution)
- **Insight:** Primary Labs baut Incubations (Stage 0→1: Ideation → First Product). AgentTrust löst Stage 2→3 (Pilot → Production). **KOMPLEMENTÄR, nicht identisch.** Florian's OIR Pitch könnte sein: "I built AgentTrust to solve Stage 2→3 for existing startups. Could we incubate the PLATFORM itself at Primary Labs — same framework, but for Stage 0→1?"
- **Differentiation:** Andere OIR Candidates = Operator Background. Florian = Operator Background + gebaut was Primary Labs Incubations NACH Launch brauchen werden (AgentTrust Calibration Framework). Meta-Fit: "I'm not just an operator, I'm an operator who builds tools for operators."
- **Angle:** "Primary Labs incubates companies. I build frameworks that help those companies SCALE post-incubation. Let's incubate the scaling framework itself."
- **Risk:** Zu meta. Brian könnte sagen "wir brauchen einen Operator, keinen Framework-Builder." Mitigation: AgentTrust zeigen als APPLIED tool (wir nutzen es selbst), nicht nur Theorie.
- **Connection zu C-001:** Glasswing = Portfolio-Problem (60 cos stuck Stage 2→3). Primary Labs = Pre-Portfolio-Problem (Incubations scheitern post-launch). Gleiche Lösung, unterschiedliche Stages. AgentTrust = Universal Calibration Layer für JEDE Stage.
- **Confidence:** 80% — Angle ist stark, aber Execution-Risiko (Brian's Priorities unknown).
- **Next:** Wenn Primary antwortet: AgentTrust als Incubation-Kandidat pitchen (nicht nur als Skill).

## C-019: Fitzpatrick 7-Questions × ICP Post-Pilot Validation × Glashütte/Andreas
- **Fakten:** T-054 (7-Power-Questions), C-017 (ICP needs 5-10 customers), T-048 (PostHog: 5 = good sign)
- **Insight:** C-017 referenzierte "6-Fragen Diver Survey" — FALSCH. Es ist **Fitzpatrick's 7-Power-Questions** aus "The Mom Test". GOLD STANDARD für Customer Discovery. NACH Glashütte + Andreas Piloten: Diese 7 Fragen an 10-15 ähnliche Prospects stellen → ICP v1.0.
- **Questions:**   1. "Erzählen Sie mir vom letzten Mal als das passiert ist" (Past behavior, not hypothetical)
  2. "Was passiert wenn Sie das Problem NICHT lösen?" (Pain size)
  3. "Was haben Sie schon versucht?" (Problem big enough to search for solutions?)
  4. "Was ist falsch an dem was Sie probiert haben?" (Competitor weaknesses)
  5. "Wie viel zahlen Sie aktuell dafür?" (Price anchor)
  6. "Was sollte ich noch gefragt haben?" (Unknown unknowns)
  7. "Mit wem sollte ich noch sprechen?" (Snowball effect)
- **Golden Rules:** (1) NIEMALS Produkt zeigen (vermeidet false positives), (2) IMMER 1 Frage die dein Business zerstören könnte (vermeidet false confidence)
- **Anwendung:** HUNTER Agent braucht diese 7 Fragen als Discovery-Script. Nicht "Wollen Sie unser Produkt kaufen?" sondern "Wie lösen Sie X heute?"
- **Confidence:** 98% — Fitzpatrick = Industry Standard (Mom Test Buch), Studio Zao implementiert es.
- **Next:** Nach beiden Piloten: 10 Discovery Calls mit 7-Questions Script → Patterns finden → ICP v1.0 finalisieren.

## C-020: AgentTrust × Galileo AI × Complementary Not Competitive
- **Fakten:** T-055 (5 Evaluation Platforms), T-056 (Galileo Details), C-008 (AgentTrust Differentiation)
- **Insight:** C-008 sagte "no competition in calibration" — KORREKT, ABER wir haben **Galileo AI** übersehen. Galileo macht "eval-to-guardrail lifecycle" + Luna-2 models (97% cost reduction) + hallucination detection. **AM NÄCHSTEN zu AgentTrust, ABER unterschiedliche Dimensionen:**
  - **Galileo:** Single-Dimension (Hallucinations), Guardrails (stop/allow), Production Monitoring
  - **AgentTrust:** Multi-Dimension (8-Dim Trust Score: Accuracy, Reliability, Safety, Transparency, Efficiency, Robustness, Alignment, Auditability), Calibration (how much to trust), Budget-CoCoA (cost-aware)
- **Overlap:** Beide machen "AI safety" + "production guardrails". ABER: Galileo = Binary (hallucination yes/no), AgentTrust = Continuous (trust 0-100%, confidence intervals).
- **Positioning:** AgentTrust = "Multi-Dimensional Trust Calibration Layer" ÜBER Observability (LangSmith, Arize) + Guardrails (Galileo). Integration: LangSmith traces → AgentTrust Trust Score → Galileo Guardrails. **Layer Cake, nicht Konkurrenz.**
- **Pricing Insight:** Galileo Luna-2 = 97% cost reduction vs GPT-4. AgentTrust Budget-CoCoA = similar angle (cheap Haiku for checks). Beide optimieren cost/quality trade-off.
- **Competitive Matrix Update:**   - **Observability:** LangSmith, Arize, Langfuse (what happened?)
  - **Evaluation:** Maxim AI, Braintrust (how good is it?)
  - **Guardrails:** Galileo (should I stop it?)
  - **Calibration:** AgentTrust (how much should I trust it?)
- **Confidence:** 92% — Galileo existiert, aber löst anderes Problem (hallucinations vs trust).
- **Next:** AgentTrust README muss Galileo als Complementary Tool positionieren: "Use Galileo for hallucination guardrails, AgentTrust for multi-dimensional trust scoring."

## C-021: Primary Labs × TBC × Tabs × Stage 0→1 + 2→3 Evidence
- **Fakten:** T-057 (TBC $25M Seed, Brian Schechter), T-058 (Tabs $55M Series B, incubated at Primary Labs), C-018 (Primary Labs = Stage 0→1)
- **Insight:** **C-018 war Hypothese, JETZT ist es BEWEIS.** Primary Labs baut aktiv Incubations (Tabs = Proof), Brian Schechter führt Deals (TBC = neueste Announcement Feb 2026). **Tabs war incubated, jetzt Series B** — perfektes Stage 0→1 → 2→3 Beispiel. TBC = früher Stage (Seed), Tabs = später Stage (Series B). Florian's AgentTrust Framework passt zu BEIDEN:
  - **TBC (Stage 0→1):** Living neural networks brauchen Calibration — "trust biological compute output"
  - **Tabs (Stage 2→3):** AR agents skalieren, brauchen Multi-Dimensional Trust für compliance (audit trail)
- **Primary Labs Activity:** Fund V = $625M (recent), PrimaryLabs "launched multiple companies in portfolio". NICHT nur historisch (Snowflake) — AKTIV jetzt (Tabs beweist es).
- **Follow-up Angle:** Florian's DM kann jetzt referenzieren: "I saw your TBC announcement — biological compute + AI agents is exactly the moonshot thinking Primary Labs excels at. AgentTrust's calibration framework could help companies like TBC and Tabs build trust boundaries as they scale."
- **Differentiation:** Florian = nicht nur Operator, sondern baut Frameworks die Primary Labs Portfolio/Incubations nach Launch brauchen. Meta-Fit: "I don't just operate, I build the infra operators use."
- **Timing:** TBC announced Feb 11 (Fortune), Feb 13 (Primary blog). Florian applied Feb 18. Follow-up DM JETZT (Feb 20) = 48h post-application, peak timing per T-047.
- **Confidence:** 98% — TBC + Tabs sind verifiziert, Brian Schechter Announcements sind real, Primary Labs Incubation Activity ist NICHT nur historisch.
- **Next:** Draft LinkedIn DM an Brian Schechter mit TBC/Tabs reference. Value-focused, nicht "checking in".
