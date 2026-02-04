# n8n Workflow: CNC Planner Lead-Automation

*Erstellt: 2026-02-03 | ENGINEER*

---

## 🎯 Ziel

Minimaler manueller Aufwand beim Outreach für 11 CNC-Leads in Sachsen/Thüringen.
**Florian reviewed nur noch fertige Email-Drafts und klickt "Approve".**

---

## 1. Workflow-Diagramm (ASCII)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        CNC LEAD OUTREACH AUTOMATION                          │
└─────────────────────────────────────────────────────────────────────────────┘

    ┌──────────────┐
    │   TRIGGER    │
    │ Google Sheet │──── Neue Zeile mit Status "New"
    │  (Webhook)   │
    └──────┬───────┘
           │
           ▼
    ┌──────────────┐
    │  ENRICHMENT  │
    │  HTTP Node   │──── Website scrapen (wenn vorhanden)
    │              │──── Firmenname + Branche extrahieren
    └──────┬───────┘
           │
           ▼
    ┌──────────────┐
    │ AI DRAFTING  │
    │  OpenAI/     │──── Personalisierte Email generieren
    │  Claude API  │──── Bezug auf Firma + Pain Points
    └──────┬───────┘
           │
           ▼
    ┌──────────────┐
    │ REVIEW QUEUE │
    │ Google Sheet │──── Draft in "Review" Tab schreiben
    │   Update     │──── Status → "Pending Review"
    └──────┬───────┘
           │
           │ (Florian reviewed manuell)
           │
           ▼
    ┌──────────────┐
    │   TRIGGER 2  │
    │ Google Sheet │──── Status wird "Approved"
    │  (Webhook)   │
    └──────┬───────┘
           │
           ▼
    ┌──────────────┐
    │  SEND EMAIL  │
    │   Gmail /    │──── Email an Lead senden
    │   SMTP Node  │──── CC an Florian
    └──────┬───────┘
           │
           ▼
    ┌──────────────┐
    │   UPDATE     │
    │ Google Sheet │──── Status → "Sent"
    │              │──── Sent Date eintragen
    └──────────────┘
