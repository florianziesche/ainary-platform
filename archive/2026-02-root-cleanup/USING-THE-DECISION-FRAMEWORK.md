# Using the Multi-Agent Decision Framework — Integration Guide
*How to actually use these new documents in your workflow*

---

## 🎯 What You Got

After Action Item 5, you now have:

| File | Purpose | When to Use |
|------|---------|-------------|
| `SKILL-AUDIT.md` | Skill inventory (62 total) | Before deciding "no skill exists" |
| `standards/AGENT-DECISION-FRAMEWORK.md` | Complete decision framework (13.6 KB) | Deep dive, study once |
| `standards/SPAWN-DECISION-QUICKREF.md` | 1-page cheat sheet | Keep open during task routing |
| `scripts/should-i-spawn.sh` | Interactive decision helper | When uncertain about spawning |
| `memory/gamma-log.jsonl` | Decision tracking log | After each multi-agent decision |

---

## 📖 How to Use (Step-by-Step)

### Step 1: First Time Setup (One-Time)

1. **Read the framework** (30 min):
   ```bash
   cat standards/AGENT-DECISION-FRAMEWORK.md
   ```
   Focus on:
   - Decision tree (section "Decision Tree")
   - Token budget rules (section "Token Budget Rules")
   - Anti-patterns (section "Anti-Patterns")

2. **Familiarize with skills** (15 min):
   ```bash
   cat SKILL-AUDIT.md | less
   ```
   Skim the categories, note high-use skills you didn't know existed

3. **Print the quick reference** (optional):
   ```bash
   cat standards/SPAWN-DECISION-QUICKREF.md
   ```
   Print or keep open in a terminal window

4. **Test the decision script**:
   ```bash
   ./scripts/should-i-spawn.sh "Write blog post" 20 25000
   ```

---

### Step 2: Every Task (Daily Workflow)

When a task comes in, follow this sequence:

#### A. Quick Mental Check (3 seconds)
```
Is it < 5 min? → Just do it (single agent)
Is it > 15 min? → Decompose (go to B)
In between? → Check skill first (go to C)
```

#### B. For Complex Tasks (>15 min)
1. Open quick reference:
   ```bash
   cat standards/SPAWN-DECISION-QUICKREF.md
   ```

2. Ask yourself:
   - Can I parallelize? (Independent subtasks?)
   - Is output >15k tokens? (3× overhead threshold?)
   - Does a skill exist? (Check SKILL-AUDIT.md)

3. If uncertain, run:
   ```bash
   ./scripts/should-i-spawn.sh
   ```
   (Interactive prompts guide you)

4. **Log your decision** (important!):
   - Script offers to log automatically
   - Or manually: `echo '{...}' >> memory/gamma-log.jsonl`

#### C. Skill Check
```bash
# Quick search
ls ~/.openclaw/workspace/skills/ | grep -i [keyword]
ls ~/.nvm/versions/node/v*/lib/node_modules/openclaw/skills/ | grep -i [keyword]

# Or open audit
cat SKILL-AUDIT.md | grep -i [keyword]
```

If skill exists → Use it (single agent)
If no skill → Continue to decision tree

---

### Step 3: Weekly Review (Mondays)

1. **Analyze Γ data**:
   ```bash
   # Count decisions this week
   cat memory/gamma-log.jsonl | jq -s 'length'
   
   # Average Γ by task type
   cat memory/gamma-log.jsonl | jq -s 'group_by(.task_type) | map({type: .[0].task_type, avg_gamma: (map(.gamma) | add / length)})'
   
   # Find inefficient tasks (Γ < 1.2)
   cat memory/gamma-log.jsonl | jq 'select(.gamma < 0.0012)'
   ```

2. **Update framework** if needed:
   - Found a pattern that always works? → Document it
   - Found a task type that never benefits? → Add to anti-patterns
   - Repeated a task 5+ times? → Consider creating a skill

3. **Clean up logs** (optional):
   ```bash
   # Archive old entries (keep last 100)
   tail -100 memory/gamma-log.jsonl > memory/gamma-log.tmp
   mv memory/gamma-log.tmp memory/gamma-log.jsonl
   ```

---

## 🎮 Real-World Examples

### Example 1: Job Application Batch
**Task:** "Apply to 10 VC funds with custom cover letters"

