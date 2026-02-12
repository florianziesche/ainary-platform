# 🔬 RESEARCH SYNTHESIS — 3 Hypothesen × 5 Linsen
*2026-02-10 | 6 Agents (Academic, Cognitive, Practitioner, Contrarian, Experimenter, + Behavioral pending)*

---

## HYPOTHESE 1: "Curated Memory > Raw Logs (10x)"

### VERDICT: ✅ BESTÄTIGT — aber mit Nuance

| Linse | Sagt | Stärke |
|-------|------|--------|
| Academic | Mem0: 26% besser, 91% weniger Latenz, >90% Token-Ersparnis | Stark |
| Cognitive | Menschliches Gehirn vergisst 70% in 24h — Vergessen ist FEATURE | Stark |
| Practitioner | MemGPT: 92% vs 32% Accuracy in langen Gesprächen | Stark |
| Contrarian | Long-Context (2M tokens) macht Curation evtl. obsolet | Mittel |
| Experimenter | Konkreter Test: 20 Tasks × 3 Bedingungen, $6 | Ready |

**Convergence:** 4/5 bestätigen. Curated Memory ist besser UND billiger.

**Die Contrarian-Nuance die alles verändert:**
> "Die 10x reflektiert wahrscheinlich Cost Optimization, nicht Quality Optimization. Raw Logs sind vielleicht BESSER — wir können sie uns nur nicht leisten."

**Revised Hypothesis:**
> "Curated memory outperforms raw logs in cost-constrained production (10x access, 90% cost reduction). But as context windows grow to 2M+ tokens, the quality gap may close — leaving curation as an economic, not epistemological, advantage."

**Open Question (kein Paper beantwortet das):**
> Wie bestimmt man automatisch die optimale Curation-Frequenz und -Granularität für verschiedene Task-Typen?

**Cognitive Gold:** Das menschliche Gehirn konsolidiert Memory im Schlaf (episodisch → semantisch). AI Agents haben keinen "Schlaf" — aber HEARTBEAT.md könnte genau diese Rolle spielen. Periodische Konsolidierung = künstlicher Schlaf.

---

## HYPOTHESE 2: "Definition of Done Gap" (Agent sagt 100%, ist 30%)

### VERDICT: ✅ STARK BESTÄTIGT — und quantifiziert

| Linse | Sagt | Stärke |
|-------|------|--------|
| Academic | 🔥 Paper von Feb 6, 2026: Gemini 77% predicted → 22% actual (55pp Gap!) | Sehr stark |
| Cognitive | Dunning-Kruger + Planning Fallacy — identisches menschliches Muster | Stark |
| Practitioner | SWE-bench: 13.86% (2024) → 50%+ (2025), aber "Done" ≠ Production-Ready | Stark |
| Contrarian | Es ist ein Calibration-Problem, kein Capability-Problem — fixbar | Mittel |
| Experimenter | 15 Tasks × 10-Punkte-Rubrik × Self-Assessment, $10 | Ready |

**Convergence: 5/5 bestätigen den Gap. Stärkstes Signal aller 3 Hypothesen.**

**Key Numbers:**
- GPT-5.2-Codex: 73% predicted → 35% actual (38pp Gap)
- Gemini-3-Pro: 77% predicted → 22% actual (55pp Gap)
- Claude Opus 4.5: 61% predicted → 27% actual (34pp Gap)
- **Pre-execution Schätzungen sind BESSER als post-execution Reviews** (counterintuitive!)

**Contrarian-Insight:**
> "Adversarial Prompting ('find bugs' statt 'verify correctness') reduziert Overconfidence um 15pp."
→ Das erklärt warum unser Agent H (Adversarial) im CNC-Experiment der zweitbeste war!

**Cognitive Parallel:**
- Dunning-Kruger: Unteres Quartil schätzt sich auf 60. Perzentile
- Planning Fallacy: 64% Zeitüberschreitung bei Projekten
- **Expertise-Calibration braucht 1000+ Feedback-Loops** — Agents bekommen fast nie Feedback

**OPEN QUESTION (Publishable!):**
> Kann man Agents beibringen, "Grad der Fertigstellung" (10%-30%-70%-100%) statt binär (done/not done) einzuschätzen?
> **Niemand forscht daran.** Alle Papers sind binär (succeed/fail). Das Kontinuum ist unerforscht.

**🏆 DIES IST DAS STÄRKSTE PAPER-THEMA.** Wir haben:
1. Frisches SOTA-Paper das den Gap quantifiziert (4 Tage alt)
2. Eigene Production-Daten die es bestätigen
3. Eine offene Forschungsfrage die niemand beantwortet hat
4. Concrete Experiment-Design um es zu testen ($10)

---

## HYPOTHESE 3: "Meta-Skills Transfer > Domain Knowledge"

### VERDICT: ⚠️ MIXED — kontextabhängig

