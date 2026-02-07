# Sequoia AGI Research - Quick Summary

**Research completed:** February 7, 2026

## What I Found

### 1. Sequoia's Core Thesis
- **AGI definition:** "The ability to figure things out" (functional, not technical)
- **3 ingredients:** Pre-training (2022) + Inference-time compute (2024) + Long-horizon agents (2026)
- **Key claim:** 2026 is AGI because you can now "hire" AI agents as colleagues

### 2. The Data (METR Benchmarks)
- AI task horizons doubling every **~7 months** since 2019
- Claude Opus 4.5: **4h49m time horizon** (can complete 5-hour tasks with 50% success)
- **Extrapolation:** Full-day tasks by 2028, year-long by 2034

### 3. The Critical Gap: Streaming Input
**THE CORE INSIGHT:** Current AI = snapshot processors, not continuous thinkers

**Technical problem:**
- LLMs work in **batches** (input → context window → output → repeat)
- Real intelligence needs **streaming** (continuous perception + world model updates)
- No current agent has persistent spatial-temporal memory

**Why it matters:**
- **Works now:** Code, writing, research (stateless digital tasks)
- **Struggles:** Manufacturing, robotics, legal (needs continuous awareness)
- **Blocks path to:** True "general" intelligence, embodied AI, always-on operation

**Quote from UC Berkeley researcher:**
> "How do you develop an intelligent LLM vision system that can actually have streaming input and update its understanding of the world? That's a big open problem. I think AGI is not possible without actually solving this problem."

### 4. Where Sequoia is Right
✅ Long-horizon agents are a real breakthrough (2026 ≠ 2022)  
✅ METR trend is impressive (6+ years of exponential growth)  
✅ Coding agents genuinely feel like "colleagues"  
✅ Functional definition matters for business

### 5. Where Sequoia Underplays Limits
❌ Reliability gap still exists (hallucinations, context loss)  
❌ Snapshot architecture limits deployment (manufacturing, physical world)  
❌ Extrapolation to 2034 ignores architectural hurdles  
❌ "Hireable" is domain-specific, not universal

## Best Article Angles (Ranked)

### #1: "The Streaming Input Problem" 
Why AI can handle 5-hour tasks in benchmarks but can't work a full day in reality. The architectural gap between batch and streaming processing.

**Target:** Technical founders, AI product managers  
**Unique value:** Explains *why* certain deployments fail technically

### #2: "AGI for VCs vs. AGI for Engineers"
Sequoia and researchers are talking past each other — functional vs. technical definitions reveal different timelines.

**Target:** Tech-savvy business audience  
**Unique value:** Reconciles hype with reality

### #3: "Domain-by-Domain: Where Your AI 'Employee' Actually Works"
Mapping what's deployable now (software) vs. what needs more R&D (manufacturing, legal).

**Target:** Business operators, investors  
**Unique value:** Actionable deployment guidance

## Key Sources

1. **Sequoia essay:** https://sequoiacap.com/article/2026-this-is-agi/
2. **METR benchmarks:** https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/
3. **Scientific American (world models):** Jan 2026 article on streaming input gap
4. **Factory.ai (context windows):** Technical deep-dive on limitations
5. **Hacker News critique:** Skeptical business perspective

## The Money Quote

From Sequoia:
> "What can you achieve when your plans are measured in centuries? A century is 200,000 clinical trials no one's cross-referenced. A century is every customer support ticket ever filed, finally mined for signal."

**The counter:**
Not without solving streaming input first.

---

**Full research brief:** `sequoia-agi-research.md` (34KB, comprehensive)
