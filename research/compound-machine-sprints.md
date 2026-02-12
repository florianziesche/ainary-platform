# Compound Machine Sprint-Roadmap

**Version:** 1.0  
**Stand:** 11. Februar 2026  
**Autor:** Mia (OpenClaw Agent) für Florian Ziesche  
**Status:** Execution Roadmap

---

## Overview

**Ziel:** In 5 Wochen von "Research Intake läuft" zu "Full Loop: Research → Content → Distribution → Feedback" kommen.

**Philosophie:**
- **Sprint > Marathon:** Lieber 5 fokussierte Wochen als 6 Monate verwässerte Arbeit
- **Ship Early, Ship Often:** Jeder Sprint endet mit LIVE-Features
- **Iterate, Don't Perfect:** V1 muss funktionieren, nicht perfekt sein
- **Feedback > Planning:** Jeder Sprint basiert auf Learnings vom vorherigen

**Success Criteria:**
- **Nach Sprint 5:** Full Compound Machine läuft autonom
- **Florian's Involvement:** Max 2h/Woche (Review, Feedback, nicht Execution)
- **Output:** 1 Research Brief/Woche, 1 Artikel/Woche, automatisch distribuiert

---

## Sprint Structure (für alle Sprints)

Jeder Sprint folgt diesem Pattern:

1. **WAS:** Welche Features bauen wir?
2. **WARUM:** Warum ist das wichtig? Was unlockt es?
3. **WIE:** Tech-Stack, Implementation, Schritte
4. **DELIVERABLES:** Was ist am Ende LIVE?
5. **ABHÄNGIGKEITEN:** Was brauchen wir vorher?
6. **RISKS:** Was kann schiefgehen?
7. **SUCCESS METRICS:** Wie messen wir Erfolg?

---

# Sprint 1 (Woche 1): Foundation

**Dates:** 11. Feb - 17. Feb 2026  
**Theme:** "Get the Machine Breathing"

## WAS

### 1. Research Intake LIVE machen
- Blogwatcher Cron läuft schon → erweitern zu Multi-Source Scraper
- ArXiv, Google Scholar, Twitter AI-Feed scrapen
- Raw Papers/Posts → Obsidian Inbox

### 2. Paper Index aufsetzen in Obsidian
- Ordnerstruktur: `20-Knowledge/AI-Agents/Papers/`
- Template für Paper-Notes (Title, Authors, Date, ArXiv Link, Status)
- Tagging-System (multi-agent, memory, reasoning, etc.)

### 3. Memory-Hierarchie Ordnerstruktur finalisieren
- L1: `00-Principles/`
- L2: `20-Knowledge/`
- L3: `01-Daily/` (existiert schon)
- L4: `~/FZ/Inbox/` + Vector DB (Setup)

### 4. Erster automatischer Research Brief
- Weekly Synthesis: "Diese Woche: X Papers, Y Themen, Z Trends"
- Cron: Jeden Sonntag 18:00
- Output: Obsidian Note + Telegram Message

---

## WARUM

**Foundation ist alles.** Ohne saubere Intake + Memory-Struktur wird alles chaotisch. Wir brauchen:
- **Automated Intake:** Florian muss nicht manuell Papers suchen
- **Structured Memory:** Papers sind nicht "irgendwo", sondern organisiert und abrufbar
- **First Feedback Loop:** Research Brief = erster Proof-of-Concept, dass das System nützlich ist

**Ohne Sprint 1:** Alles andere baut auf Sand.

---

## WIE

### Tech-Stack
- **Scraping:** Python (`requests`, `BeautifulSoup`, ArXiv API)
- **Storage:** Obsidian (Markdown), Vector DB (Pinecone Free Tier)
- **Cron:** OpenClaw Cron
- **LLM:** Claude Sonnet 4.5

### Implementation Steps

#### 1.1 Multi-Source Scraper (2 Tage)

**ArXiv:**
```python
import arxiv

def scrape_arxiv(query='AI agents', max_results=20):
    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.SubmittedDate
    )
    papers = []
    for result in search.results():
        papers.append({
            'title': result.title,
            'authors': [a.name for a in result.authors],
            'abstract': result.summary,
            'arxiv_id': result.entry_id.split('/')[-1],
            'published': result.published,
            'pdf_url': result.pdf_url
        })
    return papers
```

**Google Scholar (via Serpapi):**
```python
from serpapi import GoogleSearch

def scrape_google_scholar(query='AI agents', num=10):
    params = {
        "engine": "google_scholar",
        "q": query,
        "api_key": os.getenv('SERPAPI_KEY')
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    return results.get('organic_results', [])
```

**Twitter (via API v2):**
```python
import tweepy

def scrape_twitter_ai_feed():
    client = tweepy.Client(bearer_token=os.getenv('TWITTER_BEARER'))
    query = '(AI agents OR LLM agents) lang:en -is:retweet'
    tweets = client.search_recent_tweets(query=query, max_results=20)
    return tweets.data
```

**Orchestration (Daily Cron):**
```python
def daily_intake():
    # Scrape all sources
    arxiv_papers = scrape_arxiv()
    scholar_papers = scrape_google_scholar()
    tweets = scrape_twitter_ai_feed()
    
    # Filter by keywords (Florian's interests)
    keywords = ['multi-agent', 'memory', 'reasoning', 'self-improvement', 'RAG']
    relevant_papers = filter_by_keywords(arxiv_papers + scholar_papers, keywords)
    
    # Save to Obsidian Inbox
    for paper in relevant_papers:
        save_to_obsidian_inbox(paper)
    
    # Log
    print(f"Intake complete: {len(relevant_papers)} papers saved")
```

**Cron Setup:**
```bash
# OpenClaw Cron (every day at 8:00 AM)
0 8 * * * /usr/bin/python3 ~/.openclaw/workspace/skills/intake/daily_intake.py
```

---

#### 1.2 Paper Index + Templates (1 Tag)

**Obsidian Template (`templates/paper-note.md`):**
```markdown
---
title: {{title}}
authors: {{authors}}
date: {{published_date}}
arxiv: {{arxiv_id}}
status: inbox
tags: [paper, {{tags}}]
---

# {{title}}

**Authors:** {{authors}}  
**Date:** {{published_date}}  
**ArXiv:** [{{arxiv_id}}](https://arxiv.org/abs/{{arxiv_id}})  
**Status:** 🟡 Inbox

---

## Abstract

{{abstract}}

---

## Notes

(To be filled by Reader Agent)

---

## Critique

(To be filled by Critic Agent)

---

## Related Papers

- [[]]
```

**Ordnerstruktur:**
```
20-Knowledge/AI-Agents/
├── Papers/
│   ├── inbox/          # New papers, not yet read
│   ├── scored/         # Scored, waiting for Reader
│   ├── reviewed/       # Read + summarized
│   └── archive/        # Old, low-score papers
├── Concepts/
│   ├── Multi-Agent-Architectures.md
│   ├── Memory-Systems.md
│   └── Self-Improvement.md
└── Trends/
    └── 2026-02-weekly-trends.md
```