**Process:**
1. Mental check: >15 min, >50k tokens → Complex
2. Open quick reference: Can parallelize? YES (10 independent applications)
3. Check skill: `ls skills/ | grep vc` → Found `vc-application`
4. Decision: Use `vc-application` skill, but spawn 5 sub-agents (batched, 2 funds each)
5. Log:
   ```bash
   ./scripts/should-i-spawn.sh "VC applications batch" 60 80000
   # Answer prompts: yes to parallel, no to skill (custom covers needed)
   # → Recommends MULTI-AGENT
   ```

**Outcome:** Multi-agent parallel, 5× faster than sequential

---

### Example 2: Email Summary
**Task:** "Summarize my inbox"

**Process:**
1. Mental check: <5 min, <2k tokens → Simple
2. Check skill: `himalaya` or `gog` exists
3. Decision: Single agent + skill
4. No need to log (trivial task)

**Outcome:** Single agent, done in 30 seconds

---

### Example 3: Research Deep Dive
**Task:** "Research AI agent frameworks and write a 10-page report"

**Process:**
1. Mental check: >15 min, >30k tokens → Complex
2. Run decision script:
   ```bash
   ./scripts/should-i-spawn.sh "Research + report" 120 35000
   ```
3. Prompts:
   - Skill exists? NO (custom research)
   - Can parallelize? PARTIALLY (research yes, writing no)
   - Immediate response? NO
   - → Recommends EVALUATE/MULTI-AGENT
4. Decision: Spawn RESEARCHER (parallel for 5 frameworks), then WRITER (sequential)
5. Log via script

**Outcome:** Hierarchical coordination, research parallelized, writing sequential

---

## 🚨 Common Mistakes to Avoid

### Mistake 1: Not Checking Skills First
**Wrong:** Spawn sub-agent to "send email"
**Right:** Check `ls skills/ | grep -i email` → Find `himalaya`, use it

**Fix:** Always run skill check before spawning

---

### Mistake 2: Spawning for Sequential Tasks
**Wrong:** Task A → Spawn agent → Task B → Spawn agent → Task C
**Right:** Single agent handles A → B → C sequentially

**Fix:** Only spawn if parallelism gains exist

---

### Mistake 3: Ignoring Token Threshold
**Wrong:** Task outputs 5k tokens → Spawn sub-agent (5k overhead = 100% waste)
**Right:** Output must be >15k (3× overhead) to justify spawn

**Fix:** Quick math: `output_tokens / 5000 > 3`?

---

### Mistake 4: Not Logging Decisions
**Wrong:** Spawn sub-agents repeatedly without tracking Γ
**Right:** Log every decision → Analyze patterns → Improve over time

**Fix:** Use script's auto-log feature or manual entry

---

## 📊 Success Metrics

### Week 1 Goals
- [ ] 100% of complex tasks use decision framework
- [ ] All multi-agent decisions logged to gamma-log.jsonl
- [ ] At least 1 weekly review completed

### Month 1 Goals
- [ ] Identify 2-3 task types that consistently benefit from multi-agent
- [ ] Identify 2-3 task types that should NEVER use multi-agent
- [ ] Create 1 new skill from repeated sub-agent pattern
- [ ] Average Γ for multi-agent tasks > 1.2

### Long-Term Goals
- [ ] Framework becomes second nature (no need for script)
- [ ] Skill library grows to cover 90%+ of tasks
- [ ] Token efficiency improves 15-30% (fewer wasteful spawns)
- [ ] Self-optimization loop active (Γ data → framework updates → better decisions)

---

## 🔧 Customization Tips

### Add Your Own Patterns
Found a pattern that works? Add it to the framework:

```bash
# Edit framework
vim standards/AGENT-DECISION-FRAMEWORK.md

# Add under "Multi-Agent Patterns" section:
### Pattern 4: Your New Pattern
**When:** [conditions]
**Example:** [your use case]
**Γ Impact:** [high/medium/low]
```

### Create Task-Specific Scripts
For frequently repeated decisions:

```bash
# Example: vc-application-decider.sh
if [ $NUM_FUNDS -gt 3 ]; then
    echo "Use multi-agent (parallel)"
else
    echo "Use single agent (sequential)"
fi
```

### Integrate with Pre-Flight
Update `scripts/pre-flight.sh` to call decision helper:

```bash
# Add to pre-flight.sh
if [ "$TASK_COMPLEXITY" == "high" ]; then
    ./scripts/should-i-spawn.sh "$TASK_DESC" "$ESTIMATED_MIN" "$ESTIMATED_TOKENS"
fi
```

---

## 📚 Reference Quick Links

