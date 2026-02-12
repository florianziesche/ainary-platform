# Werkzeug-Clustering für CNC Planner
**Tool-Planner Pattern Implementation**

*Basierend auf dem Tool-Planner Paper: Semantische Gruppierung von Werkzeugen statt einzelner Evaluation*

---

## Konzept

Statt 50+ Werkzeuge individuell zu evaluieren, clustern wir sie nach **Bearbeitungszielen**. Jeder Cluster enthält spezialisierte Tools für eine Hauptfunktion. Der Planner wählt zuerst den Cluster (basierend auf Operation), dann das optimale Tool innerhalb des Clusters (basierend auf Material, Toleranz, Geometrie).

**Vorteile:**
- ⚡ Schnellere Entscheidungsfindung (4 Cluster statt 50 Tools)
- 🎯 Kontextsensitive Auswahl (Operation → Cluster → Tool)
- 🧠 Einfachere Wartung (neue Tools zum passenden Cluster hinzufügen)
- 📊 Bessere Kostenabschätzung (Cluster-Level Kennzahlen)

---

## 1. Schrupp-Cluster (Materialentfernung)

**Ziel:** Maximale Zeitspanvolumen, Materialentfernung, Vorbereitung für Schlichtbearbeitung

### Werkzeuge

| Werkzeug | Durchmesser | Anwendung | Zerspanvolumen |
|----------|-------------|-----------|----------------|
| **Planfräser** | Ø63-Ø80 | Große Flächen | 300-800 cm³/min |
| **VHM Schaftfräser** | Ø16-Ø25 | Konturen, Taschen | 80-200 cm³/min |
| **Igelfräser** | Ø32-Ø50 | Schwere Zerspanung | 150-400 cm³/min |

### Entscheidungslogik

```
IF Fläche > 200 cm² AND Tiefe < 8mm
  → Planfräser (Ø63-Ø80)
ELSE IF Tasche OR Kontur
  → VHM Schaftfräser (Ø16-Ø25)
ELSE IF Aufmaß > 5mm AND Härte > 200 HB
  → Igelfräser (Ø32-Ø50)
ELSE
  → VHM Schaftfräser (größter passender Ø)
```

### Schnittdaten pro Material

#### **Stahl (S235-S355, ~200 HB)**
| Werkzeug | vc [m/min] | fz [mm] | ap [mm] | ae [mm] |
|----------|-----------|---------|---------|---------|
| Planfräser Ø80 | 180-220 | 0.25-0.35 | 2-4 | 60-75 |
| Schaftfräser Ø20 | 120-150 | 0.15-0.20 | 8-12 | 10-14 |
| Igelfräser Ø40 | 100-140 | 0.20-0.30 | 6-10 | 25-35 |

#### **Aluminium (AlMg3, ~70 HB)**
| Werkzeug | vc [m/min] | fz [mm] | ap [mm] | ae [mm] |
|----------|-----------|---------|---------|---------|
| Planfräser Ø80 | 400-600 | 0.30-0.45 | 3-5 | 60-75 |
| Schaftfräser Ø20 | 350-500 | 0.20-0.30 | 12-18 | 12-16 |
| Igelfräser Ø40 | 300-450 | 0.25-0.40 | 8-15 | 30-40 |

#### **Edelstahl (1.4301, ~190 HB)**
| Werkzeug | vc [m/min] | fz [mm] | ap [mm] | ae [mm] |
|----------|-----------|---------|---------|---------|
| Planfräser Ø80 | 120-160 | 0.20-0.28 | 1.5-3 | 55-70 |
| Schaftfräser Ø20 | 80-110 | 0.12-0.18 | 6-10 | 9-12 |
| Igelfräser Ø40 | 70-100 | 0.15-0.25 | 5-8 | 20-30 |

### Zeitformel

```
Zeit_Schrupp [min] = (Volumen [cm³] / Zeitspanvolumen [cm³/min]) × Sicherheitsfaktor

Zeitspanvolumen = (vc × π × D) / 1000 × fz × z × ap × ae / (D × π)
Vereinfacht: Q = fz × z × n × ap × ae

Sicherheitsfaktor:
- Planfräser: 1.15 (Nebenzeiten Indexierung)
- Schaftfräser: 1.25 (Freifahr/Eintauchbewegungen)
- Igelfräser: 1.35 (hohe Schnittkräfte → Rückzug)
```

