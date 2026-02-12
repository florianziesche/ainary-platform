# Output Delivery Rules - Procedural Memory

**Purpose:** How to deliver outputs to Florian effectively (process knowledge)

---

## Core Principles

1. **Path/Link Always:** Every output includes full file path or URL
2. **Context First:** Explain WHAT it is and WHY it matters before sharing
3. **Options > Solutions:** Give 2-3 choices when strategic, decide when tactical (>90% confidence)
4. **Quality Score Yourself:** A/B/C/? after major deliverables
5. **Ask for Feedback:** On important outputs, explicitly ask "Does this work for you?"

---

## Before Any Output

### Pre-Delivery Checklist

**From `standards/checklists/before-any-output.md` (when it exists):**

- [ ] **Audience Tag Present?** `[KUNDE]` `[LP/VC]` `[PUBLIC]` `[INTERN]`
- [ ] **Source All Facts?** Numbers/claims have `[Source: ...]` citations
- [ ] **File Path Ready?** Full path to share: `/Users/florianziesche/...`
- [ ] **Context Prepared?** One-sentence "what this is and why it matters"
- [ ] **Quality Self-Score?** A/B/C/? prediction before delivery

**Every 3 edits to a document:**
- [ ] Same audience as intended?
- [ ] Same message as Florian would write?

---

## Output Format by Type

### 1. Code/Features (HTML, JavaScript, etc.)

**Format:**
```
✅ [Feature Name] Complete

What: [One sentence description]
Location: /full/path/to/file.html
Size: XXX KB

Key Features:
- Feature 1
- Feature 2
- Feature 3

Status: [Ready to demo / Needs testing / Draft]
Confidence: [75-95%]
```

**Example:**
```
✅ CNC Planner v19 Complete

What: Presentation-ready demo with AI recommendations, risk analysis, and PDF export
Location: /Users/florianziesche/Projects/cnc-planner/cnc-v19-demo.html
Size: 393 KB

Key Features:
- Prüfprotokoll with 8 intelligent questions
- Pricing insights panel (customer tier, risk premium)
- Change tracking protocol
- Risikoanalyse PDF generator
- 11 operations for Lagerungstraverse (661 min calculated)

Status: Ready to present (you said "Schaut gut aus. Ich stelle es vor")
Confidence: 90% (based on your feedback)
```

---

### 2. Reports/Documents (PDF, LaTeX, Markdown)

**Format:**
```
📄 [Report Name]

What: [Purpose in one sentence]
Format: [PDF/LaTeX/Markdown]
Pages: X
Location: /full/path/to/file.pdf

Key Sections:
- Section 1
- Section 2
- Section 3

Audience: [KUNDE/LP/INTERN/PUBLIC]
Status: [Final / Draft / Review needed]
```

**Example:**
```
📄 Risikoanalyse Lagerungstraverse

What: 16-page risk analysis for Andreas Brand (MBS) covering cost scenarios, decision matrix, and "Why CNC Planner Pro"
Format: LaTeX PDF
Pages: 16
Location: ~/Desktop/Risikoanalyse-Lagerungstraverse-v2.pdf

Key Sections:
- Risk Matrix (TikZ visualization)
- 3 Pricing Scenarios (€14,200 - €26,800)
- Complete Fertigungsanweisung (11 operations)
- Roadmap & Workflow diagrams

Audience: [KUNDE] - Andreas Brand @ MBS
Status: Final, sent via Telegram
```

---

### 3. Research/Analysis (Long-form)

**For reports >10 pages:**

**Format:**
```
🔬 [Research Topic]

Executive Summary:
[3-5 bullet points of key findings]

Full Report: [Length]
Location: /full/path/to/file.md

Want the full deep dive? [Yes/No question]
```

**Example:**
```
🔬 SOTA Paper Deep Dive (Top 3 Agent Papers)

Executive Summary:
- Single Agent + Skills > Multi-Agent until ~50-90 skill threshold
- Γ-Metric measures real collaboration value (Γ > 1 = sub-agents help)
- Memory layers (episodic/semantic/procedural) differentiate agents
- Manufacturing AI is massively under-researched (gap = opportunity)
- Constitutional AI for CNC: embed REFA rules as self-checks

Full Report: 12,000 words
Location: /Users/florianziesche/.openclaw/workspace/memory/sota-research/2026-02-10-deep-dive.md

Want the full deep dive or is the summary enough?
```

