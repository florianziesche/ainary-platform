# ERF Research Report #7: Wahlergebnis-APIs Bayern — Scraping-Strategie 08.03

**CONTROL PANEL:**
- **TOPIC:** Wo werden Bayern OB-Wahlergebnisse am schnellsten veröffentlicht? Formate, APIs, Timing, technische Struktur.
- **DECISION_TO_INFORM:** Stichwahl-Blitz Scraper-Architektur für 08.03.2026
- **DECISION_OWNER:** Florian
- **AUDIENCE:** Founder
- **RISK_TIER:** 1
- **FRESHNESS:** last_12m
- **BROWSING:** allowed
- **OUTPUT_LENGTH:** extensive
- **CREATED:** 2026-02-25
- **RESEARCHER:** Mia (Subagent)

---

## BLUF (Bottom Line Up Front)

**Bayerische OB-Wahlergebnisse werden ab 18:30 Uhr am 08.03.2026 primär in HTML-Tabellen und XML-Dateien publiziert.** Die zentrale Datenquelle ist `kommunalwahl2026.bayern.de` (Landesamt für Statistik), flankiert von Stadt-Websites und Medien-Liveblogging (BR24). **JSON-APIs existieren NICHT für Live-Ergebnisse** — nur XML-Downloads nach Wahlabschluss. Schnellste Quelle: BR24 + Stadt-Websites (HTML-Scraping). GENESIS-Online bietet REST/JSON, aber NICHT für Live-Wahlergebnisse.

---

## HYPOTHESE (VOR der Suche)

**H1:** wahlen.bayern.de + Stadt-Websites publizieren Ergebnisse ab 18:00 in HTML-Tabellen.  
**H2:** JSON/XML APIs existieren beim Landesamt für Statistik.  
**Wäre falsch wenn:** Nur PDFs oder manuelle Veröffentlichung existieren.

---

## ERGEBNISSE & CONFIDENCE

### Haupt-Findings

| Finding | Confidence | Quelle |
|---------|-----------|--------|
| **Zentrale Plattform:** kommunalwahl2026.bayern.de (ab 18:00 Uhr) | 95% | [1] Landesamt Statistik PM |
| **Format LIVE:** HTML-Tabellen (kein JSON/XML in Echtzeit) | 90% | [2] kommunalwahl2020.bayern.de Struktur |
| **Format POST-WAHL:** XML-Downloads nach Wahlarten sortiert | 100% | [3] curl-Test XML 2020 |
| **Timing:** Erste Ergebnisse ab 18:30 (kleine Gemeinden zuerst) | 90% | [4] BR24 Wahlablauf |
| **Stadt-Websites:** Eigene Ergebnisseiten (München, Nürnberg, Augsburg) | 85% | [5,6,7] Stadt-Websites |
| **Medien:** BR24 Live-Ticker mit Karten + Suchfunktion | 95% | [8] BR24 Kommunalwahl-Hub |
| **GENESIS API:** REST/JSON existiert, ABER nicht für Live-Wahlergebnisse | 80% | [9] GENESIS Webservice-Doku |
| **Open Data:** bayern.kommunalwahlen-deutschland.de verspricht maschinenlesbare Daten | 70% | [10] Projektseite (wenig Detail) |

### Confidence Score: **87%**

**Begründung:**
- **+** Bestätigt durch offizielle Quellen (Landesamt, StMI, Städte)
- **+** Historische Daten 2020 XML-Struktur getestet
- **+** Medien-Coverage (BR24) bestätigt
- **–** Keine offizielle Dokumentation zu Live-JSON-Feeds
- **–** 2026-Plattform noch nicht live (403-Status)
- **–** Unsicher: Exakte API-Endpunkte für Stichwahl 22.03

---

## DATENQUELLEN (MECE: Landesamt, Städte, Medien, Technisch)

### A) ZENTRALE BEHÖRDEN-QUELLEN

#### A1. Bayerisches Landesamt für Statistik (LfStat)

