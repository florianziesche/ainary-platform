#!/bin/bash
# DepoDigest Pro - Setup Script

echo "Setting up DepoDigest Pro..."

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install anthropic

echo "Setup complete!"
echo ""
echo "To run the analyzer:"
echo "  source venv/bin/activate"
echo "  python backend/analyzer.py data/sample_depositions/martinez_deposition.txt"
echo ""
echo "To view the demo UI:"
echo "  open app/index.html"
