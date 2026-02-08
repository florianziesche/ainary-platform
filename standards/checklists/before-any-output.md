# Pre-Flight Checklist — VOR jedem Output

*Automatisch durchgehen. Kein Output ohne diese Prüfung.*

---

## 1. SUCHE ZUERST (30 Sekunden)

```bash
# Gibt es schon ein Template/Standard dafür?
grep -i "[keyword]" INDEX.md
grep -i "[keyword]" standards/FLORIAN.md
```

- [ ] INDEX.md durchsucht — existiert schon was Ähnliches?
- [ ] Template vorhanden? → Nutzen, nicht neu bauen
- [ ] Standard/Skill vorhanden? → Lesen und befolgen

## 2. FORMAT PRÜFEN

- [ ] Was ist das richtige Format? (HTML Dashboard / LaTeX PDF / Markdown / Email Draft)
- [ ] Passt die CI? → `standards/CORPORATE-IDENTITY.md` gelesen?
- [ ] Fonts: Inter + JetBrains Mono (keine anderen)
- [ ] Farben: Gold Spectrum + Monochrome (keine anderen Akzente)
- [ ] Keine Emojis/Apple-Symbole in professionellen Dokumenten

## 3. FLORIAN-CHECK

- [ ] `standards/FLORIAN.md` konsultiert
- [ ] Ist das Output sofort nutzbar OHNE Nacharbeit?
- [ ] Empfänger/Subject/Pfad klar wenn es gesendet werden soll?
- [ ] EINE Empfehlung statt Optionen?

## 4. QUALITÄTS-CHECK

- [ ] Encoding: Umlaute korrekt (ä ö ü ß)?
- [ ] Keine Platzhalter (TODO, TBD, XXX, [...])?
- [ ] Zahlen mit Quellen belegt?
- [ ] Kontaktdaten aktuell (+49 151 230 39 208, florian@ainaryventures.com)?
- [ ] Dateiname sinnvoll und beschreibend?

## 5. DELIVERY

- [ ] Pfad angeben bei Abgabe
- [ ] Auch nach Obsidian kopieren wenn relevant?
- [ ] Auch auf Desktop wenn Florian es extern nutzt?
- [ ] Kontext mitgeben: "Was ist es, wofür, was als nächstes"

## 6. NACH ABGABE (Erinnerung)

- [ ] Output-Tracker aktualisieren: `failures/output-tracker.md`
- [ ] War der Output nützlich? Wenn nein: analysieren

---

*Ziel: 0 Outputs die Florian nicht nutzt weil die Qualität nicht stimmte.*
