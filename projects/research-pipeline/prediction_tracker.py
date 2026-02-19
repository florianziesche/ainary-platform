#!/usr/bin/env python3
"""
prediction_tracker.py — Track and score predictions across reports.

Every report can register testable, dated predictions.
Monthly cron checks for resolution. Public scorecard builds credibility.

Usage:
    python3 prediction_tracker.py add <report_id> <prediction_json>
    python3 prediction_tracker.py list
    python3 prediction_tracker.py check   # auto-check resolvable predictions
    python3 prediction_tracker.py score   # calculate accuracy
    python3 prediction_tracker.py html    # generate public scorecard
"""

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

WORKSPACE = Path.home() / ".openclaw" / "workspace"
PREDICTIONS_PATH = WORKSPACE / "research-base" / "predictions.json"


def load_predictions() -> list[dict]:
    if PREDICTIONS_PATH.exists():
        return json.loads(PREDICTIONS_PATH.read_text())
    return []


def save_predictions(predictions: list[dict]):
    PREDICTIONS_PATH.write_text(json.dumps(predictions, indent=2))


def add_prediction(report_id: str, prediction: dict):
    """Add a prediction from a report."""
    preds = load_predictions()
    pred = {
        "id": f"{report_id}-P{len([p for p in preds if p['report_id'] == report_id]) + 1}",
        "report_id": report_id,
        "claim": prediction["claim"],
        "confidence": prediction.get("confidence", 50),
        "resolve_by": prediction["resolve_by"],
        "status": "open",
        "evidence_for": [],
        "evidence_against": [],
        "created": datetime.now(timezone.utc).isoformat(),
        "resolved": None,
        "outcome": None,  # correct / incorrect / partially_correct / unresolvable
    }
    preds.append(pred)
    save_predictions(preds)
    print(f"Added: {pred['id']} — {pred['claim'][:80]}...")
    return pred


def list_predictions():
    preds = load_predictions()
    open_count = len([p for p in preds if p["status"] == "open"])
    resolved = len([p for p in preds if p["status"] == "resolved"])
    print(f"Predictions: {len(preds)} total, {open_count} open, {resolved} resolved\n")

    for p in sorted(preds, key=lambda x: x.get("resolve_by", "")):
        status_icon = {"open": "⏳", "resolved": "✅"}.get(p["status"], "?")
        outcome = p.get("outcome", "")
        outcome_str = f" → {outcome}" if outcome else ""
        print(f"  {status_icon} {p['id']} (conf: {p['confidence']}%, by: {p['resolve_by']}){outcome_str}")
        print(f"     {p['claim'][:100]}")
        if p.get("evidence_for"):
            print(f"     Evidence for: {len(p['evidence_for'])}")
        if p.get("evidence_against"):
            print(f"     Evidence against: {len(p['evidence_against'])}")
        print()


def calculate_score() -> dict:
    """Calculate prediction accuracy using Brier Score."""
    preds = load_predictions()
    resolved = [p for p in preds if p["status"] == "resolved" and p.get("outcome")]

    if not resolved:
        print("No resolved predictions yet.")
        return {"accuracy": None, "brier": None, "n": 0}

    correct = len([p for p in resolved if p["outcome"] == "correct"])
    partial = len([p for p in resolved if p["outcome"] == "partially_correct"])
    incorrect = len([p for p in resolved if p["outcome"] == "incorrect"])

    # Simple accuracy
    accuracy = (correct + 0.5 * partial) / len(resolved) if resolved else 0

    # Brier score (lower = better calibrated)
    brier_sum = 0
    for p in resolved:
        conf = p["confidence"] / 100.0
        outcome_val = {"correct": 1.0, "partially_correct": 0.5, "incorrect": 0.0,
                       "unresolvable": None}.get(p["outcome"])
        if outcome_val is not None:
            brier_sum += (conf - outcome_val) ** 2

    brier = brier_sum / len(resolved) if resolved else 0

    result = {
        "accuracy": round(accuracy * 100, 1),
        "brier_score": round(brier, 3),
        "n_resolved": len(resolved),
        "n_correct": correct,
        "n_partial": partial,
        "n_incorrect": incorrect,
        "n_open": len([p for p in preds if p["status"] == "open"]),
    }

    print(f"Prediction Score:")
    print(f"  Accuracy: {result['accuracy']}%")
    print(f"  Brier Score: {result['brier_score']} (lower = better calibrated)")
    print(f"  Resolved: {len(resolved)} ({correct}✓ {partial}~ {incorrect}✗)")
    print(f"  Open: {result['n_open']}")

    return result


