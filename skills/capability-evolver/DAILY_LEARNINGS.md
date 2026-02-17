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

---

## 2026-02-15 (Sonntag)

### OpenClaw Updates (v2026.2.14)
- **Telegram Polls:** `openclaw message poll` — nützlich für Feedback/Entscheidungen
- **Slack/Discord dmPolicy:** Neue DM-Zugangskontrolle
- **Sandbox browser binds:** Separate Browser-Container-Mounts
- **Fix:** One-shot `message send` hängt nicht mehr

### AI Agent Patterns (Anthropic Blog)
- **81% der Orgs** planen komplexere Multi-Step Agent Workflows in 2026
- **Key Insight:** "Agents as infrastructure, not experiments" — genau Mias Positionierung
- **Thomson Reuters:** 150 Jahre Fallrecht in Minuten durchsuchbar via Agent
- **eSentire:** Threat-Analyse von 5h → 7min (95% Übereinstimmung mit Experten)
- **Content-Idee für Florian:** "How I built my personal AI agent infrastructure" — unique angle vs. Enterprise-Fokus

### Workflow-Analyse (letzte 24h, Feb 14)
- **Wins:** 9/9 Research Reports fertig, Google Drive Sync funktioniert, Template v2 erstellt
- **Problem:** Viel gebaut (Reports), aber unklar ob gesendet → Send-First Pattern weiter enforced
- **Prof. Friedl Outreach** wartet auf Input — Follow-up nötig
- **Nancy iMessage** "talk about Floriana and us" — Florian sollte priorisieren

### Sofort umsetzbar
1. **Telegram Poll-Feature** für Quick Decisions nutzen (z.B. "Welchen Report zuerst senden?")
2. **Content-Pitch:** Anthropic Enterprise Agent Survey als Hook für LinkedIn Post
3. **Send-Tracker:** Gestern 9 Reports gebaut — wie viele davon raus? Heute enforced

---

## 2026-02-17 (Montag, 00:52)

### 🚀 OpenClaw v2026.2.15 — NESTED SUB-AGENTS (Game Changer)
**Release:** 2026-02-15

**Key Features:**
- **Nested sub-agents (sub-sub-agents):** `agents.defaults.subagents.maxSpawnDepth: 2` = Sub-Agents können eigene Children spawnen
- **maxChildrenPerAgent: 5** (default) — verhindert Spawn-Explosion
- **Depth-aware tool policy** + proper announce chain routing
- **Use Case für uns:** Komplexe Research-Tasks können jetzt hierarchisch delegieren (Main → Research Lead → 3 Specialist Agents)

**Weitere relevante Features:**
- **Discord Components v2:** Buttons, selects, modals, file blocks — native interaction
- **Cron webhook delivery toggle + auth token:** `cron.webhookToken` für outbound webhook posts
- **Plugins: llm_input/llm_output hooks:** Extensions können Prompts + Output observieren

**Massive Security Hardening:**
- SHA-1 → SHA-256 für Sandbox-Hashing
- Telegram bot tokens redacted in logs
- Sandbox Docker config injection geblockt (bind mounts, host networking, unconfined seccomp)
- Skills download installer restricted to per-skill tools/ directory

**ACTION:**
1. **Nested Sub-Agents testen:** Nächster komplexer Research Task (z.B. Multi-Report Synthesis) mit hierarchischer Delegation
2. **Config Update:** `maxSpawnDepth: 2` in config wenn wir hierarchische Workflows brauchen
3. **Security Audit:** Skills directory permissions prüfen

### AI Workflow Patterns 2026 — External Validation
**Quellen:** Stack-AI, Vellum, Beam, Dextralabs

**Konsens:**
1. **"Start with clarity on outcome, pick simplest workflow"** — Simplicity > Komplexität
2. **"Tool design, grounding, observability"** = wichtiger als Workflow-Komplexität
3. **9 Standard Patterns:** ReAct, Plan-Execute, Reflection, Hierarchical, Multi-Agent, Router, Parallelization, Orchestrator-Worker, Evaluator-Optimizer

**Validiert unsere Research:**
- AR-007 (Build vs Buy): "Simple composable patterns > komplexe Frameworks" ✅
- AR-010 (Agent Failure): "Planning, tool use, reflection, iteration" als Core Pattern ✅
- AR-018 (Observability): "Observability = critical" bestätigt ✅

**Key Quote (Stack-AI):**
> "Start with clarity on the outcome you want. Pick the simplest workflow shape that can achieve it safely. Then put your effort into tool design, grounding, explicit state, and observability. That is what makes agents dependable in 2026."

**Kein neues Insight** — aber starke externe Bestätigung dass unsere Pipeline-Philosophie (simple, observable, grounded) richtig ist.

### ClawHub Status
- **500+ Skills** verfügbar
- **Security:** 341 malicious skills gefunden (known, dokumentiert 2026-02-15)
- **Community-Kuratierung:** Reddit "Best Skills" Post aktiv
- **ACTION:** Florian bitten ClawHub zu browsen für neue verified Skills (browser tool nutzen)

### Send Enforcement — KEIN Update
Evolver hat keine neuen Erkenntnisse gebracht. Problem bekannt seit 2026-02-15 05:00 CET.
- 3 Tage zero sends
- €1263 opportunity cost (heute)
- Enforcement-Mechanismen existieren aber werden übersprungen

**Nächste Actions (aus DAILY_LEARNINGS 2026-02-15):**
1. Heartbeat ruft send-enforcer.sh auf
2. Git pre-commit hook blockiert commits bis gesendet
3. SOUL.md Update: "Bei 0 Sends heute: ERST senden, DANN bauen"

### Sofort umsetzbar
1. **Nested Sub-Agents:** Nächster komplexer Task hierarchisch delegieren (test maxSpawnDepth: 2)
2. **External Validation:** Stack-AI/Vellum Quotes in AR-007/AR-010 Updates nutzen
3. **Security:** Skills directory audit (sind alle Skills verified?)
