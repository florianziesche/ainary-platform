#!/bin/bash
# Start local dashboard server
cd /Users/florianziesche/.openclaw/workspace
echo "🚀 Dashboard starting at http://localhost:8888"
echo "   Press Ctrl+C to stop"
echo ""
python3 -m http.server 8888
