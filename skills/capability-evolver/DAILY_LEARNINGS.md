# Daily Self-Improvement Learnings

## 2026-02-06 (Research Session #1)

### 1. 🔄 OpenClaw Updates — v2026.2.3 & v2026.2.2

**Key new features wir nutzen können:**

| Feature | Version | Impact für uns |
|---------|---------|----------------|
| **Per-channel responsePrefix** | 2026.2.3 | Unterschiedliche Antwort-Prefixes pro Channel (z.B. "♔" für WhatsApp, anders für Discord) |
| **Cron: announce delivery mode** | 2026.2.3 | Isolated cron jobs können jetzt Ergebnisse direkt als Announce delivern — weniger Post-Processing nötig |
| **Cron: one-shot auto-delete** | 2026.2.3 | Einmal-Reminders löschen sich selbst → cleaner cron list |
| **Cron: ISO 8601 schedule.at** | 2026.2.3 | Menschlichere Zeitangaben bei Reminder-Erstellung |
| **Web UI: Agents Dashboard** | 2026.2.2 | Visuelles Agent-Management (Tools, Skills, Models, Cron) — evtl. für Florian zum Überblick |
| **QMD Memory Backend** | 2026.2.2 | Opt-in structured memory — könnte MEMORY.md-System verbessern |
| **Default subagent thinking** | 2026.2.2 | `agents.defaults.subagents.thinking` — Subagents könnten mit Thinking-Level konfiguriert werden → bessere Qualität |
| **Feishu/Lark Plugin** | 2026.2.2 | Nicht relevant für uns (China-Messenger) |
| **Cloudflare AI Gateway** | 2026.2.3 | Alternative Provider-Routing option |

**Security Fixes beachten:**
- Sandboxed media paths enforced (2026.2.3) — gut für uns
- WhatsApp login gated to owner only (2026.2.3) — security improvement
- Untrusted channel metadata blocked from system prompts — prevents injection

**Action Items:**
- [ ] Prüfen ob `agents.defaults.subagents.thinking` unsere Sub-Agent Crash-Rate (~50%) reduzieren könnte
- [ ] QMD Memory Backend evaluieren als Alternative zu MEMORY.md flat files
- [ ] responsePrefix pro Channel konfigurieren (♔ für WhatsApp)

---

### 2. 🛡️ ClawHub Security Alert — KRITISCH

**341 malicious skills auf ClawHub gefunden!** (Koi Security, Feb 4 2026)

**Was passiert:**
- Fake Skills mit professioneller Dokumentation
- "Prerequisites" Section leitet User zu Malware-Download
- macOS: Atomic Stealer (AMOS) via obfuskierte Shell-Scripts
- Windows: Trojanisierte ZIP-Archive mit Keylogging
- Ziel: API Keys, Credentials, `.clawdbot/.env` Exfiltration

**Typosquatting-Muster:**
- clawhub, clawhub1, clawhubb, clawhubcli → Fake marketplace clones
- youtube-summarize, solana-wallet-tracker → Beliebte Utility-Fakes
- auto-updater-agent → Besonders gefährlich (mimics system updates)

**Unsere installierte Skills prüfen:**
- Alle Skills unter `/Users/florianziesche/.nvm/versions/node/v24.13.0/lib/node_modules/openclaw/skills/` stammen aus dem Haupt-Package → SICHER
- Custom skill `capability-evolver` in workspace → selbst erstellt → SICHER
- **KEINE Skills von ClawHub installiert** → Wir sind NICHT betroffen

**Regel für Zukunft:**
- NIEMALS Skills von ClawHub installieren ohne Source-Code-Review
- Nur Skills aus dem offiziellen openclaw npm-Package verwenden
- Bei neuen Skills: prüfe `package.json`, `index.js` auf verdächtige URLs, shell commands, fetch() calls
- Kein `curl | sh` oder Download-Anweisungen aus Skill-Prerequisites folgen

---

### 3. 🧠 AI Agent Patterns — Neue Erkenntnisse

**Quelle 1: Anthropic "State of AI Agents 2026" Report**
- 57% der Orgs nutzen Agents für Multi-Stage Workflows (nicht mehr single-task)
- 80% berichten messbaren ROI von Agent-Investments
- Top Use Cases: Data Analysis (60%), Internal Process Automation (48%), Coding (86%)
- Hauptprobleme: System Integration (46%), Data Quality (42%), Change Management (39%)
- **Insight für Florian:** 90 leaders sagen Agents verschieben Arbeit von Routine → Strategic. Das IST Florians Content-Thesis ("AI as Chief of Staff").

