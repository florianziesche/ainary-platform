# Ainary Ontology Schema v1.0

*Inspiriert von Palantir's 3-Layer Ontology (Semantic + Kinetic + Dynamic)*
*Erstellt: 2026-03-05 | Basierend auf palantir-deep-research.md*

---

## Designprinzipien

1. **Decision-centric, not data-centric** — Schema bildet Entscheidungen ab, nicht nur Daten
2. **Everything is an Object** — Jedes Element hat ID, Typ, Properties, Links
3. **Links are typed** — Beziehungen haben Semantik (nicht nur "related to")
4. **Trust is a first-class property** — Jedes Object hat Admiralty + Confidence
5. **Provenance on everything** — Jede Aussage hat Quelle, Datum, EIJA-Tag

---

## Layer 1: SEMANTIC (was existiert)

### Object Types

```
PERSON (Kandidat, Funktionär, Journalist, Bürger)
├── id: string (unique)
├── name: string
├── type: "person"
├── party: string | null
├── role: string (OB-Kandidat, Stadtrat, Redakteur, ...)
├── properties: Record<string, string>  — flexible KV pairs
├── bio: string
├── karriere: string[]
├── zitate: {text, source, date, eija}[]
├── trustScore: {admiralty, confidence, label}
├── color: string (party-derived)
└── soWhat: string  — "→ Einordnung: ..."

MEDIUM (Zeitung, TV, Online, Social)
├── id: string
├── name: string
├── type: "media"
├── url: string
├── mediaType: "print" | "online" | "tv" | "radio" | "social"
├── reach: "lokal" | "regional" | "überregional"
├── owner: string | null
├── trustScore: {admiralty, confidence, label}
└── soWhat: string

THEMA (politisches Thema, Cluster)
├── id: string
├── label: string
├── type: "theme"
├── articleCount: number
├── sentiment: {pos, neg, neutral}
├── executiveSummary: string  — source-backed
├── konsistenz: string  — "Bestätigt durch X Quellen"
└── soWhat: string

ARTIKEL (Nachrichtenquelle)
├── id: string (auto-generated)
├── date: string (ISO)
├── title: string
├── url: string  — must return HTTP 200
├── source: string
├── summary: string
├── body: string  — EIJA-prefixed
├── sentiment: "POS" | "NEG" | "NEUTRAL"
├── admiralty: string (e.g. "B2")
├── confidence: number (0-100, derived from admiralty)
├── sourceLabel: string (auto-derived from admiralty)
├── trustNote: string
├── theme: string (→ THEMA.id)
├── entities: string[] (→ PERSON.id / MEDIUM.id)
└── temporal_weight: number

ORGANISATION (Partei, Verein, Behörde)
├── id: string
├── name: string
├── type: "organisation"
├── orgType: "partei" | "behörde" | "verein" | "unternehmen"
├── members: string[] (→ PERSON.id)
└── trustScore: {admiralty, confidence, label}

CLAIM (überprüfbare Behauptung)
├── id: string
├── claim: string
├── claimant: string (→ PERSON.id)
├── eija: "E" | "I" | "J" | "A"
├── status: "verified" | "disputed" | "unverified" | "false"
├── sources: string[]
├── confidence: number
└── soWhat: string

RESEARCH_REPORT (Input-Dokument das Claims generiert)
├── id: string (e.g. "rr-palantir-deep-2026-03")
├── title: string
├── type: "research_report"
├── date: string (ISO)
├── author: string (→ PERSON.id | "mia" | external)
├── url: string | null
├── domain: string (e.g. "agent-architecture", "kommunalpolitik", "ai-governance")
├── sourceCount: number
├── claimCount: number (auto-computed)
├── topicLinks: string[] (→ TOPIC.id)
├── admiralty: string (overall report quality)
├── confidence: number
├── abstract: string
├── methodology: string | null
└── status: "draft" | "published" | "superseded"

TOPIC (Wissens-Cluster, cross-report)
├── id: string (e.g. "topic-agent-memory", "topic-ontology")
├── label: string
├── type: "topic"
├── domain: string
├── claimCount: number (auto: alle Claims die hierhin linken)
├── reportCount: number (auto: alle Reports die hierhin linken)
├── verifiedClaimCount: number
├── contradictionCount: number
├── konsistenz: string (auto: "Bestätigt durch X Quellen")
├── lastUpdated: string (ISO)
├── subscribers: string[] (future: wer bekommt Updates)
├── executiveSummary: string (auto-generated from top claims)
└── openQuestions: string[]
```

### Link Types