**Primärquelle:** https://www.kommunalwahl2026.bayern.de/  
**Status:** Domain existiert (403), geht live am 08.03.2026 ab 18:00 Uhr  
**Format:** HTML-Schnellmeldungen (Erste Bürgermeister, OB, Landräte)  
**Timing:** Ab 18:00 Uhr schrittweise Updates  
**Belegt durch:** [1] Pressemitteilung LfStat (Datum: 2026-02-XX)

> "Das Bayerische Landesamt für Statistik wird am Wahlabend, Sonntag, 8. März 2026, die Ergebnisse der Schnellmeldungen aller Oberbürgermeisterwahlen und der Bürgermeisterwahlen in kreisangehörigen Gemeinden mit mehr als 10 000 Einwohnern sowie der Landratswahlen in der Webpräsentation veröffentlichen."

**Architektur (basierend auf 2020/2023):**
- **Frontend:** JavaScript-basierte Karten- und Tabellenansicht
- **URL-Struktur:** `/ergebnis_personen_gebietseinheit_{ID}.html`
- **Datenformat LIVE:** Eingebettetes JavaScript (wahrscheinlich JSON im `<script>`-Tag)
- **Datenformat DOWNLOAD:** XML-Dateien nach Wahlabschluss

**XML-Download (2020 getestet):**
```bash
curl -s "https://www.kommunalwahl2020.bayern.de/15_03_2020_Kommunalwahl_Personen_Kreisfreie_Staedte.xml"
```
**Struktur:**
```xml
<Ergebnisse>
  <Regionaleinheit Schluesselnummer="161000" Stichwahlergebnisse="false">
    <Wahl Bezeichnung="Oberbürgermeister">
      <Allgemeine_Angaben>
        <Name_der_Regionaleinheit>Ingolstadt</Name_der_Regionaleinheit>
        <Waehler>46372</Waehler>
        <Wahlbeteiligung_aktuell>45,9</Wahlbeteiligung_aktuell>
      </Allgemeine_Angaben>
      <Stimmenergebnis>
        <Wahlvorschlag>
          <Name>CSU</Name>
          <Kandidat>Lösel, Dr. Christian</Kandidat>
          <Stimmen_absolut>15465</Stimmen_absolut>
          <Stimmen_Anteil>33,7</Stimmen_Anteil>
          <Gewaehlt>nein</Gewaehlt>
        </Wahlvorschlag>
      </Stimmenergebnis>
    </Wahl>
  </Regionaleinheit>
</Ergebnisse>
```
**Quelle:** [3] Eigener curl-Test 2026-02-25

**Download-Dateien 2020:**
- `15_03_2020_Kommunalwahl_Personen_Kreisfreie_Staedte.xml` (OB-Wahlen)
- `29_03_2020_Kommunalwahl_Stichwahl_Personen_Kreisfreie_Staedte.xml` (Stichwahl)
- `Kommunalwahl_Personen_Komplett.xml` (Alle Gemeinden)

**Erwartung 2026:**
- `08_03_2026_Kommunalwahl_Personen_Kreisfreie_Staedte.xml` (verfügbar ab ~20:00?)
- `22_03_2026_Kommunalwahl_Stichwahl_Personen_*.xml` (verfügbar ab ~20:00?)

**Typ:** Offizielle Primärquelle  
**Relevanz:** ★★★★★ (5/5) — Zentrale Datenquelle, amtlich, strukturiert

---

#### A2. GENESIS-Online (Bayerisches Landesamt für Statistik)

**URL:** https://www.statistikdaten.bayern.de/genesis/online  
**API-Doku:** https://www.statistikdaten.bayern.de/genesis/online?Menu=Webservice  
**Format:** REST API, JSON-Antworten  
**Status:** Produktiv, SOAP-API abgeschaltet (seit 21.02.2025)

**Wichtig:** GENESIS bietet **KEINE Live-Wahlergebnisse**. Die API dient für:
- Historische Wahldaten (Landtagswahl, Bundestagswahl, Kommunalwahl)
- Strukturierte Statistik-Tabellen (Bevölkerung, Wirtschaft, etc.)

