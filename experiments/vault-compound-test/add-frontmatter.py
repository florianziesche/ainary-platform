#!/usr/bin/env python3
import os
import re
from datetime import datetime
from pathlib import Path

VAULT_PATH = "/Users/florianziesche/Library/Mobile Documents/iCloud~md~obsidian/Documents/System_OS"

# Folder to type mapping
FOLDER_TYPE_MAP = {
    "00_Inbox": ("note", "stub"),
    "02_Daily": ("daily", "active"),
    "10_Projects": ("project", "active"),
    "20_Areas": ("note", "active"),
    "30_People": ("person", "active"),
    "40_People": ("person", "active"),
    "50_Decisions": ("decision", "active"),
    "60_Resources": ("note", "active"),
    "70_Templates": ("template", "active"),
    "90_Archive": ("note", "archive"),
    "99_System": ("note", "active"),
}

def has_frontmatter(content):
    """Check if file starts with frontmatter"""
    return content.startswith("---\n") or content.startswith("---\r\n")

def get_folder_from_path(filepath):
    """Extract the top-level folder name from path"""
    parts = Path(filepath).parts
    for part in parts:
        if part.startswith(("00_", "02_", "10_", "20_", "30_", "40_", "50_", "60_", "70_", "90_", "99_")):
            return part
    return None

def detect_type_from_content(content, folder):
    """Detect note type from content if possible"""
    default_type, default_status = FOLDER_TYPE_MAP.get(folder, ("note", "active"))
    
    # Check for MOC indicators
    if "MOC" in content or "_Index" in content or "# Index" in content:
        return "moc", default_status
    
    return default_type, default_status

def create_frontmatter(note_type, status, created_date, tags=None):
    """Generate frontmatter block"""
    if tags is None:
        tags = []
    
    fm = "---\n"
    fm += f"type: {note_type}\n"
    fm += f"status: {status}\n"
    fm += f"created: {created_date}\n"
    fm += f"tags: [{', '.join(tags)}]\n"
    fm += "---\n\n"
    return fm

def process_file(filepath):
    """Add frontmatter to a file if missing"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if has_frontmatter(content):
            return False, "Already has frontmatter"
        
        folder = get_folder_from_path(filepath)
        if not folder:
            return False, "Could not determine folder"
        
        note_type, status = detect_type_from_content(content, folder)
        
        # Use file creation date if available, otherwise today
        created_date = "2026-02-15"  # Default to today
        try:
            stat = os.stat(filepath)
            created_dt = datetime.fromtimestamp(stat.st_birthtime)
            created_date = created_dt.strftime("%Y-%m-%d")
        except:
            pass
        
        frontmatter = create_frontmatter(note_type, status, created_date)
        new_content = frontmatter + content
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        return True, f"Added {note_type}/{status} frontmatter"
    
    except Exception as e:
        return False, f"Error: {str(e)}"

def main():
    """Process all files without frontmatter"""
    os.chdir(VAULT_PATH)
    
    # Read list of files without frontmatter
    with open('/tmp/files-without-frontmatter.txt', 'r') as f:
        files = [line.strip() for line in f if line.strip()]
    
    print(f"Processing {len(files)} files...")
    
    modified = 0
    skipped = 0
    
    for filepath in files:
        full_path = os.path.join(VAULT_PATH, filepath.lstrip('./'))
        success, message = process_file(full_path)
        
        if success:
            modified += 1
            print(f"✅ {filepath}: {message}")
        else:
            skipped += 1
            print(f"⏭️  {filepath}: {message}")
    
    print(f"\n📊 Summary:")
    print(f"  Modified: {modified}")
    print(f"  Skipped: {skipped}")
    print(f"  Total: {len(files)}")

if __name__ == "__main__":
    main()
