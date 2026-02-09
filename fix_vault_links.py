#!/usr/bin/env python3
import os
import re
from pathlib import Path

VAULT = Path.home() / "Library/Mobile Documents/iCloud~md~obsidian/Documents/System_OS"

def fix_wikilinks(content):
    """Replace [[path/filename]] with [[filename]] and [[path/filename|alias]] with [[filename|alias]]"""
    # Pattern to match [[path/file]] or [[path/file|alias]]
    # But exclude http:// and https://
    pattern = r'\[\[(?!https?://)(.*?/)(.*?)(\|.*?)?\]\]'
    
    def replace_link(match):
        # match.group(1) = path/ (wird entfernt)
        # match.group(2) = filename
        # match.group(3) = |alias (optional)
        filename = match.group(2)
        alias = match.group(3) if match.group(3) else ""
        return f"[[{filename}{alias}]]"
    
    return re.sub(pattern, replace_link, content)

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
    
    print(f"Processed {total_files} files")
    print(f"Changed {files_changed} files")

if __name__ == "__main__":
    main()
