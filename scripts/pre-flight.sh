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
    echo "  - 30-Knowledge/CNC-Fertigung.md (Vault)"
    echo "  - products/cnc-planner/ (Workspace)"
    echo "  - 40-People/Andreas-Brand.md (Vault)"
    ;;
  bm|kommune)
    echo "🏛️ BM/KOMMUNE-TASK: Zusätzlich laden:"
    echo "  - 30-Knowledge/Kommunal-KI.md (Vault)"
    echo "  - 30-Knowledge/Foerdermittel-Sachsen.md (Vault)"
    echo "  - 40-People/Sven-Gleissberg.md (Vault)"
    echo "  - projects/glashuette-ki/ (Workspace)"
    ;;
  vc)
    echo "💼 VC-TASK: Zusätzlich laden:"
    echo "  - 30-Knowledge/VC-Landscape.md (Vault)"
    echo "  - 10-Projects/VC-Career/ (Vault)"
    echo "  - skills/vc-application/SKILL.md (Workspace)"
    ;;
  content)
    echo "✍️ CONTENT-TASK: Zusätzlich laden:"
    echo "  - 30-Knowledge/Content-Strategy.md (Vault)"
    echo "  - content/CONTENT-STRATEGY-Q1.md (Workspace)"
    echo "  - 10-Projects/Content-Engine/ (Vault)"
    ;;
  visual|design|dashboard)
    echo "🎨 VISUAL-TASK: Zusätzlich laden:"
    echo "  - standards/CORPORATE-IDENTITY.md (Workspace)"
    echo "  - BRAND-IDENTITY-SYNTHESIS.md (Workspace)"
    echo "  - research/golden-standards/ (Workspace)"
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
