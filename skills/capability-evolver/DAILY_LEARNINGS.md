# Daily Self-Improvement Learnings

## 2026-02-15 (So, 05:00) — SEND ENFORCEMENT CRISIS

### 🚨 KRITISCHER BEFUND: 5 Tage Zero Sends = €2.105 Opportunity Cost
**Pattern:** Building ohne Shipping. 15 Reports fertig, 0 published. AgentTrust Repo privat. Research vollständig, Distribution = 0.

**ROOT CAUSE:**
1. `scripts/pre-build-check.sh` existiert aber wird NICHT enforced
2. `./scripts/send-enforcer.sh` zeigt Zahlen aber BLOCKIERT nicht
3. SOUL.md "Send First" = Hinweis, keine harte Regel
4. Florian muss am Wochenende erinnern statt System verhindert

**SOFORT IMPLEMENTIEREN:**
1. **Heartbeat MUSS send-enforcer.sh aufrufen** — Bei 0 Sends: "Du hast heute nicht gesendet. Was blockiert?"
2. **pre-build-check.sh als Git pre-commit hook** — Commit blocken bis gesendet
3. **SOUL.md Update:** "Bei 0 Sends heute: ERST senden, DANN bauen. Keine Ausnahme."
4. **Wöchentliche Targets statt täglich** (Florian Feedback) — aber Montag = Distribution Day

### OpenClaw v2026.2.14 — Neue Features (heute released)
- **Telegram Poll Sending:** `openclaw message poll` — nützlich für Votes/Entscheidungen
- **Cron text-only delivery:** Volle Outputs wenn delivery.to gesetzt — wichtig für Briefs
- **Image tool workspace paths:** Workspace-lokale Bilder erlaubt — erleichtert Workflows
- **CLI message send exits properly:** Kein Hang mehr bei one-shot sends

**ACTION:** Poll-Feature für Template-Chooser/Report-Voting nutzen. Image-Tool-Fix vereinfacht Screenshot-Workflows.

### ClawHub Security Warning
- **ClawHavoc:** 341 malicious skills auf ClawHub gefunden
- **Vetting-Problem:** Wer prüft Skills? — niemand systematisch
- **ACTION:** NUR verified skills installieren, eigene Skills im workspace/ hosten

### AI Agent Workflow Patterns 2026
- **Vellum:** MCP-powered Agent Nodes + Workflow Console — moderne Orchestrierung
- **ISO/IEC 42001 Compliance** mehrfach erwähnt — bestätigt unsere Research (AR-008)
- **Human-in-the-loop NOCH kritisch** trotz "autonomous" Hype — deckt sich mit AR-011 (67% Alert Fatigue)
- **Trend:** Simple composable patterns > komplexe Frameworks (wie wir in AR-007 fanden)

### Wiederkehrende Fehler (letzte 48h)
1. **RAM SIGKILL** — MacBook Air 8GB limit bei Pandoc parallel/backup.sh → sequenziell arbeiten
2. **Website Rollbacks** — zu viele Änderungen auf einmal → einzeln deployen
3. **Context Waste** — Report #1 ohne Context Pack (840K tokens) vs #2 mit Pack (470K) → -44%
4. **Brave Search Quota** — erschöpft, blockierte Research → jetzt Pro Plan
5. **Fact-Check Credibility** — TrustCheck ohne externe Verifikation = LLM-Meinung → Standards nötig

### Learnings aus Report Pipeline (9 Reports, QA 86.3 avg)
- **Context Pack = Game Changer:** -47% Zeit, -44% Tokens, +6 QA Punkte
- **Sonnet für Builder/QA:** Gleiche Qualität wie Opus, 40% billiger
- **Design-Zurückhaltung:** Gold sparsam, keine Deko, Economist-Stil → Autorität
- **Exec Summary + Footnotes Standard:** Ab Report #3
- **Gap Analysis:** Fester Pipeline-Schritt vor Writer

### Implementiert (letzte 48h)
✅ Context Pack System (93% Token-Reduktion)
✅ Vault Optimization (77→89 Health Score, +618 Links)
✅ Claim Notes in Obsidian (last_verified tracking)
✅ Freshness System (Cite=Verify Regel)
✅ Trust Dashboard (SHA-256 hash chain)
✅ Pipeline Improvement Protocol (wissenschaftliche Hypothesen-Tests)
✅ Self-Improvement Loop v1 Spec

### NOCH NICHT IMPLEMENTIERT (Blocker: Distribution)
- Send Enforcement (kritisch!)
- Montag Launch Stack (Reports, AgentTrust Repo public, Posts)
- Cross-Platform Distribution (X → LinkedIn → Substack → Website)

## 2026-02-13 (Fr, 06:00)

### OpenClaw Updates — v2026.2.12 (gestern!)
- **Telegram Blockquotes:** Blockquotes werden jetzt nativ gerendert statt gestrippt → Kann ich für bessere Formatierung nutzen
- **Security Hardening:** Web/Browser content wird jetzt als untrusted behandelt, SSRF-Schutz, Hook session-routing gehärtet
- **CLI:** `openclaw logs --local-time` für lokale Zeitzonen
- **Breaking:** POST /hooks/agent lehnt sessionKey overrides ab (default). Relevant falls wir Hooks nutzen.
- **Action:** Keine sofortige Aktion nötig. Blockquote-Feature testen bei nächster Gelegenheit.

### ClawHub Skills
- ClawHub (clawhub.ai) ist JS-rendered, nicht crawlbar via fetch. Manueller Check nötig.
- **Action:** Florian bitten, gelegentlich ClawHub zu browsen, oder Browser-Tool nutzen.

### AI Agent Patterns (Web Research)
- **Enterprise Agentic AI 2026:** Microsoft pusht "Workflows Agent" — wiederholbare automatisierte Business-Prozesse. Parallele zu unseren Cron-Jobs + Sub-Agents.
- **Google Antigravity:** Neue Agent-Dev-Platform, Agents direkt in Coding-Environment. Relevant für CNC/Legal AI Projekte.
- **Gemini 3.0 Agentic Reasoning:** Multi-step execution plans für komplexe Ziele. Pattern: Ambiguous goal → decompose → execute steps → validate.
- **Key Trend:** Shift von "Assistants" zu "autonomous workflow handlers". Genau was wir mit OpenClaw machen.

### Workflow-Analyse (letzte 24h)
- Kein aktiver Chat gestern Abend → keine Fehler zu analysieren
- Letzter bekannter Stand: X-Ray Platform deployed, Design-System mit Gold-Palette etabliert
- **Offene Verbesserung:** Pre-flight Script wird oft übersprungen in schnellen Interaktionen → Vereinfachung nötig?

### Sofort umsetzbar
1. Telegram Blockquotes testen für strukturiertere Nachrichten
2. Browser-Tool für ClawHub-Scan bei nächstem Heartbeat nutzen
3. "Decompose → Execute → Validate" Pattern bewusster in Sub-Agent Tasks einbauen
