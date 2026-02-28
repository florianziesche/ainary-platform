# Research Report #3: Agentic Research Automation — Von 3h zu 30min pro Analyse
*Mia ♔ | 2026-02-23 | [INTERN]*

---

## THE ANSWER
Der Weg von 3h zu 30min ist realistisch mit einer **4-Stufen-Pipeline**: (1) Automatisierte Datensammlung (Scraping + APIs), (2) LLM-gestützte Extraktion (NER, Sentiment, Zusammenfassung), (3) Strukturierte JSON-Generierung, (4) Template-Rendering. Die manuelle Arbeit bleibt: Qualitätskontrolle und E/I/J/A-Bewertung. Ziel: 80% automatisiert, 20% menschlich — das ist der Unterschied zwischen Consulting und Platform.

## CONFIDENCE: Likely (75%)
*Technisch machbar. Aber: Qualitätsverlust bei Automatisierung ist das Risiko. E/I/J/A manuell = unser USP, das darf nicht automatisiert werden.*

---

## KEY EVIDENCE

### 1. Was heute 3h dauert (IST-Prozess)
| Schritt | Zeit | Automatisierbar? |
|---------|------|-----------------|
| Kandidaten-Recherche (Wikipedia, Website, Presse) | 45 min | ✅ 90% |
| Lokale Presseartikel finden + lesen | 60 min | ✅ 70% (Scraping + Summarization) |
| Netzwerk-Mapping (Partei, Vereine, Wirtschaft) | 30 min | 🟡 50% (NER + manuell) |
| Wahlprogramm-Analyse | 20 min | ✅ 80% (LLM-Summary) |
| Vergleichsanalyse (Kandidaten gegeneinander) | 15 min | ✅ 80% |
| E/I/J/A Bewertung jedes Datenpunkts | 30 min | ❌ 0% (manuell = USP) |
| JSON-Erstellung für Template | 20 min | ✅ 95% |
| QA + Review | 20 min | ❌ 0% |
| **TOTAL** | **~3h 20min** | **~60% automatisierbar** |

**Realistisches Ziel: 1h 15min** (nicht 30 min). 30 min nur wenn E/I/J/A vereinfacht wird.

### 2. Verfügbare Tools (2025/2026)
| Tool | Funktion | Kosten | Relevanz |
|------|----------|--------|----------|
| **ScrapeGraphAI** | LLM-powered web scraping | Open source | ✅ Schema-driven extraction |
| **Browse.ai** | No-code web monitoring | $49/mo | ✅ Monitoring für laufende Kandidaten |
| **Diffbot** | Adaptive scraping + Knowledge Graph | Enterprise | 🟡 Overkill für uns |
| **scrapy-llm** | LLM in Scrapy-Pipeline | Open source | ✅ Entity extraction + normalization |
| **Firecrawl** | Web→Markdown für LLMs | Open source + API | ✅ Seiteninhalt als LLM-Input |
| **Jina Reader** | URL→LLM-ready text | Free API | ✅ Schnelle Content-Extraktion |

### 3. Die Pipeline (SOLL)
```
Phase 1: COLLECT (automatisch, ~5 min)
├── Google News API → Kandidatenname + Gemeinde → Top 20 Artikel
├── Wikipedia API → Gemeinde-Seite → Strukturierte Daten
├── Kandidaten-Website → Firecrawl → Markdown
├── Handelsregister → Firmenbeteiligungen
├── Social Media → LinkedIn (manuell), Facebook (öffentlich)
└── Wahlprogramm PDF → Text-Extraktion

Phase 2: EXTRACT (LLM, ~10 min)
├── NER: Personen, Organisationen, Orte, Daten
├── Sentiment: Pro/Contra Kandidat in jedem Artikel
├── Zusammenfassung: Jeder Artikel → 2 Sätze
├── Themen-Klassifikation: Wirtschaft, Soziales, Verkehr etc.
└── Beziehungs-Extraktion: "X ist Vorsitzender von Y"

Phase 3: STRUCTURE (Template, ~5 min)
├── JSON nach SCHEMA.md generieren
├── Placeholder-Constants füllen
├── Talking Points generieren (LLM + Quellenverweise)
└── Netzwerk-Graph-Daten berechnen

Phase 4: HUMAN QA (~45 min ⚠️ nicht automatisierbar)
├── E/I/J/A für jeden Datenpunkt vergeben
├── Faktencheck: Stimmen die extrahierten Beziehungen?
├── Ton-Check: Sind Talking Points neutral genug?
├── Vollständigkeit: Fehlen wichtige Kandidaten/Themen?
└── Final sign-off
```

