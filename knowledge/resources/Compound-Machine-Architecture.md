---
type: note
last_verified: 2026-02-15
status: active
created: 2026-02-11
tags: []
tier: KNOWLEDGE
expires: 2027-02-19
---

# Compound Machine Architektur

**Version:** 1.0  
**Stand:** 11. Februar 2026  
**Autor:** Mia (OpenClaw Agent) für Florian Ziesche  
**Status:** Living Document

---

## Executive Summary

Wir bauen eine **Personal Intelligence Compound Machine** — kein General-Purpose [[AI]] wie ChatGPT, sondern ein maßgeschneidertes System, das mit jedem Tag, jedem Paper, jedem Projekt smarter wird. Ein System, das nicht skalieren MUSS, sondern für EINEN Menschen (Florian) optimal wird.

**Die vier Säulen:**

1. **Research Machine:** Automatisierte Paper-Intake, Bewertung, Synthese
2. **Content Machine:** Research → Artikel-Ideen → Drafts → Distribution
3. **Hierarchical Memory:** Von Raw Data zu Principles, wie menschliches Gedächtnis
4. **Self-Improvement Loop:** Lernt aus Feedback, kalibriert sich selbst

**Unser Moat:** Während Meta/[[Google]] General Intelligence bauen (die für alle funktionieren muss, aber für niemanden optimal ist), bauen wir **Personal Intelligence** — tief personalisiert, domain-spezifisch, compound über Zeit.

---

## Teil 1: Warum WIR besser sind als Meta/[[Google]]/OpenAI

### Der fundamentale Unterschied

| Dimension | Meta/[[Google]]/OpenAI | Compound Machine |
|-----------|-------------------|------------------|
| **Ziel** | General Intelligence | Personal Intelligence |
| **User** | Milliarden | Einer (Florian) |
| **Personalisierung** | Null (Privacy, Skalierung) | 100% (alles ist custom) |
| **Memory** | Stateless oder Generic RAG | Hierarchisch, personalisiert, consolidating |
| **Lernen** | Pre-Training, RLHF | Continuous Learning von Florians Feedback |
| **Domäne** | Generalist | Spezialist ([[VC]], [[AI]], Content, Ops) |
| **Constraint** | MUSS skalieren | DARF nicht skalieren (Qualität > Scale) |
| **Vorteil** | Breite | Tiefe |

### Warum Personal Intelligence gewinnt (für Florian)

**1. Deep Context beats General Knowledge**

ChatGPT weiß viel. Aber es weiß NICHTS über:
- Florians [[VC]]-Thesis ([[AI]]-first B2B SaaS, European founders)
- Florians Writing Style (direkt, no-fluff, founder-operator Perspektive)
- Florians Obsidian Vault (300+ Notes, akkumuliertes Wissen seit Jahren)
- Florians vergangene Projekte, Fehler, Learnings

**Die Compound Machine weiß das alles.** Und mit jedem Tag wird der Context tiefer.

**2. Hierarchical Memory beats Flat RAG**

