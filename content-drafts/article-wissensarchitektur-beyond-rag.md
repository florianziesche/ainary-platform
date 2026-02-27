# RAG ist tot. Was jetzt kommt, ist besser.
## Wissensarchitektur für Obsidian, Agenten und die Post-RAG-Ära

*Entwurf: 27.02.2026 | Autor: Florian Ziesche | Für: Substack / Blog*

---

**TL;DR:** RAG war ein Hack. Es funktionierte, solange wir nichts Besseres hatten. Jetzt haben wir Besseres: Context Engineering, Ontologien, und Compound-Intelligence-Loops. Wer heute noch naive RAG-Pipelines baut, baut für gestern. Hier ist die Architektur, die tatsächlich funktioniert — getestet mit 679 Obsidian-Dateien, 3 AI-Agenten und realer Consulting-Arbeit.

---

## Das Problem mit RAG

Retrieval-Augmented Generation war die Antwort auf eine simple Frage: *Wie bringe ich einem LLM mein Wissen bei?*

Die Idee: Nimm deine Dokumente, zerhacke sie in Chunks, rechne Embeddings, speichere sie in einer Vektordatenbank, und wenn jemand fragt, hole die ähnlichsten Chunks und klebe sie vor den Prompt. Fertig.

Das war 2023 brillant. 2026 ist es ein Armutszeugnis.

**Warum RAG scheitert:**

**1. Chunking zerstört Kontext.** Ein 500-Zeichen-Chunk aus einem 30-Seiten-Dokument hat keinen Kontext. Er weiß nicht, wo er herkommt, was davor stand, warum er geschrieben wurde. Du verlierst die Struktur, die den Inhalt erst brauchbar macht.

**2. Embedding-Ähnlichkeit ≠ Relevanz.** "CNC-Maschine Wartungsintervall" und "CNC-Maschine Kaufpreis" haben hohe Embedding-Nähe. Aber die Antwort auf "Wann muss ich warten?" ist nicht "24.500 Euro".

**3. Kein Lernen, kein Gedächtnis.** Jede Query startet bei Null. Das System wird nicht schlauer. Es hat letzten Monat die gleiche Frage beantwortet und vergessen. Und es hat vergessen, dass die Antwort falsch war.

**4. Keine Handlungsfähigkeit.** RAG liefert Text. Es kann nichts tun. Es kann keine Lücke füllen, keine Quelle verifizieren, keinen Follow-up-Schritt ausführen.

**5. 1M-Token-Context-Windows machen naive RAG überflüssig.** Warum Chunks suchen, wenn du das ganze Dokument in den Kontext schieben kannst? Gemini hat 2M Tokens. Claude hat 200K. Bei kleinen Wissensbasen (<500 Seiten) ist Brute-Force-Context schlicht besser als RAG.

---

## Was stattdessen funktioniert

Ich arbeite seit einem Jahr mit einem System, das aus 679 Obsidian-Dateien, 3 spezialisierten AI-Agenten und einem Compound-Intelligence-Loop besteht. Hier ist, was ich gelernt habe.

### Ebene 1: Die Ontologie (statt Vektoren)

Palantir hat es vorgemacht: Ontology-Augmented Generation (OAG) statt RAG. Der Unterschied:

```
RAG:     Frage → Ähnliche Chunks finden → Antwort generieren
OAG:     Frage → Ontologie-Lookup → Logik-Tools → Aktionen → Antwort
```

Eine Ontologie definiert nicht nur *was* du weißt, sondern *wie* dein Wissen zusammenhängt. Entitäten, Eigenschaften, Beziehungen, Regeln.

**In Obsidian heißt das:** Dein Vault braucht Struktur, nicht nur Tags.

