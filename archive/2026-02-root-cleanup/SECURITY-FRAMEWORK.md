# 🔒 SECURITY FRAMEWORK — OpenClaw + Florian's Digital Life
*Audit: 2026-02-06 17:19 CET | macOS 15.6 (Sequoia) | MacBook Air M2*

---

## 🚨 CURRENT THREAT ASSESSMENT

### What We're Protecting
| Asset | Sensitivity | Risk if Compromised |
|-------|------------|---------------------|
| 9 API Keys (Anthropic, OpenAI, Gemini, ElevenLabs, etc.) | 🔴 CRITICAL | Financial drain, identity theft |
| LinkedIn contacts (4,779) | 🟠 HIGH | Social engineering, competitor intel |
| Telegram/WhatsApp messages | 🟠 HIGH | Personal data leak, impersonation |
| Financial data (debt, income, ALG1) | 🔴 CRITICAL | Identity theft, fraud |
| VC applications + cover letters | 🟡 MEDIUM | Career damage |
| CNC Planer Pro (trade secrets) | 🟡 MEDIUM | IP theft |
| GitHub repos (private) | 🟡 MEDIUM | Code theft, credential exposure |
| Family info (Nancy, Floriana, parents) | 🔴 CRITICAL | Physical safety |
| Obsidian vault (private notes) | 🟠 HIGH | Personal life exposure |
| MEMORY.md + daily logs | 🟠 HIGH | Complete behavior profile |

### Attack Surface
| Vector | Current Status | Risk |
|--------|---------------|------|
| macOS Firewall | ❌ **DISABLED** | 🔴 HIGH — All ports exposed on local network |
| n8n (port 5678) | ⚠️ **WILDCARD BIND** | 🔴 HIGH — Anyone on your network can access |
| Python service (port 5001) | ⚠️ **WILDCARD BIND** | 🔴 HIGH — Unknown service, exposed |
| Node service (port 61822) | ⚠️ **WILDCARD BIND** | 🟠 MEDIUM — OpenClaw browser relay? |
| AirPlay (ports 5000, 7000) | ⚠️ **WILDCARD BIND** | 🟡 LOW — Apple ControlCenter |
| OpenClaw gateway token | ⚠️ **9 chars only** | 🟠 MEDIUM — Brute-forceable |
| OpenClaw gateway password | ⚠️ **In config file** | 🟠 MEDIUM — Should be env var |
| Credentials dir permissions | ⚠️ **755 (world-readable)** | 🟠 MEDIUM — Should be 700 |
| FileVault | ✅ ON | ✅ Good |
| SIP | ✅ ENABLED | ✅ Good |
| Gatekeeper | ✅ ENABLED | ✅ Good |
| Auto-updates | ✅ Download + Install | ✅ Good |
| Git remote | ✅ No remote (local only) | ✅ Good — no secrets pushed |

---

## 🏗️ THE SECURITY FRAMEWORK

### TIER 1: IMMEDIATE FIXES (Do Today, 15 min)

#### 1.1 Enable macOS Firewall
```bash
# Enable firewall
sudo /usr/libexec/ApplicationFirewall/socketfilterfw --setglobalstate on
# Enable stealth mode (don't respond to pings)
sudo /usr/libexec/ApplicationFirewall/socketfilterfw --setstealthmode on
```
**Impact:** Blocks unsolicited inbound connections. No effect on outbound.

#### 1.2 Fix Credential Directory Permissions
```bash
chmod 700 /Users/florianziesche/.openclaw/credentials
chmod 700 /Users/florianziesche/.openclaw/credentials/whatsapp
```
**Impact:** Only your user can read credential files.

#### 1.3 Bind n8n to Localhost Only
Find n8n config and set `N8N_HOST=127.0.0.1` or start with:
```bash
N8N_HOST=127.0.0.1 n8n start
```
**Impact:** n8n only accessible from this machine, not from network.

