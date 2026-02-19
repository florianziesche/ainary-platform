#!/usr/bin/env python3
"""
Fix Ainary Ventures linking.
Replace both "Ainary Ventures" and "[[Ainary]] Ventures" with "[[Ainary Ventures]]"
"""
import re
from pathlib import Path

vault_path = Path("~/Library/Mobile Documents/iCloud~md~obsidian/Documents/System_OS").expanduser()

total_fixes = 0
files_changed = 0

for md_file in vault_path.rglob('*.md'):
    if '.obsidian' in md_file.parts or 'vault-index' in md_file.parts:
        continue
    
    try:
        content = md_file.read_text(encoding='utf-8')
        original = content
        
        # Replace "[[Ainary]] Ventures" with "[[Ainary Ventures]]"
        content = re.sub(r'\[\[Ainary\]\] Ventures', '[[Ainary Ventures]]', content)
        
        # Replace remaining "Ainary Ventures" (not already linked) with "[[Ainary Ventures]]"
        # But not if already in [[Ainary Ventures]]
        content = re.sub(r'(?<!\[\[)Ainary Ventures(?!\]\])', '[[Ainary Ventures]]', content)
        
        if content != original:
            # Count changes
            fixes = original.count('[[Ainary]] Ventures') + (len(re.findall(r'(?<!\[\[)Ainary Ventures(?!\]\])', original)))
            if fixes > 0:
                md_file.write_text(content, encoding='utf-8')
                files_changed += 1
                total_fixes += fixes
                print(f"✓ {md_file.relative_to(vault_path)}: {fixes} fixes")
    except Exception as e:
        print(f"✗ {md_file.relative_to(vault_path)}: {e}")

print()
print(f"Summary: {total_fixes} fixes in {files_changed} files")
