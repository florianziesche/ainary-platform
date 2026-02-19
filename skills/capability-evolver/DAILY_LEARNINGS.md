# Daily Self-Improvement Learnings

## 2026-02-19 (Mi, 03:40) — FALSE NEGATIVE BUG + OpenClaw 2026.2.17

### 🐛 CRITICAL BUG: Send Enforcement False Negative
**Symptom:** Evolver claimed "3 days zero sends, €1263 opportunity cost"  
**Reality:** Glasswing email SENT (19:42), FutureSight CV v2 finalized, verified in memory/2026-02-19.md

**ROOT CAUSE:**
- `send-enforcer.sh` parsing logic fehlt oder schaut auf falsches Log
- Evolver triggert ENFORCEMENT MODE bei False Positive → Noise statt Signal

**FIX NEEDED:**
1. `send-enforcer.sh` → TESTEN mit memory/YYYY-MM-DD.md statt nur session logs
2. Evolver → FALSE NEGATIVE check: bei <3 Sends, memory/*.md scan BEFORE enforcement
3. Confidence Calibration: "0 sends detected" → "Confidence 70%, check if emails/Telegram sent"

**LESSON:** System triggerte auf Schätzung statt Fakten. "Trust but verify" auch für Automationen.

---

### OpenClaw v2026.2.17 (Released Feb 18) — Upgrade Relevant
**Anthropic Features:**
- **1M Context Beta Support:** `params.context1m: true` für Opus/Sonnet → nützlich für große Report Context Packs
- **Sonnet 4.6 Support:** anthropic/claude-sonnet-4-6 mit Fallback zu 4.5 → upgrade wenn stable

**Workflow Improvements:**
- **Nested Sub-Agents:** maxSpawnDepth: 2 erlaubt Sub-Sub-Agents (default 5 children) → komplexe Research-Ketten
- **Subagent Tool-Result Compaction:** Auto-truncate oversized outputs → verhindert context overflow crashes
- **Read Tool Auto-Paging:** Keine expliziten limits mehr, auto-chunks für große Dateien
- **Slack Text Streaming:** Echtzeit-Output statt Batch (falls wir Slack integrieren)

**Platform/Security:**
- **Telegram Inline Button Styles:** primary|success|danger → UX für Voting/Actions
- **Cron Webhook Delivery:** Per-job webhooks statt nur announce → external integrations
- **iOS Share Extension:** Shared URL/text/image → Gateway → relevant wenn Nancy iOS nutzt

**Fixes Worth Noting:**
- Memory FTS fallback für Non-ASCII queries → bessere Suche in Deutsch/CJK
- Discord Components v2 → nicht relevant für uns (Telegram only)

**ACTION:** Update auf 2026.2.17 wenn stable (aktuell v2026.2.15?). 1M Context + Sonnet 4.6 relevant für Report-Pipeline.

---

### AI Agent Workflow Patterns 2026 (Externe Research)
**Key Patterns:**
1. **Planning → Tool Use → Reflection → Iteration** (Agentic Loop Standard)
2. **Hierarchical Multi-Agent:** Main Coordinator + Specialist Sub-Agents
3. **Sequential Pipelines:** Research → Synthesis → QA → Publish (unser aktuelles Modell)
4. **Decentralized Swarms:** Parallel Agents mit Merge (teuer, selten sinnvoll)

**Relevant für uns:**
- **Memory Management Critical:** "Agents that remember compound faster" (deckt sich mit MEMORY.md layered approach)
- **Uncertainty Handling:** "Deliberate feedback loops > fire-and-forget" (deckt sich mit QA-Agent Pattern)
- **Human-in-Loop Still Essential:** 67% automation mit manual review = sweet spot (AR-011 bestätigt)

**NOT Relevant:**
- "Swarm" Hype = teuer, debugging nightmare
- "Autonomous" Claims = Marketing, echte Use Cases brauchen Gates

---

### ClawHub/Showcase Scan — Keine neuen Skills für Florian
- ClawHub rendered page → kein structured output
- Showcase = User Stories, keine neuen patterns
- **Security Note:** ClawHavoc = 341 malicious skills detected → NUR verified skills

**ACTION:** NOOP. Wir entwickeln eigene Skills nach Bedarf.

---

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

---

## 2026-02-18 (Dienstag, 05:00) — SEND ENFORCEMENT + LEARNING SCAN

### 🧬 Capability Evolution Run #0040
**Status:** ⚠️ SEND ENFORCEMENT MODE (3 zero-send days, €1263 opportunity cost)

### OpenClaw v2026.2.17 Released (Feb 18)
**Relevant für Florian:**
- **Sonnet 4.6 support** (anthropic/claude-sonnet-4-6) — wir nutzen es bereits ✅
- **1M context beta:** `params.context1m: true` für Opus/Sonnet → nützlich für deep research
- **Memory search FTS fallback** + query expansion → bessere memory_search Ergebnisse
- **Auto-read paging:** Größere Contexts können mehr Zeilen lesen bevor Truncation
- **Subagent context handling:** Bessere Guidance bei truncated/compacted tool output
- **iOS share extension:** URL/Text/Image direkt an Gateway senden

**Security Hardening (wichtig):**
- Sandbox Docker config injection blocked
- Skills download restricted to tools/ directory
- Better handling of untrusted web content

**ACTION:**
- 1M context beta testen für komplexe Research Tasks (AR-XXX series)
- Memory search sollte jetzt präziser sein durch FTS fallback

### ClawHub Status
- **500+ skills** verfügbar (wir haben ~45 installiert)
- **3002 community skills** in awesome-openclaw-skills repo
- **Security:** 341 malicious skills bekannt, nur verified skills installieren
- **ACTION:** Browser-Scan von clawhub.com für relevante neue skills (z.B. VC research, sales, outreach)

### AI Agent Workflow Patterns (Feb 2026 — External Validation)
**4 Kategorien (Stack-AI Guide 2026):**
1. Single agent workflows
2. Hierarchical multi-agent workflows
3. Sequential pipeline workflows
4. Decentralized swarm workflows

**Core Patterns (bestätigt von Stack-AI, Dextralabs, MLMastery):**
- **Planning + reflection + iteration** = Basis (genau was wir in AR-010 fanden)
- **MCP/A2A protocols** emerging as standards
- **FinOps for agents** (cost tracking) wird Standard
- **Multi-agent orchestration** > single agent

**Key Stats:**
- **40% of enterprise apps** will have task-specific AI agents by 2026 (Gartner)
- **81% of orgs** planen komplexere multi-step agent workflows (Anthropic)

**Validiert unsere Research:**
- AR-007 (Build vs Buy): Simple composable patterns > komplexe Frameworks ✅
- AR-010 (Agent Failure): Planning + reflection + iteration als Core ✅
- AR-018 (Observability): Observability = critical ✅

**KEINE neuen Patterns** — externe Bestätigung unserer Findings.

### 📊 Last 48h Analysis (Memory Review)
**Good:**
- Primary OIR CV v2 fertig, submitted ✅
- 8 VC email research completed ✅
- Execution Platform v6 gebaut (Flywheel + A/B + confidence)
- CV Generator v2 with confidence scoring
- Quality self-reflection: "2h Platform gebaut statt 8 Emails zu senden"

**Bad (ENFORCEMENT FAILURE):**
- **0 emails sent** trotz 11 cover letters ready
- **€450/month Kindergarten** brennt weiter (Kündigung nicht abgeschickt)
- **ALG1 application** nicht fortgesetzt
- Built Platform v1→v6 statt 8 Emails zu senden
- **3 zero-send days = €1263 opportunity cost**

**Root Cause (unchanged since Feb 15):**
1. `scripts/pre-build-check.sh` existiert aber wird NICHT enforced
2. `scripts/send-enforcer.sh` zeigt Zahlen aber BLOCKIERT nicht
3. SOUL.md "Send First" = Hinweis, keine harte Regel
4. Morning plans say "send" but execution drifts to building
5. Platform has "send" buttons that don't work yet

### 🚨 CRITICAL IMPLEMENTATIONS NEEDED (Priority Order)
1. **Heartbeat MUST call send-enforcer.sh** — Bei 0 sends: "Du hast heute nicht gesendet. Was blockiert?"
2. **Morning briefing:** First section = "Sends gestern: X. Heute geplant: Y. Blocker?"
3. **SOUL.md strengthening:** "Bei 0 Sends heute: ERST senden, DANN bauen. Keine Ausnahme. Frage 'Wurde heute gesendet?' BEVOR jeder Build-Task."
4. **Confidence threshold for building:** < 70% confidence → ask before building, ≥ 70% → ask "Gesendet heute?"
5. **Execution Platform:** Make send buttons ACTUALLY work (gog gmail send integration)

### ⚡ IMPLEMENTED NOW (during this evolution run)
✅ SOUL.md updated with stronger send-first enforcement
✅ Confidence threshold documented in AGENTS.md
✅ DAILY_LEARNINGS.md updated with Feb 18 scan

### 🎯 NEXT EVOLUTION CYCLE MUST:
1. Add send-check to heartbeat.md (ref/HEARTBEAT.md)
2. Test 1M context beta for research tasks
3. Integrate gog gmail send into Execution Platform
4. Add automated send-tracking to evening review

### Key Insight
The system is **high-quality but UNUSED**. We build excellent tools, write strong content, generate perfect CVs — and ship 0%. The evolution priority is **ENFORCEMENT mechanisms** not new features. Make sending EASIER than not sending.

---

## 2026-02-19 (Mittwoch, 03:37) — MORNING BRIEF BUG + OPENLAW UPDATES

### 🐛 CRITICAL BUG FOUND: Morning Brief False Negatives
**Discovery:** Evolver SEND ENFORCEMENT MODE activated (claimed "0 sends"), BUT memory/2026-02-19.md shows:
- **Glasswing VC email SENT** ✅ (rudina@glasswing.vc, message_id 19c736b44c46a5b6)
- **FutureSight CV v2 FINALIZED** ✅ (PDF on Desktop, ready for portal)
- **Primary Application SUBMITTED** ✅ (Florian manually submitted via portal)

**Root Cause:** Morning brief checks **approximate send counts** OR looks at wrong timeframe, NOT actual message logs.

**Impact:**
- False enforcement creates noise ("you haven't sent" when you have)
- Undermines trust in the enforcement system
- Wastes cognitive energy on false alarms

**FIX NEEDED:**
1. Morning brief MUST query actual delivery logs (gog, message tool, sessions history)
2. Check BEFORE dramatizing ("0 sends = €XXX lost")
3. Display actual sends: "Glasswing email (19:42), Primary submitted (08:15)"

**Learnings:**
- D-189: Morning brief dramatisierte statt Fakten zu prüfen — Florian caught this
- ENFORCEMENT = good. FALSE ENFORCEMENT = worse than none.
- Quality gate: verify BEFORE claiming zero

**ACTION:** Add fact-check step to morning brief cron job (check actual sends, not estimates)

---

### 🚀 OpenClaw v2026.2.17 — Key Updates (Released Feb 18)
**Already covered in Feb 18 learnings, no new release since then.**

**Reminder of most relevant features:**
- **1M context beta:** `params.context1m: true` → test for deep research
- **Memory search FTS fallback** → should improve memory_search accuracy
- **Subagent context guards** → better handling of truncated outputs
- **Auto-read paging** → larger contexts read more before truncation

---

### 🔍 ClawHub Scan — No Major New Skills
**Search:** "openclaw new skills clawhub 2026"
**Findings:**
- **500+ skills** on ClawHub (known since Feb 15)
- **3002+ skills** in awesome-openclaw-skills repo (GitHub)
- **Reddit discussion** (1 week ago) about best skills to install
- **No specific NEW skills found** in scan

**Interpretation:** Skill ecosystem is stable, no urgent installs needed.

**ACTION:** No immediate action. Next manual browse when Florian asks or specific need arises.

---

### 📊 AI Agent Workflow Patterns 2026 — ZERO New Insights
**Search:** "AI agent workflow patterns 2026 best practices"
**Findings:**
- **Vellum Guide:** MCP-powered nodes, workflow sharing, collaborative building
- **GoodData:** Core components, common patterns, use cases (Dec 2025)
- **Phaedra Solutions:** ISO/IEC 42001 compliance mentioned (we already know this from AR-008)
- **GitHub Gist:** "Follow established project conventions before introducing new abstractions"

**Verdict:** ZERO new patterns. Everything aligns with existing research (AR-007, AR-010, AR-018).

**Key confirmation:**
- Simple composable patterns > complex frameworks ✅ (AR-007)
- Planning + reflection + iteration = core ✅ (AR-010)
- Observability critical ✅ (AR-018)
- ISO 42001 compliance growing ✅ (AR-008)

**ACTION:** No updates needed. External validation confirms our research is current.

---

### 📅 Memory Scan (2026-02-18 + 2026-02-19)
**Patterns identified:**
1. **3x Demo-Rebuild Failed:** Complex UI (4400-line HTML, 85 API endpoints) can't be copy-pasted. Lesson: use real backend OR enhance existing version, don't rebuild from scratch.
2. **gog OAuth expires ~weekly:** Re-auth needed regularly. Fixed via `gog auth add`.
3. **Em-dashes (—) = LLM tell:** Florian catches every time. NEVER use in CVs.
4. **Sub-Agent Quality Limit:** 4400-line HTML too complex for single-shot. Needs multi-pass or different approach.
5. **Send First Violation:** Build-tasks started without checking "Wurde heute gesendet?" — happened multiple times.

**New Decisions (D-182 to D-194):**
- D-187: "50-Jähriger MacBook Test" for UX — every UI element must be usable without explanation
- D-188: FutureSight CV Summary compact (SMB-focused, CEO not CTO)
- D-193: Glashütte Demo = Light Dashboard (after 3 failed platform-copy attempts)
- D-194: Subtitle with role + company name shows research

**Key Insight (Florian):**
- "Der Standard/das Template IS the Product" — Standards compound, every output improves the standard
- "Wenn der Build Revenue unterstützt, dann ist er gut" — not every build is procrastination
- "Du sagst 0 Sends, aber wir haben HOF + Primary gesendet" — morning brief was WRONG

---

### ⚡ IMPLEMENTATIONS NEEDED (Updated Priority)
1. **FIX MORNING BRIEF BUG** (CRITICAL) — Check actual sends before claiming zero
2. **Add pre-build question to SOUL.md** — "Wurde heute gesendet?" before every >30min build
3. **Test 1M context beta** — For next deep research task (AR-XXX)
4. **Browser-scan ClawHub** — Only when Florian asks or specific need

---

### 🎯 Evolution Cycle Summary
**What went well:**
- Found critical bug in morning brief (false negatives)
- Confirmed external AI workflow research = no new insights
- Identified 5 recurring patterns from memory

**What to improve:**
- DAILY_LEARNINGS now 237 lines — needs summarization/archival strategy
- Evolver activated send enforcement based on false data — fix verification first
- No actual CODE changes implemented (only documentation)

**Next cycle MUST:**
1. Implement morning brief fact-check
2. Update SOUL.md with stronger pre-build enforcement
3. Consider DAILY_LEARNINGS archival (move old months to archive/)

**Confidence:** 85% — Bug found and documented, but not yet fixed. External scan complete but no new actionable insights.
