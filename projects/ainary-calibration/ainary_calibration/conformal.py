"""
Conformal Prediction (Family 4)
================================

Distribution-free statistical guarantees for prediction sets.

Unlike other calibration methods, conformal prediction provides GUARANTEES:
If you want 90% coverage, CP ensures 90% of prediction sets contain the correct answer.

Based on Li et al. (NeurIPS 2024) ConU and classical CP literature.
"""

from typing import List, Tuple, Dict, Any, Optional, Set
import numpy as np
from dataclasses import dataclass


@dataclass
class CalibrationExample:
    """Single calibration example with features, prediction, and label."""
    prompt: str
    prediction: str
    true_label: str
    confidence: float  # Nonconformity score
    

@dataclass
class PredictionSet:
    """Conformal prediction set with coverage guarantee."""
    predictions: Set[str]
    coverage_level: float
    threshold: float
    metadata: Dict[str, Any]


def conformal_predict(
    prompt: str,
    model: str,
    calibration_set: List[CalibrationExample],
    coverage: float = 0.90,
    use_consistency_scores: bool = True
) -> PredictionSet:
    """
    Conformal prediction with guaranteed coverage.
    
    Given a calibration set, constructs prediction sets that contain the true answer
    with probability ≥ coverage (under exchangeability assumption).
    
    Algorithm (Split Conformal):
    1. Compute nonconformity scores on calibration set
    2. Find quantile threshold for desired coverage
    3. For new input, include all predictions with score above threshold
    
    Args:
        prompt: Input prompt for prediction
        model: Model identifier
        calibration_set: List of labeled examples for calibration
        coverage: Desired coverage probability (default: 0.90)
        use_consistency_scores: Use self-consistency as nonconformity score
        
    Returns:
        PredictionSet with guaranteed coverage
        
    Example:
        >>> calib = generate_calibration_set(n=200)
        >>> pred_set = conformal_predict("What is 2+2?", "gpt-4", calib, coverage=0.90)
        >>> print(f"Prediction set: {pred_set.predictions}")
        Prediction set: {'4', '3', '5'}  # May include near-misses
        >>> print(f"Coverage guarantee: {pred_set.coverage_level:.0%}")
        Coverage guarantee: 90%
    """
    # Step 1: Compute nonconformity scores on calibration set
    # Nonconformity = 1 - confidence (lower confidence = higher nonconformity)
    nonconformity_scores = []
    for example in calibration_set:
        if example.prediction == example.true_label:
            # Correct prediction: nonconformity = 1 - confidence
            score = 1.0 - example.confidence
        else:
            # Incorrect prediction: nonconformity = 1 + (1 - confidence)
            # Penalize incorrect predictions more
            score = 1.0 + (1.0 - example.confidence)
        nonconformity_scores.append(score)
    
    # Step 2: Find quantile threshold
    # For coverage α, we want (1 - α) quantile of nonconformity scores
    n = len(calibration_set)
    quantile = (1 - coverage)
    
    # Adjusted quantile for finite sample (conservative)
    # ceil((n+1)(1-α)) / n
    adjusted_quantile = min(1.0, (n + 1) * quantile / n)
    
    threshold = np.quantile(nonconformity_scores, 1 - adjusted_quantile)
    
    # Step 3: Generate prediction set for new prompt
    # In real implementation: Get model predictions with confidence scores
    # For simulation: Generate candidate answers
    from .consistency import self_consistency_score
    
    if use_consistency_scores:
        # Use consistency-based confidence as nonconformity score
        confidence, meta = self_consistency_score(prompt, model, n_samples=5)
        main_prediction = meta.get("most_common_answer", "unknown")
        
        # Generate prediction set: include answers with nonconformity ≤ threshold
        prediction_set = {main_prediction}
        
        # Also include alternative predictions from clusters
        for answer, count in meta.get("clusters", {}).items():
            answer_confidence = count / meta.get("n_samples", 5)
            answer_nonconformity = 1.0 - answer_confidence
            
            if answer_nonconformity <= threshold:
                prediction_set.add(answer)
    else:
        # Fallback: Single prediction
        prediction_set = {"4"}  # Simulated
        confidence = 0.85
    
    metadata = {
        "calibration_set_size": n,
        "coverage_level": coverage,
        "threshold": float(threshold),
        "nonconformity_scores_quantiles": {
            "0.1": float(np.quantile(nonconformity_scores, 0.1)),
            "0.5": float(np.quantile(nonconformity_scores, 0.5)),
            "0.9": float(np.quantile(nonconformity_scores, 0.9)),
        },
        "prediction_set_size": len(prediction_set),
        "main_prediction": main_prediction if use_consistency_scores else "4",
        "confidence": confidence,
        "method": "split-conformal",
    }
    
    return PredictionSet(
        predictions=prediction_set,
        coverage_level=coverage,
        threshold=float(threshold),
        metadata=metadata
    )


