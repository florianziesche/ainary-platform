# 🎯 CNC Planer Pro — Demo Script
## Meeting: 04.02.2026, 10:30 Uhr | Maschinenbau Schlottwitz

**Teilnehmer:** Florian + Onkel (Geschäftsführer) + Arbeitsvorbereiter (AV)
**Ziel:** Arbeitsvorbereiter soll sagen "Das will ich haben" oder konkreten nächsten Schritt vereinbaren
**Dauer:** ~30 min (davon 15–20 min Demo)

---

## 1. ✅ Pre-Meeting Checklist

### Am Abend vorher (03.02.)
- [ ] **Laptop voll laden** (100% + Ladekabel mitnehmen)
- [ ] **demo.html testen** — `~/Desktop/cnc-deploy/demo.html` im Browser öffnen
- [ ] **OpenAI API Key prüfen** — in der App auf ⚙ klicken, Key eingeben, testen ob GPT-4o Vision funktioniert
  - Test: Screenshot einer beliebigen technischen Zeichnung hochladen → kommt JSON zurück?
  - Falls Key abgelaufen: neuen unter https://platform.openai.com/api-keys generieren
  - **Guthaben prüfen!** Mindestens $5 sollten drauf sein
- [ ] **Alle 3 Beispielprojekte durchklicken:**
  - Grundplatte (Ø130, 1.4571) → Tabs durchgehen
  - Lagerbock (120×80×55, 42CrMo4) → Dimensionen ändern → Neuberechnung prüfen
  - Flansch (Ø145, S355) → NC-Code Tab → Heidenhain prüfen
- [ ] **PDF-Export testen** — "PDF drucken" Button → kommt sauberes Angebot/Fertigungsanweisung?
- [ ] **Offline-Fähigkeit prüfen** — WLAN aus, App neu laden → Beispielprojekte müssen funktionieren
  - ⚠️ KI-Upload braucht Internet! Shop-WLAN-Passwort vorher beim Onkel erfragen
- [ ] **Test-Zeichnung vorbereiten** — eine einfache PDF-Zeichnung auf dem Laptop haben (Backup falls der AV keine mitbringt)
- [ ] **Browser-Tab vorbereiten** — demo.html öffnen, auf Startseite lassen (nicht schon ein Projekt geladen)

### Am Morgen
- [ ] **Handy auf stumm**
- [ ] **Laptop-Notifications aus** (Fokus-Modus)
- [ ] **Browser:** Nur 1 Tab offen (demo.html), keine peinlichen Tabs
- [ ] **Bildschirmhelligkeit auf Maximum** (Werkstatt-Beleuchtung!)
- [ ] **Font-Größe im Browser auf 110-125%** — damit der AV auch aus seiner Position mitlesen kann
- [ ] **Notizblock + Stift mitnehmen** — für seine Anforderungen/Feedback

---

## 2. 🤝 Opening (2–3 min)

### Ankommen & Rapport

> **Ziel:** Entspannte Atmosphäre, du bist Gast in seiner Welt. Er ist der Experte — du bist hier um zu lernen.

**Einstieg (an den Onkel gewandt):**
> "Danke, dass ihr euch die Zeit nehmt. Ich bin gespannt, wie die Arbeitsvorbereitung hier bei euch läuft."

**An den AV gewandt:**
> "Ich hab von [Onkel] gehört, dass Sie hier die Kalkulation und Arbeitsvorbereitung machen. Wie lange machen Sie das schon?"

→ **Lass ihn erzählen.** Das ist SEIN Gebiet. Respekt zeigen.

**Überleitung:**
> "Ich hab mir in den letzten Monaten die Frage gestellt: Kann man diesen ganzen Prozess — von der Zeichnung bis zum Angebot und Fertigungsauftrag — mit KI deutlich schneller machen? Ich zeig Ihnen heute mal, was ich gebaut hab. Und mich interessiert vor allem: Was denken Sie als Praktiker — funktioniert das so?"

→ **Wichtig:** Du bittest um seine Expertise, nicht um seinen Kauf!

---

## 3. 🔍 Discovery-Fragen

> **Ziel:** Verstehen, wo der Schmerz am größten ist. Notizen machen!

### Muss-Fragen (vor der Demo stellen)

