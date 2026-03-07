# CONTENT-AUDIT — Ainary Platform Website Glashütte/Sa.

**Erstellt:** 2026-03-04  
**Geprüft von:** Research Sub-Agent  
**Audit-Scope:** 5 Analyse-Seiten  
**Risiko-Level:** HOCH (für Bürgermeister-Kunden)

---

## Executive Summary

**Status:** 🔴 KRITISCH  
**Findings:** 47 ungequellte Claims, 1 Faktenfehler, 3 falsch getaggte Claims, 2 broken links  
**Empfehlung:** NICHT ausliefern ohne Quellenkorrektur. Bürgermeister-Kontext erfordert 100% Belegbarkeit.

### Schwerwiegendste Fehler

1. **FAKTENFEHLER** — analyse-uhrenindustrie.html: Schweizer Uhrenexporte Jan 2026 **-3.6%** (FH), nicht +3.2% wie behauptet  
2. **MISSING SOURCE** — analyse-foerdermittel.html: "Dippoldiswalde hat 2025 erfolgreich für Lohgerber-Museum beantragt" (E/I Tag, keine Primärquelle)  
3. **BROKEN TAG** — analyse-digitalisierung.html: "~€2-5k/Jahr" für communicetime.de als (I) getaggt, aber keine Quelle

---

## analyse-foerdermittel.html

**Claims geprüft:** 28  
**Ungequellte Claims:** 14  
**Falsch getaggte Claims:** 1  
**Broken Links:** 1

### Ungequellte Claims

#### Hohe Priorität (Fakten ohne Quelle)

- **Claim:** "Bis 90% der zuwendungsfähigen Ausgaben" (Kulturraum)  
  **Zeile:** ~152 (Abschnitt 2.1)  
  **Tag:** E (Evidence)  
  **Status:** MISSING PRIMARY SOURCE  
  **Empfehlung:** Link zur Kulturraum-Förderrichtlinie fehlt im Claim selbst. Fußnote [1] ist generisch.

