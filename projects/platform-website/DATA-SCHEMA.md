# DATA-SCHEMA.md — Verbindliches Daten-Schema für City Dossiers

**Version:** 3.0
**Stand:** 2026-02-24
**Referenz-Dossier:** Bamberg (143 Punkte, GOLD STANDARD)
**Template:** `dossier.html` — liest ausschließlich `data/cities/{city_id}.json`

---

## Prinzip

**1 Template + N Datensätze.** Jede Stadt ist eine JSON-Datei. Das Template rendert dynamisch. Schema-Änderungen propagieren zu ALLEN Städten.

- **Keine hardcoded Daten im Template** — alles aus JSON
- **Defensive Rendering** — jedes Feld kann fehlen, Template crasht nicht
- **Qualitäts-Gate** — `rag/validate_city.py` prüft vor Deploy
- **Automatisierte Tests** — `test_dossier.js` prüft alle 8 Städte mit Playwright

---

## Datei-Struktur

```
data/cities/{city_id}.json     ← eine Datei pro Stadt
```

**city_id**: Kleinbuchstaben, keine Umlaute (`nuernberg`, `fuerth`, `wuerzburg`)

---

## 1. TENANT — Stadt-Metadaten

| Feld | Typ | Required | Quelle | Beispiel |
|------|-----|----------|--------|----------|
| `id` | string | ✅ | manuell | `"bamberg"` |
| `name` | string | ✅ | manuell | `"Kampagnen-Intelligence Bamberg"` |
| `gemeinde` | string | ✅ | Wikipedia | `"Bamberg"` |
| `landkreis` | string | ✅ | Wikipedia | `"Kreisfreie Stadt Bamberg"` |
| `typ` | string | ✅ | manuell | `"OB-Wahl"` |
| `wahl` | string | ✅ | offiziell | `"08.03.2026"` |
| `ew` | string | ✅ | Stat. Landesamt | `"~78.000"` |
| `regierungsbezirk` | string | ✅ | Wikipedia | `"Oberfranken"` |
| `state` | string | ✅ | — | `"Bayern"` |
| `quellen` | int | ✅ | auto (count) | `42` |
| `password` | string | ✅ | manuell | `"bamberg2026"` |
| `organisationen` | array | ✅ min 3 | Recherche | Parteien, Bündnisse, Vereine |
| `alerts` | array | ✅ min 3 | Nachrichtenrecherche | Kritische Entwicklungen |
| `gemeinderat2020` | array | ✅ | Wahlergebnis 2020 | `[{partei, prozent, sitze}]` |
| `strukturdaten` | object | ✅ | Stat. Landesamt | EW, Fläche, Dichte etc. |

### Quellen für TENANT
- **Primär:** Wikipedia Gemeinde-Seite, Statistisches Landesamt Bayern
- **Wahltermin:** Bayerisches Landesamt für Statistik / Gemeindewahlleiter
- **Gemeinderat:** Offizielles Wahlergebnis 2020 (Gemeindewebsite)
- **Alerts:** Lokalpresse (Fränkischer Tag, BR24, SZ Regionalteil)

---

## 2. KB — Knowledge Base (Kandidaten-Dossiers)

**Struktur:** `"kb": { "kandidat_id": { ... }, ... }`

Jeder Kandidat als eigener Key. **Mindestens 3 Kandidaten** pro Stadt.

### Entity-Schema

| Feld | Typ | Required | Quelle | Beschreibung |
|------|-----|----------|--------|--------------|
| `name` | string | ✅ | offiziell | Voller Name |
| `role` | string | ✅ | Recherche | `"OB-Kandidatin Bamberg"` |
| `party` | string | ✅ | offiziell | Parteiname |
| `since` | string | ✅ | Recherche | Seit wann aktiv |
| `result` | string | ✅ | — | `"Wahl 08.03.2026"` |
| `risk` | int | ✅ | Bewertung | 0-100 Risiko-Score |
| `trust` | int | ✅ | Bewertung | 1-10 Trust-Score |
| `sources` | int | ✅ | auto (count) | Anzahl Quellen |
| `color` | string | ✅ | Design | CSS-Variable `"var(--red)"` |
| `summary` | string | ✅ min 50 Wörter | Recherche | Zusammenfassung |
| `properties` | array | ✅ min 5 | Recherche | `[{k: "Alter", v: "50"}]` |
| `connections` | array | ✅ min 2 | Recherche | `[{to, label, color}]` |
| `controversies` | array | empfohlen | Presse | Skandale, Kritik |
| `timeline` | array | empfohlen | Recherche | Karriere-Zeitstrahl |
| `steckbrief` | object | ✅ | Recherche | Siehe unten |
| `karriere` | array | ✅ min 3 | Recherche | Lebenslauf-Stationen |
| `zitate` | array | ✅ min 1 | Presse/Interviews | Wörtliche Zitate |
| `quellen` | array | ✅ min 3 | — | Quellenverzeichnis |
| `trustScore` | object | ✅ | Bewertung | `{score, label, reasoning, sources}` |