| Linse | Sagt | Stärke |
|-------|------|--------|
| Academic | Skill-Based Single Agent = Multi-Agent mit 54% weniger Tokens | Stark |
| Cognitive | Polymaths 2-3x wahrscheinlicher Nobelpreis, Analogical Reasoning | Mittel |
| Practitioner | r > 0.92 Korrelation Input/Output Education Levels cross-domain (Anthropic) | Stark |
| Contrarian | Fine-Tuning schlägt Zero-Shot; GPT-4+MedPrompt schlägt aber Specialist | Gemischt |
| Experimenter | Meta-Skill (Debugging) trainieren → auf Kochen + Legal transferieren, $7 | Ready |

**Keine Convergence — das ist die interessanteste Hypothese weil sie CONTESTED ist.**

**Die Wahrheit ist differenzierter:**
> - **Generalist + Advanced Prompting > Specialist** (GPT-4 + MedPrompt > Med-PaLM 2)
> - **ABER: Fine-Tuned Specialist > Generalist + Simple Prompting**
> - **Der Trick ist nicht das Modell, sondern die METHODE** (Prompting-Strategie = Meta-Skill)

**Academic Gold:**
- Phase Transition bei ~80-90 Skills: Skill-Selection bricht zusammen
- Hierarchische Organisation stellt Performance wieder her
- **Mirrors menschliches Chunking** (Miller's 7±2)

**Contrarian's stärkstes Argument:**
> "Negative Transfer ist real — wenn Domains zu weit divergieren, SCHADET Cross-Training."
> Beispiel: Manufacturing-Wissen hilft bei VC-Thesis, aber SCHADET bei Lyrik-Schreiben.

**Revised Hypothesis:**
> "Meta-skills (reasoning, decomposition, structured analysis) transfer better than domain facts — BUT only when domains share structural similarity. Negative transfer occurs when domain distance exceeds a threshold."

---

## 🔥 CROSS-CUTTING FINDINGS (Was nur durch 5 Linsen sichtbar wird)

### 1. Adversarial = Calibration Tool
- Academic: Adversarial Prompting reduziert Overconfidence um 15pp
- CNC-Experiment: Agent H (Adversarial) war zweitbester Schätzer
- Cognitive: "Consider the opposite" verbessert menschliche Calibration
- **→ Adversarial Review sollte STANDARD sein für jeden Agent-Output**

### 2. Schlaf = Konsolidierung
- Cognitive: Menschliches Gehirn konsolidiert im Schlaf
- Academic: Mem0 "consolidation pipelines"
- OpenClaw: HEARTBEAT.md = künstlicher Schlaf?
- **→ Periodische Memory-Konsolidierung ist biologisch validiert**

### 3. Vergessen ist ein Feature
- Cognitive: 70% in 24h vergessen = Feature, nicht Bug
- Academic: >90% Token-Ersparnis durch selektives Vergessen
- Contrarian: Aber was wenn du das Falsche vergisst?
- **→ "Intelligent Forgetting" als eigenes Forschungsfeld**

### 4. Pre-Execution > Post-Execution Assessment
- Academic: Agents schätzen VOR der Aufgabe besser als DANACH
- Cognitive: Planning Fallacy = je mehr du weißt, desto overconfidenter
- **→ "Schätze erst, dann arbeite" als Agent-Design-Prinzip**

---

## 📊 EXPERIMENT-READINESS

| Experiment | Kosten | Dauer | Hypothesis | Bereit? |
|-----------|--------|-------|------------|---------|
| Memory Access Patterns | $6 | 60 min | H1: Curated 10x | ✅ Scripts ready |
| Task Completion Calibration | $10 | 75 min | H2: Done Gap | ✅ Scripts ready |
| Meta-Skills Transfer | $7 | 60 min | H3: Transfer > Domain | ✅ Scripts ready |
| **TOTAL** | **$23** | **~2h** | | **Heute Abend?** |

---

## 🎯 PUBLICATION STRATEGY

**Stärkstes Paper-Thema: "The Definition of Done Gap"**

Warum:
1. Frischestes SOTA-Paper (4 Tage alt) — Timing perfekt
2. Unsere eigenen Production-Daten validieren es
3. Offene Forschungsfrage (Kontinuum statt binär) — niemand arbeitet daran
4. Experiment kostet $10 und läuft in 75 Minuten
5. Relevant für JEDEN der AI Agents baut (große Audience)

**Format-Empfehlung:**
1. Blog Post (diese Woche) — "Your AI Agent Lies About Being Done. Here's Proof."
2. arXiv Preprint (2 Wochen) — With experiment data
3. Workshop Paper (ICLR MemAgents oder NeurIPS Agent Workshop)

---

*6 Agents × 3 Topics × 5 Linsen = 90 Research-Perspektiven*
*Kosten: ~$12 | Dauer: ~20 min | Output: 130KB Research + Synthesis*