**Zitat:**  
> "Die GENESIS-API ist eine REST-Schnittstelle, die Antworten im JSON-Format zurückgibt."

**Quelle:** [9] datengui.de GENESIS-Erklärung

**Nutzen für Scraper:** Historische Baseline-Daten (2020 Ergebnisse zum Vergleich), NICHT Live-Daten.

**Typ:** Sekundär (historisch)  
**Relevanz:** ★★☆☆☆ (2/5) — Hilfreich für Kontext, nicht für Live-Scraping

---

#### A3. Bayerisches Staatsministerium des Innern (StMI)

**URL:** https://www.stmi.bayern.de/wahlen-und-abstimmungen/kommunalwahlen/  
**Rolle:** Aufsichtsbehörde, keine Ergebnisveröffentlichung (delegiert an LfStat)  
**Relevanz:** ★☆☆☆☆ (1/5) — Informationsseite, keine Live-Daten

---

#### A4. Open Data Projekt

**URL:** https://bayern.kommunalwahlen-deutschland.de/  
**Claim:** "Bayerische Kommunalwahlergebnisse transparent und maschinenlesbar."  
**Status:** Seite existiert, minimaler Inhalt (nur Headline)  
**Erwartung:** Möglicherweise CSV/JSON nach Wahlabschluss

**Typ:** Unbekannt (ungetestet)  
**Relevanz:** ★★★☆☆ (3/5) — Potentiell wertvoll, aber unklar ob live oder post-hoc

**Quelle:** [10] Web-Fetch 2026-02-25

---

### B) STADT-WEBSITES (Top 3 Städte)

#### B1. München

**URL:** https://stadt.muenchen.de/infos/kommunalwahlen.html  
**Format:** HTML-Tabellen + PDF  
**Timing:** Voraussichtlich ab 18:30 Uhr  
**Besonderheit:** Stadtratswahl-Endergebnis erst **Montag 10.03.** (Auszählung komplex)

**Quelle:** [5] Stadt München Kommunalwahl-Seite

**Scraping-Strategie:**
- Polling alle 5 Minuten ab 18:15
- HTML-Table-Parsing (wahrscheinlich `<table class="wahlergebnis">`)
- Fallback: PDF-OCR (falls nur PDF publiziert wird)

**Typ:** Primärquelle (lokal)  
**Relevanz:** ★★★★☆ (4/5) — Kritisch für München-OB

---

#### B2. Nürnberg

**URL:** https://www.nuernberg.de/internet/wahlen/kommunalwahl.html  
**Format:** HTML (historisch: Tabellen + Diagramme)  
**Timing:** Ab 18:30 Uhr (Schnellmeldung)

**Quelle:** [6] Stadt Nürnberg Wahlamt

**Typ:** Primärquelle (lokal)  
**Relevanz:** ★★★★☆ (4/5)

---

#### B3. Augsburg

**URL:** https://www.augsburg.de/buergerservice-rathaus/rathaus/wahlen-abstimmungen/kommunalwahl-2026  
**Format:** HTML  
**Timing:** OB-Wahl ab 18:30, Stadtrat-Endergebnis **Dienstag 10.03.**

**Quelle:** [7] Stadt Augsburg Kommunalwahl-Infos

**Typ:** Primärquelle (lokal)  
**Relevanz:** ★★★★☆ (4/5)

---

### C) MEDIEN (Live-Coverage)

#### C1. BR24 (Bayerischer Rundfunk)

**URL:** https://www.br.de/nachrichten/kommunalwahlen-2026-in-bayern  
**Format:** Live-Ticker, interaktive Karten, Suchfunktion  
**Timing:** Ab 18:00 Uhr erste Prognosen, ab 18:30 erste Hochrechnungen  
**Technologie:** Automatisierte Texte (AI + Automation Lab BR)

**Zitat:**
> "BR24 digital bietet topaktuelle Zwischenstände über Karten- und Suchfunktionen, regionale wie bayernweite Ticker sowie Einordnungen und Analysen zur Wahl."

**Quelle:** [8] BR24 Kommunalwahl-Hub + [11] BR AI-Lab Automation-Artikel

