# Beipackzettel — Der Standard (v1.0)

*"Wie der Beipackzettel bei Medikamenten: Jeder AI-Output muss einen haben."*
*Source: github.com/florianziesche/agenttrust*

---

## Was ist der Beipackzettel?

Pflicht-Metadaten auf JEDEM Agent-Output. Nicht optional. Nicht "nice to have".
Der Leser weiß in 10 Sekunden:
- Wie verlässlich ist das? (Confidence)
- Worauf basiert es? (Sources)
- Was weiß der Agent nicht? (Uncertainties)
- Was kann schiefgehen? (Risks)
- Was wurde nicht geprüft? (Not Checked)

---

## Felder (alle Pflicht)

### 1. Confidence (float, 0-100)

**MUSS berechnet sein, nicht geschätzt.**

Drei Methoden (AgentTrust Library), in Reihenfolge der Stärke:

#### Methode 1: Budget-CoCoA (stärkste — `sample_consistency()`)
```python
from agenttrust import sample_consistency
result = sample_consistency(my_llm, "What causes inflation?", n=3)
# 3/3 agree → HIGH (>85%)
# 2/3 agree → MEDIUM (60-85%)
# 1/3 agree → LOW (<60%)
```
**Formel:** `pct = 30 + agreement_ratio × 55` (cap 30-95%)
**Wann:** Wenn Budget für 3 LLM-Calls pro Claim vorhanden.
**Kosten:** 3× API Call pro Claim.

#### Methode 2: AgentTrust 3-Signal Formula (Standard — Python-computed)
```python
claim_conf = 0.5 × SOURCE + 0.3 × CONSISTENCY + 0.2 × STRUCTURAL

SOURCE = admiralty_score × verification_score × recency
  admiralty:    A1=0.95  A2=0.85  B2=0.70  C3=0.40  D4=0.20  E2=0.10
  verification: verified=1.0  partial=0.5  unverifiable=0.1
  recency:      max(0.5, 1.0 - (current_year - evidence_year) × 0.1)

CONSISTENCY = Budget-CoCoA proxy (from verification status)
  verified     → 0.85  (high agreement)
  partial      → 0.60  (medium)
  unverifiable → 0.30  (low)

STRUCTURAL = deterministic checks on text
  DOI pattern (10.xxxx/)  → +0.30
  URL present             → +0.15
  Specific percentage     → +0.10
  Specific year           → +0.05
  Source reference [S#]   → +0.10
  Cap at 0.50

report_confidence = Σ(claim_conf × claim_weight) / Σ(claim_weight)
  claim_weight: load-bearing=1.0  supporting=0.6  contextual=0.3
```
**Wann:** Standard für alle Reports. Python berechnet, nicht LLM.
**Kosten:** $0 (deterministisch).

#### Methode 3: Verbalized Confidence (schwächste — `verbalized_confidence()`)
```python
from agenttrust import verbalized_confidence
result = verbalized_confidence("I'm 90% confident this is correct.")
# stated: 90% → calibrated: 63% (× 0.7 discount)
```
**Formel:** `calibrated = stated × 0.7`
**Wann:** Nur als Fallback wenn weder CoCoA noch 3-Signal möglich.
**Warum 0.7:** LLMs sind ~84% der Zeit overconfident (PMC/12249208). 30% Discount.

### 2. Risk Level (enum: HIGH / MEDIUM / LOW)

**Python berechnet (gleiche Logik wie `agenttrust.Beipackzettel.risk_level`):**
```python
if confidence < 50 or len(risks) >= 3:
    risk_level = "HIGH"
elif confidence >= 80 and len(risks) == 0:
    risk_level = "LOW"
else:
    risk_level = "MEDIUM"
```

### 3. Grounded (bool)

`True` wenn mindestens 1 Source vorhanden. `False` = **roter Alarm**.
Ungrounded Output sollte nie automatisch shipped werden.

### 4. Sources (list[str])

Jede Quelle die der Agent genutzt hat. Leer = "pure generation with no grounding" = red flag.
Format: "[S#] Titel (Venue, Year)" oder URL.

### 5. Uncertainties (list[str])

Was der Agent NICHT weiß. Muss spezifisch sein.
- ✅ "Cross-domain generalization of ECE 27.3% figure is unverified"
- ❌ "There may be things we don't know"

### 6. Risks (list[str])

Was schiefgehen kann wenn jemand auf diesen Output handelt.
- ✅ "Cost estimates are author estimates — real deployment may cost 5-10x more"
- ❌ "Things might change"

### 7. Not Checked (list[str])

