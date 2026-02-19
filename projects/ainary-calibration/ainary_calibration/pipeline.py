"""
3-Tier Calibration Pipeline
============================

Orchestrates multi-tier calibration architecture from AR-020-v2:

Tier 1: Consistency-Based Default (all agent outputs)
Tier 2: Conformal Prediction for High-Stakes
Tier 3: Selective Prediction for Human Routing

Entry point: calibrate(prompt, model, tier="auto")
"""

from typing import Optional, Dict, Any, Literal
from dataclasses import dataclass
from enum import Enum

from .consistency import self_consistency_score, budget_cocoa
from .verbal import verbalized_confidence, afce_confidence
from .conformal import conformal_predict, generate_calibration_set, CalibrationExample
from .selective import route_by_confidence, RouteDecision
from .metrics import calibration_summary


class CalibrationTier(str, Enum):
    """Calibration tier levels."""
    TIER_1 = "tier1"  # Consistency-based (fast, cheap)
    TIER_2 = "tier2"  # + Conformal prediction (guarantees)
    TIER_3 = "tier3"  # + Selective prediction (routing)
    AUTO = "auto"     # Auto-select based on task risk


@dataclass
class CalibratedResult:
    """Result of calibration pipeline."""
    answer: str
    confidence: float
    tier: CalibrationTier
    route: Optional[RouteDecision]
    cost: float
    metadata: Dict[str, Any]


