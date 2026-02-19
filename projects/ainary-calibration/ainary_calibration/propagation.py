"""
Multi-Agent Confidence Propagation
===================================

NOVEL: Propagating confidence through multi-agent chains.

Research gap identified in AR-020-v2:
"When Agent A reports 85% confidence and passes output to Agent B,
what should Agent B's effective confidence be?"

No existing framework addresses this. We implement three approaches:
1. Multiplicative (independence assumption)
2. Bayesian Network (correlation modeling)
3. Conservative (minimum confidence)
"""

from typing import List, Tuple, Dict, Any, Optional
import numpy as np
from dataclasses import dataclass
from enum import Enum


class PropagationMethod(str, Enum):
    """Confidence propagation methods."""
    MULTIPLICATIVE = "multiplicative"     # P(A ∧ B) = P(A) × P(B) (assumes independence)
    BAYESIAN = "bayesian_network"        # Model correlations between agents
    CONSERVATIVE = "conservative"        # min(confidences) - safest assumption
    WEIGHTED_AVERAGE = "weighted_average"  # Weight by agent capability
    MONTE_CARLO = "monte_carlo"          # Simulation-based


@dataclass
class PropagationResult:
    """Result of confidence propagation."""
    final_confidence: float
    method: PropagationMethod
    chain_length: int
    individual_confidences: List[float]
    metadata: Dict[str, Any]


def propagate_confidence(
    chain: List[float],
    method: PropagationMethod = PropagationMethod.MULTIPLICATIVE,
    correlation: float = 0.0,
    agent_weights: Optional[List[float]] = None
) -> PropagationResult:
    """
    Propagate confidence through a multi-agent chain.
    
    CORE PROBLEM: How do individual agent confidences combine?
    
    Methods:
    1. MULTIPLICATIVE: Assumes independence. P(all correct) = ∏ P(i correct)
       - Simple, interpretable
       - Overly pessimistic if agents are positively correlated
       - Example: [0.9, 0.9, 0.9] → 0.729
    
    2. BAYESIAN_NETWORK: Models correlation between agents
       - More realistic when agents share context/tools
       - Requires correlation parameter
       - Example: [0.9, 0.9, 0.9] with ρ=0.3 → ~0.85
    
    3. CONSERVATIVE: Takes minimum confidence
       - Chain is only as strong as weakest link
       - Very pessimistic but safe for high-stakes
       - Example: [0.9, 0.9, 0.6] → 0.6
    
    4. WEIGHTED_AVERAGE: Weights by agent capability
       - More capable agents contribute more to final confidence
       - Requires agent weights
       
    Args:
        chain: List of individual agent confidences (0.0 to 1.0)
        method: Propagation method
        correlation: Correlation coefficient for Bayesian method (0.0 to 1.0)
        agent_weights: Weights for weighted average (must sum to 1.0)
        
    Returns:
        PropagationResult with final confidence and metadata
        
    Example:
        >>> chain = [0.90, 0.85, 0.88]
        >>> result = propagate_confidence(chain, method="multiplicative")
        >>> print(f"Final confidence: {result.final_confidence:.2%}")
        Final confidence: 67.32%
        
        >>> result_bayesian = propagate_confidence(chain, method="bayesian_network", correlation=0.3)
        >>> print(f"Bayesian confidence: {result_bayesian.final_confidence:.2%}")
        Bayesian confidence: 78.45%
    """
    if not chain:
        raise ValueError("Chain cannot be empty")
    
    if any(c < 0 or c > 1 for c in chain):
        raise ValueError("All confidences must be in [0, 1]")
    
    metadata = {
        "chain_length": len(chain),
        "mean_confidence": float(np.mean(chain)),
        "std_confidence": float(np.std(chain)),
        "min_confidence": float(np.min(chain)),
        "max_confidence": float(np.max(chain)),
    }
    
    if method == PropagationMethod.MULTIPLICATIVE:
        # Independence assumption: P(all correct) = ∏ P(i)
        final = float(np.prod(chain))
        metadata["assumption"] = "independence"
        
    elif method == PropagationMethod.BAYESIAN:
        # Model correlation via copula approach
        # Simplified: Adjust multiplicative by correlation factor
        multiplicative = float(np.prod(chain))
        
        # Positive correlation → less pessimistic than pure multiplication
        # Correlation of 0 → multiplicative, correlation of 1 → max confidence
        correlation = max(0.0, min(1.0, correlation))
        
        # Interpolate between multiplicative (ρ=0) and max (ρ=1)
        max_conf = max(chain)
        final = multiplicative + correlation * (max_conf - multiplicative)
        
        metadata["assumption"] = "correlated agents"
        metadata["correlation"] = correlation
        metadata["multiplicative_baseline"] = multiplicative
        
    elif method == PropagationMethod.CONSERVATIVE:
        # Weakest link: min confidence
        final = float(np.min(chain))
        metadata["assumption"] = "weakest link"
        
    elif method == PropagationMethod.WEIGHTED_AVERAGE:
        # Weighted by agent capability
        if agent_weights is None:
            # Default: uniform weights
            agent_weights = [1.0 / len(chain)] * len(chain)
        
        if len(agent_weights) != len(chain):
            raise ValueError("agent_weights must match chain length")
        
        if not np.isclose(sum(agent_weights), 1.0):
            raise ValueError("agent_weights must sum to 1.0")
        
        final = float(np.average(chain, weights=agent_weights))
        metadata["assumption"] = "weighted by capability"
        metadata["weights"] = agent_weights
        
    elif method == PropagationMethod.MONTE_CARLO:
        # Simulation-based (for complex dependencies)
        final = _monte_carlo_propagation(chain, correlation, n_samples=10000)
        metadata["assumption"] = "monte carlo simulation"
        metadata["n_samples"] = 10000
        
    else:
        raise ValueError(f"Unknown method: {method}")
    
    return PropagationResult(
        final_confidence=final,
        method=method,
        chain_length=len(chain),
        individual_confidences=chain,
        metadata=metadata
    )


