# Should I Spawn a Sub-Agent? — Quick Reference Card
*Keep this visible when making routing decisions*

---

## ⚡ The 3-Second Decision

```
Output < 15k tokens?          → ❌ NO SUB-AGENT
Can I parallelize?            → ✅ MAYBE (check below)
Does a skill exist?           → ❌ NO SUB-AGENT (use skill)
Is it urgent/interactive?     → ❌ NO SUB-AGENT (latency)
```

---

## 📊 Decision Table

| Task Time | Output Tokens | Skills | Decision |
|-----------|---------------|--------|----------|
| <5 min | <2k | 1-3 | ❌ Single + Skill |
| 5-15 min | 2k-10k | 3-10 | ⚠️ Check skill first |
| 5-15 min | 10k-15k | 3-10 | ⚠️ Maybe (if no skill) |
| >15 min | >15k | >10 | ✅ Decompose → Route |

---

## ✅ Spawn When...

- [ ] Task is >15 min OR >15k tokens output
- [ ] Can parallelize into 2+ independent subtasks
- [ ] No existing skill handles 80%+ of task
- [ ] Expected Γ > 1.2 (based on history)
- [ ] Not time-sensitive (user can wait)

**If 3+ checked → SPAWN**

---

## ❌ DON'T Spawn When...

- [ ] Output <15k tokens (below 3× overhead threshold)
- [ ] Task is sequential (A→B→C, no parallelism)
- [ ] Existing skill already handles it
- [ ] User expects immediate response
- [ ] Task is repetitive (create skill instead)

**If 2+ checked → DON'T SPAWN**

---

## 🎯 Common Patterns

### ✅ GOOD (Spawn Sub-Agent)
- "Apply to 10 VC funds" → 10× HUNTER (parallel)
- "Research 5 companies + write memos" → RESEARCHER (parallel)
- "Create investor deck from scratch" → RESEARCHER + WRITER
- "Security audit all systems" → OPERATOR (specialized)

### ❌ BAD (Use Single Agent)
- "Send email" → Just use himalaya/gog
- "Add note to Obsidian" → Just use obsidian skill
- "Summarize article" → Use summarize skill
- "Check calendar" → Just use gog skill

---

## 💰 Token Economics

```
Sub-Agent Overhead:  ~5,000 tokens
Break-even Output:   >15,000 tokens (3× overhead)
Max Parallel:        5 agents (OpenClaw limit)
```

**Example:**
```
Task: "Generate 5 research briefs"
Single agent: 5 × 8k = 40k tokens, 30 min
Multi-agent:  5 × (5k overhead + 8k work) = 65k tokens, 6 min

Time saved:   24 min → ✅ WORTH IT
Token cost:   +25k (+62%) → ⚠️ Expensive but fast
```

---

## 📈 Γ-Metric Cheat Sheet

```
Γ = Task Success Score / Total Tokens

Γ > 1.5   → 🟢 Excellent (keep doing this)
Γ 1.2-1.5 → 🟡 Good (monitor)
Γ 1.0-1.2 → 🟠 Marginal (re-evaluate after 10 runs)
Γ < 1.0   → 🔴 INEFFICIENT (revert to single agent)
```

**After 10 runs:** If avg Γ < 1.2 → Stop spawning for this task type

---

## 🔍 Quick Checks Before Spawning

```bash
# 1. Does skill exist?
ls ~/.openclaw/workspace/skills/ | grep -i [keyword]

# 2. Check Γ history for this task type
cat memory/gamma-log.jsonl | jq 'select(.task_type=="[type]") | .gamma'

# 3. Estimate tokens
echo "Output: [estimate]k tokens"
echo "Overhead: 5k per agent"
echo "Break-even: >15k"
```

---

## 🚦 Traffic Light System

### 🟢 GREEN: Spawn Multi-Agent
- Parallel independent tasks (N>3)
- >15 min estimated time
- >30k token output
- Γ history > 1.2

### 🟡 YELLOW: Evaluate Carefully
- Medium complexity (5-15 min)
- 10-30k token output
- Some parallelism possible
- No clear Γ history

### 🔴 RED: Single Agent Only
- <5 min task
- <15k output
- Sequential dependencies
- Skill exists
- Time-sensitive

---

## 📝 Decision Log Template

```
Task: [description]
Estimated time: [X] min
Estimated output: [Y]k tokens
Parallelizable? [YES/NO]
Skill exists? [YES/NO - name]
Γ history: [value or "none"]

Decision: [SINGLE/MULTI/HIERARCHICAL]
Reasoning: [1-2 sentences]
```

---

## 🔗 Full Docs

- **Detailed framework:** `standards/AGENT-DECISION-FRAMEWORK.md`
- **Skill inventory:** `SKILL-AUDIT.md`
- **Decision history:** `memory/gamma-log.jsonl`
- **Agent definitions:** `AGENTS.md`

---

*Print this card and keep it visible during task routing*
*Update based on Γ data from gamma-log.jsonl*
