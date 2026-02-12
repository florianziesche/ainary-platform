# Research Tools Detailed Comparison (2026)

---

## Quick Reference Matrix

| Tool | Type | License | Setup | Cost | Best For |
|------|------|---------|-------|------|----------|
| **PaperQA2** | RAG Q&A | Open (Apache 2.0) | ⭐ Easy | €0-10/month | Citation-backed answers |
| **STORM** | Article Gen | Open (MIT) | ⭐⭐ Medium | €3-10/article | Wikipedia-style reports |
| **AI Scientist** | Full Pipeline | Open (RAISL) | ⭐⭐⭐ Hard | €15+/paper | Experimental research |
| **OpenScholar** | Scientific LLM | Open (Apache 2.0) | ⭐⭐⭐ Hard | Variable | Scientific synthesis |
| **Elicit** | SaaS | Proprietary | ⭐ Instant | €10-42/month | Quick searches |
| **Consensus** | SaaS | Proprietary | ⭐ Instant | Free-€20/month | Paper discovery |
| **Perplexity** | SaaS | Proprietary | ⭐ Instant | €20/month | General research |

---

## Detailed Comparison

### 1. PaperQA2

#### Overview
High-accuracy RAG system for scientific literature with citations.

#### Strengths
- ✅ Easy setup (pip install)
- ✅ Excellent citation quality
- ✅ Multimodal (images/tables in PDFs)
- ✅ Superhuman performance on benchmarks
- ✅ Flexible (works with any LLM/embedding)
- ✅ Active development (Future House)

#### Weaknesses
- ❌ Requires you to provide PDFs
- ❌ Best with frontier models (expensive)
- ❌ No automatic paper discovery
- ❌ Learning curve for advanced features

#### Cost Breakdown
- **Setup**: Free (open source)
- **Embeddings**: €0.13 per 1M tokens (OpenAI) OR free (local)
- **LLM calls**: €2-10 per 1000 queries (depends on model)
- **Total monthly**: €0-50 for moderate use

#### When to Use
- Need precise answers with citations
- Building on existing literature
- Quality control (fact-checking)
- Custom research workflows

#### When NOT to Use
- Need automatic paper discovery
- Want fully automated research
- Working with non-technical users

---

### 2. STORM

#### Overview
Generates comprehensive Wikipedia-style articles through multi-perspective research.

#### Strengths
- ✅ Comprehensive coverage
- ✅ Multiple perspectives (avoids bias)
- ✅ Good structure (outline → article)
- ✅ Active research project (Stanford)
- ✅ Co-STORM for human-in-loop

#### Weaknesses
- ❌ Requires search API access (costs)
- ❌ Wikipedia style (may need adaptation)
- ❌ Takes time (30-60 min per article)
- ❌ Citations limited to search results

#### Cost Breakdown
- **Setup**: Free (open source)
- **Search API**: €0-20/month (You.com, Bing)
- **LLM calls**: €3-10 per article
- **Total per article**: €3-15

#### When to Use
- Exploring new topics (comprehensive overview)
- Need structured long-form content
- Want multiple perspectives
- Building knowledge bases

#### When NOT to Use
- Need quick answers
- Have specific papers to cite
- Want non-Wikipedia format
- Working without internet

---

### 3. AI Scientist

#### Overview
Full pipeline from idea generation → experiments → paper → review.

#### Strengths
- ✅ Complete research automation
- ✅ Actually runs experiments
- ✅ Generates real papers (LaTeX)
- ✅ Self-review mechanism
- ✅ Template system (extensible)

#### Weaknesses
- ❌ High complexity (GPU required)
- ❌ Limited to code-based research
- ❌ Safety concerns (executes LLM code)
- ❌ Template setup is time-intensive
- ❌ Quality varies by model

#### Cost Breakdown
- **Setup**: Free (open source)
- **Compute**: Requires GPU (€0.50-2/hour)
- **LLM calls**: €15-30 per paper
- **Total per paper**: €20-50