1. **"Wie läuft das bei Ihnen heute ab, wenn eine neue Anfrage reinkommt?"**
   - Wer gibt die Zeichnung? Papier oder PDF?
   - Wie viele Anfragen pro Woche?

2. **"Wie kalkulieren Sie aktuell — Excel, Erfahrungswerte, oder gemischt?"**
   - → Bestätigung einholen: "60-90 Minuten pro Teil hab ich gehört?"
   - Was dauert dabei am längsten?

3. **"Für wie viele verschiedene Werkstoffe kalkulieren Sie?"**
   - → Vergleich: App hat 16 Werkstoffe mit korrekten Dichten/Zeitfaktoren

4. **"Wer macht den NC-Code? Direkt an der Maschine oder am CAM?"**
   - Welche Steuerung? → Heidenhain TNC? Siemens 840D? Fanuc?

5. **"Was nervt Sie am meisten am aktuellen Prozess?"**
   - → Das ist die GOLD-Frage. Was auch immer er sagt — darauf die Demo ausrichten.

### Bonus-Fragen (falls er redselig ist)
- "Wie oft verschätzen Sie sich bei der Zeitkalkulation?"
- "Haben Sie mal einen Auftrag verloren wegen zu langem Angebotsprozess?"
- "Dokumentieren Sie die Fertigungsparameter irgendwo, oder ist das Erfahrungswissen?"

---

## 4. 🖥️ Demo-Flow (15–20 min)

### Phase 1: Erster Eindruck (2 min)

> "Gut, dann zeig ich Ihnen mal, was die Software kann. Das Ganze läuft komplett im Browser — kein installieren, kein Cloud-Account nötig."

**[Laptop öffnen — demo.html ist auf der Startseite]**

→ Kurz die Oberfläche zeigen: Projekte oben, Upload-Bereich, Tabs unten

> "Sie sehen hier drei Beispielprojekte, die ich vorbereitet hab. Ich geh mal ein typisches Drehteil durch."

---

### Phase 2: Beispielprojekt Grundplatte (5 min)

**[Klick auf "Grundplatte WCAD-15-02-2020"]**

→ Loading-Animation läuft (5 Steps: Zeichnung laden → Material → Bearbeitung → NC-Code → Fertig)

> "Die Software erkennt automatisch: Rundteil, Edelstahl 1.4571, Ø130 Rohmaß, 10 Bearbeitungsschritte."

**[Tab: Angebot]**
> "Hier haben wir direkt ein fertiges Angebot. Stückpreis, Menge, MwSt — alles berechnet. Das können Sie so an den Kunden schicken."

**[Tab: Kalkulation]** ← Hier die meiste Zeit verbringen!
> "Jetzt wird's interessant für Sie als Arbeitsvorbereiter. Schauen Sie mal..."

**Zeigen:**
- Materialkosten-Berechnung (Rohmaße → Volumen → Gewicht → Kilopreis × Dichte)
- Maschinenzeit pro Operation (OP10 bis OP100)
- Kritische Operationen markiert (Ø120 h5, Ø26 H7)
- Maschinenstundensatz €85/h

> "Kommen Ihnen diese Zeiten realistisch vor? 41,8 Minuten Gesamtzeit für so eine Grundplatte in 1.4571?"

→ **PAUSE. Seine Reaktion abwarten.** Das ist der wichtigste Moment.

---

### Phase 3: Live-Kalkulation — der WOW-Effekt (3 min)

> "Jetzt zeig ich Ihnen den Unterschied zu Excel. Passen Sie mal auf..."

**[Dimension ändern: Durchmesser von 130 auf 160]**

> "Ich ändere einfach den Durchmesser auf 160..."

→ **Alle Werte aktualisieren sich sofort:** Gewicht, Materialkosten, Bearbeitungszeit, Maschinenkosten, Gesamtpreis

> "Sehen Sie? Gewicht, Material, Bearbeitungszeit — alles passt sich live an. In Excel müssten Sie jetzt 5 Zellen manuell anpassen."

**[Material ändern: von 1.4571 auf AlMg3]**

> "Und wenn der Kunde jetzt sagt: 'Geht das auch in Aluminium?' ..."

→ Zeigen wie sich Gewicht dramatisch ändert (Dichte 8.0 → 2.66), Bearbeitungszeit sinkt (Zeitfaktor 1.35 → 0.65), Preis sich komplett verschiebt

