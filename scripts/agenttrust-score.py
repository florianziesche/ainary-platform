#!/usr/bin/env python3
"""AgentTrust Score Manager — CLI for tracking trust across sessions.

Usage:
    agenttrust-score.py update <agent_id> <stated_confidence> <outcome> [reason]
    agenttrust-score.py status [agent_id]
    agenttrust-score.py review <output_file> [--tier 2]
    agenttrust-score.py history <agent_id> [--last 10]

Outcomes: good, bad, flagged_real, hidden_problem
Agents: main, writer, researcher, builder, hunter, dealmaker

Scores persist in memory/agenttrust-state.json
"""

import json
import sys
import os
import time
from pathlib import Path

# Add agenttrust to path
REPO = Path(__file__).resolve().parent.parent / "projects" / "agenttrust"
sys.path.insert(0, str(REPO))

from agenttrust.core.trust_score import TrustScore, TrustLevel
from agenttrust.core.beipackzettel import Beipackzettel
from agenttrust.qa.reviewer import review

STATE_FILE = Path(__file__).resolve().parent.parent / "memory" / "agenttrust-state.json"
MARKDOWN_FILE = Path(__file__).resolve().parent.parent / "memory" / "trust-score.md"


def load_state() -> dict:
    """Load persisted trust state."""
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text())
    return {"agents": {}, "events": []}


def save_state(state: dict):
    """Persist trust state."""
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(json.dumps(state, indent=2))


def get_trust_score(state: dict, agent_id: str) -> TrustScore:
    """Reconstruct TrustScore from persisted state."""
    score = state.get("agents", {}).get(agent_id, {}).get("score", 0)
    return TrustScore(agent_id, initial_score=score)


def update_score(agent_id: str, stated_confidence: float, outcome: str, reason: str = ""):
    """Record a trust event and update the score."""
    state = load_state()
    ts = get_trust_score(state, agent_id)
    event = ts.update(stated_confidence, outcome, reason)

    # Persist
    if "agents" not in state:
        state["agents"] = {}
    state["agents"][agent_id] = {
        "score": ts.score,
        "level": ts.trust_level.value,
        "updated": time.time(),
    }
    if "events" not in state:
        state["events"] = []
    state["events"].append({
        "agent_id": agent_id,
        "timestamp": event.timestamp,
        "stated_confidence": event.stated_confidence,
        "outcome": event.outcome,
        "delta": event.delta,
        "reason": event.reason,
        "score_after": ts.score,
    })
    save_state(state)

    # Update markdown
    update_markdown(state)

    level_emoji = {
        "untrusted": "🔴",
        "supervised": "🟡",
        "spot_check": "🟢",
        "autonomous": "⭐",
    }
    emoji = level_emoji.get(ts.trust_level.value, "❓")
    print(f"{emoji} {agent_id}: {ts.score}/100 ({ts.trust_level.value}) | delta: {event.delta:+d} | {event.reason}")


def show_status(agent_id: str = None):
    """Show trust scores for all agents or a specific one."""
    state = load_state()
    agents = state.get("agents", {})

    if agent_id:
        agents = {agent_id: agents.get(agent_id, {"score": 0, "level": "untrusted"})}

    level_emoji = {"untrusted": "🔴", "supervised": "🟡", "spot_check": "🟢", "autonomous": "⭐"}

    print("Agent Trust Scores")
    print("=" * 50)
    for aid, data in sorted(agents.items()):
        score = data.get("score", 0)
        level = data.get("level", "untrusted")
        emoji = level_emoji.get(level, "❓")
        qa_rate = {"untrusted": "100%", "supervised": "50%", "spot_check": "20%", "autonomous": "0%"}
        print(f"  {emoji} {aid:15s} Score: {score:3d}/100  Level: {level:12s}  QA: {qa_rate.get(level, '?')}")
    print()

    # Last 5 events
    events = state.get("events", [])
    if agent_id:
        events = [e for e in events if e["agent_id"] == agent_id]
    events = events[-5:]
    if events:
        print("Recent Events:")
        for e in events:
            delta = f"+{e['delta']}" if e['delta'] > 0 else str(e['delta'])
            print(f"  [{delta:3s}] {e['agent_id']:10s} conf:{e['stated_confidence']:3.0f}% outcome:{e['outcome']:15s} → {e.get('score_after', '?')}")


def review_output(output_file: str, tier: int = 2):
    """Review an output file using the 8-dimension rubric."""
    text = Path(output_file).read_text()
    result = review(text, tier=tier)

    print(f"Review: {output_file}")
    print(f"Verdict: {result.verdict} ({result.rubric_score.total}/{result.rubric_score.max_total})")
    print(f"Tier: {tier} (threshold: {10 + (tier-1)*2})")
    print()
    for dim_id, score in result.rubric_score.scores.items():
        bar = "██" * score + "░░" * (2 - score)
        print(f"  {dim_id:15s} {bar} {score}/2")
    if result.issues:
        print(f"\nIssues:")
        for issue in result.issues:
            print(f"  ⚠️  {issue}")


