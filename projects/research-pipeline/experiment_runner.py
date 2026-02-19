#!/usr/bin/env python3
"""
Pipeline Optimization Experiment Runner (v1.0)

Runs 50 controlled experiments to determine optimal research pipeline configuration.
Measures: Rubric Score, Claim Verification Rate, Novel Insight Score, Contradiction Detection.

Usage:
    # Run all phases sequentially
    python3 experiment_runner.py --run-all

    # Run single phase
    python3 experiment_runner.py --phase 1

    # Run single experiment
    python3 experiment_runner.py --run 1

    # Evaluate all completed runs
    python3 experiment_runner.py --evaluate

    # Show results dashboard
    python3 experiment_runner.py --results

    # Estimate cost before running
    python3 experiment_runner.py --estimate

Design: Sequential phases. Each phase uses results from previous.
Budget: ~$300 total for 50 runs.
"""

import argparse
import csv
import json
import os
import re
import statistics
import sys
import time
from dataclasses import dataclass, field, asdict
from datetime import datetime
from pathlib import Path
from typing import Optional, List, Dict, Any, Tuple

# Import from research_factory
sys.path.insert(0, str(Path(__file__).parent))
from research_factory import (
    create_intake, run_pipeline, run_hypothesis_pipeline,
    run_dialectic_pipeline, run_single_agent_pipeline,
    MODELS, compute_report_confidence, load_claims_from_json,
)

# --- Paths ---
WORKSPACE = Path(os.path.expanduser("~/.openclaw/workspace"))
EXPERIMENT_DIR = WORKSPACE / "research" / "experiments" / "pipeline-optimization"
RUNS_DIR = EXPERIMENT_DIR / "runs"
EVAL_DIR = EXPERIMENT_DIR / "evaluations"

# --- Constants ---
DEFAULT_TOPIC = "Trust Calibration for AI Agents"
STRESS_TOPICS = [
    "Agent Governance and Safety Frameworks",
    "EU AI Act Compliance for Enterprise AI Systems",
    "Autonomous Research Methods and Quality Assurance",
]

# Fixed evaluator model (never changes across experiments)
EVALUATOR_MODEL = "claude-sonnet-4-5-20250514"


# ============================================================
# EXPERIMENT DESIGN
# ============================================================

@dataclass
class ExperimentConfig:
    """Single experiment configuration."""
    run_id: int
    phase: int
    phase_name: str
    # Factors
    rag_timing: str         # "once" | "per_round" | "per_stage"
    architecture: str       # "single_1r" | "single_3r" | "hypo_5" | "dialectic"
    model_strategy: str     # "haiku" | "sonnet" | "mixed"
    feedback_loop: bool     # With/without reviewer feedback between rounds
    # Ablation (Phase 4)
    disable_component: str = ""  # "" | "assets" | "contradictions" | "claims" | "rubric" | "beipackzettel" | "source_policy"
    # Topic override (Phase 5)
    topic: str = DEFAULT_TOPIC
    # Metadata
    description: str = ""
    depends_on_phase: int = 0
    repetition: int = 1


