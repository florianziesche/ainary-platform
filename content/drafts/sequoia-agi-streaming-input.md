# Sequoia Says AGI Is Here. They're Missing the Hard Part.

*Why the world's sharpest VCs are celebrating a milestone we haven't actually reached yet.*

---

Sequoia Capital just published "[2026: This is AGI](https://www.sequoiacap.com/article/2026-this-is-agi/)." Not "getting close." Not "almost there." **This is AGI.**

Coming from one of the most sophisticated technology investors on the planet, this isn't hype—it's a thesis. And the data they present is genuinely impressive: METR benchmarks show AI task horizons doubling every ~7 months. Claude Opus 4.5 now solves roughly 50% of tasks that take humans five hours to complete. These systems can chain together reasoning steps, use tools, debug their own errors, and persist through multi-hour assignments.

Their definition: AGI is "the ability to figure things out." Pre-training gives world knowledge. Inference-time compute enables deeper reasoning. Long-horizon agents execute complex workflows. Put it together, and you have systems that can tackle open-ended problems across domains.

I want to respect this argument. Sequoia isn't a meme fund chasing narrative—they're builders who've been funding the best technology companies for decades. When they stake a claim this bold, it deserves serious engagement.

But as someone who has spent years shipping AI into BMW factories, Siemens production lines, and enterprise legal workflows, I see a critical gap in their framework.

**They're celebrating batch processors. Humans are streaming processors.**

And that difference isn't a detail. It's the entire game.

---

## The Snapshot Problem

Here's what current "AGI" actually does:

1. Receives a context window (the task, relevant data, chat history)
2. Processes that snapshot
3. Returns an output
4. Waits for the next snapshot

This is **brilliant batch processing**. The context windows are getting larger (now 200K+ tokens). The reasoning is getting deeper (o3 can think for minutes). The tool use is getting more sophisticated (agents can write code, search the web, execute multi-step plans).

But it's still fundamentally: *snapshot → process → respond → wait.*

A human working on a complex task doesn't operate this way. You continuously perceive your environment. You notice when something changes mid-task. You update your understanding in real-time. You catch errors as they emerge, not after the batch completes.

When I led AI integration at my manufacturing startup, this distinction became painfully clear. We were using vision systems to detect defects on production lines. The models were excellent—on static images. But on a manufacturing floor, conditions change constantly: lighting shifts, material batches vary, operators adjust machine settings.

A snapshot-based system processes Frame 1, returns a decision, processes Frame 2, returns a decision. Each judgment is isolated. There's no continuous model of "the line is running hot today" or "this batch has slightly different reflectivity" or "the operator just changed the feed rate."

The model doesn't *know* anything is happening between frames. It doesn't update a world model. It just processes the next batch when it arrives.

---

## Batch vs. Streaming: Why It Matters

The difference shows up everywhere once you look for it:

**In legal review:** Current AI can read a 500-page contract and flag risks. Impressive! But during a live negotiation where terms are changing in real-time across email, Zoom, and Slack? The model isn't *in* the negotiation. You feed it snapshots: "Here's the updated draft." It processes. You go back to negotiating. It's a brilliant consultant you keep pulling out of the room to brief.

**In customer support:** AI can handle tickets end-to-end. But when a customer's mood shifts mid-conversation, or they mention something off-hand that reframes the entire issue, the system doesn't maintain a continuous understanding. It processes each message independently (with conversation history as context, yes—but still as a batch).

**In newsrooms:** I've seen AI draft articles from briefs. But a human reporter working a breaking story is continuously integrating new information: a source texts back, another outlet publishes an angle, a livestream reveals new details. The reporter's mental model updates in real-time. Current AI requires you to re-prompt with updates: "Here's new info, regenerate the draft." It's a writing tool, not a thinking partner moving through the story with you.

The "long-horizon agents" Sequoia celebrates are solving longer tasks, but they're not *continuously present* in the way humans are. They're processing longer batches, not streaming perception.

---

## What Streaming Input Would Actually Look Like

Imagine an AI that doesn't wait for the next prompt. It's always perceiving:

- **Continuous sensory input:** Not "process this image," but a feed it constantly monitors, building and updating a model of what's happening.
- **Persistent world models:** Not "here's the context for this task," but an evolving understanding it maintains across time.
- **Real-time model updates:** Not "give me new info and I'll regenerate," but "I notice the situation has changed, let me adjust my understanding and approach."
- **Interrupt-driven attention:** Not "wait for the next prompt," but "something important just happened, I need to surface this now."

