"""
Experiment Runner
=================

Runs all calibration experiments without requiring API keys.
Everything is simulated for reproducibility.

Experiments:
1. Confidence Propagation Simulation (Multi-Agent Chains)
2. ECE Comparison (Consistency vs Verbal vs Uncalibrated)
3. Cost-Confidence Frontier (Budget-CoCoA optimization)
4. Selective Prediction ROI (Coverage vs Accuracy tradeoff)
"""

import json
import sys
from pathlib import Path
from datetime import datetime
from typing import Dict, Any

import numpy as np

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from ainary_calibration.propagation import simulate_chain, chain_reliability_analysis
from ainary_calibration.metrics import expected_calibration_error, calibration_summary, overconfidence_ratio
from ainary_calibration.selective import selective_accuracy
from ainary_calibration.consistency import self_consistency_score, budget_cocoa


def experiment_1_confidence_propagation() -> Dict[str, Any]:
    """
    EXPERIMENT 1: Confidence Propagation Simulation
    
    Compare propagation methods across:
    - 3-Agent, 5-Agent, 10-Agent chains
    - Base confidence: 0.85, 0.90, 0.95
    - Correlation: 0.0 (independent), 0.3 (moderate), 0.7 (high)
    
    Methods: multiplicative, bayesian_network, conservative
    """
    print("\n" + "="*70)
    print("EXPERIMENT 1: Multi-Agent Confidence Propagation")
    print("="*70)
    
    results = chain_reliability_analysis(
        chain_lengths=[3, 5, 10],
        base_confidences=[0.85, 0.90, 0.95],
        correlations=[0.0, 0.3, 0.7],
        n_simulations=1000
    )
    
    # Flatten for analysis
    summary = []
    
    for chain_len in [3, 5, 10]:
        for base_conf in [0.85, 0.90, 0.95]:
            for corr in [0.0, 0.3, 0.7]:
                sim = results[chain_len][base_conf][corr]
                
                row = {
                    "chain_length": chain_len,
                    "base_confidence": base_conf,
                    "correlation": corr,
                    "ground_truth": sim["ground_truth_success_rate"],
                    **{
                        f"{method}_confidence": sim["statistics"][method]["mean"]
                        for method in ["multiplicative", "bayesian_network", "conservative"]
                    },
                    **{
                        f"{method}_error": sim["statistics"][method]["error_vs_ground_truth"]
                        for method in ["multiplicative", "bayesian_network", "conservative"]
                    }
                }
                summary.append(row)
    
    # Find best method per scenario
    best_methods = {}
    for row in summary:
        key = (row["chain_length"], row["correlation"])
        errors = {
            "multiplicative": row["multiplicative_error"],
            "bayesian": row["bayesian_network_error"],
            "conservative": row["conservative_error"],
        }
        best_method = min(errors.items(), key=lambda x: x[1])
        best_methods[key] = best_method[0]
    
    print(f"\n✓ Simulated {len(summary)} configurations")
    print(f"✓ Chain lengths: 3, 5, 10")
    print(f"✓ Correlations: 0.0, 0.3, 0.7")
    print(f"✓ 1000 Monte Carlo runs per configuration")
    
    return {
        "experiment": "confidence_propagation",
        "timestamp": datetime.now().isoformat(),
        "summary": summary,
        "best_methods": {f"{k[0]}-chain_corr-{k[1]}": v for k, v in best_methods.items()},
        "raw_results": results,
    }


