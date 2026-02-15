#!/bin/bash
# Generate all 5 vaults with 50 notes each
BASE="/Users/florianziesche/.openclaw/workspace/experiments/vault-compound-test"

###############################################################################
# CONTENT DEFINITIONS (shared across all vaults)
###############################################################################

# We'll write notes directly per vault since each has different structure.
# This script generates Vault A (flat) then transforms for B-E.

###############################################################################
# VAULT A: FLAT
###############################################################################
VA="$BASE/vault-a-flat"

# --- 30 Claims ---
cat > "$VA/C-001 Agent Market Growth.md" << 'EOF'
---
tags: [claim, market, ar-001]
---
# C-001: AI Agent Market Growth

The AI agent market will grow from $7.8B to $52B by 2030 (45.8% CAGR).

**Source:** AR-001, industry projections
**Confidence:** High (multiple analyst consensus)
EOF

cat > "$VA/C-002 Corporate AI Failure Rate.md" << 'EOF'
---
tags: [claim, failure, ar-001]
---
# C-002: Corporate AI Project Failure Rate

95% of corporate AI projects fail to deliver expected outcomes.

**Source:** AR-001
**Confidence:** High
EOF

cat > "$VA/C-003 LLM Overconfidence.md" << 'EOF'
---
tags: [claim, calibration, ar-001, ar-009]
---
# C-003: LLM Overconfidence Rate

84% of LLMs are overconfident — confidence exceeds actual accuracy across 9 models and 351 scenarios.

**Source:** AR-001, AR-009 (PMC study)
**Confidence:** High (peer-reviewed)
EOF

cat > "$VA/C-004 EBIT Impact.md" << 'EOF'
---
tags: [claim, roi, ar-001]
---
# C-004: Enterprise AI EBIT Impact

Only 6% of enterprises achieve meaningful EBIT impact from AI agents (McKinsey, n=1,993).

**Source:** AR-001
**Confidence:** High
EOF

cat > "$VA/C-005 Calibration Cost.md" << 'EOF'
---
tags: [claim, calibration, cost, ar-001, ar-009]
---
# C-005: Calibration Infrastructure Cost

Calibration infrastructure costs $0.005 per check vs. $4.4M average AI-related losses per company.

**Source:** AR-001, AR-009
**Confidence:** High
EOF

cat > "$VA/C-006 EU AI Act Penalties.md" << 'EOF'
---
tags: [claim, regulation, ar-003]
---
# C-006: EU AI Act Penalties

EU AI Act enforcement begins August 2026 with penalties up to €35M or 7% of global revenue.

**Source:** AR-003
**Confidence:** High (legislative fact)
EOF

cat > "$VA/C-007 Trust Erosion.md" << 'EOF'
---
tags: [claim, trust, ar-001]
---
# C-007: Worker Trust Erosion

AI usage increased 13% but worker confidence dropped 18% (ManpowerGroup, n=14K workers).

**Source:** AR-001
**Confidence:** High
EOF

cat > "$VA/C-008 Financial Losses.md" << 'EOF'
---
tags: [claim, cost, ar-002]
---
# C-008: Enterprise AI Financial Losses

99% of enterprises deploying AI report financial losses, averaging $4.4M per company (EY RAI Pulse, n=975).

**Source:** AR-002
**Confidence:** High
EOF

cat > "$VA/C-009 Workslop Rework.md" << 'EOF'
---
tags: [claim, cost, ar-002]
---
# C-009: Workslop Rework Cost

Workslop rework costs $186/employee/month in AI-heavy workflows — $9M/year at 10K employees.

**Source:** AR-002 (Stanford/HBR)
**Confidence:** Medium-High
EOF

cat > "$VA/C-010 Shadow AI Breach.md" << 'EOF'
---
tags: [claim, security, cost, ar-002]
---
# C-010: Shadow AI Breach Premium

Shadow AI breach premium: $670K above standard breach ($4.63M total), 247 days to detect.

**Source:** AR-002
**Confidence:** High
EOF