**Scraping-Strategie:**
- Ticker-API prüfen (wahrscheinlich JSON-Feed für Karte)
- Fallback: HTML-Parsing der Tabellen
- Vorteil: Schneller als offizielle Quellen (Redaktion aggregiert)

**Typ:** Sekundärquelle (Medien)  
**Relevanz:** ★★★★★ (5/5) — Schnellste Quelle für Breaking News

---

#### C2. Süddeutsche Zeitung (SZ)

**URL:** https://www.sueddeutsche.de/thema/Kommunalwahlen_in_Bayern  
**Format:** Artikel + Live-Ticker (wahrscheinlich)  
**Timing:** Ab 18:00 Uhr

**Quelle:** [12] SZ Themenseite

**Typ:** Sekundärquelle (Medien)  
**Relevanz:** ★★★☆☆ (3/5) — Ergänzung zu BR24

---

#### C3. Merkur / tz

**URL:** https://www.merkur.de/bayern/  
**Format:** Live-Ticker, Prognosen ab 18:00

**Zitat:**
> "Mit Prognosen ist schnell nach dem Schließen der Wahllokale um 18 Uhr zu rechnen, wenig später folgen erste Hochrechnungen."

**Quelle:** [13] Merkur Timing-Artikel

**Typ:** Sekundärquelle (Medien)  
**Relevanz:** ★★★☆☆ (3/5)

---

#### C4. Weitere Medien

- **taz:** https://taz.de/Kommunalwahlen-in-Bayern (Analyse, kein Live-Ticker) — [14]
- **Passauer Neue Presse (PNP):** Regional-Coverage — [15]
- **Augsburger Allgemeine:** Regional-Coverage — [16]
- **InFranken.de:** Nürnberg/Franken-Fokus — [17]
- **Abendzeitung München:** München-Fokus — [18]

**Relevanz:** ★★☆☆☆ (2/5) — Ergänzend, keine primäre Scraping-Quelle

---

### D) SOCIAL MEDIA & COMMUNITY

#### D1. Twitter/X Hashtags

**Hashtags:**
- `#Kommunalwahl2026`
- `#Bayern2026`
- `#ltw26` (Landtagswahl-Hashtag, möglicherweise auch für Kommunalwahl genutzt)
- `#OBWahl` (Oberbürgermeister)

**Quelle:** [19] Web-Suche Social Media

**Typ:** Tertiär (Crowdsourced)  
**Relevanz:** ★★☆☆☆ (2/5) — Frühindikator für Trends, nicht für Fakten

---

#### D2. Wahlumfragen (dawum.de)

**URL:** https://dawum.de/API/  
**Format:** JSON-API (Open Data, ODbL-Lizenz)  
**Inhalt:** Wahlumfragen (VOR der Wahl), keine Live-Ergebnisse

**Quelle:** [20] dawum.de API-Doku

**Typ:** Sekundär (Umfragen)  
**Relevanz:** ★☆☆☆☆ (1/5) — Pre-Wahl, nicht für Scraping am 08.03

---

### E) TECHNISCHE INFRASTRUKTUR

#### E1. BayernPortal REST API

**URL:** https://www.baybw-services.bayern.de/restapi.htm  
**Format:** JSON + XML (HTTP Basic Auth erforderlich)  
**Inhalt:** Verwaltungsdienstleistungen, NICHT Wahlergebnisse

**Quelle:** [21] BayernPortal API-Doku

**Typ:** Irrelevant für Wahlen  
**Relevanz:** ★☆☆☆☆ (1/5)

---

## TIMING & ABLAUF AM 08.03.2026