### Steckbrief-Felder (min 4 von 6 ausgefüllt)

| Feld | Beispiel |
|------|----------|
| `alter` | `"50"` |
| `beruf` | `"Juristin, Ex-Gesundheitsministerin"` |
| `familienstand` | `"verheiratet"` |
| `wohnort` | `"Bamberg"` |
| `partei` | `"CSU"` |
| `ausbildung` | `"Jura-Studium, Staatsexamen"` |

### Quellen für KB
- **Primär:** Offizielle Partei-Website, Wikipedia, Abgeordnetenprofil
- **Summary:** Lokalpresse (min 3 unabhängige Quellen)
- **Karriere:** LinkedIn, Lebenslauf auf Partei-Website, Wikipedia
- **Zitate:** Zeitungsinterviews, Pressemitteilungen, TV-Auftritte
- **Properties:** Kombiniert aus allen Quellen
- **Trust Score:** Eigene Bewertung basierend auf Quellenqualität

---

## 3. GRAPH — Netzwerk-Visualisierung

```json
{
  "graph": {
    "nodes": [
      {"id": "huml", "label": "Melanie Huml", "sub": "CSU · Ex-Ministerin", "group": "threat", "r": 28, "info": "CSU, Risk: 55"}
    ],
    "links": [
      {"source": "huml", "target": "gluesenkamp", "label": "Hauptgegner", "color": "var(--red)"}
    ]
  }
}
```

| Feld | Required | Beschreibung |
|------|----------|--------------|
| `nodes[].id` | ✅ | Muss mit KB-Key übereinstimmen |
| `nodes[].label` | ✅ | Anzeigename |
| `nodes[].sub` | ✅ | Untertitel (Partei · Rolle) |
| `nodes[].group` | ✅ | `threat` / `ally` / `neutral` / `institution` |
| `nodes[].r` | ✅ | Radius (10-40, basierend auf Relevanz) |
| `links[].source` | ✅ | Node-ID |
| `links[].target` | ✅ | Node-ID |
| `links[].label` | ✅ | Beziehungstyp |

**Min:** 8 Nodes, 10 Links pro Stadt

### Quellen für GRAPH
- **Abgeleitet** aus KB-Connections + Partei-Konstellationen
- **Beziehungstypen:** Hauptgegner, Koalitionspartner, Konkurrenz, Unterstützung, Nachfolge

---

## 4. NEWS — Nachrichtenlage

```json
{
  "news": [
    {
      "title": "SZ: Bamberg OB-Wahl...",
      "source": "Süddeutsche Zeitung",
      "date": "21.02.2026",
      "body": "Dreikampf so offen wie...",
      "sentiment": "NEU",
      "impact": "MITTEL",
      "entities": ["huml", "gluesenkamp"],
      "url": "https://..."
    }
  ]
}
```

| Feld | Required | Werte |
|------|----------|-------|
| `title` | ✅ | Headline mit Quellenprefix |
| `source` | ✅ | Medienname |
| `date` | ✅ | TT.MM.JJJJ oder JJJJ-MM-TT |
| `body` | ✅ min 20 Wörter | Zusammenfassung |
| `sentiment` | ✅ | `POS` / `NEG` / `NEU` / `MIX` |
| `impact` | ✅ | `HOCH` / `MITTEL` / `NIEDRIG` |
| `entities` | empfohlen | Array von KB-Keys |
| `url` | empfohlen | Quell-URL |

**Min:** 5 News-Items pro Stadt, nicht älter als 6 Monate

