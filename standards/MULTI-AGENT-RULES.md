# MULTI-AGENT-RULES.md
# When to Use Single vs Multi-Agent Architecture

**Last Updated:** 2026-02-10  
**Status:** Active Standard

---

## Core Principle

**Default to single-agent unless complexity clearly justifies coordination overhead.**

Multi-agent systems have costs:
- Token overhead (communication, coordination)
- Latency (sequential handoffs)
- Context fragmentation
- Error propagation risk

**Γ (Collaboration Gain) > 1.0** is the goal. If multi-agent doesn't outperform single-agent at the same token budget, you're wasting resources.

---

## Decision Tree

```
┌─────────────────────────────────┐
│ Is this a complex task?         │
│ (Multiple distinct skills       │
│  or >10k tokens expected)       │
└────────┬───────────────┬────────┘
         │ NO            │ YES
         ▼               ▼
    ┌────────┐      ┌────────────────────────────┐
    │ SINGLE │      │ Can it be parallelized?    │
    │ AGENT  │      │ (Independent subtasks)     │
    └────────┘      └──────┬──────────────┬──────┘
                           │ NO           │ YES
                           ▼              ▼
                    ┌──────────────┐  ┌──────────────┐
                    │ Sequential?  │  │ MULTI-AGENT  │
                    │ (A→B→C)      │  │ (Parallel)   │
                    └──┬────────┬──┘  └──────────────┘
                       │ >3     │ ≤3
                       │ steps  │ steps
                       ▼        ▼
                  ┌────────┐ ┌────────┐
                  │ MULTI  │ │ SINGLE │
                  │ AGENT  │ │ AGENT  │
                  └────────┘ └────────┘
```

---

## Rules (Derived from Research)

### ✅ Use SINGLE AGENT when:

1. **Task requires <50 distinct skills**
   - Single agent can handle the full scope
   - No specialized expertise needed beyond general capability

2. **Expected output <5,000 tokens**
   - Coordination overhead would dominate
   - Faster to do it in one pass

3. **Task is sequential and simple**
   - Straightforward workflow (read → think → write)
   - No benefit from parallelization

4. **Latency is critical**
   - Multi-agent adds handoff delays
   - Real-time response needed

5. **Task is exploratory/creative**
   - Requires continuous context and flow state
   - Context switching would hurt quality

**Examples:**
- Write a blog post
- Research a single topic
- Draft an email
- Answer a question
- Summarize a document
- Code a single feature

---

### ✅ Use MULTI-AGENT when:

1. **Task requires >50 distinct skills**
   - Specialized expertise needed (RESEARCHER + WRITER + ANALYST)
   - Each agent has deep domain focus

2. **Subtasks can run in parallel**
   - Research 5 companies simultaneously
   - Generate multiple content variants
   - Independent data collection tasks

3. **Task has clear module boundaries**
   - Research → Analysis → Recommendation
   - Data Collection → Processing → Visualization
   - Each stage benefits from specialized agent

4. **Quality > Speed**
   - Willing to trade latency for better output
   - Each agent can deep-dive in their domain

5. **Task is large (>10k token output)**
   - Breaking into chunks prevents context overload
   - Specialization improves per-section quality

6. **Iterative refinement needed**
   - One agent drafts, another reviews/edits
   - Separation of concerns improves objectivity

**Examples:**
- Multi-company research + comparison report
- Complex proposal (research + writing + review)
- Large content pipeline (research → draft → edit → optimize)
- System design (architect + implementer + reviewer)
- Parallel data gathering (scrape 10 sources)

---

## Token Budget Thresholds

| Expected Output | Recommended Approach |
|-----------------|---------------------|
| <1,000 tokens   | Single agent (always) |
| 1,000-5,000 tokens | Single agent (unless parallel subtasks) |
| 5,000-15,000 tokens | Consider multi-agent if >3 distinct phases |
| >15,000 tokens  | Multi-agent (break into chunks) |

**Coordination Overhead:** Each agent handoff costs ~500-1,000 tokens (context passing, instructions, validation).

**Break-even point:** Multi-agent only makes sense if quality gain or parallelization saves >20% tokens compared to single-agent at same quality.

---

## Agent Specialization Guide

When going multi-agent, use these specialized roles:

| Agent | When to Use | Strengths |
|-------|-------------|-----------|
| **HUNTER** | Job search, sales pipeline | Persistence, tracking, follow-up |
| **WRITER** | Long-form content | Clarity, flow, voice consistency |
| **RESEARCHER** | Deep dives, fact-finding | Thoroughness, synthesis, citations |
| **ANALYST** | Data, metrics, trends | Numbers, patterns, insights |
| **STRATEGIST** | Decisions, trade-offs | Frameworks, second-order thinking |
| **OPERATOR** | Systems, automation | Structure, scalability, SOPs |
| **DEALMAKER** | Proposals, negotiations | Persuasion, value framing |

**Anti-pattern:** Invoking an agent for a 2-minute task. Just do it yourself.

---

## Γ-Tracking Integration

After every multi-agent task, log metrics:
```bash
./scripts/gamma-tracker.sh \
    "task_name" \
    <agents_used> \
    <tokens_in> \
    <tokens_out> \
    <runtime_sec> \
    <output_file_path>
```

**Weekly review:**
```bash
./scripts/gamma-report.sh 7
```

**Red flags (investigate):**
- Γ < 0.5 of average → Task should've been single-agent
- >3 agents on <5k token task → Over-engineered
- >50% of tasks below avg Γ → Recalibrate decision tree

---

## Common Mistakes

### ❌ Over-delegation
**Problem:** Spawning sub-agent for every small subtask  
**Fix:** Only delegate if task is >2,000 tokens OR requires specialized skill

### ❌ Linear Pipeline Abuse
**Problem:** Agent A → Agent B → Agent C for sequential work  
**Fix:** Use multi-agent only if each stage adds unique expertise. Otherwise, single agent with phased approach.

### ❌ Context Loss
**Problem:** Agent B doesn't have full context from Agent A  
**Fix:** Pass comprehensive context (include relevant files, not just summary). Or reconsider if single-agent would be better.

### ❌ Token Budget Ignorance
**Problem:** Not tracking if multi-agent actually saves tokens  
**Fix:** Use gamma-tracker.sh religiously. Let data drive decisions.

---

## Decision Checklist

Before spawning a sub-agent, answer:

1. ☑ Is expected output >5,000 tokens?
2. ☑ Are there 2+ distinct specialized skills needed?
3. ☑ Can subtasks run in parallel OR does each phase need deep focus?
4. ☑ Will coordination overhead (<1,000 tokens) be worth it?
5. ☑ Am I avoiding this because I'm lazy, or is it genuinely complex?

**If 3+ YES → Multi-agent**  
**If 2 or fewer YES → Single agent**

---

## Continuous Improvement

This is a living document. Update based on:
- Γ-report insights (weekly review)
- Failed tasks (post-mortems)
- Token waste patterns
- User feedback (Florian's corrections)

**Monthly review:** Look at gamma-log.json, identify patterns, update thresholds.

---

## References

- OpenClaw Sub-agent System: `AGENTS.md`
- Tracking: `scripts/gamma-tracker.sh`, `scripts/gamma-report.sh`
- Memory: `memory/gamma-log.json`

---

**Remember:** Multi-agent is a tool, not a default. Use it when it multiplies value, not just because you can.

*Γ > 1 or bust.* 🎯