def build_experiment_plan() -> List[ExperimentConfig]:
    """Build the full 50-run experiment plan."""
    runs = []
    run_id = 1

    # ─── Phase 1: BASELINES (8 runs) ───
    for rep in range(1, 3):
        runs.append(ExperimentConfig(
            run_id=run_id, phase=1, phase_name="Baselines",
            rag_timing="once", architecture="single_1r",
            model_strategy="sonnet", feedback_loop=False,
            description=f"Baseline: Sonnet, no feedback (rep {rep})",
            repetition=rep,
        ))
        run_id += 1

    for rep in range(1, 3):
        runs.append(ExperimentConfig(
            run_id=run_id, phase=1, phase_name="Baselines",
            rag_timing="once", architecture="single_1r",
            model_strategy="haiku", feedback_loop=False,
            description=f"Baseline: Haiku, no feedback (rep {rep})",
            repetition=rep,
        ))
        run_id += 1

    for rep in range(1, 3):
        runs.append(ExperimentConfig(
            run_id=run_id, phase=1, phase_name="Baselines",
            rag_timing="once", architecture="single_1r",
            model_strategy="sonnet", feedback_loop=True,
            description=f"Baseline: Sonnet + feedback (rep {rep})",
            repetition=rep,
        ))
        run_id += 1

    for rep in range(1, 3):
        runs.append(ExperimentConfig(
            run_id=run_id, phase=1, phase_name="Baselines",
            rag_timing="once", architecture="single_1r",
            model_strategy="mixed", feedback_loop=False,
            description=f"Baseline: Mixed model (rep {rep})",
            repetition=rep,
        ))
        run_id += 1

    # ─── Phase 2: RAG TIMING (9 runs) ───
    for rag in ["once", "per_round", "per_stage"]:
        for rep in range(1, 4):
            runs.append(ExperimentConfig(
                run_id=run_id, phase=2, phase_name="RAG Timing",
                rag_timing=rag, architecture="single_3r",
                model_strategy="BEST_FROM_P1", feedback_loop=True,
                description=f"RAG={rag}, iterative 3r (rep {rep})",
                depends_on_phase=1, repetition=rep,
            ))
            run_id += 1

    # ─── Phase 3: ARCHITECTURE (12 runs) ───
    for arch in ["single_1r", "single_3r", "hypo_5", "dialectic"]:
        for rep in range(1, 4):
            runs.append(ExperimentConfig(
                run_id=run_id, phase=3, phase_name="Architecture",
                rag_timing="BEST_FROM_P2", architecture=arch,
                model_strategy="BEST_FROM_P1", feedback_loop=True,
                description=f"Arch={arch} (rep {rep})",
                depends_on_phase=2, repetition=rep,
            ))
            run_id += 1

    # ─── Phase 4: ABLATION (12 runs) ───
    for component in ["assets", "contradictions", "claims", "rubric", "beipackzettel", "source_policy"]:
        for rep in range(1, 3):
            runs.append(ExperimentConfig(
                run_id=run_id, phase=4, phase_name="Ablation",
                rag_timing="BEST_FROM_P2", architecture="BEST_FROM_P3",
                model_strategy="BEST_FROM_P1", feedback_loop=True,
                disable_component=component,
                description=f"Ablation: without {component} (rep {rep})",
                depends_on_phase=3, repetition=rep,
            ))
            run_id += 1

    # ─── Phase 5: STRESS TESTS (9 runs) ───
    for topic in STRESS_TOPICS:
        for rep in range(1, 4):
            short = topic.split()[0]
            runs.append(ExperimentConfig(
                run_id=run_id, phase=5, phase_name="Stress Test",
                rag_timing="BEST_FROM_P2", architecture="BEST_FROM_P3",
                model_strategy="BEST_FROM_P1", feedback_loop=True,
                topic=topic,
                description=f"Stress: {short} (rep {rep})",
                depends_on_phase=3, repetition=rep,
            ))
            run_id += 1

    return runs


# ============================================================
# PRE-REGISTERED HYPOTHESES
# ============================================================

HYPOTHESES = [
    {
        "id": "H1",
        "claim": "Sonnet outperforms Haiku by >2 Rubric points on average",
        "confidence_prior": 0.85,
        "basis": "Model capability benchmarks (MMLU, HumanEval)",
        "phase": 1,
        "metric": "rubric_score",
        "test": "mean(sonnet) - mean(haiku) > 2",
    },
    {
        "id": "H2",
        "claim": "RAG after every stage > RAG once, by >1 Rubric point",
        "confidence_prior": 0.60,
        "basis": "Researcher analogy: revisiting literature improves depth",
        "phase": 2,
        "metric": "rubric_score",
        "test": "mean(per_stage) - mean(once) > 1",
    },
    {
        "id": "H3",
        "claim": "Dialectic (5 agents) outperforms Single Agent (3 rounds)",
        "confidence_prior": 0.55,
        "basis": "Uncertain: breadth may add noise vs depth",
        "phase": 3,
        "metric": "rubric_score",
        "test": "mean(dialectic) > mean(single_3r)",
    },
    {
        "id": "H4",
        "claim": "Feedback loop improves Rubric score by >1 point",
        "confidence_prior": 0.75,
        "basis": "Peer review literature shows iterative improvement",
        "phase": 1,
        "metric": "rubric_score",
        "test": "mean(feedback) - mean(no_feedback) > 1",
    },
    {
        "id": "H5",
        "claim": "Claim Ledger removal causes largest quality drop of any single component",
        "confidence_prior": 0.50,
        "basis": "Pure guess. Could also be Source Policy or Rubric.",
        "phase": 4,
        "metric": "rubric_score",
        "test": "drop(claims) > max(drop(others))",
    },
    {
        "id": "H6",
        "claim": "Best pipeline generalizes: <2 Rubric point variance across 4 topics",
        "confidence_prior": 0.65,
        "basis": "Templates are topic-agnostic, but RAG quality may vary",
        "phase": 5,
        "metric": "rubric_score",
        "test": "stdev(topic_means) < 2",
    },
]


