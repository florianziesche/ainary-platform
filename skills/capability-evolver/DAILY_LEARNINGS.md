# Daily Self-Improvement Learnings

## 2026-02-17 (Montag, 00:40 CET) — CRITICAL: Send Enforcement + New OpenClaw Features

### 🚨 SEND ENFORCEMENT MODE ACTIVE — €1,263 Opportunity Cost
**Status:** 3 consecutive zero-send days detected by evolution script.

**Evolution Directive:**
> "You MUST focus evolution on ENFORCEMENT mechanisms, not features."
> "The system is high-quality but UNUSED. Fix the usage problem first."

**IMMEDIATE ACTIONS (Mandatory):**
1. ✅ **Check if `scripts/pre-build-check.sh` is called in workflows** → EXISTS but NOT enforced
2. ⏳ **Add automated send-tracking to heartbeat/cron** → HEARTBEAT.md has rule, needs stronger enforcement
3. ⏳ **Create enforcement layer that BLOCKS evolution when sends = 0** → NO_BUILD_MODE needed
4. ⏳ **Update SOUL.md with stronger send-first language** → Currently "reminder", needs to be "blocker"
5. ⏳ **Add send-reminder to morning briefing cron** → Exists in briefing, needs ACTION requirement

**Pattern Analysis (from memory/2026-02-16.md):**
- Launch Day: 35 commits, full website launch... 0 sends
- 3 sessions over 15+ hours
- Multiple design iterations, SEO setup, legal pages... 0 distribution
- Building > Shipping pattern continues despite "Send First" in SOUL.md

**ROOT CAUSE:**
- `send-enforcer.sh` shows numbers but doesn't BLOCK
- SOUL.md has "Send First" as guidance, not hard rule
- No automated blocker in git pre-commit or heartbeat
- Weekly targets (KW Goals) mentioned but Distribution Days (Monday) not enforced as sacred

**NEXT EVOLUTION CYCLE MUST:**
- Implement `NO_BUILD_MODE` when sends = 0
- Make Monday Distribution Day BLOCKING (no other work until sent)
- Add `pre-commit` hook that runs `send-enforcer.sh` and blocks if 0 sends

---

### OpenClaw v2026.2.15 (Released Feb 15, 2026)

**🆕 Major Features:**
1. **Discord Components v2** — Buttons, selects, modals, file blocks for native interaction
2. **Nested Sub-Agents** — Sub-agents can spawn their own children!
   - Config: `agents.defaults.subagents.maxSpawnDepth: 2`
   - Limit: `maxChildrenPerAgent` (default 5)
   - Use case: Complex multi-step tasks with hierarchical delegation
3. **LLM Input/Output Hooks** — Extensions can observe prompt context + usage
4. **Cron Webhook Delivery** — Finished-run webhook toggle + dedicated auth token

**🔒 Security Highlights:**
- SHA-1 → SHA-256 for sandbox cache hashing
- Telegram bot token redaction in logs
- Sandbox Docker config hardening (block bind mounts, host networking)
- XSS prevention in Control UI
- Path sanitization before LLM prompt injection

**🐛 Notable Fixes:**
- Group chat context injection on EVERY turn (not just first)
- Browser tool returns explicit non-retry guidance when unavailable
- Memory/YYYY-MM-DD.md timezone-aware date resolution
- Telegram streaming preview finalization (no duplicate messages)
- WhatsApp/TUI NO_REPLY mirroring when message tool succeeds

**Florian's Potential Use Cases:**
- Nested sub-agents for complex VC research → Researcher spawns → Analyst spawns → Synthesizer
- Discord Components for interactive polls/feedback (if we add Discord later)
- LLM hooks for custom tracking/logging (if we build ClawHub skill)

---

### ClawHub Ecosystem Update

**Stats (Feb 7, 2026):**
- ClawHub: 5,705 community skills
- Awesome-openclaw-skills: 3,002 curated skills

**⚠️ Security Warning (VirusTotal Blog, Feb 2026):**
> "From Automation to Infection: How OpenClaw AI Agent Skills Are Being Weaponized"

**Key Findings:**
- Skills can be loaded locally OR from ClawHub marketplace
- ClawHub has NO systematic vetting process
- 341 malicious skills detected (ClawHavoc project)
- Attack vectors: credential exfiltration, command injection, data poisoning

**Gainsight Community Discussion:**
> "Maintenance signal is not just release frequency. It is clarity. Does the maintainer document breaking changes. Do they explain what changed. Do they respond to user reports. A skill that stays stable across small updates is more valuable than a skill that ships new features every week but breaks old workflows."