def calibrate(
    prompt: str,
    model: str = "simulated",
    tier: Literal["tier1", "tier2", "tier3", "auto"] = "auto",
    task_risk: Literal["low", "medium", "high"] = "medium",
    calibration_set: Optional[list] = None,
    budget_per_query: Optional[float] = None,
) -> CalibratedResult:
    """
    Main calibration pipeline entry point.
    
    Implements 3-tier calibration architecture from AR-020-v2:
    
    TIER 1 (Default):
        - Self-consistency scoring (3-5 samples)
        - Cost: ~$0.005-0.015
        - ECE: ~25-30% (down from 40%+ uncalibrated)
        - Use: All agent outputs
    
    TIER 2 (High-Stakes):
        - TIER 1 + Conformal prediction
        - Provides statistical guarantees (90% coverage)
        - Cost: ~$0.020-0.030
        - Use: Financial, legal, medical decisions
    
    TIER 3 (Human-in-Loop):
        - TIER 2 + Selective prediction routing
        - Routes to human/better model when uncertain
        - Cost: Variable (depends on routing)
        - Use: Production agent systems
    
    AUTO (Recommended):
        - Selects tier based on task_risk
        - Low risk → TIER 1
        - Medium risk → TIER 2
        - High risk → TIER 3
    
    Args:
        prompt: User query/prompt
        model: Model identifier (default: "simulated")
        tier: Calibration tier ("tier1", "tier2", "tier3", "auto")
        task_risk: Risk level ("low", "medium", "high") for auto-routing
        calibration_set: Optional pre-generated calibration set for TIER 2
        budget_per_query: Optional budget constraint
        
    Returns:
        CalibratedResult with confidence, routing, and metadata
        
    Example:
        >>> result = calibrate("What is 2+2?", tier="tier1")
        >>> print(f"Answer: {result.answer}, Confidence: {result.confidence:.2%}")
        Answer: 4, Confidence: 80.00%
        >>> print(f"Tier: {result.tier}, Cost: ${result.cost:.4f}")
        Tier: tier1, Cost: $0.0050
        
        >>> result_high_stakes = calibrate("Approve $1M transaction?", task_risk="high")
        >>> print(f"Tier: {result_high_stakes.tier}, Route: {result_high_stakes.route}")
        Tier: tier3, Route: REVIEW
    """
    # Auto-select tier based on task risk
    if tier == "auto":
        if task_risk == "low":
            tier = "tier1"
        elif task_risk == "medium":
            tier = "tier2"
        else:  # high
            tier = "tier3"
    
    total_cost = 0.0
    metadata = {
        "task_risk": task_risk,
        "selected_tier": tier,
    }
    
    # TIER 1: Consistency-Based Calibration (ALWAYS run)
    if budget_per_query and budget_per_query < 0.01:
        # Budget-constrained: Use Budget-CoCoA
        confidence_t1, cost_t1, meta_t1 = budget_cocoa(prompt, model, n_samples=3)
        answer = meta_t1.get("most_common_answer", "unknown")
    else:
        # Standard self-consistency
        confidence_t1, meta_t1 = self_consistency_score(prompt, model, n_samples=5)
        answer = meta_t1.get("most_common_answer", "unknown")
        cost_t1 = meta_t1.get("cost_estimate", 0.005)
    
    total_cost += cost_t1
    metadata["tier1"] = {
        "method": "self-consistency",
        "confidence": confidence_t1,
        "cost": cost_t1,
        "n_samples": meta_t1.get("n_samples", 5),
        "clusters": meta_t1.get("clusters", {}),
    }
    
    # If TIER 1 only, return early
    if tier == "tier1":
        return CalibratedResult(
            answer=answer,
            confidence=confidence_t1,
            tier=CalibrationTier.TIER_1,
            route=None,
            cost=total_cost,
            metadata=metadata,
        )
    
    # TIER 2: + Conformal Prediction
    if calibration_set is None:
        # Generate synthetic calibration set
        calibration_set = generate_calibration_set(n=200)
    
    pred_set = conformal_predict(
        prompt=prompt,
        model=model,
        calibration_set=calibration_set,
        coverage=0.90,
        use_consistency_scores=True
    )
    
    # Cost of conformal: Calibration set generation (one-time) + prediction
    cost_t2 = 0.010  # Amortized cost
    total_cost += cost_t2
    
    # Adjust confidence based on prediction set size
    # Smaller set = more confident
    set_size_penalty = min(0.2, (len(pred_set.predictions) - 1) * 0.05)
    confidence_t2 = max(0.0, confidence_t1 - set_size_penalty)
    
    metadata["tier2"] = {
        "method": "conformal-prediction",
        "prediction_set": list(pred_set.predictions),
        "set_size": len(pred_set.predictions),
        "coverage_guarantee": pred_set.coverage_level,
        "confidence_adjusted": confidence_t2,
        "cost": cost_t2,
    }
    
    # If TIER 2 only, return
    if tier == "tier2":
        return CalibratedResult(
            answer=answer,
            confidence=confidence_t2,
            tier=CalibrationTier.TIER_2,
            route=None,
            cost=total_cost,
            metadata=metadata,
        )
    
    # TIER 3: + Selective Prediction / Routing
    routing_result = route_by_confidence(
        confidence=confidence_t2,
        task_risk=task_risk
    )
    
    # Cost varies by route
    if routing_result.route == RouteDecision.AUTO:
        cost_t3 = 0.0  # No additional cost
    elif routing_result.route == RouteDecision.REVIEW:
        cost_t3 = 0.0  # Human review cost tracked separately
    elif routing_result.route == RouteDecision.ESCALATE:
        cost_t3 = 0.050  # Cost of routing to better model (e.g., GPT-4)
    else:  # ABSTAIN
        cost_t3 = 0.0
    
    total_cost += cost_t3
    
    metadata["tier3"] = {
        "method": "selective-prediction",
        "route": routing_result.route.value,
        "should_answer": routing_result.should_answer,
        "reason": routing_result.reason,
        "cost": cost_t3,
        "thresholds": routing_result.metadata.get("adjusted_thresholds", {}),
    }
    
    return CalibratedResult(
        answer=answer,
        confidence=confidence_t2,
        tier=CalibrationTier.TIER_3,
        route=routing_result.route,
        cost=total_cost,
        metadata=metadata,
    )


def batch_calibrate(
    prompts: list[str],
    model: str = "simulated",
    tier: str = "auto",
    task_risk: str = "medium",
) -> list[CalibratedResult]:
    """
    Batch calibration for multiple prompts.
    
    More efficient than individual calls (can share calibration set).
    
    Args:
        prompts: List of prompts to calibrate
        model: Model identifier
        tier: Calibration tier
        task_risk: Risk level
        
    Returns:
        List of CalibratedResult objects
    """
    # Generate shared calibration set (Tier 2+)
    shared_calib_set = None
    if tier in ["tier2", "tier3", "auto"]:
        shared_calib_set = generate_calibration_set(n=200)
    
    results = []
    for prompt in prompts:
        result = calibrate(
            prompt=prompt,
            model=model,
            tier=tier,
            task_risk=task_risk,
            calibration_set=shared_calib_set,
        )
        results.append(result)
    
    return results


