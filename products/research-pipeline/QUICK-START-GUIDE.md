# Research Pipeline Quick Start Guide
**Get running in 30 minutes**

---

## Installation

### 1. Install PaperQA2
```bash
pip install paper-qa>=5
```

### 2. Set API Keys
```bash
# OpenAI (required for embeddings + LLM)
export OPENAI_API_KEY="sk-..."

# Semantic Scholar (optional but recommended)
export SEMANTIC_SCHOLAR_API_KEY="..."

# Get S2 key: https://www.semanticscholar.org/product/api
```

### 3. Verify Installation
```bash
pqa --version
# Should show: paper-qa version 2025.x.x or later
```

---

## Quick Test (5 minutes)

### Prepare Test Papers
```bash
# Create paper directory
mkdir ~/research_test
cd ~/research_test

# Download test paper
curl -o paperqa2.pdf https://arxiv.org/pdf/2409.13740
```

### Run First Query
```bash
pqa ask "What is PaperQA2?"
```

You should see:
1. Index building (embedding the paper)
2. Evidence gathering (finding relevant passages)
3. Answer generation (with citations)

---

## Basic Workflows

### Workflow 1: Literature Q&A

```bash
# Navigate to folder with papers
cd ~/papers/ai_agents

# Ask questions
pqa ask "What are the main challenges in AI agent research?"

# Use different settings
pqa --settings high_quality ask "What are the limitations of current approaches?"

# Faster/cheaper
pqa --settings fast ask "What are key papers in this domain?"
```

### Workflow 2: Topic Research from Scratch

```bash
# 1. Create project folder
mkdir ~/research_projects/ai_in_vc
cd ~/research_projects/ai_in_vc

# 2. Add papers manually (download PDFs)
# Or use search tools to find relevant papers

# 3. Build index
pqa index

# 4. Explore topic
pqa ask "How are AI agents being used in venture capital?"
pqa ask "What are the success cases?"
pqa ask "What are the limitations?"

# 5. View history
pqa search "venture capital"
```

### Workflow 3: Evidence Gathering for Writing

```python
# save as: research_helper.py
from paperqa import Settings, ask

# Setup
settings = Settings(
    paper_directory="~/papers/ai_agents",
    temperature=0.3,  # Lower = more factual
    answer.answer_max_sources=5
)

# Research questions
questions = [
    "What are the main approaches to AI agent architectures?",
    "What are the performance benchmarks?",
    "What are the open challenges?",
    "What are the practical applications?",
]

# Gather evidence
results = {}
for q in questions:
    print(f"\n{'='*60}")
    print(f"Q: {q}")
    print('='*60)
    
    response = ask(q, settings=settings)
    results[q] = response
    
    print(response.answer)
    print("\nSources:")
    for ctx in response.contexts:
        print(f"  - {ctx.text.name}: {ctx.text.doc.citation}")

# Save results
import json
with open("research_results.json", "w") as f:
    json.dump({q: r.model_dump() for q, r in results.items()}, f, indent=2)
```

Run:
```bash
python research_helper.py > research_output.txt
```

---

## Python API Examples

### Example 1: Simple Q&A
```python
from paperqa import Settings, ask

answer = ask(
    "What is retrieval-augmented generation?",
    settings=Settings(paper_directory="~/papers")
)

print(answer.answer)
print("\nCitations:")
for ctx in answer.contexts:
    print(f"  [{ctx.text.name}] {ctx.text.doc.citation}")
```

### Example 2: Custom Configuration
```python
from paperqa import Settings, ask
from paperqa.settings import AnswerSettings

# Configure for high quality
settings = Settings(
    llm="gpt-4o",
    summary_llm="gpt-4o",
    temperature=0.1,
    answer=AnswerSettings(
        evidence_k=15,  # Consider more evidence
        answer_max_sources=7,  # Include more sources in answer
        evidence_summary_length="about 150 words",
    )
)

answer = ask("Your question here", settings=settings)
```

### Example 3: Batch Processing
```python
import asyncio
from paperqa import Settings, agent_query

async def research_topic(topic: str, questions: list[str]):
    """Research a topic by answering multiple questions."""
    
    settings = Settings(
        paper_directory=f"~/papers/{topic}",
        llm="gpt-4o-mini",  # Cheaper
    )
    
    results = []
    for q in questions:
        print(f"Processing: {q}")
        response = await agent_query(q, settings=settings)
        results.append({
            "question": q,
            "answer": response.answer,
            "sources": len(response.contexts)
        })
    
    return results

# Run
topic = "ai_agents"
questions = [
    "What are the main architectures?",
    "What are the benchmarks?",
    "What are the challenges?",
]

results = asyncio.run(research_topic(topic, questions))

for r in results:
    print(f"\nQ: {r['question']}")
    print(f"A: {r['answer'][:200]}...")
    print(f"Sources: {r['sources']}")
```

