# Report Blueprint — A+++ Output Definition (v1.0)

## Die 3 Tests

Bevor irgendetwas geschrieben wird:

1. **Der 2-Minuten Test:** Ein VP liest nur das Executive Summary → kann er entscheiden?
2. **Der Montag-Morgen Test:** Kann der Leser am Montag mit Phase 1 der Empfehlung anfangen?
3. **Der "Wusste ich nicht" Test:** Würden 3 Domain-Experten beim Opener sagen "Das wusste ich nicht"?

Wenn einer der 3 Tests fail → Report ist nicht A+++.

---

## Die 12 Bausteine

### 1. BEIPACKZETTEL
**Was:** Maschinenlesbarer + menschenlesbarer Steckbrief des Reports.
**Warum:** Der Leser weiß in 10 Sekunden: Wie verlässlich? Worauf basiert? Was fehlt?
**Format:**
```
| Field | Value |
|-------|-------|
| Confidence | X% (AgentTrust formula, not guessed) |
| Risk Level | HIGH / MEDIUM / LOW |
| Grounded | Yes/No |
| Sources | N numbered [S1]-[SN] |
| E/I/J/A | E:X I:X J:X A:X |
| Research Type | Systematic Review / Expert Synthesis / Dialectic |
| Self-Calibration | Applied / Not Applied |
```
Sources (list), Uncertainties (list), Risks (list), Not Checked (list).

**Qualitätsbar:** Confidence ist BERECHNET (Formel), nicht geschätzt. E>50%, J<20%.
**Anti-Pattern:** "Confidence: High" ohne Formel. Leere Uncertainties-Liste.

---

### 2. OPENER (erste 3 Sätze)
**Was:** Das Erste was der Leser sieht. Entscheidet ob er weiterliest.
**Warum:** McKinsey-Partner lesen max 1 Seite bevor sie entscheiden ob der Rest relevant ist.
**Format:** 3 Sätze. Kein Kontext, keine Definition, kein "In today's world".
- Satz 1: Die Überraschung (was ein Experte NICHT weiß)
- Satz 2: Warum das jetzt relevant ist (Trigger/Deadline)
- Satz 3: Was dieser Report liefert (nicht "untersucht", sondern "liefert")

**Qualitätsbar:** 3 Domain-Experten fragen: "Wusstet ihr Satz 1?" Mindestens 2 sagen Nein.
**Beispiel GOOD:**
> "The training that makes your AI helpful is the same training that makes it overconfident — and the damage is regime-dependent, not absolute. Three papers from January 2026 proved agent-specific calibration works, but no open-source implementation exists. This report delivers a production integration guide with cost models and a phased deployment plan."

**Beispiel BAD:**
> "Trust calibration is an important topic in the field of artificial intelligence. As AI systems become more prevalent, the need for calibration grows. This report examines current methods."

**Anti-Pattern:** Definition als Opener. Historie als Opener. "It's worth noting."

---

