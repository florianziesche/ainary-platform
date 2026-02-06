#!/usr/bin/env zsh
# board-consult.sh — Get multi-perspective advice from AI Board of Advisors
# Outputs formatted prompts for sessions_spawn.
#
# Usage:
#   ./scripts/board-consult.sh list                  — Show all advisors
#   ./scripts/board-consult.sh prompt "Your question" — Generate full board prompt
#   ./scripts/board-consult.sh marc "Your question"   — Single advisor prompt
#
# Advisors: marc, munger, thiel, hoffman, elad

set -e
cd "$(dirname "$0")/.."

BOLD='\033[1m'
CYAN='\033[0;36m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

# --- Advisor Definitions (zsh associative arrays) ---
typeset -A ADVISOR_NAME ADVISOR_LENS ADVISOR_TONE ADVISOR_QUESTION

ADVISOR_NAME[marc]="Marc Andreessen"
ADVISOR_LENS[marc]="Technology vision, market timing, contrarian bets. 'Software is eating the world.'"
ADVISOR_TONE[marc]="Confident, data-driven, long blog posts. References history. Bullish on technology. Dismissive of regulation. Uses specific examples and frameworks."
ADVISOR_QUESTION[marc]="Why now? What changed in the technology that makes this possible TODAY?"

ADVISOR_NAME[munger]="Charlie Munger"
ADVISOR_LENS[munger]="Risk assessment, second-order thinking, avoiding stupidity. Mental models from biology, physics, psychology."
ADVISOR_TONE[munger]="Dry wit, blunt, grandfatherly wisdom. Loves inversion. References Berkshire history. 'All I want to know is where I'm going to die, so I'll never go there.'"
ADVISOR_QUESTION[munger]="Invert, always invert. How could this FAIL? What's the base rate for ventures like this?"

ADVISOR_NAME[thiel]="Peter Thiel"
ADVISOR_LENS[thiel]="Zero-to-one thinking, monopoly dynamics, hidden truths, definite optimism."
ADVISOR_TONE[thiel]="Philosophical, contrarian, provokes with questions. References Girard, Strauss. Dislikes incrementalism. 'Competition is for losers.'"
ADVISOR_QUESTION[thiel]="What important truth do very few people agree with you on? Is this 0→1 or 1→n?"

ADVISOR_NAME[hoffman]="Reid Hoffman"
ADVISOR_LENS[hoffman]="Network effects, blitzscaling, strategic alliances, platform dynamics."
ADVISOR_TONE[hoffman]="Warm but strategic. Thinks in networks and systems. References LinkedIn scaling, Greylock portfolio. Collaborative tone."
ADVISOR_QUESTION[hoffman]="What's the network effect? How does this get BETTER with more users?"

ADVISOR_NAME[elad]="Elad Gil"
ADVISOR_LENS[elad]="Operational scaling, hiring, what breaks at each growth stage. The High Growth Handbook."
ADVISOR_TONE[elad]="Practical, operator-minded, structured. Thinks in checklists and playbooks. References Color Genomics, Google, Twitter scaling."
ADVISOR_QUESTION[elad]="What breaks when this 10x's? Have you solved the scaling bottleneck before it hits?"

ADVISORS=(marc munger thiel hoffman elad)

# --- Functions ---
show_list() {
    echo ""
    echo -e "${BOLD}🏛️ AINARY VENTURES — Board of Advisors${NC}"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    for key in "${ADVISORS[@]}"; do
        echo -e "  ${GREEN}$key${NC} — ${BOLD}${ADVISOR_NAME[$key]}${NC}"
        echo -e "    Lens: ${ADVISOR_LENS[$key]}"
        echo ""
    done
    echo -e "Usage: ${CYAN}./scripts/board-consult.sh prompt \"Your question\"${NC}"
    echo -e "       ${CYAN}./scripts/board-consult.sh marc \"Your question\"${NC}"
    echo ""
}

