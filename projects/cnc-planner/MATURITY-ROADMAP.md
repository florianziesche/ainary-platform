# CNC Planner Pro — Maturity Roadmap

**Ziel:** Verkaufsfähiges Produkt auf Spanflug-Niveau
**Benchmark:** Spanflug MAKE (€149-499/Monat SaaS)

---

## 🎯 Was macht Spanflug "reif"?

### Aus der Analyse:
1. **CAD/PDF Upload** → Automatische Bauteilanalyse
2. **Intelligenter Algorithmus** → "An Millionen Teilen optimiert"
3. **Detaillierte Kostenaufschlüsselung** → Material, Programmierung, Rüsten, Fertigung, Nachbearbeitung
4. **Arbeitsvorbereitung** → Arbeitsplan mit allen Fertigungsschritten
5. **Angebotserstellung** → PDF-Export, Kundenmanagement
6. **Anpassbarkeit** → Eigene Maschinen, Parameter, Preise
7. **Archiv** → Teile, Kalkulationen, Angebote speichern
8. **ERP-Integration** → Schnittstelle zu bestehenden Systemen
9. **Cloud-basiert** → Browser, kein Install
10. **Datensicherheit** → ISO 27001, DSGVO

### Spanflug's Kernversprechen:
> "Innerhalb weniger Sekunden erhalten Sie einen Kalkulationsvorschlag inkl. einer **detaillierten Aufschlüsselung** der veranschlagten Kosten. Diesen können Sie anschließend **individuell anpassen**."

---

## 📊 Reifegrad-Modell

### Level 1: Demo (Wo wir sind)
- ✅ Grundkalkulation funktioniert
- ✅ 2 Demo-Teile
- ✅ Einstellungen (Stundensätze)
- ❌ Nicht produktionsreif

### Level 2: MVP (Minimum Viable Product)
- Alle v14-Features implementiert
- Stabil, keine Bugs
- PDF-Export funktioniert
- **→ Kann bei Demo gezeigt werden**

### Level 3: Beta (Testbar)
- Upload von eigenen Teilen (STEP/PDF)
- Speichern von Kalkulationen
- Mehrere Benutzer
- **→ Kann kostenlos getestet werden**

### Level 4: Production (Verkaufsfähig)
- Zuverlässig und schnell
- Onboarding-Flow
- Bezahlung integriert
- Support-Dokumentation
- **→ Kann verkauft werden (€49-149/Monat)**

### Level 5: Enterprise (Spanflug-Niveau)
- ERP-Integration
- Team-Management
- API für Automatisierung
- ISO 27001 zertifiziert
- **→ Premium-Pricing (€299-499/Monat)**

---

## 🚀 PHASEN-PLAN

### Phase 0: Fundament (JETZT — vor Demo)
**Ziel:** Demo-fähige Version

**Aufgaben:**
1. [ ] Alle v14-Features in v15 integriert
2. [ ] Kein Feature-Regression
3. [ ] Kalkulation 100% korrekt
4. [ ] PDF-Export funktioniert

**Definition of Done:**
- Florian kann Demo ohne Bugs zeigen
- Andreas kann mit echten Zahlen rechnen
- Nachvollziehbarkeit gegeben

**Zeit:** 4-6h fokussierte Arbeit

---

### Phase 1: MVP Polish (1 Woche)
**Ziel:** Testbar durch Nicht-Entwickler

**Aufgaben:**
1. [ ] Onboarding-Flow (erste Schritte)
2. [ ] Fehlerbehandlung (keine Crashes)
3. [ ] Mobile-Ansicht funktional
4. [ ] 5+ Demo-Teile mit realen Daten
5. [ ] Hilfe-Texte an kritischen Stellen
6. [ ] Loading-States überall

**Definition of Done:**
- Fremde Person kann ohne Anleitung kalkulieren
- Keine Error-Alerts
- Funktioniert auf Tablet

---

### Phase 2: Upload & Persistenz (2 Wochen)
**Ziel:** Eigene Teile hochladen und speichern

**Aufgaben:**
1. [ ] STEP-Datei Upload (3D)
2. [ ] PDF-Zeichnung Upload
3. [ ] Automatische Maß-Extraktion (Basic)
4. [ ] localStorage für Kalkulationen
5. [ ] Export/Import von Projekten
6. [ ] Kunden-Datenbank (Name, Kontakt)

**Definition of Done:**
- User lädt STEP hoch → Maße werden erkannt
- Kalkulation bleibt nach Browser-Refresh
- Kunde kann als Vorlage gespeichert werden

---

### Phase 3: Account & Bezahlung (2 Wochen)
**Ziel:** Zahlende Kunden möglich

**Aufgaben:**
1. [ ] User Registration/Login
2. [ ] Stripe/Paddle Integration
3. [ ] Subscription Plans (Free/Pro/Business)
4. [ ] Usage Limits (5 free/month)
5. [ ] Backend für Daten-Persistenz
6. [ ] DSGVO-konforme Datenhaltung

**Definition of Done:**
- Kunde kann Account erstellen
- Kunde kann €49/Monat bezahlen
- Kalkulationen sind cloud-gespeichert

---

### Phase 4: Intelligenz (4 Wochen)
**Ziel:** Automatische Analyse

**Aufgaben:**
1. [ ] 3D-Geometrie-Analyse (Feature-Erkennung)
2. [ ] Automatische Werkzeug-Auswahl
3. [ ] Zeit-Schätzung aus Geometrie
4. [ ] Feedback-Loop (Ist vs. Soll)
5. [ ] Machine Learning für Zeitvorhersage
6. [ ] "An X Teilen trainiert" Anzeige

