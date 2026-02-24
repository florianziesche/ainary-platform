# PRODUCT-SPEC.md — Dossier Platform Specification
## Verbindliche Produkt-Spezifikation für jedes UI-Element

**Version:** 1.0
**Erstellt:** 2026-02-24
**Autor:** Mia ♔
**Prinzip:** Palantir Foundry Ontology — jedes Element hat Object Type, Properties, Links, Actions.
**Regel:** Keine Code-Änderung ohne Referenz auf diese Spec. Kein Deploy ohne Test gegen diese Spec.

---

## Architektur-Überblick

```
┌─────────────────────────────────────────────────────┐
│  DATENQUELLEN                                        │
│  web_search · Scraper · Google Trends · YouTube API  │
│  Instagram · Pressearchiv · Ratsinformationssystem   │
└──────────────────┬──────────────────────────────────┘
                   │ Erhebung (manuell/Cron)
                   ▼
┌─────────────────────────────────────────────────────┐
│  CITY JSON  (data/cities/{city}.json)                │
│  Canonical data source. Schema = diese Spec.         │
│  Validierung: validate_city.py + test_dossier.js     │
└──────────────────┬──────────────────────────────────┘
                   │ fetch() beim Laden
                   ▼
┌─────────────────────────────────────────────────────┐
│  normalizeCity()                                     │
│  Defaults setzen. Schema-Drift abfangen.             │
│  EINE Stelle, ALLE Defaults.                         │
└──────────────────┬──────────────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────────────┐
│  RENDERING (dossier.html)                            │
│  Liest NUR normalisierte Daten.                      │
│  Darf NIEMALS auf undefined zugreifen.               │
│  Zeigt IMMER: Daten → Interpretation → Aktion.       │
└─────────────────────────────────────────────────────┘
```

### Palantir-Prinzipien die wir anwenden:
1. **Ontology = Single Source of Truth.** City JSON ist die Ontologie.
2. **Object → Property → Link → Action.** Jede Entity hat Properties, Links zu anderen Entities, und empfohlene Actions.
3. **Every data point tells a story.** Kein Datenpunkt ohne "So What". Zahl allein = wertlos.
4. **Closed-loop operations.** Insight → Action → Ergebnis → neuer Insight.

### Rendering-Regel (NICHT VERHANDELBAR):
Jede Sektion zeigt DREI Ebenen:
- **DATEN:** Was ist der Fakt? (Zahl, Name, Datum)
- **INTERPRETATION:** Was bedeutet das? ("So What")
- **AKTION:** Was sollte der Nutzer tun? ("Jetzt handeln")

### Icon-Regel (NICHT VERHANDELBAR):
- KEINE Apple-Emojis (⚠️, 📊, etc.) — werden als □ auf Windows/Android angezeigt
- NUR CSS-basierte Icons: farbige Punkte, SVG, oder Text-Badges
- Evidence-Tags: `<span class="ev ev-j">J</span>` (existierendes System)

---

## §1 BRIEFING TAB

Der Briefing-Tab ist die Startseite. Ein Wahlkampfmanager öffnet das morgens und weiß in 30 Sekunden: Was ist los? Was muss ich heute tun?

---

### §1.1 Weekly Brief Header

**Was sieht der User:**
Begrüßung + Zusammenfassung der Woche in 2-3 Sätzen. Anzahl Tage bis zur Wahl. Top-Prioritäten.

**Warum:**
Orientierung. Der User weiß sofort: Wo stehen wir? Was ist dringend?

**Palantir-Äquivalent:** Dashboard Header mit Alert-Count + Mission-Status.

**JSON-Pfad:** `weekly_brief`
```json
{
  "title": "Lage-Briefing Bamberg — KW 9/2026",
  "date": "24.02.2026",
  "daysToElection": 12,
  "summary": "12 Tage vor der Wahl: Dreikampf...",
  "priorities": [
    {"text": "Huml-Pressekonferenz am Mittwoch beobachten", "urgency": "HOCH"},
    {"text": "Glüsenkamp Social-Media-Push analysieren", "urgency": "MITTEL"}
  ],
  "watchItems": [
    {"text": "Google Trends Huml: +127% in 7 Tagen", "type": "SIGNAL"},
    {"text": "Noch keine TV-Debatte terminiert", "type": "LÜCKE"}
  ]
}
```

**Datenquelle:** Manuell zusammengestellt aus allen anderen Sektionen. Wird wöchentlich aktualisiert.

**Update-Mechanismus:**
1. Cron-Agent liest NEWS, SOCIAL, FORECAST, PATTERNS
2. Generiert 2-3 Sätze Summary + Top-3 Prioritäten
3. Schreibt in `weekly_brief` im City JSON

**Qualitätskriterium:**
- `summary`: Min. 50 Zeichen, max. 300 Zeichen
- `priorities`: Min. 2 Items, jedes mit `text` + `urgency` (HOCH/MITTEL/NIEDRIG)
- `watchItems`: Min. 1 Item
- `daysToElection`: Berechnet aus `tenant.wahl` — darf NICHT hardcoded sein
- `date`: Muss aktuell sein (max. 7 Tage alt)

**Test:**
```
✓ weekly_brief.summary.length >= 50
✓ weekly_brief.priorities.length >= 2
✓ Jede priority hat text + urgency
✓ weekly_brief.watchItems.length >= 1
✓ Kein "undefined" im gerenderten HTML
✓ daysToElection === Differenz(tenant.wahl, heute)
```

**Rendering-Regel:**
- Greeting: "Guten [Morgen/Tag/Abend], [USER.name]" — NICHT "Herr Besucher"
- Wenn `priorities` leer → zeige "Keine Prioritäten diese Woche" (NICHT "0 Prioritäten")
- daysToElection prominent mit Farbcodierung: >14 grün, 7-14 amber, <7 rot

