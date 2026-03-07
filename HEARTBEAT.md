# Heartbeat Checklist

## Sub-Agent Audit (PRIORITY 0 — check FIRST)
- `subagents list` → any completed since last heartbeat?
- For each completed: was knowledge-worker spawned on its output? If NO → spawn now
- Model check: was any sub-agent spawned with opus? Flag waste
- Did any sub-agent task say "read file X" instead of pasting context? → Fix pattern

## Agent Architecture (PRIORITY 1)
- What broke since last heartbeat? Fix the SYSTEM, not the symptom
- Any cron errors? → Root cause → Fix the standard/process that caused it
- Are there patterns across failures? → New rule in AGENTS.md or SUB-AGENT-CONTEXT.md
- Can any manual step be automated? → Build it

## Knowledge Compound (PRIORITY 2)
- New insights from overnight work → Cross-link to existing knowledge
- Open hypotheses testable with today's data? → Test one
- verified-truths.md outdated? → Update or flag
- Standards improved? → Propagate to sub-agent context

## Product & Distribution (PRIORITY 3)
- Is there a product closer to launch? → What's the next blocker?
- Research outputs that validate/invalidate product direction? → Log decision
- Any automation that could serve customers directly? → Document

## Housekeeping
- memory/daily/YYYY-MM-DD.md exists? Create if not
- Stale files (>7d daily, not consolidated) → Merge into knowledge/
- Workspace cleaner than yesterday? One thing better