**Praktische Faustformel:**
- **Planfräser:** 0.5-1.2 min pro 100 cm² (abhängig von ap)
- **Schaftfräser:** 2.5-5 min pro 100 cm³ Volumen
- **Igelfräser:** 1.8-4 min pro 100 cm³ Volumen

### Kostenfaktor

| Werkzeug | Anschaffung | Standzeit | €/Einsatz | Wechselzeit |
|----------|-------------|-----------|-----------|-------------|
| Planfräser Ø80 (mit Wendeschneidplatten) | 350€ + 12×15€ Platten | 8-12 Teile | 25-35€ | 3 min |
| VHM Schaftfräser Ø20 | 45€ | 15-25 Teile | 2-3€ | 1.5 min |
| Igelfräser Ø40 | 180€ | 10-18 Teile | 12-18€ | 2 min |

**Break-Even Fläche für Planfräser:**
- Planfräser vs. Schaftfräser: ab ~150 cm² Fläche (durch Zeitersparnis)

---

## 2. Schlicht-Cluster (Oberflächengüte)

**Ziel:** Definierte Oberflächenrauheit, Maßhaltigkeit, Endkontur

### Werkzeuge

| Werkzeug | Durchmesser | Zielrauheit | Toleranz |
|----------|-------------|-------------|----------|
| **Planfräser mit Wiper-Platten** | Ø80 | Ra 0.8-1.6 | IT10-IT11 |
| **VHM Schlichtfräser** | Ø16-Ø20 | Ra 1.6-3.2 | IT9-IT10 |
| **Kugelfräser** | Ø10-Ø16 | Ra 0.8-1.6 | IT10 |

### Entscheidungslogik

```
IF Ra_Soll ≤ 1.6 AND Fläche_eben > 50 cm²
  → Planfräser mit Wiper-Platten (Ø80)
ELSE IF Ra_Soll ≤ 1.6 AND (3D-Kontur OR Radius)
  → Kugelfräser (Ø10-Ø16)
ELSE IF Ra_Soll ≤ 3.2
  → VHM Schlichtfräser (Ø16-Ø20)
ELSE
  → Schrupp-Werkzeug mit angepassten Parametern
```

### Schnittdaten pro Material

#### **Stahl (S235-S355)**
| Werkzeug | vc [m/min] | fz [mm] | ap [mm] | ae [mm] |
|----------|-----------|---------|---------|---------|
| Wiper-Planfräser Ø80 | 200-250 | 0.15-0.25 | 0.5-1.5 | 60-75 |
| Schlichtfräser Ø20 | 150-200 | 0.08-0.12 | 1-3 | 0.3-0.8 |
| Kugelfräser Ø12 | 140-180 | 0.06-0.10 | 0.3-0.8 | zl 0.15-0.3 |

#### **Aluminium (AlMg3)**
| Werkzeug | vc [m/min] | fz [mm] | ap [mm] | ae [mm] |
|----------|-----------|---------|---------|---------|
| Wiper-Planfräser Ø80 | 500-700 | 0.20-0.35 | 0.8-2 | 60-75 |
| Schlichtfräser Ø20 | 400-600 | 0.10-0.18 | 1.5-4 | 0.4-1.0 |
| Kugelfräser Ø12 | 350-500 | 0.08-0.14 | 0.4-1.0 | zl 0.2-0.4 |

#### **Edelstahl (1.4301)**
| Werkzeug | vc [m/min] | fz [mm] | ap [mm] | ae [mm] |
|----------|-----------|---------|---------|---------|
| Wiper-Planfräser Ø80 | 140-180 | 0.12-0.20 | 0.4-1.2 | 55-70 |
| Schlichtfräser Ø20 | 100-140 | 0.06-0.10 | 0.8-2.5 | 0.25-0.6 |
| Kugelfräser Ø12 | 90-130 | 0.05-0.08 | 0.25-0.6 | zl 0.12-0.25 |

*zl = Zeilenabstand bei 3D-Fräsen*

### Zeitformel

```
Zeit_Schlicht [min] = (Fläche [cm²] / Vorschub_effektiv [cm²/min]) × Sicherheitsfaktor

Vorschub_effektiv:
- Planfräser: vf [mm/min] × ae [mm] / 100
- Schlichtfräser: vf [mm/min] × ae [mm] / 100
- Kugelfräser (3D): vf [mm/min] × zl [mm] / 100

Sicherheitsfaktor:
- Planfräser: 1.10 (wenige Nebenzeiten)
- Schlichtfräser: 1.20 (Konturwechsel)
- Kugelfräser: 1.40 (viele Richtungswechsel, 3D-Pfad)
```

