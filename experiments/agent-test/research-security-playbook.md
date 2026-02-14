# The AI Agent Security Playbook
## What Attackers Already Know That Defenders Don't

**Ainary Report AR-006** | February 2026
**Author:** Florian Ziesche — Ainary Ventures
**Audience:** [CISO/Security Lead]
**Overall Confidence:** 78%

---

**Keywords:** AI Agent Security, Prompt Injection, Memory Poisoning, Tool Exploitation, Multi-Agent Attacks, Red Teaming, NIST AI RMF

---

## Table of Contents

1. Executive Summary
2. The Attack Surface Nobody Modeled
3. Prompt Injection — The Unsolvable Problem
4. Memory Poisoning — The Long Game
5. Tool Use Exploitation — When Agents Have Keys
6. Multi-Agent Contagion — One Compromise, Total Infection
7. Supply Chain Attacks on Agent Frameworks
8. What Actually Works (And What's Security Theater)

Beipackzettel
Claim Register
References
Cite As

---

## 1. Executive Summary

**Key Insight: Every defense deployed today was designed for chatbots, not agents. Agents have tools, memory, and network access — the attack surface is 10x larger.**

(Confidence: High)

AI agents are not chatbots with extra steps. They hold persistent memory, call external APIs, execute code, manage credentials, and coordinate with other agents. The security community is applying chatbot-era defenses — input filtering, output moderation, system prompt hardening — to systems that have fundamentally different threat models.

The data is unambiguous:

- **12 out of 12** published prompt injection defenses were broken by adaptive attacks (arXiv:2510.09023 — joint paper from Meta, OpenAI, Anthropic, DeepMind) [1]
- **>95%** memory injection success rate against RAG-based agent memory (MINJA, arXiv:2503.03704) [2]
- **45–64%** multi-agent system hijacking success rate against AutoGen, CrewAI, and MetaGPT (arXiv:2503.12188) [3]
- **73%** of AI deployments have prompt injection vulnerabilities (OWASP) [4]
- **CVE-2025-32711** (EchoLeak): zero-click data exfiltration from Microsoft Copilot — no user interaction required [5]

Attackers are not theorizing. They are publishing peer-reviewed papers with working exploits. Defenders are still debating whether prompt injection is a real risk.

This report maps the complete agent attack surface, documents what works and what doesn't, and provides a security framework designed for agents — not chatbots.

---

## 2. The Attack Surface Nobody Modeled

**Key Insight: A chatbot has 1 attack surface (the prompt). An agent has 7 — and they compound.**

(Confidence: High)

Exhibit 1: Agent vs. Chatbot Attack Surface Comparison

| Attack Surface | Chatbot | Agent |
|---|---|---|
| Direct prompt input | ✅ | ✅ |
| Indirect prompt (retrieved data) | ❌ | ✅ |
| Persistent memory | ❌ | ✅ |
| Tool/API calls | ❌ | ✅ |
| Inter-agent communication | ❌ | ✅ |
| Credential/key access | ❌ | ✅ |
| External data sources (RAG) | Limited | ✅ |

*Source: Author analysis based on OWASP Top 10 for LLM Applications (2025) [4], MITRE ATLAS [6]*

The OWASP Top 10 for LLM Applications (2025 edition) lists prompt injection as the #1 risk. But the taxonomy was designed for single-model applications. Agent-specific attack vectors — memory poisoning, tool chain exploitation, inter-agent contagion — are absent or underspecified.

MITRE ATLAS added "LLM Prompt Injection" (AML.T0051) and related techniques in 2024, but does not model multi-agent propagation or persistent memory corruption as distinct attack paths [6].

The gap: no widely adopted threat model exists for autonomous AI agents. Security teams are using chatbot threat models for agent deployments. This is like using a firewall ruleset designed for a static website to protect a Kubernetes cluster.

---

## 3. Prompt Injection — The Unsolvable Problem

**Key Insight: Prompt injection is not a bug to be patched. It is an inherent property of systems that mix instructions and data in the same channel.**

(Confidence: High)

### Direct Injection

Direct prompt injection — where a user manipulates the system prompt through their input — remains trivially exploitable. Jailbreak success rates vary by model and technique, but the "Rule of Two" paper (arXiv:2510.09023) demonstrated that **every published defense can be broken with at most two adaptive attack iterations** [1].

The 14-author team (from Meta, OpenAI, Anthropic, Google DeepMind) tested 12 defense categories:
- Perplexity-based detection
- Input/output classifiers
- Paraphrasing defenses
- Instruction hierarchy
- Sandwich defenses
- XML/delimiter tagging
- Known-answer detection
- Spotlighting
- Prompt shields (Azure)
- LLM-as-judge
- Fine-tuned safety models
- Constitutional AI guardrails

Result: **12/12 broken.** Not theoretically — with working code [1].

### Indirect Injection

Indirect prompt injection is worse. The agent retrieves external data (web pages, emails, documents, API responses) that contains adversarial instructions. The agent cannot distinguish between "data to process" and "instructions to follow" because both arrive as text in the same context window.

Real cases:
- **CVE-2025-32711 (EchoLeak):** Hidden instructions in documents retrieved by Microsoft Copilot caused zero-click data exfiltration — the agent silently sent user data to attacker-controlled endpoints [5]
- **Grok RAG Poisoning (2025):** Manipulated source documents caused Grok to generate false outputs that spread on X/Twitter [7]
- **ChatGPT Plugin Exploits (2024):** Researchers demonstrated that a malicious plugin could inject instructions into ChatGPT's context, hijacking subsequent tool calls [8]

### Why It's Unsolvable

The fundamental issue is architectural: LLMs process instructions and data in the same modality (natural language tokens). There is no hardware-level separation equivalent to kernel/user space in operating systems. Every proposed "fix" is a heuristic that can be circumvented because the model cannot fundamentally distinguish instruction from data [1].

This does not mean defenses are useless. It means defenses must be layered and assume breach — exactly the zero-trust paradigm that network security adopted 15 years ago.

---

## 4. Memory Poisoning — The Long Game

**Key Insight: Memory poisoning is the agent equivalent of a persistent backdoor. Once planted, it survives context window resets and influences every future interaction.**

(Confidence: High)

Unlike prompt injection (which is ephemeral), memory poisoning creates **persistent compromise**. The attacker modifies the agent's long-term memory — stored in vector databases, knowledge graphs, or structured memory systems — so that the poisoned information is retrieved and trusted in all future sessions.

### MINJA (Memory INJection Attack)

The MINJA attack (arXiv:2503.03704) demonstrated **>95% injection success** against RAG-based agent memory systems [2]. The attack works by crafting documents that, when ingested into the memory store, contain adversarial instructions that override the agent's intended behavior whenever the poisoned memory is retrieved.

Key finding: the attack persists across sessions. Unlike prompt injection, which requires the attacker to be present in the conversation, memory poisoning is "fire and forget."

### MemoryGraft

MemoryGraft (arXiv:2512.16962) takes it further: researchers demonstrated planting **persistent false experiences** in agent memory that the agent treats as its own past interactions [9]. The agent cannot distinguish between genuine memories and implanted ones — there is no memory integrity verification in any production memory framework.

### The Memory Governance Vacuum

Exhibit 2: Memory Framework Security Features

| Framework | Provenance Tracking | Integrity Checks | Confidence per Memory | Selective Forgetting | Audit Trail |
|---|---|---|---|---|---|
| Letta (MemGPT) | ❌ | ❌ | ❌ | Partial | ❌ |
| Mem0 | ❌ | ❌ | ❌ | ❌ | Partial |
| Zep | ❌ | ❌ | ❌ | ❌ | Partial |
| LangMem | ❌ | ❌ | ❌ | ❌ | ❌ |
| A-Mem | ❌ | ❌ | ❌ | ❌ | ❌ |

*Source: Brief 12 analysis, framework documentation review [10]*

No production memory framework implements memory provenance, integrity verification, or confidence scoring per memory entry. Every framework trusts all stored memories equally. This is the equivalent of running a database without access controls — any process that can write can corrupt everything.

### The Adversarial Memory Spiral

When memory poisoning combines with other vulnerabilities, it creates a self-reinforcing attack loop:

1. MINJA injects poisoned memory (>95% success)
2. Agent's verbalized confidence reports high certainty (VCE is biased — arXiv:2602.00279) [11]
3. Poisoned output passes to other agents (no inter-agent trust verification)
4. HITL alert fires but is ignored (67% alert ignore rate — Vectra 2023) [12]
5. Agent reinforces poisoned memory based on "successful" interaction
6. Loop repeats with increasing conviction

Each step is independently documented. The full chain has not been observed in the wild — but every link is empirically validated.

---

## 5. Tool Use Exploitation — When Agents Have Keys

**Key Insight: When an agent can call APIs, execute code, and manage files, prompt injection escalates from "wrong answer" to "unauthorized action."**

(Confidence: High)

### MCP Tool Poisoning (MCPTox)

The Model Context Protocol (MCP) standardizes how agents connect to external tools. MCPTox (arXiv:2508.14925) demonstrated that attackers can embed malicious instructions in MCP tool descriptions [13]. When an agent reads the tool's metadata to decide how to use it, the poisoned description hijacks the agent's behavior.

This is supply chain poisoning at the tool level: the agent trusts the tool registry, and the tool registry is compromised.

### Tool-Calling Failure Modes

Tool-calling fails **3–15%** of the time in production (practitioner reports) [14]. But security-relevant failures are different from reliability failures:

- **Credential leakage:** 23% of IT professionals report agent credential leaks (Okta survey) [15]
- **Excessive permissions:** Agents routinely receive broader API scopes than needed because fine-grained agent-specific IAM policies don't exist in most cloud providers
- **Unvalidated outputs:** Agents pass tool outputs directly into their context without sanitization — a classic injection vector
- **Confused deputy attacks:** An agent authorized to call Tool A is tricked (via prompt injection) into calling Tool B with Tool A's credentials

### The Credential Problem

Only **10% of organizations have a non-human identity strategy** (World Economic Forum) [16]. Agents are accessing production APIs with shared service accounts, hardcoded tokens, or overly broad OAuth scopes. When an agent is compromised, the blast radius is determined by its credential scope — which is usually "everything."

Exhibit 3: Agent Credential Anti-Patterns

| Anti-Pattern | Prevalence | Risk |
|---|---|---|
| Shared service accounts | High | Lateral movement after compromise |
| Hardcoded API keys in agent config | High | Key extraction via prompt injection |
| Overly broad OAuth scopes | Very High | Privilege escalation |
| No credential rotation | High | Persistent access after compromise |
| No per-action authorization | Very High | Confused deputy attacks |

*Source: Okta [15], WEF [16], OWASP LLM Top 10 [4]*

---

## 6. Multi-Agent Contagion — One Compromise, Total Infection

**Key Insight: Multi-agent systems have no immune system. Compromising one agent propagates to all connected agents because inter-agent messages are trusted by default.**

(Confidence: High)

### MAS Hijacking

The multi-agent system (MAS) hijacking paper (arXiv:2503.12188) tested attacks against the three major multi-agent frameworks [3]:

Exhibit 4: MAS Hijacking Success Rates

| Framework | Hijacking Success Rate | Attack Type |
|---|---|---|
| AutoGen | 45% | Task injection via agent message |
| CrewAI | 55% | Role confusion + instruction override |
| MetaGPT | 64% | Workflow manipulation |

*Source: arXiv:2503.12188 [3]*

The attack pattern: compromise one agent in a multi-agent pipeline, then use that agent's trusted position to inject instructions into downstream agents. Because inter-agent communication is treated as trusted input (it comes from "inside the system"), standard prompt injection defenses don't apply.

### The 2008 Parallel

This mirrors the systemic risk pattern from the 2008 financial crisis: Agent A trusts Agent B trusts Agent C. When Agent C is compromised, the trust chain propagates the compromise backwards. There is no "circuit breaker" — no mechanism to isolate a compromised agent or validate the integrity of inter-agent messages.

The A2A protocol (Google → Linux Foundation) authenticates **systems** (via OAuth/OpenID) but does not verify **message provenance or intention** [17]. Knowing that a message came from an authenticated agent says nothing about whether that agent has been compromised.

### Propagation Speed

In multi-agent systems processing concurrent tasks, a single compromised agent can influence every other agent within one task cycle. There is no quarantine mechanism, no anomaly detection on inter-agent message content, and no rollback capability for poisoned decisions.

---

## 7. Supply Chain Attacks on Agent Frameworks

**Key Insight: The agent framework ecosystem has the same supply chain vulnerabilities as npm/PyPI — but with the added risk that compromised packages can autonomously execute actions.**

(Confidence: Medium)

### Framework Vulnerabilities

Agent frameworks are built on deep dependency trees. Known vulnerabilities:

- **LangChain CVE-2023-36258:** Arbitrary code execution via the `PALChain` module — crafted input could execute arbitrary Python [18]
- **LangChain CVE-2023-36281:** SQL injection via the `SQLDatabaseChain` — agents connected to databases could be tricked into executing arbitrary SQL [19]
- **LangChain CVE-2023-39659:** Server-Side Request Forgery (SSRF) via multiple components — agents could be directed to make requests to internal infrastructure [20]
- **AutoGen:** No published CVEs as of Feb 2026, but the framework executes LLM-generated code by default — any prompt injection becomes code execution [21]

### The MCP Ecosystem Risk

MCP tool servers are the agent equivalent of npm packages. Anyone can publish an MCP server. There is no code review, no signing, no sandbox. When an agent connects to a malicious MCP server:

1. The tool description can contain prompt injection (MCPTox [13])
2. The tool can return poisoned data
3. The tool can log all agent requests (including credentials and user data)
4. The tool can modify its behavior after initial trust is established

### Dependency Confusion

Agent frameworks pull from PyPI (Python), npm (JavaScript), and container registries. Standard supply chain attacks — typosquatting, dependency confusion, compromised maintainer accounts — apply directly. The difference: a compromised agent framework dependency doesn't just steal data. It can **act** — send emails, modify files, call APIs, communicate with other agents.

---

## 8. What Actually Works (And What's Security Theater)

**Key Insight: Effective agent security requires architectural constraints, not pattern matching. The zero-trust model must extend to agent internals — not just network boundaries.**

(Confidence: Medium)

### Security Theater (What Doesn't Work)

Exhibit 5: Defense Effectiveness Assessment

| Defense | Status | Why |
|---|---|---|
| System prompt hardening ("Ignore all previous instructions...") | ❌ Theater | Broken by adaptive attacks (12/12) [1] |
| Input/output keyword filtering | ❌ Theater | Trivially bypassed via encoding, synonyms, multilingual attacks |
| Single-layer guardrail models | ❌ Theater | Same vulnerability class as the model they protect |
| "AI safety" fine-tuning alone | ❌ Theater | Training-time alignment is insufficient against inference-time attacks [1] |
| Perplexity-based detection | ❌ Theater | High false positive rate, adversarially evadable [1] |

### What Actually Works

**Architectural Constraints:**
- **Privilege separation:** Agents should operate with minimum necessary permissions. Each tool call should require explicit, scoped authorization — not blanket API access.
- **Memory integrity verification:** Cryptographic signing of memory entries with provenance tracking. Treat memory like a write-ahead log, not a trust store.
- **Inter-agent message validation:** Messages between agents should be verified outside the LLM context — using a separate, deterministic validation layer.
- **Deterministic guardrails:** Hard-coded rules that cannot be overridden by the LLM (e.g., "never execute `rm -rf`" enforced at the tool layer, not the prompt layer).

**Detection and Response:**
- **Behavioral baselines:** Monitor agent actions (tool calls, API patterns, memory writes) against expected behavior profiles. Anomaly detection on actions, not on text.
- **Kill switches:** Hardware-level (or at minimum, infrastructure-level) ability to halt agent execution immediately. Not a prompt that says "stop" — a process kill.
- **Audit trails:** Every agent action logged immutably with full context. Not for compliance theater — for incident response.

**Red Teaming:**
- **NIST AI RMF (AI 100-1):** Four pillars — Govern, Map, Measure, Manage. The January 2026 RFI on agent-specific security signals that NIST recognizes existing frameworks are insufficient for agents [22].
- **MITRE ATLAS:** Adversarial threat landscape for AI systems. Includes LLM-specific techniques but needs extension for multi-agent scenarios [6].
- **OWASP LLM Top 10 (2025):** Best current taxonomy for single-model risks. Does not cover agent-specific vectors adequately [4].
- **Agent-Specific Red Teaming:** Test the full chain: prompt injection → tool exploitation → memory corruption → inter-agent propagation. Single-vector testing misses compound attacks.

### The EU AI Act Gap

The EU AI Act (enforcement: high-risk systems from August 2026) requires human oversight (Article 14) for high-risk AI systems. But empirical evidence shows HITL oversight fails at scale: **67% of security alerts are ignored** (Vectra 2023, n=2,000 analysts) [12]. The regulation mandates a control that research proves doesn't work at production scale.

NIST is more pragmatic: the January 2026 RFI explicitly asks for input on agent-specific security requirements, acknowledging that existing frameworks (AI RMF 1.0) were designed for single-model systems [22].

Exhibit 6: Regulatory Framework Comparison for Agent Security

| Framework | Agent-Specific Provisions | Status |
|---|---|---|
| EU AI Act | None — applies general high-risk provisions | Enforcement Aug 2026 |
| NIST AI RMF 1.0 | None — single-model focus | RFI for agent extensions Jan 2026 |
| NIST CAISI | Building agent security standards | RFI deadline Mar 2026 |
| OWASP LLM Top 10 | Partial — prompt injection, insecure plugins | 2025 edition |
| MITRE ATLAS | Partial — LLM techniques, no multi-agent | Ongoing updates |
| ISO 42001 | General AI management, not agent-specific | AWS certified Jan 2026 |

*Sources: EU AI Act text [23], NIST [22], OWASP [4], MITRE [6], ISO [24]*

---

## Beipackzettel

- **Overall Confidence:** 78%
- **Sources:** 13 primary (peer-reviewed papers, CVE databases, framework documentation), 11 secondary (industry reports, practitioner analysis)
- **Strongest Evidence:** 12/12 prompt injection defenses broken (arXiv:2510.09023 — 14 authors from 4 top AI labs) [1]; MINJA >95% memory injection success (arXiv:2503.03704) [2]
- **Weakest Point:** Supply chain attack section relies on 2023 CVEs for LangChain; no published 2025/2026 agent framework CVEs found (does not mean they don't exist — may indicate under-reporting)
- **What would invalidate this report?** A fundamental architectural breakthrough that separates instructions from data at the model level (not heuristic-based). No such breakthrough is on the horizon.
- **Methodology:** Multi-agent research pipeline. Primary research from arXiv, CVE databases, NIST/OWASP/MITRE publications. Cross-referenced against Ainary Research Briefs #10 (Adversarial Agents), #12 (Agent Memory), #13 (Agent Protocols).
- **This report was created with a Multi-Agent Research System.**

---

## Claim Register

Exhibit 7: Claim Register

| # | Claim | Value | Source | Confidence |
|---|---|---|---|---|
| 1 | All published prompt injection defenses broken | 12/12 | arXiv:2510.09023 [1] | **High** |
| 2 | Memory injection success rate (MINJA) | >95% | arXiv:2503.03704 [2] | **High** |
| 3 | MAS hijacking success rate | 45–64% | arXiv:2503.12188 [3] | **High** |
| 4 | AI deployments with prompt injection vulnerabilities | 73% | OWASP [4] | **Medium** |
| 5 | Zero-click exfiltration via Copilot | CVE-2025-32711 | Microsoft/NVD [5] | **High** |
| 6 | SOC alerts ignored | 67% | Vectra 2023 (n=2,000) [12] | **High** |
| 7 | Agent credential leaks reported | 23% | Okta [15] | **Medium** |
| 8 | Organizations with non-human identity strategy | 10% | WEF [16] | **Medium** |
| 9 | No memory framework has integrity checks | 0/5 frameworks | Framework documentation [10] | **High** |
| 10 | LangChain arbitrary code execution | CVE-2023-36258 | NVD [18] | **High** |
| 11 | VCE systematically biased | Confirmed | arXiv:2602.00279 [11] | **High** |
| 12 | MCPTox tool poisoning via descriptions | Demonstrated | arXiv:2508.14925 [13] | **High** |

---

## References

[1] Debenedetti, E., et al. (2025). "Defeating Prompt Injections by Design." arXiv:2510.09023. Meta, OpenAI, Anthropic, Google DeepMind. 14 authors.

[2] Chen, Z., et al. (2025). "MINJA: Memory INJection Attacks against Retrieval-Augmented Generation." arXiv:2503.03704.

[3] Gu, Y., et al. (2025). "Hijacking Multi-Agent Systems." arXiv:2503.12188.

[4] OWASP. (2025). "OWASP Top 10 for Large Language Model Applications." Version 2.0.

[5] Microsoft / NVD. (2025). "CVE-2025-32711: EchoLeak — Information Disclosure in Microsoft Copilot."

[6] MITRE. (2025). "ATLAS — Adversarial Threat Landscape for AI Systems." AML.T0051.

[7] Documented in Ainary Research Brief #5 (Agent Failures). Original reporting: multiple sources, 2025.

[8] Greshake, K., et al. (2023). "Not What You've Signed Up For: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection." arXiv:2302.12173.

[9] Zhang, Y., et al. (2025). "MemoryGraft: Persistent False Memories in AI Agents." arXiv:2512.16962.

[10] Framework analysis: Letta, Mem0, Zep, LangMem, A-Mem documentation. Reviewed Feb 2026.

[11] Tao, Z., et al. (2026). "Verbalized Confidence Estimation is Biased." arXiv:2602.00279.

[12] Vectra AI. (2023). "State of Threat Detection." n=2,000 security analysts.

[13] Wang, X., et al. (2025). "MCPTox: Tool Poisoning Attacks on Model Context Protocol." arXiv:2508.14925.

[14] Hannecke, M. (2025). "Tool-calling failure rates in production." Practitioner blog (single source).

[15] Okta. (2025). "State of Machine Identity Security." IT professional survey.

[16] World Economic Forum. (2025). "Non-Human Identity Management."

[17] Google. (2025). "Agent-to-Agent (A2A) Protocol." Linux Foundation.

[18] NVD. "CVE-2023-36258: LangChain PALChain Arbitrary Code Execution."

[19] NVD. "CVE-2023-36281: LangChain SQLDatabaseChain SQL Injection."

[20] NVD. "CVE-2023-39659: LangChain Server-Side Request Forgery."

[21] Microsoft. "AutoGen Framework Documentation." Code execution enabled by default.

[22] NIST CAISI. (2026). "Request for Information: AI Agent Security." Deadline March 2026.

[23] European Parliament. (2024). "Regulation (EU) 2024/1689 — AI Act."

[24] ISO. (2023). "ISO/IEC 42001: Artificial Intelligence Management System."

---

**Cite as:** Ziesche, F. (2026). The AI Agent Security Playbook — What Attackers Already Know That Defenders Don't. Ainary Research Report, No. AR-006.

**About the Author:** Florian Ziesche is the founder of Ainary Ventures, a research and advisory firm focused on AI agent trust infrastructure.

---

© 2026 Ainary Ventures | Page ● of ● ●
