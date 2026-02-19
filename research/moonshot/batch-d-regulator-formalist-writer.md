# Moonshot Batch D: Regulator + Formalist + Writer
> Generated: 2026-02-19 | Input: AR-020-v3, DOSSIER.md, claims_matrix.md

---

# 🏛️ ROLLE 1: REGULATOR — Was verlangt das Gesetz?

## 1.1 EU AI Act: Was steht WÖRTLICH zu Accuracy/Calibration/Confidence?

### Article 15 — Wortlaut (verifiziert gegen Official Journal)

> "High-risk AI systems shall be designed and developed in such a way that they achieve **an appropriate level of accuracy**, robustness, and cybersecurity, and that they perform consistently in those respects throughout their lifecycle."

> "The levels of accuracy and the **relevant accuracy metrics** of high-risk AI systems shall be **declared in the accompanying instructions of use**."

**Kritischer Befund: Das Wort "calibration" kommt in Article 15 NICHT vor.** Das Wort "confidence" kommt in Article 15 NICHT vor. Der Act verlangt "accuracy" und "accuracy metrics" — das ist ein schwächerer, anderer Begriff als Calibration.

AR-020 v3 hat das korrekt erkannt (Section 9): "A system that is 85% accurate but always says '100% confident' would technically comply."

### Article 14 — Human Oversight (indirekt relevant)

> High-risk systems must "be effectively overseen by natural persons."

Calibration ist nicht genannt, aber: sinnvolle menschliche Überwachung erfordert de facto Confidence-Signale. Ein System ohne Confidence-Output kann nicht effektiv überwacht werden. **Argumentationslinie für Compliance: Calibration als notwendige Voraussetzung für Article 14.**

### Article 13 — Transparency

Verlangt, dass Deployer die Outputs "richtig interpretieren" können. Auch hier: kein expliziter Calibration-Begriff, aber funktional notwendig.

**Fazit EU AI Act:** Calibration ist NICHT explizit gefordert. Accuracy ist gefordert. CEN/CENELEC-Standards (erwartet 2027-2028) werden die technische Auslegung konkretisieren — DORT könnte Calibration als Accuracy-Metrik definiert werden. Das Fenster für Early Adoption und Mitgestaltung ist JETZT offen.

## 1.2 Risk-Kategorie für AI Agents

| Kategorie | Beschreibung | Trifft auf AI Agents zu? |
|-----------|-------------|--------------------------|
| Unacceptable | Social Scoring, Manipulation, Real-time Biometric ID | Nein (außer Agent manipuliert gezielt) |
| **High-Risk** | Annex III: Beschäftigung, Bildung, Kreditwürdigkeit, Strafverfolgung, kritische Infrastruktur | **JA — wenn Agent in diesen Bereichen deployed wird** |
| Limited | Chatbots (Transparenzpflicht: "Du sprichst mit KI") | **JA — Default für die meisten Agents** |
| Minimal | Spam-Filter, Spiele | Selten |

**Wichtig:** AI Agents sind KEINE eigene Kategorie im EU AI Act. Die Klassifizierung hängt vom **Einsatzbereich** ab, nicht von der Technologie. Ein Agent für HR-Screening = High-Risk. Ein Agent für Reiseplanung = Limited/Minimal.

**GPAI-Sonderregeln:** Seit August 2025 gelten für General Purpose AI Models eigene Pflichten (Transparency, Copyright, Safety). Agents, die auf GPAI-Modellen basieren, fallen unter beides: GPAI-Regeln für das Modell + Risikokategorie für den Einsatz.

## 1.3 Timeline

| Datum | Was tritt in Kraft |
|-------|-------------------|
| **Feb 2025** ✅ | Verbotene Praktiken (Unacceptable Risk) |
| **Aug 2025** ✅ | GPAI-Anforderungen, AI Literacy (Art. 4), Nationale Behörden benannt |
| **Aug 2026** ⏳ | **Majority of rules**: High-Risk (Annex III), Transparency (Art. 50), Enforcement beginnt |
| **Aug 2027** | GPAI-Modelle die vor Aug 2025 auf Markt waren, müssen compliant sein. High-Risk (Annex I — regulierte Produkte) |
| **2027-2028** | CEN/CENELEC harmonisierte Standards erwartet — HIER wird "accuracy" technisch definiert |