### Example 4: Adding Papers Programmatically
```python
from paperqa import Docs, Settings
import asyncio

async def build_index():
    docs = Docs()
    settings = Settings(
        embedding="text-embedding-3-small",
        llm="gpt-4o-mini"
    )
    
    # Add papers
    papers = [
        "paper1.pdf",
        "paper2.pdf",
        "paper3.pdf",
    ]
    
    for paper in papers:
        print(f"Adding: {paper}")
        await docs.aadd(paper, settings=settings)
    
    # Query
    session = await docs.aquery(
        "What are the main findings?",
        settings=settings
    )
    
    print(session.answer)
    
    return docs

docs = asyncio.run(build_index())
```

---

## Semantic Scholar API Examples

### Example 1: Search Papers
```python
import requests

S2_API_KEY = "your_key"
BASE_URL = "https://api.semanticscholar.org/graph/v1"

def search_papers(query: str, limit: int = 10):
    """Search for papers on Semantic Scholar."""
    
    response = requests.get(
        f"{BASE_URL}/paper/search",
        params={
            "query": query,
            "limit": limit,
            "fields": "title,abstract,citationCount,year,authors,venue,openAccessPdf"
        },
        headers={"x-api-key": S2_API_KEY}
    )
    
    return response.json()["data"]

# Search
papers = search_papers("AI agents for scientific research", limit=20)

# Filter high-impact recent papers
recent_high_impact = [
    p for p in papers
    if p.get("year", 0) >= 2023 and p.get("citationCount", 0) > 10
]

for paper in recent_high_impact:
    print(f"{paper['title']} ({paper['year']})")
    print(f"  Citations: {paper['citationCount']}")
    if paper.get("openAccessPdf"):
        print(f"  PDF: {paper['openAccessPdf']['url']}")
    print()
```

### Example 2: Download Open Access Papers
```python
import requests
from pathlib import Path

def download_paper(paper_id: str, output_dir: str = "papers"):
    """Download paper PDF if open access."""
    
    # Get paper details
    response = requests.get(
        f"{BASE_URL}/paper/{paper_id}",
        params={"fields": "title,openAccessPdf"},
        headers={"x-api-key": S2_API_KEY}
    )
    
    paper = response.json()
    
    if not paper.get("openAccessPdf"):
        print(f"No open access PDF for: {paper['title']}")
        return None
    
    # Download PDF
    pdf_url = paper["openAccessPdf"]["url"]
    pdf_response = requests.get(pdf_url)
    
    # Save
    Path(output_dir).mkdir(exist_ok=True)
    filename = f"{output_dir}/{paper_id}.pdf"
    
    with open(filename, "wb") as f:
        f.write(pdf_response.content)
    
    print(f"Downloaded: {paper['title']}")
    return filename

# Example: Download PaperQA2 paper
download_paper("CorpusId:272828610")
```

### Example 3: Build Citation Network
```python
def get_citation_network(paper_id: str, depth: int = 1):
    """Get papers that cite this paper."""
    
    response = requests.get(
        f"{BASE_URL}/paper/{paper_id}/citations",
        params={
            "fields": "title,year,citationCount",
            "limit": 100
        },
        headers={"x-api-key": S2_API_KEY}
    )
    
    citations = response.json()["data"]
    
    return [
        {
            "title": c["citingPaper"]["title"],
            "year": c["citingPaper"].get("year"),
            "citations": c["citingPaper"].get("citationCount", 0),
        }
        for c in citations
    ]

# Example
network = get_citation_network("CorpusId:272828610")
print(f"Found {len(network)} citing papers")

# Sort by citations
top_citers = sorted(network, key=lambda x: x["citations"], reverse=True)[:10]
for p in top_citers:
    print(f"{p['title']} ({p['year']}) - {p['citations']} citations")
```

---

## STORM Integration (Advanced)

### Install STORM
```bash
pip install knowledge-storm
```

### Basic Usage
```python
from knowledge_storm import STORMWikiRunner, STORMWikiRunnerArguments, STORMWikiLMConfigs
from knowledge_storm.lm import LitellmModel
from knowledge_storm.rm import YouRM
import os

# Configure models
lm_configs = STORMWikiLMConfigs()

gpt_4o = LitellmModel(
    model='gpt-4o',
    api_key=os.getenv("OPENAI_API_KEY"),
    max_tokens=3000,
    temperature=1.0
)

gpt_35 = LitellmModel(
    model='gpt-3.5-turbo',
    api_key=os.getenv("OPENAI_API_KEY"),
    max_tokens=500,
    temperature=1.0
)

# Use cheaper model for conversation, expensive for writing
lm_configs.set_conv_simulator_lm(gpt_35)
lm_configs.set_question_asker_lm(gpt_35)
lm_configs.set_outline_gen_lm(gpt_4o)
lm_configs.set_article_gen_lm(gpt_4o)
lm_configs.set_article_polish_lm(gpt_4o)

# Configure retrieval
rm = YouRM(ydc_api_key=os.getenv('YDC_API_KEY'), k=10)

# Setup runner
engine_args = STORMWikiRunnerArguments(
    output_dir='./storm_output',
    max_conv_turn=5,
    max_perspective=3,
)

runner = STORMWikiRunner(engine_args, lm_configs, rm)

# Generate article
topic = "AI Agents in Venture Capital"
runner.run(
    topic=topic,
    do_research=True,
    do_generate_outline=True,
    do_generate_article=True,
    do_polish_article=True,
)

# Output will be in ./storm_output/
# - storm_gen_outline.txt (outline)
# - storm_gen_article.txt (full article)
# - storm_gen_article_polished.txt (final version)
```

