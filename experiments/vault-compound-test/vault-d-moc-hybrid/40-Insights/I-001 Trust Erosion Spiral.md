---
tags: [insight, cross-cutting]
---
# I-001: The Trust Erosion Spiral is Self-Reinforcing

Across AR-001, AR-002, AR-006, and AR-009, a consistent pattern emerges: overconfidence → alert fatigue → HITL failure → catastrophe. Each stage makes the next worse.

Memory poisoning (AR-006, >95% success) feeds corrupted data into the system. Overconfident calibration (AR-009, 84%) means the system doesn't flag corruption. Alert fatigue (AR-002, 67% ignored) means humans don't catch what the system misses. The spiral accelerates.

This is the strongest cross-cutting finding: security, calibration, and human factors form a doom loop that no single intervention addresses.

## See Also
- [[10-MOCs/MOC-Insights]]
- [[10-MOCs/MOC-Reports]]
