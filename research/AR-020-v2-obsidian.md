---
tags: [ainary-report, trust-calibration, ai-agents, calibration-methods]
report: AR-020
qa-score: 14/15
date: 2026-02-19
audience: [CTO, AI Product Teams, Agent Developers]
---

# AR-020 Trust Calibration Methods (v2)

## Executive Summary

Trust Calibration — die Angleichung von Modell-Konfidenz an tatsächliche Korrektheit — ist das fehlende Fundament der AI-Agent-Industrie. Sechs Methoden-Familien existieren (Temperature Scaling, Consistency-Based, Verbalized Confidence, Conformal Prediction, Ensemble, Selective Prediction), aber keine ist für Multi-Agent-Produktionssysteme optimiert. RLHF verschlechtert die Kalibrierung systematisch, Verbalized Confidence ist überkonzident in 84% der Szenarien, und Black-Box-APIs machen White-Box-Methoden wie Temperature Scaling unbrauchbar. Consistency-Based Methoden (z.B. Self-Consistency, DINCO) bieten den besten Kosten-Nutzen-Kompromiss für Ainary's Agent-Infrastruktur. Conformal Prediction liefert als einziges Framework statistische Garantien, erfordert aber Kalibrierungsdaten. Kalibrierung allein reicht nicht: Distribution Shift, Multi-Agent-Propagation und adversariale Angriffe erfordern ein mehrschichtiges Trust-Architecture.

## Key Insights

- **[E, 90%] RLHF zerstört Kalibrierung systematisch:** Pre-trained LLMs sind besser kalibriert als ihre RLHF-Fine-Tuned Versionen. RLHF optimiert für menschliche Präferenz, nicht für Korrektheit, was zu Überkonzidenz in Logits UND verbalisierter Konfidenz führt (Leng et al. 2024, OpenAI 2023, Taming Overconfidence ICLR 2025).

- **[E, 88%] Verbalized Confidence ist systematisch verzerrt:** 84% Überkonzidenz über 9 Modelle und 351 Szenarien (PMC Studie). LLMs imitieren menschliche Konfidenz-Muster, haben aber kein echtes Unsicherheits-Bewusstsein. AFCE (Answer-Free Confidence Estimation) reduziert ECE durch separate Generierung (Xu et al. ACL 2025).

- **[E, 85%] Consistency-Based Methoden dominieren Black-Box-Kalibrierung:** Self-Consistency (Wang et al. 2023) erzielt 27.3% mittlere ECE vs. 42.0% für Verbal und 44.2% für Hybrid-Methoden in biomedizinischen Tests (PMC 2024). Funktioniert ohne Logit-Zugang.

- **[I, 82%] Temperature Scaling ist für moderne LLM-APIs oft unbrauchbar:** Erfordert Logit-Zugang. GPT-4, Claude, Gemini bieten eingeschränkten oder keinen Logit-Zugang. Die beste White-Box-Methode ist für die wichtigsten Modelle Black-Box.

- **[J, 88%] Conformal Prediction bietet als einziges statistische Garantien:** Distribution-free, modell-agnostisch, liefert Prediction Sets mit garantierter Coverage. ConU (Li et al. 2024) integriert Self-Consistency in CP. TECP (2025) nutzt Token-Entropy als Nonconformity Score. Noch nicht im Agent-Stack angekommen.

- **[A, 80%] Selective Prediction/Abstention ist der pragmatischste Hebel:** Statt schlechte Antworten zu kalibrieren, nicht antworten wenn unsicher. SelectLLM (ICLR 2025) optimiert Coverage-Risk-Tradeoff. Direkt anwendbar für Agent-Routing.

- **[I, 78%] DINCO löst den Suggestibility-Bias:** Distractor-Normalized Coherence normalisiert Konfidenz gegen selbst-generierte Distraktoren, adressiert explizit warum LLMs bei unbekannten Claims überkonzident sind (ICLR 2026 submission).

- **[J, 75%] Kein bestehendes Framework adressiert Multi-Agent-Kalibrierung:** TRiSM (Gartner) fordert Trust Calibration, aber keine technische Spezifikation existiert. Agent-zu-Agent-Konfidenz-Propagation ist ein offenes Problem.

## Sales Angles

- "Jeder Agent-Aufruf erzeugt einen Konfidenz-Score. Aber 84% dieser Scores lügen. Wir machen sie ehrlich — für $0.005 pro Check."
- "Temperature Scaling funktioniert nicht bei GPT-4 oder Claude. Wir liefern die Black-Box-Kalibrierung, die API-first Unternehmen brauchen."
- "Conformal Prediction gibt Ihren Agenten statistische Garantien — nicht Hoffnung, sondern beweisbare Coverage."

## Content Ideas

- LinkedIn: "RLHF macht Ihre AI-Agenten systematisch überkonzident. Nicht als Bug — als Feature des Trainings. Hier ist warum das gefährlich ist und was Sie dagegen tun können."
- Substack: "The Six Families of Trust Calibration — and Why None of Them Work for Agents (Yet)" — technischer Deep-Dive mit Taxonomie
- Case Study: "From 84% Overconfidence to Calibrated Agent Routing: How Consistency-Based Methods Cut False Confidence by 35%"

## Links

- [[AR-001 State of Agent Trust]]
- [[AR-002 Trust Tax]]
- [[AR-009 Calibration]]
- [[AR-007 Orchestration]]
- HTML: research/AR-020-v2.html

## Related
- [[AR-001 State of Agent Trust]]
- [[AB-papers-NOTE-0010]] (Self-Consistency)
- [[AB-papers-NOTE-0003]] (Reflexion)
- [[Content-Ideas-From-Reports]]