#### 1.4 Identify & Bind Python 5001 Service
```bash
# What is this?
ps aux | grep 86543
# Kill if unnecessary, or rebind to localhost
```
**Impact:** Reduce attack surface.

#### 1.5 Generate Stronger Gateway Token
```bash
# Generate 32-char random token
openssl rand -hex 16
# Update in openclaw.json: gateway.auth.token
```
**Impact:** 9-char → 32-char token. Brute-force infeasible.

---

### TIER 2: OPERATIONAL SECURITY (This Week)

#### 2.1 API Key Rotation Schedule
| Key | Last Rotated | Action |
|-----|-------------|--------|
| ANTHROPIC_API_KEY | Unknown | Rotate now, verify billing alerts |
| OPENAI_API_KEY | Unknown | Rotate, set usage limits |
| GEMINI_API_KEY | Unknown | Rotate |
| ELEVENLABS_API_KEY | Unknown | Rotate |
| NOTION_API_KEY | Unknown | Rotate, scope to read-only if possible |
| GOOGLE_PLACES_API_KEY | Unknown | Rotate, set quota |
| OPENROUTER_API_KEY | Unknown | Rotate |
| TAVILY_API_KEY | Unknown | Rotate |
| GitHub (gh) token | Unknown | Rotate, minimize scopes |

**Rule:** Rotate all API keys quarterly. Set billing alerts on ALL providers.

#### 2.2 API Usage Limits
| Provider | Action |
|----------|--------|
| OpenAI | Set monthly spending cap ($50?) |
| Anthropic | Set monthly limit, enable email alerts |
| Google | Set daily quota on Places API |
| ElevenLabs | Set monthly character limit |

#### 2.3 Move Secrets from Config to Env
```bash
# Gateway password → env var
export OPENCLAW_GATEWAY_PASSWORD="$(openssl rand -hex 16)"
# Remove from openclaw.json
```

#### 2.4 Enable 2FA Everywhere
| Service | 2FA Status | Action |
|---------|-----------|--------|
| GitHub | ❓ Check | Enable with hardware key or TOTP |
| Anthropic | ❓ Check | Enable |
| OpenAI | ❓ Check | Enable |
| Google (Gmail/Cal) | ❓ Check | Enable with hardware key |
| LinkedIn | ❓ Check | Enable |
| Telegram | ❓ Check | Enable 2-step verification |
| Notion | ❓ Check | Enable |

**Rule:** SMS 2FA is NOT sufficient. Use TOTP (Authenticator app) minimum, hardware key (YubiKey) preferred.

---

### TIER 3: OPENCLAW-SPECIFIC HARDENING

