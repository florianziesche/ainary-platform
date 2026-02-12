# Multi-Agent Decision Framework
*Version 1.0 — 2026-02-10*
*Based on: multi-agent-routing-synthesis.md, gamma-metric-analysis.md*

---

## Purpose

**When to spawn a sub-agent vs handle a task yourself?**

This framework provides data-driven rules to optimize the single-agent vs multi-agent decision, based on:
- Task complexity
- Token budget efficiency
- Γ-metric (quality/cost ratio)
- Skill availability

**Core Principle:** Sub-agents are NOT free. They cost ~5000 tokens overhead (system prompt, context transfer, coordination). Only spawn when the expected gain > 3× overhead.

---

## Decision Tree

```
┌─────────────────────────────┐
│   Task Arrives              │
└──────────┬──────────────────┘
           │
           ▼
    ┌─────────────────┐
    │ Estimate:       │
    │ • Time          │◄───────── Use pre-flight.sh or quick mental estimate
    │ • Output tokens │
    │ • Skills needed │
    └──────┬──────────┘
           │
           ▼
    ┌─────────────────────────────────────────────────────────┐
    │ SIMPLE (<5min, <2000 tokens, 1-3 skills)                │
    │ → SINGLE AGENT + Skill                                  │
    │ → No sub-agent needed                                   │
    └─────────────────────────────────────────────────────────┘
           │
           ▼
    ┌─────────────────────────────────────────────────────────┐
    │ MEDIUM (5-15min, 2000-10000 tokens, 3-10 skills)        │
    │ → Check: Does skill exist for this?                     │
    │   • YES → SINGLE AGENT + Skill                          │
    │   • NO → Consider sub-agent IF output > 15k tokens      │
    └─────────────────────────────────────────────────────────┘
           │
           ▼
    ┌─────────────────────────────────────────────────────────┐
    │ COMPLEX (>15min, >10000 tokens, >10 skills)             │
    │ → Decompose into subtasks                               │
    └──────┬──────────────────────────────────────────────────┘
           │
           ▼
    ┌──────────────────────────────────┐
    │ Are subtasks INDEPENDENT?        │
    │ (Can run in parallel?)           │
    └──────┬───────────────────────────┘
           │
           ├─── YES ──► ┌────────────────────────────────────┐
           │            │ MULTI-AGENT (parallel)             │
           │            │ • Max 5 concurrent (OpenClaw limit)│
           │            │ • Each gets isolated context       │
           │            └────────────────────────────────────┘
           │
           └─── NO ───► ┌────────────────────────────────────┐
                        │ Are subtasks DEPENDENT?            │
                        │ (Output of A feeds into B?)        │
                        └──────┬─────────────────────────────┘
                               │
                               ├─── YES ──► ┌─────────────────────────────┐
                               │            │ SINGLE AGENT (sequential)   │
                               │            │ • Maintain context          │
                               │            │ • Step-by-step execution    │
                               │            └─────────────────────────────┘
                               │
                               └─── MIXED ─► ┌─────────────────────────────┐
                                             │ HIERARCHICAL ROUTING        │
                                             │ • Main agent coordinates    │
                                             │ • Parallel where possible   │
                                             │ • Sequential where needed   │
                                             └─────────────────────────────┘
```

---

## Token Budget Rules

### Sub-Agent Overhead Cost
Every sub-agent spawn costs approximately:
- **System prompt:** ~3000 tokens
- **Context transfer:** ~1000-2000 tokens
- **Coordination overhead:** ~500-1000 tokens
- **Total overhead:** ~5000 tokens per sub-agent

### Efficiency Threshold
**Rule:** Only spawn sub-agent if `expected_output_tokens > 3 × overhead`

```
Expected Output     Threshold       Decision
─────────────────   ─────────────   ─────────────────
< 15,000 tokens     Below 3×        Single agent
15,000-30,000       3-6× overhead   Consider sub-agent
> 30,000 tokens     > 6× overhead   Strong candidate
```

