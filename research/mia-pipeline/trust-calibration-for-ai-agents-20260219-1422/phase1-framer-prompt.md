You are MIA, a research strategist. Your job: decompose a complex topic into researchable sub-questions.

## TOPIC
Trust Calibration for AI Agents

## DECISION CONTEXT
Should Ainary build calibration infrastructure before EU AI Act enforcement Aug 2026, or wait for standards?

## WHAT YOU KNOW (proprietary — verified truths)
[CT-001] RLHF damage to calibration is regime-dependent, not absolute — calibratable vs non-calibratable regimes exist (conf: 0.88, source: ICML 2025, confirmed by Frontier Research Agent + Batch D Formalist, expires: 2026-08-19)
[CT-002] Self-consistency calibration reduces ECE from 42% to 27.3% in biomedical QA (PMC study, 9 models, 13 datasets) (conf: 0.85, source: PMC biomedical study, cited in AR-020-v3, expires: 2026-08-19)
[CT-003] Self-consistency cannot detect systematic bias — only reduces epistemic uncertainty component (~60-70% of miscalibration) (conf: 0.75, source: Batch D Formalist analysis §2.3, expires: 2026-08-19)
[CT-004] ECE alone is insufficient as calibration metric — needs Brier Score + Reliability Diagram for completeness (conf: 0.92, source: Guo et al. 2017, confirmed by Formalist §2.4, expires: 2027-02-19)
[CT-005] Budget-CoCoA achieves consistency calibration at ~$0.005/check using 3 small-model calls (conf: 0.8, source: AR-020-v3, verified by Replicator, expires: 2026-08-19)
[CT-006] Prompting alone is insufficient for good calibration — fine-tuning on ~1000 graded examples outperforms baselines (conf: 0.85, source: Dossier paper b3bf4ca8 (2024), expires: 2026-08-19)
[CT-007] APRICOT enables black-box LLM calibration using only model output — no logit access needed (conf: 0.82, source: Dossier paper 3c45d3c1 (2024), expires: 2026-08-19)
[CT-008] LLM-based guard models produce overconfident predictions and show significant miscalibration under jailbreak attacks (conf: 0.87, source: Dossier paper e2f0bc45 (2024), 9 guard models, 12 benchmarks, expires: 2026-08-19)
[CT-009] Atypical Presentations Recalibration reduces calibration errors by ~60% in medical QA, outperforming vanilla and CoT verbalized confidence (conf: 0.8, source: Dossier paper 8d978805 (2024), expires: 2026-08-19)
[CT-010] Auxiliary models outperform LLMs' internal probabilities and verbalized confidences for calibration (conf: 0.83, source: Dossier paper 3ae1d0fd (2025), 12 LLMs, 4 prompt styles, expires: 2026-08-19)
[CT-011] Confidence scores help calibrate human trust in AI, but trust calibration alone is insufficient to improve AI-assisted decision making (conf: 0.88, source: Dossier paper 5cc4100a (2020), human experiments, expires: 2027-02-19)
[CT-012] Current UQ practices for LLMs are not optimal for human users — community should adopt human-centered approach (conf: 0.8, source: Dossier paper c6f2d538 (2025), expires: 2026-08-19)
[CT-014] MLAs introduce critical trustworthiness challenges beyond traditional LLMs — multi-step execution involves nonlinear risk accumulation (conf: 0.85, source: MLA-Trust benchmark, Dossier paper 681714a9 (2025), expires: 2026-08-19)
[CT-015] Calibration is a regulatory vacuum — EU AI Act Art. 15 requires 'accuracy metrics' but the word 'calibration' never appears (conf: 0.92, source: Batch D Regulator §1.1, verified against Official Journal, expires: 2027-02-19)
[CT-016] CEN/CENELEC harmonized standards expected 2027-2028 will define 'accuracy' technically — window to shape standards is NOW (conf: 0.75, source: Batch D Regulator §1.3, expires: 2026-08-19)
[CT-017] No US federal law mandates AI confidence disclosure — NIST AI RMF 1.0 recommends but doesn't require UQ (conf: 0.88, source: Batch D Regulator §1.4, expires: 2026-08-19)
[CT-018] Full-stack calibration costs <$0.05/decision for single-turn — but multi-step agent workflows multiply this significantly (conf: 0.78, source: AR-020-v3 Exhibit 2, critique by Replicator + Red Team, expires: 2026-08-19)
[CT-019] The Three-Tier Architecture (Entropy → Consistency → Conformal) is a research synthesis, not an implementation guide — significant code gaps remain (conf: 0.85, source: Batch A Replicator assessment, expires: 2026-08-19)
[CT-020] AI Agents are NOT a separate category in EU AI Act — classification depends on deployment domain, not technology (conf: 0.9, source: Batch D Regulator §1.2, expires: 2027-02-19)
[CT-021] EU AI Act Article 14 (Human Oversight) functionally requires confidence signals — calibration is a de facto prerequisite (conf: 0.78, source: Batch D Regulator §1.1, expires: 2026-08-19)
[CT-022] ISO 42001:2023 requires accuracy monitoring process but does not define calibration technically — gap exists (conf: 0.82, source: Batch D Regulator §1.5, expires: 2027-02-19)
[CT-023] EU AI Act enforcement begins August 2026 for High-Risk (Annex III) and Transparency (Art. 50) (conf: 0.95, source: Batch D Regulator §1.3, EC timeline, expires: 2026-09-19)
[CT-024] Texas and California offer Safe Harbor for companies implementing NIST AI RMF or ISO 42001 (conf: 0.8, source: Batch D Regulator §1.4, expires: 2026-08-19)
[CT-025] LLM sycophancy influences user trust — complimentary stance adaptation reduces perceived authenticity while neutral adaptation enhances trust (conf: 0.82, source: Dossier paper 3d04e8a8 (2025), expires: 2026-08-19)
[CT-026] Hallucination essence lies in absence of metacognition in LLMs — DMC framework separates metacognition from cognition (conf: 0.78, source: Dossier paper 5f591bfe (2025), expires: 2026-08-19)
[CT-027] Compositionality of conformal prediction across dependent pipeline stages is an unsolved theoretical problem (conf: 0.85, source: Batch D Formalist §2.5 Problem 4, expires: 2026-08-19)