#### When to Use
- Experimental ML research
- Have GPU infrastructure
- Need reproducible experiments
- Exploring research ideas at scale

#### When NOT to Use
- Literature reviews
- Conceptual research
- No GPU access
- Need human-level insights

---

### 4. OpenScholar

#### Overview
Retrieval-augmented LM specialized for scientific literature (45M papers).

#### Strengths
- ✅ Fully open (data + models + code)
- ✅ Outperforms GPT-4o on science Q&A
- ✅ Self-reflective (improves own answers)
- ✅ Citation-aware (filters by quality)
- ✅ Published in Nature (2025)

#### Weaknesses
- ❌ Heavy infrastructure (200M embeddings)
- ❌ Complex deployment
- ❌ Focused on literature synthesis only
- ❌ Best performance requires full setup

#### Cost Breakdown
- **Setup**: Free (open source)
- **Infrastructure**: High (200M embeddings → 100GB+ RAM)
- **LLM calls**: Variable (can use open models)
- **Hosted demo**: Free (Allen AI)

#### When to Use
- Need highest quality scientific synthesis
- Have infrastructure
- Want open research stack
- Building scientific products

#### When NOT to Use
- Limited compute resources
- Need quick setup
- Working outside academic domains

---

### 5. Elicit

#### Overview
Commercial AI research assistant with 125M+ paper database.

#### Strengths
- ✅ Zero setup (instant)
- ✅ Clean UI (non-technical friendly)
- ✅ Large corpus (125M papers)
- ✅ Data extraction (tables)
- ✅ Research alerts
- ✅ Regular updates

