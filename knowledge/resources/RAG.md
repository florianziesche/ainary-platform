---
type: knowledge
last_verified: 2026-02-15
status: evergreen
created: 2026-01-31
tier: KNOWLEDGE
expires: 2027-02-19
---

# RAG (Retrieval-Augmented Generation)

*Your deep expertise area. Document what you know.*

---

## What It Is

RAG combines:
1. **Retrieval** — Find relevant documents/chunks from a knowledge base
2. **Generation** — [[LLM]] generates answer using retrieved context

---

## Key Components

### Embedding Models
- OpenAI `text-embedding-3-small/large`
- Cohere Embed
- Open source: `bge`, `e5`, `instructor`

### Vector Databases
- **Pinecone** — Managed, scales well
- **ChromaDB** — Local, lightweight (you use this)
- **Weaviate** — Hybrid search
- **Qdrant** — Fast, Rust-based

### Chunking Strategies
- Fixed size (512-1024 tokens)
- Semantic chunking
- Document-aware (respect headers, paragraphs)
- Sliding window with overlap

---

## Your Legal [[AI]] Implementation

*From your Legal [[AI]] Platform:*

- Sub-0.2% hallucination rate (how?)
- Multi-agent architecture:
  - **Questioner** — Clarifies query
  - **Researcher** — Retrieves + synthesizes
  - **Validator** — Checks accuracy
  - **Reporter** — Formats output

**What made it work:**
- [Add your learnings]

---

## Common Failure Modes

1. **Wrong chunks retrieved** — Embedding doesn't capture semantic meaning
2. **Lost in the middle** — [[LLM]] ignores middle of long context
3. **Hallucination** — [[LLM]] makes up facts not in context
4. **Stale data** — Index not updated

---

## Best Practices

- Chunk size matters: too small = no context, too big = noise
- Hybrid search (keyword + semantic) often beats pure vector
- Reranking improves precision
- Always show sources to user

---

## Resources

- [Add papers, articles, tutorials]

---

*Last updated: 2026-01-31*