---

### §1.2 KPI-Leiste (Stat Cards)

**Was sieht der User:**
5 Karten in einer Reihe: Dossiers | Meldungen | Akteure | Kontroversen | Hypothesen

**Warum:**
Sofort-Überblick über den Datenbestand. "Wie viel wissen wir?"

**Palantir-Äquivalent:** KPI Tiles in Foundry Dashboard.

**JSON-Pfad:** Berechnet aus `kb`, `news`, `graph`, `hypotheses`, `actions`
```
Dossiers:      Object.keys(KB).length
Meldungen:     NEWS.length
Akteure:       GRAPH.nodes.length + " | " + GRAPH.links.length + " Verbindungen"
Kontroversen:  Σ KB[k].controversies.length + Σ KB[k].contradictions.length
Hypothesen:    HYPOTHESES.length
```

**Datenquelle:** Computed aus bestehenden Sektionen. Keine eigene Datenerhebung.

**Update-Mechanismus:** Automatisch bei JSON-Update (keine separate Pflege).

**Qualitätskriterium:**
- Jeder Wert > 0 (wenn 0: "—" anzeigen, nicht "0")
- Delta-Text zeigt Kontext, nicht nur Zahl
- Klickbar → führt zum relevanten Tab

**Test:**
```
✓ Alle 5 Cards rendern
✓ Kein Wert ist "undefined" oder "NaN"
✓ Jede Card hat onclick-Handler
```

---

### §1.3 Aktive Alerts

**Was sieht der User:**
Rote/Amber Alert-Boxen mit Priorität und kurzer Beschreibung. Nur bei Alerts.

**Warum:**
Dringende Entwicklungen die sofort Aufmerksamkeit brauchen.

**Palantir-Äquivalent:** Alert Panel / Notification Center.

**JSON-Pfad:** `tenant.alerts`
```json
[
  {
    "title": "Masken-Affäre: neue Dokumente aufgetaucht",
    "meta": "BR24, 20.02.2026",
    "priority": "KRITISCH",
    "entity": "huml"
  }
]
```

**Datenquelle:** Manuell kuratiert + automatisch aus NEWS mit `impact === 'HOCH'`.

**Update-Mechanismus:**
1. Bei jedem News-Update: Prüfe ob `impact === 'HOCH'` → auto-alert generieren
2. Manuell: Alerts hinzufügen/entfernen im JSON

**Qualitätskriterium:**
- Jeder Alert hat `title`, `meta`, `priority`
- `priority`: KRITISCH | HOCH | MITTEL
- Nicht mehr als 5 aktive Alerts (sonst verliert es Wirkung)
- Alerts die >14 Tage alt sind → archivieren

**Test:**
```
✓ Wenn alerts.length > 0: Alert-Box sichtbar
✓ Wenn alerts.length === 0: Sektion nicht angezeigt (kein leerer Container)
✓ Jeder Alert zeigt Titel + Meta
✓ Farbcodierung: KRITISCH=rot, HOCH=amber, MITTEL=blau
```

---

### §1.4 Jetzt Relevant (Entity Cards)

**Was sieht der User:**
3-4 Karten der wichtigsten Kandidaten/Akteure mit Name, Partei, Summary-Satz, Risk-Score.

**Warum:**
Schnellzugriff auf die Key Players. "Wer sind die Hauptfiguren?"

**Palantir-Äquivalent:** Object Cards in Foundry Workshop.

**JSON-Pfad:** `kb` — sortiert nach `risk` (höchstes Risiko zuerst)

**Datenquelle:** KB-Entities werden bei Stadtrecherche erstellt.

**Update-Mechanismus:** Bei Enrichment-Runs werden Properties, Risk, Sources aktualisiert.

**Qualitätskriterium:**
- Min. 3 Entities pro Stadt
- Jede Entity hat: `name`, `party`, `role`, `summary` (≥50 Zeichen), `risk` (0-100)
- Summary darf NICHT abgeschnitten werden ("..." ist VERBOTEN)
  → Entweder vollständiger Satz ODER max. 120 Zeichen mit sauberem Ende
- Color muss gesetzt sein (CSS Variable, kein Hex)

**Test:**
```
✓ Min. 3 Entity-Cards gerendert
✓ Kein Summary enthält "..."
✓ Kein Summary enthält "undefined"
✓ Jede Card zeigt Name + Partei + Summary
✓ Klick öffnet Entity-Detail
```

**Rendering-Regel:**
- Summary: Wenn > 120 Zeichen → am letzten Satzende vor 120 abschneiden
- Risk-Score: Farbcodiert (>50 rot, 25-50 amber, <25 grün)
- Kein Evidence-Tag nötig (es sind Überblicks-Cards)

---

### §1.5 Wahlprognose

**Was sieht der User:**
Horizontale Balken für jeden Kandidaten (Min-Max Range mit zentralem Wert).
Stichwahl-Wahrscheinlichkeit. Treiber. Historische Vergleiche.

**Warum:**
DIE Kernfrage: Wer gewinnt? Wie wahrscheinlich ist eine Stichwahl?

**Palantir-Äquivalent:** Prediction Model Output mit Confidence Intervals.