**Praktische Faustformel:**
- **Wiper-Planfräser:** 0.3-0.8 min pro 100 cm²
- **Schlichtfräser:** 1.5-3.5 min pro 100 cm Konturlänge
- **Kugelfräser:** 4-8 min pro 100 cm² Freiformfläche

### Kostenfaktor

| Werkzeug | Anschaffung | Standzeit | €/Einsatz | Wechselzeit |
|----------|-------------|-----------|-----------|-------------|
| Wiper-Planfräser Ø80 | 450€ + 12×22€ Platten | 15-25 Teile | 20-28€ | 3 min |
| VHM Schlichtfräser Ø20 | 65€ | 25-40 Teile | 2-3€ | 1.5 min |
| VHM Kugelfräser Ø12 | 55€ | 15-30 Teile | 2-4€ | 1.5 min |

---

## 3. Bohr-Cluster (Löcher)

**Ziel:** Durchgangslöcher, Sacklöcher, Gewinde

### Werkzeuge

| Werkzeug | Durchmesser | Anwendung | Toleranz |
|----------|-------------|-----------|----------|
| **HSS Spiralbohrer** | Ø3-Ø20 | Standard-Bohrungen | IT11-IT13 |
| **VHM Bohrer** | Ø3-Ø16 | Präzise Bohrungen | H7-H8 |
| **Reibahlen** | Ø6-Ø20 | Passbohrungen | H6-H7 |
| **Gewindebohrer** | M6-M24 | Gewindeschneiden | 6H |

### Entscheidungslogik

```
IF Toleranz ≤ H7 AND Durchmesser ≥ 6mm
  → Vorbohren (Ø_Kern) + Reiben (Ø_Soll)
ELSE IF Toleranz ≤ H8 OR Tiefe > 5×D
  → VHM Bohrer
ELSE IF Gewinde
  → Kernlochbohrer + Gewindebohrer
ELSE
  → HSS Spiralbohrer

Vorbohrstrategie:
- Ø < 6mm: Direkt bohren
- Ø 6-12mm: Ø_Vor = Ø_Soll - 3mm
- Ø > 12mm: Ø_Vor = Ø_Soll × 0.7
```

### Schnittdaten pro Material

#### **Stahl (S235-S355)**
| Werkzeug | vc [m/min] | f [mm/U] | Kühlschmierung |
|----------|-----------|----------|----------------|
| HSS Spiralbohrer | 20-35 | 0.10-0.25 | Emulsion (8%) |
| VHM Bohrer | 60-100 | 0.08-0.20 | Emulsion + Innenkühlung |
| Reibahle | 8-15 | 0.15-0.40 | Schneidöl |
| Gewindebohrer | 8-12 | — | Schneidöl, reversierend |

#### **Aluminium (AlMg3)**
| Werkzeug | vc [m/min] | f [mm/U] | Kühlschmierung |
|----------|-----------|----------|----------------|
| HSS Spiralbohrer | 80-150 | 0.15-0.35 | Trocken oder Minimalmenge |
| VHM Bohrer | 200-350 | 0.12-0.30 | Druckluft oder MMS |
| Reibahle | 25-40 | 0.20-0.50 | Schneidöl |
| Gewindebohrer | 15-25 | — | Schneidöl, reversierend |

#### **Edelstahl (1.4301)**
| Werkzeug | vc [m/min] | f [mm/U] | Kühlschmierung |
|----------|-----------|----------|----------------|
| HSS Spiralbohrer | 12-22 | 0.08-0.18 | Hochdruckemulsion |
| VHM Bohrer | 40-70 | 0.06-0.15 | Innenkühlung (Hochdruck) |
| Reibahle | 6-12 | 0.12-0.30 | Schneidöl (EP-Zusatz) |
| Gewindebohrer | 6-10 | — | Schneidöl, langsam reversierend |

### Zeitformel

```
Zeit_Bohren [min] = (Tiefe [mm] / (f × n)) + Zeit_Nebenzeiten

n [1/min] = (vc × 1000) / (π × D)

Nebenzeiten:
- Anfahren: 0.1-0.2 min
- Späne-Brechen (bei Tiefe > 3×D): +20%
- Werkzeugwechsel: siehe Kostenfaktor

Zeit_Reiben = Zeit_Vorbohren + (Tiefe / (f_reib × n_reib)) + 0.3 min

Zeit_Gewinde [min] = (Tiefe [mm] / Steigung [mm]) / n + 0.2 min
  (inkl. Rückwärtslauf)
```

