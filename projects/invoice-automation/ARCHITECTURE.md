# Invoice Automation Workflow - 36ZERO Vision

> **Version:** 1.0  
> **Erstellt:** 2026-02-03  
> **Status:** Design Phase  
> **Autor:** ENGINEER (Applied AI Engineer)

---

## Executive Summary

Automatisierter Rechnungs- und Mahnworkflow für 36ZERO Vision mit sevdesk-Integration. 
**Kernprinzip:** User Confirmation vor jedem externen Send - keine automatischen Emails ohne Freigabe.

---

## 1. Architektur-Empfehlung

### ✅ Empfehlung: Option C - Hybrid (n8n + Dashboard)

| Aspekt | Option A (n8n only) | Option B (Full App) | **Option C (Hybrid)** |
|--------|---------------------|---------------------|----------------------|
| Aufwand | 2-3 Tage | 2-3 Wochen | **4-5 Tage** |
| Wartung | Niedrig | Hoch | Niedrig |
| Flexibilität | Mittel | Hoch | **Hoch** |
| UX | Basic | Excellent | **Gut** |
| Skalierbarkeit | Begrenzt | Unbegrenzt | **Ausreichend** |

**Warum Hybrid:**
- n8n übernimmt die schwere Arbeit (API Calls, Scheduling, Email)
- Dashboard gibt Übersicht und Bestätigungs-Interface
- Schnelle Iteration, keine Server-Wartung für Custom Backend
- sevdesk bleibt Single Source of Truth

### Komponenten-Übersicht

```
┌─────────────────────────────────────────────────────────────────────┐
│                        36ZERO Invoice Automation                     │
├─────────────────────────────────────────────────────────────────────┤
│                                                                       │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────────────┐   │
│  │   sevdesk    │◄──►│     n8n      │◄──►│  Dashboard (HTML)    │   │
│  │   (Source)   │    │  (Backend)   │    │  (User Interface)    │   │
│  └──────────────┘    └──────────────┘    └──────────────────────┘   │
│         │                   │                       │                │
│         ▼                   ▼                       ▼                │
│  • Rechnungsdaten    • Workflow Logic       • Kunden-Übersicht      │
│  • Zahlungsstatus    • Email Versand        • Confirmation UI       │
│  • PDF Generation    • Scheduling           • Status Tracking       │
│  • Kontakte          • Webhooks             • Offene Posten         │
│                                                                       │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 2. Workflow-Diagramm

### 2.1 Hauptworkflow (Invoice → Reminder Sequence)

```
                              ┌─────────────────┐
                              │  SEVDESK SYNC   │
                              │  (alle 4 Std)   │
                              └────────┬────────┘
                                       │
                                       ▼
                        ┌──────────────────────────┐
                        │  Neue/Offene Rechnungen  │
                        │  aus sevdesk abrufen     │
                        └────────────┬─────────────┘
                                     │
                    ┌────────────────┼────────────────┐
                    ▼                ▼                ▼
            ┌───────────┐    ┌───────────┐    ┌───────────┐
            │   NEU     │    │  OFFEN    │    │  BEZAHLT  │
            │ (Status)  │    │ (überfällig)│   │  (done)   │
            └─────┬─────┘    └─────┬─────┘    └───────────┘
                  │                │                 │
                  ▼                ▼                 │
        ┌─────────────────┐  Berechne Tage          │
        │ Initial Email   │  überfällig             │
        │ (mit Rechnung)  │       │                 │
        └────────┬────────┘       │                 │
                 │                ▼                 │
                 │    ┌───────────────────────┐     │
                 │    │ REMINDER QUEUE        │     │
                 │    │ ├─ 14 Tage → Mahnung 1│     │
                 │    │ ├─ 28 Tage → Mahnung 2│     │
                 │    │ └─ 42 Tage → Mahnung 3│     │
                 │    └───────────┬───────────┘     │
                 │                │                 │
                 ▼                ▼                 │
        ┌─────────────────────────────────┐        │
        │      USER CONFIRMATION          │        │
        │  ┌────────────────────────────┐ │        │
        │  │ Dashboard zeigt:           │ │        │
        │  │ • Kunde                    │ │        │
        │  │ • Betrag                   │ │        │
        │  │ • Mahnstufe               │ │        │
        │  │ • Email-Preview           │ │        │
        │  │                           │ │        │
        │  │ [✓ Senden] [✗ Überspringen]│ │        │
        │  └────────────────────────────┘ │        │
        └─────────────┬───────────────────┘        │
                      │                            │
            ┌─────────┴─────────┐                  │
            ▼                   ▼                  │
    ┌───────────────┐   ┌───────────────┐         │
    │ EMAIL SENDEN  │   │  SKIP/SPÄTER  │         │
    │ + PDF Attach  │   │   (loggen)    │         │
    └───────┬───────┘   └───────────────┘         │
            │                                      │
            ▼                                      │
    ┌───────────────┐                             │
    │ sevdesk Update│◄────────────────────────────┘
    │ (Notiz/Status)│
    └───────────────┘
