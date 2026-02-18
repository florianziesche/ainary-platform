# Security — Execution Platform (ISO 27001 aligned)

**Version:** 1.0 | **Date:** 2026-02-19 | **Classification:** INTERNAL

> See also: [ARCHITECTURE.md](ARCHITECTURE.md) · [DOCUMENTATION.md](DOCUMENTATION.md) · [DB-SCHEMA.md](DB-SCHEMA.md)

---

## 1. Data Classification

| Data Type | Examples | Classification | Storage |
|-----------|----------|---------------|---------|
| Findings, Topics | Research results, task context | INTERNAL | workbench.db |
| Trust Scores, Decisions | Skill scores, correction rules | INTERNAL | workbench.db |
| API Keys, Credentials | OPENAI_API_KEY, ANTHROPIC_API_KEY | RESTRICTED | Environment variables |
| User Data | Email addresses, names (contacts) | CONFIDENTIAL | workbench.db |
| Published Research | Blog posts, public analyses | PUBLIC | Git / website |
| Conversation History | Messages between Florian & Mia | INTERNAL | workbench.db |
| Uploaded Documents | CVs, attachments per topic | CONFIDENTIAL | uploads/ directory |

### Classification Levels

| Level | Definition | Handling |
|-------|-----------|----------|
| **PUBLIC** | No harm if disclosed | No restrictions |
| **INTERNAL** | Business context, no PII | Localhost only, no sharing |
| **CONFIDENTIAL** | Contains PII or sensitive business data | Encrypted storage (planned), access-controlled |
| **RESTRICTED** | Credentials, secrets | Never committed to git, env vars only |

---

## 2. Access Control

| Control | Current State | Target State |
|---------|--------------|-------------|
| Users | Single user (Florian) | Multi-user with RBAC (Phase 5) |
| Network | localhost:8080 only | HTTPS + auth for remote |
| Authentication | None (localhost trust model) | JWT/OAuth for remote deployment |
| Authorization | N/A (single user) | Role-based (admin, viewer) |
| API Access | Unrestricted on localhost | Token-based for external access |
| CORS | `*` (permissive) | Origin-restricted in production |

**Current trust model:** The platform binds to `127.0.0.1:8080`. No external network access. Physical access to the machine = full access. This is acceptable for single-user localhost operation.

---

## 3. Data Storage

| Store | Location | Content | Backup |
|-------|----------|---------|--------|
| SQLite DB | `backend/workbench.db` | All platform data (topics, messages, corrections, trust, events) | Manual copy, Git (schema only) |
| Memory Files | `memory/*.md` | Knowledge cache, decisions, connections | Git-tracked |
| Uploaded Files | `uploads/{topic_id}/` | User-uploaded documents per topic | Not backed up |
| Obsidian Vault | `~/Documents/Obsidian/` | Personal notes, research | iCloud sync |
| Configuration | Environment variables | API keys, secrets | Not backed up (re-created manually) |

**Database size:** ~14 GB (includes seeded data, conversation history, events).

---

## 4. Encryption

| Layer | Current | Planned |
|-------|---------|---------|
| At Rest (DB) | None (relies on macOS FileVault) | Application-level encryption for CONFIDENTIAL data |
| At Rest (Files) | macOS FileVault (full-disk) | Same + encrypted uploads |
| In Transit | N/A (localhost only) | HTTPS/TLS for remote deployment |
| Secrets | Environment variables | Vault/Keychain integration |

**FileVault status:** Enabled on Florian's MacBook Air. All disk data encrypted at OS level.

---

## 5. Backup & Recovery

| What | Method | Frequency | Location |
|------|--------|-----------|----------|
| Code & Docs | Git (GitHub) | Every commit | Remote repository |
| Database | Manual `cp workbench.db workbench.db.bak` | Ad-hoc | Local disk |
| Database | Google Drive upload (attempted) | Planned: daily | GDrive |
| Memory Files | Git-tracked | Every commit | Remote repository |
| Obsidian Vault | iCloud sync | Automatic | iCloud |

### Recovery Procedure

1. **Code:** `git clone` or `git checkout` to restore any version
2. **Database:** Copy backup file to `backend/workbench.db`
3. **Full rebuild:** `git clone` → `pip install` → restore DB → `python3 app.py`

**RTO (Recovery Time Objective):** < 30 minutes for full platform restore.
**RPO (Recovery Point Objective):** Last git commit (code), last manual backup (DB).

---

## 6. Incident Response

### If data is leaked or compromised:

1. **Contain:** Stop the platform (`launchctl unload com.ainary.workbench.plist`)
2. **Assess:** Determine what data was exposed (check classification table above)
3. **Rotate:** Immediately rotate all API keys (OpenAI, Anthropic, Gmail)
4. **Notify:** Contact Florian Ziesche (sole operator and data controller)
5. **Document:** Log incident in `memory/incidents.md` with timeline and actions taken
6. **Fix:** Patch the vulnerability, update SECURITY.md

### Contact

| Role | Person | Channel |
|------|--------|---------|
| Data Controller | Florian Ziesche | Direct |
| System Operator | Florian Ziesche | Direct |

---

## 7. Known Risks

| Risk | Severity | Mitigation |
|------|----------|------------|
| API keys in environment variables (not rotated) | HIGH | Rotate quarterly, use keychain (planned) |
| No authentication on localhost API | MEDIUM | Acceptable for single-user; required before remote deployment |
| 14 GB database on limited disk | MEDIUM | Monitor via `/api/health` disk check; archive old data |
| CORS set to `*` | LOW | Localhost-only mitigates; restrict in production |
| innerHTML without escaping (XSS) | LOW | Localhost-only mitigates; sanitize before remote deployment |
| No automated DB backups | MEDIUM | Implement cron-based backup to external storage |
| Uploaded files not scanned | LOW | Single-user uploads only; scan before multi-user |

---

## 8. Improvement Plan

| Priority | Action | Target Date | Status |
|----------|--------|-------------|--------|
| HIGH | Add authentication (JWT) for remote access | Phase 5 | Planned |
| HIGH | Automated daily DB backup (GDrive/S3) | Q1 2026 | In Progress |
| MEDIUM | HTTPS/TLS for non-localhost deployment | Phase 5 | Planned |
| MEDIUM | Rotate API keys quarterly | Ongoing | Manual |
| MEDIUM | Restrict CORS to specific origins | Before remote deploy | Planned |
| LOW | Application-level encryption for CONFIDENTIAL data | Phase 6 | Planned |
| LOW | Sanitize innerHTML to prevent XSS | Phase 4 | Planned |

---

## 9. Input Validation

| Control | Status | Details |
|---------|--------|---------|
| API Input Validation | ✅ | Pydantic models on all endpoints |
| SQL Injection Prevention | ✅ | Parameterized queries only |
| File Upload Sanitization | ✅ | `safe_name()` function, sandboxed directory |
| Path Traversal | ✅ | File paths validated and restricted |

---

*This document is reviewed quarterly. Last review: 2026-02-19.*