> "Der Werkstoff ändert auch die Schnittgeschwindigkeiten, die Zustellungen im NC-Code — alles automatisch."

**[Tab: Maschinencode]**

> "Schauen Sie sich den Heidenhain-Code an — die Spindeldrehzahl, die Vorschübe, die Zustelltiefe — das passt sich alles an den Werkstoff und die Maße an."

→ Falls er Siemens hat: **Klick auf "Siemens 840D"** Button → Code wechselt das Format!

---

### Phase 4: Werkzeuge & Fertigungsanweisung (2 min)

**[Tab: Werkzeuge]**

> "Hier sehen Sie die komplette Werkzeugliste mit Schnittdaten — Schnittgeschwindigkeit, Vorschub, Zustellung, Standzeit. Alles werkstoffabhängig berechnet."

**[Tab: Fertigungsanweisung]**

> "Und das hier geht direkt an die Maschine. Jeder Bediener sieht genau: Welche OP, welches Werkzeug, welche Parameter. Kritische Toleranzen sind rot markiert."

> "Kennen Sie das — neuer Mitarbeiter an der Maschine, und das Erfahrungswissen fehlt? Das hier löst das."

---

### Phase 5: 🌟 DER WOW-MOMENT — Seine Zeichnung (5 min)

> **Das ist das Herzstück der Demo!**

> "So, jetzt kommt der spannende Teil. Haben Sie zufällig eine aktuelle Zeichnung da? Irgendein Teil, das Sie gerade kalkulieren oder kürzlich gemacht haben?"

**Fall A: Er hat eine Zeichnung (Idealfall)**
- Er gibt ein PDF oder zeigt ein Blatt → Foto mit Handy machen
- **[Zeichnung in die Drop-Zone ziehen]**
- Warten auf GPT-4o Analyse (~10-15 Sekunden)
- Ergebnis zeigen: erkannte Maße, Werkstoff, Operationen, geschätzte Zeit

> "Stimmt das so ungefähr? [Maße zeigen] Und die Bearbeitungszeit — wie weit ist das von Ihrer Excel-Kalkulation weg?"

→ **Sein Urteil ist GOLD wert.** Notizen machen!

**Fall B: Keine Zeichnung da**
- → "Kein Problem, beschreiben Sie mir mal ein typisches Teil, das Sie letzte Woche gemacht haben."
- Seine Beschreibung in das Textfeld eingeben
- "Zum Beispiel: Lagerbock 42CrMo4, 120×80×55, Bohrung Ø25 H7, 4×M6"
- → Ergebnis zeigen

**Fall C: Kein Internet im Shop**
- → Zweites Beispielprojekt zeigen (Lagerbock) — "Stellen Sie sich vor, das wäre Ihr Teil"
- Werte so anpassen, dass sie zu einem echten Teil passen, das er beschreibt

> "In der Vollversion können Sie jede Zeichnung hochladen — PDF, Bild, sogar STEP-Dateien. Die KI erkennt Maße, Werkstoff, Toleranzen. Und dann steht die Kalkulation in unter 2 Minuten."

---

### Phase 6: PDF-Export (1 min)

**[Klick auf "PDF drucken"]**

> "Und am Ende: Ein Klick, und Sie haben ein professionelles Angebot als PDF. Oder eine Fertigungsanweisung für die Werkstatt. Fertig."

→ PDF öffnen lassen, kurz zeigen wie es aussieht

---

## 5. 💰 Pricing-Gespräch

> **Nur ansprechen, wenn ER danach fragt oder die Demo gut lief!**

### Vorbereitung: ROI-Rechnung im Kopf haben

| Szenario | Ohne CNC Planer | Mit CNC Planer |
|----------|-----------------|----------------|
| Zeit pro Kalkulation | 60-90 min | 5-10 min |
| Kalkulationen/Woche | ~10-15 | gleich |
| Zeitersparnis/Woche | — | ~12-15 Stunden |
| AV-Stundenlohn (intern) | ~35-45 €/h | — |
| Ersparnis/Monat | — | ~2.000-2.700 € |

### Gesprächsführung

> Wenn er fragt "Was kostet das?"

> "Bevor wir über den Preis reden — was wäre Ihnen die Zeitersparnis wert? Wenn Sie statt 60 Minuten pro Teil nur noch 5 brauchen?"

→ Lass IHN rechnen. Er kennt seine Zahlen.

