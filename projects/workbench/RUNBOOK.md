# Runbook — Execution Platform (Operations)

**Version:** 1.0 | **Date:** 2026-02-19

> See also: [ARCHITECTURE.md](ARCHITECTURE.md) · [DOCUMENTATION.md](DOCUMENTATION.md) · [SECURITY.md](SECURITY.md)

---

## 1. Quick Start

```bash
# Option A: launchctl (auto-start on login)
launchctl load ~/Library/LaunchAgents/com.ainary.workbench.plist

# Option B: Manual
cd projects/workbench/backend && python3 app.py

# Health check
curl http://localhost:8080/api/health
```

**Expected health response:**
```json
{"status": "ok", "db_size_mb": ..., "disk_free_gb": ..., "uptime": ...}
```

**Access:** Open `http://localhost:8080` in any browser.

---

## 2. Restart

```bash
# Graceful restart via launchctl
launchctl kickstart -k gui/$(id -u)/com.ainary.workbench

# Hard restart (stop + start)
launchctl unload ~/Library/LaunchAgents/com.ainary.workbench.plist
launchctl load ~/Library/LaunchAgents/com.ainary.workbench.plist

# Manual restart
# Kill existing process on port 8080, then:
lsof -ti:8080 | xargs kill -9
cd projects/workbench/backend && python3 app.py
```

---

## 3. Logs

| Log | Location | Contents |
|-----|----------|----------|
| App stdout | `~/Library/Logs/com.ainary.workbench.stdout.log` | Server output, request logs |
| App stderr | `~/Library/Logs/com.ainary.workbench.stderr.log` | Errors, tracebacks |
| Events table | `workbench.db → events` | Application-level audit trail |
| Activity Feed | UI sidebar → Activity | Recent actions, visible in browser |

```bash
# Tail live logs
tail -f ~/Library/Logs/com.ainary.workbench.stdout.log

# Search for errors
grep -i "error\|traceback" ~/Library/Logs/com.ainary.workbench.stderr.log

# Query events from DB
sqlite3 backend/workbench.db "SELECT * FROM events ORDER BY created_at DESC LIMIT 20;"
```

---

## 4. Database

| Property | Value |
|----------|-------|
| Location | `projects/workbench/backend/workbench.db` |
| Engine | SQLite 3.51.2 (WAL mode) |
| Size | ~14 GB |
| Schema | See [DB-SCHEMA.md](DB-SCHEMA.md) |

### Backup

```bash
# Quick backup
cp backend/workbench.db backend/workbench.db.bak.$(date +%Y%m%d)

# Safe backup (while running — uses SQLite backup API)
sqlite3 backend/workbench.db ".backup 'backend/workbench.db.bak'"
```

### Restore

```bash
# Stop the platform first
launchctl unload ~/Library/LaunchAgents/com.ainary.workbench.plist

# Restore
cp backend/workbench.db.bak backend/workbench.db

# Restart
launchctl load ~/Library/LaunchAgents/com.ainary.workbench.plist
```

### Integrity Check

```bash
sqlite3 backend/workbench.db "PRAGMA integrity_check;"
# Expected: "ok"
```

---

## 5. Common Issues

### Port 8080 in use
```bash
lsof -ti:8080 | xargs kill -9
python3 app.py
```

### Database locked
Cause: Multiple processes accessing DB, or crashed process holding lock.
```bash
# Find processes using the DB
fuser backend/workbench.db
# Kill stale processes, then restart
```

### Disk full
The 14 GB database on limited disk can cause issues.
```bash
# Check disk space
df -h /
# Check DB size
ls -lh backend/workbench.db
# Vacuum to reclaim space
sqlite3 backend/workbench.db "VACUUM;"
```

### SIGKILL on large operations
Cause: macOS kills process due to memory pressure during large DB operations.
Fix: Close other applications, or break operations into smaller batches.

### WebSocket disconnects
Cause: Browser tab inactive, network change.
Fix: Refresh the browser. WebSocket auto-reconnects on page load.

---

## 6. Cron Jobs

| Schedule | Job | Purpose |
|----------|-----|---------|
| Login | `com.ainary.workbench.plist` | Auto-start platform via launchctl |
| (Planned) Daily | DB backup to GDrive | Automated backup |
| (Planned) Weekly | `VACUUM` on workbench.db | Reclaim disk space |

Check active cron/launchctl:
```bash
launchctl list | grep ainary
crontab -l
```

---

## 7. Monitoring

### Health Endpoint
```bash
curl -s http://localhost:8080/api/health | python3 -m json.tool
```
Returns: DB size, disk free space, uptime.

### Disk Space
```bash
df -h /  # System disk
du -sh backend/workbench.db  # DB size
```

### Process Check
```bash
pgrep -f "python3 app.py" && echo "Running" || echo "Stopped"
```

### Activity Feed
The UI sidebar shows recent events (messages, corrections, trust changes). Use for quick operational awareness.

### Key Metrics to Watch
- DB size growth (should not exceed available disk - 5 GB buffer)
- Error rate in stderr log
- Trust score trends (declining = quality issue)
- Pre-flight pass rate (target: >80%)

---

## 8. Deployment

### Current: Local Only
- macOS (Apple Silicon)
- Python 3.14.2
- Single `python3 app.py` process
- No containers, no cloud

### Future: Docker (Planned)
```dockerfile
# Planned Dockerfile structure
FROM python:3.14-slim
COPY backend/ /app/
COPY index.html /app/
WORKDIR /app
RUN pip install fastapi uvicorn httpx python-multipart
CMD ["python3", "app.py"]
```

### Future: Remote Deployment Checklist
- [ ] Add authentication (JWT/OAuth)
- [ ] Enable HTTPS/TLS
- [ ] Restrict CORS origins
- [ ] Sanitize innerHTML (XSS prevention)
- [ ] Set up automated backups
- [ ] Configure log rotation
- [ ] Add health check monitoring/alerting

---

## 9. Emergency Procedures

### DB Corruption
```bash
# 1. Stop platform
launchctl unload ~/Library/LaunchAgents/com.ainary.workbench.plist

# 2. Check integrity
sqlite3 backend/workbench.db "PRAGMA integrity_check;"

# 3a. If recoverable:
sqlite3 backend/workbench.db ".recover" | sqlite3 backend/workbench_recovered.db
mv backend/workbench_recovered.db backend/workbench.db

# 3b. If not recoverable: restore from backup
cp backend/workbench.db.bak backend/workbench.db

# 4. Restart
launchctl load ~/Library/LaunchAgents/com.ainary.workbench.plist
```

### Rollback Code Changes
```bash
# Rollback to last known good commit
git log --oneline -10  # Find the commit
git checkout <commit-hash> -- projects/workbench/backend/app.py
# Restart platform
```

### Complete Platform Reset
```bash
# Nuclear option — fresh start
git clone <repo-url> workspace-fresh
cp backend/workbench.db workspace-fresh/projects/workbench/backend/
# Point launchctl to new directory
```

### API Key Compromise
1. Immediately rotate keys at provider (OpenAI, Anthropic)
2. Update environment variables
3. Restart platform
4. See [SECURITY.md](SECURITY.md) § Incident Response

---

*This document is reviewed quarterly. Last review: 2026-02-19.*
