#!/bin/bash
# CNC Planer Pro — Sales Deck Tool
# Usage:
#   ./deck-tool.sh open          Open in browser for preview
#   ./deck-tool.sh pdf           Export to PDF
#   ./deck-tool.sh edit          Interactive edit mode
#   ./deck-tool.sh set KEY VALUE Update a specific field
#   ./deck-tool.sh list          List all editable fields
#   ./deck-tool.sh backup        Create timestamped backup

set -euo pipefail

DECK_DIR="$(cd "$(dirname "$0")" && pwd)"
HTML_FILE="$DECK_DIR/presentation-v4-updated.html"
PDF_FILE="$DECK_DIR/presentation-v4-updated.pdf"
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
BACKUP_DIR="$DECK_DIR/backups"

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
BOLD='\033[1m'
NC='\033[0m'

header() {
    echo ""
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${BOLD}  CNC Planer Pro — Deck Tool${NC}"
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
}

cmd_open() {
    echo -e "${GREEN}Opening presentation in browser...${NC}"
    open "$HTML_FILE"
}

cmd_pdf() {
    echo -e "${YELLOW}Generating PDF...${NC}"
    
    "$CHROME" \
        --headless=new \
        --disable-gpu \
        --no-sandbox \
        --print-to-pdf="$PDF_FILE" \
        --print-to-pdf-no-header \
        --no-pdf-header-footer \
        "file://$HTML_FILE" 2>/dev/null
    
    if [ -f "$PDF_FILE" ]; then
        SIZE=$(du -h "$PDF_FILE" | cut -f1)
        PAGES=$(python3 -c "
import subprocess
result = subprocess.run(['mdls', '-name', 'kMDItemNumberOfPages', '$PDF_FILE'], capture_output=True, text=True)
print(result.stdout.split('=')[-1].strip())
" 2>/dev/null || echo "?")
        echo -e "${GREEN}✓ PDF saved: $PDF_FILE ($SIZE, $PAGES pages)${NC}"
        open "$PDF_FILE"
    else
        echo -e "${RED}✗ PDF generation failed${NC}"
        exit 1
    fi
}

cmd_backup() {
    mkdir -p "$BACKUP_DIR"
    TIMESTAMP=$(date +%Y%m%d-%H%M%S)
    cp "$HTML_FILE" "$BACKUP_DIR/presentation-v4-$TIMESTAMP.html"
    echo -e "${GREEN}✓ Backup saved: backups/presentation-v4-$TIMESTAMP.html${NC}"
}

cmd_list() {
    header
    echo ""
    echo -e "${BOLD}Editable Fields:${NC}"
    echo ""
    echo -e "  ${BOLD}slide1-title${NC}      Cover title"
    echo -e "  ${BOLD}slide1-subtitle${NC}   Cover subtitle"
    echo -e "  ${BOLD}slide2-number${NC}     Problem big number (e.g., 10,3h)"
    echo -e "  ${BOLD}slide2-label${NC}      Problem label"
    echo -e "  ${BOLD}slide4-avg${NC}        Validation average (e.g., +9,8%)"
    echo -e "  ${BOLD}slide4-parts${NC}      Number of parts"
    echo -e "  ${BOLD}slide4-total${NC}      Total pieces"
    echo -e "  ${BOLD}slide7-example-calcs${NC}  ROI example: calcs/month"
    echo -e "  ${BOLD}slide7-example-mins${NC}   ROI example: mins/calc"
    echo -e "  ${BOLD}slide7-example-rate${NC}   ROI example: hourly rate"
    echo -e "  ${BOLD}slide8-price1${NC}     Starter price"
    echo -e "  ${BOLD}slide8-price2${NC}     Professional price"
    echo -e "  ${BOLD}slide8-setup${NC}      Setup fee"
    echo -e "  ${BOLD}contact-name${NC}      Contact name"
    echo -e "  ${BOLD}contact-email${NC}     Contact email"
    echo -e "  ${BOLD}contact-phone${NC}     Contact phone"
    echo -e "  ${BOLD}date${NC}              Deck date"
    echo ""
    echo -e "  Usage: ${BLUE}./deck-tool.sh set slide8-price1 '€ 199'${NC}"
    echo ""
}

cmd_set() {
    local KEY="${1:-}"
    local VALUE="${2:-}"
    
    if [ -z "$KEY" ] || [ -z "$VALUE" ]; then
        echo -e "${RED}Usage: ./deck-tool.sh set KEY VALUE${NC}"
        echo "Run './deck-tool.sh list' to see available keys."
        exit 1
    fi
    
    cmd_backup
    
    case "$KEY" in
        contact-name)
            sed -i '' "s|<div style=\"font-size: 20px; font-weight: 600; color: white;\">.*</div>|<div style=\"font-size: 20px; font-weight: 600; color: white;\">$VALUE</div>|" "$HTML_FILE"
            ;;
        contact-email)
            sed -i '' "s|florian@ziesche.co|$VALUE|g" "$HTML_FILE"
            ;;
        contact-phone)
            sed -i '' "s|+1 347 740 1465|$VALUE|g" "$HTML_FILE"
            ;;
        date)
            sed -i '' "s|6\. Februar 2026|$VALUE|g" "$HTML_FILE"
            sed -i '' "s|06\.02\.2026|$(echo "$VALUE" | sed 's/ //g')|g" "$HTML_FILE"
            ;;
        slide8-price1)
            sed -i '' "/<div class=\"price-tier\">Starter/,/<div class=\"price-amount\">/{s|<div class=\"price-amount\">.*</div>|<div class=\"price-amount\">$VALUE</div>|};" "$HTML_FILE"
            ;;
        slide8-price2)
            sed -i '' "/<div class=\"price-tier\">Professional/,/<div class=\"price-amount\">/{s|<div class=\"price-amount\">.*</div>|<div class=\"price-amount\">$VALUE</div>|};" "$HTML_FILE"
            ;;
        *)
            echo -e "${RED}Unknown key: $KEY${NC}"
            echo "Run './deck-tool.sh list' to see available keys."
            exit 1
            ;;
    esac
    
    echo -e "${GREEN}✓ Updated $KEY → $VALUE${NC}"
}

