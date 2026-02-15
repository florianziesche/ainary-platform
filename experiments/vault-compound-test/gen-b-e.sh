#!/bin/bash
BASE="/Users/florianziesche/.openclaw/workspace/experiments/vault-compound-test"
VA="$BASE/vault-a-flat"
VB="$BASE/vault-b-para"
VC="$BASE/vault-c-zettelkasten"
VD="$BASE/vault-d-moc-hybrid"
VE="$BASE/vault-e-graph-first"

###############################################################################
# VAULT B: PARA - Organize by actionability
###############################################################################
# Projects: Active research (Claims, Decisions)
# Areas: Ongoing concerns (Concepts)
# Resources: Reference material (Insights)
# Archive: Completed items

# Projects/Agent-Trust-Research: Claims related to active research
for f in "$VA"/C-*.md; do
  cp "$f" "$VB/Projects/Agent-Trust-Research/"
done

# Areas/AI-Governance: Concepts
for f in "$VA"/K-*.md; do
  cp "$f" "$VB/Areas/AI-Governance/"
done

# Resources/Frameworks: Insights
for f in "$VA"/I-*.md; do
  cp "$f" "$VB/Resources/Frameworks/"
done

# Archive/Completed: Decisions
for f in "$VA"/D-*.md; do
  cp "$f" "$VB/Archive/Completed/"
done

# Add minimal links within projects only (PARA style)
for f in "$VB/Projects/Agent-Trust-Research"/C-*.md; do
  echo -e "\n## Project Context\nPart of: Agent Trust Research Project" >> "$f"
done

echo "Vault B (PARA) complete: $(find "$VB" -name '*.md' | wc -l) notes"

###############################################################################
# VAULT C: ZETTELKASTEN - Atomic notes, dense cross-linking, sequence IDs
###############################################################################

# Create index notes
cat > "$VC/0-Index.md" << 'EOFI'
# Index

## Claims
- [[1a-agent-market-growth]]
- [[1b-corporate-ai-failure]]
- [[1c-llm-overconfidence]]
- [[1d-ebit-impact]]
- [[1e-calibration-cost]]
- [[2a-eu-penalties]]
- [[2b-trust-erosion]]
- [[2c-financial-losses]]
- [[2d-workslop-rework]]
- [[2e-shadow-ai-breach]]
- [[3a-alert-fatigue]]
- [[3b-compliance-cost]]
- [[3c-agent-regulatory-hole]]
- [[3d-maturity-gap]]
- [[3e-banking-ai-potential]]
- [[4a-jpmorgan-ai]]
- [[4b-prompt-injection]]
- [[4c-memory-injection]]
- [[4d-multi-agent-hijacking]]
- [[4e-agent-attack-surface]]
- [[5a-multi-agent-cost]]
- [[5b-agentic-cancellation]]
- [[5c-board-competence]]
- [[5d-caremark-extension]]
- [[5e-vce-bias]]
- [[6a-multi-agent-amplification]]
- [[6b-trust-debt]]
- [[6c-klarna-rollback]]
- [[6d-iso-42001]]
- [[6e-banking-compliance-cost]]

## Concepts
- [[7a-trust]]
- [[7b-calibration]]
- [[7c-hitl]]
- [[7d-memory]]
- [[7e-compounding]]
- [[8a-regulation]]
- [[8b-multi-agent-systems]]
- [[8c-governance]]
- [[8d-security]]
- [[8e-maturity]]

## Insights
- [[9a-trust-erosion-spiral]]
- [[9b-calibration-keystone]]
- [[9c-regulation-reality-gap]]
- [[9d-cost-asymmetry]]
- [[9e-multi-agent-paradox]]

## Decisions
- [[10a-report-template]]
- [[10b-calibration-focus]]
- [[10c-eu-first]]
- [[10d-anti-complexity]]
- [[10e-board-governance]]
EOFI

# Function to create zettelkasten note with links
zk_note() {
  local id="$1" title="$2" content="$3" links="$4"
  cat > "$VC/$id.md" << EOF
# $title

$content

## Links
$links
EOF
}

# Claims as atomic zettelkasten notes (with 3+ links each)
zk_note "1a-agent-market-growth" "Agent Market Growth" \
"The AI agent market will grow from \$7.8B to \$52B by 2030 (45.8% CAGR). Source: AR-001." \
"- [[1b-corporate-ai-failure]] — yet 95% of projects fail
- [[1d-ebit-impact]] — only 6% see EBIT impact
- [[7a-trust]] — trust gap explains the disparity
- [[0-Index]]"

zk_note "1b-corporate-ai-failure" "Corporate AI Failure Rate" \
"95% of corporate AI projects fail to deliver expected outcomes. Source: AR-001." \
"- [[1a-agent-market-growth]] — despite massive market growth
- [[3d-maturity-gap]] — maturity, not technology, is the gap
- [[7e-compounding]] — failures compound into trust debt
- [[0-Index]]"

zk_note "1c-llm-overconfidence" "LLM Overconfidence Rate" \
"84% of LLMs are overconfident — confidence exceeds actual accuracy across 9 models, 351 scenarios. Source: AR-001, AR-009." \
"- [[5e-vce-bias]] — VCE biased 20-30pp upward
- [[7b-calibration]] — calibration is the fix
- [[3a-alert-fatigue]] — overconfidence drives alert fatigue
- [[9a-trust-erosion-spiral]] — feeds the doom loop
- [[0-Index]]"

zk_note "1d-ebit-impact" "Enterprise AI EBIT Impact" \
"Only 6% of enterprises achieve meaningful EBIT impact from AI agents (McKinsey, n=1,993). Source: AR-001." \
"- [[1a-agent-market-growth]] — market grows despite low impact
- [[3d-maturity-gap]] — 62% experiment, 6% succeed
- [[8e-maturity]] — maturity model explains why
- [[0-Index]]"

zk_note "1e-calibration-cost" "Calibration Infrastructure Cost" \
"Calibration costs \$0.005/check vs. \$4.4M average losses per company. Source: AR-001, AR-009." \
"- [[7b-calibration]] — concept overview
- [[9d-cost-asymmetry]] — extreme prevention/failure ratio
- [[2c-financial-losses]] — the \$4.4M it prevents
- [[10b-calibration-focus]] — our strategic decision
- [[0-Index]]"

zk_note "2a-eu-penalties" "EU AI Act Penalties" \
"EU AI Act enforcement begins August 2026 with penalties up to €35M or 7% of global revenue. Source: AR-003." \
"- [[3b-compliance-cost]] — \$2-5M setup cost
- [[8a-regulation]] — regulatory landscape
- [[10c-eu-first]] — our compliance strategy
- [[0-Index]]"

zk_note "2b-trust-erosion" "Worker Trust Erosion" \
"AI usage increased 13% but worker confidence dropped 18% (ManpowerGroup, n=14K). Source: AR-001." \
"- [[7a-trust]] — trust is the central theme
- [[9a-trust-erosion-spiral]] — part of the spiral
- [[6b-trust-debt]] — this is trust debt accumulating
- [[0-Index]]"

zk_note "2c-financial-losses" "Enterprise AI Financial Losses" \
"99% of enterprises deploying AI report financial losses, averaging \$4.4M per company (EY, n=975). Source: AR-002." \
"- [[1e-calibration-cost]] — \$0.005 fix
- [[9d-cost-asymmetry]] — extreme ratio
- [[6b-trust-debt]] — losses = trust debt
- [[0-Index]]"

