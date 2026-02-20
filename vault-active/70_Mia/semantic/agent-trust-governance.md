# Agent Trust Governance — Domain Knowledge
*Auto-consolidated: 2026-02-20 22:02 | 19 findings | avg conf: 74% | 6 verified*

## Verified Claims (conf ≥80%)

**RF-001** [90%]: Pre-Flight mit Regex fängt 80% der Output-Fehler bei 0 Kosten und <50ms
Source: Execution Platform Pre-Flight Engine Tests, 2026-02-18
Tags: ai_quality, pre_flight, regex

**RF-048** [90%]: Full autonomous software engineering still not here — agents need human-in-the-loop for complex decisions
Source: Cross-referenced from multiple production reports (Notion, Box, Lovable, Cognizant), Feb 2026
Tags: agent_trust, human_in_loop

**C002** [85% ✓]: 84% of LLM outputs are overconfident (verbalized confidence exceeds actual accuracy)
Source: PMC/12249208 (9 models, 351 scenarios)
Tags: ai_trust

**C001** [85% ✓]: 67% of security alerts are ignored by SOC analysts
Source: Vectra 2023 (n=2,000 SOC professionals)
Tags: ai_trust

**C004** [85% ✓]: 6% of companies achieve 'AI High Performer' status with 2-3x productivity gains
Source: McKinsey State of AI 2025 (n=1,993 companies)
Tags: ai_trust

**C005** [85% ✓]: MemoryGraft attack achieves >95% memory injection success rate
Source: MINJA research (2024)
Tags: ai_trust

**C013** [85% ✓]: Air Canada held legally liable for chatbot hallucination
Source: Court ruling 2024
Tags: ai_trust

**C014** [85%]: Grok RAG poisoning contaminated thousands of responses before detection
Source: Security disclosure 2024
Tags: ai_trust

**C015** [85%]: Waymo required 7 collisions before issuing recall
Source: NHTSA reporting + media
Tags: ai_trust

**RF-045** [85%]: 86% of Enterprise Copilot spending ($7.2B) goes into agent-based systems, not chat interfaces
Source: Iterathon.tech / Enterprise AI Spending Analysis, Dec 2025/Jan 2026
Tags: market_data, enterprise_ai, agents

## Emergent Patterns

**claim × ai_trust** (15 findings): 84% of LLM outputs are overconfident (verbalized confidence ; 67% of security alerts are ignored by SOC analysts; 6% of companies achieve 'AI High Performer' status with 2-3x

**claim × obsidian_import** (15 findings): 84% of LLM outputs are overconfident (verbalized confidence ; 67% of security alerts are ignored by SOC analysts; 6% of companies achieve 'AI High Performer' status with 2-3x

**ai_trust × obsidian_import** (15 findings): 84% of LLM outputs are overconfident (verbalized confidence ; 67% of security alerts are ignored by SOC analysts; 6% of companies achieve 'AI High Performer' status with 2-3x

## Developing (50-80% confidence)

- RF-002 [73%]: Bayesian Trust Scoring konvergiert schneller als lineares +2/-3 bei kleinen Stic
- C009 [60%]: VW Cariad $7.5B loss attributed to AI orchestration complexity
- C003 [60%]: Tool calling fails 3-15% of the time in production agent systems
- C006 [60%]: 80-99% false positive rate in healthcare alert systems
- C007 [60%]: Each reminder reduces response rate by 30% (alert fatigue)
- C008 [60%]: Klarna saved $60M with AI agents but reversed deployment due to trust failures
- C010 [60%]: 96% of security breaches are disclosed by the attacker, not internal detection
- C011 [60%]: LangChain grew from 0 to 100k GitHub stars in approximately 1 year
- C012 [60%]: Vercel achieved $200M ARR via DX-first design philosophy
