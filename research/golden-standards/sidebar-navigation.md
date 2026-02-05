# Golden Standard: Sidebar Navigation

*Basierend auf Linear, Notion, Figma, Stripe*

---

## 1. Struktur

### Layout
```
┌─────────────────────────────────────────────────┐
│ ┌─────────┐ ┌─────────────────────────────────┐ │
│ │         │ │                                 │ │
│ │ SIDEBAR │ │         MAIN CONTENT            │ │
│ │  260px  │ │          flex: 1                │ │
│ │         │ │                                 │ │
│ │         │ │                                 │ │
│ └─────────┘ └─────────────────────────────────┘ │
└─────────────────────────────────────────────────┘
```

### Sections (von oben nach unten)
```
┌─────────────────┐
│ LOGO + NAME     │  ← 56px height
├─────────────────┤
│ Primary Nav     │  ← Hauptfunktionen
│  • Item 1       │
│  • Item 2       │
│  • Item 3       │
├─────────────────┤
│ Secondary Nav   │  ← Optional (Ausgabe)
│  • Item 4       │
│  • Item 5       │
├─────────────────┤
│      ↕         │  ← flex-grow (Spacer)
├─────────────────┤
│ Footer Nav      │  ← Einstellungen, Hilfe
│  • Settings     │
│  • Help         │
└─────────────────┘
```

---

## 2. CSS Spezifikationen

### Container
```css
.sidebar {
    width: 260px;
    height: 100vh;
    position: fixed;
    left: 0;
    top: 0;
    background: var(--color-surface);
    border-right: 1px solid var(--color-gray-200);
    display: flex;
    flex-direction: column;
    z-index: 20;
}
```

### Header/Logo
```css
.sidebar-header {
    height: 56px;
    padding: 0 16px;
    display: flex;
    align-items: center;
    border-bottom: 1px solid var(--color-gray-200);
}

.sidebar-logo {
    font-size: 16px;
    font-weight: 600;
    color: var(--color-gray-900);
}
```

### Navigation Section
```css
.sidebar-nav {
    flex: 1;
    overflow-y: auto;
    padding: 8px;
}

.nav-section {
    margin-bottom: 24px;
}

.nav-section-title {
    font-size: 11px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: var(--color-gray-500);
    padding: 8px 12px 4px;
}
```

### Navigation Item
```css
.nav-item {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 8px 12px;
    margin: 2px 0;
    border-radius: 6px;
    font-size: 14px;
    font-weight: 500;
    color: var(--color-gray-600);
    cursor: pointer;
    transition: all 150ms ease;
}

.nav-item:hover {
    background: var(--color-gray-100);
    color: var(--color-gray-900);
}

.nav-item.active {
    background: var(--color-primary);
    color: white;
}

.nav-item-icon {
    width: 20px;
    height: 20px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 16px;
    opacity: 0.8;
}

.nav-item.active .nav-item-icon {
    opacity: 1;
}
```

### Footer
```css
.sidebar-footer {
    padding: 8px;
    border-top: 1px solid var(--color-gray-200);
}
```

---

## 3. Verhalten

### Hover States
- Background: `--color-gray-100` (subtle)
- Text: `--color-gray-900` (darker)
- Transition: 150ms

### Active States
- Background: `--color-primary` (solid)
- Text: `white`
- Icon: `white` mit voller Opacity

### Keyboard Navigation
- `Tab` navigiert durch Items
- `Enter/Space` aktiviert Item
- `Arrow Up/Down` für schnelle Navigation

### Mobile (< 768px)
```css
@media (max-width: 768px) {
    .sidebar {
        transform: translateX(-100%);
        transition: transform 300ms ease;
    }
    
    .sidebar.open {
        transform: translateX(0);
    }
    
    .sidebar-overlay {
        position: fixed;
        inset: 0;
        background: rgba(0,0,0,0.5);
    }
}
```

---

## 4. Icons

### Empfohlen: Simple Line Icons
```
Teil auswählen:    ◻ (square)
Parameter:         ⚙ (gear)
Ergebnis:          € (euro) oder 📊 (chart)
Angebot:           📄 (document)
NC-Code:           </> (code)
Einstellungen:     ⚙ (gear, smaller)
```

### SVG Größe
- Icon: 20×20px
- Stroke-width: 1.5-2px
- Color: currentColor

---

## 5. Für CNC Planner Pro

### Empfohlene Struktur

```
┌─────────────────┐
│ CNC Planner Pro │
├─────────────────┤
│ KALKULATION     │  ← Section Title
│  ◻ Teil         │
│  ⚙ Parameter    │
│  € Ergebnis     │
├─────────────────┤
│ AUSGABE         │
│  📄 Angebot     │
│  </> NC-Code    │
├─────────────────┤
│      ↕         │
├─────────────────┤
│  ⚙ Einstellungen│  ← Immer unten
└─────────────────┘
```

### Warum diese Struktur?
1. **Kalkulation** ist der Kern → oben
2. **Ausgabe** ist das Ergebnis → nach Kalkulation
3. **Einstellungen** sind konfiguration → unten (wie in 99% aller Apps)

---

*Golden Standard v1.0*
