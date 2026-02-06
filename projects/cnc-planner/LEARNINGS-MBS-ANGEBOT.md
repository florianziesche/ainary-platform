# Learnings aus MBS Angebot 20260072

**Quelle:** `/Users/florianziesche/Downloads/2026-02-05 23-36.pdf`  
**Datum Analyse:** 2026-02-06 00:35

---

## 📋 Was zeigt das Dokument?

**Echtes Angebot von MBS Maschinenbau Schlottwitz GmbH & Co. KG**
- Angebotsnummer: 20260072
- Datum: 28.01.2026
- Kunde: Müller Industrie GmbH, Hauptstraße 26, 09619 Mulda
- Bearbeiter: Sebastian Uhlig

---

## ✅ Was können wir ÜBERNEHMEN:

### 1. **Zeichnungsnummern als Referenz**
```
Platte — Zchng Nr. 2500473.01.01.02.01.001
Zylinder — Zchng Nr. 2500473.01.01.02.01.002
Block — Zchng Nr. 2500473.01.01.01.01.001
```

**→ FÜR CNC PLANER PRO:**
- Zeichnungsnummer PROMINENT im Opening Card
- Format: `Zeichnung-Nr.: XXXX.XX.XX.XX.XX.XXX`
- Macht Angebot nachvollziehbar und professionell

---

### 2. **Artikelnummer-System**
```
Alle Positionen: E-STI-0001
```

**→ FÜR CNC PLANER PRO:**
- Eindeutige Artikelnummer pro Teil generieren
- Format: `E-CNC-XXXX` oder kundenspezifisch
- Im Angebot und Fertigungsanweisung verwenden

---

### 3. **Tabellen-Struktur (Angebot)**

| Pos | Artikelnummer | Bezeichnung | Menge | Einzelpreis | Gesamtpreis |
|-----|---------------|-------------|-------|-------------|-------------|
| 10  | E-STI-0001    | Platte      | 10    | 98,10       | 981,00      |
| 20  | E-STI-0001    | Zylinder    | 20    | 60,80       | 1.216,00    |

**→ FÜR CNC PLANER PRO:**
- Position-Nummerierung (10, 20, 30... wie in Fertigungsplänen)
- Klare Spalten: Pos | Artikelnr | Bezeichnung | Menge | EP | GP
- Gesamtsumme am Ende

---

### 4. **Footer - Rechtliche Informationen**

**MBS hat:**
- Geschäftsführer
- Handelsregister-Nummer
- USt-ID
- Bankverbindung
- IBAN/BIC

**→ FÜR CNC PLANER PRO:**
- Template für Firmen-Footer
- Platzhalter für Kontaktdaten
- Optional: Geschäftsbedingungen-Link

---

### 5. **Angebots-Gültigkeit**

> "Unser Angebot ist freibleibend mit einer Gültigkeit von 4 Wochen"

**→ FÜR CNC PLANER PRO:**
- Automatisches Gültigkeitsdatum (Heute + 4 Wochen)
- Im Angebot prominent zeigen
- Standard: 4 Wochen (anpassbar in Einstellungen)

---

### 6. **Hinweise zur Preiskalkulation**

> "Die Preiskalkulation basiert auf derzeit gültigen Materialaufschlagspreisen / Zustellpreisen. Änderung innerhalb der Angebotsgültigkeit behalten sich eventuelle Nachkalkulationen und Anpassungen vor."

**→ FÜR CNC PLANER PRO:**
- Disclaimer im Angebot-Footer:
  ```
  Preise basierend auf aktuellen Materialkosten. 
  Änderungen vorbehalten bei stark schwankenden Marktpreisen.
  ```

---

### 7. **Zahlungsbedingungen**

> "Für Bestellungen unter 100,- € Warenwert berechnen wir einen Mindermengenzuschlag von pauschal 35,-€"

**→ FÜR CNC PLANER PRO:**
- Mindermengenzuschlag konfigurierbar
- Zahlungsziel konfigurierbar (z.B. "30 Tage netto")
- Skonto optional (z.B. "2% bei Zahlung innerhalb 14 Tagen")

---

### 8. **Sonderwünsche-Hinweis**

> "Kommen Sonderwünsche und Kundenwünsche zum Einsatz, so behalten wir uns, eventuell vorhandene Restmaterial separat in Rechnung zu stellen."

**→ FÜR CNC PLANER PRO:**
- Checkbox "Sonderwünsche berücksichtigt"
- Optionaler Hinweis im Angebot

---

### 9. **Mengenangaben pro Position**

```
10 Stück Platte
20 Stück Zylinder
5 Stück Halter
```

**→ FÜR CNC PLANER PRO:**
- Stückzahl MUSS im Angebot pro Position stehen
- Einzelpreis × Menge = Gesamtpreis
- Bei Losgröße > 1: Einrichtkosten-Verteilung zeigen

---

### 10. **Professionelles Layout**

**Design-Prinzipien:**
- ✅ Klare Hierarchie (Header → Tabelle → Footer)
- ✅ Schwarz/Weiß mit Logo-Farbe als Akzent
- ✅ Tabellarisch, keine Schnörkel
- ✅ Alle Infos auf einen Blick
- ✅ Zeichnungsnummer als Referenz
- ✅ Rechtliche Absicherung im Footer

---

## 🔧 KONKRETE TODOs für CNC Planer Pro:

### ANGEBOT-Tab verbessern:

1. **Zeichnungsnummer** ins Opening Card (neben Bauteil-Name)
   ```
   Bauteil: Platte (Lagerbock)
   Zeichnung-Nr.: 2500473.01.01.02.01.001
   ```

2. **Artikelnummer** generieren (z.B. `E-CNC-0001`)

3. **Position-Nummerierung** in Tabelle (10, 20, 30...)

4. **Gültigkeit** automatisch berechnen und anzeigen:
   ```
   Gültig bis: 05.03.2026 (4 Wochen)
   ```

5. **Footer mit Rechtsinformationen** Template:
   ```
   Geschäftsführer: [Name]
   Handelsregister: [HR-Nummer]
   USt-ID: [USt-ID]
   IBAN: [IBAN]
   
   Zahlungsbedingungen: 30 Tage netto
   Mindermengenzuschlag: €35 bei Auftragswert < €100
   ```

6. **Hinweise zur Kalkulation** (Disclaimer):
   ```
   Die Preise basieren auf aktuellen Materialkosten und 
   Standard-Fertigungsparametern (±15% Genauigkeit). 
   Änderungen bei Sonderwünschen oder stark schwankenden 
   Marktpreisen vorbehalten.
   ```

---

## 🎯 Priorität:

**P0 - Für Demo morgen (10:30):**
- ✅ Zeichnungsnummer prominent zeigen
- ✅ Gültigkeit berechnen (Heute + 4 Wochen)
- ✅ Footer mit Disclaimer

**P1 - Nach Demo:**
- Artikelnummer-System
- Position-Nummerierung
- Zahlungsbedingungen konfigurierbar
- Mindermengenzuschlag

---

## 💡 Key Insight:

**MBS Angebot ist EXTREM nüchtern und professionell:**
- Keine Emojis
- Keine bunten Farben
- Keine Marketing-Sprache
- NUR Fakten: Zeichnung, Menge, Preis, Bedingungen

**→ Unser CNC Planer Pro Design (neu mit Industrial Colors) ist GENAU richtig!**

---

*Analysiert: 2026-02-06 00:35*  
*Für Demo bei Onkel (10:30)*