```yaml
# Nicht das hier:
tags: [AI, consulting, München]

# Sondern das hier:
type: company
name: 36ZERO Vision
status: exited
founded: 2018
location: München
clients: [BMW, Siemens, Bosch]
raised: €5M
sector: Computer Vision
lessons_learned:
  - Enterprise-Sales-Zyklen dauern 9 Monate
  - MVPs überzeugen Ingenieure, PowerPoints überzeugen Vorstände
```

Das zweite Format kann ein Agent lesen, verstehen und *verarbeiten*. Das erste ist Dekoration.

### Ebene 2: Der Knowledge Graph (statt Chunk-Suche)

Microsoft's GraphRAG hat gezeigt: Die interessantesten Antworten stehen nicht IN einem Dokument, sondern ZWISCHEN Dokumenten.

In Obsidian: **Bidirektionale Links sind dein Knowledge Graph.**

Aber die meisten Leute linken falsch. Sie linken `[[München]]` in jedem zweiten Dokument und erzeugen einen nutzlosen Hub. 

Besserer Ansatz: **Typisierte Links.**

```markdown
Verbunden mit [[Andreas Brand]] als:: Pilotkunde
Abgeleitet von:: [[36ZERO Vision#Lessons Learned]]
Widerspricht:: [[Hypothese: MVPs reichen für Mittelstand]]
```

Jetzt kann ein Agent nicht nur finden, sondern *schlussfolgern*: "Andreas Brand ist Pilotkunde UND im Mittelstand. Die Erfahrung von 36ZERO sagt: MVPs überzeugen Ingenieure. Also zeige Andreas den Prototyp, nicht das Deck."

Das ist kein RAG. Das ist Reasoning über Struktur.

### Ebene 3: Self-Critique (statt blinder Retrieval)

SELF-RAG (ICLR 2024) hat gezeigt, dass ein System, das seine eigenen Ausgaben hinterfragt, dramatisch besser performt.

Die Reflexions-Tokens:
- `[Retrieve?]` — Muss ich überhaupt nachschlagen?
- `[IsRelevant?]` — Ist das, was ich gefunden habe, relevant?
- `[IsSupported?]` — Ist meine Antwort durch Evidenz gestützt?
- `[IsUseful?]` — Hilft das dem Nutzer tatsächlich?

**In der Praxis:** Mein System hat einen Quality Ratchet. Scores können nur steigen, nie fallen. Wenn eine Antwort letztes Mal mit 7/10 bewertet wurde, muss die nächste Version mindestens 7/10 erreichen. Alles andere wird verworfen.

RAG hat keinen Ratchet. RAG gibt dir, was die Kosinus-Ähnlichkeit hergibt, und hofft auf das Beste.

### Ebene 4: Compound Intelligence (statt statischer Wissensbasis)

Hier wird es interessant. Die meisten Wissenssysteme — auch die mit RAG — sind statisch. Du füllst sie, du fragst sie ab. Ende.

Mein System hat einen Compound-Intelligence-Loop:

```
SCHEMA → DETECT (Lücken) → FILL (automatisch) → VALIDATE → REFLECT → EVOLVE
```

Konkretes Beispiel: Ich analysiere den CNC-Markt in Sachsen.

1. **Schema sagt:** Jeder Betrieb braucht: Name, Maschinenpark, Mitarbeiter, Digitalisierungsgrad
2. **Detect findet:** Bei 4 von 12 Betrieben fehlt der Digitalisierungsgrad
3. **Fill sucht:** Automatisch nach IHK-Daten, Websites, Handelsregister
4. **Validate prüft:** Sind die gefundenen Daten konsistent?
5. **Reflect fragt:** Warum fehlte das? Gibt es ein Muster?
6. **Evolve lernt:** "Betriebe unter 20 MA haben selten eine Website → alternative Quellen nötig"

Nächstes Mal, wenn ein Betrieb unter 20 MA auftaucht, nutzt das System direkt die alternative Quelle. Es hat *gelernt*.

RAG kann das nicht. RAG hat kein "nächstes Mal".