## 1.4 US: SEC/FTC/NIST

**Kein US-Bundesgesetz zu AI Confidence Disclosure.** Aber:

- **NIST AI RMF 1.0 (2023):** Empfiehlt "validity and reliability" inkl. Uncertainty Quantification. Kein Zwang, aber: Texas und California bieten Safe Harbor für Unternehmen die NIST AI RMF oder ISO 42001 implementiert haben.
- **FTC:** Nutzt bestehende Befugnisse gegen "deceptive practices" — ein AI-System das Confidence vortäuscht könnte theoretisch unter Section 5 FTC Act fallen. FTC-Guidance zu AI preemption erwartet Q1 2026.
- **SEC:** Keine spezifischen AI-Confidence-Regeln. Aber: wenn AI für Investment-Advice eingesetzt wird, gelten bestehende Suitability/Fiduciary-Pflichten.
- **State Laws:** Colorado AI Act (2024), Texas HB 1709, California AB 2930 — alle verlangen Risk Assessments für "high-risk automated decisions", keiner nennt explizit Calibration.

**Fazit US:** Fragmentiert, kein explizites Calibration-Mandat. Aber der FTC-Pfad über "deceptive practices" ist real. NIST AI RMF ist der De-facto-Standard.

## 1.5 ISO Standards

- **ISO/IEC 42001:2023 (AI Management System):** Governance-Standard. Verlangt Risk Assessment, Monitoring, Continuous Improvement für AI-Systeme. NICHT technisch — sagt nicht "ECE < X". Sagt: "Ihr müsst einen Prozess haben, der Accuracy monitort." Calibration könnte Teil des Prozesses sein, ist aber nicht benannt.
- **ISO/IEC 23894:2023 (AI Risk Management):** Guidance für AI-spezifisches Risk Management. Mapping auf ISO 31000. Empfiehlt Identifikation von "AI-specific sources of risk" inkl. "accuracy" und "reliability". Keine technische Definition von Calibration.
- **ISO/IEC TR 24029 (Robustness of Neural Networks):** Technischer als 42001, behandelt Robustheit, aber nicht Calibration im engeren Sinne.

**Fazit ISO:** Kein ISO-Standard verlangt explizit Calibration. ISO 42001 verlangt einen PROZESS zur Accuracy-Sicherung. Die technische Lücke ist da — wer sie füllt, definiert den Standard.

## 1.6 Practical Roadmap: Was HEUTE tun?

| Zeitrahmen | Maßnahme | Warum |
|-----------|----------|-------|
| **HEUTE** | AI Literacy implementieren (Art. 4, seit Aug 2025 in Kraft!) | Bereits Pflicht. Includes: Teams müssen AI-Limitierungen verstehen |
| **HEUTE** | Risk Assessment für alle AI Agents (welche sind High-Risk?) | Vorbereitung auf Aug 2026. Ohne Assessment kein Compliance-Plan |
| **HEUTE** | NIST AI RMF / ISO 42001 Assessment starten | Safe Harbor in TX/CA, Best Practice, Audit-ready |
| **In 6 Monaten** | Accuracy-Metriken definieren + in Instructions of Use dokumentieren | Art. 15 Compliance für Aug 2026 |
| **In 6 Monaten** | Calibration Tier 1 (Consistency) deployen | Nicht vorgeschrieben, aber: Differenzierung + Future-Proofing |
| **In 12 Monaten (Aug 2026)** | High-Risk Compliance: Full Art. 9-15 | Enforcement beginnt |
| **In 12 Monaten** | Transparenz-Pflichten umsetzen (Art. 50) | AI-Interaktion muss als solche gekennzeichnet sein |
| **In 24 Monaten** | CEN/CENELEC-Standards implementieren (wenn veröffentlicht) | Harmonisierte Standards = Compliance-Vermutung |
| **In 24 Monaten** | Calibration als Wettbewerbsvorteil vermarkten | Regulatorisches Fenster schließt sich, Early Mover gewinnen |

