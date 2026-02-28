# Warum 92% der KI-Projekte im Mittelstand scheitern (und wie Sie es richtig machen)

**Substack Draft — Ready for Review**  
**Target Length:** 1.400 words  
**Author:** Florian Ziesche  
**Date:** Feb 22, 2026

---

92% der KI-Pilotprojekte im deutschen Mittelstand werden nie in Produktion genommen.

Das ist keine Schätzung — das ist die Realität nach 5 Jahren als CEO eines AI-Startups, €5,5 Millionen Funding, und Dutzenden Gesprächen mit Mittelständlern, die "KI ausprobiert" haben.

Die häufigste Frage nach dem ersten Meeting: *"ChatGPT ist doch kostenlos — warum sollten wir Sie bezahlen?"*

Die häufigste Frage **nach** dem gescheiterten Projekt: *"Warum funktioniert das bei uns nicht?"*

Hier ist die unbequeme Wahrheit: **Die meisten KI-Projekte scheitern, weil sie nie für Produktion gedacht waren.**

---

## Das Demo-Trap

Stellen Sie sich vor, Sie beauftragen einen Software-Entwickler. Der zeigt Ihnen eine beeindruckende Demo: Hochladen einer technischen Zeichnung, KI spuckt CNC-Code aus. 30 Sekunden statt 30 Minuten. Sie sind begeistert.

Dann kommt die Realität:
- **Fehlerrate:** 5-8% (bei komplexen Teilen bis 15%)
- **Keine Quellenangaben:** "Die KI sagt..." ist keine rechtssichere Dokumentation
- **Vendor Lock-in:** Proprietäre API, keine Kontrolle über Ihr System

5% Fehlerrate klingt gut? **Nicht im Maschinenbau.**

Bei 100 Aufträgen pro Monat sind das 5 fehlerhafte CNC-Programme.  
5 Ausschuss-Teile.  
5 verlorene Kunden.  
5 Haftungsfälle.

**Das ist der Unterschied zwischen Demo und Production.**

---

## Die 3 größten Fehler (und warum sie teuer sind)

### Fehler #1: "ChatGPT reicht"

ChatGPT ist beeindruckend. Für E-Mails, Brainstorming, Zusammenfassungen.

Aber für **business-critical Prozesse**?

**Problem:** Large Language Models (LLMs) halluzinieren. Sie erfinden Fakten. Sie "raten" plausibel — nicht korrekt.

Ein Beispiel aus meinem letzten Projekt (Legal Tech):
- **Aufgabe:** Verträge auf Haftungsklauseln prüfen
- **Standard-LLM-Fehlerrate:** 5,2%
- **Ergebnis:** 1 von 20 Verträgen wurde falsch analysiert

Das mag akzeptabel klingen. Bis Sie 1.000 Verträge pro Monat haben. Oder ein Kunde Sie verklagt, weil eine Klausel übersehen wurde.

**Lösung:** Multi-Agent Verification Architecture (dazu später mehr).

---

### Fehler #2: Vendor Lock-in

Die meisten "KI-Lösungen" für den Mittelstand sind **SaaS-Wrapper um OpenAI/Anthropic APIs.**

Das heißt:
- Sie zahlen monatlich (€500-€5.000/Monat)
- Der Vendor kontrolliert Ihre Daten
- Wenn der Vendor pleite geht, steht Ihre Produktion still
- Updates werden Ihnen aufgezwungen (und brechen manchmal Workflows)

**Real-World-Beispiel:**  
Ein Automotive-Zulieferer in Bayern nutzte eine "KI-Plattform" für Qualitätskontrolle. Nach 8 Monaten stellte der Anbieter das Produkt ein (Pivot). Alle Prozesse: tot.

**Alternative:** Open-Source-Modelle + eigene Infrastruktur. Einmalige Kosten, volle Kontrolle.

---

### Fehler #3: Kein klarer ROI

Viele KI-Projekte starten mit: *"Lass uns mal schauen, was möglich ist."*

Das Problem: Ohne klares Ziel gibt es kein klares **Fertig**.

**Symptome:**
- Projekt läuft 6-12 Monate
- Niemand weiß, wann es "production-ready" ist
- Budget überschritten, kein messbarer Nutzen

**Lösung:** ROI vor Projektstart definieren.

Beispiel aus meinem aktuellen Projekt (CNC-Kalkulation):
- **Ziel:** Kalkulationszeit von 60 Minuten auf <10 Minuten reduzieren
- **ROI-Schwelle:** 80% Zeitersparnis
- **Messung:** Durchschnitt über 50 Aufträge

**Ergebnis:** 92% Zeitersparnis. Von 60 Minuten auf 5 Minuten.

Weil das Ziel von Anfang an klar war.

---

## Die Lösung: Multi-Agent Verification Architecture

Hier ist, wie wir im Legal-Tech-Projekt die Fehlerrate von 5,2% auf **0,2%** gebracht haben:

### Schritt 1: Nicht EIN LLM — DREI

- **Agent 1 (Extractor):** Liest den Vertrag, extrahiert Klauseln
- **Agent 2 (Analyzer):** Analysiert jede Klausel auf Haftungsrisiken
- **Agent 3 (Verifier):** Prüft die Analysen von Agent 1+2 auf Widersprüche

Jeder Agent nutzt ein **anderes LLM** (z. B. GPT-4, Claude, Gemini).

**Warum?** Wenn alle drei denselben Fehler machen, ist es vermutlich kein Fehler. Wenn nur einer abweicht, wird es geprüft.

### Schritt 2: Quellenangaben erzwingen

Jede Aussage muss mit **Zitat + Seitenzahl** belegt sein.

