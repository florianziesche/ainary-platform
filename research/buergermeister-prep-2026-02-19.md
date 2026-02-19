# Bürgermeister Glashütte — Meeting Prep Checklist
**Meeting:** Montag, 23.02.2026, 11:30 Uhr, Rathaus Glashütte  
**Teilnehmer:** Sven Gleißberg (Bürgermeister) + Florian Ziesche  
**Ziel:** Pilot-Projekt €15-30K für AI-gestützte Verwaltungsdigitalisierung pitchen

---

## ✅ TECHNISCHE VORBEREITUNG

### Demo-Datei
**Gefunden:** `/Users/florianziesche/.openclaw/workspace/projects/workbench/demos/glashuette.html`

**Inhalt:**
- **Executive Board Dashboard** mit KPIs (OZG-Umsetzung 3/58, 1 Online-Service, Ø12min Bearbeitungszeit)
- **4 Stages:** Analyse → Umsetzung → Kommunikation → Ergebnis
- **Findings:** 15 Analyse, 9 Umsetzung, 5 Kommunikation, 8 Ergebnis (37 total)
- **Live Features:**
  - Stadtrat-Übersicht (AfD 5, CDU 4, WVs 8, Grüne 1)
  - 16 Ortsteile Stimmungsmonitor
  - Bürgerstimmung 62% positiv / 23% neutral / 15% negativ
  - 10 laufende AI Tasks (Zeitungstracker, Fördermittel-Scanner, Sentimentanalyse)
  - Agent Trust Scores (RESEARCHER 74, OPERATOR 55, HUNTER 45, WRITER 40, DEALMAKER 30)

**Art:** HTML Dashboard (statisch, kein Backend) — zeigt WIE es aussehen würde, nicht live-connected.

---

### Checkliste: Technik & Demo

- [ ] **Laptop VOLLSTÄNDIG geladen** (nicht nur 80% — Meeting kann länger dauern)
- [ ] **Offline-Kopie der Demo** auf Desktop (Backup falls WLAN ausfällt)
- [ ] **Browser-Tab vorbereitet:** `file:///Users/florianziesche/.openclaw/workspace/projects/workbench/demos/glashuette.html` vorher öffnen
- [ ] **Alle Links/Buttons im Dashboard getestet:**
  - [ ] Executive Board → Stage Views (Analyse, Umsetzung, Kommunikation, Ergebnis) funktionieren?
  - [ ] Context Panel öffnet sich?
  - [ ] Findings sind klickbar und Details erscheinen?
  - [ ] Tab-Wechsel Bürgermeister ↔ Agents & Tasks geht?
- [ ] **Screenshot-Backup:** 3-4 Screenshots vom Dashboard in Keynote/PDF falls Browser crasht
- [ ] **Presenter Mode:** Bildschirmauflösung testen (falls Beamer) — Dashboard ist responsive?
- [ ] **Scrolling:** Lange Listen (Findings, Tasks) sind scrollbar ohne Bug?

---

## 📋 INHALTLICHE VORBEREITUNG

### Ziel des Meetings (aus memory/daily/2026-02-19.md)
**Phase 1:** Analyse & Konzept (1-2 Wochen)  
**Phase 2:** Pilotbetrieb (4-6 Wochen) — **EMPFOHLEN**  
**Phase 3:** Laufende Optimierung

**Florians Pitch-Strategie (aus glashuette-pilot-analyse.md):**
1. Einstieg: "Sie sind 'Der Kommunikator' — wie stehen Sie zur Digitalisierung?"
2. Problem: Sachsen-Digimeter (15 Jahre!), Dippoldiswalde hat Online-Terminbuchung, Glashütte nicht
3. Lösung: 3-Phasen-Modell, Quick Win in 4 Wochen
4. Förderung: EFRE bis 60%
5. Next Step: 2-Wochen-Sprint für Phase 1

**Killer-Argument:**  
> "Dippoldiswalde hat Online-Terminbuchung. Glashütte — weltweit bekannt für Präzision — sollte digital nicht hinterherhinken."

---

### Checkliste: Inhalt & Argumentation

- [ ] **3 Maßnahmen auswendig:**
  1. Quick Wins (Online-Termin + 10 Formulare) — €5-8K, 4-6 Wochen
  2. AI Bürger-Auskunft — €8-15K, 6-8 Wochen
  3. OZG Prozessautomatisierung — €15-25K, 3-4 Monate