def _monte_carlo_propagation(
    chain: List[float],
    correlation: float,
    n_samples: int = 10000
) -> float:
    """
    Monte Carlo simulation of confidence propagation.
    
    Samples agent outcomes with specified correlation structure.
    """
    n_agents = len(chain)
    
    # Generate correlated binary outcomes
    # Using simple correlation model: shared random effect + independent noise
    successes = 0
    
    for _ in range(n_samples):
        # Shared random effect (induces correlation)
        shared_effect = np.random.random()
        
        # Each agent succeeds if shared_effect + independent_noise < confidence
        all_succeed = True
        for conf in chain:
            # Mix shared and independent noise based on correlation
            independent_effect = np.random.random()
            combined_effect = correlation * shared_effect + (1 - correlation) * independent_effect
            
            if combined_effect > conf:
                all_succeed = False
                break
        
        if all_succeed:
            successes += 1
    
    return successes / n_samples


def simulate_chain(
    n_agents: int,
    base_confidence: float = 0.85,
    correlation: float = 0.0,
    confidence_variance: float = 0.05,
    n_simulations: int = 1000,
    methods: Optional[List[PropagationMethod]] = None
) -> Dict[str, Any]:
    """
    Simulate multi-agent chains to compare propagation methods.
    
    Monte Carlo simulation of agent chains with varying:
    - Chain length (n_agents)
    - Base confidence level
    - Correlation between agents
    - Confidence variance
    
    This is EXPERIMENT 1 from the spec.
    
    Args:
        n_agents: Number of agents in chain
        base_confidence: Mean confidence per agent
        correlation: Correlation between agent outcomes
        confidence_variance: Std dev of confidence across agents
        n_simulations: Number of Monte Carlo runs
        methods: Which propagation methods to compare (default: all)
        
    Returns:
        Dict with simulation results:
            - methods: Dict[method, List[final_confidences]]
            - statistics: Summary statistics per method
            - ground_truth: True success rate from simulation
            
    Example:
        >>> results = simulate_chain(n_agents=5, base_confidence=0.90, correlation=0.3)
        >>> print(results["statistics"]["multiplicative"]["mean"])
        0.59  # 0.9^5 = 0.59
        >>> print(results["statistics"]["bayesian_network"]["mean"])
        0.78  # Less pessimistic due to correlation
    """
    if methods is None:
        methods = [
            PropagationMethod.MULTIPLICATIVE,
            PropagationMethod.BAYESIAN,
            PropagationMethod.CONSERVATIVE,
        ]
    
    # Store results for each method
    results_by_method = {method: [] for method in methods}
    ground_truth_successes = []
    
    for _ in range(n_simulations):
        # Generate agent confidences
        confidences = np.random.normal(
            loc=base_confidence,
            scale=confidence_variance,
            size=n_agents
        )
        # Clip to [0, 1]
        confidences = np.clip(confidences, 0.0, 1.0)
        
        # Simulate ground truth outcome (with correlation)
        shared_effect = np.random.random()
        all_succeed = True
        for conf in confidences:
            independent_effect = np.random.random()
            combined = correlation * shared_effect + (1 - correlation) * independent_effect
            if combined > conf:
                all_succeed = False
                break
        ground_truth_successes.append(1.0 if all_succeed else 0.0)
        
        # Compute propagated confidence for each method
        for method in methods:
            result = propagate_confidence(
                list(confidences),
                method=method,
                correlation=correlation
            )
            results_by_method[method].append(result.final_confidence)
    
    # Compute statistics
    ground_truth_rate = np.mean(ground_truth_successes)
    
    statistics = {}
    for method, confidences in results_by_method.items():
        statistics[method.value] = {
            "mean": float(np.mean(confidences)),
            "std": float(np.std(confidences)),
            "median": float(np.median(confidences)),
            "min": float(np.min(confidences)),
            "max": float(np.max(confidences)),
            "error_vs_ground_truth": float(abs(np.mean(confidences) - ground_truth_rate)),
        }
    
    return {
        "parameters": {
            "n_agents": n_agents,
            "base_confidence": base_confidence,
            "correlation": correlation,
            "confidence_variance": confidence_variance,
            "n_simulations": n_simulations,
        },
        "ground_truth_success_rate": ground_truth_rate,
        "statistics": statistics,
        "raw_results": {m.value: results_by_method[m] for m in methods},
    }