**JSON-Pfad:** `forecast`
```json
{
  "wahltermin": "08.03.2026",
  "stichwahl": "22.03.2026",
  "stichwahlConf": 60,
  "stichwahlRange": {"min": 70, "max": 95, "label": "Stichwahl wahrscheinlich"},
  "kandidaten": [
    {"id": "huml", "name": "Huml", "partei": "CSU", "min": 28, "max": 38, "zentral": 33, "conf": 65, "tag": "A"}
  ],
  "historie": [
    {"jahr": "2020", "wg": "1", "gewinner": "Starke (SPD)", "wb": "52,3%", "anmerkung": "Corona-Wahl"}
  ],
  "treiber": {
    "fuer_stichwahl": ["8 Kandidaten splitten Stimmen", "..."],
    "gegen_stichwahl": ["Huml hat CSU-Apparat"],
    "stichwahlSzenario": "Stichwahl Huml vs. Glüsenkamp"
  },
  "keyfactors": ["Mobilisierung junger Wähler", "..."],
  "title": "OB-Wahl Bamberg 2026 — Prognose",
  "method": "Strukturelle Analyse + historische Muster",
  "confidence": 60,
  "gaps": "Keine Umfragedaten verfügbar..."
}
```

**Datenquelle:**
- Historische Wahlergebnisse: Wikipedia, Wahlarchiv
- Strukturdaten: Bayerisches Landesamt für Statistik
- Kandidaten-Stärke: Pressearchiv + Social Media Analyse
- KEINE Umfragen verfügbar → Confidence max. 65%

**Update-Mechanismus:**
1. Einmalig: Historische Daten + Strukturanalyse
2. Wöchentlich: Treiber-Faktoren aktualisieren basierend auf News
3. Post-Wahl: Echtergebnis eintragen, Prognose-Güte bewerten

**Qualitätskriterium:**
- `kandidaten`: Min. 2, jeder mit `min`, `max`, `zentral`, `name`, `partei`
- `min` < `zentral` < `max`
- `stichwahlConf`: 0-100, NICHT hardcoded auf 50
- `historie`: Min. 1 historischer Wahlgang
- `keyfactors`: Min. 2
- `method` + `gaps`: Transparent machen was wir NICHT wissen

**Test:**
```
✓ Min. 2 Kandidaten-Balken gerendert
✓ Kein "undefined%" oder "NaN%"
✓ Stichwahl-Wahrscheinlichkeit sichtbar mit Prozentwert
✓ Min. 1 historischer Vergleich
✓ Methode + Gaps sichtbar (Transparenz)
```

**Rendering-Regel:**
- Balken: Farbig nach Partei (CSU=blau, Grüne=grün, SPD=rot, AfD=dunkelrot)
- Confidence-Tag: `<span class="ev ev-{tag}">{tag}</span>` vor jedem Wert
- Gaps prominent zeigen (nicht verstecken) — Transparenz = Vertrauen
- INTERPRETATION: Unter den Balken ein Satz: "Huml führt, aber Stichwahl zu 85% wahrscheinlich wegen Stimmen-Splitting"

---

### §1.6 Aktuelle Lage (News Feed)

**Was sieht der User:**
Chronologische Liste der wichtigsten Meldungen mit Sentiment-Farbe, Quelle, Datum.

**Warum:**
"Was ist in den letzten 7 Tagen passiert?"

**Palantir-Äquivalent:** Event Timeline / Intelligence Feed.

**JSON-Pfad:** `news`
```json
[
  {
    "title": "Huml präsentiert 10-Punkte-Plan für Bamberg",
    "source": "Fränkischer Tag",
    "date": "2026-02-20",
    "body": "Melanie Huml hat ihren 10-Punkte-Plan vorgestellt...",
    "sentiment": "POSITIV",
    "impact": "MITTEL",
    "entities": ["huml"],
    "url": "https://..."
  }
]
```

**Datenquelle:**
- Pressearchiv: Fränkischer Tag, BR24, Nordbayerischer Kurier
- Google News Alerts
- Ratsinformationssystem

**Update-Mechanismus:**
1. Web-Search nach "{Stadt} OB-Wahl {Kandidat}" wöchentlich
2. Neue Meldungen mit Sentiment + Impact taggen
3. In `news` Array anhängen, chronologisch sortiert

**Qualitätskriterium:**
- Min. 5 Meldungen pro Stadt
- Jede Meldung hat: `title`, `source`, `date`, `body` (≥30 Zeichen)
- `sentiment`: POSITIV | NEGATIV | NEUTRAL | KRITISCH
- `date`: ISO-Format (YYYY-MM-DD), nicht älter als 60 Tage
- `entities`: Min. 1 verknüpfte Entity-ID
- `url`: Pflicht wenn verfügbar

**Test:**
```
✓ Min. 5 News-Items gerendert
✓ Jede News hat Titel + Source + Datum
✓ Sentiment-Farbe korrekt (POSITIV=grün, NEGATIV=rot, etc.)
✓ Kein "undefined" in Titel oder Body
✓ Sortierung: Neueste zuerst
```

---

### §1.7 Risiko-Ranking

**Was sieht der User:**
Horizontale Balken für jede Entity, sortiert nach Risk-Score.

**Warum:**
"Wer ist am verwundbarsten? Wo sind die Angriffsflächen?"

**Palantir-Äquivalent:** Risk Matrix / Threat Assessment.

**JSON-Pfad:** Berechnet aus `kb[k].risk`

**Datenquelle:** Computed aus Kontroversen-Anzahl, Quellen-Vertrauenswürdigkeit, Widersprüche.

**Update-Mechanismus:** Automatisch bei KB-Updates.

**Qualitätskriterium:**
- Jede Entity hat `risk` (0-100)
- Risk basiert auf nachprüfbaren Fakten, nicht Meinung
- Entities ohne Kontroversen: Risk ≤ 30

**Test:**
```
✓ Balken für jede KB-Entity
✓ Sortierung: Höchster Risk zuerst
✓ Farbe: >50 rot, 25-50 amber, <25 grün
✓ Klick öffnet Entity-Detail
```

---