**Quelle 2: Agentic Design Patterns (Medium, Sunil Rao)**
- **Exception Handling & Recovery Pattern**: 3-Phase Cycle (Detection → Handling → Recovery)
  - Detection: Red flags monitoren (500 errors, gibberish output, timeouts)
  - Handling: Retry → Fallback → Log
  - Recovery: State Rollback → Self-Correction
- **Direkt anwendbar auf uns:** Sub-Agent crashes (~50% Rate). Wir könnten:
  1. Crash-Detection in spawn-Logik einbauen
  2. Automatic retry mit vereinfachtem Task
  3. Fallback auf main-session Execution wenn spawn fehlschlägt

**Quelle 3: Opus 4.6 auf Azure verfügbar**
- "Best suited for agentic workflows, reliably orchestrating complex tasks across dozens of tools"
- "Proactively spin up sub-agents, parallelize work, drive tasks forward with minimal oversight"
- Wir hatten den Upgrade-Versuch letzte Nacht → "not allowed". Model ID möglicherweise noch nicht bei Anthropic direkt verfügbar, nur via Azure.

---

### 4. 📊 Workflow-Analyse: Letzte 24h

**Was GUT lief (Feb 5-6):**
- ✅ Massive CNC v18 Hardening: 4188 lines, 164KB, 10 commits in einer Nacht
- ✅ DEFormatter-Library: Konsistente Formatierung überall
- ✅ Quote Section: Dynamische Angebotserstellung funktioniert
- ✅ Build Blocker System deployed (Evolution Cycle #21): Automatische Send-Enforcement
- ✅ All 25 onclick handlers verified (100% coverage)

**Was SCHLECHT lief:**
- ❌ 0 External Sends (wieder!) — Build Blocker wurde deployed aber noch nicht getestet im Einsatz
- ❌ Opus 4.6 Upgrade fehlgeschlagen — Model ID nicht verfügbar
- ❌ Nacht-Session bis 02:30 → Energie für Tag verbraucht?
- ❌ Demo-Ergebnis vom Onkel noch nicht dokumentiert (war gestern 10:30)

**Pattern erkannt:**
- Night Sessions = hoher Output, aber 0 Sends
- Building without sending continues to be THE core problem
- Build Blocker exists now but needs first real-world test today

**Optimierungs-Vorschläge:**
1. **Morning = Send Time**: Erste 30min des Tages NUR für Sends nutzen (Emails, Applications)
2. **Night = Build Time**: Abends bauen ist OK, aber morgens muss dann gesendet werden
3. **Demo Feedback Loop**: Onkel-Demo Ergebnis sofort dokumentieren → Leads generieren

---

### 5. 🔧 Konkrete Verbesserungen (Sofort implementierbar)

**A. Sub-Agent Retry Pattern** (aus Agentic Design Patterns)
```
Wenn sub-agent crasht:
1. Wait 5s
2. Retry mit vereinfachtem Task (weniger Kontext)
3. Wenn 2x crash → fallback auf main session
4. Log crash-reason für Debugging
```

**B. Morning Send Ritual (Cron Job)**
- Täglich 08:30: "Was sind die 3 ready-to-send Items? → JETZT SENDEN"
- Integration mit Build Blocker: Wenn 0 sends um 10:00 → Blocker aktiv

**C. ClawHub Skill Vetting Checklist**
- [ ] Source Code gelesen?
- [ ] Keine curl/wget/fetch zu externen URLs?
- [ ] Keine Prerequisites die Downloads verlangen?
- [ ] Package.json dependencies bekannt?
- [ ] Kein Zugriff auf .env oder credentials?

**D. Config Update Candidates**
- `agents.defaults.subagents.thinking: "medium"` — Subagent Qualität erhöhen
- Per-channel responsePrefix konfigurieren

---

### Meta: Forschungs-Effizienz

- **Dauer:** ~5 Minuten (parallel fetching)
- **Quellen:** GitHub Releases, ClawHub, 8 Web Search Results, 3 Deep-Dives
- **Actionable Items:** 8 konkrete Verbesserungen identifiziert
- **Security Alert:** 1 kritischer Fund (ClawHub Malware)
- **Nächste Session:** 2026-02-07 07:00 CET

---

*Generated by Mia's Daily Self-Improvement Research — 2026-02-06 07:07 CET*
