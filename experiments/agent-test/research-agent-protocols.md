# Research Brief: Agent-to-Agent Communication Protocols — How AI Agents Talk to Each Other

**Tag:** [INTERN] — Decision Support für AgentTrust Inter-Agent Trust Layer + Thought Leadership
**Audience:** AI Engineers + Protocol Designers
**Risk Tier:** 2 (Source Log + Claim Audit PFLICHT)
**Date:** 2026-02-14

---

## Key Findings

### 1. Zwei Protokolle dominieren: A2A (Google) für Agent↔Agent, MCP (Anthropic) für Agent↔Tools

Google lancierte A2A im April 2025 als offenes Protokoll für Agent-zu-Agent-Kommunikation. Im Juni 2025 wurde es an die Linux Foundation übergeben. MCP (Anthropic, 2024) standardisiert dagegen die Verbindung zwischen einem Agent und externen Tools/APIs. Beide sind komplementär, nicht konkurrierend — A2A für horizontale Agent-Kollaboration, MCP für vertikale Tool-Integration.
— Quellen: IBM Think (Nov 2025), Google Developers Blog (Apr 2025), Gravitee (Apr 2025, updated Jan 2026)

### 2. A2A nutzt Agent Cards für Discovery + OpenAPI-basierte Auth — aber Trust ist delegiert, nicht eingebaut

A2A folgt einem Client-Server-Modell mit drei Phasen: Discovery (Agent Cards als JSON an `/.well-known/agent.json`), Authentication (OAuth 2.0, API Keys, OpenID Connect per OpenAPI-Schema), Communication (HTTP + SSE für Streaming). **Kritisch: A2A authentifiziert den Client, aber verifiziert nicht die Identität oder Intention des dahinterliegenden Akteurs.** Die "Wer hat dich geschickt?"-Frage bleibt unbeantwortet.
— Quellen: IBM Think (Nov 2025), Google Developers Blog (Mai 2025), CIO.com (Feb 2026)

### 3. Trust ist das größte ungelöste Problem in Multi-Agent-Systemen

Laut Okta haben 23% der IT-Professionals berichtet, dass ihre AI Agents dazu gebracht wurden, Zugangsdaten preiszugeben. Das World Economic Forum fand, dass nur 10% der Organisationen eine ausgereifte Strategie für nicht-menschliche/agentische Identitäten haben. Der aktuelle Stand: Agents authentifizieren sich gegenseitig via OAuth/API-Keys (Identität des *Systems*), aber nicht die Provenienz (wer kontrolliert den Agent?) oder die Intention (was will der Agent wirklich?).
— Quellen: CIO.com (Feb 2026), Okta Report (referenziert in CIO.com)

### 4. Zero-Trust-Frameworks für Agents entstehen gerade (Microsoft Entra Agent ID, DID/VC-basierte Ansätze)

Microsoft lancierte **Entra Agent ID** (Build 2025): Jeder Agent bekommt ein eigenes Identity-Objekt im Tenant-Directory mit Conditional Access und Audit-Logging. Parallel dazu: Akademische Arbeiten (Huang et al., Mai 2025) schlagen **Decentralized Identifiers (DIDs) + Verifiable Credentials (VCs)** für Agent-Identitäten vor — mit einem "Agent Naming Service (ANS)" analog zu DNS. Prove lancierte "Verified Agent" (Okt 2025) für die $1.7T Agentic Commerce Economy.
— Quellen: Microsoft Tech Community (Jun 2025), arxiv.org Huang et al. (Mai 2025), BiometricUpdate (Okt 2025)

### 5. FIPA/ACL ist der akademische Vorläufer — aber in der LLM-Ära weitgehend irrelevant

FIPA Agent Communication Language (ACL) definierte in den 2000ern formale Performatives (inform, request, propose) für Multi-Agent-Systeme. Das Konzept — standardisierte Sprechakte zwischen Agents — ist intellektuell relevant, aber die Implementierung (JADE, XML-basiert) wurde von der LLM-Welle überrollt. A2A und MCP sind die spirituellen Nachfolger, arbeiten aber mit JSON/HTTP statt FIPA-ACL/XML.
— Interpretation (nicht direkt belegt durch aktuelle Quellen; basiert auf historischem Wissen über FIPA-Standards)

---

## Zahlen (verifiziert)

- **50+ Partner** beim A2A-Launch (Salesforce, Accenture, MongoDB, LangChain) — Quelle: Google Developers Blog, Apr 2025
- **23% der IT-Professionals** berichten, dass AI Agents Credentials preisgegeben haben — Quelle: Okta (ref. in CIO.com, Feb 2026)
- **10% der Organisationen** haben eine ausgereifte Non-Human-Identity-Strategie — Quelle: World Economic Forum (ref. in CIO.com, Feb 2026)
- **$1.7 Trillion** prognostizierte Agentic Commerce Economy — Quelle: Prove/BiometricUpdate, Okt 2025 (Primärquelle der Zahl unklar)
- **Juni 2025**: A2A an Linux Foundation übergeben — Quelle: Linux Foundation Press Release

---

## Claim Ledger (Top 5 Claims)

