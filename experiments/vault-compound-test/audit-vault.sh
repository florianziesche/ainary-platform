#!/bin/bash

VAULT_PATH="/Users/florianziesche/Library/Mobile Documents/iCloud~md~obsidian/Documents/System_OS"
cd "$VAULT_PATH" || exit 1

echo "=== VAULT AUDIT REPORT ==="
echo "Generated: $(date)"
echo ""

# Total files
total_files=$(find . -name "*.md" | wc -l | tr -d ' ')
echo "📁 Total markdown files: $total_files"
echo ""

# Files per folder
echo "📂 Files per folder:"
for dir in $(ls -d */ 2>/dev/null | sort); do
    count=$(find "$dir" -name "*.md" | wc -l | tr -d ' ')
    echo "  $dir $count files"
done
echo ""

# Frontmatter detection
echo "📋 Frontmatter analysis:"
files_with_frontmatter=0
files_without_frontmatter=0

while IFS= read -r file; do
    if head -n 1 "$file" | grep -q "^---$"; then
        files_with_frontmatter=$((files_with_frontmatter + 1))
    else
        files_without_frontmatter=$((files_without_frontmatter + 1))
    fi
done < <(find . -name "*.md")

echo "  ✅ With frontmatter: $files_with_frontmatter"
echo "  ❌ Without frontmatter: $files_without_frontmatter"
echo ""

# Link analysis
echo "🔗 Link analysis:"
total_links=0
files_with_links=0
files_without_links=0

while IFS= read -r file; do
    link_count=$(grep -o '\[\[.*\]\]' "$file" | wc -l | tr -d ' ')
    if [ "$link_count" -gt 0 ]; then
        files_with_links=$((files_with_links + 1))
        total_links=$((total_links + link_count))
    else
        files_without_links=$((files_without_links + 1))
    fi
done < <(find . -name "*.md")

avg_links=$((total_links / total_files))
echo "  Total outgoing links: $total_links"
echo "  Files with links: $files_with_links"
echo "  Files without links: $files_without_links"
echo "  Average links per note: $avg_links"
echo ""

# People folder audit
echo "👥 People folder audit:"
people_30=$(find ./30_People/ -name "*.md" 2>/dev/null | wc -l | tr -d ' ')
people_40=$(find ./40_People/ -name "*.md" 2>/dev/null | wc -l | tr -d ' ')
echo "  30_People/: $people_30 files"
echo "  40_People/: $people_40 files"
echo ""

# Health score estimate
frontmatter_pct=$((files_with_frontmatter * 100 / total_files))
links_pct=$((files_with_links * 100 / total_files))
health_score=$(( (frontmatter_pct + links_pct) / 2 ))

echo "📊 Health Score Estimate: $health_score/100"
echo "  Frontmatter coverage: $frontmatter_pct%"
echo "  Link coverage: $links_pct%"
