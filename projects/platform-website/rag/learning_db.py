#!/usr/bin/env python3
"""
Learning Database — SQLite-based cross-city intelligence system.
Replaces error_db.json + BEIPACKZETTEL.md with queryable database.

Usage:
  python3 learning_db.py init                    # Create DB
  python3 learning_db.py ingest <city>           # Ingest city JSON, extract patterns
  python3 learning_db.py ingest-all              # Ingest all cities
  python3 learning_db.py error <city> <type> <desc>  # Log error
  python3 learning_db.py rules                   # Show all active prevention rules
  python3 learning_db.py patterns                # Show cross-city patterns
  python3 learning_db.py briefing                # Generate agent briefing (for next spawn)
  python3 learning_db.py dashboard               # Full dashboard
  python3 learning_db.py contradictions          # Cross-city contradictions
"""

import sqlite3, json, sys, os, re
from datetime import datetime
from collections import Counter

DB_PATH = os.path.join(os.path.dirname(__file__), "learning.db")
CITIES_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "cities")


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    return conn


def init_db():
    conn = get_db()
    conn.executescript("""
    -- Cities metadata
    CREATE TABLE IF NOT EXISTS cities (
        slug TEXT PRIMARY KEY,
        gemeinde TEXT,
        typ TEXT,
        wahl_typ TEXT,
        einwohner INTEGER,
        source_count INTEGER DEFAULT 0,
        claim_count INTEGER DEFAULT 0,
        candidate_count INTEGER DEFAULT 0,
        validation_score INTEGER DEFAULT 0,
        has_ob_wahl BOOLEAN DEFAULT 1,
        agent_version TEXT,
        ingested_at TEXT,
        researched_at TEXT
    );

    -- All sources across all cities
    CREATE TABLE IF NOT EXISTS sources (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        city_slug TEXT,
        source_id TEXT,
        name TEXT,
        url TEXT,
        type TEXT,
        access_date TEXT,
        FOREIGN KEY (city_slug) REFERENCES cities(slug)
    );

    -- All claims across all cities
    CREATE TABLE IF NOT EXISTS claims (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        city_slug TEXT,
        claim_id TEXT,
        claim TEXT,
        eija TEXT,
        source_ref TEXT,
        confidence INTEGER,
        category TEXT,
        FOREIGN KEY (city_slug) REFERENCES cities(slug)
    );

    -- All candidates across all cities
    CREATE TABLE IF NOT EXISTS candidates (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        city_slug TEXT,
        slug TEXT,
        name TEXT,
        party TEXT,
        role TEXT,
        amtsinhaber BOOLEAN DEFAULT 0,
        bio TEXT,
        FOREIGN KEY (city_slug) REFERENCES cities(slug)
    );

    -- Errors caught by validation or manual review
    CREATE TABLE IF NOT EXISTS errors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        city_slug TEXT,
        error_type TEXT,
        severity TEXT DEFAULT 'MEDIUM',
        description TEXT,
        actual TEXT,
        prevention_rule_id INTEGER,
        caught_by TEXT,
        created_at TEXT DEFAULT (datetime('now')),
        FOREIGN KEY (city_slug) REFERENCES cities(slug),
        FOREIGN KEY (prevention_rule_id) REFERENCES prevention_rules(id)
    );

    -- Prevention rules (learned from errors)
    CREATE TABLE IF NOT EXISTS prevention_rules (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        rule TEXT UNIQUE,
        category TEXT,
        source_error_id INTEGER,
        times_prevented INTEGER DEFAULT 0,
        active BOOLEAN DEFAULT 1,
        created_at TEXT DEFAULT (datetime('now'))
    );

    -- Cross-city patterns
    CREATE TABLE IF NOT EXISTS patterns (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pattern_type TEXT,
        description TEXT,
        cities_involved TEXT,
        confidence INTEGER,
        evidence TEXT,
        created_at TEXT DEFAULT (datetime('now'))
    );

    -- Agent runs log
    CREATE TABLE IF NOT EXISTS agent_runs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        city_slug TEXT,
        prompt_version TEXT,
        runtime_seconds INTEGER,
        tokens_used INTEGER,
        validation_score INTEGER,
        errors_found INTEGER DEFAULT 0,
        schema_ok BOOLEAN DEFAULT 1,
        created_at TEXT DEFAULT (datetime('now'))
    );

    CREATE INDEX IF NOT EXISTS idx_sources_city ON sources(city_slug);
    CREATE INDEX IF NOT EXISTS idx_claims_city ON claims(city_slug);
    CREATE INDEX IF NOT EXISTS idx_candidates_city ON candidates(city_slug);
    CREATE INDEX IF NOT EXISTS idx_candidates_party ON candidates(party);
    CREATE INDEX IF NOT EXISTS idx_errors_type ON errors(error_type);
    CREATE INDEX IF NOT EXISTS idx_claims_eija ON claims(eija);
    """)

    # Seed prevention rules from known errors
    rules = [
        ("ALWAYS verify BM/OB title against official city website", "VERIFICATION"),
        ("ALL social media handles MUST be verified via web_search. No guessing.", "VERIFICATION"),
        ("Check if current Amtsinhaber is running again BEFORE building profile", "RESEARCH"),
        ("2020 election results MUST come from kommunalwahl2020.bayern.de only", "SOURCE"),
        ("Forecast percentages must sum to 95-105%. If not, re-research.", "VALIDATION"),
        ("tenant MUST be an object, not a string", "SCHEMA"),
        ("kb MUST be a dict of dicts, not an array or dict of arrays", "SCHEMA"),
        ("claim_ledger.eija must be string 'E','I','J', or 'A', not 'status' or dict", "SCHEMA"),
        ("quellenverzeichnis must be array of objects, not array of strings", "SCHEMA"),
        ("news MUST be an array [...], not an object {...}", "SCHEMA"),
        ("First check if OB-Wahl exists or only Stadtratswahl", "RESEARCH"),
        ("Bio must be at least 50 characters", "QUALITY"),
        ("No duplicate URLs in quellenverzeichnis", "QUALITY"),
    ]
    for rule, cat in rules:
        conn.execute("INSERT OR IGNORE INTO prevention_rules (rule, category) VALUES (?, ?)", (rule, cat))

    conn.commit()
    print(f"✅ Database initialized: {DB_PATH}")
    return conn