zk_note "2d-workslop-rework" "Workslop Rework Cost" \
"Workslop rework costs \$186/employee/month in AI-heavy workflows — \$9M/year at 10K employees. Source: AR-002." \
"- [[2c-financial-losses]] — part of the \$4.4M
- [[7a-trust]] — trust tax line item
- [[1c-llm-overconfidence]] — overconfidence causes rework
- [[0-Index]]"

zk_note "2e-shadow-ai-breach" "Shadow AI Breach Premium" \
"Shadow AI breach premium: \$670K above standard breach (\$4.63M total), 247 days to detect. Source: AR-002." \
"- [[8d-security]] — security concept
- [[2c-financial-losses]] — another trust tax line item
- [[7a-trust]] — trust erosion driver
- [[0-Index]]"

zk_note "3a-alert-fatigue" "Alert Fatigue in SOC Operations" \
"67% of SOC alerts are ignored. 80-99% of healthcare AI alerts are false positives. HITL becomes rubber stamp. Source: AR-002, AR-009." \
"- [[7c-hitl]] — HITL concept
- [[1c-llm-overconfidence]] — overconfidence → too many alerts
- [[9a-trust-erosion-spiral]] — Phase 3 of the spiral
- [[9c-regulation-reality-gap]] — regulators assume HITL works
- [[0-Index]]"

zk_note "3b-compliance-cost" "EU AI Act Compliance Cost" \
"EU AI Act compliance costs \$2-5M for initial setup, 5-20x higher than US equivalents. Source: AR-003." \
"- [[2a-eu-penalties]] — vs €35M penalties
- [[9d-cost-asymmetry]] — still cheaper than non-compliance
- [[8a-regulation]] — regulatory landscape
- [[0-Index]]"

zk_note "3c-agent-regulatory-hole" "Agent-Shaped Regulatory Hole" \
"Neither EU nor US framework defines AI agents. Multi-agent liability is a black hole. Source: AR-003." \
"- [[8a-regulation]] — regulatory concept
- [[8b-multi-agent-systems]] — what's undefined
- [[9c-regulation-reality-gap]] — regulation vs reality
- [[0-Index]]"

zk_note "3d-maturity-gap" "Experimentation vs Production Gap" \
"62% experiment with agents, <10% deploy enterprise-wide, only 6% see EBIT impact. Source: AR-004." \
"- [[1d-ebit-impact]] — the 6% number
- [[8e-maturity]] — maturity model explains gap
- [[1b-corporate-ai-failure]] — 95% failure rate
- [[0-Index]]"

zk_note "3e-banking-ai-potential" "Banking Employee AI Impact" \
"73% of banking employee time has AI impact potential — 39% automation, 34% augmentation. Source: AR-005." \
"- [[6e-banking-compliance-cost]] — why banks must adopt
- [[4a-jpmorgan-ai]] — deployment reality
- [[7a-trust]] — but trust gap prevents full adoption
- [[0-Index]]"

zk_note "4a-jpmorgan-ai" "JPMorgan AI Deployment" \
"JPMorgan has 2,000+ AI use cases and \$150B+ daily fraud detection — mostly supervised tooling, not autonomous agents. Source: AR-005." \
"- [[3e-banking-ai-potential]] — banking AI potential
- [[3d-maturity-gap]] — use cases ≠ autonomous deployment
- [[8e-maturity]] — Level 1-2 maturity despite scale
- [[0-Index]]"

zk_note "4b-prompt-injection" "Prompt Injection Defenses Broken" \
"Every published prompt injection defense (12/12) has been broken by adaptive attacks. Source: AR-006." \
"- [[8d-security]] — security concept
- [[4e-agent-attack-surface]] — one of 7 vectors
- [[7b-calibration]] — calibration detects anomalies
- [[0-Index]]"

zk_note "4c-memory-injection" "Memory Injection Success Rate" \
"MINJA attacks achieve >95% success rates, creating persistent backdoors surviving session resets. Source: AR-006." \
"- [[7d-memory]] — memory architecture concept
- [[9a-trust-erosion-spiral]] — feeds the spiral
- [[8d-security]] — critical security gap
- [[4b-prompt-injection]] — related attack vector
- [[0-Index]]"

zk_note "4d-multi-agent-hijacking" "Multi-Agent System Hijacking" \
"Multi-agent hijacking succeeds 45-64% across AutoGen/CrewAI/MetaGPT. Zero inter-agent trust verification. Source: AR-006." \
"- [[8b-multi-agent-systems]] — MAS concept
- [[8d-security]] — security vector
- [[6a-multi-agent-amplification]] — amplifies miscalibration too
- [[0-Index]]"

zk_note "4e-agent-attack-surface" "Agent Attack Surface" \
"Agent attack surface is 7x larger than chatbots: 7 vectors. Source: AR-006." \
"- [[8d-security]] — security concept
- [[4b-prompt-injection]] — vector 1
- [[4c-memory-injection]] — vector 3
- [[4d-multi-agent-hijacking]] — vector 5
- [[0-Index]]"

zk_note "5a-multi-agent-cost" "Multi-Agent Cost Scaling" \
"5-agent pipeline costs 10-30x a single agent, not 5x. Super-linear scaling. Source: AR-007." \
"- [[8b-multi-agent-systems]] — MAS concept
- [[9e-multi-agent-paradox]] — the paradox
- [[5b-agentic-cancellation]] — drives cancellations
- [[10d-anti-complexity]] — our stance
- [[0-Index]]"

zk_note "5b-agentic-cancellation" "Agentic Project Cancellation Rate" \
">40% of agentic AI projects will be canceled by 2027. Performance quality is #1 barrier. Source: AR-007." \
"- [[5a-multi-agent-cost]] — cost driver
- [[8b-multi-agent-systems]] — MAS concept
- [[10d-anti-complexity]] — our recommendation
- [[0-Index]]"

zk_note "5c-board-competence" "Board AI Competence Gap" \
"Only 22% of CEOs say their board supports them on AI. Source: AR-008." \
"- [[8c-governance]] — governance concept
- [[5d-caremark-extension]] — creates liability
- [[10e-board-governance]] — our product opportunity
- [[0-Index]]"

zk_note "5d-caremark-extension" "Caremark Duty Extends to AI" \
"Directors who fail to monitor AI risk face personal liability under Delaware law. Source: AR-008." \
"- [[8c-governance]] — governance concept
- [[5c-board-competence]] — board isn't ready
- [[2a-eu-penalties]] — regulatory pressure
- [[0-Index]]"

zk_note "5e-vce-bias" "Verbalized Confidence Bias" \
"VCE is biased upward by 20-30pp, poor correlation with correctness (r ≈ 0.3-0.5). Source: AR-009." \
"- [[1c-llm-overconfidence]] — the overconfidence problem
- [[7b-calibration]] — calibration fixes this
- [[6a-multi-agent-amplification]] — amplified in chains
- [[0-Index]]"

zk_note "6a-multi-agent-amplification" "Multi-Agent Calibration Amplification" \
"Multi-agent verification amplifies miscalibration. Compound overconfidence approaches 100% in 3-agent chains. Source: AR-009." \
"- [[5e-vce-bias]] — individual agent bias
- [[8b-multi-agent-systems]] — MAS concept
- [[9e-multi-agent-paradox]] — the paradox
- [[7b-calibration]] — calibration as fix
- [[0-Index]]"

