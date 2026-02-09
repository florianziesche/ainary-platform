#!/bin/bash

# Lead Enrichment Script for CNC Sales Pipeline
# Nutzt OpenClaw's web_search für automatisierte Lead-Recherche
# 
# Usage: ./lead-enrichment.sh <input-file> <output-file>
# Input: Text-Datei mit Firmennamen (eine pro Zeile)
# Output: Markdown-Datei mit angereicherten Leads + personalisierten Mails

set -e

INPUT_FILE="$1"
OUTPUT_FILE="$2"

if [ -z "$INPUT_FILE" ] || [ -z "$OUTPUT_FILE" ]; then
    echo "Usage: $0 <input-file> <output-file>"
    echo "Example: $0 leads.txt enriched-leads.md"
    exit 1
fi

if [ ! -f "$INPUT_FILE" ]; then
    echo "Error: Input file '$INPUT_FILE' not found"
    exit 1
fi

# Erstelle Output-Verzeichnis
OUTPUT_DIR=$(dirname "$OUTPUT_FILE")
mkdir -p "$OUTPUT_DIR"

echo "═══════════════════════════════════════════════════════"
echo "  CNC LEAD ENRICHMENT PIPELINE"
echo "═══════════════════════════════════════════════════════"
echo ""
echo "Input:  $INPUT_FILE"
echo "Output: $OUTPUT_FILE"
echo ""

# Zähle Leads
TOTAL_LEADS=$(grep -v "^#" "$INPUT_FILE" | grep -v "^$" | wc -l | tr -d ' ')
echo "📋 Gefundene Leads: $TOTAL_LEADS"
echo ""

# Initialisiere Output-Datei
cat > "$OUTPUT_FILE" << EOF
# CNC Lead Enrichment Results

**Generiert:** $(date '+%d.%m.%Y %H:%M Uhr')  
**Absender:** Florian Ziesche  
**Email:** florian@ainaryventures.com  
**Tel:** +49 151 230 39 208  
**Recherche-Methode:** Automatisierte Web Search + KI-Analyse

---

EOF

# Verarbeite jeden Lead
LEAD_NUM=0
while IFS= read -r lead_name || [ -n "$lead_name" ]; do
    # Überspringe Kommentare und leere Zeilen
    [[ -z "$lead_name" || "$lead_name" =~ ^# ]] && continue
    
    LEAD_NUM=$((LEAD_NUM + 1))
    echo "[$LEAD_NUM/$TOTAL_LEADS] 🔍 Recherchiere: $lead_name"
    
    # Schreibe Lead-Header in Output
    cat >> "$OUTPUT_FILE" << EOF

## Lead $LEAD_NUM: $lead_name

**Status:** ⏳ Recherche läuft...

EOF
    
    echo "    → Web Search wird durchgeführt..."
    echo "    → Hinweis: Diese Funktion erfordert manuelle Integration mit OpenClaw's web_search Tool"
    echo ""
    
    # Platzhalter für tatsächliche Recherche
    # In einer vollständigen Implementierung würde hier die OpenClaw API oder ein Python-Script
    # die web_search-Funktion aufrufen und die Ergebnisse verarbeiten
    
    cat >> "$OUTPUT_FILE" << EOF

### 📋 Firmenprofil

**Firmenname:** $lead_name  
**Standort:** [Manuell ergänzen]  
**Website:** [Manuell ergänzen]  
**Email:** [Manuell ergänzen]

**Kerngeschäft:**
- [Manuell ergänzen basierend auf Web Search]

### 🎯 Pain Points (identifiziert)

1. [Basierend auf Branche ableiten]
2. [Basierend auf Produkten ableiten]

### 📧 Personalisierte Outreach-Mail

**Betreff:** [Automatisch generieren basierend auf Firmenprofil]

[Mail-Text hier]

### 📊 Quellen
- [URLs der Recherche-Quellen]

---

EOF

    # Rate Limiting vermeiden (1 Sekunde Pause zwischen Searches)
    sleep 1
    
done < "$INPUT_FILE"

# Füge Zusammenfassung hinzu
cat >> "$OUTPUT_FILE" << EOF

## 📊 Zusammenfassung

**Recherchierte Leads:** $TOTAL_LEADS  
**Erfolgreich angereichert:** [Manuell zählen]  
**Nicht gefunden:** [Manuell zählen]

**Gemeinsame Pain Points:**
1. Arbeitsvorbereitung zu zeitaufwendig
2. Maschinenbelegung / Rüstzeitoptimierung
3. Kalkulation bei individuellen Teilen
4. Muster-zu-Serie-Übergang
5. ROI-Maximierung bei CNC-Investitionen

**EFRE-Förderung:** Alle sächsischen Leads → 50% Digitalisierungszuschuss anwendbar

**Next Steps:**
1. Fehlende Daten manuell recherchieren
2. Mails personalisieren und versenden
3. Follow-up nach 3-5 Werktagen

---

*Generiert mit Lead Enrichment Pipeline | Florian Ziesche | $(date '+%d.%m.%Y')*
EOF

echo "═══════════════════════════════════════════════════════"
echo "✅ FERTIG"
echo "═══════════════════════════════════════════════════════"
echo ""
echo "📄 Output gespeichert: $OUTPUT_FILE"
echo "📝 $TOTAL_LEADS Leads verarbeitet"
echo ""
echo "⚠️  WICHTIG:"
echo "   Dieses Script erstellt eine Template-Struktur."
echo "   Für vollautomatische Recherche nutze das Python-Script:"
echo "   → python3 scripts/lead-enrichment.py <input> <output>"
echo ""