### Quellen für NEWS
- **Primär:** Lokalpresse (Fränkischer Tag, Mittelbayerische, etc.)
- **Sekundär:** BR24, SZ Bayern, Spiegel (wenn relevant)
- **Kein Scraping** — manuelle Zusammenfassung + URL

---

## 5. HYPOTHESES — Testbare Prognosen

```json
{
  "hypotheses": [
    {
      "id": "H1",
      "title": "Stichwahl Huml vs. Glüsenkamp",
      "status": "TESTING",
      "confidence": 65,
      "stColor": "var(--amber)",
      "summary": "Wahrscheinlichstes Szenario...",
      "forEvidence": ["CSU-Basis stark", "Landesbonus"],
      "againstEvidence": ["Masken-Affäre Risiko"]
    }
  ]
}
```

| Feld | Required | Werte |
|------|----------|-------|
| `id` | ✅ | `H1`, `H2`, ... |
| `title` | ✅ | Klare These |
| `status` | ✅ | `TESTING` / `CONFIRMED` / `REJECTED` |
| `confidence` | ✅ | 0-100 |
| `summary` | ✅ | Begründung |
| `forEvidence` | ✅ | Array — Belege dafür |
| `againstEvidence` | ✅ | Array — Belege dagegen |

**Min:** 2 Hypothesen pro Stadt

### Quellen für HYPOTHESES
- **Abgeleitet** aus Patterns, Forecast, News
- **Evidence:** Muss auf konkrete Quellen referenzieren

---

## 6. SENTIMENT — Stimmungsbild

```json
{
  "sentiment": {
    "overall": "Hochspannung — offenster Dreikampf seit Jahrzehnten",
    "trend": "Glüsenkamp und Huml gleichauf",
    "entities": {
      "huml": {"label": "Huml", "score": -0.3}
    },
    "topics": [
      {
        "name": "Masken-Affäre / Emix-Deal",
        "topic": "Masken-Affäre / Emix-Deal",
        "valence": -0.7,
        "volume": "HOCH",
        "desc": "Humls Rolle...",
        "pct": -70,
        "posts": [
          {"author": "Spiegel", "text": "...", "date": "12.2022", "source": "spiegel.de"}
        ]
      }
    ]
  }
}
```

**WICHTIG:** Topic-Objekte MÜSSEN das Feld `name` haben (nicht nur `topic` oder `label`). Das Template liest `t.name`.

| Feld | Required | Beschreibung |
|------|----------|--------------|
| `topics[].name` | ✅ | **Kanonischer Anzeigename** |
| `topics[].valence` | ✅ | -1.0 bis +1.0 |
| `topics[].volume` | ✅ | `HOCH` / `MITTEL` / `NIEDRIG` |
| `topics[].desc` | ✅ | Erklärung |
| `topics[].pct` | ✅ | -100 bis +100 (für Balkendiagramm) |
| `topics[].posts` | ✅ min 2 | Belegstellen mit Quelle |

**Min:** 3 Topics pro Stadt

### Quellen für SENTIMENT
- **Posts:** Echte Zeitungsartikel, Pressemitteilungen, Social-Media-Posts
- **Valence:** Abgeleitet aus Tonalität der Berichterstattung
- **Kein Fabrication** — jeder Post muss real und belegbar sein

---

## 7. PATTERNS — Cross-Entity Muster

```json
{
  "patterns": [
    {
      "id": "cp1",
      "label": "Masken-Altlast als Wahlkampf-Faktor",
      "entities": ["huml"],
      "severity": "HOCH",
      "meaning": "Humls Verwicklung im Emix-Maskendeal...",
      "confidence": 85,
      "invalidateIf": "Neue Daten widerlegen dieses Pattern.",
      "soWhat": "Für den Kunden: ...",
      "evidenceTags": [{"type": "E"}]
    }
  ]
}
```

| Feld | Required | Werte |
|------|----------|-------|
| `id` | ✅ | `cp1`, `cp2`, ... |
| `label` | ✅ | **Nicht `titel`** |
| `meaning` | ✅ | **Nicht `beschreibung`** |
| `severity` | ✅ | `HOCH` / `MITTEL` / `NIEDRIG` |
| `confidence` | ✅ | 0-100 |
| `soWhat` | ✅ | Was bedeutet das für den Kunden? |
| `invalidateIf` | ✅ | Was würde dieses Pattern entkräften? |
| `evidenceTags` | ✅ | `[{type: "E"/"J"/"I"}]` (Empirisch/Journalistisch/Indiz) |
| `entities` | ✅ | Betroffene KB-Keys |

