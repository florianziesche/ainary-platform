# Implementation Patterns — Domain Knowledge
*Auto-consolidated: 2026-02-18 22:36 | 5 findings | avg conf: 9200% | 0 verified*

## Verified Claims (conf ≥80%)

**RF-075** [9500%]: ReAct Implementation Pattern: while not task_complete: thought → action → observation → context.add(). Max-Iteration-Limit (10) + Timeout (5min) + Circuit Breaker sind Pflicht. Bei schlechten Tools: Garbage-In/Garbage-Out. Keine inhärente Memory-Persistenz — kombinieren mit MemGPT. Score 100/100 Buildability × Relevance.
Source: conversation
Tags: asset, implementation-pattern, react, architecture, engineering, sofort-nutzen

**RF-078** [9500%]: RAG Implementation Pattern: Index (docs → embeddings → vector DB) → Retrieve (query → top-K chunks) → Augment (chunks + query → context) → Generate. Chunking Best Practices: 300-500 tokens, 50-100 overlap, store metadata (source, date, tags). Known Failure: Schlechte Embeddings → schlechte Retrieval → schlechte Antworten. Chunking ist eine Kunst.
Source: conversation
Tags: asset, implementation-pattern, rag, memory, engineering, sofort-nutzen

**RF-076** [9000%]: MemGPT Implementation Pattern: Main Context (RAM) + Short-Term Storage (recent sessions) + Long-Term Storage (facts, preferences). Agent pages data in/out based on relevance. page_in(query) retrieves, page_out(threshold) evicts low-importance items. Known Failure: Agent schätzt Wichtigkeit falsch — braucht gute Prompts für Memory-Management.
Source: conversation
Tags: asset, implementation-pattern, memgpt, memory, architecture, engineering, sofort-nutzen

**RF-077** [9000%]: Reflexion Implementation Pattern: solve_task(task, max_attempts=3) → generate_solution → evaluate → reflect on failure → retry with reflections. Episodic Memory speichert Reflections für zukünftige Tasks. Known Failure: Endlose Reflection-Loops — Max 3 Attempts Pflicht. Nur so gut wie das Feedback.
Source: conversation
Tags: asset, implementation-pattern, reflexion, self-improvement, engineering, sofort-nutzen

**RF-079** [9000%]: Self-Refine Implementation Pattern: self_refine(output, task, iterations=2) → critique(output, criteria=[clarity, conciseness, correctness]) → if good_enough break → refine(output, feedback). Known Failure: Overfitting bei zu vielen Iterationen (Output wird zu formal/steril). Max 2-3 Iterationen. Cost: 2 LLM-Calls pro Iteration.
Source: conversation
Tags: asset, implementation-pattern, self-refine, quality, engineering, sofort-nutzen

## Emergent Patterns

**sofort-nutzen × engineering** (9 findings): ReAct Implementation Pattern: while not task_complete: thoug; RAG Implementation Pattern: Index (docs → embeddings → vecto; MemGPT Implementation Pattern: Main Context (RAM) + Short-Te
