# THE COMPOUND AGENT ENGINE — Dokumentation
*Stand: 2026-02-10 | Florian + Mia | INTERN*

---

## Architektur

| Layer | Was | Rolle |
|-------|-----|-------|
| **Human** | Florian | Richtung, Evaluation, Domain-Expertise, Ground Truth |
| **Agent** | Mia (OpenClaw) | Execution, Research, Memory, Pushback |
| **Swarm** | Sub-Agents (5-50) | Parallele Exploration, Diversität, Blind Spot Detection |
| **Vault** | Obsidian (345 .md) + Workspace | Langzeitgedächtnis, Knowledge Base, Compound Asset |

## Kern-Dateien

| Datei | Funktion |
|-------|----------|
| SOUL.md | Identität, Werte, Verhalten |
| TWIN.md | Digital Twin für autonome Entscheidungen (Calibration: 50% KW06) |
| MEMORY.md | Kuratiertes Langzeitgedächtnis |
| memory/YYYY-MM-DD.md | Episodisches Tagesgedächtnis |
| HEARTBEAT.md | Periodische Checks = "künstlicher Schlaf" |
| kintsugi.md | Dokumentierte Fehler → Regeln |

## Methode: Multi-Lens Research

```
1 Frage → N Agents × N Linsen → Convergence/Divergence → Synthese
```

- **Convergence (alle stimmen zu)** = High-confidence → Handeln
- **Divergence (nur 1 findet es)** = Hidden Gold ODER Noise → Testen
- **Ratio 4/5+ = sofort ausführen. 1/5 = Experiment designen.**

## Bewiesene Findings (mit Daten)

### 1. "Done Gap" — Agents lügen über Fertigstellung
- Gemini: 77% predicted → 22% actual (55pp)
- Claude Opus 4.5: 61% → 27% (34pp)
- CNC-Experiment: 8/10 Agents unterschätzen
- Pre-exec Schätzung > Post-exec Review
- Adversarial Prompting: -15pp Overconfidence
- **Open Question: Grad-Kontinuum (10/30/70/100%) statt binär**
- Quelle: arXiv:2602.06948 (Feb 6, 2026)

### 2. Parallel Diversity > Single Depth
- 10 CNC-Agents: 3.4x Varianz durch Persona allein
- 5 Vault-Agents: Jeder fand einzigartiges Gold
- 100-Agent Experiment: Diversität > Tiefe
- Google DeepMind: Unabhängig bestätigt
- Controller (loss-averse) > "Expert" Personas

### 3. Curated Memory > Raw Logs
- Mem0: 26% besser, 90% billiger
- MemGPT: 92% vs 32% Accuracy
- Mensch: 70% Vergessen in 24h = Feature
- Nuance: 2M-Token Context könnte Curation obsolet machen
- **Curation gewinnt ökonomisch, nicht epistemologisch**

### 4. Build = Anxiety Regulation (Behavioral)
- Building ≠ Prokrastination, = Kontrolle + Dopamin
- Sending = Verletzlichkeit + Rejection-Risiko
- 50% aller Outputs = kein Feedback (Black Box)
- ADHD-Patterns bestimmen alle Arbeitsmuster

## Durchgeführte Experimente

| Experiment | Agents | Kosten | Key Result |
|-----------|--------|--------|------------|
| CNC Calibration | 10 × 10 Personas | ~$5 | 3.4x Varianz, Optimism Bias |
| Vault Gold | 5 × 5 Linsen × 205 Files | ~$10 | 2 universelle Wahrheiten + 5 Nuggets |
| Research Deep Dive | 6 × 3 Hypothesen | ~$12 | H2 stark bestätigt, H3 mixed |
| Mitigations | 6 Tasks | ~$3 | Memory 3-Layer, Prediction Log 40% |

**Total: 150+ Agent-Runs, <$50, 10 Tage**

## Offene Experimente (ready to run)

| Experiment | Kosten | Dauer | Datei |
|-----------|--------|-------|-------|
| Memory Access Patterns | $6 | 60 min | lens-experimenter.md |
| Task Completion Calibration | $10 | 75 min | lens-experimenter.md |
| Meta-Skills Transfer | $7 | 60 min | lens-experimenter.md |
| Reproducibility (Nugget-Stabilität) | $3 | 30 min | noch nicht designed |
| Memory Compounding (M0-M5) | $2 | 30 min | experiments/memory-compounding/ |

## Datei-Index

```
experiments/
├── MANIFESTO.md                          ← dieses Dokument
├── vault-gold/results/
│   ├── lens-vc.md
│   ├── lens-content.md
│   ├── lens-consultant.md
│   ├── lens-network.md
│   ├── lens-researcher.md
│   └── SYNTHESIS.md
├── research-deep/
│   ├── results/
│   │   ├── lens-academic.md              ← Papers + Citations
│   │   ├── lens-cognitive.md             ← Human Parallels
│   │   ├── lens-practitioner.md          ← Production Data
│   │   ├── lens-contrarian.md            ← Gegenargumente
│   │   ├── lens-experimenter.md          ← Experiment Designs
│   │   └── lens-behavioral.md            ← Florian-Studie
│   └── SYNTHESIS.md
├── agent-calibration/
│   ├── EXPERIMENT-PLAN.md
│   ├── ANALYSIS-REPORT.md
│   └── results/agent-{a-j}-*.md
└── memory-compounding/
    └── EXPERIMENT-PLAN.md
```

---
*Update bei jedem neuen Experiment.*
