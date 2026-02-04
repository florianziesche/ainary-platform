# sevdesk API Research - Invoice Automation

> **Erstellt:** 2026-02-03  
> **Researcher:** RESEARCHER (Head of R&D)  
> **Projekt:** Mahnwesen Automation für Mia

---

## 📋 Executive Summary

sevdesk bietet eine umfassende REST API (ab Tarif "Buchhaltung Pro"), die alle relevanten Funktionen für Invoice Automation abdeckt. **Wichtig:** Es gibt KEINE nativen Webhooks für Zahlungseingänge - Polling ist erforderlich.

**Empfohlene Lösung:** n8n mit Community Node `n8n-nodes-sevdesk-v2` oder Make.com (beste Integration).

---

## 1. 🔐 Authentication

### API Key Setup

```
Ort: Einstellungen → Benutzer → [Username] → API Token
Format: 32-stelliger hexadezimaler String
```

**Best Practice:** Eigenen API-User erstellen (nicht persönlichen Account verwenden)

### Request Header

```http
Authorization: YOUR_API_TOKEN
Content-Type: application/json
Accept: application/json
```

**Wichtig:** Kein OAuth verfügbar - nur API Key Authentication.

### Beispiel (curl)

```bash
curl -X GET "https://my.sevdesk.de/api/v1/Invoice" \
  -H "Authorization: YOUR_API_TOKEN" \
  -H "Accept: application/json"
```

---

## 2. 📡 Relevante API Endpoints

### Base URL
```
https://my.sevdesk.de/api/v1
```

### Invoices (Rechnungen)

| Endpoint | Method | Beschreibung |
|----------|--------|--------------|
| `/Invoice` | GET | Liste aller Rechnungen |
| `/Invoice/{id}` | GET | Einzelne Rechnung abrufen |
| `/Invoice/{id}/getPdf` | GET | PDF einer Rechnung |
| `/Invoice/{id}/render` | GET | PDF rendern (forciert) |
| `/Invoice/{id}/sendViaEmail` | POST | Rechnung per Email senden |
| `/Invoice/{id}/bookAmount` | PUT | Rechnung als bezahlt markieren |
| `/Invoice/Factory/saveInvoice` | POST | Neue Rechnung erstellen |

#### Filter für unbezahlte Rechnungen

```bash
# Alle fälligen Rechnungen (status = 200 = Open/Delivered, delinquent = überfällig)
GET /Invoice?status=200&delinquent=true

# Status-Codes:
# 100 = Draft
# 200 = Open/Delivered
# 1000 = Paid
```

#### Beispiel: Unbezahlte Rechnungen abrufen

```bash
curl -X GET "https://my.sevdesk.de/api/v1/Invoice?status=200" \
  -H "Authorization: YOUR_API_TOKEN"
```

### Contacts (Kunden)

| Endpoint | Method | Beschreibung |
|----------|--------|--------------|
| `/Contact` | GET | Liste aller Kontakte |
| `/Contact/{id}` | GET | Einzelner Kontakt |
| `/Contact` | POST | Kontakt erstellen |
| `/Contact/{id}` | PUT | Kontakt aktualisieren |

#### Filter

```bash
# Nur Kunden (category.id = 3)
GET /Contact?depth=1&category[id]=3&category[objectName]=Category

# Nach Kundennummer suchen
GET /Contact?customerNumber=KD-1000
```

### Payment Status

| Endpoint | Method | Beschreibung |
|----------|--------|--------------|
| `/Invoice/{id}/bookAmount` | PUT | Als bezahlt markieren |
| `/Invoice/{id}` | GET | Status prüfen (status-Feld) |

#### Rechnung als bezahlt buchen

```bash
curl -X PUT "https://my.sevdesk.de/api/v1/Invoice/{invoiceId}/bookAmount" \
  -H "Authorization: YOUR_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "amount": 119.00,
    "date": "2026-02-03",
    "type": "N",
    "checkAccount": {
      "id": YOUR_CHECK_ACCOUNT_ID,
      "objectName": "CheckAccount"
    },
    "checkAccountTransaction": null
  }'
```