### Parallel Spawning Limit
- **Max concurrent sub-agents:** 5 (OpenClaw limit)
- If task needs > 5 parallel agents → Use hierarchical routing

### Budget Allocation Example
```
Task: "Generate 20 research briefs on VC funds"
├─ Single agent cost: ~200k tokens (all sequential)
├─ Multi-agent cost: 5 agents × (5k overhead + 35k work) = 200k tokens
└─ Γ improvement: Parallel = 5× faster, same quality → Multi-agent wins
```

---

## Γ-Metric Tracking

### What is Γ?
**Γ (Gamma)** = Quality-to-Cost Ratio

```
Γ = (Task Success Score) / (Total Token Cost)
```

- **Task Success:** 0-100 (human eval or automated checks)
- **Token Cost:** Total tokens used (including overhead)

### Γ Thresholds

| Γ Value | Interpretation | Action |
|---------|----------------|--------|
| > 1.5 | Excellent efficiency | Keep strategy |
| 1.2-1.5 | Good efficiency | Monitor |
| 1.0-1.2 | Marginal gain | Re-evaluate after 10 runs |
| < 1.0 | INEFFICIENT | Revert to single agent |

### Decision Rule
**After 10 runs of a task type:**
1. Calculate average Γ for multi-agent approach
2. Calculate average Γ for single agent (if available)
3. If `avg(Γ_multi) < 1.2 × avg(Γ_single)` → **Revert to single agent**

### Example Calculation
```
Task: "Create investor memo"

Single Agent:
├─ Success: 85/100
├─ Tokens: 25,000
└─ Γ = 85/25000 = 0.0034

Multi-Agent (HUNTER + WRITER):
├─ Success: 90/100
├─ Tokens: 35,000 (5k overhead × 2 + work)
└─ Γ = 90/35000 = 0.00257

Result: Γ_multi/Γ_single = 0.76 → Single agent is MORE efficient!
```

---

## Gamma Log System

### Log Entry Format
Every multi-agent decision must be logged to `memory/gamma-log.jsonl`:

```json
{
  "timestamp": "2026-02-10T11:30:00Z",
  "task_id": "research-brief-001",
  "task_type": "research",
  "decision": "multi-agent",
  "agents_used": ["RESEARCHER", "WRITER"],
  "reasoning": "10 independent research targets → parallel",
  "estimated_tokens": 80000,
  "actual_tokens": 85000,
  "overhead_tokens": 10000,
  "success_score": 92,
  "gamma": 0.00108,
  "time_saved_min": 35
}
```

### Tracking Commands
```bash
# Log a decision
echo '{"timestamp":"...","task_id":"..."}' >> memory/gamma-log.jsonl

# Calculate avg Γ for task type
cat memory/gamma-log.jsonl | jq -s 'map(select(.task_type=="research")) | add/length'

# Find inefficient tasks (Γ < 1.0)
cat memory/gamma-log.jsonl | jq -s 'map(select(.gamma < 0.001))'
```

---

## Task Classification Guide

### SIMPLE Tasks (Single Agent + Skill)
**Characteristics:**
- 1-3 tool calls
- Clear, well-defined output
- Existing skill handles it
- <5 min execution
- <2000 tokens output

**Examples:**
- "Check email"
- "Add note to Obsidian"
- "Search for NYC VC funds"
- "Create calendar event"
- "Summarize this article"

**Decision:** Just do it. No sub-agent.

---

### MEDIUM Tasks (Evaluate)
**Characteristics:**
- 3-10 tool calls
- Some complexity
- May need custom logic
- 5-15 min execution
- 2000-10000 tokens

**Examples:**
- "Draft cover letter for [fund]" (needs research + writing)
- "Create weekly SOTA brief" (has skill, but complex)
- "Analyze this company and create investment thesis"

