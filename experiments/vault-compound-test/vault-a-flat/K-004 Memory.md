---
tags: [concept, memory, security]
---
# K-004: Memory Architecture

AI agent memory is a critical attack surface. No production memory framework (Letta, Mem0, Zep, LangMem, A-Mem) implements provenance tracking, integrity checks, or confidence scoring.

Memory injection (MINJA) achieves >95% success rates, creating persistent backdoors. Memory poisoning + no detection + propagation + human failure = self-reinforcing attack loop.

Memory = persistent backdoor when compromised. Key gap: no provenance tracking for memory entries.

**Appears in:** AR-001, AR-006