### 3. EXECUTIVE SUMMARY (SCR)
**Was:** Situation → Complication → Resolution. 3 Absätze + "If you read nothing else" Bullets.
**Warum:** Der VP liest NUR das. Es muss standalone funktionieren.
**Format:**
- **Situation** (1 Absatz): Was ist der aktuelle Zustand? Fakten, keine Meinung.
- **Complication** (1 Absatz): Was ist das Problem / die Veränderung / die Deadline?
- **Resolution** (1 Absatz): Was empfiehlt der Report? Konkret, nicht "further research needed".
- **"If you read nothing else:"** (3-5 Bullets, standalone, jeder mit [S#] oder [E/I/J])

**Qualitätsbar:** Executive Summary ohne Rest des Reports lesen → kann man entscheiden? Ja = Pass.
**Anti-Pattern:** Resolution sagt "it depends" oder "further research needed" ohne Kontext.

---

### 4. CUSTOM FRAMEWORK
**Was:** EIN originales Modell/Framework das NUR in diesem Report existiert.
**Warum:** Das ist der €200K-Wert. Jeder kann Quellen zusammenfassen. Nur McKinsey liefert ein Framework das Zusammenhänge zeigt die man nicht googlen kann.
**Format:**
- Name (einprägsam, z.B. "The Confidence Stack", "Trust Calibration Maturity Model")
- Visuelle Beschreibung (Achsen, Quadranten/Level, so dass der Leser es zeichnen kann)
- Mapping: Wo liegen die Findings auf dem Framework?
- "So What": Was sagt das Framework was die einzelnen Findings nicht sagen?

**Qualitätsbar:** Google den Framework-Namen → 0 Ergebnisse = Original. >0 = nicht original.
**Anti-Pattern:** Generische 2x2 Matrix. Framework das nur die Findings nochmal auflistet.

---

### 5. KEY FINDINGS (5-7)
**Was:** Die wichtigsten Erkenntnisse, narrativ geschrieben mit Case Studies inline.
**Warum:** Das Fleisch des Reports. Hier entscheidet sich die Qualität.
**Format pro Finding:**
```
**Finding:** [1 Satz, prägnant]
[E/I/J Label + [S#] im Claim Ledger, NICHT inline im Text]

[2-3 Absätze Narrativ mit eingewobenen Case Studies]

**Section Confidence:** X% — [warum, was ist unsicher]
**For the decision maker:** [1-2 Sätze, "So What"]
```

**Qualitätsbar:** 
- Jedes Finding hat ein "So What"
- Jedes Finding hat Section Confidence mit Begründung
- >60% der Findings sind E-basiert
- Case Studies sind REAL (verifizierbar), nicht hypothetisch

**Anti-Pattern:** Finding ohne "So What". Finding ohne Source. Hypothetische Case Study.

---

### 6. CASE STUDIES (2-3 inline)
**Was:** Reale Beispiele die Findings illustrieren.
**Warum:** Menschen erinnern Geschichten, nicht Statistiken.
**Format:**
- Was passiert ist (3-5 Sätze, konkret: Firma, Jahr, Zahlen)
- Source (URL, Court Record, News Article)
- Lesson für den Leser (1 Satz)
- Verbindung zum Finding (explizit)

**Qualitätsbar:** Case Study ist googlebar und verifizierbar. Keine erfundenen Beispiele.
**Anti-Pattern:** "Consider a hypothetical company..." / Erfundene Case Study.

---

### 7. RECOMMENDATIONS
**Was:** Konkrete Handlungsempfehlungen mit Phased Plan.
**Warum:** McKinsey-Reports ohne Recommendations sind €200K Zusammenfassungen.
**Format:**
- **Decision Matrix:** Wenn Szenario A → tue X. Wenn Szenario B → tue Y.
- **Phased Plan:**
  - Woche 1: [spezifische Aktion, wer, Output]
  - Monat 1: [spezifische Aktion, wer, Output]
  - Quartal 1: [spezifische Aktion, wer, Output]
- **"Do Not Deploy If":** 5 spezifische Bedingungen
- **Cost/Benefit:** Ranges, nicht Punkt-Schätzungen. "Author estimate" wo nötig.

Jede Recommendation:
- [A] Label (verweist auf E/I/J die sie stützen)
- "If Wrong:" — was passiert wenn die Empfehlung falsch ist? Reversibel?

**Qualitätsbar:** Montag-Morgen Test: Kann der Leser Woche 1 am Montag starten?
**Anti-Pattern:** "Consider implementing..." ohne Timeline. "Do more research" als Recommendation.

---

### 8. RISKS & "WHAT WOULD CHANGE THIS"
**Was:** Top 5 Risiken + spezifische Trigger die Conclusions invalidieren.
**Warum:** Ehrlichkeit > Zuversicht. Der Leser muss wissen wann er den Report ignorieren sollte.
**Format:**
- **Risiko:** [spezifisch, nicht generisch]
- **Wahrscheinlichkeit × Impact:** H/M/L Matrix
- **Trigger:** [spezifisches Event das eintreffen müsste]
- **Was dann:** [was der Leser tun sollte wenn der Trigger eintritt]
- **Monitoring:** [wie man den Trigger beobachtet]

**Qualitätsbar:** Trigger sind spezifisch genug um testbar zu sein. "Market changes" ist KEIN Trigger. "EU AI Act enforcement verschoben über Aug 2026 hinaus" IST ein Trigger.
**Anti-Pattern:** Generische Risiken. "Further research needed" ohne Kontext.

---

### 9. CLAIM LEDGER (Appendix)
**Was:** 12 tragende Claims mit E/I/J/A Label, Source, Admiralty, Confidence.
**Warum:** Macht den Report auditierbar. Jeder Claim ist verfolgbar.
**Format:**
| # | Claim | Label | [S#] | Admiralty | Confidence | If Low: what would raise it? |

**Qualitätsbar:** Jeder Claim im Body Text ist im Claim Ledger. Kein Claim ohne Source oder [J] Label.
**Anti-Pattern:** Claims die im Body stehen aber nicht im Ledger. "High Confidence" ohne Begründung.

---

### 10. SOURCE LOG (Appendix)
**Was:** Jede Quelle mit ID, Titel, Typ, URL/DOI, Key Finding, Caveats.
**Warum:** Nachprüfbarkeit. Ohne Source Log ist der Report eine Meinung.
**Format:** Template D (ERF Templates).
**Qualitätsbar:** >70% Tier 1/2 Quellen. Jede [S#] im Body hat einen Eintrag. Kein Eintrag ohne Body-Referenz.
**Anti-Pattern:** Sources die nie zitiert werden. Fake URLs. Quellen ohne Access Date.

---

### 11. CONTRADICTION REGISTER (Appendix)
**Was:** Wo sich Quellen widersprechen + was das für die Entscheidung bedeutet.
**Warum:** Widersprüche glätten = Vertrauen zerstören. Offenlegen = Vertrauen aufbauen.
**Format:** Template F (ERF Templates).
**Qualitätsbar:** Mindestens 1 Contradiction (wenn 0: Report hat nicht genug gegraben).
**Anti-Pattern:** 0 Contradictions in einem komplexen Thema = verdächtig.

---

### 12. SELF-CALIBRATION RESULTS (Appendix)
**Was:** Der Report wendet die Methoden die er beschreibt auf sich selbst an.
**Warum:** Meta-Credibility. Wenn der Report über Trust Calibration seine eigenen Claims nicht kalibrieren kann, warum sollte man ihm trauen?
**Format:**
- E/I/J/A Distribution (Zahlen + Bewertung: healthy/warning/red flag)
- CRT Cross-Check: Welche CRTs bestätigt/widersprochen?
- Consistency Check: 3-5 Key Claims rephrased, Agreement Rate
- AgentTrust Confidence Formula: Input-Werte + Berechnung
- Reviewer Rubric Score: X/16

**Qualitätsbar:** Self-Calibration ist durchgeführt, nicht nur beschrieben. Rubric ≥13/16 für Tier 2.
**Anti-Pattern:** "Self-calibration was applied" ohne Ergebnisse.

---

## Akzeptanzkriterien (Wann ist es FERTIG?)

### A+++ (McKinsey, €200K)
- [ ] Alle 12 Bausteine vorhanden
- [ ] 3 Tests bestanden (2-Minuten, Montag-Morgen, "Wusste ich nicht")
- [ ] Rubric ≥15/16
- [ ] E >50%, J <20%
- [ ] Custom Framework ist original (0 Google-Ergebnisse)
- [ ] Mindestens 1 Contradiction aufgedeckt
- [ ] Self-Calibration durchgeführt mit Ergebnissen
- [ ] Alle Case Studies verifizierbar
- [ ] Phased Plan startet Woche 1
- [ ] Beipackzettel vollständig (keine leeren Listen)

### A+ (Sehr gut, publishable)
- [ ] 10 von 12 Bausteinen vorhanden
- [ ] Rubric ≥13/16
- [ ] E >50%, J <20%
- [ ] Recommendations mit Timeline

### B (Akzeptabel, intern nutzbar)
- [ ] 8 von 12 Bausteinen
- [ ] Rubric ≥10/16
- [ ] Source Log vorhanden

### C (Überarbeiten)
- [ ] <8 Bausteine oder Rubric <10/16
- [ ] Zurück an Phase 3 (Synthesis) mit spezifischen Fix Requests