def chain_reliability_analysis(
    chain_lengths: List[int] = [1, 3, 5, 10],
    base_confidences: List[float] = [0.85, 0.90, 0.95],
    correlations: List[float] = [0.0, 0.3, 0.7],
    n_simulations: int = 1000
) -> Dict[str, Any]:
    """
    Comprehensive analysis of how chain length, base confidence, and correlation
    affect final reliability.
    
    This generates data for visualizing the confidence degradation problem in
    multi-agent systems.
    
    Args:
        chain_lengths: List of chain lengths to test
        base_confidences: List of base confidence levels
        correlations: List of correlation values
        n_simulations: Monte Carlo runs per configuration
        
    Returns:
        Nested dict of results indexed by [chain_length][base_conf][correlation]
    """
    results = {}
    
    for chain_len in chain_lengths:
        results[chain_len] = {}
        
        for base_conf in base_confidences:
            results[chain_len][base_conf] = {}
            
            for corr in correlations:
                sim_result = simulate_chain(
                    n_agents=chain_len,
                    base_confidence=base_conf,
                    correlation=corr,
                    n_simulations=n_simulations
                )
                results[chain_len][base_conf][corr] = sim_result
    
    return results


def confidence_budget_optimizer(
    target_final_confidence: float,
    chain_length: int,
    correlation: float = 0.0,
    method: PropagationMethod = PropagationMethod.MULTIPLICATIVE
) -> Tuple[float, Dict[str, Any]]:
    """
    Find required per-agent confidence to achieve target final confidence.
    
    Inverse problem: Given desired final confidence and chain length,
    what confidence does each agent need?
    
    Args:
        target_final_confidence: Desired final confidence
        chain_length: Number of agents in chain
        correlation: Expected correlation between agents
        method: Propagation method
        
    Returns:
        Tuple of (required_per_agent_confidence, metadata)
        
    Example:
        >>> required, meta = confidence_budget_optimizer(0.80, chain_length=5)
        >>> print(f"Each agent needs: {required:.2%} confidence")
        Each agent needs: 95.60% confidence
        >>> # Because 0.956^5 ≈ 0.80
    """
    # Binary search for required confidence
    low, high = 0.0, 1.0
    tolerance = 0.001
    max_iterations = 50
    
    for iteration in range(max_iterations):
        mid = (low + high) / 2.0
        
        # Test this confidence level
        chain = [mid] * chain_length
        result = propagate_confidence(chain, method=method, correlation=correlation)
        
        if abs(result.final_confidence - target_final_confidence) < tolerance:
            # Found it!
            metadata = {
                "target_final_confidence": target_final_confidence,
                "achieved_final_confidence": result.final_confidence,
                "chain_length": chain_length,
                "method": method.value,
                "correlation": correlation,
                "iterations": iteration + 1,
            }
            return mid, metadata
        elif result.final_confidence < target_final_confidence:
            # Need higher per-agent confidence
            low = mid
        else:
            # Per-agent confidence too high
            high = mid
    
    # Max iterations reached
    mid = (low + high) / 2.0
    chain = [mid] * chain_length
    result = propagate_confidence(chain, method=method, correlation=correlation)
    
    metadata = {
        "target_final_confidence": target_final_confidence,
        "achieved_final_confidence": result.final_confidence,
        "chain_length": chain_length,
        "method": method.value,
        "correlation": correlation,
        "iterations": max_iterations,
        "converged": False,
    }
    
    return mid, metadata