**Script: `create_paper_note.py`**
```python
def create_paper_note(paper):
    template = load_template('paper-note.md')
    note = template.format(
        title=paper['title'],
        authors=', '.join(paper['authors']),
        published_date=paper['published'],
        arxiv_id=paper['arxiv_id'],
        abstract=paper['abstract'],
        tags='ai-agents'
    )
    
    # Save to Obsidian
    filepath = f"20-Knowledge/AI-Agents/Papers/inbox/{paper['arxiv_id']}.md"
    save_to_obsidian(filepath, note)
```

---

#### 1.3 Memory-Hierarchie Setup (1 Tag)

**L1 (Principles):**
- Manuell: Florian schreibt 5-10 Core Principles
- Example:
```markdown
# Simplicity > Complexity

When in doubt, choose the simpler solution. Complex systems break.

## Examples
- ReAct > LATS (simpler, works)
- Markdown > Database (readable, versionable)
- Few-Shot > Fine-Tuning (faster, cheaper)
```

**L2 (Domain Knowledge):**
- Existierende Obsidian Notes migrieren
- Structure:
```
20-Knowledge/
├── AI-Agents/
├── VC-Fundraising/
├── Content-Creation/
└── Operations/
```

**L3 (Episodic):**
- Existiert schon: `01-Daily/YYYY-MM-DD.md`
- Nichts zu tun

**L4 (Raw):**
- **Filesystem:** `~/FZ/Inbox/`
- **Vector DB:** Pinecone Setup
```python
import pinecone

pinecone.init(api_key=os.getenv('PINECONE_API_KEY'), environment='us-west1-gcp-free')
index = pinecone.Index('florian-memory-l4')

def add_to_vector_db(paper):
    embedding = get_embedding(paper['abstract'])  # OpenAI embeddings
    index.upsert([(paper['arxiv_id'], embedding, {'title': paper['title']})])
```

---

#### 1.4 Weekly Research Brief (2 Tage)

**Synthesizer Agent:**
```python
def weekly_synthesis():
    # Load papers from last 7 days
    papers = load_papers_last_7_days()
    
    # Summarize
    titles = [p['title'] for p in papers]
    abstracts = [p['abstract'][:200] for p in papers]
    
    prompt = f"""
    Diese Woche wurden {len(papers)} Papers zur Inbox hinzugefügt:
    
    {format_papers_list(papers)}
    
    Erstelle einen Research Brief (500 Wörter):
    1. Themen-Übersicht (welche Themen dominieren?)
    2. Top 3 Papers (mit Begründung)
    3. Emerging Trends (was ist neu/interessant?)
    4. Relevanz für Florian (VC, AI Agent Building, Content)
    
    Stil: Direkt, no-fluff, praktisch
    """
    
    brief = llm.generate(prompt)
    
    # Save to Obsidian
    date_str = datetime.now().strftime('%Y-%m-%d')
    save_to_obsidian(f'20-Knowledge/AI-Agents/Trends/weekly-brief-{date_str}.md', brief)
    
    # Send to Telegram
    send_telegram_message(f"📊 Weekly Research Brief:\n\n{brief[:500]}...\n\nFull: [Obsidian Link]")
```

**Cron Setup:**
```bash
# Every Sunday at 6 PM
0 18 * * 0 /usr/bin/python3 ~/.openclaw/workspace/skills/synthesizer/weekly_synthesis.py
```

---

## DELIVERABLES

Am Ende von Sprint 1 (17. Feb):

✅ **Daily Intake läuft:** 10-20 Papers/Tag → Obsidian Inbox  
✅ **Obsidian strukturiert:** L1-L4 Ordner existieren, Paper-Templates ready  
✅ **Vector DB LIVE:** Pinecone läuft, Embeddings für L4  
✅ **Erster Research Brief:** Sonntag 18:00, automatisch generiert + delivered  

**Demo:** Florian zeigt Obsidian Inbox + wöchentlichen Brief

---

## ABHÄNGIGKEITEN

- ✅ OpenClaw Cron (existiert)
- ✅ Obsidian Vault (existiert)
- 🔧 API Keys: ArXiv (free), Serpapi (paid), Twitter (free tier), Pinecone (free tier)
- 🔧 Claude API (existiert)

---

## RISKS

| Risk | Mitigation |
|------|-----------|
| **Scraper fails (Rate Limits)** | Retry-Logic, Backoff, Fallback zu manual links |
| **Obsidian Sync conflicts** | Atomic writes, lock files |
| **Pinecone quota exceeded** | Start small (100 papers), upgrade later |
| **Weekly Brief ist generic** | Iterate on prompt, add few-shot examples |

---

## SUCCESS METRICS