```

### 2.2 Confirmation Flow Detail

```
┌─────────────────────────────────────────────────────────────────┐
│                    CONFIRMATION QUEUE                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│   n8n erkennt: "Rechnung #2024-042 ist 14 Tage überfällig"      │
│                              │                                    │
│                              ▼                                    │
│   ┌─────────────────────────────────────────────────────────┐   │
│   │  1. Erstelle Pending Action in Queue (JSON/DB)          │   │
│   │  2. Generiere Email-Draft mit Template                   │   │
│   │  3. Hole PDF von sevdesk                                 │   │
│   │  4. Setze Status: AWAITING_CONFIRMATION                  │   │
│   └─────────────────────────────────────────────────────────┘   │
│                              │                                    │
│                              ▼                                    │
│   ┌─────────────────────────────────────────────────────────┐   │
│   │  Dashboard zeigt Notification Badge                      │   │
│   │  User öffnet Pending Actions                            │   │
│   └─────────────────────────────────────────────────────────┘   │
│                              │                                    │
│              ┌───────────────┴───────────────┐                   │
│              ▼                               ▼                    │
│   ┌─────────────────┐             ┌─────────────────┐           │
│   │ ✓ BESTÄTIGEN    │             │ ✗ ABLEHNEN      │           │
│   │                 │             │                 │           │
│   │ • Edit möglich  │             │ • Grund angeben │           │
│   │ • Preview Email │             │ • Snooze Option │           │
│   │ • Jetzt senden  │             │ • Skip permanent│           │
│   └────────┬────────┘             └────────┬────────┘           │
│            │                                │                     │
│            ▼                                ▼                     │
│   ┌─────────────────┐             ┌─────────────────┐           │
│   │ n8n Webhook     │             │ Log + Next      │           │
│   │ → Email senden  │             │ Reminder        │           │
│   │ → sevdesk Notiz │             │ ggf. anpassen   │           │
│   └─────────────────┘             └─────────────────┘           │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
```

---

## 3. sevdesk API Endpoints

### 3.1 Benötigte Endpoints

| Endpoint | Methode | Zweck |
|----------|---------|-------|
| `/Invoice` | GET | Alle Rechnungen abrufen |
| `/Invoice/{id}` | GET | Einzelne Rechnung Details |
| `/Invoice/{id}/getPdf` | GET | PDF der Rechnung |
| `/Invoice/{id}/sendViaEmail` | POST | Email direkt über sevdesk (Alternative) |
| `/Contact` | GET | Kundendaten für Email |
| `/Contact/{id}` | GET | Einzelner Kunde |
| `/Invoice/{id}/changeStatus` | PUT | Status ändern |
| `/CommunicationWay` | GET | Email-Adressen eines Kontakts |

### 3.2 API Call Beispiele

```javascript
// Base Configuration
const SEVDESK_BASE = 'https://my.sevdesk.de/api/v1';
const headers = {
  'Authorization': `${SEVDESK_API_TOKEN}`,
  'Content-Type': 'application/json'
};

// 1. Offene Rechnungen abrufen (Status: 200 = Offen, 1000 = Bezahlt)
GET /Invoice?status=200&embed=contact

// Response enthält:
{
  "objects": [{
    "id": "12345",
    "invoiceNumber": "2024-042",
    "contact": { "id": "67890", "name": "Kunde GmbH" },
    "invoiceDate": "2024-01-15",
    "timeToPay": 14,
    "sumGross": "2380.00",
    "status": "200"
  }]
}

// 2. PDF abrufen
GET /Invoice/12345/getPdf
// Returns: Base64 encoded PDF

// 3. Kontakt-Email holen
GET /CommunicationWay?contact[id]=67890&type=EMAIL

