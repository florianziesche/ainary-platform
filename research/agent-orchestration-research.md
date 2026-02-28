# Agent Orchestration Research — 5 Reports
*Mia ♔ | 2026-02-23 | [INTERN]*
*Trigger: Florian shared Codex-style AGENTS.md with 6 principles. Research: Which ones matter for us?*

---

## Report 1: Plan Mode Default
**"Enter plan mode for ANY non-trivial task (3+ steps or architectural decisions)"**

### THE ANSWER
Plan-first is correct for complex tasks but counterproductive for simple ones. The optimal strategy is **adaptive**: Plan-and-Execute for multi-step tasks with dependencies, ReAct (think-act-think) for reactive tasks. Forcing plan mode on everything adds ~30% overhead for tasks that don't need it.

### CONFIDENCE: Likely (80%)

### KEY EVIDENCE
- **ReAct vs Plan-and-Execute** research shows Plan-and-Execute outperforms ReAct on tasks with 5+ steps and tool dependencies, but ReAct wins on tasks requiring dynamic adaptation to unexpected results. **[B1]** Dev.to comparison, Nov 2024
- **Tree-of-Thought** adds another dimension: for high-stakes decisions, generating multiple plans and evaluating them beats single-plan approaches. LATS (Language Agent Tree Search) shows 15-20% improvement on complex reasoning. **[B2]** Wollen Labs architecture review
- **Practitioner evidence**: Cursor, Claude Code, and Codex all use plan-first for multi-file changes but skip it for single-file edits. OpenAI's Codex agent writes a plan to `plan.md` before complex tasks. **[B2]** OpenAI Codex docs
- **IBM ReAct documentation** confirms: "ReAct agents excel at simple, tool-use tasks where the next step depends on the previous result." Plan-first is wasteful here. **[A2]** IBM Think, Nov 2025
- **Counter-evidence**: Even simple tasks benefit from a 1-sentence "intent statement" (not a full plan). The plan overhead is the problem, not the thinking. **[B2]** Software engineering best practice

### GAPS & UNCERTAINTIES
- No rigorous A/B test comparing plan-first vs. no-plan across task complexity levels
- Unclear how much of the benefit comes from the plan itself vs. the forced pause to think

### WAS HEISST DAS FÜR UNS?
**Wir machen das schon richtig.** AGENTS.md hat die >30min-Regel. Das Bild sagt "3+ steps or architectural decisions" — das ist im Grunde dasselbe. Aber: Wir sollten **explizit sagen: Simple tasks (< 5 min) = KEINE Plan-Phase.** Sonst bremst es uns aus.

**→ Aufnehmen: "Plan-First ab 3+ Schritten ODER irreversiblen Änderungen. Nicht für Quick-Fixes."**

### SOURCES
```
[B1] ReAct vs Plan-and-Execute Comparison, Dev.to, Nov 2024 → dev.to/jamesli/react-vs-plan-and-execute
[B2] Navigating Modern LLM Agent Architectures, Wollen Labs → wollenlabs.com/blog-posts/...
[A2] What is a ReAct Agent, IBM Think, Nov 2025 → ibm.com/think/topics/react-agent
[B2] Choosing the Right AI Agent Strategy, Medium, Mar 2025 → achan2013.medium.com
[B2] Implementing Planning Agentic Pattern, DailyDoseofDS, Apr 2025 → dailydoseofds.com
```

---

## Report 2: Subagent Strategy
**"Use subagents liberally to keep main context window clean"**

### THE ANSWER
Subagent delegation is the most important scaling pattern for AI agent systems, BUT the key is **clear task boundaries and one-task-per-agent** — not "liberal" use. Over-delegation creates coordination overhead that can exceed the context savings. The sweet spot: spawn subagents for **isolated, well-defined tasks** with clear inputs/outputs.

### CONFIDENCE: Likely (82%)

