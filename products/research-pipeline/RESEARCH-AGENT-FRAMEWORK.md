# AI-Powered Research Agent Framework
**Status of the Art: Agent-Generated Research (2026)**

*Research completed: 2026-02-10*  
*For: Florian Ziesche*

---

## Executive Summary

AI agents can now autonomously produce research — from literature review to hypothesis generation to full paper writing. This document analyzes 5 leading frameworks and proposes a practical research pipeline tailored to Florian's unique position as Operator + Builder + Investor.

**Key Finding**: We can TODAY deploy a semi-autonomous research pipeline using open-source tools + free APIs.

**Estimated Setup Time**: 2-4 hours  
**Monthly Cost**: €0-50 (depending on API usage)  
**Quality Output**: Wikipedia-level articles → Blog-ready content

---

## 1. State of the Art: Leading Frameworks (2026)

### 1.1 Stanford STORM
**Website**: https://storm.genie.stanford.edu/  
**Status**: ✅ Open source, actively maintained  
**GitHub**: https://github.com/stanford-oval/storm  

#### How It Works
STORM (Synthesis of Topic Outlines through Retrieval and Multi-perspective Question Asking) breaks article generation into two stages:

1. **Pre-writing Stage**
   - Conducts Internet-based research
   - Collects references from multiple perspectives
   - Generates hierarchical outline
   - Uses simulated conversations between "writer" and "expert"

2. **Writing Stage**
   - Populates outline with collected information
   - Adds citations automatically
   - Produces Wikipedia-style articles

#### Key Innovation
**Perspective-Guided Question Asking**: STORM surveys existing articles on similar topics, identifies different perspectives (e.g., technical, business, historical), and uses them to guide the research process. This ensures comprehensive coverage.

#### Real-World Performance
- 70,000+ users tested the live system
- Experienced Wikipedia editors find it "helpful in pre-writing stage"
- Can produce articles on breaking topics faster than human writers

#### Deployment Options
**✅ Can deploy locally:**
```bash
pip install knowledge-storm
# Requires: OpenAI API key OR local LLM via llama.cpp
# Supports: YouRM, BingSearch, BraveRM search engines
```

**💰 Cost per article**: ~$3-10 (depending on depth, using GPT-4o)

#### Co-STORM (Collaborative Version)
- **New in 2024**: Human-in-the-loop variant
- Allows steering the research process interactively
- Maintains dynamic "mind map" of discovered information
- Published at EMNLP 2024

#### Limitations
- Requires access to search APIs (You.com, Bing, etc.)
- Wikipedia style may not match all use cases
- Citations limited to what search engines surface

---

### 1.2 AI Scientist (Sakana AI)
**Website**: https://github.com/SakanaAI/AI-Scientist  
**Status**: ✅ Open source (released Aug 2024)  
**Paper**: https://arxiv.org/abs/2408.06292

#### How It Works
**Full scientific pipeline**: Idea → Experiment → Paper → Review

**Three Templates Provided:**
1. **NanoGPT** (transformer experiments)
2. **2D Diffusion** (generative model research)
3. **Grokking** (neural network generalization)

#### Workflow
1. **Idea Generation**: LLM brainstorms research ideas
2. **Experiment Execution**: Writes & runs Python code
3. **Paper Writing**: Generates LaTeX paper with plots
4. **Automated Review**: LLM provides peer review

#### Key Innovations
- **Executable Research**: Actually runs experiments, not just literature synthesis
- **Self-Review**: Built-in quality control via LLM reviewer
- **Template System**: Easy to extend to new domains

#### Real Output Quality
From their example papers:
- ✅ "DualScale Diffusion: Adaptive Feature Balancing"
- ✅ "StyleFusion: Adaptive Multi-style Generation"
- Papers are technically coherent with real experimental results

#### Deployment Complexity
**⚠️ High computational requirements:**
- Needs GPU for experiments
- Requires Linux + NVIDIA CUDA
- Each paper costs **~$15 with Claude Sonnet 3.5**
- Can take hours to complete full pipeline