### 4. OSINT für Politiker — Was schon existiert
- **RECON VILLAGE Talk**: "Applied OSINT for Politics" — systematische Methoden für Politiker-Recherche aus öffentlichen Quellen. Techniken: Handelsregister, Parteispenden-Datenbank, Social Media Cross-Referencing. **[B2]** TIB AV-Portal
- **Virginia Tech OSINT Ethics**: Entwickeln ein Ethics Framework für politisches OSINT. Wichtig für uns: **Wir dürfen das** (alles öffentlich), aber wir MÜSSEN transparent sein über Quellen. **[A2]** Virginia Tech, Sep 2025

### 5. ADR-002 Constraint: KEIN LLM in der Produktionskette
Unsere eigene Regel: "No LLM for production chain — hallucination risk = project end."

**Lösung:** LLM für VORARBEIT (Sammlung, Extraktion, Entwurf), aber MENSCH für Endprodukt (E/I/J/A, Faktencheck, Final). LLM output wird NIE ungeprüft zum Kunden geschickt.

---

## GAPS & UNCERTAINTIES
1. **Lokale Pressequalität**: Kleine Gemeinden haben wenig Online-Presse. Für Gemeinden <5.000 EW gibt es oft nur die lokale Tageszeitung (Paywall)
2. **Paywall-Problem**: SZ, Donaukurier, Merkur — die besten Quellen sind hinter Paywalls
3. **Handelsregister-Zugang**: Kostet €4,50/Auszug. Bei 50 Kandidaten × 3 Personen = €675
4. **LLM-Qualität für deutsche Kommunalpolitik**: Aktuelle Modelle kennen Ottobrunn, aber nicht Dinkelsbühl-Interna

---

## IMPLEMENTATION PLAN

### Phase 1: Quick Wins (diese Woche)
| Was | Tool | Zeitersparnis |
|-----|------|--------------|
| Artikel-Sammlung automatisieren | Google News API + Firecrawl | -30 min/Analyse |
| Wikipedia-Daten automatisch extrahieren | Wikipedia API | -10 min |
| JSON-Template automatisch füllen | Script (generate-v2.js erweitern) | -15 min |

### Phase 2: Mittelfristig (nach 10 Kunden)
| Was | Tool | Zeitersparnis |
|-----|------|--------------|
| NER + Beziehungsextraktion | GPT-4o / Claude + Prompt-Template | -20 min |
| Sentiment pro Artikel | Classifier-Prompt | -10 min |
| Netzwerk-Graph automatisch | Beziehungsdaten → D3.js | -15 min |

### Phase 3: Langfristig (nach 50 Kunden)
| Was | Tool | Zeitersparnis |
|-----|------|--------------|
| QA-Hire für E/I/J/A | Werkstudent (€15/h) | Florians Zeit = 0 |
| Monitoring-Dashboard | Browse.ai / Custom | Automatische Alerts |
| Full Pipeline CLI | `ainary build --gemeinde Dinkelsbühl` | One-Command-Build |

### Ziel-Zeiten
| Phase | Zeit/Analyse | Florians Arbeit |
|-------|-------------|-----------------|
| Heute | 3h 20min | 3h 20min |
| Phase 1 | 2h 15min | 2h 15min |
| Phase 2 | 1h 15min | 45 min (QA only) |
| Phase 3 | 1h | 0 min (QA-Hire) |

---

## SOURCES
```
[B2] AI Data Scraping 2026, Startup House → startup-house.com/blog/...
[B2] Top 5 Web Scraping AI Agents, GPTBots → gptbots.ai/blog/...
[B2] Best AI Web Scraping Tools, AIMultiple → research.aimultiple.com/ai-web-scraping/
[B2] ScrapeGraphAI → scrapegraphai.com
[B2] Browse.ai → browse.ai
[B2] Applied OSINT for Politics, RECON VILLAGE → av.tib.eu/media/39947
[A2] OSINT Ethics Framework, Virginia Tech → news.vt.edu/articles/2025/...
[B2] OSINT Tools 2025, Talkwalker → talkwalker.com/blog/best-osint-tools
[B2] OSINT Tools 2025, Social Links → blog.sociallinks.io/top-10-osint-tools...
```

---

*Report 3/10 complete. ♔*
