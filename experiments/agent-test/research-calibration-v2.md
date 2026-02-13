# Executive Brief: Calibration Methods for LLM Confidence — What Works in Production?

**Tag:** [INTERN]  
**Tier:** 2 (Decision Support)  
**Decision:** Sollen wir unser Honesty-as-Currency System um spezifische Calibration-Methoden erweitern?  
**Date:** 2026-02-14

---

## Key Findings (max 5)

1. **Verbalized Confidence (einfach "frag das Modell") ist systematisch schlecht kalibriert** — LLMs sind overconfident wenn sie sich selbst bewerten. Neueste Studie (Jan 2026) zeigt: Verbalized approaches sind "systematically biased and poorly correlated with correctness." — Quelle: [arxiv 2602.00279](https://arxiv.org/html/2602.00279)

2. **Sample Consistency (mehrfach fragen, Antworten vergleichen) liefert die zuverlässigste Kalibrierung** — Gleiche Studie: "answer frequency (consistency across samples) yields the most reliable calibration." Das ist die Self-Consistency Methode aus Wang et al. 2022. — Quelle: [arxiv 2602.00279](https://arxiv.org/html/2602.00279), bestätigt durch [Hobelsberger et al. 2025](https://arxiv.org/html/2510.20460v1)

3. **Hybrid-Ansatz (CoCoA) schlägt Einzelmethoden** — Confidence-Consistency Aggregation kombiniert Token-Wahrscheinlichkeiten mit Sample Consistency und liefert "best reliability overall, improving both calibration and discrimination." — Quelle: [Hobelsberger et al. 2025, arxiv 2510.20460](https://arxiv.org/html/2510.20460v1), basierend auf Vashurin et al. 2025

4. **Logit/Token-Probability ist brauchbar, aber instruction-tuning macht es schlechter** — Instruction tuning erzeugt "strong probability mass polarization" → Token-Level Confidence wird unzuverlässiger. Reasoning-Finetuning mildert das teilweise. — Quelle: [arxiv 2602.00279](https://arxiv.org/html/2602.00279)

5. **Temperature Scaling (Post-Hoc) funktioniert als schneller Fix** — MIT's "Thermometer" Methode nutzt klassisches Temperature Scaling, adaptiert für LLMs. Effizient kalibrierbar für neue Tasks ohne Retraining. — Quelle: [ScienceDaily/MIT, Aug 2024](https://www.sciencedaily.com/releases/2024/08/240801121940.htm)

---

## Die 5 Methoden im Vergleich

### 1. Verbalized Confidence Elicitation (VCE)
**Was:** Model wird per Prompt gebeten, seine Confidence als Zahl (0-100%) anzugeben.  
**Implementierung:** Prompt-Suffix: "Rate your confidence 0-100%". Trivial zu implementieren.

| Pro | Contra |
|-----|--------|
| Zero-Code, funktioniert mit jeder API | Systematisch overconfident |
| Kein API-Zugang zu Logits nötig | Schlecht korreliert mit Korrektheit |
| Sofort einsetzbar | Biased durch RLHF (Modelle "wollen" confident klingen) |

**Evidence:** Hobelsberger et al. (2025) zeigen VCE als schwächste der 4 getesteten Methoden. Arxiv 2602.00279 (Jan 2026) bestätigt: "verbalized approaches are systematically biased."  
**Interpretation:** Für unser System als Standalone unbrauchbar, aber als *ein Signal unter mehreren* potenziell nutzbar.

### 2. Sample Consistency (Self-Consistency)
**Was:** Gleiche Frage N-mal stellen (temperature > 0), Antworten vergleichen. Häufigste Antwort = confident.  
**Implementierung:** N=5-10 Samples, Antwort-Clustering (semantisch oder exakt), Ratio der häufigsten Antwort = Confidence Score.

| Pro | Contra |
|-----|--------|
| Beste Kalibrierung in aktuellen Studien | N API-Calls → N× Kosten + Latenz |
| Black-Box: funktioniert ohne Logit-Zugang | Nur für Fragen mit diskreten Antworten gut |
| Intuitiv verständlich | Bei open-ended Generation schwer zu clustern |

**Evidence:** Wang et al. 2022 (Self-Consistency), bestätigt durch arxiv 2602.00279 (Jan 2026) als "most reliable calibration."  
**Interpretation:** Beste Einzelmethode, aber teuer. Für kritische Entscheidungen (wo Honesty-as-Currency am wichtigsten ist) lohnt sich der Overhead.

### 3. Logit-Based / Maximum Sequence Probability (MSP)
**Was:** Token-Wahrscheinlichkeiten aus dem Modell auslesen, Durchschnitt/Minimum/Gesamtlikelihood berechnen.  
**Implementierung:** API mit `logprobs=true` (OpenAI, Anthropic teils), dann avg(log_prob) über Tokens.

| Pro | Contra |
|-----|--------|
| Schnell, ein API-Call | Nicht alle APIs bieten Logprobs |
| Gut für kurze, faktische Antworten | Instruction-Tuning verzerrt die Probabilities |
| Keine Extra-Kosten | Hohe Probability ≠ korrekt (confident hallucinations) |

**Evidence:** Karapetyan (Medium, Jun 2025): gute Übersicht der Methodik. Guo et al. 2017: moderne NNs sind overconfident. Arxiv 2602.00279: "instruction tuning induces strong probability mass polarization."  
**Interpretation:** Nützlich als schnelles Signal, aber allein nicht ausreichend. Besonders bei API-only Zugang (Claude, GPT) oft nicht verfügbar.

### 4. CoCoA (Confidence-Consistency Aggregation)
**Was:** Hybrid: kombiniert Logit-Confidence mit Sample Consistency.  
**Implementierung:** Score = f(MSP, Consistency). Vashurin et al. 2025 definieren die Aggregation.

| Pro | Contra |
|-----|--------|
| Beste Gesamtperformance in Benchmarks | Braucht sowohl Logits als auch Multi-Sampling |
| Verbessert Kalibrierung UND Diskrimination | Höchste Komplexität |
| Robuster als Einzelmethoden | Nicht trivial ohne Logit-Zugang |

**Evidence:** Hobelsberger et al. 2025: "hybrid CoCoA approach yields the best reliability overall."  
**Interpretation:** Gold-Standard, aber für unser System möglicherweise over-engineered wenn wir keinen Logit-Zugang haben.

### 5. Temperature Scaling (Post-Hoc Calibration)
**Was:** Logits durch einen gelernten Temperatur-Parameter T dividieren, um Overconfidence zu korrigieren. Klassische Methode, adaptiert für LLMs.  
**Implementierung:** Kleines Validation-Set nötig, T wird per NLL-Minimierung gelernt. MIT's "Thermometer" macht das effizient.

| Pro | Contra |
|-----|--------|
| Einfach, bewährt (seit Platt Scaling) | Braucht Logit-Zugang + Labeled Data |
| Fixiert Overconfidence effektiv | Task-spezifisch (T muss pro Task gelernt werden) |
| Kein Retraining des Modells | Nicht anwendbar bei Black-Box APIs |

**Evidence:** MIT Thermometer (ScienceDaily, Aug 2024). Guo et al. 2017 (Originalarbeit zu NN-Calibration).  
**Interpretation:** Relevant wenn wir eigene Modelle hosten. Für API-basierte Nutzung nicht direkt anwendbar.

---

## Was können wir SOFORT implementieren?

**→ Verbalized Confidence + Consistency-Check Hybrid (Budget-CoCoA)**

Ohne Logit-Zugang, rein prompt-basiert:

```
Schritt 1: Bei kritischen Outputs → 3 Samples generieren (temp=0.7)
Schritt 2: Semantic Similarity zwischen Samples prüfen (Embeddings oder LLM-Judge)
Schritt 3: Consistency Score = Anteil übereinstimmender Kernantworten
Schritt 4: VCE als Tiebreaker (nur wenn Consistency unklar)
Schritt 5: Confidence = weighted(Consistency × 0.8, VCE × 0.2)
```

**Warum diese Gewichtung?** Weil Evidence zeigt: Consistency >> VCE für Kalibrierung. VCE nur als schwaches Zusatzsignal. *(Begründung: arxiv 2602.00279)*

**Kosten:** 3× statt 1× API-Calls für kritische Outputs. Für Routine-Outputs: kein Overhead (nur VCE als Minimum).

**Integration in Honesty-as-Currency:**
- Confidence < 0.5 → "Ich bin mir unsicher" (aktuelles System)
- Confidence 0.5-0.8 → Antwort mit Hedge + Quellen-Empfehlung
- Confidence > 0.8 → Normale Antwort
- Die Schwellen sind initial heuristisch, können mit Nutzerfeedback kalibriert werden

---

## Contradiction Register

| Konflikt | Quellen | Warum unterschiedlich | Impact |
|----------|---------|----------------------|--------|
| VCE "brauchbar" vs "systematisch biased" | Kadavath 2022 vs arxiv 2602.00279 | Kadavath testete base models, neuere Studie instruction-tuned models. RLHF macht Overconfidence schlimmer. | Hoch — VCE allein ist für production ungeeignet |
| Logit-Confidence "informativ" vs "polarisiert" | Hendrycks 2017 vs arxiv 2602.00279 | Pre- vs Post-Instruction-Tuning. Ältere Forschung an base models. | Mittel — Logits sind brauchbar, aber mit Vorsicht |

---

## Claim Ledger

| # | Claim | Evidence | Confidence | Was würde Confidence erhöhen? |
|---|-------|----------|-----------|-------------------------------|
| 1 | Sample Consistency ist die zuverlässigste Black-Box Calibration-Methode | arxiv 2602.00279 (Jan 2026), Hobelsberger et al. 2025, Wang et al. 2022 | **High** — 3 unabhängige Quellen | — |
| 2 | Verbalized Confidence ist systematisch overconfident | arxiv 2602.00279, Xiong et al. 2023, Hobelsberger et al. 2025 | **High** — konsistent über Studien | — |
| 3 | CoCoA (Hybrid) schlägt alle Einzelmethoden | Hobelsberger et al. 2025 (1 Studie, 4 QA-Tasks) | **Medium** — nur 1 Primärquelle, aber methodisch solide | Replikation auf anderen Tasks/Modellen |
| 4 | Instruction Tuning verschlechtert Token-Level Calibration | arxiv 2602.00279 (Jan 2026) | **Medium** — 1 Quelle, aber mechanistisch plausibel | Bestätigung über mehrere Modell-Familien |
| 5 | 3-5 Samples reichen für brauchbare Consistency-Scores | Wang et al. 2022 (Self-Consistency Paper), Praxis-Reports | **Medium** — Original-Paper nutzt 5-40 Samples, genaues Minimum unklar | Eigene A/B-Tests mit unserem System |

---

## Empfehlung

**Judgment (meine Meinung, klar als solche gekennzeichnet):**

Ja, Honesty-as-Currency sollte erweitert werden — aber pragmatisch:

1. **Sofort:** Verbalized Confidence als Minimum-Signal bei JEDEM Output (kostet nichts extra, ist besser als nichts, auch wenn schlecht kalibriert)
2. **Kurzfristig (1-2 Wochen):** Budget-CoCoA (3-Sample Consistency) für Outputs die als "kritisch" getaggt sind (Tier 2/3 Entscheidungen)
3. **Nicht jetzt:** Logit-basierte Methoden oder Temperature Scaling — wir nutzen APIs, haben keinen Logit-Zugang bei Claude/GPT
4. **Messen:** Eigenes Calibration-Tracking aufbauen — bei jedem Confidence-Score den wir ausgeben, Feedback sammeln ob die Antwort tatsächlich korrekt war. Damit können wir unsere Schwellen über Zeit kalibrieren.

Der größte Quick-Win ist nicht die Methode, sondern das **Tracking**: Wenn wir systematisch erfassen wie oft unsere Confidence-Level stimmen, können wir jede Methode über Zeit verbessern.

---

## Beipackzettel

```
Confidence: 72%
Sources checked: 14
Verified facts: 8
Unverified claims: 2 (Claim #5 Sample-Minimum, CoCoA Generalisierbarkeit)
Search queries used: 
  - "LLM calibration methods confidence production 2025 2026"
  - "language model confidence calibration verbalized probability implementation"  
  - "LLM confidence estimation production systems practical approaches token probability"
Time spent: ~8 min
Freshness: Alle Kernquellen 2025-2026
```

---

*Begründung Struktur: AGENT.md verlangt Evidence/Interpretation/Judgment Trennung → jede Methode hat separates Evidence + Interpretation. Empfehlung ist als Judgment gekennzeichnet. Claim Ledger per Tier 2 Anforderung. Corrections.md: Direkt, keine langen Einleitungen, 1 Empfehlung mit klarem "Mein Vote".*