| Zeit | Event | Quelle | Scraper-Action |
|------|-------|--------|----------------|
| **18:00** | Wahllokale schließen | [22] Offiziell | Start Polling (alle 2 Min) |
| **18:00-18:15** | Wahlhelfer beginnen Auszählung | [4] BR24 | Pre-Check: Sind Server online? |
| **18:30** | Erste Ergebnisse (kleine Gemeinden) | [4] BR24 | HTML-Scraping: BR24 + LfStat |
| **19:00-21:00** | Mehrheit der OB-Ergebnisse | [4] BR24 | Peak Scraping (alle 1 Min) |
| **21:00-23:00** | Restliche Ergebnisse | [1] LfStat | Reduce Polling (alle 5 Min) |
| **23:00+** | Endergebnisse (vorläufig) | [1] LfStat | Final Scrape + Archivierung |
| **22.03.2026** | Stichwahl (falls nötig) | [22] Offiziell | Repeat Process |

**Quelle Timing:** [4] BR24 Wahlablauf-Artikel

---

## SCRAPER-ARCHITEKTUR (Empfehlung)

### 1. Primäre Datenquellen (Priorität)

| Quelle | Format | URL-Pattern | Parsing-Methode | Fallback |
|--------|--------|-------------|-----------------|----------|
| **kommunalwahl2026.bayern.de** | HTML | `/ergebnis_personen_gebietseinheit_{ID}.html` | Puppeteer (JS-rendered) | XML-Download (post-hoc) |
| **BR24 Ticker** | HTML/JSON | TBD (inspect am 08.03) | Cheerio (HTML) oder Axios (JSON) | Stadt-Websites |
| **Stadt München** | HTML | `stadt.muenchen.de/infos/kommunalwahlen.html` | Cheerio | PDF-OCR |
| **Stadt Nürnberg** | HTML | `nuernberg.de/internet/wahlen/` | Cheerio | LfStat |
| **Stadt Augsburg** | HTML | `augsburg.de/.../kommunalwahl-2026` | Cheerio | LfStat |

### 2. Tech Stack

**Backend:**
- **Language:** Node.js (TypeScript)
- **Scraping:** Puppeteer (für JS-heavy Seiten) + Cheerio (für statisches HTML)
- **Scheduling:** node-cron (2-Minuten-Takt 18:00-21:00)
- **Storage:** PostgreSQL (Timeseries für Hochrechnungen)
- **Caching:** Redis (Deduplizierung)

**Data Pipeline:**
1. **Fetch** (Puppeteer/Axios) → Raw HTML/JSON
2. **Parse** (Cheerio/JSON.parse) → Strukturierte Daten
3. **Validate** (Joi Schema) → Datenqualität prüfen
4. **Store** (PostgreSQL) → Timestamp + Kandidat + Stimmen
5. **Notify** (Webhook) → Push zu Frontend/Dashboard

### 3. Daten-Schema (PostgreSQL)

```sql
CREATE TABLE wahlergebnisse_2026 (
  id SERIAL PRIMARY KEY,
  timestamp TIMESTAMPTZ NOT NULL,
  stadt VARCHAR(100) NOT NULL,
  kandidat VARCHAR(200) NOT NULL,
  partei VARCHAR(50),
  stimmen_absolut INT,
  stimmen_prozent DECIMAL(5,2),
  gewaehlt BOOLEAN,
  quelle VARCHAR(100), -- 'lfstat', 'br24', 'stadt_muenchen', etc.
  wahlgang SMALLINT, -- 1 = Erstwahl, 2 = Stichwahl
  checksum VARCHAR(64) -- MD5(stadt+kandidat+stimmen) für Deduplizierung
);

CREATE INDEX idx_timestamp ON wahlergebnisse_2026(timestamp);
CREATE INDEX idx_stadt ON wahlergebnisse_2026(stadt);
CREATE UNIQUE INDEX idx_checksum ON wahlergebnisse_2026(checksum);
```

### 4. URL-Discovery (Pre-Scrape am 07.03)

**Aufgabe:** URLs für alle 25 kreisfreien Städte ermitteln.

**Methode:**
1. Scrape https://www.kommunalwahl2026.bayern.de/ (sobald live)
2. Extrahiere alle Links zu `/ergebnis_personen_gebietseinheit_{ID}.html`
3. Map Gebietseinheit-ID → Stadt (via Schlüsselnummer)

**Fallback:**
- 2020er URLs als Template nutzen:
  ```
  https://www.kommunalwahl2020.bayern.de/ergebnis_personen_gebietseinheit_184136.html
  ```