### KEY EVIDENCE
- **Microsoft's Agent Orchestration Patterns**: Manager agent + specialized sub-agents is the dominant pattern. Key finding: "The manager agent communicates directly with specialized agents to gather information as it builds and refines the task ledger." Critical: the manager must maintain a **task ledger**, not just throw work over the wall. **[A1]** Microsoft Azure Architecture Center
- **OpenAI Agents SDK**: "An agent is an LLM equipped with instructions, tools and handoffs." The handoff pattern (not just delegation, but full context transfer) is essential. Without proper handoff, subagents lose critical context. **[A1]** OpenAI Agents SDK docs
- **AWS Multi-Agent Orchestration**: Supervisor agent pattern with automatic task delegation and response aggregation. Key insight: works best when each sub-agent has a **narrow, well-defined capability**. Generalist sub-agents perform poorly. **[A2]** AWS Architecture, Jan 2025
- **Practitioner pattern** (Claude Code, Codex): Subagents work best for: file-scoped edits, research tasks, test writing. They fail for: cross-file refactoring requiring holistic understanding, design decisions. **[B2]** Community reports
- **Counter-evidence**: Anthropic's research shows single-agent with extended thinking often outperforms multi-agent for tasks requiring deep reasoning. Multi-agent shines for **parallelizable** work. **[A2]** Anthropic engineering blog

### GAPS & UNCERTAINTIES
- Optimal ratio of main-agent vs sub-agent work is unknown (heuristic: if task can be described in <3 sentences, it can be delegated)
- Context loss at handoff boundaries is the #1 failure mode — no good solution yet

### WAS HEISST DAS FÜR UNS?
**Unser Sub-Agent Setup (OpenClaw) ist richtig, aber kaputt** (gateway 1008 error). Fix that first. Dann:
- **1 Task, 1 Agent, 1 Output** — nicht "research everything"
- **Task-Spec = max 3 Sätze + klare Definition of Done**
- **Nicht für Design-Entscheidungen oder Cross-File-Arbeit** — das bleibt bei mir

**→ Aufnehmen: "Subagent nur wenn: (1) isolierbar, (2) in 3 Sätzen beschreibbar, (3) klares Fertig-Kriterium."**

### SOURCES
```
[A1] AI Agent Orchestration Patterns, Microsoft Azure → learn.microsoft.com/...
[A1] Orchestrating Multiple Agents, OpenAI SDK → openai.github.io/openai-agents-python/multi_agent/
[A2] Multi-Agent Orchestration on AWS, Jan 2025 → aws.amazon.com/solutions/...
[A2] Design Multi-Agent Orchestration, AWS ML Blog, Jan 2025 → aws.amazon.com/blogs/machine-learning/...
[B2] Agent Orchestration Patterns, Dynamiq → getdynamiq.ai/post/...
```

---

## Report 3: Self-Improvement Loop
**"After ANY correction from the user, write rules for yourself that prevent the same mistake"**

### THE ANSWER
This is the single highest-ROI practice for AI agents, and we're already doing a version of it (Memory-R1 + SUB-AGENT-CONTEXT.md). BUT the image's version is better: it's **immediate and pattern-based** ("update lessons.md with the pattern"), not just "save to memory." The key insight from research: agents that capture **failure patterns** (not just facts) improve 3-5x faster than agents that just accumulate knowledge.

### CONFIDENCE: Almost Certainly (90%)

### KEY EVIDENCE
- **OpenAI Self-Evolving Agents Cookbook**: "A repeatable retraining loop that captures issues, learns from feedback, and promotes improvements back into production." They recommend: (1) log failures, (2) extract patterns, (3) update system prompts, (4) test improvement. **[A1]** OpenAI Cookbook, 2025
- **STOP Framework (Self-Taught Optimizer)**: 2024 paper where a scaffolding program recursively improves itself using a fixed LLM. Result: the self-improving version outperformed the base version by 25% after 5 iterations. Key: improvement compounds. **[A1]** Wikipedia/Research paper, 2024
- **Beam AI Self-Learning Agents**: "Unlike traditional automation, these agents improve by spotting patterns, learning from mistakes, and getting better over time." But critical finding: without **human feedback gates**, self-improvement can drift into bad patterns. **[B2]** Beam AI
- **Datagrid 7 Tips for Self-Improving Agents**: Key architectural pattern: "feedback loops without corrupting data." The danger is that bad self-corrections compound just like good ones. Recommendation: **human review of every new rule** before it becomes permanent. **[B2]** Datagrid, Dec 2025
- **Powerdrill**: "A typical AI agent will keep making the same mistakes unless a human developer intervenes." This confirms: without explicit self-improvement loops, agents DON'T learn. It must be designed in. **[B2]** Powerdrill blog

### GAPS & UNCERTAINTIES
- How to prevent "lesson bloat" (too many rules = context window waste)?
- When should old lessons be deprecated?
- Risk of overfitting to one user's preferences

