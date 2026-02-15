# Claim Ledger — AR-032: Knowledge Compounding with AI: Obsidian + Agent

**Created:** 2026-02-15  
**Tier:** 2  
**Claims:** 20  

Badge Key: **E** = Empirical | **I** = Inferred | **J** = Judgment | **A** = Anecdotal

---

## Core Claims

**C1** [E] Chunk size significantly affects retrieval quality in RAG systems. Smaller chunks (64-128 tokens) are optimal for fact-based queries; larger chunks (512-1024 tokens) are better for contextual understanding.  
Sources: [S7] Fraunhofer arXiv, [S12] NVIDIA  
Confidence: 90% — replicated across multiple datasets and embedding models.

**C2** [E] Anthropic's Contextual Retrieval reduces failed retrievals by 49% (67% with reranking) by prepending document-level context to each chunk before embedding.  
Sources: [S9] Anthropic  
Confidence: 85% — single-vendor benchmark but methodologically sound.

**C3** [I] Atomic notes (~200 words, one idea per note) are structurally equivalent to well-formed chunks for embedding-based retrieval, making Zettelkasten-style vaults inherently better suited for AI retrieval than long-form notes.  
Sources: [S7], [S8], [S17] Weaviate ("small and focused chunks capture one clear idea → precise embedding")  
Confidence: 70% — **No direct measurement exists** on actual PKM vaults. Inferred from chunking research applied to note structure. This is the central unvalidated claim of the report.

**C4** [E] Default settings for popular chunking strategies often produce poor retrieval performance. Parameterization matters more than strategy choice.  
Sources: [S8] Chroma Research  
Confidence: 85% — controlled evaluation with reproducible code.

**C5** [J] The value of Zettelkasten for AI integration lies in the *thinking process* of creating atomic notes, not in the manual linking. RAG may automate link discovery, but cannot automate the articulation of ideas.  
Sources: [S14] Sascha Fast ("you can't automate what you can't articulate"), [S15] AI Productivity Playbook  
Confidence: 60% — judgment based on expert opinion. No empirical test of this decomposition.

**C6** [A] AI-organized PKM systems (where AI handles filing, tagging, linking) achieve higher sustained usage than manual systems. Case study: COG system used for 3+ months after 5 previous abandoned attempts.  
Sources: [S13] DEV.to (COG case study)  
Confidence: 40% — single anecdotal case (N=1). Pattern resonates with widespread PKM abandonment but lacks controlled comparison.

**C7** [E] YAML frontmatter metadata (tags, aliases) is NOT indexed by at least one major Obsidian AI plugin (Copilot), meaning carefully curated human metadata is invisible to AI retrieval.  
Sources: [S18] GitHub issue #1471  
Confidence: 80% — confirmed by feature request as of April 2025. May have been fixed since.

**C8** [I] MCP (Model Context Protocol) represents a paradigm shift from plugin-based to protocol-based AI integration for PKM, enabling any AI assistant to interact with any vault.  
Sources: [S6] MCP-Obsidian ecosystem (multiple implementations)  
Confidence: 75% — multiple implementations exist, but adoption is early-stage.

**C9** [E] Obsidian has grown beyond 1 million users, indicating a large addressable market for PKM + AI integration.  
Sources: [S5] Obsidian official blog  
Confidence: 95% — first-party data.

**C10** [I] Hybrid retrieval (semantic embeddings + BM25 keyword matching) outperforms either method alone for PKM queries, because personal notes contain both conceptual ideas and specific identifiers (dates, names, project codes).  
Sources: [S9] Anthropic, [S16] PKM+RAG Medium article  
Confidence: 75% — well-established in enterprise RAG; not directly tested on personal vaults.

---

## Building on AR-015/025/026

**C11** [I] AR-015's finding that "quality does not compound but efficiency does" applies to PKM + AI: AI retrieval doesn't make your *notes* better, but it makes *finding and using* them dramatically more efficient.  
Sources: AR-015 (internal), [S13] COG case study  
Confidence: 70% — consistent with our own data (QA scores flat, token usage down 50%).

**C12** [I] AR-015's three compounding proxies (emergence rate, self-reference ratio, value per note) can be operationalized for PKM + AI measurement: emergence = questions answerable by combining notes; self-reference = internal citations in new outputs; value per note = retrieval frequency × output contribution.  
Sources: AR-015 (internal)  
Confidence: 65% — framework exists but remains untested outside our own system.

**C13** [J] The "graveyard problem" (AR-015: most notes are never retrieved) is the single biggest barrier to knowledge compounding. AI retrieval addresses this by making the entire vault searchable, but only if note structure supports embedding quality.  
Sources: AR-015 (internal), [S17] Weaviate, [S13] COG  
Confidence: 65%

---

## Architecture Claims

**C14** [I] The optimal Obsidian vault structure for AI retrieval is: atomic notes (one concept each) + consistent YAML frontmatter + dense internal links + flat or shallow folder hierarchy.  
Sources: Synthesized from [S7], [S8], [S14], [S17]  
Confidence: 55% — theoretically sound but zero empirical validation on real vaults.

**C15** [I] Folder hierarchy has minimal impact on AI retrieval quality (AI searches by embedding similarity, not folder path). Folders serve humans, not AI.  
Sources: Inferred from RAG architecture (none of the retrieval systems use folder structure)  
Confidence: 70%

**C16** [E] Knowledge graphs (GraphRAG) provide superior retrieval for complex, multi-hop queries compared to pure vector search.  
Sources: [S11] Springer BISE, [S16] PKM+RAG Medium  
Confidence: 75% — established in enterprise; applicability to small personal vaults is uncertain.

**C17** [J] The most valuable AI integration for PKM is not "chat with your notes" but automated synthesis: periodic consolidation of scattered notes into structured outputs.  
Sources: [S13] COG (/consolidate-knowledge), [S14] Zettelkasten.de  
Confidence: 55% — judgment based on practitioner reports. The "chat" use case is more common but potentially less valuable.

**C18** [I] Transactive Memory Systems theory predicts that human-AI knowledge teams work best when each party's knowledge domain is clearly understood. In PKM, this means: human knows *what* is in the vault; AI handles *retrieval* of specifics.  
Sources: [S10] Frontiers in Psychology  
Confidence: 60% — theoretical extrapolation from team-level TMS to individual PKM.

**C19** [A] The most common PKM failure pattern is: "initial excitement → capture → manual organization overwhelm → abandon." This pattern repeats across tools (Notion, Obsidian, custom apps).  
Sources: [S13] (5 abandoned attempts documented)  
Confidence: 75% — anecdotal but widely recognized in PKM communities.

**C20** [J] What actually compounds in PKM + AI is NOT the notes themselves but three things: (1) the human's ability to articulate questions, (2) the AI's contextual index quality (better embeddings from better notes), and (3) the feedback loop between retrieval results and note refinement.  
Sources: Synthesized from AR-015, [S14], [S9], [S17]  
Confidence: 50% — original thesis for this report. Testable but untested.
