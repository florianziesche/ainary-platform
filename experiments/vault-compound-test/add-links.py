#!/usr/bin/env python3
import os
import re
from pathlib import Path
from collections import defaultdict

VAULT_PATH = "/Users/florianziesche/Library/Mobile Documents/iCloud~md~obsidian/Documents/System_OS"

# Priority folders
PRIORITY_FOLDERS = [
    "20_Areas",
    "10_Projects", 
    "50_Decisions",
    "30_People",
    "40_People"
]

def load_note_index():
    """Load all available notes"""
    with open('/tmp/all-notes-index.txt', 'r') as f:
        notes = [line.strip() for line in f if line.strip()]
    
    # Create a mapping of note name (without path) to full path
    note_map = {}
    for note in notes:
        name = Path(note).stem
        note_map[name] = note
    
    return notes, note_map

def extract_existing_links(content):
    """Extract all existing wiki links from content"""
    links = re.findall(r'\[\[([^\]]+)\]\]', content)
    # Handle links with aliases [[target|alias]]
    links = [link.split('|')[0] for link in links]
    return set(links)

def has_related_section(content):
    """Check if note already has a Related section"""
    return bool(re.search(r'^## Related', content, re.MULTILINE))

def get_folder_from_path(filepath):
    """Extract the top-level folder from path"""
    parts = Path(filepath).parts
    for part in parts:
        if any(part.startswith(prefix) for prefix in ["00_", "02_", "10_", "20_", "30_", "40_", "50_", "60_", "70_", "90_", "99_"]):
            return part
    return None

def find_related_notes(note_path, content, all_notes, note_map, existing_links):
    """Find related notes based on content and context"""
    related = []
    
    # Get current note's folder
    current_folder = get_folder_from_path(note_path)
    
    # Extract keywords from content (simple approach)
    content_lower = content.lower()
    words = re.findall(r'\b[a-z]{4,}\b', content_lower)
    word_freq = defaultdict(int)
    for word in words:
        word_freq[word] += 1
    
    # Get top keywords
    top_keywords = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:10]
    keywords = set([kw[0] for kw in top_keywords])
    
    # Score notes by relevance
    scored_notes = []
    
    for note in all_notes:
        if note == note_path:
            continue
        
        note_name = Path(note).stem
        
        # Skip if already linked
        if note_name in existing_links:
            continue
        
        # Skip navigation files
        if note_name in ['_NAV', '_Index']:
            continue
        
        score = 0
        
        # Same folder = +10 points
        note_folder = get_folder_from_path(note)
        if note_folder == current_folder:
            score += 10
        
        # Priority folders get bonus
        if note_folder in PRIORITY_FOLDERS:
            score += 5
        
        # Check for keyword matches in note name
        note_name_lower = note_name.lower().replace('-', ' ')
        for keyword in keywords:
            if keyword in note_name_lower:
                score += 3
        
        # MOCs are good to link to
        if 'MOC' in note_name or 'Index' in note_name:
            score += 2
        
        if score > 0:
            scored_notes.append((score, note_name, note))
    
    # Sort by score and take top 5
    scored_notes.sort(reverse=True, key=lambda x: x[0])
    related = [note[1] for note in scored_notes[:5]]
    
    return related

def add_related_section(filepath, content, related_notes):
    """Add a Related section to the note"""
    if not related_notes:
        return False, "No related notes found"
    
    if has_related_section(content):
        return False, "Already has Related section"
    
    # Add Related section at the end
    related_section = "\n\n## Related\n"
    for note in related_notes:
        related_section += f"- [[{note}]]\n"
    
    new_content = content.rstrip() + related_section
    
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True, f"Added {len(related_notes)} links"
    except Exception as e:
        return False, f"Error: {str(e)}"

def is_priority_note(note_path):
    """Check if note is in a priority folder"""
    folder = get_folder_from_path(note_path)
    return folder in PRIORITY_FOLDERS

def main():
    """Process priority notes and add links"""
    os.chdir(VAULT_PATH)
    
    # Load note index
    all_notes, note_map = load_note_index()
    print(f"Loaded index of {len(all_notes)} notes\n")
    
    # Get list of notes without links
    with open('/tmp/files-without-links.txt', 'r') as f:
        files_without_links = [line.strip().lstrip('./') for line in f if line.strip()]
    
    # Also process all priority folder notes (even if they have some links)
    priority_notes = []
    for note in all_notes:
        if is_priority_note(note) and not note.endswith('_NAV'):
            priority_notes.append(note)
    
    # Combine and deduplicate
    notes_to_process = list(set(files_without_links + priority_notes))
    
    # Sort by priority
    notes_to_process.sort(key=lambda x: (not is_priority_note(x), x))
    
    print(f"Processing {len(notes_to_process)} notes (prioritizing {len(priority_notes)} priority notes)...\n")
    
    modified = 0
    skipped = 0
    limit = 100  # Process top 100
    
    for i, note_path in enumerate(notes_to_process[:limit]):
        # Ensure .md extension
        if not note_path.endswith('.md'):
            note_path = note_path + '.md'
        full_path = os.path.join(VAULT_PATH, note_path) if not note_path.startswith('/') else note_path
        
        try:
            with open(full_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Skip if empty or too short
            if len(content) < 50:
                skipped += 1
                continue
            
            # Extract existing links
            existing_links = extract_existing_links(content)
            
            # Find related notes
            related = find_related_notes(note_path, content, all_notes, note_map, existing_links)
            
            # Add related section
            success, message = add_related_section(full_path, content, related)
            
            if success:
                modified += 1
                print(f"✅ {note_path}: {message}")
            else:
                skipped += 1
                # print(f"⏭️  {note_path}: {message}")
        
        except Exception as e:
            skipped += 1
            print(f"❌ {note_path}: Error - {str(e)}")
    
    print(f"\n📊 Summary:")
    print(f"  Modified: {modified}")
    print(f"  Skipped: {skipped}")
    print(f"  Total processed: {min(limit, len(notes_to_process))}")

if __name__ == "__main__":
    main()
