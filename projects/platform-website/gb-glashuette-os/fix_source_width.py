#!/usr/bin/env python3
"""Move source sections inside the main .page div instead of being separate .page divs"""
import os, re
os.chdir(os.path.dirname(os.path.abspath(__file__)))

fixed = 0
for fname in sorted(os.listdir('.')):
    if not fname.endswith('.html'):
        continue
    with open(fname) as f:
        content = f.read()
    
    # Pattern: separate .page div for sources outside the main content
    # Replace: <div class="page" style="margin-top:0;padding-top:0">...sources...</div>
    # With just the inner div (no .page wrapper), placed before </div>\n<div id="shared-footer">
    
    old_pattern = '\n<!-- Quellenverzeichnis -->\n<div class="page" style="margin-top:0;padding-top:0">\n'
    if old_pattern not in content:
        continue
    
    # Extract the source block
    start = content.find(old_pattern)
    # Find the closing </div> of the .page wrapper (it's the one that closes the page div)
    # The structure is: <div class="page"...>\n  <div>...sources...</div>\n</div>
    # We need to find the matching closing </div>
    
    # Simpler approach: replace the wrapper
    new_content = content.replace(
        '\n<!-- Quellenverzeichnis -->\n<div class="page" style="margin-top:0;padding-top:0">\n',
        '\n<!-- Quellenverzeichnis -->\n'
    )
    # Now remove the extra closing </div> that was for the .page wrapper
    # Find where </div>\n<div id="shared-footer"> or </div>\n\n</body> is
    # The pattern after the sources is: </div>\n  </div>\n</div>\n<div id="shared-footer">
    # Should become: </div>\n  </div>\n<div id="shared-footer">
    
    # Actually let me do this differently - just add max-width styling to the source wrapper
    content2 = content.replace(
        '<div class="page" style="margin-top:0;padding-top:0">',
        '<div style="max-width:var(--page-max,820px);margin:0 auto;padding:0 var(--page-pad,48px) 48px">'
    )
    
    if content2 != content:
        with open(fname, 'w') as f:
            f.write(content2)
        fixed += 1
        print(f"  ✓ {fname}")

print(f"\nFixed {fixed} files")
