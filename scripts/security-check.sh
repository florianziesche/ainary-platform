#!/bin/bash
# security-check.sh — Quick security health check
# Verifies critical security settings from SECURITY-FRAMEWORK.md
# Run periodically (weekly heartbeat or cron)
# Usage: ./scripts/security-check.sh [--json]

set -e
cd "$(dirname "$0")/.."

JSON_MODE=false
[ "$1" = "--json" ] && JSON_MODE=true

SCORE=0
MAX_SCORE=0
ISSUES=()
PASS=()

# --- Helper ---
check() {
    local name="$1"
    local result="$2"  # 0=pass, 1=fail, 2=warn
    local detail="$3"
    local weight="${4:-1}"
    
    MAX_SCORE=$((MAX_SCORE + weight))
    
    if [ "$result" -eq 0 ]; then
        SCORE=$((SCORE + weight))
        PASS+=("✅ $name: $detail")
    elif [ "$result" -eq 1 ]; then
        ISSUES+=("🔴 $name: $detail")
    else
        SCORE=$((SCORE + (weight / 2)))
        ISSUES+=("🟡 $name: $detail")
    fi
}

# --- Checks ---

# 1. macOS Firewall
FW_STATE=$(/usr/libexec/ApplicationFirewall/socketfilterfw --getglobalstate 2>/dev/null | grep -c "enabled" || echo "0")
FW_STATE=$(echo "$FW_STATE" | head -1 | tr -d '[:space:]')
FW_STATE=${FW_STATE:-0}
if [ "$FW_STATE" -gt 0 ]; then
    check "Firewall" 0 "Enabled" 3
else
    check "Firewall" 1 "DISABLED — run: sudo /usr/libexec/ApplicationFirewall/socketfilterfw --setglobalstate on" 3
fi

# 2. Stealth Mode
STEALTH=$(/usr/libexec/ApplicationFirewall/socketfilterfw --getstealthmode 2>/dev/null | grep -c "enabled" || echo "0")
STEALTH=$(echo "$STEALTH" | head -1 | tr -d '[:space:]')
STEALTH=${STEALTH:-0}
if [ "$STEALTH" -gt 0 ]; then
    check "Stealth Mode" 0 "Enabled" 1
else
    check "Stealth Mode" 2 "Disabled — run: sudo /usr/libexec/ApplicationFirewall/socketfilterfw --setstealthmode on" 1
fi

# 3. FileVault
FV=$(fdesetup status 2>/dev/null | grep -c "On" || echo "0")
if [ "$FV" -gt 0 ]; then
    check "FileVault" 0 "Disk encryption enabled" 3
else
    check "FileVault" 1 "DISABLED — enable in System Settings > Privacy & Security" 3
fi

# 4. SIP
SIP=$(csrutil status 2>/dev/null | grep -c "enabled" || echo "0")
if [ "$SIP" -gt 0 ]; then
    check "SIP" 0 "System Integrity Protection enabled" 2
else
    check "SIP" 1 "DISABLED — major security risk" 2
fi

# 5. Wildcard binds (services on 0.0.0.0)
WILD_COUNT=$(lsof -iTCP -sTCP:LISTEN -P -n 2>/dev/null | grep -c "\*:" || echo "0")
WILD_COUNT=$(echo "$WILD_COUNT" | head -1 | tr -d '[:space:]')
if [ "$WILD_COUNT" -le 3 ]; then
    check "Wildcard Binds" 0 "$WILD_COUNT services on 0.0.0.0 (acceptable)" 2
elif [ "$WILD_COUNT" -le 6 ]; then
    check "Wildcard Binds" 2 "$WILD_COUNT services on 0.0.0.0 — review with: lsof -iTCP -sTCP:LISTEN -P -n" 2
else
    check "Wildcard Binds" 1 "$WILD_COUNT services on 0.0.0.0 — HIGH exposure" 2
fi

