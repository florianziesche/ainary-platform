#!/bin/bash

# AI Advisory Board - Test Script

echo "🎯 AI Advisory Board - Test Runner"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Check if OPENAI_API_KEY is set
if [ -z "$OPENAI_API_KEY" ]; then
    echo "❌ OPENAI_API_KEY not set"
    echo ""
    echo "To run this tool, you need an OpenAI API key:"
    echo ""
    echo "1. Get your API key from: https://platform.openai.com/api-keys"
    echo "2. Set it in your environment:"
    echo "   export OPENAI_API_KEY='sk-...'"
    echo ""
    echo "Or create a .env file:"
    echo "   echo 'OPENAI_API_KEY=sk-...' > .env"
    echo "   source .env"
    echo ""
    exit 1
fi

echo "✅ OPENAI_API_KEY found"
echo ""

# Run the test question
echo "Running test question..."
echo ""

node board.js "Should I launch on Monday with an MVP or wait until the product is polished?"

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✅ Test complete!"
echo ""
echo "Open the generated HTML file in output/ to see the full report."
echo ""
