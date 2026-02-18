"""Seed messages and proposals for key topics."""
import sqlite3
import json
from pathlib import Path

DB_PATH = Path(__file__).parent / "workbench.db"

def seed():
    db = sqlite3.connect(str(DB_PATH))
    
    # Clear existing messages
    db.execute("DELETE FROM votes")
    db.execute("DELETE FROM proposals")
    db.execute("DELETE FROM messages")
    
    # ── STEUER-MAHNUNG ──
    m1 = db.execute("INSERT INTO messages (topic_id, sender, content, msg_type) VALUES (?,?,?,?)",
        ("steuer", "system", "Topic created · Detected Feb 10 · USt Q3/2024–Q3/2025 · b.rabl@rueterpartner.de", "system")).lastrowid
    
    m2 = db.execute("INSERT INTO messages (topic_id, sender, content, msg_type) VALUES (?,?,?,?)",
        ("steuer", "mia", "USt-Zahlungen Q3/2024 bis Q3/2025 offen. Email von Barbara Rabl (Rüter & Partner). Genauer Betrag noch unbekannt.", "text")).lastrowid
    
    # Problem proposal
    db.execute("INSERT INTO proposals (message_id, proposal_type, content, confidence, confidence_reason, options) VALUES (?,?,?,?,?,?)",
        (m2, "Problem", "Offene Steuerschuld. Ignorieren führt zu Zinsen, Mahngebühren, schlimmstenfalls Zwangsvollstreckung.", 
         95, "Mahnung ist eindeutig, Betrag fehlt", "[]"))
    
    # Solution proposal with options
    options = [
        {"title": "Ratenzahlung vereinbaren", "recommended": True,
         "description": "Proaktiv antworten, Zahlungsbereitschaft zeigen, Ratenzahlung vorschlagen. Verhindert Eskalation.",
         "draft": "<b>An:</b> b.rabl@rueterpartner.de\n<b>Betreff:</b> USt-Zahlungen — Ratenzahlungsvereinbarung\n\nSehr geehrte Frau Rabl,\n\nvielen Dank für Ihre Erinnerung bezüglich der offenen USt-Zahlungen (Q3/2024 bis Q3/2025).\n\nIch möchte die offenen Beträge begleichen und würde gerne eine Ratenzahlungsvereinbarung besprechen, da mein Einkommen als Freelancer schwankt.\n\nKönnten Sie mir die Gesamtsumme zusammenstellen?\nFür ein Telefonat stehe ich jederzeit zur Verfügung.\n\nMit freundlichen Grüßen\nFlorian Ziesche"},
        {"title": "Erst Email lesen, Betrag prüfen", "recommended": False,
         "description": "Betrag ist unbekannt. Kann €500 oder €5.000 sein. Bei kleinem Betrag: Einmalzahlung. Bei großem: Ratenzahlung."},
        {"title": "Steuerberater kontaktieren", "recommended": False,
         "description": "Wenn unklar ob die Forderung berechtigt ist. Kostet Zeit, schützt vor Überzahlung."}
    ]
    db.execute("INSERT INTO proposals (message_id, proposal_type, content, confidence, confidence_reason, options) VALUES (?,?,?,?,?,?)",
        (m2, "Recommendation", "3 Optionen:", 82, "Standard-Vorgehen bei Steuerschulden", json.dumps(options)))
    
    # ── GLASSWING ──
    m3 = db.execute("INSERT INTO messages (topic_id, sender, content, msg_type) VALUES (?,?,?,?)",
        ("glasswing", "system", "Topic created · Feb 7 · Cover letter batch generated", "system")).lastrowid
    
    m4 = db.execute("INSERT INTO messages (topic_id, sender, content, msg_type) VALUES (?,?,?,?)",
        ("glasswing", "mia", "Cover letter ready. Hook: AgentTrust maps to Glasswing's Five-Stage Framework. Strong thesis overlap with Rudina's keynote.", "text")).lastrowid
    
    db.execute("INSERT INTO proposals (message_id, proposal_type, content, confidence, confidence_reason, options) VALUES (?,?,?,?,?,?)",
        (m4, "Solution", "Send cold email to rudina@glasswing.vc with AgentTrust × Framework angle.", 
         88, "Stärkster Thesis-Overlap aller Funds", "[]"))
    
    m5 = db.execute("INSERT INTO messages (topic_id, sender, content, msg_type) VALUES (?,?,?,?)",
        ("glasswing", "system", "11 days without action · Dwell alert", "system")).lastrowid
    
    m6 = db.execute("INSERT INTO messages (topic_id, sender, content, msg_type) VALUES (?,?,?,?)",
        ("glasswing", "human", "Ich will erst auf LinkedIn und HN posten. Social proof bevor ich die Email sende.", "text")).lastrowid
    
    m7 = db.execute("INSERT INTO messages (topic_id, sender, content, msg_type) VALUES (?,?,?,?)",
        ("glasswing", "mia", "Makes strategic sense. Updated path:", "text")).lastrowid
    
    gl_options = [
        {"title": "Parallel: Send + Post + Follow-up", "recommended": True,
         "description": "Email heute (85% impact). LinkedIn post morgen. Follow-up mit Link (95%, 2nd touchpoint). Total > warten."},
        {"title": "Sequential: Post first, send with proof", "recommended": False,
         "description": "LinkedIn post schreiben, posten, warten auf Traction, dann Email mit Link. Stärkerer Ersteindruck, höheres Verzögerungsrisiko."}
    ]
    db.execute("INSERT INTO proposals (message_id, proposal_type, content, confidence, confidence_reason, options) VALUES (?,?,?,?,?,?)",
        (m7, "Decision", "Parallel oder Sequential?", 75, "Beides valide, Parallel ist sicherer gegen Verzögerung", json.dumps(gl_options)))
    
    # ── COPILOT ──
    m8 = db.execute("INSERT INTO messages (topic_id, sender, content, msg_type) VALUES (?,?,?,?)",
        ("copilot", "mia", "GitHub Copilot Trial endet morgen (Feb 18). $19/Monat wenn nicht gecancelt.", "text")).lastrowid
    
    cop_options = [
        {"title": "Cancel", "recommended": True,
         "description": "Spart $228/Jahr. Mia schreibt den Code. Cursor ist dein IDE. Copilot bringt marginalen Mehrwert."},
        {"title": "Keep 1 month", "recommended": False,
         "description": "$19 um zu testen ob es bei quick edits hilft. Review im März. Low risk, reversible."}
    ]
    db.execute("INSERT INTO proposals (message_id, proposal_type, content, confidence, confidence_reason, options) VALUES (?,?,?,?,?,?)",
        (m8, "Recommendation", "Cancel oder Keep?", 70, "Du codest selten selbst, aber $19 ist wenig Risiko", json.dumps(cop_options)))
    
    # ── BATCH VCs ──
    for vc_id, vc_name, contact, email in [
        ("betaworks", "Betaworks", "Jordan Crook", "jordan@betaworks.com"),
        ("bloomberg", "Bloomberg Beta", "Roy Bahat", "roy@bloombergbeta.com"),
        ("conviction", "Conviction", "Niki Nguyen", "niki@conviction.com"),
        ("firstmark", "FirstMark Capital", "Matt Turck", "matt@firstmarkcap.com"),
        ("generalcatalyst", "General Catalyst", "Jeannette zu Fürstenberg", "jzufurstenberg@generalcatalyst.com"),
        ("lionheart", "Lionheart Ventures", "Brandon Goldman", "brandon@lionheart.vc"),
        ("lux", "Lux Capital", "Tracie Rotter", "tracie.rotter@luxcapital.com"),
        ("point72", "Point72 Ventures", "Kevin Berardinelli", "kevin@p72.vc"),
    ]:
        mid = db.execute("INSERT INTO messages (topic_id, sender, content, msg_type) VALUES (?,?,?,?)",
            (vc_id, "mia", f"Cover letter PDF + CV ready. Contact: {contact} ({email}). Email address researched and verified.", "text")).lastrowid
        
        send_options = [
            {"title": "Send now", "recommended": True,
             "description": f"Send email to {email} with CoverLetter.pdf + CV.pdf attached.",
             "draft": f"<b>To:</b> {email}\n<b>Subject:</b> AI-Native Operator — Former CEO, €5.5M raised\n<b>Attachments:</b> CoverLetter.pdf, CV.pdf"},
            {"title": "Customize first", "recommended": False,
             "description": "Review and personalize the cover letter before sending."}
        ]
        db.execute("INSERT INTO proposals (message_id, proposal_type, content, confidence, confidence_reason, options) VALUES (?,?,?,?,?,?)",
            (mid, "Ready to Send", f"All materials ready for {vc_name}.", 85, "PDF + CV fertig, Email verified", json.dumps(send_options)))
    
    # ── BOTTLENECK RESOLVED ──
    m9 = db.execute("INSERT INTO messages (topic_id, sender, content, msg_type) VALUES (?,?,?,?)",
        ("bottleneck-emails", "mia", "All 8 email addresses researched. 6 high confidence, 2 medium. Systemic blocker resolved.", "text")).lastrowid
    
    db.execute("INSERT INTO proposals (message_id, proposal_type, content, confidence, confidence_reason, options) VALUES (?,?,?,?,?,?)",
        (m9, "Resolution", "Bottleneck cleared. 8 VC applications moved from Draft to Ready.", 90, "Emails verified via multiple sources", "[]"))
    
    db.commit()
    db.close()
    print("Seeded messages + proposals for all topics.")

if __name__ == "__main__":
    seed()