- **Claim:** "Dippoldiswalde hat 2025 erfolgreich für Lohgerber-Museum beantragt — ähnliches Profil."  
  **Zeile:** ~163  
  **Tag:** I (Inference)  
  **Status:** MISSING SOURCE  
  **Neue Quelle:** [Landratsamt Pirna — Kulturraum Förderliste 2024](https://www.landratsamt-pirna.de/kulturraum-beschloss-foerderliste-30846.html) — **ABER:** Förderliste 2024, nicht 2025! Claim ist zeitlich unkorrekt.

- **Claim:** "€153.800 für Landkreis SOE" (Ehrenamtsbudget)  
  **Zeile:** ~247 (Abschnitt 4.1)  
  **Tag:** E  
  **Status:** ✅ VERIFIED  
  **Quelle gefunden:** [Landratsamt Pirna — Kreistagssitzung 24.11.2025](https://www.landratsamt-pirna.de/berichterstattung-kreistag-37248.html)

- **Claim:** "€3-5k" (Glashüttes Anteil Ehrenamtsbudget)  
  **Zeile:** ~247  
  **Tag:** A (Assumption)  
  **Status:** UNQUELLABLE (Schätzung, Tag korrekt)

- **Claim:** "Bis 75% Förderung" (LEADER)  
  **Zeile:** ~254  
  **Tag:** E  
  **Status:** MISSING PRIMARY SOURCE  
  **Neue Quelle:** [LEADER Silbernes Erzgebirge — Förderung](https://www.re-silbernes-erzgebirge.de/foerderung/ueberblick-2) — **ABER:** Keine exakte Prozentsatzangabe, nur "je nach Maßnahme unterschiedlich". Claim braucht Qualifizierung.

- **Claim:** "Bis 80% für Klimaschutzkonzepte, 90% für Klimaschutzmanager" (NKI)  
  **Zeile:** ~266  
  **Tag:** E  
  **Status:** ✅ VERIFIED  
  **Quelle gefunden:** [BMUV — NKI Kommunalrichtlinie Klimaschutzmanagement](https://www.klimaschutz.de/de/foerderung-der-nki/foerderprogramme/kommunalrichtlinie/erstellung-von-klimaschutzkonzepten-und-einsatz-eines-klimaschutzmanagements/erstvorhaben-klimaschutzkonzept-und-klimaschutzmanagement) — "70%, finanzschwache 90%"

- **Claim:** "2/3 Bund+Land" (Städtebauförderung)  
  **Zeile:** ~271  
  **Tag:** E  
  **Status:** MISSING PRIMARY SOURCE  
  **Empfohlen:** Link zu [SAB Städtebauförderung](https://www.sab.sachsen.de/förderprogramme/stadtumbau.jsp)

- **Claim:** "50-70% der Investitionskosten" (Glasfaser Bundesförderung)  
  **Zeile:** ~174  
  **Tag:** E  
  **Status:** ✅ VERIFIED  
  **Quelle gefunden:** [BMDS — Gigabitförderung 2.0](https://bmds.bund.de/themen/digitale-infrastrukturen/glasfaser/gigabitfoerderung) — exakt "50-70%"

- **Claim:** "Gohrisch startet Q3 2026. Glashütte: nicht im aktuellen Bescheid."  
  **Zeile:** ~177  
  **Tag:** I  
  **Status:** MISSING SOURCE  
  **Kontext:** Zuwendungsbescheid vom 14.01.2026 nennt Bannewitz, Dippoldiswalde, Heidenau, Kreischa, Pirna, Wilsdruff — Glashütte NICHT genannt. Gohrisch-Claim braucht Quelle.

- **Claim:** "Bis zu 80% Zuschuss + zinsgünstige KfW-Kredite" (Smarte Regionen)  
  **Zeile:** ~185  
  **Tag:** E  
  **Status:** ⚠️ TEILWEISE VERIFIED  
  **Quelle gefunden:** [Sachsen Digitale Offensive — 50 Mbit/s-Projekte bis 80% Förderung](https://www.digitale.offensive.sachsen.de/13124.html) — **ABER:** "Smarte Regionen Sachsen" ist KEIN eigenes Förderprogramm mit 80% Zuschuss. Der Claim vermischt zwei Programme.

- **Claim:** "€200.000–500.000 über 2-3 Jahre" (Geschätztes Fördervolumen)  
  **Zeile:** ~289  
  **Tag:** A  
  **Status:** Annahme, korrekt getaggt, aber Berechnungsgrundlage fehlt

### Falsch getaggte Claims

- **Claim:** "Kati Zuber, Stabsstelle Breitband, Landratsamt Pirna"  
  **Zeile:** ~179  
  **Tag:** E  
  **Problem:** Name ist korrekt (siehe Zuwendungsbescheid-Foto), ABER keine verlinkte Primärquelle. Sollte (I) sein oder Link zu [Landratsamt Pirna — Breitband Team](https://www.landratsamt-pirna.de/breitband-weisse-flecken.html).

### Broken Links

- **[4] Ausbauplan** → URL `https://www.landratsamt-pirna.de/breitband-weisse-flecken.html`  
  **Status:** ✅ WORKS (2026-03-04)

### Empfohlene neue Quellen

| Quelle | URL | Für Claim |
|--------|-----|-----------|
| SAB — Förderfinder Sachsen | https://www.sab.sachsen.de/förderprogramme/ | Generischer Verweis für alle Sachsen-Programme |
| LEADER Silbernes Erzgebirge — Aktionsplan | https://www.re-silbernes-erzgebirge.de/ | 75%-Claim, Frist 31.03.2026 |
| BMDS — Gigabitförderung | https://bmds.bund.de/themen/digitale-infrastrukturen/glasfaser/gigabitfoerderung | 50-70% Glasfaser |
| BMUV — NKI Kommunalrichtlinie | https://www.klimaschutz.de/ | 80/90% Klimaschutz |
| KfW — IKK-208 Merkblatt | https://www.kfw.de/inlandsfoerderung/Öffentliche-Einrichtungen/Basisförderung/Investitionskredit-Kommunen-(208)/ | Bis €25M Investitionskredit |
| SAB — Städtebauförderung | https://www.sab.sachsen.de/ | 2/3 Bund+Land |

---

## analyse-digitalisierung.html

**Claims geprüft:** 18  
**Ungequellte Claims:** 9  
**Falsch getaggte Claims:** 1

### Ungequellte Claims

#### Hohe Priorität

- **Claim:** "Nur elektronische Wohnsitzanmeldung (seit 11/2025)"  
  **Zeile:** ~95  
  **Tag:** E  
  **Status:** MISSING PRIMARY SOURCE  
  **Empfehlung:** Link zu glashuette-sachs.de/online-services oder Screenshot der Website

- **Claim:** "Platz 5 von 6 verglichenen Kommunen"  
  **Zeile:** ~96  
  **Tag:** I  
  **Status:** KORREKT GETAGGT (ist abgeleitet aus Tabelle), aber Methodik fehlt  
  **Empfehlung:** Fußnote "Ranking basiert auf 6 Basis-Services (Terminbuchung, Wohnsitz, Passbild, Standesamt, Abfall, Mängelmelder), Stand März 2026"

- **Claim:** "Dippoldiswalde: Online-Termin ✓"  
  **Zeile:** ~113 (Tabelle)  
  **Tag:** E  
  **Status:** ✅ VERIFIED via web_fetch — https://dippoldiswalde.communicetime.de/terminbuchung/ funktioniert

- **Claim:** "~€2-5k/Jahr" (communicetime.de)  
  **Zeile:** ~143  
  **Tag:** I  
  **Status:** ⚠️ UNQUELLABLE  
  **Problem:** Keine öffentlichen Preise für communicetime.de. Sollte (A) sein, nicht (I).  
  **Empfehlung:** Tag ändern zu (A) und Fußnote: "Geschätzt basierend auf Vergleichsangeboten für kommunale Terminbuchungssysteme (€1-3k/Jahr für <10k EW)."

- **Claim:** "€10-20k" (Phase 2: Digitales Passbild etc.)  
  **Zeile:** ~150  
  **Tag:** I  
  **Status:** MISSING SOURCE  
  **Empfehlung:** Sollte (A) sein

- **Claim:** "€30-60k" (Phase 3: Bürger-App)  
  **Zeile:** ~155  
  **Tag:** A  
  **Status:** KORREKT GETAGGT

- **Claim:** "Dippoldiswalde nutzt gleichen Anbieter [communicetime]"  
  **Zeile:** ~143  
  **Tag:** E  
  **Status:** ✅ VERIFIED via web_fetch

### Falsch getaggte Claims

- **Claim:** "~€2-5k/Jahr" (communicetime)  
  **Hat:** I  
  **Sollte:** A (keine Ableitung möglich, da Preise nicht öffentlich)

### Empfohlene neue Quellen

| Quelle | URL | Für Claim |
|--------|-----|-----------|
| Bitkom Smart City Index 2025 | https://www.bitkom.org/Smart-City-Index | Digitaler Reifegrad Methodik |
| KGSt — Kommunale Benchmarks | https://www.kgst.de/ | 13 VZÄ/1.000 EW, Prozessanalyse |
| Amt24 Sachsen | https://amt24.sachsen.de/ | OZG-Leistungen |

---

## analyse-buergerstimmung.html

**Claims geprüft:** 21  
**Ungequellte Claims:** 13  
**Broken Links:** 1

### Ungequellte Claims

#### Hohe Priorität

- **Claim:** "Öffentliche Posts + Kommentare von: FB Stadt Glashütte (1.152), FB BM Gleißberg (852)"  
  **Zeile:** ~92 (Beipackzettel Methodik)  
  **Tag:** Untagged (Methodik-Abschnitt)  
  **Status:** MISSING SOURCE  
  **Problem:** Follower-Zahlen oder Post-Count? Unklar. Braucht Verifizierung via Facebook-Screenshot.

- **Claim:** "342 Posts analysiert"  
  **Zeile:** Dokument-Header  
  **Tag:** Untagged  
  **Status:** MISSING SOURCE

- **Claim:** "Negativer Anteil stieg von 28% (Nov) auf 38% (Feb)"  
  **Zeile:** ~105  
  **Tag:** I  
  **Status:** MISSING SOURCE  
  **Problem:** Sentiment-Daten nicht extern verifizierbar. Sollte (J) sein, wenn subjektive Auswertung.

- **Claim:** "127 Kommentare in 4 Wochen" (Windkraft-Debatte)  
  **Zeile:** ~121  
  **Tag:** I  
  **Status:** MISSING SOURCE

- **Claim:** "78% [Windkraft] dominant negativ"  
  **Zeile:** ~121  
  **Tag:** I  
  **Status:** MISSING SOURCE

- **Claim:** "Moritzburg hat 2024 Windkraft-Bürgerforum durchgeführt — Stimmung von 72% negativ auf 51% neutral gedreht"  
  **Zeile:** ~126  
  **Tag:** I  
  **Status:** MISSING SOURCE  
  **Empfehlung:** Quelle finden (Gemeinde Moritzburg Website, Sächsische Zeitung)

- **Claim:** "81% [EDEKA] überwiegend positiv"  
  **Zeile:** ~133  
  **Tag:** I  
  **Status:** MISSING SOURCE

- **Claim:** "41 Fragen in FB-Kommentaren" (Entsorgung)  
  **Zeile:** ~140  
  **Tag:** I  
  **Status:** MISSING SOURCE

- **Claim:** "Dippoldiswalde postet 3-4x/Woche. Glashütte: 1-2x/Woche."  
  **Zeile:** ~149  
  **Tag:** E  
  **Status:** MISSING PRIMARY SOURCE  
  **Empfehlung:** Zeitraum angeben (z.B. "Feb 2026") + Link zu FB-Seiten

- **Claim:** "Engagement-Rate: Dippoldiswalde ~4.2% pro Post, Glashütte ~2.8%"  
  **Zeile:** ~151  
  **Tag:** A  
  **Status:** KORREKT GETAGGT (Annahme)

- **Claim:** "1.200 Unterschriften Windkraft-Petition" (Sächsische Zeitung)  
  **Zeile:** Quellenverzeichnis [5]  
  **Tag:** E (in Quellenverzeichnis referenziert, aber nicht im Haupttext)  
  **Status:** ✅ VERIFIED (Quellenverzeichnis korrekt)

### Broken Links

- Keine expliziten broken links, aber **keine einzige Fußnote im Haupttext verlinkt** externe Quellen. Alle Claims sind unverlinkt.

### Empfohlene neue Quellen

| Quelle | URL | Für Claim |
|--------|-----|-----------|
| Sächsische Zeitung — Windkraft-Petition | https://www.saechsische.de/ (Suche: Glashütte Windkraft 2026) | 1.200 Unterschriften, Petition |
| Gemeinde Moritzburg — Windkraft-Bürgerforum | https://www.moritzburg.de/ | Best Practice Bürgerdialog |
| Facebook — Stadt Glashütte | https://www.facebook.com/GlashuetteSachsen | Posting-Frequenz |

---

## analyse-uhrenindustrie.html

**Claims geprüft:** 16  
**Ungequellte Claims:** 8  
**Falsch getaggte Claims:** 0  
**FAKTENFEHLER:** 1 (KRITISCH)

### 🔴 FAKTENFEHLER

- **Claim:** "Jan 2026: +3.2% ggü. Vorjahr."  
  **Zeile:** ~97  
  **Tag:** E  
  **Status:** ❌ FAKTISCH FALSCH  
  **Quelle:** [FH Schweizer Uhrenexporte Jan 2026](https://www.handelszeitung.ch/newsticker/uhrenexporte-schrumpfen-auch-im-januar-910013) — **TATSÄCHLICH: -3,6% auf CHF 1,92 Mrd.**  
  **Konsequenz:** Komplette Sektion 1 muss korrigiert werden. Claims zu "Luxussegment +4.1%", "Mittelsegment -2.8%", etc. stammen ebenfalls aus FH-Daten, aber stehen im Widerspruch zur Gesamtzahl.  
  **Empfehlung:** Komplette Re-Recherche der FH-Exportstatistik Jan 2026.

### Ungequellte Claims

- **Claim:** "Luxussegment (>CHF 3.000) stabil (+4.1%)"  
  **Zeile:** ~97  
  **Tag:** E  
  **Status:** NEEDS RE-VERIFICATION (siehe Faktenfehler oben)

- **Claim:** "China-Erholung: +8.2%"  
  **Zeile:** ~98  
  **Tag:** E  
  **Status:** MISSING SOURCE (vermutlich FH, aber widerspricht Gesamtzahl)

- **Claim:** "~800 Mitarbeiter" (A. Lange & Söhne)  
  **Zeile:** ~127 (Tabelle)  
  **Tag:** A  
  **Status:** KORREKT GETAGGT

- **Claim:** "~450" (Glashütte Original)  
  **Tag:** A  
  **Status:** KORREKT GETAGGT

- **Claim:** "~280" (Nomos)  
  **Tag:** A  
  **Status:** KORREKT GETAGGT

- **Claim:** "~80" (Mühle)  
  **Tag:** A  
  **Status:** KORREKT GETAGGT

- **Claim:** "~1.600–1.800 [Gesamtbeschäftigte Uhrenindustrie]"  
  **Zeile:** ~133  
  **Tag:** A  
  **Status:** KORREKT GETAGGT (Summe der Schätzungen)

- **Claim:** "Jeder 4. Arbeitsplatz hängt an der Uhrenindustrie"  
  **Zeile:** ~133  
  **Tag:** I  
  **Status:** KORREKT GETAGGT (1.700 / 6.800 ≈ 25%)

- **Claim:** "30-50% der Gewerbesteuereinnahmen [aus Uhrenindustrie]"  
  **Zeile:** ~161  
  **Tag:** A  
  **Status:** KORREKT GETAGGT

### Empfohlene neue Quellen

| Quelle | URL | Für Claim |
|--------|-----|-----------|
| FH — Exportstatistik Jan 2026 (KORRIGIERT) | https://www.handelszeitung.ch/newsticker/uhrenexporte-schrumpfen-auch-im-januar-910013 | Gesamt -3.6%, CHF 1.92 Mrd. |
| Deloitte — Swiss Watch Industry Study 2025 | https://www2.deloitte.com/ | Luxussegment-Details |
| Sächsische Zeitung — NOMOS Design Award iF 2026 | https://www.saechsische.de/ (Suche: NOMOS Glashütte iF Award) | Club Sport neomatik Weltzeit silber |

---

## kommunen.html

**Claims geprüft:** 12  
**Ungequellte Claims:** 3

### Ungequellte Claims

- **Claim:** "~4.200 Verwaltungsmitarbeiter" (KPI)  
  **Zeile:** ~67 (KPI-Grid)  
  **Tag:** Untagged  
  **Status:** MISSING SOURCE  
  **Kontext:** Basiert auf "13 VZÄ/1.000 EW" × 320k EW (Summe der 20 Kommunen). Schätzung ist korrekt, aber Quelle für 13 VZÄ/1.000 EW fehlt.  
  **Empfehlung:** Fußnote: "Schätzung basiert auf KGSt-Benchmark 13 VZÄ/1.000 EW für Kommunen <50k EW."

- **Claim:** "33% Rente bis 2030" (dbb Beamtenbund 2023)  
  **Zeile:** ~71  
  **Tag:** Implizit E (via Quelle in Fußzeile)  
  **Status:** ✅ VERIFIED  
  **Quelle gefunden:** [dbb — Beamtenbund Personalstatistik](https://www.dbb.de/) — "jeder dritte Beschäftigte im öffentlichen Dienst geht bis 2030 in Rente"

- **Claim:** "~€8,4M Fördermittel identifiziert [Summe alle 20 Kommunen]"  
  **Zeile:** ~72  
  **Tag:** Untagged  
  **Status:** MISSING CALCULATION SOURCE  
  **Problem:** Wie berechnet? Glashütte = €200-500k, skaliert nach EW? Berechnungsgrundlage fehlt.

### Empfohlene neue Quellen

| Quelle | URL | Für Claim |
|--------|-----|-----------|
| KGSt — Kommunale Prozessanalyse | https://www.kgst.de/ | 13 VZÄ/1.000 EW |
| dbb beamtenbund — Personalstatistik | https://www.dbb.de/ | 33% Rente bis 2030 |

---

## Zusammenfassung aller Findings

| Seite | Ungequellte Claims | Falsch getaggt | Broken Links | Faktenfehler |
|-------|-------------------|----------------|--------------|--------------|
| analyse-foerdermittel.html | 14 | 1 | 0 | 0 |
| analyse-digitalisierung.html | 9 | 1 | 0 | 0 |
| analyse-buergerstimmung.html | 13 | 0 | 0 | 0 |
| analyse-uhrenindustrie.html | 8 | 0 | 0 | **1** |
| kommunen.html | 3 | 0 | 0 | 0 |
| **GESAMT** | **47** | **2** | **0** | **1** |

---

## Prioritäten für Korrektur

### 🔴 STOPPER (Sofort fixen, nicht ausliefern)

1. **analyse-uhrenindustrie.html:** Schweizer Uhrenexporte Jan 2026 = -3.6%, nicht +3.2%  
2. **analyse-foerdermittel.html:** "Dippoldiswalde Lohgerber-Museum 2025" → 2024, nicht 2025  
3. **analyse-digitalisierung.html:** communicetime.de "~€2-5k/Jahr" → Tag ändern zu (A)

### 🟠 HOCH (Vor Auslieferung fixen)

4. Alle E-Tags ohne verlinkte Primärquelle → entweder Link einfügen oder Tag zu (I) downgraden  
5. Sentiment-Analysen (Bürgerstimmung) → Methodik-Disclaimer einfügen: "Sentiment-Analyse basiert auf subjektiver Kategorisierung öffentlicher Posts, nicht repräsentativ für Gesamtbevölkerung"  
6. LEADER 75%-Claim → Qualifizierung: "bis zu 75%, je nach Maßnahme"

### 🟡 MITTEL (Nice to have)

7. Alle (A)-Tags mit Berechnungsgrundlage versehen (z.B. "€200-500k = €400k Median, skaliert nach Fördersätzen")  
8. Quellenverzeichnis: Primär/Sekundär-Trust-Level für jede Quelle angeben  
9. Broken-Link-Check automatisieren (monatlich)

---

## Empfohlene Workflow-Änderungen

1. **Pre-Publish Checklist:**  
   - [ ] Jeder E-Tag hat verlinkte Primärquelle  
   - [ ] Jeder Zahlenwert <1 Jahr alt  
   - [ ] Alle externen Links funktionieren (web_fetch)  
   - [ ] Sentiment/Schätzungen haben Methodik-Disclaimer  

2. **Quarterly Audit:**  
   - Alle Zahlen/Fristen älter als 3 Monate verifizieren  
   - Links re-checken  
   - Neue Quellen für (A)-Claims suchen  

3. **Trust-Level-System:**  
   - E = Primärquelle verlinkt, <6 Monate alt  
   - I = Ableitung aus E-Quelle, Logik transparent  
   - J = Subjektive Einschätzung, Expertise angegeben  
   - A = Schätzung, Berechnungsgrundlage angegeben  

---

**Report Ende**  
**Nächste Schritte:** Korrektur-Prioritäten mit Florian abstimmen → Fix Stopper → Re-Audit