### §1.8 Themen-Radar (Briefing-Variante, aus THEMEN)

**Was sieht der User:**
Bubble-Chart oder sortierte Liste der Top-Themen mit Relevanz-Score.

**Warum:**
"Worüber redet die Stadt? Was bewegt die Wähler?"

**Palantir-Äquivalent:** Topic Model / Trend Analysis.

**JSON-Pfad:** `themen.radar`
```json
{
  "radar": [
    {
      "topic": "Digitalisierung",
      "relevance": 85,
      "trend": "steigend",
      "candidates": ["huml", "gluesenkamp"],
      "soWhat": "Beide Top-Kandidaten positionieren sich hier — Differenzierung schwierig"
    }
  ]
}
```

**Datenquelle:**
- Pressearchiv-Analyse: Welche Themen werden wie oft erwähnt?
- Ratssitzungen: Welche Themen wurden behandelt?
- Google Trends: Was suchen Bürger?

**Update-Mechanismus:**
1. Themen aus News + Pressearchiv extrahieren
2. Relevanz-Score: Frequenz × Recency × Impact
3. Trend berechnen: steigende vs. fallende Erwähnung

**Qualitätskriterium:**
- Min. 3 Themen pro Stadt
- Jedes Thema: `topic` (Name), `relevance` (0-100), `trend` (steigend/fallend/stabil)
- **`soWhat`**: PFLICHT — Was bedeutet dieses Thema für den Wahlkampf?
- `candidates`: Welche Kandidaten positionieren sich?

**Test:**
```
✓ Min. 3 Themen gerendert
✓ Jedes Thema hat Name + Relevanz-Wert + Trend
✓ soWhat-Text vorhanden und sichtbar
✓ Kein "undefined"
```

---

### §1.9 Social Media Intelligence

**Was sieht der User:**
Profilkarten der Kandidaten mit Follower-Zahlen, Engagement-Rates, Assessment.
Darunter: Insights mit "So What" und Handlungsempfehlung.

**Warum:**
"Wie stark ist der digitale Wahlkampf? Wer gewinnt online?"

**Palantir-Äquivalent:** Social Listening Dashboard / Digital Footprint Analysis.

**JSON-Pfad:** `social`
```json
{
  "kandidaten": [
    {
      "id": "huml",
      "name": "Melanie Huml",
      "partei": "CSU",
      "instagram": {"handle": "@melaniehuml", "followers": 2100, "posts30d": 12, "engagement": 3.2},
      "facebook": {"url": "...", "followers": 5400},
      "website": "https://...",
      "assessment": "Aktive Social-Präsenz, aber niedrige Engagement-Rate"
    }
  ],
  "insights": [
    {
      "title": "Engagement-Gap zwischen Huml und Glüsenkamp",
      "body": "Huml hat 3x mehr Follower, aber Glüsenkamp hat 2x höheres Engagement...",
      "severity": "HOCH",
      "soWhat": "Glüsenkamp mobilisiert seine Basis besser. Für Huml heißt das: Content-Strategie überdenken."
    }
  ],
  "momentum_index": {
    "method": "30% IG Engagement + 20% IG Growth + 20% Google Trends + 15% YouTube + 15% Activity",
    "candidates": [
      {"name": "Huml", "party": "CSU", "composite_score": 10},
      {"name": "Glüsenkamp", "party": "Grüne", "composite_score": 6}
    ],
    "verdict": "Offenes Rennen (10 vs 6)",
    "source": "Composite Score"
  }
}
```

**Datenquelle:**
- Instagram: Follower, Posts, Engagement (Scraper oder manuell)
- Facebook: Follower, Aktivität
- Google Trends: Suchinteresse
- YouTube: Video-Count, Views

**Update-Mechanismus:**
1. Wöchentlich: Instagram/Facebook Zahlen aktualisieren
2. Wöchentlich: Google Trends Pull
3. Momentum Index: Automatisch aus Komponenten berechnen

**Qualitätskriterium:**
- Min. 2 Kandidaten-Profile
- Jeder Kandidat: Min. 1 Platform mit Zahlen
- `insights`: Min. 1 mit `title`, `body`, `soWhat`
- **`soWhat` bei JEDEM Insight**: PFLICHT — "Was bedeutet das für den Wahlkampf?"
- Momentum Index: `candidates` mit `composite_score`
- `verdict`: Zusammenfassung in einem Satz

**Test:**
```
✓ Min. 2 Kandidaten-Profile gerendert
✓ Jedes Profil zeigt min. 1 Platform-Zahl
✓ Min. 1 Insight mit soWhat
✓ Momentum Index sichtbar mit Verdict
✓ Kein "undefined" oder "null"
✓ Keine Apple-Emojis
```

**Rendering-Regel:**
- DATEN: Follower-Zahlen, Engagement-Rate
- INTERPRETATION: `insight.body` erklärt den Kontext
- AKTION: `insight.soWhat` sagt was zu tun ist
- Momentum Index: Balken-Visualisierung mit Score + Verdict-Text

---

### §1.10 Google Trends Intelligence

**Was sieht der User:**
Vergleichschart der Suchtrends + Interpretation.

**Warum:**
"Wen googeln die Wähler? Wer hat Momentum?"

**JSON-Pfad:** `social.google_trends`
```json
{
  "source": "Google Trends (Bayern, 90 Tage)",
  "updated": "2026-02-24",
  "comparison": {
    "huml": {"avg": 55, "peak": 100, "trend_7d": "+127%"},
    "gluesenkamp": {"avg": 5, "peak": 12, "trend_7d": "+1400%"}
  },
  "insight": "Huml dominiert Suchinteresse (11x), aber Glüsenkamp zeigt explosives Wachstum"
}
```