```
PERSON --[kandidiert_in]--> WAHL
PERSON --[mitglied_von]--> ORGANISATION
PERSON --[zitiert_in]--> ARTIKEL
PERSON --[kontroverse_mit]--> PERSON
PERSON --[thematisch_verbunden]--> THEMA
MEDIUM --[berichtet_über]--> THEMA
MEDIUM --[interviewt]--> PERSON
MEDIUM --[owned_by]--> ORGANISATION
ARTIKEL --[published_by]--> MEDIUM
ARTIKEL --[erwähnt]--> PERSON
ARTIKEL --[gehört_zu]--> THEMA
ARTIKEL --[bestätigt|widerspricht]--> CLAIM
CLAIM --[aufgestellt_von]--> PERSON
THEMA --[beeinflusst]--> PERSON (sentiment: POS/NEG/NEUTRAL)

// Research Ontology Network Links
RESEARCH_REPORT --[enthält]--> CLAIM (1:N)
RESEARCH_REPORT --[behandelt]--> TOPIC (M:N)
RESEARCH_REPORT --[zitiert]--> RESEARCH_REPORT (cross-reference)
CLAIM --[gehört_zu]--> TOPIC (M:N)
CLAIM --[bestätigt]--> CLAIM (cross-report verification)
CLAIM --[widerspricht]--> CLAIM (contradiction detection)
TOPIC --[verwandt_mit]--> TOPIC (semantic proximity)
TOPIC --[subsumiert]--> TOPIC (hierarchy: "AI Governance" > "Agent Memory")
```

---

## Layer 2: KINETIC (was passieren kann) — NEU

### Action Types

```
RESEARCH_ARTICLE
  trigger: Neue URL entdeckt
  input: url, source
  output: ARTIKEL object (enriched)
  steps:
    1. Fetch URL → HTTP 200 check
    2. Extract: title, date, summary, entities
    3. Classify: admiralty, sentiment, theme, EIJA
    4. Auto-derive: sourceLabel, trustNote, confidence
    5. Link: zu PERSON, MEDIUM, THEMA

VERIFY_CLAIM
  trigger: Neuer Claim identifiziert
  input: claim text, claimant
  steps:
    1. web_search für Bestätigung/Widerlegung
    2. 3-Quellen-Regel: ≥3 unabhängige → "verified"
    3. EIJA-Tag zuweisen
    4. confidence berechnen
    5. Konsistenz-Badge generieren

UPDATE_FORECAST
  trigger: Neue Daten (Umfrage, Artikel, Event)
  input: city, new_data
  steps:
    1. Existing forecast laden
    2. Bayesian update mit neuen Daten
    3. Momentum-Indikator berechnen (↑↓→)
    4. BLUF narrative generieren

GENERATE_BRIEFING
  trigger: Scheduled (täglich/wöchentlich) oder on-demand
  input: city
  steps:
    1. Alle Artikel seit letztem Briefing laden
    2. BLUF narrative aus Top-3 Entwicklungen
    3. Blind-Spot-Radar: was fehlt?
    4. 48h Watchlist generieren
    5. Handlungsimpulse ableiten

ENRICH_PERSON
  trigger: Neuer Kandidat identifiziert
  input: name, party, city
  steps:
    1. web_search für Profil, Karriere, Zitate
    2. KB-Entry erstellen mit Properties
    3. Graph-Links zu Themen aus Artikeln ableiten
    4. trustScore setzen
    5. soWhat formulieren

EXTRACT_CLAIMS (Research Ontology Network — CORE ACTION)
  trigger: Neuer Research Report abgeschlossen
  input: report_text, sources[], domain
  output: RESEARCH_REPORT + CLAIM[] + TOPIC links
  steps:
    1. Report-Metadaten erfassen (title, date, author, sources)
    2. Claims extrahieren: jede überprüfbare Aussage = 1 Claim
    3. EIJA-Tag pro Claim: E=Evidenz, I=Interpretation, J=Bewertung, A=Annahme
    4. Admiralty pro Claim (von Quellen-Qualität ableiten)
    5. Topic-Zuordnung: existierender Topic oder neuer Topic?
    6. Cross-Check: bestätigt/widerspricht Claim einen bestehenden Claim?
    7. Konsistenz-Badges updaten auf betroffenen Topics
    8. Verified Truths updaten wenn ≥3 unabhängige Bestätigungen
  compound_effect: "Jeder neue Report macht alle bestehenden Topics reicher"

COMPOUND_TOPICS (Network Effect Engine)
  trigger: Nach EXTRACT_CLAIMS oder periodisch
  input: topic_id oder "all"
  steps:
    1. Alle Claims für Topic aggregieren
    2. Contradictions identifizieren (Claims die sich widersprechen)
    3. Konsistenz berechnen: verified / total claims
    4. Executive Summary regenerieren (top claims, gewichtet nach confidence)
    5. Open Questions identifizieren: Topics mit <3 Claims oder hohem A-Anteil
    6. Cross-Topic Connections: Claims die in >1 Topic auftauchen
    7. Subscriber-Notification: "Topic X hat 3 neue Claims seit deinem letzten Check"
  output: Updated TOPIC objects, contradiction alerts, konsistenz badges

INGEST_EXTERNAL_RESEARCH (Scale-Action für 500+ Reports)
  trigger: Neue externe Quelle (Paper, Blog, Report)
  input: url | pdf | text
  steps:
    1. Content extrahieren (web_fetch / pdf)
    2. Qualität bewerten: Admiralty-Code für Gesamtquelle
    3. → EXTRACT_CLAIMS pipeline
    4. Deduplizierung: Claim schon vorhanden? → Link statt Duplikat
    5. Domain-Routing: welche Topics betroffen?
  scale: 500 Reports → ~5.000 Claims → ~50 Topics → Network Effect
```

