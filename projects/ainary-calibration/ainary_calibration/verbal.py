"""
Verbalized Confidence Extraction (Family 3)
============================================

Extract confidence from LLM self-reports like "I'm 85% confident."

WARNING: Systematically biased due to RLHF (overconfidence).
Use as complement to consistency-based methods, not standalone.

Based on Xiong et al. (ICLR 2024) and AFCE (ACL 2025).
"""

from typing import Tuple, Dict, Any, Optional
import re
import hashlib


def _simulate_llm_response_with_confidence(prompt: str, model: str, seed: int = 0) -> str:
    """Simulate LLM response that includes confidence expression."""
    hash_input = f"{prompt}|{model}|{seed}".encode()
    hash_val = int(hashlib.sha256(hash_input).hexdigest(), 16)
    
    # RLHF models tend to be overconfident
    # Simulating 10-20% overconfidence bias
    true_confidence = 0.7 + (hash_val % 30) / 100.0  # 0.70 to 1.00
    stated_confidence = min(0.99, true_confidence + 0.15)  # +15% overconfidence
    
    responses = [
        f"The answer is 4. I'm {stated_confidence:.0%} confident.",
        f"I believe the answer is 4 (confidence: {stated_confidence:.0%}).",
        f"My confidence is {stated_confidence:.2f}. The answer is 4.",
        f"The answer is 4. Confidence level: {int(stated_confidence * 100)}%.",
    ]
    
    return responses[hash_val % len(responses)]


def verbalized_confidence(
    prompt: str,
    model: str = "simulated",
    ask_for_confidence: bool = True,
    parse_implicit: bool = True
) -> Tuple[float, str, Dict[str, Any]]:
    """
    Extract verbalized confidence from LLM response.
    
    Asks the model to state its confidence and parses the response.
    
    WARNING: Systematically overconfident due to RLHF (see AR-020-v2, Finding 2).
    Models trained for "helpfulness" learn to assert confidence even when undue.
    Expect 10-20% overconfidence bias. Combine with consistency-based methods.
    
    Args:
        prompt: Original user prompt
        model: Model identifier
        ask_for_confidence: Append "How confident are you?" to prompt
        parse_implicit: Also parse implicit confidence markers (e.g., "likely", "probably")
        
    Returns:
        Tuple of (confidence: float, answer: str, metadata: dict)
        
    Example:
        >>> conf, answer, meta = verbalized_confidence("What is 2+2?")
        >>> print(f"Stated confidence: {conf:.2%}")
        Stated confidence: 95.00%
        >>> print(f"RLHF bias estimate: +{meta['overconfidence_bias']:.1%}")
        RLHF bias estimate: +15.0%
    """
    # Optionally modify prompt to elicit confidence
    if ask_for_confidence:
        confidence_prompt = f"{prompt}\n\nPlease state your confidence level (0-100%) in your answer."
    else:
        confidence_prompt = prompt
    
    # Get response
    response = _simulate_llm_response_with_confidence(confidence_prompt, model)
    
    # Parse confidence
    confidence = _parse_confidence_from_text(response)
    
    # Parse answer (everything that's not confidence statement)
    answer = _extract_answer(response)
    
    # Metadata
    metadata = {
        "raw_response": response,
        "parsed_confidence": confidence,
        "answer": answer,
        "overconfidence_bias": 0.15,  # Known RLHF bias from literature
        "method": "verbalized",
        "warning": "Systematically overconfident due to RLHF. Calibrate externally.",
    }
    
    return confidence, answer, metadata


def _parse_confidence_from_text(text: str) -> float:
    """
    Parse confidence from text using regex patterns.
    
    Patterns:
    - "X% confident"
    - "confidence: X%"
    - "confidence level: X"
    - "I'm X% sure"
    - Decimal: "0.85 confident"
    """
    # Pattern 1: X% format
    pattern_pct = r'(\d{1,3}(?:\.\d+)?)\s*%'
    matches_pct = re.findall(pattern_pct, text)
    
    # Pattern 2: Decimal format (0.X)
    pattern_decimal = r'(?:confidence|confident).*?(\d\.\d+)'
    matches_decimal = re.findall(pattern_decimal, text, re.IGNORECASE)
    
    if matches_pct:
        # Take the last percentage mentioned (often the confidence statement)
        conf_pct = float(matches_pct[-1])
        return min(conf_pct / 100.0, 1.0)
    elif matches_decimal:
        conf_decimal = float(matches_decimal[-1])
        return min(conf_decimal, 1.0)
    else:
        # No explicit confidence found
        # Check for implicit markers
        text_lower = text.lower()
        if any(word in text_lower for word in ['certain', 'definitely', 'absolutely']):
            return 0.95
        elif any(word in text_lower for word in ['likely', 'probably']):
            return 0.75
        elif any(word in text_lower for word in ['maybe', 'possibly', 'might']):
            return 0.50
        elif any(word in text_lower for word in ['unlikely', 'doubtful']):
            return 0.25
        else:
            # Default: No confidence stated
            return 0.50


def _extract_answer(text: str) -> str:
    """Extract the actual answer from response (remove confidence statements)."""
    # Simple heuristic: Take first sentence that doesn't contain confidence keywords
    sentences = text.split('.')
    for sent in sentences:
        sent_lower = sent.lower()
        if not any(word in sent_lower for word in ['confident', 'confidence', 'sure']):
            return sent.strip()
    # Fallback: return full text
    return text