**Datenquelle:** Google Trends (manuell abgefragt, kein API)

**Update-Mechanismus:** Wöchentlich: Screenshot + Zahlen manuell übertragen

**Qualitätskriterium:**
- Min. 2 Kandidaten verglichen
- `trend_7d`: Prozentuale Veränderung letzte 7 Tage
- `insight`: Pflicht — Was bedeutet der Trend?
- `updated`: Max. 7 Tage alt

**Test:**
```
✓ Trends-Chart gerendert
✓ Min. 2 Kandidaten im Vergleich
✓ Insight-Text sichtbar
✓ Kein "undefined"
```

---

### §1.11 Momentum Index

**Was sieht der User:**
Composite Score pro Kandidat als Balken + Verdict-Text.

**Warum:**
DIE Killer-Metrik. Ein Score der ALLE digitalen Signale fusioniert.

**JSON-Pfad:** `social.momentum_index` (siehe §1.9)

**Rendering-Regel:**
- Balken horizontal, sortiert nach Score
- Verdict prominent unter den Balken
- Methode in Kleinschrift anzeigen (Transparenz)
- INTERPRETATION: "Score 10 vs 6 bedeutet: [Kontext]"

---

### §1.12 Sentiment Topics (Themen-Radar aus SENTIMENT)

**Was sieht der User:**
Halbkreis-Gauge oder Balken pro Thema mit Sentiment-Wert + Beitrags-Anzahl.

**Warum:**
"Welche Themen sind positiv/negativ besetzt?"

**JSON-Pfad:** `sentiment.topics`
```json
[
  {
    "name": "Masken-Affäre / Emix-Deal",
    "pct": -75,
    "posts": [
      {"author": "BR24", "text": "...", "date": "2026-02-15", "sent": -0.8}
    ],
    "desc": "Huml-Belastung",
    "volume": "HOCH"
  }
]
```

**WICHTIG:** Feld heißt `name`, NICHT `topic` oder `label`. Das ist in normalizeCity() abgesichert.

**Datenquelle:** Pressearchiv + Social Media Posts, manuell kuratiert.

**Qualitätskriterium:**
- Min. 3 Topics
- Jedes Topic: `name`, `pct` (-100 bis +100), `posts` (min. 1)
- `desc`: Einzeilige Erklärung
- Posts mit `author`, `text`, `date`, `sent`

**Test:**
```
✓ Min. 3 Topics gerendert
✓ Jedes Topic hat Name + Prozentwert
✓ Jedes Topic hat min. 1 Post (NICHT "0 Beiträge")
✓ Kein "undefined"
```

---

### §1.13 Erkannte Muster (Preview)

**Was sieht der User:**
1-2 Muster-Cards aus PATTERNS mit Label + Severity.

**Warum:**
Teaser für den Strategie-Tab. "Es gibt versteckte Muster."

**JSON-Pfad:** `patterns[0..1]`

**Rendering-Regel:**
- Max. 2 Muster-Cards
- Klick führt zu Strategie-Tab
- `severity` als Farb-Badge

**Test:**
```
✓ Min. 1 Pattern-Card wenn patterns.length > 0
✓ Klick öffnet Strategie-Tab
```

---

### §1.14 Top-Hypothese (Preview)

**Was sieht der User:**
Die wichtigste Hypothese mit Confidence-Balken.

**Warum:**
Teaser für den Vergleich-Tab. "Was ist unsere Hauptthese?"

**JSON-Pfad:** `hypotheses[0]`

**Rendering-Regel:**
- Nur 1 Hypothese (die mit höchster Confidence)
- Confidence-Balken mit Prozent
- Klick führt zu Vergleich-Tab

**Test:**
```
✓ Hypothese gerendert wenn hypotheses.length > 0
✓ Confidence-Wert sichtbar
✓ Klick öffnet Vergleich-Tab
```

---

## §2 VERGLEICH TAB

Der Vergleich-Tab beantwortet: "Wie stehen die Kandidaten zueinander?"

---

### §2.1 Vergleichs-Matrix

**Was sieht der User:**
Tabelle: Spalten = Kandidaten, Zeilen = Dimensionen (Risk, Partei, Rolle, Kontroversen, Quellen, Karriere, Sentiment, Trend, Prognose).

**Warum:**
Direkter Head-to-Head Vergleich auf einen Blick.

**Palantir-Äquivalent:** Object Comparison Table.

**JSON-Pfad:** Computed aus `kb`, `sentiment.entities`, `forecast.kandidaten`

**Dimensionen und ihre Datenquellen:**

| Zeile | Daten aus | Formel |
|-------|-----------|--------|
| Risk Score | `kb[k].risk` | Direkt |
| Partei | `kb[k].party` | Direkt |
| Rolle | `kb[k].role` | Direkt |
| Kontroversen | `kb[k].controversies.length + kb[k].contradictions.length` | Computed |
| Quellen | `kb[k].quellen.length` | Computed |
| Karriere | `kb[k].karriere.length` + " Stationen" | Computed |
| Sentiment | `sentiment.entities[k].sent` oder `.score` | Fallback-Kette |
| Trend | `sentiment.entities[k].trend` oder `.label` | Fallback-Kette |
| Prognose 1.WG | `forecast.kandidaten.find(c => c.id === k)` → min-max% | Lookup |

**CRITICAL:** Nicht jede Entity hat Sentiment oder Forecast-Daten.
→ Wenn nicht vorhanden: "—" anzeigen, NICHT crashen.
→ `normalizeCity()` muss `sentiment.entities` für ALLE KB-Keys initialisieren.

**Qualitätskriterium:**
- Jede KB-Entity hat eine Spalte
- Kein "undefined" in irgendeiner Zelle
- Sentiment/Trend: Wenn keine Daten → "—" (Dash)
- Prognose: Wenn Entity nicht in `forecast.kandidaten` → "—"

