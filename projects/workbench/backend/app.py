"""
Execution Platform Backend — MVP
FastAPI + SQLite. Topics, Messages, Votes, Trust.
"""

from fastapi import FastAPI, HTTPException, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from typing import Optional, List, Set
import sqlite3
import json
import os
import asyncio
import httpx
from datetime import datetime
from pathlib import Path

DB_PATH = Path(__file__).parent / "workbench.db"
STATIC_PATH = Path(__file__).parent.parent  # serves index.html

app = FastAPI(title="Execution Platform")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

# ── Global Error Handler ──
from starlette.requests import Request
from starlette.responses import JSONResponse

@app.exception_handler(sqlite3.OperationalError)
async def db_error_handler(request: Request, exc: sqlite3.OperationalError):
    return JSONResponse(status_code=503, content={"detail": f"Database error: {str(exc)[:200]}", "type": "db_error"})

@app.exception_handler(sqlite3.IntegrityError)
async def db_integrity_handler(request: Request, exc: sqlite3.IntegrityError):
    return JSONResponse(status_code=409, content={"detail": f"Constraint violation: {str(exc)[:200]}", "type": "integrity_error"})

@app.exception_handler(Exception)
async def global_error_handler(request: Request, exc: Exception):
    # Log to stderr for debugging
    import traceback
    traceback.print_exc()
    return JSONResponse(status_code=500, content={"detail": f"Internal error: {type(exc).__name__}: {str(exc)[:200]}", "type": "internal_error"})

# ── WebSocket Hub ──

class ConnectionManager:
    def __init__(self):
        self.connections: List[WebSocket] = []
    
    async def connect(self, ws: WebSocket):
        await ws.accept()
        self.connections.append(ws)
    
    def disconnect(self, ws: WebSocket):
        if ws in self.connections:
            self.connections.remove(ws)
    
    async def broadcast(self, event: dict):
        dead = []
        for ws in self.connections:
            try:
                await ws.send_json(event)
            except:
                dead.append(ws)
        for ws in dead:
            self.disconnect(ws)

ws_manager = ConnectionManager()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await ws_manager.connect(websocket)
    try:
        while True:
            # Keep alive — client can send pings
            data = await websocket.receive_text()
            if data == "ping":
                await websocket.send_json({"type": "pong"})
    except WebSocketDisconnect:
        ws_manager.disconnect(websocket)

def notify(event_type: str, data: dict):
    """Queue a broadcast event. Called from sync code."""
    import asyncio
    event = {"type": event_type, **data}
    try:
        loop = asyncio.get_event_loop()
        if loop.is_running():
            loop.create_task(ws_manager.broadcast(event))
    except RuntimeError:
        pass

# ── DB Setup ──

def get_db():
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    return conn

def init_db():
    db = get_db()
    db.executescript("""
        CREATE TABLE IF NOT EXISTS folders (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            parent_id TEXT,
            position INTEGER DEFAULT 0,
            color TEXT,
            icon TEXT,
            collapsed INTEGER DEFAULT 0,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        );
        CREATE TABLE IF NOT EXISTS topics (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            stage TEXT DEFAULT 'revenue',
            parent_id TEXT,
            folder_id TEXT,
            folder_position INTEGER DEFAULT 0,
            progress INTEGER DEFAULT 0,
            state TEXT DEFAULT 'active',
            meta TEXT DEFAULT '{}',
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            updated_at TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (folder_id) REFERENCES folders(id)
        );
        CREATE TABLE IF NOT EXISTS steps (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic_id TEXT NOT NULL,
            label TEXT NOT NULL,
            done INTEGER DEFAULT 0,
            position INTEGER DEFAULT 0,
            FOREIGN KEY (topic_id) REFERENCES topics(id)
        );
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic_id TEXT NOT NULL,
            sender TEXT NOT NULL,
            content TEXT NOT NULL,
            msg_type TEXT DEFAULT 'text',
            meta TEXT DEFAULT '{}',
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (topic_id) REFERENCES topics(id)
        );
        CREATE TABLE IF NOT EXISTS proposals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            message_id INTEGER NOT NULL,
            proposal_type TEXT NOT NULL,
            content TEXT NOT NULL,
            confidence INTEGER,
            confidence_reason TEXT,
            options TEXT DEFAULT '[]',
            chosen_option TEXT,
            meta TEXT DEFAULT '{}',
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (message_id) REFERENCES messages(id)
        );
        CREATE TABLE IF NOT EXISTS votes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            proposal_id INTEGER NOT NULL,
            direction TEXT NOT NULL,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (proposal_id) REFERENCES proposals(id)
        );
        CREATE TABLE IF NOT EXISTS connections (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            from_topic TEXT NOT NULL,
            to_topic TEXT NOT NULL,
            relation TEXT,
            FOREIGN KEY (from_topic) REFERENCES topics(id),
            FOREIGN KEY (to_topic) REFERENCES topics(id)
        );
        CREATE TABLE IF NOT EXISTS documents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic_id TEXT NOT NULL,
            name TEXT NOT NULL,
            path TEXT,
            url TEXT,
            doc_type TEXT DEFAULT 'file',
            FOREIGN KEY (topic_id) REFERENCES topics(id)
        );
        CREATE TABLE IF NOT EXISTS eval_responses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question_id INTEGER NOT NULL,
            answers TEXT NOT NULL,
            session_date TEXT NOT NULL,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        );
        CREATE TABLE IF NOT EXISTS trust_scores (
            agent TEXT PRIMARY KEY,
            score INTEGER DEFAULT 0,
            total_votes INTEGER DEFAULT 0,
            up_votes INTEGER DEFAULT 0,
            down_votes INTEGER DEFAULT 0,
            updated_at TEXT DEFAULT CURRENT_TIMESTAMP
        );
    """)
    
    db.executescript("""
        CREATE TABLE IF NOT EXISTS corrections (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            rule TEXT NOT NULL,
            category TEXT DEFAULT 'general',
            wrong TEXT DEFAULT '',
            rght TEXT DEFAULT '',
            source_topic TEXT,
            severity INTEGER DEFAULT 2,
            active INTEGER DEFAULT 1,
            violation_count INTEGER DEFAULT 0,
            last_violated TEXT,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        );
        CREATE TABLE IF NOT EXISTS quality_standards (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            rule TEXT NOT NULL,
            category TEXT DEFAULT 'general',
            output_type TEXT DEFAULT 'general',
            active INTEGER DEFAULT 1,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        );
        CREATE TABLE IF NOT EXISTS trust_skills (
            skill TEXT PRIMARY KEY,
            score INTEGER DEFAULT 50,
            total INTEGER DEFAULT 0,
            up INTEGER DEFAULT 0,
            down INTEGER DEFAULT 0,
            updated_at TEXT DEFAULT CURRENT_TIMESTAMP
        );
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic_id TEXT,
            event_type TEXT NOT NULL,
            detail TEXT DEFAULT '{}',
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        );
        CREATE TABLE IF NOT EXISTS preferences (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            scope TEXT NOT NULL,
            key TEXT NOT NULL,
            value TEXT NOT NULL,
            confidence INTEGER DEFAULT 50,
            data_points INTEGER DEFAULT 0,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            updated_at TEXT DEFAULT CURRENT_TIMESTAMP
        );
    """)
    
    # Findings (Compound Knowledge Engine)
    db.executescript("""
        CREATE TABLE IF NOT EXISTS findings (
            id TEXT PRIMARY KEY,
            claim TEXT NOT NULL,
            context TEXT,
            confidence REAL DEFAULT 0.50,
            status TEXT DEFAULT 'alive',
            killed_by TEXT,
            source_type TEXT,
            source_detail TEXT,
            extracted_from TEXT,
            tags TEXT DEFAULT '[]',
            research_line TEXT,
            used_in_systems TEXT DEFAULT '[]',
            used_in_content TEXT DEFAULT '[]',
            used_in_revenue TEXT DEFAULT '[]',
            supports TEXT DEFAULT '[]',
            contradicts TEXT DEFAULT '[]',
            derived_from TEXT DEFAULT '[]',
            compound_score REAL DEFAULT 0.0,
            topic_id TEXT,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            updated_at TEXT DEFAULT CURRENT_TIMESTAMP
        );
        CREATE TABLE IF NOT EXISTS confidence_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            finding_id TEXT NOT NULL,
            old_confidence REAL,
            new_confidence REAL,
            reason TEXT,
            source TEXT,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (finding_id) REFERENCES findings(id)
        );
        CREATE TABLE IF NOT EXISTS research_lines (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            description TEXT,
            status TEXT DEFAULT 'active',
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        );
    """)
    
    # Migrations for existing DBs
    try:
        db.execute("ALTER TABLE topics ADD COLUMN folder_id TEXT")
    except: pass
    try:
        db.execute("ALTER TABLE topics ADD COLUMN folder_position INTEGER DEFAULT 0")
    except: pass
    try:
        db.execute("ALTER TABLE findings ADD COLUMN verified INTEGER DEFAULT 0")
    except: pass
    try:
        db.execute("ALTER TABLE findings ADD COLUMN source_url TEXT")
    except: pass
    
    # Seed default folders
    default_folders = [
        ("heute", "Heute", None, 0, "#d4a853", "☀"),
        ("wichtig", "Wichtig", None, 1, "#c47070", "!"),
        ("vc-apps", "VC Applications", None, 2, None, "V"),
        ("consulting", "Consulting", None, 3, None, "C"),
        ("content", "Content", None, 4, None, "W"),
        ("admin", "Admin / Legal", None, 5, None, "A"),
        ("later", "Später", None, 6, None, "…"),
    ]
    for fid, fname, fparent, fpos, fcolor, ficon in default_folders:
        db.execute("INSERT OR IGNORE INTO folders (id, name, parent_id, position, color, icon) VALUES (?,?,?,?,?,?)",
                   (fid, fname, fparent, fpos, fcolor, ficon))
    
    # Seed corrections from corrections.md
    corrections_seed = [
        # Design
        ("Neon-Farben verboten. Nur Black + White + Gold (#c8aa50)", "design", "Neon-Farben", "Black + White + Gold (#c8aa50)", 3),
        ("Max font-weight 600 (Semibold), nie 700 (Bold)", "design", "font-weight 700", "Max 600", 2),
        ("Custom SVG Icons (Lucide), keine Emoji", "design", "Emoji als Icons", "SVG (Lucide, stroke-width 1.5)", 2),
        ("Keine fake Zahlen", "design", "Fake Zahlen ('2,847 professionals')", "Ehrliche Zahlen oder weglassen", 3),
        ("Keine 'Trusted by' Logos ohne echte Kunden", "design", "Trusted by [Logos]", "Erst nach Launch", 2),
        ("Substanz > Optik", "design", "Viel Deko, wenig Information", "Substanz zeigen", 2),
        ("Solo Founder Voice: 'I' nicht 'We'", "design", "'We'", "'I'", 3),
        ("Keine Stock Photos oder AI-generated Images", "design", "Stock photos / AI images", "SVG Graphics, code-based", 2),
        ("opacity:1 als CSS Default", "design", "opacity:0 defaults", "opacity:1", 2),
        ("Kein 'McKinsey-grade', nur 'Consultant-grade'", "design", "'McKinsey-grade'", "'Consultant-grade'", 2),
        # Content
        ("Keine LLM-Phrasen ('In today\\'s rapidly evolving...')", "content", "LLM-Phrasen", "Florians Stimme: direkt, kurz, spezifisch", 3),
        ("Echte Firmennamen statt generische", "content", "'a major payment processor'", "'Stripe'", 2),
        ("Direkt zum Punkt, keine langen Einleitungen", "content", "Lange Einleitungen", "Direkt anfangen", 2),
        ("1 Empfehlung, nicht 5 Optionen", "content", "5 Optionen", "1 Empfehlung mit 'Mein Vote:'", 3),
        ("Max 1 Telegram-Nachricht pro Delivery", "content", "Mehrere Nachrichten", "Max 1", 2),
        ("Nie 'Great question!' / 'I\\'d be happy to!'", "content", "Sycophantic phrases", "Einfach antworten", 3),
        # Process
        ("Erst Fragen stellen, dann bauen", "process", "Sofort bauen", "Problem erst definieren", 3),
        ("Edit für existierende Dateien, nie Write", "process", "Write für existierende Files", "Edit nutzen", 2),
        ("Max 1-2 Iterationen nach Bestätigung", "process", "10 Iterationen", "Fragen → Bestätigung → 1-2 Iterationen", 2),
        ("Bei jedem Build fragen: Bringt das Revenue?", "process", "Features vorschlagen", "Revenue-Frage stellen", 3),
        ("Sub-Agent Briefings exakt: 'Kopiere 1:1, ändere NUR Text'", "process", "Vages Briefing", "Exaktes Briefing", 2),
        ("Sofort in Datei schreiben, keine Mental Notes", "process", "Mental notes", "Sofort schreiben", 2),
        ("Qualität > Speed: 'Lass dir Zeit. Besser einmal länger.'", "process", "Schnell + schlecht", "Einmal richtig", 3),
        # Tone
        ("Direkt, Deutsch, kurz mit Florian", "tone", "Förmlich", "Direkt", 2),
        ("Florian ist technisch — nicht zu viel erklären", "tone", "Zu viel erklären", "Er versteht", 2),
        ("Ehrlich + Pushback, kein Sycophancy", "tone", "'Great idea!'", "Ehrliche Meinung", 3),
        # Facts
        ("IMMER Originaldokumente lesen, nie aus Gedächtnis", "facts", "Thesis aus Gedächtnis", "Quelle lesen", 3),
        ("NIE Preise/Kosten in Kunden-Docs", "facts", "Preise zeigen", "Nur Nutzen", 3),
        ("Audience-Tags: [KUNDE] [LP/VC] [PUBLIC] [INTERN]", "facts", "Audiences vermischen", "Tags nutzen", 2),
    ]
    for rule, cat, wrong, right, sev in corrections_seed:
        exists = db.execute("SELECT 1 FROM corrections WHERE rule = ?", (rule,)).fetchone()
        if not exists:
            db.execute("INSERT INTO corrections (rule, category, wrong, rght, severity) VALUES (?,?,?,?,?)",
                       (rule, cat, wrong, right, sev))
    
    # Seed quality standards
    standards_seed = [
        ("Max 5-7 Sätze", "length", "email"),
        ("Konkreter Grund warum ICH an DICH schreibe", "relevance", "email"),
        ("1 klarer CTA (Call, Demo, Antwort)", "structure", "email"),
        ("Kein 'I hope this finds you well'", "tone", "email"),
        ("Hook in Zeile 1 (Zahl oder provokante Aussage)", "structure", "linkedin"),
        ("Max 1.300 Zeichen", "length", "linkedin"),
        ("Max 3 Hashtags", "format", "linkedin"),
        ("Persönliche Story > generische Tipps", "content", "linkedin"),
        ("Florians Stimme: direkt, ehrlich, spezifisch", "tone", "blog"),
        ("Echte Namen, echte Zahlen", "facts", "blog"),
        ("5-8 Min Lesezeit", "length", "blog"),
        ("Personal Story + Numbers + Lesson + Philosophical Closer", "structure", "blog"),
        ("Black + White + Gold only", "design", "website"),
        ("Mobile-first: IMMER vor Deploy testen", "process", "website"),
        ("Quellenangaben wo möglich", "facts", "report"),
        ("Keine Investment-Preise in Kunden-Docs", "facts", "report"),
        ("Confidence angeben wenn unsicher", "transparency", "general"),
        ("Ehrliche Zahlen oder weglassen", "facts", "general"),
    ]
    for rule, cat, otype in standards_seed:
        exists = db.execute("SELECT 1 FROM quality_standards WHERE rule = ?", (rule,)).fetchone()
        if not exists:
            db.execute("INSERT INTO quality_standards (rule, category, output_type) VALUES (?,?,?)",
                       (rule, cat, otype))
    
    # Seed trust per skill
    skill_seeds = [
        ("cv_generation", 45), ("email_drafts", 30), ("research", 70),
        ("linkedin_content", 15), ("website_design", 55), ("report_generation", 60),
        ("financial_decisions", 5), ("consulting_outreach", 25), ("translation", 50),
    ]
    for skill, score in skill_seeds:
        db.execute("INSERT OR IGNORE INTO trust_skills (skill, score) VALUES (?,?)", (skill, score))
    
    # Seed trust scores
    for agent in ['main', 'writer', 'researcher', 'builder', 'hunter', 'dealmaker']:
        db.execute("INSERT OR IGNORE INTO trust_scores (agent, score) VALUES (?, ?)",
                   (agent, 8 if agent == 'main' else 1))
    
    db.commit()
    db.close()