**Dann die Preise:**

> "Es gibt drei Varianten:"
> - **Professional — €149/Monat:** Alles was Sie heute gesehen haben. Bis zu 50 Kalkulationen/Monat, alle Werkstoffe, PDF-Export.
> - **Business — €299/Monat:** Für Teams, unbegrenzte Kalkulationen, eigene Werkstoffdatenbank, Projekthistorie, plus einmalige Einrichtung.
> - **Enterprise:** Individuell — für Firmen mit speziellen Anforderungen (z.B. ERP-Anbindung, eigene Maschinen-Datenbank).

> "Für einen Betrieb in Ihrer Größe wäre Professional der richtige Einstieg. 149 Euro im Monat, das haben Sie nach 3-4 Kalkulationen wieder drin."

### Wenn er zögert:

> "Wir können auch erstmal mit einem Testmonat starten. Sie nutzen es 4 Wochen im Alltag, und dann entscheiden Sie, ob es sich lohnt."

---

## 6. 🛡️ Objection Handling

### "Das rechnet doch falsch / Die Zeiten stimmen nicht"
> "Genau deswegen bin ich hier — ich brauche Ihren Input. Die Zeitfaktoren und Maschinenstundensätze kann man anpassen. Welche Werte nutzen Sie?"
> → Notizen machen! Das ist Produkt-Feedback.

### "Unsere Teile sind zu komplex dafür"
> "Haben Sie ein Beispiel? Zeigen Sie mir das komplexeste Teil, das Sie letzte Woche gemacht haben."
> → Upload testen oder händisch konfigurieren
> "Bei 80% der Teile spart es Zeit. Die restlichen 20% machen Sie weiter wie bisher."

### "Wir haben kein Budget für neue Software"
> "Versteh ich. Aber rechnen wir mal: Wenn Ihr Arbeitsvorbereiter pro Teil 45 Minuten spart, und Sie machen 10 Teile die Woche — das sind 30 Stunden im Monat. Bei 40€/h internen Kosten sind das 1.200€ Ersparnis. Die Software kostet 149€."

### "Meine Excel-Tabelle reicht mir"
> "Excel ist super flexibel, keine Frage. Aber generiert Ihnen Excel auch den NC-Code? Oder eine Fertigungsanweisung mit Werkzeugdaten? Oder passt es automatisch die Zeiten an, wenn sich der Werkstoff ändert?"
> → Nicht Excel schlecht machen, sondern zeigen was dazukommt.

### "Was ist mit Datenschutz / Cloud?"
> "Die App läuft komplett lokal in Ihrem Browser. Die Zeichnungsdaten gehen nur für die KI-Analyse an OpenAI — und auch das können wir in der Enterprise-Version auf eigenen Servern lösen."

### "Das ist ja nur eine Demo"
> "Richtig — und genau deswegen bin ich hier. Ich will sehen, ob das für einen echten Betrieb wie euren passt. Euer Feedback fließt direkt in die Entwicklung ein."
> → Ehrlichkeit ist hier die beste Strategie. Kein Overcommitting.

### "Wer macht den Support?"
> "In der Anfangsphase direkt ich. Das heißt: kurze Wege, schnelle Anpassungen. Wenn etwas nicht passt, wird es sofort gefixt."

---

## 7. 🎯 Close — Der nächste Schritt

### Wenn die Demo gut lief (er nickt, stellt Fragen, will mehr sehen):

> "Was denken Sie — könnte das bei Ihnen im Alltag funktionieren?"

→ Seine Antwort abwarten.

> "Mein Vorschlag: Ich schick Ihnen morgen die App mit einer Testlizenz. Sie probieren es 2-3 Wochen mit Ihren echten Teilen. Und dann setzen wir uns nochmal zusammen und schauen, was angepasst werden muss."

**Konkretes Datum vereinbaren:**
> "Passt es Ihnen, wenn wir in 3 Wochen nochmal telefonieren? Dann können Sie mir sagen, was funktioniert und was nicht."

### Wenn er skeptisch aber höflich ist:

> "Ich merke, Sie sind noch nicht ganz überzeugt — und das ist völlig in Ordnung. Was müsste die Software können, damit Sie sagen: Das nutze ich?"

→ **ZUHÖREN.** Seine Anforderungen sind die Roadmap.

### Wenn es nicht gut lief:

