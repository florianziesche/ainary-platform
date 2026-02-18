"""Seed the database with current state."""
import sqlite3
import json
from pathlib import Path

DB_PATH = Path(__file__).parent / "workbench.db"

def seed():
    db = sqlite3.connect(str(DB_PATH))
    
    # Topics
    topics = [
        # Revenue - VC Applications
        ("glasswing", "Glasswing Ventures", "revenue", None, 60, {"contact": "Rudina Seseri", "email": "rudina@glasswing.vc", "potential": "$120K+"}),
        ("insight", "Insight Partners", "revenue", None, 40, {"contact": "Onsite Advisor", "potential": "$150K+"}),
        ("futuresight", "FutureSight", "revenue", None, 20, {"contact": "Co-Founder CEO", "portal": "workable"}),
        ("betaworks", "Betaworks", "revenue", None, 40, {"contact": "Jordan Crook", "email": "jordan@betaworks.com"}),
        ("bloomberg", "Bloomberg Beta", "revenue", None, 40, {"contact": "Roy Bahat", "email": "roy@bloombergbeta.com"}),
        ("conviction", "Conviction", "revenue", None, 40, {"contact": "Niki Nguyen", "email": "niki@conviction.com"}),
        ("firstmark", "FirstMark Capital", "revenue", None, 40, {"contact": "Matt Turck", "email": "matt@firstmarkcap.com"}),
        ("generalcatalyst", "General Catalyst", "revenue", None, 40, {"contact": "Jeannette zu Fürstenberg", "email": "jzufurstenberg@generalcatalyst.com"}),
        ("lionheart", "Lionheart Ventures", "revenue", None, 40, {"contact": "Brandon Goldman", "email": "brandon@lionheart.vc"}),
        ("lux", "Lux Capital", "revenue", None, 40, {"contact": "Tracie Rotter", "email": "tracie.rotter@luxcapital.com"}),
        ("point72", "Point72 Ventures", "revenue", None, 40, {"contact": "Kevin Berardinelli", "email": "kevin@p72.vc"}),
        # Revenue - Decisions
        ("steuer", "Steuer-Mahnung", "revenue", None, 15, {"contact": "Barbara Rabl", "email": "b.rabl@rueterpartner.de", "type": "decision"}),
        ("bottleneck-emails", "8 Missing Emails — Resolved", "revenue", None, 100, {"type": "bottleneck", "resolved": True}),
        ("copilot", "GitHub Copilot Trial", "systems", None, 0, {"type": "decision", "deadline": "2026-02-18"}),
        # Content
        ("linkedin10", "10 LinkedIn Posts", "content", None, 80, {}),
        ("glasswing-post", "Glasswing Framework Post", "content", None, 10, {"platforms": ["linkedin", "hackernews"]}),
        ("3laws", "3 Laws of Agent Trust", "content", None, 60, {"platform": "substack", "variants": 5}),
        # Systems
        ("workbench", "Execution Platform", "systems", None, 30, {"type": "product"}),
        ("agenttrust", "AgentTrust", "systems", None, 70, {"repo": "projects/agenttrust"}),
        # Research
        ("research-directed", "Directed Research Agent", "research", None, 50, {"cron": "c352e111"}),
    ]
    
    for t in topics:
        db.execute("INSERT OR REPLACE INTO topics (id, name, stage, parent_id, progress, meta) VALUES (?,?,?,?,?,?)",
                   (t[0], t[1], t[2], t[3], t[4], json.dumps(t[5])))
    
    # Steps for Glasswing
    glasswing_steps = [
        ("glasswing", "Cover letter written", 1, 1),
        ("glasswing", "Email address found", 1, 2),
        ("glasswing", "Subject line set", 1, 3),
        ("glasswing", "LinkedIn post written", 0, 4),
        ("glasswing", "LinkedIn post published", 0, 5),
        ("glasswing", "Email sent", 0, 6),
    ]
    for s in glasswing_steps:
        db.execute("INSERT OR IGNORE INTO steps (topic_id, label, done, position) VALUES (?,?,?,?)", s)
    
    # Steps for Steuer
    steuer_steps = [
        ("steuer", "Mahnung detected", 1, 1),
        ("steuer", "Decide approach", 0, 2),
        ("steuer", "Read original email", 0, 3),
        ("steuer", "Draft response", 0, 4),
        ("steuer", "Send response", 0, 5),
        ("steuer", "Resolved", 0, 6),
    ]
    for s in steuer_steps:
        db.execute("INSERT OR IGNORE INTO steps (topic_id, label, done, position) VALUES (?,?,?,?)", s)
    
    # Steps for batch VCs (same pattern)
    for vc in ["betaworks", "bloomberg", "conviction", "firstmark", "generalcatalyst", "lionheart", "lux", "point72"]:
        vc_steps = [
            (vc, "Cover letter PDF", 1, 1),
            (vc, "CV ready", 1, 2),
            (vc, "Email found", 1, 3),
            (vc, "Send email", 0, 4),
        ]
        for s in vc_steps:
            db.execute("INSERT OR IGNORE INTO steps (topic_id, label, done, position) VALUES (?,?,?,?)", s)
    
    # Connections
    connections = [
        ("glasswing", "glasswing-post", "Prerequisite — social proof before sending"),
        ("glasswing", "agenttrust", "Core asset — Five-Stage Framework implementation"),
        ("glasswing-post", "glasswing", "Enables — social proof for cold email"),
        ("steuer", "copilot", "Both financial decisions"),
        ("workbench", "agenttrust", "Trust scoring integration"),
    ]
    for c in connections:
        db.execute("INSERT OR IGNORE INTO connections (from_topic, to_topic, relation) VALUES (?,?,?)", c)
    
    # Documents
    docs = [
        ("glasswing", "cover-letter-final.md", "job-applications/glasswing/cover-letter-final.md", None, "md"),
        ("glasswing", "CV.pdf", "job-applications/glasswing/CV.pdf", None, "pdf"),
        ("glasswing", "glasswing.vc", None, "https://glasswing.vc", "web"),
        ("steuer", "Original Email", None, None, "email"),
        ("steuer", "decision-queue.md", "memory/decision-queue.md", None, "md"),
    ]
    for d in docs:
        db.execute("INSERT OR IGNORE INTO documents (topic_id, name, path, url, doc_type) VALUES (?,?,?,?,?)", d)
    
    db.commit()
    db.close()
    print(f"Seeded {len(topics)} topics, steps, connections, documents.")

if __name__ == "__main__":
    seed()
