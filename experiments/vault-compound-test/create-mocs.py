#!/usr/bin/env python3
import os
import re
from pathlib import Path
from collections import defaultdict

VAULT_PATH = "/Users/florianziesche/Library/Mobile Documents/iCloud~md~obsidian/Documents/System_OS"

# Folder names and MOC titles
FOLDER_MOCS = {
    "00_Inbox": ("Inbox", "Unsorted notes and quick captures"),
    "02_Daily": ("Daily Notes", "Daily logs and reflections"),
    "10_Projects": ("Projects", "Active and archived projects"),
    "20_Areas": ("Areas", "Areas of responsibility and focus"),
    "30_People": ("People", "Public figures, thought leaders, and media"),
    "40_People": ("Personal Network", "Business contacts and personal relationships"),
    "50_Decisions": ("Decisions", "Decision log and rationale"),
    "60_Resources": ("Resources", "Knowledge base and reference materials"),
    "70_Templates": ("Templates", "Note templates and structures"),
    "90_Archive": ("Archive", "Archived projects and notes"),
    "99_System": ("System", "Vault meta and system notes"),
}

def get_all_notes_in_folder(folder_path):
    """Get all markdown files in a folder and its subfolders"""
    notes = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.md') and not file.startswith('_') and file != '_Index.md':
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, folder_path)
                notes.append(rel_path)
    return sorted(notes)

def organize_by_subfolder(notes):
    """Organize notes by subfolder"""
    organized = defaultdict(list)
    
    for note in notes:
        parts = Path(note).parts
        if len(parts) > 1:
            subfolder = parts[0]
            organized[subfolder].append(note)
        else:
            organized['_root'].append(note)
    
    return organized

def create_moc_content(folder_name, title, description, notes):
    """Generate MOC content"""
    content = f"""---
type: moc
status: active
created: 2026-02-15
tags: [moc]
---

# {title}

{description}

**Total notes:** {len(notes)}

"""
    
    # Organize notes by subfolder
    organized = organize_by_subfolder(notes)
    
    # Add root notes first
    if '_root' in organized and organized['_root']:
        for note in organized['_root']:
            note_name = Path(note).stem
            content += f"- [[{note_name}]]\n"
        content += "\n"
    
    # Add subfolders
    for subfolder in sorted([s for s in organized.keys() if s != '_root']):
        content += f"## {subfolder}\n\n"
        for note in organized[subfolder]:
            note_name = Path(note).stem
            content += f"- [[{note_name}]]\n"
        content += "\n"
    
    return content

def create_or_update_moc(folder_path, folder_name):
    """Create or update MOC for a folder"""
    if folder_name not in FOLDER_MOCS:
        return False, "No MOC config"
    
    title, description = FOLDER_MOCS[folder_name]
    
    # Get all notes in folder
    notes = get_all_notes_in_folder(folder_path)
    
    if not notes:
        return False, "No notes in folder"
    
    # Generate MOC content
    moc_content = create_moc_content(folder_name, title, description, notes)
    
    # Write to _Index.md
    index_path = os.path.join(folder_path, "_Index.md")
    
    try:
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(moc_content)
        return True, f"Created MOC with {len(notes)} notes"
    except Exception as e:
        return False, f"Error: {str(e)}"

def main():
    """Process all numbered folders and create MOCs"""
    os.chdir(VAULT_PATH)
    
    print("Creating MOC index files...\n")
    
    created = 0
    skipped = 0
    
    for folder_name in sorted(FOLDER_MOCS.keys()):
        folder_path = os.path.join(VAULT_PATH, folder_name)
        
        if not os.path.exists(folder_path):
            print(f"⏭️  {folder_name}: Folder not found")
            skipped += 1
            continue
        
        success, message = create_or_update_moc(folder_path, folder_name)
        
        if success:
            created += 1
            print(f"✅ {folder_name}/_Index.md: {message}")
        else:
            skipped += 1
            print(f"⏭️  {folder_name}: {message}")
    
    print(f"\n📊 Summary:")
    print(f"  Created/Updated: {created}")
    print(f"  Skipped: {skipped}")
    print(f"  Total: {len(FOLDER_MOCS)}")

if __name__ == "__main__":
    main()
