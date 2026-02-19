# Moonshot Batch B: Librarian · Comparatist · Futurist

> Generated: 2026-02-19 · Input: AR-020-v3-full.md + Dossier (30 papers) + claims_matrix + timeline + graph_stats + 5 web searches

---

## 📚 ROLLE 1: LIBRARIAN — Was fehlt in der Literatur?

### Beipackzettel
| Field | Value |
|-------|-------|
| Agent | 🔬 RESEARCHER / Librarian |
| Model | claude-opus-4-6 |
| Confidence | 78% |
| Key Finding | Report nutzt 25+ Quellen solide, aber das Dossier ist mit 30 Papers VIEL dünner als die behaupteten 146 — die Pipeline hat nur 30 analysiert. Wichtige Lücken existieren. |
| Recommendation | 8-10 Papers nachrüsten, insbesondere SConU, Domain-Shift CP, und APRICOT |

### 1.1 Dossier vs. Report: Coverage-Analyse

**Ehrliches Problem:** Das Dossier behauptet 30 Papers analysiert zu haben (Meta: "Papers analyzed: 30"), NICHT 146. Die Zahl 146 stammt nirgends aus den Dateien. Der Graph hat 190 Nodes, aber davon sind nur 26 Papers — der Rest sind Methods, Datasets, Models, Claims.

**Was im Dossier steht, aber NICHT im Report:**

| Paper | Warum relevant | Warum fehlt es? |
|-------|---------------|-----------------|
| **APRICOT** (2024) — "Auxiliary Prediction of Confidence Targets" | Black-box Calibration ohne Modellzugang, direkt Tier-1-relevant | Report erwähnt es NIRGENDS, obwohl es ein direkter Konkurrent zu Budget-CoCoA ist |
| **STeCa** — Step-Level Trajectory Calibration (2025) | Agent-Trajectory-Calibration wie HTC, aber anderer Ansatz | Direkte Alternative zu HTC/GAC, Report ignoriert es |
| **"Be Friendly, Not Friends"** — LLM Sycophancy & Trust (2025) | Erklärt WARUM Overconfidence beim User ankommt — ergänzt RLHF-Mechanismus | Report fokussiert auf Modell-Calibration, ignoriert User-seitige Trust-Verzerrung |
| **Epistemic Alignment Framework** (2025) | Structured intermediary between user needs und system capabilities | Konzeptionell relevant für Tier 3 (Human Routing) |
| **MLA-Trust Benchmark** (2025) | Multimodal Agent Trustworthiness | Report ignoriert multimodale Agents komplett |

### 1.2 Papers die dem Report WIDERSPRECHEN