zk_note "6b-trust-debt" "Trust Debt Compounds" \
"Retroactive trust infrastructure costs 5-10x proactive deployment. Source: AR-002." \
"- [[7a-trust]] — trust concept
- [[7e-compounding]] — negative compounding
- [[2c-financial-losses]] — the cost
- [[9d-cost-asymmetry]] — prevention is cheaper
- [[0-Index]]"

zk_note "6c-klarna-rollback" "Klarna AI Rollback" \
"Klarna claimed \$60M savings, replaced 853 FTEs, then required partial rollback. Metrics masked quality degradation. Source: AR-002, AR-005." \
"- [[2c-financial-losses]] — financial impact
- [[3e-banking-ai-potential]] — banking context
- [[1c-llm-overconfidence]] — root cause
- [[8c-governance]] — board oversight failure
- [[0-Index]]"

zk_note "6d-iso-42001" "ISO 42001 as Bridge Standard" \
"ISO 42001 bridges EU and US compliance. AWS first certified Jan 2026. Source: AR-003." \
"- [[8a-regulation]] — regulatory context
- [[2a-eu-penalties]] — what it helps avoid
- [[10c-eu-first]] — our compliance strategy
- [[0-Index]]"

zk_note "6e-banking-compliance-cost" "Banking Annual Compliance Cost" \
"\$270B annual compliance costs + 55-65% cost ratios make AI adoption structurally inevitable. Source: AR-005." \
"- [[3e-banking-ai-potential]] — banking potential
- [[9d-cost-asymmetry]] — cost dynamics
- [[6c-klarna-rollback]] — but not without risk
- [[0-Index]]"

# Concepts
zk_note "7a-trust" "Trust" \
"Central theme across all reports. Three-layer gap: Communication (solved), Identity (emerging), Trustworthiness (missing). Trust Tax = hidden costs (\$4.4M avg). Trust Debt compounds 5-10x. Erosion spiral: overconfidence → discovery → alert fatigue → binary choice → catastrophe.

Appears in: AR-001, AR-002, AR-004, AR-005, AR-008, AR-009." \
"- [[9a-trust-erosion-spiral]] — the spiral
- [[6b-trust-debt]] — debt compounds
- [[7b-calibration]] — the fix
- [[1c-llm-overconfidence]] — root cause
- [[2c-financial-losses]] — the cost
- [[0-Index]]"

zk_note "7b-calibration" "Calibration" \
"Aligning AI confidence with actual accuracy. 84% of LLMs are overconfident. VCE biased 20-30pp. Five methods: Temperature Scaling, Conformal Prediction, Sample Consistency (\$0.003), Budget-CoCoA (\$0.005), Selective Prediction.

ROI: 1:1,500,000. Appears in 7/9 reports.

Appears in: AR-001, AR-002, AR-004, AR-005, AR-009." \
"- [[9b-calibration-keystone]] — keystone intervention
- [[1c-llm-overconfidence]] — the problem
- [[5e-vce-bias]] — specific bias pattern
- [[7a-trust]] — trust restoration
- [[10b-calibration-focus]] — our strategy
- [[0-Index]]"

zk_note "7c-hitl" "Human-in-the-Loop (HITL)" \
"Regulatory requirement (EU AI Act Article 14) and operational necessity. The HITL paradox: regulation requires it but evidence shows it fails. 67% SOC alerts ignored. 80-99% healthcare false positives.

Improving calibration directly improves HITL by reducing noise.

Appears in: AR-002, AR-003, AR-006, AR-009." \
"- [[3a-alert-fatigue]] — the failure evidence
- [[9c-regulation-reality-gap]] — regulation vs reality
- [[7b-calibration]] — calibration fixes HITL
- [[8a-regulation]] — regulatory mandate
- [[0-Index]]"

zk_note "7d-memory" "Memory Architecture" \
"Critical attack surface. No production framework implements provenance tracking, integrity checks, or confidence scoring. MINJA >95% success. Memory poisoning + no detection + propagation + human failure = self-reinforcing attack loop.

Appears in: AR-001, AR-006." \
"- [[4c-memory-injection]] — attack details
- [[8d-security]] — security context
- [[9a-trust-erosion-spiral]] — feeds the spiral
- [[7b-calibration]] — could detect anomalies
- [[0-Index]]"

zk_note "7e-compounding" "Compounding" \
"Knowledge generates increasing returns when properly structured. Negative compounding: Trust Debt at 5-10x, overconfidence amplification. Positive compounding: calibration ROI at 1:1,500,000, regulatory compliance building defensibility.

Architecture determines whether compounding is positive or negative.

Appears in: AR-001, AR-002, AR-007, AR-009." \
"- [[6b-trust-debt]] — negative compounding
- [[9d-cost-asymmetry]] — positive ROI compounding
- [[6a-multi-agent-amplification]] — error compounding
- [[7b-calibration]] — positive intervention
- [[0-Index]]"

zk_note "8a-regulation" "Regulation" \
"EU AI Act: Aug 2026, €35M penalties. US: zero federal framework, 40+ state bills. Regulatory trilemma: fast OR compliant OR insured. Agent-shaped hole in both jurisdictions. EU extraterritorial reach.

Appears in: AR-001, AR-003, AR-005, AR-008." \
"- [[2a-eu-penalties]] — EU penalties
- [[3b-compliance-cost]] — compliance cost
- [[3c-agent-regulatory-hole]] — agent gap
- [[6d-iso-42001]] — bridge standard
- [[9c-regulation-reality-gap]] — regulation vs reality
- [[0-Index]]"

zk_note "8b-multi-agent-systems" "Multi-Agent Systems" \
"Multiple agents collaborating. Cost 10-30x (super-linear). Nine failure modes. Hijacking 45-64%. False consensus from verification. Anthropic: simple patterns outperform complex frameworks for most cases.

Appears in: AR-001, AR-006, AR-007, AR-009." \
"- [[5a-multi-agent-cost]] — cost scaling
- [[4d-multi-agent-hijacking]] — security risk
- [[6a-multi-agent-amplification]] — calibration risk
- [[9e-multi-agent-paradox]] — the paradox
- [[10d-anti-complexity]] — our stance
- [[0-Index]]"

zk_note "8c-governance" "Governance" \
"Board-level AI oversight inadequate. 22% CEO satisfaction. Avg director age 59.1. Caremark extending to AI. Seven essential board questions. Fragile governance = 40% missed productivity gains.

Appears in: AR-002, AR-004, AR-008." \
"- [[5c-board-competence]] — the gap
- [[5d-caremark-extension]] — legal liability
- [[10e-board-governance]] — our product
- [[8a-regulation]] — regulatory context
- [[0-Index]]"

zk_note "8d-security" "Security" \
"Agent attack surface 7x chatbots across 7 vectors. Prompt injection unsolvable (same modality). Defense: architectural constraints, not prompt engineering. Supply chain: MCP = npm without review.

Appears in: AR-001, AR-005, AR-006, AR-007." \
"- [[4b-prompt-injection]] — injection attacks
- [[4c-memory-injection]] — memory attacks
- [[4d-multi-agent-hijacking]] — MAS attacks
- [[4e-agent-attack-surface]] — full surface
- [[7d-memory]] — memory as vector
- [[0-Index]]"

zk_note "8e-maturity" "Maturity" \
"AGENT framework: 5 dimensions × 5 levels. Level 3 (Calibrated) = survival threshold for Aug 2026. 80%+ at Level 1. Existing models have agent-shaped blind spots.

Level 1→3: Inventory (1-3 months) + Calibration (\$0.005/check, 3-9 months).