### Ebene 5: Context Engineering (die neue Disziplin)

"Context Engineering" ist der Begriff, der RAG ablöst. Nicht weil RAG verschwindet, sondern weil RAG nur ein Werkzeug in einem größeren Werkzeugkasten wird.

Context Engineering fragt: **Was braucht das LLM in diesem Moment, um die bestmögliche Entscheidung zu treffen?**

Manchmal ist das ein Chunk aus der Vektordatenbank. Manchmal ist es das komplette Dokument im Long Context. Manchmal ist es ein Graph-Traversal. Manchmal ist es ein Tool-Call zu einer API. Manchmal ist es eine Erinnerung aus einer früheren Konversation.

Das Entscheidende: **Context Engineering ist nicht Retrieval. Es ist Architektur.**

```
Naive RAG:           Query → Vector Search → Top-K → Prompt → Answer
Context Engineering: Query → Intent Analysis → Route → 
                     [Graph | Vector | Cache | Tool | Memory | Long Context] →
                     Assemble → Validate → Prompt → Answer → Learn
```

---

## Die Obsidian-Architektur, die das ermöglicht

Jetzt wird's praktisch. So sieht ein Vault aus, der nicht nur "Second Brain" ist, sondern eine Wissensmaschine:

### Ordnerstruktur

```
📁 Vault/
├── 📁 00-Inbox/           # Capture, weekly processing
├── 📁 10-Projects/        # Aktive, zeitgebundene Arbeit
├── 📁 20-Areas/           # Laufende Verantwortungen
├── 📁 30-Resources/       # Evergreen-Referenz nach Thema
├── 📁 40-Archive/         # Abgeschlossen
├── 📁 50-People/          # Ein Note pro Person = dein CRM
├── 📁 60-Decisions/       # Entscheidungslog mit Reasoning
├── 📁 70-Agents/          # Agent-Konfigurationen + Memory
├── 📁 80-Knowledge/       # Ontologie-Dateien (YAML Frontmatter)
└── 📁 90-System/          # Dashboards, Templates, Meta
```

### Die 4 Regeln für AI-Ready Notes

**Regel 1: Strukturiertes Frontmatter.** Jede Note braucht maschinenlesbare Metadaten. Nicht optional.

```yaml
---
type: insight
source: CB Insights Research
date: 2026-02-27
confidence: 0.8
tags: [ai-agents, enterprise, market-size]
connections:
  - supports: "[[Hypothese: Agent-Markt >$50B bis 2028]]"
  - contradicts: "[[Hypothese: Enterprises warten ab]]"
status: verified
---
```

**Regel 2: Atomare Notes.** Eine Idee, eine Note. Nicht fünf Ideen in einem Meeting-Protokoll begraben. Extrahiere.

**Regel 3: Typisierte Links.** Nicht einfach `[[X]]`, sondern `unterstützt::`, `widerspricht::`, `abgeleitet von::`, `nächster Schritt::`.

**Regel 4: Hypothesen explizit machen.** Schreibe nicht "Ich glaube, dass...". Schreibe:

```markdown
## Hypothese: MVPs > PowerPoints im Mittelstand
- Status: testing
- Evidenz dafür: [[36ZERO Vision#Enterprise Sales]], [[Andreas Brand Feedback]]
- Evidenz dagegen: [[IHK Gespräch Dresden]] (wollten erstmal Präsentation)
- Confidence: 65%
- Test: Nächste 3 Beratungen mit Prototyp statt Deck starten
```

Das ist eine Hypothese, die ein Agent testen, tracken und updaten kann. "Ich glaube, dass..." ist ein Gedanke, der in der Luft hängt.

---

## Was das für die Praxis bedeutet

### Für Obsidian-Nutzer
Dein Vault ist nur so gut wie seine Struktur. Investiere 20% deiner Vault-Zeit in Strukturierung und 80% in Capturing. Die meisten machen es umgekehrt.