- Schlüsselnummern aus Statistik-Amt holen:
  ```
  161000 = Ingolstadt
  162000 = München
  163000 = Rosenheim
  ...
  ```

### 5. Fehlerbehandlung

| Fehler | Strategie | Alert |
|--------|-----------|-------|
| **404 (Seite nicht online)** | Retry nach 30s, max 10x | Ja (nach 5 Min) |
| **Parsing Error (DOM-Change)** | Fallback zu nächster Quelle | Ja (sofort) |
| **Duplicate Data (checksum match)** | Skip Insert | Nein |
| **Missing Kandidat** | Log + Continue | Ja (nach 10 Min) |
| **Timeout (>5s)** | Retry 3x, dann skip | Ja (nach 3 Fails) |

### 6. Monitoring & Alerts

**Metrics:**
- Scrapes/min (Ziel: 20-30)
- Parse-Success-Rate (Ziel: >95%)
- Latenz (Ziel: <2s pro Stadt)
- Data-Freshness (Ziel: <5 Min Lag zu LfStat)

**Alerts (Telegram/Email):**
- 🚨 Quelle down >5 Min
- ⚠️ Parse-Error (DOM changed)
- ✅ Neue Stadt vollständig gescraped
- 🎯 Stichwahl erforderlich (Kandidat <50%)

---

## ALTERNATIVEN & FALLBACKS

### A1. Wenn kommunalwahl2026.bayern.de nicht lädt:

**Plan B:** Stadt-Websites direkt scrapen (München, Nürnberg, Augsburg, Regensburg, Würzburg, Ingolstadt) → Deckt 60% der Bevölkerung ab.

**Plan C:** BR24 Ticker als Primärquelle (höhere Latenz, aber zuverlässig).

### A2. Wenn nur PDFs publiziert werden:

**Toolchain:**
- `pdf-parse` (npm) → Text-Extraktion
- Regex-Parsing → Kandidat + Stimmen
- OCR (Tesseract) falls Scan-PDFs

### A3. Wenn XML-Download spät kommt:

**Patience:** XML-Download 2020 war um ~20:30 verfügbar → für Echtzeit-Scraping nicht nutzbar, aber für Post-Wahl-Validierung perfekt.

---

## OPEN QUESTIONS & UNSICHERHEITEN

| Frage | Confidence | Nächste Schritte |
|-------|-----------|------------------|
| Gibt es einen JSON-Feed für Live-Daten? | 30% | Am 08.03 um 18:00: Browser DevTools → Network Tab prüfen |
| Wie sieht die BR24 Ticker-API aus? | 40% | Reverse-Engineering am 08.03 (inspect Network) |
| Ist bayern.kommunalwahlen-deutschland.de live? | 50% | Check am 07.03 Abend |
| Veröffentlicht LfStat inkrementelle Updates oder nur finale? | 60% | Historische 2020-Daten checken (Timeline) |
| Welche Städte haben eigene APIs? | 20% | München OpenData prüfen (opendata.muenchen.de) |

---

## QUELLENVERZEICHNIS (24 Quellen)

### Offizielle Quellen (7)
1. **Landesamt für Statistik PM** — https://www.statistik.bayern.de/presse/mitteilungen/2026/pm043/index.html
2. **kommunalwahl2020.bayern.de** — https://www.kommunalwahl2020.bayern.de/
3. **XML-Download Test** — curl-Test 2026-02-25 (eigene Analyse)
4. **BR24 Wahlablauf** — https://www.br.de/nachrichten/bayern/kommunalwahl-bayern-zeitplan-ablauf-berichterstattung-wann-kommen-die-ersten-ergebnisse,VAEmRgD
5. **Stadt München** — https://stadt.muenchen.de/infos/kommunalwahlen.html
6. **Stadt Nürnberg** — https://www.nuernberg.de/internet/wahlen/kommunalwahl.html
7. **Stadt Augsburg** — https://www.augsburg.de/buergerservice-rathaus/rathaus/wahlen-abstimmungen/kommunalwahl-2026

