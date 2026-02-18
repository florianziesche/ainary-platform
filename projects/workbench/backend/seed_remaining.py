"""Seed messages + proposals for all empty topics."""
import sqlite3
import json
from pathlib import Path

DB_PATH = Path(__file__).parent / "workbench.db"

def msg(db, topic_id, sender, content, msg_type="text"):
    return db.execute(
        "INSERT INTO messages (topic_id, sender, content, msg_type) VALUES (?,?,?,?)",
        (topic_id, sender, content, msg_type)
    ).lastrowid

def prop(db, message_id, ptype, content, conf=None, reason=None, options=None):
    db.execute(
        "INSERT INTO proposals (message_id, proposal_type, content, confidence, confidence_reason, options) VALUES (?,?,?,?,?,?)",
        (message_id, ptype, content, conf, reason, json.dumps(options or []))
    )

def seed():
    db = sqlite3.connect(str(DB_PATH))

    # ── INSIGHT PARTNERS ──
    m = msg(db, "insight", "system", "Topic created · Feb 7 · Onsite Advisor role identified")
    m = msg(db, "insight", "mia", "Insight Partners sucht Onsite Advisors — Operating Partner mit AI/SaaS Expertise. Kein öffentliches Job Posting gefunden, aber sie rekrutieren laufend über Netzwerk.")
    prop(db, m, "Research", "Insight ist einer der größten Growth Equity Funds ($90B+ AUM). Onsite Advisors arbeiten direkt mit Portfolio-Firmen — passt zu deinem Operator-Profil.", 75, "Kein offenes Posting, Cold Outreach nötig")
    m = msg(db, "insight", "mia", "Nächste Schritte:")
    prop(db, m, "Recommendation", "Cold outreach an Insight's Talent team.", 72, "Kein direkter Kontakt, Pattern-basierte Email", [
        {"title": "Email an Talent Team", "recommended": True,
         "description": "talent@insightpartners.com oder über LinkedIn. Insight hat ein großes Talent-Team das Onsite Advisors rekrutiert.",
         "draft": "<b>To:</b> talent@insightpartners.com\n<b>Subject:</b> Onsite Advisor — AI/SaaS Operator (€5.5M raised, BMW/Siemens)\n\nDear Insight Talent Team,\n\nI'm reaching out regarding Onsite Advisor opportunities. As former CEO of an AI SaaS company (€5.5M raised, clients: BMW, Siemens, Bosch), I bring hands-on experience scaling AI products in enterprise environments.\n\nI'd welcome the chance to discuss how my operator background could serve Insight's portfolio.\n\nBest,\nFlorian Ziesche"},
        {"title": "LinkedIn Warm Intro suchen", "recommended": False,
         "description": "Erst checken ob es Mutual Connections gibt. Höhere Antwortrate, aber dauert länger."},
        {"title": "Über Portal bewerben", "recommended": False,
         "description": "insightpartners.com/careers — falls ein passendes Posting existiert. Geringste Conversion."}
    ])

    # ── FUTURESIGHT ──
    m = msg(db, "futuresight", "system", "Topic created · Feb 12 · Co-Founder & CEO — AI GTM Agents for SMBs")
    m = msg(db, "futuresight", "mia", "FutureSight sucht einen Co-Founder & CEO für AI GTM Agents für KMU. Workable-Portal. Die JD ist JS-heavy geladen — ich konnte sie nicht vollständig scrapen.")
    prop(db, m, "Problem", "Brauche die vollständige Job Description um ein starkes Cover Letter zu schreiben. Workable rendert mit JavaScript — web_fetch reicht nicht.", 90, "Technische Limitierung bestätigt")
    m = msg(db, "futuresight", "human", "Ich kopiere die JD wenn ich Zeit habe.")
    m = msg(db, "futuresight", "mia", "Waiting. Sobald du die JD postest, schreibe ich sofort das Cover Letter.")
    prop(db, m, "Blocker", "⏸ Warte auf JD von Florian. Ohne JD kann ich kein personalisiertes Cover Letter schreiben.", 95, "Harter Blocker — nur Florian kann lösen", [
        {"title": "JD jetzt kopieren (2 min)", "recommended": True,
         "description": "Öffne https://apply.workable.com/futuresight/ → Copy-paste die JD hier rein. Dann schreibe ich sofort."},
        {"title": "Skip — andere Bewerbungen priorisieren", "recommended": False,
         "description": "8 andere Funds sind ready to send. FutureSight kann warten."}
    ])

    # ── GLASSWING POST ──
    m = msg(db, "glasswing-post", "system", "Topic created · Feb 17 · Prerequisite für Glasswing Email")
    m = msg(db, "glasswing-post", "mia", "Florian will einen LinkedIn-Post über Glasswing's Five-Stage Framework schreiben — als Social Proof bevor die Cold Email rausgeht. Stärkster Content-Angle: AgentTrust implementiert genau dieses Framework.")
    prop(db, m, "Solution", "LinkedIn Post: 'I reverse-engineered Glasswing's Five-Stage AI Framework and built it open-source.' Hook → Framework → Implementation → CTA.", 80, "Starker Angle, aber Post muss noch geschrieben werden", [
        {"title": "Post jetzt schreiben lassen", "recommended": True,
         "description": "Ich schreibe den Draft. Hook: 'Glasswing published a Five-Stage Framework for AI Trust. I built it.' ~1200 Zeichen, LinkedIn-optimiert."},
        {"title": "Erst auf HackerNews posten", "recommended": False,
         "description": "AgentTrust auf HN posten → Traction → LinkedIn mit HN-Link. Mehr Social Proof, aber dauert 24-48h."},
        {"title": "Parallel: Post + Email gleichzeitig", "recommended": False,
         "description": "Email heute, Post morgen, Follow-up mit Link. Schneller, aber ohne Social Proof im Erst-Kontakt."}
    ])

    # ── 10 LINKEDIN POSTS ──
    m = msg(db, "linkedin10", "system", "Topic created · Feb 10 · Content Engine — 10 Posts in Pipeline")
    m = msg(db, "linkedin10", "mia", "10 LinkedIn Posts geplant. Themen: AI Agent Architecture, Trust in AI, Founder→VC Transition, Open Source, Mittelstand + AI. Bisher 8 Drafts geschrieben, 0 published.")
    prop(db, m, "Problem", "8 Drafts, 0 published. Das ist ein klassisches Building-Pattern — Content produzieren ohne zu senden.", 88, "Bekanntes Pattern, siehe SOUL.md Anti-Building Regel")
    m = msg(db, "linkedin10", "mia", "Empfehlung: 1 Post pro Tag publizieren statt alle auf einmal. Startet Momentum.")
    prop(db, m, "Recommendation", "Heute den besten Draft reviewen und posten. Morgen den nächsten.", 85, "Konsistenz > Perfektionism", [
        {"title": "Besten Post auswählen + posten", "recommended": True,
         "description": "Ich zeige dir die 3 stärksten Drafts. Du wählst einen. Review → Post → Done. 10 Minuten."},
        {"title": "Alle 8 überarbeiten, dann Batch-posten", "recommended": False,
         "description": "Qualität, aber hohes Risiko dass nichts rausgeht. Dein Pattern."}
    ])

    # ── 3 LAWS OF AGENT TRUST ──
    m = msg(db, "3laws", "system", "Topic created · Feb 14 · Substack Artikel — 5 Varianten geschrieben")
    m = msg(db, "3laws", "mia", "Substack-Artikel '3 Laws of Agent Trust' — 5 Varianten erstellt. Variante 3 (Narrative + Technical) war am stärksten. Noch nicht published.")
    prop(db, m, "Solution", "Variante 3 finalisieren und auf Substack publizieren. Dann als LinkedIn-Teaser repurposen.", 78, "5 Varianten sind genug. Schiff es.", [
        {"title": "Variante 3 finalisieren + publishen", "recommended": True,
         "description": "Final edit pass, dann auf Substack publizieren. Danach LinkedIn-Teaser (300 Zeichen + Link)."},
        {"title": "A/B: Variante 3 vs. 5 testen", "recommended": False,
         "description": "Beide an 5 Leute schicken, Feedback sammeln, dann die bessere publishen. +2 Tage."}
    ])

    # ── DIRECTED RESEARCH AGENT ──
    m = msg(db, "research-directed", "system", "Topic created · Feb 17 · Cron c352e111 · 6:00/14:00/22:00")
    m = msg(db, "research-directed", "mia", "Directed Research Agent ersetzt 3 breite Research Crons. Läuft 3× täglich. Sucht gezielt Wissenslücken in verified-truths.md und connections.md, füllt sie mit Web-Recherche.")
    prop(db, m, "Status", "Erster Run um 14:00 war erfolgreich. 22:00 Run gerade gelaufen (ok, 2m39s). Output wird via Telegram delivered.", 90, "Cron läuft, Status ok")
    m = msg(db, "research-directed", "mia", "Monitoring:")
    prop(db, m, "Recommendation", "Qualität der Findings nach 3 Tagen evaluieren. Wenn >50% Noise → Prompt schärfen.", 75, "Zu früh um Qualität zu bewerten", [
        {"title": "3 Tage laufen lassen, dann evaluieren", "recommended": True,
         "description": "Sammle Findings von 9 Runs. Dann: Wie viele waren nutzbar? Wie viele verified-truths entstanden?"},
        {"title": "Jetzt Prompt anpassen", "recommended": False,
         "description": "Zu früh. Brauchen erstmal Datenpunkte."}
    ])

    # ── AGENTTRUST ──
    m = msg(db, "agenttrust", "system", "Topic created · Feb 12 · Python CLI + GitHub Repo")
    m = msg(db, "agenttrust", "mia", "AgentTrust: Trust-Scoring-System für AI Agents. CLI wrapper (scripts/agenttrust-score.py) verbindet Python-Repo mit Workflow. Aktueller Stand: main=8, writer=1, researcher=1, builder=1.")
    prop(db, m, "Status", "System funktioniert. Quality Audit Cron nutzt es 3× täglich. Trust Scores steigen/fallen basierend auf Output-Qualität.", 85, "System läuft, Scores noch sehr niedrig")
    m = msg(db, "agenttrust", "mia", "AgentTrust ist auch der stärkste Content-Angle: Glasswing's Framework implementiert als Open Source.")
    prop(db, m, "Connection", "AgentTrust verbindet 3 Flywheel-Stages: Systems (das Tool) → Content (der Artikel/Post) → Revenue (Glasswing-Bewerbung). Stärkstes Asset im Portfolio.", 90, "Direkte Verbindung zu 3 Revenue-Opportunities")

    # ── EXECUTION PLATFORM (WORKBENCH) ──
    m = msg(db, "workbench", "system", "Topic created · Feb 17 · 6 Design-Iterationen · Backend MVP live")
    m = msg(db, "workbench", "mia", "Execution Platform: Human+AI Workbench. 6 Iterationen heute. Finale Architektur: Flywheel Pipeline + Topic Conversations + Confidence-scored Proposals + A/B Testing + Daily Eval. Backend: FastAPI + SQLite, läuft auf Port 8080.")
    prop(db, m, "Status", "Frontend verbunden mit API. Topics, Messages, Steps, Votes funktionieren. Noch offen: Multi-select Daily Eval, A/B Testing Pattern, Priority Scoring.", 82, "MVP funktional, Feature-Gaps bekannt")
    m = msg(db, "workbench", "mia", "Content-Angle: 'How I built an AI Execution Platform and sent 14 VC applications in one week.' 50K+ Impression Potential auf LinkedIn.")
    prop(db, m, "Recommendation", "Erst nutzen, dann darüber schreiben. Story braucht Ergebnisse.", 88, "Build → Use → Results → Story → Content", [
        {"title": "1 Woche nutzen, dann Post schreiben", "recommended": True,
         "description": "Sammle echte Metriken: Wie viele Decisions getroffen? Wie viel Trust aufgebaut? Dann authentischer Post."},
        {"title": "Jetzt schon darüber posten", "recommended": False,
         "description": "Teaser-Post möglich, aber ohne Ergebnisse ist es nur ein Build-Announcement. Schwächerer Content."}
    ])

    # ── LIONHEART — fix: only has 1 msg, needs proposal ──
    # Check existing
    existing = db.execute("SELECT COUNT(*) FROM proposals p JOIN messages m ON p.message_id=m.id WHERE m.topic_id='lionheart'").fetchone()[0]
    if existing == 0:
        m = msg(db, "lionheart", "mia", "Next step:")
        prop(db, m, "Ready to Send", "All materials ready for Lionheart Ventures.", 85, "PDF + CV fertig, Email verified", [
            {"title": "Send now", "recommended": True,
             "description": "Send email to brandon@lionheart.vc with CoverLetter.pdf + CV.pdf attached.",
             "draft": "<b>To:</b> brandon@lionheart.vc\n<b>Subject:</b> AI-Native Operator — Former CEO, €5.5M raised\n<b>Attachments:</b> CoverLetter.pdf, CV.pdf"},
            {"title": "Customize first", "recommended": False,
             "description": "Review and personalize the cover letter before sending."}
        ])

    db.commit()
    db.close()
    print("Seeded all remaining topics with messages + proposals.")

if __name__ == "__main__":
    seed()