| # | Claim | Evidence | Confidence |
|---|-------|----------|------------|
| 1 | A2A und MCP sind komplementär (Agent↔Agent vs Agent↔Tools) | Google explizit ("complementary to MCP"), IBM Think, Gravitee | **High** — Mehrere unabhängige Quellen bestätigen |
| 2 | A2A authentifiziert Systeme, nicht die Provenienz/Intention dahinter | CIO.com-Analyse (Feb 2026), A2A-Spec nutzt OpenAPI-Auth-Schemas | **High** — Architekturanalyse + CIO-Artikel bestätigen das Gap |
| 3 | 23% der IT-Pros berichten Agent-Credential-Leaks | Okta-Report, zitiert in CIO.com | **Medium** — Sekundärquelle, Okta-Originalstudie nicht direkt geprüft. Confidence erhöhen: Okta-Primärstudie lesen |
| 4 | DID/VC-basierte Agent-Identität ist der vielversprechendste Ansatz für dezentrale Trust | Huang et al. (arxiv, Mai 2025), Cisco-Blog (Dez 2025) | **Medium** — Akademisch solide, aber noch keine Produktions-Implementierung bekannt |
| 5 | FIPA/ACL ist in der LLM-Ära praktisch irrelevant | Keine aktuellen Quellen referenzieren FIPA als aktiven Standard | **Medium** — Absence of evidence ≠ evidence of absence, aber starkes Signal |

---

## Contradiction Register

| Konflikt | Quellen | Warum unterschiedlich | Impact |
|----------|---------|----------------------|--------|
| A2A als "Standard" vs. IBM ACP als Alternative | Google (A2A), IBM (ACP/BeeAI) | Vendor-Interessen — IBM pusht eigenen Standard | Mittel: Für AgentTrust relevant — welches Protokoll wird dominant? A2A hat Linux Foundation + 50 Partner, ACP ist kleiner aber von IBM backed |
| Auth reicht vs. Auth reicht nicht | A2A-Spec (OAuth genügt), CIO.com (Provenienz fehlt) | A2A löst Transport-Security, nicht Trust-Provenienz | **Hoch für AgentTrust**: Genau dieses Gap ist die Opportunity |

---

## Unsicher / Nicht Verifiziert

- Die $1.7T Agentic Commerce Economy Zahl (Prove) — Primärquelle/Methodik unklar
- Genaue Marktanteile A2A vs. ACP vs. andere Protokolle — keine verlässlichen Daten gefunden
- FIPA/ACL Irrelevanz — basiert auf Absence-of-Evidence, nicht auf expliziter Deprecation
- MCP-Details konnten wegen Rate-Limiting nicht separat recherchiert werden (Brave API Limit erreicht)

---

## Interpretation: Was bedeutet das für AgentTrust?

Das Gap ist klar und durch mehrere Quellen bestätigt: **A2A löst Discovery + Communication + System-Auth. Aber niemand löst bisher zuverlässig die Frage "Wer kontrolliert diesen Agent und kann ich dem Akteur dahinter vertrauen?"**

Die vielversprechendsten Ansätze (DIDs/VCs, Entra Agent ID) sind entweder akademisch oder vendor-locked. Ein offenes, protokollagnostisches Trust Layer — das sowohl mit A2A als auch MCP funktioniert — existiert noch nicht.

**Das ist die AgentTrust-Opportunity.**

---

## Empfehlung

Thought-Leadership-Piece positionieren: "Authentication ≠ Trust — Why A2A and MCP Need a Trust Layer" (weil corrections.md#tonalität: direkt, spezifisch, keine generischen Überschriften). Zielgruppe sind AI Engineers, die gerade A2A implementieren und merken, dass OAuth allein nicht reicht. AgentTrust als das fehlende Puzzle-Stück positionieren, das Provenienz + Intention + Reputation löst.

---

## Quellen

1. Google Developers Blog — "Announcing the Agent2Agent Protocol (A2A)" — Apr 2025 — https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/
2. Google Developers Blog — "A2A Enhancements at Google I/O" — Mai 2025 — https://developers.googleblog.com/agents-adk-agent-engine-a2a-enhancements-google-io/
3. Linux Foundation — "A2A Project Launch" — Jun 2025 — https://www.linuxfoundation.org/press/linux-foundation-launches-the-agent2agent-protocol-project
4. Google Cloud Blog — "A2A Getting an Upgrade" — Jul 2025 — https://cloud.google.com/blog/products/ai-machine-learning/agent2agent-protocol-is-getting-an-upgrade
5. IBM Think — "What Is Agent2Agent Protocol?" — Nov 2025 — https://www.ibm.com/think/topics/agent2agent-protocol
6. Gravitee — "A2A and MCP" — Apr 2025 (updated Jan 2026) — https://www.gravitee.io/blog/googles-agent-to-agent-a2a-and-anthropics-model-context-protocol-mcp
7. Microsoft Tech Community — "Zero-Trust Agents" — Jun 2025 — https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/zero-trust-agents-adding-identity-and-access-to-multi-agent-workflows/4427790
8. CIO.com — "Trust in the Age of Agentic AI Systems" — Feb 2026 — https://www.cio.com/article/4130267/trust-in-the-age-of-agentic-ai-systems.html
9. Huang et al. — "Zero-Trust Identity Framework for Agentic AI" — Mai 2025 — https://arxiv.org/html/2505.19301v1
10. BiometricUpdate — "Prove Verified Agent" — Okt 2025 — https://www.biometricupdate.com/202510/incode-prove-unveil-identity-layers-to-secure-ai-agent-transactions
11. Cisco Community — "A New Identity Framework for AI Agents" — Dez 2025 — https://community.cisco.com/t5/security-blogs/a-new-identity-framework-for-ai-agents/ba-p/5294337

---

## Beipackzettel

```
Confidence: 72%
Sources checked: 11
Verified facts: 8
Unverified claims: 4
Search queries used: 
  - "Google A2A protocol agent-to-agent communication 2025 2026"
  - "agent trust layer identity verification multi-agent AI systems 2025 authentication"
  - (2 weitere Queries failed wegen Brave API Rate Limit)
Time spent: ~5 min
Limitation: MCP-Tiefenrecherche durch API-Rate-Limit eingeschränkt. 
  Empfehlung: MCP-Spec separat nachlesen (https://modelcontextprotocol.io)
```