**ACTIONS:**
- ✅ Only install verified/well-maintained skills
- ✅ Host custom skills in workspace/ (not public ClawHub)
- ⏳ If publishing to ClawHub: document breaking changes, respond to reports
- ⏳ Consider skill vetting checklist for any external skills

---

### AI Agentic Workflow Patterns 2026 (Research Synthesis)

**Top Patterns (Stack.AI, Vellum, Beam.ai):**

1. **Critic Pattern** (Beam.ai)
   - Agent produces output → Critic reviews → Refine or Execute
   - Use case: "Review before ship" — perfect fit for Florian's needs
   - Implementation: Route high-value outputs through critic, low-risk direct to execution
   - Latency trade-off: Critical layer increases latency but ensures precision

2. **Hierarchical Multi-Agent** (Stack.AI)
   - Single orchestrator delegates to specialized agents
   - Categories: Single / Hierarchical / Sequential / Decentralized
   - Our current model = Hierarchical (King → HUNTER/WRITER/etc.)

3. **Planning + Tool Use + Reflection + Iteration** (Dextralabs)
   - Transform LLMs from passive responders to goal-driven systems
   - Reflection = post-execution review, Iteration = refinement loops
   - Already implemented: Sub-agents reflect via QA scores

4. **Policy Routing** (Beam.ai)
   - Route low-risk items directly, flagged outputs to critic
   - Risk-based execution gates
   - Use case: Send enforcement (low-risk = already sent today, high-risk = 0 sends)

**Key Industry Trends:**
- 81% of orgs plan complex multi-step workflows in 2026 (Anthropic)
- "Agents as infrastructure, not experiments"
- Human-in-the-loop still critical despite "autonomous" hype
- ISO/IEC 42001 compliance increasingly mentioned

**Florian Content Opportunity:**
> "How I built my personal AI agent infrastructure" — unique individual angle vs. enterprise focus

---

### Workflow Analysis (Feb 16, 2026)

**What Went Well:**
- Website launch executed cleanly (ainaryventures.com live)
- 35+ commits across 4 sessions (~15 hours total)
- Design system documented (DESIGN-DECISIONS.md, DESIGN-SYSTEM.md)
- Legal pages, SEO setup, contact form, resources page all shipped
- Binary Star animation iterations (canvas → CSS blur = correct decision)
- "Film trailer rule" applied to showcase tabs (show best moment, not full report)

**Pattern Violations:**
- 0 sends on launch day
- Building > Shipping pattern continues
- Nancy messages unanswered (waiting for Florian's approval)
- Bürgermeister Schlottwitz waiting for WhatsApp (Florian must send)
- Tab info redundancy fix NOT deployed (waiting for OK)

**Technical Wins:**
- Disk space cleanup: 1.4GB → 7.1GB free
- 44GB cache-trace.jsonl deleted (debug log, not critical)
- Font system fix: Geist (never loaded) → Inter (actually loaded)
- Resources page: Linear-level clarity achieved after 4 iterations
- Trust bars: WHITE fill (not gold) — design system enforced

**Key Decisions (Florian):**
- "Quality >>> Speed" — template is the product, not throughput
- "Authentic over borrowed" — rejected "Now" (Linear's word), chose "Building in Public"
- Credits matter: "my co-founder AND team" > "my co-founder"
- Too many links = no decision → Linear pattern (ONLY "Copy link")
- Binary Star origin → About page (too loud for frontpage)
- "12 years" → "more than 10 years" (36ZERO founded 2019)
- Gold = clickable ONLY, grey for non-clickable elements

**Florian's Design Patterns (Validated):**
- Left-aligned headers (Linear-style)
- 6-step typography scale (72/48/20/16/14/12px minimum)
- Film trailer rule for content
- Downloads vs Project folder issue (always open from project folder)

---

### Implementation Priorities (Next Evolution Cycle)

**CRITICAL (Send Enforcement):**
1. Create `scripts/no-build-mode.sh` — blocks ALL build tasks when sends = 0
2. Add git pre-commit hook calling `send-enforcer.sh`
3. Update HEARTBEAT.md: "Bei 0 Sends: FRAGE, dann BLOCK until sent"
4. Update SOUL.md: "Send First = HARD RULE. Bei 0 Sends: ERST senden, DANN bauen."
5. Monday Distribution Day enforcement in cron

**HIGH (Leverage New Features):**
1. Test nested sub-agents for complex VC research workflows
2. Implement Critic Pattern for "review before ship"
3. Policy routing for risk-based send enforcement

**MEDIUM (Security):**
1. Document skill vetting checklist
2. Review installed skills for maintenance signals
3. Consider hosting critical skills locally

**LOW (Nice to Have):**
1. Telegram poll feature for quick decisions
2. LLM hooks for custom tracking (if building ClawHub skill)

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