---

### 4. Email Drafts

**Format:**
```
✉️ Email Draft: [Recipient]

Subject: [Subject line]
Tone: [Professional / Casual / Persuasive]
Length: [X words]

Location: /full/path/to/draft.md

Key Points:
- Point 1
- Point 2
- Point 3

Ready to send or need edits?
```

**Example:**
```
✉️ Email Draft: Andreas Brand (Praxistest)

Subject: CNC Planner Pro - Bereit für echten Praxistest
Tone: Professional but friendly (family relation)
Length: 320 words

Location: /Users/florianziesche/Projects/cnc-planner/email-andreas-praxistest.md

Key Points:
- Thanks for positive feedback
- Demo video attached (you recorded today)
- Ready for real calculation with Lagerungstraverse
- Two options: full integration or parallel test

Ready to send after you review tonight?
```

---

### 5. System Changes (Configs, Installations)

**Format:**
```
⚙️ [System Change]

What Changed: [Description]
Location: [Path or system component]
Impact: [What this enables/fixes]

Status: [Active / Needs restart / Test needed]
Rollback: [How to undo if needed]
```

**Example:**
```
⚙️ Smart Connections v4.1.8 Installed

What Changed: Obsidian plugin for semantic search across vault
Location: ~/Library/Mobile Documents/iCloud~md~obsidian/.../community-plugins/
Impact: You can now search vault by meaning, not just keywords

Status: Active (you opened Obsidian and configured it)
Rollback: Disable in Obsidian > Settings > Community Plugins
```

---

### 6. Quick Wins (Maintenance, Cleanups)

**Format:**
```
🧹 [Task Completed]

What: [One sentence]
Result: [Measurable outcome]
Time: [How long it took]
```

**Example:**
```
🧹 Disk Cleanup Complete

What: Freed up space by removing Homebrew caches, npm, pip, go modules
Result: 90% full → 57% full (11 GB freed)
Time: 8 minutes
```

---

## Delivery Channels

### 1. Direct Response (Webchat/Telegram)
- **Use for:** Immediate answers, quick outputs, <500 words
- **Format:** Conversational, direct, concise

### 2. File + Path (For all documents)
- **Use for:** Any file created/modified
- **Format:** Always include full path: `/Users/florianziesche/.openclaw/workspace/...`
- **Why:** "I created a file" without location = useless

### 3. Telegram for Important Deliverables
- **Use for:** Reports, PDFs, demos ready to share with clients
- **Format:** File attachment + brief context message
- **Example:** Risikoanalyse PDF sent with "16-page risk analysis for Andreas, includes all scenarios"

---

## Quality Self-Scoring (Mandatory)

**After every major output, predict quality score:**

### Score Definitions:
- **A** = Will be used as-is (90%+ confidence)
- **B** = Minor edits likely (70-89% confidence)
- **C** = Might need rework (<70% confidence)
- **?** = Uncertain / No immediate feedback expected

### How to Score:
1. **Is this presentation-ready?** (polished, complete, professional)
2. **Did I validate assumptions?** (checked sources, tested calculations)
3. **Is the format what Florian prefers?** (based on past patterns)
4. **Would I bet on this being used as-is?** (honest self-assessment)

### Update Output Tracker:
After delivery, log in `/Users/florianziesche/.openclaw/workspace/failures/output-tracker.md`:
```
| Date | Output | Predicted | Actual | Notes |
|------|--------|-----------|--------|-------|
| 2026-02-10 | CNC v19 | A | A | Florian: "Ich stelle es vor" |
```

---

## Feedback Loop Rules

### 1. Explicit Feedback Requests (Important Outputs)
**When to ask:**
- Proposals (memory restructure, new features)
- Email drafts before sending
- Strategic documents (positioning, thesis)
- First-time formats (new type of deliverable)

**How to ask:**
- "Does this work for you?"
- "Should I implement this or wait for feedback?"
- "Ready to send or need edits?"
- "Is this presentation-ready or should I polish more?"

**Don't ask for trivial outputs:**
- Bug fixes (just fix it)
- File organizations (just do it)
- Research lookups (just deliver)

---

### 2. Track Patterns (Learn Florian's Preferences)

**After 5-10 outputs of same type:**
- Which format worked best?
- What level of detail did he use?
- What got used as-is vs edited?
- What got ignored?

**Adjust future outputs based on patterns.**