// 4. Notiz zur Rechnung hinzufügen (nach Mahnung)
POST /Invoice/12345/changeStatus
{
  "value": 200,  // bleibt offen
  "comment": "1. Mahnung versendet am 2024-01-29"
}
```

### 3.3 Webhook Setup (Optional)

sevdesk bietet Webhooks für:
- Neue Rechnung erstellt
- Zahlung eingegangen
- Status geändert

```
POST https://your-n8n-instance/webhook/sevdesk-invoice-update
```

---

## 4. User Flow (Confirmation Steps)

### 4.1 Täglicher Workflow

```
┌────────────────────────────────────────────────────────────────┐
│                     TÄGLICHER USER FLOW                         │
├────────────────────────────────────────────────────────────────┤
│                                                                  │
│  08:00  ─►  n8n Sync läuft automatisch                         │
│             • Holt alle offenen Rechnungen                      │
│             • Prüft Fälligkeiten                                │
│             • Erstellt Pending Actions                          │
│                                                                  │
│  09:00  ─►  User öffnet Dashboard                              │
│             ┌────────────────────────────────────┐              │
│             │  🔔 3 Aktionen warten auf Freigabe │              │
│             └────────────────────────────────────┘              │
│                                                                  │
│         ─►  Klick auf "Pending Actions"                        │
│             ┌────────────────────────────────────────────────┐ │
│             │ ┌──────────────────────────────────────────┐   │ │
│             │ │ Mahnung 1: Kunde A GmbH                  │   │ │
│             │ │ Rechnung: #2024-038 | €1.250,00          │   │ │
│             │ │ Überfällig: 16 Tage                      │   │ │
│             │ │ [Preview] [✓ Senden] [Später] [Skip]     │   │ │
│             │ └──────────────────────────────────────────┘   │ │
│             │ ┌──────────────────────────────────────────┐   │ │
│             │ │ Mahnung 2: Kunde B AG                    │   │ │
│             │ │ Rechnung: #2024-031 | €3.800,00          │   │ │
│             │ │ Überfällig: 32 Tage                      │   │ │
│             │ │ [Preview] [✓ Senden] [Später] [Skip]     │   │ │
│             │ └──────────────────────────────────────────┘   │ │
│             │ ┌──────────────────────────────────────────┐   │ │
│             │ │ Initial: Neue Rechnung für Kunde C       │   │ │
│             │ │ Rechnung: #2024-052 | €890,00            │   │ │
│             │ │ Fällig in: 14 Tagen                      │   │ │
│             │ │ [Preview] [✓ Senden] [Später] [Skip]     │   │ │
│             │ └──────────────────────────────────────────┘   │ │
│             └────────────────────────────────────────────────┘ │
│                                                                  │
│         ─►  Klick auf "Preview" zeigt:                         │
│             • Email-Text (editierbar)                          │
│             • PDF-Vorschau                                     │
│             • Empfänger-Email                                  │
│                                                                  │
│         ─►  Klick auf "✓ Senden":                              │
│             • Webhook an n8n                                   │
│             • Email wird versendet                             │
│             • sevdesk Notiz wird erstellt                      │
│             • ✓ Bestätigung im Dashboard                       │
│                                                                  │
│  Fertig ─►  Dashboard aktualisiert sich                        │
│             • Pending Count: 0                                 │
│             • Letzte Aktionen sichtbar                         │
│                                                                  │
└────────────────────────────────────────────────────────────────┘
```

### 4.2 Confirmation UI Mockup

```
┌─────────────────────────────────────────────────────────────────────────┐
│  36ZERO Vision - Invoice Dashboard                          👤 User ▼  │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐    │
│  │  OFFEN      │  │  ÜBERFÄLLIG │  │  MAHNUNGEN  │  │  PENDING    │    │
│  │   12        │  │      5      │  │      3      │  │    🔔 3     │    │
│  │  €28.450    │  │   €12.300   │  │   €8.200    │  │  Aktionen   │    │
│  └─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘    │
│                                                                          │
│  ═══════════════════════════════════════════════════════════════════    │
│                                                                          │
│  📋 Kunden-Übersicht                                    [Filter ▼]      │
│  ┌────────────────────────────────────────────────────────────────┐    │
│  │ Kunde          │ Rechnung  │ Betrag    │ Tage │ Status        │    │
│  ├────────────────┼───────────┼───────────┼──────┼───────────────┤    │
│  │ Kunde A GmbH   │ #2024-038 │ €1.250,00 │  16  │ ⚠️ Mahnung 1  │    │
│  │ Kunde B AG     │ #2024-031 │ €3.800,00 │  32  │ 🔴 Mahnung 2  │    │
│  │ Kunde C Ltd    │ #2024-044 │ €2.100,00 │   8  │ 🟡 Offen      │    │
│  │ Kunde D GmbH   │ #2024-052 │ €890,00   │  -6  │ 🟢 Neu        │    │
│  │ Kunde E        │ #2024-029 │ €4.350,00 │  45  │ 🔴 Mahnung 3  │    │
│  └────────────────────────────────────────────────────────────────┘    │
│                                                                          │
│  ═══════════════════════════════════════════════════════════════════    │
│                                                                          │
│  🕐 Letzte Aktionen                                                     │
│  • 09:15 - Mahnung 1 an Kunde A gesendet ✓                             │
│  • 09:12 - Rechnung #2024-052 an Kunde C gesendet ✓                    │
│  • Gestern 14:30 - Zahlung Kunde F eingegangen (€1.800) ✓              │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 5. Reminder Konfiguration