**Test:**
```
✓ Tabelle gerendert mit KB.length Spalten
✓ 9 Zeilen sichtbar
✓ 0 Zellen mit "undefined"
✓ 0 Zellen mit "NaN"
✓ Sentiment-Zeile zeigt Werte ODER "—"
```

---

### §2.2 Kontroversen-Heatmap

**Was sieht der User:**
Farbige Blöcke pro Entity: Rot = Schwerwiegend, Amber = Mittel, Purple = Widerspruch.

**Warum:**
"Wo sind die Angriffsflächen? Wer hat Leichen im Keller?"

**JSON-Pfad:** `kb[k].controversies` + `kb[k].contradictions`

**Qualitätskriterium:**
- Zeigt ALLE KB-Entities
- Leere Zeilen: Grauer Block mit "0" (nicht unsichtbar)
- Tooltip zeigt Kontroversentitel bei Hover

**Test:**
```
✓ Eine Zeile pro KB-Entity
✓ Legende sichtbar (4 Farben)
✓ Kein "undefined" in Tooltips
```

---

### §2.3 Hypothesen

**Was sieht der User:**
Karten mit Hypothesentitel, Status, Confidence-Balken, Für/Gegen-Evidenz.

**Warum:**
"Was glauben wir? Wie sicher sind wir? Was spricht dafür/dagegen?"

**Palantir-Äquivalent:** Hypothesis Manager / Analysis of Competing Hypotheses (ACH).

**JSON-Pfad:** `hypotheses`
```json
[
  {
    "id": "h1",
    "title": "Stichwahl Huml vs. Glüsenkamp",
    "status": "testing",
    "confidence": 75,
    "summary": "...",
    "forEvidence": ["8 Kandidaten splitten Stimmen", "..."],
    "againstEvidence": ["Huml könnte >50% mit CSU-Apparat holen"]
  }
]
```

**Qualitätskriterium:**
- Min. 1 Hypothese pro Stadt
- `confidence`: 0-100
- `forEvidence` + `againstEvidence`: Min. 1 jeweils
- `status`: confirmed | testing | rejected

**Test:**
```
✓ Min. 1 Hypothese gerendert
✓ Confidence-Balken sichtbar mit Prozentwert
✓ Für + Gegen Evidenz sichtbar
✓ Kein "undefined"
```

---

## §3 STRATEGIE TAB

Der Strategie-Tab beantwortet: "Was sollte der Kandidat/Wahlkampfmanager TUEN?"

---

### §3.1 Talking Points

**Was sieht der User:**
Accordion-Karten pro Thema mit konkreten Gesprächspunkten.

**Warum:**
"Was sage ich beim nächsten Pressetermin / Bürgergespräch?"

**Palantir-Äquivalent:** Action Items / Playbook.

**JSON-Pfad:** `talking_points`
```json
[
  {
    "topic": "Masken-Affäre",
    "points": [
      "Huml war damals Gesundheitsministerin — Rolle klar abgrenzen",
      "Fakten: Emix-Deal wurde vom Rechnungshof geprüft, Ergebnis: ...",
      "Konter: 'Ich habe Verantwortung übernommen und Konsequenzen gezogen'"
    ]
  }
]
```

**Datenquelle:** Aus News + Kontroversen + Patterns abgeleitet, manuell verfeinert.

**Qualitätskriterium:**
- Min. 3 Topics
- Jedes Topic: Min. 2 konkrete Talking Points
- Points sind HANDLUNGSANWEISUNGEN, nicht Beschreibungen
  → "Sag: ..." nicht "Es gibt eine Kontroverse"

**Test:**
```
✓ Min. 3 Talking-Point Karten
✓ Jede Karte hat Titel + min. 2 Points
✓ Kein "undefined"
✓ Accordion öffnet/schließt korrekt
```

---

### §3.2 Szenarien

**Was sieht der User:**
Szenario-Karten mit Name, Beschreibung, Wahrscheinlichkeits-Label, und (optional) Ergebnis-Balken.

**Warum:**
"Was kann passieren? Wie bereite ich mich vor?"

**JSON-Pfad:** `scenarios`
```json
[
  {
    "name": "Stichwahl Huml vs. Glüsenkamp",
    "desc": "Wahrscheinlichstes Szenario: CSU und Grüne in der Stichwahl",
    "label": "likely",
    "results": {
      "huml": 52,
      "gluesenkamp": 48,
      "stichwahl": 85
    },
    "note": "Mobilisierung entscheidet"
  }
]
```

**CRITICAL:** `results` ist OPTIONAL. Viele Szenarien haben keine quantitativen Ergebnisse.
→ Wenn `results` leer/fehlt: Nur Name + Desc + Label zeigen.
→ `normalizeCity()` setzt `sc.results = sc.results || {}`

**Qualitätskriterium:**
- Min. 2 Szenarien pro Stadt
- `label`: likely | possible | unlikely | wildcard
- `desc`: Min. 30 Zeichen
- `results`: Optional, aber wenn vorhanden: Werte summieren ~100%

**Test:**
```
✓ Min. 2 Szenario-Karten
✓ Kein JS-Crash bei leeren results
✓ Label-Badge farbcodiert
✓ Kein "undefined"
```

---

### §3.3 Patterns → Actions (Strategische Muster)

**Was sieht der User:**
Pattern-Karten mit: Label, Bedeutung, "So What" (Cross-City Learning), Entkräftet-wenn, Verknüpfte Entities.

**Warum:**
DAS Alleinstellungsmerkmal. Cross-City Pattern Recognition. "In Regensburg hat X funktioniert → das könnte für Bamberg bedeuten Y."

