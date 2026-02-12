#!/bin/bash
# Pre-Flight Check — Mia muss das VOR jeder Aufgabe lesen
# Usage: ./scripts/pre-flight.sh [task-type]
# task-type: cnc | bm | vc | content | visual | general

TASK="${1:-general}"
WS="$HOME/.openclaw/workspace"
VAULT="$HOME/Library/Mobile Documents/iCloud~md~obsidian/Documents/System_OS"

echo "=== PRE-FLIGHT CHECK ==="
echo "Task: $TASK"
echo ""

# SEND-FIRST CHECK for build-related tasks (CNC, content, dashboards)
BUILD_TASKS="cnc|visual|design|dashboard"
if [[ "$TASK" =~ $BUILD_TASKS ]]; then
    echo "⚠️  BUILD-TASK DETECTED — SEND-FIRST CHECK REQUIRED ⚠️"
    echo ""
    # Run send-enforcer in silent mode (no shame)
    if [ -f "$WS/scripts/send-enforcer.sh" ]; then
        bash "$WS/scripts/send-enforcer.sh" 2>/dev/null || true
    fi
    echo ""
    echo "🛑 RULE: No building >2 features without 1 send."
    echo "   If zero sends today → SEND SOMETHING FIRST."
    echo ""
    read -p "Press ENTER to continue or Ctrl+C to send first..."
    echo ""
fi


# Always load
echo "📋 IMMER LADEN:"
echo "  - TWIN.md (Entscheidungsmodell)"
echo "  - standards/FLORIAN.md (Erwartungen)"
echo "  - standards/checklists/before-any-output.md (Checkliste)"
echo ""

# Task-specific
case $TASK in
  cnc)
    echo "🔧 CNC-TASK: Zusätzlich laden:"
    echo "  - 60_Resources/Knowledge/ (Vault — CNC-Fertigung)"
    echo "  - products/cnc-planner/ (Workspace)"
    echo "  - 30_People/ (Vault — Andreas Brand)"
    ;;
  bm|kommune)
    echo "🏛️ BM/KOMMUNE-TASK: Zusätzlich laden:"
    echo "  - 60_Resources/Knowledge/ (Vault — Kommunal-KI, Fördermittel)"
    echo "  - 30_People/ (Vault — Sven Gleißberg)"
    echo "  - projects/glashuette-ki/ (Workspace)"
    ;;
  vc)
    echo "💼 VC-TASK: Zusätzlich laden:"
    echo "  - 60_Resources/VC/ (Vault — VC Landscape)"
    echo "  - 20_Areas/Venture-Capital/ (Vault — Applications, Thesis, Fund-Research)"
    echo "  - skills/vc-application/SKILL.md (Workspace)"
    ;;
  content)
    echo "✍️ CONTENT-TASK: Zusätzlich laden:"
    echo "  - 20_Areas/Content/ (Vault — Strategy, Queue, Ideas)"
    echo "  - content/CONTENT-STRATEGY-Q1.md (Workspace)"
    ;;
  visual|design|dashboard)
    echo "🎨 VISUAL-TASK: Zusätzlich laden:"
    echo "  - standards/CORPORATE-IDENTITY.md (Workspace)"
    echo "  - BRAND-IDENTITY-SYNTHESIS.md (Workspace)"
    echo "  - research/golden-standards/ (Workspace)"
    ;;
  freelance|consulting)
    echo "💰 FREELANCE-TASK: Zusätzlich laden:"
    echo "  - 20_Areas/Freelance/ (Vault)"
    echo "  - sales/AI-CONSULTING-PLAYBOOK.md (Workspace)"
    echo "  - 30_People/ (Vault — relevante Kontakte)"
    ;;
  *)
    echo "📌 GENERAL: Nur Basis-Dateien."
    echo "  - grep -i '[keyword]' INDEX.md → relevante Dateien finden"
    ;;
esac

echo ""
echo "🔍 SUCHE: grep -i '[keyword]' $WS/INDEX.md"
echo ""
echo "⚠️ VERGISS NICHT: Output-Tracker nach Abgabe updaten!"
echo "   $WS/failures/output-tracker.md"
echo "==========================="