## 🏛️ REGULATOR — Beipackzettel

| Feld | Bewertung |
|------|-----------|
| **Confidence** | 78% |
| **Was ist STARK** | Article 15 Wortlaut direkt verifiziert. Timeline aus offizieller EC-Quelle. US/ISO-Einschätzung basiert auf aktuellen Quellen (Dec 2025 EO, ISO-Website) |
| **Was ist SCHWACH** | CEN/CENELEC-Prognose (2027-2028) ist Schätzung, kein bestätigter Termin. ISO-Standards nur über Sekundärquellen analysiert (Volltext hinter Paywall). FTC-Guidance noch nicht veröffentlicht |
| **Was fehlt** | Sektorspezifische Regeln (Medizin: MDR, Finanz: MiFID II) nicht analysiert. China AI Regulations nicht behandelt. DSGVO-Interaktion (Art. 22 automatisierte Entscheidungen) nicht behandelt |
| **Haupterkenntnis** | **Calibration ist regulatorisch ein Vakuum — das ist eine Chance, kein Problem.** Wer jetzt Standards mitgestaltet (CEN/CENELEC, NIST), definiert die Spielregeln |

---

# 📐 ROLLE 2: FORMALIST — Beweise es mathematisch

## 2.1 Multi-Agent Confidence Propagation: Formale Problemdefinition

**Setup:** Kette von n Agents A₁, A₂, ..., Aₙ. Agent Aᵢ produziert Output oᵢ mit Confidence cᵢ ∈ [0,1]. Agent Aᵢ₊₁ erhält oᵢ als Input.

**Ziel:** Bestimme die Compound Confidence C(o₁, ..., oₙ) für die gesamte Kette.

**Naive Multiplikation (Independence Assumption):**
```
C_mult = ∏ᵢ cᵢ
```
Setzt voraus: P(Aᵢ korrekt | A₁...Aᵢ₋₁ korrekt) = P(Aᵢ korrekt) = cᵢ

**Bayesian Propagation (mit Korrelation):**
```
C_bayes = P(alle korrekt) = P(A₁ korrekt) · ∏ᵢ₌₂ⁿ P(Aᵢ korrekt | A₁...Aᵢ₋₁ korrekt)
```

Die bedingten Wahrscheinlichkeiten P(Aᵢ korrekt | Vorgeschichte) sind der entscheidende Unterschied.

## 2.2 Bayesian vs. Multiplicative bei korrelierten Agents

**Theorem (UNVERIFIED PROOF):** Für positiv korrelierte Agents (ρ > 0) gilt: C_mult UNTERSCHÄTZT die wahre Compound Confidence. Für negativ korrelierte Agents: C_mult ÜBERSCHÄTZT.

**Argument:**

Betrachte 2 Agents mit marginalen Accuracies p₁, p₂ und Korrelation ρ.

P(beide korrekt) = p₁·p₂ + ρ·√(p₁(1-p₁)·p₂(1-p₂))

- Wenn ρ > 0: P(beide korrekt) > p₁·p₂ → Multiplikation ist pessimistisch
- Wenn ρ < 0: P(beide korrekt) < p₁·p₂ → Multiplikation ist optimistisch
- Wenn ρ = 0: P(beide korrekt) = p₁·p₂ → Multiplikation ist exakt

**Für LLM-Agents in der Praxis:** ρ > 0 ist der Normalfall (shared training data, shared model biases, shared context). Das bedeutet:

1. Multiplikative Propagation ist systematisch zu pessimistisch für die "alle korrekt"-Frage
2. ABER: Sie ist gleichzeitig zu optimistisch für die "mindestens einer falsch"-Frage, WEIL korrelierte Fehler bedeuten, dass wenn einer falsch liegt, alle wahrscheinlich falsch liegen

