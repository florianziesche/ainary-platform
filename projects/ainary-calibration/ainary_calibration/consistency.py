"""
Consistency-Based Calibration (Family 2)
=========================================

Self-consistency scoring for black-box LLMs. Core calibration method for agent systems.

Based on Wang et al. (ICLR 2023) and PMC biomedical study (2024).
Achieves 27.3% ECE vs. 42.0% for verbalized confidence.
"""

from typing import List, Tuple, Dict, Any, Optional
import numpy as np
from collections import Counter
import hashlib


def _simulate_llm_response(prompt: str, model: str, temperature: float = 0.7, seed: int = 0) -> str:
    """
    Simulate LLM response for testing (no API needed).
    
    Uses deterministic hashing with seed for reproducible variation.
    """
    # Hash prompt + model + seed to get deterministic variation
    hash_input = f"{prompt}|{model}|{seed}".encode()
    hash_val = int(hashlib.sha256(hash_input).hexdigest(), 16)
    
    # Generate response variants based on hash
    # In real implementation, this would be LLM API call
    base_responses = [
        "The answer is 4.",
        "2 + 2 equals 4.",
        "Four (4).",
        "The result is 4.",
        "It's 4.",
        "The answer is 5.",  # Occasional error
        "That would be 4.",
    ]
    
    # Temperature affects diversity
    if temperature < 0.3:
        # Low temp → always same answer
        return base_responses[0]
    elif temperature > 0.9:
        # High temp → more variation
        idx = hash_val % len(base_responses)
    else:
        # Medium temp → mostly correct with some variation
        idx = hash_val % (len(base_responses) - 1)  # Avoid error response usually
    
    return base_responses[idx]


def _semantic_cluster(responses: List[str], threshold: float = 0.8) -> Dict[str, int]:
    """
    Cluster responses by semantic similarity.
    
    In production, this would use embeddings (OpenAI, Cohere, local Sentence-BERT).
    For simulation, we use simple normalized string matching.
    
    Args:
        responses: List of text responses
        threshold: Similarity threshold for clustering
        
    Returns:
        Dictionary mapping cluster representative to count
    """
    # Simple simulation: normalize and cluster exact matches
    normalized = []
    for r in responses:
        # Normalize: lowercase, remove punctuation, strip
        norm = r.lower().strip().rstrip('.')
        # Extract core answer (very simple parsing)
        if 'four' in norm or '4' in norm:
            norm = "4"
        elif 'five' in norm or '5' in norm:
            norm = "5"
        elif 'three' in norm or '3' in norm:
            norm = "3"
        normalized.append(norm)
    
    # Count clusters
    clusters = Counter(normalized)
    return dict(clusters)


def self_consistency_score(
    prompt: str,
    model: str = "simulated",
    n_samples: int = 5,
    temperature: float = 0.7,
    use_semantic_clustering: bool = True
) -> Tuple[float, Dict[str, Any]]:
    """
    Calculate confidence via self-consistency sampling.
    
    Samples N responses with temperature > 0, clusters by semantic similarity,
    and uses the largest cluster frequency as confidence proxy.
    
    Based on Wang et al. (ICLR 2023): "Self-Consistency Improves Chain of Thought
    Reasoning in Language Models."
    
    Args:
        prompt: Input prompt for the model
        model: Model identifier (for simulation: "simulated")
        n_samples: Number of samples to draw (default: 5)
        temperature: Sampling temperature (default: 0.7)
        use_semantic_clustering: Use semantic clustering vs exact match (default: True)
        
    Returns:
        Tuple of (confidence: float, metadata: dict)
        - confidence: 0.0 to 1.0 (largest cluster frequency / n_samples)
        - metadata: {
            "n_samples": int,
            "clusters": Dict[str, int],
            "most_common_answer": str,
            "cost_estimate": float
          }
          
    Example:
        >>> confidence, meta = self_consistency_score("What is 2+2?", n_samples=5)
        >>> print(f"Confidence: {confidence:.2%}")
        Confidence: 80.00%
        >>> print(meta["most_common_answer"])
        4
    """
    # Sample N responses
    responses = []
    for i in range(n_samples):
        response = _simulate_llm_response(prompt, model, temperature, seed=i)
        responses.append(response)
    
    # Cluster responses
    if use_semantic_clustering:
        clusters = _semantic_cluster(responses)
    else:
        clusters = dict(Counter(responses))
    
    # Confidence = largest cluster / total
    if not clusters:
        confidence = 0.0
        most_common = None
    else:
        most_common = max(clusters.items(), key=lambda x: x[1])
        confidence = most_common[1] / n_samples
    
    # Cost estimate (assuming $0.001 per call for small model)
    cost_estimate = n_samples * 0.001
    
    metadata = {
        "n_samples": n_samples,
        "clusters": clusters,
        "most_common_answer": most_common[0] if most_common else None,
        "most_common_count": most_common[1] if most_common else 0,
        "cost_estimate": cost_estimate,
        "responses": responses,
    }
    
    return confidence, metadata