---

## Obsidian Integration

### Auto-Generate Notes
```python
from paperqa import ask, Settings
from pathlib import Path
import datetime

def create_research_note(topic: str, questions: list[str], output_dir: str):
    """Create an Obsidian note with research results."""
    
    settings = Settings(paper_directory="~/papers")
    
    # Header
    note = f"# {topic}\n\n"
    note += f"*Created: {datetime.date.today()}*\n\n"
    note += "## Research Questions\n\n"
    
    # Answer each question
    for i, q in enumerate(questions, 1):
        note += f"### Q{i}: {q}\n\n"
        
        response = ask(q, settings=settings)
        note += f"{response.answer}\n\n"
        
        # Add sources
        note += "**Sources:**\n"
        for ctx in response.contexts:
            note += f"- [[{ctx.text.doc.docname}]] - {ctx.text.name}\n"
        note += "\n"
    
    # Save to Obsidian vault
    output_path = Path(output_dir) / f"{topic.replace(' ', '_')}.md"
    output_path.write_text(note)
    
    print(f"Note created: {output_path}")
    return output_path

# Example
create_research_note(
    topic="AI Agents in Operations",
    questions=[
        "What are the main use cases?",
        "What are the success metrics?",
        "What are the challenges?",
    ],
    output_dir="~/Library/Mobile Documents/iCloud~md~obsidian/Documents/System_OS/20-Knowledge/"
)
```

---

## Tips & Tricks

### 1. Speed Up Queries
```bash
# Use cheaper/faster model
pqa --llm gpt-4o-mini ask "Your question"

# Reduce evidence gathering
pqa --answer.evidence_k 5 ask "Your question"

# Use fast preset
pqa --settings fast ask "Your question"
```

### 2. Improve Quality
```bash
# Use high quality preset
pqa --settings high_quality ask "Your question"

# Increase evidence
pqa --answer.evidence_k 20 ask "Your question"

# Use better model
pqa --llm gpt-4o ask "Your question"
```

### 3. Save Money
```python
# Use local embeddings (free!)
from paperqa import Settings

settings = Settings(
    embedding="st-multi-qa-MiniLM-L6-cos-v1",  # Free
    llm="gpt-4o-mini",  # $0.15 per 1M tokens
)
```

### 4. Debug Issues
```bash
# Verbose output
pqa --verbosity 3 ask "Your question"

# Check index status
pqa --agent.index.paper_directory ~/papers status

# Rebuild index
rm -rf ~/.pqa/indexes/*
pqa index
```

---

## Common Issues & Solutions

### Issue: "No papers found"
**Solution**: Check paper directory path
```bash
# Show current settings
pqa view

# Specify directory explicitly
pqa --agent.index.paper_directory /full/path/to/papers ask "Question"
```

### Issue: "Rate limit exceeded"
**Solution**: Add rate limits
```bash
pqa --llm_config '{"rate_limit": {"gpt-4o": "10000 per 1 minute"}}' ask "Question"

# Or use tier-specific presets
pqa --settings tier1_limits ask "Question"
```

### Issue: "Poor quality answers"
**Solutions**:
1. Check paper relevance (is the answer in your papers?)
2. Increase evidence_k
3. Use better model (gpt-4o instead of gpt-4o-mini)
4. Add more papers to index

### Issue: "Slow performance"
**Solutions**:
1. Use gpt-4o-mini instead of gpt-4o
2. Reduce evidence_k
3. Use local embeddings
4. Batch queries with async

---

## Next Steps

1. **Test the pipeline**: Run through workflows above
2. **Create first research note**: Pick a topic, answer 5 questions
3. **Integrate with workflow**: Connect to Obsidian/Notion
4. **Automate**: Build scripts for recurring research tasks
5. **Scale**: Add more papers, explore STORM integration

---

## Resources

- **PaperQA2 Docs**: https://github.com/Future-House/paper-qa
- **S2 API Tutorial**: https://www.semanticscholar.org/product/api/tutorial
- **STORM GitHub**: https://github.com/stanford-oval/storm
- **Framework Doc**: See `RESEARCH-AGENT-FRAMEWORK.md` in this folder

---

*For questions, check the main framework doc or docs linked above.*
