# Lead Enrichment Pipeline - Dokumentation

## Übersicht

Automatisiertes System zur Recherche und Anreicherung von CNC-Leads mit personalisierten Outreach-Mails.

## Dateien

### 1. `lead-enrichment.sh`
**Bash-Script für manuelle/semi-automatische Nutzung**

```bash
./lead-enrichment.sh <input-file> <output-file>
```

**Input-Format:**
```
# Kommentare mit # beginnen
HUSS Maschinenbau
CPT Präzisionstechnik
Metalworkers Freital
```

**Output:** Markdown-Datei mit strukturiertem Template

**Nutzen:** 
- Schnell einsetzbar ohne zusätzliche Dependencies
- Erstellt strukturierte Templates die manuell ausgefüllt werden
- Gut für kleine Batches (5-10 Leads)

---

### 2. `lead-enrichment.py`
**Python-Script für vollautomatische Recherche**

```bash
python3 lead-enrichment.py <input-file> <output-file>
```

**Features:**
- Pain Point-Erkennung basierend auf Branche
- Email-Template-System mit Personalisierung
- Strukturierte Markdown-Ausgabe
- Erweiterbar mit OpenClaw Web Search Integration

**Hinweis:** Aktuell noch Referenz-Implementierung. Für tatsächliche Web-Recherche muss es als OpenClaw Agent laufen.

---

## Workflow

### Schritt 1: Input-Datei erstellen

Erstelle eine Textdatei mit Firmennamen (eine pro Zeile):

```bash
cat > leads.txt << EOF
HUSS Maschinenbau
CPT Präzisionstechnik
Metalworkers Freital
Dresdner Feinmechanik
EOF
```

### Schritt 2: Script ausführen

**Option A - Bash (semi-automatisch):**
```bash
./scripts/lead-enrichment.sh leads.txt sales/enriched-leads.md
```

**Option B - Python (automatisch):**
```bash
python3 scripts/lead-enrichment.py leads.txt sales/enriched-leads.md
```

**Option C - Als OpenClaw Agent (empfohlen für große Batches):**
```
Bitte King Agent: "Recherchiere diese 10 CNC Leads und erstelle personalisierte Outreach-Mails"
```

### Schritt 3: Ergebnisse prüfen und versenden

1. Output-Datei öffnen: `sales/enriched-leads-*.md`
2. Fehlende Daten ergänzen
3. Mails personalisieren wenn nötig
4. Copy-Paste in Email-Client oder CRM

---

## Output-Struktur

Jeder angereicherte Lead enthält:

### 📋 Firmenprofil
- Name, Standort, Website
- Email, Telefon (wenn gefunden)
- Kerngeschäft & Spezialisierung
- Mitarbeiterzahl (geschätzt)

### 🎯 Pain Points
- 3-5 identifizierte Schmerzpunkte
- Abgeleitet aus Branche und Produkten
- Basis für Personalisierung

### 📧 Outreach-Mail
- **Copy-paste ready**
- Deutsch, Siezen
- Konkreter Nutzen (Zeit-/Kostenersparnis)
- Kein "Wir", nur "Ich"
- 50% EFRE-Förderung erwähnt
- CTA: 15 Min Gespräch

### 📊 Quellen
- URLs der Recherche-Quellen
- Nachvollziehbarkeit

---

## Email-Ton (Wichtig!)

### ✅ DO:
- Deutsch, Siezen
- Direkt, kein Geschwafel
- Konkreter Nutzen (Zeitersparnis, Kostensenkung)
- "Ich" statt "Wir" (Florian ist Einzelunternehmer)
- MBS Schlottwitz als Referenz erwähnen
- 50% EFRE-Förderung als Hook
- Regionaler Bezug wenn möglich
- CTA: 15 Min Gespräch oder Vor-Ort-Termin

### ❌ DON'T:
- Keine Preise nennen
- Kein Consulting-Sprech
- Keine generischen Templates
- Keine langen Absätze (max. 6-8 Sätze)
- Keine em-dashes (—)
- Nicht wie AI klingen