- ✅ 50+ Papers in Obsidian Inbox nach 7 Tagen
- ✅ Erster Weekly Brief delivered (Florian's Rating: 6+/10)
- ✅ Memory-Hierarchie visuell sauber (Florian kann navigieren)
- ✅ Zero manual work (außer Florian's Feedback)

---

# Sprint 2 (Woche 2): Reader + Critic

**Dates:** 18. Feb - 24. Feb 2026  
**Theme:** "From Intake to Insight"

## WAS

### 1. Paper PDF Download + Text-Extraktion
- Automatischer Download von ArXiv PDFs
- PDF → Text Conversion (`pdftotext`)
- Text cleaning + chunking

### 2. Zusammenfassungs-Agent (Reader)
- Liest Paper-Text, erstellt 200-Wort-Summary
- Extrahiert Key Insights (3-5 Bullets)
- Updated Obsidian Note mit Summary

### 3. Praxis-Scoring
- Scorer Agent (LLM-basiert)
- Score 1-10 für: Praxis-Relevanz, Neuheit, Rigor, Domain-Fit
- Saved in Obsidian Frontmatter

### 4. Critic Agent (Red Team)
- Kritisiert Papers: Was fehlt? Was könnte falsch sein?
- Saved als "Critique" Section in Obsidian

---

## WARUM

**Intake allein reicht nicht.** Wir haben jetzt 50+ Papers, aber Florian kann nicht alle lesen. Wir brauchen:
- **Scoring:** Welche Papers sind Worth Reading?
- **Summaries:** Quick Overview ohne Full Read
- **Critique:** Verhindert Hype-Bias, fördert kritisches Denken

**Nach Sprint 2:** Florian kann in 10min durch Summaries scannen und entscheiden: "Das lese ich, das nicht"

---

## WIE

### Implementation Steps

#### 2.1 PDF Download + Text Extraction (1 Tag)

**Download:**
```python
import requests

def download_pdf(arxiv_id, output_dir='~/FZ/Inbox/'):
    url = f'https://arxiv.org/pdf/{arxiv_id}.pdf'
    response = requests.get(url)
    filepath = f'{output_dir}/{arxiv_id}.pdf'
    with open(filepath, 'wb') as f:
        f.write(response.content)
    return filepath
```

**Text Extraction:**
```bash
# Install pdftotext
brew install poppler

# Extract
pdftotext ~/FZ/Inbox/2402.12345.pdf ~/FZ/Inbox/2402.12345.txt
```

**Python Wrapper:**
```python
import subprocess

def extract_text_from_pdf(pdf_path):
    txt_path = pdf_path.replace('.pdf', '.txt')
    subprocess.run(['pdftotext', pdf_path, txt_path])
    with open(txt_path, 'r') as f:
        text = f.read()
    return text
```

**Text Cleaning:**
```python
def clean_paper_text(text):
    # Remove headers, footers, page numbers
    # Keep: Abstract, Introduction, Method, Results, Conclusion
    # This is heuristic-based, not perfect
    sections = extract_sections(text)
    return '\n\n'.join(sections)
```

---

#### 2.2 Zusammenfassungs-Agent (2 Tage)

**Reader Agent:**
```python
def summarize_paper(paper_text, paper_metadata):
    prompt = f"""
    Fasse dieses AI-Paper zusammen für einen VC/AI Practitioner:
    
    Title: {paper_metadata['title']}
    Authors: {paper_metadata['authors']}
    
    Text: {paper_text[:4000]}  # First 4k chars (Abstract + Intro)
    
    Output (200 Wörter):
    1. Kernidee (1 Satz)
    2. Methode (wie funktioniert's?)
    3. Ergebnisse (was kam raus?)
    4. Relevanz (warum wichtig für Practitioners?)
    
    Stil: Direkt, no-fluff, praktisch
    """
    
    summary = llm.generate(prompt, max_tokens=500)
    
    # Extract Key Insights
    insights_prompt = f"""
    Basierend auf diesem Paper:
    
    {summary}
    
    Extrahiere 3-5 Key Insights (Bullets):
    - Insight 1
    - Insight 2
    - ...
    
    Fokus: Was kann ich daraus lernen/umsetzen?
    """
    
    insights = llm.generate(insights_prompt)
    
    return {'summary': summary, 'insights': insights}
```

**Update Obsidian Note:**
```python
def update_paper_note_with_summary(arxiv_id, summary_data):
    filepath = f'20-Knowledge/AI-Agents/Papers/inbox/{arxiv_id}.md'
    note = load_obsidian_note(filepath)
    
    # Append summary
    note += f'\n\n## Summary\n\n{summary_data["summary"]}'
    note += f'\n\n## Key Insights\n\n{summary_data["insights"]}'
    
    # Update status
    note = note.replace('status: inbox', 'status: summarized')
    
    save_obsidian_note(filepath, note)
```

**Cron: Daily Reader**
```python
def daily_reader():
    # Find papers with status=inbox (not yet summarized)
    papers = find_papers_by_status('inbox')
    
    for paper in papers[:5]:  # Max 5/day (cost control)
        pdf_path = download_pdf(paper['arxiv_id'])
        text = extract_text_from_pdf(pdf_path)
        summary = summarize_paper(text, paper)
        update_paper_note_with_summary(paper['arxiv_id'], summary)
    
    print(f"Summarized {len(papers[:5])} papers")
```

**Cron:**
```bash
# Every day at 9:00 AM (after Intake)
0 9 * * * /usr/bin/python3 ~/.openclaw/workspace/skills/reader/daily_reader.py
```

---

#### 2.3 Scorer Agent (1 Tag)

**Scoring:**
```python
def score_paper(paper_summary, paper_metadata):
    prompt = f"""
    Bewerte dieses Paper für Florian (VC, AI Agent Builder, Content Creator):
    
    Title: {paper_metadata['title']}
    Summary: {paper_summary}
    
    Score 1-10 für:
    1. Praxis-Relevanz (kann ich das umsetzen?)
    2. Neuheit (ist das wirklich neu?)
    3. Rigor (solide Methodik?)
    4. Domain-Fit (passt zu VC/AI Agents/Content?)
    
    Output: JSON
    {{
        "praxis": 8,
        "neuheit": 7,
        "rigor": 9,
        "domain_fit": 8,
        "overall": 8.0,
        "reasoning": "Kurze Begründung (50 Wörter)"
    }}
    """
    
    response = llm.generate(prompt, response_format='json')
    return json.loads(response)
```

**Update Obsidian Frontmatter:**
```python
def update_paper_score(arxiv_id, scores):
    filepath = f'20-Knowledge/AI-Agents/Papers/inbox/{arxiv_id}.md'
    note = load_obsidian_note(filepath)
    
    # Update frontmatter
    frontmatter = extract_frontmatter(note)
    frontmatter['score_praxis'] = scores['praxis']
    frontmatter['score_neuheit'] = scores['neuheit']
    frontmatter['score_rigor'] = scores['rigor']
    frontmatter['score_domain_fit'] = scores['domain_fit']
    frontmatter['score_overall'] = scores['overall']
    frontmatter['status'] = 'scored'
    
    note = update_frontmatter(note, frontmatter)
    save_obsidian_note(filepath, note)
```

**Integrate into Reader:**
```python
def daily_reader():
    papers = find_papers_by_status('inbox')
    
    for paper in papers[:5]:
        # Summarize
        pdf_path = download_pdf(paper['arxiv_id'])
        text = extract_text_from_pdf(pdf_path)
        summary = summarize_paper(text, paper)
        update_paper_note_with_summary(paper['arxiv_id'], summary)
        
        # Score
        scores = score_paper(summary['summary'], paper)
        update_paper_score(paper['arxiv_id'], scores)
        
        # Move to scored folder if score > 7
        if scores['overall'] >= 7:
            move_paper_to_folder(paper['arxiv_id'], 'scored')
        else:
            move_paper_to_folder(paper['arxiv_id'], 'archive')
```

---

#### 2.4 Critic Agent (1 Tag)

**Red Team:**
```python
def critique_paper(paper_summary, paper_metadata):
    prompt = f"""
    Du bist ein skeptischer Wissenschaftler. Kritisiere dieses Paper:
    
    Title: {paper_metadata['title']}
    Summary: {paper_summary}
    
    Fragen:
    1. Was könnte methodisch falsch sein?
    2. Welche Annahmen sind unrealistisch?
    3. Was fehlt in der Evaluation?
    4. Ist das wirklich neu oder nur Re-Branding?
    5. Wie robust sind die Results?
    
    Output: 150-Wort-Kritik
    Stil: Hart, aber fair. Keine Angriffe, nur sachliche Kritik.
    """
    
    critique = llm.generate(prompt)
    return critique
```

**Update Note:**
```python
def update_paper_critique(arxiv_id, critique):
    filepath = get_paper_filepath(arxiv_id)
    note = load_obsidian_note(filepath)
    note += f'\n\n## Critique\n\n{critique}'
    save_obsidian_note(filepath, note)
```

**Integrate:**
```python
def daily_reader():
    papers = find_papers_by_status('inbox')
    
    for paper in papers[:5]:
        # Summarize + Score
        summary = summarize_paper(...)
        scores = score_paper(...)
        
        # Critique (only for high-score papers)
        if scores['overall'] >= 7:
            critique = critique_paper(summary['summary'], paper)
            update_paper_critique(paper['arxiv_id'], critique)
```

---

## DELIVERABLES

Am Ende von Sprint 2 (24. Feb):

✅ **50+ Papers summarized:** Alle Inbox-Papers haben Summary + Key Insights  
✅ **Scoring läuft:** Jedes Paper hat Score 1-10  
✅ **High-Score Papers haben Critique:** Red Team verhindert Hype-Bias  
✅ **Obsidian sortiert:** Papers in `scored/` (>7) oder `archive/` (<7)  

**Demo:** Florian öffnet random Paper-Note, sieht Summary + Score + Critique

---

## ABHÄNGIGKEITEN

- ✅ Sprint 1 abgeschlossen (Intake + Memory)
- 🔧 `pdftotext` installed
- 🔧 Claude API (cost: ~$5-10 für 50 Papers)

---

## RISKS

| Risk | Mitigation |
|------|-----------|
| **PDF Extraction fails** | Fallback: OCR (Tesseract), manual text copy |
| **Summary ist zu generic** | Few-shot examples, iterate on prompt |
| **Scorer ist uncalibrated** | Expected! Sprint 4 fixes this mit Feedback |
| **Critic ist zu harsh** | Tune prompt, add "be fair" instruction |

---

## SUCCESS METRICS

- ✅ 50+ Papers mit Summary + Score
- ✅ Florian's Feedback: "Summaries sind nützlich" (6+/10)
- ✅ Top 5 Papers (Score 9+) sind tatsächlich relevant (Florian validates)
- ✅ Critic identifies mindestens 1 echtes Problem in einem Paper

---

# Sprint 3 (Woche 3): Synthesizer + Content Pipeline

**Dates:** 25. Feb - 3. März 2026  
**Theme:** "From Research to Content"

## WAS

### 1. Weekly Synthesis Cron (verbessert)
- Nicht nur "was kam rein", sondern "was bedeutet das?"
- Pattern-Erkennung über Papers
- Cross-Paper Insights

### 2. Ideator Agent
- Research Papers → Artikel-Ideen
- 5 Ideas/Woche, ranked by Engagement-Potential

### 3. Writer Agent (Florians Voice)
- Idee + Outline → 1000-Wort-Draft
- Few-Shot Learning mit Florians bestehenden Artikeln
- Self-Refine Loop (Draft → Critique → Revise)

### 4. First Published Article (Manual Distribution)
- Florian reviewed + approved Draft
- Published auf Substack (manual, Sprint 5 automatisiert das)

---

## WARUM

**Der Wendepunkt:** Research ist jetzt strukturiert. Jetzt machen wir daraus Content.

**Warum wichtig:**
- **Compound Effect:** Research ohne Output ist vergeudet
- **Feedback Loop:** Content Performance zeigt, was Audience interessiert → adjustiert Research Priorities
- **Florians Sichtbarkeit:** 1 Artikel/Woche = 50 Artikel/Jahr = VC Thought Leadership

**Nach Sprint 3:** Erster Auto-Generated Draft ist LIVE.

---

## WIE

### Implementation Steps

#### 3.1 Enhanced Weekly Synthesis (1 Tag)

**Pattern Recognition:**
```python
def weekly_synthesis_enhanced():
    papers = load_papers_last_7_days()
    
    # Group by themes
    themes = extract_themes(papers)  # LLM-based clustering
    
    prompt = f"""
    Diese Woche: {len(papers)} Papers, {len(themes)} Hauptthemen.
    
    Papers: {format_papers_list(papers)}
    Themes: {themes}
    
    Erstelle eine Synthese (800 Wörter):
    
    1. **Themen-Overview:** Was dominiert diese Woche?
    2. **Cross-Paper Insights:** Welche Papers ergänzen sich? Welche widersprechen sich?
    3. **Emerging Patterns:** Was ist neu/interessant im AI Agent Space?
    4. **Implications for Practitioners:** Was heißt das für Builder/VCs?
    5. **Content Ideas:** Welche 3 Artikel-Ideen ergeben sich daraus?
    
    Stil: Analytisch, pattern-focused, praktisch
    """
    
    synthesis = llm.generate(prompt)
    
    # Save + Send
    save_to_obsidian(f'20-Knowledge/AI-Agents/Trends/synthesis-{date}.md', synthesis)
    send_telegram_message(f'📊 Weekly Synthesis:\n\n{synthesis[:500]}...')
    
    return synthesis
```

---

#### 3.2 Ideator Agent (2 Tage)

**Idea Generation:**
```python
def generate_article_ideas(synthesis, top_papers):
    prompt = f"""
    Basierend auf dieser Woche's Research:
    
    Synthesis: {synthesis}
    Top Papers: {format_papers_list(top_papers)}
    
    Generiere 5 Artikel-Ideen für Florians Blog (VC/AI Agents/Content):
    
    Für jede Idee:
    - Title (catchy, klar)
    - Hook (1 Satz: Warum sollte jemand das lesen?)
    - Angle (Was ist der unique Take?)
    - Audience (VC, Founders, AI Engineers?)
    - Engagement-Potential (1-10)
    
    Output: JSON Array
    [
        {{
            "title": "...",
            "hook": "...",
            "angle": "...",
            "audience": "...",
            "engagement": 8
        }},
        ...
    ]
    
    Regeln:
    - Praktisch > Akademisch
    - Contrarian Angles > Obvious Takes
    - "How to" > "What is"
    """
    
    ideas = llm.generate(prompt, response_format='json')
    return json.loads(ideas)
```

**Ranking:**
```python
def rank_ideas(ideas):
    # Sort by engagement potential
    ranked = sorted(ideas, key=lambda x: x['engagement'], reverse=True)
    return ranked[:3]  # Top 3
```

**Save:**
```python
def save_article_ideas(ideas):
    for idea in ideas:
        filepath = f'content/ideas/{slugify(idea["title"])}.md'
        content = f"""
# {idea['title']}

**Hook:** {idea['hook']}
**Angle:** {idea['angle']}
**Audience:** {idea['audience']}
**Engagement Potential:** {idea['engagement']}/10

---

## Outline

(To be filled by Outliner or manually)
        """
        save_to_workspace(filepath, content)
```

---

#### 3.3 Writer Agent (3 Tage)

**Step 1: Outliner**
```python
def create_outline(idea):
    prompt = f"""
    Erstelle ein Outline für diesen Artikel:
    
    Title: {idea['title']}
    Hook: {idea['hook']}
    Angle: {idea['angle']}
    Audience: {idea['audience']}
    
    Output: 5-7 Sections mit Bullets
    
    1. Hook/Intro (warum lesen?)
    2. Context/Background (was muss man wissen?)
    3. Core Insight 1
    4. Core Insight 2
    5. Core Insight 3
    6. Implications/Takeaways
    7. CTA/Conclusion
    
    Jede Section: 2-3 Bullets mit Key Points
    """
    
    outline = llm.generate(prompt)
    return outline
```

**Step 2: Writer (Florians Voice)**
```python
def write_article_draft(outline, florians_articles):
    # Load Florian's past articles for few-shot
    examples = load_florians_articles(limit=3)
    
    prompt = f"""
    Schreibe einen Blog-Artikel basierend auf diesem Outline:
    
    {outline}
    
    ---
    
    Style Guide (aus Florians bisherigen Artikeln):
    
    {format_articles_for_fewshot(examples)}
    
    ---
    
    Regeln:
    - Direkt, no-fluff
    - Kurze Sätze, kurze Absätze
    - Praktische Takeaways
    - Keine Buzzwords ("revolutionary", "game-changing" → banned)
    - Ehrlich (auch über Unsicherheiten)
    - Founder-Operator Perspektive (nicht Academic)
    
    Länge: 1000-1200 Wörter
    Format: Markdown
    """
    
    draft = llm.generate(prompt, max_tokens=2000)
    return draft
```

**Step 3: Self-Refine Loop**
```python
def refine_draft(draft, max_iterations=2):
    for i in range(max_iterations):
        # Self-Critique
        critique_prompt = f"""
        Kritisiere diesen Draft:
        
        {draft}
        
        Fragen:
        - Ist der Hook stark genug?
        - Sind die Insights klar und actionable?
        - Ist der Stil konsistent (direkt, no-fluff)?
        - Gibt es Buzzwords? (eliminieren!)
        - Ist die Länge OK? (1000-1200 Wörter)
        
        Output: Score 1-10 + 3-5 Verbesserungsvorschläge
        """
        
        critique = llm.generate(critique_prompt, response_format='json')
        
        # If score > 8, done
        if critique['score'] >= 8:
            break
        
        # Revise
        revise_prompt = f"""
        Überarbeite diesen Draft basierend auf diesem Feedback:
        
        Draft: {draft}
        
        Feedback: {critique['suggestions']}
        
        Output: Improved Draft (1000-1200 Wörter)
        """
        
        draft = llm.generate(revise_prompt, max_tokens=2000)
    
    return draft
```

**Full Pipeline:**
```python
def weekly_content_creation():
    # Generate ideas from synthesis
    synthesis = load_latest_synthesis()
    top_papers = load_top_papers_last_week()
    ideas = generate_article_ideas(synthesis, top_papers)
    ranked_ideas = rank_ideas(ideas)
    
    # Pick top idea
    best_idea = ranked_ideas[0]
    
    # Create outline
    outline = create_outline(best_idea)
    
    # Write draft
    florians_articles = load_florians_articles()
    draft = write_article_draft(outline, florians_articles)
    
    # Refine
    final_draft = refine_draft(draft)
    
    # Save
    save_to_workspace(f'content/drafts/{slugify(best_idea["title"])}.md', final_draft)
    
    # Notify Florian
    send_telegram_message(f'📝 New Draft Ready:\n\nTitle: {best_idea["title"]}\n\n{final_draft[:300]}...\n\nReview: [Link]')
```

**Cron:**
```bash
# Every Monday at 10:00 AM
0 10 * * 1 /usr/bin/python3 ~/.openclaw/workspace/skills/writer/weekly_content_creation.py
```

---

#### 3.4 Manual Publishing (1 Tag)

**Workflow:**
1. Florian reviewed Draft in Obsidian/Workspace
2. Florian edits + approves
3. Florian manually publishes zu Substack (Sprint 5 automatisiert das)

**Why Manual:** Wir wollen sicherstellen, dass Quality stimmt bevor wir auto-publish.

---

## DELIVERABLES

Am Ende von Sprint 3 (3. März):

✅ **Enhanced Weekly Synthesis:** Pattern-Recognition, Cross-Paper Insights  
✅ **5 Artikel-Ideen generiert:** Ranked by Engagement-Potential  
✅ **Erster Auto-Generated Draft:** 1000+ Wörter, Florians Voice  
✅ **Erster Published Artikel:** Florian approved + published (manual)  

**Demo:** Florian zeigt Published Artikel + Draft-Quality

---

## ABHÄNGIGKEITEN

- ✅ Sprint 2 abgeschlossen (Papers summarized + scored)
- 🔧 Florians past articles (3-5 examples für few-shot)
- 🔧 Substack Account

---

## RISKS

| Risk | Mitigation |
|------|-----------|
| **Writer Voice ist off** | Iterate on prompt, add more few-shot examples, Florian feedback |
| **Draft Quality < Publishable** | Expected! Self-Refine Loop + Human-Review |
| **Ideas sind generic** | Add contrarian angle instruction, review with Florian |
| **Florian rejects Draft** | Good! Iterate, learn, improve prompt |

---

## SUCCESS METRICS

- ✅ Erster Draft delivered (Florian receives Telegram notification)
- ✅ Florian's Rating: "Draft ist 70% done" (needs editing, but solid foundation)
- ✅ Published Artikel gets 50+ Views in first week
- ✅ Florian: "I would use this system weekly"

---

# Sprint 4 (Woche 4): Self-Improvement Loop

**Dates:** 4. März - 10. März 2026  
**Theme:** "Learning from Feedback"

## WAS

### 1. Calibrator: Predicted vs Actual Relevanz
- Track: Scorer predicted 8/10, Florian rated 5/10 → Error
- Analyze errors, update Scoring-Prompt

### 2. Reflector: Wöchentliche Selbstreflexion
- "Was lief gut? Was nicht? Was habe ich gelernt?"
- Saved in L3 (Episodic Memory)

### 3. Automatic Memory Promotion
- Daily: L4 (Raw) → L3 (Episodic)
- Weekly: L3 (Episodic) → L2 (Domain Knowledge)

### 4. Feedback-Loop: Content Performance → Research Priorities
- Track: Artikel über Multi-Agent performed gut → Mehr Multi-Agent Papers

---

## WARUM

**Systeme ohne Feedback stagnieren.** Nach Sprint 3 haben wir einen Full Loop (Research → Content), aber er verbessert sich nicht selbst.

**Sprint 4 macht das System lernfähig:**
- **Calibration:** Scorer wird mit jedem Paper besser
- **Reflection:** System reflektiert über Erfolge/Fehler
- **Memory Promotion:** Wichtige Insights wandern von Raw → Principles
- **Content Feedback:** Audience sagt uns, was funktioniert → adjustiert Research

**Nach Sprint 4:** System ist nicht statisch, sondern **compound**.

---

## WIE

### Implementation Steps

#### 4.1 Calibrator (2 Tage)

**Feedback Collection:**
```python
def collect_florian_feedback(arxiv_id):
    # Florian rates paper (1-10) via Telegram or Obsidian
    # Options:
    # 1. Telegram: "Rate this paper: /rate 2402.12345 8"
    # 2. Obsidian: Update frontmatter `florian_rating: 8`
    
    paper = load_paper(arxiv_id)
    predicted_score = paper['score_overall']
    actual_score = paper.get('florian_rating')
    
    if actual_score:
        error = actual_score - predicted_score
        log_calibration_error(arxiv_id, predicted_score, actual_score, error)
```

**Error Analysis:**
```python
def weekly_calibration():
    errors = load_calibration_errors_last_week()
    
    prompt = f"""
    Scorer Calibration Analysis:
    
    Diese Woche: {len(errors)} Papers rated by Florian
    
    Errors:
    {format_errors(errors)}
    
    Fragen:
    1. Welche Papers wurden overrated? (Predicted > Actual)
    2. Welche Papers wurden underrated? (Predicted < Actual)
    3. Welche Features korrelieren mit Errors?
    4. Was muss ich am Scoring-Prompt ändern?
    
    Output: 3-5 konkrete Verbesserungsvorschläge für den Scorer
    """
    
    improvements = llm.generate(prompt)
    
    # Save to Memory
    save_to_memory(f'calibration-analysis-{date}.md', improvements)
    
    # Notify Florian
    send_telegram_message(f'🔧 Scorer Calibration:\n\n{improvements}')
```

**Update Scorer Prompt:**
```python
def update_scorer_prompt(improvements):
    # Manual: Florian reviews improvements and updates scorer prompt
    # OR: Automatic (risky, but possible)
    current_prompt = load_scorer_prompt()
    
    update_prompt = f"""
    Current Scorer Prompt:
    
    {current_prompt}
    
    Improvements (from Calibration Analysis):
    
    {improvements}
    
    Output: Updated Scorer Prompt (improved based on feedback)
    """
    
    new_prompt = llm.generate(update_prompt)
    
    # Save (with version control)
    save_scorer_prompt(new_prompt, version=get_next_version())
```

---

#### 4.2 Reflector (1 Tag)

**Weekly Reflection:**
```python
def weekly_reflection():
    week_summary = load_episodic_last_7_days()
    
    prompt = f"""
    Wöchentliche Retrospektive (Compound Machine):
    
    Diese Woche:
    {week_summary}
    
    Fragen:
    1. Was lief gut? (Erfolge, positive Surprises)
    2. Was lief schlecht? (Fehler, Bottlenecks)
    3. Was habe ich gelernt? (Insights, Patterns)
    4. Was sollte ich nächste Woche anders machen?
    
    Output: 300-Wort-Reflection
    Stil: Ehrlich, selbstkritisch, actionable
    """
    
    reflection = llm.generate(prompt)
    
    # Save to L3 (Episodic Memory)
    save_to_memory(f'01-Daily/reflection-{date}.md', reflection)
    
    # Notify Florian
    send_telegram_message(f'🧠 Weekly Reflection:\n\n{reflection}')
```

**Cron:**
```bash
# Every Sunday at 8 PM
0 20 * * 0 /usr/bin/python3 ~/.openclaw/workspace/skills/reflector/weekly_reflection.py
```

---

#### 4.3 Automatic Memory Promotion (2 Tage)

**Daily Consolidation (L4 → L3):**
```python
def daily_consolidation():
    # Load raw items from L4
    raw_items = load_raw_inbox()  # Papers, tweets, notes
    
    prompt = f"""
    Florian's Day Review:
    
    Raw Events (heute): {format_raw_items(raw_items)}
    
    Was war heute wichtig?
    - Welche Papers waren relevant?
    - Welche Meetings/Notizen?
    - Welche Insights?
    
    Output: 200-Wort-Zusammenfassung (für Daily Note)
    """
    
    summary = llm.generate(prompt)
    
    # Save to L3
    save_to_obsidian(f'01-Daily/{date}.md', summary)
    
    # Cleanup L4 (delete unimportant items)
    cleanup_raw_inbox()
```

**Weekly Consolidation (L3 → L2):**
```python
def weekly_consolidation():
    episodic_notes = load_episodic_last_7_days()
    
    prompt = f"""
    Weekly Consolidation (L3 → L2):
    
    Diese Woche (Episodic Notes):
    {episodic_notes}
    
    Fragen:
    1. Welche Learnings sind wiederverwendbar? (gehören ins Domain Knowledge L2)
    2. Welche Patterns? (wiederholen sich über mehrere Tage)
    3. Was ist nur temporal? (bleibt in L3)
    
    Output: Updates für L2 (Domain Knowledge)
    
    Format:
    - Update existing note: "20-Knowledge/AI-Agents/Multi-Agent-Architectures.md"
    - OR: Create new note: "20-Knowledge/AI-Agents/New-Pattern.md"
    
    Für jedes Update:
    - Note Path
    - New Content (was hinzufügen?)
    """
    
    updates = llm.generate(prompt, response_format='json')
    
    # Apply updates
    for update in updates:
        apply_to_domain_knowledge(update['note_path'], update['content'])
```

**Cron:**
```bash
# Daily: 10 PM
0 22 * * * /usr/bin/python3 ~/.openclaw/workspace/skills/memory/daily_consolidation.py

# Weekly: Sunday 9 PM
0 21 * * 0 /usr/bin/python3 ~/.openclaw/workspace/skills/memory/weekly_consolidation.py
```

---

#### 4.4 Content Feedback Loop (1 Tag)

**Track Performance:**
```python
def track_content_performance(article_url):
    # Substack Analytics (via API or scraping)
    stats = get_substack_stats(article_url)
    
    return {
        'views': stats['views'],
        'likes': stats['likes'],
        'comments': stats['comments'],
        'engagement': stats['views'] * 0.6 + stats['likes'] * 5 + stats['comments'] * 10
    }
```

**Adjust Research Priorities:**
```python
def monthly_priority_adjustment():
    # Load published articles from last 30 days
    articles = load_published_articles_last_30_days()
    
    # Track performance
    performance = []
    for article in articles:
        stats = track_content_performance(article['url'])
        performance.append({
            'title': article['title'],
            'topics': article['topics'],
            'engagement': stats['engagement']
        })
    
    # Analyze
    prompt = f"""
    Content Performance Analysis:
    
    {format_performance(performance)}
    
    Fragen:
    1. Welche Topics performed gut? (hohe Engagement)
    2. Welche Topics performed schlecht? (niedrige Engagement)
    3. Was sollte ich mehr/weniger researchen?
    
    Output: Adjusted Research Priorities (Keywords für Intake)
    """
    
    priorities = llm.generate(prompt)
    
    # Update Intake Keywords
    update_intake_keywords(priorities)
    
    # Notify Florian
    send_telegram_message(f'📊 Research Priorities Updated:\n\n{priorities}')
```

---

## DELIVERABLES

Am Ende von Sprint 4 (10. März):

✅ **Calibration läuft:** Scorer-Errors tracked + analyzed  
✅ **Weekly Reflection:** System reflektiert über Erfolge/Fehler  
✅ **Memory Promotion läuft:** Daily L4→L3, Weekly L3→L2  
✅ **Content Feedback Loop:** Performance → Research Priorities  

**Demo:** Florian zeigt Calibration-Report + Updated Domain Knowledge Notes

---

## ABHÄNGIGKEITEN

- ✅ Sprint 3 abgeschlossen (Content läuft)
- 🔧 Florian's Feedback (Paper Ratings)
- 🔧 Substack Analytics API

---

## RISKS

| Risk | Mitigation |
|------|-----------|
| **Memory Promotion quality** | Conservative (lieber zu viel als zu wenig), Human-Review |
| **Calibration diverges** | Hard limits (max 10% change per iteration) |
| **Feedback Loop is noisy** | Use 30-day window, not weekly (more stable) |
| **System becomes unstable** | Version control for prompts, rollback if needed |

---

## SUCCESS METRICS

- ✅ Scorer accuracy improves (Error < 2 Punkte nach 2 Wochen)
- ✅ L2 (Domain Knowledge) wächst (5+ new notes or updates)
- ✅ Florian: "System lernt tatsächlich"
- ✅ Content-Feedback führt zu mindestens 1 Priority-Shift

---

# Sprint 5 (Woche 5): Distribution + Polish

**Dates:** 11. März - 17. März 2026  
**Theme:** "Close the Loop"

## WAS

### 1. Substack Publishing Pipeline
- Auto-Publish (mit Human-Approval Checkpoint)
- Draft → Florian Approval → Publish

### 2. LinkedIn/Twitter Repurposing
- 1 Blog → LinkedIn Post + Twitter Thread
- Auto-Schedule (Buffer/Hootsuite oder custom)

### 3. Performance Tracking Dashboard
- Obsidian Note: "Content Performance"
- Views, Likes, Comments pro Artikel
- Updated monthly

### 4. Full Loop Documentation
- "How to use Compound Machine" Guide
- Florian kann System self-service nutzen

---

## WARUM

**Der Final Boss:** Distribution. Content ohne Distribution ist unsichtbar.

**Sprint 5 schließt den Loop:**
- Research → Content → **Distribution** → Feedback → Research
- **Fully Automated** (mit Human Checkpoints wo nötig)

**Nach Sprint 5:** Compound Machine läuft autonom. Florian's Job: Feedback geben, nicht Execute.

---

## WIE

### Implementation Steps

#### 5.1 Substack Auto-Publishing (2 Tage)

**Approval Workflow:**
```python
def publish_workflow():
    # 1. Draft is ready
    draft = load_latest_draft()
    
    # 2. Notify Florian for approval
    send_telegram_message(f"""
📝 New Draft Ready for Publishing:

Title: {draft['title']}

Preview: {draft['content'][:300]}...

Actions:
/approve_{draft['id']} - Publish now
/edit_{draft['id']} - Edit first
/reject_{draft['id']} - Don't publish
    """)
    
    # 3. Wait for approval (Telegram command)
    # (Implemented via Telegram Bot handlers)
```

**Substack API Publishing:**
```python
def publish_to_substack(draft):
    # Substack API (if available) OR Web Automation (Playwright)
    
    # Option 1: API
    response = requests.post(
        'https://api.substack.com/v1/posts',
        headers={'Authorization': f'Bearer {SUBSTACK_API_KEY}'},
        json={
            'title': draft['title'],
            'body': draft['content'],
            'status': 'published'
        }
    )
    
    # Option 2: Web Automation (if no API)
    from playwright.sync_api import sync_playwright
    
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto('https://substack.com/publish')
        # Login, fill form, publish
        # (Implementation details omitted)
    
    return response.json()['url']
```

**Full Workflow:**
```python
def weekly_publishing():
    draft = load_latest_draft()
    
    # Send for approval
    approval_id = request_approval(draft)
    
    # Wait for approval (polling or webhook)
    while not is_approved(approval_id):
        time.sleep(60)  # Check every minute
    
    # Publish
    url = publish_to_substack(draft)
    
    # Save URL
    update_draft_with_url(draft['id'], url)
    
    # Notify Florian
    send_telegram_message(f'✅ Published: {draft["title"]}\n\n{url}')
```

---

#### 5.2 Repurposing Pipeline (2 Tage)

**LinkedIn Post:**
```python
def create_linkedin_post(article):
    prompt = f"""
    Repurpose this blog article für LinkedIn:
    
    Article: {article['content']}
    
    Output: LinkedIn Post (300 Wörter max)
    
    Format:
    - Hook (1-2 Sätze, attention-grabbing)
    - Key Points (3-5 Bullets)
    - CTA (Read full article: [link])
    
    Stil: Professional, punchy, no-fluff
    """
    
    post = llm.generate(prompt)
    return post
```

**Twitter Thread:**
```python
def create_twitter_thread(article):
    prompt = f"""
    Repurpose this blog article für Twitter Thread:
    
    Article: {article['content']}
    
    Output: Twitter Thread (10 Tweets max, numbered)
    
    Format:
    1/ Hook (strong, controversial if possible)
    2-9/ Key Points (one per tweet, punchy)
    10/ CTA (Read full: [link])
    
    Rules:
    - Max 280 chars/tweet
    - Use line breaks for readability
    - No hashtags (organic > spam)
    """
    
    thread = llm.generate(prompt, response_format='json')  # Array of tweets
    return json.loads(thread)
```

**Scheduling:**
```python
def schedule_distribution(article, linkedin_post, twitter_thread):
    # Option 1: Buffer/Hootsuite API
    buffer_api.schedule(linkedin_post, time='+2 days', platform='linkedin')
    buffer_api.schedule(twitter_thread, time='+3 days', platform='twitter')
    
    # Option 2: Custom (store + cron)
    schedule_db.insert({
        'type': 'linkedin',
        'content': linkedin_post,
        'publish_at': datetime.now() + timedelta(days=2)
    })
```

---

#### 5.3 Performance Tracking (1 Tag)

**Dashboard (Obsidian Note):**
```markdown
# Content Performance Dashboard

**Last Updated:** 2026-03-15

## Published Articles (Last 30 Days)

| Title | Published | Views | Likes | Comments | Engagement |
|-------|-----------|-------|-------|----------|------------|
| Multi-Agent Systems | 2026-03-01 | 500 | 20 | 5 | 650 |
| Memory in AI Agents | 2026-03-08 | 300 | 15 | 3 | 405 |

## Top Performers

1. **Multi-Agent Systems** (Engagement: 650)
   - Topics: multi-agent, AutoGen, MetaGPT
   - Insight: Audience loves practical architecture comparisons

2. **Memory in AI Agents** (Engagement: 405)
   - Topics: MemGPT, RAG, hierarchical memory
   - Insight: Technical deep-dives perform well

## Trends

- **Multi-Agent content:** High engagement
- **Memory systems:** Moderate engagement
- **VC-specific content:** Low engagement (only 2 samples, need more data)

## Action Items

- ✅ More Multi-Agent content (high demand)
- ⚠️ Test more VC-specific angles (current sample too small)
```

**Auto-Update:**
```python
def update_performance_dashboard():
    articles = load_published_articles_last_30_days()
    
    # Fetch stats
    performance = []
    for article in articles:
        stats = track_content_performance(article['url'])
        performance.append({
            'title': article['title'],
            'published': article['date'],
            'views': stats['views'],
            'likes': stats['likes'],
            'comments': stats['comments'],
            'engagement': stats['engagement'],
            'topics': article['topics']
        })
    
    # Sort by engagement
    top_performers = sorted(performance, key=lambda x: x['engagement'], reverse=True)[:3]
    
    # Generate dashboard
    dashboard = generate_dashboard_markdown(performance, top_performers)
    
    # Save
    save_to_obsidian('20-Knowledge/Content-Creation/Performance-Dashboard.md', dashboard)
```

**Cron:**
```bash
# Monthly: 1st of month, 9 AM
0 9 1 * * /usr/bin/python3 ~/.openclaw/workspace/skills/tracker/update_dashboard.py
```

---

#### 5.4 Documentation + Polish (2 Tage)

**User Guide:**
```markdown
# Compound Machine - User Guide

## Daily

**Nothing!** System runs autonomously.

## Weekly

### Sunday Evening (6-8 PM)

1. **Read Weekly Research Brief** (Telegram notification)
   - Review Top Papers
   - Optional: Rate papers (helps Calibrator)

2. **Review Article Draft** (Telegram notification, Monday morning)
   - Approve, Edit, or Reject
   - If Approved: Auto-published to Substack

3. **Check Weekly Reflection** (Telegram, Sunday 8 PM)
   - What did the system learn?
   - Any action items?

## Monthly

### First Week of Month

1. **Review Performance Dashboard** (Obsidian)
   - Which content performed well?
   - Adjust priorities if needed

2. **Review Domain Knowledge Growth** (Obsidian L2)
   - Did Memory Consolidation work?
   - Any insights to promote to L1 (Principles)?

## Commands (Telegram)

- `/rate [arxiv_id] [score]` - Rate a paper (1-10)
- `/approve_[draft_id]` - Approve draft for publishing
- `/edit_[draft_id]` - Request edits (opens Obsidian link)
- `/reject_[draft_id]` - Don't publish
- `/status` - System health check
- `/synthesis` - Re-generate weekly synthesis (if missed)

## Troubleshooting

**Intake not working?**
- Check cron: `crontab -l`
- Check logs: `~/.openclaw/logs/intake.log`

**Scorer seems off?**
- Rate more papers (Calibrator needs feedback)
- Review `memory/calibration-analysis-*.md`

**Draft quality low?**
- Add more few-shot examples (Florian's articles)
- Review Writer prompt: `skills/writer/prompt.txt`

**Distribution failed?**
- Check Substack API key
- Check Buffer/Hootsuite quota
```

---

## DELIVERABLES

Am Ende von Sprint 5 (17. März):

✅ **Auto-Publishing läuft:** Draft → Approval → Publish (Substack)  
✅ **Repurposing läuft:** Blog → LinkedIn + Twitter (scheduled)  
✅ **Performance Dashboard:** Live, updated monthly  
✅ **Full Loop operational:** Research → Content → Distribution → Feedback → Research  
✅ **Documentation:** Florian kann System selbst nutzen  

**Demo:** Florian zeigt Full Workflow (Research Brief → Draft → Published → Repurposed)

---

## ABHÄNGIGKEITEN

- ✅ Sprint 4 abgeschlossen (Feedback Loops)
- 🔧 Substack API (oder Web Automation)
- 🔧 Buffer/Hootsuite Account (oder custom scheduling)

---

## RISKS

| Risk | Mitigation |
|------|-----------|
| **Auto-Publishing fails** | Retry-logic, Fallback to manual, Notify Florian |
| **Repurposed content is off-brand** | Human-Review first 3 posts, iterate prompts |
| **Scheduling fails** | Notifications, Manual backup |
| **Florian doesn't approve in time** | Timeout (24h), then skip week |

---

## SUCCESS METRICS

- ✅ 1 Article auto-published (with approval)
- ✅ LinkedIn + Twitter content scheduled
- ✅ Performance Dashboard shows growth (Views week-over-week)
- ✅ Florian: "I spend <2h/week on this system"
- ✅ Full Loop demonstrable (Research to Feedback in 1 week)

---

# Post-Sprint 5: What's Next?

**Compound Machine v1 ist LIVE.** Jetzt: Iterate, Optimize, Expand.

## Iteration Areas

### 1. Quality Improvements
- **Writer Voice:** More few-shot examples, tune prompts
- **Scorer Calibration:** Continuous learning from Florian's feedback
- **Memory Consolidation:** Better heuristics for what's important

### 2. Feature Expansions
- **Video Content:** Repurpose articles → YouTube scripts
- **Newsletters:** Weekly digest of Research + Insights
- **Podcast:** Auto-generate podcast scripts from articles

### 3. Scale
- **More Sources:** Reddit, Hacker News, Medium
- **More Platforms:** Substack → Ghost, Medium, Dev.to
- **Collaboration:** Multiple writers (Florian + guests)

### 4. Advanced Features
- **Predictive Scoring:** ML model (not just LLM) for paper relevance
- **Agent Skill Library:** Voyager-style (learn new skills, save to library)
- **Cross-Agent Learning:** Multi-user Compound Machine (network effects)

---

## 6-Month Roadmap (After Sprint 5)

**Month 2 (April):**
- Iterate on Writer Voice (10+ articles published)
- Scorer Calibration (100+ papers rated)
- First Newsletter sent

**Month 3 (May):**
- Add Reddit/HN to Intake
- Video script generation
- Performance Dashboard v2 (more metrics)

**Month 4 (June):**
- Multi-platform Publishing (Substack + Medium + Dev.to)
- Advanced Memory Traversal (Graph DB)
- First Cross-Domain Insight (VC + AI Agents)

**Month 5 (July):**
- Predictive Scoring (ML model)
- Agent Skill Library (Voyager-inspired)
- First Guest Collaboration

**Month 6 (August):**
- **Review Milestone:** 500+ L2 Notes, 50+ Articles, 5000+ Views/Month
- **Decision:** Scale to other domains? Open-source framework? Keep private?

---

## Success Criteria (6 Months)

**Quantitative:**
- ✅ 50+ Articles published (1/week)
- ✅ 5000+ Views/month (compound growth)
- ✅ 500+ L2 Notes (Domain Knowledge)
- ✅ Florian spends <2h/week on system

**Qualitative:**
- ✅ Florian: "This is my Second Brain"
- ✅ Florian: "I can't imagine working without it"
- ✅ System delivers genuine insights (not just summaries)
- ✅ System has opinions (not just facts)

---

## Final Thoughts

**Compound Machine ist kein Feature, es ist eine Philosophie:**

- **Personal > General:** Tief personalisiert beats Generic AI
- **Compound > Linear:** Jeder Tag macht das System besser
- **Feedback > Planning:** System lernt aus Reality, nicht Theorie
- **Ship > Perfect:** V1 ist gut genug, V10 wird großartig

**Die nächsten 5 Wochen sind kritisch.** Sprint by sprint, feature by feature, wir bauen Florians Personal Intelligence.

**Let's build.**

---

*Florian, bereit für Sprint 1? Starting: 11. Februar 2026. Ending: Full Compound Machine, 17. März 2026.*
