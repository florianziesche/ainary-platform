#!/bin/bash
# Florian Command Center — Quick Access
# Usage: ./d [command]

WORKSPACE="/Users/florianziesche/.openclaw/workspace"
cd "$WORKSPACE"

# Colors
BLUE='\033[0;34m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

case "$1" in
    # Quick Actions
    "decile"|"1")
        open job-applications/decile-capital-resident/
        open "https://jobs.lever.co/decilegroup/a483fcca-97b4-4c78-9a93-48254bac28e4/apply"
        echo -e "${GREEN}✓ Decile folder + application form opened${NC}"
        ;;
    "demo"|"2")
        open projects/cnc-planner/demo-onkel/demo.html
        echo -e "${GREEN}✓ CNC Demo opened${NC}"
        ;;
    "deck"|"3")
        open products/cnc-planner/sales/presentation-v2.html
        echo -e "${GREEN}✓ Sales Deck opened${NC}"
        ;;
    "substack"|"4")
        open content/drafts/substack/
        open "https://finitematter.substack.com/publish/post"
        echo -e "${GREEN}✓ Substack drafts + editor opened${NC}"
        ;;
    "outreach"|"5")
        open outreach/ready-to-send/
        echo -e "${GREEN}✓ Outreach folder opened${NC}"
        ;;
    "cv"|"6")
        open job-applications/cv-generator/cv-florian.html
        echo -e "${GREEN}✓ CV editor opened${NC}"
        ;;
    "linkedin"|"7")
        open content/linkedin/
        open "https://www.linkedin.com/in/florianziesche/"
        echo -e "${GREEN}✓ LinkedIn posts + profile opened${NC}"
        ;;
    
    # Documents
    "north"|"ns")
        open NORTH_STAR.md
        ;;
    "memory"|"mem")
        open MEMORY.md
        ;;
    "done"|"dod")
        open DEFINITION-OF-DONE.md
        ;;
    
    # Folders
    "jobs")
        open job-applications/
        ;;
    "products")
        open products/
        ;;
    "content")
        open content/
        ;;
    ".")
        open .
        ;;
    
    # Help / Menu
    *)
        echo ""
        echo -e "${BLUE}♔ COMMAND CENTER${NC}"
        echo -e "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
        echo ""
        echo -e "${YELLOW}QUICK ACTIONS:${NC}"
        echo "  ./d decile    [1]  → Decile Application SENDEN"
        echo "  ./d demo      [2]  → CNC Demo öffnen"
        echo "  ./d deck      [3]  → Sales Deck öffnen"
        echo "  ./d substack  [4]  → Substack Drafts + Editor"
        echo "  ./d outreach  [5]  → Outreach Emails"
        echo "  ./d cv        [6]  → CV bearbeiten"
        echo "  ./d linkedin  [7]  → LinkedIn Posts"
        echo ""
        echo -e "${YELLOW}DOCUMENTS:${NC}"
        echo "  ./d north          → NORTH_STAR.md"
        echo "  ./d memory         → MEMORY.md"
        echo "  ./d done           → DEFINITION-OF-DONE.md"
        echo ""
        echo -e "${YELLOW}FOLDERS:${NC}"
        echo "  ./d jobs           → Job Applications"
        echo "  ./d products       → Products"
        echo "  ./d content        → Content"
        echo "  ./d .              → Workspace Root"
        echo ""
        echo -e "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
        echo -e "${GREEN}Tip: ./d 1 = ./d decile${NC}"
        echo ""
        ;;
esac
