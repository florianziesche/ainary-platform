"""
Execution Platform Backend — MVP
FastAPI + SQLite. Topics, Messages, Votes, Trust.
"""

from fastapi import FastAPI, HTTPException, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import Optional, List, Set
import sqlite3
import json
import os
import asyncio
from datetime import datetime
from pathlib import Path

DB_PATH = Path(__file__).parent / "workbench.db"
STATIC_PATH = Path(__file__).parent.parent  # serves index.html

app = FastAPI(title="Execution Platform")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

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
        CREATE TABLE IF NOT EXISTS topics (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            stage TEXT DEFAULT 'revenue',
            parent_id TEXT,
            progress INTEGER DEFAULT 0,
            meta TEXT DEFAULT '{}',
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            updated_at TEXT DEFAULT CURRENT_TIMESTAMP
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
    conns = db.execute("""
        SELECT c.*, t.name as target_name FROM connections c 
        JOIN topics t ON c.to_topic = t.id 
        WHERE c.from_topic = ?
    """, (topic_id,)).fetchall()
    
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
    for stage in ['research', 'systems', 'content', 'revenue']:
        row = db.execute("SELECT COUNT(*) as count, AVG(progress) as avg_progress FROM topics WHERE stage = ?", (stage,)).fetchone()
        stages[stage] = {"count": row['count'], "avg_progress": row['avg_progress'] or 0}
    
    total_votes = db.execute("SELECT COUNT(*) as c FROM votes").fetchone()['c']
    outcomes = db.execute("SELECT COUNT(*) as c FROM topics WHERE progress = 100").fetchone()['c']
    db.close()
    
    return {
        "stages": stages,
        "total_items": sum(s['count'] for s in stages.values()),
        "outcomes": outcomes,
        "total_votes": total_votes
    }

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

# ── Serve Frontend ──
app.mount("/", StaticFiles(directory=str(STATIC_PATH), html=True), name="static")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
