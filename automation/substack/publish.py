#!/usr/bin/env python3
"""
Publish a Substack article from Markdown.
Usage: python3 publish.py <markdown_file> [--draft]

Requires: SUBSTACK_COOKIES_STRING or SUBSTACK_EMAIL + SUBSTACK_PASSWORD in .env
"""

import os
import sys
import re
from dotenv import load_dotenv
from substack import Api
from substack.post import Post

load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

PUBLICATION_URL = "https://finitematter.substack.com"


def markdown_to_substack(md_content):
    """Convert markdown to Substack post blocks."""
    lines = md_content.strip().split('\n')
    blocks = []
    
    # Skip YAML-like front matter
    in_front_matter = False
    content_lines = []
    for line in lines:
        if line.strip() == '---':
            in_front_matter = not in_front_matter
            continue
        if not in_front_matter:
            content_lines.append(line)
    
    # Parse title and subtitle from first lines
    title = ""
    subtitle = ""
    body_start = 0
    
    for i, line in enumerate(content_lines):
        if line.startswith('# ') and not title:
            title = line[2:].strip()
            body_start = i + 1
            continue
        if line.startswith('**Subject Line'):
            continue
        if line.startswith('**Subtitle:'):
            subtitle = line.replace('**Subtitle:**', '').strip()
            body_start = i + 1
            continue
        if line.startswith('**Preview Text'):
            body_start = i + 1
            continue
        if line.strip() and not line.startswith('**') and not line.startswith('*') and body_start <= i:
            break
    
    # Build body content
    paragraph_buffer = []
    
    for line in content_lines[body_start:]:
        line = line.rstrip()
        
        # Skip metadata lines
        if line.startswith('**Subject Line') or line.startswith('**Subtitle') or line.startswith('**Preview'):
            continue
            
        # Heading
        if line.startswith('## '):
            if paragraph_buffer:
                blocks.append({'type': 'paragraph', 'content': ' '.join(paragraph_buffer)})
                paragraph_buffer = []
            blocks.append({'type': 'heading', 'level': 2, 'content': line[3:].strip()})
            continue
        
        if line.startswith('### '):
            if paragraph_buffer:
                blocks.append({'type': 'paragraph', 'content': ' '.join(paragraph_buffer)})
                paragraph_buffer = []
            blocks.append({'type': 'heading', 'level': 3, 'content': line[4:].strip()})
            continue
        
        # Horizontal rule
        if line.strip() == '---':
            if paragraph_buffer:
                blocks.append({'type': 'paragraph', 'content': ' '.join(paragraph_buffer)})
                paragraph_buffer = []
            blocks.append({'type': 'horizontalRule'})
            continue
        
        # Blockquote
        if line.startswith('> '):
            if paragraph_buffer:
                blocks.append({'type': 'paragraph', 'content': ' '.join(paragraph_buffer)})
                paragraph_buffer = []
            blocks.append({'type': 'blockquote', 'content': line[2:].strip()})
            continue
        
        # List item
        if line.startswith('- **') or line.startswith('- '):
            if paragraph_buffer:
                blocks.append({'type': 'paragraph', 'content': ' '.join(paragraph_buffer)})
                paragraph_buffer = []
            content = line[2:].strip()
            blocks.append({'type': 'listItem', 'content': content})
            continue
        
        # Empty line = paragraph break
        if not line.strip():
            if paragraph_buffer:
                blocks.append({'type': 'paragraph', 'content': ' '.join(paragraph_buffer)})
                paragraph_buffer = []
            continue
        
        # Regular text
        paragraph_buffer.append(line)
    
    if paragraph_buffer:
        blocks.append({'type': 'paragraph', 'content': ' '.join(paragraph_buffer)})
    
    return title, subtitle, blocks


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 publish.py <markdown_file> [--draft]")
        sys.exit(1)
    
    md_file = sys.argv[1]
    draft_only = '--draft' in sys.argv
    
    with open(md_file, 'r') as f:
        md_content = f.read()
    
    title, subtitle, blocks = markdown_to_substack(md_content)
    
    print(f"Title: {title}")
    print(f"Subtitle: {subtitle}")
    print(f"Blocks: {len(blocks)}")
    print(f"Mode: {'DRAFT' if draft_only else 'PUBLISH'}")
    
    # Auth
    cookies_string = os.getenv("SUBSTACK_COOKIES_STRING")
    email = os.getenv("SUBSTACK_EMAIL")
    password = os.getenv("SUBSTACK_PASSWORD")
    
    if cookies_string:
        api = Api(cookies_string=cookies_string, publication_url=PUBLICATION_URL)
    elif email and password:
        api = Api(email=email, password=password, publication_url=PUBLICATION_URL)
    else:
        print("ERROR: Set SUBSTACK_COOKIES_STRING or SUBSTACK_EMAIL + SUBSTACK_PASSWORD in .env")
        sys.exit(1)
    
    user_id = api.get_user_id()
    print(f"Authenticated as user {user_id}")
    
    post = Post(title, subtitle, user_id, audience="everyone")
    
    for block in blocks:
        post.add(block)
    
    draft = api.post_draft(post.get_draft())
    draft_id = draft.get("id")
    print(f"Draft created: {draft_id}")
    
    if not draft_only:
        api.prepublish_draft(draft_id)
        api.publish_draft(draft_id)
        print(f"PUBLISHED: https://finitematter.substack.com/p/{draft.get('slug', 'new-post')}")
    else:
        print(f"Draft saved. Edit at: https://finitematter.substack.com/publish/post/{draft_id}")


if __name__ == '__main__':
    main()
