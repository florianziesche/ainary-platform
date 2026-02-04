#!/bin/bash
# Google Drive Daily Sync Script
# Syncs heavy files (images, PDFs, etc.) from local to Google Drive
# Run via cron at 23:00 CET or manually
#
# Evolution Log:
#   v1 (2026-02-03): Initial version
#   v2 (2026-02-04): Fixed subshell counter bug, added folder listing cache,
#                     added changelog auto-upload, improved error reporting

# No set -e: we handle errors per-file and want the sync to continue on partial failures

# Configuration
ACCOUNT="florian@ainaryventures.com"
CONFIG_FILE="$(dirname "$0")/gdrive-config.json"
WORKSPACE="$HOME/.openclaw/workspace"
LOG_DIR="$WORKSPACE/logs/gdrive-sync"
DATE=$(date +%Y-%m-%d)
MONTH=$(date +%Y-%m)
LOG_FILE="$LOG_DIR/$DATE.log"

# Folder IDs (from config)
PROJECTS_ID="1CfJZ9hjr58vOnQPMJyTWvfSo_dQ0Xn_3"
ASSETS_ID="1OUM8qpHiBWldQGfE0BVFb8aQohvn7YTr"
SCREENSHOTS_ID="1XUmp4hDYo_w-p9tOHiBRPnNyOhul3jy4"
CNC_PLANNER_ID="1sw0J_gj1uf8QqGzAku_GxSnvg3I5TZ3K"
DAILY_LOGS_ID="1-fkwhSyUCRB6pr7IpbygtcFEVBxvSnVu"
CHANGELOG_ID="1_AU9_YCbDKqyocmEnqQLKuau9hstlGhP"

# Create log & cache directories
mkdir -p "$LOG_DIR"
CACHE_DIR=$(mktemp -d)
trap 'rm -rf "$CACHE_DIR"' EXIT

# Counters (using temp files to survive subshells)
COUNTER_FILE="$CACHE_DIR/counters"
echo "0 0 0" > "$COUNTER_FILE"

increment_counter() {
    local field="$1"  # uploaded|skipped|errors
    local counts
    counts=$(cat "$COUNTER_FILE")
    local uploaded=$(echo "$counts" | awk '{print $1}')
    local skipped=$(echo "$counts" | awk '{print $2}')
    local errors=$(echo "$counts" | awk '{print $3}')
    case "$field" in
        uploaded) uploaded=$((uploaded + 1)) ;;
        skipped)  skipped=$((skipped + 1)) ;;
        errors)   errors=$((errors + 1)) ;;
    esac
    echo "$uploaded $skipped $errors" > "$COUNTER_FILE"
}

read_counters() {
    cat "$COUNTER_FILE"
}

# Start logging
echo "=== Google Drive Sync ===" | tee "$LOG_FILE"
echo "Date: $DATE" | tee -a "$LOG_FILE"
echo "Time: $(date +%H:%M:%S)" | tee -a "$LOG_FILE"
echo "" | tee -a "$LOG_FILE"

# Cache folder listings (one API call per folder, not per file)
cache_folder_listing() {
    local folder_id="$1"
    local cache_file="$CACHE_DIR/listing_${folder_id}"
    if [ ! -f "$cache_file" ]; then
        gog drive ls --parent "$folder_id" --account "$ACCOUNT" --plain 2>/dev/null > "$cache_file" || touch "$cache_file"
    fi
    echo "$cache_file"
}

# Function to upload file if not exists (uses cached listing)
upload_if_new() {
    local file="$1"
    local parent_id="$2"
    local filename=$(basename "$file")
    
    # Use cached listing
    local listing_file
    listing_file=$(cache_folder_listing "$parent_id")
    
    if grep -qF "$filename" "$listing_file" 2>/dev/null; then
        echo "Skipping (exists): $filename" | tee -a "$LOG_FILE"
        increment_counter skipped
    else
        echo "Uploading: $filename" | tee -a "$LOG_FILE"
        if gog drive upload "$file" --parent "$parent_id" --account "$ACCOUNT" 2>&1 | tee -a "$LOG_FILE"; then
            increment_counter uploaded
            # Invalidate cache for this folder (new file added)
            rm -f "$CACHE_DIR/listing_${parent_id}"
        else
            echo "ERROR uploading: $filename" | tee -a "$LOG_FILE"
            increment_counter errors
        fi
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

# Auto-upload changelog (was manual before)
echo "" | tee -a "$LOG_FILE"
echo "--- Changelog ---" | tee -a "$LOG_FILE"
CHANGELOG_FILE="$WORKSPACE/docs/gdrive/CHANGELOG/${MONTH}.md"
if [ -f "$CHANGELOG_FILE" ]; then
    CHANGELOG_NAME=$(basename "$CHANGELOG_FILE")
    # Always upload latest changelog (replace if exists)
    existing_id=$(gog drive ls --parent "$CHANGELOG_ID" --account "$ACCOUNT" --plain 2>/dev/null | grep -F "$CHANGELOG_NAME" | awk '{print $1}' || true)
    if [ -n "$existing_id" ]; then
        echo "Replacing changelog: $CHANGELOG_NAME (deleting old: $existing_id)" | tee -a "$LOG_FILE"
        gog drive delete "$existing_id" --account "$ACCOUNT" --force 2>/dev/null || true
    fi
    echo "Uploading changelog: $CHANGELOG_NAME" | tee -a "$LOG_FILE"
    gog drive upload "$CHANGELOG_FILE" --parent "$CHANGELOG_ID" --account "$ACCOUNT" 2>&1 | tee -a "$LOG_FILE" || true
fi

# Summary with correct counters
echo "" | tee -a "$LOG_FILE"
echo "--- Summary ---" | tee -a "$LOG_FILE"
FINAL=$(read_counters)
FINAL_UPLOADED=$(echo "$FINAL" | awk '{print $1}')
FINAL_SKIPPED=$(echo "$FINAL" | awk '{print $2}')
FINAL_ERRORS=$(echo "$FINAL" | awk '{print $3}')
echo "Uploaded: $FINAL_UPLOADED" | tee -a "$LOG_FILE"
echo "Skipped: $FINAL_SKIPPED" | tee -a "$LOG_FILE"
echo "Errors: $FINAL_ERRORS" | tee -a "$LOG_FILE"
echo "Completed: $(date +%H:%M:%S)" | tee -a "$LOG_FILE"

# Upload log to Drive
echo "" | tee -a "$LOG_FILE"
echo "Uploading sync log to Drive..." | tee -a "$LOG_FILE"
gog drive upload "$LOG_FILE" --parent "$DAILY_LOGS_ID" --account "$ACCOUNT" 2>&1 || true

echo "Done!"