> "Ich sehe, das passt im Moment noch nicht ganz. Darf ich Sie fragen: Was wäre der wichtigste Punkt, der sich ändern müsste?"

→ Notizen machen, bedanken, gehen. Kein Druck.

### In jedem Fall:
- [ ] **Kontaktdaten des AV einholen** (Handy-Nummer oder E-Mail)
- [ ] **Feedback-Widget zeigen:** "Falls Ihnen später noch was einfällt — hier können Sie direkt Feedback geben"
- [ ] **Konkreten nächsten Schritt festlegen** (Datum!)

---

## 8. 📋 Post-Meeting Follow-up

### Noch am selben Tag (04.02.)
- [ ] **Notizen digitalisieren** — alles was der AV gesagt hat, seine Einwände, seine Wünsche
- [ ] **Dankes-Nachricht an den Onkel** (WhatsApp/Telefon)
  > "Danke fürs Organisieren! Wie war dein Eindruck?"
- [ ] **Dankes-E-Mail an den AV** (falls E-Mail bekommen)
  > Kurz, professionell, mit Zusammenfassung der besprochenen nächsten Schritte
- [ ] Feedback in `memory/2026-02-04.md` dokumentieren

### Innerhalb von 48h
- [ ] **Falls Testlizenz versprochen:** App-Zugang einrichten und zusenden
- [ ] **Falls Anpassungswünsche:** Roadmap updaten, priorisieren
- [ ] **Falls er eine Zeichnung geteilt hat:** Ergebnis der KI-Analyse nochmal sauber aufbereiten und zuschicken

### In 2-3 Wochen
- [ ] **Follow-up Call/Besuch** (zum vereinbarten Termin)
- [ ] Fragen: "Wie oft haben Sie es genutzt? Was hat funktioniert, was nicht?"
- [ ] → Wenn positiv: Abo-Abschluss anbieten

---

## 9. 🧠 Mental Notes

### Mindset
- Du bist **NICHT im Verkaufsmodus**. Du bist im **Lernmodus**.
- Der AV ist der Experte. Du baust ein Tool FÜR IHN.
- Jede Kritik ist ein Geschenk — das ist die Produkt-Roadmap.
- Dein Onkel ist der Türöffner, aber der AV ist der Entscheider (im Sinne von: wenn er es nicht nutzt, bringt es nichts).

### Körpersprache
- Laptop so drehen, dass der AV direkt draufschauen kann
- Neben ihm stehen, nicht gegenüber (gemeinsam aufs Problem schauen)
- Blickkontakt halten wenn er spricht, nicht auf den Bildschirm starren

### Dont's
- ❌ Nicht über Features reden, die es noch nicht gibt
- ❌ Nicht "in Zukunft wird das..." sagen — nur zeigen was DA ist
- ❌ Nicht die Zeiten/Werte verteidigen wenn er sagt sie stimmen nicht — **seine Werte übernehmen**
- ❌ Nicht länger als 25 Minuten bleiben (er hat zu arbeiten)
- ❌ Nicht den Preis von dir aus ansprechen

### Do's
- ✅ Seine Sprache übernehmen (Zustellung, Aufmaß, Werkstoffnummer — nicht "Parameter")
- ✅ Ehrlich sein: "Das ist ein Prototyp, ich will wissen ob die Richtung stimmt"
- ✅ Stift und Papier nutzen — zeigt, dass du seine Worte ernst nimmst
- ✅ Wenn er einen Fehler findet: "Super, genau dafür bin ich hier" und aufschreiben

---

## 10. ⚡ Quick Reference: Demo-Hotkeys

| Aktion | Wo |
|--------|-----|
| Projekt laden | Klick auf Projektkarte oben |
| Dimensionen ändern | Input-Felder: Durchmesser/X, Y, Z, Aufmaß |
| Material wechseln | Dropdown "Werkstoff" |
| NC-Code Format | Buttons: Heidenhain / Siemens 840D / Fanuc |
| Zeichnung hochladen | Drop-Zone oben ODER Klick |
| API-Key eingeben | ⚙ Zahnrad-Icon rechts oben |
| PDF exportieren | "PDF drucken" Button im Angebot/Fertigungsanweisung Tab |
| Aufschlag ändern | "Marge %" Feld in der Kalkulation |

---

*Viel Erfolg, Florian! 🔧*