```

---

## 2. Benötigte n8n Nodes

### Workflow A: Lead → Draft

| # | Node | Typ | Funktion |
|---|------|-----|----------|
| 1 | **Trigger** | Google Sheets Trigger | Neue Zeilen erkennen |
| 2 | **Filter** | IF | Nur Status = "New" |
| 3 | **HTTP Request** | HTTP | Website scrapen (optional) |
| 4 | **AI Node** | OpenAI / HTTP Request (Claude) | Email-Draft generieren |
| 5 | **Google Sheets** | Update Row | Draft + Status speichern |

### Workflow B: Approval → Send

| # | Node | Typ | Funktion |
|---|------|-----|----------|
| 1 | **Trigger** | Google Sheets Trigger | Zeilen-Updates erkennen |
| 2 | **Filter** | IF | Nur Status = "Approved" |
| 3 | **Gmail** | Gmail / SMTP | Email versenden |
| 4 | **Google Sheets** | Update Row | Status → "Sent" |

---

## 3. Setup-Anleitung (Step by Step)

### Phase 1: Google Sheet vorbereiten (10 min)

1. **Neues Google Sheet erstellen:** `CNC Lead Pipeline`

2. **Spalten anlegen:**
   ```
   A: ID
   B: Firma
   C: Ort
   D: Kontakt (Name)
   E: Email
   F: Telefon
   G: Website
   H: Warum (Pain Point)
   I: Status (New / Pending Review / Approved / Sent / Replied)
   J: Email Draft (Subject)
   K: Email Draft (Body)
   L: Sent Date
   M: Notes
   ```

3. **Leads aus cnc-leads-sachsen-thueringen.md importieren**

4. **Alle neuen Leads: Status = "New"**

---

### Phase 2: n8n Workflow A — Lead Processing (20 min)

#### Node 1: Google Sheets Trigger
```json
{
  "operation": "onRowAdded",
  "sheetId": "[DEINE_SHEET_ID]",
  "range": "Leads!A:M",
  "options": {
    "pollTimes": {
      "mode": "everyMinute"
    }
  }
}
```

#### Node 2: IF (Filter)
```
Condition: {{$json["Status"]}} equals "New"
```

#### Node 3: HTTP Request (Website Scrape) — OPTIONAL
```json
{
  "method": "GET",
  "url": "={{$json['Website']}}",
  "options": {
    "timeout": 5000
  }
}
```
*Hinweis: Kann übersprungen werden wenn Website nicht verfügbar*

#### Node 4: OpenAI / Claude API
```json
{
  "model": "gpt-4o",
  "messages": [
    {
      "role": "system",
      "content": "Du schreibst Cold Emails für CNC Planner, eine Fertigungsplanungssoftware. Stil: Professionell, direkt, keine Floskeln. Max 150 Wörter. Erwähne einen konkreten Pain Point der Firma."
    },
    {
      "role": "user",
      "content": "Firma: {{$json['Firma']}}\nOrt: {{$json['Ort']}}\nKontakt: {{$json['Kontakt']}}\nBranche/Info: {{$json['Warum']}}\n\nSchreibe eine personalisierte Cold Email mit:\n1. Subject Line\n2. Body\n\nFormat: JSON mit 'subject' und 'body'"
    }
  ]
}
```

#### Node 5: Google Sheets Update
```json
{
  "operation": "update",
  "sheetId": "[DEINE_SHEET_ID]",
  "range": "Leads!I:K",
  "values": [
    ["Pending Review", "{{$json.subject}}", "{{$json.body}}"]
  ]
}
```

---

### Phase 3: n8n Workflow B — Send on Approval (15 min)

#### Node 1: Google Sheets Trigger
```json
{
  "operation": "onRowUpdated",
  "sheetId": "[DEINE_SHEET_ID]",
  "range": "Leads!A:M"
}
```

#### Node 2: IF (Filter)
```
Condition: {{$json["Status"]}} equals "Approved"
```

#### Node 3: Gmail Node
```json
{
  "operation": "send",
  "to": "={{$json['Email']}}",
  "subject": "={{$json['Email Draft (Subject)']}}",
  "message": "={{$json['Email Draft (Body)']}}",
  "options": {
    "ccList": "florian@example.com"
  }
}
```

#### Node 4: Google Sheets Update
```json
{
  "operation": "update",
  "values": [
    ["Sent", "={{$now.format('YYYY-MM-DD')}}"]
  ]
}
```

---

## 4. Was Florian manuell einrichten muss

### API Keys & Credentials

| Service | Was wird benötigt | Wo holen |
|---------|-------------------|----------|
| **Google Sheets** | OAuth2 Credentials | n8n → Credentials → Google Sheets OAuth2 |
| **Gmail** | OAuth2 Credentials | n8n → Credentials → Gmail OAuth2 |
| **OpenAI** | API Key | platform.openai.com → API Keys |
| *Optional: Claude* | API Key | console.anthropic.com → API Keys |

### Manuelle Schritte

1. [ ] Google Sheet erstellen mit obiger Struktur
2. [ ] 11 Leads aus Markdown in Sheet kopieren
3. [ ] n8n: Google OAuth2 Credentials einrichten
4. [ ] n8n: Gmail OAuth2 Credentials einrichten
5. [ ] n8n: OpenAI API Key hinterlegen
6. [ ] Workflow A importieren/bauen
7. [ ] Workflow B importieren/bauen
8. [ ] Test mit einem Dummy-Lead

---

## 5. Geschätzter Aufwand

| Task | Zeit |
|------|------|
| Google Sheet Setup | 10 min |
| Leads importieren | 5 min |
| n8n Credentials | 15 min |
| Workflow A bauen | 20 min |
| Workflow B bauen | 15 min |
| Testen & Debuggen | 15 min |
| **GESAMT** | **~80 min** |

---

## 🔄 Täglicher Workflow für Florian

1. **Morgens:** Google Sheet öffnen
2. **Filter:** Status = "Pending Review"
3. **Review:** Draft lesen, ggf. editieren
4. **Approve:** Status auf "Approved" setzen
5. **Done:** Email geht automatisch raus

**Erwartete tägliche Zeit: 5-10 min für 3-5 Leads**

---

## 📊 Bonus: Tracking-Dashboard

Füge diese Formeln im Sheet hinzu:

```
=COUNTIF(I:I, "New")           → Neue Leads
=COUNTIF(I:I, "Pending Review") → Zu reviewen
=COUNTIF(I:I, "Sent")          → Gesendet
=COUNTIF(I:I, "Replied")       → Antworten
```

---

## ⚡ Schnellstart-Alternative

Falls 80 min zu viel:

**Minimal Viable Workflow (30 min):**
1. Google Sheet mit manuellen Drafts
2. NUR Workflow B (Approval → Send)
3. AI-Drafts manuell über ChatGPT/Claude erstellen

→ Automatisiert zumindest das Senden!

---

## 🚀 Nächste Schritte

1. [ ] Demo morgen abwarten
2. [ ] Bei Erfolg: Sheet aufsetzen
3. [ ] Ersten Workflow (B) bauen — schneller Erfolg
4. [ ] Dann Workflow A für AI-Drafts

---

*Bei Fragen: ENGINEER ist ready 🛠️*