### Beispiel-Hooks:

**Investment Hook:**
> "ich habe gesehen, dass Sie 2025 in eine neue Haas ST-25Y investiert haben. Glückwunsch zur Investition."

**Regional Hook:**
> "Ich komme aus der Region und habe gesehen, dass Sie in Sehmatal-Neudorf mit CNC-Zerspanung arbeiten."

**Research Hook:**
> "ich habe gesehen, dass CPT im InTeLeMat-Forschungsprojekt aktiv ist. Flexible Fertigung und Digitalisierung sind auch meine Themen."

---

## Pain Points nach Branche

### CNC-Zerspanung
1. Rüstzeitoptimierung bei wechselnden Auftragsgrößen
2. Maschinenbelegungsplanung über mehrere CNC-Maschinen
3. Manuelle Arbeitsvorbereitung bindet Kapazitäten
4. Kalkulation für individuelle Teile zeitaufwendig
5. Kapazitätsauslastung bei schwankender Auftragslage

### Präzisionsfertigung
1. Enge Toleranzen erfordern präzise Planung
2. Übergang Prototyp → Serie muss effizient gestaltet werden
3. Qualitätssicherung bei Kleinserien aufwendig
4. CAD/CAM-Integration optimierbar
5. Arbeitsvorbereitung für kundenspezifische Teile komplex

### Metallbearbeitung
1. Koordination verschiedener Fertigungsbereiche
2. Effizienz und Wirtschaftlichkeit bei manuellen Prozessen
3. Rüstzeiten reduzieren für schnelleren ROI
4. Maschinenbelegung bei heterogenem Maschinenpark
5. Auslastungsoptimierung nach Investitionen

---

## Integration mit OpenClaw

Für vollautomatische Nutzung als OpenClaw Agent:

```python
# In OpenClaw Agent Context:
results = web_search(
    query=f"{company_name} Sachsen CNC",
    count=5,
    country="DE"
)

# Ergebnisse parsen
company_data = extract_company_info(results)

# Mail generieren
email = generate_personalized_email(company_data)
```

---

## Beispiel-Run

```bash
$ ./scripts/lead-enrichment.sh test-leads.txt sales/test-output.md

═══════════════════════════════════════════════════════
  CNC LEAD ENRICHMENT PIPELINE
═══════════════════════════════════════════════════════

Input:  test-leads.txt
Output: sales/test-output.md

📋 Gefundene Leads: 5

[1/5] 🔍 Recherchiere: HUSS Maschinenbau
    → Web Search wird durchgeführt...

[2/5] 🔍 Recherchiere: CPT Präzisionstechnik
    → Web Search wird durchgeführt...

...

═══════════════════════════════════════════════════════
✅ FERTIG
═══════════════════════════════════════════════════════

📄 Output gespeichert: sales/test-output.md
📝 5 Leads verarbeitet
```

---

## Nächste Schritte

### Kurzfristig (Manual):
1. Script mit Leads nutzen
2. Fehlende Daten manuell recherchieren
3. Mails versenden
4. Response-Rate tracken

### Mittelfristig (Semi-Auto):
1. OpenClaw Web Search direkt integrieren
2. LinkedIn-Suche für Entscheider automatisieren
3. Email-Finder-API integrieren (Hunter.io, Snov.io)

### Langfristig (Full-Auto):
1. CRM-Integration (Notion/Airtable)
2. Automatisches Follow-up-System
3. Response-Tracking und A/B-Testing
4. Pipeline-Metriken Dashboard

---

## Troubleshooting

**Problem:** "Rate limit exceeded"  
**Lösung:** Pausen zwischen Suchen einbauen (sleep 2-5 Sekunden)

**Problem:** "Firma nicht gefunden"  
**Lösung:** Manuell recherchieren oder aus Liste entfernen

**Problem:** "Email zu generisch"  
**Lösung:** Mehr firmenpezifische Details in Personalisierung einbauen

---

*Erstellt: 09.02.2026 | Florian Ziesche*