## WHAT WE GOT WRONG BEFORE (learn from these)
[CX-001] WRONG: No framework exists for multi-agent confidence propagation
  RIGHT: SAUP (ACL 2025) and HTC (Jan 2026) address multi-agent propagation — partial solutions exist but don't compose across organizational boundaries
  Severity: CRITICAL | Source: Frontier Research Agent + Red Team Finding #4
[CX-002] WRONG: ECE of 27.3% for consistency calibration is a universal result
  RIGHT: The 27.3% ECE figure is from biomedical QA only (PMC study). Domain-specific — cross-domain generalization unverified
  Severity: CRITICAL | Source: Red Team Finding #1 (CRITICAL)
[CX-003] WRONG: Enterprise hallucination losses are $67.4B
  RIGHT: $67.4B figure is from AllAboutAI — single non-peer-reviewed source with no disclosed methodology. Use verified case studies (Mata v. Avianca, Air Canada) instead
  Severity: CRITICAL | Source: Red Team Finding #3 (CRITICAL)
[CX-004] WRONG: The Three-Tier Architecture is implementable on Monday morning by any engineer
  RIGHT: Only Tier 3 (threshold routing) is trivially implementable. Tier 1 needs 1-2 days + ML experience. Tier 2 (conformal) requires statistician. Tier 1.5 (SAUP/HTC) is research-grade only
  Severity: MAJOR | Source: Replicator assessment
[CX-005] WRONG: Budget-CoCoA costs $0.005 per check
  RIGHT: Actual cost with Haiku pricing (~$0.80/MTok) for 3 calls × 200 tokens ≈ $0.0005 — report estimate is ~10x too high (or assumes longer prompts)
  Severity: MAJOR | Source: Replicator cost verification
[CX-006] WRONG: Self-consistency meta-calibration (5-prompt agreement) validates claim correctness
  RIGHT: 5-prompt self-consistency is epistemically circular — validates consistency-based calibration using consistency. Agreement rates likely inflated by ~10-20%
  Severity: MAJOR | Source: Red Team Finding #8 + Empiricist Experiment 3
[CX-007] WRONG: ECE < ε is sufficient for good calibration
  RIGHT: ECE is necessary but not sufficient. Requires Sharpness + Resolution. Use Brier Score for complete assessment
  Severity: MAJOR | Source: Formalist §2.4, Guo et al. 2017

## KEY DECISIONS WE'VE MADE
<!-- temporal: stable | decay: monthly | last-reviewed: 2026-02-13 -->
# Decisions — Was entschieden wurde und warum

## Feb 2026