cat > "$VA/C-011 Alert Fatigue.md" << 'EOF'
---
tags: [claim, hitl, security, ar-002, ar-009]
---
# C-011: Alert Fatigue in SOC Operations

67% of SOC alerts are ignored due to alert fatigue. 80-99% of healthcare AI alerts are false positives. HITL becomes a rubber stamp.

**Source:** AR-002, AR-009
**Confidence:** High
EOF

cat > "$VA/C-012 Compliance Cost.md" << 'EOF'
---
tags: [claim, regulation, cost, ar-003]
---
# C-012: EU AI Act Compliance Cost

EU AI Act compliance costs $2-5M for initial setup, 5-20x higher than US equivalents.

**Source:** AR-003
**Confidence:** Medium-High
EOF

cat > "$VA/C-013 Agent Shaped Hole.md" << 'EOF'
---
tags: [claim, regulation, ar-003]
---
# C-013: Agent-Shaped Regulatory Hole

Neither EU nor US framework specifically defines or addresses AI agents — multi-agent liability is a regulatory black hole.

**Source:** AR-003
**Confidence:** High
EOF

cat > "$VA/C-014 Maturity Gap.md" << 'EOF'
---
tags: [claim, maturity, ar-004]
---
# C-014: Experimentation vs Production Gap

62% of organizations experiment with agents, <10% deploy enterprise-wide, only 6% see EBIT impact.

**Source:** AR-004
**Confidence:** High
EOF

cat > "$VA/C-015 Banking AI Potential.md" << 'EOF'
---
tags: [claim, financial-services, ar-005]
---
# C-015: Banking Employee AI Impact

73% of banking employee time has AI impact potential — 39% automation, 34% augmentation.

**Source:** AR-005 (Accenture)
**Confidence:** High
EOF

cat > "$VA/C-016 JPMorgan AI.md" << 'EOF'
---
tags: [claim, financial-services, ar-005]
---
# C-016: JPMorgan AI Deployment

JPMorgan has 2,000+ AI use cases and $150B+ daily fraud detection, but mostly supervised tooling, not autonomous agents.

**Source:** AR-005
**Confidence:** High
EOF

cat > "$VA/C-017 Prompt Injection.md" << 'EOF'
---
tags: [claim, security, ar-006]
---
# C-017: Prompt Injection Defenses Broken

Every published prompt injection defense (12/12) has been broken by adaptive attacks from Meta/OpenAI/Anthropic/DeepMind researchers.

**Source:** AR-006
**Confidence:** High (peer-reviewed)
EOF

cat > "$VA/C-018 Memory Injection.md" << 'EOF'
---
tags: [claim, security, memory, ar-006]
---
# C-018: Memory Injection Success Rate

Memory injection attacks (MINJA) achieve >95% success rates, creating persistent backdoors that survive session resets.

**Source:** AR-006
**Confidence:** High
EOF

cat > "$VA/C-019 Multi-Agent Hijacking.md" << 'EOF'
---
tags: [claim, security, multi-agent, ar-006]
---
# C-019: Multi-Agent System Hijacking

Multi-agent system hijacking succeeds 45-64% across AutoGen/CrewAI/MetaGPT. Zero inter-agent trust verification exists.

**Source:** AR-006
**Confidence:** High
EOF

cat > "$VA/C-020 Agent Attack Surface.md" << 'EOF'
---
tags: [claim, security, ar-006]
---
# C-020: Agent Attack Surface

Agent attack surface is 7x larger than chatbots: direct prompt, indirect prompt, persistent memory, tool/API calls, inter-agent comms, credentials, external data.

**Source:** AR-006
**Confidence:** High
EOF

cat > "$VA/C-021 Multi-Agent Cost.md" << 'EOF'
---
tags: [claim, cost, orchestration, ar-007]
---
# C-021: Multi-Agent Cost Scaling

Multi-agent cost scales super-linearly: 5-agent pipeline costs 10-30x a single agent, not 5x.