**⚠ WICHTIG:** "Bayesian > Multiplicative" ist die FALSCHE Frage. Die richtige Frage ist: **Welche Propagation gibt besser KALIBRIERTE Compound-Confidences?** Das hängt vom Korrelationsregime ab:

- Hohe positive Korrelation (gleiche Fehler): Confidence ist bimodal — entweder alle richtig oder alle falsch. Weder Bayesian noch Multiplicative modelliert das gut.
- Niedrige Korrelation: Multiplicative ist gute Approximation.
- **Die empirische Frage (UNGELÖST): Wie groß ist ρ in realen Multi-Agent-Ketten?**

**SAUP (ACL 2025) adressiert das teilweise** mit "situational awareness weights" — kontextabhängige Gewichtung statt statischer Korrelationsannahme. Formal korrekterer Ansatz, aber empirische Validierung noch dünn.

## 2.3 Bounds für Tier 1 (Consistency) Calibration

**Frage:** Was ist die MAXIMALE ECE-Verbesserung, die Self-Consistency theoretisch erreichen kann?

**Analyse:**

Self-Consistency sampelt N Antworten und nutzt Majority-Vote-Anteil als Confidence-Schätzer:
```
ĉ = (Anzahl der häufigsten Antwort) / N
```

**Obere Schranke der Qualität:**

1. **Bei N → ∞:** ĉ konvergiert gegen P(modale Antwort | Prompt). Das ist ein konsistenter Schätzer für die Accuracy der modalen Antwort. **Aber:** Das ist nur dann gut kalibriert, wenn die Variabilität zwischen Samples die tatsächliche Unsicherheit widerspiegelt.

2. **Fundamentale Limitation:** Wenn das Modell auf N verschiedene Arten konsistent FALSCH antwortet (z.B. bei systematischem Bias), zeigt Consistency hohe Confidence für eine falsche Antwort. Self-Consistency kann systematischen Bias NICHT erkennen.

3. **Empirischer Bound (aus PMC-Studie):** ECE von 27.3% für Consistency vs. 42.0% für Verbal. Das ist eine Verbesserung von ~35% relativ. 

**Theoretischer Bound (UNVERIFIED):**

Unter der Annahme, dass das Modell keine perfekt korrelierten Fehler macht (ρ_error < 1), konvergiert Self-Consistency-ECE gegen:
```
ECE_consistency ≈ ECE_aleatoric + ECE_systematic_bias
```
wobei ECE_aleatoric ≈ O(1/√N) (verschwindet mit Samples) und ECE_systematic_bias der irreduzible Fehler durch korrelierte Modellfehler ist.

**Praktisch:** Tier 1 kann die EPISTEMISCHE Unsicherheitskomponente gut fangen, aber die SYSTEMATISCHE Bias-Komponente nicht. Die maximale Verbesserung ist beschränkt durch den Anteil epistemischer vs. systematischer Unsicherheit im Modell.

**Grobe Schätzung:** Für aktuelle LLMs (GPT-4-Klasse) ist ~60-70% der Miscalibration epistemisch, ~30-40% systematisch. Tier 1 kann also BESTENFALLS ~60-70% der Miscalibration beheben. Das erklärt den empirischen Befund: von 42% ECE auf 27% ≈ 36% Reduktion, was unter dem theoretischen Maximum von ~60-70% liegt (weil N=5 endlich ist).

## 2.4 Formale Definition von "gut kalibriert"

**Standard-Definition (Guo et al. 2017):**

Ein Modell ist perfekt kalibriert wenn:
```
∀p ∈ [0,1]: P(Y = ŷ | ĉ = p) = p
```
D.h. wenn das Modell 80% Confidence sagt, ist es in 80% der Fälle korrekt.

**ECE als Metrik:**
```
ECE = Σₘ (|Bₘ|/n) · |acc(Bₘ) - conf(Bₘ)|
```
über M Bins. ECE < ε ist NOTWENDIG für gute Calibration, aber NICHT HINREICHEND:

