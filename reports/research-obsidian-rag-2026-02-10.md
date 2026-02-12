# RAG over Obsidian Vault Research Report
**Date:** 2026-02-10  
**Focus:** Building Retrieval-Augmented Generation for local Obsidian knowledge base  
**Vault Location:** `~/Library/Mobile Documents/iCloud~md~obsidian/Documents/System_OS/`

---

## Overview

Retrieval-Augmented Generation (RAG) over an Obsidian vault transforms your personal knowledge base into a queryable AI assistant. Instead of searching manually, you ask questions in natural language and get answers grounded in your notes—with citations and relevance scores.

**The RAG Pipeline:**
```
Question → Vector Search → Retrieve Relevant Notes → Add to LLM Context → Generate Answer
```

**Key Benefits:**
- 🔍 **Semantic search** — Find notes by meaning, not just keywords
- 🧠 **Context-aware answers** — AI cites your actual notes
- 🔒 **100% local** — No cloud, no privacy concerns
- 🔗 **Link-aware** — Follows [[wikilinks]] to expand context (GraphRAG)

**Why this matters for you:**
- Query 10+ years of notes instantly
- "What did I learn about [topic] across all projects?"
- AI synthesizes scattered insights into coherent answers
- Compound your knowledge instead of searching endlessly

---

## Top 3 Options

### 1. **ObsidianRAG Plugin** (Native, Easiest)
**GitHub:** https://github.com/Vasallo94/ObsidianRAG  
**Type:** Native Obsidian plugin + Python backend  
**Status:** ✅ Available now (v3), pending Community Plugin approval

**What it does:**
- Native Obsidian plugin (one-click install)
- 100% local & private (runs on your machine)
- Advanced RAG: Hybrid search (Vector + BM25) + CrossEncoder reranking
- GraphRAG: Follows [[wikilinks]] to expand context
- Real-time streaming answers (token-by-token)
- Source attribution (relevance scores + note links)

**Architecture:**
```
Obsidian Plugin (TypeScript) → HTTP → Backend (Python/FastAPI)
                                          ↓
                                    LangGraph → Ollama LLM
                                          ↓
                                   ChromaDB (Vector Store)
```

**Pros:**
✅ Native plugin experience (ribbon icon, command palette)  
✅ Best-in-class RAG pipeline (hybrid search + reranking)  
✅ GraphRAG (follows note links intelligently)  
✅ Multilingual (works in any language)  
✅ Auto-starts backend server  
✅ Active development (v3 released Feb 2026)  

**Cons:**
❌ Requires Python backend (extra setup)  
❌ Needs Ollama installed (5-10GB models)  
❌ Uses ChromaDB (vector database setup)  
❌ Not yet in Community Plugins (manual install for now)  

**Setup Complexity:** ⭐⭐⭐⚪⚪ (3/5)

**Best for:** Users who want the best RAG quality and don't mind installing Python/Ollama

---

### 2. **Smart Connections Plugin** (Easiest, Most Popular)
**GitHub:** https://github.com/brianpetro/obsidian-smart-connections  
**Type:** Pure Obsidian plugin (no external backend)  
**Status:** ✅ Available in Community Plugins

**What it does:**
- Chat with your notes via AI (GPT-4, Claude, Gemini, or local Llama)
- Semantic search sidebar (see related notes while writing)
- Embedding-based similarity (finds conceptually related notes)
- Works with 100+ LLM providers (OpenAI, Anthropic, local via Ollama)

**Architecture:**
```
Obsidian Plugin → Embeddings (local or API) → Vector Index
                       ↓
                  LLM API (OpenAI/Claude/local) → Chat Interface
```

**Pros:**
✅ One-click install from Community Plugins  
✅ No backend needed (runs entirely in Obsidian)  
✅ Mature & stable (3+ years development)  
✅ Smart Chat feature (conversational interface)  
✅ Flexible LLM choice (cloud or local)  
✅ Large user base (proven in production)  