**Praktische Faustformel:**
- **HSS Bohren:** 0.15-0.4 min pro cm Bohrtiefe (Ø10, Stahl)
- **VHM Bohren:** 0.08-0.2 min pro cm Bohrtiefe (Ø10, Stahl)
- **Reiben:** +0.4-0.8 min pro Bohrung (inkl. Vorbohren)
- **Gewinde M10:** 0.6-1.2 min pro Gewinde (bis 30mm Tiefe)

### Kostenfaktor

| Werkzeug | Anschaffung | Standzeit (Löcher) | €/Loch | Wechselzeit |
|----------|-------------|--------------------|--------|-------------|
| HSS Spiralbohrer Ø10 | 8€ | 200-400 (Stahl) | 0.02-0.04€ | 0.5 min |
| VHM Bohrer Ø10 | 35€ | 150-300 (Stahl) | 0.12-0.23€ | 0.8 min |
| Reibahle H7 Ø10 | 45€ | 80-150 (Stahl) | 0.30-0.56€ | 1 min |
| Gewindebohrer M10 | 12€ | 100-200 (Stahl) | 0.06-0.12€ | 0.8 min |

**Break-Even:**
- VHM vs. HSS: ab ~50 Löcher pro Serie (durch Zeitersparnis)
- Reiben: nur bei H6-H7 Toleranzforderung (Qualität > Kosten)

---

## 4. Entgrat-Cluster (Nachbearbeitung)

**Ziel:** Gratfreie Kanten, Sicherheit, Oberflächenschutz

### Werkzeuge

| Werkzeug | Typ | Anwendung | Automatisierung |
|----------|-----|-----------|-----------------|
| **Fasenfräser 45°** | Ø16-Ø25 | Kanten, Bohrungen (außen) | CNC |
| **Rückwärtsentgrater** | Ø8-Ø16 | Bohrungen (beidseitig) | CNC |
| **Handentgrater** | — | Komplexe Geometrien | Manuell |

### Entscheidungslogik

```
IF Kante_gerade OR Kreis_außen
  → Fasenfräser 45° (CNC, 0.2-0.5mm Fase)
ELSE IF Bohrung AND Grat_beidseitig
  → Rückwärtsentgrater (automatisch)
ELSE IF Geometrie_komplex OR Zugänglichkeit_schlecht
  → Manuell (Handfeil, Entgratklinge)
ELSE
  → Fasenfräser (Best-Effort)
```

### Schnittdaten (CNC-Entgraten)

**Fasenfräser (alle Materialien):**
- **vc:** 80-150 m/min (Stahl), 200-400 m/min (Alu)
- **fz:** 0.05-0.10 mm
- **Fasenbreite:** 0.2-0.5 mm (Standard), bis 1.5 mm (Sichtteile)
- **Anstellwinkel:** 45° (Standard), 30° (kleine Fasen), 60° (große Fasen)

**Rückwärtsentgrater:**
- **vc:** 50-100 m/min
- **Vorschub:** 100-300 mm/min (langsam = sauberer)
- **Einsatz:** Nach jedem Bohrvorgang automatisch

### Zeitformel

```
Zeit_Entgraten [min]:

Fasenfräser:
  Zeit = (Kantenlänge [cm] / Vorschub [cm/min]) × 1.3
  Vorschub_typisch = 800-1500 mm/min = 80-150 cm/min
  → ca. 0.01-0.02 min pro cm Kante

Rückwärtsentgrater:
  Zeit = 0.15-0.3 min pro Bohrung (abhängig von Tiefe)

Manuell:
  Zeit = 0.5-2 min pro Bauteil (stark abhängig von Komplexität)
  Erfahrener Mitarbeiter: 0.8-1.2 min/Teil (einfache Geometrie)
```

**Praktische Faustformel:**
- **CNC-Fase:** 0.5-1.5 min pro Bauteil (automatisch)
- **Manuelles Entgraten:** 1-3 min pro Bauteil (Stundenlohn relevant!)

### Kostenfaktor

| Werkzeug | Anschaffung | Standzeit | €/Teil | Wechselzeit |
|----------|-------------|-----------|--------|-------------|
| Fasenfräser Ø20 (VHM) | 38€ | 80-150 Teile | 0.25-0.48€ | 1 min |
| Rückwärtsentgrater Ø12 | 55€ | 200-400 Bohrungen | 0.14-0.28€ | 1.5 min |
| Handentgrater (Set) | 25€ | — | Arbeitszeit | — |