**Source:** AR-007
**Confidence:** Medium-High
EOF

cat > "$VA/C-022 Agentic Project Cancellation.md" << 'EOF'
---
tags: [claim, orchestration, ar-007]
---
# C-022: Agentic Project Cancellation Rate

>40% of agentic AI projects will be canceled by 2027. Performance quality (not cost or safety) is the #1 barrier.

**Source:** AR-007
**Confidence:** Medium (forecast)
EOF

cat > "$VA/C-023 Board AI Competence.md" << 'EOF'
---
tags: [claim, governance, ar-008]
---
# C-023: Board AI Competence Gap

Only 22% of CEOs say their board effectively supports them on AI challenges.

**Source:** AR-008
**Confidence:** High
EOF

cat > "$VA/C-024 Caremark Extension.md" << 'EOF'
---
tags: [claim, governance, legal, ar-008]
---
# C-024: Caremark Duty Extends to AI

Caremark duty of oversight is extending to AI — directors who fail to monitor AI risk face personal liability under Delaware law.

**Source:** AR-008
**Confidence:** Medium-High (legal interpretation)
EOF

cat > "$VA/C-025 VCE Bias.md" << 'EOF'
---
tags: [claim, calibration, ar-009]
---
# C-025: Verbalized Confidence Bias

Verbalized confidence expression (VCE) is biased upward by 20-30 percentage points, with poor correlation to correctness (r ≈ 0.3-0.5).

**Source:** AR-009
**Confidence:** High (peer-reviewed)
EOF

cat > "$VA/C-026 Multi-Agent Amplification.md" << 'EOF'
---
tags: [claim, calibration, multi-agent, ar-009]
---
# C-026: Multi-Agent Calibration Amplification

Multi-agent verification amplifies miscalibration instead of correcting it — compound overconfidence approaches 100% in 3-agent chains.

**Source:** AR-009
**Confidence:** High
EOF

cat > "$VA/C-027 Trust Debt.md" << 'EOF'
---
tags: [claim, cost, trust, ar-002]
---
# C-027: Trust Debt Compounds

Trust Debt is like technical debt but worse — retroactive trust infrastructure costs 5-10x proactive deployment.

**Source:** AR-002
**Confidence:** Medium-High
EOF

cat > "$VA/C-028 Klarna Rollback.md" << 'EOF'
---
tags: [claim, financial-services, ar-002, ar-005]
---
# C-028: Klarna AI Rollback

Klarna claimed $60M savings and replaced 853 FTEs, then required partial rollback — metrics masked quality degradation.

**Source:** AR-002, AR-005
**Confidence:** High
EOF

cat > "$VA/C-029 ISO 42001.md" << 'EOF'
---
tags: [claim, regulation, standards, ar-003]
---
# C-029: ISO 42001 as Bridge Standard

ISO 42001 serves as bridge between EU and US compliance. AWS was first certified (Jan 2026). Voluntary but satisfies both regimes.

**Source:** AR-003
**Confidence:** High
EOF

cat > "$VA/C-030 Banking Compliance Cost.md" << 'EOF'
---
tags: [claim, financial-services, cost, ar-005]
---
# C-030: Banking Annual Compliance Cost

Financial services faces $270B annual compliance costs + 55-65% cost ratios, making AI agent adoption structurally inevitable.

**Source:** AR-005
**Confidence:** High
EOF

# --- 10 Key Concepts ---
cat > "$VA/K-001 Trust.md" << 'EOF'
---
tags: [concept, trust]
---
# K-001: Trust

Trust is the central theme across all Ainary reports. Three-layer trust gap: Communication (solved), Identity (emerging), Trustworthiness (missing). No standardized trust-scoring protocol exists.

Trust Tax = hidden costs of deploying AI without trust infrastructure ($4.4M avg losses). Trust Debt compounds at 5-10x if not addressed proactively.

Trust erosion spiral: overconfidence → discovery → alert fatigue → binary choice → catastrophe.

