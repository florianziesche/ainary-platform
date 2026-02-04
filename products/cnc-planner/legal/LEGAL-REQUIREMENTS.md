# Legal Requirements – CNC Planner Pro

**Erstellt:** 03. Februar 2026  
**Autor:** RESEARCHER (R&D)  
**Kontext:** B2B SaaS für Maschinenbau, Anbieter: Florian Ziesche (Einzelunternehmer), Standort: Schlottwitz, Deutschland

---

## Executive Summary

| Anforderung | Status | Priorität | Handlungsbedarf |
|-------------|--------|-----------|-----------------|
| Impressum | 🔴 Fehlt | **KRITISCH** | Sofort erstellen |
| Datenschutzerklärung | ✅ Vorhanden | - | Kleine Ergänzungen |
| AGB | ✅ Vorhanden | - | Gut, keine Änderung |
| Cookie-Banner | ✅ Nicht nötig | - | Kein Tracking = kein Banner |
| Widerrufsbelehrung | ✅ Nicht nötig | - | B2B = keine Pflicht |

---

## 1. Impressum (§5 DDG, ehemals §5 TMG)

### Gesetzliche Grundlage

Seit 14.05.2024 gilt das **Digitale-Dienste-Gesetz (DDG)** statt TMG. Die Pflichten bleiben gleich, nur der Begriff "Telemedien" wurde durch "digitale Dienste" ersetzt.

### Pflichtangaben für Einzelunternehmer

| Pflichtangabe | Erforderlich | Details |
|---------------|--------------|---------|
| Vollständiger Name | ✅ Ja | Vor- und Zuname (mind. 1 Vorname) |
| Anschrift | ✅ Ja | Vollständige Straßenanschrift, kein Postfach |
| E-Mail | ✅ Ja | Muss funktionsfähig sein |
| Telefonnummer | ✅ Ja | Mit Vorwahl, erreichbar |
| USt-IdNr. | ⚠️ Falls vorhanden | Wenn zugeteilt |
| Wirtschafts-ID | ⚠️ Falls vorhanden | Seit Nov 2024 |
| Steuernummer | ❌ NICHT | Gehört NICHT ins Impressum! |
| Registereintrag | ⚠️ Falls vorhanden | HR, Gewerberegister etc. |
| Aufsichtsbehörde | ❌ Nein | Nur bei zulassungspflichtigen Berufen |
| OS-Plattform-Link | ❌ Nein | Wird am 20.07.2025 eingestellt |

### Anforderungen an Darstellung

- **Leicht erkennbar:** Als "Impressum" oder "Kontakt" bezeichnet
- **Max. 2 Klicks** von Startseite erreichbar (empfohlen: 1 Klick)
- **Ständig verfügbar:** Link im Footer auf jeder Seite
- **Nicht in AGB verstecken:** Separate Seite erforderlich

---

## 2. Impressum-Template (Copy-Paste Ready)

```html
<h1>Impressum</h1>

<h2>Angaben gemäß § 5 DDG</h2>

<p>
<strong>Florian Ziesche</strong><br>
Müglitztalstraße 45<br>
01768 Glashütte OT Schlottwitz<br>
Deutschland
</p>

<h2>Kontakt</h2>

<p>
Telefon: +49 (0) XXXX XXXXXXX<br>
E-Mail: kontakt@cncplanner.de
</p>

<h2>Umsatzsteuer-Identifikationsnummer</h2>

<p>
Umsatzsteuer-Identifikationsnummer gemäß § 27a Umsatzsteuergesetz:<br>
DE XXXXXXXXX
</p>

<p><em>oder falls keine vorhanden:</em></p>

<p>
Eine Umsatzsteuer-Identifikationsnummer wurde noch nicht zugeteilt.
</p>

<h2>Redaktionell verantwortlich</h2>

<p>
Florian Ziesche<br>
(Anschrift wie oben)
</p>

<h2>EU-Streitschlichtung</h2>

<p>
Die Europäische Kommission stellt die OS-Plattform zur Online-Streitbeilegung zum 20.07.2025 ein. 
Eine Teilnahme an Streitbeilegungsverfahren vor einer Verbraucherschlichtungsstelle erfolgt nicht.
</p>
```

### Markdown-Version für statische Sites