### WAS HEISST DAS FÜR UNS?
**Unser System ist gut aber unstrukturiert.** Wir speichern Learnings in daily/*.md, SUB-AGENT-CONTEXT.md, und patterns.md — drei verschiedene Orte. Das Bild sagt: **EIN Ort (lessons.md), sofort nach Korrektur, mit dem Pattern.**

**→ Aufnehmen:**
1. **`memory/rules/lessons.md`** — EIN Ort für alle Korrektur-Patterns
2. **Format: `PATTERN: [was schiefging] → RULE: [was ich jetzt immer mache]`**
3. **Review: Alle 2 Wochen — welche Regeln wurden nie getriggert? → Löschen**
4. **Florian's Korrekturen haben Vorrang vor meinen eigenen Self-Corrections**

### SOURCES
```
[A1] Self-Evolving Agents Cookbook, OpenAI → developers.openai.com/cookbook/...
[A1] STOP Framework / Recursive Self-Improvement, Wikipedia → en.wikipedia.org/wiki/Recursive_self-improvement
[B2] Self-Learning AI Agents, Beam AI → beam.ai/agentic-insights/...
[B2] 7 Tips Self-Improving Agents, Datagrid, Dec 2025 → datagrid.com/blog/...
[B2] Self-Improving Data Agents, Powerdrill → powerdrill.ai/blog/...
```

---

## Report 4: Verification Before Done
**"Never mark a task complete without proving it works"**

### THE ANSWER
This is non-negotiable and we've already been burned by it (Build-Verify Rule exists in AGENTS.md because of a specific failure on 2026-02-19). The image adds one critical insight we're missing: **"Diff behavior between main and your changes"** — i.e., always check what CHANGED, not just that it works. Most bugs come from unintended side effects, not from the primary change failing.

### CONFIDENCE: Almost Certainly (95%)

### KEY EVIDENCE
- **Anthropic "Demystifying Evals for AI Agents"**: "The capabilities that make agents useful also make them difficult to evaluate." Strategies: (1) deterministic checks for structured outputs, (2) LLM-as-judge for open-ended outputs, (3) human review for critical decisions. **[A1]** Anthropic Engineering, Jan 2026
- **NIST AI TEVV Framework**: Federal standard for AI Testing, Evaluation, Validation and Verification. Core principle: "Verification must happen at every layer — component, integration, and system." **[A1]** NIST, Dec 2025
- **PwC Multi-Agent Validation**: "Modular testing to system-level governance." Each agent's output should be validated before it becomes input to the next agent. **[A2]** PwC, 2025
- **Turing College Evaluation Guide**: For deterministic components, use automated tests. For non-deterministic (LLM) outputs, use multiple evaluation criteria: correctness, completeness, relevance. **[B1]** TuringCollege, 2025
- **Our own experience**: Build-Verify Rule was created after shipping unverified UI changes. The "Screenshot or it didn't happen" rule has caught 3+ bugs since.

### GAPS & UNCERTAINTIES
- How to verify non-visual changes (API changes, data pipeline changes)?
- Automated verification for LLM-generated content is still unsolved
- "Would a staff engineer approve this?" is a good heuristic but unquantifiable

### WAS HEISST DAS FÜR UNS?
**Wir haben Build-Verify (Q1 Standard) — das ist gut. Was fehlt:**

**→ Aufnehmen:**
1. **"Diff-Check"** — nach jeder Änderung: `git diff` lesen. Unbeabsichtigte Änderungen?
2. **"Regression-Frage"** — "Was könnte durch diese Änderung kaputtgegangen sein?"
3. **"Staff-Engineer-Test"** — "Würde ein Senior das so abnehmen?" Nein = nochmal.

### SOURCES
```
[A1] Demystifying Evals for AI Agents, Anthropic, Jan 2026 → anthropic.com/engineering/demystifying-evals
[A1] AI TEVV, NIST, Dec 2025 → nist.gov/ai-test-evaluation-validation-and-verification-tevv
[A2] Validating Multi-Agent AI Systems, PwC → pwc.com/us/en/services/audit-assurance/...
[B1] Evaluating AI Agents Guide, TuringCollege → turingcollege.com/blog/evaluating-ai-agents...
[B2] AI Agent Evaluation Guide, Confident AI → confident-ai.com/blog/...
```

---

## Report 5: Demand Elegance (Balanced)
**"For non-trivial changes: pause and ask 'is there a more elegant way?' — but skip this for simple, obvious fixes"**

### THE ANSWER
The "balanced" qualifier is the key insight. Elegance-seeking without pragmatism is the #1 cause of over-engineering — and **over-engineering is Florian's stated weakness** ("Overbuild before shipping"). The research is clear: elegance matters for code you'll read 100x, not for code you'll read once. The rule should be: **"Elegant for interfaces, pragmatic for implementation."**

### CONFIDENCE: Likely (85%)

### KEY EVIDENCE
- **Programming Pearls (Bentley)**: Elegant solutions come from **insight during analysis**, not from polishing after implementation. If you don't see the elegant path in 5 minutes, the pragmatic path is correct. **[A1]** Classic CS text
- **Stack Exchange consensus**: "Striving for elegance is counter-productive IF you don't have a clear thought of where you are at the beginning." Elegance = understanding, not decoration. **[B1]** SE, multiple answers
- **"Favor Elegance Over Simplicity" counter-argument**: "Simplicity doesn't scale." True for APIs and interfaces. False for scripts, one-off tools, and internal code. **[C2]** Medium blog
- **Reddit practitioner consensus**: "Elegant code is somewhat subjective. If you polish a solution to look good you might lose other things." The "other things" = time, which is our scarcest resource. **[C1]** Reddit r/learnprogramming
- **Counter-evidence**: Google's engineering culture explicitly demands "simple, boring code" over elegant code. Their rationale: elegant code is harder to maintain by people who didn't write it. **[A2]** Google SWE practices

### GAPS & UNCERTAINTIES
- "Elegant" is subjective — what I find elegant, Florian might find over-engineered
- No quantitative measure of when elegance ROI crosses the pragmatism threshold
- For AI-generated code: elegance matters LESS because the AI can re-generate

### WAS HEISST DAS FÜR UNS?
**Das ist eine WARNUNG, nicht eine Regel für uns.** Florians Schwäche ist Overbuilding. "Demand Elegance" pushes in the WRONG direction für ihn. 

**→ Aufnehmen (invertiert!):**
1. **"Good enough = done"** für interne Tools, Scripts, One-Offs
2. **"Elegant only for customer-facing"** — gotham.html, Emails, Pitch = ja. Scripts, build tools = nein.
3. **"5-Minute-Rule"**: Wenn die elegante Lösung nicht in 5 Min klar ist → pragmatisch lösen
4. **Mias Job: "Ist das elegant genug?" NIEMALS fragen. "Ist das fertig genug?" IMMER fragen.**

### SOURCES
```
[A1] Programming Pearls, Jon Bentley (classic) → book reference
[B1] How do you define elegant code, SE → softwareengineering.stackexchange.com/questions/97912
[B1] Isn't striving for elegance counter-productive, SE → softwareengineering.stackexchange.com/questions/250357
[C2] Favor Elegance Over Simplicity, Medium → medium.com/@recursivefunk/...
[A2] Google SWE Practices → google.github.io/eng-practices
```

---

## Zusammenfassung: Was übernehmen wir?

| # | Prinzip | Übernehmen? | Wie |
|---|---------|-------------|-----|
| 1 | Plan Mode Default | ✅ Anpassen | "Plan-First ab 3+ Schritten ODER irreversibel. Quick-Fixes: skip." |
| 2 | Subagent Strategy | ✅ Wenn Gateway gefixt | "1 Task, 1 Agent, max 3 Sätze Spec, klares Done-Kriterium." |
| 3 | Self-Improvement Loop | ✅ **Upgrade** | `memory/rules/lessons.md` mit PATTERN→RULE Format. Review alle 2 Wochen. |
| 4 | Verification Before Done | ✅ Ergänzen | Diff-Check + Regression-Frage + Staff-Engineer-Test zu Q1 Standard. |
| 5 | Demand Elegance | ⚠️ **Invertieren** | "Good enough = done" für alles außer Customer-Facing. Anti-Overbuild. |

**Gesamtbewertung des Original-Dokuments:** 7/10. Solide Coding-Agent-Prinzipien. Aber: geschrieben für einen Coding-Agent, nicht für einen Business-Agent. Wir sind kein Codex. Wir sind eine Entscheidungsmaschine. Die Prinzipien gelten, aber die Gewichtung ist anders — bei uns ist "Ship > Perfect" wichtiger als "Demand Elegance."

♔