cmd_edit() {
    header
    echo ""
    echo -e "${BOLD}Interactive Edit Mode${NC}"
    echo -e "Type field=value to change, 'list' for fields, 'pdf' to export, 'open' to preview, 'q' to quit"
    echo ""
    
    while true; do
        echo -ne "${BLUE}deck>${NC} "
        read -r INPUT
        
        case "$INPUT" in
            q|quit|exit)
                echo -e "${GREEN}Done.${NC}"
                break
                ;;
            list)
                cmd_list
                ;;
            pdf)
                cmd_pdf
                ;;
            open)
                cmd_open
                ;;
            backup)
                cmd_backup
                ;;
            *=*)
                KEY="${INPUT%%=*}"
                VALUE="${INPUT#*=}"
                KEY=$(echo "$KEY" | xargs)
                VALUE=$(echo "$VALUE" | xargs)
                cmd_set "$KEY" "$VALUE"
                ;;
            "")
                continue
                ;;
            *)
                echo -e "${YELLOW}Use field=value format. Type 'list' for fields.${NC}"
                ;;
        esac
    done
}

cmd_slide() {
    local SLIDE_NUM="${1:-}"
    if [ -z "$SLIDE_NUM" ]; then
        echo -e "${RED}Usage: ./deck-tool.sh slide NUMBER${NC}"
        exit 1
    fi
    
    echo -e "${BOLD}Slide $SLIDE_NUM content:${NC}"
    echo ""
    # Extract slide content between SLIDE N markers
    sed -n "/SLIDE $SLIDE_NUM:/,/SLIDE $((SLIDE_NUM + 1)):/p" "$HTML_FILE" | \
        grep -E 'slide-title|slide-subtitle|slide-label|big-number|metric-value|card-title|price-amount|cta-title|validation-number' | \
        sed 's/<[^>]*>//g; s/^[[:space:]]*/  /' | \
        grep -v '^[[:space:]]*$'
    echo ""
}

# Main
case "${1:-help}" in
    open)    cmd_open ;;
    pdf)     cmd_pdf ;;
    edit)    cmd_edit ;;
    set)     cmd_set "${2:-}" "${3:-}" ;;
    list)    cmd_list ;;
    backup)  cmd_backup ;;
    slide)   cmd_slide "${2:-}" ;;
    help|*)
        header
        echo ""
        echo -e "  ${BOLD}Commands:${NC}"
        echo -e "    ${GREEN}open${NC}              Preview in browser"
        echo -e "    ${GREEN}pdf${NC}               Export to PDF & open"
        echo -e "    ${GREEN}edit${NC}              Interactive edit mode"
        echo -e "    ${GREEN}set KEY VALUE${NC}     Update a field"
        echo -e "    ${GREEN}list${NC}              Show editable fields"
        echo -e "    ${GREEN}slide N${NC}           Show slide N content"
        echo -e "    ${GREEN}backup${NC}            Create timestamped backup"
        echo ""
        echo -e "  ${BOLD}Quick PDF:${NC} ./deck-tool.sh pdf"
        echo -e "  ${BOLD}Edit mode:${NC} ./deck-tool.sh edit"
        echo ""
        ;;
esac
