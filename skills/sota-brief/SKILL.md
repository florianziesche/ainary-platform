# Weekly SOTA Brief Generator

*Version 1.0 — 2026-02-06*

---

## Purpose

Generate a weekly State-of-the-Art (SOTA) brief covering key developments in:
- **Legal AI** (EvenUp, CaseMark, Supio, regulatory changes)
- **Manufacturing AI** (CNC automation, process optimization, industry 4.0)
- **VC/Investment** (funding rounds, market movements, fund theses)
- **Agentic Systems** (new agent frameworks, reasoning models, agent architectures)

The brief is saved as `sota-YYYY-MM-DD.md` to the OpenClaw workspace and should be short, actionable, and confidence-rated.

---

## Execution Task Description

**Objective:** Generate a weekly SOTA brief covering AI developments relevant to Florian's business verticals.

**Instructions:**

1. **Search for SOTA news across 4 verticals:**
   - Legal AI: EvenUp, CaseMark, Supio, Westlaw AI, LexisNexis developments, regulatory updates
   - Manufacturing AI: CNC software updates, AI-powered manufacturing, Industry 4.0, Siemens/Autodesk announcements
   - VC/Investment: Fund announcements, Series A/B rounds in AI, LP activity, market sentiment
   - Agentic Systems: Claude releases, other LLM agent frameworks, new agent architectures, reasoning models

2. **For each vertical, identify 3-5 items covering:**
   - New product releases or significant feature updates
   - Competitive landscape movements (startups, established players)
   - Industry trends or regulatory changes
   - Notable research papers or technical breakthroughs
   - Market signals (funding, partnerships, M&A)

3. **Source Requirements:**
   - Minimum 2 independent sources per item (higher confidence)
   - Single source items marked as "Confidence: Low"
   - URLs provided for all items
   - Publication date within last 7 days (or most recent if older)

4. **Output Format (Markdown):**
   ```
   # SOTA Brief — [YYYY-MM-DD]

   ## Legal AI

   ### [Item Title]
   - **What:** [1-2 sentence description]
   - **Why it matters:** [1 sentence impact for Florian's business]
   - **Sources:** [Link 1], [Link 2]
   - **Confidence:** High / Medium / Low

   [3-5 items total per vertical]

   ## Manufacturing AI
   [Same format]

   ## VC/Investment
   [Same format]

   ## Agentic Systems
   [Same format]

   ---

   ## Summary
   [2-3 sentence synthesis of biggest trends across all verticals]

   **Generated:** [Timestamp]
   **Next brief:** [Next week date]
   ```

5. **Save to workspace:**
   - File path: `/Users/florianziesche/.openclaw/workspace/sota-YYYY-MM-DD.md`
   - Use today's date in filename
   - File should be 2-3 KB (concise, not comprehensive)

6. **Delivery (if running with deliver: true):**
   - Send via Telegram to Florian with format:
   ```
   📊 WEEKLY SOTA BRIEF — [DATE]

   [Summary section]

   **Read full brief:** [Link to workspace file]

   Confidence ratings: High / Medium / Low
   ```

---

## Research Methodology

**Phase 0: Gold Standard Check**
- Check if existing SOTA briefs exist in workspace for format reference
- Use research/SKILL.md guidelines for sourcing

**Phase 1: Search Strategy**
1. Web search for "[Vertical Name] AI news 2026"
2. Check official product pages (Anthropic, OpenAI, Google, etc.)
3. Search ArXiv for recent papers (last 7 days)
4. Check Twitter/X for announcements from key figures
5. Monitor VC news sites (TechCrunch, The Information, Pitchbook summaries)

**Phase 2: Triangulation**
- Each item must have 2+ sources
- If only 1 source available → mark as Low confidence
- Prioritize primary sources (official announcements, research papers)

**Phase 3: Synthesis**
- Don't just list news — identify patterns
- Highlight competitive implications
- Note how items relate to Florian's business (Legal AI + Manufacturing AI intersection)

**Phase 4: Quality Check**
- Confidence ratings are truthful (not optimistic)
- Each item answers "Why does Florian care?"
- File saves successfully to workspace with correct date format

---

## Scheduling

**Cron Expression:** `0 20 * * 0` (Every Sunday at 8:00 PM Berlin time)

Alternative suggestions:
- `0 8 * * 1` (Every Monday at 8:00 AM Berlin time) — More fresh start feel

---

## Success Criteria

- [ ] 4-5 items per vertical (16-20 total items)
- [ ] All items have confidence ratings
- [ ] All items have at least 1 source URL
- [ ] File saved with correct naming convention (sota-YYYY-MM-DD.md)
- [ ] File is 2-4 KB (concise, not sprawling)
- [ ] Delivery message sent to Florian if enabled
- [ ] Next week's date correctly calculated

---

## Known Gotchas

| Issue | Solution |
|-------|----------|
| News is older than 7 days | Still include if it's significant; note age in source |
| Can't find 2 sources for item | Mark as Low confidence, include if newsworthy |
| Vertical has no news | Leave section or write "No significant moves this week" |
| SOTA brief not delivering | Check workspace path is correct, check Telegram config |
| Items too long | Trim to 1-2 sentences per item, cut "Why it matters" to 1 sentence |

---

## Integration Notes

- Runs weekly via cron job in OpenClaw
- Saves to OpenClaw workspace (same as MEMORY.md, NORTH_STAR.md)
- Can optionally deliver via Telegram using same channel as Morning Brief
- Uses web search and fetch tools (no special API keys required)
- Estimated runtime: 8-12 minutes (3 min per vertical search)

---

## Feedback Log

| Date | Issue | Resolution | Change |
|------|-------|-----------|--------|
| 2026-02-06 | Initial spec | N/A | Version 1.0 created |

---

*Next review: After first 3 runs. Adjust confidence calibration, source quality, vertical weighting based on Florian feedback.*