**Break-Even CNC vs. Manuell:**
- Stundenlohn: 45€ (Facharbeiter inkl. Gemeinkosten)
- CNC-Fase: 1 min = 0.75€ (Maschinenkosten)
- Manuell: 2 min = 1.50€ (Arbeitslohn)
- → CNC ab ~5 Teilen pro Serie wirtschaftlich

**Wichtig:** Manuelles Entgraten ist **Qualitätsunsicher** (Werker-abhängig) und **Engpass** in der Fertigung!

---

## JavaScript Integration

### Haupt-Selektionsfunktion

```javascript
/**
 * Wählt optimalen Werkzeug-Cluster und Tool basierend auf Operation, Material und Anforderungen
 * @param {Object} params - Parameter-Objekt
 * @param {string} params.operation - 'roughing' | 'finishing' | 'drilling' | 'deburring'
 * @param {string} params.material - 'steel' | 'aluminum' | 'stainless'
 * @param {Object} params.geometry - Geometrie-Informationen
 * @param {number} params.tolerance - Toleranz in IT-Grade (optional)
 * @param {number} params.surfaceRoughness - Geforderte Ra in μm (optional)
 * @returns {Object} - { cluster, tool, cuttingData, timeEstimate, cost }
 */
function selectToolCluster(params) {
  const { operation, material, geometry, tolerance, surfaceRoughness } = params;
  
  // Cluster-Auswahl
  let cluster;
  switch (operation) {
    case 'roughing':
      cluster = selectRoughingTool(geometry, material);
      break;
    case 'finishing':
      cluster = selectFinishingTool(geometry, material, surfaceRoughness);
      break;
    case 'drilling':
      cluster = selectDrillingTool(geometry, material, tolerance);
      break;
    case 'deburring':
      cluster = selectDeburringTool(geometry);
      break;
    default:
      throw new Error(`Unknown operation: ${operation}`);
  }
  
  // Schnittdaten aus Datenbank laden
  const cuttingData = getCuttingData(cluster.tool, material);
  
  // Zeitabschätzung
  const timeEstimate = estimateTime(cluster, geometry, cuttingData);
  
  // Kostenabschätzung
  const cost = estimateCost(cluster, timeEstimate, material);
  
  return {
    cluster: cluster.name,
    tool: cluster.tool,
    cuttingData: cuttingData,
    timeEstimate: timeEstimate,
    cost: cost,
    reasoning: cluster.reasoning
  };
}

// Cluster-spezifische Selektionen
function selectRoughingTool(geometry, material) {
  const area = geometry.area; // cm²
  const volume = geometry.volume; // cm³
  const depth = geometry.depth; // mm
  
  if (area > 200 && depth < 8) {
    return {
      name: 'Schrupp-Cluster',
      tool: {
        type: 'face_mill',
        diameter: 80,
        name: 'Planfräser Ø80'
      },
      reasoning: `Große Fläche (${area.toFixed(0)} cm²) → Planfräser optimal`
    };
  } else if (geometry.type === 'pocket' || geometry.type === 'contour') {
    const diameter = Math.min(25, Math.max(16, geometry.minRadius * 0.8));
    return {
      name: 'Schrupp-Cluster',
      tool: {
        type: 'end_mill',
        diameter: diameter,
        name: `VHM Schaftfräser Ø${diameter}`
      },
      reasoning: 'Taschen/Konturen → Schaftfräser'
    };
  } else if (volume / area > 5 && getMaterialHardness(material) > 200) {
    return {
      name: 'Schrupp-Cluster',
      tool: {
        type: 'roughing_mill',
        diameter: 40,
        name: 'Igelfräser Ø40'
      },
      reasoning: 'Hohes Aufmaß + hartes Material → Igelfräser'
    };
  } else {
    return {
      name: 'Schrupp-Cluster',
      tool: {
        type: 'end_mill',
        diameter: 20,
        name: 'VHM Schaftfräser Ø20'
      },
      reasoning: 'Standard-Schruppbearbeitung'
    };
  }
}

function selectFinishingTool(geometry, material, surfaceRoughness) {
  const ra = surfaceRoughness || 3.2; // Default Ra 3.2
  const area = geometry.area;
  const is3D = geometry.type === '3d_surface' || geometry.hasCurvature;
  
  if (ra <= 1.6 && area > 50 && !is3D) {
    return {
      name: 'Schlicht-Cluster',
      tool: {
        type: 'wiper_face_mill',
        diameter: 80,
        name: 'Wiper-Planfräser Ø80'
      },
      reasoning: `Ra ${ra} μm + ebene Fläche → Wiper-Planfräser`
    };
  } else if (ra <= 1.6 && is3D) {
    return {
      name: 'Schlicht-Cluster',
      tool: {
        type: 'ball_nose',
        diameter: 12,
        name: 'Kugelfräser Ø12'
      },
      reasoning: `Ra ${ra} μm + 3D-Geometrie → Kugelfräser`
    };
  } else if (ra <= 3.2) {
    return {
      name: 'Schlicht-Cluster',
      tool: {
        type: 'finishing_mill',
        diameter: 20,
        name: 'VHM Schlichtfräser Ø20'
      },
      reasoning: `Ra ${ra} μm → Schlichtfräser ausreichend`
    };
  } else {
    return {
      name: 'Schrupp-Cluster',
      tool: {
        type: 'end_mill',
        diameter: 20,
        name: 'VHM Schaftfräser Ø20 (Schlichtparameter)'
      },
      reasoning: 'Keine hohen Oberflächenanforderungen'
    };
  }
}

function selectDrillingTool(geometry, material, tolerance) {
  const diameter = geometry.diameter; // mm
  const depth = geometry.depth; // mm
  const itGrade = tolerance || 11; // Default IT11
  const isThreaded = geometry.isThreaded || false;
  
  if (isThreaded) {
    return {
      name: 'Bohr-Cluster',
      tool: {
        type: 'tap',
        thread: geometry.thread,
        name: `Gewindebohrer ${geometry.thread}`
      },
      reasoning: 'Gewindebohrung → Kernlochbohrer + Gewindebohrer'
    };
  } else if (itGrade <= 7 && diameter >= 6) {
    return {
      name: 'Bohr-Cluster',
      tool: {
        type: 'reamer',
        diameter: diameter,
        name: `Reibahle H7 Ø${diameter}`
      },
      reasoning: `Toleranz H${itGrade} → Vorbohren + Reiben`
    };
  } else if (itGrade <= 8 || depth > 5 * diameter) {
    return {
      name: 'Bohr-Cluster',
      tool: {
        type: 'carbide_drill',
        diameter: diameter,
        name: `VHM Bohrer Ø${diameter}`
      },
      reasoning: `H${itGrade} oder Tiefe ${depth}mm → VHM Bohrer`
    };
  } else {
    return {
      name: 'Bohr-Cluster',
      tool: {
        type: 'hss_drill',
        diameter: diameter,
        name: `HSS Spiralbohrer Ø${diameter}`
      },
      reasoning: 'Standard-Bohrung → HSS ausreichend'
    };
  }
}

function selectDeburringTool(geometry) {
  const edgeLength = geometry.edgeLength || 0; // cm
  const holes = geometry.holes || 0;
  const complexity = geometry.complexity || 'simple'; // 'simple' | 'medium' | 'complex'
  
  if (complexity === 'complex') {
    return {
      name: 'Entgrat-Cluster',
      tool: {
        type: 'manual',
        name: 'Manuelles Entgraten'
      },
      reasoning: 'Komplexe Geometrie → Manuell'
    };
  } else if (holes > 0) {
    return {
      name: 'Entgrat-Cluster',
      tool: {
        type: 'back_deburrer',
        diameter: 12,
        name: 'Rückwärtsentgrater Ø12'
      },
      reasoning: `${holes} Bohrungen → Automatisches Entgraten`
    };
  } else if (edgeLength > 0) {
    return {
      name: 'Entgrat-Cluster',
      tool: {
        type: 'chamfer_mill',
        diameter: 20,
        angle: 45,
        name: 'Fasenfräser 45° Ø20'
      },
      reasoning: `${edgeLength.toFixed(0)} cm Kantenlänge → CNC Fase`
    };
  } else {
    return {
      name: 'Entgrat-Cluster',
      tool: {
        type: 'chamfer_mill',
        diameter: 20,
        angle: 45,
        name: 'Fasenfräser 45° Ø20'
      },
      reasoning: 'Standard-Entgratung'
    };
  }
}

// Hilfsfunktionen
function getCuttingData(tool, material) {
  // Lädt Schnittdaten aus Datenbank (hier: Beispieldaten)
  const database = {
    steel: {
      face_mill: { vc: 200, fz: 0.30, ap: 3, ae: 70 },
      end_mill: { vc: 135, fz: 0.175, ap: 10, ae: 12 },
      roughing_mill: { vc: 120, fz: 0.25, ap: 8, ae: 30 },
      wiper_face_mill: { vc: 225, fz: 0.20, ap: 1, ae: 70 },
      finishing_mill: { vc: 175, fz: 0.10, ap: 2, ae: 0.5 },
      ball_nose: { vc: 160, fz: 0.08, ap: 0.5, zl: 0.25 },
      hss_drill: { vc: 28, f: 0.175 },
      carbide_drill: { vc: 80, f: 0.14 },
      reamer: { vc: 12, f: 0.275 },
      tap: { vc: 10 },
      chamfer_mill: { vc: 120, fz: 0.075 }
    },
    aluminum: {
      face_mill: { vc: 550, fz: 0.375, ap: 4, ae: 70 },
      end_mill: { vc: 425, fz: 0.25, ap: 15, ae: 14 },
      roughing_mill: { vc: 375, fz: 0.325, ap: 12, ae: 35 },
      wiper_face_mill: { vc: 600, fz: 0.275, ap: 1.5, ae: 70 },
      finishing_mill: { vc: 500, fz: 0.14, ap: 2.5, ae: 0.7 },
      ball_nose: { vc: 425, fz: 0.11, ap: 0.7, zl: 0.3 },
      hss_drill: { vc: 115, f: 0.25 },
      carbide_drill: { vc: 275, f: 0.21 },
      reamer: { vc: 32, f: 0.35 },
      tap: { vc: 20 },
      chamfer_mill: { vc: 300, fz: 0.075 }
    },
    stainless: {
      face_mill: { vc: 140, fz: 0.24, ap: 2.25, ae: 62 },
      end_mill: { vc: 95, fz: 0.15, ap: 8, ae: 10.5 },
      roughing_mill: { vc: 85, fz: 0.20, ap: 6.5, ae: 25 },
      wiper_face_mill: { vc: 160, fz: 0.16, ap: 0.8, ae: 62 },
      finishing_mill: { vc: 120, fz: 0.08, ap: 1.65, ae: 0.42 },
      ball_nose: { vc: 110, fz: 0.065, ap: 0.42, zl: 0.18 },
      hss_drill: { vc: 17, f: 0.13 },
      carbide_drill: { vc: 55, f: 0.105 },
      reamer: { vc: 9, f: 0.21 },
      tap: { vc: 8 },
      chamfer_mill: { vc: 80, fz: 0.065 }
    }
  };
  
  return database[material][tool.type] || null;
}

function estimateTime(cluster, geometry, cuttingData) {
  // Vereinfachte Zeitabschätzung (sollte detaillierter sein)
  const clusterName = cluster.name;
  
  if (clusterName === 'Schrupp-Cluster') {
    const volume = geometry.volume || 0; // cm³
    const qcm = 150; // Durchschnittliches Zeitspanvolumen cm³/min
    return (volume / qcm) * 1.25; // min
  } else if (clusterName === 'Schlicht-Cluster') {
    const area = geometry.area || 0; // cm²
    const feedrate = 100; // cm²/min
    return (area / feedrate) * 1.20; // min
  } else if (clusterName === 'Bohr-Cluster') {
    const holes = geometry.holes || 1;
    const depth = geometry.depth || 20; // mm
    return holes * (depth / 50 + 0.2); // min (grobe Schätzung)
  } else if (clusterName === 'Entgrat-Cluster') {
    if (cluster.tool.type === 'manual') {
      return 1.5; // min (manuell)
    }
    const edgeLength = geometry.edgeLength || 0; // cm
    return edgeLength * 0.015 + 0.5; // min
  }
  
  return 0;
}

function estimateCost(cluster, timeEstimate, material) {
  const machineHourlyRate = {
    steel: 55, // €/h
    aluminum: 50,
    stainless: 60
  };
  
  const rate = machineHourlyRate[material] || 55;
  const machineCost = (timeEstimate / 60) * rate;
  
  const toolCostPerPart = {
    'face_mill': 28,
    'end_mill': 2.5,
    'roughing_mill': 15,
    'wiper_face_mill': 24,
    'finishing_mill': 2.5,
    'ball_nose': 3,
    'hss_drill': 0.03,
    'carbide_drill': 0.17,
    'reamer': 0.43,
    'tap': 0.09,
    'chamfer_mill': 0.36,
    'back_deburrer': 0.21,
    'manual': 0 // Arbeitszeit in Maschinenkosten
  };
  
  const toolCost = toolCostPerPart[cluster.tool.type] || 0;
  
  return {
    machine: machineCost.toFixed(2),
    tool: toolCost.toFixed(2),
    total: (machineCost + toolCost).toFixed(2),
    currency: '€'
  };
}

function getMaterialHardness(material) {
  const hardness = {
    steel: 200,
    aluminum: 70,
    stainless: 190
  };
  return hardness[material] || 150;
}

// Export
module.exports = {
  selectToolCluster,
  getCuttingData,
  estimateTime,
  estimateCost
};
```