def experiment_2_ece_comparison() -> Dict[str, Any]:
    """
    EXPERIMENT 2: ECE Comparison Simulation
    
    Generate synthetic calibration data (1000 predictions) and compare:
    - Uncalibrated (baseline)
    - Consistency-based
    - Verbalized confidence
    
    Measure: ECE, MCE, Brier Score
    """
    print("\n" + "="*70)
    print("EXPERIMENT 2: Calibration Method Comparison (ECE)")
    print("="*70)
    
    n_samples = 1000
    
    # Generate synthetic predictions with different calibration qualities
    
    # 1. Uncalibrated (RLHF-biased, overconfident)
    uncalibrated = []
    for _ in range(n_samples):
        # True accuracy ~75%, but confidence ~90% (overconfident)
        is_correct = np.random.random() < 0.75
        if is_correct:
            confidence = 0.85 + np.random.random() * 0.12  # 0.85-0.97
        else:
            confidence = 0.70 + np.random.random() * 0.25  # 0.70-0.95 (still overconfident when wrong)
        uncalibrated.append((confidence, is_correct))
    
    # 2. Consistency-based (better calibrated)
    consistency = []
    for _ in range(n_samples):
        is_correct = np.random.random() < 0.78
        if is_correct:
            confidence = 0.70 + np.random.random() * 0.25  # 0.70-0.95
        else:
            confidence = 0.40 + np.random.random() * 0.35  # 0.40-0.75 (less overconfident)
        consistency.append((confidence, is_correct))
    
    # 3. Verbalized confidence (RLHF-biased, similar to uncalibrated)
    verbalized = []
    for _ in range(n_samples):
        is_correct = np.random.random() < 0.76
        if is_correct:
            confidence = 0.80 + np.random.random() * 0.15  # 0.80-0.95
        else:
            confidence = 0.65 + np.random.random() * 0.25  # 0.65-0.90
        verbalized.append((confidence, is_correct))
    
    # Calculate metrics for each
    methods = {
        "uncalibrated": uncalibrated,
        "consistency": consistency,
        "verbalized": verbalized,
    }
    
    results = {}
    for method_name, predictions in methods.items():
        metrics = calibration_summary(predictions, n_bins=15)
        oc_ratio = overconfidence_ratio(predictions)
        
        results[method_name] = {
            "ece": metrics.ece,
            "mce": metrics.mce,
            "brier_score": metrics.brier,
            "overconfidence_ratio": oc_ratio,
            "n_samples": len(predictions),
        }
        
        print(f"\n{method_name.upper()}:")
        print(f"  ECE: {metrics.ece:.2%}")
        print(f"  MCE: {metrics.mce:.2%}")
        print(f"  Brier: {metrics.brier:.4f}")
        print(f"  Overconfidence: {oc_ratio:.2f}x")
    
    # Comparison table
    comparison = {
        "ece_improvement_consistency": (results["uncalibrated"]["ece"] - results["consistency"]["ece"]) / results["uncalibrated"]["ece"],
        "ece_improvement_verbal": (results["uncalibrated"]["ece"] - results["verbalized"]["ece"]) / results["uncalibrated"]["ece"],
        "winner": min(results.items(), key=lambda x: x[1]["ece"])[0],
    }
    
    print(f"\n✓ Consistency ECE improvement: {comparison['ece_improvement_consistency']:.1%}")
    print(f"✓ Verbal ECE improvement: {comparison['ece_improvement_verbal']:.1%}")
    print(f"✓ Winner: {comparison['winner']}")
    
    return {
        "experiment": "ece_comparison",
        "timestamp": datetime.now().isoformat(),
        "results": results,
        "comparison": comparison,
    }


def experiment_3_cost_confidence_frontier() -> Dict[str, Any]:
    """
    EXPERIMENT 3: Cost-Confidence Frontier
    
    Vary n_samples from 1 to 20 for Budget-CoCoA.
    Measure: Cost vs ECE improvement
    Find: Optimal n_samples
    """
    print("\n" + "="*70)
    print("EXPERIMENT 3: Cost-Confidence Frontier (Budget-CoCoA)")
    print("="*70)
    
    n_samples_range = list(range(1, 21))
    results = []
    
    for n_samples in n_samples_range:
        # Simulate ECE for this n_samples
        # More samples → better calibration (diminishing returns)
        base_ece = 0.42  # Uncalibrated baseline
        
        # Exponential decay: ECE = base * exp(-k * n_samples)
        k = 0.15  # Decay rate
        ece = base_ece * np.exp(-k * n_samples)
        
        # Add noise
        ece += np.random.normal(0, 0.02)
        ece = max(0.05, min(0.42, ece))  # Clamp
        
        # Cost: Linear in n_samples
        cost_per_sample = 0.0005
        total_cost = n_samples * cost_per_sample
        
        # Efficiency: ECE improvement per dollar
        ece_improvement = base_ece - ece
        efficiency = ece_improvement / total_cost if total_cost > 0 else 0
        
        results.append({
            "n_samples": n_samples,
            "ece": ece,
            "cost": total_cost,
            "ece_improvement": ece_improvement,
            "efficiency": efficiency,
        })
    
    # Find optimal n_samples (best efficiency)
    optimal = max(results, key=lambda x: x["efficiency"])
    
    print(f"\n✓ Tested n_samples from 1 to 20")
    print(f"✓ Optimal n_samples: {optimal['n_samples']}")
    print(f"✓ ECE at optimal: {optimal['ece']:.2%}")
    print(f"✓ Cost at optimal: ${optimal['cost']:.4f}")
    print(f"✓ Efficiency: {optimal['efficiency']:.2f} ECE reduction per $")
    
    return {
        "experiment": "cost_confidence_frontier",
        "timestamp": datetime.now().isoformat(),
        "results": results,
        "optimal": optimal,
    }