def calibrate_with_verbalized_fallback(
    prompt: str,
    model: str = "simulated",
    use_afce: bool = True,
) -> CalibratedResult:
    """
    Calibrate using consistency-based method with verbalized confidence fallback.
    
    Useful when consistency checking is too expensive or when model always gives
    identical responses (low diversity).
    
    Args:
        prompt: User prompt
        model: Model identifier
        use_afce: Use AFCE (Answer-Free Confidence Estimation) for verbalized
        
    Returns:
        CalibratedResult
    """
    # Try consistency-based first
    confidence_consistency, meta = self_consistency_score(prompt, model, n_samples=5)
    answer = meta.get("most_common_answer", "unknown")
    
    # Check diversity
    clusters = meta.get("clusters", {})
    n_clusters = len(clusters)
    
    if n_clusters == 1:
        # Low diversity → fallback to verbalized confidence
        if use_afce:
            confidence_verbal, answer_verbal, meta_verbal = afce_confidence(prompt, model)
        else:
            confidence_verbal, answer_verbal, meta_verbal = verbalized_confidence(prompt, model)
        
        # Average the two
        final_confidence = (confidence_consistency + confidence_verbal) / 2.0
        
        metadata = {
            "method": "hybrid",
            "consistency": {
                "confidence": confidence_consistency,
                "n_clusters": n_clusters,
                "low_diversity": True,
            },
            "verbalized": {
                "confidence": confidence_verbal,
                "method": "afce" if use_afce else "standard",
            },
            "final_confidence": final_confidence,
        }
    else:
        # Good diversity → use consistency
        final_confidence = confidence_consistency
        metadata = {
            "method": "consistency",
            "confidence": confidence_consistency,
            "n_clusters": n_clusters,
        }
    
    return CalibratedResult(
        answer=answer,
        confidence=final_confidence,
        tier=CalibrationTier.TIER_1,
        route=None,
        cost=0.015,
        metadata=metadata,
    )


def cost_analysis(
    n_queries: int = 1000,
    tier: str = "auto",
    task_risk_distribution: Optional[Dict[str, float]] = None,
) -> Dict[str, Any]:
    """
    Analyze cost of calibration pipeline at scale.
    
    Args:
        n_queries: Number of queries per month
        tier: Calibration tier
        task_risk_distribution: Distribution of task risks (default: 60% low, 30% medium, 10% high)
        
    Returns:
        Cost analysis dict
    """
    if task_risk_distribution is None:
        task_risk_distribution = {
            "low": 0.60,
            "medium": 0.30,
            "high": 0.10,
        }
    
    # Cost per tier (average)
    tier_costs = {
        "tier1": 0.010,
        "tier2": 0.025,
        "tier3": 0.035,  # Excluding escalation cost
    }
    
    if tier == "auto":
        # Weighted average based on task risk distribution
        avg_cost = (
            task_risk_distribution["low"] * tier_costs["tier1"] +
            task_risk_distribution["medium"] * tier_costs["tier2"] +
            task_risk_distribution["high"] * tier_costs["tier3"]
        )
    else:
        avg_cost = tier_costs.get(tier, 0.020)
    
    total_cost_month = n_queries * avg_cost
    total_cost_year = total_cost_month * 12
    
    return {
        "n_queries_per_month": n_queries,
        "avg_cost_per_query": avg_cost,
        "total_cost_per_month": total_cost_month,
        "total_cost_per_year": total_cost_year,
        "tier": tier,
        "task_risk_distribution": task_risk_distribution,
        "breakdown": {
            "tier1_percentage": task_risk_distribution["low"] if tier == "auto" else (1.0 if tier == "tier1" else 0.0),
            "tier2_percentage": task_risk_distribution["medium"] if tier == "auto" else (1.0 if tier == "tier2" else 0.0),
            "tier3_percentage": task_risk_distribution["high"] if tier == "auto" else (1.0 if tier == "tier3" else 0.0),
        }
    }