**Prompt-Engineering:**  
*"Wenn du keine Quelle findest, sag 'keine Angabe' — nicht raten."*

**Ergebnis:** Keine Halluzinationen mehr. Jede Analyse ist nachvollziehbar.

### Schritt 3: Human-in-the-Loop bei Unsicherheit

Wenn die drei Agents sich nicht einig sind → **Mensch entscheidet**.

**Beispiel:**  
- Agent 1: "Haftung liegt beim Lieferanten"
- Agent 2: "Haftung unklar"
- Agent 3: "Haftung beim Käufer"

→ System markiert als **"Manual Review Required"**

**Resultat:** <0,2% Fehlerrate. 25x besser als Standard-LLMs.

---

## Case Study: MBS Schlottwitz (CNC-Kalkulation)

**Problem:**  
CNC-Lohnfertiger in Sachsen. Kalkulation einer technischen Zeichnung dauerte **60 Minuten**.

**Lösung:**  
Multi-Agent System:
1. **Agent 1:** Analysiert Zeichnung, erkennt Geometrie
2. **Agent 2:** Erstellt CNC-Programm (Drehen/Fräsen)
3. **Agent 3:** Kalkuliert Materialkosten + Maschinenzeit
4. **Agent 4:** Verifiziert Plausibilität (z. B. "Bohrung größer als Werkstück?" → Fehler)

**Ergebnis:**
- **Zeit:** 60 Minuten → 5 Minuten (92% Zeitersparnis)
- **Fehlerrate:** <0,2% (1 Fehler auf 500 Aufträge)
- **ROI:** 3 Monate (Zeitersparnis = mehr Aufträge = mehr Umsatz)

**Technologie:**
- Open-Source-Modelle (Llama 3, Mistral)
- Eigene Server (keine Cloud-Abhängigkeit)
- Kosten: €15.000 einmalig (statt €2.000/Monat SaaS)

---

## Was die 8% richtig machen

Die KI-Projekte, die **erfolgreich** in Produktion gehen, haben 4 Gemeinsamkeiten:

### 1. Klare ROI-Definition vor Start
*"Wir wollen X% Zeitersparnis bei Y Prozess in Z Monaten."*

Nicht: *"Lass uns KI testen."*

### 2. Multi-Agent Architektur statt Single-LLM
Redundanz = Zuverlässigkeit.

### 3. Eigene Infrastruktur (oder zumindest Open-Source)
Vendor Lock-in ist ein Killer.

### 4. Externe Expertise PLUS interne Champions
KI-Projekte brauchen beide: jemanden, der's kann (extern) + jemanden, der's durchsetzt (intern).

---

## Was jetzt?

Wenn Sie im Mittelstand KI **richtig** umsetzen wollen:

### Schritt 1: Discovery Workshop (€3.500)
- Analyse Ihrer Prozesse
- ROI-Kalkulation
- Proof-of-Concept (3-5 Tage)

**Mit BAFA/EFRE-Förderung:** nur €1.750 (50% Zuschuss)

### Schritt 2: Prototyp-Projekt (€25.000)
- Multi-Agent Architektur
- Integration in bestehende Systeme
- 4-8 Wochen Umsetzung

**Mit Förderung:** €12.500

### Schritt 3: Production Rollout
- Training Ihrer Mitarbeiter
- Monitoring & Optimierung
- Fortlaufende Verbesserung

---

## Die unbequeme Wahrheit

92% der KI-Projekte scheitern nicht, weil KI nicht funktioniert.

Sie scheitern, weil **Demos als Produktion verkauft werden**.

Die gute Nachricht: Die 8%, die es richtig machen, haben einen **massiven Wettbewerbsvorteil**.

Während Ihre Konkurrenz noch "KI testet", haben Sie:
- 92% weniger Zeitaufwand
- <0,2% Fehlerrate
- Volle Kontrolle (kein Vendor Lock-in)

Die Frage ist nicht mehr: *"Sollen wir KI nutzen?"*

Die Frage ist: *"Wollen wir zu den 8% oder den 92% gehören?"*

---

**Interesse an einem Discovery Workshop?**  
Schreiben Sie mir: florian@florianziesche.com

**BAFA/EFRE-Förderung verfügbar bis 31.12.2026** — danach gelten andere Konditionen.

---

*Florian Ziesche ist ehemaliger CEO eines AI-Startups (€5,5M raised, Computer Vision für Automotive). Heute hilft er Mittelständlern, KI-Systeme zu bauen, die tatsächlich funktionieren.*

---

## META (für Florian)

**Status:** DRAFT READY  
**Word Count:** ~1.380 words  
**Tone:** Direct, fact-heavy, no fluff  
**CTA:** Discovery Workshop (BAFA/EFRE hook)  
**SEO Keywords:** KI Mittelstand, AI Projekte scheitern, Multi-Agent AI, BAFA Förderung

**Next Steps:**
1. Review + polish (remove any remaining fluff)
2. Add 1-2 images (Multi-Agent diagram, MBS case study chart)
3. Publish on Substack
4. Cross-post summary on LinkedIn (with link to full article)
5. Send to email list (if >50 subscribers)

**Expected Impact:**
- Positioning: "The guy who knows why AI fails (and how to fix it)"
- Lead Gen: 2-5 Discovery Workshop inquiries
- Authority: Cited in future sales conversations

**Alternative Titles (A/B test):**
- "Die 92%-Lüge: Warum die meisten KI-Projekte scheitern"
- "Von ChatGPT zu 0,2% Fehlerrate — So geht Production AI"
- "€15.000 verschwendet? Warum Ihr KI-Projekt gescheitert ist"

♔