### Mahnungen / Reminders (invoiceType: MA)

| Endpoint | Method | Beschreibung |
|----------|--------|--------------|
| `/Invoice/Factory/saveInvoice` | POST | Mahnung erstellen (invoiceType="MA") |

**Wichtig für sevdesk Update 2.0:** 
- `reminderCharge` darf NICHT > 0 sein bei Mahnungen!
- Mahnungen basieren immer auf existierenden Rechnungen

#### Mahnung erstellen (Beispiel)

```bash
curl -X POST "https://my.sevdesk.de/api/v1/Invoice/Factory/saveInvoice" \
  -H "Authorization: YOUR_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "invoice": {
      "objectName": "Invoice",
      "invoiceType": "MA",
      "contact": {"id": CONTACT_ID, "objectName": "Contact"},
      "invoiceDate": "2026-02-03",
      "status": 100,
      "dunningLevel": 1,
      "reminderDeadline": "2026-02-17",
      "taxRule": {"id": "1", "objectName": "TaxRule"},
      "currency": "EUR",
      "contactPerson": {"id": USER_ID, "objectName": "SevUser"},
      "header": "Zahlungserinnerung",
      "address": "Kunde GmbH\nMusterstraße 1\n12345 Berlin"
    }
  }'
```

### Check Accounts (Bankkonten)

| Endpoint | Method | Beschreibung |
|----------|--------|--------------|
| `/CheckAccount` | GET | Bankkonten abrufen |
| `/CheckAccountTransaction` | GET | Transaktionen |

### Nächste Rechnungs-/Mahnnummer

```bash
# Nächste Rechnungsnummer
GET /SevSequence/Factory/getByType?objectType=Invoice&type=RE

# Nächste Mahnnummer
GET /SevSequence/Factory/getByType?objectType=Invoice&type=MA
```

---

## 3. 📊 Pagination & Rate Limits

### Pagination

```bash
GET /Invoice?limit=100&offset=0&countAll=true
```

| Parameter | Beschreibung | Default |
|-----------|--------------|---------|
| `limit` | Max. Einträge (1-1000) | 100 |
| `offset` | Start-Index | 0 |
| `countAll` | Gesamtanzahl in Response | false |

### Rate Limits

**Keine offiziellen Rate Limits dokumentiert!**

Best Practices:
- Requests moderat halten (max. 1-2/Sekunde)
- Bei 429-Errors: Exponential Backoff
- Für Bulk-Operations: Batching nutzen

---

## 4. 🔔 Webhooks

### ⚠️ KEINE nativen Webhooks verfügbar!

sevdesk bietet **keine Webhooks** für Events wie:
- Zahlungseingänge
- Rechnungsstatus-Änderungen
- Neue Kontakte

### Workaround: Polling

```javascript
// Pseudo-Code für n8n/Make
// Alle 15-30 Minuten prüfen:

1. GET /Invoice?status=200  // Alle offenen Rechnungen
2. GET /CheckAccountTransaction?startDate=LAST_CHECK  // Neue Transaktionen
3. Vergleichen & Matchen
4. Bei Match: Invoice als bezahlt markieren
```

---

## 5. 🏠 Native Mahnfunktionen in sevdesk

### Was sevdesk nativ kann:

✅ **Zahlungserinnerungen erstellen** (aus fälligen Rechnungen)
✅ **Mahnungen erstellen** (nach Zahlungserinnerung)
✅ **Mahnfristen konfigurieren** (Einstellungen → System → Aufträge & Rechnungen)
✅ **Automatischer Zahlungsabgleich** (bei verknüpften Bankkonten)
✅ **Filter für fällige Rechnungen** (Rechnungen → Filter: Fällig)

### Was sevdesk NICHT kann:

❌ **Automatischer Mahnversand** (manueller Klick erforderlich)
❌ **Webhooks bei Zahlungseingang**
❌ **Eskalations-Workflows** (mehrstufige automatische Mahnung)

### Workflow in sevdesk UI:

