#!/bin/bash
# Mia System Backup — runs daily via cron
# Backs up: workspace, memory, soul, identity, all config

BACKUP_DIR="$HOME/FZ/Backups/mia-system"
DATE=$(date +%Y-%m-%d_%H%M)
BACKUP_FILE="$BACKUP_DIR/mia-backup-$DATE.tar.gz"
WORKSPACE="$HOME/.openclaw/workspace"

# Create backup directory
mkdir -p "$BACKUP_DIR"

# Create compressed backup
tar -czf "$BACKUP_FILE" \
  -C "$HOME/.openclaw" \
  workspace/SOUL.md \
  workspace/IDENTITY.md \
  workspace/USER.md \
  workspace/MEMORY.md \
  workspace/AGENTS.md \
  workspace/TOOLS.md \
  workspace/HEARTBEAT.md \
  workspace/ACTIVE_TASK.md \
  workspace/memory/ \
  workspace/content/ \
  workspace/job-applications/ \
  workspace/products/ \
  workspace/projects/ \
  workspace/assets/ \
  workspace/scripts/ \
  workspace/experiments/ \
  2>/dev/null

# Keep only last 14 backups (2 weeks)
ls -t "$BACKUP_DIR"/mia-backup-*.tar.gz 2>/dev/null | tail -n +15 | xargs rm -f 2>/dev/null

# Report
SIZE=$(du -h "$BACKUP_FILE" 2>/dev/null | cut -f1)
COUNT=$(ls "$BACKUP_DIR"/mia-backup-*.tar.gz 2>/dev/null | wc -l | tr -d ' ')
echo "✅ Backup complete: $BACKUP_FILE ($SIZE) | $COUNT backups stored"