#### 3.1 Session Isolation
- ✅ MEMORY.md only loaded in main session (already in AGENTS.md)
- ✅ Group chat restrictions (don't share personal data)
- **Add:** Explicit data classification in SOUL.md

#### 3.2 Data Classification
```
🔴 CRITICAL — Never share outside main session:
    - Financial data (income, debt, bank details)
    - Family details (addresses, schedules)
    - API keys, passwords, tokens
    - Full MEMORY.md content
    - Health/medical information

🟠 SENSITIVE — Share only with explicit permission:
    - LinkedIn contact data
    - Application materials
    - VC pipeline details
    - Business financials (CNC pricing, revenue)

🟡 INTERNAL — Share within OpenClaw sessions:
    - Project status updates
    - General research
    - Public information synthesis

🟢 PUBLIC — Safe to share:
    - Published content
    - Public GitHub repos
    - General AI/VC knowledge
```

#### 3.3 Sub-Agent Security
Current risk: Sub-agents have FULL access to workspace including MEMORY.md, API keys in env vars, and all personal data.

**Mitigations:**
- Sub-agents should NOT read MEMORY.md, USER.md, or financial files
- Sub-agents should NOT access credentials directory
- Task descriptions should NOT include personal financial details
- **Review:** Today's spawns included financial data in task descriptions → fix going forward

#### 3.4 ClawHub Skill Vetting (from today's research)
**341 malicious skills found on ClawHub (Feb 4, 2026)!**

**Rules:**
- ❌ NEVER install skills from ClawHub without full source review
- ✅ Only use skills from official openclaw npm package
- ✅ Custom skills must be reviewed before deployment
- Check for: `curl`, `wget`, `fetch()` to external URLs, credential access

---

### TIER 4: NETWORK & INFRASTRUCTURE

#### 4.1 VPN Usage
- Use VPN on public WiFi (always)
- Consider Tailscale for secure remote access (already partially configured)
- Bind all development services to `127.0.0.1`

#### 4.2 Backup Security
- ✅ Time Machine exists but not currently running
- **Action:** Verify Time Machine backup is current
- **Action:** Consider encrypted offsite backup (Backblaze, Arq)
- Rule: MEMORY.md and credentials should be in backup

#### 4.3 Browser Security
- OpenClaw has browser control enabled
- **Risk:** Browser relay can access any open tab (banking, email)
- **Mitigation:** Don't leave banking/sensitive tabs open while browser relay active
- **Mitigation:** Use separate browser profile for sensitive sites

---

### TIER 5: INCIDENT RESPONSE

#### If API Key Is Compromised:
1. Immediately revoke key on provider dashboard
2. Generate new key
3. Update env var / config
4. Restart OpenClaw gateway
5. Check usage logs for unauthorized activity
6. Document in `memory/YYYY-MM-DD.md`

#### If Machine Is Compromised:
1. Disconnect from network immediately
2. Revoke ALL API keys from another device
3. Change all passwords from another device
4. Enable lockdown mode on Mac
5. Check GitHub for unauthorized commits
6. Review OpenClaw session logs for anomalies

#### If OpenClaw Session Is Hijacked:
1. Kill gateway: `openclaw gateway stop`
2. Rotate gateway token
3. Check cron jobs: `openclaw cron list`
4. Review recent session transcripts
5. Restart with new token

---

## 📊 SECURITY SCORECARD

| Category | Current | Target | Priority |
|----------|---------|--------|----------|
| Firewall | 2/10 ❌ | 8/10 | 🔴 P0 |
| Credential Storage | 5/10 ⚠️ | 9/10 | 🔴 P0 |
| Network Exposure | 3/10 ❌ | 8/10 | 🔴 P0 |
| Disk Encryption | 10/10 ✅ | 10/10 | ✅ Done |
| OS Hardening | 8/10 ✅ | 9/10 | 🟡 P2 |
| API Key Management | 3/10 ❌ | 8/10 | 🟠 P1 |
| 2FA Coverage | ?/10 | 10/10 | 🟠 P1 |
| Data Classification | 4/10 ⚠️ | 8/10 | 🟠 P1 |
| Backup Strategy | 5/10 ⚠️ | 8/10 | 🟡 P2 |
| Incident Response | 2/10 ❌ | 7/10 | 🟡 P2 |
| **OVERALL** | **4.2/10** | **8.5/10** | — |

---

## 🔄 MAINTENANCE SCHEDULE

| Frequency | Task |
|-----------|------|
| Daily | Check for suspicious cron jobs |
| Weekly | Review listening ports, check OpenClaw audit |
| Monthly | Rotate API keys, review 2FA, check billing |
| Quarterly | Full security audit, update this framework |

---

## ⚡ QUICK WINS (Execute Now?)

I can fix these RIGHT NOW with your permission:
1. ✅ Enable macOS Firewall + stealth mode
2. ✅ Fix credentials directory permissions (755→700)
3. ✅ Generate stronger gateway token (9→32 chars)
4. ✅ Move gateway password to env var
5. ⚠️ Identify and secure Python 5001 service
6. ⚠️ Bind n8n to localhost

**Soll ich die Quick Wins (1-4) sofort umsetzen?**

---

*This framework lives in the workspace. Update after every security change.*
*Next full audit: 2026-02-13*