#### Weaknesses
- ❌ Not open source (vendor lock-in)
- ❌ Limited customization
- ❌ Recurring costs
- ❌ Black box (can't inspect pipeline)
- ❌ No local deployment

#### Cost Breakdown
- **Free**: 5,000 credits (one-time)
- **Basic**: €10/month (12k credits)
- **Plus**: €42/month (60k credits)
- **Enterprise**: Custom

#### When to Use
- Need instant results
- Non-technical team members
- Quick exploratory research
- Don't want to manage infrastructure

#### When NOT to Use
- Building custom workflows
- Need full control
- Want to avoid vendor lock-in
- Have tight budget (long-term)

---

### 6. Consensus (Bonus)

#### Overview
AI-powered search for scientific papers with consensus extraction.

#### Strengths
- ✅ Shows scientific consensus
- ✅ 200M+ papers
- ✅ Free tier available
- ✅ Good for fact-checking

#### Weaknesses
- ❌ Limited to yes/no questions
- ❌ No full-text access
- ❌ Less flexible than Elicit

#### Cost
- **Free**: 20 searches/month
- **Premium**: €20/month (unlimited)

#### When to Use
- Quick fact-checking
- Finding consensus on questions
- Non-academic users

---

## Feature Comparison

| Feature | PaperQA2 | STORM | AI Scientist | OpenScholar | Elicit |
|---------|----------|-------|--------------|-------------|--------|
| **Paper Discovery** | ❌ Manual | ✅ Auto | ❌ N/A | ✅ Built-in | ✅ Built-in |
| **Citation Quality** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| **Answer Quality** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Customization** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐ |
| **Ease of Use** | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Speed** | ⭐⭐⭐⭐ | ⭐⭐ | ⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Cost Efficiency** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |

---

## Use Case Matrix

### Literature Review
1. **PaperQA2** (best for owned PDFs)
2. OpenScholar (best for broad corpus)
3. Elicit (best for speed)
4. STORM (best for comprehensive)

### Question Answering
1. **PaperQA2** (best accuracy)
2. OpenScholar (best for science)
3. Elicit (best for speed)

### Article Writing
1. **STORM** (best structure)
2. PaperQA2 (best citations)
3. AI Scientist (if experimental)

### Paper Discovery
1. **Elicit** (easiest)
2. OpenScholar (most comprehensive)
3. Semantic Scholar API (most flexible)

### Experimental Research
1. **AI Scientist** (only option)

---

## Decision Tree

```
START
│
├─ Need to run experiments?
│  └─ YES → AI Scientist
│  └─ NO → Continue
│
├─ Have PDFs already?
│  └─ YES → PaperQA2
│  └─ NO → Continue
│
├─ Need comprehensive article?
│  └─ YES → STORM
│  └─ NO → Continue
│
├─ Want zero setup?
│  └─ YES → Elicit
│  └─ NO → Continue
│
├─ Have infrastructure?
│  └─ YES → OpenScholar
│  └─ NO → PaperQA2 or Elicit
```

---

## Recommended Stack by Persona

### Academic Researcher
- **Primary**: PaperQA2 (citations) + OpenScholar (synthesis)
- **Secondary**: AI Scientist (if experimental)
- **Tools**: Semantic Scholar API, Zotero

### Content Creator / Writer
- **Primary**: STORM (articles) + PaperQA2 (fact-check)
- **Secondary**: Elicit (quick searches)
- **Tools**: Obsidian, Grammarly

### VC / Investor (Florian!)
- **Primary**: PaperQA2 (due diligence) + STORM (theses)
- **Secondary**: Elicit (speed), Consensus (fact-check)
- **Tools**: Notion, Obsidian

### Startup Operator
- **Primary**: Elicit (speed) + PaperQA2 (deep dives)
- **Secondary**: STORM (knowledge base)
- **Tools**: Notion, Slack

### Independent Researcher
- **Primary**: PaperQA2 (cheap + flexible)
- **Secondary**: STORM (comprehensive)
- **Tools**: Local LLMs, Obsidian

---

## Integration Patterns

### Pattern 1: Discovery → Deep Dive
1. **Elicit** for initial paper discovery
2. **Download PDFs** from results
3. **PaperQA2** for deep Q&A
4. **Obsidian** for note-taking

### Pattern 2: Comprehensive Research
1. **STORM** for topic overview + outline
2. **PaperQA2** for detailed evidence on each section
3. **Manual editing** for voice + insights
4. **n8n** for distribution

### Pattern 3: Experimental Workflow
1. **Literature review** with PaperQA2
2. **Identify gaps** manually
3. **AI Scientist** for experiments
4. **PaperQA2** for related work section

### Pattern 4: Continuous Learning
1. **Semantic Scholar API** for new paper alerts
2. **PaperQA2** for quick summaries
3. **STORM** for quarterly deep dives
4. **Obsidian** for knowledge base

---

## Cost Comparison (Monthly)

### Light Use (5 hours/month)
- **PaperQA2**: €5 (API calls)
- **STORM**: €15 (2 articles)
- **Elicit Free**: €0
- **Total DIY**: €20

### Moderate Use (20 hours/month)
- **PaperQA2**: €20
- **STORM**: €60 (6 articles)
- **Elicit Basic**: €10
- **Total DIY**: €80
- **Total SaaS**: €10

### Heavy Use (60 hours/month)
- **PaperQA2**: €50
- **STORM**: €180 (18 articles)
- **Elicit Plus**: €42
- **Total DIY**: €230
- **Total SaaS**: €42

**Verdict**: SaaS wins on heavy use if you just need search. DIY wins if you need customization or citations.

---

## Future Outlook (2026+)

### Likely Improvements
1. **OpenScholar S2 API**: Makes deployment trivial
2. **STORM + PaperQA2 integration**: Best of both
3. **Local LLMs**: Cost → €0 for inference
4. **Multimodal advances**: Better figure/table understanding

### Emerging Tools
- **Research agents with tool use** (LangChain, LlamaIndex)
- **Specialized scientific LLMs** (Med-PaLM, etc.)
- **Collaborative research platforms** (Notion AI, etc.)

### Recommendation
Start with **PaperQA2** (easy, flexible, cheap). Add **STORM** if you write long-form. Avoid **Elicit** unless you need instant gratification or have non-technical team. Watch **OpenScholar** for when S2 API integrates it.

---

*Last updated: 2026-02-10*  
*For implementation guides, see `QUICK-START-GUIDE.md`*