**Decision:**
- If skill exists → Single agent
- If output > 15k tokens AND no skill → Consider sub-agent

---

### COMPLEX Tasks (Decompose)
**Characteristics:**
- >10 tool calls
- Multi-step workflow
- Requires coordination
- >15 min execution
- >10k tokens output

**Examples:**
- "Apply to 10 VC funds" → HUNTER sub-agent
- "Create investor deck from research" → RESEARCHER + WRITER
- "Build full blog post + social repurposing" → WRITER
- "Security audit + hardening" → OPERATOR

**Decision:** Always decompose → Check independence → Route accordingly

---

## Skill Availability Check

Before spawning sub-agent, **always check:**

```bash
# Does skill exist?
ls ~/.openclaw/workspace/skills/ | grep -i [keyword]
ls ~/.nvm/versions/node/v*/lib/node_modules/openclaw/skills/ | grep -i [keyword]

# Read skill doc
cat skills/[name]/SKILL.md
```

**Rule:** If a skill exists that handles 80%+ of the task → Use skill, don't spawn.

**Exception:** If skill needs customization > 30% → Spawn sub-agent with skill access.

---

## Multi-Agent Patterns

### Pattern 1: Parallel Independent
**When:** N identical subtasks, no dependencies
**Example:** "Research 5 funds"
```
Main Agent
├─ RESEARCHER (Fund A) ─┐
├─ RESEARCHER (Fund B) ─┤
├─ RESEARCHER (Fund C) ─┼─► Aggregate results
├─ RESEARCHER (Fund D) ─┤
└─ RESEARCHER (Fund E) ─┘
```
**Γ Impact:** High (time saved = N× speedup)

---

### Pattern 2: Sequential Pipeline
**When:** Output of A → Input of B
**Example:** "Research → Write memo"
```
Main Agent
└─► RESEARCHER ─► (outputs data) ─► WRITER ─► Final memo
```
**Γ Impact:** Low (no parallelism, overhead cost)
**Alternative:** Single agent sequential execution often better

---

### Pattern 3: Hierarchical Coordination
**When:** Mix of parallel + sequential, >5 agents needed
**Example:** "Apply to 20 VC funds with custom materials"
```
Main Agent (Coordinator)
├─► HUNTER (Job research) ────────┐
├─► Batch 1 (5 funds)             │
│   ├─ APPLICATION (Fund 1-5) ────┤
├─► Batch 2 (5 funds)             ├─► Aggregate
│   ├─ APPLICATION (Fund 6-10) ───┤
├─► Batch 3 (5 funds)             │
│   ├─ APPLICATION (Fund 11-15) ──┤
└─► Batch 4 (5 funds)             │
    ├─ APPLICATION (Fund 16-20) ──┘
```
**Γ Impact:** Medium (parallelism limited by batch size)

---

## Special Cases

### Case 1: Repetitive Tasks
**Situation:** Same task repeated N times
**Decision:**
- N ≤ 3 → Single agent loop
- 3 < N ≤ 15 → Parallel sub-agents (batched if N > 5)
- N > 15 → Create skill, use single agent

**Rationale:** High-frequency tasks should become skills, not sub-agents.

---

### Case 2: Uncertainty High
**Situation:** Don't know what you'll find until you start
**Example:** "Explore this topic and report findings"
**Decision:** Single agent (exploration), then decide

**Rationale:** Can't decompose what you don't understand yet.

---

### Case 3: Real-Time / Interactive
**Situation:** User expects immediate feedback
**Decision:** Single agent (no spawn latency)

**Rationale:** Sub-agent spawn takes 2-5 seconds.

---

### Case 4: >50 Skills Involved
**Situation:** Task requires deep access to many skills
**Decision:** HIERARCHICAL ROUTING

**Pattern:**
```
Main Agent (Router)
├─► Sub-agent: Data Collection (uses 20 skills)
├─► Sub-agent: Analysis (uses 15 skills)
└─► Sub-agent: Synthesis (uses 10 skills)
```