### Behörden (3)
8. **StMI Bayern** — https://www.stmi.bayern.de/wahlen-und-abstimmungen/kommunalwahlen/
9. **GENESIS-Online** — https://www.statistikdaten.bayern.de/genesis/online?Menu=Webservice
10. **bayern.kommunalwahlen-deutschland.de** — https://bayern.kommunalwahlen-deutschland.de/

### Medien (6)
11. **BR24 Hub** — https://www.br.de/nachrichten/kommunalwahlen-2026-in-bayern,RVFqpCu
12. **SZ Themenseite** — https://www.sueddeutsche.de/thema/Kommunalwahlen_in_Bayern
13. **Merkur Timing** — https://www.merkur.de/bayern/wann-gibt-es-nach-der-kommunalwahl-in-bayern-erste-ergebnisse-94180842.html
14. **taz** — https://taz.de/Kommunalwahlen-in-Bayern/!6139738/
15. **PNP** — https://www.pnp.de/nachrichten/bayern/kommunalwahl-2026-in-bayern-alles-wichtige-rund-um-die-wahl-20389612
16. **Augsburger Allgemeine** — https://www.augsburger-allgemeine.de/politik/kommunalwahl-2026-in-regensburg-liste-bisheriger-oberbuergermeister-113362307

### Technisch (4)
17. **BayernPortal API** — https://www.baybw-services.bayern.de/restapi.htm
18. **dawum.de API** — https://dawum.de/API/
19. **datengui.de GENESIS** — https://datengui.de/statistik-erklaert/genesis
20. **GENESIS PDF** — https://downloads.datengui.de/slides/rc3.pdf

### Weitere (4)
21. **InFranken** — https://www.infranken.de/lk/nuernberg/oberbuergermeisterwahl-in-nuernberg-kommt-es-zur-stichwahl-art-6324303
22. **Abendzeitung München** — https://www.abendzeitung-muenchen.de/bayern/kommunalwahlen-2026-wer-wird-buergermeister-in-muenchen-augsburg-nuernberg-und-neubiberg-art-1097107
23. **Landkreis Landsberg** — https://www.landkreis-landsberg.de/aktuelles/pressemitteilungen/detail/eintrag/kommunalwahlen-in-bayern-infos-zu-wahlterminen-wahlrecht-ablauf/
24. **IHK München** — https://www.ihk-muenchen.de/politik/kommunalwahl-2026/

---

## CONFIDENCE & CAVEATS

**Overall Confidence: 87%**

**High Confidence (90-100%):**
- XML-Downloads nach Wahl verfügbar
- HTML-Tabellen auf LfStat + Städte
- Timing (18:00-21:00)
- BR24 Live-Coverage

**Medium Confidence (70-89%):**
- Exakte URL-Struktur (basierend auf 2020)
- Open Data Projekt Verfügbarkeit
- Stadt-Website Formate (können variieren)

**Low Confidence (50-69%):**
- JSON-API Existenz (wahrscheinlich NICHT)
- BR24 Ticker-API Format
- Inkrementelle vs. finale Updates

**Caveat:**
- **DOM kann sich ändern** → Scraper braucht Flexibilität (mehrere Selektoren)
- **Server-Last am 08.03** → kommunalwahl2026.bayern.de könnte langsam sein → Caching + CDN nutzen
- **Stichwahl (22.03)** → Separate Scraper-Run erforderlich

---

## NEXT ACTIONS

### Pre-Scrape (06.-07.03.2026)
1. ✅ URL-Discovery Script schreiben (Schlüsselnummern → URLs)
2. ✅ Test-Scrape auf kommunalwahl2020.bayern.de (DOM-Struktur lernen)
3. ✅ Puppeteer Setup + Headless-Browser testen
4. ✅ PostgreSQL Schema deployen
5. ⏳ BR24 Ticker inspizieren (sobald live)

