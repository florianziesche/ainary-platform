# Context Packs — Compressed Briefings for Sub-Agents

## What Are Context Packs?

Context Packs are compressed, structured summaries of our full research corpus. Instead of loading all 18 source files (~200K tokens), a sub-agent loads 1-2 packs (~12-15K tokens total) and has everything needed to work.

**Goal:** <15K tokens input per agent instead of ~50-200K.

---

## Available Packs

| Pack | File | Size | Contains | Load When |
|---|---|---|---|---|
| **Research Pack** | `research-pack.md` | ~12K tokens | All 15 briefs + 2 syntheses + gap research compressed. Per-brief summaries, cross-references, strongest/weakest claims, known gaps. | Writing report sections, QA checks, any task needing research data |
| **Pipeline Pack** | `pipeline-pack.md` | ~4K tokens | Agent roles, pipeline phases, quality standards, voice rules, design rules, known mistakes, report structure. | Any task: writing, building, QA, orchestration |

### Loading Rules

| Task Type | Load |
|---|---|
| **WRITE** (report section) | research-pack.md + pipeline-pack.md |
| **QA** (verify claims/voice) | research-pack.md + pipeline-pack.md |
| **BUILD** (website/tools) | pipeline-pack.md only |
| **RESEARCH** (new brief) | pipeline-pack.md only (don't bias with existing research) |
| **SYNTHESIS** (cross-reference) | research-pack.md + pipeline-pack.md |

---

## Update Process

### After Each New Brief
1. Read the new brief
2. Add 3-5 line summary to research-pack.md (same format as existing entries)
3. Update Cross-References if new brief reinforces/contradicts existing ones
4. Update Known Gaps (remove if filled, add if new gaps discovered)
5. Update Strongest/Weakest Claims if new brief changes rankings

### After Each Synthesis
1. Update Synthesis Highlights section
2. Update Predictions if changed
3. Update Cross-References

### After Corrections
1. Update pipeline-pack.md Known Mistakes section
2. Update Voice/Design Rules if applicable

---

## Quality Guarantees

- **No information loss**: Every number retains its source
- **Confidence levels preserved**: High/Medium/Low carried through
- **Cross-references explicit**: What reinforces/contradicts what
- **Gaps documented**: What we don't know is as important as what we do
- **Weakest claims flagged**: Prevents building on shaky foundations

---

## Measurable Goals

| Metric | Before | After | Target |
|---|---|---|---|
| Tokens per agent input | 50-200K | ~12-15K | <15K ✅ |
| Source traceability | Full (in files) | Preserved (brief name + source) | No loss ✅ |
| Agent cold-start time | Minutes (reading all files) | Seconds (1-2 packs) | <30s ✅ |
| Confidence preservation | Full | Full (H/M/L per claim) | No loss ✅ |

---

*Created: 2026-02-14 | Maintainer: BUILDER agent or KING*