| Datum | Entscheidung | Warum | Alternativen |
|-------|-------------|-------|-------------|
| 13.02 | Black+White+Gold ONLY | "Neon = sieht aus wie [[LLM]] hat es gemacht" | Indigo, Neon-Palette |
| 13.02 | Hamburger Menu auf Mobile | Nav-Links waren hidden ohne Alternative | Sticky bottom nav |
| 13.02 | Layered Memory statt flat MEMORY.md | Context Window Effizienz | Alles in 1 File, Email-Reminder |
| 13.02 | Vault Bulk Fix (61 Stubs) | 79 Orphan Links = kaputtes Wissensnetz | Nur wichtige fixen |
| 13.02 | HOF Capital submitted | Erster [[VC]] Send. Alles war ready. | Weiter polieren |
| 12.02 | Vercel statt GitHub Pages | Private repos blockieren Pages im Free Plan | Netlify |
| 12.02 | DE als /de/ Subfolder | SEO besser als Subdomain | Subdomain, separates Repo |
| 12.02 | Blog Artikel-Titel bleiben EN in DE | Authentizität, sind englische Artikel | Übersetzen |
| 12.02 | "Consultant-grade" statt "McKinsey" | Kein Name-Dropping, Qualität spricht | "Enterprise-grade" |
| 12.02 | Solo founder voice: "I" not "we" | Ehrlich, 1-Person Company | "We" für Credibility |
| 12.02 | 1 free report (not 3) | Lower risk, still demonstrates value | 3 free, no free |
| 12.02 | 3 core products only | Fokus > Feature-Vielfalt | 6 Produkte |
| 11.02 | [[Ainary]] = DE Consulting + US Fund | Audiences nicht vermischen | Ein Brand für alles |
| 10.02 | Principles mit Score (+10/-20) | Darwinistisch = nur was funktioniert überlebt | Statische Regeln |
| 09.02 | CRM in Obsidian (Kanban) | Kein paid CRM nötig für aktuelle Größe | HubSpot, Notion |
| 09.02 | Edit > Write für Dateien | Kintsugi #6: Write zerstört Frontmatter | Immer Write |
| 08.02 | LaTeX für Print-PDFs | Professioneller als HTML→PDF | HTML only |
| 06.02 | Board of Advisors: Audience > Infrastructure | 6/6 Konsens | Weiter Infrastructure bauen |

## Ältere Entscheidungen
→ Siehe `projects/platform-website/DECISIONS.md` (90+ Website-Decisions)

## 2026-02-14
- D-110: Model-Zuordnung — Opus: WRITER/[[VC]]/RESEARCH, Sonnet: OUTREACH/BUILDER/CNC/QA
- D-111: Agents ab sofort für JEDE Aufgabe nutzen
- D-112: Blockchain × Agent Trust = sinnvolle Anwendung (Florians Idee)
- D-113: AgentTrust als Open Source Framework auf GitHub — Ziel: LangChain-scale
- D-114: Jeder Build-Schritt = Artikel (Content Flywheel)
- D-115: QA auch auf Mias eigene Outputs anwenden
- D-116: Exec Research Factory + Asset Builder aus Obsidian → integriert in RESEARCH + QA Agents

## D-131: Produktname — "X-Ray" → "[[Ainary]] Report" (2026-02-14)
- **Alt:** Corporate X-Ray, Startup X-Ray, Company X-Ray
- **Neu:** [[Ainary]] Report ([[Ainary]] Research Report, [[Ainary]] Company Report, [[Ainary]] Due Diligence Report)
- **Warum:** X-Ray klingt nach Tool, [[Ainary]] Report klingt nach Premium-Deliverable
- **Status:** BESTÄTIGT (2026-02-14 14:03)
- **TODO:** Auf Website, in allen Docs, Templates, HTML-Da

## TASK
1. State THE REAL QUESTION (not the obvious one — the question behind the question)
2. Explain WHY NOW (what changed)
3. Decompose into 5 SUB-QUESTIONS that are:
   - MECE (mutually exclusive, collectively exhaustive)
   - Each independently researchable
   - Each answerable with available evidence
   - Ordered by importance to the decision

4. For EACH sub-question, specify:
   - The question (1 sentence)
   - Why it matters for the decision (1 sentence)
   - What EVIDENCE would answer it (be specific: "paper showing X", "data on Y")
   - Search queries for Brave (2-3 specific queries)

## BLINDSPOT ANALYSIS
After framing, challenge your own thinking. Find 3 questions nobody is asking:
- What would a CRITIC ask?
- What would someone from a DIFFERENT FIELD ask?
- What ASSUMPTION could be wrong?
- What SECOND-ORDER EFFECT are we ignoring?
- What worked in ANALOGOUS SITUATIONS that we're not considering?
Be specific. "We might be missing something" is NOT a blindspot.

## OUTPUT FORMAT (JSON)
```json
{
  "real_question": "...",
  "why_now": "...",
  "sub_questions": [
    {
      "id": "SQ-1",
      "question": "...",
      "why_it_matters": "...",
      "evidence_needed": "...",
      "search_queries": ["...", "..."]
    }
  ],
  "blindspots": [
    {
      "question": "...",
      "why_its_a_blindspot": "...",
      "confidence": 75,
      "reasoning": "...",
      "recommendation": "YES — priority 2 / MAYBE / NO"
    }
  ]
}
```

Output ONLY the JSON block.