**Min:** 2 Patterns pro Stadt

---

## 8. ACTIONS — Empfohlene Maßnahmen

```json
{
  "actions": [
    {
      "priority": "HOCH",
      "prColor": "var(--red)",
      "title": "Stichwahl-Analyse vorbereiten",
      "body": "Am 08.03 abends: Sofort Gegner-Analyse...",
      "evidence": "Analyse",
      "urgency": "08.03.2026"
    }
  ]
}
```

**Min:** 2 Actions pro Stadt

---

## 9. FORECAST — Wahlprognose

```json
{
  "forecast": {
    "wahltermin": "08.03.2026",
    "stichwahl": "22.03.2026",
    "stichwahlConf": 60,
    "stichwahlRange": {"min": 70, "max": 95},
    "kandidaten": [
      {"id": "huml", "name": "Melanie Huml", "partei": "CSU", "min": 25, "max": 50, "zentral": 35, "conf": 45, "tag": "J"}
    ],
    "historie": [
      {"jahr": 2008, "wg": 1, "gewinner": "Starke (SPD) 52,2%"}
    ],
    "keyfactors": ["..."],
    "title": "OB-Wahl Bamberg 2026 — Prognose",
    "method": "Strukturelle Analyse + historische Muster",
    "confidence": 60,
    "evidence": "J"
  }
}
```

| Feld | Required | Beschreibung |
|------|----------|--------------|
| `wahltermin` | ✅ | Erster Wahlgang |
| `stichwahl` | ✅ | Stichwahl-Datum |
| `stichwahlConf` | ✅ | Stichwahl-Wahrscheinlichkeit (0-100) |
| `kandidaten` | ✅ min 3 | Prognose pro Kandidat |
| `kandidaten[].tag` | ✅ | Evidence-Level: `E`/`J`/`I`/`A` |
| `historie` | empfohlen | Historische Wahlergebnisse |
| `method` | ✅ | Methodik-Beschreibung |

### Evidence-Level für Prognosen
- **E (Empirisch):** Basierend auf Umfragen oder harten Daten
- **J (Journalistisch):** Basierend auf Presseberichte + Analyse
- **I (Indiz):** Abgeleitet aus Indikatoren
- **A (Annahme):** Strukturelle Schätzung

### Quellen für FORECAST
- **Historie:** Offizielle Wahlergebnisse (Gemeindewebsite, Stat. Landesamt)
- **Prognose:** Eigene Analyse basierend auf Strukturdaten + Trends
- **KEINE Umfragen fabricieren** — "Keine Umfragedaten verfügbar" wenn keine existieren

---

## 10. SOCIAL — Social Media Intelligence

```json
{
  "social": {
    "title": "Social Media Intelligence — Bamberg",
    "lastUpdated": "2026-02-24",
    "platforms": ["Instagram", "Facebook", "Website"],
    "kandidaten": [
      {
        "id": "huml",
        "name": "Melanie Huml",
        "partei": "CSU",
        "instagram": {"handle": "@melaniehuml", "followers": 4200, "posts": 450},
        "facebook": {"url": "...", "followers": 8500},
        "website": "melaniehuml.de",
        "assessment": "Ex-Ministerin mit Landes-Profil..."
      }
    ],
    "insights": [
      {"title": "Titel", "body": "Text", "severity": "HOCH", "soWhat": "..."}
    ],
    "google_trends": {
      "source": "Google Trends (Bayern, 90 Tage)",
      "updated": "2026-02-24",
      "comparison": {"huml": 17.0, "gluesenkamp": 1.6},
      "insight": "..."
    },
    "momentum_index": {
      "method": "30% IG Engagement + 20% IG Growth + 20% Google Trends + 15% YouTube + 15% Activity",
      "source": "Composite Score",
      "updated": "2026-02-24",
      "candidates": [{"name": "...", "score": 10, "breakdown": {...}}],
      "verdict": "Offenes Rennen"
    }
  }
}
```

**WICHTIG:**
- `insights[].title` und `insights[].body` sind die kanonischen Felder (nicht `type`/`text`)
- Instagram-Handles müssen via `web_search` verifiziert werden
- `momentum_index.source` darf NICHT `null` sein

