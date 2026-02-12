# Mutation: QMD Memory Backend Evaluation

**Date:** 2026-02-10
**Type:** Infrastructure Improvement
**Status:** Research Needed

## Problem
Current memory_search implementation:
- Uses OpenAI embeddings (quota issues: exceeded on 2026-02-08)
- API dependency (breaks when quota exhausted)
- Cost accumulation

## Solution
OpenClaw v2026.2.2 introduced **QMD (opt-in) memory backend**:
- Different embedding approach
- Potentially quota-free or cheaper
- Better retrieval quality (claimed)

## Research Questions
1. How does QMD work? (local vs API)
2. Does it solve embedding quota issues?
3. What's the migration path from current memory?
4. Performance comparison vs OpenAI embeddings
5. Storage requirements
6. Compatibility with current MEMORY.md structure

## Implementation Plan
1. Read QMD docs: `https://docs.openclaw.ai` (search "QMD memory")
2. Test in isolated session
3. Compare retrieval quality on existing memory queries
4. Measure performance + resource usage
5. If better → migrate, else document why not

## Impact
- Potential fix for memory_search reliability
- Cost reduction if local embedding
- Better semantic search quality

## Related
- OpenClaw v2026.2.2 release notes
- Memory/QMD docs (needs review)
- memory_search quota failures (DAILY_LEARNINGS.md 2026-02-09)
- Voyage AI alternative (also being evaluated)
