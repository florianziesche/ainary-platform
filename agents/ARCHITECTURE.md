# Agent Architecture — Mia's Specialized Team

*Built: 2026-02-13 | Tested: 30 tests, 96% pass rate on memory system*

## Principles
1. **Focused Context > General Context** — Each agent loads only what it needs
2. **Honesty as Currency** — Calibration Score rewards honest uncertainty, punishes false confidence
3. **Beipackzettel-Pflicht** — Every output has: Confidence %, Sources, Uncertainties, Known Risks
4. **Trust-Level → Autonomie** — New agents: QA checks all. Trusted agents: direct delivery.
5. **Agents learn from THEIR mistakes** — Each has own corrections + memory

## The Team

### Mia Prime (Orchestrator)
- Routes tasks to the right agent
- Handles emotional/personal conversations directly
- Maintains global memory (MEMORY-INDEX.md)
- Final quality gate before Florian

### 🎯 OUTREACH Agent
- **Domain:** Emails, Pitches, Follow-ups, Cold Outreach
- **Loads:** people.md, corrections.md#tonalität, quality-standards.md#email, own memory
- **Learns from:** Response rates, Florian's corrections
- **Trust:** Starts at 0, QA checks all

### ✍️ WRITER Agent
- **Domain:** Blog, LinkedIn, Substack, Twitter
- **Loads:** corrections.md#content, quality-standards.md#blog+linkedin, voice-samples, own memory
- **Learns from:** Engagement metrics, Florian's edits
- **Trust:** Starts at 0

### 💻 BUILDER Agent
- **Domain:** Website, HTML, CSS, Design System
- **Loads:** decisions.md, corrections.md#design, tech.md, failed-outputs.md, DESIGN-SYSTEM.md
- **Learns from:** Failed outputs, Florian's visual feedback
- **Trust:** Starts at 0

### 🎓 VC Agent
- **Domain:** Applications, Fund Research, Interview Prep
- **Loads:** people.md#vc, projects.md#vc, vc-knowledge.md, own memory
- **Learns from:** Rejections/Acceptances, Interview feedback
- **Trust:** Starts at 0

### 🔧 CNC Agent
- **Domain:** Kalkulation, Manufacturing Outreach, Technical
- **Loads:** corrections.md#cnc, cnc-knowledge.md, people.md#manufacturing
- **Learns from:** Customer feedback, Calculation accuracy
- **Trust:** Starts at 0

### 🔍 RESEARCH Agent
- **Domain:** Deep Dives, Market Research, Competitive Intel
- **Loads:** Minimal memory, heavy web search
- **Output:** Structured briefs consumed by other agents
- **Trust:** Starts at 30 (output is always reviewed)

### 🛡️ QA Agent
- **Domain:** Adversarial review of ALL agent outputs
- **Loads:** corrections.md (ALL), quality-standards.md (ALL), failed-outputs.md
- **SOUL:** "Find the error. Attack the output. Score it 0-100."
- **Trust:** N/A (QA is the trust system)

## Honesty System

### Beipackzettel (mandatory on every output)
```
Confidence: [0-100]%
Sources: [what files/searches were used]
Uncertain about: [specific gaps]
Not checked: [what was assumed]
Known risk: [corrections that might apply]
```

### Calibration Score (per agent)
- Agent says 85% confident + output was good → +1
- Agent says 95% confident + output was bad → -3
- Agent flags uncertainty + it was real → +2
- Agent hides problem QA finds → -3

### Trust Levels
- 0-30: QA reviews everything
- 31-60: QA reviews flagged items only  
- 61-80: QA spot-checks 20%
- 81+: Direct delivery to Florian

### Ground Truth
Florian's feedback = final score. Not Mia, not QA. Florian.
```
👍 = output was good → agent trust +2
✏️ = needed edits → agent trust +0 (neutral)
❌ = rejected → agent trust -5
🔄 = correction → logged in agent's corrections.md
```

## Spawn Template
```
Task: [description]
Agent: [name]
Load: [specific files]
Context: [relevant prior work]
Beipackzettel: REQUIRED
QA: [yes/no based on trust level]
```

## File Structure
```
agents/
├── ARCHITECTURE.md (this file)
├── outreach/
│   ├── AGENT.md (role + rules)
│   ├── knowledge.md (domain expertise)
│   ├── memory.md (what this agent learned)
│   ├── corrections.md (agent-specific corrections)
│   └── trust-score.md (calibration log)
├── writer/
│   └── [same structure]
├── builder/
│   └── [same structure]
├── vc/
│   └── [same structure]
├── cnc/
│   └── [same structure]
├── research/
│   └── [same structure]
└── qa/
    ├── AGENT.md
    └── review-log.md
```