Appears in: AR-004, AR-001, AR-002." \
"- [[3d-maturity-gap]] — the gap
- [[7b-calibration]] — Level 3 requires it
- [[8c-governance]] — governance dimension
- [[1d-ebit-impact]] — explains low impact
- [[0-Index]]"

# Insights
zk_note "9a-trust-erosion-spiral" "The Trust Erosion Spiral is Self-Reinforcing" \
"Cross-cutting: overconfidence → alert fatigue → HITL failure → catastrophe. Memory poisoning (>95%) feeds corrupted data. Overconfident calibration (84%) doesn't flag it. Alert fatigue (67% ignored) means humans miss it. The spiral accelerates.

This is the strongest cross-cutting finding: security, calibration, and human factors form a doom loop.

Sources: AR-001, AR-002, AR-006, AR-009." \
"- [[7a-trust]] — trust concept
- [[1c-llm-overconfidence]] — overconfidence
- [[3a-alert-fatigue]] — alert fatigue
- [[4c-memory-injection]] — memory poisoning
- [[7c-hitl]] — HITL failure
- [[0-Index]]"

zk_note "9b-calibration-keystone" "Calibration is the Keystone Intervention" \
"At \$0.005/check with ROI 1:1,500,000, calibration appears in 7/9 reports. Addresses overconfidence, alert fatigue, security anomalies, governance metrics, compliance, financial trust scoring, maturity threshold.

No other single intervention touches this many problem domains.

Sources: AR-001-009." \
"- [[7b-calibration]] — concept
- [[1e-calibration-cost]] — cost data
- [[9d-cost-asymmetry]] — ROI
- [[10b-calibration-focus]] — our decision
- [[0-Index]]"

zk_note "9c-regulation-reality-gap" "Regulation Demands What Technology Can't Deliver" \
"EU AI Act mandates effective human oversight (Article 14). But: 67% alerts ignored, HITL empirically broken, prompt injection unsolvable, multi-agent liability undefined.

Creates compliance theater risk: technically compliant but practically unprotected.

Sources: AR-002, AR-003, AR-006, AR-009." \
"- [[7c-hitl]] — HITL failure
- [[8a-regulation]] — regulatory mandate
- [[3a-alert-fatigue]] — empirical evidence
- [[4b-prompt-injection]] — unsolvable
- [[0-Index]]"

zk_note "9d-cost-asymmetry" "Extreme Cost Asymmetry" \
"Prevention-to-failure ratios: Calibration \$0.005 vs \$4.4M (1:880,000). Compliance \$2-5M vs €35M (1:7-17). Trust infra \$135/mo vs \$7.5B VW (1:1,500,000+). Proactive vs retroactive: 1x vs 5-10x.

Strongest economic argument for trust infrastructure.

Sources: AR-002, AR-003, AR-009." \
"- [[1e-calibration-cost]] — calibration cost
- [[2c-financial-losses]] — failure cost
- [[6b-trust-debt]] — debt multiplier
- [[7e-compounding]] — ROI compounds
- [[0-Index]]"

zk_note "9e-multi-agent-paradox" "Multi-Agent Systems Amplify Both Value and Risk" \
"MAS promise orchestrated intelligence but: cost 10-30x, hijacking 45-64%, false consensus, 40% cancellation. Anthropic: simple patterns outperform complex frameworks.

Paradox: industry builds toward multi-agent, evidence favors single-agent + simple orchestration.

Sources: AR-006, AR-007, AR-009." \
"- [[8b-multi-agent-systems]] — concept
- [[5a-multi-agent-cost]] — cost
- [[4d-multi-agent-hijacking]] — security
- [[6a-multi-agent-amplification]] — calibration
- [[10d-anti-complexity]] — our stance
- [[0-Index]]"

# Decisions
zk_note "10a-report-template" "Report Template Design Decision" \
"**Decision:** Standardize all reports with: Executive Summary, Key Insights (5), Sales Angles (3), Content Ideas (3), Links.

**Rationale:** Consistent structure enables cross-report analysis. Implemented AR-001 through AR-009.

**Date:** 2026-02-14 | **Status:** Implemented" \
"- [[9b-calibration-keystone]] — analysis enabled by structure
- [[10b-calibration-focus]] — related decision
- [[0-Index]]"

zk_note "10b-calibration-focus" "Calibration as Core Product Thesis" \
"**Decision:** Position calibration as primary value proposition.

**Rationale:** Touches 7/9 reports, clearest ROI (\$0.005 vs \$4.4M), keystone intervention. Narrower = stronger differentiation.

**Date:** 2026-02-14 | **Status:** Active" \
"- [[7b-calibration]] — concept
- [[9b-calibration-keystone]] — evidence
- [[1e-calibration-cost]] — cost data
- [[0-Index]]"

zk_note "10c-eu-first" "Build EU Compliance as Floor" \
"**Decision:** Design for EU AI Act first, adapt for US.

**Rationale:** EU stricter + extraterritorial reach. EU floor automatically satisfies most US state requirements.

**Date:** 2026-02-14 | **Status:** Active" \
"- [[8a-regulation]] — regulatory landscape
- [[2a-eu-penalties]] — penalties
- [[6d-iso-42001]] — bridge standard
- [[0-Index]]"

zk_note "10d-anti-complexity" "Anti-Complexity Stance on Multi-Agent" \
"**Decision:** Recommend single-agent + simple orchestration over complex multi-agent frameworks.

**Rationale:** Anthropic's finding that simple patterns outperform + 10-30x cost + 40% cancellation rate.

**Date:** 2026-02-14 | **Status:** Active" \
"- [[8b-multi-agent-systems]] — concept
- [[9e-multi-agent-paradox]] — evidence
- [[5a-multi-agent-cost]] — cost data
- [[0-Index]]"

zk_note "10e-board-governance" "Board Governance Training as Revenue Stream" \
"**Decision:** Develop Board AI Readiness product combining AR-008 governance + AR-004 maturity assessment.

**Rationale:** 22% satisfaction + Caremark liability + Aug 2026 deadline = urgent buyer need. High-ticket, low-cost.

**Date:** 2026-02-14 | **Status:** Planned" \
"- [[8c-governance]] — concept
- [[5c-board-competence]] — the gap
- [[8e-maturity]] — maturity assessment
- [[0-Index]]"

echo "Vault C (ZETTELKASTEN) complete: $(find "$VC" -name '*.md' | wc -l) notes"

###############################################################################
# VAULT D: MOC-HYBRID - Numbered folders + MOC index files
###############################################################################

# Copy content to appropriate folders
for f in "$VA"/C-*.md; do
  bn=$(basename "$f")
  # Add moderate linking
  cp "$f" "$VD/20-Claims/$bn"
  echo -e "\n## See Also\n- [[10-MOCs/MOC-Claims]]\n- [[10-MOCs/MOC-Reports]]" >> "$VD/20-Claims/$bn"
done

for f in "$VA"/K-*.md; do
  bn=$(basename "$f")
  cp "$f" "$VD/30-Concepts/$bn"
  echo -e "\n## See Also\n- [[10-MOCs/MOC-Concepts]]\n- [[10-MOCs/MOC-Reports]]" >> "$VD/30-Concepts/$bn"
done

for f in "$VA"/I-*.md; do
  bn=$(basename "$f")
  cp "$f" "$VD/40-Insights/$bn"
  echo -e "\n## See Also\n- [[10-MOCs/MOC-Insights]]\n- [[10-MOCs/MOC-Reports]]" >> "$VD/40-Insights/$bn"
done