def ingest_city(slug, conn=None):
    """Ingest a city JSON into the database."""
    if conn is None:
        conn = get_db()

    path = os.path.join(CITIES_DIR, f"{slug}.json")
    if not os.path.exists(path):
        print(f"  ❌ {path} not found")
        return

    with open(path) as f:
        data = json.load(f)

    tenant = data.get("tenant", {})
    if isinstance(tenant, str):
        gemeinde = tenant
        typ = "unknown"
        wahl_typ = "unknown"
    else:
        gemeinde = tenant.get("gemeinde", slug)
        typ = tenant.get("typ", "unknown")
        wahl = tenant.get("wahl", {})
        wahl_typ = wahl.get("typ", "unknown") if isinstance(wahl, dict) else "unknown"

    sources = data.get("quellenverzeichnis", [])
    claims_data = data.get("claim_ledger", [])
    kb = data.get("kb", {})
    meta = data.get("_meta", {})

    # Determine if OB-Wahl exists
    has_ob = wahl_typ in ("OB-Wahl", "BM-Wahl")

    # Delete existing data for this city (re-ingest)
    for table in ["sources", "claims", "candidates"]:
        conn.execute(f"DELETE FROM {table} WHERE city_slug = ?", (slug,))

    # Insert city
    conn.execute("""
        INSERT OR REPLACE INTO cities
        (slug, gemeinde, typ, wahl_typ, source_count, claim_count, candidate_count, has_ob_wahl, agent_version, ingested_at, researched_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (slug, gemeinde, typ, wahl_typ, len(sources), len(claims_data), len(kb),
          has_ob, meta.get("agent", "unknown"), datetime.now().isoformat(), meta.get("last_enriched", "")))

    # Insert sources
    for s in sources:
        if isinstance(s, dict):
            conn.execute("INSERT INTO sources (city_slug, source_id, name, url, type, access_date) VALUES (?,?,?,?,?,?)",
                         (slug, s.get("id",""), s.get("name",""), s.get("url",""), s.get("type",""), s.get("accessDate","")))

    # Insert claims
    for c in claims_data:
        if isinstance(c, dict):
            eija = c.get("eija", c.get("status", ""))
            source_ref = c.get("source", "")
            if isinstance(source_ref, (dict, list)):
                source_ref = json.dumps(source_ref)
            conf = c.get("confidence", 0)
            if isinstance(conf, float) and conf <= 1:
                conf = int(conf * 100)
            if isinstance(eija, (dict, list)):
                eija = str(eija)
            tier = c.get("tier", "EPHEMERAL")
            conn.execute("INSERT INTO claims (city_slug, claim_id, claim, eija, source_ref, confidence, tier) VALUES (?,?,?,?,?,?,?)",
                         (slug, c.get("id",""), c.get("claim",""), eija, source_ref, conf, tier))

    # Insert candidates
    for cslug, cdata in kb.items():
        if isinstance(cdata, dict):
            conn.execute("INSERT INTO candidates (city_slug, slug, name, party, role, amtsinhaber, bio) VALUES (?,?,?,?,?,?,?)",
                         (slug, cslug, cdata.get("name",""), cdata.get("party",""), cdata.get("role",""),
                          cdata.get("amtsinhaber", False), cdata.get("bio","")))

    conn.commit()
    print(f"  ✅ {gemeinde}: {len(sources)} sources, {len(claims_data)} claims, {len(kb)} candidates")


def ingest_all():
    conn = get_db()
    for f in sorted(os.listdir(CITIES_DIR)):
        if f.endswith('.json') and f != 'internal.json':
            ingest_city(f.replace('.json', ''), conn)

    # Auto-detect cross-city patterns
    detect_patterns(conn)


def detect_patterns(conn):
    """Auto-detect cross-city patterns from ingested data."""
    # Pattern 1: Party dominance
    rows = conn.execute("""
        SELECT party, COUNT(*) as cnt, GROUP_CONCAT(DISTINCT city_slug) as cities
        FROM candidates WHERE amtsinhaber = 1 GROUP BY party ORDER BY cnt DESC
    """).fetchall()
    for r in rows:
        if r['cnt'] >= 2:
            conn.execute("""
                INSERT OR REPLACE INTO patterns (pattern_type, description, cities_involved, confidence, evidence)
                VALUES (?, ?, ?, ?, ?)
            """, ("PARTY_DOMINANCE", f"{r['party']} hat {r['cnt']} Amtsinhaber",
                  r['cities'], min(95, 50 + r['cnt'] * 10),
                  f"{r['cnt']} cities with {r['party']} incumbent"))

    # Pattern 2: No OB-Wahl cities
    no_ob = conn.execute("SELECT slug, gemeinde FROM cities WHERE has_ob_wahl = 0").fetchall()
    if no_ob:
        cities = ", ".join(r['slug'] for r in no_ob)
        conn.execute("""
            INSERT OR REPLACE INTO patterns (pattern_type, description, cities_involved, confidence, evidence)
            VALUES (?, ?, ?, ?, ?)
        """, ("NO_OB_WAHL", f"{len(no_ob)} Städte haben keine OB-Wahl (bereits gewählt)",
              cities, 100, "Agent-verified: OB already elected in prior year"))

    # Pattern 3: Source diversity
    rows = conn.execute("""
        SELECT city_slug, COUNT(DISTINCT type) as type_count, COUNT(*) as total
        FROM sources GROUP BY city_slug HAVING total >= 30
    """).fetchall()
    low_diversity = [r for r in rows if r['type_count'] < 3]
    if low_diversity:
        conn.execute("""
            INSERT OR REPLACE INTO patterns (pattern_type, description, cities_involved, confidence, evidence)
            VALUES (?, ?, ?, ?, ?)
        """, ("LOW_SOURCE_DIVERSITY", f"{len(low_diversity)} cities have <3 source types",
              ", ".join(r['city_slug'] for r in low_diversity), 80,
              "Source type analysis"))

    conn.commit()
    print(f"\n  📊 Patterns detected: {conn.execute('SELECT COUNT(*) FROM patterns').fetchone()[0]}")


def show_dashboard(conn=None):
    if conn is None:
        conn = get_db()

    print("\n" + "="*60)
    print("📊 LEARNING DATABASE DASHBOARD")
    print("="*60)

    # Overview
    stats = conn.execute("SELECT COUNT(*) as cities FROM cities").fetchone()
    src = conn.execute("SELECT COUNT(*) as n FROM sources").fetchone()
    clm = conn.execute("SELECT COUNT(*) as n FROM claims").fetchone()
    cand = conn.execute("SELECT COUNT(*) as n FROM candidates").fetchone()
    err = conn.execute("SELECT COUNT(*) as n FROM errors").fetchone()
    rules = conn.execute("SELECT COUNT(*) as n, SUM(times_prevented) as prevented FROM prevention_rules WHERE active=1").fetchone()

    print(f"\n  Cities: {stats['cities']}")
    print(f"  Sources: {src['n']}")
    print(f"  Claims: {clm['n']}")
    print(f"  Candidates: {cand['n']}")
    print(f"  Errors logged: {err['n']}")
    print(f"  Active rules: {rules['n']} (prevented: {rules['prevented'] or 0})")

    # Party breakdown
    print(f"\n--- Candidates by Party ---")
    for r in conn.execute("SELECT party, COUNT(*) as cnt FROM candidates WHERE party != '' GROUP BY party ORDER BY cnt DESC LIMIT 10"):
        print(f"  {r['party']}: {r['cnt']}")

    # Amtsinhaber by party
    print(f"\n--- Amtsinhaber by Party ---")
    for r in conn.execute("SELECT party, COUNT(*) as cnt FROM candidates WHERE amtsinhaber=1 AND party != '' GROUP BY party ORDER BY cnt DESC"):
        print(f"  {r['party']}: {r['cnt']}")

    # Cities without OB-Wahl
    no_ob = conn.execute("SELECT gemeinde FROM cities WHERE has_ob_wahl = 0").fetchall()
    if no_ob:
        print(f"\n--- Keine OB-Wahl (nur Stadtrat) ---")
        for r in no_ob:
            print(f"  {r['gemeinde']}")

    # EIJA distribution
    print(f"\n--- Claims by EIJA ---")
    for r in conn.execute("SELECT eija, COUNT(*) as cnt FROM claims WHERE eija IN ('E','I','J','A') GROUP BY eija ORDER BY cnt DESC"):
        print(f"  {r['eija']}: {r['cnt']}")

    # Source types
    print(f"\n--- Sources by Type ---")
    for r in conn.execute("SELECT type, COUNT(*) as cnt FROM sources WHERE type != '' GROUP BY type ORDER BY cnt DESC LIMIT 8"):
        print(f"  {r['type']}: {r['cnt']}")

    # Top domains
    print(f"\n--- Top Source Domains ---")
    for r in conn.execute("""
        SELECT SUBSTR(url, INSTR(url, '//') + 2,
               CASE WHEN INSTR(SUBSTR(url, INSTR(url, '//') + 2), '/') > 0
               THEN INSTR(SUBSTR(url, INSTR(url, '//') + 2), '/') - 1
               ELSE LENGTH(url) END) as domain,
        COUNT(*) as cnt FROM sources WHERE url LIKE 'http%' GROUP BY domain ORDER BY cnt DESC LIMIT 10
    """):
        print(f"  {r['domain']}: {r['cnt']}")

    # Duplicate URLs across cities
    print(f"\n--- Cross-City Duplicate URLs ---")
    dupes = conn.execute("""
        SELECT url, COUNT(DISTINCT city_slug) as cities, GROUP_CONCAT(DISTINCT city_slug) as which
        FROM sources WHERE url != '' GROUP BY url HAVING cities > 1 ORDER BY cities DESC LIMIT 5
    """).fetchall()
    for r in dupes:
        print(f"  {r['url'][:60]}... → {r['cities']} cities ({r['which']})")
    if not dupes:
        print("  (none)")

    # Patterns
    print(f"\n--- Cross-City Patterns ---")
    for r in conn.execute("SELECT pattern_type, description, confidence FROM patterns ORDER BY confidence DESC"):
        print(f"  [{r['confidence']}%] {r['description']}")


def generate_briefing():
    """Generate a briefing for the next agent based on all learnings."""
    conn = get_db()

    print("\n## Agent Briefing (auto-generated from Learning DB)")
    print()

    # Active rules
    print("### Prevention Rules")
    for r in conn.execute("SELECT rule, category, times_prevented FROM prevention_rules WHERE active=1 ORDER BY times_prevented DESC"):
        print(f"- [{r['category']}] {r['rule']} (prevented {r['times_prevented']}x)")

    # Patterns
    print("\n### Cross-City Patterns")
    for r in conn.execute("SELECT description, confidence FROM patterns WHERE confidence >= 70 ORDER BY confidence DESC"):
        print(f"- [{r['confidence']}%] {r['description']}")

    # Common errors
    print("\n### Common Error Types")
    for r in conn.execute("SELECT error_type, COUNT(*) as cnt FROM errors GROUP BY error_type ORDER BY cnt DESC LIMIT 5"):
        print(f"- {r['error_type']}: {r['cnt']}x")

    # Cities without OB-Wahl
    no_ob = conn.execute("SELECT gemeinde FROM cities WHERE has_ob_wahl = 0").fetchall()
    if no_ob:
        print(f"\n### Cities WITHOUT OB-Wahl (already elected)")
        for r in no_ob:
            print(f"- {r['gemeinde']}")


def show_contradictions():
    """Find contradictions across cities."""
    conn = get_db()
    print("\n--- Cross-City Contradictions ---")

    # Check if same person appears in multiple cities with different data
    dupes = conn.execute("""
        SELECT name, GROUP_CONCAT(DISTINCT city_slug) as cities, GROUP_CONCAT(DISTINCT party) as parties
        FROM candidates GROUP BY name HAVING COUNT(DISTINCT city_slug) > 1
    """).fetchall()
    for r in dupes:
        if len(set(r['parties'].split(','))) > 1:
            print(f"  ⚠️ {r['name']}: different parties across {r['cities']} ({r['parties']})")

    if not dupes:
        print("  ✅ No contradictions found")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "init":
        init_db()
    elif cmd == "ingest":
        conn = get_db()
        ingest_city(sys.argv[2], conn)
    elif cmd == "ingest-all":
        ingest_all()
    elif cmd == "error":
        conn = get_db()
        conn.execute("INSERT INTO errors (city_slug, error_type, description) VALUES (?,?,?)",
                     (sys.argv[2], sys.argv[3], sys.argv[4]))
        conn.commit()
        print(f"  ✅ Error logged for {sys.argv[2]}")
    elif cmd == "rules":
        conn = get_db()
        for r in conn.execute("SELECT * FROM prevention_rules WHERE active=1"):
            print(f"  [{r['category']}] {r['rule']} (prevented {r['times_prevented']}x)")
    elif cmd == "patterns":
        conn = get_db()
        detect_patterns(conn)
        for r in conn.execute("SELECT * FROM patterns ORDER BY confidence DESC"):
            print(f"  [{r['confidence']}%] {r['pattern_type']}: {r['description']}")
    elif cmd == "briefing":
        generate_briefing()
    elif cmd == "dashboard":
        show_dashboard()
    elif cmd == "contradictions":
        show_contradictions()
    else:
        print(f"Unknown command: {cmd}")
        print(__doc__)