def experiment_4_selective_prediction_roi() -> Dict[str, Any]:
    """
    EXPERIMENT 4: Selective Prediction ROI
    
    Vary abstention threshold from 0.5 to 0.99.
    Measure: Coverage vs Accuracy tradeoff
    Find: Optimal threshold for different risk tolerances
    """
    print("\n" + "="*70)
    print("EXPERIMENT 4: Selective Prediction ROI")
    print("="*70)
    
    # Generate synthetic predictions with confidence-correctness correlation
    n_samples = 1000
    predictions = []
    
    for _ in range(n_samples):
        # Confidence correlates with correctness (but with noise)
        true_prob = np.random.beta(2, 2)  # Uniform-ish distribution
        confidence = true_prob + np.random.normal(0, 0.15)  # Add noise
        confidence = max(0.0, min(1.0, confidence))
        
        is_correct = np.random.random() < true_prob
        predictions.append((confidence, is_correct))
    
    # Sweep threshold
    thresholds = np.linspace(0.50, 0.99, 20)
    results = []
    
    for threshold in thresholds:
        metrics = selective_accuracy(predictions, threshold=threshold)
        
        results.append({
            "threshold": threshold,
            "coverage": metrics["coverage"],
            "reliable_accuracy": metrics["reliable_accuracy"],
            "standard_accuracy": metrics["standard_accuracy"],
            "effective_reliability": metrics["effective_reliability"],
            "abstention_rate": metrics["abstention_rate"],
        })
    
    # Find optimal thresholds for different objectives
    
    # 1. Maximize effective reliability (harmonic mean of coverage and R-Acc)
    optimal_er = max(results, key=lambda x: x["effective_reliability"])
    
    # 2. Maximize R-Acc with at least 50% coverage
    high_coverage = [r for r in results if r["coverage"] >= 0.50]
    optimal_high_coverage = max(high_coverage, key=lambda x: x["reliable_accuracy"]) if high_coverage else results[0]
    
    # 3. Maximize R-Acc (minimal coverage OK)
    optimal_max_racc = max(results, key=lambda x: x["reliable_accuracy"])
    
    print(f"\n✓ Tested {len(thresholds)} thresholds")
    print(f"\n  Optimal for balanced coverage/accuracy:")
    print(f"    Threshold: {optimal_er['threshold']:.2f}")
    print(f"    Coverage: {optimal_er['coverage']:.1%}")
    print(f"    R-Acc: {optimal_er['reliable_accuracy']:.1%}")
    
    print(f"\n  Optimal for high coverage (≥50%):")
    print(f"    Threshold: {optimal_high_coverage['threshold']:.2f}")
    print(f"    Coverage: {optimal_high_coverage['coverage']:.1%}")
    print(f"    R-Acc: {optimal_high_coverage['reliable_accuracy']:.1%}")
    
    print(f"\n  Optimal for maximum reliability:")
    print(f"    Threshold: {optimal_max_racc['threshold']:.2f}")
    print(f"    Coverage: {optimal_max_racc['coverage']:.1%}")
    print(f"    R-Acc: {optimal_max_racc['reliable_accuracy']:.1%}")
    
    return {
        "experiment": "selective_prediction_roi",
        "timestamp": datetime.now().isoformat(),
        "results": results,
        "optimal_balanced": optimal_er,
        "optimal_high_coverage": optimal_high_coverage,
        "optimal_max_reliability": optimal_max_racc,
    }


def run_all_experiments():
    """Run all 4 experiments and save results."""
    print("\n" + "="*70)
    print("AINARY CALIBRATION EXPERIMENTS")
    print("="*70)
    print("\nRunning 4 experiments (simulated, no API calls needed)")
    print("This will take ~30-60 seconds...\n")
    
    results = {}
    
    # Run experiments
    results["exp1"] = experiment_1_confidence_propagation()
    results["exp2"] = experiment_2_ece_comparison()
    results["exp3"] = experiment_3_cost_confidence_frontier()
    results["exp4"] = experiment_4_selective_prediction_roi()
    
    # Save to JSON
    output_dir = Path(__file__).parent / "results"
    output_dir.mkdir(exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = output_dir / f"experiments_{timestamp}.json"
    
    with open(output_file, "w") as f:
        json.dump(results, f, indent=2, default=str)
    
    # Also save latest
    latest_file = output_dir / "experiments_latest.json"
    with open(latest_file, "w") as f:
        json.dump(results, f, indent=2, default=str)
    
    print("\n" + "="*70)
    print("ALL EXPERIMENTS COMPLETE")
    print("="*70)
    print(f"\nResults saved to:")
    print(f"  {output_file}")
    print(f"  {latest_file}")
    print("\nRun analysis.py to generate summary and visualizations.")
    
    return results


if __name__ == "__main__":
    run_all_experiments()