```markdown
# Impressum

## Angaben gemäß § 5 DDG

**Florian Ziesche**  
Müglitztalstraße 45  
01768 Glashütte OT Schlottwitz  
Deutschland

## Kontakt

Telefon: +49 (0) XXXX XXXXXXX  
E-Mail: kontakt@cncplanner.de

## Umsatzsteuer-Identifikationsnummer

Umsatzsteuer-Identifikationsnummer gemäß § 27a Umsatzsteuergesetz:  
DE XXXXXXXXX

*(Falls keine vorhanden: "Eine Umsatzsteuer-Identifikationsnummer wurde noch nicht zugeteilt.")*

## Redaktionell verantwortlich

Florian Ziesche  
(Anschrift wie oben)

## EU-Streitschlichtung

Die Europäische Kommission stellt die OS-Plattform zur Online-Streitbeilegung zum 20.07.2025 ein.
Eine Teilnahme an Streitbeilegungsverfahren vor einer Verbraucherschlichtungsstelle erfolgt nicht.
```

---

## 3. Cookie-Banner: Empfehlung

### Rechtliche Grundlage

Das **TTDSG (Telekommunikation-Telemedien-Datenschutz-Gesetz)** regelt Cookies in Deutschland:

- **§25 TTDSG:** Einwilligung nur bei nicht-technisch-notwendigen Cookies erforderlich
- **Technisch notwendige Cookies:** Keine Einwilligung nötig

### Analyse CNC Planner Pro

Laut bestehender Datenschutzerklärung werden folgende Cookies verwendet:

| Cookie | Typ | Einwilligung nötig? |
|--------|-----|---------------------|
| session_id | Technisch notwendig | ❌ Nein |
| auth_token | Technisch notwendig | ❌ Nein |
| preferences | Technisch notwendig | ❌ Nein |

**Kein Google Analytics, kein Facebook Pixel, kein Marketing-Tracking.**

### 🎯 Empfehlung: KEIN Cookie-Banner nötig

Da CNC Planner Pro ausschließlich technisch notwendige Cookies verwendet, ist **kein Cookie-Banner erforderlich**.

**Vorteile:**
- Bessere User Experience (kein nerviges Popup)
- Höhere Conversion (Banner = 5-15% Absprungrate)
- Kein Wartungsaufwand für Consent-Management
- Rechtlich sauber

### Falls später Analytics gewünscht

Wenn Analytics hinzugefügt werden soll, empfehle ich:

| Tool | Empfehlung | Cookie-Banner? |
|------|------------|----------------|
| **Plausible** | ⭐ Empfohlen | Nein (cookieless) |
| **Fathom** | ⭐ Empfohlen | Nein (cookieless) |
| **Matomo** (self-hosted) | Gut | Konfigurierbar |
| Google Analytics | Nicht empfohlen | Ja, komplexes Consent |

**Privacy-freundliche Analytics (Plausible/Fathom) = Kein Cookie-Banner nötig!**

---

## 4. DSGVO-Datenschutzerklärung: Review

### Status: ✅ Vorhanden und gut

Die existierende Datenschutzerklärung in `docs/iso27001/PRIVACY-POLICY.md` ist umfassend und enthält:

| Anforderung | Status |
|-------------|--------|
| Verantwortlicher mit Kontakt | ✅ |
| Kategorien betroffener Daten | ✅ |
| Verarbeitungszwecke | ✅ |
| Rechtsgrundlagen (Art. 6 DSGVO) | ✅ |
| Speicherdauer | ✅ |
| Empfänger/Auftragsverarbeiter | ✅ |
| Internationale Transfers | ✅ (nur EU) |
| Betroffenenrechte | ✅ |
| Aufsichtsbehörde | ✅ |
| Datensicherheit | ✅ |
| Cookies | ✅ |

### Kleine Verbesserungen (niedrige Priorität)

1. **Auftragsverarbeiter konkretisieren:** Aktuell Platzhalter – echte Dienstleister benennen sobald bekannt
2. **Hosting-Provider:** Welcher Provider wird verwendet? (Hetzner, Netcup, etc.)
3. **E-Mail-Provider:** Welcher Dienst für Transaktionsmails?
4. **AVV erwähnen:** Link zum AVV-Template für Kunden die einen benötigen

---

## 5. AGB für SaaS: Bewertung

### Rechtliche Einordnung

- **AGB sind nicht gesetzlich vorgeschrieben**, aber dringend empfohlen
- Bei B2B gelten §§305 ff. BGB, aber weniger streng als bei B2C
- Ohne AGB: Gesetzliche Regelungen (BGB Mietrecht/Werkvertrag) gelten → oft ungünstig für Anbieter

