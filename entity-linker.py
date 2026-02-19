#!/usr/bin/env python3
"""
Batch entity linker for Obsidian vault.
Replaces unlinked entity mentions with [[entity]] links.
Skips frontmatter, URLs, and already-linked text.
"""
import re
import sys
from pathlib import Path

def is_in_frontmatter(content, pos):
    """Check if position is within frontmatter (between --- markers)"""
    # Find first ---
    first_marker = content.find('---')
    if first_marker == -1 or pos < first_marker:
        return False
    
    # Find second ---
    second_marker = content.find('---', first_marker + 3)
    if second_marker == -1:
        return False
    
    return first_marker <= pos <= second_marker

def is_in_url(content, pos):
    """Check if position is within a URL"""
    # Look back and forward for URL patterns
    start = max(0, pos - 100)
    end = min(len(content), pos + 100)
    context = content[start:end]
    local_pos = pos - start
    
    # Check for http:// or https://
    url_pattern = r'https?://[^\s\)]+|www\.[^\s\)]+'
    for match in re.finditer(url_pattern, context):
        if match.start() <= local_pos <= match.end():
            return True
    return False

def is_already_linked(content, match_pos, entity_len):
    """Check if entity is already in [[brackets]]"""
    start = match_pos
    end = match_pos + entity_len
    
    # Check if preceded by [[
    if start >= 2 and content[start-2:start] == '[[':
        return True
    
    # Check if followed by ]]
    if end + 2 <= len(content) and content[end:end+2] == ']]':
        return True
    
    return False

def link_entity(file_path, entity, link_text=None):
    """Replace unlinked entity mentions with [[link]]"""
    if link_text is None:
        link_text = entity
    
    content = file_path.read_text(encoding='utf-8')
    original = content
    
    # Find all mentions of the entity
    pattern = re.compile(re.escape(entity), re.IGNORECASE)
    matches = list(pattern.finditer(content))
    
    # Process matches in reverse to maintain positions
    replacements = 0
    for match in reversed(matches):
        pos = match.start()
        
        # Skip if in frontmatter
        if is_in_frontmatter(content, pos):
            continue
        
        # Skip if in URL
        if is_in_url(content, pos):
            continue
        
        # Skip if already linked
        if is_already_linked(content, pos, len(entity)):
            continue
        
        # Replace with link - preserve original case
        original_text = match.group(0)
        replacement = f'[[{link_text}]]'
        content = content[:pos] + replacement + content[pos + len(original_text):]
        replacements += 1
    
    # Write back if changes were made
    if content != original:
        file_path.write_text(content, encoding='utf-8')
        return replacements
    
    return 0

def main():
    if len(sys.argv) < 3:
        print("Usage: entity-linker.py <vault_path> <entity> [link_text]")
        sys.exit(1)
    
    vault_path = Path(sys.argv[1])
    entity = sys.argv[2]
    link_text = sys.argv[3] if len(sys.argv) > 3 else entity
    
    if not vault_path.exists():
        print(f"Vault not found: {vault_path}")
        sys.exit(1)
    
    # Find all markdown files
    md_files = []
    for md_file in vault_path.rglob('*.md'):
        # Skip .obsidian and vault-index
        if '.obsidian' in md_file.parts or 'vault-index' in md_file.parts:
            continue
        md_files.append(md_file)
    
    print(f"Processing {len(md_files)} markdown files...")
    print(f"Entity: '{entity}' -> [[{link_text}]]")
    print()
    
    total_replacements = 0
    files_changed = 0
    
    for md_file in md_files:
        try:
            replacements = link_entity(md_file, entity, link_text)
            if replacements > 0:
                files_changed += 1
                total_replacements += replacements
                print(f"✓ {md_file.relative_to(vault_path)}: {replacements} links")
        except Exception as e:
            print(f"✗ {md_file.relative_to(vault_path)}: {e}")
    
    print()
    print(f"Summary: {total_replacements} links created in {files_changed} files")

if __name__ == '__main__':
    main()
