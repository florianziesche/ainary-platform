#!/usr/bin/env python3
import os
import re
from pathlib import Path
from datetime import datetime

VAULT = Path.home() / "Library/Mobile Documents/iCloud~md~obsidian/Documents/System_OS"

def extract_date_from_content(content):
    """Try to extract a date from the content"""
    # Look for dates in format YYYY-MM-DD
    date_pattern = r'20\d{2}-\d{2}-\d{2}'
    matches = re.findall(date_pattern, content)
    if matches:
        # Return the first/earliest date found
        return min(matches)
    return None

def add_created_metadata(filepath):
    """Add Created metadata to a file if missing"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if already has Created:
        if 'Created:' in content:
            return False
        
        # Try to find date in content
        found_date = extract_date_from_content(content)
        
        if found_date:
            metadata = f"\n\n*Created: {found_date} | Author: unknown*\n"
        else:
            # Use file modification time as fallback
            mtime = os.path.getmtime(filepath)
            file_date = datetime.fromtimestamp(mtime).strftime('%Y-%m-%d')
            metadata = f"\n\n*Created: ~{file_date} [estimated] | Author: unknown*\n"
        
        # Append metadata at the end
        new_content = content.rstrip() + metadata
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        return True
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False

def main():
    files_changed = 0
    total_files = 0
    
    # Find all .md files without Created:
    for md_file in VAULT.rglob("*.md"):
        if ".trash" in str(md_file):
            continue
        
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if 'Created:' not in content:
                total_files += 1
                if add_created_metadata(md_file):
                    files_changed += 1
                    print(f"Added metadata: {md_file.name}")
        except Exception as e:
            print(f"Error reading {md_file}: {e}")
    
    print(f"\nProcessed {total_files} files without Created:")
    print(f"Added metadata to {files_changed} files")

if __name__ == "__main__":
    main()
