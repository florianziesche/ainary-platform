#!/usr/bin/env python3
import os
import re
from pathlib import Path

VAULT = Path.home() / "Library/Mobile Documents/iCloud~md~obsidian/Documents/System_OS"

def fix_wikilinks(content):
    """Replace [[path/filename]] with [[filename]] and [[path/filename|alias]] with [[filename|alias]]"""
    
    # Skip absolute file paths (Users/..., Raw-Captures/...)
    # Only fix Obsidian-style wikilinks
    
    lines = content.split('\n')
    fixed_lines = []
    
    for line in lines:
        # Find all wikilinks in the line
        # Pattern: [[...]]
        def fix_link(match):
            link_content = match.group(1)
            
            # Skip if it's a URL
            if 'http://' in link_content or 'https://' in link_content:
                return match.group(0)
            
            # Skip absolute paths (starting with Users/ or Raw-Captures/)
            if link_content.startswith('Users/') or link_content.startswith('Raw-Captures/'):
                return match.group(0)
            
            # Skip example formats in documentation
            if link_content == 'to/file|Display Text' or link_content == 'path/to/file|Display Text':
                return match.group(0)
            
            # Check if there's a path separator
            if '/' not in link_content:
                return match.group(0)  # Nothing to fix
            
            # Split by | to separate link from alias
            if '|' in link_content:
                link_part, alias_part = link_content.split('|', 1)
            else:
                link_part = link_content
                alias_part = None
            
            # Remove path, keep only filename
            # Handle both "path/file" and "path/"
            if link_part.endswith('/'):
                # Case: [[path/|alias]] or [[path/]]
                # Extract the folder name as filename
                parts = link_part.rstrip('/').split('/')
                filename = parts[-1] if parts else link_part
            else:
                # Case: [[path/file]] or [[path/file|alias]]
                parts = link_part.split('/')
                filename = parts[-1]
            
            # Reconstruct the link
            if alias_part:
                return f"[[{filename}|{alias_part}]]"
            else:
                return f"[[{filename}]]"
        
        # Apply regex to find and fix all wikilinks in the line
        fixed_line = re.sub(r'\[\[([^\]]+)\]\]', fix_link, line)
        fixed_lines.append(fixed_line)
    
    return '\n'.join(fixed_lines)

def process_file(filepath):
    """Process a single markdown file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = fix_wikilinks(content)
        
        # Only write if something changed
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
    return False

def main():
    files_changed = 0
    total_files = 0
    
    # Find all .md files
    for md_file in VAULT.rglob("*.md"):
        if ".trash" in str(md_file):
            continue
        
        total_files += 1
        if process_file(md_file):
            files_changed += 1
            print(f"Fixed: {md_file.name}")
    
    print(f"\nProcessed {total_files} files")
    print(f"Changed {files_changed} files")

if __name__ == "__main__":
    main()
