# Research Report #10: Kommunale Daten als Moat — Wer besitzt Deutschlands Gemeinde-Daten?
*Mia ♔ | 2026-02-23 | [INTERN]*

---

## THE ANSWER
Kommunale Daten in Deutschland sind **öffentlich zugänglich aber fragmentiert** — verteilt über 50+ Quellen, verschiedene Formate, verschiedene Update-Zyklen. Der Moat liegt NICHT in den Daten selbst (die kann jeder scrapen), sondern in der **Aggregation, Strukturierung und Verknüpfung**. Wer als Erster eine proprietäre, strukturierte Datenbank aller bayerischen Kandidaten + Beziehungen + Positionen + Voting-History aufbaut, hat einen 12-18 Monate Vorsprung. Das ist unser Moat.

## CONFIDENCE: Likely (82%)

---

## KEY EVIDENCE

### 1. Öffentliche Datenquellen für Kommunalpolitik
| Quelle | Daten | Format | API? | Qualität |
|--------|-------|--------|------|----------|
| **GENESIS-Online** (Destatis) | Bevölkerung, Finanzen, Wirtschaft per Gemeinde | CSV, JSON | ✅ REST API | 🟢 Hoch |
| **Regionaldatenbank Deutschland** | Tief gegliederte Statistik per Gemeinde | CSV | ✅ API | 🟢 Hoch |
| **GovData.de** | 100K+ Datensätze aller Verwaltungsebenen | Diverse | ✅ CKAN API | 🟡 Unstrukturiert |
| **Bayerisches Landesamt für Statistik** | Wahlstatistiken, Kandidatenlisten | PDF, Excel | ❌ Manual | 🟢 Hoch |
| **Kommunale Websites** | BM-Profile, Gemeinderats-Zusammensetzung | HTML | ❌ Scraping | 🟡 Inkonsistent |
| **Handelsregister** | Firmenbeteiligungen von Kandidaten | PDF | 🟡 €4,50/Auszug | 🟢 Hoch |
| **Parteien-Websites** | Kandidatenlisten, Wahlprogramme | HTML/PDF | ❌ Scraping | 🟡 Variable |
| **Lokalpresse** | Artikel über Kandidaten | HTML (Paywall) | ❌ | 🟢 Inhaltlich stark |
| **Wikipedia** | Gemeinde-Artikel, Bürgermeister-Listen | API | ✅ | 🟡 Lückenhaft für <20K EW |

### 2. Was NICHT öffentlich ist (= wahrer Moat)
| Daten | Warum wertvoll | Quelle |
|-------|---------------|--------|
| **Beziehungsnetzwerke** zwischen Kandidaten | Koalitionspotential, Feindschaften | Eigene Analyse aus Presse + Sozialen Medien |
| **Voting-History** im Gemeinderat | Zuverlässigkeit, Konsens-Fähigkeit | Ratsprotokolle (öffentlich aber nie aggregiert) |
| **Wahlkampf-Finanzierung** auf Kommunalebene | Wer finanziert wen? | Rechenschaftsberichte (oft nicht digital) |
| **Historische Koalitionen** | Welche Bündnisse funktionieren? | Eigene Recherche |
| **Sentiment-Scores** pro Kandidat | Medienbild über Zeit | Eigene NLP-Analyse auf Lokalpresse |

### 3. Moat-Strategie
```
Phase 1 (jetzt, 0-10 Kunden):
  → Manuell pro Gemeinde. Qualität > Quantität.
  → Jede Analyse wird zur Datenbank-Eintragung.
  → Strukturiertes JSON (SCHEMA.md) = proprietär.

Phase 2 (10-50 Kunden):
  → Automatisierte Sammlung (Report #3 Pipeline).
  → Ratsprotokolle systematisch scrapen + NER.
  → Beziehungsgraph als Knowledge Graph.

Phase 3 (50+ Kunden):
  → Proprietäre Datenbank = Produkt.
  → API-Zugang für Wahlkampf-Agenturen.
  → Historische Daten = Zeitvorteil.
```

### 4. Defensive Moat-Bewertung
| Moat-Typ | Stärke | Wachstum über Zeit |
|----------|--------|-------------------|
| **Daten-Aggregation** | 🟡 Mittel (reproduzierbar) | 📈 Wächst mit jedem Kunden |
| **Beziehungs-Graph** | 🟢 Stark (schwer zu kopieren) | 📈 Exponentiell (Netzwerkeffekt) |
| **Historische Tiefe** | 🟢 Stark (nicht nachholbar) | 📈 Wächst linear pro Wahlzyklus |
| **Struktur + Schema** | 🟡 Mittel (kopierbar) | → Stagniert nach 1x Design |
| **E/I/J/A Bewertung** | 🟢 Stark (human intelligence) | 📈 Wächst mit Erfahrung |
| **Lokales Wissen** | 🟢 Stark (domain expertise) | 📈 Compound |

### 5. Technische APIs für automatisierte Sammlung
- **GENESIS API**: `https://www-genesis.destatis.de/genesisWS/rest/` — Bevölkerung, Finanzen per Gemeindeschlüssel
- **GovData CKAN API**: `https://www.govdata.de/ckan/api/3/` — Suche nach Datensätzen
- **Wikipedia API**: `https://de.wikipedia.org/w/api.php` — Gemeinde-Infos, Personen
- **Bayerisches Landesamt**: Keine API, aber strukturierte PDFs für Wahlergebnisse

---

## STRATEGIC RECOMMENDATION
**Jede Analyse die wir bauen ist ein Moat-Baustein.** Das heißt:
1. **SCHEMA.md streng einhalten** — jede Analyse in gleichem JSON-Format → aggregierbar
2. **Beziehungen explizit speichern** — jede Kandidat→Organisation→Person Verbindung = Kante im Graph
3. **Ratsprotokolle sammeln** — wenn wir eine Gemeinde analysieren, Ratsprotokolle der letzten 2 Jahre mitnehmen
4. **Nichts wegwerfen** — Rohdaten archivieren, nicht nur Endprodukt

**Der Moat entsteht nicht durch ein einmaliges Projekt. Er entsteht durch JEDE einzelne Analyse die wir verkaufen.** Consulting mit Daten-Rückfluss = Platform.

---

## SOURCES
```
[A1] GENESIS-Online Datenbank → www-genesis.destatis.de
[A1] GovData — Datenportal für Deutschland → govdata.de
[A1] Statistikportal.de Open Data → statistikportal.de/de/open-data
[A1] Destatis Open Data / API → destatis.de/EN/Service/OpenData/
[A2] Bayerisches Landesamt für Statistik Kommunalwahlen → statistik.bayern.de/wahlen/kommunalwahlen/
```

---

*Report 10/10 complete. ♔*