# ============================================================
# MODEL CONFIGURATION
# ============================================================

MODEL_CONFIGS = {
    "haiku": {
        "stage1_producer": "claude-haiku-4-5-20250514",
        "stage1_reviewer": "claude-haiku-4-5-20250514",
        "stage2_assets": "claude-haiku-4-5-20250514",
        "stage3_integrate": "claude-haiku-4-5-20250514",
        "hypothesis_gen": "claude-haiku-4-5-20250514",
        "synthesis": "claude-haiku-4-5-20250514",
    },
    "sonnet": {
        "stage1_producer": "claude-sonnet-4-5-20250514",
        "stage1_reviewer": "claude-sonnet-4-5-20250514",
        "stage2_assets": "claude-sonnet-4-5-20250514",
        "stage3_integrate": "claude-sonnet-4-5-20250514",
        "hypothesis_gen": "claude-sonnet-4-5-20250514",
        "synthesis": "claude-sonnet-4-5-20250514",
    },
    "mixed": {
        "stage1_producer": "claude-sonnet-4-5-20250514",
        "stage1_reviewer": "claude-sonnet-4-5-20250514",
        "stage2_assets": "claude-haiku-4-5-20250514",
        "stage3_integrate": "claude-haiku-4-5-20250514",
        "hypothesis_gen": "claude-sonnet-4-5-20250514",
        "synthesis": "claude-sonnet-4-5-20250514",
    },
}

# Cost estimates per run (USD)
COST_ESTIMATES = {
    ("single_1r", "haiku"): 0.50,
    ("single_1r", "sonnet"): 3.00,
    ("single_1r", "mixed"): 2.00,
    ("single_3r", "haiku"): 1.50,
    ("single_3r", "sonnet"): 8.00,
    ("single_3r", "mixed"): 5.00,
    ("hypo_5", "haiku"): 3.00,
    ("hypo_5", "sonnet"): 15.00,
    ("hypo_5", "mixed"): 10.00,
    ("dialectic", "haiku"): 5.00,
    ("dialectic", "sonnet"): 25.00,
    ("dialectic", "mixed"): 15.00,
}


# ============================================================
# EVALUATOR (fixed, independent of experiment)
# ============================================================