### Für AI-Consulting
Wenn du Kunden RAG verkaufst, verkaufst du 2023. Verkaufe stattdessen **Wissensarchitektur**: Ontologien, Knowledge Graphs, Compound Intelligence. Das ist der eigentliche Wert.

### Für SaaS-Builder
Dein nächstes Feature ist nicht "besseres RAG". Es ist Context Engineering: dem LLM zur richtigen Zeit den richtigen Kontext geben. Manchmal Vektor-Suche. Manchmal Graph-Traversal. Manchmal einfach das ganze Dokument.

### Für Gründer mit ADHS
(Ja, das bin ich.)

Das System muss *für dich arbeiten*, nicht umgekehrt. Die Compound-Intelligence-Loop ist perfekt für ADHS-Gehirne: Du wirfst Rohmaterial rein, der Agent strukturiert, verbindet und lernt. Du musst nicht organisieren. Du musst nur capturen. Das System organisiert sich selbst.

---

## Das Fazit

RAG war ein Meilenstein. Es hat gezeigt, dass LLMs mit externem Wissen arbeiten können. Aber es war immer ein Hack: Chunks statt Verständnis, Ähnlichkeit statt Relevanz, statisch statt lernend.

Was jetzt kommt, ist fundamental anders:

| | RAG (2023) | Post-RAG (2026) |
|---|---|---|
| Wissensform | Chunks in Vektoren | Ontologien + Knowledge Graphs |
| Retrieval | Kosinus-Ähnlichkeit | Context Engineering (Multi-Route) |
| Qualität | Keine Garantie | Self-Critique + Quality Ratchet |
| Lernen | Keins | Compound Intelligence Loop |
| Handlung | Nur Text generieren | Detect → Fill → Validate → Act |
| Architektur | Pipeline | Feedback-Loop |

**Die Zukunft gehört nicht dem besten Retrieval. Sie gehört der besten Wissensarchitektur.**

Und die fängt in deinem Obsidian Vault an.

---

*Florian Ziesche baut AI-Systeme die lernen. Vorher: CEO von 36ZERO Vision (Cloud CV, €5M raised, Kunden: BMW, Siemens, Bosch). Jetzt: AI-Consulting für Mittelstand und Compound Intelligence Research bei Ainary Ventures.*

*Nächste Woche: Wie ich 3 AI-Agenten manage, die zusammen schlauer sind als jeder einzelne.*

---

## Meta / Notizen

### Quellen
- Palantir OAG: Palantir Blog, Jan 2024 (Ontology-Augmented Generation)
- Microsoft GraphRAG: Microsoft Research, Apr 2024
- SELF-RAG: Asai et al., ICLR 2024 (Oral Presentation)
- KG-RAG: Nature Scientific Reports, 2025
- "RAG is Dead" Debatte: VentureBeat Jan 2026, Towards Data Science Oct 2025, UCStrategies Feb 2026
- Context Engineering: TheNewStack Jul 2025, RAGFlow Dec 2025
- Eigene Erfahrung: 679 Obsidian-Dateien, 3 Agenten, Ainary Compound Intelligence Engine

### Repurpose-Plan
- **Substack:** Full Article (dieser Text)
- **LinkedIn:** Kurzversion, 5 Punkte warum RAG tot ist + 1 Grafik (die Vergleichstabelle)
- **Twitter/X Thread:** "RAG ist tot. Hier sind 5 Dinge die besser funktionieren:" (1 Tweet pro Ebene)
- **Workshop-Material:** Slides aus den 5 Ebenen + Live-Demo mit Obsidian Vault

### Bevor du veröffentlichst
1. Grafik erstellen: Die Comparison Table als Visual
2. Obsidian-Vault-Screenshot anonymisieren
3. CTA: Link zu Templates (SOUL.md, AGENTS.md, Vault-Struktur)
4. Cross-check: Alle Paper-Referenzen verifizieren
