# Research: Einrichtzeit & Spannung bei CNC-Fräsen

**Erstellt:** 2026-02-05
**Anlass:** Feedback aus Demo mit Andreas — Fragen zur Spannung und wie das Programm die Position nachvollzieht

---

## 1. Ground Truth: Was wissen wir?

### Validierte Fakten (aus Recherche):

**Kosten von Rüstzeit:**
- 4 Umspannungen/Tag × 220 Tage = **880 Stunden/Jahr**
- Bei €85/h Maschinenstundensatz = **€74.800 Produktivitätsverlust**
- → Rüstzeit ist ein MASSIVER Kostenfaktor

**Rüstzeit-Richtwerte:**
| Methode | Typische Zeit | Reduktion |
|---------|---------------|-----------|
| Manuelles Spannen (Schraubstock) | 15-60 min | Baseline |
| Spannpratzen auf Tisch | 30-60 min | Aufwändiger |
| Nullpunktspannsystem | <5 min | -90% |
| Hauptzeitparalleles Rüsten | Variable | Rüsten außerhalb der Maschine |

**Spannung und Position (WCS):**
- **G54-G59** = Work Coordinate Systems (Nullpunktverschiebung)
- Definiert: Wo ist der Werkstück-Nullpunkt relativ zum Maschinen-Nullpunkt?
- **Problem:** CAM-Software setzt WCS, aber Bediener muss REAL messen/antasten
- Bei Tischspannung: Jedes Mal neu ausrichten und Nullpunkt setzen

---

## 2. Das Problem das Andreas anspricht:

### Schraubstock vs. Tischspannung:

**Schraubstock:**
- ✅ Position reproduzierbar (wenn Schraubstock einmal ausgerichtet)
- ✅ Schnelles Wechseln von Werkstücken
- ❌ Nur für passende Geometrien
- → WCS muss nur 1x gesetzt werden, dann für alle Teile gleich

**Tischspannung (Spannpratzen):**
- ✅ Flexibel für große/unförmige Teile
- ❌ Jedes Teil muss neu positioniert werden
- ❌ Nullpunkt muss jedes Mal neu angetastet werden
- → WCS-Setup ist Teil der Rüstzeit PRO TEIL

### Die Kernfrage:
> "Woher weiß das Programm, wo das Teil liegt?"

**Antwort:**
1. CAM-Software definiert theoretischen Nullpunkt (z.B. Ecke des Rohteils)
2. Bediener spannt Teil auf Maschine
3. Bediener tastet Nullpunkt an (Kantentaster, 3D-Taster, manuell)
4. Bediener trägt Offset in Steuerung ein (G54 X... Y... Z...)
5. Programm läuft relativ zu diesem Offset

→ **Das Programm "weiß" es nicht automatisch — der Bediener muss es der Maschine sagen!**

---

## 3. Faktoren die Einrichtzeit beeinflussen:

| Faktor | Einfluss | Typische Zeit |
|--------|----------|---------------|
| **Spannmittel wechseln** | Hoch | 10-30 min |
| **Schraubstock ausrichten** | Mittel | 5-15 min |
| **Teil einspannen** | Niedrig | 2-5 min |
| **Nullpunkt antasten** | Mittel | 5-15 min |
| **Werkzeuge einwechseln** | Variabel | 2-5 min/Werkzeug |
| **Programm laden/prüfen** | Niedrig | 2-5 min |
| **Erstes Teil Probelauf** | Hoch bei Prototyp | 10-30 min |

**Grobe Schätzung Gesamtzeit:**
- Einfaches Teil, Schraubstock vorhanden: **15-25 min**
- Komplexes Teil, Tischspannung: **30-60 min**
- Mit Nullpunktspannsystem: **5-10 min**

---

## 4. Was CNC Planer Pro berücksichtigen sollte:

### Muss abgefragt werden:
1. **Spannart:** Schraubstock / Spannpratzen / Nullpunktsystem / Spezialvorrichtung
2. **Anzahl Aufspannungen:** 1 / 2 / 3 / mehr
3. **Ausrichten nötig?** Ja (Tisch) / Nein (Schraubstock bereits ausgerichtet)
4. **Nullpunkt-Antasten:** Manuell / Messtaster / Kantentaster

### Kalkulationslogik:
```
Einrichtzeit = 
  + Basis (Programm laden, prüfen): 5 min
  + Spannmittel-Setup: 
    - Schraubstock (vorhanden): 0 min
    - Schraubstock (neu ausrichten): 10 min
    - Spannpratzen: 20 min
  + Nullpunkt-Antasten:
    - Messtaster: 3 min
    - Kantentaster: 8 min
    - Manuell: 12 min
  + Werkzeugwechsel: n × 3 min
  + Probelauf (Erstteil): 10-20 min
```

---

## 5. Offene Fragen für Andreas / Betrieb:

1. **Welche Spannmittel sind Standard?**
   - Schraubstockgrößen vorhanden?
   - Nullpunktspannsystem?
   - Spannpratzen-Sortiment?

2. **Wie wird Nullpunkt gesetzt?**
   - Messtaster?
   - Kantentaster?
   - Manuelles Ankratzen?

3. **Typische Rüstzeiten im Betrieb?**
   - Einfaches Teil (Schraubstock)?
   - Komplexes Teil (Tischspannung)?

4. **Gibt es Standard-Arbeitsanweisungen?**
   - Dokumentierte Abläufe?
   - Checklisten?

5. **Wie wird Ausrichtung dokumentiert?**
   - Schraubstock-Position bekannt?
   - Referenzpunkte am Tisch?

---

## 6. Implikation für CNC Planer Pro:

### Was die Software NICHT automatisch wissen kann:
- Tatsächliche Spannmittel im Betrieb
- Ob Schraubstock bereits ausgerichtet ist
- Nullpunkt-Antastmethode
- Maschinenspezifische Setup-Zeiten

### Was wir brauchen:
1. **Betriebsspezifische Einstellungen:**
   - Rüstzeit-Multiplikator (schnell/normal/aufwändig)
   - Standard-Spannmethode
   - Antastmethode

2. **Pro-Teil-Eingabe:**
   - Empfohlene Spannart
   - Anzahl Aufspannungen
   - Besondere Anforderungen

3. **Feedback-Loop:**
   - Tatsächliche Rüstzeit nach Fertigung erfassen
   - System lernt und passt Schätzungen an

---

*Nächster Schritt: Fragen mit Andreas klären, dann Logik im CNC Planer anpassen.*