EVALUATOR_PROMPT = """You are an independent research quality evaluator.
Score this report on 4 dimensions. Be harsh, calibrated, and consistent.

## RUBRIC

### 1. Rubric Score (0-16)
Score each dimension 0-2:
1) Decision alignment — Does the report answer the stated question?
2) Evidence discipline — Are citations present and verifiable?
3) Uncertainty integrity — Is confidence explicit? What changes the conclusion?
4) Contradictions handled — Are conflicts surfaced and explained?
5) Actionability — Are decision criteria + next steps clear?
6) Structure compliance — All required sections present?
7) Failure modes realism — Are risks REAL?
8) Risk mitigation — Recency, injection, bias controls?

### 2. Claim Verification Rate (0.0 - 1.0)
What fraction of factual claims in the report have a specific, verifiable source?
Count: claims_with_source / total_claims

### 3. Novel Insight Score (0-5)
0 = Nothing new, all common knowledge
1 = Mostly known, 1 minor new framing
2 = Some new connections between known ideas
3 = 1-2 genuinely new insights an expert might not know
4 = Multiple novel insights with evidence
5 = Paradigm-shifting finding with strong evidence

### 4. Contradiction Detection (count)
How many contradictions between sources/claims does the report:
a) Identify explicitly?
b) Attempt to resolve?

## OUTPUT FORMAT (JSON only)
```json
{
  "rubric_scores": {
    "decision_alignment": 0,
    "evidence_discipline": 0,
    "uncertainty_integrity": 0,
    "contradictions_handled": 0,
    "actionability": 0,
    "structure_compliance": 0,
    "failure_modes_realism": 0,
    "risk_mitigation": 0
  },
  "rubric_total": 0,
  "claim_verification_rate": 0.0,
  "novel_insight_score": 0,
  "contradictions_found": 0,
  "contradictions_resolved": 0,
  "evaluator_notes": "Brief justification for scores"
}
```

## REPORT TO EVALUATE
"""


def evaluate_report(report_text: str, client=None) -> Dict:
    """
    Run the fixed evaluator on a report.
    Returns standardized scores dict.
    """
    from research_factory import init_client, llm_call, API_BACKEND

    if client is None:
        client = init_client()

    prompt = EVALUATOR_PROMPT + report_text[:30000]
    text = llm_call(client, EVALUATOR_MODEL, prompt, max_tokens=1500)
    try:
        result = json.loads(re.search(r'\{.*\}', text, re.DOTALL).group())
    except Exception:
        result = {
            "rubric_total": 0,
            "claim_verification_rate": 0,
            "novel_insight_score": 0,
            "contradictions_found": 0,
            "contradictions_resolved": 0,
            "error": "Could not parse evaluator output",
            "raw": text[:500],
        }

    return result


# ============================================================
# EXPERIMENT RUNNER
# ============================================================

def resolve_best_from(plan: List[ExperimentConfig], phase: int,
                      factor: str) -> str:
    """
    Resolve BEST_FROM_P{N} placeholders using completed evaluation data.
    Reads scores.csv to find best configuration for a factor.
    """
    scores_path = EVAL_DIR / "scores.csv"
    if not scores_path.exists():
        # Default fallbacks
        defaults = {
            "model_strategy": "sonnet",
            "rag_timing": "per_round",
            "architecture": "single_3r",
        }
        return defaults.get(factor, "sonnet")

    # Read scores and find best
    with open(scores_path) as f:
        reader = csv.DictReader(f)
        rows = [r for r in reader if int(r.get("phase", 0)) == phase]

    if not rows:
        return "sonnet"  # fallback

    # Group by factor value, compute mean rubric_total
    from collections import defaultdict
    groups = defaultdict(list)
    for r in rows:
        key = r.get(factor, "unknown")
        try:
            groups[key].append(float(r.get("rubric_total", 0)))
        except ValueError:
            pass

    if not groups:
        return "sonnet"

    best = max(groups.items(), key=lambda x: statistics.mean(x[1]) if x[1] else 0)
    return best[0]


def resolve_config(config: ExperimentConfig,
                   plan: List[ExperimentConfig]) -> ExperimentConfig:
    """Resolve BEST_FROM_P{N} placeholders in a config."""
    c = ExperimentConfig(**asdict(config))

    if c.model_strategy.startswith("BEST_FROM"):
        c.model_strategy = resolve_best_from(plan, 1, "model_strategy")

    if c.rag_timing.startswith("BEST_FROM"):
        c.rag_timing = resolve_best_from(plan, 2, "rag_timing")

    if c.architecture.startswith("BEST_FROM"):
        c.architecture = resolve_best_from(plan, 3, "architecture")

    return c


def apply_model_config(strategy: str):
    """Override research_factory.MODELS with the given strategy."""
    import research_factory
    config = MODEL_CONFIGS.get(strategy, MODEL_CONFIGS["sonnet"])
    for key, value in config.items():
        research_factory.MODELS[key] = value
    # If using OpenAI backend, model names get mapped automatically via OPENAI_MODELS