def show_history(agent_id: str, last: int = 10):
    """Show event history for an agent."""
    state = load_state()
    events = [e for e in state.get("events", []) if e["agent_id"] == agent_id]
    events = events[-last:]

    print(f"History for {agent_id} (last {last}):")
    for e in events:
        delta = f"+{e['delta']}" if e['delta'] > 0 else str(e['delta'])
        ts = time.strftime("%Y-%m-%d %H:%M", time.localtime(e['timestamp']))
        print(f"  {ts} [{delta:3s}] conf:{e['stated_confidence']:3.0f}% {e['outcome']:15s} → score:{e.get('score_after', '?')} | {e['reason']}")


def update_markdown(state: dict):
    """Update the markdown trust score file."""
    agents = state.get("agents", {})
    level_emoji = {"untrusted": "🔴", "supervised": "🟡", "spot_check": "🟢", "autonomous": "⭐"}

    lines = [
        "# Agent Trust Scores",
        f"*Auto-generated by agenttrust-score.py. Last: {time.strftime('%Y-%m-%d %H:%M')}*",
        "",
        "## Current Scores",
        "",
        "| Agent | Score | Level | QA Rate | Autonomie |",
        "|-------|-------|-------|---------|-----------|",
    ]
    qa_rates = {"untrusted": "100%", "supervised": "50%", "spot_check": "20%", "autonomous": "0%"}
    autonomy_desc = {
        "untrusted": "QA prüft alles",
        "supervised": "QA prüft Flagged",
        "spot_check": "QA Stichproben 20%",
        "autonomous": "Direkte Auslieferung",
    }
    for aid, data in sorted(agents.items()):
        level = data.get("level", "untrusted")
        emoji = level_emoji.get(level, "❓")
        lines.append(
            f"| {emoji} {aid} | {data.get('score', 0)}/100 | {level} | {qa_rates.get(level, '?')} | {autonomy_desc.get(level, '?')} |"
        )

    # Last 10 events
    events = state.get("events", [])[-10:]
    if events:
        lines += [
            "",
            "## Recent Events",
            "",
            "| Zeit | Agent | Conf | Outcome | Delta | Score | Reason |",
            "|------|-------|------|---------|-------|-------|--------|",
        ]
        for e in events:
            ts = time.strftime("%m-%d %H:%M", time.localtime(e['timestamp']))
            delta = f"+{e['delta']}" if e['delta'] > 0 else str(e['delta'])
            lines.append(
                f"| {ts} | {e['agent_id']} | {e['stated_confidence']:.0f}% | {e['outcome']} | {delta} | {e.get('score_after', '?')} | {e['reason'][:40]} |"
            )

    lines += [
        "",
        "## Scoring Rules",
        "- Good output + high confidence → +1",
        "- Bad output + high confidence (≥80%) → -3 (overconfident)",
        "- Bad output + low confidence → -1 (wrong but honest)",
        "- Flagged uncertainty that was real → +2",
        "- Hidden problem QA finds → -3",
        "",
        "## Trust Levels",
        "- 0-30: 🔴 UNTRUSTED — QA reviews everything",
        "- 31-60: 🟡 SUPERVISED — QA reviews flagged items",
        "- 61-80: 🟢 SPOT_CHECK — QA spot-checks 20%",
        "- 81+: ⭐ AUTONOMOUS — Direct delivery",
    ]

    MARKDOWN_FILE.write_text("\n".join(lines) + "\n")


if __name__ == "__main__":
    args = sys.argv[1:]

    if not args or args[0] == "help":
        print(__doc__)
        sys.exit(0)

    cmd = args[0]

    if cmd == "update" and len(args) >= 4:
        agent_id = args[1]
        confidence = float(args[2])
        outcome = args[3]
        reason = " ".join(args[4:]) if len(args) > 4 else ""
        update_score(agent_id, confidence, outcome, reason)

    elif cmd == "status":
        agent_id = args[1] if len(args) > 1 else None
        show_status(agent_id)

    elif cmd == "review" and len(args) >= 2:
        tier = 2
        if "--tier" in args:
            tier = int(args[args.index("--tier") + 1])
        review_output(args[1], tier)

    elif cmd == "history" and len(args) >= 2:
        last = 10
        if "--last" in args:
            last = int(args[args.index("--last") + 1])
        show_history(args[1], last)

    else:
        print(f"Unknown command: {cmd}")
        print(__doc__)
        sys.exit(1)
