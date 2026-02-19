#!/usr/bin/env python3
"""
Trust System Merge Migration
Deprecates trust_scores (agent-level) → trust_skills (skill-level Bayesian) as single source of truth.

SAFE: No data deletion. Backs up DB, exports legacy data.
"""

import sqlite3
import json
import shutil
from pathlib import Path
from datetime import datetime

DB_PATH = Path(__file__).parent / "workbench.db"
BACKUP_PATH = Path(__file__).parent / f"workbench.db.bak-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
ARCHIVE_PATH = Path(__file__).parent / "trust_scores_archive.json"

def main():
    print("=" * 60)
    print("TRUST SYSTEM MERGE MIGRATION")
    print("=" * 60)
    print()
    
    # Step 1: Backup
    print("📦 Step 1: Backing up database...")
    if not DB_PATH.exists():
        print(f"❌ ERROR: Database not found at {DB_PATH}")
        return 1
    
    shutil.copy2(DB_PATH, BACKUP_PATH)
    print(f"✅ Backup created: {BACKUP_PATH}")
    print(f"   Size: {BACKUP_PATH.stat().st_size / 1024:.1f} KB")
    print()
    
    # Step 2: Connect
    print("🔌 Step 2: Connecting to database...")
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    print("✅ Connected")
    print()
    
    # Step 3: Export trust_scores
    print("💾 Step 3: Exporting trust_scores for archival...")
    cursor.execute("SELECT * FROM trust_scores ORDER BY agent")
    trust_scores = [dict(row) for row in cursor.fetchall()]
    
    if not trust_scores:
        print("⚠️  WARNING: trust_scores table is empty")
    else:
        print(f"✅ Found {len(trust_scores)} agent records:")
        for ts in trust_scores:
            print(f"   - {ts['agent']:12s} | score: {ts['score']:3d} | votes: ↑{ts['up_votes']} ↓{ts['down_votes']}")
    
    archive_data = {
        "exported_at": datetime.now().isoformat(),
        "source_table": "trust_scores",
        "reason": "Migration to trust_skills as single source of truth",
        "records": trust_scores
    }
    
    with open(ARCHIVE_PATH, 'w') as f:
        json.dump(archive_data, f, indent=2)
    
    print(f"✅ Archived to: {ARCHIVE_PATH}")
    print()
    
    # Step 4: Verify trust_skills
    print("🔍 Step 4: Verifying trust_skills table...")
    cursor.execute("SELECT * FROM trust_skills ORDER BY score DESC")
    trust_skills = [dict(row) for row in cursor.fetchall()]
    
    if not trust_skills:
        print("⚠️  WARNING: trust_skills table is empty! Migration may require seeding.")
    else:
        print(f"✅ Found {len(trust_skills)} skill records:")
        for ts in trust_skills[:10]:  # Show top 10
            print(f"   - {ts['skill']:20s} | score: {ts['score']:3d} | feedback: ↑{ts['up']} ↓{ts['down']}")
        if len(trust_skills) > 10:
            print(f"   ... and {len(trust_skills) - 10} more")
    print()
    
    # Step 5: Migration summary
    print("📊 Step 5: Migration Summary")
    print("-" * 60)
    print(f"trust_scores records:  {len(trust_scores)}")
    print(f"trust_skills records:  {len(trust_skills)}")
    print()
    print("Migration strategy:")
    print("  ✅ trust_scores exported to JSON (archive)")
    print("  ✅ trust_scores table kept (no drop, rollback safety)")
    print("  ✅ trust_skills is already primary (no data migration needed)")
    print()
    print("Next steps (manual):")
    print("  1. Update app.py endpoints to use trust_skills")
    print("  2. Deprecate GET /api/trust (add warning header)")
    print("  3. Redirect vote updates to trust_skills")
    print("  4. Update DB-SCHEMA.md")
    print("  5. Test all endpoints")
    print()
    
    # Step 6: Optional — Mark trust_scores as archived
    print("🏷️  Step 6: Mark trust_scores as deprecated (metadata)...")
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS _schema_metadata (
                table_name TEXT PRIMARY KEY,
                status TEXT,
                deprecated_at TEXT,
                notes TEXT
            )
        """)
        cursor.execute("""
            INSERT OR REPLACE INTO _schema_metadata (table_name, status, deprecated_at, notes)
            VALUES (?, ?, ?, ?)
        """, (
            "trust_scores",
            "deprecated",
            datetime.now().isoformat(),
            "Migrated to trust_skills (skill-level Bayesian). Kept for archival only."
        ))
        conn.commit()
        print("✅ Metadata updated: trust_scores marked as deprecated")
    except Exception as e:
        print(f"⚠️  Could not update metadata: {e}")
    print()
    
    conn.close()
    
    print("=" * 60)
    print("✅ MIGRATION COMPLETE")
    print("=" * 60)
    print()
    print(f"Backup:  {BACKUP_PATH}")
    print(f"Archive: {ARCHIVE_PATH}")
    print()
    print("Safe to proceed with code changes. Rollback: restore backup.")
    print()
    
    return 0

if __name__ == "__main__":
    exit(main())
