#!/bin/bash
DIR="$(cd "$(dirname "$0")" && pwd)"
DOC="$DIR/test-document.md"
OUT="$DIR/results"
mkdir -p "$OUT"

NAIVE="Summarize this meeting."

DECENT="Extract the key decisions, financial metrics, and action items from these board meeting notes. Use bullet points."

read -r -d '' EXPERT << 'EOF'
You are a board secretary preparing the official meeting minutes. Extract from these raw notes:

1. ATTENDEES: Full name, role, arrival/departure notes
2. FINANCIAL SUMMARY: All numbers mentioned (revenue, costs, margins, runway, burn rate) with context
3. KEY DECISIONS: What was decided, vote counts if any, who dissented
4. RISKS & BLOCKERS: Technical, financial, legal — with severity and deadlines
5. ACTION ITEMS: Owner, deliverable, deadline — table format
6. STRATEGIC ITEMS: Acquisition interest, pricing changes, competitive threats

Format as structured markdown. Flag any items where the notes are ambiguous with [UNCLEAR]. Include exact numbers, not approximations.
EOF

MODELS=("gpt-4o" "gpt-5.2" "gemini-2.5-flash")
MODEL_LABELS=("GPT-4o" "GPT-5.2" "Gemini-2.5-Flash")
PROMPT_LABELS=("naive" "decent" "expert")
PROMPTS=("$NAIVE" "$DECENT" "$EXPERT")

echo "🧪 Starting Prompt vs Model Benchmark"
echo "======================================"

for m_idx in 0 1 2; do
    model="${MODELS[$m_idx]}"
    model_label="${MODEL_LABELS[$m_idx]}"
    
    for p_idx in 0 1 2; do
        prompt_label="${PROMPT_LABELS[$p_idx]}"
        outfile="$OUT/${model_label}_${prompt_label}.md"
        prompt="${PROMPTS[$p_idx]}"
        
        echo ""
        echo "▶ Running: $model_label × $prompt_label"
        
        START_TIME=$(date +%s)
        
        oracle --engine api --model "$model" -p "$prompt" --file "$DOC" --force --write-output "$outfile" 2>/dev/null
        
        END_TIME=$(date +%s)
        ELAPSED=$((END_TIME - START_TIME))
        
        if [ -f "$outfile" ] && [ -s "$outfile" ]; then
            CHARS=$(wc -c < "$outfile")
            echo "  ✓ Done in ${ELAPSED}s — ${CHARS} chars"
        else
            echo "  ✗ Failed (${ELAPSED}s)"
        fi
    done
done

echo ""
echo "======================================"
echo "✅ All runs complete."