# 6. OpenClaw credentials dir permissions
CRED_DIR="$HOME/.openclaw"
if [ -d "$CRED_DIR" ]; then
    PERMS=$(stat -f "%OLp" "$CRED_DIR" 2>/dev/null || echo "unknown")
    if [ "$PERMS" = "700" ]; then
        check "Credential Dir" 0 "~/.openclaw is 700 (owner-only)" 2
    else
        check "Credential Dir" 2 "~/.openclaw is $PERMS — should be 700: chmod 700 ~/.openclaw" 2
    fi
fi

# 7. Git secrets check (no API keys in tracked files)
SECRETS_FOUND=0
if command -v git &>/dev/null && [ -d .git ]; then
    # Check tracked files for common API key patterns
    SECRETS_FOUND=$(git grep -l "sk-ant-\|sk-proj-\|sk-[a-zA-Z0-9]\{20,\}\|AIza[a-zA-Z0-9_-]\{35\}" -- ':!*.md' ':!SECURITY*' 2>/dev/null | wc -l | tr -d '[:space:]' || echo "0")
fi
if [ "$SECRETS_FOUND" -eq 0 ]; then
    check "Git Secrets" 0 "No API keys in tracked files" 2
else
    check "Git Secrets" 1 "$SECRETS_FOUND files with potential API keys in git" 2
fi

# 8. macOS auto-updates
AUTO_UPD=$(defaults read /Library/Preferences/com.apple.SoftwareUpdate AutomaticCheckEnabled 2>/dev/null || echo "0")
if [ "$AUTO_UPD" = "1" ]; then
    check "Auto-Updates" 0 "macOS auto-update check enabled" 1
else
    check "Auto-Updates" 2 "Auto-update checking may be disabled" 1
fi

# --- Score ---
if [ "$MAX_SCORE" -gt 0 ]; then
    PERCENT=$((SCORE * 100 / MAX_SCORE))
else
    PERCENT=0
fi

# Status emoji
if [ "$PERCENT" -ge 80 ]; then
    STATUS="🟢"
elif [ "$PERCENT" -ge 60 ]; then
    STATUS="🟡"
elif [ "$PERCENT" -ge 40 ]; then
    STATUS="🟠"
else
    STATUS="🔴"
fi

# --- Output ---
if [ "$JSON_MODE" = true ]; then
    ISSUE_JSON=""
    for i in "${ISSUES[@]}"; do
        [ -n "$ISSUE_JSON" ] && ISSUE_JSON="$ISSUE_JSON,"
        ISSUE_JSON="$ISSUE_JSON\"$(echo "$i" | sed 's/"/\\"/g')\""
    done
    PASS_JSON=""
    for p in "${PASS[@]}"; do
        [ -n "$PASS_JSON" ] && PASS_JSON="$PASS_JSON,"
        PASS_JSON="$PASS_JSON\"$(echo "$p" | sed 's/"/\\"/g')\""
    done
    echo "{\"score\":$PERCENT,\"status\":\"$STATUS\",\"issues\":[$ISSUE_JSON],\"passed\":[$PASS_JSON]}"
else
    echo ""
    echo "🔒 SECURITY CHECK — $(date +%Y-%m-%d\ %H:%M)"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""
    echo "$STATUS Score: $PERCENT% ($SCORE/$MAX_SCORE)"
    echo ""
    
    if [ ${#PASS[@]} -gt 0 ]; then
        for p in "${PASS[@]}"; do
            echo "  $p"
        done
    fi
    
    if [ ${#ISSUES[@]} -gt 0 ]; then
        echo ""
        for i in "${ISSUES[@]}"; do
            echo "  $i"
        done
    fi
    
    echo ""
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    
    if [ "$PERCENT" -lt 60 ]; then
        echo "⚠️  Security below acceptable threshold. Fix red items."
    elif [ "$PERCENT" -lt 80 ]; then
        echo "🟡 Acceptable but could improve. Review yellow items."
    else
        echo "✅ Security posture is solid."
    fi
    echo ""
fi