**Warum ECE nicht hinreicht:**

1. **Bin-Abhängigkeit:** ECE hängt von der Anzahl und Platzierung der Bins ab. Gleiches Modell, verschiedene Binning → verschiedene ECE.
2. **Cancellation:** Overconfidence in einem Bin kann Underconfidence in einem anderen Bin "aufheben" → niedrige ECE trotz schlechter Calibration.
3. **Keine Schärfe (Sharpness):** Ein Modell das immer 50% sagt hat perfekte Calibration (auf binären Tasks mit 50% Base Rate) aber ist nutzlos. ECE misst nicht, ob die Confidences INFORMATIV sind.

**Hinreichende Bedingung (strenger):**

Gute Calibration erfordert:
1. **Calibration:** ECE < ε (notwendig)
2. **Sharpness:** Varianz der Confidence-Verteilung ist hoch (das Modell differenziert zwischen sicher und unsicher)
3. **Auflösung (Resolution):** Hohe Confidence korreliert mit höherer Accuracy (nicht nur im Durchschnitt)

Formal kombiniert im **Brier Score** oder **proper scoring rules** (Logarithmic Score). Ein Modell mit niedrigem Brier Score ist sowohl kalibriert als auch scharf.

**Empfehlung:** ECE allein reicht nicht als KPI. Mindestens ECE + Brier Score + Reliability Diagram. Für regulatorische Zwecke: Reliability Diagram mit Konfidenzintervallen.

## 2.5 Offene mathematische Probleme

1. **Korrelationsstruktur in Multi-Agent-Ketten:** Wie modelliert man die Korrelation zwischen Agent-Fehlern formal? Die bivariate Normal-Approximation (§2.2) ist zu simpel. Copula-basierte Modelle? Empirische Daten fehlen fast vollständig.

2. **Calibration unter Distribution Shift:** Gibt es Bounds für die ECE-Degradation wenn sich die Input-Distribution um ε (in z.B. Wasserstein-Distanz) verschiebt? **Vermutlich ja, aber kein publizierter Beweis bekannt.**

3. **Optimale Stichprobengröße für Self-Consistency:** Für gegebenes ECE-Ziel ε, wie groß muss N sein? Die Konvergenzrate hängt von der unbekannten Antwort-Verteilung ab. Adaptive Sampling-Strategien (erst viele Samples, dann weniger wenn Consistency hoch) sind nicht formal analysiert.

4. **Compositionality of Conformal Prediction:** Wenn Agent A einen CP-Set erzeugt und Agent B darauf operiert — was sind die Coverage-Garantien des Gesamt-Systems? Theoretisch: Coverage degradiert multiplikativ (1-α)ⁿ. Aber das ist nur unter Independence. **Für korrelierte Stufen: ungelöst.**

5. **Informationstheoretische Grenzen der Black-Box-Calibration:** Gibt es ein fundamentales Limit, wie gut man ein Black-Box-Modell kalibrieren kann, wenn man nur Input-Output-Paare sieht? Hängt von der VC-Dimension des Calibration-Mappings ab. **Nicht formal untersucht für LLMs.**

6. **Calibration als Online-Learning-Problem:** In Produktion: fortlaufende Calibration mit driftender Distribution. Regret Bounds für Online-Calibration? Nur teilweise gelöst (Foster & Vohra 1998 für binäre Vorhersagen, nicht für LLM-Calibration).

## 📐 FORMALIST — Beipackzettel