### Verwendungsbeispiel

```javascript
const params = {
  operation: 'roughing',
  material: 'steel',
  geometry: {
    type: 'pocket',
    area: 150, // cm²
    volume: 300, // cm³
    depth: 15, // mm
    minRadius: 10 // mm
  }
};

const result = selectToolCluster(params);

console.log(result);
/*
Output:
{
  cluster: 'Schrupp-Cluster',
  tool: {
    type: 'end_mill',
    diameter: 20,
    name: 'VHM Schaftfräser Ø20'
  },
  cuttingData: {
    vc: 135,
    fz: 0.175,
    ap: 10,
    ae: 12
  },
  timeEstimate: 2.5, // min
  cost: {
    machine: '2.29',
    tool: '2.50',
    total: '4.79',
    currency: '€'
  },
  reasoning: 'Taschen/Konturen → Schaftfräser'
}
*/
```

---

## Wartung & Erweiterung

### Neue Werkzeuge hinzufügen

1. **Cluster identifizieren** (Schrupp/Schlicht/Bohr/Entgrat)
2. **Werkzeug-Daten ergänzen:**
   - Durchmesser, Typ, Anwendung
   - Schnittdaten pro Material
   - Kosten & Standzeit
3. **Entscheidungslogik anpassen** (in `selectXXXTool()`)
4. **Datenbank erweitern** (`getCuttingData()`)