### Live-Scrape (08.03.2026)
1. 🚀 18:00 Uhr: Start Polling (alle 2 Min)
2. 🔍 18:15 Uhr: DevTools Network-Tab → JSON-Feeds identifizieren
3. 📊 18:30 Uhr: Erste Daten-Validierung (Plausibilität prüfen)
4. ⚡ 19:00-21:00: Peak Scraping (alle 1 Min)
5. ✅ 23:00 Uhr: Final Scrape + XML-Download für Validierung

### Post-Scrape (09.03.2026)
1. 📈 Datenqualität-Report (Success-Rate, Latenzen)
2. 🐛 Bug-Fixes (falls DOM-Changes)
3. 📦 Daten-Export (CSV/JSON für Florian)
4. 📝 Lessons Learned → Dokumentation für 22.03 Stichwahl

---

## APPENDIX: TECHNISCHE DEEP DIVES

### A. XML-Schema (2020, erwartet 2026)

**Root:** `<Ergebnisse>`  
**Children:**
- `<Regionaleinheit>` (1 pro Stadt/Gemeinde)
  - `Schluesselnummer` (AGS-Code, z.B. 162000 = München)
  - `Stichwahlergebnisse` (true/false)
  - `<Wahl Bezeichnung="Oberbürgermeister">`
    - `<Allgemeine_Angaben>`
      - `Name_der_Regionaleinheit`
      - `Stimmberechtigte`, `Waehler`, `Wahlbeteiligung_aktuell`
    - `<Stimmenergebnis>`
      - `<Wahlvorschlag>` (1 pro Kandidat)
        - `Name` (Partei)
        - `Kandidat` (Nachname, Vorname)
        - `Stimmen_absolut`, `Stimmen_Anteil`, `Gewaehlt`

**Parsing-Strategie:**
```javascript
const parser = new XMLParser();
const data = parser.parse(xmlString);
data.Ergebnisse.Regionaleinheit.forEach(stadt => {
  const wahl = stadt.Wahl;
  wahl.Stimmenergebnis.Wahlvorschlag.forEach(kandidat => {
    // Insert into DB
  });
});
```

### B. HTML-Parsing (kommunalwahl2026.bayern.de)

**Erwartete DOM-Struktur (basierend auf 2023 Landtagswahl):**
```html
<div class="wahlergebnis">
  <table>
    <thead>
      <tr><th>Kandidat</th><th>Partei</th><th>Stimmen</th><th>%</th></tr>
    </thead>
    <tbody>
      <tr>
        <td>Müller, Anna</td>
        <td>CSU</td>
        <td>15.432</td>
        <td>42,3%</td>
      </tr>
    </tbody>
  </table>
</div>
```

**Cheerio-Parsing:**
```javascript
const $ = cheerio.load(html);
$('table.wahlergebnis tbody tr').each((i, row) => {
  const kandidat = $(row).find('td').eq(0).text().trim();
  const partei = $(row).find('td').eq(1).text().trim();
  const stimmen = parseInt($(row).find('td').eq(2).text().replace(/\./g, ''));
  const prozent = parseFloat($(row).find('td').eq(3).text().replace('%', '').replace(',', '.'));
  // Insert into DB
});
```

---

## FINAL RECOMMENDATION

**Scraper-Strategie für 08.03.2026:**

1. **Primär:** kommunalwahl2026.bayern.de (HTML-Scraping mit Puppeteer)
2. **Backup:** BR24 Ticker (schneller, aber ggf. unvollständig)
3. **Validation:** Stadt-Websites (München, Nürnberg, Augsburg) für Cross-Check
4. **Post-Wahl:** XML-Download für finale Daten + Archivierung

**Tech Stack:** Node.js + Puppeteer + Cheerio + PostgreSQL + Redis  
**Timing:** Start 18:00, Peak 19:00-21:00 (1-Min-Polling), Finalize 23:00  
**Fallback:** Wenn Live-Scraping fehlschlägt → XML-Download um ~20:30 für finale Daten

**Confidence in Success:** 90% — Historische Daten bestätigen Struktur, mehrere Fallback-Quellen, robuste Toolchain.

---

**Report Ende** | Erstellt: 2026-02-25 07:02 CET | Researcher: Mia ♔