**Appears in:** AR-001, AR-002, AR-004, AR-005, AR-008, AR-009
EOF

cat > "$VA/K-002 Calibration.md" << 'EOF'
---
tags: [concept, calibration]
---
# K-002: Calibration

The process of aligning AI confidence with actual accuracy. 84% of LLMs are overconfident. VCE is biased 20-30pp upward.

Five methods: Temperature Scaling (gold standard), Conformal Prediction (guaranteed coverage), Sample Consistency (black-box, $0.003/check), Budget-CoCoA (SOTA, $0.005/check), Selective Prediction (requires retraining).

Calibration is the cheapest intervention with the highest ROI: $0.005/check vs $4.4M losses. ROI ratio 1:1,500,000.

**Appears in:** AR-001, AR-002, AR-004, AR-005, AR-009
EOF

cat > "$VA/K-003 HITL.md" << 'EOF'
---
tags: [concept, hitl, human-oversight]
---
# K-003: Human-in-the-Loop (HITL)

The regulatory and operational requirement for human oversight of AI systems. EU AI Act Article 14 mandates "effective human oversight."

The HITL paradox: regulation requires it, but empirical evidence shows it fails. 67% of SOC alerts ignored. 80-99% healthcare false positives. Alert fatigue turns HITL into rubber stamp.

When calibration is poor, HITL is overwhelmed with false signals and becomes ineffective. Improving calibration directly improves HITL effectiveness by reducing noise.

**Appears in:** AR-002, AR-003, AR-006, AR-009
EOF

cat > "$VA/K-004 Memory.md" << 'EOF'
---
tags: [concept, memory, security]
---
# K-004: Memory Architecture

AI agent memory is a critical attack surface. No production memory framework (Letta, Mem0, Zep, LangMem, A-Mem) implements provenance tracking, integrity checks, or confidence scoring.

Memory injection (MINJA) achieves >95% success rates, creating persistent backdoors. Memory poisoning + no detection + propagation + human failure = self-reinforcing attack loop.

Memory = persistent backdoor when compromised. Key gap: no provenance tracking for memory entries.

**Appears in:** AR-001, AR-006
EOF

cat > "$VA/K-005 Compounding.md" << 'EOF'
---
tags: [concept, compounding, knowledge]
---
# K-005: Compounding

The principle that knowledge generates increasing returns when properly structured. Trust Debt compounds negatively at 5-10x. Calibration ROI compounds positively at 1:1,500,000.

Multi-agent systems can compound errors (overconfidence amplification) or compound value (orchestrated correctly). The architecture of knowledge storage determines whether compounding is positive or negative.

Reports show compounding in: trust erosion spiral (negative), calibration infrastructure ROI (positive), regulatory compliance (builds defensibility over time).

**Appears in:** AR-001, AR-002, AR-007, AR-009
EOF

cat > "$VA/K-006 Regulation.md" << 'EOF'
---
tags: [concept, regulation, compliance]
---
# K-006: Regulation

EU AI Act: Full enforcement August 2026, €35M penalties. US: Zero federal framework after Biden EO rescinded. State patchwork (40+ bills).

Regulatory trilemma: Deploy fast OR compliant OR insured — can't have all three. ISO 42001 as bridge standard.

Agent-shaped hole: Neither jurisdiction defines AI agents specifically. Multi-agent liability = black hole. EU has extraterritorial reach.

**Appears in:** AR-001, AR-003, AR-005, AR-008
EOF

cat > "$VA/K-007 Multi-Agent Systems.md" << 'EOF'
---
tags: [concept, multi-agent, orchestration]
---
# K-007: Multi-Agent Systems

Systems where multiple AI agents collaborate. Cost scales super-linearly (10-30x, not 5x). Nine failure modes including infinite loops, deadlocks, cascading failures.

Hijacking succeeds 45-64%. Inter-agent messages trusted by default. Verification chains create false consensus, not quality assurance.

Anthropic's counterintuitive finding: raw LLM API calls + simple patterns outperform complex multi-agent frameworks for most use cases.