1. Rechnung erstellen & senden
2. Nach Fälligkeit: "Mahnung / Zahlungserinnerung" klicken
3. Zahlungserinnerung wird generiert
4. Bei Nicht-Zahlung: "Nächste Mahnung erstellen"
5. Bei Zahlung: "Als bezahlt markieren"

---

## 6. 🔧 Integrations-Plattformen

### n8n (Empfohlen für Self-Hosted)

**Community Node verfügbar:**

```bash
# Option 1: n8n-nodes-sevdesk (von nico-kow)
npm install n8n-nodes-sevdesk

# Option 2: n8n-nodes-sevdesk-v2 (neuer, API v2)
npm install n8n-nodes-sevdesk-v2
```

**Unterstützte Operationen (n8n-nodes-sevdesk):**

| Resource | Operations |
|----------|------------|
| Invoices | Book, Cancel, Create/Update, Get Many, Get PDF, Is Partially Paid, Mark as Sent, Render, Send via Email |
| Contacts | CRUD, Address, Communication Ways |
| Parts | CRUD, Get Stock |
| Check Accounts | CRUD, Get Balance |
| Transactions | CRUD |
| Vouchers | CRUD |

**Installation n8n:**
1. Community Nodes → Install
2. Package Name: `n8n-nodes-sevdesk` oder `n8n-nodes-sevdesk-v2`
3. Credentials: API Key eingeben

**Alternativ: HTTP Request Node**
```
Für nicht unterstützte Endpoints → HTTP Request Node verwenden
```

### Make.com (Beste Integration!)

**Native sevdesk App mit Modulen für:**

- ✅ Invoices: Create, Book, Get, Search, Cancel, Delete, Send Email, Render PDF, Mark as Sent, Check Partial Payment
- ✅ Vouchers: Watch, Create, Update, Book, Get, Search, Upload File
- ✅ Contacts: Watch, Create, Update, Get, Search, Create Address
- ✅ Orders: Watch, Create, Update, Get, Search, Delete, Create Position
- ✅ Parts: Create, Update, Get, Search, Get Stock

**Setup Make.com:**
1. sevdesk App hinzufügen
2. API Token aus sevdesk kopieren
3. Verbindung herstellen

### Zapier

⚠️ **KEINE offizielle Integration!**

sevdesk hat keinen Zapier-Partner-Status. Workaround nur über:
- Webhooks by Zapier (eingehend)
- HTTP Requests (ausgehend)

**Nicht empfohlen** für sevdesk-Projekte.

---

## 7. 💡 Beispiel-Workflows

### Workflow 1: Tägliche Mahnprüfung (n8n)

```
[Schedule Trigger: 9:00 täglich]
    ↓
[sevdesk: Get Invoices (status=200, delinquent=true)]
    ↓
[Filter: invoiceDate > 14 Tage]
    ↓
[Loop: Für jede Rechnung]
    ↓
[IF: Keine Zahlungserinnerung existiert]
    ↓
[HTTP Request: Zahlungserinnerung erstellen]
    ↓
[sevdesk: Send Invoice via Email]
    ↓
[Slack/Email: Benachrichtigung an Buchhaltung]
```

### Workflow 2: Zahlungseingangs-Monitoring (Make.com)

```
[Schedule: Alle 30 Minuten]
    ↓
[sevdesk: Search Check Account Transactions (letzte 30 Min)]
    ↓
[sevdesk: Search Invoices (status=200)]
    ↓
[Iterator + Filter: Matching Betrag + Verwendungszweck]
    ↓
[sevdesk: Book Invoice Amount]
    ↓
[Slack: Benachrichtigung "Zahlung eingegangen"]
```

---

## 8. 📝 Beispiel-Requests (curl)

### Alle offenen Rechnungen

```bash
curl -X GET "https://my.sevdesk.de/api/v1/Invoice?status=200&limit=100" \
  -H "Authorization: YOUR_API_TOKEN"
```

### Überfällige Rechnungen (älter als 14 Tage)

```bash
curl -X GET "https://my.sevdesk.de/api/v1/Invoice?status=200&delinquent=true" \
  -H "Authorization: YOUR_API_TOKEN"
```

