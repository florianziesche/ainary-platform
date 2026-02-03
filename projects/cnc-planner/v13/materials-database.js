// ==========================================
// CNC PLANNER PRO — MATERIALS DATABASE
// ==========================================
// Comprehensive database of materials with machining parameters
// Last updated: 2026-02-03

const MATERIALS_DB = {
    // === EDELSTAHL ===
    '1.4571': {
        name: 'X6CrNiMoTi17-12-2',
        shortName: 'V4A',
        group: 'Edelstahl',
        density: 7.98,
        pricePerKg: 7.00,
        machinabilityFactor: 1.0,
        hardness: '180 HB',
        tensileStrength: '500-700 MPa',
        cuttingSpeed: { rough: 80, finish: 120 },
        notes: 'Säurebeständig, für chemische Industrie'
    },
    '1.4301': {
        name: 'X5CrNi18-10',
        shortName: 'V2A',
        group: 'Edelstahl',
        density: 7.90,
        pricePerKg: 5.50,
        machinabilityFactor: 0.9,
        hardness: '170 HB',
        tensileStrength: '500-700 MPa',
        cuttingSpeed: { rough: 90, finish: 130 },
        notes: 'Standard-Edelstahl, gute Korrosionsbeständigkeit'
    },
    '1.4404': {
        name: 'X2CrNiMo17-12-2',
        shortName: '316L',
        group: 'Edelstahl',
        density: 7.95,
        pricePerKg: 6.50,
        machinabilityFactor: 0.95,
        hardness: '175 HB',
        tensileStrength: '480-680 MPa',
        cuttingSpeed: { rough: 85, finish: 125 },
        notes: 'Niedrig Kohlenstoff, schweißbar'
    },
    '1.4462': {
        name: 'X2CrNiMoN22-5-3',
        shortName: 'Duplex',
        group: 'Edelstahl',
        density: 7.80,
        pricePerKg: 9.00,
        machinabilityFactor: 1.2,
        hardness: '270 HB',
        tensileStrength: '640-880 MPa',
        cuttingSpeed: { rough: 60, finish: 90 },
        notes: 'Duplex-Stahl, hohe Festigkeit'
    },

    // === BAUSTAHL ===
    'S235': {
        name: 'S235JR',
        shortName: 'S235',
        group: 'Baustahl',
        density: 7.85,
        pricePerKg: 0.90,
        machinabilityFactor: 0.5,
        hardness: '120 HB',
        tensileStrength: '360-510 MPa',
        cuttingSpeed: { rough: 180, finish: 250 },
        notes: 'Standard-Baustahl'
    },
    'S355': {
        name: 'S355J2',
        shortName: 'S355',
        group: 'Baustahl',
        density: 7.85,
        pricePerKg: 1.20,
        machinabilityFactor: 0.55,
        hardness: '150 HB',
        tensileStrength: '470-630 MPa',
        cuttingSpeed: { rough: 160, finish: 220 },
        notes: 'Höherfester Baustahl'
    },

    // === VERGÜTUNGSSTAHL ===
    'C45': {
        name: 'C45E',
        shortName: 'C45',
        group: 'Vergütungsstahl',
        density: 7.85,
        pricePerKg: 1.80,
        machinabilityFactor: 0.65,
        hardness: '200 HB',
        tensileStrength: '560-850 MPa',
        cuttingSpeed: { rough: 140, finish: 200 },
        notes: 'Standard-Vergütungsstahl'
    },
    '42CrMo4': {
        name: '42CrMo4',
        shortName: '42CrMo4',
        group: 'Vergütungsstahl',
        density: 7.85,
        pricePerKg: 2.50,
        machinabilityFactor: 0.75,
        hardness: '250 HB',
        tensileStrength: '900-1100 MPa',
        cuttingSpeed: { rough: 100, finish: 150 },
        notes: 'Hochfest, für Maschinenbau'
    },
    '34CrNiMo6': {
        name: '34CrNiMo6',
        shortName: '34CrNiMo6',
        group: 'Vergütungsstahl',
        density: 7.85,
        pricePerKg: 3.20,
        machinabilityFactor: 0.8,
        hardness: '280 HB',
        tensileStrength: '1000-1200 MPa',
        cuttingSpeed: { rough: 90, finish: 130 },
        notes: 'Sehr hochfest, für Getriebe'
    },

    // === EINSATZSTAHL ===
    '16MnCr5': {
        name: '16MnCr5',
        shortName: '16MnCr5',
        group: 'Einsatzstahl',
        density: 7.85,
        pricePerKg: 2.20,
        machinabilityFactor: 0.6,
        hardness: '160 HB',
        tensileStrength: '500-800 MPa',
        cuttingSpeed: { rough: 150, finish: 210 },
        notes: 'Für Zahnräder, einsatzhärten'
    },
    '20MnCr5': {
        name: '20MnCr5',
        shortName: '20MnCr5',
        group: 'Einsatzstahl',
        density: 7.85,
        pricePerKg: 2.40,
        machinabilityFactor: 0.65,
        hardness: '170 HB',
        tensileStrength: '550-850 MPa',
        cuttingSpeed: { rough: 140, finish: 200 },
        notes: 'Für größere Zahnräder'
    },

    // === ALUMINIUM ===
    'AlMg3': {
        name: 'EN AW-5754',
        shortName: 'AlMg3',
        group: 'Aluminium',
        density: 2.66,
        pricePerKg: 4.50,
        machinabilityFactor: 0.35,
        hardness: '70 HB',
        tensileStrength: '190-240 MPa',
        cuttingSpeed: { rough: 400, finish: 600 },
        notes: 'Gute Korrosionsbeständigkeit, schweißbar'
    },
    'AlMgSi1': {
        name: 'EN AW-6082',
        shortName: 'AlMgSi1',
        group: 'Aluminium',
        density: 2.70,
        pricePerKg: 5.00,
        machinabilityFactor: 0.4,
        hardness: '95 HB',
        tensileStrength: '290-340 MPa',
        cuttingSpeed: { rough: 350, finish: 550 },
        notes: 'Gute Festigkeit, für Konstruktion'
    },
    'Al7075': {
        name: 'EN AW-7075',
        shortName: 'Al7075',
        group: 'Aluminium',
        density: 2.81,
        pricePerKg: 8.00,
        machinabilityFactor: 0.45,
        hardness: '150 HB',
        tensileStrength: '510-570 MPa',
        cuttingSpeed: { rough: 300, finish: 500 },
        notes: 'Hochfest, für Luftfahrt'
    },
    'Al2024': {
        name: 'EN AW-2024',
        shortName: 'Al2024',
        group: 'Aluminium',
        density: 2.78,
        pricePerKg: 7.50,
        machinabilityFactor: 0.45,
        hardness: '120 HB',
        tensileStrength: '440-490 MPa',
        cuttingSpeed: { rough: 320, finish: 520 },
        notes: 'Hochfest, für Luftfahrt'
    },

    // === KUPFERLEGIERUNGEN ===
    'CuZn39Pb3': {
        name: 'CuZn39Pb3',
        shortName: 'Ms58',
        group: 'Messing',
        density: 8.47,
        pricePerKg: 8.00,
        machinabilityFactor: 0.3,
        hardness: '100 HB',
        tensileStrength: '380-450 MPa',
        cuttingSpeed: { rough: 250, finish: 400 },
        notes: 'Automaten-Messing, beste Zerspanbarkeit'
    },
    'CuZn37': {
        name: 'CuZn37',
        shortName: 'Ms63',
        group: 'Messing',
        density: 8.44,
        pricePerKg: 9.00,
        machinabilityFactor: 0.4,
        hardness: '90 HB',
        tensileStrength: '300-400 MPa',
        cuttingSpeed: { rough: 220, finish: 350 },
        notes: 'Standard-Messing'
    },
    'CuSn8': {
        name: 'CuSn8',
        shortName: 'Bronze',
        group: 'Bronze',
        density: 8.80,
        pricePerKg: 12.00,
        machinabilityFactor: 0.5,
        hardness: '100 HB',
        tensileStrength: '300-400 MPa',
        cuttingSpeed: { rough: 180, finish: 280 },
        notes: 'Zinnbronze, für Gleitlager'
    },

    // === KUNSTSTOFFE ===
    'PA6': {
        name: 'Polyamid 6',
        shortName: 'PA6',
        group: 'Kunststoff',
        density: 1.14,
        pricePerKg: 6.00,
        machinabilityFactor: 0.25,
        hardness: '-',
        tensileStrength: '70-85 MPa',
        cuttingSpeed: { rough: 300, finish: 500 },
        notes: 'Technischer Kunststoff, gute Festigkeit'
    },
    'PA66': {
        name: 'Polyamid 66',
        shortName: 'PA66',
        group: 'Kunststoff',
        density: 1.14,
        pricePerKg: 7.00,
        machinabilityFactor: 0.25,
        hardness: '-',
        tensileStrength: '80-90 MPa',
        cuttingSpeed: { rough: 300, finish: 500 },
        notes: 'Höhere Steifigkeit als PA6'
    },
    'POM': {
        name: 'Polyoxymethylen',
        shortName: 'POM-C',
        group: 'Kunststoff',
        density: 1.41,
        pricePerKg: 5.50,
        machinabilityFactor: 0.2,
        hardness: '-',
        tensileStrength: '60-70 MPa',
        cuttingSpeed: { rough: 350, finish: 550 },
        notes: 'Beste Zerspanbarkeit, für Präzisionsteile'
    },
    'PEEK': {
        name: 'Polyetheretherketon',
        shortName: 'PEEK',
        group: 'Kunststoff',
        density: 1.32,
        pricePerKg: 80.00,
        machinabilityFactor: 0.35,
        hardness: '-',
        tensileStrength: '90-100 MPa',
        cuttingSpeed: { rough: 200, finish: 350 },
        notes: 'Hochtemperatur-Kunststoff, sehr teuer'
    },
    'PTFE': {
        name: 'Polytetrafluorethylen',
        shortName: 'Teflon',
        group: 'Kunststoff',
        density: 2.20,
        pricePerKg: 25.00,
        machinabilityFactor: 0.3,
        hardness: '-',
        tensileStrength: '20-35 MPa',
        cuttingSpeed: { rough: 250, finish: 400 },
        notes: 'Chemisch resistent, für Dichtungen'
    },

    // === TITAN ===
    'Ti6Al4V': {
        name: 'Ti-6Al-4V',
        shortName: 'Ti Grade 5',
        group: 'Titan',
        density: 4.43,
        pricePerKg: 35.00,
        machinabilityFactor: 1.5,
        hardness: '334 HB',
        tensileStrength: '895-1000 MPa',
        cuttingSpeed: { rough: 40, finish: 70 },
        notes: 'Hochfest, für Luftfahrt und Medizin'
    },
    'TiGr2': {
        name: 'Ti Grade 2',
        shortName: 'Ti Grade 2',
        group: 'Titan',
        density: 4.51,
        pricePerKg: 28.00,
        machinabilityFactor: 1.3,
        hardness: '200 HB',
        tensileStrength: '345-450 MPa',
        cuttingSpeed: { rough: 50, finish: 80 },
        notes: 'Reintitan, gute Korrosionsbeständigkeit'
    },

    // === GUSS ===
    'GG25': {
        name: 'EN-GJL-250',
        shortName: 'GG25',
        group: 'Gusseisen',
        density: 7.25,
        pricePerKg: 1.50,
        machinabilityFactor: 0.5,
        hardness: '180 HB',
        tensileStrength: '250 MPa',
        cuttingSpeed: { rough: 150, finish: 200 },
        notes: 'Grauguss, für Maschinenbetten'
    },
    'GGG40': {
        name: 'EN-GJS-400',
        shortName: 'GGG40',
        group: 'Gusseisen',
        density: 7.10,
        pricePerKg: 2.00,
        machinabilityFactor: 0.6,
        hardness: '150 HB',
        tensileStrength: '400 MPa',
        cuttingSpeed: { rough: 130, finish: 180 },
        notes: 'Sphäroguss, höhere Festigkeit'
    }
};

// Helper function to get material by key
function getMaterial(key) {
    return MATERIALS_DB[key] || null;
}

// Get all materials grouped
function getMaterialsGrouped() {
    const groups = {};
    Object.entries(MATERIALS_DB).forEach(([key, mat]) => {
        if (!groups[mat.group]) groups[mat.group] = [];
        groups[mat.group].push({ key, ...mat });
    });
    return groups;
}

// Calculate machining time factor based on material
function getMachiningFactor(materialKey) {
    const mat = MATERIALS_DB[materialKey];
    return mat ? mat.machinabilityFactor : 1.0;
}

// Export for use
if (typeof module !== 'undefined') {
    module.exports = { MATERIALS_DB, getMaterial, getMaterialsGrouped, getMachiningFactor };
}