- [ ] **Förderung:** EFRE Digitalisierung Zuschuss bis 60%, max €10K (Heranführung) — Quelle: SAB Sachsen
- [ ] **Vergleichszahlen parat:**
  - Sachsen: 15 Jahre bis OZG-Vollständigkeit (Digimeter 2025)
  - 75% Bürger befürworten KI in Behörden (eGovernment MONITOR 2024)
  - 37% der Kommunen setzen KI ein oder planen es (Civey 2025)
- [ ] **Was zeigen wir im Dashboard?** (Reihenfolge festlegen)
  1. Executive Board KPIs (zeigt IST-Zustand = Problem)
  2. Stadtrat + Ortsteile (zeigt: "Wir verstehen Ihre Komplexität")
  3. Laufende Tasks (zeigt: "So sieht der Pilot aus")
  4. Stage: Umsetzung (zeigt: "Das sind die konkreten Maßnahmen")
- [ ] **Fragen vorbereiten:**
  - "Welche Fachverfahren nutzen Sie?" (Prosoz, VOIS, HSH?)
  - "Nutzen Sie Amt24 oder sächsischen Portalverbund?"
  - "Wie groß ist Ihre IT-Abteilung?"
  - "Gibt es Druck vom Stadtrat zur Digitalisierung?"
- [ ] **Einwand-Handling:**
  - "Datenschutz?" → On-Premise oder EU-gehostete LLMs, kein US-Cloud
  - "Zu teuer?" → Phasenmodell, Stop nach Quick Wins möglich (€5K Risiko)
  - "Bürger sind zu alt für digitale Services?" → 75% Zustimmung bundesweit, Quick Wins helfen JETZT (Verwaltungsentlastung)

---

## 🎯 MEETING-ABLAUF (30 Min)

| Zeit | Phase | Key Points |
|------|-------|------------|
| 0-5 min | Small Talk + Einstieg | Uhrenstadt-Kompliment, "Der Kommunikator"-Zitat, Transition zu Digitalisierung |
| 5-10 min | Problem | Sachsen-Digimeter (15 Jahre!), Dippoldiswalde-Vergleich, OZG 3/58 |
| 10-20 min | **Demo** | Dashboard zeigen (siehe Reihenfolge oben), 2-3 konkrete Beispiele durchklicken |
| 20-25 min | Lösung + Förderung | 3-Phasen-Modell, EFRE 60%, Risiko nur €5K bei Abbruch nach Phase 1 |
| 25-30 min | Next Step | Angebot über €18K mit Phasen-Gates, 2-Wochen-Sprint Start |

---

## ⚠️ BACKUP-PLAN: Internet ausfällt

- [ ] **Offline-Demo auf Laptop** (siehe oben — HTML-Datei lokal)
- [ ] **PDF-Export:** Dashboard als PDF vorher exportieren (Print to PDF im Browser)
- [ ] **Keynote/Powerpoint Backup:** 5 Slides mit Screenshots falls alles crasht
  1. Problem (OZG-Zahlen)
  2. Dashboard Executive Board
  3. Laufende Tasks
  4. 3-Phasen-Modell
  5. Förderung + Next Step
- [ ] **Handy-Hotspot aktivierbar** falls WLAN tot, LTE als Fallback

---

## 📞 NACHBEREITUNG

- [ ] **Follow-up Email innerhalb 24h:** Zusammenfassung, Angebot anhängen
- [ ] **Angebot vorbereiten:** €18K aufgeteilt in 3 Phasen mit Milestones
- [ ] **Fördermittel-Antrag:** EFRE Digitalisierung Zuschuss recherchieren (wer beantragt? Kommune oder Dienstleister?)
- [ ] **Lessons Learned:** Was hat funktioniert? Was war unklar? → memory/daily/2026-02-23.md

---

## 🔥 CONFIDENCE CHECK

**Vor dem Meeting fragen:**
1. Kann ich die 3 Maßnahmen in 30 Sekunden erklären? (Ja/Nein)
2. Weiß ich was im Dashboard klickbar ist? (Ja/Nein)
3. Habe ich Backup falls Internet ausfällt? (Ja/Nein)
4. Kenne ich die Top 3 Einwände + Antworten? (Ja/Nein)
5. Ist das Ziel klar? (Pilot-Go, nicht Vollauftrag) (Ja/Nein)

**Alle 5 = Ja → READY. Sonst nochmal diese Checkliste durchgehen.**

---

**Erstellt:** 2026-02-19, 04:54 CET  
**Quelle:** glashuette.html Demo + glashuette-pilot-analyse.md + memory/daily/2026-02-19.md  
**Status:** READY — Laptop laden + Demo testen = letzter Schritt