### Rechnung als bezahlt markieren

```bash
curl -X PUT "https://my.sevdesk.de/api/v1/Invoice/12345/bookAmount" \
  -H "Authorization: YOUR_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "amount": 1190.00,
    "date": "2026-02-03T10:00:00",
    "type": "N",
    "checkAccount": {
      "id": 1,
      "objectName": "CheckAccount"
    }
  }'
```

### Kontaktdaten abrufen

```bash
curl -X GET "https://my.sevdesk.de/api/v1/Contact/12345?embed=addresses,communicationWays" \
  -H "Authorization: YOUR_API_TOKEN"
```

### Rechnung-PDF herunterladen

```bash
curl -X GET "https://my.sevdesk.de/api/v1/Invoice/12345/getPdf" \
  -H "Authorization: YOUR_API_TOKEN" \
  -o rechnung_12345.pdf
```

### System-Version prüfen (1.0 vs 2.0)

```bash
curl -X GET "https://my.sevdesk.de/api/v1/Tools/bookkeepingSystemVersion" \
  -H "Authorization: YOUR_API_TOKEN"
```

---

## 9. ⚠️ Limitierungen & Hinweise

### API-Verfügbarkeit
- Nur ab Tarif **"Buchhaltung Pro"**
- API Token hat **unbegrenzte Gültigkeit**
- Bei Löschung des Users → Token ungültig!

### sevdesk-Update 2.0 (ab 2024)
- Neue `taxRule` statt altem `taxType`
- Strengere Validierung
- Mahnungen (`invoiceType: "MA"`) mit `reminderCharge > 0` nicht mehr möglich
- Status-Änderung nur noch über spezifische Endpoints

### Fehlende Features
- ❌ Keine Webhooks
- ❌ Keine OAuth-Authentifizierung
- ❌ Kein Sandbox-Environment
- ❌ Rate Limits nicht dokumentiert

### Datenformat
- Timestamps: Unix-Timestamp oder ISO-8601
- Währung: ISO-4217 Codes (EUR, USD, etc.)
- Embedded Objects: Mit `?embed=contact,positions` erweitern

---

## 10. 🎯 Empfehlungen für Invoice Automation

### Technologie-Stack

| Komponente | Empfehlung |
|------------|------------|
| Automation | **Make.com** (beste sevdesk-Integration) oder **n8n** (self-hosted) |
| Trigger | Schedule (Polling alle 15-30 Min) |
| Monitoring | Slack/Email Notifications |

### MVP-Workflow

1. **Täglich 9:00**: Prüfe überfällige Rechnungen
2. **Nach 7 Tagen**: Automatische Zahlungserinnerung per Email
3. **Nach 14 Tagen**: 1. Mahnung + Benachrichtigung an Mia
4. **Nach 21 Tagen**: 2. Mahnung + Eskalation
5. **Parallel**: Zahlungseingangs-Check alle 30 Min

### Nächste Schritte

1. [ ] sevdesk Tarif prüfen (Buchhaltung Pro?)
2. [ ] API Token generieren
3. [ ] Make.com oder n8n Account einrichten
4. [ ] Bankkonten-IDs abrufen (`GET /CheckAccount`)
5. [ ] Test-Workflow erstellen
6. [ ] Email-Templates für Mahnungen definieren

---

## 📚 Quellen & Links

- [sevdesk API Dokumentation](https://api.sevdesk.de/)
- [sevdesk Tech Blog - API News](https://tech.sevdesk.com/api_news/)
- [n8n Community Node (GitHub)](https://github.com/nico-kow/n8n-nodes-sevdesk)
- [Make.com sevdesk App](https://apps.make.com/sevdesk)
- [Unofficial OpenAPI Spec](https://github.com/j-mastr/sevdesk-api)
- [sevdesk Hilfe - Mahnungen](https://hilfe.sevdesk.de/de/articles/9167192-mahnungen)
- [sevdesk Hilfe - API](https://hilfe.sevdesk.de/de/articles/9374668-sevdesk-api)

---

*Dokument erstellt von RESEARCHER | Projekt: Invoice Automation für Mia*
