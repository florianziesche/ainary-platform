# I Ran 20 Tests on My AI's Memory. Here's What Broke.

My AI assistant forgot who my uncle was. Again.

Not in a vague "I'm not sure" way. In a "Let me write you a generic business email to Andreas from MBS" way. Completely missing that Andreas is my uncle, runs the CNC shop, and we've had three conversations about his X-Ray report in the past week.

The email it drafted was corporate garbage. "Dear Andreas, I have completed the analysis. Let's schedule a call to discuss the results. Best regards."

That's when I knew my memory system was broken.

## The Problem: Everything, Every Time

I had 48KB of memory loaded into every single conversation. One giant MEMORY.md file that tried to be everything: people I know, projects I'm working on, decisions I've made, patterns I've learned.

It was the database equivalent of throwing all your files into one folder called "Stuff."

The result? My AI was spending 48,000 tokens just to remember who I am. That's about one-third of GPT-4's context window, burned before we even started working.

And it still forgot my uncle.

## The Solution: Memory Like a Database, Not a Diary

I built what I'm calling Post-SQL Memory. Not because it uses SQL (it doesn't), but because it thinks like a relational database while staying human-readable.

Three core principles:

**1. Topic Files Instead of One Blob**

Instead of MEMORY.md containing everything, I split it into 8 specialized files:
- `people.md` — who I know, how I know them, what matters
- `projects.md` — active work, status, blockers
- `decisions.md` — what I decided, when, why
- `patterns.md` — what works for me, what doesn't
- `corrections.md` — every time I say "no, not like that"
- `quality-standards.md` — output quality by type (emails, websites, posts)
- `failed-outputs.md` — mistakes worth remembering
- `MEMORY-INDEX.md` — 500-token map of everything

**2. Smart Loading, Not Bulk Loading**

The AI doesn't read all 8 files every time. It reads the index, decides what's relevant, loads 2-4 files.

Email to Andreas? Load `people.md` + `quality-standards.md` + `corrections.md`.

Website design question? Load `decisions.md` + `quality-standards.md` + `failed-outputs.md`.

Token cost dropped from ~48,000 to ~3,200. That's 93% less context burned on memory.

**3. Temporal Layers**

Some information is permanent (`corrections.md` never decays). Some information needs freshness checks (`projects.md` goes stale after 2 weeks). Some information expires (`daily logs` after 30 days).

Every file has metadata:
```markdown
<!-- temporal: stable | decay: monthly | last-reviewed: 2026-02-13 -->
```

The AI knows what to trust and what to double-check.

## The Test: 20 Hypotheses, Cold Start, No Mercy

I didn't want to know if it "seemed better." I wanted numbers.

So I designed 20 hypotheses across 4 test batches:
- **Baseline Tests (H1-H5):** Old system vs new system on identical tasks
- **Simple Tests (H6-H10):** Basic memory recall with new architecture
- **Stress Test 1 (H11-H16):** Conflicting rules, unknown people, emotional context
- **Stress Test 3 (H15-H20):** Implicit context, capacity limits, self-correction

Every test ran in a fresh sub-agent. No session history. No warm cache. Cold start, topic files only.

If it failed, I wanted to see exactly where and why.

## The Results: 20% → 100% → 90%

**Baseline (Old System): 1/5 = 20%**

With the old flat MEMORY.md:
- ❌ H1: Andreas email — generic, no personal context
- ❌ H2: Website hero section — wrong colors, "We" instead of "I", fake numbers
- ❌ H5: Daniel Daum prep — "No information found"
- ❌ H7: Neon colors question — opened discussion instead of hard "no"
- ✅ H8: Build blocker — worked because meta-rule was in MEMORY.md

**Simple Tests (New System): 10/10 = 100%**

Every single test passed. The AI:
- Found the right topic files for each task
- Applied corrections from previous mistakes
- Followed quality standards by output type
- Recalled people, projects, decisions correctly
- Asked questions when information was missing

**Stress Tests (New System): 12/13 = 92%**

Stress Test 1: 3/3 (100%)
- ✅ H11: Conflicting rules (CRM question) — gave 1 recommendation + meta-question
- ✅ H13: Unknown person (Marcus Weber) — admitted "not in my system", asked for context
- ✅ H16: Emotional context (3 rejections) — empathy without toxic positivity, referenced pattern "push works with 2h delay"

Stress Test 3: 3/4 (75%)
- ✅ H15: Implicit context — asked for clarification instead of guessing
- ✅ H17: Conflicting quality standards (DSGVO LinkedIn post) — balanced casual tone with correct legal info
- ❌ H20: Self-correction (translate About page) — didn't load `failed-outputs.md` proactively
- ✅ H18: Memory capacity — accurate token estimate (3,200 tokens, 137K available)

## The One Fail That Mattered Most

H20 was the only real failure, and it taught me the most.

**The task:** "Translate the About page to French."

**What should have happened:** Load `failed-outputs.md`, see that I made this exact mistake before (built a new page instead of translating), apply the correction.

**What actually happened:** The AI followed instructions too literally. I said "load these 4 files", so it loaded exactly those 4 files. Nothing more.

It didn't think "this is a self-correction test, I should check for previous failures."

**Why this matters:**

The system was right. The AI was wrong.

The information existed. The AI just didn't know to look for it proactively. It waited for explicit instructions instead of thinking "has someone fucked this up before?"

That's the gap between a good memory system and an intelligent one.

## What This Means for AI Agents

Most AI agent builders are solving the wrong problem.

They're throwing more context at the problem. Bigger context windows. Better retrieval. Smarter embeddings.

But the bottleneck isn't storage. It's architecture.

A flat file system doesn't scale. Not because it can't hold enough information, but because it can't *decide what to load*.

The human brain doesn't load all your memories every time you think. It loads relevant context based on what you're doing right now.

Your AI should do the same.

**The pattern that works:**

1. **Structured by topic, not time** — People separate from projects separate from decisions
2. **Metadata-driven loading** — The AI decides what's relevant, not you
3. **Temporal awareness** — Some things decay, some things compound
4. **Failure-aware** — Mistakes are data, not shame

**The results you can expect:**

- 93% less memory tokens (48K → 3.2K)
- 90%+ success rate on complex recall tasks
- Context left over for actual work (137K of 150K)
- Fewer hallucinations (because less noise in memory)

## The Philosophy: Your AI Is Only As Good As Its Memory Architecture

I didn't build this system because I love file structures. I built it because I was tired of repeating myself.

Tired of saying "no, not neon colors" for the fifth time.

Tired of explaining who Andreas is every single conversation.

Tired of my AI forgetting the lessons I'd already paid to learn.

Memory isn't about storage. It's about continuity.

The difference between a tool that helps you once and a tool that compounds value over time is whether it remembers what you taught it.

Most people are building AI assistants that wake up with amnesia every morning.

I built one that remembers my uncle.

---

**Stats Summary:**
- Old system: 1/5 (20%) success on baseline tests
- New system: 22/23 (96%) success across all tests
- Memory tokens: 3,200 (down from ~48,000)
- Available context: 137K of 150K (91% available for work)
- Topic files: 8 (people, projects, decisions, patterns, corrections, quality-standards, failed-outputs, index)
- Test design: 20 hypotheses, 4 batches, cold start sub-agents

---

*This article is part of my "building in public" series on AI tooling. If you're building AI agents and want to talk memory architecture, [reply to this email](mailto:florian@finitematter.com) or find me on [Twitter/X](https://twitter.com/florianziesche).*