for f in "$VA"/D-*.md; do
  bn=$(basename "$f")
  cp "$f" "$VD/50-Decisions/$bn"
  echo -e "\n## See Also\n- [[10-MOCs/MOC-Decisions]]" >> "$VD/50-Decisions/$bn"
done

# Create MOC files
cat > "$VD/10-MOCs/MOC-Claims.md" << 'EOF'
# MOC: Claims

Map of all atomic claims extracted from Ainary Research Reports.

## By Report
### AR-001: State of Agent Trust
- [[20-Claims/C-001 Agent Market Growth]]
- [[20-Claims/C-002 Corporate AI Failure Rate]]
- [[20-Claims/C-003 LLM Overconfidence]]
- [[20-Claims/C-004 EBIT Impact]]
- [[20-Claims/C-005 Calibration Cost]]
- [[20-Claims/C-007 Trust Erosion]]

### AR-002: Trust Tax
- [[20-Claims/C-008 Financial Losses]]
- [[20-Claims/C-009 Workslop Rework]]
- [[20-Claims/C-010 Shadow AI Breach]]
- [[20-Claims/C-011 Alert Fatigue]]
- [[20-Claims/C-027 Trust Debt]]
- [[20-Claims/C-028 Klarna Rollback]]

### AR-003: EU-US Regulation
- [[20-Claims/C-006 EU AI Act Penalties]]
- [[20-Claims/C-012 Compliance Cost]]
- [[20-Claims/C-013 Agent Shaped Hole]]
- [[20-Claims/C-029 ISO 42001]]

### AR-004: Maturity Model
- [[20-Claims/C-014 Maturity Gap]]

### AR-005: Financial Services
- [[20-Claims/C-015 Banking AI Potential]]
- [[20-Claims/C-016 JPMorgan AI]]
- [[20-Claims/C-030 Banking Compliance Cost]]

### AR-006: Security Playbook
- [[20-Claims/C-017 Prompt Injection]]
- [[20-Claims/C-018 Memory Injection]]
- [[20-Claims/C-019 Multi-Agent Hijacking]]
- [[20-Claims/C-020 Agent Attack Surface]]

### AR-007: Orchestration
- [[20-Claims/C-021 Multi-Agent Cost]]
- [[20-Claims/C-022 Agentic Project Cancellation]]

### AR-008: Governance
- [[20-Claims/C-023 Board AI Competence]]
- [[20-Claims/C-024 Caremark Extension]]

### AR-009: Calibration
- [[20-Claims/C-025 VCE Bias]]
- [[20-Claims/C-026 Multi-Agent Amplification]]

## See Also
- [[MOC-Concepts]]
- [[MOC-Insights]]
- [[MOC-Decisions]]
- [[MOC-Reports]]
EOF

cat > "$VD/10-MOCs/MOC-Concepts.md" << 'EOF'
# MOC: Concepts

## Core Concepts
- [[30-Concepts/K-001 Trust]] — Central theme, three-layer gap
- [[30-Concepts/K-002 Calibration]] — Keystone intervention, $0.005/check
- [[30-Concepts/K-003 HITL]] — Human oversight paradox
- [[30-Concepts/K-004 Memory]] — Attack surface, no provenance
- [[30-Concepts/K-005 Compounding]] — Positive and negative
- [[30-Concepts/K-006 Regulation]] — EU vs US divide
- [[30-Concepts/K-007 Multi-Agent Systems]] — Cost and risk amplification
- [[30-Concepts/K-008 Governance]] — Board-level oversight gap
- [[30-Concepts/K-009 Security]] — 7x attack surface
- [[30-Concepts/K-010 Maturity]] — AGENT framework, Level 3 threshold

## See Also
- [[MOC-Claims]]
- [[MOC-Insights]]
- [[MOC-Reports]]
EOF

cat > "$VD/10-MOCs/MOC-Insights.md" << 'EOF'
# MOC: Cross-Cutting Insights

- [[40-Insights/I-001 Trust Erosion Spiral]] — Self-reinforcing doom loop
- [[40-Insights/I-002 Calibration as Keystone]] — Touches 7/9 reports
- [[40-Insights/I-003 Regulation-Reality Gap]] — Compliance theater risk
- [[40-Insights/I-004 Cost Asymmetry]] — 1:1,500,000 prevention ratio
- [[40-Insights/I-005 Multi-Agent Paradox]] — Simple beats complex

## See Also
- [[MOC-Concepts]]
- [[MOC-Claims]]
- [[MOC-Reports]]
EOF

cat > "$VD/10-MOCs/MOC-Decisions.md" << 'EOF'
# MOC: Decisions

- [[50-Decisions/D-001 Report Template]] — Standardized structure (Implemented)
- [[50-Decisions/D-002 Calibration Focus]] — Core product thesis (Active)
- [[50-Decisions/D-003 EU-First Compliance]] — Build EU as floor (Active)
- [[50-Decisions/D-004 Anti-Complexity]] — Single-agent + simple orchestration (Active)
- [[50-Decisions/D-005 Board Governance Product]] — Revenue stream (Planned)

## See Also
- [[MOC-Insights]]
- [[MOC-Reports]]
EOF

cat > "$VD/10-MOCs/MOC-Reports.md" << 'EOF'
# MOC: Ainary Research Reports

## Reports
- **AR-001** State of Agent Trust — Market overview, trust gap
- **AR-002** Trust Tax — Hidden costs of untrusted AI
- **AR-003** EU-US Regulation — Transatlantic divide
- **AR-004** Maturity Model — AGENT framework
- **AR-005** Financial Services — Banking playbook
- **AR-006** Security Playbook — Attack surfaces
- **AR-007** Orchestration — Multi-agent coordination
- **AR-008** Governance — Board oversight
- **AR-009** Calibration — Confidence alignment

## Navigation
- [[MOC-Claims]] — 30 atomic claims
- [[MOC-Concepts]] — 10 key concepts
- [[MOC-Insights]] — 5 cross-cutting insights
- [[MOC-Decisions]] — 5 strategic decisions
EOF

echo "Vault D (MOC-HYBRID) complete: $(find "$VD" -name '*.md' | wc -l) notes"

###############################################################################
# VAULT E: GRAPH-FIRST - Rich frontmatter, 5+ links, dataview queries
###############################################################################

# Function for graph-first notes with rich metadata
gf_note() {
  local filename="$1" title="$2" type="$3" content="$4" links="$5" confidence="$6" sources="$7"
  cat > "$VE/$filename.md" << EOF
---
type: $type
status: active
confidence: $confidence
source: [$sources]
created: 2026-02-14
modified: 2026-02-15
tags: [${type}]
aliases: []
---
# $title

$content

## Links
$links

## Backlinks
<!-- Dataview: list where contains(file.outlinks, this.file.link) -->
EOF
}

# Claims (30)
gf_note "C-001" "Agent Market Growth" "claim" \
"AI agent market: \$7.8B → \$52B by 2030 (45.8% CAGR). Source: AR-001." \
"- [[C-002]] — yet 95% fail
- [[C-004]] — only 6% EBIT impact
- [[K-001]] — trust gap explains disparity
- [[K-005]] — market growth = compounding opportunity
- [[I-004]] — cost asymmetry in the market" "high" "AR-001"

gf_note "C-002" "Corporate AI Failure Rate" "claim" \
"95% of corporate AI projects fail. Source: AR-001." \
"- [[C-001]] — despite market growth
- [[C-014]] — maturity gap detail
- [[K-010]] — maturity explains failures
- [[K-001]] — trust gap root cause
- [[K-005]] — negative compounding" "high" "AR-001"