### Status: ✅ Vorhanden und gut

Die existierenden AGB in `docs/legal/TERMS-OF-SERVICE.md` sind solide:

| Aspekt | Bewertung |
|--------|-----------|
| B2B-Ausschluss von Verbrauchern | ✅ §1 Abs. 2 |
| SaaS-Leistungsbeschreibung | ✅ §2 und §4 |
| Haftungsbeschränkung | ✅ §9 (wichtig bei NC-Code!) |
| Verfügbarkeit (SLA) | ✅ §7 (99,5%) |
| Kündigung | ✅ §11 |
| Datenschutz-Verweis | ✅ §10 |
| Deutsches Recht | ✅ §13 |
| Gerichtsstand | ✅ §13 (Dresden für Kaufleute) |

### Besonders positiv

Der **Haftungsausschluss für NC-Code** in §9 Abs. 3 ist essentiell:
> "Der Anbieter übernimmt keine Haftung für [...] Schäden an Maschinen, Werkzeugen oder Werkstücken"

Das ist bei CNC-Software kritisch und gut gelöst.

---

## 6. Widerrufsbelehrung: Nicht erforderlich

### Gesetzliche Grundlage

- **§312g BGB:** Widerrufsrecht gilt nur für Verbraucherverträge (B2C)
- **§13 BGB (Verbraucher):** Natürliche Person, die außerhalb gewerblicher Tätigkeit handelt
- **§14 BGB (Unternehmer):** Gewerbliche/selbstständige Tätigkeit

### Anwendung auf CNC Planner Pro

Die AGB schließen Verbraucher explizit aus:

> *"Die Software richtet sich ausschließlich an Unternehmer im Sinne des § 14 BGB. Verbraucher sind von der Nutzung ausgeschlossen."* (§1 Abs. 2 AGB)

### 🎯 Empfehlung: Keine Widerrufsbelehrung

Da CNC Planner Pro ein reines **B2B-Produkt** ist:
- ❌ Keine Widerrufsbelehrung erforderlich
- ❌ Kein 14-tägiges Widerrufsrecht
- ✅ Vertragliche Kündigungsfristen in AGB (§11) regeln

**Risiko:** Falls doch ein Verbraucher bestellt, könnte dieser theoretisch ein Widerrufsrecht geltend machen. Das wird aber durch:
1. B2B-Ausschluss in AGB
2. B2B-Pricing (monatliche Abo-Modelle)
3. B2B-Messaging auf Website

praktisch ausgeschlossen.

---

## 7. Checkliste: Was brauchen wir?

### 🔴 KRITISCH (Sofort umsetzen)

- [ ] **Impressum erstellen** und auf Website einbinden
  - Footer-Link auf jeder Seite
  - Eigene Unterseite `/impressum` oder `/legal`
  - Template oben verwenden
  - USt-IdNr. oder "nicht zugeteilt" eintragen
  - Echte Telefonnummer eintragen

### 🟡 EMPFOHLEN (Diese Woche)

- [ ] **Datenschutzerklärung veröffentlichen**
  - Bereits vorhanden als Markdown
  - In HTML konvertieren und auf `/datenschutz` hosten
  - Footer-Link hinzufügen

- [ ] **AGB veröffentlichen**
  - Bereits vorhanden als Markdown
  - In HTML konvertieren und auf `/agb` hosten
  - Link in Checkout/Registrierung
  - Checkbox: "Ich akzeptiere die AGB"

### 🟢 OPTIONAL (Später)

- [ ] **AVV-Template erstellen** für Kunden die einen benötigen
- [ ] **Auftragsverarbeiter in Datenschutzerklärung konkretisieren** sobald Hosting etc. final
- [ ] **Privacy-freundliche Analytics** (Plausible/Fathom) wenn gewünscht

---

## 8. Rechtliche Hinweise

**Disclaimer:** Diese Recherche ersetzt keine Rechtsberatung. Bei Unsicherheiten sollte ein auf IT-Recht spezialisierter Anwalt konsultiert werden.

**Quellen:**
- IHK Chemnitz: Impressumspflicht
- eRecht24: Impressum Pflichtangaben
- IT-Recht Kanzlei: AGB für SaaS
- §5 DDG (Digitale-Dienste-Gesetz)
- §25 TTDSG (Telekommunikation-Telemedien-Datenschutz-Gesetz)
- DSGVO Art. 6, 12-22, 28

---

*Erstellt: 03.02.2026 | RESEARCHER | Für: Team CNC Planner*