#### Limitations
- **Safety concerns**: Executes LLM-written code (requires containerization)
- Limited to domains that can be expressed in code
- Template setup is time-intensive
- Quality varies significantly by base model (Claude >> GPT-4o > others)
- Not suitable for literature reviews or conceptual work

---

### 1.3 PaperQA2 (Future House)
**Website**: https://github.com/Future-House/paper-qa  
**Status**: ✅ Open source, enterprise-grade  
**Paper**: https://arxiv.org/abs/2409.13740

#### How It Works
**High-accuracy RAG (Retrieval-Augmented Generation) specialized for scientific papers**

**Three-Phase Workflow:**

1. **Paper Search**
   - LLM generates keyword queries
   - Searches local PDF repository
   - Chunks, embeds, and indexes papers

2. **Gather Evidence**
   - Embeds user query
   - Ranks top k document chunks
   - Creates contextual summaries
   - LLM re-scores for relevance

3. **Generate Answer**
   - Assembles best summaries
   - Generates answer with in-text citations
   - Includes source attribution

#### Key Innovations
- **Metadata-aware**: Automatically fetches citation counts, journal quality from Semantic Scholar/Crossref
- **Multimodal**: Parses images/tables from PDFs
- **Superhuman performance**: Outperforms humans on scientific Q&A benchmarks

#### Deployment Options
**✅ Multiple interfaces:**
```bash
# CLI interface
pip install paper-qa
pqa ask "What is PaperQA2?"

# Python API
from paperqa import ask
answer = ask("What is PaperQA2?", 
             settings=Settings(paper_directory="my_papers"))

# Agentic mode (autonomous document discovery)
# Manual mode (precise control)
```

#### Cost Structure
- **Free**: Semantic Scholar API (100 req/sec)
- **Paid**: OpenAI embeddings (~$0.13 per 1M tokens)
- **Alternative**: Use local embeddings (sentence-transformers) for €0

#### Advanced Features
- **Hybrid search**: Combines dense embeddings + sparse keyword search
- **LLM-powered enrichment**: Generates synthetic captions for images/tables
- **Supports**: PDF, .txt, .md, .html, .docx, .xlsx, .pptx, code files
- **Quality controls**: Evidence relevance scoring, citation validation

#### Limitations
- Requires you to provide the PDFs (no automatic paper fetching)
- Best with frontier models (GPT-4o, Claude Sonnet)
- Quality degrades significantly with smaller models

---

### 1.4 Elicit (Commercial Tool)
**Website**: https://elicit.com/  
**Status**: ✅ Commercial SaaS  
**Pricing**: Free tier available, Pro from $10/month

#### How It Works
**AI research assistant with 125M+ paper database**

**Core Features:**
- Literature search across massive corpus
- Automated data extraction from papers
- Paper summarization
- Citation finding
- Research alerts (stay updated on topics)

#### Key Capabilities
- Search up to 1,000 relevant papers at once
- Analyze up to 20,000 data points
- Chat with papers
- Extract structured data into tables

#### Business Model
- **Free**: 5,000 one-time credits
- **Basic**: $10/month (12,000 credits/month)
- **Plus**: $42/month (60,000 credits/month + team features)
- **Enterprise**: Custom pricing

#### Strengths
- **Zero setup**: Works immediately
- **Clean UI**: Non-technical users can use it
- **Maintained**: Regular updates and improvements