1. **"Current UQ practices not optimal for human users"** (Dossier Claim #25) — Der Report empfiehlt technische ECE-Optimierung. Dieses Paper argumentiert: ECE ist das falsche Ziel. Humans brauchen andere UQ als Maschinen. **Direkter Widerspruch zu Tier 1-3 Architektur, die rein technisch gedacht ist.**

2. **"Cheaper models as initial judges"** (Dossier Claim #11) — Unterstützt Budget-CoCoA, ABER Claim #4 ("Current UQ practices not optimal") konterkariert die Annahme, dass billige Consistency-Checks = gute Calibration.

3. **"Existing works neglect generalization to other prompt styles"** (Dossier Claim #23) — Direkt relevant: Report empfiehlt Self-Consistency als Default, aber die Generalisierbarkeit über Prompt-Styles ist NICHT belegt.

### 1.3 Ignorierte Forschungsrichtungen

1. **Human-Centered UQ** — Eine ganze Richtung die sagt: Calibration für Maschinen ≠ Calibration für Menschen. Report ignoriert das komplett.
2. **Multimodal Agent Trust** — MLA-Trust Benchmark existiert, Report behandelt nur Text-Agents.
3. **Sycophancy als Trust-Vektor** — Nicht nur Calibration-Bias, sondern aktive Trust-Manipulation durch Gesprächsstil.
4. **Domain-Shift-Aware Conformal Prediction** (Lin et al., Oct 2025, arXiv:2510.05566) — Direkt relevant für Section 8 (Distribution Shift), aber nicht im Report.

### 1.4 Web-Search: Papers die WEDER im Report NOCH im Dossier sind

| Paper | Quelle | Relevanz |
|-------|--------|----------|
| **SConU** — Selective Conformal Uncertainty in LLMs (ACL 2025) | aclanthology.org/2025.acl-long.934 | Verbindet Conformal Prediction + Selective Prediction — genau die Tier 2+3 Kombination die Report empfiehlt, aber als einzelne Methode |
| **Domain-Shift-Aware CP for LLMs** (Lin et al., Oct 2025) | arXiv:2510.05566 | Löst das in Section 8 als "unsolved" markierte Problem teilweise |
| **"Towards Responsible LLM-empowered Multi-Agent Systems"** (Feb 2025) | arXiv:2502.01714 | Direkt relevant für Section 5 — behandelt Uncertainty Propagation in MAS |
| **Nathan Lambert: "RLHF" Book** (2025-2026, living document) | arXiv:2504.12501 | Umfassendstes Werk zu RLHF, geht über einzelne Papers hinaus |
| **Conformal Prediction for EHR Extraction** (AAAI-SS 2025) | ojs.aaai.org | Production deployment von CP in Healthcare — Case Study die Report fehlt |

---

## 🌍 ROLLE 2: COMPARATIST — Wo stehen wir vs. SOTA?

### Beipackzettel
| Field | Value |
|-------|-------|
| Agent | 🔬 RESEARCHER / Comparatist |
| Model | claude-opus-4-6 |
| Confidence | 72% — begrenzt durch fehlende direkte Benchmark-Vergleiche |
| Key Finding | Die 3-Tier Architektur ist PRAKTISCHER als Alternativen, aber WENIGER rigoros. Ainary positioniert sich richtig im "Practical + Mid-Cost" Quadranten. |
| Recommendation | APRICOT als Tier-1-Alternative evaluieren. SConU für Tier-2/3-Fusion. Konkrete ECE-Zahlen für Ainary-Setup messen. |

### 2.1 Framework-Vergleich: 3-Tier vs. Existierende

| Dimension | Ainary 3-Tier | APRICOT | ConU | SAUP | HTC/GAC | STeCa |
|-----------|--------------|---------|------|------|---------|-------|
| **Scope** | Full-stack architecture | Single-method (black-box) | Single-method (CP) | Propagation framework | Agent trajectories | Agent step-level |
| **Access** | Black-box first | Black-box only | Needs logprobs | Any | Any | Any |
| **Guarantees** | None (Tier 1), Statistical (Tier 2) | None | Statistical | Mathematical | None | None |
| **Cost** | $0.005-0.046/decision | Low (1 aux model) | Variable | Minimal | Low | Low |
| **Production-Ready** | ✅ (prescriptive) | ⚠ (method, not arch) | ⚠ (cold start) | ❌ (theoretical) | ❌ (preprint) | ❌ (preprint) |
| **Multi-Agent** | Partial (Tier 3 routing) | ❌ | ❌ | ✅ | Partial | Partial |
| **Human-Centered** | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |

**Was andere BESSER machen:**
- **APRICOT**: Braucht keinen Mehrfach-Sampling — ein Auxiliary Model reicht. Potenziell billiger UND schneller als Budget-CoCoA.
- **ConU/SConU**: Statistische Garantien die Ainary Tier 1 nicht hat.
- **SAUP**: Mathematisches Framework für Propagation — Ainary hat nur "route to human".
- **Domain-Shift-Aware CP**: Löst das Distribution-Shift-Problem, das Report als "unsolved" markiert.

**Was Ainary BESSER macht:**
- **Einziges Full-Stack-Framework** das von "was deploye ich Montag" bis "wie comply ich mit EU AI Act" reicht.
- **Kostenanalyse** — kein anderes Paper hat eine Waterfall-Kostenanalyse.
- **Decision Tree** — kein anderes Framework hat einen prescriptive Decision Tree.
- **Meta-Calibration** — einziger Report der sich selbst kalibriert.

### 2.2 Benchmark-Vergleich: ECE/MCE

| Method | Typical ECE | Context | Source |
|--------|------------|---------|--------|
| Temperature Scaling (white-box) | ~0.25% | Vision models, ideal setting | Guo et al. 2017 |
| BaseCal-ReEval | -42.9% vs. baselines | 5 datasets, 3 LLM families | Tan et al. Jan 2026 |
| BaseCal-Proj | -35.3% vs. baselines | Same, lower compute | Tan et al. Jan 2026 |
| Self-Consistency (Ainary Tier 1) | ~27% absolute | PMC biomedical, 13 datasets | PMC 2024 |
| Verbalized Confidence | ~42% absolute | Same setting | PMC 2024 |
| APRICOT | Not directly comparable | Different benchmarks | 2024 |
| HTC/GAC | "Best on GAIA" | Agent benchmark, not ECE | Zhang et al. 2026 |

**Ehrliche Bewertung:** Die 27% ECE für Self-Consistency ist NICHT gut. Es ist besser als Verbalized (42%), aber Temperature Scaling erreicht 0.25%. Der Vergleich ist unfair (white-box vs. black-box), aber Kunden interessiert das nicht. BaseCal erreicht 42.9% REDUCTION — das wäre ~15.5% ECE wenn man von 27% startet. **Ainary's Tier 1 ist nicht SOTA — es ist das Beste was OHNE Modellzugang geht.**

### 2.3 Positioning Map

```
                    HIGH QUALITY (low ECE)
                         │
    Temperature Scaling  │  BaseCal
    (white-box only)     │  (needs base model)
                         │
                         │         SConU
   ─────────────────────────────────────────
   LOW COST              │              HIGH COST
                         │
         ★ Ainary 3-Tier │    Ensemble Methods
         Budget-CoCoA    │    (GETS, cascading)
         APRICOT         │
                         │
                    LOW QUALITY (high ECE)
                    
    ACADEMIC ←───────────────────────→ PRACTICAL
         │                                  │
    SAUP, ConU, HTC                   ★ Ainary
    (frameworks, papers)              (deployable Monday)
    SConU, BaseCal                    Budget-CoCoA
    (methods, benchmarks)             APRICOT
```

**Ainary's Position:** Mid-Quality, Low-Cost, Highly Practical. Das ist die richtige Nische für ein Startup — nicht die beste Calibration, aber die einzige die man sofort deployen kann.

---

## 🔮 ROLLE 3: FUTURIST — Was kommt in 12 Monaten?

### Beipackzettel
| Field | Value |
|-------|-------|
| Agent | 🔬 RESEARCHER / Futurist |
| Model | claude-opus-4-6 |
| Confidence | 65% — Predictions über 12 Monate bei diesem Tempo sind inherent unsicher |
| Key Finding | EU AI Act High-Risk-Deadline (Aug 2026) wird der größte Katalysator. Native Calibration von Providern ist das größte Risiko. |
| Recommendation | Ainary muss sich als COMPLIANCE-LAYER positionieren, nicht als Calibration-Methode. Methoden werden commoditized, Compliance-Frameworks nicht. |

### 3.1 Drei Entwicklungen die das Feld verändern werden

**1. EU AI Act High-Risk Enforcement (August 2026)** [85% — weil Gesetz bereits verabschiedet, Deadline steht fest]
- Ab August 2026 müssen High-Risk AI Systems compliant sein.
- Artikel 15 fordert "appropriate accuracy" — bisher ohne Calibration-Pflicht.
- ABER: CEN/CENELEC-Standards werden das operationalisieren. Calibration wird de facto Standard.
- **Impact auf Ainary:** RIESIGE Chance. Jedes EU-Unternehmen mit High-Risk AI braucht eine Lösung.

**2. Native Confidence von LLM-Providern (12-18 Monate)** [60% — Signale da, aber Timing unsicher]
- OpenAI hat bereits logprobs partial exposed. Nächster Schritt: native confidence scores.
- Anthropic, Google werden folgen (Wettbewerbsdruck).
- Wenn GPT-5 mit eingebautem Confidence-Score kommt → Ainary Tier 1 (Self-Consistency) wird TEILWEISE obsolet.
- **Aber:** Native Confidence ist single-method → Ainary's Multi-Method + Compliance-Layer bleibt relevant.

**3. Agent-Frameworks integrieren Calibration (6-12 Monate)** [70% — LangChain, CrewAI etc. bewegen sich in diese Richtung]
- LangChain, AutoGen, CrewAI werden Confidence-Scoring als Feature einbauen.
- Basierend auf HTC/GAC, SAUP-Konzepten.
- **Impact:** Commoditization der Basismethoden. Ainary's Differenzierung muss ÜBER die Methode hinausgehen.

### 3.2 Werden unsere Empfehlungen in 12 Monaten noch gelten?

| Empfehlung | Gültig in 12 Monaten? | Warum? |
|-----------|----------------------|--------|
| Tier 1: Self-Consistency als Default | ⚠ TEILWEISE — wenn Provider native Confidence liefern, wird Consistency zum Fallback | 60% |
| Tier 2: Conformal Prediction für High-Stakes | ✅ JA — CP wird wichtiger, nicht weniger | 85% |
| Tier 3: Selective Prediction / Human Routing | ✅ JA — wird durch Regulierung sogar MEHR gebraucht | 90% |
| 3-Tier als Architektur | ✅ JA — die Struktur bleibt, die Methoden in jedem Tier ändern sich | 80% |
| Cost <$0.05/decision | ⚠ WIRD BILLIGER — API-Preise fallen, native Confidence ist gratis | 75% |

### 3.3 Risiken

| Risiko | Wahrscheinlichkeit | Impact | Mitigation |
|--------|-------------------|--------|------------|
| OpenAI/Anthropic bieten native Calibration → Tier 1 wird Commodity | 60% in 12 Monaten | HIGH — Kernprodukt-Differenzierung gefährdet | Positionierung als Compliance + Multi-Method Layer |
| HTC/GAC repliciert NICHT → Family 7 fällt weg | 25% | MEDIUM — Report verliert ein Kapitel, Architektur bleibt | Nicht zu stark auf einzelne Preprints setzen |
| EU AI Act Enforcement wird verschoben/verwässert | 15% | HIGH — Compliance-Urgency sinkt | Diversifizieren: nicht nur EU, auch ISO 42001, SOC2 |
| Self-Consistency funktioniert nicht at scale (>1M calls/day) | 20% | MEDIUM — Kosten explodieren | Cost-Cascading: Tier 0 → Tier 1 nur bei Bedarf |

### 3.4 Chancen

| Chance | Wahrscheinlichkeit | Impact | Action |
|--------|-------------------|--------|--------|
| EU AI Act Enforcement → Calibration wird de facto Pflicht | 85% | HUGE — $B Markt entsteht | First-mover-Advantage JETZT aufbauen |
| Insurance/Liability für AI-Entscheidungen → Calibration als Versicherungs-Requirement | 40% in 12 Monaten | HIGH | Paper/Position zu "Calibration as Insurability Condition" |
| Multi-Agent-Frameworks brauchen Calibration-Middleware | 70% | HIGH | SDK/API als Middleware-Layer anbieten |
| Human-Centered UQ wird Forschungs-Hot-Topic | 60% | MEDIUM | Position Paper zu "Calibration for Humans, Not Machines" |

### 3.5 Predictions mit Confidence

1. **"Mindestens ein Major LLM Provider wird native Confidence Scores anbieten"** [65% — weil OpenAI logprobs bereits teilweise exponiert, Markt-Pull durch Enterprise-Kunden]

2. **"EU AI Act High-Risk Enforcement wird NICHT verschoben"** [80% — weil politischer Wille stark, erste Bußgelder werden medienwirksam]

3. **"Agentic Calibration wird eigene Konferenz-Track bekommen (NeurIPS/ICML 2026/2027)"** [55% — weil HTC, STeCa, SAUP zeigen: es gibt genug Material, aber Timing unsicher]

4. **"Self-Consistency wird in mindestens 2 Major Agent-Frameworks als Default eingebaut"** [70% — weil es einfach zu implementieren ist und der Report es populär macht]

5. **"Innerhalb von 12 Monaten wird ein Major AI-Incident direkt auf fehlende Calibration zurückgeführt"** [75% — weil Agent-Deployments exponentiell steigen und Calibration nicht mitkommt. Die Frage ist nicht ob, sondern wann.]

---

## Meta: Cross-Role Synthese

### Was alle drei Rollen gemeinsam sagen:

1. **Der Report ist GUT für Practitioners, aber LÜCKEN für Academics.** Die Librarian-Analyse zeigt: wichtige Papers fehlen (APRICOT, SConU, Human-Centered UQ). Der Report ist ein Practitioner-Guide, kein Survey.

2. **Ainary's Positioning ist RICHTIG, aber FRAGIL.** Low-Cost + Practical ist die richtige Nische. Aber wenn Provider native Calibration anbieten, schmilzt der Vorteil. Die Flucht nach vorne: Compliance-Layer + Multi-Method.

3. **Die nächsten 6 Monate sind das Window.** EU AI Act Enforcement August 2026 → Unternehmen fangen JETZT an zu suchen. Wer in 6 Monaten kein Calibration-Angebot hat, kommt zu spät.

### Top 3 Actions:

1. **APRICOT und SConU in Report V4 einbauen** — sie sind direkt relevant und stärken die Architektur
2. **Compliance-Narrative stärken** — "Calibration as EU AI Act Readiness" statt "Calibration as Technical Method"
3. **Human-Centered UQ als Differenzierung** — niemand sonst macht das, und es ist eine echte Lücke

---

*Brutal ehrlich: Der Report ist solide Arbeit. Aber das Dossier ist DÜNN (30 Papers, nicht 146 wie suggeriert). Die Web-Searches haben 5 direkt relevante Papers gefunden die fehlen. Die Architektur ist praktisch gut, aber akademisch nicht SOTA. Das ist OK — das ist nicht das Ziel. Das Ziel ist "was deploye ich Montag" und da ist AR-020 v3 das beste was es gibt.*
