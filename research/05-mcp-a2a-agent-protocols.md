# Research Report #5: MCP vs A2A vs ACP — Die Protocol Wars 2026
*Mia ♔ | 2026-02-23 | [INTERN]*

---

## THE ANSWER
Die Agent-Infrastruktur konvergiert auf **drei Protokoll-Ebenen**: MCP (Agent↔Tools), A2A (Agent↔Agent), und ACP (Agent↔Agent innerhalb eines Systems). MCP hat gewonnen — es wurde von Anthropic an die Linux Foundation gespendet und wird von OpenAI, Google und Block unterstützt. Für uns relevant: MCP könnte unser Research-Pipeline als Tool-Server exponieren. Aber: für unsere aktuelle Phase (0-10 Kunden) ist das **irrelevant**. Keine Architektur-Entscheidung nötig bis Phase 2.

## CONFIDENCE: Likely (78%)

---

## KEY EVIDENCE

### Die drei Protokolle
| Protokoll | Ersteller | Zweck | Status |
|-----------|-----------|-------|--------|
| **MCP** | Anthropic (Nov 2024) | AI ↔ Tools (Datenbanken, APIs, Dateisysteme) | ✅ Gewinner. Linux Foundation. OpenAI+Anthropic+Block. |
| **A2A** | Google (Apr 2025) | AI ↔ AI (verschiedene Systeme) | 🟡 Wachsend. 50+ Partner. |
| **ACP** | IBM/BeeAI | AI ↔ AI (innerhalb eines Systems) | 🟡 Nische. |
| **UTCP** | Community | Unified Tool Calling (OpenAI+Anthropic+Google vereinen) | 🔴 Früh. |

### Emerging Consensus
> "MCP for tools, ACP or A2A for agent collaboration. Which agent protocol wins may matter less than having one at all." **[B1]** Context Studios, Feb 2026

### Was bedeutet das für unsere Architektur?
| Unser System | Aktuell | Mit MCP |
|-------------|---------|---------|
| Research Pipeline | Manuell + Scripts | MCP-Server: `ainary-research` → LLM kann Tools aufrufen |
| Template Generator | `generate-v2.js` | Bleibt (kein MCP nötig) |
| Analytics | Custom API | Bleibt (zu spezifisch für MCP) |
| Gotham Frontend | Static HTML | Bleibt (Client, kein Agent) |

**Verdict:** MCP ist relevant für Phase 2 (Automatisierung). Für Phase 1: ignorieren.

---

## SOURCES
```
[A1] MCP Wikipedia → en.wikipedia.org/wiki/Model_Context_Protocol
[B1] MCP and A2A: Building the AI Agent Internet, Medium, Feb 2026 → medium.com/@aftab001x/...
[B1] ACP vs MCP Protocol War, Context Studios, Feb 2026 → contextstudios.ai/blog/...
[B2] MCP vs A2A for Business Automation, Cohorte → cohorte.co/blog/...
[B2] Memory in AI: MCP+A2A, Orca Security, May 2025 → orca.security/resources/blog/...
```

---

*Report 5/10 complete. ♔*