### 5.1 Standard-Staffelung

| Stufe | Trigger | Ton | Template |
|-------|---------|-----|----------|
| **Initial** | Rechnung erstellt | Freundlich | `email_invoice.html` |
| **Mahnung 1** | +14 Tage nach Fälligkeit | Höflich-erinnernd | `email_reminder_1.html` |
| **Mahnung 2** | +28 Tage nach Fälligkeit | Bestimmt | `email_reminder_2.html` |
| **Mahnung 3** | +42 Tage nach Fälligkeit | Ultimatum | `email_reminder_3.html` |

### 5.2 Email Templates (Beispiel Mahnung 1)

```html
Betreff: Erinnerung: Rechnung {{invoice_number}} - 36ZERO Vision

Guten Tag {{contact_name}},

wir möchten Sie freundlich daran erinnern, dass die Zahlung 
für folgende Rechnung noch aussteht:

Rechnungsnummer: {{invoice_number}}
Rechnungsdatum:  {{invoice_date}}
Fällig seit:     {{due_date}}
Offener Betrag:  {{amount}} EUR

Bitte überweisen Sie den Betrag auf unser Konto:
[Bankverbindung]

Sollte sich Ihre Zahlung mit dieser Erinnerung gekreuzt haben,
betrachten Sie dieses Schreiben bitte als gegenstandslos.

Mit freundlichen Grüßen,
36ZERO Vision

---
Im Anhang: Rechnungskopie (PDF)
```

---

## 6. Technische Implementierung

### 6.1 n8n Workflows

```
Workflow 1: "Invoice Sync" (Scheduled - alle 4h)
├── Trigger: Schedule (08:00, 12:00, 16:00, 20:00)
├── HTTP Request: sevdesk GET /Invoice?status=200
├── Function: Calculate overdue days
├── IF: Neue Pending Actions nötig?
│   ├── YES → Create Pending Action
│   └── NO → End
└── Store in: pending_actions.json / SQLite

Workflow 2: "Send Confirmed Email" (Webhook)
├── Trigger: Webhook /confirm-send
├── Validate: Action ID exists
├── HTTP Request: sevdesk GET PDF
├── Send Email: SMTP mit Attachment
├── HTTP Request: sevdesk POST Notiz
├── Update: pending_actions → completed
└── Respond: Success/Error

Workflow 3: "Payment Check" (Scheduled - 2x täglich)
├── Trigger: Schedule (10:00, 18:00)
├── HTTP Request: sevdesk GET /Invoice (alle)
├── Compare: Mit lokalem Status
├── IF: Zahlung eingegangen?
│   ├── YES → Update Status, Remove Reminders
│   └── NO → Continue
└── Dashboard Refresh
```

### 6.2 Dashboard Tech Stack

```
Frontend (Static HTML + JS):
├── index.html          - Dashboard Layout
├── css/
│   └── style.css       - Tailwind oder Bootstrap
├── js/
│   ├── app.js          - Main Logic
│   ├── api.js          - n8n Webhook Calls
│   └── chart.js        - Optional: Charts
└── Hosting: Einfacher Webserver oder n8n Static

Data Flow:
├── n8n speichert Status in JSON/SQLite
├── Dashboard fetcht via n8n Webhook
└── Aktionen triggern n8n Workflows
```

### 6.3 Datenmodell

