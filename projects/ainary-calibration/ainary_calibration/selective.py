"""
Selective Prediction / Abstention (Family 6)
=============================================

Instead of calibrating bad predictions, refuse to predict when uncertain.

Based on SelectLLM (ICLR 2025) and "Know Your Limits" survey (TACL 2025).
Most pragmatic approach for production agent systems.
"""

from typing import Tuple, Dict, Any, Optional, Literal
from dataclasses import dataclass
from enum import Enum


class RouteDecision(str, Enum):
    """Routing decision based on confidence."""
    AUTO = "auto"           # High confidence: Execute automatically
    REVIEW = "review"       # Medium confidence: Human review recommended
    ESCALATE = "escalate"   # Low confidence: Escalate to expert/better model
    ABSTAIN = "abstain"     # Very low confidence: Refuse to answer


@dataclass
class SelectionResult:
    """Result of selective prediction."""
    should_answer: bool
    route: RouteDecision
    confidence: float
    reason: str
    metadata: Dict[str, Any]


def should_abstain(
    confidence: float,
    threshold: float = 0.60,
    task_risk: Literal["low", "medium", "high"] = "medium"
) -> Tuple[bool, str]:
    """
    Determine if model should abstain from answering.
    
    Based on "Know Your Limits" (TACL 2025) abstention framework.
    
    Args:
        confidence: Confidence score (0.0 to 1.0)
        threshold: Minimum confidence to answer (default: 0.60)
        task_risk: Risk level of the task (adjusts threshold)
        
    Returns:
        Tuple of (should_abstain: bool, reason: str)
        
    Example:
        >>> abstain, reason = should_abstain(0.45, threshold=0.60)
        >>> print(abstain, reason)
        True "Confidence (0.45) below threshold (0.60)"
    """
    # Adjust threshold based on task risk
    risk_adjustments = {
        "low": -0.15,     # Lower bar for low-risk tasks
        "medium": 0.0,    # Default threshold
        "high": +0.20,    # Higher bar for high-risk tasks
    }
    
    adjusted_threshold = threshold + risk_adjustments.get(task_risk, 0.0)
    adjusted_threshold = max(0.0, min(1.0, adjusted_threshold))  # Clamp to [0, 1]
    
    if confidence < adjusted_threshold:
        reason = f"Confidence ({confidence:.2f}) below {task_risk}-risk threshold ({adjusted_threshold:.2f})"
        return True, reason
    else:
        reason = f"Confidence ({confidence:.2f}) above threshold ({adjusted_threshold:.2f})"
        return False, reason


def route_by_confidence(
    confidence: float,
    thresholds: Optional[Dict[str, float]] = None,
    task_risk: Literal["low", "medium", "high"] = "medium"
) -> SelectionResult:
    """
    Route decision based on confidence level (multi-tier routing).
    
    Amazon's cascading ensembles (2024) reduced calibration error by 46% using
    confidence-based routing: high confidence → cheap model, low → expensive model.
    
    Default thresholds:
    - AUTO (>0.85): Execute automatically
    - REVIEW (0.60-0.85): Human review recommended
    - ESCALATE (0.40-0.60): Escalate to more capable model
    - ABSTAIN (<0.40): Refuse to answer
    
    Thresholds adjust based on task risk.
    
    Args:
        confidence: Confidence score
        thresholds: Custom thresholds (default: see above)
        task_risk: Risk level (adjusts thresholds)
        
    Returns:
        SelectionResult with routing decision
        
    Example:
        >>> result = route_by_confidence(0.92, task_risk="high")
        >>> print(result.route)
        RouteDecision.AUTO
        >>> result = route_by_confidence(0.50, task_risk="high")
        >>> print(result.route)
        RouteDecision.ESCALATE
    """
    # Default thresholds
    if thresholds is None:
        thresholds = {
            "auto": 0.85,
            "review": 0.60,
            "escalate": 0.40,
        }
    
    # Adjust for risk level
    risk_adjustments = {
        "low": -0.15,
        "medium": 0.0,
        "high": +0.15,
    }
    adjustment = risk_adjustments.get(task_risk, 0.0)
    
    adjusted_thresholds = {
        k: max(0.0, min(1.0, v + adjustment))
        for k, v in thresholds.items()
    }
    
    # Determine route
    if confidence >= adjusted_thresholds["auto"]:
        route = RouteDecision.AUTO
        should_answer = True
        reason = f"High confidence ({confidence:.2%}) → automatic execution"
    elif confidence >= adjusted_thresholds["review"]:
        route = RouteDecision.REVIEW
        should_answer = True
        reason = f"Medium confidence ({confidence:.2%}) → human review recommended"
    elif confidence >= adjusted_thresholds["escalate"]:
        route = RouteDecision.ESCALATE
        should_answer = False
        reason = f"Low confidence ({confidence:.2%}) → escalate to more capable model"
    else:
        route = RouteDecision.ABSTAIN
        should_answer = False
        reason = f"Very low confidence ({confidence:.2%}) → abstain from answering"
    
    metadata = {
        "confidence": confidence,
        "task_risk": task_risk,
        "adjusted_thresholds": adjusted_thresholds,
        "original_thresholds": thresholds,
    }
    
    return SelectionResult(
        should_answer=should_answer,
        route=route,
        confidence=confidence,
        reason=reason,
        metadata=metadata
    )