**Cons:**
❌ Less advanced RAG (no hybrid search or reranking)  
❌ Paid tier for advanced features (Connections Pro)  
❌ Requires API keys (unless using local model)  
❌ No GraphRAG (doesn't follow [[links]])  

**Setup Complexity:** ⭐⭐⚪⚪⚪ (2/5)

**Best for:** Users who want simplicity and don't mind cloud LLM APIs

---

### 3. **Custom RAG Pipeline** (Most Flexible, Most Work)
**Type:** DIY solution (Python script + vector DB + LLM)  
**Status:** Build-it-yourself

**What it does:**
- Full control over every component
- Choose your vector DB (Qdrant, Milvus, Chroma, Pinot, DuckDB)
- Choose your embeddings (OpenAI, Cohere, local Sentence Transformers)
- Choose your LLM (Ollama, Claude API, GPT-4)
- Expose via MCP server or REST API

**Example Stack:**
```
Markdown Parser → Embeddings (paraphrase-multilingual-mpnet-base-v2)
                       ↓
                 Vector DB (Qdrant or DuckDB)
                       ↓
                 Query → Retrieve Top-K → LLM (Ollama) → Answer
```

**Reference Implementations:**
- **DuckDB + MotherDuck:** https://motherduck.com/blog/obsidian-rag-duckdb-motherduck/ (5 days old!)
- **Milvus + Ollama:** https://mcpmarket.com/server/personal-notes-assistant (MCP server)
- **LightRAG:** https://forum.obsidian.md/t/neural-composer-local-graph-rag-made-easy-lightrag-integration/109891 (GraphRAG variant)

**Pros:**
✅ Maximum flexibility (every component customizable)  
✅ Can expose via MCP (integrate with any AI client)  
✅ Production-ready options (DuckDB, Qdrant)  
✅ Serverless deployment possible (MotherDuck)  
✅ Learn the internals (great for understanding RAG)  

**Cons:**
❌ High initial effort (10-20 hours setup)  
❌ Requires programming (Python)  
❌ Maintenance burden (updates, debugging)  
❌ No Obsidian UI (external interface)  

**Setup Complexity:** ⭐⭐⭐⭐⭐ (5/5)

**Best for:** Developers who want full control or need to expose RAG via API/MCP

---

## Comparison Matrix

| Feature | ObsidianRAG | Smart Connections | Custom Pipeline |
|---------|-------------|-------------------|-----------------|
| **Installation** | Medium (plugin + backend) | Easy (plugin only) | Hard (DIY) |
| **RAG Quality** | ★★★★★ (hybrid + rerank) | ★★★⭐⭐ (basic vector) | ★★★★★ (configurable) |
| **GraphRAG** | ✅ Yes | ❌ No | ⚠️ Optional |
| **Local/Private** | ✅ 100% | ⚠️ Depends on LLM | ✅ 100% |
| **Obsidian Integration** | ✅ Native plugin | ✅ Native plugin | ❌ External |
| **LLM Choice** | Ollama (local) | Any (API/local) | Any |
| **Cost** | Free | Free + Paid Pro | Free (self-hosted) |
| **Maintenance** | Low | Very Low | High |
| **Best For** | Quality-focused users | Beginners | Developers |

---

## Implementation Steps

### Option 1: ObsidianRAG (Recommended for Quality)

#### Step 1: Install Backend (10 mins)
```bash
# Install Python package
pip install obsidianrag
# Or use pipx for isolation
pipx install obsidianrag

# Install Ollama
brew install ollama  # macOS
# Or download from https://ollama.ai/

# Pull a model
ollama pull gemma3  # 5GB, good balance
# Alternatives: qwen2.5 (Spanish), llama3.2 (smaller)
```

#### Step 2: Install Plugin (5 mins)
- Download from GitHub Releases: https://github.com/Vasallo94/ObsidianRAG/releases
- Extract to `.obsidian/plugins/obsidianrag/`
- Enable in Obsidian → Settings → Community Plugins

*Once approved for Community Plugins, this will be one-click*

#### Step 3: Configure (5 mins)
- Settings → ObsidianRAG
  - Server Port: 8000 (default)
  - LLM Model: gemma3
  - Auto-start Server: ✅
  - Show Source Links: ✅

#### Step 4: Start & Test (5 mins)
```bash
# Manual start (or enable auto-start)
obsidianrag serve --vault ~/Library/Mobile\ Documents/iCloud~md~obsidian/Documents/System_OS/

# Or from Obsidian:
# Command Palette → "ObsidianRAG: Start Backend Server"
```

**Test queries:**
- "What notes do I have about CNC machining?"
- "Summarize my thoughts on tool management"
- "What did I learn about feeds and speeds?"

**Expected output:**
- Answer text (with markdown)
- Source note links (clickable)
- Relevance scores (0-1, green = high)

**Total time:** 25-30 minutes

---

### Option 2: Smart Connections (Recommended for Simplicity)

#### Step 1: Install Plugin (2 mins)
- Obsidian → Settings → Community Plugins → Browse
- Search "Smart Connections"
- Install + Enable

#### Step 2: Configure (5 mins)
- Settings → Smart Connections
  - Choose LLM provider:
    - **Cloud:** OpenAI (GPT-4), Anthropic (Claude), Google (Gemini)
    - **Local:** Ollama (requires separate install)
  - Add API key (if cloud)
  - Choose embedding model:
    - **Local:** all-MiniLM-L6-v2 (auto-download)
    - **Cloud:** OpenAI text-embedding-3-small

#### Step 3: Index Vault (10-30 mins, one-time)
- Plugin will auto-index on first run
- Progress bar shows notes processed
- Creates `.smart-connections/` folder with embeddings

#### Step 4: Use Smart Chat (0 mins)
- Click "Smart Chat" icon in left ribbon
- Ask questions: "What notes mention [topic]?"
- AI searches vault and provides answers with note links

**Total time:** 15-40 minutes (depending on vault size)

---

### Option 3: Custom Pipeline (Developers Only)

#### High-Level Steps (10-20 hours)
1. **Parse Obsidian vault** (Python: glob .md files)
2. **Chunk notes** (split by headings, paragraphs, or fixed size)
3. **Generate embeddings:**
   ```python
   from sentence_transformers import SentenceTransformer
   model = SentenceTransformer('paraphrase-multilingual-mpnet-base-v2')
   embeddings = model.encode(chunks)
   ```
4. **Store in vector DB:**
   - **DuckDB:** https://motherduck.com/blog/obsidian-rag-duckdb-motherduck/
   - **Qdrant:** `docker run -p 6333:6333 qdrant/qdrant`
   - **Chroma:** `pip install chromadb`
5. **Build query interface:**
   ```python
   def query(question):
       q_emb = model.encode(question)
       results = vector_db.search(q_emb, top_k=5)
       context = "\n".join([r.text for r in results])
       prompt = f"Context:\n{context}\n\nQuestion: {question}"
       return llm.generate(prompt)
   ```
6. **Expose via API or MCP server**

**Recommended Resources:**
- **DuckDB Guide:** https://motherduck.com/blog/obsidian-rag-duckdb-motherduck/
- **RAG Plugin (Beta):** https://forum.obsidian.md/t/developing-obsidian-rag-search-plugin-beta/100876
- **ParthSareen's Repo:** https://github.com/ParthSareen/obsidian-rag

---

## Embedding Models for Personal Knowledge Bases

### Best Embedding Models (2026)

| Model | Size | Best For | License |
|-------|------|----------|---------|
| **paraphrase-multilingual-mpnet-base-v2** | 420MB | Multilingual, Obsidian default | Apache 2.0 |
| **all-MiniLM-L6-v2** | 80MB | Fast, lightweight, English | Apache 2.0 |
| **bge-large-en-v1.5** | 1.3GB | High quality, English | MIT |
| **nomic-embed-text** (Ollama) | 274MB | Ollama-native, good quality | Apache 2.0 |
| **text-embedding-3-small** (OpenAI) | API | Cloud, high quality, $$ | Proprietary |

**Recommendation for your vault:**
- **Local:** `paraphrase-multilingual-mpnet-base-v2` (ObsidianRAG default)
- **Smallest:** `all-MiniLM-L6-v2` (Smart Connections default)
- **Best Quality:** `bge-large-en-v1.5` or OpenAI's `text-embedding-3-small`

**Why embeddings matter:**
- They convert text → vectors (numbers)
- Similar concepts have similar vectors
- Vector search finds semantic matches, not just keywords
- "CNC setup" matches "machine configuration" even if exact words differ

---

## Effort Estimate

| Option | Setup Time | Ongoing Effort | Difficulty |
|--------|------------|----------------|------------|
| **ObsidianRAG** | 30-60 mins | Low (auto-updates) | ⭐⭐⭐ Medium |
| **Smart Connections** | 15-40 mins | Very Low | ⭐⭐ Easy |
| **Custom Pipeline** | 10-20 hours | High (maintenance) | ⭐⭐⭐⭐⭐ Hard |

**Breakdown (ObsidianRAG, recommended):**
1. **Install Python/Ollama:** 10-15 mins (one-time)
2. **Install plugin:** 5 mins (will be instant once in Community Plugins)
3. **Configure:** 5 mins
4. **Test & iterate:** 10-30 mins (learning prompts, tuning settings)
5. **Total:** **30-60 mins** for working RAG system

**Breakdown (Smart Connections):**
1. **Install plugin:** 2 mins
2. **Configure LLM:** 5 mins (API key or Ollama setup)
3. **Index vault:** 10-30 mins (automatic, depends on vault size)
4. **Total:** **15-40 mins**

**Breakdown (Custom Pipeline):**
1. **Research:** 2-4 hours (learning RAG concepts, choosing stack)
2. **Setup environment:** 2-4 hours (Python, vector DB, dependencies)
3. **Implement pipeline:** 4-8 hours (parsing, chunking, indexing)
4. **Build interface:** 2-4 hours (API or CLI)
5. **Testing/debugging:** 2-4 hours
6. **Total:** **10-20 hours**

---

## Links & Sources

### ObsidianRAG
- **GitHub:** https://github.com/Vasallo94/ObsidianRAG
- **Releases:** https://github.com/Vasallo94/ObsidianRAG/releases
- **Features:** Hybrid search, CrossEncoder reranking, GraphRAG
- **Tech Stack:** LangGraph, Ollama, ChromaDB, FastAPI

### Smart Connections
- **GitHub:** https://github.com/brianpetro/obsidian-smart-connections
- **Website:** https://smartconnections.app/
- **Community Plugin:** Available in Obsidian plugin browser
- **Reddit Discussion:** https://www.reddit.com/r/ObsidianMD/comments/1fzmkdk/just_wanted_to_mention_that_the_smart_connections/

### Custom RAG Examples
- **DuckDB + MotherDuck:** https://motherduck.com/blog/obsidian-rag-duckdb-motherduck/ (Feb 2026)
- **Personal Notes Assistant (MCP):** https://mcpmarket.com/server/personal-notes-assistant
- **Neural Composer (LightRAG):** https://forum.obsidian.md/t/neural-composer-local-graph-rag-made-easy-lightrag-integration/109891
- **RAG Plugin (Beta):** https://forum.obsidian.md/t/developing-obsidian-rag-search-plugin-beta/100876
- **ParthSareen's Repo:** https://github.com/ParthSareen/obsidian-rag
- **Laurent's API:** https://laurentcazanove.com/blog/obsidian-rag-api (Meilisearch)

### Vector Databases
- **ChromaDB:** https://www.trychroma.com/ (ObsidianRAG default)
- **Qdrant:** https://qdrant.tech/ (production-ready, Docker)
- **Milvus:** https://milvus.io/ (scalable, cloud-native)
- **DuckDB:** https://duckdb.org/ (serverless, SQL-based)

### Embedding Models
- **SentenceTransformers:** https://www.sbert.net/
- **HuggingFace Models:** https://huggingface.co/sentence-transformers
- **OpenAI Embeddings:** https://platform.openai.com/docs/guides/embeddings
- **Cohere Embeddings:** https://cohere.com/embeddings
- **Best Models 2026:** https://artsmart.ai/blog/top-embedding-models-in-2025/

### RAG Concepts
- **Obsidian Forum (RAG Discussion):** https://forum.obsidian.md/t/obsidian-rag-personal-ai-bot/93020
- **Reddit (LocalLLaMA):** https://www.reddit.com/r/LocalLLaMA/comments/1gp3w02/using_a_rag_to_analyze_journals_and_entries_from/
- **RAG Best Practices:** https://www.openxcell.com/blog/best-embedding-models/

---

## Recommendation for Your Setup

### Immediate: Start with Smart Connections (This Week)
**Why:**
- ✅ Fastest setup (15 mins)
- ✅ Already in Community Plugins
- ✅ Works with Claude API (you're using Anthropic)
- ✅ Proven & stable

**Action:**
1. Install Smart Connections plugin
2. Add Anthropic API key
3. Let it index your vault (coffee break)
4. Test: "What did I document about [recent project]?"

### Medium-term: Upgrade to ObsidianRAG (Month 1)
**Why:**
- ✅ Better RAG quality (hybrid search + reranking)
- ✅ GraphRAG (follows note links)
- ✅ 100% local (no API costs)
- ✅ Real-time streaming

**Action:**
1. Install Ollama + gemma3 model
2. Install ObsidianRAG plugin (from releases)
3. Configure to use your vault path
4. Compare quality vs Smart Connections
5. Keep whichever you prefer

### Long-term: Consider Custom MCP Server (Month 2+)
**Why:**
- ✅ Expose RAG via MCP (works with any AI client)
- ✅ Integrate with other tools (calendar, email)
- ✅ Production-ready stack (DuckDB + serverless)

**Action:**
1. Follow MotherDuck guide (DuckDB + embeddings)
2. Wrap in MCP server (Python SDK)
3. Use from Claude Desktop, OpenClaw, Cursor, etc.

---

## Key Takeaways

✅ **Multiple production-ready options exist** — No need to build from scratch  
✅ **Smart Connections is easiest** — 15 mins to working RAG  
✅ **ObsidianRAG has best quality** — Hybrid search + reranking + GraphRAG  
✅ **100% local is possible** — Ollama + local embeddings (no cloud)  
✅ **Your vault is ready** — iCloud path works fine with all solutions  

⚠️ **Watch out for:**
- **Vault size** — Indexing 10+ years of notes takes 10-30 mins (one-time)
- **Model size** — Ollama models are 2-10GB (ensure disk space)
- **API costs** — If using cloud LLMs (Smart Connections), queries cost $0.001-0.01 each
- **Note format** — RAG works best with well-structured notes (headings, clear topics)

**Bottom line:** Start with Smart Connections this week. If you love it and want better quality, upgrade to ObsidianRAG next month. Your vault is the perfect size for RAG—10+ years of notes = massive value unlock.