gf_note "C-003" "LLM Overconfidence" "claim" \
"84% of LLMs overconfident across 9 models, 351 scenarios. Source: AR-001, AR-009." \
"- [[C-025]] — VCE bias detail
- [[K-002]] — calibration concept
- [[C-011]] — drives alert fatigue
- [[I-001]] — feeds trust erosion spiral
- [[K-003]] — undermines HITL" "high" "AR-001, AR-009"

gf_note "C-004" "Enterprise AI EBIT Impact" "claim" \
"Only 6% achieve meaningful EBIT impact (McKinsey, n=1,993). Source: AR-001." \
"- [[C-001]] — market context
- [[C-014]] — experimentation gap
- [[K-010]] — maturity framework
- [[C-002]] — failure rate
- [[D-002]] — our calibration focus" "high" "AR-001"

gf_note "C-005" "Calibration Infrastructure Cost" "claim" \
"\$0.005/check vs \$4.4M losses. Source: AR-001, AR-009." \
"- [[K-002]] — calibration concept
- [[I-004]] — cost asymmetry pattern
- [[C-008]] — the \$4.4M figure
- [[D-002]] — our product thesis
- [[I-002]] — keystone intervention" "high" "AR-001, AR-009"

gf_note "C-006" "EU AI Act Penalties" "claim" \
"Aug 2026 enforcement, €35M or 7% global revenue. Source: AR-003." \
"- [[C-012]] — compliance cost
- [[K-006]] — regulation concept
- [[D-003]] — EU-first strategy
- [[C-029]] — ISO bridge
- [[I-003]] — regulation-reality gap" "high" "AR-003"

gf_note "C-007" "Worker Trust Erosion" "claim" \
"AI usage +13%, worker confidence -18% (n=14K). Source: AR-001." \
"- [[K-001]] — trust concept
- [[I-001]] — spiral pattern
- [[C-027]] — trust debt
- [[C-003]] — overconfidence cause
- [[K-005]] — negative compounding" "high" "AR-001"

gf_note "C-008" "Enterprise AI Financial Losses" "claim" \
"99% report losses, \$4.4M average (EY, n=975). Source: AR-002." \
"- [[C-005]] — vs \$0.005 fix
- [[I-004]] — cost asymmetry
- [[C-027]] — trust debt
- [[K-001]] — trust tax
- [[C-009]] — rework component" "high" "AR-002"

gf_note "C-009" "Workslop Rework Cost" "claim" \
"\$186/employee/month, \$9M/year at 10K employees. Source: AR-002." \
"- [[C-008]] — total loss context
- [[K-001]] — trust tax line item
- [[C-003]] — overconfidence drives rework
- [[K-002]] — calibration reduces it
- [[I-004]] — cost pattern" "medium-high" "AR-002"

gf_note "C-010" "Shadow AI Breach Premium" "claim" \
"\$670K above standard breach (\$4.63M total), 247 days to detect. Source: AR-002." \
"- [[K-009]] — security concept
- [[C-008]] — loss component
- [[K-001]] — trust tax item
- [[C-020]] — attack surface
- [[K-008]] — governance gap enables" "high" "AR-002"

gf_note "C-011" "Alert Fatigue" "claim" \
"67% SOC alerts ignored. 80-99% healthcare false positives. HITL = rubber stamp. Source: AR-002, AR-009." \
"- [[K-003]] — HITL concept
- [[C-003]] — overconfidence root cause
- [[I-001]] — spiral Phase 3
- [[I-003]] — regulation demands working HITL
- [[K-002]] — calibration as fix" "high" "AR-002, AR-009"

gf_note "C-012" "EU Compliance Cost" "claim" \
"\$2-5M initial setup, 5-20x higher than US. Source: AR-003." \
"- [[C-006]] — vs €35M penalty
- [[I-004]] — still cheaper than failure
- [[K-006]] — regulatory context
- [[D-003]] — our strategy
- [[C-029]] — ISO as bridge" "medium-high" "AR-003"

gf_note "C-013" "Agent Regulatory Hole" "claim" \
"Neither EU nor US defines AI agents. Multi-agent liability = black hole. Source: AR-003." \
"- [[K-006]] — regulation concept
- [[K-007]] — what's undefined
- [[I-003]] — regulation-reality gap
- [[C-019]] — hijacking in undefined space
- [[C-024]] — Caremark may fill gap" "high" "AR-003"

gf_note "C-014" "Maturity Gap" "claim" \
"62% experiment, <10% deploy, 6% EBIT impact. Source: AR-004." \
"- [[C-004]] — EBIT detail
- [[K-010]] — maturity framework
- [[C-002]] — failure rate
- [[K-001]] — trust explains gap
- [[D-002]] — our response" "high" "AR-004"

gf_note "C-015" "Banking AI Potential" "claim" \
"73% of banking time has AI impact (39% auto, 34% augment). Source: AR-005." \
"- [[C-030]] — compliance cost driver
- [[C-016]] — JPMorgan reality
- [[K-001]] — trust gap prevents full adoption
- [[C-028]] — Klarna cautionary tale
- [[K-009]] — security concerns" "high" "AR-005"

gf_note "C-016" "JPMorgan AI" "claim" \
"2,000+ use cases, \$150B+ daily fraud detection — mostly supervised, not autonomous. Source: AR-005." \
"- [[C-015]] — banking potential
- [[C-014]] — maturity gap in practice
- [[K-010]] — Level 1-2 despite scale
- [[K-007]] — not truly multi-agent
- [[K-001]] — trust gap limits autonomy" "high" "AR-005"

gf_note "C-017" "Prompt Injection Broken" "claim" \
"12/12 defenses broken by Meta/OpenAI/Anthropic/DeepMind. Source: AR-006." \
"- [[K-009]] — security concept
- [[C-020]] — attack surface vector
- [[K-002]] — calibration detects anomalies
- [[I-003]] — undermines regulatory assumptions
- [[C-018]] — combined with memory attacks" "high" "AR-006"

gf_note "C-018" "Memory Injection" "claim" \
"MINJA >95% success, persistent backdoors survive resets. Source: AR-006." \
"- [[K-004]] — memory concept
- [[I-001]] — feeds the spiral
- [[K-009]] — security gap
- [[C-017]] — related vector
- [[C-011]] — combined with alert fatigue" "high" "AR-006"

gf_note "C-019" "Multi-Agent Hijacking" "claim" \
"45-64% success across AutoGen/CrewAI/MetaGPT. Zero trust verification. Source: AR-006." \
"- [[K-007]] — MAS concept
- [[K-009]] — security vector
- [[C-026]] — also amplifies miscalibration
- [[I-005]] — multi-agent paradox
- [[C-013]] — in regulatory black hole" "high" "AR-006"

gf_note "C-020" "Agent Attack Surface" "claim" \
"7x larger than chatbots: 7 vectors. Source: AR-006." \
"- [[K-009]] — security concept
- [[C-017]] — prompt injection
- [[C-018]] — memory injection
- [[C-019]] — MAS hijacking
- [[K-010]] — maturity must address" "high" "AR-006"

gf_note "C-021" "Multi-Agent Cost" "claim" \
"5-agent pipeline costs 10-30x single agent. Source: AR-007." \
"- [[K-007]] — MAS concept
- [[I-005]] — the paradox
- [[C-022]] — drives cancellations
- [[D-004]] — our anti-complexity stance
- [[I-004]] — cost asymmetry" "medium-high" "AR-007"