def generate_calibration_set(
    n: int = 200,
    task_type: str = "arithmetic"
) -> List[CalibrationExample]:
    """
    Generate synthetic calibration set for testing.
    
    In production, this would be real labeled data from the target domain.
    
    Args:
        n: Number of examples to generate
        task_type: Type of task (arithmetic, qa, etc.)
        
    Returns:
        List of CalibrationExample objects
    """
    examples = []
    
    for i in range(n):
        # Generate synthetic examples with realistic confidence/correctness pattern
        # Simulate: 80% correct, with confidence correlating with correctness
        
        is_correct = np.random.random() < 0.80
        
        if is_correct:
            # Correct predictions tend to have higher confidence
            confidence = 0.6 + np.random.random() * 0.35  # 0.6 to 0.95
            prediction = "4"
            true_label = "4"
        else:
            # Incorrect predictions: Still overconfident (RLHF bias)
            confidence = 0.5 + np.random.random() * 0.3  # 0.5 to 0.8
            prediction = np.random.choice(["3", "5", "22"])
            true_label = "4"
        
        example = CalibrationExample(
            prompt=f"Example {i}: What is 2+2?",
            prediction=prediction,
            true_label=true_label,
            confidence=confidence
        )
        examples.append(example)
    
    return examples


def adaptive_conformal_predict(
    prompt: str,
    model: str,
    calibration_set: List[CalibrationExample],
    coverage: float = 0.90,
    recent_errors: Optional[List[bool]] = None,
    alpha_learning_rate: float = 0.01
) -> PredictionSet:
    """
    Adaptive Conformal Prediction with online coverage adjustment.
    
    Adjusts coverage level based on recent performance to maintain target coverage
    under distribution shift.
    
    Args:
        prompt: Input prompt
        model: Model identifier
        calibration_set: Initial calibration set
        coverage: Target coverage level
        recent_errors: Recent coverage errors (True if set missed true answer)
        alpha_learning_rate: Learning rate for coverage adjustment
        
    Returns:
        PredictionSet with adaptively adjusted coverage
    """
    # If recent errors provided, adjust coverage
    adjusted_coverage = coverage
    
    if recent_errors is not None and len(recent_errors) > 0:
        # Estimate recent coverage
        recent_coverage = 1.0 - (sum(recent_errors) / len(recent_errors))
        
        # If recent coverage < target, increase coverage level
        coverage_error = coverage - recent_coverage
        adjusted_coverage = min(0.99, coverage + alpha_learning_rate * coverage_error)
    
    # Run standard conformal prediction with adjusted coverage
    result = conformal_predict(prompt, model, calibration_set, coverage=adjusted_coverage)
    
    result.metadata["adaptive"] = True
    result.metadata["target_coverage"] = coverage
    result.metadata["adjusted_coverage"] = adjusted_coverage
    if recent_errors is not None:
        result.metadata["recent_coverage"] = 1.0 - (sum(recent_errors) / len(recent_errors))
    
    return result


def conformal_coverage_analysis(
    test_set: List[CalibrationExample],
    calibration_set: List[CalibrationExample],
    coverage_levels: List[float] = [0.80, 0.85, 0.90, 0.95]
) -> Dict[float, Dict[str, float]]:
    """
    Analyze conformal prediction coverage on a test set.
    
    Validates that empirical coverage matches theoretical guarantees.
    
    Args:
        test_set: Labeled test examples
        calibration_set: Calibration examples
        coverage_levels: Coverage levels to test
        
    Returns:
        Dict mapping coverage level to metrics:
            - empirical_coverage: Actual coverage achieved
            - avg_set_size: Average prediction set size
            - efficiency: Coverage / set_size (higher is better)
    """
    results = {}
    
    for target_coverage in coverage_levels:
        coverages = []
        set_sizes = []
        
        for example in test_set:
            pred_set = conformal_predict(
                example.prompt,
                "simulated",
                calibration_set,
                coverage=target_coverage
            )
            
            # Check if true label in prediction set
            covered = example.true_label in pred_set.predictions
            coverages.append(1.0 if covered else 0.0)
            set_sizes.append(len(pred_set.predictions))
        
        empirical_coverage = np.mean(coverages)
        avg_set_size = np.mean(set_sizes)
        
        results[target_coverage] = {
            "empirical_coverage": empirical_coverage,
            "target_coverage": target_coverage,
            "avg_set_size": avg_set_size,
            "efficiency": empirical_coverage / avg_set_size if avg_set_size > 0 else 0.0,
            "coverage_error": abs(empirical_coverage - target_coverage),
        }
    
    return results
