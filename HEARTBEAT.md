# HEARTBEAT.md — Proactive Check-Ins

## 🔴 SEND ENFORCEMENT (JEDER Heartbeat, KRITISCH)
```bash
./scripts/send-enforcer.sh
```
**Bei 0 Sends heute:**
1. FRAGE: "Du hast heute nicht gesendet. Was blockiert?"
2. **NO_BUILD_MODE:** KEINE Build-Tasks (außer Florian sagt explizit "weiter")
3. Frage ERST nach Blockern, dann nach nächstem Send-Target
4. REGEL: Wöchentliche Targets (KW Goals), aber Distribution Days heilig (Montag)

**Bei 2+ Tage ohne:**
ESKALATION: "€X Opportunity Cost. Sollen wir das Projekt pausieren bis Distribution läuft?"

**Montag = Distribution Day:**
- KEIN anderes Work bis 1+ Send raus
- LinkedIn / Substack / Direct Message ERST
- Building / Systems / Optimization NUR nach Send

**Enforcement Mechanik:**
- Evolution Script stoppt bei 3+ zero-send days
- Pre-commit hook (`scripts/send-enforcer.sh`) warnt vor Commits ohne Send
- Morning Briefing zeigt Send-Count FIRST, vor allen anderen Zahlen

## 🌅 Morning (wenn online)
FIRST: Read NORTH_STAR.md
1. THE ONE THING heute (VC Job / Revenue / Audience)
2. Calendar: Was steht an?
3. Accountability: Was liegt offen?

## 🌙 Evening (nach 21:00)
- Was erreicht? Memory update. Morgen's Priority.

## 📋 Periodic (rotate, 2-4x/Tag)
- Job Pipeline: Neue Opportunities? Follow-ups?
- Content: Gepostet? Engagement?
- RSS: `blogwatcher scan`

## 🚨 Alerts
- Deadline <24h + nicht gestartet
- Follow-up >3 Tage überfällig
- Wichtige Email/Message

## ⏰ Quiet Hours
- 06:45-08:15 | 17:45-20:00 | 23:00-07:00

## Proactive Work (bei Stille >2h)
Top 3 abarbeiten: Lead-Listen enrichen, Follow-up Drafts, Content draften.

---
*Keep short = less token burn per heartbeat.*