generate_advisor_prompt() {
    local key="$1"
    local question="$2"
    
    cat <<EOF
You are ${ADVISOR_NAME[$key]}, serving on the Advisory Board of Ainary Ventures (an emerging AI-focused VC fund being built by Florian Ziesche, a former startup CEO with deep AI expertise, currently based in Germany).

YOUR IDENTITY:
- Name: ${ADVISOR_NAME[$key]}
- Lens: ${ADVISOR_LENS[$key]}
- Tone: ${ADVISOR_TONE[$key]}
- Your signature question: "${ADVISOR_QUESTION[$key]}"

CONTEXT ABOUT AINARY VENTURES:
- Thesis: AI-first startups, vertical AI, founder-operator advantage
- Stage: Pre-fund, building track record and network
- Florian's edge: 5 years founder/CEO, raised €5.5M+, deep LLM/RAG/agent expertise
- Current projects: CNC Planer Pro (manufacturing AI), AI consulting for German Mittelstand, VC Lab program
- Financial reality: ~€70K debt, needs €6K/month, targeting €500K revenue ASAP

INSTRUCTIONS:
- Stay completely in character as ${ADVISOR_NAME[$key]}
- Apply YOUR specific frameworks and mental models
- Be direct and opinionated — this is a board meeting, not a therapy session
- If you disagree with the premise, say so
- End with your signature question applied to this specific situation
- Keep it to 300-500 words — board time is expensive

THE QUESTION:
$question
EOF
}

generate_full_board_prompt() {
    local question="$1"
    
    cat <<EOF
You are moderating an Advisory Board meeting for Ainary Ventures. Present the following question to ALL five advisors and synthesize their responses.

THE BOARD:
1. Marc Andreessen — Technology vision, market timing, "Why now?"
2. Charlie Munger — Risk assessment, inversion, "How could this fail?"
3. Peter Thiel — Zero-to-one thinking, "What truth do few agree with?"
4. Reid Hoffman — Network effects, blitzscaling, "What's the network effect?"
5. Elad Gil — Operational scaling, "What breaks at 10x?"

CONTEXT ABOUT AINARY VENTURES:
- AI-focused emerging VC fund by Florian Ziesche (ex-startup CEO, €5.5M+ raised)
- Thesis: AI-first startups, vertical AI, founder-operator advantage
- Current: CNC Planer Pro, AI consulting for German Mittelstand, VC Lab program
- Financial: ~€70K debt, needs €6K/month, targeting €500K revenue

INSTRUCTIONS:
1. Each advisor speaks IN CHARACTER (200-300 words each)
2. They MUST disagree where appropriate — consensus is suspicious
3. After all five, write a "BOARD SYNTHESIS" section:
   - Points of agreement
   - Key disagreements
   - The ONE thing they'd all insist on
4. End with: "The board recommends: [specific action]"

THE QUESTION FOR THE BOARD:
$question
EOF
}

# --- Main ---
ACTION="${1:-list}"
QUESTION="${2:-}"

case "$ACTION" in
    list)
        show_list
        ;;
    prompt)
        if [ -z "$QUESTION" ]; then
            echo "❌ Usage: ./scripts/board-consult.sh prompt \"Your question for the full board\""
            exit 1
        fi
        echo ""
        echo -e "${BOLD}🏛️ Full Board Prompt Generated${NC}"
        echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
        echo ""
        generate_full_board_prompt "$QUESTION"
        echo ""
        echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
        echo -e "${CYAN}→ Copy the above and use with sessions_spawn task parameter${NC}"
        echo -e "${CYAN}→ Or pipe: ./scripts/board-consult.sh prompt \"Q\" | pbcopy${NC}"
        ;;
    marc|munger|thiel|hoffman|elad)
        if [ -z "$QUESTION" ]; then
            echo "❌ Usage: ./scripts/board-consult.sh $ACTION \"Your question\""
            exit 1
        fi
        echo ""
        echo -e "${BOLD}🪑 ${ADVISOR_NAME[$ACTION]} — Advisory Prompt${NC}"
        echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
        echo ""
        generate_advisor_prompt "$ACTION" "$QUESTION"
        echo ""
        echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
        echo -e "${CYAN}→ Use with sessions_spawn or paste into any LLM${NC}"
        ;;
    *)
        echo "❌ Unknown action: $ACTION"
        echo "   Use: list, prompt, marc, munger, thiel, hoffman, elad"
        exit 1
        ;;
esac