gf_note "C-022" "Agentic Cancellation" "claim" \
">40% canceled by 2027. Quality is #1 barrier. Source: AR-007." \
"- [[C-021]] — cost driver
- [[K-007]] — MAS concept
- [[D-004]] — our recommendation
- [[K-002]] — calibration improves quality
- [[K-010]] — maturity gap" "medium" "AR-007"

gf_note "C-023" "Board Competence Gap" "claim" \
"22% of CEOs say board supports them on AI. Source: AR-008." \
"- [[K-008]] — governance concept
- [[C-024]] — creates liability
- [[D-005]] — our product
- [[K-010]] — maturity includes governance
- [[I-003]] — regulation-reality gap" "high" "AR-008"

gf_note "C-024" "Caremark Extension" "claim" \
"Directors face personal liability for failing to monitor AI risk. Source: AR-008." \
"- [[K-008]] — governance concept
- [[C-023]] — boards aren't ready
- [[C-006]] — regulatory pressure
- [[D-005]] — our product
- [[I-003]] — regulation vs reality" "medium-high" "AR-008"

gf_note "C-025" "VCE Bias" "claim" \
"Biased upward 20-30pp, r ≈ 0.3-0.5 with correctness. Source: AR-009." \
"- [[C-003]] — overconfidence problem
- [[K-002]] — calibration fixes
- [[C-026]] — amplified in chains
- [[I-001]] — feeds spiral
- [[D-002]] — our product addresses" "high" "AR-009"

gf_note "C-026" "Multi-Agent Amplification" "claim" \
"Verification amplifies miscalibration. ~100% overconfidence in 3-agent chains. Source: AR-009." \
"- [[C-025]] — individual bias
- [[K-007]] — MAS concept
- [[I-005]] — the paradox
- [[K-002]] — calibration as fix
- [[D-004]] — anti-complexity" "high" "AR-009"

gf_note "C-027" "Trust Debt" "claim" \
"Retroactive trust infra costs 5-10x proactive. Source: AR-002." \
"- [[K-001]] — trust concept
- [[K-005]] — negative compounding
- [[C-008]] — the cost
- [[I-004]] — cost asymmetry
- [[D-002]] — our proactive approach" "medium-high" "AR-002"

gf_note "C-028" "Klarna Rollback" "claim" \
"\$60M claimed savings, 853 FTEs, partial rollback. Metrics masked quality degradation. Source: AR-002, AR-005." \
"- [[C-008]] — financial impact
- [[C-015]] — banking context
- [[C-003]] — overconfidence root
- [[K-008]] — governance failure
- [[K-002]] — calibration would have caught it" "high" "AR-002, AR-005"

gf_note "C-029" "ISO 42001" "claim" \
"Bridge between EU/US compliance. AWS first certified Jan 2026. Source: AR-003." \
"- [[K-006]] — regulatory context
- [[C-006]] — EU penalties
- [[D-003]] — our strategy
- [[C-012]] — compliance cost
- [[K-008]] — governance standard" "high" "AR-003"

gf_note "C-030" "Banking Compliance Cost" "claim" \
"\$270B annual + 55-65% cost ratios. AI adoption structurally inevitable. Source: AR-005." \
"- [[C-015]] — banking potential
- [[I-004]] — cost dynamics
- [[C-028]] — but not risk-free
- [[K-001]] — trust needed for adoption
- [[K-006]] — regulatory pressure" "high" "AR-005"

# Concepts (10)
gf_note "K-001" "Trust" "concept" \
"Central theme. Three-layer gap: Communication (solved), Identity (emerging), Trustworthiness (missing). Trust Tax = \$4.4M avg. Trust Debt compounds 5-10x. Erosion spiral: overconfidence → discovery → fatigue → binary choice → catastrophe.

Appears in: AR-001, AR-002, AR-004, AR-005, AR-008, AR-009." \
"- [[I-001]] — the spiral
- [[C-027]] — debt compounds
- [[K-002]] — the fix
- [[C-003]] — root cause
- [[C-008]] — the cost
- [[K-005]] — compounding dynamics" "high" "AR-001, AR-002, AR-004, AR-005, AR-008, AR-009"

gf_note "K-002" "Calibration" "concept" \
"Aligning AI confidence with accuracy. 84% overconfident. VCE biased 20-30pp. Five methods. ROI: 1:1,500,000. Appears in 7/9 reports.

Methods: Temperature Scaling, Conformal Prediction, Sample Consistency (\$0.003), Budget-CoCoA (\$0.005), Selective Prediction." \
"- [[I-002]] — keystone intervention
- [[C-003]] — the problem
- [[C-025]] — VCE bias
- [[K-001]] — trust restoration
- [[D-002]] — our strategy
- [[K-003]] — improves HITL" "high" "AR-001, AR-002, AR-004, AR-005, AR-009"

gf_note "K-003" "Human-in-the-Loop" "concept" \
"EU AI Act Article 14 mandate. HITL paradox: required but fails. 67% alerts ignored. 80-99% false positives. Calibration improves HITL by reducing noise." \
"- [[C-011]] — failure evidence
- [[I-003]] — regulation vs reality
- [[K-002]] — calibration fixes HITL
- [[K-006]] — regulatory mandate
- [[I-001]] — spiral Phase 3" "high" "AR-002, AR-003, AR-006, AR-009"

gf_note "K-004" "Memory Architecture" "concept" \
"Critical attack surface. No provenance tracking in any production framework. MINJA >95% success. Memory = persistent backdoor." \
"- [[C-018]] — attack details
- [[K-009]] — security context
- [[I-001]] — feeds spiral
- [[K-002]] — detect anomalies
- [[C-020]] — part of 7x surface" "high" "AR-001, AR-006"

gf_note "K-005" "Compounding" "concept" \
"Knowledge generates increasing returns when structured. Negative: Trust Debt 5-10x, overconfidence amplification. Positive: calibration ROI 1:1,500,000, compliance building defensibility." \
"- [[C-027]] — negative compounding
- [[I-004]] — positive ROI
- [[C-026]] — error compounding
- [[K-002]] — positive intervention
- [[K-001]] — trust dynamics" "high" "AR-001, AR-002, AR-007, AR-009"

gf_note "K-006" "Regulation" "concept" \
"EU: Aug 2026, €35M. US: zero federal, 40+ state bills. Trilemma: fast OR compliant OR insured. Agent-shaped hole. EU extraterritorial." \
"- [[C-006]] — EU penalties
- [[C-012]] — compliance cost
- [[C-013]] — agent gap
- [[C-029]] — ISO bridge
- [[I-003]] — regulation vs reality
- [[D-003]] — our strategy" "high" "AR-001, AR-003, AR-005, AR-008"

gf_note "K-007" "Multi-Agent Systems" "concept" \
"Cost 10-30x (super-linear). Nine failure modes. Hijacking 45-64%. False consensus. Anthropic: simple > complex." \
"- [[C-021]] — cost scaling
- [[C-019]] — security risk
- [[C-026]] — calibration risk
- [[I-005]] — the paradox
- [[D-004]] — our stance
- [[K-009]] — security dimension" "high" "AR-001, AR-006, AR-007, AR-009"

gf_note "K-008" "Governance" "concept" \
"Board oversight inadequate. 22% satisfaction. Avg director 59.1. Caremark extending to AI. Seven questions. 40% missed gains." \
"- [[C-023]] — the gap
- [[C-024]] — liability
- [[D-005]] — our product
- [[K-006]] — regulatory context
- [[K-010]] — maturity dimension" "high" "AR-002, AR-004, AR-008"

