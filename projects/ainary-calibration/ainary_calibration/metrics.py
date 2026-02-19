"""
Calibration Metrics
===================

ECE, MCE, Brier Score, and Reliability Diagrams for evaluating calibration quality.

Based on Guo et al. (ICML 2017) and calibration literature.
"""

from typing import List, Tuple, Dict, Any, Optional
import numpy as np
from dataclasses import dataclass


@dataclass
class CalibrationMetrics:
    """Container for calibration metrics."""
    ece: float  # Expected Calibration Error
    mce: float  # Maximum Calibration Error
    brier: float  # Brier Score
    n_bins: int
    bin_stats: List[Dict[str, float]]
    
    
def expected_calibration_error(
    predictions: List[Tuple[float, bool]],
    n_bins: int = 15
) -> Tuple[float, List[Dict[str, float]]]:
    """
    Calculate Expected Calibration Error (ECE).
    
    ECE measures average difference between confidence and accuracy across bins.
    Lower is better. Perfect calibration = 0.0.
    
    Typical values:
    - Uncalibrated LLMs: 30-45% ECE
    - Verbalized confidence: 35-42% ECE
    - Self-consistency: 20-30% ECE
    - Temperature scaling: 2-5% ECE (white-box only)
    
    Formula:
    ECE = Σ (|B_i| / n) * |acc(B_i) - conf(B_i)|
    where B_i is the i-th confidence bin.
    
    Args:
        predictions: List of (confidence, is_correct) tuples
        n_bins: Number of bins (default: 15, following Guo et al. 2017)
        
    Returns:
        Tuple of (ece: float, bin_stats: List[Dict])
        
    Example:
        >>> preds = [(0.9, True), (0.8, True), (0.6, False), (0.95, True)]
        >>> ece, bins = expected_calibration_error(preds)
        >>> print(f"ECE: {ece:.2%}")
        ECE: 8.33%
    """
    if not predictions:
        return 0.0, []
    
    n = len(predictions)
    
    # Create bins
    bin_edges = np.linspace(0, 1, n_bins + 1)
    bin_stats = []
    total_ece = 0.0
    
    for i in range(n_bins):
        bin_lower = bin_edges[i]
        bin_upper = bin_edges[i + 1]
        
        # Predictions in this bin
        in_bin = [
            (conf, correct) for conf, correct in predictions
            if bin_lower <= conf < bin_upper or (i == n_bins - 1 and conf == bin_upper)
        ]
        
        if not in_bin:
            # Empty bin
            bin_stats.append({
                "bin_lower": bin_lower,
                "bin_upper": bin_upper,
                "count": 0,
                "avg_confidence": 0.0,
                "accuracy": 0.0,
                "calibration_error": 0.0,
            })
            continue
        
        # Compute bin statistics
        confidences = [conf for conf, _ in in_bin]
        corrects = [correct for _, correct in in_bin]
        
        avg_confidence = np.mean(confidences)
        accuracy = np.mean(corrects)
        calibration_error = abs(avg_confidence - accuracy)
        
        # Weight by bin size
        bin_weight = len(in_bin) / n
        total_ece += bin_weight * calibration_error
        
        bin_stats.append({
            "bin_lower": bin_lower,
            "bin_upper": bin_upper,
            "count": len(in_bin),
            "avg_confidence": float(avg_confidence),
            "accuracy": float(accuracy),
            "calibration_error": float(calibration_error),
        })
    
    return float(total_ece), bin_stats


def maximum_calibration_error(
    predictions: List[Tuple[float, bool]],
    n_bins: int = 15
) -> Tuple[float, int]:
    """
    Calculate Maximum Calibration Error (MCE).
    
    MCE is the worst-case calibration error across all bins.
    Measures maximum deviation between confidence and accuracy.
    
    Args:
        predictions: List of (confidence, is_correct) tuples
        n_bins: Number of bins
        
    Returns:
        Tuple of (mce: float, worst_bin_index: int)
        
    Example:
        >>> preds = [(0.9, False), (0.9, False), (0.1, True), (0.1, True)]
        >>> mce, worst_bin = maximum_calibration_error(preds)
        >>> print(f"MCE: {mce:.2%}")
        MCE: 90.00%  # Bin at 0.9 has 0% accuracy
    """
    if not predictions:
        return 0.0, -1
    
    _, bin_stats = expected_calibration_error(predictions, n_bins)
    
    # Find bin with maximum calibration error
    max_error = 0.0
    worst_bin = -1
    
    for i, bin_stat in enumerate(bin_stats):
        if bin_stat["count"] > 0 and bin_stat["calibration_error"] > max_error:
            max_error = bin_stat["calibration_error"]
            worst_bin = i
    
    return float(max_error), worst_bin


def brier_score(
    predictions: List[Tuple[float, bool]]
) -> float:
    """
    Calculate Brier Score.
    
    Brier Score measures mean squared difference between predicted probabilities
    and actual outcomes. Lower is better. Range: [0, 1].
    
    Perfect predictions: 0.0
    Random predictions: 0.25 (for binary)
    
    Formula:
    BS = (1/n) Σ (p_i - y_i)^2
    where p_i is predicted probability and y_i is actual outcome (0 or 1).
    
    Args:
        predictions: List of (confidence, is_correct) tuples
        
    Returns:
        Brier score (float)
        
    Example:
        >>> preds = [(0.9, True), (0.8, True), (0.3, False), (0.2, False)]
        >>> bs = brier_score(preds)
        >>> print(f"Brier Score: {bs:.4f}")
        Brier Score: 0.0175  # Very well calibrated
    """
    if not predictions:
        return 0.0
    
    squared_errors = [
        (conf - (1.0 if correct else 0.0)) ** 2
        for conf, correct in predictions
    ]
    
    return float(np.mean(squared_errors))


