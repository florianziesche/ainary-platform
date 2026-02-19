# Ainary Research Pipeline

**Automated research report generation using Claude Opus + hierarchical RAG.**

Produces A+++ grade research reports with:
- Tiered knowledge retrieval (CORE 2x → KNOWLEDGE 1.5x → EPHEMERAL 0.5x)
- Per-paragraph evidence classification (E/I/J/A badges)
- Beipackzettel (Information Safety Label) per report
- 13 deterministic validation checks
- Self-calibrating confidence scores

## Quick Start

```bash
# Create run directory
OUTDIR=~/.openclaw/workspace/research/mia-pipeline/my-topic-$(date +%Y%m%d-%H%M)
mkdir -p "$OUTDIR"

# Write research brief (see SETUP.md for full schema)
cat > "$OUTDIR/research-brief.json" << 'EOF'
{
  "topic": "Your Topic Here",
  "decision": "What should the reader decide?",
  "audience": "Who reads this?",
  "audience_tag": "PUBLIC",
  "sub_questions": ["Question 1?", "Question 2?", "Question 3?"]
}
EOF
echo '{"claims": []}' > "$OUTDIR/all-claims.json"
echo '{"contradictions": []}' > "$OUTDIR/contradictions.json"

# Run pipeline (~60-90 min with OAuth, ~5 min with API key)
python3 mia_synthesis_v3.py "$OUTDIR" --version v1
```

## Documentation

- **[SETUP.md](SETUP.md)** — Complete setup guide (zero to first report)
- **[ARCHITECTURE.md](ARCHITECTURE.md)** — Pipeline architecture, data flow, design decisions

## Architecture

```
research-brief.json
       ↓
Phase A: Outline (Opus) → JSON structure with 7 sections
Phase B: Sections (Opus × 7) → Each section with RAG context + validation
Phase C: Merge (Python) → Single document + Beipackzettel
Phase D: Validate (Python) → 13 checks (E/I/J/A ratio, grounding, consistency)
Phase E: Grade (Python) → A+++/A++/A+/B/C
       ↓
final-report.md + beipackzettel.json + validation-report.json
```

## Knowledge Tiers

| Tier | Boost | Example |
|---|---|---|
| **CORE** | 2.0x | Verified claims (CRTs), self-corrections, curated findings |
| **KNOWLEDGE** | 1.5x | Peer-reviewed papers, audited research |
| **OPERATIONAL** | 1.0x | Project status, people, decisions |
| **EPHEMERAL** | 0.5x | Daily notes, session logs |

## Reports Produced

| ID | Topic | Grade | Words | Date |
|---|---|---|---|---|
| MIA-001 | Trust Calibration for AI Agents | A+++ | 7,339 | 2026-02-19 |
| MIA-002 | Hierarchical Knowledge: OpenClaw + Obsidian | — | — | 2026-02-19 |

## Requirements

- Python 3.10+
- OpenClaw (for OAuth) or Anthropic API key
- No external Python dependencies (stdlib only)
- Optional: `agenttrust` library (`pip install -e .`)

## License

Private. Ainary Ventures.