**Palantir-Äquivalent:** Pattern of Life Analysis / Cross-Entity Intelligence.

**JSON-Pfad:** `patterns`
```json
[
  {
    "id": "cp1",
    "label": "Masken-Altlast als Wahlkampf-Faktor",
    "entities": ["huml"],
    "severity": "HOCH",
    "color": "var(--red)",
    "meaning": "Die Masken-Affäre belastet Humls Kandidatur trotz Aufklärung",
    "confidence": 75,
    "invalidateIf": "Neue Entlastungsdokumente oder Gerichtsentscheidung",
    "soWhat": "In Regensburg hat die REWAG-Affäre dem Amtsinhaber 8% gekostet → ähnliches Muster möglich",
    "evidenceTags": [{"type": "E"}, {"type": "J"}],
    "relatedViews": ["entity:huml"]
  }
]
```

**CRITICAL FIELDS:**
- `meaning`: Was IST das Muster? (Beschreibung)
- `soWhat`: Was BEDEUTET es für DICH? (Cross-City Learning + Handlung)
- `invalidateIf`: Wann ist das Muster FALSCH? (Falsifizierbarkeit)
- `confidence`: Wie sicher? (0-100)

**Datenquelle:** Cross-City Analyse. Muster aus anderen Städten auf aktuelle Stadt übertragen.

**Qualitätskriterium:**
- Min. 2 Patterns pro Stadt
- JEDES Pattern hat: `label`, `meaning`, `soWhat`, `confidence`
- `soWhat` enthält Cross-City Referenz ODER konkrete Handlungsempfehlung
- `soWhat` darf NICHT abgeschnitten sein (kein Truncation!)
- `invalidateIf`: Pflicht — zeigt dass wir kritisch denken

**Test:**
```
✓ Min. 2 Pattern-Karten
✓ Jede Karte zeigt: Label + Meaning + soWhat
✓ soWhat vollständig (nicht abgeschnitten, kein "...")
✓ invalidateIf sichtbar
✓ Confidence-Wert sichtbar
✓ Verknüpfte Entities klickbar
✓ Keine Apple-Emojis
✓ Kein "undefined"
```

**Rendering-Regel:**
- DATEN: Pattern Label + Severity Badge
- INTERPRETATION: `meaning` erklärt das Muster
- AKTION: `soWhat` in eigener Box mit "→ Für Sie:" Prefix
- Entity-Tags: Klickbar, öffnet Entity-Detail
- Keine Truncation! Vollständiger Text. Wenn zu lang → expandable/accordion.

---

## §4 NETZWERK TAB (Graph)

### §4.1 Netzwerk-Graph

**Was sieht der User:**
Force-directed Graph mit Nodes (Personen/Organisationen) und Links (Beziehungen).

**Warum:**
"Wer kennt wen? Welche Netzwerke gibt es?"

**JSON-Pfad:** `graph`
```json
{
  "nodes": [
    {"id": "huml", "label": "Huml", "sub": "CSU", "group": "kandidat", "r": 18}
  ],
  "links": [
    {"source": "huml", "target": "soeder", "label": "Partei", "color": "var(--blue)"}
  ]
}
```

**Qualitätskriterium:**
- Min. 8 Nodes
- Min. 10 Links
- Jeder Node: `id`, `label`, `r` (Radius ≥ 8)
- Jeder Link: `source`, `target`, `label`

**Test:**
```
✓ Graph rendert ohne JS-Error
✓ Nodes sichtbar + klickbar
✓ Labels lesbar
✓ Hover zeigt Tooltip
```

---

## §5 DOSSIER TAB (Entity Detail)

### §5.1 Entity Detail View

**Was sieht der User:**
Vollständiges Profil einer Person: Steckbrief, Karriere, Zitate, Quellen, Timeline, Trust Score.

**Warum:**
"Alles was wir über diese Person wissen, an einem Ort."

**Palantir-Äquivalent:** Object View.

**JSON-Pfad:** `kb[entityId]`

**Sektionen:**
1. **Header:** Name, Party, Role, Summary
2. **Steckbrief:** Key-Value Paare (Alter, Wohnort, Beruf, etc.)
3. **Properties:** Detaillierte Eigenschaften mit Quellen
4. **Karriere:** Chronologische Stationen
5. **Kontroversen:** Mit Severity + Confidence
6. **Zitate:** Originaltexte mit Kontext + Quelle
7. **Quellen:** Alle verwendeten Quellen mit Trust-Score
8. **Timeline:** Visuelle Zeitleiste
9. **Trust Score:** Composite Vertrauenswürdigkeit
10. **Connections:** Beziehungen zu anderen Entities

**Qualitätskriterium:**
- `summary`: Min. 50 Zeichen
- `properties`: Min. 5
- `karriere`: Min. 3 Stationen
- `quellen`: Min. 3
- `zitate`: Min. 1

**Test:**
```
✓ Alle 10 Sektionen rendern (oder "Keine Daten" Fallback)
✓ Kein "undefined" im gesamten View
✓ Properties haben key + val
✓ Timeline rendern ohne Crash
✓ Quellen zeigen URL als klickbaren Link
```

---

## §6 CROSS-CUTTING CONCERNS

### §6.1 Passwort-Gate

**Mechanismus:** URL-Parameter `?admin` bypassed Gate. Sonst: Passwort-Eingabe.
**Passwort:** `tenant.password` oder Default `ainary2026`

### §6.2 Breadcrumb Navigation

**Format:** Radar → {Stadt} → {Tab}
**Regel:** Immer sichtbar. "Radar" linkt zu `radar.html`.

### §6.3 Sidebar (Ontology + Intel Feed + Patterns)

