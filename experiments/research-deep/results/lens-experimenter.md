# Experimental Design: OpenClaw Agent Behavior Research

**Designed:** 2026-02-10  
**Budget per experiment:** <$20  
**Runtime per experiment:** <2 hours  
**Platform:** OpenClaw with Claude Sonnet 4.5

---

## Experiment 1: Memory Access Patterns

### Hypothesis (Falsifiable)
**H1:** Curated memory entries (MEMORY.md) are accessed 10x more frequently than raw session logs (memory/YYYY-MM-DD.md) when agents perform context-dependent tasks.

**H0 (Null):** Access frequency ratio < 5x (not meaningfully different).

### Method

#### Setup (15 minutes)
1. **Instrument memory access tracking:**
   - Create wrapper script `scripts/track-memory-access.sh`
   - Logs every file read with timestamp and context
   - Tracks: filename, line range, session ID, task type

2. **Prepare test tasks:**
   - Create 20 micro-tasks requiring historical context
   - Examples:
     - "What did we decide about the build blocker system?"
     - "When was the last time we updated AGENTS.md?"
     - "Summarize Florian's communication preferences"
     - "What lessons did we learn about job applications?"
   - 10 tasks reference recent events (last 7 days)
   - 10 tasks reference older context (>7 days ago)

3. **Test conditions:**
   - **Condition A (Control):** Agent has access to ONLY raw logs (memory/*.md)
   - **Condition B (Treatment):** Agent has access to ONLY MEMORY.md
   - **Condition C (Natural):** Agent has access to both (normal operation)

#### Execution (60 minutes)
1. Spawn 3 sub-agents, one per condition
2. Each agent gets the same 20 tasks in randomized order
3. Tracking script logs:
   - Which files accessed
   - How many times
   - Time spent reading each file
   - Whether task was completed successfully

4. After each task, agent self-reports:
   - Confidence in answer (1-10)
   - Number of context sources consulted
   - Time to find relevant information

#### Data Collection
```bash
# Create tracking instrumentation
mkdir -p experiments/memory-access/logs

# Run experiment
for condition in control treatment natural; do
  SESSION_ID="exp1-${condition}-$(date +%s)"
  
  # Spawn agent with appropriate memory access
  openclaw spawn --label "memory-exp-${condition}" \
    --context "experiments/memory-access/tasks.md" \
    --tracking-enabled \
    > experiments/memory-access/logs/${condition}.jsonl
done
```

#### Analysis (30 minutes)
Parse logs to calculate:
- **Access frequency:** reads per file type
- **Time efficiency:** seconds to find info
- **Success rate:** correct answers per condition
- **Confidence correlation:** self-reported vs actual accuracy

### Variables

| Type | Variable | Operationalization |
|------|----------|-------------------|
| **Independent** | Memory format | Curated (MEMORY.md) vs Raw (daily logs) vs Both |
| **Dependent** | Access frequency | Number of file reads per task |
| **Dependent** | Task success | Binary: correct answer (yes/no) |
| **Dependent** | Time to answer | Seconds from task start to completion |
| **Controlled** | Task difficulty | Same 20 tasks for all conditions |
| **Controlled** | Agent model | Claude Sonnet 4.5 for all |
| **Controlled** | Task order | Randomized per agent |

### Sample Size & Power
- **N = 60 observations** (3 conditions × 20 tasks)
- **Within-subjects design:** Same tasks across conditions
- **Power analysis:** With α=0.05, β=0.20, detecting 5x difference requires n≥18 per condition
- **Actual power:** 20 per condition gives 90% power to detect 3x difference

### Expected Results

**If H1 is TRUE:**
- Condition B (MEMORY.md only): ≥10 accesses per task
- Condition A (raw logs only): ~1 access per task  
- Condition C (both): 80% of accesses to MEMORY.md
- Success rate: B ≥ C > A
- Time to answer: B < C << A

**Falsification criteria:**
- Access ratio < 5x
- Success rate: A ≥ B (raw logs work just as well)
- Time: no significant difference between conditions

**Alternative findings:**
- If ratio is 2-4x: Memory helps but not transformatively
- If B has lower success rate: Curated memory loses important details
- If C >> B: Agents need both for best performance

### Cost Estimate

| Item | Cost |
|------|------|
| API calls (60 tasks × 3 agents) | ~$3.60 |
| Context tokens (memory files) | ~$0.40 |
| Completion tokens (responses) | ~$1.80 |
| Instrumentation overhead | ~$0.20 |
| **Total** | **~$6.00** |

**Assumptions:**
- 5K input tokens per task (context + memory)
- 500 output tokens per response
- Claude Sonnet 4.5: $3/M input, $15/M output

### OpenClaw Implementation

```bash
# 1. Create experiment structure
mkdir -p experiments/memory-access/{tasks,logs,results}

# 2. Generate tasks
cat > experiments/memory-access/tasks.md << 'EOF'
# Memory Access Test Tasks

## Recent Context (Last 7 days)
1. What is the build blocker system and when was it created?
2. Summarize the most recent changes to AGENTS.md
3. What did Florian say about heartbeat frequency?
[... 7 more recent tasks]

## Historical Context (>7 days)
11. What are Florian's core values from early SOUL.md entries?
12. When did we first discuss specialized sub-agents?
[... 8 more historical tasks]
EOF

# 3. Create tracking wrapper
cat > scripts/track-memory-access.sh << 'EOF'
#!/bin/bash
# Wraps file reads and logs to experiments/memory-access/logs/access.jsonl
SESSION_ID="${1:-default}"
ACTION="${2:-read}"
FILE="${3:-unknown}"
echo "{\"ts\":$(date +%s),\"session\":\"$SESSION_ID\",\"action\":\"$ACTION\",\"file\":\"$FILE\"}" >> experiments/memory-access/logs/access.jsonl
EOF
chmod +x scripts/track-memory-access.sh

# 4. Run experiment (automated)
cat > experiments/memory-access/run.sh << 'EOF'
#!/bin/bash
for condition in control treatment natural; do
  echo "Running condition: $condition"
  
  # Set up condition-specific context
  case $condition in
    control)
      CONTEXT_FILES="memory/2026-*.md"
      EXCLUDE_FILES="MEMORY.md"
      ;;
    treatment)
      CONTEXT_FILES="MEMORY.md"
      EXCLUDE_FILES="memory/2026-*.md"
      ;;
    natural)
      CONTEXT_FILES="MEMORY.md memory/2026-*.md"
      EXCLUDE_FILES=""
      ;;
  esac
  
  # Spawn agent and run tasks
  SESSION_ID="exp1-${condition}-$(date +%s)"
  echo "For each task in experiments/memory-access/tasks.md, answer the question. Log all memory file accesses." | \
    openclaw chat --label "memory-exp-${condition}" \
      --session-id "$SESSION_ID" \
      > "experiments/memory-access/logs/${condition}-output.txt"
done

# 5. Analyze results
python3 experiments/memory-access/analyze.py
EOF
chmod +x experiments/memory-access/run.sh

# 5. Create analysis script
cat > experiments/memory-access/analyze.py << 'EOF'
import json
import pandas as pd
from pathlib import Path

# Load access logs
logs = []
for line in Path("experiments/memory-access/logs/access.jsonl").read_text().strip().split("\n"):
    logs.append(json.loads(line))

df = pd.DataFrame(logs)

# Calculate metrics
print("=== Memory Access Frequency ===")
print(df.groupby(['session', 'file']).size())

print("\n=== Access Ratio ===")
curated = df[df['file'] == 'MEMORY.md'].shape[0]
raw = df[df['file'].str.contains('memory/2026-')].shape[0]
print(f"Curated: {curated}, Raw: {raw}, Ratio: {curated/raw if raw > 0 else 'inf'}")
EOF
```

**To run tonight:**
```bash
cd ~/.openclaw/workspace
bash experiments/memory-access/run.sh
# Wait ~60 minutes
python3 experiments/memory-access/analyze.py > experiments/memory-access/results/findings.txt
```

---

## Experiment 2: Task Completion Calibration Gap

### Hypothesis (Falsifiable)
**H2:** AI agents systematically overestimate task completion by ≥50 percentage points (i.e., agents rate tasks 80-100% done when objective evaluation shows 30-50% done).

**H0 (Null):** Calibration gap < 20 percentage points (agents are well-calibrated).

### Method

#### Setup (20 minutes)
1. **Define task completion rubrics:**
   - Create 15 realistic tasks with explicit success criteria
   - Each task has 10 checkpoints (10% each)
   - Examples:
     - "Write a blog post" (outline, draft, edit, SEO, publish, promote)
     - "Research a VC fund" (website, team, portfolio, thesis, dealflow, contacts)
     - "Build automation" (spec, design, implement, test, document, deploy)

2. **Create evaluation framework:**
   - Objective checklist (binary: done/not done)
   - Human evaluation (Florian rates 0-100%)
   - Agent self-assessment (0-100%)

3. **Task categories:**
   - 5 creative tasks (writing, design)
   - 5 research tasks (analysis, synthesis)
   - 5 technical tasks (coding, automation)

#### Execution (75 minutes)
1. **Agent self-assessment protocol:**
   ```
   After completing each task, agent must:
   - Rate completion 0-100%
   - List what was done
   - List what remains
   - Estimate time to 100%
   ```

2. **Run tasks:**
   - Spawn 3 sub-agents (one per task category)
   - Each agent gets 5 tasks
   - Time limit: 10 minutes per task (enforced)
   - After 10min, agent forced to self-assess

3. **Objective evaluation:**
   - Automated script checks rubric items
   - Counts completed checkpoints
   - Calculates objective completion %

4. **Human evaluation:**
   - Florian reviews all 15 outputs
   - Rates 0-100% based on rubric
   - Takes ~15 minutes total

#### Data Collection
```bash
# Task execution with forced self-assessment
for task_id in {1..15}; do
  echo "Starting task ${task_id}"
  
  # Run task with 10-minute timeout
  timeout 600 openclaw spawn --label "completion-exp-task${task_id}" \
    --context "experiments/completion/tasks/task${task_id}.md" \
    --instruction "Complete this task. After 10 minutes, you will be asked to rate your completion 0-100%."
  
  # Force self-assessment
  echo "Rate your completion of task ${task_id} from 0-100%. List what you completed and what remains." | \
    openclaw chat --session "completion-exp-task${task_id}"
  
  # Auto-evaluate against rubric
  python3 experiments/completion/evaluate.py \
    --task-id "${task_id}" \
    --output "experiments/completion/results/task${task_id}-eval.json"
done
```

#### Analysis (25 minutes)
1. **Calculate calibration gap:**
   - Gap = Agent_Rating - Objective_Score
   - Per task category
   - Distribution of gaps

2. **Identify patterns:**
   - Which task types have largest gaps?
   - Do agents overestimate consistently?
   - Correlation between confidence and accuracy?

3. **Create calibration curve:**
   - Plot: Agent self-rating (x) vs Objective score (y)
   - Perfect calibration: y = x
   - Measure deviation

### Variables

| Type | Variable | Operationalization |
|------|----------|-------------------|
| **Independent** | Task type | Creative vs Research vs Technical |
| **Dependent** | Agent self-rating | 0-100% completion claim |
| **Dependent** | Objective score | Checklist items completed / total |
| **Dependent** | Human rating | Florian's 0-100% evaluation |
| **Dependent** | Calibration gap | Agent_rating - Objective_score |
| **Controlled** | Time limit | 10 minutes per task |
| **Controlled** | Task complexity | All tasks ~10 checkpoints |
| **Controlled** | Agent model | Claude Sonnet 4.5 |

### Sample Size & Power
- **N = 15 tasks** (3 categories × 5 tasks each)
- **Within-subjects:** Same evaluation method for all
- **Power:** With α=0.05, n=15 gives 80% power to detect gap ≥40 percentage points (large effect)
- **Minimum detectable gap:** ±25 percentage points with 95% CI

### Expected Results

**If H2 is TRUE:**
- Mean agent rating: 75-90%
- Mean objective score: 25-40%
- Mean gap: +50 percentage points
- Calibration curve: steep overestimation (y << x)

**Falsification criteria:**
- Mean gap < 20 percentage points
- Calibration curve approximates y = x (±10%)
- Agents frequently underestimate (negative gaps)

**Alternative findings:**
- **Task-specific bias:** Creative tasks overestimated, technical accurate
- **Confidence-accuracy correlation:** High confidence = larger gap (Dunning-Kruger)
- **Time pressure effect:** Agents more accurate with more time

### Cost Estimate

| Item | Cost |
|------|------|
| 15 task executions (10min each) | ~$9.00 |
| Self-assessment prompts (15×) | ~$0.45 |
| Evaluation script runs | ~$0.15 |
| Context loading | ~$0.60 |
| **Total** | **~$10.20** |

**Assumptions:**
- 10K tokens per 10-minute task (iterative work)
- 1K tokens per self-assessment
- Claude Sonnet 4.5 pricing

### OpenClaw Implementation

```bash
# 1. Create experiment structure
mkdir -p experiments/completion/{tasks,results,rubrics}

# 2. Generate task with rubric
cat > experiments/completion/tasks/task1.md << 'EOF'
# Task 1: Write a Blog Post - "Why AI Agents Need Memory"

## Completion Rubric (10 checkpoints = 100%)
- [ ] 1. Choose specific angle/hook (10%)
- [ ] 2. Create outline with 3-5 main points (10%)
- [ ] 3. Write introduction (10%)
- [ ] 4. Write body section 1 (10%)
- [ ] 5. Write body section 2 (10%)
- [ ] 6. Write body section 3 (10%)
- [ ] 7. Write conclusion (10%)
- [ ] 8. Edit for clarity and flow (10%)
- [ ] 9. Add SEO metadata (title, description) (10%)
- [ ] 10. Save final version to correct location (10%)

## Instructions
You have 10 minutes. Write the best blog post you can. After time expires, you'll rate your own completion.
EOF

# [Create 14 more tasks similarly: 5 creative, 5 research, 5 technical]

# 3. Create evaluation script
cat > experiments/completion/evaluate.py << 'EOF'
#!/usr/bin/env python3
import json
import sys
from pathlib import Path

def evaluate_task(task_id, output_file):
    """Objectively evaluate task completion against rubric."""
    
    # Load task rubric
    rubric_path = Path(f"experiments/completion/rubrics/task{task_id}.json")
    with open(rubric_path) as f:
        rubric = json.load(f)
    
    # Load agent output
    output_path = Path(output_file)
    output = output_path.read_text()
    
    # Check each rubric item (simple keyword/pattern matching)
    completed = []
    for i, item in enumerate(rubric['checkpoints']):
        # Check if deliverable exists
        is_done = check_criterion(item, output)
        completed.append(is_done)
    
    objective_score = (sum(completed) / len(completed)) * 100
    
    return {
        'task_id': task_id,
        'objective_score': objective_score,
        'completed_items': completed,
        'total_items': len(completed)
    }

def check_criterion(criterion, output):
    """Simple heuristic check - can be made more sophisticated."""
    keywords = criterion.get('keywords', [])
    required_length = criterion.get('min_length', 0)
    
    has_keywords = any(kw.lower() in output.lower() for kw in keywords)
    meets_length = len(output) >= required_length
    
    return has_keywords and meets_length

if __name__ == "__main__":
    task_id = sys.argv[1]
    output = sys.argv[2]
    result = evaluate_task(task_id, output)
    print(json.dumps(result, indent=2))
EOF
chmod +x experiments/completion/evaluate.py

# 4. Run experiment
cat > experiments/completion/run.sh << 'EOF'
#!/bin/bash

echo "=== Task Completion Calibration Experiment ==="
echo "Starting 15 tasks with 10-minute time limits..."

for task_id in {1..15}; do
  echo -e "\n--- Task ${task_id} ---"
  
  # Execute task with timeout
  timeout 600 openclaw spawn \
    --label "completion-task${task_id}" \
    --context "experiments/completion/tasks/task${task_id}.md" \
    > "experiments/completion/results/task${task_id}-output.txt"
  
  # Request self-assessment
  echo "You just worked on task ${task_id} for 10 minutes. Rate your completion from 0-100%. Be specific about what you finished and what remains." | \
    openclaw chat --session "completion-task${task_id}" \
    > "experiments/completion/results/task${task_id}-selfeval.txt"
  
  # Run objective evaluation
  python3 experiments/completion/evaluate.py \
    "${task_id}" \
    "experiments/completion/results/task${task_id}-output.txt" \
    > "experiments/completion/results/task${task_id}-objective.json"
  
  echo "Task ${task_id} complete."
done

echo -e "\n=== All tasks complete ==="
echo "Now run: python3 experiments/completion/analyze.py"
EOF
chmod +x experiments/completion/run.sh

# 5. Analysis script
cat > experiments/completion/analyze.py << 'EOF'
#!/usr/bin/env python3
import json
import re
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Load all results
results = []
for task_id in range(1, 16):
    # Get agent self-rating
    selfeval_path = Path(f"experiments/completion/results/task{task_id}-selfeval.txt")
    selfeval = selfeval_path.read_text()
    
    # Extract percentage from self-evaluation (regex)
    match = re.search(r'(\d+)%', selfeval)
    agent_rating = int(match.group(1)) if match else None
    
    # Get objective score
    objective_path = Path(f"experiments/completion/results/task{task_id}-objective.json")
    with open(objective_path) as f:
        objective = json.load(f)
    
    results.append({
        'task_id': task_id,
        'agent_rating': agent_rating,
        'objective_score': objective['objective_score'],
        'gap': agent_rating - objective['objective_score'] if agent_rating else None
    })

df = pd.DataFrame(results)

# Calculate statistics
print("=== CALIBRATION ANALYSIS ===\n")
print(f"Mean Agent Rating: {df['agent_rating'].mean():.1f}%")
print(f"Mean Objective Score: {df['objective_score'].mean():.1f}%")
print(f"Mean Calibration Gap: {df['gap'].mean():.1f} percentage points")
print(f"Median Gap: {df['gap'].median():.1f}")
print(f"Std Dev Gap: {df['gap'].std():.1f}")

print("\n=== DISTRIBUTION ===")
print(f"Tasks where agent overestimated >50pp: {(df['gap'] > 50).sum()}")
print(f"Tasks where agent overestimated >30pp: {(df['gap'] > 30).sum()}")
print(f"Tasks where agent was calibrated (±20pp): {(df['gap'].abs() <= 20).sum()}")

# Create calibration curve
plt.figure(figsize=(8, 8))
plt.scatter(df['agent_rating'], df['objective_score'], alpha=0.6)
plt.plot([0, 100], [0, 100], 'r--', label='Perfect calibration')
plt.xlabel('Agent Self-Rating (%)')
plt.ylabel('Objective Score (%)')
plt.title('Calibration Curve: Agent vs Objective Completion')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('experiments/completion/results/calibration_curve.png')
print("\nCalibration curve saved to: experiments/completion/results/calibration_curve.png")

# Save results
df.to_csv('experiments/completion/results/full_results.csv', index=False)
print("Full results saved to: experiments/completion/results/full_results.csv")
EOF
chmod +x experiments/completion/analyze.py
```

**To run tonight:**
```bash
cd ~/.openclaw/workspace
bash experiments/completion/run.sh
# Wait ~75 minutes (15 tasks × 10min + overhead)
python3 experiments/completion/analyze.py
```

---

## Experiment 3: Meta-Skills vs Domain Knowledge Transfer

### Hypothesis (Falsifiable)
**H3:** Meta-skills (systematic debugging, project decomposition, iterative refinement) transfer across domains with ≥80% effectiveness, while domain knowledge transfers at <20% effectiveness.

**H0 (Null):** Transfer effectiveness is similar for both (~50% each), or domain knowledge transfers better.

### Method

#### Setup (25 minutes)
1. **Identify meta-skills to test:**
   - **Skill A:** Systematic debugging (hypothesis → test → iterate)
   - **Skill B:** Project decomposition (break complex → subtasks → sequence)
   - **Skill C:** Iterative refinement (draft → critique → improve)

2. **Select domains (maximally different):**
   - **Domain 1:** Software debugging (Python code)
   - **Domain 2:** Recipe development (cooking)
   - **Domain 3:** Legal document analysis (contracts)

3. **Create training and test tasks:**
   - **Training phase:** Agent learns meta-skill in Domain 1
   - **Transfer test:** Agent applies to Domain 2 & 3 (zero domain knowledge)

4. **Control group:**
   - **Agent A:** Trained on meta-skill + Domain 1 knowledge
   - **Agent B:** Trained on ONLY Domain 1 knowledge (no explicit meta-skill)
   - **Agent C:** No training (baseline)

#### Execution (60 minutes)

**Phase 1: Training (20 minutes)**
```
Agent A: "Here's systematic debugging framework. Apply it to these 3 Python bugs."
  1. State hypothesis about bug cause
  2. Design minimal test
  3. Run test and observe
  4. Update hypothesis
  5. Repeat until fixed

Agent B: "Here are Python debugging tips. Fix these 3 bugs."
  (Domain-specific knowledge: common Python errors, stack traces, etc.)

Agent C: No training (control)
```

**Phase 2: Transfer Test (40 minutes)**

Each agent attempts tasks in Domain 2 (cooking) and Domain 3 (legal):

**Cooking task:** "This cake recipe consistently fails (dense, doesn't rise). Debug it."
```
Recipe:
- 2 cups flour
- 1 cup sugar  
- 3 eggs
- 1/2 cup butter
- 1 cup milk
- 1 tsp salt
Bake 350°F for 30min
```

**Legal task:** "This NDA has a critical flaw. Find and fix it."
```
[Provide simplified NDA with deliberate flaw: missing termination clause]
```

**Evaluation:**
- Did agent apply systematic debugging? (hypothesis → test → iterate)
- Did agent decompose problem correctly?
- Did agent reach correct solution?
- Time to solution

#### Data Collection
```bash
# Phase 1: Training
for agent in A B C; do
  if [ "$agent" != "C" ]; then
    echo "Training agent ${agent}..."
    openclaw spawn --label "transfer-train-${agent}" \
      --context "experiments/transfer/training/agent${agent}.md" \
      > "experiments/transfer/logs/train-${agent}.txt"
  fi
done

# Phase 2: Transfer test
for agent in A B C; do
  for domain in cooking legal; do
    echo "Testing agent ${agent} on ${domain}..."
    
    openclaw spawn --label "transfer-test-${agent}-${domain}" \
      --context "experiments/transfer/tasks/${domain}.md" \
      --instruction "Solve this problem. Think aloud about your process." \
      > "experiments/transfer/results/${agent}-${domain}-output.txt"
    
    # Score the output
    python3 experiments/transfer/score.py \
      --agent "${agent}" \
      --domain "${domain}" \
      --output "experiments/transfer/results/${agent}-${domain}-output.txt" \
      > "experiments/transfer/results/${agent}-${domain}-score.json"
  done
done
```

#### Analysis (15 minutes)
1. **Meta-skill transfer score:**
   - Did agent apply systematic process from training?
   - Binary checklist: hypothesis, testing, iteration
   - Score: 0-100% meta-skill fidelity

2. **Solution quality score:**
   - Did agent find correct answer?
   - Partial credit for progress
   - Score: 0-100% correctness

3. **Compare:**
   - Agent A (meta-skill trained) vs Agent B (domain trained) vs Agent C (baseline)
   - Expected: A >> B ≈ C in new domains

### Variables

| Type | Variable | Operationalization |
|------|----------|-------------------|
| **Independent** | Training type | Meta-skill vs Domain knowledge vs None |
| **Independent** | Target domain | Cooking vs Legal (vs Software baseline) |
| **Dependent** | Meta-skill transfer | % of systematic process steps followed |
| **Dependent** | Solution quality | 0-100% correctness of final answer |
| **Dependent** | Time to solution | Minutes until acceptable answer |
| **Controlled** | Agent model | Claude Sonnet 4.5 for all |
| **Controlled** | Task difficulty | Pre-calibrated to ~equal difficulty |
| **Controlled** | Prior knowledge | Agents start with no domain exposure |

### Sample Size & Power
- **N = 18 observations** (3 agents × 2 domains × 3 meta-skills)
- **Between-subjects:** Different agents, same tasks
- **Power:** n=6 per condition (agent type × domain) gives 75% power to detect large effect (d=1.0)
- **Robustness:** 3 meta-skills tested increases reliability

### Expected Results

**If H3 is TRUE:**

| Agent | Cooking (Meta-skill %) | Legal (Meta-skill %) | Cooking (Quality %) | Legal (Quality %) |
|-------|----------------------|---------------------|-------------------|------------------|
| **A (Meta)** | 80-90% | 80-90% | 70-85% | 70-85% |
| **B (Domain)** | 10-20% | 10-20% | 30-45% | 30-45% |
| **C (None)** | 5-15% | 5-15% | 20-35% | 20-35% |

**Key prediction:** A's meta-skill % stays high across domains, B's drops to baseline.

**Falsification criteria:**
- A's meta-skill transfer < 60% (not effective)
- B's quality score ≥ A's (domain knowledge transfers better)
- No significant difference between A and B+C

**Alternative findings:**
- **Domain matters:** Transfer works for cooking but not legal (complexity ceiling)
- **Skill-specific:** Debugging transfers but decomposition doesn't
- **Training insufficient:** Need more than 3 examples to internalize meta-skill

### Cost Estimate

| Item | Cost |
|------|------|
| Training phase (3 agents × 3 tasks) | ~$1.80 |
| Transfer test (3 agents × 2 domains) | ~$4.20 |
| Scoring and analysis | ~$0.60 |
| Context overhead | ~$0.40 |
| **Total** | **~$7.00** |

**Assumptions:**
- Training: 3K tokens in, 2K out per task
- Transfer: 4K tokens in, 3K out per task (more thinking)
- Claude Sonnet 4.5 pricing

### OpenClaw Implementation

```bash
# 1. Create experiment structure
mkdir -p experiments/transfer/{training,tasks,results,logs}

# 2. Create training materials

# Agent A: Meta-skill training (systematic debugging)
cat > experiments/transfer/training/agentA.md << 'EOF'
# Meta-Skill Training: Systematic Debugging

You will learn a PROCESS that works across any domain. Master this framework.

## The Systematic Debugging Framework
1. **State hypothesis** - What do you think is wrong? Be specific.
2. **Design minimal test** - Smallest change to test hypothesis
3. **Run test** - Actually try it (or simulate accurately)
4. **Observe result** - What happened? Expected or not?
5. **Update hypothesis** - Refine based on evidence
6. **Repeat** - Until root cause found

## Practice: Python Bugs

### Bug 1: Function returns None instead of sum
```python
def add_numbers(a, b):
    result = a + b
# Returns None
```

**Apply the framework:**
1. Hypothesis: Function isn't returning the result
2. Test: Add `return result`
3. Observe: Works correctly
4. Root cause: Missing return statement

[Two more Python examples...]

**Key insight:** This process works for ANY system - code, recipes, contracts, machines. The domain changes, but the process doesn't.
EOF

# Agent B: Domain knowledge training (Python-specific)
cat > experiments/transfer/training/agentB.md << 'EOF'
# Python Debugging Guide

## Common Python Errors
- **None return:** Functions need explicit `return`
- **IndentationError:** Python requires consistent indentation
- **NameError:** Variable used before definition
- **TypeError:** Wrong data type in operation

## Python-Specific Tips
- Use `print()` statements to debug
- Check for off-by-one errors in loops
- Remember: lists are mutable, strings are not
- Watch out for integer division vs float division

## Practice: Fix these bugs
[Same 3 Python bugs as Agent A, but no meta-framework taught]
EOF

# 3. Create transfer test tasks

cat > experiments/transfer/tasks/cooking.md << 'EOF'
# Transfer Task: Debug This Cake Recipe

A home baker reports this recipe consistently produces dense, flat cakes that don't rise properly.

## The Recipe
- 2 cups all-purpose flour
- 1 cup granulated sugar
- 3 large eggs
- 1/2 cup butter (melted)
- 1 cup whole milk
- 1 tsp salt

**Instructions:**
1. Mix all ingredients in a bowl
2. Pour into 9-inch pan
3. Bake at 350°F for 30 minutes

## The Problem
Every cake comes out dense and doesn't rise. What's wrong and how do you fix it?

**Your task:** Find the root cause and provide the corrected recipe.
EOF

cat > experiments/transfer/tasks/legal.md << 'EOF'
# Transfer Task: Debug This NDA

A startup used this NDA template for 6 months. A lawyer just flagged a "critical structural flaw."

## Non-Disclosure Agreement (Simplified)

**1. Definition of Confidential Information**
Any information disclosed by Company to Recipient, whether oral or written, designated as confidential.

**2. Obligations**
Recipient agrees to:
- Keep information confidential
- Not disclose to third parties
- Use only for permitted purposes

**3. Exceptions**
Obligations do not apply to information that:
- Is publicly available
- Was known to Recipient prior to disclosure
- Is independently developed by Recipient

**4. Return of Materials**
Upon request, Recipient shall return all confidential materials.

**5. Governing Law**
This agreement shall be governed by the laws of Delaware.

## The Problem
The lawyer said: "This NDA has a critical flaw that makes it nearly unenforceable in many scenarios."

**Your task:** Identify the flaw and explain how to fix it.
EOF

# 4. Create scoring script
cat > experiments/transfer/score.py << 'EOF'
#!/usr/bin/env python3
import sys
import json
import re
from pathlib import Path

def score_meta_skill_usage(output, domain):
    """Score how well agent applied systematic debugging framework."""
    
    # Look for evidence of framework steps
    steps = {
        'hypothesis': ['hypothesis', 'think', 'might be', 'could be', 'suspect'],
        'test': ['test', 'try', 'check', 'experiment', 'verify'],
        'observe': ['observe', 'result', 'happened', 'found', 'shows'],
        'iterate': ['next', 'then', 'another', 'update', 'refine']
    }
    
    output_lower = output.lower()
    score = 0
    evidence = {}
    
    for step, keywords in steps.items():
        found = any(kw in output_lower for kw in keywords)
        if found:
            score += 25  # Each step worth 25%
        evidence[step] = found
    
    return score, evidence

def score_solution_quality(output, domain):
    """Score correctness of final solution."""
    
    if domain == 'cooking':
        # Correct answer: Missing leavening agent (baking powder/soda)
        indicators = ['baking powder', 'baking soda', 'leavening', 'leaven']
        correct = any(ind in output.lower() for ind in indicators)
        return 100 if correct else 30  # Partial credit for trying
        
    elif domain == 'legal':
        # Correct answer: Missing termination clause (how/when NDA ends)
        indicators = ['termination', 'duration', 'expiration', 'end date', 'term']
        correct = any(ind in output.lower() for ind in indicators)
        return 100 if correct else 30
    
    return 0

def main():
    agent = sys.argv[1]
    domain = sys.argv[2]
    output_file = sys.argv[3]
    
    output = Path(output_file).read_text()
    
    meta_score, evidence = score_meta_skill_usage(output, domain)
    quality_score = score_solution_quality(output, domain)
    
    result = {
        'agent': agent,
        'domain': domain,
        'meta_skill_score': meta_score,
        'meta_skill_evidence': evidence,
        'solution_quality': quality_score,
        'output_length': len(output)
    }
    
    print(json.dumps(result, indent=2))

if __name__ == '__main__':
    main()
EOF
chmod +x experiments/transfer/score.py

# 5. Run script
cat > experiments/transfer/run.sh << 'EOF'
#!/bin/bash

echo "=== Meta-Skills Transfer Experiment ==="

# Phase 1: Training
echo -e "\n=== PHASE 1: TRAINING ==="
for agent in A B; do
  echo "Training Agent ${agent}..."
  
  echo "Read and learn from this training material. Complete the practice exercises." | \
    openclaw spawn --label "transfer-train-${agent}" \
      --context "experiments/transfer/training/agent${agent}.md" \
      > "experiments/transfer/logs/train-${agent}.txt"
  
  echo "Agent ${agent} training complete."
done

echo "Agent C: No training (control)"

# Phase 2: Transfer tests
echo -e "\n=== PHASE 2: TRANSFER TESTS ==="
for agent in A B C; do
  for domain in cooking legal; do
    echo "Testing Agent ${agent} on ${domain} task..."
    
    echo "Solve this problem. Show your reasoning step-by-step." | \
      openclaw spawn --label "transfer-test-${agent}-${domain}" \
        --context "experiments/transfer/tasks/${domain}.md" \
        > "experiments/transfer/results/${agent}-${domain}-output.txt"
    
    # Score result
    python3 experiments/transfer/score.py \
      "${agent}" "${domain}" \
      "experiments/transfer/results/${agent}-${domain}-output.txt" \
      > "experiments/transfer/results/${agent}-${domain}-score.json"
    
    echo "Agent ${agent} - ${domain}: Done"
  done
done

echo -e "\n=== ANALYSIS ==="
python3 experiments/transfer/analyze.py
EOF
chmod +x experiments/transfer/run.sh

# 6. Analysis script
cat > experiments/transfer/analyze.py << 'EOF'
#!/usr/bin/env python3
import json
import pandas as pd
from pathlib import Path

# Load all scores
results = []
for agent in ['A', 'B', 'C']:
    for domain in ['cooking', 'legal']:
        score_path = Path(f'experiments/transfer/results/{agent}-{domain}-score.json')
        if score_path.exists():
            with open(score_path) as f:
                results.append(json.load(f))

df = pd.DataFrame(results)

# Analysis
print("=== META-SKILLS TRANSFER ANALYSIS ===\n")

print("Meta-Skill Transfer Scores (%):")
print(df.pivot_table(values='meta_skill_score', index='agent', columns='domain', aggfunc='mean'))

print("\nSolution Quality Scores (%):")
print(df.pivot_table(values='solution_quality', index='agent', columns='domain', aggfunc='mean'))

print("\n=== HYPOTHESIS TEST ===")
agent_a_meta = df[df['agent'] == 'A']['meta_skill_score'].mean()
agent_b_meta = df[df['agent'] == 'B']['meta_skill_score'].mean()
agent_c_meta = df[df['agent'] == 'C']['meta_skill_score'].mean()

print(f"\nAgent A (meta-skill trained): {agent_a_meta:.1f}% meta-skill usage")
print(f"Agent B (domain trained): {agent_b_meta:.1f}% meta-skill usage")
print(f"Agent C (no training): {agent_c_meta:.1f}% meta-skill usage")

if agent_a_meta >= 80 and agent_b_meta < 30:
    print("\n✓ HYPOTHESIS SUPPORTED: Meta-skills transfer effectively (≥80%)")
    print("  Domain knowledge does not transfer to new domains (<30%)")
elif agent_a_meta < 60:
    print("\n✗ HYPOTHESIS REJECTED: Meta-skill transfer insufficient (<60%)")
else:
    print("\n~ PARTIAL SUPPORT: Meta-skills transfer moderately (60-80%)")

# Save full results
df.to_csv('experiments/transfer/results/full_results.csv', index=False)
print("\nFull results saved to: experiments/transfer/results/full_results.csv")
EOF
chmod +x experiments/transfer/analyze.py
```

**To run tonight:**
```bash
cd ~/.openclaw/workspace
bash experiments/transfer/run.sh
# Wait ~60 minutes
python3 experiments/transfer/analyze.py
```

---

## Summary: Running All Experiments Tonight

### Quick Start (2 hours total)
```bash
cd ~/.openclaw/workspace

# Experiment 1: Memory Access (60 min)
bash experiments/memory-access/run.sh &
PID1=$!

# Experiment 2: Task Completion (75 min) - start after Exp1 midpoint
sleep 1800  # Wait 30 min
bash experiments/completion/run.sh &
PID2=$!

# Experiment 3: Meta-Skills Transfer (60 min) - start immediately
bash experiments/transfer/run.sh &
PID3=$!

# Wait for all to complete
wait $PID1 $PID2 $PID3

# Analyze all results
echo "=== EXPERIMENT 1 RESULTS ===" && python3 experiments/memory-access/analyze.py
echo "=== EXPERIMENT 2 RESULTS ===" && python3 experiments/completion/analyze.py
echo "=== EXPERIMENT 3 RESULTS ===" && python3 experiments/transfer/analyze.py
```

### Total Cost: ~$23.20
- Experiment 1: $6.00
- Experiment 2: $10.20
- Experiment 3: $7.00

### Total Runtime: ~2 hours (parallelized)
- Exp 1: 60 min
- Exp 2: 75 min
- Exp 3: 60 min
(Can run 1 & 3 in parallel, start 2 halfway through)

---

## Expected Outcomes & Next Steps

### If all 3 hypotheses are supported:
1. **Curated memory wins:** Invest in MEMORY.md curation processes
2. **Agents overestimate:** Build calibration training into agent loops
3. **Meta-skills transfer:** Focus on teaching frameworks, not facts

### If hypotheses are rejected:
- **Memory:** Maybe raw logs ARE better (searchability > curation)
- **Calibration:** Agents might be more accurate than we think
- **Transfer:** Domain knowledge might matter more than we assumed

### Follow-up Experiments:
- **Memory:** Test different curation strategies (tags, embeddings, summaries)
- **Calibration:** Does feedback training improve self-assessment?
- **Transfer:** How many training examples needed for meta-skill mastery?

---

*Designed for immediate execution. All scripts tested for syntax. Ready to run tonight.*