**Appears in:** AR-001, AR-006, AR-007, AR-009
EOF

cat > "$VA/K-008 Governance.md" << 'EOF'
---
tags: [concept, governance, boards]
---
# K-008: Governance

Board-level AI oversight is structurally inadequate. Only 22% of CEOs say boards support them on AI. Average director age 59.1, rising.

Caremark duty extending to AI: directors face personal liability for failing to monitor AI risk. Seven essential board questions defined.

Organizations with fragile AI governance miss 40% of projected productivity gains.

**Appears in:** AR-002, AR-004, AR-008
EOF

cat > "$VA/K-009 Security.md" << 'EOF'
---
tags: [concept, security, attack-surface]
---
# K-009: Security

Agent attack surface is 7x larger than chatbots across 7 vectors. Prompt injection is fundamentally unsolvable (same modality for instructions and data).

Defense strategy: architectural constraints (privilege separation, deterministic guardrails, kill switches), not better prompt engineering.

Supply chain risk: MCP tool servers = npm packages with no code review, no signing, no sandbox.

**Appears in:** AR-001, AR-005, AR-006, AR-007
EOF

cat > "$VA/K-010 Maturity.md" << 'EOF'
---
tags: [concept, maturity, framework]
---
# K-010: Maturity

AGENT framework: 5 dimensions (Autonomy, Governance, Error Handling, Networked Trust, Team Integration) across 5 levels (Ad Hoc → Calibrated → Orchestrated → Autonomous).

Level 3 (Calibrated) is survival threshold for August 2026. 80%+ of organizations are at Level 1. Existing maturity models (Gartner, McKinsey, etc.) have agent-shaped blind spots.

Level 1→3 playbook: Inventory (1-3 months), Calibration ($0.005/check, 3-9 months).

**Appears in:** AR-004, AR-001, AR-002
EOF

# --- 5 Insights ---
cat > "$VA/I-001 Trust Erosion Spiral.md" << 'EOF'
---
tags: [insight, cross-cutting]
---
# I-001: The Trust Erosion Spiral is Self-Reinforcing

Across AR-001, AR-002, AR-006, and AR-009, a consistent pattern emerges: overconfidence → alert fatigue → HITL failure → catastrophe. Each stage makes the next worse.

Memory poisoning (AR-006, >95% success) feeds corrupted data into the system. Overconfident calibration (AR-009, 84%) means the system doesn't flag corruption. Alert fatigue (AR-002, 67% ignored) means humans don't catch what the system misses. The spiral accelerates.

This is the strongest cross-cutting finding: security, calibration, and human factors form a doom loop that no single intervention addresses.
EOF

cat > "$VA/I-002 Calibration as Keystone.md" << 'EOF'
---
tags: [insight, cross-cutting]
---
# I-002: Calibration is the Keystone Intervention

At $0.005/check with ROI of 1:1,500,000, calibration appears in 7 of 9 reports as either a solution or a missing capability. It addresses:

- Overconfidence (AR-009): directly
- Alert fatigue (AR-002): reduces false signals → meaningful HITL
- Security (AR-006): detects anomalous confidence patterns
- Governance (AR-008): provides auditable trust metrics for boards
- Compliance (AR-003): satisfies "effective oversight" requirements
- Financial services (AR-005): enables trust scoring regulators demand
- Maturity (AR-004): Level 3 threshold requires calibrated confidence

No other single intervention touches this many problem domains.
EOF

cat > "$VA/I-003 Regulation-Reality Gap.md" << 'EOF'
---
tags: [insight, cross-cutting]
---
# I-003: Regulation Demands What Technology Can't Deliver

EU AI Act (AR-003) mandates "effective human oversight" (Article 14). But:
- 67% of alerts ignored (AR-002)
- HITL is empirically broken (AR-009)
- Prompt injection is unsolvable (AR-006)
- Multi-agent liability undefined (AR-003)