**Immer sichtbar** auf der linken Seite. Zeigt:
- Entity-Counts mit Badges
- Intel Feed (letzte 3 News)
- Pattern-Preview (1-2 Patterns)

### §6.4 Icon/Emoji Policy

**VERBOTEN:**
- Apple Emojis: ⚠️ 📊 🔥 ❌ ✅ etc.
- Unicode-Symbole die auf Windows/Android fehlen

**ERLAUBT:**
- CSS-Badges: `<span class="ev ev-j">J</span>`
- Farbige Punkte via CSS: `background: var(--red); border-radius: 50%`
- SVG Icons (inline)
- Text: HOCH, MITTEL, NIEDRIG als Badges

### §6.5 Truncation Policy

**VERBOTEN:**
- Text mit "..." abschneiden bei Strategie-Cards
- Sentences die mitten im Wort enden

**ERLAUBT:**
- Accordion/Expandable für lange Texte
- "Mehr anzeigen" Button
- Automatisches Abschneiden NUR am Satzende

### §6.6 "Leere Daten" Policy

Wenn eine Sektion keine Daten hat:
- **NICHT:** Leeren Container zeigen
- **NICHT:** "0 Items" anzeigen
- **STATTDESSEN:** Sektion komplett ausblenden ODER "Keine Daten verfügbar — wird aktualisiert" Fallback

---

## §7 AUTOMATED TEST SPECIFICATION

`test_dossier.js` muss folgendes prüfen für JEDE der 8 Städte:

### §7.1 Global Checks
```
✓ Seite lädt ohne JS-Error
✓ Auth-Gate wird übersprungen mit ?admin
✓ Titel enthält Stadtname
✓ Breadcrumb sichtbar
```

### §7.2 Per-Tab Checks
```
BRIEFING:
  ✓ briefing-view.innerHTML.length > 500
  ✓ 0 "undefined" im Text
  ✓ 0 "NaN" im Text
  ✓ Weekly Brief sichtbar (wenn Daten vorhanden)
  ✓ Min. 3 Entity Cards
  ✓ Keine Apple-Emojis (regex: /[\u{1F600}-\u{1F9FF}]/u)

VERGLEICH:
  ✓ switchView('compare') ohne Error
  ✓ compare-view.innerHTML.length > 500
  ✓ 0 "undefined" im Text
  ✓ Matrix-Tabelle sichtbar
  ✓ Min. 1 Hypothese

STRATEGIE:
  ✓ switchView('strategy') ohne Error
  ✓ strategy-view.innerHTML.length > 500
  ✓ 0 "undefined" im Text
  ✓ Kein Text mit "..." (Truncation)
  ✓ Keine Apple-Emojis

NETZWERK:
  ✓ switchView('graph') ohne Error
  ✓ SVG oder Canvas Element vorhanden

DOSSIER:
  ✓ showEntity(firstEntityId) ohne Error
  ✓ Entity-Name sichtbar
```

### §7.3 Data Completeness per City
```
✓ KB entities >= 3
✓ NEWS items >= 5
✓ PATTERNS >= 2
✓ HYPOTHESES >= 1
✓ FORECAST.kandidaten >= 2
✓ SENTIMENT.topics >= 3, each with posts.length >= 1
✓ SOCIAL.insights >= 1 with soWhat
✓ TALKING_POINTS >= 3
✓ SCENARIOS >= 2
✓ GRAPH.nodes >= 8
```

---

## Anhang A: Update-Frequenz Übersicht

| Daten | Frequenz | Methode | Verantwortlich |
|-------|----------|---------|----------------|
| News | 2x/Woche | web_search + manuell | Cron-Agent |
| Social Media Zahlen | 1x/Woche | Scraper + manuell | Cron-Agent |
| Google Trends | 1x/Woche | Manuell | Agent |
| YouTube | 1x/Woche | YouTube API | Agent |
| Kontroversen | Bei Ereignis | Manuell | Agent |
| Prognose | 1x/Woche | Strukturanalyse | Agent |
| Weekly Brief | 1x/Woche | Auto-generiert | Cron-Agent |
| Talking Points | Bei Ereignis | Manuell | Agent |
| Szenarien | 1x/2 Wochen | Manuell | Agent |

## Anhang B: Farbcodierung

| Kontext | Rot | Amber | Grün | Blau | Purple |
|---------|-----|-------|------|------|--------|
| Risk | >50 | 25-50 | <25 | — | — |
| Severity | SCHWERWIEGEND | MITTEL | NIEDRIG | — | — |
| Sentiment | NEGATIV | NEUTRAL | POSITIV | — | — |
| Urgency | HOCH | MITTEL | NIEDRIG | — | — |
| Confidence | <30% | 30-70% | >70% | — | — |
| Kontroverse | Schwerwiegend | Mittel | — | — | Widerspruch |
| Partei | AfD/SPD | — | Grüne | CSU | — |

## Anhang C: Glossar

| Term | Definition |
|------|-----------|
| **Entity** | Person, Organisation, oder Thema in der Knowledge Base |
| **Pattern** | Wiederkehrendes Muster das aus Daten erkannt wurde |
| **Hypothese** | Testbare Annahme mit Für/Gegen-Evidenz |
| **Momentum Index** | Composite Score aus allen digitalen Signalen |
| **soWhat** | Interpretation + Handlungsempfehlung eines Datenpunkts |
| **Cross-City Learning** | Erkenntnis die von Stadt A auf Stadt B übertragbar ist |
| **Stichwahl-Blitz** | 14-Tage-Produkt nach Erstwahl für Stichwahl-Kandidaten |

---

*Ende der Spec. Jede Code-Änderung referenziert §-Nummer. Jeder Test prüft gegen diese Spec.*