```javascript
// Pending Action
{
  "id": "uuid",
  "type": "REMINDER_1" | "REMINDER_2" | "REMINDER_3" | "INITIAL",
  "invoice_id": "sevdesk_id",
  "invoice_number": "#2024-042",
  "contact_id": "sevdesk_contact_id",
  "contact_name": "Kunde A GmbH",
  "contact_email": "buchhaltung@kunde-a.de",
  "amount": 1250.00,
  "days_overdue": 16,
  "status": "PENDING" | "SENT" | "SKIPPED" | "SNOOZED",
  "created_at": "2024-01-29T08:00:00Z",
  "sent_at": null,
  "email_draft": "...",
  "pdf_url": "sevdesk://invoice/12345/pdf"
}

// Invoice Tracking
{
  "invoice_id": "sevdesk_id",
  "invoice_number": "#2024-042",
  "contact_name": "Kunde A GmbH",
  "amount": 1250.00,
  "due_date": "2024-01-15",
  "status": "OPEN" | "PAID" | "REMINDER_1" | "REMINDER_2" | "REMINDER_3",
  "reminders_sent": [
    { "type": "INITIAL", "date": "2024-01-01" },
    { "type": "REMINDER_1", "date": "2024-01-29" }
  ],
  "last_synced": "2024-01-29T08:00:00Z"
}
```

---

## 7. Aufwandsschätzung

### 7.1 Detaillierte Schätzung

| Komponente | Aufwand | Beschreibung |
|------------|---------|--------------|
| **n8n Setup** | 0.5 Tage | Installation, sevdesk Credentials |
| **Workflow 1: Sync** | 1 Tag | API Integration, Logik |
| **Workflow 2: Send** | 0.5 Tage | Email + PDF + Webhook |
| **Workflow 3: Payment** | 0.5 Tage | Status-Sync |
| **Dashboard HTML** | 1 Tag | UI, Tables, Cards |
| **Dashboard JS** | 1 Tag | API Calls, Interactions |
| **Email Templates** | 0.5 Tage | 4 Templates (DE) |
| **Testing** | 0.5 Tage | End-to-End Flow |
| **Dokumentation** | 0.5 Tage | Setup Guide |
| **Buffer** | 0.5 Tage | Unvorhergesehenes |

### 7.2 Zusammenfassung

| Phase | Aufwand |
|-------|---------|
| **MVP (funktional)** | 3-4 Tage |
| **Polish (schön)** | +1-2 Tage |
| **Gesamt** | **4-6 Tage** |

### 7.3 Voraussetzungen

- [ ] sevdesk API Token (vorhanden?)
- [ ] n8n Instanz (self-hosted oder Cloud?)
- [ ] SMTP Credentials für Email-Versand
- [ ] Domain für Dashboard Hosting (optional)

---

## 8. Nächste Schritte

### Phase 1: Setup (Tag 1)
1. sevdesk API Token beschaffen/testen
2. n8n Instanz aufsetzen
3. Basis-Workflow für Sync erstellen
4. API Connection validieren

### Phase 2: Core Workflows (Tag 2-3)
1. Invoice Sync Workflow
2. Pending Action Logik
3. Email Send Workflow
4. Payment Check Workflow

### Phase 3: Dashboard (Tag 4)
1. HTML/CSS Grundstruktur
2. API Integration
3. Confirmation UI
4. Testing

### Phase 4: Polish (Tag 5-6)
1. Email Templates finalisieren
2. Error Handling
3. Dokumentation
4. User Training

---

## 9. Risiken & Mitigation

| Risiko | Wahrscheinlichkeit | Impact | Mitigation |
|--------|-------------------|--------|------------|
| sevdesk API Limits | Mittel | Hoch | Caching, Rate Limiting |
| Email Delivery Issues | Niedrig | Mittel | Logging, Retry Logic |
| User vergisst Confirmation | Mittel | Mittel | Tägliche Notification |
| Daten-Desync | Niedrig | Hoch | Regelmäßiger Full Sync |

---

## 10. Erweiterungsmöglichkeiten (Future)

- [ ] WhatsApp/SMS Reminders (mit Confirmation)
- [ ] Multi-User Support mit Rollen
- [ ] Automatische Mahngebühren-Berechnung
- [ ] Integration mit Inkasso-Service (3. Mahnung+)
- [ ] Analytics: Zahlungsverhalten pro Kunde
- [ ] Mobile App / PWA

---

*Dokument erstellt von ENGINEER für 36ZERO Vision*
*Bei Fragen: Ticket im Projekt-Channel erstellen*
