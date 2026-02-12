# Mutation: Grok Search Provider Alternative

**Date:** 2026-02-10
**Type:** Feature Addition
**Status:** Documented (Implementation pending)

## Problem
Brave Search API has quota limits (2000/month on Free plan). When quota runs low, web_search tool becomes unreliable.

## Solution
OpenClaw v2026.2.9 added **Grok (xAI)** as a web_search provider alternative.

## Implementation
When Brave quota <500 remaining (~end of month), switch to Grok:

```bash
# Check Brave quota
grep "quota_current" memory/*.md | tail -1

# If low, test Grok
openclaw config.get | grep -A5 web_search
# Add Grok provider config if needed
```

## Impact
- Reduces dependency on single search provider
- Prevents search failures during high-usage periods
- Cost optimization (Grok pricing TBD)

## Next Steps
1. Research Grok API pricing
2. Test Grok search quality vs Brave
3. Document provider switching workflow
4. Add auto-fallback logic if Brave quota exhausted

## Related
- OpenClaw v2026.2.9 release notes
- Brave quota tracking in DAILY_LEARNINGS.md
- agents/EXECUTION-TRACKER.md (quota monitoring)
