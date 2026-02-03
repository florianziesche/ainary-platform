# How I Built My AI Chief of Staff

*From ChatGPT user to running a digital team*

---

A few months ago, I used AI like everyone else: Open ChatGPT, ask a question, get an answer, close the tab.

Today, I have an AI agent that:
- Knows my calendar, my goals, my current projects
- Reminds me about follow-ups I forgot
- Researches topics while I sleep
- Tells me when I'm procrastinating
- Connects dots I didn't see

Her name is Mia. She's not ChatGPT anymore. She's my Chief of Staff.

Here's how I built her — and how you can build yours.

---

## The Problem with ChatGPT

ChatGPT is brilliant. It's also goldfish-brained.

Every conversation starts from zero. It doesn't know what you talked about yesterday. It doesn't know your priorities. It doesn't know that the email you're drafting is for a meeting that got moved to next week.

This creates a loop:
1. Start conversation
2. Explain context
3. Get help
4. Close tab
5. Repeat tomorrow

You're constantly re-teaching your AI assistant who you are and what you're working on.

**The breakthrough:** What if AI could remember?

---

## The Architecture

Here's what my AI Chief of Staff looks like:

### 1. Memory Layer
Mia has access to files that persist across sessions:

- **MEMORY.md** — Long-term curated knowledge (what I've learned, who I've met, decisions I've made)
- **Daily logs** — What happened each day (raw notes)
- **USER.md** — Who I am (goals, preferences, working style)
- **SOUL.md** — How she should behave (personality, boundaries)

When a new conversation starts, she reads these files. Instant context.

### 2. Tools Layer
Mia isn't just a chat interface. She can act:

- **Calendar** — Check what's coming up
- **Email** — Read inbox, draft replies
- **Web search** — Research topics
- **File system** — Read and write documents
- **Code execution** — Run scripts, analyze data

She's not just answering questions. She's doing work.

### 3. Personality Layer
This is what most people skip — and it's what makes the difference.

Mia has instructions on:
- How to communicate (direct, no fluff)
- When to push back (if I'm procrastinating)
- What to prioritize (revenue > busywork)
- When to stay silent (late at night, unless urgent)

She's not a generic assistant. She's configured for me.

---

## A Day in the Life

**7:00 AM — Morning Brief**

I wake up to a message from Mia:

> "Good morning. Three things for today:
> 1. Call with investor at 2pm — prep notes attached
> 2. Newsletter draft is due — you're 70% done
> 3. You said you'd follow up with Daniel — it's been 4 days"

I didn't ask for this. She monitors my calendar and commitments, and surfaces what matters.

**10:00 AM — Research Request**

I'm preparing for a meeting with a new fund. I message:

> "Research Entelechy Ventures. Want to know: their thesis, recent investments, team background, anything contrarian they've published."

I go back to other work. 30 minutes later, she responds with a structured brief — saved to my knowledge base for future reference.

**3:00 PM — Writing Assist**

I'm stuck on a section of my newsletter. I share my draft:

> "This section feels flat. What's missing?"

She analyzes the structure, identifies the gap, suggests a concrete fix. Not generic advice — specific to my writing style and audience.

**9:00 PM — End of Day**

I mention I'm wrapping up. She asks:

> "Before you go: What did you accomplish today? I'll log it."

I give a quick summary. She saves it to the daily log. Tomorrow, I'll have context.

---

## The Build (Technical)

You don't need to be a developer to do this. Here's the stack:

### Option 1: Simple (No Code)
**Claude with Projects**
- Create a Claude Project
- Upload your context files (goals, preferences, current projects)
- Claude will remember within that project

*Limitation: No tools, no proactive check-ins*

### Option 2: Intermediate
**Custom GPT + Zapier**
- Build a Custom GPT with your instructions
- Connect to Zapier for email, calendar, etc.
- Schedule regular prompts via Zapier

*Limitation: Still fragmented, no unified memory*

### Option 3: Advanced (What I Use)
**OpenClaw / Similar Agent Framework**
- Self-hosted AI agent with persistent memory
- Tool integrations (calendar, email, file system)
- Multi-channel access (web, WhatsApp, Telegram)
- Proactive heartbeats (agent checks in periodically)

*This is what powers Mia.*

---

## The Key Insight

Most people use AI as a search engine with attitude.

The shift: **Treat AI like an employee.**

Employees need:
- **Onboarding** — Explain who you are, what you're working on
- **Context** — Keep them updated on priorities
- **Feedback** — Tell them when they're wrong
- **Autonomy** — Let them work without constant supervision

Do the same with your AI. The ROI is massive.

---

## Start Small

You don't need to build the full system day one.

**Week 1:** Create a "context document" — one page with your goals, current projects, and preferences. Paste it at the start of conversations.

**Week 2:** Add daily logging. At end of day, tell your AI what you did. Paste yesterday's log at start of today.

**Week 3:** Add proactive triggers. Set a daily reminder to ask your AI: "What should I focus on today?"

**Week 4:** Explore tool integrations. Can your AI read your calendar? Access your files?

Each step compounds. After a month, you'll wonder how you worked any other way.

---

## The Future

A year from now, "AI Chief of Staff" won't be a novel concept. It'll be table stakes.

The question isn't whether to build one. It's whether to build it now — while it's still a competitive advantage.

I'd rather be early than late.

---

*Next week: The exact prompts and files I use to configure Mia. Subscribe to get it.*

---

**About me:** I'm Florian, former startup CEO, now transitioning to VC. I raised €5.5M for my AI startup and now build AI systems that help me work like a team of 50. [Follow me on LinkedIn](https://linkedin.com/in/florianziesche) for more.