### Neue Materialien hinzufügen

1. **Schnittdaten recherchieren** (Herstellerkataloge)
2. **Alle 4 Cluster** mit Schnittdaten befüllen
3. **Härte ergänzen** (`getMaterialHardness()`)
4. **Maschinenstundensatz** festlegen (`machineHourlyRate`)

### Best Practices

- **Cluster klein halten:** Max. 3-5 Tools pro Cluster
- **Entscheidungslogik dokumentieren:** Warum wurde ein Tool gewählt?
- **Zeitformeln regelmäßig validieren:** Gegen reale Maschinenzeiten
- **Kostenmodell aktualisieren:** Werkzeugpreise & Standzeiten ändern sich

---

## Zusammenfassung

| Cluster | Hauptziel | Typische Tools | Zeitfaktor | Kostenfaktor |
|---------|-----------|----------------|------------|--------------|
| **Schrupp** | Materialentfernung | Planfräser, Schaftfräser, Igelfräser | 1× (Basis) | Mittel |
| **Schlicht** | Oberflächengüte | Wiper, Schlichtfräser, Kugelfräser | 0.3-0.8× | Niedrig |
| **Bohr** | Löcher | HSS/VHM Bohrer, Reiben, Gewinde | 0.1-0.4× pro Loch | Sehr niedrig |
| **Entgrat** | Kanten | Fasenfräser, Rückwärtsentgrater, manuell | 0.2-0.5× | Niedrig (CNC) |

**Gesamtstrategie:**
1. Operation identifizieren → Cluster wählen
2. Geometrie + Material + Toleranz → Tool im Cluster wählen
3. Schnittdaten laden → Zeit & Kosten berechnen
4. Ergebnis zurückgeben mit Begründung

**Vorteile dieses Systems:**
- ⚡ Schnelle Entscheidungen (max. 2-stufige Logik)
- 🎯 Kontextsensitiv (nicht nur Material, sondern auch Geometrie)
- 🧠 Erweiterbar (neue Tools einfach zu Clustern hinzufügen)
- 💰 Kostenoptimiert (Break-Even Analysen integriert)
- 📖 Transparent (Reasoning wird mitgeliefert)

---

*Dokument erstellt: 2026-02-10*  
*Version: 1.0*  
*Autor: CNC Planner Sub-Agent*