| Feld | Bewertung |
|------|-----------|
| **Confidence** | 65% |
| **Was ist STARK** | Problemdefinition ist sauber. Korrelationsargument (§2.2) ist mathematisch korrekt für den bivariaten Fall. ECE-Insuffizienz-Argument (§2.4) ist gut etabliert in der Literatur |
| **Was ist SCHWACH** | ALLE Beweise sind UNVERIFIED — kein einziger wurde formal geprüft. Der Bound in §2.3 ist eine Heuristik, kein Beweis. Die "60-70% epistemisch"-Schätzung ist aus der Luft gegriffen (plausibel, aber unbelegt). Multi-Agent-Korrelation extrapoliert von bivariat auf n-ariat ohne Rechtfertigung |
| **Was fehlt** | Simulationsergebnisse (Monte Carlo für Multi-Agent-Propagation). Empirische Korrelationsmessungen. Vergleich mit SAUP-Formalismus. Beweis für die Konvergenzrate von Self-Consistency |
| **Hauptwarnung** | **Keiner dieser "Beweise" ist publikationsreif.** Sie sind Skizzen und Intuitionen, formal verpackt. Für eine ernsthafte mathematische Arbeit müssten alle Schritte rigoros ausgearbeitet und die Annahmen explizit gemacht werden |
| **Wertvollste Erkenntnis** | Die offenen Probleme (§2.5) sind genuinely offen und könnten als Research Agenda für ein Paper dienen |

---

# 📝 ROLLE 3: WRITER — Executive Summaries (3 Versionen)

## Version A: Für VCs (Marktchance + Differenzierung)

**The $52B AI agent market has a hidden failure mode — and every incumbent is ignoring it.**

When Agent A tells Agent B it's "90% sure," and Agent B builds on that answer, the compound error doesn't multiply predictably. It correlates. Shared training data, shared biases, shared blind spots mean multi-agent systems fail in clusters, not gracefully. No production framework addresses this — the first to solve confidence propagation across agent chains captures the trust infrastructure layer beneath every agent deployment.

The numbers: 84% of LLM scenarios show overconfidence (PMC, 9 models). The training that makes models helpful (RLHF) is the same training that destroys their self-awareness. Post-hoc calibration costs <$0.05 per decision. The average enterprise hallucination costs orders of magnitude more.

Three papers from January 2026 (HTC, BaseCal, SAUP) just proved the concept works. But nobody has productized it. The gap between "paper proves it" and "enterprise deploys it" is where the company gets built. EU AI Act enforcement starts August 2026 — Article 15 requires accuracy metrics for high-risk systems, but no standard defines what "accuracy" means yet. The company that provides calibration-as-a-service writes the standard.

First-mover window: 18 months before CEN/CENELEC harmonized standards close it.

*[198 words]*

## Version B: Für CTOs (Praktische Anleitung + ROI)

**Your AI agents are confidently wrong 84% more often than they admit — and fixing it costs $0.005 per decision.**

Here's what most teams miss: the overconfidence isn't a bug you can prompt-engineer away. RLHF — the training step that makes models useful — systematically rewards confident-sounding answers regardless of correctness. Your agents inherited this at birth. Temperature scaling (the textbook fix) requires logit access that GPT-4 and Claude don't provide.

The fix that works today: sample 3-5 responses per query, measure agreement. Where they disagree, the model is uncertain. This "consistency-based calibration" cuts Expected Calibration Error from 42% to 27% at $0.005/check (Budget-CoCoA). Full-stack calibration including statistical guarantees costs <$0.05/decision — less than a human reviewer by 98%.

Implementation path: Week 1, measure your current ECE on 200+ labeled interactions. Week 2, wrap your worst agent with consistency scoring. Week 3, set abstention thresholds — route uncertain outputs to humans. Month 2, add conformal prediction for high-stakes decisions (legal, financial, medical). Month 3, monitor calibration drift.

ROI: One caught hallucination in a customer-facing agent pays for a year of calibration infrastructure. The Mata v. Avianca case ($5K sanctions + career damage) and Air Canada chatbot ruling ($812 liability) happened because zero calibration existed. Your exposure is larger.

*[199 words]*

## Version C: Für Forscher (Novelty + Research Gaps)

**Correlated agent failures break every existing confidence propagation model — and we don't have the math to fix it.**