init_db()

# ── Models ──

class TopicCreate(BaseModel):
    id: str
    name: str
    stage: str = "revenue"
    parent_id: Optional[str] = None
    meta: dict = {}

class MessageCreate(BaseModel):
    sender: str
    content: str
    msg_type: str = "text"
    meta: dict = {}

class ProposalCreate(BaseModel):
    proposal_type: str
    content: str
    confidence: Optional[int] = None
    confidence_reason: Optional[str] = None
    options: list = []

class VoteCreate(BaseModel):
    direction: str  # "up" or "down"

class StepCreate(BaseModel):
    label: str
    done: bool = False

class EvalResponse(BaseModel):
    question_id: int
    answers: List[str]  # Multiple selection

# ── Topics ──

@app.get("/api/topics")
def list_topics(stage: Optional[str] = None):
    db = get_db()
    if stage:
        rows = db.execute("SELECT * FROM topics WHERE stage = ? ORDER BY created_at", (stage,)).fetchall()
    else:
        rows = db.execute("SELECT * FROM topics ORDER BY stage, created_at").fetchall()
    db.close()
    return [dict(r) for r in rows]

@app.post("/api/topics")
def create_topic(t: TopicCreate):
    db = get_db()
    db.execute("INSERT INTO topics (id, name, stage, parent_id, meta) VALUES (?,?,?,?,?)",
               (t.id, t.name, t.stage, t.parent_id, json.dumps(t.meta)))
    db.commit()
    db.close()
    return {"id": t.id, "status": "created"}

@app.get("/api/topics/{topic_id}")
def get_topic(topic_id: str):
    db = get_db()
    row = db.execute("SELECT * FROM topics WHERE id = ?", (topic_id,)).fetchone()
    if not row:
        raise HTTPException(404, "Topic not found")
    
    # Get steps, messages, docs, connections
    steps = db.execute("SELECT * FROM steps WHERE topic_id = ? ORDER BY position", (topic_id,)).fetchall()
    messages = db.execute("SELECT * FROM messages WHERE topic_id = ? ORDER BY created_at", (topic_id,)).fetchall()
    docs = db.execute("SELECT * FROM documents WHERE topic_id = ? AND (kind = 'doc' OR kind IS NULL)", (topic_id,)).fetchall()
    refs = db.execute("SELECT * FROM documents WHERE topic_id = ? AND kind = 'ref'", (topic_id,)).fetchall()
    # Bidirectional connections with stage info
    conns_out = db.execute("""
        SELECT c.*, t.name as target_name, t.stage as target_stage, 'downstream' as direction
        FROM connections c 
        JOIN topics t ON c.to_topic = t.id 
        WHERE c.from_topic = ?
    """, (topic_id,)).fetchall()
    conns_in = db.execute("""
        SELECT c.id, c.from_topic as to_topic, c.to_topic as from_topic, c.relation,
               t.name as target_name, t.stage as target_stage, 'upstream' as direction
        FROM connections c 
        JOIN topics t ON c.from_topic = t.id 
        WHERE c.to_topic = ?
    """, (topic_id,)).fetchall()
    conns = list(conns_out) + list(conns_in)
    
    # Get proposals for messages
    msg_list = []
    for m in messages:
        md = dict(m)
        proposals = db.execute("SELECT * FROM proposals WHERE message_id = ?", (m['id'],)).fetchall()
        md['proposals'] = []
        for p in proposals:
            pd = dict(p)
            votes = db.execute("SELECT direction, COUNT(*) as cnt FROM votes WHERE proposal_id = ? GROUP BY direction", (p['id'],)).fetchall()
            pd['votes'] = {v['direction']: v['cnt'] for v in votes}
            pd['options'] = json.loads(pd['options']) if pd['options'] else []
            md['proposals'].append(pd)
        msg_list.append(md)
    
    db.close()
    result = dict(row)
    result['steps'] = [dict(s) for s in steps]
    result['messages'] = msg_list
    result['documents'] = [dict(d) for d in docs]
    result['references'] = [dict(r) for r in refs]
    result['connections'] = [dict(c) for c in conns]
    return result

# ── Messages ──

@app.post("/api/topics/{topic_id}/messages")
def add_message(topic_id: str, m: MessageCreate):
    db = get_db()
    cursor = db.execute("INSERT INTO messages (topic_id, sender, content, msg_type, meta) VALUES (?,?,?,?,?)",
                        (topic_id, m.sender, m.content, m.msg_type, json.dumps(m.meta)))
    msg_id = cursor.lastrowid
    db.execute("UPDATE topics SET updated_at = CURRENT_TIMESTAMP WHERE id = ?", (topic_id,))
    
    # Auto-respond to human messages
    mia_msg_id = None
    if m.sender == 'human' and m.content.strip():
        response = generate_chat_response(db, topic_id, m.content.strip())
        if response:
            r_cursor = db.execute("INSERT INTO messages (topic_id, sender, content, msg_type) VALUES (?,?,?,?)",
                        (topic_id, "mia", response['message'], "text"))
            mia_msg_id = r_cursor.lastrowid
            if response.get('proposal'):
                p = response['proposal']
                db.execute("INSERT INTO proposals (message_id, proposal_type, content, confidence, confidence_reason, options) VALUES (?,?,?,?,?,?)",
                    (mia_msg_id, p['type'], p['content'], p.get('confidence'), p.get('reason'), json.dumps(p.get('options', []))))
    
    db.commit()
    db.close()
    
    # Notify all connected clients
    notify("message", {"topic_id": topic_id, "sender": m.sender, "content": m.content})
    if mia_msg_id:
        notify("message", {"topic_id": topic_id, "sender": "mia"})
    
    return {"id": msg_id, "status": "created"}


def generate_chat_response(db, topic_id, content):
    """Generate response to free-text messages based on topic context."""
    topic = db.execute("SELECT * FROM topics WHERE id = ?", (topic_id,)).fetchone()
    if not topic:
        return None
    
    meta = json.loads(topic['meta']) if topic['meta'] else {}
    name = topic['name']
    stage = topic['stage']
    progress = topic['progress']
    low = content.lower()
    
    # Detect intent
    if any(w in low for w in ['adresse', 'address', 'straße', 'str.', 'plz']):
        return {
            "message": "Adresse notiert. Ich aktualisiere das Dokument.",
            "proposal": {
                "type": "Update",
                "content": f"Adresse für {name} aktualisiert. Nächster Schritt?",
                "confidence": 85,
                "reason": "Adresse erhalten",
                "options": [
                    {"title": "Dokument finalisieren", "recommended": True, "description": "Adresse einsetzen und das Schreiben fertigstellen."},
                    {"title": "Noch etwas ändern", "recommended": False, "description": "Weitere Änderungen am Dokument vornehmen."}
                ]
            }
        }
    
    if any(w in low for w in ['senden', 'send', 'schick', 'raus', 'abschicken', 'los']):
        return {
            "message": f"Wird gesendet. Ich markiere den Step als erledigt.",
            "proposal": {
                "type": "Confirmation",
                "content": f"Gesendet-Bestätigung für {name}.",
                "confidence": 90,
                "reason": "Explizite Sende-Anweisung"
            }
        }
    
    if any(w in low for w in ['done', 'erledigt', 'fertig', 'geschafft', 'check']):
        _advance_next_step(db, topic_id)
        steps = db.execute("SELECT COUNT(*) as total, SUM(done) as done FROM steps WHERE topic_id = ?", (topic_id,)).fetchone()
        done = steps['done'] or 0
        total = steps['total'] or 0
        remaining = total - done
        return {
            "message": f"Step erledigt. {done}/{total} abgeschlossen. {'Noch ' + str(remaining) + ' Steps.' if remaining > 0 else 'Alle Steps fertig! Topic abgeschlossen.'}",
        }
    
    if any(w in low for w in ['skip', 'später', 'later', 'nicht jetzt', 'pause']):
        return {
            "message": f"Verstanden. {name} wird zurückgestellt. Ich erinnere dich morgen.",
        }
    
    if any(w in low for w in ['warum', 'why', 'wieso', 'explain', 'erklär']):
        return {
            "message": f"Stage: {stage} | Progress: {progress}% | {meta.get('contact', 'Kein Kontakt')}. Was genau willst du wissen?",
        }
    
    if any(w in low for w in ['priorität', 'priority', 'wichtig', 'urgent', 'dringend']):
        cost = meta.get('monthly_cost')
        potential = meta.get('potential')
        urgency_note = f"€{cost}/Monat laufende Kosten." if cost else (f"Potential: {potential}" if potential else "")
        return {
            "message": f"Aktuelle Priorität von {name}: Progress {progress}%. {urgency_note} Soll ich die Priorität ändern?",
            "proposal": {
                "type": "Priority",
                "content": "Priorität anpassen?",
                "confidence": 70,
                "reason": "Prioritäts-Frage erkannt",
                "options": [
                    {"title": "Hochstufen — diese Woche erledigen", "recommended": True, "description": "Deadline: Freitag. Tägliche Erinnerung."},
                    {"title": "Normal lassen", "recommended": False, "description": "Bleibt im regulären Flow."},
                    {"title": "Zurückstellen", "recommended": False, "description": "Erstmal andere Themen priorisieren."}
                ]
            }
        }
    
    if '?' in content:
        return {
            "message": f"Gute Frage. Ich habe dazu noch keine spezifische Info in diesem Topic. Kannst du mehr Kontext geben, dann recherchiere ich.",
        }
    
    # Default: acknowledge + ask for clarity
    return {
        "message": f"Notiert. Willst du das als nächsten Schritt für {name}, oder ist das Kontext für später?",
        "proposal": {
            "type": "Clarification",
            "content": "Wie soll ich das einordnen?",
            "confidence": 60,
            "reason": "Intent unklar",
            "options": [
                {"title": "Als nächsten Action Step", "recommended": True, "description": "Wird als nächste Aktion eingetragen."},
                {"title": "Als Kontext / Info", "recommended": False, "description": "Wird als Notiz zum Topic gespeichert."}
            ]
        }
    }

# ── Proposals ──

@app.post("/api/messages/{message_id}/proposals")
def add_proposal(message_id: int, p: ProposalCreate):
    db = get_db()
    cursor = db.execute(
        "INSERT INTO proposals (message_id, proposal_type, content, confidence, confidence_reason, options) VALUES (?,?,?,?,?,?)",
        (message_id, p.proposal_type, p.content, p.confidence, p.confidence_reason, json.dumps(p.options))
    )
    db.commit()
    db.close()
    return {"id": cursor.lastrowid, "status": "created"}

@app.post("/api/proposals/{proposal_id}/choose")
def choose_option(proposal_id: int, option: dict):
    db = get_db()
    chosen = option.get('option')
    db.execute("UPDATE proposals SET chosen_option = ? WHERE id = ?", (chosen, proposal_id))
    
    # Get context for smart response
    row = db.execute("""
        SELECT p.*, m.topic_id, t.name as topic_name
        FROM proposals p 
        JOIN messages m ON p.message_id = m.id
        JOIN topics t ON m.topic_id = t.id
        WHERE p.id = ?
    """, (proposal_id,)).fetchone()
    
    if row:
        topic_id = row['topic_id']
        opts = json.loads(row['options']) if row['options'] else []
        chosen_idx = ord(chosen) - 65 if chosen and len(chosen) == 1 else -1
        chosen_opt = opts[chosen_idx] if 0 <= chosen_idx < len(opts) else None
        
        # Generate contextual response
        response = generate_response(db, topic_id, row['topic_name'], row['proposal_type'], chosen, chosen_opt)
        
        # Post as Mia message
        cursor = db.execute("INSERT INTO messages (topic_id, sender, content, msg_type) VALUES (?,?,?,?)",
                   (topic_id, "mia", response['message'], "text"))
        msg_id = cursor.lastrowid
        
        # If response has a follow-up proposal
        if response.get('proposal'):
            p = response['proposal']
            db.execute("INSERT INTO proposals (message_id, proposal_type, content, confidence, confidence_reason, options) VALUES (?,?,?,?,?,?)",
                (msg_id, p['type'], p['content'], p.get('confidence'), p.get('reason'), json.dumps(p.get('options', []))))
        
        # Auto-advance steps if applicable
        if response.get('advance_step'):
            _advance_next_step(db, topic_id)
        
        db.execute("UPDATE topics SET updated_at = CURRENT_TIMESTAMP WHERE id = ?", (topic_id,))
    
    db.commit()
    db.close()
    
    notify("topic_update", {"topic_id": row['topic_id'] if row else ''})
    return {"status": "chosen"}


def _advance_next_step(db, topic_id):
    """Mark the next undone step as done."""
    step = db.execute("SELECT id FROM steps WHERE topic_id = ? AND done = 0 ORDER BY position LIMIT 1", (topic_id,)).fetchone()
    if step:
        db.execute("UPDATE steps SET done = 1 WHERE id = ?", (step['id'],))
        _recalc_progress(db, topic_id)