| Need | File | Command |
|------|------|---------|
| Full framework | `standards/AGENT-DECISION-FRAMEWORK.md` | `cat standards/AGENT-DECISION-FRAMEWORK.md` |
| Quick reference | `standards/SPAWN-DECISION-QUICKREF.md` | `cat standards/SPAWN-DECISION-QUICKREF.md` |
| Skill inventory | `SKILL-AUDIT.md` | `cat SKILL-AUDIT.md` |
| Decision helper | `scripts/should-i-spawn.sh` | `./scripts/should-i-spawn.sh` |
| Γ analysis | `memory/gamma-log.jsonl` | `cat memory/gamma-log.jsonl \| jq` |

---

## 🎓 Learning Path

### Beginner (Week 1)
1. Read AGENT-DECISION-FRAMEWORK.md once (30 min)
2. Keep SPAWN-DECISION-QUICKREF.md open during work
3. Use `should-i-spawn.sh` for every complex task
4. Log all decisions

### Intermediate (Week 2-4)
1. Start pattern recognition (which tasks benefit?)
2. Reduce script usage as intuition builds
3. Conduct first weekly Γ review
4. Update framework with learnings

### Advanced (Month 2+)
1. Framework becomes automatic (no need for script)
2. Proactively identify skill creation opportunities
3. Contribute patterns back to framework
4. Optimize token budgets based on Γ data

---

## 🤝 Integration with Existing Workflow

### With AGENTS.md
```
Task arrives
→ Check AGENT-DECISION-FRAMEWORK (spawn or not?)
  → If spawn: Check AGENTS.md (which specialized agent?)
  → If single: Execute directly
```

### With pre-flight.sh
```
./scripts/pre-flight.sh [task-type]
→ Loads task-specific knowledge
→ Calls should-i-spawn.sh automatically (if complex)
→ Proceeds with decision
```

### With MEMORY.md
```
After task completion
→ Log to gamma-log.jsonl
→ If significant: Update MEMORY.md with learnings
→ Weekly: Review Γ patterns, update long-term memory
```

---

## 💡 Pro Tips

1. **Batch similar tasks** — If you're doing 10 similar things, that's a signal to parallelize
2. **Trust the math** — Output < 15k tokens? Don't spawn. Math doesn't lie.
3. **Skills > Sub-agents** — Repeated patterns should become skills
4. **Log everything** — Can't optimize what you don't measure
5. **Review weekly** — Patterns emerge over 10+ runs, not 1-2

---

## 🆘 Troubleshooting

### "I don't know if I can parallelize"
→ Ask: "Could 2 people work on this simultaneously without stepping on each other?"
→ If yes: Parallelizable
→ If no: Sequential

### "Script recommends spawn, but I'm not sure"
→ Check Γ history: Has this task type been done before?
→ If no history: Try it, log the result, learn
→ If history shows Γ < 1.2: Don't spawn

### "Task is complex but no parallelism"
→ Single agent is likely better
→ Sub-agent only adds overhead, no speed gain
→ Exception: If specialized agent (HUNTER, WRITER) has domain expertise

### "I forgot to log a decision"
→ Log it retroactively:
   ```bash
   echo '{"timestamp":"2026-02-10T12:00:00Z","task_id":"...","gamma":0.0015}' >> memory/gamma-log.jsonl
   ```
→ Better late than never!

---

## ✅ Daily Checklist

**Before starting work:**
- [ ] Quick reference open in terminal (`cat standards/SPAWN-DECISION-QUICKREF.md`)
- [ ] Know where decision script is (`./scripts/should-i-spawn.sh`)

**For each complex task:**
- [ ] Run mental 3-second check (simple/medium/complex?)
- [ ] Check skill library if medium/complex
- [ ] Use decision script if uncertain
- [ ] Log decision to gamma-log.jsonl

**End of day:**
- [ ] Review logged decisions (any surprises?)
- [ ] Update MEMORY.md if learned something significant

**Monday morning:**
- [ ] Weekly Γ review (10 min)
- [ ] Identify patterns (what worked, what didn't)
- [ ] Update framework or create new skills if needed

---

## 🎯 Conclusion

**The framework is only useful if you use it.**

- **Week 1:** Lean on scripts heavily
- **Week 2-4:** Build intuition
- **Month 2+:** Framework becomes automatic

Every logged decision makes the system smarter. Every Γ review improves efficiency. This is compound knowledge — it grows over time.

**Start simple:**
1. Keep quick reference open
2. Use decision script for complex tasks
3. Log decisions
4. Review weekly

The rest will follow.

---

*Integration guide version 1.0 — 2026-02-10*
*Update based on real-world usage patterns*
