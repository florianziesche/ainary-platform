# Prompt Registry — Research Pipeline v2

*Single source of truth for which spawn templates exist, their version, and approval status.*

---

## Registry

| Prompt ID | Name | Phase | Current Version | Status | Canonical Location | Last Eval | Known Limitations |
|-----------|------|-------|----------------|--------|-------------------|-----------|-------------------|
| SP-RES | Research Agent | 2 | v1.0 | Active | `agents/spawn-templates/RESEARCH-AGENT.md` | 2026-02-15 | Depends on web_search quality; internal sources need manual flagging |
| SP-EXP | Experiment Agent | 3 | v1.0 | Active | `agents/spawn-templates/EXPERIMENT-AGENT.md` | 2026-02-15 | Simulations labeled honestly but still self-generated data |
| SP-VAL | Validation Agent | 4 | v1.0 | Active | `agents/spawn-templates/VALIDATION-AGENT.md` | 2026-02-15 | Same model biases as Writer; cross-validation is partial |
| SP-WRT | Writer Agent | 5 | v1.0 | Active | `agents/spawn-templates/WRITER-AGENT.md` | 2026-02-15 | E/I/J/A labeling untested; may still default to 62-82% confidence |
| SP-QA | QA Agent | 6 | v1.0 | Active | `agents/spawn-templates/QA-AGENT.md` | 2026-02-15 | Same model can't catch own blindspots; math verification strongest |
| SP-FIX | Fix Agent | 7 | v1.0 | Active | `agents/spawn-templates/FIX-AGENT.md` | 2026-02-15 | "No new claims" rule untested at scale |
| SP-THE | Thesis Development Agent | 2.5 | v1.0 | Active | `agents/spawn-templates/THESIS-AGENT.md` | 2026-02-15 | New — untested. Quality depends on Research Agent gap map quality |
| SP-AST | Asset Builder Agent | 9 | v1.0 | Active | `agents/spawn-templates/ASSET-AGENT.md` | 2026-02-15 | RAG JSON schema untested; no downstream consumer yet |

## Rules

1. Only **Active** templates may be used for spawning agents
2. **Tier 2+ reports** require: Research + Thesis + Writer + QA + Fix (minimum 5 agents)
3. **Tier 3 reports** require: All 8 agents in sequence
4. Changes to any template:
   - Update version (v1.0 → v1.1 for minor, v2.0 for major)
   - Entry in `CHANGELOG.md`
   - Re-run at least 1 regression test from EVAL-PACK
5. **Deprecation:** Mark status = Deprecated, link replacement, record reason in CHANGELOG

## Model Assignment

| Agent | Default Model | Override Allowed? |
|-------|--------------|-------------------|
| Research | Opus | Yes (Sonnet for Tier 1) |
| Thesis | Opus | No — quality-critical, creative thinking |
| Experiment | Opus | Yes |
| Validation | Opus + Search | No — needs search |
| Writer | Opus | Yes (Sonnet for Tier 1) |
| QA | Opus | No — quality-critical |
| Fix | Sonnet | Yes (Opus for Tier 3) |
| Asset Builder | Sonnet | Yes |

---

*Created: 2026-02-15 | Owner: Mia (maintained by Main session)*