def generate_response(db, topic_id, topic_name, proposal_type, chosen, chosen_opt):
    """Generate a contextual Mia response based on the choice made."""
    title = chosen_opt['title'] if chosen_opt else f"Option {chosen}"
    desc = chosen_opt.get('description', '') if chosen_opt else ''
    has_draft = bool(chosen_opt.get('draft')) if chosen_opt else False
    recommended = chosen_opt.get('recommended', False) if chosen_opt else False
    
    # Get topic meta
    topic = db.execute("SELECT meta, stage FROM topics WHERE id = ?", (topic_id,)).fetchone()
    meta = json.loads(topic['meta']) if topic else {}
    email = meta.get('email', '')
    
    # Context-aware responses based on proposal type and topic
    if proposal_type == "Ready to Send" and chosen == "A":
        return {
            "message": f"Verstanden. Email an {email} wird vorbereitet. Draft ist oben — prüf Subject Line und Attachments, dann sende ich.",
            "advance_step": True,
            "proposal": {
                "type": "Action",
                "content": f"Email bereit. Prüfe den Draft und bestätige mit 'Senden'.",
                "confidence": 90,
                "reason": "Draft + Attachments vorhanden",
                "options": [
                    {"title": "Senden bestätigen", "recommended": True, "description": f"Sendet die Email an {email} mit CoverLetter.pdf + CV.pdf."},
                    {"title": "Subject Line ändern", "recommended": False, "description": "Aktuelle Subject Line überarbeiten bevor gesendet wird."},
                    {"title": "Zurückstellen", "recommended": False, "description": "Nicht jetzt senden. Topic bleibt offen."}
                ]
            }
        }
    
    if proposal_type == "Recommendation" and chosen == "A":
        if has_draft:
            return {
                "message": f"Option {chosen} gewählt: {title}. Draft liegt oben — kannst du direkt kopieren oder anpassen. Nächster Step wird markiert.",
                "advance_step": True,
                "proposal": {
                    "type": "Next Step",
                    "content": "Draft ist bereit. Was jetzt?",
                    "confidence": 85,
                    "reason": "Draft vorhanden, nächster Schritt klar",
                    "options": [
                        {"title": "Draft übernehmen und ausführen", "recommended": True, "description": "Nutze den Draft wie er ist. Nächster Step."},
                        {"title": "Draft anpassen", "recommended": False, "description": "Änderungen am Draft vornehmen."}
                    ]
                }
            }
        return {
            "message": f"Gut. {title} — ich bereite den nächsten Schritt vor.",
            "advance_step": True
        }
    
    if proposal_type == "Urgency" and chosen == "A":
        return {
            "message": f"Kündigungsschreiben steht als Draft oben. Du brauchst: (1) Name + Adresse des Kindergartens, (2) Ausdrucken, (3) Unterschreiben, (4) Einschreiben bei der Post. Jeder Tag = anteilig €15 verbrannt.",
            "advance_step": True,
            "proposal": {
                "type": "Blocker",
                "content": "Ich brauche den Namen und die Adresse des Kindergartens um das Schreiben zu finalisieren.",
                "confidence": 95,
                "reason": "Ohne Adresse kein Brief",
                "options": [
                    {"title": "Adresse eingeben", "recommended": True, "description": "Schreib den Kindergarten-Namen und die Adresse hier rein."},
                    {"title": "Im Vertrag nachschauen", "recommended": False, "description": "Vertrag raussuchen, Adresse + Kündigungsfrist prüfen."}
                ]
            }
        }
    
    if proposal_type == "Decision":
        return {
            "message": f"Entscheidung: {title}. Wird umgesetzt.",
            "advance_step": True,
            "proposal": {
                "type": "Execution",
                "content": f"Umsetzung von Option {chosen} läuft. Ich update den Status.",
                "confidence": 80,
                "reason": "Entscheidung getroffen"
            }
        }
    
    if proposal_type == "Solution" and chosen == "A":
        return {
            "message": f"{title} — ich starte die Umsetzung. Nächster Step wird freigeschaltet.",
            "advance_step": True
        }
    
    if proposal_type == "Blocker":
        if chosen == "A":
            return {"message": f"Warte auf deinen Input: {title}. Sobald du es hier postest, mache ich weiter."}
        return {"message": f"Verstanden: {title}. Topic wird entsprechend priorisiert."}
    
    if proposal_type == "Status":
        return {"message": f"Acknowledged. Weiter beobachten."}
    
    # Fallback for non-A choices
    if chosen != "A":
        return {
            "message": f"Option {chosen} gewählt: {title}. {desc[:120]}{'...' if len(desc)>120 else ''}" if desc else f"Option {chosen}: {title}. Wird berücksichtigt.",
            "advance_step": False
        }
    
    # Generic fallback
    return {
        "message": f"Verstanden. {title}. Nächster Schritt wird vorbereitet.",
        "advance_step": True
    }

# ── Votes ──

@app.post("/api/proposals/{proposal_id}/vote")
def vote_proposal(proposal_id: int, v: VoteCreate):
    db = get_db()
    db.execute("INSERT INTO votes (proposal_id, direction) VALUES (?,?)", (proposal_id, v.direction))
    
    # Update trust score for 'main' agent
    if v.direction == "up":
        db.execute("UPDATE trust_scores SET up_votes = up_votes + 1, total_votes = total_votes + 1, score = MIN(100, score + 1), updated_at = CURRENT_TIMESTAMP WHERE agent = 'main'")
    else:
        db.execute("UPDATE trust_scores SET down_votes = down_votes + 1, total_votes = total_votes + 1, score = MAX(0, score - 2), updated_at = CURRENT_TIMESTAMP WHERE agent = 'main'")
    
    db.commit()
    db.close()
    
    notify("trust_update", {"proposal_id": proposal_id, "direction": v.direction})
    return {"status": "voted"}

# ── Steps ──

@app.post("/api/topics/{topic_id}/steps")
def add_step(topic_id: str, s: StepCreate):
    db = get_db()
    pos = db.execute("SELECT COALESCE(MAX(position),0)+1 FROM steps WHERE topic_id = ?", (topic_id,)).fetchone()[0]
    cursor = db.execute("INSERT INTO steps (topic_id, label, done, position) VALUES (?,?,?,?)",
                        (topic_id, s.label, int(s.done), pos))
    # Recalc progress
    _recalc_progress(db, topic_id)
    db.commit()
    db.close()
    return {"id": cursor.lastrowid}

@app.patch("/api/steps/{step_id}")
def toggle_step(step_id: int):
    db = get_db()
    db.execute("UPDATE steps SET done = 1 - done WHERE id = ?", (step_id,))
    row = db.execute("SELECT topic_id FROM steps WHERE id = ?", (step_id,)).fetchone()
    topic_id = None
    if row:
        topic_id = row['topic_id']
        _recalc_progress(db, topic_id)
    db.commit()
    db.close()
    
    if topic_id:
        notify("topic_update", {"topic_id": topic_id})
    return {"status": "toggled"}

def _recalc_progress(db, topic_id):
    row = db.execute("SELECT COUNT(*) as total, SUM(done) as done FROM steps WHERE topic_id = ?", (topic_id,)).fetchone()
    if row['total'] > 0:
        pct = int((row['done'] / row['total']) * 100)
        db.execute("UPDATE topics SET progress = ? WHERE id = ?", (pct, topic_id))

# ── Documents & Connections ──

@app.post("/api/topics/{topic_id}/documents")
def add_document(topic_id: str, doc: dict):
    db = get_db()
    db.execute("INSERT INTO documents (topic_id, name, path, url, doc_type) VALUES (?,?,?,?,?)",
               (topic_id, doc['name'], doc.get('path'), doc.get('url'), doc.get('doc_type', 'file')))
    db.commit()
    db.close()
    return {"status": "added"}

@app.post("/api/connections")
def add_connection(conn: dict):
    db = get_db()
    db.execute("INSERT INTO connections (from_topic, to_topic, relation) VALUES (?,?,?)",
               (conn['from'], conn['to'], conn.get('relation')))
    db.commit()
    db.close()
    return {"status": "connected"}

# ── Trust ──

@app.get("/api/trust")
def get_trust():
    db = get_db()
    rows = db.execute("SELECT * FROM trust_scores ORDER BY agent").fetchall()
    db.close()
    return [dict(r) for r in rows]

# ── Eval ──

@app.post("/api/eval")
def submit_eval(responses: List[EvalResponse]):
    db = get_db()
    today = datetime.now().strftime("%Y-%m-%d")
    for r in responses:
        db.execute("INSERT INTO eval_responses (question_id, answers, session_date) VALUES (?,?,?)",
                   (r.question_id, json.dumps(r.answers), today))
    db.commit()
    db.close()
    return {"status": "saved", "date": today}

@app.get("/api/eval/history")
def eval_history(days: int = 7):
    db = get_db()
    rows = db.execute("SELECT * FROM eval_responses ORDER BY created_at DESC LIMIT ?", (days * 10,)).fetchall()
    db.close()
    return [dict(r) for r in rows]

# ── Pipeline Stats ──

@app.get("/api/pipeline")
def pipeline_stats():
    db = get_db()
    stages = {}
    stage_order = ['research', 'systems', 'content', 'revenue']
    
    for stage in stage_order:
        row = db.execute("SELECT COUNT(*) as count, AVG(progress) as avg_progress FROM topics WHERE stage = ?", (stage,)).fetchone()
        stages[stage] = {"count": row['count'], "avg_progress": row['avg_progress'] or 0}
    
    total_votes = db.execute("SELECT COUNT(*) as c FROM votes").fetchone()['c']
    outcomes = db.execute("SELECT COUNT(*) as c FROM topics WHERE progress = 100").fetchone()['c']
    
    # Cross-stage connections: count how many topics in each stage connect to topics in the next stage
    flows = {}
    for i in range(len(stage_order) - 1):
        src_stage = stage_order[i]
        dst_stage = stage_order[i+1]
        flow = db.execute("""
            SELECT COUNT(DISTINCT c.from_topic) as connected
            FROM connections c
            JOIN topics t1 ON c.from_topic = t1.id
            JOIN topics t2 ON c.to_topic = t2.id
            WHERE t1.stage = ? AND t2.stage = ?
        """, (src_stage, dst_stage)).fetchone()
        
        # Also check reverse direction (downstream topics linking back to upstream)
        flow_rev = db.execute("""
            SELECT COUNT(DISTINCT c.from_topic) as connected
            FROM connections c
            JOIN topics t1 ON c.from_topic = t1.id
            JOIN topics t2 ON c.to_topic = t2.id
            WHERE t1.stage = ? AND t2.stage = ?
        """, (dst_stage, src_stage)).fetchone()
        
        total_flow = (flow['connected'] or 0) + (flow_rev['connected'] or 0)
        src_count = stages[src_stage]['count']
        conversion = round(total_flow / src_count * 100) if src_count > 0 else 0
        
        flows[f"{src_stage}_to_{dst_stage}"] = {
            "connected": total_flow,
            "source_count": src_count,
            "conversion_pct": conversion
        }
    
    # Findings stats per research line
    findings_by_line = db.execute("""
        SELECT research_line, COUNT(*) as count, 
               SUM(CASE WHEN status = 'alive' THEN 1 ELSE 0 END) as alive,
               ROUND(AVG(confidence), 2) as avg_conf,
               ROUND(SUM(compound_score), 1) as total_score
        FROM findings WHERE research_line IS NOT NULL
        GROUP BY research_line ORDER BY total_score DESC LIMIT 5
    """).fetchall()
    
    # Orphan detection: topics with 0 connections to other stages for >7 days
    orphans = db.execute("""
        SELECT t.id, t.name, t.stage, t.created_at
        FROM topics t
        WHERE t.id NOT IN (SELECT from_topic FROM connections)
        AND t.id NOT IN (SELECT to_topic FROM connections)
        AND julianday('now') - julianday(t.created_at) > 7
        AND t.stage IN ('research', 'systems', 'content')
    """).fetchall()
    
    db.close()
    
    return {
        "stages": stages,
        "total_items": sum(s['count'] for s in stages.values()),
        "outcomes": outcomes,
        "total_votes": total_votes,
        "flows": flows,
        "research_lines": [dict(r) for r in findings_by_line],
        "orphans": [{"id": o['id'], "name": o['name'], "stage": o['stage']} for o in orphans]
    }

@app.get("/api/pipeline/detail")
def pipeline_detail():
    """Full pipeline data for cross-stage view: topics with connections and findings per stage."""
    db = get_db()
    stage_order = ['research', 'systems', 'content', 'revenue']
    result = {}
    
    for stage in stage_order:
        topics = db.execute("""
            SELECT t.id, t.name, t.stage, t.progress, t.state, t.created_at
            FROM topics t WHERE t.stage = ?
            ORDER BY t.progress DESC, t.name
        """, (stage,)).fetchall()
        
        topic_list = []
        for t in topics:
            td = dict(t)
            
            # Connections out (downstream)
            conns_out = db.execute("""
                SELECT t2.name, t2.stage, c.relation
                FROM connections c JOIN topics t2 ON c.to_topic = t2.id
                WHERE c.from_topic = ?
            """, (t['id'],)).fetchall()
            
            # Connections in (upstream)
            conns_in = db.execute("""
                SELECT t2.name, t2.stage, c.relation
                FROM connections c JOIN topics t2 ON c.from_topic = t2.id
                WHERE c.to_topic = ?
            """, (t['id'],)).fetchall()
            
            td['connections_out'] = [dict(c) for c in conns_out]
            td['connections_in'] = [dict(c) for c in conns_in]
            
            # Findings count
            findings = db.execute(
                "SELECT COUNT(*) as c, SUM(CASE WHEN status='alive' THEN 1 ELSE 0 END) as alive FROM findings WHERE topic_id = ?",
                (t['id'],)
            ).fetchone()
            td['findings_total'] = findings['c'] or 0
            td['findings_alive'] = findings['alive'] or 0
            
            topic_list.append(td)
        
        result[stage] = topic_list
    
    db.close()
    return result

# ── File Viewer ──

@app.get("/api/file")
def read_file(path: str):
    """Read a workspace file and return its content."""
    import os
    base = "/Users/florianziesche/.openclaw/workspace"
    full = os.path.normpath(os.path.join(base, path))
    if not full.startswith(base):
        raise HTTPException(403, "Access denied")
    if not os.path.exists(full):
        raise HTTPException(404, "File not found")
    try:
        with open(full, 'r') as f:
            content = f.read(50000)
        return {"path": path, "content": content, "truncated": len(content) >= 50000}
    except Exception as e:
        raise HTTPException(500, str(e))

from fastapi.responses import FileResponse, HTMLResponse
import mimetypes