### Quellen für SOCIAL
- **Instagram:** Öffentliche Profile, via web_search verifiziert
- **Facebook:** Öffentliche Seiten
- **Google Trends:** trends.google.de (Bayern, 90 Tage, Vergleich)
- **Momentum Index:** Eigene Berechnung aus IG + Google Trends + YouTube + Activity

---

## 11. YOUTUBE — YouTube Intelligence

```json
{
  "youtube": {
    "source": "YouTube Data API v3",
    "scraped": "2026-02-24",
    "candidates": [
      {"name": "Melanie Huml", "video_count": 2, "has_own_channel": false, "top_videos": [...]}
    ],
    "city_videos": [
      {"title": "...", "channel": "...", "url": "https://youtu.be/...", "published": "2026-02-03"}
    ],
    "insight": "Red Diamond Insight Text",
    "cross_platform_gap": "Vergleich YT vs IG vs Google Trends"
  }
}
```

### Quellen für YOUTUBE
- **API:** YouTube Data API v3 (Key: in Environment)
- **Suche:** `"{kandidat_name}" {stadt} Kommunalwahl 2026`
- **Top Videos:** Sortiert nach Relevanz, max 5 pro Kandidat

---

## 12. TALKING POINTS — Einsatzbereite Argumente

```json
{
  "talking_points": [
    {
      "topic": "Masken-Affäre als Vertrauensfrage",
      "points": [
        {"text": "Zitat oder Argument...", "ev": "E", "src": "Spiegel 13.12.2022"}
      ]
    }
  ]
}
```

| Feld | Required | Beschreibung |
|------|----------|--------------|
| `topic` | ✅ | Thema |
| `points[].text` | ✅ | Wörtlicher Talking Point |
| `points[].ev` | ✅ | Evidence: `E`/`J`/`I`/`A` |
| `points[].src` | ✅ | Quellen-Angabe |

---

## 13. SCENARIOS — Stichwahl-Szenarien

```json
{
  "scenarios": [
    {
      "name": "Stichwahl Huml vs. Glüsenkamp (55%)",
      "desc": "CSU-Basis trägt Huml auf Platz 1...",
      "label": "possible",
      "results": {}
    }
  ]
}
```

| Feld | Required | Werte |
|------|----------|-------|
| `name` | ✅ | Szenario-Name |
| `desc` | ✅ | Beschreibung |
| `label` | ✅ | `best` / `worst` / `stichwahl_win` / `possible` |

---

## 14. WEEKLY BRIEF — Lage-Briefing

```json
{
  "weekly_brief": {
    "title": "Lage-Briefing Bamberg — KW 9/2026",
    "date": "24.02.2026",
    "daysToElection": 12,
    "summary": "12 Tage vor der Wahl...",
    "priorities": [
      {"action": "...", "ev": "J", "deadline": "08.03.2026"}
    ],
    "watchItems": [
      {"item": "...", "trigger": "...", "response": "..."}
    ]
  }
}
```

---

## 15. STICHWAHL PREDICTION — Prognose-Zusammenfassung

```json
{
  "stichwahl_prediction": {
    "probability": 85,
    "likely_matchup": "Huml (CSU) vs Glüsenkamp (Grüne)",
    "digital_advantage": "Huml (11x mehr gegoogelt)",
    "wildcard": "Glüsenkamp +1400% Google Trend",
    "reason": "8 zugelassene Kandidaten...",
    "source": "Composite: Google Trends + Instagram + Press + 2020 Patterns",
    "updated": "2026-02-24"
  }
}
```

---

## Feld-Naming Regeln (NICHT VERHANDELBAR)

| ✅ Richtig | ❌ Falsch | Kontext |
|-----------|----------|---------|
| `label` | `titel` | Patterns |
| `meaning` | `beschreibung` | Patterns |
| `party` | `partei` | KB Entities |
| `role` | `rolle` | KB Entities |
| `properties` | `steckbrief` (als Array) | KB Entities |
| `name` | `label`, `topic` | Sentiment Topics |
| `title` + `body` | `type` + `text` | Social Insights |
| `src` oder `source` | — | Talking Points (beides OK) |

---

## Qualitäts-Anforderungen

### Minimum pro Stadt (PASS = 90 Punkte)

