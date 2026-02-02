# Google Drive — florian@ainaryventures.com

*Zentrales Dokumentations- und Asset-Management für alle Projekte*

---

## 📂 Ordnerstruktur

```
florian@ainaryventures.com/
│
├── 00_DOCUMENTATION/           ← Technische Dokumentation
│   ├── SYSTEMS/                ← System-Dokumentation
│   ├── CHANGELOG/              ← Versions-History
│   └── USER_GUIDES/            ← Nutzeranleitungen
│
├── 10_PROJECTS/                ← Projekt-Assets (Bilder, PDFs)
│   ├── Ainary_Ventures/        ← Pitch Decks, Brand Materials
│   ├── CNC_Planner/            ← Screenshots, Demo-PDFs
│   ├── Legal/                  ← Verträge, Legal Docs
│   ├── VC_Career/              ← Research PDFs, Interview Prep
│   └── Vertical_AI/            ← AI Research Materials
│
├── 20_ASSETS/                  ← Medien & Vorlagen
│   ├── Brand/                  ← Logos, Brand Guidelines
│   ├── Headshots/              ← Profilbilder
│   ├── Screenshots/            ← App Screenshots
│   └── Templates/              ← Design Templates
│
├── 30_CONTENT/                 ← Content für Blog/Social
│   └── Blog/                   ← Blog-Assets
│
├── 80_ARCHIVE/                 ← Abgeschlossene/alte Projekte
│
└── 90_SYNC_LOG/                ← Sync-Protokolle
    └── daily_logs/             ← Tägliche Sync-Reports
```

---

## 🔄 Sync-Strategie

### Was wird synchronisiert

| Quelle | Dateitypen | Ziel |
|--------|------------|------|
| `~/.openclaw/workspace/` | `*.png, *.jpg, *.pdf, *.docx` | `10_PROJECTS/` |
| `~/FZ/` | Heavy Files | Entsprechende Ordner |
| Obsidian Attachments | Bilder, PDFs | `20_ASSETS/` |

### Was NICHT synchronisiert wird

- Markdown-Dateien (bleiben in Git/Obsidian)
- Code-Dateien (`.py`, `.js`, `.html`, etc.)
- Config-Dateien
- `node_modules`, `.git`, Cache-Ordner

### Sync-Zeitplan

- **Täglich 23:00 CET**: Automatischer Sync via OpenClaw Cron
- **Manuell**: Bei Bedarf via `scripts/gdrive-sync.sh`

---

## 📋 Workflow

### Neue Datei hinzufügen

1. Datei lokal erstellen/bearbeiten
2. Nächster automatischer Sync lädt hoch
3. Oder: Manuell `gog drive upload <datei> --parent <folder-id>`

### Datei suchen

```bash
gog drive search "query" --account florian@ainaryventures.com
```

### Datei herunterladen

```bash
gog drive download <file-id> --out ./local-path/
```

---

## 🔑 Wichtige Ordner-IDs

| Ordner | ID |
|--------|-----|
| 00_DOCUMENTATION | `13Q-ZnEEvn4I2FFwRxefbCXNmZ2dU2MBA` |
| 10_PROJECTS | `1CfJZ9hjr58vOnQPMJyTWvfSo_dQ0Xn_3` |
| 20_ASSETS | `1OUM8qpHiBWldQGfE0BVFb8aQohvn7YTr` |
| 30_CONTENT | `1V3aQXLMf32ZROcweoyWcpL9xXsEVyeVv` |
| 80_ARCHIVE | `1ZgOPTkfxOfybS-upqJ9SEUZ66VCuAGCI` |
| 90_SYNC_LOG | `1DKkszu3fHRckTWHFkwNnJdj4Hz63WS6K` |

Vollständige Mapping: `scripts/gdrive-config.json`

---

## 📝 Dokumentation

### System-Dokumentation (00_DOCUMENTATION/SYSTEMS/)

- **OpenClaw.md** — Konfiguration, Skills, Memory-System
- **CNC_Planner.md** — Architektur, Features, Versionen
- **Obsidian_Setup.md** — Vault-Struktur, Plugins
- **Google_Workspace.md** — API Setup, Accounts

### Changelog (00_DOCUMENTATION/CHANGELOG/)

- Monatliche Änderungsprotokolle
- Automatisch aktualisiert beim Daily Sync

### User Guides (00_DOCUMENTATION/USER_GUIDES/)

- **Daily_Workflow.md** — Tägliche Routinen
- **Tools_Reference.md** — Quick Reference

---

## 🛠️ Wartung

### Alte Dateien archivieren

```bash
gog drive move <file-id> --parent 1ZgOPTkfxOfybS-upqJ9SEUZ66VCuAGCI
```

### Struktur prüfen

```bash
gog drive ls --account florian@ainaryventures.com
```

---

*Erstellt: 2026-02-02*
*Letzte Aktualisierung: 2026-02-02*