@app.get("/view/{path:path}")
def view_file(path: str):
    """Serve workspace files directly in browser."""
    import os
    base = "/Users/florianziesche/.openclaw/workspace"
    full = os.path.normpath(os.path.join(base, path))
    if not full.startswith(base):
        raise HTTPException(403, "Access denied")
    if not os.path.exists(full):
        raise HTTPException(404, "File not found")
    
    mime, _ = mimetypes.guess_type(full)
    
    # PDFs, images, HTML — serve directly as-is
    if mime and (mime.startswith('image/') or mime == 'application/pdf' or mime == 'text/html'):
        return FileResponse(full, media_type=mime)
    
    # Text/code files — render in a minimal dark viewer
    try:
        with open(full, 'r') as f:
            content = f.read(100000)
    except:
        return FileResponse(full)
    
    import html as html_mod
    escaped = html_mod.escape(content)
    return HTMLResponse(f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>{html_mod.escape(path)}</title>
<style>
body{{background:#0a0a0a;color:#ccc;font:13px/1.7 'SF Mono',Menlo,monospace;padding:20px 30px;margin:0}}
.path{{color:#555;font-size:11px;margin-bottom:12px;padding-bottom:8px;border-bottom:1px solid #1e1e1e}}
pre{{white-space:pre-wrap;word-wrap:break-word}}
</style></head><body>
<div class="path">{html_mod.escape(path)}</div>
<pre>{escaped}</pre>
</body></html>""")

# ── Topic CRUD (extended) ──

class TopicUpdate(BaseModel):
    name: Optional[str] = None
    stage: Optional[str] = None
    folder_id: Optional[str] = None
    progress: Optional[int] = None
    state: Optional[str] = None
    meta: Optional[dict] = None

@app.patch("/api/topics/{topic_id}")
def update_topic(topic_id: str, t: TopicUpdate):
    db = get_db()
    updates = []
    params = []
    if t.name is not None: updates.append("name=?"); params.append(t.name)
    if t.stage is not None: updates.append("stage=?"); params.append(t.stage)
    if t.folder_id is not None: updates.append("folder_id=?"); params.append(t.folder_id if t.folder_id != "" else None)
    if t.progress is not None: updates.append("progress=?"); params.append(t.progress)
    if t.state is not None: updates.append("state=?"); params.append(t.state)
    if t.meta is not None: updates.append("meta=?"); params.append(json.dumps(t.meta))
    if updates:
        updates.append("updated_at=CURRENT_TIMESTAMP")
        params.append(topic_id)
        db.execute(f"UPDATE topics SET {','.join(updates)} WHERE id=?", params)
        db.commit()
    db.close()
    notify("topic_update", {"topic_id": topic_id})
    return {"status": "updated"}

@app.delete("/api/topics/{topic_id}")
def delete_topic(topic_id: str):
    db = get_db()
    db.execute("DELETE FROM messages WHERE topic_id = ?", (topic_id,))
    db.execute("DELETE FROM steps WHERE topic_id = ?", (topic_id,))
    db.execute("DELETE FROM documents WHERE topic_id = ?", (topic_id,))
    db.execute("DELETE FROM connections WHERE from_topic = ? OR to_topic = ?", (topic_id, topic_id))
    db.execute("DELETE FROM events WHERE topic_id = ?", (topic_id,))
    db.execute("DELETE FROM topics WHERE id = ?", (topic_id,))
    db.commit()
    db.close()
    notify("topic_update", {"topic_id": topic_id})
    return {"status": "deleted"}

# ── File Upload ──

UPLOAD_DIR = Path(__file__).parent.parent / "uploads"
UPLOAD_DIR.mkdir(exist_ok=True)

from fastapi import UploadFile, File, Form

@app.post("/api/topics/{topic_id}/upload")
async def upload_file(topic_id: str, file: UploadFile = File(...), kind: str = Form("doc")):
    """Upload a file and attach it to a topic. kind = 'doc' or 'ref'"""
    # Save file
    safe_name = file.filename.replace("/", "_").replace("\\", "_")
    topic_dir = UPLOAD_DIR / topic_id
    topic_dir.mkdir(exist_ok=True)
    file_path = topic_dir / safe_name
    
    content = await file.read()
    with open(file_path, "wb") as f:
        f.write(content)
    
    # Determine doc_type from extension
    ext = safe_name.rsplit(".", 1)[-1].lower() if "." in safe_name else "file"
    doc_type_map = {"pdf": "pdf", "html": "html", "md": "md", "txt": "txt", "doc": "doc", "docx": "doc"}
    doc_type = doc_type_map.get(ext, "file")
    
    # Add to documents table
    db = get_db()
    rel_path = f"projects/workbench/uploads/{topic_id}/{safe_name}"
    db.execute("INSERT INTO documents (topic_id, name, path, doc_type, kind) VALUES (?,?,?,?,?)",
               (topic_id, safe_name, rel_path, doc_type, kind))
    
    # Log event
    db.execute("INSERT INTO events (topic_id, event_type, detail) VALUES (?,?,?)",
               (topic_id, "file_uploaded", json.dumps({"name": safe_name, "kind": kind, "size": len(content)})))
    
    db.commit()
    db.close()
    
    notify("topic_update", {"topic_id": topic_id})
    return {"status": "uploaded", "name": safe_name, "path": rel_path, "size": len(content)}

@app.delete("/api/topics/{topic_id}/documents/{doc_id}")
def delete_document(topic_id: str, doc_id: int, delete_file: bool = True):
    """Remove a document/reference. Optionally deletes the file from disk."""
    db = get_db()
    doc = db.execute("SELECT * FROM documents WHERE id = ? AND topic_id = ?", (doc_id, topic_id)).fetchone()
    if not doc:
        db.close()
        raise HTTPException(404, "Document not found")
    
    doc_name = doc['name']
    doc_path = doc['path']
    
    # Delete from DB
    db.execute("DELETE FROM documents WHERE id = ?", (doc_id,))
    db.execute("INSERT INTO events (topic_id, event_type, detail) VALUES (?,?,?)",
               (topic_id, "document_deleted", json.dumps({"name": doc_name, "path": doc_path})))
    db.commit()
    db.close()
    
    # Delete file from disk if requested and path exists
    file_deleted = False
    if delete_file and doc_path:
        # Resolve relative to workspace
        full_path = Path(doc_path)
        if not full_path.is_absolute():
            full_path = Path(__file__).parent.parent.parent.parent / doc_path  # workspace root
        if full_path.exists():
            full_path.unlink()
            file_deleted = True
    
    notify("topic_update", {"topic_id": topic_id})
    return {"status": "deleted", "name": doc_name, "file_deleted": file_deleted}

@app.get("/api/topics/{topic_id}/documents")
def list_documents(topic_id: str):
    """List all documents/references for a topic."""
    db = get_db()
    rows = db.execute("SELECT * FROM documents WHERE topic_id = ? ORDER BY id", (topic_id,)).fetchall()
    db.close()
    return [dict(r) for r in rows]

@app.post("/api/topics/{topic_id}/add-reference")
def add_reference(topic_id: str, body: dict):
    """Add a URL or path as a reference document."""
    db = get_db()
    name = body.get("name", "Reference")
    url = body.get("url")
    path = body.get("path")
    doc_type = body.get("doc_type", "ref")
    
    db.execute("INSERT INTO documents (topic_id, name, path, url, doc_type, kind) VALUES (?,?,?,?,?,?)",
               (topic_id, name, path, url, doc_type, "ref"))
    db.execute("INSERT INTO events (topic_id, event_type, detail) VALUES (?,?,?)",
               (topic_id, "reference_added", json.dumps({"name": name})))
    db.commit()
    db.close()
    
    notify("topic_update", {"topic_id": topic_id})
    return {"status": "added"}

# ── Corrections Engine ──

class CorrectionCreate(BaseModel):
    rule: str
    category: str = "general"  # design, content, process, tone, facts
    wrong: str = ""
    right: str = ""
    source_topic: Optional[str] = None
    severity: int = 2  # 1=minor, 2=standard, 3=critical

@app.get("/api/corrections")
def list_corrections(category: Optional[str] = None, active: bool = True):
    db = get_db()
    q = "SELECT * FROM corrections WHERE 1=1"
    params = []
    if category:
        q += " AND category = ?"; params.append(category)
    if active:
        q += " AND active = 1"
    q += " ORDER BY severity DESC, violation_count DESC"
    rows = db.execute(q, params).fetchall()
    db.close()
    return [dict(r) for r in rows]

@app.post("/api/corrections")
def create_correction(c: CorrectionCreate):
    db = get_db()
    cid = db.execute(
        "INSERT INTO corrections (rule, category, wrong, rght, source_topic, severity) VALUES (?,?,?,?,?,?)",
        (c.rule, c.category, c.wrong, c.right, c.source_topic, c.severity)
    ).lastrowid
    db.commit()
    db.close()
    notify("correction_update", {"id": cid})
    return {"id": cid, "status": "created"}

@app.post("/api/corrections/{correction_id}/violation")
def record_violation(correction_id: int, body: dict):
    """Record that this correction was violated in an output."""
    db = get_db()
    db.execute("UPDATE corrections SET violation_count = violation_count + 1, last_violated = CURRENT_TIMESTAMP WHERE id = ?",
               (correction_id,))
    topic_id = body.get("topic_id")
    if topic_id:
        db.execute("INSERT INTO events (topic_id, event_type, detail) VALUES (?,?,?)",
                   (topic_id, "correction_violation", json.dumps({"correction_id": correction_id})))
    db.commit()
    db.close()
    return {"status": "recorded"}

# ── Pre-Flight Engine (3-Layer) ──

import re as _re

def _layer1_regex_check(text: str, correction: dict) -> dict:
    """Layer 1: Regex pattern matching against correction rules. <50ms."""
    try:
        patterns = json.loads(correction.get('patterns', '[]') or '[]')
    except (TypeError, KeyError):
        patterns = []
    try:
        output_types = json.loads(correction.get('output_types', '["all"]') or '["all"]')
    except (TypeError, KeyError):
        output_types = ["all"]
    
    result = {"status": "pass", "matches": [], "layer": 1}
    
    if not patterns:
        # No patterns defined — skip (will be caught by Layer 3 LLM-Judge if needed)
        result["status"] = "skip"
        return result
    
    for pattern in patterns:
        try:
            found = _re.findall(pattern, text, _re.IGNORECASE)
            if found:
                result["matches"].extend(found[:3])  # Cap at 3 matches per pattern
                result["status"] = "fail"
        except _re.error:
            continue  # Invalid regex — skip silently
    
    return result

def _layer2_structural_check(text: str, output_type: str, meta: dict) -> list:
    """Layer 2: Output-type-specific structural validators. <100ms."""
    checks = []
    
    if not text.strip():
        checks.append({"rule": "Output ist leer", "status": "fail", "layer": 2, "category": "structural"})
        return checks
    
    word_count = len(text.split())
    
    # Universal checks
    if word_count < 5:
        checks.append({"rule": "Output zu kurz (<5 Wörter)", "status": "warn", "layer": 2, "category": "structural"})
    
    # Email-specific
    if output_type == "email":
        # Has greeting?
        has_greeting = bool(_re.search(r'^(hi|hello|hallo|dear|sehr geehrte|liebe|guten)', text, _re.IGNORECASE | _re.MULTILINE))
        if not has_greeting:
            checks.append({"rule": "Email: Anrede fehlt", "status": "warn", "layer": 2, "category": "structural"})
        
        # Has sign-off?
        has_signoff = bool(_re.search(r'(best|regards|grüße|gruß|viele grüße|beste grüße|florian|mfg)\s*$', text, _re.IGNORECASE | _re.MULTILINE))
        if not has_signoff:
            checks.append({"rule": "Email: Signatur/Grußformel fehlt", "status": "warn", "layer": 2, "category": "structural"})
        
        # Length check
        if word_count > 500:
            checks.append({"rule": "Email: Zu lang (>500 Wörter)", "status": "warn", "layer": 2, "category": "structural"})
        if word_count < 20:
            checks.append({"rule": "Email: Zu kurz (<20 Wörter)", "status": "warn", "layer": 2, "category": "structural"})
    
    # LinkedIn-specific
    if output_type == "linkedin":
        if len(text) > 3000:
            checks.append({"rule": "LinkedIn: Über 3000 Zeichen", "status": "fail", "layer": 2, "category": "structural"})
        
        # Has CTA?
        has_cta = bool(_re.search(r'(\?|comment|share|follow|what do you think|thoughts\??|agree\??|dm me)', text, _re.IGNORECASE))
        if not has_cta:
            checks.append({"rule": "LinkedIn: Kein Call-to-Action", "status": "warn", "layer": 2, "category": "structural"})
    
    # Blog-specific
    if output_type == "blog":
        if word_count < 300:
            checks.append({"rule": "Blog: Zu kurz (<300 Wörter)", "status": "warn", "layer": 2, "category": "structural"})
        
        # Has headings?
        has_headings = bool(_re.search(r'^#{1,3}\s|^[A-Z].*:$', text, _re.MULTILINE))
        if not has_headings and word_count > 200:
            checks.append({"rule": "Blog: Keine Überschriften bei >200 Wörtern", "status": "warn", "layer": 2, "category": "structural"})
    
    # Report-specific
    if output_type == "report":
        # Has sources?
        has_sources = bool(_re.search(r'(source|quelle|https?://|according to|\[\d+\])', text, _re.IGNORECASE))
        if not has_sources and word_count > 100:
            checks.append({"rule": "Report: Keine Quellen angegeben", "status": "warn", "layer": 2, "category": "structural"})
        
        # Has numbers with context?
        has_unverified_numbers = _re.findall(r'\b\d{2,}\s*%', text)
        if has_unverified_numbers and not has_sources:
            checks.append({"rule": "Report: Prozentzahlen ohne Quellenangabe", "status": "fail", "layer": 2, "category": "structural"})
    
    # Website-specific
    if output_type == "website":
        # Check for non-brand colors
        non_brand = _re.findall(r'#(?!0a0a0a|141414|1a1a1a|1e1e1e|2a2a2a|d4a853|c8aa50|c47070|ececec|8e8e8e|555|fff|000)[0-9a-fA-F]{3,6}\b', text)
        if non_brand:
            checks.append({"rule": f"Website: Nicht-Brand Farben gefunden: {', '.join(non_brand[:3])}", "status": "fail", "layer": 2, "category": "structural"})
    
    return checks

@app.get("/api/preflight/{topic_id}")
def preflight_check(topic_id: str):
    """3-Layer Pre-Flight Engine.
    Layer 1: Regex pattern matching (<50ms, deterministic)
    Layer 2: Structural validators (<100ms, output-type-specific)
    Layer 3: LLM-as-Judge (2-3s, only for REVIEW/CONFIRM — not yet implemented)
    """
    db = get_db()
    topic = db.execute("SELECT * FROM topics WHERE id = ?", (topic_id,)).fetchone()
    if not topic:
        db.close()
        raise HTTPException(404, "Topic not found")
    
    # Get the last Mia message as the "output" to check
    last_output = db.execute(
        "SELECT content FROM messages WHERE topic_id = ? AND sender = 'mia' ORDER BY created_at DESC LIMIT 1",
        (topic_id,)
    ).fetchone()
    output_text = last_output['content'] if last_output else ""
    output_lower = output_text.lower()
    
    meta = json.loads(topic['meta'] or '{}')
    output_type = meta.get('output_type', 'general')
    
    corrections = db.execute("SELECT * FROM corrections WHERE active = 1 ORDER BY severity DESC").fetchall()
    standards = db.execute("SELECT * FROM quality_standards WHERE active = 1").fetchall()
    
    checks = []
    passed = 0
    warned = 0
    failed = 0
    skipped = 0
    
    # ── Layer 1: Regex Pattern Matching ──
    for c in corrections:
        # Check if this correction applies to the output type
        try:
            c_output_types = json.loads(c['output_types'] or '["all"]')
        except (KeyError, TypeError):
            c_output_types = ["all"]
        if "all" not in c_output_types and output_type not in c_output_types:
            continue
        
        result = _layer1_regex_check(output_lower, dict(c))
        
        if result["status"] == "skip":
            # No patterns — fall back to simple string match on 'wrong' field
            if c['wrong'] and c['wrong'].strip():
                wrong_terms = [t.strip().lower() for t in c['wrong'].split(',') if t.strip() and len(t.strip()) > 2]
                matched = [t for t in wrong_terms if t in output_lower]
                if matched:
                    status = "fail" if c['severity'] >= 2 else "warn"
                    result = {"status": status, "matches": matched[:3], "layer": 1}
                else:
                    result = {"status": "pass", "matches": [], "layer": 1}
            else:
                skipped += 1
                continue
        
        status = result["status"]
        if status == "pass": passed += 1
        elif status == "warn": warned += 1
        else: failed += 1
        
        check_entry = {
            "id": c['id'], "type": "correction", "rule": c['rule'],
            "category": c['category'], "severity": c['severity'],
            "status": status, "wrong": c['wrong'], "right": c['rght'],
            "layer": result.get("layer", 1)
        }
        if result.get("matches"):
            check_entry["matches"] = result["matches"]
        checks.append(check_entry)
    
    # ── Layer 2: Structural Validators ──
    structural_checks = _layer2_structural_check(output_text, output_type, meta)
    for sc in structural_checks:
        if sc["status"] == "pass": passed += 1
        elif sc["status"] == "warn": warned += 1
        else: failed += 1
        checks.append({
            "id": None, "type": "structural", "rule": sc["rule"],
            "category": sc["category"], "severity": 2 if sc["status"] == "fail" else 1,
            "status": sc["status"], "layer": 2
        })
    
    # ── Layer 2b: Standards Check ──
    for s in standards:
        if s['output_type'] not in (output_type, 'general'):
            continue
        status = "pass" if output_text else "warn"
        if status == "pass": passed += 1
        else: warned += 1
        checks.append({
            "id": s['id'], "type": "standard", "rule": s['rule'],
            "category": s['category'], "status": status, "layer": 2
        })
    
    # ── Layer 3: LLM-as-Judge (placeholder — activated by query param) ──
    # Will be implemented in Block 3 (Mia-Bridge)
    
    total = passed + warned + failed
    overall = "pass" if failed == 0 and warned == 0 else ("fail" if failed > 0 else "warn")
    
    db.close()
    return {
        "topic_id": topic_id,
        "output_type": output_type,
        "total_checks": total,
        "skipped": skipped,
        "passed": passed,
        "warned": warned,
        "failed": failed,
        "overall": overall,
        "has_output": bool(output_text),
        "layers_run": [1, 2],
        "checks": checks
    }

@app.get("/api/trust/skills")
def get_trust_skills():
    """Get granular trust scores per skill."""
    db = get_db()
    rows = db.execute("SELECT * FROM trust_skills ORDER BY skill").fetchall()
    db.close()
    return [dict(r) for r in rows]

@app.post("/api/trust/skills/{skill}/feedback")
def skill_feedback(skill: str, body: dict):
    """Record feedback for a specific skill. direction: up/down, weight: 1-3"""
    direction = body.get("direction", "up")
    weight = body.get("weight", 1)
    detail = body.get("detail", "")
    topic_id = body.get("topic_id")
    
    db = get_db()
    
    # Upsert skill
    existing = db.execute("SELECT * FROM trust_skills WHERE skill = ?", (skill,)).fetchone()
    if not existing:
        db.execute("INSERT INTO trust_skills (skill, score, total, up, down) VALUES (?,50,0,0,0)", (skill,))
    
    # Bayesian Trust Update
    # score = (C × prior + Σ ratings) / (C + n)
    # C = 10 (confidence parameter), prior = 50 (neutral)
    # Each up = +1, each down = -1.5 (asymmetric — mistakes cost more)
    C = 10
    PRIOR = 50
    
    if direction == "up":
        db.execute("UPDATE trust_skills SET up = up + 1, total = total + 1, updated_at = CURRENT_TIMESTAMP WHERE skill = ?", (skill,))
    else:
        db.execute("UPDATE trust_skills SET down = down + 1, total = total + 1, updated_at = CURRENT_TIMESTAMP WHERE skill = ?", (skill,))
    
    # Recalculate Bayesian score
    # Formula: score = (C × prior + observed_score × n) / (C + n)
    # observed_score = 100 × (up / (up + down×1.5)) — asymmetric, downs weigh more
    row = db.execute("SELECT up, down, total FROM trust_skills WHERE skill = ?", (skill,)).fetchone()
    if row:
        up = row['up']
        down = row['down']
        n = row['total']
        # Observed quality: ratio of positive to total (with asymmetric down-weighting)
        weighted_total = up + down * 1.5
        observed_score = (up / weighted_total * 100) if weighted_total > 0 else PRIOR
        bayesian_score = (C * PRIOR + observed_score * n) / (C + n)
        bayesian_score = max(0, min(100, round(bayesian_score)))
        db.execute("UPDATE trust_skills SET score = ? WHERE skill = ?", (bayesian_score, skill))
    
    # Log event
    if topic_id:
        db.execute("INSERT INTO events (topic_id, event_type, detail) VALUES (?,?,?)",
                   (topic_id, "trust_feedback", json.dumps({"skill": skill, "direction": direction, "weight": weight, "detail": detail})))
    
    db.commit()
    db.close()
    notify("trust_update", {"skill": skill, "direction": direction})
    return {"status": "recorded"}

# ── Events / Audit Log ──

@app.get("/api/events/{topic_id}")
def get_events(topic_id: str, limit: int = 50):
    db = get_db()
    rows = db.execute("SELECT * FROM events WHERE topic_id = ? ORDER BY created_at DESC LIMIT ?",
                      (topic_id, limit)).fetchall()
    db.close()
    return [dict(r) for r in rows]

@app.post("/api/events")
def create_event(body: dict):
    db = get_db()
    db.execute("INSERT INTO events (topic_id, event_type, detail) VALUES (?,?,?)",
               (body['topic_id'], body['event_type'], json.dumps(body.get('detail', {}))))
    db.commit()
    db.close()
    return {"status": "created"}

# ── Folders ──

class FolderCreate(BaseModel):
    id: str
    name: str
    parent_id: Optional[str] = None
    color: Optional[str] = None
    icon: Optional[str] = None

class FolderUpdate(BaseModel):
    name: Optional[str] = None
    parent_id: Optional[str] = None
    color: Optional[str] = None
    icon: Optional[str] = None
    position: Optional[int] = None
    collapsed: Optional[bool] = None

@app.get("/api/folders")
def list_folders():
    db = get_db()
    rows = db.execute("SELECT * FROM folders ORDER BY position, created_at").fetchall()
    db.close()
    return [dict(r) for r in rows]

@app.post("/api/folders")
def create_folder(f: FolderCreate):
    db = get_db()
    pos = db.execute("SELECT COALESCE(MAX(position),0)+1 FROM folders WHERE parent_id IS ? ", (f.parent_id,)).fetchone()[0]
    db.execute("INSERT INTO folders (id, name, parent_id, position, color, icon) VALUES (?,?,?,?,?,?)",
               (f.id, f.name, f.parent_id, pos, f.color, f.icon))
    db.commit()
    db.close()
    notify("folder_update", {})
    return {"id": f.id, "status": "created"}

@app.patch("/api/folders/{folder_id}")
def update_folder(folder_id: str, f: FolderUpdate):
    db = get_db()
    updates = []
    params = []
    if f.name is not None: updates.append("name=?"); params.append(f.name)
    if f.parent_id is not None: updates.append("parent_id=?"); params.append(f.parent_id if f.parent_id != "" else None)
    if f.color is not None: updates.append("color=?"); params.append(f.color)
    if f.icon is not None: updates.append("icon=?"); params.append(f.icon)
    if f.position is not None: updates.append("position=?"); params.append(f.position)
    if f.collapsed is not None: updates.append("collapsed=?"); params.append(int(f.collapsed))
    if updates:
        params.append(folder_id)
        db.execute(f"UPDATE folders SET {','.join(updates)} WHERE id=?", params)
        db.commit()
    db.close()
    notify("folder_update", {})
    return {"status": "updated"}

@app.delete("/api/folders/{folder_id}")
def delete_folder(folder_id: str):
    db = get_db()
    # Unassign topics in this folder
    db.execute("UPDATE topics SET folder_id = NULL WHERE folder_id = ?", (folder_id,))
    # Move child folders to parent
    parent = db.execute("SELECT parent_id FROM folders WHERE id = ?", (folder_id,)).fetchone()
    parent_id = parent['parent_id'] if parent else None
    db.execute("UPDATE folders SET parent_id = ? WHERE parent_id = ?", (parent_id, folder_id))
    db.execute("DELETE FROM folders WHERE id = ?", (folder_id,))
    db.commit()
    db.close()
    notify("folder_update", {})
    return {"status": "deleted"}

@app.post("/api/topics/{topic_id}/move")
def move_topic_to_folder(topic_id: str, body: dict):
    db = get_db()
    folder_id = body.get('folder_id')  # None = unfiled
    position = body.get('position', 0)
    db.execute("UPDATE topics SET folder_id = ?, folder_position = ? WHERE id = ?",
               (folder_id, position, topic_id))
    db.commit()
    db.close()
    notify("topic_update", {"topic_id": topic_id})
    return {"status": "moved"}

@app.post("/api/folders/reorder")
def reorder_folders(body: dict):
    """Reorder folders. Body: {order: [{id, position, parent_id}]}"""
    db = get_db()
    for item in body.get('order', []):
        db.execute("UPDATE folders SET position = ?, parent_id = ? WHERE id = ?",
                   (item['position'], item.get('parent_id'), item['id']))
    db.commit()
    db.close()
    notify("folder_update", {})
    return {"status": "reordered"}

# ── Actions Engine ──

from cv_generator import generate_cv, FUND_CONFIG

@app.post("/api/actions/generate-cv/{fund_id}")
def action_generate_cv(fund_id: str):
    """Generate a customized CV for a fund."""
    result = generate_cv(fund_id)
    
    if result.get("error"):
        raise HTTPException(500, result["error"])
    
    # Add generated files as documents to the topic
    db = get_db()
    
    # Remove old CV docs
    db.execute("DELETE FROM documents WHERE topic_id = ? AND name LIKE 'CV%' AND kind = 'doc'", (fund_id,))
    
    # Add new ones
    db.execute("INSERT INTO documents (topic_id, name, path, doc_type, kind) VALUES (?,?,?,?,?)",
               (fund_id, "CV.pdf (Generated)", result["pdf"], "pdf", "doc"))
    db.execute("INSERT INTO documents (topic_id, name, path, doc_type, kind) VALUES (?,?,?,?,?)",
               (fund_id, "CV Preview", result["html"], "html", "doc"))
    
    # Post a message
    msg_id = db.execute("INSERT INTO messages (topic_id, sender, content, msg_type) VALUES (?,?,?,?)",
        (fund_id, "mia", f"CV generiert — {result['subtitle']}. PDF: {result['size']//1024}KB. Preview: klick auf 'CV Preview' im Context Panel.", "text")).lastrowid
    
    db.execute("INSERT INTO proposals (message_id, proposal_type, content, confidence, confidence_reason, options) VALUES (?,?,?,?,?,?)",
        (msg_id, "Result", "CV wurde generiert und als PDF gespeichert.", 95, "Chrome Headless PDF, HOF-Design Template",
         json.dumps([
            {"title": "Preview öffnen", "recommended": True, "description": f"Öffne die HTML-Preview im Browser: /view/{result['html']}"},
            {"title": "Email mit CV senden", "recommended": False, "description": "Nächster Schritt: Cover Letter + CV als Email senden."}
         ])))
    
    # Advance the "CV ready" step
    _advance_next_step(db, fund_id)
    
    db.execute("UPDATE topics SET updated_at = CURRENT_TIMESTAMP WHERE id = ?", (fund_id,))
    db.commit()
    db.close()
    
    notify("topic_update", {"topic_id": fund_id})
    notify("message", {"topic_id": fund_id, "sender": "mia"})
    
    return result

@app.get("/api/actions/available-funds")
def available_funds():
    """List funds that have CV configs."""
    return list(FUND_CONFIG.keys())

# ── AI Integration (Phase 2) ──

# AI Provider config — tries Anthropic first, falls back to OpenAI
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "")
AI_PROVIDER = "openai"  # "anthropic" or "openai"
ANTHROPIC_MODEL = "claude-sonnet-4-5-20250514"
OPENAI_MODEL = "gpt-4o-mini"

def _build_system_prompt(topic_id: str) -> str:
    """Build a context-rich system prompt for the AI based on topic data."""
    db = get_db()
    row = db.execute("SELECT * FROM topics WHERE id = ?", (topic_id,)).fetchone()
    if not row:
        db.close()
        return "Du bist Mia, AI Co-Founderin. Direkt, keine Floskeln."
    
    cols = [d[0] for d in db.execute("SELECT * FROM topics WHERE 0").description]
    topic = dict(zip(cols, row))
    meta = json.loads(topic.get("meta") or "{}")
    
    # Get corrections with patterns for enforcement
    corrections = db.execute("SELECT rule, category, severity, wrong, rght FROM corrections WHERE active = 1 ORDER BY severity DESC").fetchall()
    corrections_text = "\n".join(
        f"- [SEV {c[2]}] {c[0]}" + (f" (FALSCH: {c[3]} → RICHTIG: {c[4]})" if c[3] and c[4] else "")
        for c in corrections
    )
    
    # Get relevant standards
    output_type = meta.get("output_type", "general")
    standards = db.execute("SELECT rule FROM quality_standards WHERE output_type IN (?, 'general')", (output_type,)).fetchall()
    standards_text = "\n".join(f"- {s[0]}" for s in standards)
    
    # Get trust skills
    skills = db.execute("SELECT skill, score FROM trust_skills ORDER BY score DESC").fetchall()
    trust_text = "\n".join(f"- {s[0]}: {s[1]}/100" for s in skills)
    
    # Get recent messages for context
    msgs = db.execute("SELECT sender, content FROM messages WHERE topic_id = ? ORDER BY created_at DESC LIMIT 10", (topic_id,)).fetchall()
    msgs.reverse()
    history_text = "\n".join(f"{'Florian' if m[0]=='human' else 'Mia'}: {m[1][:200]}" for m in msgs)
    
    # Get steps
    steps = db.execute("SELECT label, done FROM steps WHERE topic_id = ? ORDER BY position", (topic_id,)).fetchall()
    steps_text = "\n".join(f"- [{'x' if s[1] else ' '}] {s[0]}" for s in steps)
    
    # Get docs
    docs = db.execute("SELECT name, kind FROM documents WHERE topic_id = ?", (topic_id,)).fetchall()
    docs_text = "\n".join(f"- {d[0]} ({d[1]})" for d in docs)
    
    db.close()
    
    return f"""Du bist Mia — AI Co-Founderin, nicht Assistentin. Direkt. Bullets > Prosa. Kein Filler.
NIE: "Great question!", "I'd be happy to!", "Absolutely!"
1 Empfehlung mit Begründung > 5 Optionen.
Sprache: Deutsch default, spiegele Florians Sprache.

## Aktueller Task: {topic['name']}
Stage: {topic['stage']} | State: {topic.get('state','active')} | Progress: {topic.get('progress',0)}%
{f"Contact: {meta.get('contact','')}" if meta.get('contact') else ''}
{f"Email: {meta.get('email','')}" if meta.get('email') else ''}
Output-Type: {output_type}

## Steps
{steps_text or 'Keine Steps definiert.'}

## Documents
{docs_text or 'Keine Dokumente.'}

## Korrekturen (IMMER beachten)
{corrections_text}

## Quality Standards ({output_type})
{standards_text}

## Trust Scores
{trust_text}

## Letzte Nachrichten
{history_text}

Antworte kurz und direkt. Bei Empfehlungen: Confidence angeben [X% — weil Y]."""

class AIRequest(BaseModel):
    message: str
    topic_id: str

@app.post("/api/ai/chat")
async def ai_chat(req: AIRequest):
    """Direct AI chat with error recovery. Returns response + auto pre-flight."""
    system_prompt = _build_system_prompt(req.topic_id)
    ai_text = ""
    model_used = ""
    usage = {}
    
    try:
        async with httpx.AsyncClient(timeout=60) as client:
            if AI_PROVIDER == "anthropic" and ANTHROPIC_API_KEY:
                resp = await client.post(
                    "https://api.anthropic.com/v1/messages",
                    headers={"x-api-key": ANTHROPIC_API_KEY, "anthropic-version": "2023-06-01", "content-type": "application/json"},
                    json={"model": ANTHROPIC_MODEL, "max_tokens": 2048, "system": system_prompt,
                          "messages": [{"role": "user", "content": req.message}]}
                )
                if resp.status_code != 200:
                    raise HTTPException(resp.status_code, f"Anthropic error: {resp.text[:200]}")
                data = resp.json()
                ai_text = data["content"][0]["text"]
                model_used = ANTHROPIC_MODEL
                usage = data.get("usage", {})
            elif OPENAI_API_KEY:
                resp = await client.post(
                    "https://api.openai.com/v1/chat/completions",
                    headers={"Authorization": f"Bearer {OPENAI_API_KEY}", "Content-Type": "application/json"},
                    json={"model": OPENAI_MODEL, "max_tokens": 2048,
                          "messages": [{"role": "system", "content": system_prompt}, {"role": "user", "content": req.message}]}
                )
                if resp.status_code != 200:
                    raise HTTPException(resp.status_code, f"OpenAI error: {resp.text[:200]}")
                data = resp.json()
                ai_text = data["choices"][0]["message"]["content"]
                model_used = OPENAI_MODEL
                usage = data.get("usage", {})
            else:
                raise HTTPException(503, "No AI API key configured")
    except httpx.TimeoutException:
        _log_ai_error(req.topic_id, "timeout", "AI request timed out after 60s")
        raise HTTPException(504, "AI provider timed out")
    except httpx.ConnectError as e:
        _log_ai_error(req.topic_id, "connection", str(e)[:200])
        raise HTTPException(502, "Cannot reach AI provider")
    except HTTPException:
        raise
    except Exception as e:
        _log_ai_error(req.topic_id, "unknown", str(e)[:200])
        raise HTTPException(500, f"AI error: {str(e)[:200]}")
    
    # Save message
    db = get_db()
    db.execute("INSERT INTO messages (topic_id, sender, content, msg_type) VALUES (?,?,?,?)",
               (req.topic_id, "mia", ai_text, "text"))
    db.execute("INSERT INTO events (topic_id, event_type, detail) VALUES (?,?,?)",
               (req.topic_id, "ai_response", json.dumps({"model": model_used, "tokens": usage})))
    db.execute("UPDATE topics SET updated_at = CURRENT_TIMESTAMP WHERE id = ?", (req.topic_id,))
    db.commit()
    db.close()
    
    notify("message", {"topic_id": req.topic_id, "sender": "mia"})
    
    # Auto pre-flight on response
    preflight = preflight_check(req.topic_id)
    
    return {"response": ai_text, "usage": usage, "preflight": preflight}

def _log_ai_error(topic_id: str, error_type: str, detail: str):
    """Log AI errors to events + messages for visibility."""
    try:
        db = get_db()
        db.execute("INSERT INTO events (topic_id, event_type, detail) VALUES (?,?,?)",
                   (topic_id, "ai_error", json.dumps({"type": error_type, "detail": detail})))
        db.execute("INSERT INTO messages (topic_id, sender, content, msg_type) VALUES (?,?,?,?)",
                   (topic_id, "system", f"AI-Fehler: {error_type} — {detail[:100]}", "text"))
        db.commit()
        db.close()
        notify("message", {"topic_id": topic_id, "sender": "system"})
    except Exception:
        pass  # Don't let error logging cause more errors

@app.post("/api/ai/stream")
async def ai_stream(req: AIRequest):
    """Streaming AI chat — returns SSE stream. Uses OpenAI streaming format."""
    system_prompt = _build_system_prompt(req.topic_id)
    
    async def generate():
        full_text = ""
        model_used = ""
        
        async with httpx.AsyncClient(timeout=120) as client:
            if AI_PROVIDER == "anthropic" and ANTHROPIC_API_KEY:
                model_used = ANTHROPIC_MODEL
                async with client.stream("POST", "https://api.anthropic.com/v1/messages",
                    headers={"x-api-key": ANTHROPIC_API_KEY, "anthropic-version": "2023-06-01", "content-type": "application/json"},
                    json={"model": ANTHROPIC_MODEL, "max_tokens": 2048, "stream": True, "system": system_prompt,
                          "messages": [{"role": "user", "content": req.message}]}
                ) as resp:
                    async for line in resp.aiter_lines():
                        if not line.startswith("data: "): continue
                        payload = line[6:]
                        if payload == "[DONE]": break
                        try:
                            event = json.loads(payload)
                            if event.get("type") == "content_block_delta":
                                delta = event["delta"].get("text", "")
                                full_text += delta
                                yield f"data: {json.dumps({'text': delta})}\n\n"
                        except json.JSONDecodeError: pass
            
            elif OPENAI_API_KEY:
                model_used = OPENAI_MODEL
                async with client.stream("POST", "https://api.openai.com/v1/chat/completions",
                    headers={"Authorization": f"Bearer {OPENAI_API_KEY}", "Content-Type": "application/json"},
                    json={"model": OPENAI_MODEL, "max_tokens": 2048, "stream": True,
                          "messages": [{"role": "system", "content": system_prompt}, {"role": "user", "content": req.message}]}
                ) as resp:
                    async for line in resp.aiter_lines():
                        if not line.startswith("data: "): continue
                        payload = line[6:]
                        if payload == "[DONE]": break
                        try:
                            event = json.loads(payload)
                            delta = event.get("choices", [{}])[0].get("delta", {}).get("content", "")
                            if delta:
                                full_text += delta
                                yield f"data: {json.dumps({'text': delta})}\n\n"
                        except json.JSONDecodeError: pass
            else:
                yield f"data: {json.dumps({'text': 'Kein AI-Provider konfiguriert.', 'done': True})}\n\n"
                return
        
        # Save complete message
        if full_text.strip():
            try:
                db = get_db()
                db.execute("INSERT INTO messages (topic_id, sender, content, msg_type) VALUES (?,?,?,?)",
                           (req.topic_id, "mia", full_text, "text"))
                db.execute("INSERT INTO events (topic_id, event_type, detail) VALUES (?,?,?)",
                           (req.topic_id, "ai_response", json.dumps({"model": model_used, "streamed": True})))
                db.execute("UPDATE topics SET updated_at = CURRENT_TIMESTAMP WHERE id = ?", (req.topic_id,))
                db.commit()
                db.close()
                
                notify("message", {"topic_id": req.topic_id, "sender": "mia"})
                
                # Auto pre-flight on streamed response
                pf = preflight_check(req.topic_id)
                yield f"data: {json.dumps({'preflight': pf})}\n\n"
            except Exception as e:
                yield f"data: {json.dumps({'error': f'Save failed: {str(e)[:100]}'})}\n\n"
        
        yield f"data: {json.dumps({'done': True})}\n\n"
    
    async def generate_safe():
        """Wrapper with error recovery for streaming."""
        try:
            async for chunk in generate():
                yield chunk
        except httpx.TimeoutException:
            _log_ai_error(req.topic_id, "timeout", "Stream timed out after 120s")
            yield f"data: {json.dumps({'error': 'AI-Timeout: Keine Antwort nach 120s. Bitte erneut versuchen.'})}\n\n"
            yield f"data: {json.dumps({'done': True})}\n\n"
        except httpx.ConnectError as e:
            _log_ai_error(req.topic_id, "connection", str(e)[:200])
            yield f"data: {json.dumps({'error': 'AI-Provider nicht erreichbar. Bitte später versuchen.'})}\n\n"
            yield f"data: {json.dumps({'done': True})}\n\n"
        except Exception as e:
            _log_ai_error(req.topic_id, "stream_error", str(e)[:200])
            yield f"data: {json.dumps({'error': f'Streaming-Fehler: {str(e)[:100]}'})}\n\n"
            yield f"data: {json.dumps({'done': True})}\n\n"
    
    return StreamingResponse(generate_safe(), media_type="text/event-stream")

# ── Action Queue (for OpenClaw tool-based actions) ──

class ActionRequest(BaseModel):
    topic_id: str
    action_type: str  # "send_email", "generate_cv", "publish"
    params: dict = {}

@app.post("/api/actions/queue")
def queue_action(req: ActionRequest):
    """Queue an action for Mia (OpenClaw) to pick up and execute."""
    db = get_db()
    db.execute("""INSERT INTO events (topic_id, event_type, detail) VALUES (?,?,?)""",
               (req.topic_id, "action_queued", json.dumps({
                   "action_type": req.action_type,
                   "params": req.params,
                   "status": "pending"
               })))
    db.commit()
    
    # Also post as a message so it's visible
    action_labels = {
        "send_email": "Email senden",
        "generate_cv": "CV generieren",
        "publish": "Veröffentlichen"
    }
    label = action_labels.get(req.action_type, req.action_type)
    db.execute("INSERT INTO messages (topic_id, sender, content, msg_type) VALUES (?,?,?,?)",
               (req.topic_id, "system", f"Aktion angefordert: {label}. Wird von Mia ausgeführt...", "text"))
    db.commit()
    db.close()
    
    notify("message", {"topic_id": req.topic_id, "sender": "system"})
    notify("action_queued", {"topic_id": req.topic_id, "action": req.action_type})
    return {"status": "queued", "action_type": req.action_type}

@app.get("/api/actions/pending")
def get_pending_actions():
    """Get all pending actions (for Mia/OpenClaw to poll)."""
    db = get_db()
    rows = db.execute("""
        SELECT topic_id, event_type, detail, created_at 
        FROM events 
        WHERE event_type = 'action_queued' 
        AND json_extract(detail, '$.status') = 'pending'
        ORDER BY created_at
    """).fetchall()
    db.close()
    return [{"topic_id": r[0], "detail": json.loads(r[2]), "created_at": r[3]} for r in rows]

@app.post("/api/actions/complete")
def complete_action(body: dict):
    """Mark a queued action as completed (called by Mia/OpenClaw)."""
    topic_id = body.get("topic_id")
    action_type = body.get("action_type")
    result = body.get("result", "completed")
    error = body.get("error")
    
    db = get_db()
    new_status = "failed" if error else "completed"
    
    # Update the pending event
    detail_updates = f"'$.status', '{new_status}', '$.result', ?"
    if error:
        detail_updates += ", '$.error', '" + str(error).replace("'", "''")[:500] + "'"
        detail_updates += ", '$.retries', COALESCE(json_extract(detail, '$.retries'), 0)"
    
    db.execute(f"""
        UPDATE events SET detail = json_set(detail, '$.status', ?, '$.result', ?)
        WHERE topic_id = ? AND event_type = 'action_queued' 
        AND json_extract(detail, '$.action_type') = ?
        AND json_extract(detail, '$.status') = 'pending'
    """, (new_status, result, topic_id, action_type))
    
    if error:
        db.execute("INSERT INTO messages (topic_id, sender, content, msg_type) VALUES (?,?,?,?)",
                   (topic_id, "system", f"Aktion fehlgeschlagen: {action_type}. Fehler: {error}", "text"))
        # Update topic state to 'error'
        db.execute("UPDATE topics SET state = 'error' WHERE id = ?", (topic_id,))
    else:
        db.execute("INSERT INTO messages (topic_id, sender, content, msg_type) VALUES (?,?,?,?)",
                   (topic_id, "system", f"Aktion abgeschlossen: {action_type}. Ergebnis: {result}", "text"))
    db.commit()
    db.close()
    
    notify("message", {"topic_id": topic_id, "sender": "system"})
    return {"status": new_status}

# ── Action Retry (Error Recovery) ──

@app.post("/api/actions/retry")
def retry_action(body: dict):
    """Retry a failed action. Increments retry count, resets to pending."""
    topic_id = body.get("topic_id")
    action_type = body.get("action_type")
    max_retries = body.get("max_retries", 3)
    
    db = get_db()
    row = db.execute("""
        SELECT id, detail FROM events 
        WHERE topic_id = ? AND event_type = 'action_queued'
        AND json_extract(detail, '$.action_type') = ?
        AND json_extract(detail, '$.status') = 'failed'
        ORDER BY created_at DESC LIMIT 1
    """, (topic_id, action_type)).fetchone()
    
    if not row:
        db.close()
        raise HTTPException(404, "No failed action found to retry")
    
    detail = json.loads(row['detail'])
    retries = detail.get('retries', 0) + 1
    
    if retries > max_retries:
        db.close()
        raise HTTPException(429, f"Max retries ({max_retries}) exceeded for {action_type}")
    
    # Reset to pending with incremented retry count
    db.execute("""
        UPDATE events SET detail = json_set(detail, '$.status', 'pending', '$.retries', ?, '$.error', null)
        WHERE id = ?
    """, (retries, row['id']))
    
    db.execute("INSERT INTO messages (topic_id, sender, content, msg_type) VALUES (?,?,?,?)",
               (topic_id, "system", f"Retry #{retries} für {action_type}...", "text"))
    
    # Reset topic state from error
    db.execute("UPDATE topics SET state = 'active' WHERE id = ? AND state = 'error'", (topic_id,))
    db.commit()
    db.close()
    
    notify("message", {"topic_id": topic_id, "sender": "system"})
    notify("action_queued", {"topic_id": topic_id, "action": action_type, "retry": retries})
    return {"status": "retrying", "retry": retries}

# ── Topic State Machine (Error Recovery) ──

VALID_STATES = {"active", "running", "blocked", "done", "error", "archived"}
VALID_TRANSITIONS = {
    "active": {"running", "blocked", "done", "archived"},
    "running": {"active", "done", "error", "blocked"},
    "blocked": {"active", "running"},
    "done": {"active", "archived"},
    "error": {"active", "running", "archived"},
    "archived": {"active"},
}

@app.post("/api/topics/{topic_id}/state")
def set_topic_state(topic_id: str, body: dict):
    """Transition topic state with validation."""
    new_state = body.get("state")
    if new_state not in VALID_STATES:
        raise HTTPException(400, f"Invalid state: {new_state}. Valid: {VALID_STATES}")
    
    db = get_db()
    topic = db.execute("SELECT state FROM topics WHERE id = ?", (topic_id,)).fetchone()
    if not topic:
        db.close()
        raise HTTPException(404, "Topic not found")
    
    current = topic['state'] or 'active'
    allowed = VALID_TRANSITIONS.get(current, set())
    if new_state not in allowed:
        db.close()
        raise HTTPException(409, f"Cannot transition from '{current}' to '{new_state}'. Allowed: {allowed}")
    
    db.execute("UPDATE topics SET state = ? WHERE id = ?", (new_state, topic_id))
    db.execute("INSERT INTO events (topic_id, event_type, detail) VALUES (?,?,?)",
               (topic_id, "state_change", json.dumps({"from": current, "to": new_state})))
    db.commit()
    db.close()
    
    notify("topic_updated", {"topic_id": topic_id, "state": new_state})
    return {"status": "ok", "from": current, "to": new_state}

# ── Mia Bridge (OpenClaw Integration) ──

@app.post("/api/mia/execute")
async def mia_execute(body: dict):
    """Direct bridge to Mia (OpenClaw). 
    Sends a task, gets a response. Used for high-trust delegated actions.
    Falls back to local GPT-4o-mini if OpenClaw unavailable."""
    task = body.get("task", "")
    topic_id = body.get("topic_id")
    context = body.get("context", {})
    
    if not task:
        raise HTTPException(400, "Task is required")
    
    db = get_db()
    
    # Build context from topic
    if topic_id:
        topic = db.execute("SELECT * FROM topics WHERE id = ?", (topic_id,)).fetchone()
        msgs = db.execute(
            "SELECT sender, content FROM messages WHERE topic_id = ? ORDER BY created_at DESC LIMIT 5",
            (topic_id,)
        ).fetchall()
        if topic:
            context["topic_name"] = topic['name']
            context["topic_stage"] = topic['stage']
        context["recent_messages"] = [{"sender": m['sender'], "content": m['content'][:200]} for m in msgs]
    
    # Get trust + corrections context
    trust_skills = db.execute("SELECT skill, score FROM trust_skills ORDER BY score DESC").fetchall()
    corrections = db.execute("SELECT rule, category FROM corrections WHERE active = 1 AND severity >= 2").fetchall()
    
    context["trust_scores"] = {t['skill']: t['score'] for t in trust_skills}
    context["active_corrections"] = [{"rule": c['rule'], "cat": c['category']} for c in corrections]
    
    db.close()
    
    # Try OpenClaw bridge first (via Action Queue pattern)
    # If OpenClaw is running, it polls /api/actions/pending
    # For now: use local AI with enriched context
    
    system_prompt = f"""Du bist Mia, Florians AI Co-Founderin. Direkt, keine Floskeln, ♔ am Ende.

Context:
- Topic: {context.get('topic_name', 'unknown')} (Stage: {context.get('topic_stage', 'unknown')})
- Trust Scores: {json.dumps(context.get('trust_scores', {}))}
- Active Corrections ({len(context.get('active_corrections', []))}): Beachte diese Regeln.

Corrections (NICHT verletzen):
{chr(10).join('- ' + c['rule'] for c in context.get('active_corrections', [])[:10])}

Recent conversation:
{chr(10).join(f"[{m['sender']}] {m['content']}" for m in context.get('recent_messages', [])[:3])}
"""
    
    # Use streaming for real-time response
    api_key = os.environ.get("OPENAI_API_KEY", "")
    if not api_key:
        raise HTTPException(503, "No AI provider configured")
    
    async def stream_mia():
        full_response = ""
        try:
            async with httpx.AsyncClient(timeout=60.0) as client:
                resp = await client.post(
                    "https://api.openai.com/v1/chat/completions",
                    headers={"Authorization": f"Bearer {api_key}"},
                    json={
                        "model": "gpt-4o-mini",
                        "messages": [
                            {"role": "system", "content": system_prompt},
                            {"role": "user", "content": task}
                        ],
                        "stream": True,
                        "max_tokens": 2000,
                        "temperature": 0.7
                    }
                )
                async for line in resp.aiter_lines():
                    if line.startswith("data: ") and line != "data: [DONE]":
                        try:
                            chunk = json.loads(line[6:])
                            delta = chunk["choices"][0].get("delta", {}).get("content", "")
                            if delta:
                                full_response += delta
                                yield f"data: {json.dumps({'chunk': delta})}\n\n"
                        except (json.JSONDecodeError, KeyError, IndexError):
                            continue
            
            # After streaming: run pre-flight on the response
            if topic_id and full_response:
                db2 = get_db()
                db2.execute("INSERT INTO messages (topic_id, sender, content, msg_type) VALUES (?,?,?,?)",
                           (topic_id, "mia", full_response, "text"))
                db2.commit()
                db2.close()
                
                # Auto pre-flight
                preflight_result = preflight_check(topic_id)
                yield f"data: {json.dumps({'preflight': preflight_result})}\n\n"
            
            yield f"data: {json.dumps({'done': True})}\n\n"
            
        except Exception as e:
            yield f"data: {json.dumps({'error': str(e)})}\n\n"
    
    return StreamingResponse(stream_mia(), media_type="text/event-stream")

# ── Compound Knowledge Engine (Findings) ──

import math as _math

def _calc_compound_score(finding: dict) -> float:
    """Calculate compound score: usage × confidence × relevance."""
    systems = json.loads(finding.get('used_in_systems') or '[]')
    content = json.loads(finding.get('used_in_content') or '[]')
    revenue = json.loads(finding.get('used_in_revenue') or '[]')
    supports = json.loads(finding.get('supports') or '[]')
    contradicts = json.loads(finding.get('contradicts') or '[]')
    
    usage = len(systems) * 3.0 + len(content) * 1.0 + len(revenue) * 5.0
    connections = (len(supports) + len(contradicts)) * 0.5
    
    # Relevance decay
    try:
        created = datetime.fromisoformat(finding.get('created_at', ''))
        age_days = (datetime.now() - created).days
    except (ValueError, TypeError):
        age_days = 0
    
    half_life = 365  # Default 1 year
    tags = json.loads(finding.get('tags') or '[]')
    tag_decay = {"ai_technology": 90, "market_data": 180, "personal_fact": 9999, "business_model": 360}
    for tag in tags:
        if tag in tag_decay:
            half_life = min(half_life, tag_decay[tag])
    
    relevance = _math.exp(-0.693 * age_days / half_life) if half_life < 9999 else 1.0
    
    confidence = finding.get('confidence', 0.5)
    if isinstance(confidence, str):
        confidence = float(confidence)
    
    return round(confidence * (usage + connections) * relevance, 2)

def _next_finding_id(db) -> str:
    """Generate next RF-XXX id."""
    row = db.execute("SELECT id FROM findings ORDER BY id DESC LIMIT 1").fetchone()
    if not row:
        return "RF-001"
    try:
        num = int(row['id'].split('-')[1]) + 1
    except (IndexError, ValueError):
        num = 1
    return f"RF-{num:03d}"

@app.get("/api/findings")
def list_findings(status: str = None, research_line: str = None, tag: str = None):
    """List findings with optional filters."""
    db = get_db()
    query = "SELECT * FROM findings WHERE 1=1"
    params = []
    
    if status:
        query += " AND status = ?"
        params.append(status)
    if research_line:
        query += " AND research_line = ?"
        params.append(research_line)
    if tag:
        query += " AND tags LIKE ?"
        params.append(f'%"{tag}"%')
    
    query += " ORDER BY compound_score DESC, confidence DESC"
    rows = db.execute(query, params).fetchall()
    db.close()
    
    results = []
    for r in rows:
        f = dict(r)
        f['compound_score'] = _calc_compound_score(f)
        f['tags'] = json.loads(f.get('tags') or '[]')
        f['used_in_systems'] = json.loads(f.get('used_in_systems') or '[]')
        f['used_in_content'] = json.loads(f.get('used_in_content') or '[]')
        f['used_in_revenue'] = json.loads(f.get('used_in_revenue') or '[]')
        f['supports'] = json.loads(f.get('supports') or '[]')
        f['contradicts'] = json.loads(f.get('contradicts') or '[]')
        f['derived_from'] = json.loads(f.get('derived_from') or '[]')
        results.append(f)
    
    return results

@app.get("/api/findings/{finding_id}")
def get_finding(finding_id: str):
    """Get a single finding with confidence history."""
    db = get_db()
    row = db.execute("SELECT * FROM findings WHERE id = ?", (finding_id,)).fetchone()
    if not row:
        db.close()
        raise HTTPException(404, "Finding not found")
    
    f = dict(row)
    f['compound_score'] = _calc_compound_score(f)
    for field in ['tags', 'used_in_systems', 'used_in_content', 'used_in_revenue', 'supports', 'contradicts', 'derived_from']:
        f[field] = json.loads(f.get(field) or '[]')
    
    # Confidence history
    history = db.execute(
        "SELECT * FROM confidence_history WHERE finding_id = ? ORDER BY created_at DESC", (finding_id,)
    ).fetchall()
    f['confidence_history'] = [dict(h) for h in history]
    
    db.close()
    return f

@app.post("/api/findings")
def create_finding(body: dict):
    """Create a new finding."""
    db = get_db()
    finding_id = body.get('id') or _next_finding_id(db)
    claim = body.get('claim', '').strip()
    
    if not claim:
        db.close()
        raise HTTPException(400, "claim is required")
    
    # Check for potential contradictions (tag-based)
    tags = body.get('tags', [])
    if isinstance(tags, str):
        tags = json.loads(tags)
    
    contradictions = []
    if tags and len(tags) >= 1:
        existing = db.execute("SELECT id, claim, tags, confidence FROM findings WHERE status = 'alive'").fetchall()
        for ex in existing:
            ex_tags = json.loads(ex['tags'] or '[]')
            shared = set(tags) & set(ex_tags)
            if len(shared) >= 2:
                contradictions.append({"id": ex['id'], "claim": ex['claim'], "shared_tags": list(shared)})
    
    confidence = body.get('confidence', 0.50)
    
    db.execute("""INSERT INTO findings 
        (id, claim, context, confidence, status, source_type, source_detail, source_url, extracted_from,
         tags, research_line, used_in_systems, used_in_content, used_in_revenue,
         supports, contradicts, derived_from, topic_id, verified)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
        (finding_id, claim, body.get('context'),
         confidence, 'alive',
         body.get('source_type', 'conversation'), body.get('source_detail'),
         body.get('source_url'), body.get('extracted_from'),
         json.dumps(tags), body.get('research_line'),
         json.dumps(body.get('used_in_systems', [])),
         json.dumps(body.get('used_in_content', [])),
         json.dumps(body.get('used_in_revenue', [])),
         json.dumps(body.get('supports', [])),
         json.dumps(body.get('contradicts', [])),
         json.dumps(body.get('derived_from', [])),
         body.get('topic_id'),
         1 if body.get('verified') else 0))
    
    # Log initial confidence
    db.execute("INSERT INTO confidence_history (finding_id, old_confidence, new_confidence, reason, source) VALUES (?,?,?,?,?)",
               (finding_id, 0, confidence, "initial", body.get('source_type', 'conversation')))
    
    # Log event
    db.execute("INSERT INTO events (topic_id, event_type, detail) VALUES (?,?,?)",
               (body.get('topic_id'), "finding_created",
                json.dumps({"finding_id": finding_id, "claim": claim[:100], "confidence": confidence})))
    
    db.commit()
    db.close()
    
    notify("finding_created", {"finding_id": finding_id})
    
    result = {"id": finding_id, "status": "created", "confidence": confidence}
    if contradictions:
        result["potential_contradictions"] = contradictions[:5]
    return result

@app.put("/api/findings/{finding_id}")
def update_finding(finding_id: str, body: dict):
    """Update a finding. Tracks confidence changes."""
    db = get_db()
    existing = db.execute("SELECT * FROM findings WHERE id = ?", (finding_id,)).fetchone()
    if not existing:
        db.close()
        raise HTTPException(404, "Finding not found")
    
    # Track confidence change
    new_confidence = body.get('confidence')
    if new_confidence is not None and float(new_confidence) != float(existing['confidence']):
        db.execute("INSERT INTO confidence_history (finding_id, old_confidence, new_confidence, reason, source) VALUES (?,?,?,?,?)",
                   (finding_id, existing['confidence'], new_confidence,
                    body.get('confidence_reason', 'manual update'),
                    body.get('confidence_source', 'manual')))
    
    # Build update query dynamically
    updatable = ['claim', 'context', 'confidence', 'status', 'killed_by', 'source_type',
                 'source_detail', 'tags', 'research_line', 'used_in_systems', 'used_in_content',
                 'used_in_revenue', 'supports', 'contradicts', 'derived_from', 'topic_id']
    
    sets = ["updated_at = CURRENT_TIMESTAMP"]
    params = []
    for field in updatable:
        if field in body:
            val = body[field]
            if isinstance(val, (list, dict)):
                val = json.dumps(val)
            sets.append(f"{field} = ?")
            params.append(val)
    
    if len(sets) > 1:
        params.append(finding_id)
        db.execute(f"UPDATE findings SET {', '.join(sets)} WHERE id = ?", params)
    
    # Recalculate compound score
    updated = db.execute("SELECT * FROM findings WHERE id = ?", (finding_id,)).fetchone()
    score = _calc_compound_score(dict(updated))
    db.execute("UPDATE findings SET compound_score = ? WHERE id = ?", (score, finding_id))
    
    # Handle status transitions
    new_status = body.get('status')
    if new_status == 'dead' and existing['status'] != 'dead':
        db.execute("INSERT INTO events (topic_id, event_type, detail) VALUES (?,?,?)",
                   (existing['topic_id'], "finding_killed",
                    json.dumps({"finding_id": finding_id, "killed_by": body.get('killed_by', '')})))
    elif new_status == 'contested' and existing['status'] != 'contested':
        db.execute("INSERT INTO events (topic_id, event_type, detail) VALUES (?,?,?)",
                   (existing['topic_id'], "finding_contested",
                    json.dumps({"finding_id": finding_id})))
    
    db.commit()
    db.close()
    
    notify("finding_updated", {"finding_id": finding_id})
    return {"status": "updated", "compound_score": score}

@app.post("/api/findings/{finding_id}/validate")
def validate_finding(finding_id: str, body: dict):
    """Validate or contradict a finding using proper Bayesian updating.
    
    P(H|E) = P(E|H) * P(H) / P(E)
    
    Source reliability = how likely this source gives correct evidence.
    If direction=support: likelihood_if_true is high, likelihood_if_false is low.
    If direction=contradict: likelihood_if_true is low, likelihood_if_false is high.
    """
    # Source reliability: P(evidence is accurate | source type)
    SOURCE_RELIABILITY = {
        "own_hypothesis": 0.40, "conversation": 0.50, "linkedin_poll": 0.55,
        "industry_report": 0.75, "academic_paper": 0.85, "own_data": 0.80,
        "revenue_validated": 0.90
    }
    
    db = get_db()
    finding = db.execute("SELECT * FROM findings WHERE id = ?", (finding_id,)).fetchone()
    if not finding:
        db.close()
        raise HTTPException(404, "Finding not found")
    
    direction = body.get('direction', 'support')  # support or contradict
    source_type = body.get('source_type', 'conversation')
    reason = body.get('reason', '')
    
    prior = finding['confidence']
    if isinstance(prior, str):
        prior = float(prior)
    reliability = SOURCE_RELIABILITY.get(source_type, 0.50)
    
    # Bayesian update:
    # P(H|E) = P(E|H) * P(H) / [P(E|H) * P(H) + P(E|~H) * P(~H)]
    if direction == 'support':
        # Evidence supports hypothesis
        # P(E|H) = reliability (reliable source likely gives supporting evidence if H true)
        # P(E|~H) = 1 - reliability (unreliable evidence if H false)
        likelihood_true = reliability
        likelihood_false = 1.0 - reliability
    else:
        # Evidence contradicts hypothesis
        # P(E|H) = 1 - reliability (contradicting evidence unlikely if H true)
        # P(E|~H) = reliability (contradicting evidence likely if H false)
        likelihood_true = 1.0 - reliability
        likelihood_false = reliability
    
    numerator = likelihood_true * prior
    denominator = numerator + likelihood_false * (1.0 - prior)
    
    if denominator == 0:
        new_conf = prior
    else:
        new_conf = numerator / denominator
    
    # Clamp to avoid 0.0 or 1.0 (hard convictions are insensitive to evidence)
    new_conf = round(max(0.02, min(0.98, new_conf)), 2)
    
    new_status = finding['status']
    if new_conf < 0.20 and finding['status'] == 'alive':
        new_status = 'contested'
    
    db.execute("UPDATE findings SET confidence = ?, status = ?, updated_at = CURRENT_TIMESTAMP WHERE id = ?",
               (new_conf, new_status, finding_id))
    db.execute("INSERT INTO confidence_history (finding_id, old_confidence, new_confidence, reason, source) VALUES (?,?,?,?,?)",
               (finding_id, prior, new_conf, f"{direction}: {reason}", source_type))
    
    # Recalculate compound score
    updated = db.execute("SELECT * FROM findings WHERE id = ?", (finding_id,)).fetchone()
    score = _calc_compound_score(dict(updated))
    db.execute("UPDATE findings SET compound_score = ? WHERE id = ?", (score, finding_id))
    
    db.commit()
    db.close()
    
    notify("finding_updated", {"finding_id": finding_id})
    return {"status": "validated", "old_confidence": prior, "new_confidence": new_conf,
            "direction": direction, "finding_status": new_status, "compound_score": score}

@app.get("/api/findings/{finding_id}/related")
def related_findings(finding_id: str):
    """Find related findings by shared tags."""
    db = get_db()
    finding = db.execute("SELECT * FROM findings WHERE id = ?", (finding_id,)).fetchone()
    if not finding:
        db.close()
        raise HTTPException(404, "Finding not found")
    
    tags = json.loads(finding['tags'] or '[]')
    if not tags:
        db.close()
        return []
    
    all_findings = db.execute("SELECT * FROM findings WHERE id != ? AND status != 'dead'", (finding_id,)).fetchall()
    db.close()
    
    related = []
    for f in all_findings:
        f_tags = json.loads(f['tags'] or '[]')
        shared = set(tags) & set(f_tags)
        if shared:
            related.append({
                "id": f['id'], "claim": f['claim'], "confidence": f['confidence'],
                "status": f['status'], "shared_tags": list(shared),
                "relevance": round(len(shared) / max(len(tags), 1), 2)
            })
    
    related.sort(key=lambda x: -x['relevance'])
    return related[:10]

@app.get("/api/findings-stats")
def findings_stats():
    """Aggregate stats for the knowledge engine."""
    db = get_db()
    total = db.execute("SELECT COUNT(*) as c FROM findings").fetchone()['c']
    alive = db.execute("SELECT COUNT(*) as c FROM findings WHERE status = 'alive'").fetchone()['c']
    contested = db.execute("SELECT COUNT(*) as c FROM findings WHERE status = 'contested'").fetchone()['c']
    dead = db.execute("SELECT COUNT(*) as c FROM findings WHERE status = 'dead'").fetchone()['c']
    
    # Top research lines by compound score
    lines = db.execute("""
        SELECT research_line, COUNT(*) as count, 
               AVG(confidence) as avg_confidence,
               SUM(compound_score) as total_score
        FROM findings WHERE research_line IS NOT NULL AND status = 'alive'
        GROUP BY research_line ORDER BY total_score DESC
    """).fetchall()
    
    # Orphans: findings not used anywhere
    orphans = db.execute("""
        SELECT COUNT(*) as c FROM findings 
        WHERE status = 'alive' 
        AND used_in_systems = '[]' AND used_in_content = '[]' AND used_in_revenue = '[]'
    """).fetchone()['c']
    
    db.close()
    return {
        "total": total, "alive": alive, "contested": contested, "dead": dead,
        "orphans": orphans,
        "research_lines": [{"line": r['research_line'], "count": r['count'],
                            "avg_confidence": round(r['avg_confidence'], 2),
                            "total_score": round(r['total_score'], 2)} for r in lines]
    }

@app.get("/api/topics/{topic_id}/findings")
def topic_findings(topic_id: str):
    """Get all findings associated with a topic."""
    db = get_db()
    rows = db.execute("SELECT * FROM findings WHERE topic_id = ? ORDER BY compound_score DESC", (topic_id,)).fetchall()
    db.close()
    results = []
    for r in rows:
        f = dict(r)
        f['compound_score'] = _calc_compound_score(f)
        f['tags'] = json.loads(f.get('tags') or '[]')
        results.append(f)
    return results

# ── Obsidian Import ──

@app.post("/api/import/obsidian-claims")
def import_obsidian_claims(body: dict):
    """Import claims from Obsidian vault as findings.
    Body: { claims: [{ id, claim, confidence, source, source_url, tags, research_line, used_in, context, status, killed_by }] }
    """
    db = get_db()
    claims = body.get('claims', [])
    if not claims:
        db.close()
        raise HTTPException(400, "claims array is required")
    
    imported = []
    skipped = []
    for c in claims:
        fid = c.get('id', '').strip()
        claim = c.get('claim', '').strip()
        if not fid or not claim:
            skipped.append({"id": fid, "reason": "missing id or claim"})
            continue
        
        # Check if already exists
        existing = db.execute("SELECT id FROM findings WHERE id = ?", (fid,)).fetchone()
        if existing:
            skipped.append({"id": fid, "reason": "already exists"})
            continue
        
        # Map Obsidian confidence levels
        conf_raw = c.get('confidence', 'MEDIUM')
        if isinstance(conf_raw, str):
            conf_map = {'HIGH': 0.85, 'MEDIUM': 0.60, 'LOW': 0.35}
            confidence = conf_map.get(conf_raw.upper(), 0.50)
        else:
            confidence = float(conf_raw)
        
        tags = c.get('tags', [])
        if isinstance(tags, str):
            tags = json.loads(tags)
        
        status = c.get('status', 'alive')
        source_type = 'agent_verified' if c.get('verified_by') else c.get('source_type', 'industry_report')
        
        db.execute("""INSERT INTO findings 
            (id, claim, context, confidence, status, killed_by, source_type, source_detail, source_url,
             extracted_from, tags, research_line, used_in_systems, used_in_content, used_in_revenue,
             supports, contradicts, derived_from, topic_id, verified)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (fid, claim, c.get('context'), confidence, status, c.get('killed_by'),
             source_type, c.get('source'), c.get('source_url'),
             c.get('extracted_from'),
             json.dumps(tags), c.get('research_line'),
             json.dumps([]), json.dumps(c.get('used_in', [])), json.dumps([]),
             json.dumps([]), json.dumps([]), json.dumps([]),
             c.get('topic_id'), 1 if c.get('verified_by') else 0))
        
        db.execute("INSERT INTO confidence_history (finding_id, old_confidence, new_confidence, reason, source) VALUES (?,?,?,?,?)",
                   (fid, 0, confidence, f"imported from Obsidian ({c.get('source', 'unknown')})", source_type))
        
        imported.append({"id": fid, "confidence": confidence, "status": status})
    
    if imported:
        db.execute("INSERT INTO events (topic_id, event_type, detail) VALUES (?,?,?)",
                   (None, "obsidian_import", json.dumps({"count": len(imported), "ids": [i['id'] for i in imported]})))
        db.commit()
    db.close()
    
    notify("findings_imported", {"count": len(imported)})
    return {"imported": len(imported), "skipped": len(skipped), "details": {"imported": imported, "skipped": skipped}}


@app.post("/api/findings/{finding_id}/verify")
def verify_finding(finding_id: str):
    """Mark a finding as human-verified. Boosts confidence based on source reliability."""
    db = get_db()
    finding = db.execute("SELECT * FROM findings WHERE id = ?", (finding_id,)).fetchone()
    if not finding:
        db.close()
        raise HTTPException(404, "Finding not found")
    
    old_conf = finding['confidence']
    # Verification boost: Bayesian update with human_verified reliability 0.90
    p_h = old_conf
    reliability = 0.90
    p_e_h = reliability
    p_e_not_h = 1 - reliability
    new_conf = round((p_e_h * p_h) / (p_e_h * p_h + p_e_not_h * (1 - p_h)), 4)
    new_conf = min(new_conf, 0.98)  # Cap
    
    db.execute("UPDATE findings SET verified = 1, confidence = ?, updated_at = CURRENT_TIMESTAMP WHERE id = ?",
               (new_conf, finding_id))
    db.execute("INSERT INTO confidence_history (finding_id, old_confidence, new_confidence, reason, source) VALUES (?,?,?,?,?)",
               (finding_id, old_conf, new_conf, "human verified", "human_verified"))
    
    score = _calc_compound_score(dict(finding) | {'confidence': new_conf})
    db.execute("UPDATE findings SET compound_score = ? WHERE id = ?", (score, finding_id))
    
    db.commit()
    db.close()
    notify("finding_verified", {"finding_id": finding_id, "confidence": new_conf})
    return {"id": finding_id, "old_confidence": old_conf, "new_confidence": new_conf, "verified": True}


# ── Health + Error Info ──

@app.get("/api/health")
def health():
    """Health check with error summary."""
    db = get_db()
    
    error_topics = db.execute("SELECT COUNT(*) as c FROM topics WHERE state = 'error'").fetchone()['c']
    pending_actions = db.execute("""
        SELECT COUNT(*) as c FROM events 
        WHERE event_type = 'action_queued' AND json_extract(detail, '$.status') = 'pending'
    """).fetchone()['c']
    failed_actions = db.execute("""
        SELECT COUNT(*) as c FROM events 
        WHERE event_type = 'action_queued' AND json_extract(detail, '$.status') = 'failed'
    """).fetchone()['c']
    total_topics = db.execute("SELECT COUNT(*) as c FROM topics").fetchone()['c']
    
    db.close()
    return {
        "status": "healthy" if error_topics == 0 and failed_actions == 0 else "degraded",
        "topics": total_topics,
        "error_topics": error_topics,
        "pending_actions": pending_actions,
        "failed_actions": failed_actions,
        "version": "0.10.0"
    }

# ── Email Send (via gog CLI) ──

import subprocess

class EmailRequest(BaseModel):
    to: str
    subject: str
    body: str
    account: str = "f.ziesche.us@gmail.com"
    attachments: List[str] = []
    topic_id: Optional[str] = None

@app.post("/api/actions/send-email")
def send_email(req: EmailRequest):
    """Send an email via gog gmail send."""
    import re
    # Validate email
    if not re.match(r'^[^\s@]+@[^\s@]+\.[^\s@]+$', req.to):
        raise HTTPException(400, f"Invalid email address: {req.to}")
    if len(req.subject.strip()) < 3:
        raise HTTPException(400, "Subject too short")
    if len(req.body.strip()) < 10:
        raise HTTPException(400, "Body too short")
    
    # Write body to temp file
    body_file = Path("/tmp/workbench_email_body.txt")
    body_file.write_text(req.body)
    
    cmd = [
        "gog", "gmail", "send",
        "--to", req.to,
        "--account", req.account,
        "--subject", req.subject,
        "--body-file", str(body_file)
    ]
    
    for att in req.attachments:
        if Path(att).exists():
            cmd.extend(["--attach", att])
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        success = result.returncode == 0
        
        # Log event
        if req.topic_id:
            db = get_db()
            event_detail = {
                "to": req.to, "subject": req.subject,
                "stdout": result.stdout[:500], "stderr": result.stderr[:500],
                "success": success
            }
            db.execute("INSERT INTO events (topic_id, event_type, detail) VALUES (?,?,?)",
                       (req.topic_id, "email_sent" if success else "email_failed",
                        json.dumps(event_detail)))
            if success:
                db.execute("INSERT INTO messages (topic_id, sender, content, msg_type) VALUES (?,?,?,?)",
                           (req.topic_id, "system", f"Email gesendet an {req.to}: \"{req.subject}\"", "text"))
                _advance_next_step(db, req.topic_id)
            else:
                db.execute("INSERT INTO messages (topic_id, sender, content, msg_type) VALUES (?,?,?,?)",
                           (req.topic_id, "system", f"Email-Versand fehlgeschlagen: {result.stderr[:200]}", "text"))
                db.execute("UPDATE topics SET state = 'error' WHERE id = ?", (req.topic_id,))
            db.commit()
            db.close()
            notify("message", {"topic_id": req.topic_id, "sender": "system"})
        
        if success:
            return {"status": "sent", "to": req.to, "subject": req.subject}
        else:
            raise HTTPException(500, f"gog error: {result.stderr[:300]}")
    except subprocess.TimeoutExpired:
        if req.topic_id:
            db = get_db()
            db.execute("INSERT INTO events (topic_id, event_type, detail) VALUES (?,?,?)",
                       (req.topic_id, "email_failed", json.dumps({"to": req.to, "error": "timeout"})))
            db.execute("UPDATE topics SET state = 'error' WHERE id = ?", (req.topic_id,))
            db.execute("INSERT INTO messages (topic_id, sender, content, msg_type) VALUES (?,?,?,?)",
                       (req.topic_id, "system", "Email-Versand: Timeout nach 30s", "text"))
            db.commit()
            db.close()
        raise HTTPException(504, "Email send timed out")
    except Exception as e:
        if req.topic_id:
            db = get_db()
            db.execute("INSERT INTO events (topic_id, event_type, detail) VALUES (?,?,?)",
                       (req.topic_id, "email_failed", json.dumps({"to": req.to, "error": str(e)[:500]})))
            db.execute("UPDATE topics SET state = 'error' WHERE id = ?", (req.topic_id,))
            db.commit()
            db.close()
        raise HTTPException(500, f"Unexpected error: {str(e)[:300]}")

# ── Serve Frontend ──
app.mount("/", StaticFiles(directory=str(STATIC_PATH), html=True), name="static")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