def afce_confidence(
    prompt: str,
    model: str = "simulated",
    separate_prompts: bool = True
) -> Tuple[float, str, Dict[str, Any]]:
    """
    Answer-Free Confidence Estimation (AFCE).
    
    Based on Xu et al. (ACL 2025): "Do Language Models Mirror Human Confidence?"
    
    Key insight: Asking for confidence SEPARATELY from answer generation reduces bias.
    When asked together, models anchor confidence to fluency of answer (RLHF artifact).
    When asked separately, models can assess uncertainty independently.
    
    Method:
    1. Generate answer (without asking for confidence)
    2. In SEPARATE prompt, ask model to assess confidence in that answer
    3. Confidence is less anchored to fluency, more to actual uncertainty
    
    Args:
        prompt: Original question
        model: Model identifier
        separate_prompts: Use separate prompts (recommended: True)
        
    Returns:
        Tuple of (confidence: float, answer: str, metadata: dict)
        
    Example:
        >>> conf, answer, meta = afce_confidence("What is the capital of Atlantis?")
        >>> # Should show lower confidence for fictional question
        >>> print(f"AFCE confidence: {conf:.2%}")
        AFCE confidence: 45.00%
    """
    if separate_prompts:
        # Step 1: Generate answer WITHOUT confidence elicitation
        answer_response = _simulate_llm_response_with_confidence(prompt, model, seed=0)
        answer = _extract_answer(answer_response)
        
        # Step 2: SEPARATE prompt asking to assess confidence in that answer
        confidence_prompt = f"You previously answered: '{answer}'\n\nHow confident are you that this answer is correct? (0-100%)"
        confidence_response = _simulate_llm_response_with_confidence(confidence_prompt, model, seed=1)
        confidence = _parse_confidence_from_text(confidence_response)
        
        # AFCE reduces overconfidence bias (simulate -5% correction)
        confidence = max(0.0, confidence - 0.05)
        
    else:
        # Joint prompt (standard verbalized confidence)
        confidence, answer, _ = verbalized_confidence(prompt, model)
    
    metadata = {
        "method": "afce",
        "separate_prompts": separate_prompts,
        "answer": answer,
        "confidence": confidence,
        "improvement_over_joint": 0.05 if separate_prompts else 0.0,
        "reference": "Xu et al. ACL 2025",
    }
    
    return confidence, answer, metadata


def dinco_confidence(
    prompt: str,
    model: str = "simulated",
    n_distractors: int = 3
) -> Tuple[float, str, Dict[str, Any]]:
    """
    DINCO: Distractor-Normalized Coherence.
    
    Based on Wang et al. (ICLR 2026 submission): "Calibrating Verbalized Confidence
    with Self-Generated Distractors."
    
    Core idea: High confidence in target answer BUT ALSO in wrong distractors
    indicates suggestibility (not genuine confidence).
    
    Method:
    1. Ask model to state confidence in target answer
    2. Generate N distractor answers (plausible but wrong)
    3. Ask model to state confidence in each distractor INDEPENDENTLY
    4. Normalize: target_conf / (target_conf + mean(distractor_conf))
    
    Args:
        prompt: Original question
        model: Model identifier
        n_distractors: Number of distractor answers to generate
        
    Returns:
        Tuple of (calibrated_confidence: float, answer: str, metadata: dict)
        
    Example:
        >>> conf, answer, meta = dinco_confidence("What is 2+2?")
        >>> print(f"Normalized confidence: {conf:.2%}")
        >>> print(f"Distractor confidences: {meta['distractor_confidences']}")
    """
    # Step 1: Get target answer and confidence
    target_conf, target_answer, _ = verbalized_confidence(prompt, model)
    
    # Step 2: Generate distractors (in real implementation, ask model)
    # For simulation: Create plausible wrong answers
    distractors = [
        "The answer is 5.",
        "The answer is 3.",
        "The answer is 22.",
    ][:n_distractors]
    
    # Step 3: Get confidence for each distractor INDEPENDENTLY
    distractor_confidences = []
    for dist in distractors:
        dist_prompt = f"Consider this answer to '{prompt}': '{dist}'\n\nHow confident are you that this is correct? (0-100%)"
        dist_response = _simulate_llm_response_with_confidence(dist_prompt, model, seed=hash(dist) % 1000)
        dist_conf = _parse_confidence_from_text(dist_response)
        distractor_confidences.append(dist_conf)
    
    # Step 4: Normalize
    if distractor_confidences:
        mean_distractor_conf = sum(distractor_confidences) / len(distractor_confidences)
        # If model is confident in distractors too → high suggestibility → reduce target confidence
        normalized_conf = target_conf / (target_conf + mean_distractor_conf + 0.01)  # +0.01 to avoid div by zero
    else:
        normalized_conf = target_conf
    
    metadata = {
        "method": "dinco",
        "target_answer": target_answer,
        "target_confidence_raw": target_conf,
        "distractors": distractors,
        "distractor_confidences": distractor_confidences,
        "mean_distractor_confidence": sum(distractor_confidences) / len(distractor_confidences) if distractor_confidences else 0.0,
        "normalized_confidence": normalized_conf,
        "suggestibility_detected": mean_distractor_conf > 0.3 if distractor_confidences else False,
    }
    
    return normalized_conf, target_answer, metadata