def budget_cocoa(
    prompt: str,
    model: str = "simulated",
    n_samples: int = 3,
    temperature: float = 0.7,
    small_model: bool = True
) -> Tuple[float, float, Dict[str, Any]]:
    """
    Budget-CoCoA: Cost-optimized consistency checking.
    
    Uses only 3 samples with a smaller/cheaper model for consistency checking.
    Trade-off: ~5-10% lower calibration quality for 40-60% cost reduction.
    
    Typical cost: ~$0.003-0.005 per check (vs $0.015+ for full self-consistency).
    
    Args:
        prompt: Input prompt
        model: Model identifier (simulated uses cheaper pricing)
        n_samples: Number of samples (default: 3, recommended range: 3-5)
        temperature: Sampling temperature
        small_model: Use small model pricing (default: True)
        
    Returns:
        Tuple of (confidence: float, cost: float, metadata: dict)
        
    Example:
        >>> conf, cost, meta = budget_cocoa("What is 2+2?")
        >>> print(f"Confidence: {conf:.2%}, Cost: ${cost:.4f}")
        Confidence: 66.67%, Cost: $0.0015
    """
    # Use smaller model pricing
    model_cost_per_call = 0.0005 if small_model else 0.001
    
    # Sample N responses (fewer than standard self-consistency)
    responses = []
    for i in range(n_samples):
        response = _simulate_llm_response(prompt, model, temperature, seed=i)
        responses.append(response)
    
    # Cluster
    clusters = _semantic_cluster(responses)
    
    # Confidence
    if not clusters:
        confidence = 0.0
        most_common = None
    else:
        most_common = max(clusters.items(), key=lambda x: x[1])
        confidence = most_common[1] / n_samples
    
    # Total cost
    total_cost = n_samples * model_cost_per_call
    
    metadata = {
        "n_samples": n_samples,
        "clusters": clusters,
        "most_common_answer": most_common[0] if most_common else None,
        "cost_per_call": model_cost_per_call,
        "total_cost": total_cost,
        "method": "budget-cocoa",
        "responses": responses,
    }
    
    return confidence, total_cost, metadata


def consistency_score_with_reasoning(
    prompt: str,
    model: str = "simulated",
    n_samples: int = 5,
    temperature: float = 0.7,
) -> Tuple[float, List[str], Dict[str, Any]]:
    """
    Self-consistency with chain-of-thought reasoning extraction.
    
    Not only clusters final answers but also checks reasoning path agreement.
    Higher quality calibration for complex reasoning tasks.
    
    Args:
        prompt: Input prompt (should elicit reasoning)
        model: Model identifier
        n_samples: Number of samples
        temperature: Sampling temperature
        
    Returns:
        Tuple of (confidence, reasoning_paths, metadata)
    """
    # Generate responses with reasoning
    responses = []
    reasoning_paths = []
    
    for i in range(n_samples):
        response = _simulate_llm_response(prompt, model, temperature, seed=i)
        responses.append(response)
        # In real implementation, extract reasoning via parsing
        # For simulation, just use full response as "reasoning"
        reasoning_paths.append(response)
    
    # Cluster both answers AND reasoning
    answer_clusters = _semantic_cluster(responses)
    reasoning_clusters = _semantic_cluster(reasoning_paths)
    
    # Confidence: Weighted combination of answer agreement and reasoning agreement
    if not answer_clusters:
        confidence = 0.0
    else:
        answer_conf = max(answer_clusters.values()) / n_samples
        reasoning_conf = max(reasoning_clusters.values()) / n_samples
        # Weight: 70% answer, 30% reasoning path
        confidence = 0.7 * answer_conf + 0.3 * reasoning_conf
    
    metadata = {
        "n_samples": n_samples,
        "answer_clusters": answer_clusters,
        "reasoning_clusters": reasoning_clusters,
        "answer_confidence": max(answer_clusters.values()) / n_samples if answer_clusters else 0.0,
        "reasoning_confidence": max(reasoning_clusters.values()) / n_samples if reasoning_clusters else 0.0,
        "combined_confidence": confidence,
    }
    
    return confidence, reasoning_paths, metadata