def reliability_diagram(
    predictions: List[Tuple[float, bool]],
    n_bins: int = 10,
    output_format: str = "ascii"
) -> str:
    """
    Generate reliability diagram (calibration plot).
    
    Plots predicted confidence (x-axis) vs. actual accuracy (y-axis).
    Perfect calibration = diagonal line (y = x).
    
    Args:
        predictions: List of (confidence, is_correct) tuples
        n_bins: Number of bins
        output_format: "ascii" (text) or "data" (return data for plotting)
        
    Returns:
        ASCII diagram or plot data as string
        
    Example:
        >>> preds = [(0.9, True), (0.8, True), (0.7, False), (0.6, True)]
        >>> print(reliability_diagram(preds, n_bins=5))
        Reliability Diagram
        ===================
        1.0|                    *
        0.8|              *
        0.6|         
        0.4|
        0.2|
        0.0+----+----+----+----+
           0.0  0.2  0.4  0.6  0.8  1.0
                Confidence →
    """
    if output_format == "data":
        # Return data for external plotting
        _, bin_stats = expected_calibration_error(predictions, n_bins)
        data = {
            "bins": [
                {
                    "confidence": (b["bin_lower"] + b["bin_upper"]) / 2,
                    "accuracy": b["accuracy"],
                    "count": b["count"],
                }
                for b in bin_stats if b["count"] > 0
            ]
        }
        return str(data)
    
    # ASCII diagram
    _, bin_stats = expected_calibration_error(predictions, n_bins)
    
    # Build ASCII plot
    height = 10
    width = 50
    
    diagram = ["Reliability Diagram", "=" * 20, ""]
    
    # Y-axis (accuracy)
    for y in range(height, -1, -1):
        acc_val = y / height
        line = f"{acc_val:.1f}|"
        
        # Plot points
        for bin_stat in bin_stats:
            if bin_stat["count"] == 0:
                continue
            
            bin_mid = (bin_stat["bin_lower"] + bin_stat["bin_upper"]) / 2
            bin_acc = bin_stat["accuracy"]
            
            # Map to character position
            x_pos = int(bin_mid * width)
            y_pos = int(bin_acc * height)
            
            if y == y_pos:
                # Add spacing
                while len(line) < x_pos + 5:
                    line += " "
                line += "*"
        
        diagram.append(line)
    
    # X-axis
    diagram.append(" 0.0+" + "-" * width)
    diagram.append("     " + " ".join(f"{i/10:.1f}" for i in range(0, 11, 2)))
    diagram.append(" " * 10 + "Confidence →")
    
    return "\n".join(diagram)


def calibration_summary(
    predictions: List[Tuple[float, bool]],
    n_bins: int = 15
) -> CalibrationMetrics:
    """
    Compute all calibration metrics in one call.
    
    Args:
        predictions: List of (confidence, is_correct) tuples
        n_bins: Number of bins for ECE/MCE
        
    Returns:
        CalibrationMetrics object
        
    Example:
        >>> preds = [(0.9, True), (0.8, True), (0.6, False)]
        >>> metrics = calibration_summary(preds)
        >>> print(f"ECE: {metrics.ece:.2%}, Brier: {metrics.brier:.4f}")
        ECE: 16.67%, Brier: 0.0467
    """
    ece, bin_stats = expected_calibration_error(predictions, n_bins)
    mce, _ = maximum_calibration_error(predictions, n_bins)
    brier = brier_score(predictions)
    
    return CalibrationMetrics(
        ece=ece,
        mce=mce,
        brier=brier,
        n_bins=n_bins,
        bin_stats=bin_stats
    )


def overconfidence_ratio(
    predictions: List[Tuple[float, bool]]
) -> float:
    """
    Calculate overconfidence ratio.
    
    Ratio of average confidence to average accuracy.
    - Ratio > 1.0 = overconfident
    - Ratio < 1.0 = underconfident
    - Ratio = 1.0 = perfectly calibrated (on average)
    
    Typical RLHF models: 1.15 to 1.30 (15-30% overconfident).
    
    Args:
        predictions: List of (confidence, is_correct) tuples
        
    Returns:
        Overconfidence ratio (float)
    """
    if not predictions:
        return 1.0
    
    avg_confidence = np.mean([conf for conf, _ in predictions])
    avg_accuracy = np.mean([1.0 if correct else 0.0 for _, correct in predictions])
    
    if avg_accuracy == 0:
        return float('inf')
    
    return float(avg_confidence / avg_accuracy)


def calibration_curve_data(
    predictions: List[Tuple[float, bool]],
    n_bins: int = 10
) -> Dict[str, List[float]]:
    """
    Extract calibration curve data for plotting.
    
    Returns x and y coordinates for reliability diagram.
    
    Args:
        predictions: List of (confidence, is_correct) tuples
        n_bins: Number of bins
        
    Returns:
        Dict with keys:
            - confidence: List of bin midpoints (x-axis)
            - accuracy: List of accuracies per bin (y-axis)
            - counts: List of sample counts per bin
            - perfect: Perfect calibration line (y = x)
    """
    _, bin_stats = expected_calibration_error(predictions, n_bins)
    
    confidence = []
    accuracy = []
    counts = []
    
    for bin_stat in bin_stats:
        if bin_stat["count"] > 0:
            bin_mid = (bin_stat["bin_lower"] + bin_stat["bin_upper"]) / 2
            confidence.append(bin_mid)
            accuracy.append(bin_stat["accuracy"])
            counts.append(bin_stat["count"])
    
    return {
        "confidence": confidence,
        "accuracy": accuracy,
        "counts": counts,
        "perfect": confidence,  # y = x line
    }