def selective_accuracy(
    predictions: list[Tuple[float, bool]],
    threshold: float = 0.60
) -> Dict[str, float]:
    """
    Calculate selective prediction metrics.
    
    Metrics from "Know Your Limits" (TACL 2025):
    - Coverage: % of examples answered
    - Reliable Accuracy (R-Acc): Of answered examples, % correct
    - Effective Reliability (ER): Balance between coverage and reliability
    
    Args:
        predictions: List of (confidence, is_correct) tuples
        threshold: Abstention threshold
        
    Returns:
        Dict with metrics:
            - coverage: % answered
            - reliable_accuracy: % correct among answered
            - standard_accuracy: % correct overall (treating abstentions as wrong)
            - effective_reliability: Harmonic mean of coverage and R-Acc
            - abstention_rate: % abstained
            
    Example:
        >>> preds = [(0.9, True), (0.5, False), (0.8, True), (0.3, False)]
        >>> metrics = selective_accuracy(preds, threshold=0.60)
        >>> print(f"Coverage: {metrics['coverage']:.1%}")
        Coverage: 50.0%
        >>> print(f"R-Acc: {metrics['reliable_accuracy']:.1%}")
        R-Acc: 100.0%
    """
    total = len(predictions)
    if total == 0:
        return {
            "coverage": 0.0,
            "reliable_accuracy": 0.0,
            "standard_accuracy": 0.0,
            "effective_reliability": 0.0,
            "abstention_rate": 0.0,
        }
    
    # Separate answered vs abstained
    answered = [(conf, correct) for conf, correct in predictions if conf >= threshold]
    abstained = [(conf, correct) for conf, correct in predictions if conf < threshold]
    
    coverage = len(answered) / total
    abstention_rate = len(abstained) / total
    
    # Reliable Accuracy: Of answered, how many correct?
    if answered:
        r_acc = sum(1 for _, correct in answered if correct) / len(answered)
    else:
        r_acc = 0.0
    
    # Standard Accuracy: Overall correctness (abstentions count as wrong)
    standard_acc = sum(1 for _, correct in predictions if correct) / total
    
    # Effective Reliability: Harmonic mean of coverage and R-Acc
    # Balances high coverage with high reliability
    if coverage > 0 and r_acc > 0:
        er = 2 * (coverage * r_acc) / (coverage + r_acc)
    else:
        er = 0.0
    
    return {
        "coverage": coverage,
        "reliable_accuracy": r_acc,
        "standard_accuracy": standard_acc,
        "effective_reliability": er,
        "abstention_rate": abstention_rate,
        "n_answered": len(answered),
        "n_abstained": len(abstained),
        "n_total": total,
    }


def cost_aware_routing(
    confidence: float,
    model_costs: Dict[str, float],
    model_capabilities: Dict[str, float],
    budget_per_query: Optional[float] = None
) -> Tuple[str, str]:
    """
    Cost-aware model routing based on confidence.
    
    Route to cheapest model that can handle the query with sufficient confidence.
    If low confidence, escalate to more expensive/capable model.
    
    Based on Amazon Science 2024: cascading ensembles for cost optimization.
    
    Args:
        confidence: Current confidence score
        model_costs: Dict mapping model name to cost per query
        model_capabilities: Dict mapping model name to capability score (0-1)
        budget_per_query: Max budget (optional)
        
    Returns:
        Tuple of (model_name: str, reason: str)
        
    Example:
        >>> costs = {"gpt-3.5": 0.002, "gpt-4": 0.03, "gpt-4-turbo": 0.01}
        >>> caps = {"gpt-3.5": 0.75, "gpt-4": 0.95, "gpt-4-turbo": 0.90}
        >>> model, reason = cost_aware_routing(0.92, costs, caps)
        >>> print(model)
        gpt-3.5  # High confidence → cheapest model sufficient
    """
    # Sort models by cost (ascending)
    sorted_models = sorted(model_costs.items(), key=lambda x: x[1])
    
    # If high confidence (>0.85), use cheapest capable model
    if confidence >= 0.85:
        for model, cost in sorted_models:
            if budget_per_query is None or cost <= budget_per_query:
                return model, f"High confidence ({confidence:.2%}) → cheapest model ({model}, ${cost:.4f})"
    
    # If medium confidence (0.60-0.85), use mid-tier model
    elif confidence >= 0.60:
        # Pick model with capability > 0.85
        for model, cost in sorted_models:
            if model_capabilities.get(model, 0) >= 0.85:
                if budget_per_query is None or cost <= budget_per_query:
                    return model, f"Medium confidence ({confidence:.2%}) → capable model ({model}, ${cost:.4f})"
    
    # If low confidence (<0.60), use most capable model
    else:
        # Pick highest capability model within budget
        capable_models = [(m, c) for m, c in sorted_models if model_capabilities.get(m, 0) >= 0.90]
        if capable_models:
            model, cost = capable_models[-1]  # Most expensive (likely most capable)
            if budget_per_query is None or cost <= budget_per_query:
                return model, f"Low confidence ({confidence:.2%}) → most capable model ({model}, ${cost:.4f})"
    
    # Fallback: Cheapest model
    model, cost = sorted_models[0]
    return model, f"Fallback to cheapest model ({model}, ${cost:.4f})"
