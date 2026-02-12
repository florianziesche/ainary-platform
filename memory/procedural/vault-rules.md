# Vault Rules — Obsidian PARA, Linking, Tags

*Prozedurales Gedächtnis: Wie organisiere ich Obsidian?*  
*Quelle: MEMORY.md, standards/LINKING-RULES.md*  
*Aktualisiert: 2026-02-10*

---

## PARA-Struktur (7 Top-Level Folders)

```
System_OS/
├── 00-Inbox/          — Quick capture, process weekly
├── 01-Daily/          — Daily notes (YYYY-MM-DD.md)
├── 10-Projects/       — Active work by priority
├── 20-Areas/          — Areas of responsibility (ongoing)
├── 60-Resources/      — Reference, Knowledge (evergreen)
├── 70-Templates/      — Reusable structures
├── 80-Archive/        — Done but worth keeping
└── 99-System/         — Meta, vault guide
```

**Changed from 13 → 7 folders** (Vault Umbau v3, Feb 2026)

**Key Insight:**
- **HOF** (House of Funds) = VC Career → 10-Projects/VC-Career/
- **CNC** = Freelance → 20-Areas/Freelance-CNC/
- **Kommunal** = Tag-Kategorie, kein eigener Ordner

---

## Linking Rules

**Read full rules:** `standards/LINKING-RULES.md`

### Wikilink Format

✅ **Richtig:** `[[Filename]]`  
❌ **Falsch:** `[[Ordner/Filename]]`

**Warum:** Obsidian findet Dateien automatisch, Ordner-Pfade brechen bei Umstrukturierungen.

---

### Inline Links (mit Kontext)

✅ **Richtig:**
```markdown
Florian's technical background in [[CNC-Fertigung]] gives him an edge in manufacturing AI consulting.
```

❌ **Falsch:**
```markdown
See also: [[CNC-Fertigung]]
```

**Warum:** Link muss sich natürlich in den Text einfügen, nicht als isolierter Verweis.

---

### Max 3-5 Links pro Datei

**Zu viele Links = Noise.**

**Regel:** Nur verlinken wenn es wirklich relevant ist. Backlinks sind automatisch in Obsidian.

---

### KEINE "Related" Sections

❌ **Falsch:**
```markdown
## Related
- [[File1]]
- [[File2]]
- [[File3]]
```

**Warum:** Backlinks Panel in Obsidian zeigt das automatisch. Doppelt verlinken = doppelte Arbeit.

---

## Tags vs Links

### Tags für Kategorien

```markdown
#freelance #vc #cnc #content #kommunal
```

**Use:** Gruppierung, Filterung, Themen

---

### Links für Beziehungen

```markdown
[[Person]], [[Project]], [[Company]]
```

**Use:** Konkrete Verbindungen zwischen Entitäten

---

### Beispiel

```markdown
#vc #application

Applied to [[House of Funds]] on 2026-02-08. 
Used [[VC-Thesis]] from [[Decile-Hub-Sprint-2]].
```

---

## Daily Notes (01-Daily/)

**Format:** `YYYY-MM-DD.md`

**Inhalt:**
- Was ist passiert?
- Entscheidungen, Learnings, Kontext
- Links zu relevanten Projects/Areas

**Review:** Weekly → Important stuff → Resources/Knowledge

---

## Projects (10-Projects/)

**Kriterien:**
- Hat ein **klares Ende** (Timeline)
- Aktiv in Arbeit
- Priorität: 1-5

**Wenn fertig:** → 80-Archive/

---

## Areas (20-Areas/)

**Kriterien:**
- **Ongoing** responsibility (kein Ende)
- z.B. Freelance-CNC, Health, Relationships

**Nicht archivieren!** Areas bleiben aktiv.

---

## Resources (60-Resources/)

**Kriterien:**
- **Evergreen** knowledge
- Reference, nicht action-orientiert
- z.B. CNC-Fertigung.md, Kommunal-KI.md, VC-Landscape.md

**Subfolders:**
```
60-Resources/
├── Knowledge/       — Fachwissen (CNC, AI, VC)
├── Templates/       — Wiederverwendbare Vorlagen
└── Reference/       — Nachschlagewerke
```

---

## Archive (80-Archive/)

**Kriterien:**
- Projekt done
- Nicht mehr aktiv, aber worth keeping
- Reference für später

**Nicht löschen!** Archive > Delete.

---

## Frontmatter (optional aber empfohlen)

```yaml
---
tags: [vc, application]
status: in-progress
created: 2026-02-08
updated: 2026-02-10
---
```

**Use:** Macht Dateien filterbar, sortierbar.

---

## Naming Conventions

- **Kebab-case:** `vc-application-hof.md`
- **Descriptive:** Name sagt was drin ist
- **No dates in filename** (außer Daily Notes)

---

## Anti-Patterns

❌ **Folder-basierte Wikilinks:** `[[10-Projects/File]]`  
❌ **Related Sections:** Obsidian macht das automatisch  
❌ **Zu viele Tags:** 3-5 max pro Datei  
❌ **Nested folders >3 levels:** Flache Struktur ist besser  

---

## Workflow

1. **Capture:** 00-Inbox/
2. **Process:** Weekly review → Move to Projects/Areas/Resources
3. **Link:** Inline, mit Kontext, max 3-5
4. **Tag:** Kategorien (#vc #cnc #content)
5. **Archive:** Wenn done → 80-Archive/

---

## Vault Location

```
~/Library/Mobile Documents/iCloud~md~obsidian/Documents/System_OS/
```

**Sync:** iCloud (automatisch)

---

## Related

- `standards/LINKING-RULES.md` — Vollständige Linking-Dokumentation
- `memory/semantic/technical-setup.md` — Obsidian-Setup
- `Vault/99-System/` — Vault Meta-Dokumentation

---

*PARA = Projects, Areas, Resources, Archive. Keep it simple.*