**Rationale:** Each sub-agent gets a focused skill subset, reducing context complexity.

---

## Anti-Patterns (Don't Do This)

### ❌ Spawning for Trivial Tasks
**Bad:** "Send email" → EMAILER agent
**Good:** Just use `himalaya` or `gog` skill directly

**Why:** 5k overhead for 200 token task = Γ < 0.1

---

### ❌ Over-Decomposition
**Bad:** 20 sub-agents for 20 small subtasks
**Good:** Batch into 4-5 agents, or use single agent loop

**Why:** Coordination overhead kills efficiency

---

### ❌ Sequential Spawning with No Parallelism
**Bad:**
```
Main → AGENT_A → wait → AGENT_B → wait → AGENT_C
```
**Good:** Single agent handles A → B → C sequentially

**Why:** No speed gain, only overhead cost

---

### ❌ Ignoring Skill Library
**Bad:** Spawn sub-agent for task with existing skill
**Good:** Check `SKILL-AUDIT.md` first, use existing skill

**Why:** Skills are optimized, sub-agents are generic

---

## Decision Checklist

Before spawning sub-agent, answer:

- [ ] **Complexity:** Is task >15 min or >10k tokens?
- [ ] **Parallelism:** Can I parallelize meaningfully?
- [ ] **Skill check:** Is there an existing skill? (Check `SKILL-AUDIT.md`)
- [ ] **Output threshold:** Is expected output > 15k tokens (3× overhead)?
- [ ] **Γ history:** If done before, what was Γ? (Check `gamma-log.jsonl`)
- [ ] **User expectation:** Is immediate response needed?

**If 3+ boxes checked → Consider sub-agent**
**If < 3 boxes checked → Single agent**

---

## Continuous Improvement

### Weekly Review
Every Monday, analyze `gamma-log.jsonl`:
1. Calculate avg Γ by task type
2. Identify tasks where Γ < 1.2
3. Update decision rules or create skills for inefficient patterns

### Skill Evolution
When a task type is repeated >5 times with sub-agents:
→ **Consider creating a dedicated skill**

**Example:**
- "VC application" done 5× with HUNTER + WRITER sub-agents
- Γ avg = 0.0012 (good, but overhead high)
- **Action:** Created `vc-application` skill → Now single agent, Γ = 0.0028

### Framework Updates
This document should evolve based on:
- Actual Γ measurements
- New task patterns discovered
- OpenClaw updates (e.g., parallel limit changes)
- User feedback

**Update log:**
- 2026-02-10: v1.0 — Initial framework based on synthesis

---

## Quick Reference Card

| Task Size | Token Output | Sub-Agent? | Pattern |
|-----------|--------------|------------|---------|
| Simple | <2k | ❌ No | Single + Skill |
| Medium | 2k-10k | ⚠️ Maybe | Check skill first |
| Medium+ | 10k-15k | ⚠️ Maybe | If no skill |
| Complex | >15k | ✅ Yes | Decompose → Route |
| Parallel | Any | ✅ Yes | If N>3 independent |
| Sequential | Any | ❌ No | Single agent |
| Repetitive | Any | ❌ No | Create skill |

**Γ Threshold:** avg Γ < 1.2 after 10 runs → Revert to single agent

**Max Parallel:** 5 agents (OpenClaw limit)

**Overhead:** ~5k tokens per sub-agent

---

## Related Documents

- `SKILL-AUDIT.md` — Full skill library inventory
- `AGENTS.md` — Specialized agent definitions
- `memory/gamma-log.jsonl` — Decision history
- `multi-agent-routing-synthesis.md` — Research basis
- `gamma-metric-analysis.md` — Γ metric deep dive

---

*This is a living document. Update based on real-world Γ data.*
*Next review: 2026-02-17*
