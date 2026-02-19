"""
Ainary Calibration Library
===========================

Trust Calibration Methods for LLM Agents

This library implements state-of-the-art calibration methods for AI agent systems,
with a focus on black-box LLM deployments. Based on AR-020-v2 research.

Main modules:
- consistency: Self-consistency based calibration (Family 2)
- verbal: Verbalized confidence extraction (Family 3)
- conformal: Conformal prediction with guarantees (Family 4)
- selective: Selective prediction and abstention (Family 6)
- propagation: Multi-agent confidence propagation (NOVEL)
- metrics: ECE, MCE, Brier score, reliability diagrams
- pipeline: 3-Tier orchestration

Quick Start:
>>> from ainary_calibration import pipeline
>>> result = pipeline.calibrate("What is 2+2?", model="simulated", tier="auto")
>>> print(f"Confidence: {result.confidence:.2%}")
"""

__version__ = "0.1.0"
__author__ = "Ainary Research"

from .consistency import self_consistency_score, budget_cocoa
from .verbal import verbalized_confidence, afce_confidence
from .conformal import conformal_predict
from .selective import should_abstain, route_by_confidence
from .propagation import propagate_confidence, simulate_chain
from .metrics import expected_calibration_error, maximum_calibration_error, brier_score, reliability_diagram
from .pipeline import calibrate

__all__ = [
    "self_consistency_score",
    "budget_cocoa",
    "verbalized_confidence",
    "afce_confidence",
    "conformal_predict",
    "should_abstain",
    "route_by_confidence",
    "propagate_confidence",
    "simulate_chain",
    "expected_calibration_error",
    "maximum_calibration_error",
    "brier_score",
    "reliability_diagram",
    "calibrate",
]
