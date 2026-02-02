#!/bin/bash
# Google Drive Daily Sync Script
# Syncs heavy files (images, PDFs, etc.) from local to Google Drive
# Run via cron at 23:00 CET or manually

set -e

# Configuration
ACCOUNT="florian@ainaryventures.com"
CONFIG_FILE="$(dirname "$0")/gdrive-config.json"
WORKSPACE="$HOME/.openclaw/workspace"
LOG_DIR="$WORKSPACE/logs/gdrive-sync"
DATE=$(date +%Y-%m-%d)
LOG_FILE="$LOG_DIR/$DATE.log"

# Folder IDs (from config)
PROJECTS_ID="1CfJZ9hjr58vOnQPMJyTWvfSo_dQ0Xn_3"
ASSETS_ID="1OUM8qpHiBWldQGfE0BVFb8aQohvn7YTr"
SCREENSHOTS_ID="1XUmp4hDYo_w-p9tOHiBRPnNyOhul3jy4"
CNC_PLANNER_ID="1sw0J_gj1uf8QqGzAku_GxSnvg3I5TZ3K"
DAILY_LOGS_ID="1-fkwhSyUCRB6pr7IpbygtcFEVBxvSnVu"
CHANGELOG_ID="1_AU9_YCbDKqyocmEnqQLKuau9hstlGhP"

# Create log directory
mkdir -p "$LOG_DIR"

# Start logging
echo "=== Google Drive Sync ===" | tee "$LOG_FILE"
echo "Date: $DATE" | tee -a "$LOG_FILE"
echo "Time: $(date +%H:%M:%S)" | tee -a "$LOG_FILE"
echo "" | tee -a "$LOG_FILE"

# Counter for uploaded files
UPLOADED=0
SKIPPED=0
ERRORS=0

# Function to upload file if not exists
upload_if_new() {
    local file="$1"
    local parent_id="$2"
    local filename=$(basename "$file")
    
    # Check if file already exists in Drive (by name in parent)
    existing=$(gog drive ls --parent "$parent_id" --account "$ACCOUNT" --plain 2>/dev/null | grep -F "$filename" || true)
    
    if [ -z "$existing" ]; then
        echo "Uploading: $filename" | tee -a "$LOG_FILE"
        if gog drive upload "$file" --parent "$parent_id" --account "$ACCOUNT" 2>&1 | tee -a "$LOG_FILE"; then
            ((UPLOADED++))
        else
            echo "ERROR uploading: $filename" | tee -a "$LOG_FILE"
            ((ERRORS++))
        fi
    else
        echo "Skipping (exists): $filename" | tee -a "$LOG_FILE"
        ((SKIPPED++))
    fi
}

# Sync CNC Planner screenshots and demos
echo "" | tee -a "$LOG_FILE"
echo "--- CNC Planner Assets ---" | tee -a "$LOG_FILE"
if [ -d "$WORKSPACE/projects/cnc-planner" ]; then
    find "$WORKSPACE/projects/cnc-planner" -type f \( -name "*.png" -o -name "*.jpg" -o -name "*.pdf" \) 2>/dev/null | while read file; do
        upload_if_new "$file" "$CNC_PLANNER_ID"
    done
fi

# Sync workspace screenshots
echo "" | tee -a "$LOG_FILE"
echo "--- Workspace Screenshots ---" | tee -a "$LOG_FILE"
find "$WORKSPACE" -maxdepth 2 -type f \( -name "*.png" -o -name "*.jpg" \) 2>/dev/null | while read file; do
    upload_if_new "$file" "$SCREENSHOTS_ID"
done

# Sync PDFs from workspace
echo "" | tee -a "$LOG_FILE"
echo "--- Workspace PDFs ---" | tee -a "$LOG_FILE"
find "$WORKSPACE" -maxdepth 3 -type f -name "*.pdf" 2>/dev/null | while read file; do
    upload_if_new "$file" "$PROJECTS_ID"
done

# Upload this log to Drive
echo "" | tee -a "$LOG_FILE"
echo "--- Summary ---" | tee -a "$LOG_FILE"
echo "Uploaded: $UPLOADED" | tee -a "$LOG_FILE"
echo "Skipped: $SKIPPED" | tee -a "$LOG_FILE"
echo "Errors: $ERRORS" | tee -a "$LOG_FILE"
echo "Completed: $(date +%H:%M:%S)" | tee -a "$LOG_FILE"

# Upload log to Drive
echo "" | tee -a "$LOG_FILE"
echo "Uploading sync log to Drive..." | tee -a "$LOG_FILE"
gog drive upload "$LOG_FILE" --parent "$DAILY_LOGS_ID" --account "$ACCOUNT" 2>&1 || true

echo "Done!"