def run_single_experiment(config: ExperimentConfig,
                          plan: List[ExperimentConfig]) -> Dict:
    """
    Execute a single experiment run.

    Returns: Dict with config + outputs + timing
    """
    resolved = resolve_config(config, plan)
    run_dir = RUNS_DIR / f"run-{config.run_id:02d}"
    run_dir.mkdir(parents=True, exist_ok=True)

    # Save config
    (run_dir / "config.json").write_text(json.dumps(asdict(resolved), indent=2))

    print(f"\n{'#' * 60}")
    print(f"# RUN {config.run_id:02d} | Phase {config.phase}: {config.phase_name}")
    print(f"# {config.description}")
    print(f"# Model: {resolved.model_strategy} | RAG: {resolved.rag_timing}")
    print(f"# Arch: {resolved.architecture} | Feedback: {resolved.feedback_loop}")
    if resolved.disable_component:
        print(f"# ABLATION: disabled={resolved.disable_component}")
    print(f"{'#' * 60}")

    # Apply model config
    apply_model_config(resolved.model_strategy)

    # Build intake
    intake = create_intake(
        resolved.topic,
        decision_to_inform="Optimal research pipeline configuration",
        decision_owner="Florian (Ainary)",
        audience="Researcher",
        risk_tier=2,
        freshness="last_12m",
        success_criteria=[
            "Comprehensive coverage of topic",
            "All claims sourced to Tier 1/2",
            "Contradictions identified and addressed",
            "Actionable recommendations",
        ],
    )

    # Apply ablation (disable component)
    if resolved.disable_component:
        intake["_ablation"] = resolved.disable_component
        # Components are disabled via intake instructions
        ablation_instructions = {
            "assets": "Do NOT produce an Asset Pack.",
            "contradictions": "Do NOT include a Contradiction Register.",
            "claims": "Do NOT include a Claim Ledger.",
            "rubric": "Do NOT include a Reviewer Rubric.",
            "beipackzettel": "Do NOT include a Beipackzettel.",
            "source_policy": "You may cite ANY source including blogs, tweets, and LLM outputs.",
        }
        intake["output_format_requirements"] = ablation_instructions.get(
            resolved.disable_component, "")

    start_time = time.time()

    try:
        # Route to correct pipeline
        if resolved.architecture == "single_1r":
            result = run_pipeline(intake, stages="1,2,3", output_dir=run_dir)

        elif resolved.architecture == "single_3r":
            result = run_single_agent_pipeline(
                intake, max_rounds=3, output_dir=run_dir)

        elif resolved.architecture == "hypo_5":
            result = run_hypothesis_pipeline(
                intake, n_hypotheses=5, output_dir=run_dir)

        elif resolved.architecture == "dialectic":
            result = run_dialectic_pipeline(
                intake, n_hypotheses=5, max_rounds=3, output_dir=run_dir)

        else:
            result = {"error": f"Unknown architecture: {resolved.architecture}"}

    except Exception as e:
        result = {"error": str(e)}
        print(f"  [ERROR] {e}")

    elapsed = time.time() - start_time

    # Save result
    run_result = {
        "run_id": config.run_id,
        "config": asdict(resolved),
        "elapsed_seconds": round(elapsed, 1),
        "timestamp": datetime.now().isoformat(),
        "result": result if not isinstance(result, dict) or "error" not in result else result,
    }
    (run_dir / "result.json").write_text(json.dumps(run_result, indent=2))

    print(f"  [Done] Run {config.run_id:02d} in {elapsed:.0f}s")
    return run_result


