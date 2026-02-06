#!/usr/bin/env python3
"""
SOTA Brief Generator for OpenClaw
Generates weekly state-of-the-art briefs covering Legal AI, Manufacturing AI, VC/Investment, Agentic Systems
"""

import os
import sys
import json
from datetime import datetime, timedelta
from pathlib import Path

# This script is designed to be called from OpenClaw with web search and fetch capabilities
# It will be invoked by the OpenClaw agent with the following message:

SOTA_GENERATION_PROMPT = """
Generate a weekly SOTA brief for the week of {week_date}.

EXECUTE THE RESEARCH SKILL:
Follow the instructions in /Users/florianziesche/.openclaw/workspace/skills/sota-brief/SKILL.md exactly.

VERTICALS TO COVER:
1. Legal AI (EvenUp, CaseMark, Supio, Westlaw, LexisNexis, regulatory)
2. Manufacturing AI (CNC, Industry 4.0, Siemens, Autodesk, process automation)
3. VC/Investment (funding rounds, LP activity, market sentiment, fund announcements)
4. Agentic Systems (Claude releases, agent frameworks, reasoning models, new architectures)

OUTPUT FORMAT:
Save to: /Users/florianziesche/.openclaw/workspace/sota-{date}.md

Use this exact markdown structure:

```markdown
# SOTA Brief — {date}

## Legal AI

### [Item Title]
- **What:** [1-2 sentence description]
- **Why it matters:** [1 sentence impact]
- **Sources:** [Link 1], [Link 2]
- **Confidence:** High / Medium / Low

[3-5 items total]

## Manufacturing AI
[Same format, 3-5 items]

## VC/Investment
[Same format, 3-5 items]

## Agentic Systems
[Same format, 3-5 items]

---

## Summary
[2-3 sentence synthesis of biggest trends]

**Generated:** {timestamp}
**Next brief:** {next_date}
```

QUALITY REQUIREMENTS:
- Each item has 1+ source URLs
- Confidence ratings are truthful
- Each item explains why Florian should care
- Items from last 7 days are prioritized
- Minimum 2 sources per item for "High" confidence
- Single source items are marked "Low" confidence
- File is 2-4 KB total (concise, not sprawling)

EXECUTION:
1. Use web search to find recent news in each vertical
2. For each promising item, fetch the source to verify details
3. Cross-reference with multiple sources to validate
4. Compile into markdown format
5. Save to workspace file
6. Report completion to main session
"""

def get_week_date():
    """Get the current week's date for the brief"""
    today = datetime.now()
    return today.strftime("%Y-%m-%d")

def get_next_week_date():
    """Calculate next week's date"""
    today = datetime.now()
    next_week = today + timedelta(days=7)
    return next_week.strftime("%Y-%m-%d")

def generate_prompt():
    """Generate the OpenClaw agent prompt for SOTA generation"""
    week_date = get_week_date()
    next_date = get_next_week_date()
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")

    prompt = SOTA_GENERATION_PROMPT.format(
        week_date=week_date,
        date=week_date,
        timestamp=current_time,
        next_date=next_date
    )

    return prompt

def main():
    """
    This script generates the prompt for OpenClaw to execute.
    In practice, OpenClaw will call this with the web search and fetch tools available.
    """

    # Create skills directory if it doesn't exist
    skill_dir = Path("/Users/florianziesche/.openclaw/workspace/skills/sota-brief")
    skill_dir.mkdir(parents=True, exist_ok=True)

    # Get the prompt to pass to OpenClaw
    prompt = generate_prompt()

    # Output the prompt (this will be used by the cron job)
    print(prompt)

    return 0

if __name__ == "__main__":
    sys.exit(main())