def generate_html():
    """Generate public prediction scorecard HTML."""
    preds = load_predictions()
    score = calculate_score()

    rows = []
    for p in sorted(preds, key=lambda x: x.get("resolve_by", "")):
        status = {"open": "⏳ Open", "resolved": "✅ Resolved"}.get(p["status"], p["status"])
        outcome = p.get("outcome", "—")
        rows.append(f"""<tr>
            <td>{p['id']}</td>
            <td>{p['claim'][:120]}</td>
            <td>{p['confidence']}%</td>
            <td>{p['resolve_by']}</td>
            <td>{status}</td>
            <td>{outcome}</td>
        </tr>""")

    accuracy_str = f"{score['accuracy']}%" if score.get("accuracy") is not None else "No data"
    brier_str = f"{score['brier_score']}" if score.get("brier_score") is not None else "—"

    html = f"""<!DOCTYPE html>
<html><head>
<meta charset="UTF-8">
<title>Ainary Prediction Scorecard</title>
<style>
  body {{ font-family: Inter, -apple-system, sans-serif; max-width: 900px; margin: 0 auto; padding: 40px; background: #fafaf8; color: #333; }}
  h1 {{ font-size: 1.6rem; color: #1a1a1a; }}
  .gold {{ color: #c8aa50; }}
  .kpi-grid {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; margin: 24px 0; }}
  .kpi {{ background: #1a1a1a; color: #fff; padding: 20px; border-radius: 8px; text-align: center; }}
  .kpi-number {{ font-size: 2rem; font-weight: 600; color: #c8aa50; }}
  .kpi-label {{ font-size: 0.75rem; color: #888; margin-top: 4px; }}
  table {{ width: 100%; border-collapse: collapse; margin: 24px 0; font-size: 0.85rem; }}
  th {{ background: #1a1a1a; color: #fff; padding: 10px; text-align: left; }}
  td {{ padding: 10px; border-bottom: 1px solid #eee; }}
  .footer {{ margin-top: 40px; padding-top: 20px; border-top: 2px solid #1a1a1a; text-align: center; font-size: 0.8rem; color: #666; }}
</style>
</head><body>
<h1><span class="gold">●</span> Ainary Prediction Scorecard</h1>
<p>Publicly tracked, testable predictions from Ainary research reports.</p>

<div class="kpi-grid">
  <div class="kpi"><div class="kpi-number">{accuracy_str}</div><div class="kpi-label">Accuracy</div></div>
  <div class="kpi"><div class="kpi-number">{brier_str}</div><div class="kpi-label">Brier Score</div></div>
  <div class="kpi"><div class="kpi-number">{score.get('n_resolved', 0)}</div><div class="kpi-label">Resolved</div></div>
  <div class="kpi"><div class="kpi-number">{score.get('n_open', 0)}</div><div class="kpi-label">Open</div></div>
</div>

<table>
  <tr><th>ID</th><th>Prediction</th><th>Conf.</th><th>Resolve By</th><th>Status</th><th>Outcome</th></tr>
  {"".join(rows)}
</table>

<div class="footer">
  <strong>Ainary Ventures</strong><br>
  AI Strategy · System Design · Execution · Consultancy · Research<br>
  Updated: {datetime.now().strftime("%Y-%m-%d")}
</div>
</body></html>"""

    out = WORKSPACE / "research" / "prediction-scorecard.html"
    out.write_text(html)
    print(f"\nScorecard: {out}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: prediction_tracker.py [add|list|check|score|html]")
        sys.exit(1)

    cmd = sys.argv[1]
    if cmd == "add" and len(sys.argv) >= 4:
        pred = json.loads(sys.argv[3])
        add_prediction(sys.argv[2], pred)
    elif cmd == "list":
        list_predictions()
    elif cmd == "score":
        calculate_score()
    elif cmd == "html":
        generate_html()
    else:
        print("Usage: prediction_tracker.py [add|list|check|score|html]")