Was angenommen aber nicht verifiziert wurde.
- ✅ "Parasuraman 2010 cited but not in full-text corpus — claim unverified"
- ❌ leer (es gibt IMMER etwas das nicht geprüft wurde)

---

## Trust Score (per Agent, kumulativ)

Der Beipackzettel ist pro Output. Der Trust Score ist pro Agent über Zeit.

### Scoring Regeln (aus `agenttrust.TrustScore`):

```
Agent sagt 85% confident + Output war gut     → +1 (kalibriert)
Agent sagt 95% confident + Output war schlecht → -3 (overconfident)
Agent flaggt Unsicherheit + war real           → +2 (ehrlich)
Agent versteckt Problem das QA findet          → -3 (unehrlich)
Agent sagt 40% confident + Output war schlecht → -1 (falsch aber ehrlich)
```

### Trust Level (bestimmt Autonomie):

```
 0-30:  UNTRUSTED   → QA reviewed ALLES          (100% Review)
31-60:  SUPERVISED  → QA reviewed Flagged Items   (50% Review)
61-80:  SPOT_CHECK  → QA spot-checks              (20% Review)
81+:    AUTONOMOUS  → Direct Delivery             (0% Review)
```

### Anwendung in MIA Pipeline:

```
Sonnet Research Agents: Trust Score beginnt bei 0 (UNTRUSTED)
  → JEDER Sub-Report wird reviewed (Phase 2b)
  → GOOD Output: +1
  → WEAK Output mit ehrlichem "Evidence Quality: low": +1 (ehrlich)
  → WEAK Output ohne Warnung: -3 (hidden problem)

Opus Synthesis: Trust Score beginnt bei 0
  → Phase 3.5 Python Validation = QA
  → New Facts detected: -3 (hidden problem)
  → No New Facts + good E/I/J/A: +1

Über Zeit:
  → Agent der konsistent GOOD liefert: Score steigt
  → Bei Score 61+: Phase 2b Review wird Spot-Check (20% statt 100%)
  → Bei Score 81+: Report geht direkt an Checkpoint 2 ohne Phase 2b
```

---

## Beipackzettel in der MIA Pipeline

```
WER SCHREIBT WAS:

Opus schreibt:                  Python berechnet + ersetzt:
─────────────                   ───────────────────────────
{{CONFIDENCE}}                  → 65.1% (AgentTrust 3-Signal)
{{EIJA}}                        → E:14 I:8 J:3 A:5
{{RISK_LEVEL}}                  → MEDIUM
Sources (Liste)                 Source Count validiert
Uncertainties (Liste)           Prüft: nicht leer?
Risks (Liste)                   Prüft: nicht leer?
Not Checked (Liste)             Prüft: nicht leer?

Sonnet QA prüft:
─────────────────
Stimmen Uncertainties inhaltlich?
Sind Risks realistisch?
Fehlt etwas Offensichtliches in Not Checked?
```

---

## Output Format (Markdown + JSON)

### Markdown (im Report, menschenlesbar):

```markdown
## BEIPACKZETTEL
| Field | Value |
|-------|-------|
| Confidence | 65.1% (AgentTrust 3-Signal, Python-computed) |
| Risk Level | MEDIUM |
| Grounded | Yes |
| Sources | 12 |
| E/I/J/A | E:14 I:8 J:3 A:5 |
| Research Type | Expert Synthesis |
| Self-Calibration | Structural Only |

### Sources
- [S7] Taming Overconfidence in LLMs (NeurIPS 2024)
- [S8] Calibration as Measurement of Trustworthiness (PMC 2024)
- ...

### Uncertainties
- Cross-domain generalization of ECE 27.3% is unverified [A4]
- Budget-CoCoA cost estimates from practitioner source [S19], not academic

### Risks
- Cost estimates are author estimates — real deployment may cost 5-10x
- HTC and BaseCal are preprints — may not survive peer review

### Not Checked
- Parasuraman 2010 [S15] not in full-text corpus
- 84% overconfidence figure [S8] not independently verified
```

### JSON (maschinenlesbar, kompatibel mit `agenttrust.Beipackzettel.to_dict()`):

```json
{
  "confidence": 65.1,
  "risk_level": "medium",
  "is_grounded": true,
  "sources": ["[S7] Taming Overconfidence...", "[S8] Calibration..."],
  "uncertainties": ["Cross-domain generalization unverified"],
  "risks": ["Cost estimates are author estimates"],
  "not_checked": ["Parasuraman 2010 not in corpus"],
  "model": "opus+sonnet",
  "agent_id": "mia-pipeline-v1",
  "eija": {"E": 14, "I": 8, "J": 3, "A": 5}
}
```