#### Limitations
- ❌ **Not open source** (vendor lock-in)
- ❌ **Limited customization** (can't tune prompts/models)
- ❌ **Recurring costs** (vs. one-time open source setup)
- ❌ **Black box**: Can't inspect/modify the pipeline

**Verdict for Florian**: Good for quick research, but not for building custom workflows or research products.

---

### 1.5 OpenScholar (Allen Institute for AI)
**Website**: https://open-scholar.allen.ai/  
**Status**: ✅ Fully open source (Nov 2024)  
**Paper**: https://www.nature.com/articles/s41586-025-10072-4 (Nature, Jan 2025)  
**GitHub**: https://github.com/AkariAsai/OpenScholar

#### How It Works
**Retrieval-augmented LM trained on 8M+ open access papers**

**Architecture:**
1. **Custom Retriever**: Trained on peS2o corpus (45M papers)
2. **Reranker**: Reorders results by relevance
3. **Fine-tuned LLM**: Llama 3.1 8B specialized for scientific synthesis
4. **Self-reflection**: Iteratively improves answers

**Full Stack Released:**
- ✅ Training data
- ✅ Model checkpoints (retriever, reranker, LLM)
- ✅ 45M paper datastore + embeddings
- ✅ Evaluation benchmark (ScholarQABench)

#### Key Innovations
- **Self-reflective generation**: Model checks its own output and retrieves more papers if needed
- **Post-hoc citation attribution**: Adds citations after generation
- **Semantic Scholar integration**: Live API calls during inference
- **Outperforms GPT-4o** on scientific question answering

#### Deployment Complexity
**⚠️ Requires significant resources:**
- 200M+ embeddings = Massive CPU memory needed
- Datastore: 45M papers chunked + indexed
- Recommended: Use their hosted demo OR wait for S2 API integration

**Easier path:**
```python
# Use OpenScholar models with your own documents
python run.py \
  --model_name OpenScholar/Llama-3.1_OpenScholar-8B \
  --use_contexts --top_n 10
```

#### Unique Strengths
- **Truly open**: Everything from data to training recipes
- **Scientific specialist**: Not a general-purpose LLM
- **Citation-aware**: Filters by citation count, journal quality
- **Expert validation**: Matches domain experts on complex queries

#### Limitations
- Heavy infrastructure requirements for full deployment
- Focused on literature synthesis, not experimental research
- Requires expertise to customize/extend

---

## 2. Framework Comparison Matrix

| Framework | Type | Open Source | Local Deploy | Cost/Article | Best For |
|-----------|------|-------------|--------------|--------------|----------|
| **STORM** | Article Generation | ✅ Yes | ✅ Easy | $3-10 | Wikipedia-style reports |
| **AI Scientist** | Full Pipeline | ✅ Yes | ⚠️ Complex | $15+ | Experimental research |
| **PaperQA2** | RAG Q&A | ✅ Yes | ✅ Easy | $0-5 | Literature Q&A, citations |
| **Elicit** | SaaS Tool | ❌ No | ❌ No | $10-42/mo | Quick searches |
| **OpenScholar** | Scientific LLM | ✅ Yes | ⚠️ Complex | Variable | Scientific synthesis |

**Ease of Setup Ranking**: PaperQA2 > STORM >> OpenScholar > AI Scientist

---

## 3. Florian's Research Pipeline: Practical Implementation

### Design Principles
1. **Leverage your unique position**: Operator + Builder + Investor perspective
2. **Automate the grind**: Literature reviews, citation gathering, trend scanning
3. **Enhance, don't replace**: AI drafts → Florian adds insights → High-value output
4. **Own your stack**: Open source = customizable + no recurring costs
5. **Ship fast**: Start simple, iterate based on what works

---

### Phase 1: Topic Scanning (Automated SOTA Scanner)
**Goal**: Identify trends, gaps, and hot topics automatically

**Tools**: 
- **Semantic Scholar API** (free, 100 req/sec)
- **PaperQA2** for scanning recent papers

**Implementation**:
```python
# Weekly trend scanner
# 1. Query S2 API for papers in target domains
#    - AI agents, VC tech, manufacturing software
# 2. Filter by: citation velocity, recent (last 3 months)
# 3. Cluster by topic using embeddings
# 4. Generate weekly "What's Hot" report
```

**Output**: Weekly email/Notion page with:
- Top 5 trending topics
- Papers gaining traction fast
- Gaps in current research
- Potential thesis angles

**Time Investment**: 
- Setup: 2-3 hours
- Maintenance: Runs automatically

---

### Phase 2: Literature Review (Semi-Automatic)
**Goal**: Deep dive on a selected topic, gather + organize relevant papers

**Tools**:
- **PaperQA2** (local deployment)
- **Semantic Scholar API** for metadata enrichment
- **Obsidian** for note organization

**Workflow**:
```bash
# Step 1: Gather papers on topic
pqa --index [topic_name] ask "What are the key papers on [topic]?"

# Step 2: Cluster papers by subtopic
# Use PaperQA2's chunking + embeddings

# Step 3: Generate summaries per cluster
# Automated contextual summarization

# Step 4: Export to Obsidian
# Create linked notes with citations
```

**Output**:
- Cluster map of literature (visual)
- 1-page summaries per cluster
- Citation network (who cites whom)
- Identified gaps + open questions

**Time Investment**:
- Manual: 6-8 hours per topic
- With AI: 1-2 hours (setup + review)

---

### Phase 3: Gap Analysis (AI + Human)
**Goal**: Identify what's missing + where Florian's perspective adds value

**Process**:
1. **AI identifies factual gaps**
   - "What research questions remain unanswered?"
   - "What methodologies haven't been tried?"
   
2. **Florian identifies perspective gaps**
   - Where is the operator view missing?
   - What do investors need to know that researchers don't cover?
   - What can builders learn from this research?

**Tool**: PaperQA2 + Custom prompts

**Example Prompt**:
```
Given this literature review on [topic], identify:
1. Unanswered research questions
2. Practical implementation gaps (theory vs. practice)
3. Investor perspectives missing from academic work
4. Opportunities for operator insights

Literature: [PaperQA2 output]
```

**Output**:
- Gap analysis doc (2-3 pages)
- Ranked list of thesis opportunities
- Unique angle identification

---

### Phase 4: Hypothesis / Thesis (Human-Led, AI-Assisted)
**Goal**: Florian formulates thesis, AI provides supporting evidence + counter-arguments

**Process**:
1. **Florian drafts thesis** (1-2 paragraphs)
2. **AI gathers supporting evidence** (PaperQA2)
3. **AI generates counter-arguments** (STORM-style multi-perspective)
4. **Florian refines thesis** based on evidence

**Tool Setup**:
```python
# Custom PaperQA2 workflow
thesis = "AI agents will replace middle management in operations"

# Find supporting evidence
support = pqa.ask(f"What evidence supports: {thesis}")

# Find counter-arguments
counter = pqa.ask(f"What evidence contradicts: {thesis}")

# Steel-man the opposing view
steelman = pqa.ask(f"What is the strongest argument against: {thesis}")
```

**Output**:
- Thesis statement (refined)
- Supporting evidence (with citations)
- Addressed counter-arguments
- Confidence level + caveats

---

### Phase 5: Writing (AI Draft → Human Edit)
**Goal**: Produce high-quality blog post / article with Florian's voice + insights

**Tools**:
- **STORM** for initial structure
- **PaperQA2** for citation-backed claims
- **Florian** for unique insights + voice

**Workflow**:
1. **STORM generates outline** (30 min)
   ```bash
   storm_runner.run(
     topic="AI Agents in Operations",
     do_research=True,
     do_generate_outline=True
   )
   ```

2. **PaperQA2 populates with citations** (1 hour)
   - For each section, query relevant evidence
   - Insert citations automatically

3. **Florian edits for voice + insights** (2-3 hours)
   - Add personal anecdotes (Operator)
   - Add implementation advice (Builder)
   - Add investment thesis (Investor)
   - Refine language for audience

4. **AI polish** (15 min)
   - Check citation formatting
   - Improve transitions
   - SEO optimization

**Output Quality**:
- **Structure**: Wikipedia-level (comprehensive, well-organized)
- **Citations**: Academic-level (properly sourced)
- **Insights**: Florian-level (unique, actionable)
- **Voice**: Professional but personal

**Time Investment**:
- Old way: 12-16 hours
- With pipeline: 4-6 hours
- **Time saved: 60-70%**

---

### Phase 6: Distribution (Automated)
**Goal**: Repurpose single article → multiple formats/channels

**Channels**:
- Blog (primary)
- LinkedIn post
- Twitter thread
- Substack newsletter
- Obsidian (archive)

**Repurposing Engine** (can build with n8n):
```
Blog post (3000 words)
  ├─> LinkedIn post (300 words, 3 key takeaways)
  ├─> Twitter thread (10 tweets, punchy)
  ├─> Email newsletter (800 words, story format)
  └─> Obsidian archive (linked to source papers)
```

**Tools**:
- **n8n** for automation workflows
- **Custom prompts** for format adaptation
- **Manual review** before publishing (5-10 min per channel)

---

## 4. Concrete Tools We Can Deploy TODAY

### 4.1 Semantic Scholar API
**What It Does**: Metadata for 200M+ papers (citations, authors, abstracts, PDFs)

**Why Use It**:
- ✅ Free (100 requests/sec)
- ✅ No rate limits with API key
- ✅ Rich metadata (citation counts, journal quality, open access status)
- ✅ Used by all major research tools (PaperQA2, OpenScholar, Elicit)

**Quick Start**:
```python
import requests

S2_API_KEY = "your_key"  # Get from semanticscholar.org/product/api

# Search papers
response = requests.get(
    "https://api.semanticscholar.org/graph/v1/paper/search",
    params={
        "query": "AI agents",
        "fields": "title,abstract,citationCount,year,authors",
        "limit": 100
    },
    headers={"x-api-key": S2_API_KEY}
)

papers = response.json()
```

**Use Cases**:
1. **Topic scanning**: Find hot papers (high citation velocity)
2. **Citation networks**: Map relationships between papers
3. **Author tracking**: Follow specific researchers
4. **PDF access**: Get open access PDFs automatically

**Integration**: Works out-of-box with PaperQA2

---

### 4.2 STORM (Open Source)
**What It Does**: Generates Wikipedia-style articles from scratch

**Deployment**:
```bash
# Install
pip install knowledge-storm

# Setup
export OPENAI_API_KEY="sk-..."
export YDC_API_KEY="..."  # You.com search

# Run
python -c "
from knowledge_storm import STORMWikiRunner, Settings

runner = STORMWikiRunner(
    Settings(paper_directory='my_papers')
)
runner.run(
    topic='AI Agents in Operations',
    do_research=True,
    do_generate_outline=True,
    do_generate_article=True
)
"
```

**When to Use**:
- New topic exploration (you know little about it)
- Need comprehensive overview
- Want to see multiple perspectives
- Prefer structured article format

**Limitations**:
- Wikipedia style (may need rewriting for blog)
- Requires search API access
- Best with frontier models (GPT-4o, Claude)

---

### 4.3 PaperQA2 (Open Source)
**What It Does**: Answer questions by citing scientific papers

**Deployment**:
```bash
# Install
pip install paper-qa

# Index your papers
mkdir research_papers
# Add PDFs...

# Query
pqa --settings high_quality \
    --agent.index.paper_directory research_papers \
    ask "What are the limitations of current AI agents?"
```

**When to Use**:
- Need specific answers with citations
- Building on existing literature
- Quality control (fact-checking claims)
- Extracting insights from large corpus

**Advanced Setup**:
```python
# Use local embeddings (free)
from paperqa import Settings

settings = Settings(
    embedding="st-multi-qa-MiniLM-L6-cos-v1",  # Free local model
    llm="gpt-4o-mini",  # Cheaper than GPT-4o
    summary_llm="gpt-4o-mini"
)
```

---

### 4.4 OpenScholar (Open Source)
**What It Does**: Scientific LLM specialized for literature synthesis

**When to Use**:
- Need highest quality scientific synthesis
- Working in well-researched domains
- Want expert-level analysis

**Deployment Note**:
- Full deployment is complex (200M embeddings)
- **Recommendation**: Wait for Semantic Scholar API integration (coming soon)
- **Alternative**: Use their hosted demo for now (https://open-scholar.allen.ai/)

**Future Integration**:
Once S2 API integrates OpenScholar retriever, it becomes plug-and-play like PaperQA2.

---

## 5. Recommended Starting Stack for Florian

### Minimum Viable Research Pipeline (MVP)

**Phase 1 Goal**: Prove value in 1 month

**Stack**:
1. **Semantic Scholar API** (free)
   - Paper discovery + metadata

2. **PaperQA2** (open source)
   - Literature Q&A
   - Citation-backed answers

3. **Claude/GPT-4o** (via API)
   - Drafting, editing, repurposing

4. **Obsidian** (existing)
   - Note storage + linking

5. **n8n** (optional for now)
   - Add later for distribution automation

**Total Monthly Cost**: €20-50 (API usage only)

**Setup Time**: 3-4 hours
- Install PaperQA2: 30 min
- Get S2 API key: 5 min
- Create first index: 30 min
- Test workflow: 2 hours

---

### First Project: Prove It Works

**Topic**: "AI Agents in VC: When to Build vs. Buy"
- Relevant to your fundraising work
- Combines operator + investor perspective
- Hot topic (high engagement)

**Timeline**: 2 weeks
- Week 1: Research (use pipeline, 6-8 hours)
- Week 2: Write (3-4 hours) + Distribute (1 hour)

**Success Metrics**:
- Article published
- Time spent < 50% of manual approach
- Quality >= previous blog posts
- 100+ LinkedIn impressions

---

## 6. Implementation Roadmap

### Week 1: Setup (3-4 hours)
- [ ] Install PaperQA2 locally
- [ ] Get Semantic Scholar API key
- [ ] Index 20-30 papers on a test topic
- [ ] Run first query + review quality

### Week 2: First Article (8-10 hours)
- [ ] Topic selection (30 min)
- [ ] Literature review with PaperQA2 (2 hours)
- [ ] Gap analysis (1 hour)
- [ ] Thesis formulation (1 hour)
- [ ] Draft with AI assistance (3 hours)
- [ ] Edit + publish (2 hours)

### Week 3: Refine Process
- [ ] Document what worked / what didn't
- [ ] Create reusable prompts
- [ ] Build templates (Obsidian + n8n)

### Week 4: Scale
- [ ] Add STORM for new topics
- [ ] Automate topic scanning (weekly)
- [ ] Set up distribution pipeline (n8n)

---

## 7. Advanced: Building Research Products

Once the basic pipeline works, you can productize it:

### Product 1: Weekly AI Trends Newsletter
- **Automated topic scanning** (S2 API)
- **AI-generated summaries** (PaperQA2)
- **Florian's commentary** (5-10 min per week)
- **Distribution** (Substack, LinkedIn)

**Unique angle**: "AI trends through an operator's lens"

### Product 2: Deep Dive Reports (Gated)
- **Monthly long-form research** (3000+ words)
- **Premium quality** (STORM + PaperQA2 + human insight)
- **Subscriber exclusive** (Substack paid tier)

### Product 3: VC Decision Support Tool
- **Custom PaperQA2 index** (AI papers + startup news)
- **Investment thesis validation** ("Is this technology ready?")
- **Share with LPs** (demonstrate research depth)

---

## 8. Key Learnings from SOTA Research

### What Works
1. **RAG >> Pure Generation**: Grounding in sources dramatically improves accuracy
2. **Multi-step Pipelines**: Break complex tasks (research → outline → write → review)
3. **Self-Reflection**: LLMs that check their own output produce better results
4. **Hybrid Search**: Combine dense embeddings + sparse keywords
5. **Human-in-Loop**: AI drafts, humans refine = 10x productivity boost

### What Doesn't Work Yet
1. **Fully Autonomous Research**: Still needs human oversight
2. **Novel Hypothesis Generation**: AI suggests known ideas, not breakthrough insights
3. **Evaluating Groundbreaking Work**: AI struggles with truly novel research
4. **Complex Causal Reasoning**: "Why" questions still challenging

### The Sweet Spot
AI excels at:
- Literature review (comprehensive, fast)
- Citation management (tedious, automated)
- Structure generation (outlines, organization)
- Initial drafting (rough but complete)

Humans still needed for:
- Unique insights (lived experience)
- Judgment calls (what matters?)
- Voice and style (personality)
- Ethical considerations

**→ Florian's advantage**: You bring all four human elements, AI handles the grunt work.

---

## 9. Open Questions & Future Research

### Technical Questions
1. **How to measure "insight density"?**
   - Can we quantify when AI adds vs. regurgitates?
   
2. **When does retrieval hurt vs. help?**
   - For creative thinking, should we turn OFF retrieval?

3. **How to evaluate research quality automatically?**
   - Citation counts lag by years
   - Need real-time quality signals

### Product Questions
1. **What format do investors actually want?**
   - Long-form? Bullet points? Visual?
   
2. **How to price research products?**
   - Newsletter: Free or paid?
   - Deep dives: €50? €500?

3. **What's the moat?**
   - If tools are open source, where's the differentiation?
   - Answer: Unique perspective + proprietary index

---

## 10. Resources & Links

### Tools Documentation
- **PaperQA2**: https://github.com/Future-House/paper-qa
- **STORM**: https://github.com/stanford-oval/storm
- **OpenScholar**: https://github.com/AkariAsai/OpenScholar
- **Semantic Scholar API**: https://www.semanticscholar.org/product/api/tutorial

### Research Papers
- **PaperQA2 Paper**: https://arxiv.org/abs/2409.13740
- **STORM Paper**: https://arxiv.org/abs/2402.14207
- **AI Scientist Paper**: https://arxiv.org/abs/2408.06292
- **OpenScholar Paper**: https://www.nature.com/articles/s41586-025-10072-4

### Communities
- **PaperQA Discord**: (via GitHub)
- **DSPy Community**: https://github.com/stanfordnlp/dspy (used by STORM)
- **r/LocalLLaMA**: Good for open source LLM discussions

---

## 11. Next Actions for Florian

### Immediate (This Week)
1. **Install PaperQA2** (30 min)
   ```bash
   pip install paper-qa
   export OPENAI_API_KEY="sk-..."
   ```

2. **Get Semantic Scholar API Key** (5 min)
   - Visit: https://www.semanticscholar.org/product/api
   - Request key (instant approval)

3. **Test Query** (15 min)
   ```bash
   # Add a few PDFs to a folder
   pqa --agent.index.paper_directory ~/papers \
       ask "What are the main challenges in AI agent research?"
   ```

4. **Decide on First Topic** (30 min)
   - What's timely + relevant?
   - Where can you add unique value?

### Short-Term (Next 2 Weeks)
1. **Complete First Article** using the pipeline
2. **Document Your Process** (what worked, what didn't)
3. **Share Draft** for feedback (test audience)

### Medium-Term (Next Month)
1. **Refine Pipeline** based on learnings
2. **Build Reusable Templates** (prompts, structures)
3. **Automate Topic Scanning** (weekly trend report)

### Long-Term (Next Quarter)
1. **Productize Research** (newsletter, reports)
2. **Integrate with n8n** (full automation)
3. **Explore OpenScholar** (when S2 API integration launches)

---

## Conclusion

**The Opportunity**: AI can now handle 60-70% of research work—the tedious parts. You focus on the 30% that matters: unique insights, judgment, and voice.

**The Path**: Start simple (PaperQA2 + S2 API), prove value in 2 weeks, then scale.

**The Moat**: Not the tools (everyone will have them), but your unique position as Operator + Builder + Investor. That's what readers can't get from pure AI.

**The Timeline**: Fully operational research pipeline in 1 month. First high-quality output in 2 weeks.

---

*Framework compiled by: King (AI Research Assistant)*  
*For questions or updates, refer to workspace: `products/research-pipeline/`*