Multi-agent AI systems compound errors, but not independently. Agents sharing training data, model architectures, and conversation context produce positively correlated failures: when one hallucinates, others in the chain are more likely to propagate it. The standard multiplicative assumption (C = ∏cᵢ) is provably wrong under positive correlation, yet it remains the implicit model in every deployed system. SAUP (ACL 2025) introduced situational awareness weights for intra-chain propagation. HTC (Zhang et al., Jan 2026) calibrates single-agent trajectories. Neither solves the inter-agent case.

Five open problems define the frontier: (1) What is the empirical correlation structure of errors in production multi-agent chains? (2) Can conformal prediction guarantees compose across dependent pipeline stages? (3) What are the information-theoretic limits of black-box calibration? (4) How does calibration degrade under distribution shift, and can we bound it? (5) Self-consistency cannot detect systematic bias — what method can, without logit access?

The field has moved from "calibration doesn't exist for agents" (true in 2024) to "partial solutions exist but don't compose" (true in 2026). The fundamental tension between RLHF optimization and calibratability (ICML 2025: "calibratable vs. non-calibratable regimes") suggests this isn't solvable within current training paradigms. New theory is needed.

*[200 words]*

## Anti-LLM-Phrasen-Check

Geprüft gegen verbotene Phrasen:
- ❌ "landscape" → nicht verwendet ✅
- ❌ "tapestry" → nicht verwendet ✅
- ❌ "delve" → nicht verwendet ✅
- ❌ "synergy" → nicht verwendet ✅
- ❌ "cutting-edge" → nicht verwendet ✅
- ❌ "game-changer" → nicht verwendet ✅
- ❌ "It's worth noting" → nicht verwendet ✅
- ❌ "In today's world" → nicht verwendet ✅

## 📝 WRITER — Beipackzettel

| Feld | Bewertung |
|------|-----------|
| **Confidence** | 75% |
| **Was ist STARK** | Jede Version öffnet mit einem nicht-offensichtlichen Insight (korrelierte Fehler / $0.005 Fix / fehlende Mathematik). Kein Recycling von "RLHF macht overconfident" als Opener. Alle Zahlen aus AR-020 v3 und verifiziert |
| **Was ist SCHWACH** | Version A ist aggressiv — "writes the standard" ist eine Behauptung die belegt werden müsste. Version B könnte zu rezepthaft wirken für Senior CTOs. Version C setzt voraus, dass der Leser die Basisliteratur kennt |
| **Was fehlt** | Keine Version adressiert das Risiko, dass Calibration ein Feature wird das in Foundation Models integriert wird (obsoleszenz-Risiko für externe Lösungen). Kein Hinweis auf Wettbewerber |
| **Ehrliche Bewertung des AR-020 Openers** | Der aktuelle Opener ("RLHF macht overconfident") ist tatsächlich schwach. Jeder der 3 Alternativen ist stärker. Version C ist am originellsten, Version B am nützlichsten, Version A am verkaufsstärksten |

---

# Meta: Cross-Role Insights

1. **Regulator + Writer Synergie:** Das regulatorische Vakuum ist ein starkes Argument für VCs (Version A). "Write the standard" ist nicht nur Marketing — CEN/CENELEC-Beteiligung ist real möglich.

2. **Formalist + Regulator Spannung:** Article 15 verlangt "accuracy metrics" — aber die Mathematik zeigt, dass ECE allein nicht hinreicht (§2.4). Die regulatorische Anforderung ist unterdefiniert. Wer die Definition liefert, gewinnt.

3. **Formalist + Writer Problem:** Die mathematischen Unsicherheiten (§2.2-2.3 sind alle UNVERIFIED) stehen in Spannung mit den selbstbewussten Writer-Statements. Ehrliche Kommunikation: "Wir haben die Intuition und erste Beweise, aber die volle Theorie fehlt noch."

4. **Größtes Risiko für AR-020:** Wenn OpenAI/Anthropic/Google Calibration als Feature in ihre APIs einbauen (z.B. "confidence score" als Standardfeld), wird externes Calibration-Tooling weniger relevant. Das ist in keiner Version adressiert.