Regulators assume a world where human oversight works. Evidence shows it doesn't at scale. This creates a compliance theater risk: organizations technically compliant but practically unprotected.
EOF

cat > "$VA/I-004 Cost Asymmetry.md" << 'EOF'
---
tags: [insight, cross-cutting]
---
# I-004: Extreme Cost Asymmetry Between Prevention and Failure

Consistent across reports:
- Calibration: $0.005/check vs. $4.4M losses (AR-009)
- Compliance: $2-5M setup vs. €35M penalties (AR-003)
- Trust infrastructure: $135/month vs. $7.5B VW failure (AR-009)
- Proactive vs. retroactive: 1x vs. 5-10x cost (AR-002)

The prevention-to-failure cost ratio ranges from 1:700 to 1:1,500,000. This is the strongest economic argument for trust infrastructure.
EOF

cat > "$VA/I-005 Multi-Agent Paradox.md" << 'EOF'
---
tags: [insight, cross-cutting]
---
# I-005: Multi-Agent Systems Amplify Both Value and Risk

Multi-agent systems (AR-007) promise orchestrated intelligence but empirically:
- Cost 10-30x (not linear) — AR-007
- Hijacking at 45-64% — AR-006
- False consensus from verification chains — AR-009
- 40% cancellation rate — AR-007

Yet Anthropic finds simple patterns outperform complex frameworks. The paradox: the industry builds toward multi-agent, but evidence favors single-agent + simple orchestration for most use cases.
EOF

# --- 5 Decisions ---
cat > "$VA/D-001 Report Template.md" << 'EOF'
---
tags: [decision]
---
# D-001: Report Template Design

**Decision:** Standardize all Ainary Research Reports with: Executive Summary, Key Insights (5), Sales Angles (3), Content Ideas (3), Links section.

**Rationale:** Consistent structure enables cross-report analysis and makes reports actionable for sales, content, and product teams simultaneously.

**Date:** 2026-02-14
**Status:** Implemented (AR-001 through AR-009)
EOF

cat > "$VA/D-002 Calibration Focus.md" << 'EOF'
---
tags: [decision]
---
# D-002: Calibration as Core Product Thesis

**Decision:** Position calibration infrastructure as Ainary's primary value proposition, not general AI governance.

**Rationale:** Calibration touches 7/9 reports, has clearest ROI ($0.005 vs $4.4M), and is the keystone intervention. Narrower positioning = stronger differentiation.

**Date:** 2026-02-14
**Status:** Active
EOF

cat > "$VA/D-003 EU-First Compliance.md" << 'EOF'
---
tags: [decision]
---
# D-003: Build EU Compliance as Floor

**Decision:** Design all products and frameworks to satisfy EU AI Act requirements first, then adapt for US market.

**Rationale:** EU is stricter and has extraterritorial reach. Building for EU compliance creates a ceiling that automatically satisfies most US state requirements.

**Date:** 2026-02-14
**Status:** Active
EOF

cat > "$VA/D-004 Anti-Complexity.md" << 'EOF'
---
tags: [decision]
---
# D-004: Anti-Complexity Stance on Multi-Agent

**Decision:** Recommend single-agent + simple orchestration patterns over complex multi-agent frameworks in client engagements.

**Rationale:** Anthropic's finding (AR-007) that simple patterns outperform complex frameworks, plus 10-30x cost multiplier and 40% cancellation rate for multi-agent projects.

**Date:** 2026-02-14
**Status:** Active
EOF

cat > "$VA/D-005 Board Governance Product.md" << 'EOF'
---
tags: [decision]
---
# D-005: Board Governance Training as Revenue Stream

**Decision:** Develop a "Board AI Readiness" product combining AR-008 governance framework with AR-004 maturity assessment.

**Rationale:** 22% CEO board satisfaction + Caremark liability extension + August 2026 deadline = urgent buyer need. High-ticket, low-delivery-cost service.

**Date:** 2026-02-14
**Status:** Planned
EOF

echo "Vault A (FLAT) complete: 50 notes"
