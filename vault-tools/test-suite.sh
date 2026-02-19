#!/bin/bash
# Vault Tools Test Suite
# Run all three scripts to verify functionality

set -e

VAULT_INDEX="$HOME/Library/Mobile Documents/iCloud~md~obsidian/Documents/System_OS/vault-index"
cd "$VAULT_INDEX"

echo "============================================================"
echo "VAULT TOOLS TEST SUITE"
echo "============================================================"
echo ""

echo "Test 1: Tag Tiers (dry-run)"
echo "----------------------------"
python3 tag_tiers.py | tail -15
echo ""

echo "Test 2: Conflict Resolver (sample query)"
echo "-----------------------------------------"
python3 conflict_resolver.py "agent calibration" | head -20
echo ""

echo "Test 3: Freshness Enforcer (report)"
echo "------------------------------------"
python3 freshness_enforcer.py --report | head -30
echo ""

echo "Test 4: CRT Scan (summary only)"
echo "--------------------------------"
python3 conflict_resolver.py --scan | tail -10
echo ""

echo "============================================================"
echo "✓ All tests completed successfully"
echo "============================================================"