| Sektion | Minimum |
|---------|---------|
| Tenant | Alle required fields |
| KB | 3 Kandidaten, je min 50-Wort Summary, 5 Properties, 3 Quellen |
| Graph | 8 Nodes, 10 Links |
| News | 5 Items, max 6 Monate alt |
| Hypotheses | 2 testbare Prognosen |
| Sentiment | 3 Topics mit je 2 Posts |
| Patterns | 2 Patterns mit soWhat + invalidateIf |
| Actions | 2 Empfehlungen |
| Forecast | Prognose mit Methodik + historischen Daten |
| Social | 3 Kandidaten mit IG-Daten |

### Quellen-Anforderungen

| Level | Min. Quellen | Typ |
|-------|-------------|-----|
| **Bronze** | 20 | Presse + Wikipedia |
| **Silber** | 30 | + Offizielle Quellen + Social Media |
| **Gold** | 40+ | + Interviews + Primärquellen + API-Daten |

### Evidence-Tags (E/J/I/A)

| Tag | Bedeutung | Anforderung |
|-----|-----------|-------------|
| **E** (Empirisch) | Durch Daten belegt | URL/Studie/Statistik angeben |
| **J** (Journalistisch) | Durch Presse gestützt | Medienname + Datum angeben |
| **I** (Indiz) | Abgeleitet/Indirekt | Herleitung beschreiben |
| **A** (Annahme) | Strukturelle Schätzung | Als Annahme kennzeichnen |

---

## Validierung

```bash
# Einzelne Stadt prüfen
python3 rag/validate_city.py bamberg

# Alle Städte prüfen
for city in bamberg regensburg nuernberg augsburg erlangen fuerth passau landshut; do
  python3 rag/validate_city.py $city
done

# Browser-Tests (8 Städte, Playwright)
node test_dossier.js
```

### Kein Deploy ohne:
1. `validate_city.py` → PASS (≥90 Punkte)
2. `test_dossier.js` → 8/8 ✅
3. JS Syntax Check → 3/3 Scripts OK

---

## Neue Stadt anlegen — Checkliste

1. [ ] `data/cities/{city_id}.json` erstellen
2. [ ] Alle 15 Sektionen befüllen (min required fields)
3. [ ] `rag/validate_city.py {city_id}` → PASS
4. [ ] `radar-data.json` aktualisieren
5. [ ] `node test_dossier.js` → alle Städte PASS
6. [ ] `vercel --prod` → Deploy
7. [ ] Live-URL testen mit `&admin` Parameter

---

*Dieses Dokument ist verbindlich. Schema-Abweichungen führen zu Rendering-Fehlern.*


## 16. Claim Ledger (NEU — Asset Builder Integration)

```json
"claim_ledger": [
  {
    "id": "CL-001",
    "claim": "string — Die Behauptung",
    "this_answers": "string — Welche Frage beantwortet das?",
    "section": "string — forecast|pattern|hypothesis",
    "classification": "E|I|J|A|Derived",
    "confidence": "High|Med|Low",
    "sources": ["S01", "S03"],
    "if_wrong": "string — Konsequenz wenn falsch",
    "if_low": "string — Was würde Confidence erhöhen?",
    "contradictions": "string — Bekannte Widersprüche"
  }
]
```

## 17. Contradiction Register (NEU)

```json
"contradictions": [
  {
    "id": "CR-001",
    "conflict": "string — Was widerspricht sich?",
    "sources_involved": ["S03", "S07"],
    "why_differ": "string — Warum unterscheiden sich die Quellen?",
    "impact": "string — Wie beeinflusst es die Analyse?",
    "resolution": "string — Was würde den Widerspruch auflösen?"
  }
]
```

## 18. Enhanced Quellenverzeichnis (Upgrade)

```json
"quellenverzeichnis": [
  {
    "id": "S01",
    "name": "string",
    "url": "string",
    "accessDate": "YYYY-MM-DD",
    "typ": "A1|A2|B1|B2|C",
    "trust": 0-100,
    "supports": ["pattern-cp1", "forecast-stichwahl"],
    "caveats": "string — Einschränkungen der Quelle"
  }
]
```

## Asset Builder Field Extensions (alle Sections)

Folgende Felder können in `patterns`, `hypotheses`, `news`, `talking_points`, `scenarios` ergänzt werden:

```json
{
  "this_answers": "string",
  "classification": "E|I|J|A|Derived|Operational",
  "sources": ["S01", "S03"],
  "if_wrong": "string"
}
```