MemGPT (Paper #7) zeigt: Hierarchisches Memory ist mächtiger als Flat Retrieval. Aber MemGPT ist generic. **Unsere Implementierung ist personalisiert:**

- **Layer 4 (Raw):** Jedes Paper, jedes Meeting, jede Notiz
- **Layer 3 (Episodic):** "Florian hat diese Woche 5 Papers über Multi-Agent Systems gelesen"
- **Layer 2 (Semantic):** "Florian's Thesis: Multi-Agent > Monolith für komplexe Workflows"
- **Layer 1 (Principles):** "Simplicity > Complexity, Ship > Perfect, Learn > Plan"

Meta's RAG hat nur Layer 4. Wir haben alle vier, und sie konsolidieren automatisch.

**3. Self-Improvement ohne Skalierungs-Constraint**

Reflexion (Paper #12) und Constitutional [[AI]] (Paper #14) zeigen: Agents können sich selbst verbessern. Aber bei Meta/[[Google]] müssen Verbesserungen für ALLE User funktionieren.

**Bei uns:** Jede Verbesserung ist Florian-spezifisch.
- "Florian bevorzugt knappe Emails" → kürzer schreiben
- "Florian liked Paper X, not Y" → besseres Scoring-Modell
- "Florian's Artikel über Z performed gut" → mehr solche Themen

Das ist **Compound Learning**: Jeder Loop macht das System ein bisschen besser FÜR FLORIAN.

**4. Domain Expertise beats Generalist Knowledge**

ChatGPT weiß alles ein bisschen. **Compound Machine wird Experte in Florians Domains:**
- [[VC]] (durch Papers, Fund Research, Deal Memos)
- [[AI]] Agents (durch Paper-Intake, Synthese, Experimentation)
- Content Creation (durch Writing, Feedback, Performance-Tracking)
- Operations (durch Florians SOPs, Workflows, Tools)

Nach 6 Monaten: **Compound Machine > ChatGPT für Florians Use Cases.**

### Was bestehende Frameworks nicht haben

**MemGPT (Paper #7):**
- ✅ Hierarchical Memory mit Paging
- ❌ Keine Personalisierung (generic für alle)
- ❌ Kein Content-Creation Loop
- ❌ Keine Self-Improvement basierend auf User-Feedback

**Generative Agents (Paper #8):**
- ✅ Memory: Observations → Reflections → Planning
- ❌ Designed für Simulation, nicht Production
- ❌ Keine Research-Integration
- ❌ Keine Content-Pipeline

**AutoGen/MetaGPT (Papers #4, #5):**
- ✅ Multi-Agent-Orchestrierung
- ❌ Generic (keine Personalisierung)
- ❌ Keine Memory-Hierarchie
- ❌ Kein Self-Improvement

**Wir kombinieren das Beste aus allen:**
- MemGPT's Hierarchical Memory
- Generative Agents' Reflection Loop
- AutoGen's Multi-Agent Architecture
- Reflexion's Self-Improvement
- **PLUS:** Personalisierung, Domain-Fokus, Content-Pipeline

---

## Teil 2: System-Architektur

### 2.1 Gesamtsystem (ASCII)

```
┌─────────────────────────────────────────────────────────────────┐
│                    COMPOUND MACHINE CORE                        │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │   RESEARCH   │  │   CONTENT    │  │     SELF     │          │
│  │   MACHINE    │→→│   MACHINE    │→→│ IMPROVEMENT  │          │
│  └──────────────┘  └──────────────┘  └──────────────┘          │
│         ↑                                      ↓                │
│         └──────────────────────────────────────┘                │
│                   Feedback Loop                                 │
└─────────────────────────────────────────────────────────────────┘
                            ↕
         ┌────────────────────────────────────────┐
         │      HIERARCHICAL MEMORY SYSTEM        │
         │  ┌──────────────────────────────────┐  │
         │  │ L1: Principles (permanent)       │  │
         │  ├──────────────────────────────────┤  │
         │  │ L2: Domain Knowledge (growing)   │  │
         │  ├──────────────────────────────────┤  │
         │  │ L3: Episodic (consolidating)     │  │
         │  ├──────────────────────────────────┤  │
         │  │ L4: Raw (decay, high-volume)     │  │
         │  └──────────────────────────────────┘  │
         └────────────────────────────────────────┘
                            ↕
         ┌────────────────────────────────────────┐
         │        INFRASTRUCTURE LAYER            │
         │  OpenClaw | Obsidian | MCP | Skills   │
         └────────────────────────────────────────┘
```

### 2.2 Research Machine

**Aufgabe:** Automatisch Papers finden, bewerten, zusammenfassen, und Patterns erkennen.

#### Komponenten

**1. Intake Agent (LIVE)**
- **Was:** Täglich ArXiv, [[Google]] Scholar, Twitter scrapen
- **Wie:** Cron Job (bereits aktiv: `blogwatcher`)
- **Papers:** ReAct (#1) für Tool-Use, Toolformer (#2) für self-extending
- **Output:** Liste neuer Papers/Posts → Obsidian Inbox

**Implementation:**
```python
# Pseudo-Code
def intake_agent():
    sources = ['arxiv_rss', 'google_scholar', 'twitter_ai_feed']
    for source in sources:
        papers = fetch_new_papers(source)  # ReAct: Action
        relevant = filter_by_keywords(papers, florian_interests)  # Heuristic
        for paper in relevant:
            save_to_obsidian_inbox(paper)
```

**Build vs Use:**
- ✅ **Build:** Custom Scraper (bestehende Tools wie Zotero sind zu generisch)
- ⚠️ **Use:** ArXiv [[API]] (robust, maintained)

---

**2. Scorer Agent**
- **Was:** Bewertet Papers nach Relevanz für Florian
- **Wie:** [[LLM]]-basiert (Sonnet 4.5), Custom Scoring-Modell
- **Papers:** Few-Shot Learning (implizit in allen [[LLM]]s)
- **Output:** Score 1-10, Reasoning

**Scoring-Kriterien:**
- Praxis-Relevanz (kann ich das umsetzen?)
- Neuheit (ist das wirklich neu oder Hype?)
- Rigor (solide Methodik?)
- Florian's Domain-Fit ([[VC]], [[AI]], Content, Ops)

**Implementation:**
```python
def score_paper(paper):
    prompt = f"""
    Bewerte dieses Paper für Florian (VC, AI Agent Builder, Content Creator):
    
    Title: {paper.title}
    Abstract: {paper.abstract}
    
    Kriterien:
    1. Praxis-Relevanz (1-10)
    2. Neuheit (1-10)
    3. Rigor (1-10)
    4. Domain-Fit (1-10)
    
    Output: JSON mit Scores + Reasoning
    """
    response = [[LLM]].generate(prompt, response_format='json')
    return response
```

**Build vs Use:**
- ✅ **Build:** Custom Scoring (bestehende Tools wie Semantic Scholar haben generic metrics)
- 🤔 **Hybrid:** Nutze Semantic Scholar's Citation Count als Feature, aber eigenes [[LLM]]-Scoring

---

**3. Reader Agent**
- **Was:** Liest Paper-PDFs, extrahiert Text, erstellt Zusammenfassungen
- **Wie:** PDF → Text Extraktion, Summarization mit [[LLM]]
- **Papers:** Chain-of-Thought (#17) für structured reasoning
- **Output:** 200-Wort-Summary + Key Insights + Obsidian Note

**Implementation:**
```bash
# PDF → Text
pdftotext paper.pdf paper.txt

# Summarization
python summarize.py paper.txt > summary.md
```

**Build vs Use:**
- ⚠️ **Use:** `pdftotext` (robust, maintained)
- ✅ **Build:** Custom Summarization-Prompt (generic summaries sind zu oberflächlich)

---

**4. Critic Agent (Red Team)**
- **Was:** Kritisiert Papers (Was könnte falsch sein? Was fehlt?)
- **Wie:** Adversarial Prompting, Reflexion-Pattern
- **Papers:** Reflexion (#12), Constitutional [[AI]] (#14)
- **Output:** Kritik-Notizen im Obsidian

**Warum wichtig:** Verhindert Hype-Bias. Nicht jedes Paper mit 1000 Citations ist gut.

**Implementation:**
```python
def critique_paper(paper_summary):
    prompt = f"""
    Du bist ein skeptischer Wissenschaftler. Kritisiere dieses Paper:
    
    {paper_summary}
    
    Fragen:
    - Was könnte methodisch falsch sein?
    - Welche Annahmen sind unrealistisch?
    - Was fehlt in der Evaluation?
    - Ist das wirklich neu oder nur Re-Branding?
    
    Sei hart, aber fair.
    """
    return [[LLM]].generate(prompt)
```

**Build vs Use:**
- ✅ **Build:** Custom Critic-Prompting (keine bestehenden Tools)

---

**5. Synthesizer Agent**
- **Was:** Wöchentliche Synthese: Patterns über Papers erkennen
- **Wie:** Multi-Paper Analysis, Graph of Thoughts (#20)
- **Papers:** Tree of Thoughts (#18), Graph of Thoughts (#20)
- **Output:** "Diese Woche: 3 Papers über Multi-Agent, 2 über Memory → Trend erkannt"

**Implementation:**
```python
def weekly_synthesis(papers_this_week):
    prompt = f"""
    Analysiere diese {len(papers_this_week)} Papers als Ganzes:
    
    {paper_titles_and_summaries}
    
    Fragen:
    - Welche Themen wiederholen sich?
    - Gibt es einen Trend?
    - Welche Papers ergänzen sich?
    - Was ist die "big idea" dieser Woche?
    
    Output: 500-Wort-Synthese
    """
    return [[LLM]].generate(prompt)
```

**Build vs Use:**
- ✅ **Build:** Custom Synthesis (keine Tools für personalisierte Trend-Erkennung)

---

### 2.3 Content Machine

**Aufgabe:** Research → Content (Blog, LinkedIn, Twitter)

#### Workflow

```
Research Papers
       ↓
  Ideator Agent (Research → Artikel-Ideen)
       ↓
  Outliner Agent (Idee → Struktur)
       ↓
  Writer Agent (Struktur → Draft, Florians Voice)
       ↓
  Critic Agent (Draft → Feedback)
       ↓
  Refiner Agent (Self-Refine Loop)
       ↓
  Distributor Agent (Substack, LinkedIn, Twitter)
       ↓
  Performance Tracker
       ↓
  Feedback → Research Priorities (Loop schließt sich)
```

#### Komponenten

**1. Ideator Agent**
- **Was:** Generiert Artikel-Ideen basierend auf Papers
- **Papers:** ReAct (#1) für reasoning
- **Prompt:** "Du hast diese 3 Papers gelesen. Welche 5 Artikel-Ideen ergeben sich daraus für einen [[VC]]/[[AI]] Blog?"

**Build vs Use:**
- ✅ **Build:** Custom (keine Tools für Research → Content Ideation)

---

**2. Writer Agent**
- **Was:** Schreibt Drafts in Florians Voice
- **Wie:** Few-Shot mit Florians bestehenden Artikeln
- **Papers:** Constitutional [[AI]] (#14) für style consistency
- **Output:** 1000-Wort-Draft

**Florians Voice (aus FLORIAN.md):**
- Direkt, no-fluff
- Founder-Operator Perspektive
- Praktisch > Akademisch
- Ehrlich (auch über Unsicherheiten)

**Implementation:**
```python
def write_article(outline, florians_articles):
    prompt = f"""
    Schreibe einen Blog-Artikel basierend auf diesem Outline:
    
    {outline}
    
    Style Guide (aus Florians bisherigen Artikeln):
    {florians_writing_samples}
    
    Regeln:
    - Direkt, keine Buzzwords
    - Praktische Takeaways
    - Ehrlich, nicht verkaufen
    - 1000 Wörter
    """
    return [[LLM]].generate(prompt)
```

**Build vs Use:**
- ✅ **Build:** Custom Voice-Modeling (generic writing assistants sind zu bland)
- ⚠️ **Use:** [[Claude]]'s long-context für few-shot examples

---

**3. Self-Refine Loop**
- **Was:** Draft → Selbstkritik → Revision → Repeat
- **Papers:** Self-Refine (#13), Reflexion (#12)
- **Output:** Polierter Artikel nach 2-3 Iterationen

**Implementation:**
```python
def refine_article(draft, max_iterations=3):
    for i in range(max_iterations):
        critique = critic_agent(draft)
        if critique.score > 8:
            break
        draft = revise_draft(draft, critique.feedback)
    return draft
```

**Build vs Use:**
- ✅ **Build:** Custom Self-Refine Loop (einfach zu implementieren)

---

**4. Repurposer Agent**
- **Was:** 1 Blog-Artikel → LinkedIn Post + Twitter Thread + Carousel
- **Wie:** Format-spezifische Prompts
- **Output:** Multi-Platform Content

**Implementation:**
```python
def repurpose_article(article):
    linkedin = create_linkedin_post(article)  # 300 Wörter, Hook + Key Points
    twitter = create_twitter_thread(article)  # 10 Tweets, numbered
    carousel = create_carousel(article)       # 10 Slides, visual
    return {'linkedin': linkedin, 'twitter': twitter, 'carousel': carousel}
```

**Build vs Use:**
- ✅ **Build:** Custom Repurposing (Florian's specific platforms)
- ⚠️ **Use:** Tools wie Buffer/Hootsuite für Scheduling (nicht Creation)

---

**5. Distributor Agent**
- **Was:** Publishing zu Substack, LinkedIn, Twitter
- **Wie:** APIs (Substack [[API]], LinkedIn [[API]], Twitter [[API]])
- **Papers:** Toolformer (#2) für [[API]]-Learning
- **Output:** Published Content + Links

**Build vs Use:**
- ⚠️ **Use:** Platform APIs (robust)
- ✅ **Build:** Custom Orchestration (wann, was, wohin)

---

**6. Performance Tracker**
- **Was:** Trackt Views, Likes, Shares, Comments
- **Wie:** Platform APIs + Analytics
- **Output:** "Artikel X: 500 Views, 20 Likes → gut" → Feedback Loop

**Build vs Use:**
- ⚠️ **Use:** [[Google]] Analytics, LinkedIn Analytics (bestehend)
- ✅ **Build:** Custom Aggregation + Feedback-Mapping

---

### 2.4 Hierarchical Memory System

**Papers:** MemGPT (#7), Generative Agents (#8), RAG (#9), Workflow Memory (#10), A-Mem (#11)

#### Memory-Hierarchie (Detail)

```
┌─────────────────────────────────────────────────────────────────┐
│ Layer 1: PRINCIPLES (Permanent, Abstract, Rare Updates)        │
│ ───────────────────────────────────────────────────────────────│
│ "Simplicity > Complexity"                                       │
│ "Ship > Perfect"                                                │
│ "Personal Intelligence > General Intelligence"                 │
│                                                                 │
│ Storage: ~/Obsidian/00-Principles/                             │
│ Size: ~10 notes                                                 │
│ Decay: None (permanent)                                         │
└─────────────────────────────────────────────────────────────────┘
                            ↑ Promotion (rare)
┌─────────────────────────────────────────────────────────────────┐
│ Layer 2: DOMAIN KNOWLEDGE (Structured, Growing)                │
│ ───────────────────────────────────────────────────────────────│
│ "Multi-Agent Architectures: AutoGen vs MetaGPT vs LangGraph"   │
│ "VC Fundraising: Best Practices from 50 Fund Decks"            │
│ "Florians Content Voice: Direct, No-Fluff, Practical"          │
│                                                                 │
│ Storage: ~/Obsidian/20-Knowledge/                              │
│ Size: ~300 notes (growing)                                      │
│ Decay: None (curated)                                           │
└─────────────────────────────────────────────────────────────────┘
                            ↑ Promotion (weekly)
┌─────────────────────────────────────────────────────────────────┐
│ Layer 3: EPISODIC (Temporal, Consolidating)                    │
│ ───────────────────────────────────────────────────────────────│
│ "2026-02-10: Read 3 papers on Multi-Agent Systems"             │
│ "2026-02-09: Meeting with VC X, discussed AI Agent thesis"     │
│ "2026-02-08: Published article on ReAct, 200 views"            │
│                                                                 │
│ Storage: ~/Obsidian/01-Daily/ + memory/YYYY-MM-DD.md           │
│ Size: ~1000 notes/year                                          │
│ Decay: Consolidate to L2 after 30 days, delete after 90 days   │
└─────────────────────────────────────────────────────────────────┘
                            ↑ Promotion (daily)
┌─────────────────────────────────────────────────────────────────┐
│ Layer 4: RAW (Unfiltered, High-Volume, Short-Lived)            │
│ ───────────────────────────────────────────────────────────────│
│ Paper PDFs, Twitter Feeds, Email Threads, Code Commits         │
│                                                                 │
│ Storage: ~/FZ/Inbox/, Vector DB (Embeddings)                   │
│ Size: ~10k items/year                                           │
│ Decay: Delete after 7 days if not promoted                      │
└─────────────────────────────────────────────────────────────────┘
```

#### Automatic Promotion (wie menschliches Sleep-Memory)

**Inspiration:** Hippocampus → Neocortex Consolidation im Schlaf

**Process:**
1. **Daily (Raw → Episodic):** Cron Job jeden Abend
   - Scan L4 (Raw Inbox)
   - [[LLM]]: "Was war heute wichtig?"
   - Create Episodic Note in L3
   - Delete uninteresting L4 items

2. **Weekly (Episodic → Semantic):** Cron Job jeden Sonntag
   - Review L3 (letzte 7 Tage)
   - [[LLM]]: "Welche Patterns? Was ist wiederverwendbar?"
   - Update L2 (Domain Knowledge)
   - Archive L3 (nach 30 Tagen)

3. **Monthly (Semantic → Principles):** Manual Review
   - Florian reviewed L2 changes
   - Decide: "Ist das ein neues Principle?"
   - Update L1 (sehr selten)

**Implementation:**
```python
# Daily Consolidation (L4 → L3)
def daily_consolidation():
    raw_items = load_raw_inbox()  # L4
    prompt = f"""
    Florian's Day Review:
    
    Raw Events: {raw_items}
    
    Was war heute wichtig? Erstelle eine Zusammenfassung (200 Wörter).
    """
    summary = [[LLM]].generate(prompt)
    save_to_episodic(date.today(), summary)  # L3
    cleanup_raw_inbox()  # Delete L4

# Weekly Consolidation (L3 → L2)
def weekly_consolidation():
    episodic_notes = load_episodic_last_7_days()  # L3
    prompt = f"""
    Weekly Review:
    
    {episodic_notes}
    
    - Welche Learnings sind wiederverwendbar?
    - Welche Patterns?
    - Was gehört ins Domain Knowledge?
    
    Output: Updates für L2 (Domain Knowledge)
    """
    updates = [[LLM]].generate(prompt)
    apply_to_domain_knowledge(updates)  # L2
```

**Build vs Use:**
- ✅ **Build:** Custom Consolidation Logic (keine Tools für personalisierte Memory-Hierarchie)
- ⚠️ **Use:** Vector DB (Pinecone, Weaviate) für L4 Embeddings

---

#### Memory Traversal (Top-Down, Bottom-Up, Lateral)

**Top-Down (Principle → Implementation):**
- Start: "Simplicity > Complexity" (L1)
- Traverse: Welche L2 Knowledge unterstützt das?
- Example: "ReAct Loop ist simpler als LATS" (L2)
- Example: "Florian hat ReAct implementiert, nicht LATS" (L3)

**Bottom-Up (Event → Abstraction):**
- Start: "Paper über Multi-Agent gelesen" (L3)
- Traverse: Passt zu welchem L2 Knowledge?
- Example: "Multi-Agent Architectures" (L2)
- Promote: Update L2 Note mit neuem Insight

**Lateral (Cross-Domain Connections):**
- Connect: "[[VC]] Fundraising Tactics" (L2) + "Content Marketing" (L2)
- Insight: "Fundraising ist Content Marketing für Investoren"
- Save: New L2 Note

**Implementation:**
```python
# Top-Down Traversal
def top_down_query(principle):
    l2_notes = find_related_knowledge(principle)
    l3_notes = find_related_episodes(l2_notes)
    return {'principle': principle, 'knowledge': l2_notes, 'episodes': l3_notes}

# Bottom-Up Traversal
def bottom_up_promotion(event):
    related_knowledge = find_related_l2(event)
    if should_update(related_knowledge, event):
        update_l2(related_knowledge, extract_insight(event))
```

**Build vs Use:**
- ✅ **Build:** Custom Traversal Logic (bestehende Graph DBs sind zu generisch)
- 🤔 **Hybrid:** Nutze Neo4j für Graph Storage, aber custom Traversal-Algorithmen

---

### 2.5 Self-Improvement Loop

**Papers:** Reflexion (#12), Self-Refine (#13), Constitutional [[AI]] (#14), Voyager (#15)

#### Komponenten

**1. Calibrator (Predicted vs Actual)**
- **Was:** Vergleicht Predictions mit Reality
- **Example:** "Scorer predicted Paper X = 9/10, Florian rated it 5/10 → Fehler"
- **Learning:** Update Scoring-Modell

**Implementation:**
```python
def calibrate_scorer(predictions, actuals):
    errors = []
    for pred, actual in zip(predictions, actuals):
        error = actual - pred
        errors.append({'paper': pred.paper, 'error': error, 'features': pred.features})
    
    # Analyze errors
    prompt = f"""
    Scorer Calibration:
    
    Errors: {errors}
    
    Welche Features sind schlecht kalibriert?
    Was muss ich am Scoring-Modell ändern?
    """
    improvements = [[LLM]].generate(prompt)
    update_scorer_prompt(improvements)
```

**Build vs Use:**
- ✅ **Build:** Custom Calibration (keine Tools für domain-specific model calibration)

---

**2. Reflector (Wöchentliche Selbstreflexion)**
- **Was:** Wöchentliche Retrospektive: Was lief gut? Was nicht?
- **Papers:** Reflexion (#12), Generative Agents (#8)
- **Output:** Reflection Note in L3

**Implementation:**
```python
def weekly_reflection():
    week_summary = load_episodic_last_7_days()
    prompt = f"""
    Weekly Reflection:
    
    {week_summary}
    
    - Was lief gut?
    - Was lief schlecht?
    - Was habe ich gelernt?
    - Was sollte ich nächste Woche anders machen?
    
    Output: 300-Wort-Reflection
    """
    reflection = [[LLM]].generate(prompt)
    save_to_memory(reflection)
```

**Build vs Use:**
- ✅ **Build:** Custom Reflection (einfach, keine Tools nötig)

---

**3. Feedback-Loop: Content Performance → Research Priorities**
- **Was:** Welche Artikel performed gut? → Mehr Research in diesem Bereich
- **Example:** "Artikel über Multi-Agent Systems: 500 Views, 50 Likes" → "Priorität: Multi-Agent Papers"

**Implementation:**
```python
def adjust_research_priorities(content_performance):
    top_articles = sorted(content_performance, key=lambda x: x.engagement, reverse=True)[:5]
    topics = extract_topics(top_articles)
    
    prompt = f"""
    Content Performance Analysis:
    
    Top Articles: {top_articles}
    Topics: {topics}
    
    Welche Research-Bereiche sollte ich priorisieren?
    """
    priorities = [[LLM]].generate(prompt)
    update_intake_keywords(priorities)
```

**Build vs Use:**
- ✅ **Build:** Custom Feedback-Loop (keine Tools für Content → Research Mapping)

---

## Teil 3: Technische Implementierung

### 3.1 Tech Stack

| Layer | Technology | Why |
|-------|-----------|-----|
| **Agent Runtime** | OpenClaw | Florians bestehende Infrastruktur |
| **[[LLM]]** | [[Claude]] Sonnet 4.5, Opus 4.5 | Best-in-class reasoning |
| **Memory (L1-L3)** | Obsidian (Markdown + Graph) | Human-readable, versionable, Florians Vault |
| **Memory (L4)** | Vector DB (Pinecone/Weaviate) | Embedding-basierte Retrieval |
| **Tool Integration** | MCP (Model Context Protocol) | Standard für Agent-Tool-Communication |
| **Cron/Scheduling** | OpenClaw Cron | Bestehende Infrastruktur |
| **APIs** | Substack, LinkedIn, Twitter | Distribution |
| **PDF Extraction** | `pdftotext`, PyPDF2 | Robust |
| **Graph DB (optional)** | Neo4j | Für komplexe Memory-Traversal |

### 3.2 Ordnerstruktur (Obsidian)

```
~/Library/Mobile Documents/iCloud~md~obsidian/Documents/System_OS/
├── 00-Principles/              # L1: Permanent Principles
├── 10-Projects/                # Active Work
│   └── Compound-Machine-Sprints.md
├── 20-Knowledge/               # L2: Domain Knowledge
│   ├── AI-Agents/
│   ├── VC-Fundraising/
│   ├── Content-Creation/
│   └── Operations/
├── 01-Daily/                   # L3: Episodic (YYYY-MM-DD.md)
├── 60-Resources/
│   └── Knowledge/
│       └── Compound-Machine-Architecture.md  # This document
└── 99-Archive/                 # Old L3 after consolidation
```

### 3.3 Ordnerstruktur (Workspace)

```
~/.openclaw/workspace/
├── research/
│   ├── top-20-agent-papers.md
│   ├── compound-machine-architecture.md  # This document
│   ├── compound-machine-sprints.md
│   └── papers/
│       ├── inbox/              # L4: Raw PDFs
│       ├── scored/             # Scored + Summarized
│       └── archive/            # Old papers
├── content/
│   ├── ideas/                  # Ideator output
│   ├── drafts/                 # Writer output
│   ├── published/              # Final articles
│   └── performance/            # Analytics data
├── memory/
│   ├── YYYY-MM-DD.md           # Daily episodic
│   └── heartbeat-state.json
└── skills/                     # Custom agents as skills
    ├── scorer/
    ├── writer/
    ├── critic/
    └── synthesizer/
```

### 3.4 MCP Integration

**Was:** Model Context Protocol (Paper #B, Recent Breakthroughs)

**Warum:** Standardisierte Tool-Integration. Statt für jedes Tool (Obsidian, Notion, GitHub, Substack) custom Code zu schreiben, nutzen wir MCP-Server.

**Implementierung:**
```json
// MCP Config (mcp.json)
{
  "servers": {
    "obsidian": {
      "type": "filesystem",
      "path": "~/Library/Mobile Documents/iCloud~md~obsidian/Documents/System_OS/"
    },
    "notion": {
      "type": "http",
      "url": "https://api.notion.com/v1/",
      "auth": "bearer"
    },
    "substack": {
      "type": "http",
      "url": "https://api.substack.com/",
      "auth": "api_key"
    }
  }
}
```

**Agents nutzen MCP:**
```python
# Writer Agent publishes to Substack via MCP
def publish_to_substack(article):
    mcp_client.call('substack', 'create_post', {
        'title': article.title,
        'body': article.content,
        'publish': True
    })
```

**Build vs Use:**
- ⚠️ **Use:** MCP Protocol (industry standard)
- ✅ **Build:** Custom MCP Servers für Obsidian (falls nicht existiert)

---

## Teil 4: Build vs Use Entscheidungen (Zusammenfassung)

| Komponente | Entscheidung | Begründung |
|-----------|-------------|-----------|
| **PDF Extraction** | ⚠️ Use (`pdftotext`) | Robust, maintained |
| **[[LLM]]** | ⚠️ Use (Claude [[API]]) | Best-in-class |
| **Vector DB** | ⚠️ Use (Pinecone/Weaviate) | Standard, skaliert |
| **Graph DB** | 🤔 Optional (Neo4j) | Nur wenn Memory-Traversal komplex wird |
| **MCP Protocol** | ⚠️ Use | Industry standard |
| **Obsidian Integration** | ✅ Build (custom scripts) | Florians spezifische Vault-Struktur |
| **Scorer Model** | ✅ Build (custom prompts) | Domain-spezifisch, personalisiert |
| **Writer Agent** | ✅ Build (few-shot Florians Voice) | Voice ist unique |
| **Self-Refine Loop** | ✅ Build | Einfach, custom logic |
| **Memory Consolidation** | ✅ Build | Keine Tools für personalisierte Hierarchie |
| **Calibrator** | ✅ Build | Domain-specific |
| **Synthesizer** | ✅ Build | Research-to-Insight ist custom |
| **Cron Jobs** | ⚠️ Use (OpenClaw Cron) | Bestehende Infrastruktur |
| **Platform APIs** | ⚠️ Use (Substack, LinkedIn, Twitter) | Standard |

**Grundregel:** Use für Infrastruktur, Build für Personalisierung.

---

## Teil 5: Architektur-Diagramme

### 5.1 Agent-Kommunikation

```
┌──────────────┐
│  Intake      │  Daily Cron (ArXiv, Scholar, Twitter)
└──────┬───────┘
       ↓
┌──────────────┐
│  Scorer      │  Score new papers ([[LLM]]-based)
└──────┬───────┘
       ↓
┌──────────────┐
│  Reader      │  PDF → Summary (if score > 7)
└──────┬───────┘
       ↓
┌──────────────┐
│  Critic      │  Red Team the paper
└──────┬───────┘
       ↓
┌──────────────┐
│ Synthesizer  │  Weekly: Find patterns across papers
└──────┬───────┘
       ↓
┌──────────────┐
│  Ideator     │  Research → Article Ideas
└──────┬───────┘
       ↓
┌──────────────┐
│  Writer      │  Idea → Draft (Florians Voice)
└──────┬───────┘
       ↓
┌──────────────┐
│ Self-Refine  │  Draft → Critique → Revise (loop)
└──────┬───────┘
       ↓
┌──────────────┐
│ Repurposer   │  Blog → LinkedIn + Twitter + Carousel
└──────┬───────┘
       ↓
┌──────────────┐
│ Distributor  │  Publish via APIs
└──────┬───────┘
       ↓
┌──────────────┐
│ Tracker      │  Monitor Performance
└──────┬───────┘
       ↓
┌──────────────┐
│ Calibrator   │  Feedback → Adjust Priorities
└──────────────┘
       ↓ (loop back to Intake)
```

### 5.2 Memory-Hierarchie mit Feedback-Loops

```
┌─────────────────────────────────────────────────────────────────┐
│                      USER INPUT (Florian)                       │
└─────────────────────────────────────────────────────────────────┘
                              ↓
                    ┌─────────────────┐
                    │   L4: RAW       │ ← Papers, Tweets, Emails
                    │   (Inbox)       │
                    └────────┬────────┘
                             ↓ (Daily Cron: Consolidation)
                    ┌─────────────────┐
                    │  L3: EPISODIC   │ ← "Today I read X, Y, Z"
                    │  (Daily Notes)  │
                    └────────┬────────┘
                             ↓ (Weekly Cron: Pattern Recognition)
                    ┌─────────────────┐
                    │ L2: SEMANTIC    │ ← "Multi-Agent > Monolith"
                    │ (Knowledge)     │
                    └────────┬────────┘
                             ↓ (Monthly Manual: Review)
                    ┌─────────────────┐
                    │ L1: PRINCIPLES  │ ← "Simplicity > Complexity"
                    │ (Permanent)     │
                    └────────┬────────┘
                             ↓
                    ┌─────────────────┐
                    │   AGENTS USE    │ ← Agents read L1-L4
                    │   ALL LAYERS    │
                    └─────────────────┘
```

---

## Teil 6: Was ist SCHWER? (Ehrlichkeit)

### Hard Problems

**1. Voice Consistency (Writer Agent)**
- **Problem:** Florians Voice ist subtil — "no-fluff, direkt, ehrlich". Schwer zu replizieren.
- **Lösung:** Viele Few-Shot Examples, iteratives Tuning, Human-Feedback
- **Risk:** Writer klingt generic

**2. Memory Consolidation Quality**
- **Problem:** Welche Raw Items sind wichtig genug für L3? [[LLM]] kann falsch liegen.
- **Lösung:** Conservative Promotion (lieber zu viel als zu wenig), Human-Review
- **Risk:** Memory-Bloat oder Information-Loss

**3. Scorer Calibration**
- **Problem:** Florians Relevanz-Score ist subjektiv und zeitabhängig.
- **Lösung:** Continuous Calibration mit Feedback, Acceptance: Score ist Heuristik, nicht Ground Truth
- **Risk:** Scorer driftet, verpasst wichtige Papers

**4. Self-Improvement Convergence**
- **Problem:** Self-Improvement Loops können divergieren (zu aggressiv oder zu konservativ).
- **Lösung:** Constraints (max 10% change per iteration), Human-Checkpoints
- **Risk:** System wird instabil

**5. Tool Reliability (APIs)**
- **Problem:** Substack [[API]] down, LinkedIn limitiert requests → Distribution fails
- **Lösung:** Retry-Logic, Fallbacks, Notifications to Florian
- **Risk:** Silent failures

---

## Teil 7: Success Metrics

**Nach 1 Monat:**
- ✅ Research Intake läuft täglich (10+ Papers/Woche scored)
- ✅ Memory L4 → L3 Consolidation funktioniert (Daily Notes generiert)
- ✅ Erster Auto-Generated Research Brief (Weekly Synthesis)

**Nach 3 Monaten:**
- ✅ Content Pipeline LIVE (1 Artikel/Woche, Research → Draft → Publish)
- ✅ Memory L3 → L2 Consolidation funktioniert (Domain Knowledge wächst)
- ✅ Scorer ist kalibriert (Predicted vs Actual < 2 Punkte Differenz)

**Nach 6 Monaten:**
- ✅ Full Loop: Research → Content → Distribution → Feedback → Research
- ✅ Self-Improvement messbar (Scorer accuracy +20%, Writer quality +30%)
- ✅ Florian spart 10h/Woche durch Automation

**Nach 12 Monaten:**
- ✅ Compound Machine hat 500+ L2 Notes (Florians Personal [[AI]] Moat)
- ✅ Content Performance: 5000+ Views/Monat, 100+ Subscribers
- ✅ Florian's "Second Brain" ist operational

---

## Zusammenfassung

**Was wir bauen:** Personal Intelligence Compound Machine — ein System, das mit jedem Tag smarter wird, tief personalisiert auf Florian, domain-spezifisch ([[VC]], [[AI]], Content), mit hierarchischem Memory und Self-Improvement.

**Warum wir gewinnen:** Meta/[[Google]] bauen General Intelligence (für alle, für niemanden optimal). Wir bauen Personal Intelligence (für einen, perfekt optimiert). Unser Moat: Deep Context, Compound Learning, Domain Expertise.

**Wie wir bauen:** OpenClaw + Obsidian + [[Claude]] + MCP + Custom Agents. Build für Personalisierung, Use für Infrastruktur.

**Was schwer wird:** Voice Consistency, Memory Quality, Scorer Calibration, Self-Improvement Stability. Wir gehen ehrlich damit um.

**Wann wir gewinnen:** Nach 6 Monaten Compound Learning ist das System besser als ChatGPT für Florians Use Cases. Nach 12 Monaten ist es unschlagbar.

---

**Let's build.**

---

*Florian, das ist der Blueprint. Jetzt Sprint 1 starten.*