### Logic Functions (deterministic)

```
derive_confidence(admiralty) → number
  A1→95, A2→90, B2→80, B3→70, C2→65, C3→60, D4→40, E2→30

derive_sourceLabel(admiralty) → string
  A1→"Amtliche Quelle", A2→"Überregionales Leitmedium",
  B2→"Regionales Leitmedium", B3→"Regionaler Fachverlag",
  C2→"Partei-/Kandidatenwebsite", C3→"Social Media / Community"

calculate_konsistenz(theme, articles[]) → string
  count = articles matching theme with ≥2 independent sources
  ≥3 → "◉ Bestätigt durch {n} unabhängige Quellen" (green)
  ≥2 → "◉ Bestätigt durch {n} Quellen" (gold)
  1  → "△ Einzelquelle" (grey)

calculate_momentum(forecast_history[]) → "↑" | "↓" | "→"
  delta = latest - previous
  |delta| < 1 → "→"
  delta > 0 → "↑"
  delta < 0 → "↓"

score_blind_spot(themes[], articles[]) → theme[]
  themes with <2 articles in last 14 days = blind spot
```

---

## Layer 3: DYNAMIC (wer darf was) — FUTURE

```
ACCESS_LEVELS:
  PUBLIC    → Basis-Dossier (Briefing, öffentliche Daten)
  CLIENT    → Voll-Dossier (Strategie, Forecasts, Handlungsimpulse)
  INTERNAL  → Rohdaten, Confidence-Details, Beipackzettel

TENANT_ISOLATION:
  Jede Stadt = eigener Tenant
  Kein Cross-Tenant Datenzugriff ohne Berechtigung
  password: per-tenant Passwortschutz (aktuell: "ainary2026")

AUDIT_LOG: (future)
  Jede Änderung an Objects loggen
  Wer hat wann welchen Claim verifiziert?
  Decision Lineage: welche Daten führten zu welcher Empfehlung?
```

---

## Mapping: Aktuelles JSON → Ontology

| JSON-Feld heute | Ontology Object Type | Status |
|---|---|---|
| `kb.*` | PERSON / MEDIUM | ✅ Existiert |
| `news[]` | ARTIKEL | ✅ Existiert |
| `graph.nodes/links` | Links zwischen Objects | ✅ Existiert |
| `newsClusteredByThema[]` | THEMA | ✅ Existiert |
| `kandidatenBlock[]` | PERSON (Subset) | ✅ Existiert |
| `medienlandschaft` | MEDIUM-Aggregation | ✅ Existiert |
| `claimsLedger[]` | CLAIM | ✅ Existiert |
| `intelligence` | BRIEFING Output | ✅ Existiert |
| `forecast[]` | FORECAST Output | ✅ Existiert |
| Logic Functions | Layer 2 Actions | 🟡 Implicit in dossier.html JS |
| Access Control | Layer 3 Dynamic | 🟡 Only password gate |
| Audit Log | Layer 3 Provenance | ❌ Missing |

### Fazit
**Layer 1 ist zu ~80% implementiert.** Object Types existieren in JSON, Links existieren im Graph. Was fehlt: formale Type-Definitionen, konsistente IDs, typed Links.

**Layer 2 ist zu ~30% implementiert.** Logic Functions existieren als JS in dossier.html (derive_confidence, formatBody, etc). Action Types existieren als manuelle Prozesse. Nicht automatisiert.

**Layer 3 ist zu ~10% implementiert.** Nur Passwort-Gate. Kein Audit Log, keine Role-Based Access, keine Decision Lineage.

---

## Nächste Schritte (priorisiert)

1. **Layer 2 formalisieren**: Logic Functions aus dossier.html extrahieren und als Standard dokumentieren
2. **Action Types als Checklisten**: RESEARCH_ARTICLE und ENRICH_PERSON als wiederholbare Prozesse
3. **Typed Links im Graph**: `filterGroup` → formale Link Types (kandidiert_in, berichtet_über, etc.)
4. **Audit Trail**: `_meta` erweitern mit Change Log pro Object
5. **Layer 3**: Wenn >5 Kunden → Role-Based Access implementieren