This is what Scientific American identified in their January 2026 piece on embodied AI: *"In neither case does the AI hold a clearly defined model of the world that it continuously updates to make more informed decisions."*

They were writing about robotics, but the insight applies everywhere. Current AI—even the most sophisticated agents—operates on discrete transactions. It doesn't *live in time* the way humans do.

---

## Why VCs Miss This and Builders Notice

Sequoia's argument works from capabilities benchmarks. Can the model solve this task? Yes. Can it handle a five-hour assignment? Yes. Therefore: AGI.

But builders work in continuous environments. We see where the batch processing breaks:

- **Manufacturing floors** where conditions drift and you need continuous monitoring, not periodic checks.
- **Live negotiations** where the real game is reading the room and adapting in real-time.
- **Crisis management** where information comes in streams and you need to maintain situational awareness, not process updates on demand.
- **Creative collaboration** where ideas build on each other fluidly, not through formal prompt-response cycles.

When you're *deploying* AI into these environments, you immediately hit the wall. The systems are incredibly capable within each transaction. But they're not *there* between transactions. They don't maintain presence.

This isn't a criticism of the technology—it's a recognition of what we've actually built. We have **narrow AGI**: systems that can match or exceed human performance on specific tasks when given a well-defined problem and sufficient context.

But **general AGI**—systems that operate with continuous understanding across time and context—remains ahead of us.

---

## The Kintsugi Moment

In Japanese philosophy, Kintsugi is the art of repairing broken pottery with gold, making the cracks visible rather than hidden. The repair becomes part of the object's history, often more beautiful than the original.

The streaming input gap isn't a flaw in current AI—it's the seam that shows us what comes next.

Sequoia is right that we've reached a major milestone. The systems we have today are genuinely transformative. They will reshape industries, create trillion-dollar companies, and change how knowledge work happens.

But naming this moment "AGI" risks missing the frontier that's now visible. The next breakthrough isn't bigger context windows or deeper reasoning on static problems. It's **continuous perception and persistent world modeling**.

The companies that build this—systems that don't just process snapshots but truly stream their understanding of the world—will define the next phase of AI.

---

## So What?

**For builders:** Stop designing for batch. Think about what your AI needs to perceive continuously. What signals should it monitor? What world model should it maintain? How does it update understanding in real-time?

The interfaces we're building today—chat, API calls, prompt-response—are fundamentally batch-oriented. The next generation will feel more like collaboration with a continuously present partner.

**For investors:** The "AGI is here" narrative will drive enormous capital into scaling current architectures. That's probably correct for the next 12-24 months. But the real asymmetry is in streaming perception and persistent world models. The companies solving *that* problem are building the actual AGI platform.

**For enterprises adopting AI:** Current systems are incredible for well-defined tasks with clear inputs and outputs. Deploy them aggressively there. But don't expect them to operate like a human team member who's continuously aware of context, reads the room, and adapts to shifting conditions. We're not there yet.

---

## The Gap Is The Opportunity

Sequoia's essay will be right in retrospect—but not yet. We're at a remarkable milestone: AI that can figure out complex problems, chain reasoning across hours, and deliver genuinely useful work.

But we're still handing these systems snapshots and waiting for responses. They don't maintain continuous understanding. They don't update world models in real-time. They process batches brilliantly, but they don't stream.

The distinction matters because **the next trillion dollars will be built by whoever closes that gap.**

I spent three years shipping AI to factories that run 24/7. I've watched these systems succeed and fail in production. The batch processing is phenomenal for discrete tasks. But the continuous environments—where humans still dominate—require something we haven't built yet.

Sequoia says AGI is here. I say: we've built the foundation. Now comes the hard part.

The gold is in the cracks.

---

**German title suggestion:**  
*"Sequoia sagt, AGI ist da. Sie übersehen den schwierigen Teil."*

**280-char Twitter hook:**  
Sequoia just declared AGI has arrived. But as someone who ships AI to factories and enterprises daily, I see the critical gap: current AI processes snapshots. Humans stream. That difference isn't a detail—it's the entire frontier. The gold is in the cracks.

---

*Florian Ziesche is a former startup CEO (€5.5M raised, shipped AI to BMW/Siemens/Bosch) and now works as an AI consultant and VC Lab Fellow. He writes about AI, venture capital, and building real systems at [ainaryventures.com](https://ainaryventures.com).*