def evaluate_all_runs():
    """Evaluate all completed runs with the fixed evaluator."""
    from research_factory import init_client
    client = init_client()
    EVAL_DIR.mkdir(parents=True, exist_ok=True)

    scores = []
    run_dirs = sorted(RUNS_DIR.glob("run-*"))

    for run_dir in run_dirs:
        config_path = run_dir / "config.json"
        if not config_path.exists():
            continue

        config = json.loads(config_path.read_text())
        run_id = config.get("run_id", 0)

        # Find the report file
        report_text = ""
        for candidate in [
            "synthesis-report.md", "final-report.md", "report.md",
            # Check subdirs
        ]:
            p = run_dir / candidate
            if p.exists():
                report_text = p.read_text()
                break

        if not report_text:
            # Check round subdirs
            for rd in sorted(run_dir.glob("round-*"), reverse=True):
                rp = rd / "report.md"
                if rp.exists():
                    report_text = rp.read_text()
                    break

        if not report_text:
            print(f"  [SKIP] Run {run_id:02d}: no report found")
            continue

        # Check if already evaluated
        eval_path = EVAL_DIR / f"eval-{run_id:02d}.json"
        if eval_path.exists():
            evaluation = json.loads(eval_path.read_text())
            print(f"  [CACHED] Run {run_id:02d}: {evaluation.get('rubric_total', '?')}/16")
        else:
            print(f"  [EVAL] Run {run_id:02d}...")
            evaluation = evaluate_report(report_text, client)
            eval_path.write_text(json.dumps(evaluation, indent=2))
            print(f"  [DONE] Run {run_id:02d}: {evaluation.get('rubric_total', '?')}/16")

        # Combine config + evaluation
        row = {
            "run_id": run_id,
            "phase": config.get("phase", 0),
            "phase_name": config.get("phase_name", ""),
            "model_strategy": config.get("model_strategy", ""),
            "rag_timing": config.get("rag_timing", ""),
            "architecture": config.get("architecture", ""),
            "feedback_loop": config.get("feedback_loop", ""),
            "disable_component": config.get("disable_component", ""),
            "topic": config.get("topic", DEFAULT_TOPIC),
            "repetition": config.get("repetition", 1),
        }
        row.update(evaluation)
        scores.append(row)

    # Write CSV
    if scores:
        scores_path = EVAL_DIR / "scores.csv"
        fieldnames = list(scores[0].keys())
        with open(scores_path, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(scores)
        print(f"\n  Scores written to {scores_path} ({len(scores)} runs)")

    return scores


# ============================================================
# ANALYSIS
# ============================================================

def analyze_results():
    """Analyze experiment results and test hypotheses."""
    scores_path = EVAL_DIR / "scores.csv"
    if not scores_path.exists():
        print("No scores.csv found. Run --evaluate first.")
        return

    with open(scores_path) as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    if not rows:
        print("No data.")
        return

    print("\n" + "=" * 70)
    print("PIPELINE OPTIMIZATION EXPERIMENT — RESULTS")
    print("=" * 70)

    # Overview
    phases_done = set(int(r["phase"]) for r in rows)
    print(f"\nRuns completed: {len(rows)}")
    print(f"Phases completed: {sorted(phases_done)}")

    # Per-phase summary
    from collections import defaultdict
    phase_scores = defaultdict(list)
    for r in rows:
        try:
            phase_scores[int(r["phase"])].append(float(r.get("rubric_total", 0)))
        except (ValueError, KeyError):
            pass

    print(f"\n{'Phase':<20} {'N':>4} {'Mean':>6} {'StdDev':>7} {'Min':>5} {'Max':>5}")
    print("-" * 50)
    for phase in sorted(phase_scores.keys()):
        s = phase_scores[phase]
        mean = statistics.mean(s)
        sd = statistics.stdev(s) if len(s) > 1 else 0
        print(f"Phase {phase:<14} {len(s):>4} {mean:>6.1f} {sd:>7.2f} {min(s):>5.0f} {max(s):>5.0f}")

    # Factor analysis
    for factor in ["model_strategy", "rag_timing", "architecture"]:
        groups = defaultdict(list)
        for r in rows:
            key = r.get(factor, "?")
            if key and not key.startswith("BEST"):
                try:
                    groups[key].append(float(r.get("rubric_total", 0)))
                except ValueError:
                    pass

        if groups:
            print(f"\n--- {factor.upper()} ---")
            print(f"{'Value':<20} {'N':>4} {'Mean':>6} {'StdDev':>7}")
            print("-" * 40)
            for key in sorted(groups.keys()):
                s = groups[key]
                mean = statistics.mean(s)
                sd = statistics.stdev(s) if len(s) > 1 else 0
                print(f"{key:<20} {len(s):>4} {mean:>6.1f} {sd:>7.2f}")

    # Ablation analysis
    ablation_rows = [r for r in rows if r.get("disable_component")]
    if ablation_rows:
        print(f"\n--- ABLATION (component removed → impact) ---")
        # Get baseline (no ablation, same phase)
        baseline_rows = [r for r in rows
                         if int(r.get("phase", 0)) == 3 and not r.get("disable_component")]
        baseline_mean = statistics.mean(
            [float(r["rubric_total"]) for r in baseline_rows]
        ) if baseline_rows else 0

        abl_groups = defaultdict(list)
        for r in ablation_rows:
            try:
                abl_groups[r["disable_component"]].append(float(r["rubric_total"]))
            except ValueError:
                pass

        print(f"{'Component':<20} {'N':>4} {'Mean':>6} {'Drop':>6} {'Impact':>10}")
        print("-" * 50)
        for comp in sorted(abl_groups.keys()):
            s = abl_groups[comp]
            mean = statistics.mean(s)
            drop = baseline_mean - mean
            impact = "CRITICAL" if drop > 3 else "HIGH" if drop > 2 else "MEDIUM" if drop > 1 else "LOW"
            print(f"{comp:<20} {len(s):>4} {mean:>6.1f} {drop:>+6.1f} {impact:>10}")

    # Hypothesis testing
    print(f"\n--- HYPOTHESIS TESTS ---")
    for h in HYPOTHESES:
        phase = h["phase"]
        if phase not in phases_done:
            print(f"  {h['id']}: PENDING (Phase {phase} not yet run)")
            continue

        phase_rows = [r for r in rows if int(r.get("phase", 0)) == phase]
        # Simplified hypothesis testing (proper stats would use scipy)
        verdict = "INSUFFICIENT DATA"

        if h["id"] == "H1" and phase_rows:
            sonnet = [float(r["rubric_total"]) for r in phase_rows
                      if r.get("model_strategy") == "sonnet" and r.get("feedback_loop") == "False"]
            haiku = [float(r["rubric_total"]) for r in phase_rows
                     if r.get("model_strategy") == "haiku"]
            if sonnet and haiku:
                diff = statistics.mean(sonnet) - statistics.mean(haiku)
                verdict = f"{'CONFIRMED' if diff > 2 else 'REFUTED'} (delta={diff:.1f})"

        elif h["id"] == "H4" and phase_rows:
            fb_yes = [float(r["rubric_total"]) for r in phase_rows
                      if r.get("feedback_loop") == "True" and r.get("model_strategy") == "sonnet"]
            fb_no = [float(r["rubric_total"]) for r in phase_rows
                     if r.get("feedback_loop") == "False" and r.get("model_strategy") == "sonnet"]
            if fb_yes and fb_no:
                diff = statistics.mean(fb_yes) - statistics.mean(fb_no)
                verdict = f"{'CONFIRMED' if diff > 1 else 'REFUTED'} (delta={diff:.1f})"

        print(f"  {h['id']}: {h['claim'][:60]}")
        print(f"       Prior: {h['confidence_prior']:.0%} | Verdict: {verdict}")

    print()


def estimate_cost():
    """Estimate total experiment cost."""
    plan = build_experiment_plan()
    total = 0
    print(f"\n{'Phase':<20} {'Runs':>5} {'Est. Cost':>10}")
    print("-" * 40)

    from collections import defaultdict
    phase_costs = defaultdict(lambda: {"runs": 0, "cost": 0})

    for config in plan:
        # Resolve model strategy for cost estimation
        model = config.model_strategy
        if model.startswith("BEST"):
            model = "sonnet"  # assume sonnet for estimation

        arch = config.architecture
        if arch.startswith("BEST"):
            arch = "single_3r"  # assume mid-range

        cost = COST_ESTIMATES.get((arch, model), 5.0)
        phase_costs[config.phase_name]["runs"] += 1
        phase_costs[config.phase_name]["cost"] += cost
        total += cost

    for phase, data in phase_costs.items():
        print(f"{phase:<20} {data['runs']:>5} ${data['cost']:>8.0f}")

    eval_cost = len(plan) * 0.50
    print(f"{'Evaluation':<20} {len(plan):>5} ${eval_cost:>8.0f}")
    total += eval_cost

    print("-" * 40)
    print(f"{'TOTAL':<20} {len(plan):>5} ${total:>8.0f}")
    print(f"\nWith 30% buffer: ${total * 1.3:.0f}")


# ============================================================
# CLI
# ============================================================

def main():
    parser = argparse.ArgumentParser(
        description="Pipeline Optimization Experiment Runner",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--run-all", action="store_true",
                        help="Run all experiments sequentially")
    parser.add_argument("--phase", type=int,
                        help="Run all experiments in a specific phase (1-5)")
    parser.add_argument("--run", type=int,
                        help="Run a single experiment by ID (1-50)")
    parser.add_argument("--evaluate", action="store_true",
                        help="Evaluate all completed runs")
    parser.add_argument("--results", action="store_true",
                        help="Show results dashboard")
    parser.add_argument("--estimate", action="store_true",
                        help="Estimate cost before running")
    parser.add_argument("--plan", action="store_true",
                        help="Show experiment plan")
    parser.add_argument("--hypotheses", action="store_true",
                        help="Show pre-registered hypotheses")

    args = parser.parse_args()

    # Setup dirs
    RUNS_DIR.mkdir(parents=True, exist_ok=True)
    EVAL_DIR.mkdir(parents=True, exist_ok=True)

    plan = build_experiment_plan()

    if args.estimate:
        estimate_cost()
        return

    if args.plan:
        print(f"\n{'ID':>4} {'Ph':>3} {'Phase':<15} {'Arch':<12} {'Model':<8} "
              f"{'RAG':<12} {'FB':>3} {'Ablation':<15} {'Description'}")
        print("-" * 110)
        for c in plan:
            print(f"{c.run_id:>4} {c.phase:>3} {c.phase_name:<15} "
                  f"{c.architecture:<12} {c.model_strategy:<8} "
                  f"{c.rag_timing:<12} {'Y' if c.feedback_loop else 'N':>3} "
                  f"{c.disable_component or '-':<15} {c.description}")
        return

    if args.hypotheses:
        print("\nPRE-REGISTERED HYPOTHESES")
        print("=" * 60)
        for h in HYPOTHESES:
            print(f"\n{h['id']}: {h['claim']}")
            print(f"  Prior confidence: {h['confidence_prior']:.0%}")
            print(f"  Basis: {h['basis']}")
            print(f"  Phase: {h['phase']} | Metric: {h['metric']}")
            print(f"  Test: {h['test']}")
        return

    if args.evaluate:
        evaluate_all_runs()
        return

    if args.results:
        analyze_results()
        return

    if args.run:
        configs = [c for c in plan if c.run_id == args.run]
        if not configs:
            print(f"Run {args.run} not found in plan (1-{len(plan)})")
            return
        run_single_experiment(configs[0], plan)
        # Auto-evaluate
        print("\n[Auto-evaluating...]")
        evaluate_all_runs()
        return

    if args.phase:
        configs = [c for c in plan if c.phase == args.phase]
        if not configs:
            print(f"Phase {args.phase} not found")
            return
        print(f"\nRunning Phase {args.phase}: {configs[0].phase_name} ({len(configs)} runs)")
        for c in configs:
            run_single_experiment(c, plan)
        # Auto-evaluate
        print("\n[Auto-evaluating phase...]")
        evaluate_all_runs()
        analyze_results()
        return

    if args.run_all:
        print(f"\nRunning ALL {len(plan)} experiments...")
        for c in plan:
            run_single_experiment(c, plan)
            # Evaluate after each phase completes
            if c.run_id == max(x.run_id for x in plan if x.phase == c.phase):
                print(f"\n[Phase {c.phase} complete — evaluating...]")
                evaluate_all_runs()
                analyze_results()
        return

    parser.print_help()


if __name__ == "__main__":
    main()