**Definition of Done:**
- STEP hochladen → Komplette Kalkulation automatisch
- Genauigkeit ±15% ohne manuelle Eingabe
- Feedback verbessert zukünftige Schätzungen

---

### Phase 5: Enterprise Features (6 Wochen)
**Ziel:** Spanflug-Parität

**Aufgaben:**
1. [ ] Team/Multi-User
2. [ ] Rollen & Berechtigungen
3. [ ] ERP-Export (CSV, XML, API)
4. [ ] Maschinenpark-Verwaltung
5. [ ] Audit-Trail
6. [ ] White-Label Option

**Definition of Done:**
- Team von 5 kann zusammen arbeiten
- Daten fließen ins ERP
- Enterprise kann €299/Monat rechtfertigen

---

## 📋 SELBST-ANWEISUNG FÜR JEDE PHASE

### Vor Implementierung:
1. **Golden Standard recherchieren** — Wie machen es die Besten?
2. **Requirement-Dokument schreiben** — Was genau wird gebaut?
3. **Definition of Done definieren** — Wann ist es fertig?
4. **Florian-Approval holen** — Bevor 1 Zeile Code

### Während Implementierung:
1. **Feature für Feature** — Nicht alles gleichzeitig
2. **Testen nach jedem Feature** — Nicht erst am Ende
3. **Commit nach jedem Feature** — Rollback möglich
4. **Screenshots machen** — Dokumentation

### Nach Implementierung:
1. **Gegen DoD prüfen** — Alle Punkte erfüllt?
2. **Florian demonstrieren** — Live zeigen
3. **Feedback einarbeiten** — Sofort, nicht später
4. **Dokumentieren** — Was wurde gelernt?

---

## 🔴 ANTI-PATTERNS VERMEIDEN

1. **"Ich bau mal schnell"** → Immer erst planen
2. **"Das kommt später"** → Wenn es kritisch ist, kommt es jetzt
3. **"Feature ist fertig"** → Erst wenn getestet und dokumentiert
4. **"Ähnlich wie vorher"** → Feature-Inventar machen
5. **"Der Code ist sauber genug"** → Wenn Zweifel, refactoren

---

## 📅 TIMELINE

| Phase | Dauer | Meilenstein |
|-------|-------|-------------|
| 0: Fundament | 1 Tag | Demo-ready |
| 1: MVP | 1 Woche | Testbar |
| 2: Upload | 2 Wochen | Eigene Teile |
| 3: Account | 2 Wochen | Erste Zahlung |
| 4: Intelligenz | 4 Wochen | Automatisch |
| 5: Enterprise | 6 Wochen | Spanflug-Level |

**Total:** ~4 Monate bis Enterprise-Niveau

---

## 💰 PRICING-REFERENZ (Spanflug)

- **Free:** 5 Teile/Monat (Lead-Gen)
- **Starter:** €149/Monat (Einzelnutzer)
- **Professional:** €299/Monat (Team)
- **Enterprise:** €499+/Monat (Custom)

### Unser Einstiegs-Pricing:
- **Free:** 3 Teile/Monat
- **Pro:** €49/Monat (Einführungspreis)
- **Business:** €149/Monat

---

## ✅ NÄCHSTER SCHRITT

**Phase 0 abschließen:**
1. V14-FEATURE-INVENTORY.md als Checkliste nehmen
2. Jedes ❌ in ✅ verwandeln
3. Demo mit Andreas morgen erfolgreich durchführen
4. Erstes Pilotprojekt starten (€750/Monat)

---

---

## 📄 PDF-EXPORT STANDARD

**ALLE PDF-Exports nutzen den 36ZERO Vision LaTeX-Standard.**

### Warum LaTeX (nicht HTML/CSS):
- ✅ Zuverlässige Seitenumbrüche
- ✅ Konsistente Header/Footer auf jeder Seite
- ✅ Professionelles Typography
- ✅ Druckfertig ohne Nachbearbeitung
- ❌ HTML-to-PDF hat fundamentale Layout-Probleme

### Dateien:
```
Template:  ~/.openclaw/workspace/research/36zero-report.tex
Skill:     ~/.openclaw/workspace/skills/report-design/SKILL.md
Compiler:  XeLaTeX (TinyTeX unter ~/Library/TinyTeX/)
```

### PDF-Dokumente für CNC Planner:

| Dokument | Inhalt | Zielgruppe |
|----------|--------|-----------|
| **Angebot** | Kunde, Bauteil, Stückpreis, Mengenrabatt, AGB | Kunde |
| **Kalkulation** | Detaillierte Kostenaufschlüsselung mit Formeln | Intern (AV) |
| **Fertigungsanweisung** | Arbeitsplan, OP-Karten, Qualitätsprüfung | Werkstatt |
| **NC-Code** | Programm mit Header, Metadaten, Kommentaren | Maschinist |

### Implementierung:
1. **In-Browser:** Vorschau als HTML (wie jetzt)
2. **Export:** Button "PDF herunterladen"
3. **Backend:** POST an Server → LaTeX kompilieren → PDF zurück
4. **Fallback:** Für Demo/MVP: Serverless (z.B. LaTeX.Online API)

### Definition of Done für PDF-Export:
- [ ] Footer auf jeder Seite identisch
- [ ] Keine Content-Überlappung
- [ ] Firmenlogo + Kontaktdaten im Header
- [ ] Seitenzahlen
- [ ] Druckbar auf A4

---

*Erstellt: 2026-02-05 18:50*
*Ziel: CNC Planner Pro auf Spanflug-Niveau*