**Example Pattern Learned:**
- **LaTeX PDFs:** Always A-rated for technical reports
- **59-page research reports:** No feedback (?-rated) → too long, need exec summaries
- **Career docs (CVs):** Always need 2-3 iterations (B-rated is expected)
- **CNC Planner v19:** A-rated when presentation-ready with all features working

---

### 3. A/B/C Variants (High-Stakes Only)

**When to offer variants:**
- Email subject lines (3 options)
- Proposal approaches (2-3 strategies)
- Headline/positioning copy (A/B test language)
- Design choices (if genuinely uncertain)

**Don't overuse:**
- Not for routine outputs
- Not when you have >90% confidence
- Not for every single decision

**Format:**
```
Here are 3 options:

**Option A: [Conservative]**
Pros: [...]
Cons: [...]

**Option B: [Balanced]**
Pros: [...]
Cons: [...]

**Option C: [Aggressive]**
Pros: [...]
Cons: [...]

My recommendation: Option B because [clear reasoning]

What do you think?
```

---

## Anti-Patterns (Never Do)

### ❌ Deliver Without Path
**Bad:** "I created the report"
**Good:** "Report created: `/Users/florianziesche/.openclaw/workspace/reports/risk-analysis.pdf`"

### ❌ Dump 50 Pages Unsolicited
**Bad:** "Here's a 59-page analysis of everything"
**Good:** "Here's a 3-bullet exec summary. Want the full 59 pages?"

### ❌ Ask for Feedback on Trivial Outputs
**Bad:** "Is it okay that I cleaned up the Downloads folder?"
**Good:** Just do it, report result: "Downloads cleaned: 390 MB freed"

### ❌ Deliver Without Context
**Bad:** "Here's the file: /path/to/file.html"
**Good:** "CNC Planner v19 ready to demo: /path/to/file.html - includes AI recommendations, risk analysis, and PDF export"

### ❌ Assume Silence = Approval
**Bad:** "I'll assume you're happy with this since you didn't respond"
**Good:** "No feedback yet on the report - marking as ?-rated in tracker, will check back in a week"

---

## Special Cases

### 1. Long-Running Tasks (Cron, Background)
**Initial Delivery:**
- What it does
- When it runs
- Where results go
- How to check/cancel

**Follow-Up (1 week later):**
- "The daily research cron has run 7 times. Is it valuable or should I cancel it?"

### 2. Proposals (Need Explicit Approval)
**Format:**
```
📋 Proposal: [Title]

What: [One sentence]
Why: [Problem it solves]
How: [High-level approach]

Impact: [What changes]
Effort: [Time estimate]

Approve to implement? Or discuss first?
```

### 3. Errors/Failures (Transparency)
**Format:**
```
⚠️ [Task] Failed

What I Tried: [Description]
Error: [Specific error message]
Root Cause: [Why it failed]

Options:
1. [Alternative approach A]
2. [Alternative approach B]
3. [Abandon and explain why]

Recommendation: [Which option + reasoning]
```

**Example:**
```
⚠️ PaperQA2 Installation Failed

What I Tried: Install PaperQA2 for research pipeline
Error: OpenAI API rate limit (500 RPM, need 2000+ RPM)
Root Cause: Free tier (Tier 1) insufficient, needs Tier 2 ($50+ spend)

Options:
1. Top up OpenAI credits to unlock Tier 2
2. Use Anthropic backend instead
3. Use Smart Connections + Mia Scanner (already working)

Recommendation: Option 3 - Smart Connections already delivers 80% of value, no extra cost
```

---

## Continuous Improvement

### Weekly Review:
- Check output-tracker.md for patterns
- Calculate A/B/C/? rates
- Identify what's working (do more)
- Identify what's failing (fix or stop)

### Monthly Review:
- Overall quality trend (improving?)
- Feedback loop effectiveness (fewer ?-rated outputs?)
- Delivery format preferences (stable patterns?)

### Quarterly Review:
- Major pattern shifts?
- New output types needed?
- Retire old patterns that don't work?

---

**Goal:** 70%+ A-rated, <25% ?-rated, 0% C-rated

**Current Baseline (2026-02-10):** 54.5% A-rated, 50% ?-rated, ~9% C-rated

---

**Last Updated:** 2026-02-10  
**Source:** Extracted from output tracker baseline + Kintsugi lessons + daily session patterns
