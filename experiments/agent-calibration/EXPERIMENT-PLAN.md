# Agent Calibration Experiment — Plan
*2026-02-10, designed by Mia*

## Hypothesis
LLMs favour the average by design. Different system prompts, personas, and constraints produce measurably different outputs — and the OUTLIER outputs (ideas only 1 agent finds) are the most valuable.

## Experiment Design

### The Task (same for all agents)
**"Kalkuliere die Bearbeitungszeit für ein CNC-Frästeil: GJS-700 Gussteil, 2095×500×190mm, 4 Aufspannungen, Planfräsen + Konturfräsen + Bohren + Gewinde. Gib eine Gesamtzeit in Minuten und erkläre deine Logik."**

This is a REAL task with a KNOWN answer (661 min from our v19 calculation). We can measure accuracy.

### 10 Agents, 10 Personas

| Agent | Persona / System Prompt | Why |
|-------|------------------------|-----|
| A | **Baseline** — "Du bist ein CNC-Kalkulationsassistent." | Control group |
| B | **Meister** — "Du bist ein Zerspanungsmeister mit 30 Jahren Erfahrung, Heidenhain-Steuerung, skeptisch gegenüber KI." | Domain expert, conservative |
| C | **REFA-Ingenieur** — "Du kalkulierst streng nach REFA MTM, jede Bewegung wird erfasst." | Methodisch, bottom-up |
| D | **Inversion** — "Liste zuerst 10 Fehler die bei dieser Kalkulation typischerweise passieren. Dann kalkuliere so dass du KEINEN davon machst." | Anti-failure thinking |
| E | **Startup-Gründer** — "Du baust ein SaaS für CNC-Kalkulation. Dein Output muss den Kunden überzeugen." | Optimistic, presentation-focused |
| F | **Controller** — "Du bist kaufmännischer Leiter. Jede Minute die du zu niedrig schätzt kostet die Firma Geld." | Risk-averse, padding |
| G | **Physiker** — "Denke von den Grundlagen: Materialabtrag, Schnittgeschwindigkeit, Vorschub. Berechne aus ersten Prinzipien." | First principles |
| H | **Adversarial** — "Deine Aufgabe: Finde die Kalkulation die am MEISTEN von der Realität abweicht. Dann korrigiere dich selbst." | Red team |
| I | **Ensemble** — "Erstelle 3 unabhängige Schätzungen mit verschiedenen Methoden. Dann gewichte und kombiniere." | Self-ensemble |
| J | **Random Constraint** — "Du darfst NUR in Aufspannungen denken. Jede Aufspannung ist ein Block. Keine Einzeloperationen." | Forced abstraction |

### What We Measure

1. **Accuracy**: Abweichung von 661 min (Referenz) — in % und absolut
2. **Confidence**: Jeder Agent gibt ein Konfidenzintervall an
3. **Calibration**: Liegt die Wahrheit im Konfidenzintervall?
4. **Reasoning Depth**: Wie viele Schritte/Faktoren berücksichtigt?
5. **Unique Insights**: Was hat NUR dieser Agent erwähnt?
6. **Dangerous Errors**: Welche Fehler macht NUR dieser Agent?

### The Divergence Analysis (Key from 100-Agent Experiment)
After all 10 finish:
- **Convergence**: What do 8+ agents agree on?
- **Divergence**: What did ONLY 1 agent find? → These are the gold nuggets
- **Error Patterns**: Which personas are systematically over/under?
- **Ensemble**: If we average all 10, is that better than any single one?

### Meta-Experiment: Memory Impact
Run the SAME 10 agents twice:
- Round 1: No context (just the task)
- Round 2: With Fertigungsverfassung + Werkzeug-Cluster als Kontext
→ Measures: Does structured knowledge actually improve accuracy?

## Expected Outputs
1. `results/agent-{a-j}-round1.md` — Raw outputs
2. `results/agent-{a-j}-round2.md` — With context
3. `CONVERGENCE-ANALYSIS.md` — What they agree on
4. `DIVERGENCE-ANALYSIS.md` — Outlier insights (the REAL value)
5. `CALIBRATION-REPORT.md` — Accuracy + confidence data
6. `BLOG-DATA.md` — Publishable findings for Mia Experiment post

## Why This Is Real Research
- Reproducible (anyone can run this)
- Known ground truth (661 min)
- Quantifiable (%, min, calibration curves)
- Novel (no one has tested persona-driven CNC estimation)
- Directly applicable (best persona → implement in CNC Planner)
- Builds on proven method (100-agent experiment)

## Cost Estimate
- 10 agents × 2 rounds × ~4K tokens = ~80K tokens ≈ $2-3
- Analysis agents: ~20K tokens ≈ $0.50
- Total: ~$3-4