gf_note "K-009" "Security" "concept" \
"7x attack surface. Prompt injection unsolvable. Defense: architectural constraints. Supply chain: MCP = npm without review." \
"- [[C-017]] — injection attacks
- [[C-018]] — memory attacks
- [[C-019]] — MAS attacks
- [[C-020]] — full surface
- [[K-004]] — memory vector
- [[I-001]] — security in the spiral" "high" "AR-001, AR-005, AR-006, AR-007"

gf_note "K-010" "Maturity" "concept" \
"AGENT: 5 dimensions × 5 levels. Level 3 = survival threshold. 80%+ at Level 1. Existing models blind to agents. L1→L3: Inventory + Calibration." \
"- [[C-014]] — the gap
- [[K-002]] — L3 requires calibration
- [[K-008]] — governance dimension
- [[C-004]] — explains low impact
- [[D-005]] — assessment product" "high" "AR-004, AR-001, AR-002"

# Insights (5)
gf_note "I-001" "Trust Erosion Spiral is Self-Reinforcing" "insight" \
"Overconfidence → alert fatigue → HITL failure → catastrophe. Memory poisoning (>95%) + uncalibrated confidence (84%) + alert fatigue (67% ignored) = doom loop. Strongest cross-cutting finding." \
"- [[K-001]] — trust concept
- [[C-003]] — overconfidence
- [[C-011]] — alert fatigue
- [[C-018]] — memory poisoning
- [[K-003]] — HITL failure
- [[K-002]] — calibration breaks the loop" "high" "AR-001, AR-002, AR-006, AR-009"

gf_note "I-002" "Calibration is the Keystone Intervention" "insight" \
"\$0.005/check, ROI 1:1,500,000, appears in 7/9 reports. Addresses overconfidence, alert fatigue, security, governance, compliance, financial trust, maturity." \
"- [[K-002]] — concept
- [[C-005]] — cost data
- [[I-004]] — ROI pattern
- [[D-002]] — our decision
- [[I-001]] — breaks the spiral" "high" "AR-001-009"

gf_note "I-003" "Regulation Demands What Technology Can't Deliver" "insight" \
"EU mandates effective oversight (Art 14). 67% alerts ignored. HITL broken. Injection unsolvable. Creates compliance theater risk." \
"- [[K-003]] — HITL failure
- [[K-006]] — regulatory mandate
- [[C-011]] — evidence
- [[C-017]] — unsolvable
- [[K-008]] — governance gap" "high" "AR-002, AR-003, AR-006, AR-009"

gf_note "I-004" "Extreme Cost Asymmetry" "insight" \
"Prevention:failure ratios from 1:700 to 1:1,500,000. Calibration \$0.005 vs \$4.4M. Compliance \$2-5M vs €35M. Proactive 1x vs retroactive 5-10x." \
"- [[C-005]] — calibration cost
- [[C-008]] — failure cost
- [[C-027]] — debt multiplier
- [[K-005]] — compounding
- [[D-002]] — our thesis" "high" "AR-002, AR-003, AR-009"

gf_note "I-005" "Multi-Agent Paradox" "insight" \
"MAS promise but: 10-30x cost, 45-64% hijacking, false consensus, 40% cancellation. Simple patterns outperform complex frameworks." \
"- [[K-007]] — concept
- [[C-021]] — cost
- [[C-019]] — security
- [[C-026]] — calibration
- [[D-004]] — our stance" "high" "AR-006, AR-007, AR-009"

# Decisions (5)
gf_note "D-001" "Report Template Design" "decision" \
"**Decision:** Standardize with: Exec Summary, Key Insights (5), Sales Angles (3), Content Ideas (3), Links. Implemented AR-001-009." \
"- [[I-002]] — analysis enabled
- [[D-002]] — related decision
- [[K-002]] — calibration focus emerged from structure
- [[K-010]] — maturity reports standardized
- [[K-001]] — trust reports standardized" "high" "Internal"

gf_note "D-002" "Calibration as Core Product Thesis" "decision" \
"Position calibration as primary value prop. Touches 7/9 reports, clearest ROI, keystone intervention." \
"- [[K-002]] — concept
- [[I-002]] — evidence
- [[C-005]] — cost data
- [[I-004]] — ROI pattern
- [[D-001]] — template revealed pattern" "high" "Internal"

gf_note "D-003" "Build EU Compliance as Floor" "decision" \
"Design for EU AI Act first. EU stricter + extraterritorial. EU floor satisfies most US requirements." \
"- [[K-006]] — regulatory landscape
- [[C-006]] — penalties
- [[C-029]] — ISO bridge
- [[C-012]] — compliance cost
- [[I-003]] — regulation-reality gap" "high" "Internal"

gf_note "D-004" "Anti-Complexity Multi-Agent" "decision" \
"Recommend single-agent + simple orchestration. Anthropic's finding + 10-30x cost + 40% cancellation." \
"- [[K-007]] — concept
- [[I-005]] — evidence
- [[C-021]] — cost data
- [[C-022]] — cancellation rate
- [[K-002]] — calibration improves single agents" "high" "Internal"

gf_note "D-005" "Board Governance Training Revenue" "decision" \
"Board AI Readiness product: AR-008 governance + AR-004 maturity. 22% satisfaction + Caremark + Aug 2026 = urgent." \
"- [[K-008]] — governance concept
- [[C-023]] — the gap
- [[K-010]] — maturity assessment
- [[C-024]] — Caremark liability
- [[K-006]] — regulatory urgency" "high" "Internal"

# Dynamic MOC via Dataview
cat > "$VE/DYNAMIC-MOC.md" << 'EOF'
---
type: navigation
status: active
confidence: high
source: [system]
created: 2026-02-14
modified: 2026-02-15
tags: [moc, dynamic]
---
# Dynamic Map of Content

## All Claims
```dataview
TABLE confidence, source
FROM #claim
SORT file.name ASC
```

## All Concepts
```dataview
TABLE confidence, source
FROM #concept
SORT file.name ASC
```

## All Insights
```dataview
TABLE confidence, source
FROM #insight
SORT file.name ASC
```

## All Decisions
```dataview
TABLE confidence, status
FROM #decision
SORT file.name ASC
```

## Most Connected Notes
```dataview
TABLE length(file.outlinks) as "Outgoing Links", length(file.inlinks) as "Incoming Links"
SORT length(file.outlinks) + length(file.inlinks) DESC
LIMIT 10
```

## Connection Suggestions
Notes with fewer than 5 links that might benefit from more connections:
```dataview
TABLE length(file.outlinks) as "Links"
WHERE length(file.outlinks) < 5
SORT length(file.outlinks) ASC
```
EOF

echo "Vault E (GRAPH-FIRST) complete: $(find "$VE" -name '*.md' | wc -l) notes"

echo ""
echo "=== ALL VAULTS COMPLETE ==="
echo "Vault A (FLAT):        $(find "$VA" -name '*.md' | wc -l) notes"
echo "Vault B (PARA):        $(find "$VB" -name '*.md' | wc -l) notes"
echo "Vault C (ZETTELKASTEN): $(find "$VC" -name '*.md' | wc -l) notes"
echo "Vault D (MOC-HYBRID):  $(find "$VD" -name '*.md' | wc -l) notes"
echo "Vault E (GRAPH-FIRST): $(find "$VE" -name '*.md' | wc -l) notes"
