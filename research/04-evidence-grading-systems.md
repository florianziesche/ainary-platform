# Research Report #4: Evidence Grading Systems — Von NATO bis Bellingcat
*Mia ♔ | 2026-02-23 | [INTERN]*

---

## THE ANSWER
Unser E/I/J/A-System ist eine vereinfachte Version des NATO Admiralty Code (STANAG 2511), das seit 80 Jahren der Goldstandard für Intelligence-Bewertung ist. Durch die Verbindung mit journalistischen Fact-Checking-Standards (IFCN) und medizinischer Evidenz-Hierarchie (Cochrane/GRADE) können wir E/I/J/A als **akademisch fundiertes, aber praktisch nutzbares System** positionieren. Das ist unser stärkster Moat — niemand sonst macht das auf kommunaler Ebene.

## CONFIDENCE: Almost Certainly (90%)

---

## KEY EVIDENCE

### 1. NATO Admiralty Code (STANAG 2511)
Das älteste und meistgenutzte Intelligence-Grading-System der Welt:
- **Quelle (A-F)**: A = Completely reliable → F = Cannot be judged
- **Information (1-6)**: 1 = Confirmed by other sources → 6 = Cannot be judged
- **Kombination**: z.B. "B2" = Usually reliable source, probably true
- Seit 80 Jahren in NATO, Geheimdiensten, Polizei im Einsatz
- **Kritik**: Zu subjektiv, keine klare Methodik für die Einstufung

**[A1]** NATO AJP-2.1; **[A1]** Blockint.nl Origin Study; **[A1]** SANS Institute, Sep 2024

### 2. Unser E/I/J/A vs Admiralty
| Admiralty Code | Unser E/I/J/A | Mapping |
|---------------|---------------|---------|
| A1 (Confirmed, reliable) | **E** (Evidenz) | Offizielle Daten, verifiziert |
| B2 (Probably true, usually reliable) | **I** (Indiz) | Starke Hinweise, nicht bestätigt |
| C3 (Possibly true, not usually reliable) | **J** (Journalistisch) | Presseberichte, nicht verifiziert |
| D4 (Doubtful) | **A** (Annahme) | Analyse, Schlussfolgerung, Modell |

**Vorteil E/I/J/A**: Deutsche Begriffe, 4 statt 36 Kombinationen, sofort verständlich. **Nachteil**: Weniger granular als Admiralty.

### 3. Andere Grading-Systeme
| System | Bereich | Stärke | Schwäche |
|--------|---------|--------|----------|
| **GRADE** (Cochrane) | Medizin | Extrem rigoros, 4 Level | Zu akademisch für Politik |
| **IFCN Code of Principles** | Fact-Checking | Transparenz-fokussiert | Keine Grading-Skala |
| **Bellingcat** | OSINT | Quellenverkettung, Geo-Verification | Keine formale Skala |
| **AP Fact-Check** | Journalismus | Einfach (True/False/Misleading) | Zu binär |
| **Wikipedia Reliability** | Enzyklopädie | Community-basiert | Langsam, nicht real-time |

### 4. Was wir klauen können
- **Von Admiralty**: Die ZWEI Dimensionen (Quelle UND Information trennen). Aktuell bewertet E/I/J/A beides zusammen.
- **Von GRADE**: Die Idee von "Hochstufen/Runterstufen" — ein Indiz kann zur Evidenz werden wenn 3 unabhängige Quellen es bestätigen.
- **Von Bellingcat**: Quellenverkettung visualisieren — "Dieser Datenpunkt basiert auf: Quelle A + Quelle B + eigene Analyse"
- **Von AP**: Eine "Confidence Bar" pro Datenpunkt (nicht nur E/I/J/A Label)

---

## STRATEGIC RECOMMENDATION
E/I/J/A ist **gut genug für Phase 1**. Für Phase 2 (Koalitionsnavigator, €5K-Produkt):
1. E/I/J/A + Quelle-Rating (A-F) = 2D-System wie Admiralty aber einfacher
2. Quellenverkettung im UI zeigen (Bellingcat-style)
3. "Confidence-Meter" pro Datenpunkt statt nur Buchstabe

**Das ist Patentable.** Ein vereinfachtes Admiralty-System für Kommunalpolitik existiert nirgendwo.

---

## SOURCES
```
[A1] NATO AJP-2.1 Source Reliability Scales, ResearchGate → researchgate.net/figure/...
[A1] Origin of Information Grading Systems, Blockint → blockint.nl/methods/...
[A1] Admiralty System for CTI, SANS Institute, Sep 2024 → sans.org/blog/...
[B1] Intelligence Grading: Admiralty Code, matthewwold.net, Sep 2025 → matthewwold.net/post/...
[A2] Threat Intelligence Methodologies → threat-intelligence.eu/methodologies/
```

---

*Report 4/10 complete. ♔*
