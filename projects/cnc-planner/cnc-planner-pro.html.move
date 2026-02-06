<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CNC Planer Pro</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
    <style>
        /* ================================================================
           CNC PLANER PRO v16 COMPLETE — DEMO READY
           All v15 features + Loading + Werkzeuge + Feedback
           ================================================================ */
        
        :root {
            /* Colors - Primary */
            --color-primary: #1E3A5F;
            --color-primary-hover: #152A45;
            --color-primary-light: #2D5A8A;
            
            /* Colors - Semantic */
            --color-success: #059669;
            --color-success-light: #D1FAE5;
            --color-warning: #D97706;
            --color-warning-light: #FEF3C7;
            --color-error: #DC2626;
            --color-error-light: #FEE2E2;
            --color-info: #2563EB;
            --color-info-light: #DBEAFE;
            
            /* Colors - Neutrals */
            --color-bg: #F8FAFC;
            --color-surface: #FFFFFF;
            --color-border: #E2E8F0;
            --color-border-light: #F1F5F9;
            
            /* Colors - Text */
            --color-text: #1E293B;
            --color-text-secondary: #64748B;
            --color-text-muted: #94A3B8;
            
            /* Typography */
            --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            --font-mono: 'JetBrains Mono', 'SF Mono', monospace;
            
            /* Spacing */
            --space-1: 4px;
            --space-2: 8px;
            --space-3: 12px;
            --space-4: 16px;
            --space-5: 20px;
            --space-6: 24px;
            --space-8: 32px;
            --space-10: 40px;
            
            /* Sizes */
            --sidebar-width: 260px;
            --header-height: 56px;
            --input-height: 40px;
            --btn-height: 36px;
            
            /* Radius */
            --radius-sm: 4px;
            --radius-md: 6px;
            --radius-lg: 8px;
            --radius-xl: 12px;
            
            /* Shadows */
            --shadow-sm: 0 1px 2px rgba(0,0,0,0.05);
            --shadow-md: 0 4px 6px rgba(0,0,0,0.07);
            --shadow-lg: 0 10px 15px rgba(0,0,0,0.1);
            
            /* Transitions */
            --transition-fast: 150ms ease;
            --transition-normal: 200ms ease;
        }
        
        /* Reset */
        *, *::before, *::after { margin: 0; padding: 0; box-sizing: border-box; }
        html, body { height: 100%; }
        
        body {
            font-family: var(--font-sans);
            font-size: 14px;
            line-height: 1.5;
            color: var(--color-text);
            background: var(--color-bg);
            -webkit-font-smoothing: antialiased;
        }
        
        /* ================================================================
           LAYOUT
           ================================================================ */
        
        .app { display: flex; min-height: 100vh; }
        
        /* Sidebar */
        .sidebar {
            width: var(--sidebar-width);
            height: 100vh;
            position: fixed;
            left: 0;
            top: 0;
            background: var(--color-surface);
            border-right: 1px solid var(--color-border);
            display: flex;
            flex-direction: column;
            z-index: 100;
        }
        
        .sidebar-header {
            height: var(--header-height);
            padding: 0 var(--space-4);
            display: flex;
            align-items: center;
            border-bottom: 1px solid var(--color-border);
        }
        
        .sidebar-logo {
            display: flex;
            align-items: center;
            gap: var(--space-3);
        }
        
        .sidebar-logo-icon {
            width: 32px;
            height: 32px;
            background: linear-gradient(135deg, var(--color-primary), var(--color-primary-light));
            border-radius: var(--radius-md);
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-weight: 700;
            font-size: 12px;
        }
        
        .sidebar-logo-text {
            font-size: 15px;
            font-weight: 600;
        }
        
        .sidebar-logo-text span {
            font-weight: 400;
            color: var(--color-text-secondary);
        }
        
        .sidebar-nav {
            flex: 1;
            overflow-y: auto;
            padding: var(--space-2);
        }
        
        .nav-section { margin-bottom: var(--space-6); }
        
        .nav-section-title {
            font-size: 11px;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            color: var(--color-text-muted);
            padding: var(--space-2) var(--space-3);
        }
        
        .nav-item {
            display: flex;
            align-items: center;
            gap: var(--space-2);
            padding: var(--space-2) var(--space-3);
            margin: 2px 0;
            border-radius: var(--radius-md);
            font-size: 14px;
            font-weight: 500;
            color: var(--color-text-secondary);
            cursor: pointer;
            transition: all var(--transition-fast);
            border: none;
            background: none;
            width: 100%;
            text-align: left;
        }
        
        .nav-item:hover { background: var(--color-bg); color: var(--color-text); }
        .nav-item.active { background: var(--color-primary); color: white; }
        
        .nav-item-icon {
            width: 20px;
            height: 20px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 16px;
        }
        
        .sidebar-footer {
            padding: var(--space-2);
            border-top: 1px solid var(--color-border);
        }
        
        /* Main */
        .main {
            flex: 1;
            margin-left: var(--sidebar-width);
            min-height: 100vh;
            display: flex;
            flex-direction: column;
        }
        
        .main-header {
            height: var(--header-height);
            padding: 0 var(--space-6);
            background: var(--color-surface);
            border-bottom: 1px solid var(--color-border);
            display: flex;
            align-items: center;
            justify-content: space-between;
            position: sticky;
            top: 0;
            z-index: 50;
        }
        
        .main-title { font-size: 16px; font-weight: 600; }
        .main-actions { display: flex; gap: var(--space-2); }
        
        .main-content {
            flex: 1;
            padding: var(--space-6);
            max-width: 1200px;
        }
        
        .section { display: none; }
        .section.active { display: block; }
        
        /* ================================================================
           COMPONENTS
           ================================================================ */
        
        /* Buttons */
        .btn {
            height: var(--btn-height);
            padding: 0 var(--space-4);
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: var(--space-2);
            font-size: 13px;
            font-weight: 500;
            font-family: inherit;
            border-radius: var(--radius-md);
            cursor: pointer;
            transition: all var(--transition-fast);
            border: none;
            white-space: nowrap;
        }
        
        .btn-primary { background: var(--color-primary); color: white; }
        .btn-primary:hover { background: var(--color-primary-hover); }
        .btn-secondary { background: var(--color-surface); color: var(--color-text); border: 1px solid var(--color-border); }
        .btn-secondary:hover { background: var(--color-bg); }
        .btn-sm { height: 32px; padding: 0 var(--space-3); font-size: 12px; }
        
        /* Form Elements */
        .form-group { margin-bottom: var(--space-4); }
        
        .form-label {
            display: block;
            font-size: 13px;
            font-weight: 500;
            color: var(--color-text-secondary);
            margin-bottom: var(--space-1);
        }
        
        .form-label-caps {
            font-size: 11px;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            color: var(--color-text-muted);
        }
        
        .input {
            height: var(--input-height);
            width: 100%;
            padding: 0 var(--space-3);
            font-size: 14px;
            font-family: inherit;
            color: var(--color-text);
            background: var(--color-surface);
            border: 1px solid var(--color-border);
            border-radius: var(--radius-md);
            transition: all var(--transition-fast);
        }
        
        .input:hover { border-color: var(--color-text-muted); }
        .input:focus { outline: none; border-color: var(--color-primary); box-shadow: 0 0 0 3px rgba(30, 58, 95, 0.1); }
        .input-mono { font-family: var(--font-mono); text-align: right; }
        .input-sm { height: 32px; font-size: 13px; }
        
        .select {
            height: var(--input-height);
            width: 100%;
            padding: 0 var(--space-8) 0 var(--space-3);
            font-size: 14px;
            font-family: inherit;
            color: var(--color-text);
            background: var(--color-surface);
            border: 1px solid var(--color-border);
            border-radius: var(--radius-md);
            cursor: pointer;
            appearance: none;
            background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 24 24' fill='none' stroke='%2364748B' stroke-width='2'%3E%3Cpolyline points='6 9 12 15 18 9'/%3E%3C/svg%3E");
            background-repeat: no-repeat;
            background-position: right 12px center;
        }
        
        .input-with-unit { position: relative; display: inline-flex; width: 100%; }
        .input-with-unit .input { padding-right: var(--space-10); }
        .input-unit {
            position: absolute;
            right: var(--space-3);
            top: 50%;
            transform: translateY(-50%);
            font-size: 13px;
            color: var(--color-text-muted);
            pointer-events: none;
        }
        
        .checkbox-group { display: flex; align-items: center; gap: var(--space-2); }
        .checkbox { width: 18px; height: 18px; accent-color: var(--color-primary); cursor: pointer; }
        .checkbox-label { font-size: 14px; cursor: pointer; }
        
        /* Cards */
        .card {
            background: var(--color-surface);
            border: 1px solid var(--color-border);
            border-radius: var(--radius-lg);
            overflow: hidden;
        }
        
        .card-header {
            padding: var(--space-4) var(--space-5);
            border-bottom: 1px solid var(--color-border-light);
            font-size: 14px;
            font-weight: 600;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .card-header-primary {
            background: var(--color-primary);
            color: white;
            border-bottom: none;
        }
        
        .card-header-info {
            background: var(--color-info-light);
            color: var(--color-info);
        }
        
        .card-header-success {
            background: var(--color-success-light);
            color: var(--color-success);
        }
        
        .card-header-warning {
            background: var(--color-warning-light);
            color: var(--color-warning);
        }
        
        .card-header-error {
            background: var(--color-error-light);
            color: var(--color-error);
        }
        
        .card-header-icon { margin-right: var(--space-2); }
        .card-header-action { font-size: 12px; font-weight: 400; opacity: 0.8; }
        .card-header-title { flex: 1; }
        
        .card-body { padding: var(--space-5); }
        
        /* Price Hero */
        .price-hero {
            background: linear-gradient(135deg, var(--color-primary), var(--color-primary-light));
            color: white;
            padding: var(--space-8);
            border-radius: var(--radius-xl);
            text-align: center;
            margin-bottom: var(--space-6);
            position: relative;
        }
        
        .price-label { font-size: 14px; font-weight: 500; opacity: 0.85; margin-bottom: var(--space-1); }
        .price-value { font-size: 48px; font-weight: 700; font-family: var(--font-mono); letter-spacing: -0.02em; line-height: 1.1; }
        .price-detail { font-size: 13px; opacity: 0.7; margin-top: var(--space-2); }
        
        /* Confidence Badge */
        .confidence-badge {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            padding: 6px 12px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 600;
            margin-top: var(--space-3);
        }
        
        .confidence-high { background: rgba(5, 150, 105, 0.2); color: #D1FAE5; }
        .confidence-medium { background: rgba(217, 119, 6, 0.2); color: #FEF3C7; }
        .confidence-low { background: rgba(220, 38, 38, 0.2); color: #FEE2E2; }
        
        /* Cost Breakdown */
        .cost-breakdown {
            background: var(--color-surface);
            border: 1px solid var(--color-border);
            border-radius: var(--radius-lg);
            overflow: hidden;
        }
        
        .cost-row {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            padding: var(--space-3) var(--space-4);
            border-bottom: 1px solid var(--color-border-light);
        }
        
        .cost-row:last-child { border-bottom: none; }
        .cost-label { font-size: 14px; color: var(--color-text-secondary); }
        
        .cost-formula {
            font-size: 12px;
            color: var(--color-text-muted);
            font-family: var(--font-mono);
            margin-top: 2px;
            cursor: help;
        }
        
        .cost-value {
            font-size: 14px;
            font-weight: 500;
            font-family: var(--font-mono);
            text-align: right;
        }
        
        .cost-row.subtotal { background: var(--color-bg); }
        .cost-row.subtotal .cost-label, .cost-row.subtotal .cost-value { font-weight: 600; }
        .cost-row.total { background: var(--color-primary); }
        .cost-row.total .cost-label, .cost-row.total .cost-value { color: white; font-weight: 600; }
        
        /* Part Cards */
        .part-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: var(--space-4);
            margin-bottom: var(--space-6);
        }
        
        .part-card {
            display: flex;
            gap: var(--space-4);
            padding: var(--space-4);
            background: var(--color-surface);
            border: 2px solid var(--color-border);
            border-radius: var(--radius-lg);
            cursor: pointer;
            transition: all var(--transition-fast);
        }
        
        .part-card:hover { border-color: var(--color-primary-light); }
        .part-card.selected { border-color: var(--color-primary); background: linear-gradient(135deg, rgba(30, 58, 95, 0.02), rgba(45, 90, 138, 0.02)); }
        
        .part-thumb {
            width: 80px;
            height: 80px;
            flex-shrink: 0;
            background: var(--color-bg);
            border-radius: var(--radius-md);
            border: 1px solid var(--color-border);
            overflow: hidden;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        
        .part-thumb img { width: 100%; height: 100%; object-fit: contain; }
        .part-info { flex: 1; min-width: 0; }
        .part-name { font-size: 14px; font-weight: 600; margin-bottom: 2px; }
        .part-number { font-size: 12px; font-family: var(--font-mono); color: var(--color-text-muted); margin-bottom: var(--space-2); }
        .part-meta { display: flex; gap: var(--space-3); font-size: 13px; color: var(--color-text-secondary); }
        .part-price { font-weight: 600; color: var(--color-primary); }
        
        /* Info Box */
        .info-box {
            background: var(--color-bg);
            border-left: 3px solid var(--color-primary);
            padding: var(--space-4);
            border-radius: 0 var(--radius-md) var(--radius-md) 0;
            font-size: 13px;
            color: var(--color-text-secondary);
            line-height: 1.6;
        }
        
        .info-box strong { color: var(--color-text); }
        
        .warning-box {
            background: var(--color-warning-light);
            border-left: 3px solid var(--color-warning);
            padding: var(--space-4);
            border-radius: 0 var(--radius-md) var(--radius-md) 0;
            font-size: 13px;
        }
        
        .warning-box strong { color: var(--color-warning); }
        
        /* Trust Badges */
        .trust-badges {
            display: flex;
            justify-content: center;
            gap: var(--space-8);
            margin-bottom: var(--space-6);
            flex-wrap: wrap;
        }
        
        .trust-badge {
            display: flex;
            align-items: center;
            gap: var(--space-2);
            color: var(--color-text-secondary);
            font-size: 13px;
        }
        
        .trust-badge svg { width: 18px; height: 18px; stroke: var(--color-text-muted); }
        
        /* Scope Notice */
        .scope-notice {
            background: var(--color-surface);
            border: 1px solid var(--color-border);
            border-radius: var(--radius-lg);
            margin-bottom: var(--space-6);
            overflow: hidden;
        }
        
        .scope-header {
            padding: var(--space-4) var(--space-5);
            cursor: pointer;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .scope-header:hover { background: var(--color-bg); }
        
        .scope-content {
            display: none;
            padding: var(--space-5);
            border-top: 1px solid var(--color-border);
            background: var(--color-bg);
        }
        
        .scope-content.expanded { display: block; }
        
        /* Grid Layouts */
        .grid-2 { display: grid; grid-template-columns: repeat(2, 1fr); gap: var(--space-5); }
        .grid-3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: var(--space-4); }
        .grid-4 { display: grid; grid-template-columns: repeat(4, 1fr); gap: var(--space-4); }
        
        .dimension-group { display: flex; align-items: flex-end; gap: var(--space-2); }
        .dimension-group .form-group { flex: 1; margin-bottom: 0; }
        .dimension-separator { padding-bottom: 10px; color: var(--color-text-muted); font-size: 16px; }
        
        /* Tables */
        .table { width: 100%; border-collapse: collapse; font-size: 13px; }
        
        .table th {
            padding: var(--space-3) var(--space-4);
            text-align: left;
            font-size: 11px;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            color: var(--color-text-muted);
            background: var(--color-bg);
            border-bottom: 1px solid var(--color-border);
        }
        
        .table td {
            padding: var(--space-3) var(--space-4);
            border-bottom: 1px solid var(--color-border-light);
            vertical-align: middle;
        }
        
        .table tr:last-child td { border-bottom: none; }
        .table .mono { font-family: var(--font-mono); }
        .table .right { text-align: right; }
        
        /* Live Results */
        .live-results {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: var(--space-4);
            padding: var(--space-5);
            background: var(--color-bg);
            border-radius: var(--radius-lg);
            border: 1px solid var(--color-border);
            margin-bottom: var(--space-5);
        }
        
        .live-result-item { text-align: center; }
        .live-result-label { font-size: 11px; text-transform: uppercase; letter-spacing: 0.05em; color: var(--color-text-muted); margin-bottom: var(--space-1); }
        .live-result-value { font-size: 20px; font-weight: 700; font-family: var(--font-mono); color: var(--color-primary); }
        
        /* Code Block */
        .code-block {
            background: #0F172A;
            border-radius: var(--radius-lg);
            padding: var(--space-5);
            overflow-x: auto;
            max-height: 400px;
            overflow-y: auto;
        }
        
        .code-block pre {
            margin: 0;
            font-family: var(--font-mono);
            font-size: 13px;
            line-height: 1.6;
            color: #E2E8F0;
            white-space: pre-wrap;
        }
        
        .code-comment { color: #64748B; }
        .code-keyword { color: #F59E0B; }
        .code-number { color: #10B981; }
        
        /* Badges */
        .badge {
            display: inline-flex;
            align-items: center;
            padding: 2px 8px;
            font-size: 11px;
            font-weight: 500;
            border-radius: var(--radius-sm);
        }
        
        .badge-success { background: var(--color-success-light); color: var(--color-success); }
        .badge-warning { background: var(--color-warning-light); color: var(--color-warning); }
        .badge-error { background: var(--color-error-light); color: var(--color-error); }
        .badge-info { background: var(--color-info-light); color: var(--color-info); }
        
        /* Instruction Sections */
        .instruction-section {
            background: var(--color-surface);
            border: 1px solid var(--color-border);
            border-radius: var(--radius-lg);
            margin-bottom: var(--space-4);
            overflow: hidden;
        }
        
        .instruction-section.critical { border-color: var(--color-error); }
        
        .instruction-header {
            background: var(--color-bg);
            padding: var(--space-4) var(--space-5);
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid var(--color-border);
        }
        
        .instruction-header.critical { background: var(--color-error-light); }
        
        .instruction-header h4 {
            font-size: 14px;
            font-weight: 600;
            display: flex;
            align-items: center;
            gap: var(--space-2);
        }
        
        .op-badge {
            background: var(--color-primary);
            color: white;
            padding: 2px 8px;
            border-radius: var(--radius-sm);
            font-size: 11px;
            font-weight: 600;
        }
        
        .op-badge.critical { background: var(--color-error); }
        
        .instruction-content { padding: var(--space-5); }
        
        .params-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: var(--space-3);
            margin-bottom: var(--space-4);
        }
        
        .param-item {
            background: var(--color-bg);
            padding: var(--space-3);
            border-radius: var(--radius-md);
            text-align: center;
            border: 1px solid var(--color-border);
        }
        
        .param-item.critical { border-color: var(--color-error); }
        .param-label { font-size: 11px; color: var(--color-text-muted); text-transform: uppercase; letter-spacing: 0.05em; }
        .param-value { font-size: 14px; font-weight: 600; font-family: var(--font-mono); }
        .param-value.critical { color: var(--color-error); }
        
        .tips-list { list-style: none; }
        
        .tips-list li {
            padding: var(--space-2) 0;
            font-size: 13px;
            color: var(--color-text-secondary);
            display: flex;
            align-items: flex-start;
            gap: var(--space-2);
            border-bottom: 1px solid var(--color-border-light);
        }
        
        .tips-list li:last-child { border-bottom: none; }
        
        .tip-icon {
            flex-shrink: 0;
            width: 20px;
            height: 20px;
            background: var(--color-bg);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 11px;
        }
        
        .tip-icon.success { background: var(--color-success-light); color: var(--color-success); }
        .tip-icon.warning { background: var(--color-warning-light); color: var(--color-warning); }
        .tip-icon.danger { background: var(--color-error-light); color: var(--color-error); }
        
        /* Tooltip */
        .tooltip {
            position: relative;
            cursor: help;
        }
        
        .tooltip::after {
            content: attr(data-tooltip);
            position: absolute;
            bottom: 100%;
            left: 50%;
            transform: translateX(-50%);
            padding: 8px 12px;
            background: var(--color-text);
            color: white;
            font-size: 12px;
            border-radius: var(--radius-md);
            white-space: nowrap;
            opacity: 0;
            visibility: hidden;
            transition: all var(--transition-fast);
            z-index: 100;
        }
        
        .tooltip:hover::after { opacity: 1; visibility: visible; }
        
        /* Loading Animation */
        .loading-overlay {
            position: fixed;
            top: 0;
            left: var(--sidebar-width);
            right: 0;
            bottom: 0;
            background: rgba(248, 250, 252, 0.95);
            display: none;
            align-items: center;
            justify-content: center;
            z-index: 1000;
            flex-direction: column;
            gap: var(--space-6);
        }
        
        .loading-overlay.active { display: flex; }
        
        .loading-spinner {
            width: 48px;
            height: 48px;
            border: 3px solid var(--color-border);
            border-top-color: var(--color-primary);
            border-radius: 50%;
            animation: spin 1s linear infinite;
        }
        
        @keyframes spin { to { transform: rotate(360deg); } }
        
        .loading-steps {
            display: flex;
            flex-direction: column;
            gap: var(--space-3);
        }
        
        .loading-step {
            display: flex;
            align-items: center;
            gap: var(--space-3);
            padding: var(--space-2) var(--space-4);
            font-size: 14px;
            color: var(--color-text-muted);
            transition: all var(--transition-normal);
        }
        
        .loading-step.active { color: var(--color-primary); font-weight: 500; }
        .loading-step.done { color: var(--color-success); }
        
        .loading-step-icon {
            width: 20px;
            height: 20px;
            border-radius: 50%;
            border: 2px solid currentColor;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 12px;
        }
        
        .loading-step.done .loading-step-icon {
            background: var(--color-success);
            border-color: var(--color-success);
            color: white;
        }
        
        /* Feedback Section */
        .feedback-card {
            background: var(--color-bg);
            border: 1px solid var(--color-border);
            border-radius: var(--radius-lg);
            padding: var(--space-5);
        }
        
        .feedback-options {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: var(--space-3);
            margin-bottom: var(--space-4);
        }
        
        .feedback-option {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: var(--space-2);
            padding: var(--space-4);
            background: var(--color-surface);
            border: 2px solid var(--color-border);
            border-radius: var(--radius-md);
            cursor: pointer;
            transition: all var(--transition-fast);
        }
        
        .feedback-option:hover { border-color: var(--color-primary-light); }
        .feedback-option.selected { border-color: var(--color-primary); background: linear-gradient(135deg, rgba(30, 58, 95, 0.05), rgba(45, 90, 138, 0.05)); }
        
        .feedback-option-icon { font-size: 24px; }
        .feedback-option-label { font-size: 13px; font-weight: 500; }
        
        /* Responsive */
        @media (max-width: 768px) {
            .sidebar { display: none; }
            .main { margin-left: 0; }
            .grid-2, .grid-3, .grid-4 { grid-template-columns: 1fr; }
            .part-grid { grid-template-columns: 1fr; }
            .live-results { grid-template-columns: repeat(2, 1fr); }
            .params-grid { grid-template-columns: repeat(2, 1fr); }
            .price-value { font-size: 36px; }
        }
    </style>
</head>
<body>
    <!-- Loading Overlay -->
    <div class="loading-overlay" id="loadingOverlay">
        <div class="loading-spinner"></div>
        <div style="font-size: 16px; font-weight: 500; color: var(--color-text);">Generiere Unterlagen...</div>
        <div class="loading-steps">
            <div class="loading-step" id="loadStep1">
                <span class="loading-step-icon">1</span>
                <span>Geometrie analysieren</span>
            </div>
            <div class="loading-step" id="loadStep2">
                <span class="loading-step-icon">2</span>
                <span>Bearbeitungszeiten berechnen</span>
            </div>
            <div class="loading-step" id="loadStep3">
                <span class="loading-step-icon">3</span>
                <span>Werkzeugkosten kalkulieren</span>
            </div>
            <div class="loading-step" id="loadStep4">
                <span class="loading-step-icon">4</span>
                <span>Maschinencode generieren</span>
            </div>
            <div class="loading-step" id="loadStep5">
                <span class="loading-step-icon">5</span>
                <span>Fertigungsanweisung erstellen</span>
            </div>
        </div>
    </div>
    
    <div class="app">
        <!-- SIDEBAR -->
        <aside class="sidebar">
            <div class="sidebar-header">
                <div class="sidebar-logo">
                    <div class="sidebar-logo-icon">CP</div>
                    <div class="sidebar-logo-text">CNC Planer <span>Pro</span></div>
                    <span style="background: var(--color-warning); color: white; font-size: 9px; padding: 2px 6px; border-radius: 3px; margin-left: 8px; font-weight: 600;">BETA</span>
                </div>
            </div>
            
            <nav class="sidebar-nav">
                <div class="nav-section">
                    <div class="nav-section-title">Eingabe</div>
                    <button class="nav-item active" data-section="part" onclick="showSection('part', this)">
                        <span>Teil</span>
                    </button>
                    <button class="nav-item" data-section="params" onclick="showSection('params', this)">
                        <span>Parameter</span>
                    </button>
                </div>
                
                <div class="nav-section">
                    <div class="nav-section-title">Ergebnis</div>
                    <button class="nav-item" data-section="result" onclick="showSection('result', this)">
                        <span>Kalkulation</span>
                    </button>
                    <button class="nav-item" data-section="instructions" onclick="showSection('instructions', this)">
                        <span>Fertigungsanweisung</span>
                    </button>
                    <button class="nav-item" data-section="quote" onclick="showSection('quote', this)">
                        <span>Angebot</span>
                    </button>
                    <button class="nav-item" data-section="code" onclick="showSection('code', this)">
                        <span>NC-Code</span>
                    </button>
                </div>
            </nav>
            
            <div class="sidebar-footer">
                <button class="nav-item" data-section="feedback" onclick="showSection('feedback', this)">
                    <span>Feedback</span>
                </button>
                <button class="nav-item" data-section="settings" onclick="showSection('settings', this)">
                    <span>Einstellungen</span>
                </button>
            </div>
        </aside>
        
        <!-- MAIN CONTENT -->
        <main class="main">
            <header class="main-header">
                <h1 class="main-title" id="mainTitle">Teil</h1>
                <div class="main-actions">
                    <button class="btn btn-secondary btn-sm" onclick="exportCSV()">CSV</button>
                    <button class="btn btn-primary btn-sm" onclick="window.print()">PDF Export</button>
                </div>
            </header>
            
            <div class="main-content">
                <!-- ========================================
                     SECTION: TEIL AUSWÄHLEN
                     ======================================== -->
                <div class="section active" id="section-part">
                    <!-- Trust Badges -->
                    <div class="trust-badges">
                        <div class="trust-badge">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><polyline points="9,12 12,15 16,10"/></svg>
                            Basierend auf echten Betriebsdaten
                        </div>
                        <div class="trust-badge">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>
                            Kalkulation in &lt;30 Sekunden
                        </div>
                        <div class="trust-badge">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14,2 14,8 20,8"/></svg>
                            NC-Code inklusive
                        </div>
                    </div>
                    
                    <!-- Scope Notice -->
                    <div class="scope-notice">
                        <div class="scope-header" onclick="toggleScope()">
                            <div>
                                <div style="font-weight: 600; color: var(--color-text);">Funktionsprinzip und Anwendungsbereich</div>
                                <div style="font-size: 12px; color: var(--color-text-muted);">Klicken für Details zu Grenzen und Anpassungsmöglichkeiten</div>
                            </div>
                            <svg id="scopeChevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--color-text-muted)" stroke-width="2" style="transition: transform 0.2s;"><polyline points="6 9 12 15 18 9"/></svg>
                        </div>
                        <div class="scope-content" id="scopeContent">
                            <div class="grid-2" style="margin-bottom: var(--space-4);">
                                <div>
                                    <div style="font-weight: 600; margin-bottom: var(--space-2);">Geeignet für</div>
                                    <ul style="font-size: 13px; color: var(--color-text-secondary); padding-left: var(--space-4);">
                                        <li>Prismatische Teile (Platten, Blöcke)</li>
                                        <li>Standardbohrungen, Senkungen</li>
                                        <li>Einfache Taschen und Konturen</li>
                                        <li>3-Achs-Bearbeitung</li>
                                        <li>Stahl, Edelstahl, Aluminium, Kunststoff</li>
                                    </ul>
                                </div>
                                <div>
                                    <div style="font-weight: 600; margin-bottom: var(--space-2);">Nicht geeignet für</div>
                                    <ul style="font-size: 13px; color: var(--color-text-secondary); padding-left: var(--space-4);">
                                        <li>Komplexe 3D-Freiformflächen</li>
                                        <li>5-Achs-Simultanbearbeitung</li>
                                        <li>Sonderwerkstoffe (Titan, Inconel)</li>
                                        <li>Toleranzen besser als IT8</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="info-box">
                                <strong>Berechnungsprinzip:</strong> Die Kalkulation basiert auf einer Referenzmaschine (3-Achs Hermle) mit validierten Stundensätzen aus echten Fertigungsaufträgen.<br>
                                <strong>Erwartete Genauigkeit:</strong> ±15% für Standardteile
                            </div>
                        </div>
                    </div>
                    
                    <!-- Part Selection -->
                    <div style="font-weight: 600; margin-bottom: var(--space-3);">Letzte analysierte Bauteile</div>
                    <div class="part-grid" id="partGrid">
                        <!-- Filled by JS -->
                    </div>
                    
                    <!-- File Upload -->
                    <div class="card" style="margin-bottom: var(--space-6);">
                        <div class="card-body" style="text-align: center; padding: var(--space-8);">
                            <div style="font-size: 32px; margin-bottom: var(--space-3); color: var(--color-text-muted);">📁</div>
                            <div style="font-weight: 600; margin-bottom: var(--space-2);">Neues Bauteil analysieren</div>
                            <div style="font-size: 13px; color: var(--color-text-muted); margin-bottom: var(--space-4);">STEP-Datei hochladen oder hier ablegen • .step, .stp, .pdf</div>
                            <input type="file" id="fileInput" accept=".step,.stp,.pdf" style="display: none;">
                            <button class="btn btn-secondary" onclick="document.getElementById('fileInput').click()">Datei auswählen</button>
                        </div>
                    </div>
                    
                    <!-- Werkstück -->
                    <div class="card" style="margin-bottom: var(--space-6);">
                        <div class="card-header"><span>Werkstück</span></div>
                        <div class="card-body">
                            <div class="form-group">
                                <label class="form-label">Werkstoff</label>
                                <select class="select" id="materialSelect" onchange="calculate()">
                                    <optgroup label="Edelstahl">
                                        <option value="1.4301">1.4301 (V2A)</option>
                                        <option value="1.4404">1.4404 (V4A)</option>
                                        <option value="1.4571">1.4571</option>
                                    </optgroup>
                                    <optgroup label="Baustahl">
                                        <option value="S235JR" selected>S235JR</option>
                                        <option value="S355J2">S355J2</option>
                                        <option value="C45">C45</option>
                                    </optgroup>
                                    <optgroup label="Vergütungsstahl">
                                        <option value="42CrMo4">42CrMo4</option>
                                        <option value="34CrNiMo6">34CrNiMo6</option>
                                    </optgroup>
                                    <optgroup label="Aluminium">
                                        <option value="AlMg3">AlMg3</option>
                                        <option value="AlMgSi1">AlMgSi1 (6082)</option>
                                        <option value="Al7075">Al7075-T6</option>
                                    </optgroup>
                                    <optgroup label="Buntmetalle">
                                        <option value="CuZn39Pb3">Messing CuZn39Pb3</option>
                                        <option value="CuSn8">Bronze CuSn8</option>
                                    </optgroup>
                                    <optgroup label="Kunststoff">
                                        <option value="POM">POM</option>
                                        <option value="PA6">PA6 (Nylon)</option>
                                        <option value="PEEK">PEEK</option>
                                    </optgroup>
                                </select>
                            </div>
                            
                            <div class="form-group">
                                <label class="form-label">Rohmaße</label>
                                <div class="dimension-group">
                                    <div class="form-group">
                                        <div class="input-with-unit">
                                            <input type="number" class="input input-mono" id="dimX" value="440" oninput="calculate()">
                                            <span class="input-unit">mm</span>
                                        </div>
                                    </div>
                                    <span class="dimension-separator">×</span>
                                    <div class="form-group">
                                        <div class="input-with-unit">
                                            <input type="number" class="input input-mono" id="dimY" value="50" oninput="calculate()">
                                            <span class="input-unit">mm</span>
                                        </div>
                                    </div>
                                    <span class="dimension-separator">×</span>
                                    <div class="form-group">
                                        <div class="input-with-unit">
                                            <input type="number" class="input input-mono" id="dimZ" value="20" oninput="calculate()">
                                            <span class="input-unit">mm</span>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            
                            <div class="form-group">
                                <label class="form-label">Stückzahl</label>
                                <div class="input-with-unit" style="width: 120px;">
                                    <input type="number" class="input input-mono" id="quantity" value="1" min="1" oninput="calculate()">
                                    <span class="input-unit">Stk</span>
                                </div>
                            </div>
                            
                            <!-- Action Buttons -->
                            <div style="display: flex; gap: var(--space-3); margin-top: var(--space-5); padding-top: var(--space-4); border-top: 1px solid var(--color-border);">
                                <button class="btn btn-secondary" onclick="calculate()" style="flex: 1;">
                                    Analysieren
                                </button>
                                <button class="btn btn-primary" onclick="confirmAndGoToParams()" style="flex: 1;">
                                    Weiter zu Parameter
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
                
                <!-- ========================================
                     SECTION: PARAMETER
                     ======================================== -->
                <div class="section" id="section-params">
                    <div style="display: flex; gap: var(--space-2); margin-bottom: var(--space-5); border-bottom: 1px solid var(--color-border); padding-bottom: var(--space-3);">
                        <button class="btn btn-sm btn-primary" id="tabParamFertigung" onclick="showParamTab('fertigung')">Fertigung</button>
                        <button class="btn btn-sm btn-secondary" id="tabParamPreis" onclick="showParamTab('preis')">Preisangaben</button>
                        <button class="btn btn-sm btn-secondary" id="tabParamMaschine" onclick="showParamTab('maschine')">Maschine</button>
                    </div>
                    
                    <div id="param-fertigung">
                        <div class="card" style="margin-bottom: var(--space-6);">
                            <div class="card-header"><span>Fertigung</span></div>
                            <div class="card-body">
                                <div class="form-group">
                                    <label class="form-label">Spannung</label>
                                    <select class="select" id="clampingSelect" onchange="calculate()">
                                        <option value="schraubstock">Schraubstock (15 min)</option>
                                        <option value="schraubstock2">2× Schraubstock (25 min)</option>
                                        <option value="tischspannung">Tischspannung (35 min)</option>
                                        <option value="nullpunkt">Nullpunktspannsystem (5 min)</option>
                                        <option value="spezial">Sondervorrichtung (45 min)</option>
                                    </select>
                                </div>
                                
                                <div class="form-group">
                                    <label class="form-label">Aufspannungen</label>
                                    <select class="select" id="setupCount" onchange="calculate()">
                                        <option value="1">1 Aufspannung</option>
                                        <option value="2" selected>2 Aufspannungen</option>
                                        <option value="3">3 Aufspannungen</option>
                                        <option value="4">4+ Aufspannungen</option>
                                    </select>
                                </div>
                                
                                <!-- Einrichtzeit Info -->
                                <div class="info-box" style="margin-bottom: var(--space-4);">
                                    <strong>Einrichtzeit:</strong> <span id="setupTimeDisplay">25 min</span> = <span id="setupCostDisplay">€37,92</span><br>
                                    <span id="clampingDescription" style="font-size: 12px;">Schraubstock: Teil spannen, Parallelität prüfen, Nullpunkt antasten.</span>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <div id="param-preis" style="display: none;">
                        <div class="card" style="margin-bottom: var(--space-5);">
                            <div class="card-header card-header-info"><span>Maschinenstundensätze (€/h)</span></div>
                            <div class="card-body" style="padding: 0; overflow-x: auto;">
                                <table class="table">
                                    <thead>
                                        <tr>
                                            <th>Arbeitsgang</th>
                                            <th class="right">Lohn (€/h)</th>
                                            <th class="right">Maschine (€/h)</th>
                                            <th class="right">Gesamt (€/h)</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr>
                                            <td><strong>CNC-Fräsen (3-Achs)</strong></td>
                                            <td class="right"><input type="number" class="input input-sm input-mono" value="49" id="rateCncLabor" style="width: 80px;" onchange="updateRates()"></td>
                                            <td class="right"><input type="number" class="input input-sm input-mono" value="42" id="rateCncMachine" style="width: 80px;" onchange="updateRates()"></td>
                                            <td class="right mono" style="font-weight: 600;" id="rateCncTotal">€91</td>
                                        </tr>
                                        <tr>
                                            <td>CNC-Fräsen (5-Achs)</td>
                                            <td class="right"><input type="number" class="input input-sm input-mono" value="52" id="rate5AxLabor" style="width: 80px;" onchange="updateRates()"></td>
                                            <td class="right"><input type="number" class="input input-sm input-mono" value="68" id="rate5AxMachine" style="width: 80px;" onchange="updateRates()"></td>
                                            <td class="right mono" id="rate5AxTotal">€120</td>
                                        </tr>
                                        <tr>
                                            <td>CNC-Drehen</td>
                                            <td class="right"><input type="number" class="input input-sm input-mono" value="45" id="rateDrehenLabor" style="width: 80px;" onchange="updateRates()"></td>
                                            <td class="right"><input type="number" class="input input-sm input-mono" value="38" id="rateDrehenMachine" style="width: 80px;" onchange="updateRates()"></td>
                                            <td class="right mono" id="rateDrehenTotal">€83</td>
                                        </tr>
                                        <tr>
                                            <td>Sägen</td>
                                            <td class="right"><input type="number" class="input input-sm input-mono" value="43" id="rateSaegenLabor" style="width: 80px;" onchange="updateRates()"></td>
                                            <td class="right"><input type="number" class="input input-sm input-mono" value="12" id="rateSaegenMachine" style="width: 80px;" onchange="updateRates()"></td>
                                            <td class="right mono" id="rateSaegenTotal">€55</td>
                                        </tr>
                                        <tr>
                                            <td>Entgraten / Schleifen</td>
                                            <td class="right"><input type="number" class="input input-sm input-mono" value="32" id="rateEntgratenLabor" style="width: 80px;" onchange="updateRates()"></td>
                                            <td class="right"><input type="number" class="input input-sm input-mono" value="4" id="rateEntgratenMachine" style="width: 80px;" onchange="updateRates()"></td>
                                            <td class="right mono" id="rateEntgratenTotal">€36</td>
                                        </tr>
                                        <tr>
                                            <td>Qualitätsprüfung</td>
                                            <td class="right"><input type="number" class="input input-sm input-mono" value="45" id="ratePruefLabor" style="width: 80px;" onchange="updateRates()"></td>
                                            <td class="right"><input type="number" class="input input-sm input-mono" value="15" id="ratePruefMachine" style="width: 80px;" onchange="updateRates()"></td>
                                            <td class="right mono" id="ratePruefTotal">€60</td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                        </div>
                        
                        <div class="info-box" style="margin-bottom: var(--space-5);">
                            <strong>Hinweis:</strong> Maschinenstundensatz = Lohnkosten + Maschinenkosten (Abschreibung, Energie, Wartung, Raumkosten). Branchenüblich: €65-95/h für 3-Achs, €90-140/h für 5-Achs.
                        </div>
                        
                        <div class="card" style="margin-bottom: var(--space-5);">
                            <div class="card-header card-header-success"><span>📦 Materialpreise (€/kg)</span></div>
                            <div class="card-body">
                                <div style="font-size: 12px; color: var(--color-text-muted); margin-bottom: var(--space-4);">
                                    Tagesaktuelle Preise vom Stahlhandel übernehmen. Verschnitt wird separat berechnet.
                                </div>
                                
                                <div style="font-weight: 600; margin-bottom: var(--space-2); color: var(--color-text-secondary);">Baustahl</div>
                                <div class="grid-4" style="gap: var(--space-3); margin-bottom: var(--space-4);">
                                    <div class="form-group" style="margin-bottom: 0;">
                                        <label class="form-label form-label-caps">S235JR</label>
                                        <div class="input-with-unit">
                                            <input type="number" class="input input-sm input-mono" value="6.79" step="0.01" id="matS235JR" onchange="updateMaterials()">
                                            <span class="input-unit">€/kg</span>
                                        </div>
                                    </div>
                                    <div class="form-group" style="margin-bottom: 0;">
                                        <label class="form-label form-label-caps">S355J2</label>
                                        <div class="input-with-unit">
                                            <input type="number" class="input input-sm input-mono" value="7.50" step="0.01" id="matS355J2" onchange="updateMaterials()">
                                            <span class="input-unit">€/kg</span>
                                        </div>
                                    </div>
                                    <div class="form-group" style="margin-bottom: 0;">
                                        <label class="form-label form-label-caps">C45</label>
                                        <div class="input-with-unit">
                                            <input type="number" class="input input-sm input-mono" value="3.50" step="0.01" id="matC45" onchange="updateMaterials()">
                                            <span class="input-unit">€/kg</span>
                                        </div>
                                    </div>
                                    <div class="form-group" style="margin-bottom: 0;">
                                        <label class="form-label form-label-caps">42CrMo4</label>
                                        <div class="input-with-unit">
                                            <input type="number" class="input input-sm input-mono" value="4.20" step="0.01" id="mat42CrMo4" onchange="updateMaterials()">
                                            <span class="input-unit">€/kg</span>
                                        </div>
                                    </div>
                                </div>
                                
                                <div style="font-weight: 600; margin-bottom: var(--space-2); color: var(--color-text-secondary);">Edelstahl</div>
                                <div class="grid-4" style="gap: var(--space-3); margin-bottom: var(--space-4);">
                                    <div class="form-group" style="margin-bottom: 0;">
                                        <label class="form-label form-label-caps">1.4301 (V2A)</label>
                                        <div class="input-with-unit">
                                            <input type="number" class="input input-sm input-mono" value="8.50" step="0.01" id="mat14301" onchange="updateMaterials()">
                                            <span class="input-unit">€/kg</span>
                                        </div>
                                    </div>
                                    <div class="form-group" style="margin-bottom: 0;">
                                        <label class="form-label form-label-caps">1.4404 (V4A)</label>
                                        <div class="input-with-unit">
                                            <input type="number" class="input input-sm input-mono" value="12.00" step="0.01" id="mat14404" onchange="updateMaterials()">
                                            <span class="input-unit">€/kg</span>
                                        </div>
                                    </div>
                                    <div class="form-group" style="margin-bottom: 0;">
                                        <label class="form-label form-label-caps">1.4571</label>
                                        <div class="input-with-unit">
                                            <input type="number" class="input input-sm input-mono" value="14.00" step="0.01" id="mat14571" onchange="updateMaterials()">
                                            <span class="input-unit">€/kg</span>
                                        </div>
                                    </div>
                                    <div class="form-group" style="margin-bottom: 0;">
                                        <label class="form-label form-label-caps">Duplex</label>
                                        <div class="input-with-unit">
                                            <input type="number" class="input input-sm input-mono" value="18.00" step="0.01" id="matDuplex" onchange="updateMaterials()">
                                            <span class="input-unit">€/kg</span>
                                        </div>
                                    </div>
                                </div>
                                
                                <div style="font-weight: 600; margin-bottom: var(--space-2); color: var(--color-text-secondary);">Aluminium</div>
                                <div class="grid-4" style="gap: var(--space-3);">
                                    <div class="form-group" style="margin-bottom: 0;">
                                        <label class="form-label form-label-caps">AlMg3</label>
                                        <div class="input-with-unit">
                                            <input type="number" class="input input-sm input-mono" value="6.50" step="0.01" id="matAlMg3" onchange="updateMaterials()">
                                            <span class="input-unit">€/kg</span>
                                        </div>
                                    </div>
                                    <div class="form-group" style="margin-bottom: 0;">
                                        <label class="form-label form-label-caps">AlMgSi1</label>
                                        <div class="input-with-unit">
                                            <input type="number" class="input input-sm input-mono" value="7.00" step="0.01" id="matAlMgSi1" onchange="updateMaterials()">
                                            <span class="input-unit">€/kg</span>
                                        </div>
                                    </div>
                                    <div class="form-group" style="margin-bottom: 0;">
                                        <label class="form-label form-label-caps">Al7075-T6</label>
                                        <div class="input-with-unit">
                                            <input type="number" class="input input-sm input-mono" value="12.00" step="0.01" id="matAl7075" onchange="updateMaterials()">
                                            <span class="input-unit">€/kg</span>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        
                        <div class="card" style="margin-bottom: var(--space-5);">
                            <div class="card-header card-header-warning"><span>Zuschlagskalkulation (Industriestandard)</span></div>
                            <div class="card-body">
                                <div style="font-size: 12px; color: var(--color-text-muted); margin-bottom: var(--space-4);">
                                    Zuschlagssätze nach betriebswirtschaftlicher Kalkulationsmethode. Basis: Herstellkosten.
                                </div>
                                
                                <table class="table">
                                    <thead>
                                        <tr>
                                            <th>Zuschlagsart</th>
                                            <th style="width: 120px;">Satz (%)</th>
                                            <th>Basis</th>
                                            <th>Branchenüblich</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr>
                                            <td>
                                                <strong>Materialgemeinkosten (MGK)</strong><br>
                                                <span style="font-size: 11px; color: var(--color-text-muted);">Einkauf, Lager, Handling</span>
                                            </td>
                                            <td><input type="number" class="input input-sm input-mono" value="10" id="zuschlagMGK" style="width: 80px;" onchange="calculate()"></td>
                                            <td class="mono" style="font-size: 12px;">auf Materialkosten</td>
                                            <td style="font-size: 12px; color: var(--color-text-muted);">5-15%</td>
                                        </tr>
                                        <tr>
                                            <td>
                                                <strong>Fertigungsgemeinkosten (FGK)</strong><br>
                                                <span style="font-size: 11px; color: var(--color-text-muted);">Meister, Instandhaltung, Energie</span>
                                            </td>
                                            <td><input type="number" class="input input-sm input-mono" value="0" id="zuschlagFGK" style="width: 80px;" onchange="calculate()"></td>
                                            <td class="mono" style="font-size: 12px;">auf Fertigungskosten</td>
                                            <td style="font-size: 12px; color: var(--color-text-muted);">100-200% (oft in MSS)</td>
                                        </tr>
                                        <tr style="background: var(--color-info-light);">
                                            <td>
                                                <strong>AV-Aufschlag</strong><br>
                                                <span style="font-size: 11px; color: var(--color-text-muted);">Arbeitsvorbereitung, Programmierung, CAM</span>
                                            </td>
                                            <td><input type="number" class="input input-sm input-mono" value="8" id="zuschlagAV" style="width: 80px;" onchange="calculate()"></td>
                                            <td class="mono" style="font-size: 12px;">auf Fertigungskosten</td>
                                            <td style="font-size: 12px; color: var(--color-text-muted);">5-15%</td>
                                        </tr>
                                        <tr style="background: var(--color-bg);">
                                            <td colspan="4" style="font-weight: 600; color: var(--color-text-secondary);">= Herstellkosten (HK)</td>
                                        </tr>
                                        <tr>
                                            <td>
                                                <strong>Verwaltungsgemeinkosten (VwGK)</strong><br>
                                                <span style="font-size: 11px; color: var(--color-text-muted);">Buchhaltung, IT, Geschäftsführung</span>
                                            </td>
                                            <td><input type="number" class="input input-sm input-mono" value="12" id="zuschlagVwGK" style="width: 80px;" onchange="calculate()"></td>
                                            <td class="mono" style="font-size: 12px;">auf Herstellkosten</td>
                                            <td style="font-size: 12px; color: var(--color-text-muted);">8-15%</td>
                                        </tr>
                                        <tr>
                                            <td>
                                                <strong>Vertriebsgemeinkosten (VtGK)</strong><br>
                                                <span style="font-size: 11px; color: var(--color-text-muted);">Angebote, Kundenbetreuung, Versand</span>
                                            </td>
                                            <td><input type="number" class="input input-sm input-mono" value="5" id="zuschlagVtGK" style="width: 80px;" onchange="calculate()"></td>
                                            <td class="mono" style="font-size: 12px;">auf Herstellkosten</td>
                                            <td style="font-size: 12px; color: var(--color-text-muted);">3-8%</td>
                                        </tr>
                                        <tr style="background: var(--color-bg);">
                                            <td colspan="4" style="font-weight: 600; color: var(--color-text-secondary);">= Selbstkosten (SK)</td>
                                        </tr>
                                        <tr style="background: var(--color-success-light);">
                                            <td>
                                                <strong>Gewinnzuschlag / Marge</strong><br>
                                                <span style="font-size: 11px; color: var(--color-text-muted);">Unternehmensgewinn</span>
                                            </td>
                                            <td><input type="number" class="input input-sm input-mono" value="10" id="zuschlagGewinn" style="width: 80px;" onchange="calculate()"></td>
                                            <td class="mono" style="font-size: 12px;">auf Selbstkosten</td>
                                            <td style="font-size: 12px; color: var(--color-text-muted);">5-15%</td>
                                        </tr>
                                        <tr style="background: var(--color-primary); color: white;">
                                            <td colspan="4" style="font-weight: 600;">= Angebotspreis (netto)</td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                        </div>
                    </div>
                    
                    <div id="param-maschine" style="display: none;">
                        <div class="card" style="margin-bottom: var(--space-6);">
                            <div class="card-header"><span>Maschine</span></div>
                            <div class="card-body">
                                <div class="form-group">
                                    <label class="form-label">CNC-Typ</label>
                                    <select class="select" id="cncType">
                                        <option value="3-achs" selected>3-Achs</option>
                                        <option value="5-achs">5-Achs</option>
                                    </select>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <!-- Plausibility Warnings -->
                    <div id="warningsContainer"></div>
                    
                    <button class="btn btn-primary" onclick="showSection('result', document.querySelector('.nav-item[data-section=&quot;result&quot;]'))">Kalkulation anzeigen →</button>
                </div>
                
                <!-- ========================================
                     SECTION: ERGEBNIS
                     ======================================== -->
                <div class="section" id="section-result">
                    <!-- Price Hero with Confidence -->
                    <div class="price-hero">
                        <div class="price-label">Stückpreis</div>
                        <div class="price-value" id="priceDisplay">€64,89</div>
                        <div class="price-detail">inkl. Material, Bearbeitung, Einrichtung</div>
                        <div class="confidence-badge confidence-medium" id="confidenceBadge">
                            <span>🟡</span> ±15% Genauigkeit — Standardteil
                        </div>
                    </div>
                    
                    <div class="grid-2">
                        <!-- Kostenaufschlüsselung -->
                        <div class="card">
                            <div class="card-header"><span>Kostenaufschlüsselung</span></div>
                            <div class="cost-breakdown" style="border: none; border-radius: 0;">
                                <div class="cost-row">
                                    <div>
                                        <div class="cost-label">Material + MGK</div>
                                        <div class="cost-formula tooltip" id="matFormula" data-tooltip="Gewicht × Preis/kg + Materialgemeinkosten">2,2 kg × €6,79/kg + 10% MGK</div>
                                    </div>
                                    <div class="cost-value" id="matCost">€16,42</div>
                                </div>
                                <div class="cost-row">
                                    <div>
                                        <div class="cost-label">Fertigung + AV</div>
                                        <div class="cost-formula tooltip" id="machFormula" data-tooltip="Fertigungskosten + AV-Aufschlag">12,5 min × €91/h + 8% AV</div>
                                    </div>
                                    <div class="cost-value" id="machCost">€18,96</div>
                                </div>
                                <div class="cost-row">
                                    <div>
                                        <div class="cost-label">Einrichtung</div>
                                        <div class="cost-formula tooltip" id="setupFormula" data-tooltip="Einrichtzeit × Stundensatz ÷ Stückzahl">25 min × €91/h ÷ 1</div>
                                    </div>
                                    <div class="cost-value" id="setupCost">€37,92</div>
                                </div>
                                <div class="cost-row">
                                    <div>
                                        <div class="cost-label">Werkzeugverschleiß</div>
                                        <div class="cost-formula">pauschal, werkstoffabhängig</div>
                                    </div>
                                    <div class="cost-value" id="toolCost">€20,74</div>
                                </div>
                                <div class="cost-row">
                                    <div>
                                        <div class="cost-label">VwGK + VtGK</div>
                                        <div class="cost-formula" id="additionalFormula">Verwaltung + Vertrieb</div>
                                    </div>
                                    <div class="cost-value" id="additionalCost">€15,17</div>
                                </div>
                                <div class="cost-row subtotal">
                                    <div class="cost-label">Selbstkosten</div>
                                    <div class="cost-value" id="totalCost">€109,21</div>
                                </div>
                                <div class="cost-row">
                                    <div class="cost-label">+ Gewinn (<span id="marginDisplay">10</span>%)</div>
                                    <div class="cost-value" id="marginCost">€10,92</div>
                                </div>
                                <div class="cost-row total">
                                    <div class="cost-label">Angebotspreis</div>
                                    <div class="cost-value" id="sellPrice">€120,13</div>
                                </div>
                            </div>
                        </div>
                        
                        <!-- Mengenstaffel -->
                        <div class="card">
                            <div class="card-header"><span>📈 Mengenstaffel</span></div>
                            <div class="card-body">
                                <table class="table">
                                    <thead>
                                        <tr>
                                            <th>Stückzahl</th>
                                            <th class="right">Pro Stück</th>
                                            <th class="right">Gesamt</th>
                                        </tr>
                                    </thead>
                                    <tbody id="quantityTable"></tbody>
                                </table>
                                
                                <div class="info-box" style="margin-top: var(--space-4);">
                                    Bei größeren Mengen sinkt der Stückpreis, da Einricht- und Prüfkosten verteilt werden.
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <!-- Marge anpassen -->
                    <div class="card" style="margin-top: var(--space-5);">
                        <div class="card-body" style="display: flex; align-items: center; gap: var(--space-4);">
                            <span style="color: var(--color-text-secondary);">Marge anpassen:</span>
                            <div class="input-with-unit" style="width: 100px;">
                                <input type="number" class="input input-mono" id="marginInput" value="10" min="0" max="100" oninput="calculate()">
                                <span class="input-unit">%</span>
                            </div>
                            <span style="margin-left: auto; color: var(--color-text-secondary);">Gesamtauftragswert:</span>
                            <strong style="font-size: 18px; font-family: var(--font-mono);" id="orderTotal">€120,13</strong>
                        </div>
                    </div>
                    
                    <!-- Kalkulationsgrundlage -->
                    <div class="card" style="margin-top: var(--space-5);">
                        <div class="card-header"><span>📋 Kalkulationsgrundlage</span></div>
                        <div class="card-body">
                            <div class="grid-2" style="font-size: 13px; margin-bottom: var(--space-4);">
                                <div>
                                    <div style="color: var(--color-text-muted); margin-bottom: 4px;">Datenquelle</div>
                                    <div>Echte Betriebsdaten (validiert)</div>
                                </div>
                                <div>
                                    <div style="color: var(--color-text-muted); margin-bottom: 4px;">Stundensätze</div>
                                    <div>Aus Nachkalkulation verifiziert</div>
                                </div>
                                <div>
                                    <div style="color: var(--color-text-muted); margin-bottom: 4px;">Zeitberechnung</div>
                                    <div>Formelbasiert (±15% Genauigkeit)</div>
                                </div>
                                <div>
                                    <div style="color: var(--color-text-muted); margin-bottom: 4px;">Materialpreise</div>
                                    <div>Aktueller Einkaufspreis + Handling</div>
                                </div>
                            </div>
                            
                            <!-- Normen & Methodik -->
                            <div style="background: var(--color-bg); padding: var(--space-4); border-radius: var(--radius-md); border-left: 3px solid var(--color-primary);">
                                <div style="font-weight: 600; margin-bottom: var(--space-2);">Normen & Berechnungsmethodik</div>
                                <div style="font-size: 13px; color: var(--color-text-secondary); line-height: 1.7;">
                                    <strong>Zeitgliederung nach REFA</strong> (Verband für Arbeitsstudien e.V.)<br>
                                    • Auftragszeit T = Rüstzeit (t<sub>r</sub>) + Ausführungszeit (t<sub>a</sub>)<br>
                                    • Grundzeit t<sub>g</sub> = Hauptzeit (t<sub>h</sub>) + Nebenzeit (t<sub>n</sub>)<br>
                                    • Stückzeit t<sub>e</sub> = Grundzeit + Verteilzeit + Erholzeit<br><br>
                                    
                                    <strong>Schnittdatenberechnung nach VDI 3321</strong><br>
                                    • Schnittgeschwindigkeit v<sub>c</sub> = π × d × n / 1000<br>
                                    • Vorschubgeschwindigkeit v<sub>f</sub> = f<sub>z</sub> × z × n<br>
                                    • Maschinenhauptzeit t<sub>h</sub> = L / v<sub>f</sub><br><br>
                                    
                                    <strong>Fertigungsverfahren nach DIN 8580</strong><br>
                                    Klassifikation: Gruppe 3 – Trennen (Spanen mit geometrisch bestimmter Schneide)<br><br>
                                    
                                    <strong>Werkstoffkennwerte nach DIN EN 10027</strong><br>
                                    Werkstoffnummern, Dichte, Zerspanbarkeit
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                
                <!-- ========================================
                     SECTION: ANGEBOT
                     ======================================== -->
                <div class="section" id="section-quote">
                    <div class="card">
                        <div class="card-header">
                            <span>Angebot ANG-2026-0042</span>
                            <div style="display: flex; gap: var(--space-2);">
                                <button class="btn btn-secondary btn-sm">✉️ E-Mail</button>
                                <button class="btn btn-primary btn-sm" onclick="window.print()">📥 PDF</button>
                            </div>
                        </div>
                        <div class="card-body">
                            <div style="display: flex; justify-content: space-between; margin-bottom: var(--space-6); padding-bottom: var(--space-4); border-bottom: 2px solid var(--color-primary);">
                                <div>
                                    <div style="font-size: 20px; font-weight: 700; color: var(--color-primary);">ANGEBOT</div>
                                    <div style="font-size: 13px; color: var(--color-text-muted);">ANG-2026-0042</div>
                                </div>
                                <div style="text-align: right; font-size: 13px; color: var(--color-text-secondary);">
                                    <div><strong>Ihre Firma GmbH</strong></div>
                                    <div>Datum: <span id="quoteDate">05.02.2026</span></div>
                                    <div>Gültig bis: <span id="quoteValidUntil">05.03.2026</span></div>
                                </div>
                            </div>
                            
                            <table class="table">
                                <thead>
                                    <tr>
                                        <th>Pos.</th>
                                        <th>Beschreibung</th>
                                        <th class="right">Menge</th>
                                        <th class="right">EP (€)</th>
                                        <th class="right">GP (€)</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr>
                                        <td>1</td>
                                        <td id="quoteDesc">Verbindungsplatte 2500473...</td>
                                        <td class="right mono" id="quoteQty">1</td>
                                        <td class="right mono" id="quoteEP">120,13</td>
                                        <td class="right mono" id="quoteGP">120,13</td>
                                    </tr>
                                </tbody>
                            </table>
                            
                            <div style="margin-top: var(--space-6); padding-top: var(--space-4); border-top: 1px solid var(--color-border);">
                                <div style="display: flex; justify-content: flex-end;">
                                    <div style="text-align: right; width: 250px;">
                                        <div style="display: flex; justify-content: space-between; margin-bottom: var(--space-2);">
                                            <span style="color: var(--color-text-secondary);">Zwischensumme:</span>
                                            <span class="mono" id="quoteSubtotal">€120,13</span>
                                        </div>
                                        <div style="display: flex; justify-content: space-between; margin-bottom: var(--space-2);">
                                            <span style="color: var(--color-text-secondary);">+ MwSt. 19%:</span>
                                            <span class="mono" id="quoteMwst">€22,82</span>
                                        </div>
                                        <div style="display: flex; justify-content: space-between; font-size: 16px; font-weight: 600; padding-top: var(--space-2); border-top: 2px solid var(--color-primary);">
                                            <span>GESAMT:</span>
                                            <span class="mono" style="color: var(--color-primary);" id="quoteTotal">€142,95</span>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            
                            <div style="margin-top: var(--space-6); font-size: 12px; color: var(--color-text-muted);">
                                <strong>Zahlungsbedingungen:</strong> 14 Tage netto ab Rechnungsdatum<br>
                                <strong>Lieferzeit:</strong> ca. 3-4 Wochen nach Auftragseingang
                            </div>
                        </div>
                    </div>
                </div>
                
                <!-- ========================================
                     SECTION: FERTIGUNGSANWEISUNG
                     ======================================== -->
                <div class="section" id="section-instructions">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: var(--space-5);">
                        <div style="display: flex; gap: var(--space-2);">
                            <button class="btn btn-primary btn-sm" onclick="window.print()">PDF drucken</button>
                            <button class="btn btn-secondary btn-sm">E-Mail</button>
                        </div>
                        <span class="badge badge-info">KI-generierte Anweisungen</span>
                    </div>
                    
                    <!-- Document Header -->
                    <div class="card" style="margin-bottom: var(--space-5);">
                        <div class="card-body">
                            <div style="display: flex; justify-content: space-between; margin-bottom: var(--space-5); padding-bottom: var(--space-4); border-bottom: 3px solid var(--color-primary);">
                                <div>
                                    <h3 style="color: var(--color-primary); font-size: 18px; font-weight: 700;">FERTIGUNGSANWEISUNG</h3>
                                    <p id="faPartName" style="color: var(--color-text-muted); font-size: 13px;">Verbindungsplatte — 2500473.01.11.02.00.001</p>
                                </div>
                                <div style="text-align: right; font-size: 13px; color: var(--color-text-muted);">
                                    <div>Freigabe: 05.02.2026</div>
                                    <div>Version: 1.0</div>
                                </div>
                            </div>
                            
                            <div class="grid-3" style="margin-bottom: var(--space-4);">
                                <div>
                                    <div style="font-weight: 600; margin-bottom: var(--space-2);">Werkstück</div>
                                    <table style="font-size: 13px; width: 100%;">
                                        <tr><td style="color: var(--color-text-muted); padding: 2px 0;">Werkstoff:</td><td id="faMaterial" style="padding: 2px 0;"><strong>S235JR</strong></td></tr>
                                        <tr><td style="color: var(--color-text-muted); padding: 2px 0;">Rohteil:</td><td id="faRawDims" style="padding: 2px 0;">440 × 50 × 20 mm</td></tr>
                                        <tr><td style="color: var(--color-text-muted); padding: 2px 0;">Gewicht:</td><td id="faWeight" style="padding: 2px 0;">2,2 kg</td></tr>
                                    </table>
                                </div>
                                <div>
                                    <div style="font-weight: 600; margin-bottom: var(--space-2);">Maschine</div>
                                    <table style="font-size: 13px; width: 100%;">
                                        <tr><td style="color: var(--color-text-muted); padding: 2px 0;">Maschine:</td><td style="padding: 2px 0;"><strong>FEHLMANN VERSA 943</strong></td></tr>
                                        <tr><td style="color: var(--color-text-muted); padding: 2px 0;">Steuerung:</td><td style="padding: 2px 0;">Heidenhain TNC 640</td></tr>
                                        <tr><td style="color: var(--color-text-muted); padding: 2px 0;">Zeit:</td><td id="faMachiningTime" style="padding: 2px 0;"><strong>12,5 min</strong></td></tr>
                                    </table>
                                </div>
                                <!-- Zeichnung Upload entfernt -->
                            </div>
                            
                            <div class="info-box">
                                <strong>Toleranzen:</strong> Allgemein DIN ISO 2768-mK • Oberfläche Rz 25
                            </div>
                        </div>
                    </div>

                    <!-- Zeichnungs-Vorschau -->
                    <!-- Qualitätsprüfung -->
                    <div class="instruction-section">
                        <div class="instruction-header">
                            <h4>Qualitätsprüfung</h4>
                            <span class="badge badge-info">QS</span>
                        </div>
                        <div class="instruction-content">
                            <table class="table">
                                <thead>
                                    <tr>
                                        <th>Prüfmerkmal</th>
                                        <th>Soll</th>
                                        <th>Prüfmittel</th>
                                        <th class="right">Zeit</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr>
                                        <td>Ø26 H7</td>
                                        <td class="mono">26,000 / 26,021</td>
                                        <td>Innenmessschraube</td>
                                        <td class="right mono">0,8 min</td>
                                    </tr>
                                    <tr>
                                        <td>Höhe</td>
                                        <td class="mono">20,0 ±0,1</td>
                                        <td>Messschieber</td>
                                        <td class="right mono">0,3 min</td>
                                    </tr>
                                    <tr>
                                        <td>Oberfläche</td>
                                        <td class="mono">Rz ≤ 25</td>
                                        <td>Vergleichsmuster</td>
                                        <td class="right mono">0,5 min</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
                
                <!-- ========================================
                     SECTION: KALKULATION (Detailliert)
                     ======================================== -->
                <div class="section" id="section-calculation">
                    </div>
                    
                    <!-- Legende -->
                    <div class="info-box" style="margin-bottom: var(--space-5);">
                        <strong>Berechnungsformel:</strong> t<sub>h</sub> = Verfahrweg L [mm] ÷ Vorschub v<sub>f</sub> [mm/min] &nbsp;|&nbsp; 
                        <strong>Nebenzeit:</strong> Werkzeugwechsel + Positionieren + Zustellung + Späne entfernen
                    </div>
                    
                    <!-- 2-Spalten Layout: Maschine + Material -->
                    <div class="grid-2" style="margin-bottom: var(--space-5);">
                        <!-- Maschinenzeitkalkulation -->
                        <div class="card">
                            <div class="card-header card-header-info"><span>Maschinenzeitkalkulation</span></div>
                            <div class="card-body">
                                <table class="table">
                                    <tbody>
                                        <tr>
                                            <td>Hauptzeit (th)</td>
                                            <td class="right mono" id="calcTh">31,2 min</td>
                                        </tr>
                                        <tr>
                                            <td>Nebenzeit (tn)</td>
                                            <td class="right mono" id="calcTn">8,0 min</td>
                                        </tr>
                                        <tr style="background: var(--color-bg); font-weight: 600;">
                                            <td>Gesamtzeit</td>
                                            <td class="right mono" id="calcTimeTotal">39,2 min</td>
                                        </tr>
                                        <tr>
                                            <td>× Stundensatz</td>
                                            <td class="right mono">€91/h</td>
                                        </tr>
                                        <tr style="background: var(--color-info-light); font-weight: 600;">
                                            <td>= Maschinenkosten</td>
                                            <td class="right mono" id="calcMachCost">€59,47</td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                        </div>
                        
                        <!-- Materialkalkulation -->
                        <div class="card">
                            <div class="card-header card-header-success"><span>📦 Materialkalkulation</span></div>
                            <div class="card-body">
                                <table class="table">
                                    <tbody>
                                        <tr>
                                            <td>Rohmaße</td>
                                            <td class="right mono" id="calcRawDims">130 × 130 × 47 mm</td>
                                        </tr>
                                        <tr>
                                            <td>Volumen</td>
                                            <td class="right mono" id="calcVolume">794.170 mm³</td>
                                        </tr>
                                        <tr>
                                            <td>Werkstoff / Dichte</td>
                                            <td class="right mono" id="calcDensity">S235JR / 7,85 g/cm³</td>
                                        </tr>
                                        <tr style="background: var(--color-bg); font-weight: 600;">
                                            <td>Gewicht</td>
                                            <td class="right mono" id="calcWeight">6,23 kg</td>
                                        </tr>
                                        <tr>
                                            <td>× Preis + 10% Verschnitt</td>
                                            <td class="right mono" id="calcMatFormula">€6,79/kg × 1,1</td>
                                        </tr>
                                        <tr style="background: var(--color-success-light); font-weight: 600;">
                                            <td>= Materialkosten</td>
                                            <td class="right mono" id="calcMatCost">€46,57</td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                        </div>
                    </div>
                    
                    <!-- Einrichtkosten -->
                    <div class="card" style="margin-bottom: var(--space-5);">
                        <div class="card-header card-header-warning"><span>Einrichtkosten (Rüstzeit)</span></div>
                        <div class="card-body">
                            <div class="grid-2">
                                <table class="table">
                                    <tbody>
                                        <tr>
                                            <td>Spannmethode</td>
                                            <td class="right" id="calcClamping">Schraubstock</td>
                                        </tr>
                                        <tr>
                                            <td>Basis-Einrichtzeit</td>
                                            <td class="right mono">15 min</td>
                                        </tr>
                                        <tr>
                                            <td>Aufspannungen</td>
                                            <td class="right mono" id="calcSetups">2×</td>
                                        </tr>
                                        <tr style="background: var(--color-bg); font-weight: 600;">
                                            <td>Gesamt-Einrichtzeit</td>
                                            <td class="right mono" id="calcSetupTime">24 min</td>
                                        </tr>
                                    </tbody>
                                </table>
                                <table class="table">
                                    <tbody>
                                        <tr>
                                            <td>× Stundensatz</td>
                                            <td class="right mono">€91/h</td>
                                        </tr>
                                        <tr style="background: var(--color-warning-light); font-weight: 600;">
                                            <td>= Einrichtkosten</td>
                                            <td class="right mono" id="calcSetupCostDetail">€36,40</td>
                                        </tr>
                                        <tr>
                                            <td>÷ Stückzahl</td>
                                            <td class="right mono" id="calcQtyDetail">1</td>
                                        </tr>
                                        <tr style="font-weight: 600;">
                                            <td>= Pro Stück</td>
                                            <td class="right mono" id="calcSetupPerPiece">€36,40</td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                            <div class="info-box" style="margin-top: var(--space-4);">
                                <strong>Tipp:</strong> Bei Serienproduktion werden Einrichtkosten auf alle Teile verteilt — der Stückpreis sinkt erheblich.
                            </div>
                        </div>
                    </div>
                    
                    <!-- Berechnungsmethodik -->
                    <div class="card" style="margin-bottom: var(--space-5);">
                        <div class="card-header"><span>📖 Berechnungsmethodik (Normen)</span></div>
                        <div class="card-body" style="font-size: 13px; line-height: 1.7;">
                            <div class="grid-2">
                                <div>
                                    <strong style="color: var(--color-primary);">Zeitgliederung nach REFA</strong><br>
                                    <span style="color: var(--color-text-secondary);">
                                        T = t<sub>r</sub> + t<sub>a</sub> (Rüst + Ausführung)<br>
                                        t<sub>g</sub> = t<sub>h</sub> + t<sub>n</sub> (Haupt + Neben)
                                    </span>
                                </div>
                                <div>
                                    <strong style="color: var(--color-primary);">Schnittdaten nach VDI 3321</strong><br>
                                    <span style="color: var(--color-text-secondary);">
                                        v<sub>c</sub> = π×d×n/1000<br>
                                        t<sub>h</sub> = L / v<sub>f</sub>
                                    </span>
                                </div>
                                <div>
                                    <strong style="color: var(--color-primary);">DIN 8580</strong><br>
                                    <span style="color: var(--color-text-secondary);">Fertigungsverfahren — Trennen (Spanen)</span>
                                </div>
                                <div>
                                    <strong style="color: var(--color-primary);">DIN EN 10027</strong><br>
                                    <span style="color: var(--color-text-secondary);">Werkstoffnummern & Kennwerte</span>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <!-- Gesamtkalkulation -->
                    <div class="card">
                        <div class="card-header card-header-primary"><span>Gesamtkalkulation</span></div>
                        <div class="card-body" style="padding: 0; overflow-x: auto;">
                            <table class="table">
                                <thead>
                                    <tr>
                                        <th>Kostenart</th>
                                        <th class="right">Berechnung</th>
                                        <th class="right">Pro Stück</th>
                                        <th class="right">Gesamt</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr>
                                        <td>Material</td>
                                        <td class="right mono" style="color: var(--color-text-muted); font-size: 12px;">6,23 kg × €6,79 × 1,1</td>
                                        <td class="right mono">€46,57</td>
                                        <td class="right mono">€46,57</td>
                                    </tr>
                                    <tr>
                                        <td>Maschinenzeit</td>
                                        <td class="right mono" style="color: var(--color-text-muted); font-size: 12px;">39,2 min × €91/h</td>
                                        <td class="right mono">€59,47</td>
                                        <td class="right mono">€59,47</td>
                                    </tr>
                                    <tr>
                                        <td>Werkzeugverschleiß</td>
                                        <td class="right mono" style="color: var(--color-text-muted); font-size: 12px;">pauschal (werkstoffabh.)</td>
                                        <td class="right mono">€20,74</td>
                                        <td class="right mono">€20,74</td>
                                    </tr>
                                    <tr style="background: var(--color-warning-light);">
                                        <td>Einrichtung</td>
                                        <td class="right mono" style="color: var(--color-warning); font-size: 12px;">24 min × €91/h ÷ 1</td>
                                        <td class="right mono" style="color: var(--color-warning);">€36,40</td>
                                        <td class="right mono">€36,40</td>
                                    </tr>
                                    <tr style="background: var(--color-bg);">
                                        <td>Nebenzeiten</td>
                                        <td class="right mono" style="color: var(--color-text-muted); font-size: 12px;">Entgraten + Prüfung</td>
                                        <td class="right mono">€7,58</td>
                                        <td class="right mono">€7,58</td>
                                    </tr>
                                    <tr style="background: var(--color-bg); font-weight: 600;">
                                        <td>HERSTELLKOSTEN</td>
                                        <td></td>
                                        <td class="right mono">€170,76</td>
                                        <td class="right mono">€170,76</td>
                                    </tr>
                                    <tr>
                                        <td>+ Marge 10%</td>
                                        <td></td>
                                        <td class="right mono">€17,08</td>
                                        <td class="right mono">€17,08</td>
                                    </tr>
                                    <tr style="background: var(--color-primary); color: white; font-weight: 600;">
                                        <td>VERKAUFSPREIS</td>
                                        <td></td>
                                        <td class="right mono">€187,84</td>
                                        <td class="right mono">€187,84</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
                
                <!-- ========================================
                     SECTION: WERKZEUGE
                     ======================================== -->
                <div class="section" id="section-tools">
                    <div class="card" style="margin-bottom: var(--space-5);">
                        <div class="card-header"><span>Schnittparameter</span></div>
                        <div class="card-body" style="padding: 0; overflow-x: auto;">
                            <table class="table" id="cuttingParamsTable">
                                <thead>
                                    <tr>
                                        <th>Werkzeug</th>
                                        <th>Operation</th>
                                        <th class="right">Vc [m/min]</th>
                                        <th class="right">n [U/min]</th>
                                        <th class="right">fz [mm/Z]</th>
                                        <th class="right">vf [mm/min]</th>
                                        <th class="right">ap [mm]</th>
                                        <th class="right">ae [mm]</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr>
                                        <td><strong>T1</strong> Planfräser Ø63</td>
                                        <td>Planfräsen</td>
                                        <td class="right mono">160</td>
                                        <td class="right mono">808</td>
                                        <td class="right mono">0,15</td>
                                        <td class="right mono">485</td>
                                        <td class="right mono">2,0</td>
                                        <td class="right mono">45</td>
                                    </tr>
                                    <tr>
                                        <td><strong>T2</strong> VHM-Fräser Ø20</td>
                                        <td>Schruppen</td>
                                        <td class="right mono">120</td>
                                        <td class="right mono">1910</td>
                                        <td class="right mono">0,08</td>
                                        <td class="right mono">611</td>
                                        <td class="right mono">8,0</td>
                                        <td class="right mono">10</td>
                                    </tr>
                                    <tr>
                                        <td><strong>T3</strong> VHM-Schlichtfräser Ø16</td>
                                        <td>Schlichten</td>
                                        <td class="right mono">140</td>
                                        <td class="right mono">2785</td>
                                        <td class="right mono">0,05</td>
                                        <td class="right mono">557</td>
                                        <td class="right mono">0,3</td>
                                        <td class="right mono">8</td>
                                    </tr>
                                    <tr>
                                        <td><strong>T11</strong> Feinbohrkopf Ø26</td>
                                        <td>Feinbohren</td>
                                        <td class="right mono">100</td>
                                        <td class="right mono">1225</td>
                                        <td class="right mono">0,08</td>
                                        <td class="right mono">98</td>
                                        <td class="right mono">0,15</td>
                                        <td class="right mono">—</td>
                                    </tr>
                                    <tr>
                                        <td><strong>T12</strong> Feinbohrkopf Ø44</td>
                                        <td>Feinbohren</td>
                                        <td class="right mono">100</td>
                                        <td class="right mono">723</td>
                                        <td class="right mono">0,08</td>
                                        <td class="right mono">58</td>
                                        <td class="right mono">0,15</td>
                                        <td class="right mono">—</td>
                                    </tr>
                                    <tr>
                                        <td><strong>T13</strong> Gewindefräser M8</td>
                                        <td>Gewinde</td>
                                        <td class="right mono">80</td>
                                        <td class="right mono">3183</td>
                                        <td class="right mono">—</td>
                                        <td class="right mono">1,25</td>
                                        <td class="right mono">1,25</td>
                                        <td class="right mono">—</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                    
                    <div class="info-box" style="margin-bottom: var(--space-5);">
                        <strong>Legende:</strong> Vc = Schnittgeschwindigkeit | n = Drehzahl | fz = Vorschub pro Zahn | vf = Vorschubgeschwindigkeit | ap = Schnitttiefe | ae = Zustellung
                    </div>
                    
                    <div class="card">
                        <div class="card-header"><span>Werkzeugkosten</span></div>
                        <div class="card-body" style="padding: 0; overflow-x: auto;">
                            <table class="table">
                                <thead>
                                    <tr>
                                        <th>Werkzeug</th>
                                        <th class="right">Preis [€]</th>
                                        <th class="right">Standzeit [min]</th>
                                        <th class="right">Einsatzzeit [min]</th>
                                        <th class="right">Kosten [€]</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr>
                                        <td>T1 Planfräser Ø63 (WSP)</td>
                                        <td class="right mono">45,00</td>
                                        <td class="right mono">120</td>
                                        <td class="right mono">2,7</td>
                                        <td class="right mono">1,01</td>
                                    </tr>
                                    <tr>
                                        <td>T2 VHM-Fräser Ø20</td>
                                        <td class="right mono">185,00</td>
                                        <td class="right mono">90</td>
                                        <td class="right mono">5,1</td>
                                        <td class="right mono">10,48</td>
                                    </tr>
                                    <tr>
                                        <td>T3 VHM-Schlichtfräser Ø16</td>
                                        <td class="right mono">165,00</td>
                                        <td class="right mono">80</td>
                                        <td class="right mono">3,6</td>
                                        <td class="right mono">7,43</td>
                                    </tr>
                                    <tr>
                                        <td>T11/T12 Feinbohrköpfe</td>
                                        <td class="right mono">35,00</td>
                                        <td class="right mono">200</td>
                                        <td class="right mono">1,4</td>
                                        <td class="right mono">0,25</td>
                                    </tr>
                                    <tr>
                                        <td>T13 Gewindefräser M8</td>
                                        <td class="right mono">89,00</td>
                                        <td class="right mono">100</td>
                                        <td class="right mono">1,8</td>
                                        <td class="right mono">1,60</td>
                                    </tr>
                                    <tr style="background: var(--color-bg); font-weight: 600;">
                                        <td>Gesamt</td>
                                        <td class="right mono">—</td>
                                        <td class="right mono">—</td>
                                        <td class="right mono">14,6</td>
                                        <td class="right mono">€20,77</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                    
                    <div class="warning-box" style="margin-top: var(--space-5);">
                        <strong>Hinweis:</strong> Bei hartem Werkstoff (1.4571 Edelstahl) können Werkzeugkosten 15-20% der Gesamtkosten ausmachen. Standzeiten sind werkstoffabhängig und können bei schwer zerspanbaren Materialien um 30-50% reduziert sein.
                    </div>
                    
                    <!-- Feedback -->
                    <div class="feedback-card" style="margin-top: var(--space-6);">
                        <div style="text-align: center; margin-bottom: var(--space-4);">
                            <strong>Wie genau war diese Kalkulation?</strong>
                            <div style="font-size: 13px; color: var(--color-text-secondary);">Ihr Feedback hilft uns, die Algorithmen zu verbessern</div>
                        </div>
                        <div class="feedback-options">
                            <div class="feedback-option" onclick="selectFeedback(this, 'correct')">
                                <span class="feedback-option-icon">✓</span>
                                <span class="feedback-option-label">Korrekt</span>
                            </div>
                            <div class="feedback-option" onclick="selectFeedback(this, 'low')">
                                <span class="feedback-option-icon">↓</span>
                                <span class="feedback-option-label">Zu niedrig</span>
                            </div>
                            <div class="feedback-option" onclick="selectFeedback(this, 'high')">
                                <span class="feedback-option-icon">↑</span>
                                <span class="feedback-option-label">Zu hoch</span>
                            </div>
                            <div class="feedback-option" onclick="selectFeedback(this, 'other')">
                                <span class="feedback-option-icon">?</span>
                                <span class="feedback-option-label">Sonstiges</span>
                            </div>
                        </div>
                        <textarea id="feedbackComment" placeholder="Optionaler Kommentar... (z.B. 'Tatsächliche Zeit war 35 min statt 25 min')" 
                            style="width: 100%; height: 80px; padding: var(--space-3); border: 1px solid var(--color-border); border-radius: var(--radius-md); resize: vertical; font-family: inherit; font-size: 13px; margin-bottom: var(--space-3);"></textarea>
                        <button class="btn btn-primary" onclick="submitFeedback()" style="width: 100%;">Feedback senden</button>
                    </div>
                </div>
                
                <!-- ========================================
                     SECTION: NC-CODE
                     ======================================== -->
                <div class="section" id="section-code">
                    <div class="card">
                        <div class="card-header">
                            <span>NC-Code Generator</span>
                            <div style="display: flex; gap: var(--space-2);">
                                <button class="btn btn-primary btn-sm" id="btnHeidenhain" onclick="setCodeFormat('heidenhain')">Heidenhain</button>
                                <button class="btn btn-secondary btn-sm" id="btnSiemens" onclick="setCodeFormat('siemens')">Siemens</button>
                                <button class="btn btn-secondary btn-sm" id="btnFanuc" onclick="setCodeFormat('fanuc')">Fanuc</button>
                            </div>
                            <div style="display: flex; gap: var(--space-2);">
                                <button class="btn btn-secondary btn-sm" onclick="copyCode()">Kopieren</button>
                                <button class="btn btn-primary btn-sm" onclick="downloadCode()">Download</button>
                            </div>
                        </div>
                        <div class="card-body" style="padding: 0;">
                            <div class="code-block" id="codeBlock">
<pre><span class="code-comment">; ========================================</span>
<span class="code-comment">; CNC PLANNER PRO — Automatisch generiert</span>
<span class="code-comment">; ========================================</span>
<span class="code-comment">; Werkstück:  Verbindungsplatte</span>
<span class="code-comment">; Werkstoff:  S235JR</span>
<span class="code-comment">; Maschine:   FEHLMANN VERSA 943</span>
<span class="code-comment">; Steuerung:  Heidenhain TNC 640</span>
<span class="code-comment">; ========================================</span>

<span class="code-keyword">BEGIN PGM</span> VERBINDUNGSPLATTE <span class="code-keyword">MM</span>

<span class="code-comment">; --- WERKZEUGLISTE ---</span>
<span class="code-keyword">TOOL DEF</span> <span class="code-number">1</span> L+<span class="code-number">0</span> R+<span class="code-number">31.5</span>  <span class="code-comment">; Planfräser Ø63</span>
<span class="code-keyword">TOOL DEF</span> <span class="code-number">2</span> L+<span class="code-number">0</span> R+<span class="code-number">10</span>    <span class="code-comment">; VHM-Fräser Ø20</span>
<span class="code-keyword">TOOL DEF</span> <span class="code-number">11</span> L+<span class="code-number">0</span> R+<span class="code-number">13</span>   <span class="code-comment">; Feinbohrkopf Ø26</span>

<span class="code-comment">; OP10: PLANFRÄSEN</span>
<span class="code-keyword">TOOL CALL</span> <span class="code-number">1</span> Z S<span class="code-number">800</span>
L Z+<span class="code-number">100</span> R0 FMAX M3
L X+<span class="code-number">0</span> Y+<span class="code-number">0</span> FMAX

<span class="code-keyword">CYCL DEF</span> <span class="code-number">230</span> <span class="code-keyword">FACE MILLING</span>
  Q<span class="code-number">225</span>=+<span class="code-number">0</span>
  Q<span class="code-number">218</span>=<span class="code-number">450</span>
  Q<span class="code-number">219</span>=<span class="code-number">60</span>
  Q<span class="code-number">202</span>=<span class="code-number">2</span>
  Q<span class="code-number">207</span>=<span class="code-number">300</span>

<span class="code-keyword">CYCL CALL</span>
L Z+<span class="code-number">100</span> FMAX
M5

<span class="code-comment">; OP20: KONTUR</span>
<span class="code-keyword">TOOL CALL</span> <span class="code-number">2</span> Z S<span class="code-number">2500</span>
M3
<span class="code-comment">; ... weitere Bearbeitung</span>

<span class="code-comment">; OP30: FEINBOHREN Ø26 H7</span>
<span class="code-keyword">TOOL CALL</span> <span class="code-number">11</span> Z S<span class="code-number">1200</span>
M3
L X+<span class="code-number">220</span> Y+<span class="code-number">25</span> FMAX

<span class="code-keyword">CYCL DEF</span> <span class="code-number">201</span> <span class="code-keyword">BORING</span>
  Q<span class="code-number">200</span>=<span class="code-number">2</span>
  Q<span class="code-number">201</span>=-<span class="code-number">25</span>
  Q<span class="code-number">206</span>=<span class="code-number">100</span>

<span class="code-keyword">CYCL CALL</span>
L Z+<span class="code-number">100</span> FMAX
M5
M30

<span class="code-keyword">END PGM</span> VERBINDUNGSPLATTE <span class="code-keyword">MM</span></pre>
                            </div>
                        </div>
                    </div>
                    
                    <div class="info-box" style="margin-top: var(--space-4);">
                        <strong>Programm-Info:</strong> 85 Zeilen | Geschätzte Laufzeit: 12,5 min | Maschine: FEHLMANN VERSA 943<br>
                        <strong style="color: var(--color-warning);">Hinweis:</strong> Code vor Einsatz prüfen.
                    </div>
                </div>
                
                <!-- ========================================
                     SECTION: FEEDBACK & CROSS-LEARNINGS
                     ======================================== -->
                <div class="section" id="section-feedback">
                    
                    <!-- Tabs -->
                    <div style="display: flex; gap: var(--space-2); margin-bottom: var(--space-5); border-bottom: 1px solid var(--color-border); padding-bottom: var(--space-3);">
                        <button class="btn btn-sm btn-primary" id="tabFeedbackEingabe" onclick="showFeedbackTab('eingabe')">Feedback erfassen</button>
                        <button class="btn btn-sm btn-secondary" id="tabFeedbackLearnings" onclick="showFeedbackTab('learnings')">🧠 Cross-Learnings</button>
                        <button class="btn btn-sm btn-secondary" id="tabFeedbackHistorie" onclick="showFeedbackTab('historie')">📋 Historie</button>
                    </div>
                    
                    <!-- TAB: Feedback Eingabe -->
                    <div id="feedback-eingabe">
                        <div class="card" style="margin-bottom: var(--space-5);">
                            <div class="card-header card-header-info"><span>Fertigungs-Feedback erfassen</span></div>
                            <div class="card-body">
                                <div class="grid-3" style="gap: var(--space-4); margin-bottom: var(--space-5);">
                                    <div class="form-group" style="margin-bottom: 0;">
                                        <label class="form-label">Projekt-Nr.</label>
                                        <input type="text" class="input input-mono" id="fbProjektNr" value="2500473.01" readonly style="background: var(--color-bg);">
                                    </div>
                                    <div class="form-group" style="margin-bottom: 0;">
                                        <label class="form-label">Datum</label>
                                        <input type="date" class="input" id="fbDatum" value="2026-02-05">
                                    </div>
                                    <div class="form-group" style="margin-bottom: 0;">
                                        <label class="form-label">Erfasser</label>
                                        <input type="text" class="input" id="fbErfasser" placeholder="Name oder Kürzel">
                                    </div>
                                </div>
                                
                                <div style="font-weight: 600; margin-bottom: var(--space-3); color: var(--color-text-muted); font-size: 12px; text-transform: uppercase;">Zeitabweichungen pro Operation</div>
                                
                                <table class="table" style="margin-bottom: var(--space-5);">
                                    <thead>
                                        <tr>
                                            <th style="width: 80px;">OP</th>
                                            <th>Beschreibung</th>
                                            <th style="width: 100px;">Kalk.</th>
                                            <th style="width: 100px;">Ist</th>
                                            <th style="width: 80px;">Delta</th>
                                            <th style="width: 150px;">Grund</th>
                                            <th>Notiz</th>
                                        </tr>
                                    </thead>
                                    <tbody id="feedbackOpsTable">
                                        <tr>
                                            <td class="mono">OP10</td>
                                            <td>Planfräsen</td>
                                            <td class="mono right">2,7 min</td>
                                            <td><input type="number" class="input input-sm input-mono" style="width: 70px;" step="0.1" onchange="updateFeedbackDelta(this)"></td>
                                            <td class="mono right" data-delta>—</td>
                                            <td>
                                                <select class="input input-sm" style="width: 130px;">
                                                    <option value="">—</option>
                                                    <option value="einrichtung">Einrichtung</option>
                                                    <option value="werkzeug">Werkzeug</option>
                                                    <option value="material">Material</option>
                                                    <option value="toleranz">Toleranz</option>
                                                    <option value="nc">NC-Programm</option>
                                                    <option value="sonstiges">Sonstiges</option>
                                                </select>
                                            </td>
                                            <td><input type="text" class="input input-sm" placeholder="z.B. Fräskanten nötig"></td>
                                        </tr>
                                        <tr>
                                            <td class="mono">OP20</td>
                                            <td>Kontur schruppen</td>
                                            <td class="mono right">8,0 min</td>
                                            <td><input type="number" class="input input-sm input-mono" style="width: 70px;" step="0.1" onchange="updateFeedbackDelta(this)"></td>
                                            <td class="mono right" data-delta>—</td>
                                            <td>
                                                <select class="input input-sm" style="width: 130px;">
                                                    <option value="">—</option>
                                                    <option value="einrichtung">Einrichtung</option>
                                                    <option value="werkzeug">Werkzeug</option>
                                                    <option value="material">Material</option>
                                                    <option value="toleranz">Toleranz</option>
                                                    <option value="nc">NC-Programm</option>
                                                    <option value="sonstiges">Sonstiges</option>
                                                </select>
                                            </td>
                                            <td><input type="text" class="input input-sm" placeholder=""></td>
                                        </tr>
                                        <tr style="background: rgba(254,226,226,0.3);">
                                            <td class="mono" style="color: var(--color-error);">OP50</td>
                                            <td>Schlichten h5 ⚠️</td>
                                            <td class="mono right">5,1 min</td>
                                            <td><input type="number" class="input input-sm input-mono" style="width: 70px;" step="0.1" onchange="updateFeedbackDelta(this)"></td>
                                            <td class="mono right" data-delta>—</td>
                                            <td>
                                                <select class="input input-sm" style="width: 130px;">
                                                    <option value="">—</option>
                                                    <option value="einrichtung">Einrichtung</option>
                                                    <option value="werkzeug">Werkzeug</option>
                                                    <option value="material">Material</option>
                                                    <option value="toleranz" selected>Toleranz</option>
                                                    <option value="nc">NC-Programm</option>
                                                    <option value="sonstiges">Sonstiges</option>
                                                </select>
                                            </td>
                                            <td><input type="text" class="input input-sm" placeholder="z.B. 3× nachgemessen"></td>
                                        </tr>
                                        <tr style="background: rgba(254,226,226,0.3);">
                                            <td class="mono" style="color: var(--color-error);">OP60</td>
                                            <td>Feinbohren H7 ⚠️</td>
                                            <td class="mono right">4,1 min</td>
                                            <td><input type="number" class="input input-sm input-mono" style="width: 70px;" step="0.1" onchange="updateFeedbackDelta(this)"></td>
                                            <td class="mono right" data-delta>—</td>
                                            <td>
                                                <select class="input input-sm" style="width: 130px;">
                                                    <option value="">—</option>
                                                    <option value="einrichtung">Einrichtung</option>
                                                    <option value="werkzeug">Werkzeug</option>
                                                    <option value="material">Material</option>
                                                    <option value="toleranz">Toleranz</option>
                                                    <option value="nc">NC-Programm</option>
                                                    <option value="sonstiges">Sonstiges</option>
                                                </select>
                                            </td>
                                            <td><input type="text" class="input input-sm" placeholder=""></td>
                                        </tr>
                                    </tbody>
                                    <tfoot style="background: var(--color-bg); font-weight: 600;">
                                        <tr>
                                            <td colspan="2">Einrichtung (Setup)</td>
                                            <td class="mono right">25 min</td>
                                            <td><input type="number" class="input input-sm input-mono" style="width: 70px;" id="fbSetupIst" step="1" onchange="updateSetupDelta()"></td>
                                            <td class="mono right" id="fbSetupDelta">—</td>
                                            <td>
                                                <select class="input input-sm" style="width: 130px;" id="fbSetupGrund">
                                                    <option value="">—</option>
                                                    <option value="fraeskanten">Fräskanten</option>
                                                    <option value="ausrichten">Ausrichten</option>
                                                    <option value="nullpunkt">Nullpunkt</option>
                                                    <option value="spannung">Spannung</option>
                                                    <option value="sonstiges">Sonstiges</option>
                                                </select>
                                            </td>
                                            <td><input type="text" class="input input-sm" id="fbSetupNotiz" placeholder="z.B. Fräskanten für Parallelspanner"></td>
                                        </tr>
                                        <tr style="background: var(--color-primary); color: white;">
                                            <td colspan="2">GESAMT</td>
                                            <td class="mono right">42 min</td>
                                            <td class="mono right" id="fbGesamtIst">— min</td>
                                            <td class="mono right" id="fbGesamtDelta">—</td>
                                            <td colspan="2"></td>
                                        </tr>
                                    </tfoot>
                                </table>
                                
                                <div class="grid-2" style="gap: var(--space-5);">
                                    <div>
                                        <div style="font-weight: 600; margin-bottom: var(--space-3);">Ergebnis</div>
                                        <div style="display: flex; flex-direction: column; gap: var(--space-2);">
                                            <label style="display: flex; align-items: center; gap: var(--space-2); cursor: pointer;">
                                                <input type="radio" name="fbErgebnis" value="io_erst" checked> ✅ Teil i.O. (Erstfertigung)
                                            </label>
                                            <label style="display: flex; align-items: center; gap: var(--space-2); cursor: pointer;">
                                                <input type="radio" name="fbErgebnis" value="io_korrektur"> ✅ Teil i.O. (nach Korrektur)
                                            </label>
                                            <label style="display: flex; align-items: center; gap: var(--space-2); cursor: pointer;">
                                                <input type="radio" name="fbErgebnis" value="nacharbeit"> ⚠️ Nacharbeit nötig
                                            </label>
                                            <label style="display: flex; align-items: center; gap: var(--space-2); cursor: pointer;">
                                                <input type="radio" name="fbErgebnis" value="ausschuss"> ❌ Ausschuss
                                            </label>
                                        </div>
                                    </div>
                                    <div>
                                        <div style="font-weight: 600; margin-bottom: var(--space-3);">Empfehlung für nächstes Mal</div>
                                        <textarea class="input" id="fbEmpfehlung" rows="4" placeholder="Was sollte bei der nächsten Kalkulation anders sein? z.B. 'Vorschub bei h5 um 20% reduzieren'"></textarea>
                                    </div>
                                </div>
                            </div>
                        </div>
                        
                        <div style="display: flex; gap: var(--space-3);">
                            <button class="btn btn-primary" onclick="saveFeedback()">💾 Feedback speichern</button>
                            <button class="btn btn-secondary" onclick="clearFeedbackForm()">🗑️ Formular leeren</button>
                        </div>
                    </div>
                    
                    <!-- TAB: Cross-Learnings -->
                    <div id="feedback-learnings" style="display: none;">
                        
                        <!-- Kalkulations-Genauigkeit -->
                        <div class="card" style="margin-bottom: var(--space-5);">
                            <div class="card-header card-header-primary"><span>📈 Kalkulations-Genauigkeit</span></div>
                            <div class="card-body">
                                <div class="grid-3" style="gap: var(--space-5); text-align: center;">
                                    <div>
                                        <div style="font-size: 32px; font-weight: 700; color: var(--color-warning);" id="avgDeviation">+18%</div>
                                        <div style="font-size: 12px; color: var(--color-text-muted);">Ø Abweichung</div>
                                        <div style="font-size: 11px; color: var(--color-text-muted);">(Ziel: ±15%)</div>
                                    </div>
                                    <div>
                                        <div style="font-size: 32px; font-weight: 700; color: var(--color-primary);" id="feedbackCount">12</div>
                                        <div style="font-size: 12px; color: var(--color-text-muted);">Feedbacks</div>
                                        <div style="font-size: 11px; color: var(--color-text-muted);">erfasst</div>
                                    </div>
                                    <div>
                                        <div style="font-size: 32px; font-weight: 700; color: var(--color-success);" id="patternsFound">3</div>
                                        <div style="font-size: 12px; color: var(--color-text-muted);">Muster</div>
                                        <div style="font-size: 11px; color: var(--color-text-muted);">erkannt</div>
                                    </div>
                                </div>
                                
                                <div style="margin-top: var(--space-5);">
                                    <div style="font-size: 12px; color: var(--color-text-muted); margin-bottom: var(--space-2);">Häufigste Zeitfresser</div>
                                    <div style="display: flex; flex-direction: column; gap: var(--space-2);">
                                        <div style="display: flex; align-items: center; gap: var(--space-3);">
                                            <span style="width: 100px; font-size: 13px;">Einrichtung</span>
                                            <div style="flex: 1; height: 20px; background: var(--color-bg); border-radius: var(--radius-sm); overflow: hidden;">
                                                <div style="width: 72%; height: 100%; background: var(--color-error);"></div>
                                            </div>
                                            <span class="mono" style="width: 50px; text-align: right; color: var(--color-error);">+18%</span>
                                        </div>
                                        <div style="display: flex; align-items: center; gap: var(--space-3);">
                                            <span style="width: 100px; font-size: 13px;">Toleranz</span>
                                            <div style="flex: 1; height: 20px; background: var(--color-bg); border-radius: var(--radius-sm); overflow: hidden;">
                                                <div style="width: 60%; height: 100%; background: var(--color-warning);"></div>
                                            </div>
                                            <span class="mono" style="width: 50px; text-align: right; color: var(--color-warning);">+15%</span>
                                        </div>
                                        <div style="display: flex; align-items: center; gap: var(--space-3);">
                                            <span style="width: 100px; font-size: 13px;">Bearbeitung</span>
                                            <div style="flex: 1; height: 20px; background: var(--color-bg); border-radius: var(--radius-sm); overflow: hidden;">
                                                <div style="width: 12%; height: 100%; background: var(--color-success);"></div>
                                            </div>
                                            <span class="mono" style="width: 50px; text-align: right; color: var(--color-success);">+3%</span>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        
                        <!-- Erkannte Muster -->
                        <div class="card" style="margin-bottom: var(--space-5);">
                            <div class="card-header card-header-warning"><span>🔄 Erkannte Muster</span></div>
                            <div class="card-body" style="padding: 0;">
                                <div id="patternsContainer">
                                    
                                    <!-- Muster 1 -->
                                    <div style="padding: var(--space-4); border-bottom: 1px solid var(--color-border-light);">
                                        <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: var(--space-3);">
                                            <div>
                                                <div style="font-weight: 600; color: var(--color-text);">Einrichtzeit bei Parallelspanner</div>
                                                <div style="font-size: 12px; color: var(--color-text-muted);">Häufigkeit: 8/12 Aufträge (67%) • Ø Mehraufwand: +12 min</div>
                                            </div>
                                            <span style="background: var(--color-error-light); color: var(--color-error); padding: 2px 8px; border-radius: var(--radius-sm); font-size: 11px; font-weight: 600;">HOCH</span>
                                        </div>
                                        <div style="background: var(--color-bg); padding: var(--space-3); border-radius: var(--radius-md); margin-bottom: var(--space-3);">
                                            <div style="font-size: 12px; color: var(--color-text-muted); margin-bottom: var(--space-1);">Ursache</div>
                                            <div style="font-size: 13px;">Fräskanten für Parallelspanner fehlen in der Kalkulation. Werker müssen zusätzlich Flächen anfräsen.</div>
                                        </div>
                                        <div style="display: flex; align-items: center; gap: var(--space-3);">
                                            <span style="font-size: 13px;">💡 <strong>Vorschlag:</strong> Setup-Zeit +15 min bei Spannart "Parallelspanner"</span>
                                            <button class="btn btn-sm btn-primary" onclick="applyPattern('setup_parallel', 15)">Anwenden</button>
                                            <button class="btn btn-sm btn-secondary" onclick="ignorePattern('setup_parallel')">Ignorieren</button>
                                        </div>
                                    </div>
                                    
                                    <!-- Muster 2 -->
                                    <div style="padding: var(--space-4); border-bottom: 1px solid var(--color-border-light);">
                                        <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: var(--space-3);">
                                            <div>
                                                <div style="font-weight: 600; color: var(--color-text);">Toleranz h5/H7 unterschätzt</div>
                                                <div style="font-size: 12px; color: var(--color-text-muted);">Häufigkeit: 5/7 Passungen (71%) • Ø Mehraufwand: +4 min pro Passung</div>
                                            </div>
                                            <span style="background: var(--color-warning-light); color: var(--color-warning); padding: 2px 8px; border-radius: var(--radius-sm); font-size: 11px; font-weight: 600;">MITTEL</span>
                                        </div>
                                        <div style="background: var(--color-bg); padding: var(--space-3); border-radius: var(--radius-md); margin-bottom: var(--space-3);">
                                            <div style="font-size: 12px; color: var(--color-text-muted); margin-bottom: var(--space-1);">Ursache</div>
                                            <div style="font-size: 13px;">Messzeit und reduzierter Vorschub bei engen Toleranzen nicht ausreichend einkalkuliert.</div>
                                        </div>
                                        <div style="display: flex; align-items: center; gap: var(--space-3);">
                                            <span style="font-size: 13px;">💡 <strong>Vorschlag:</strong> Toleranz-Faktor 1.3× für h5/H7</span>
                                            <button class="btn btn-sm btn-primary" onclick="applyPattern('tolerance_factor', 1.3)">Anwenden</button>
                                            <button class="btn btn-sm btn-secondary" onclick="ignorePattern('tolerance_factor')">Ignorieren</button>
                                        </div>
                                    </div>
                                    
                                    <!-- Muster 3 -->
                                    <div style="padding: var(--space-4);">
                                        <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: var(--space-3);">
                                            <div>
                                                <div style="font-weight: 600; color: var(--color-text);">Material S235: Rohteil-Übermaß</div>
                                                <div style="font-size: 12px; color: var(--color-text-muted);">Häufigkeit: 4/10 Aufträge (40%) • Ø Mehraufwand: +3 min</div>
                                            </div>
                                            <span style="background: var(--color-info-light); color: var(--color-info); padding: 2px 8px; border-radius: var(--radius-sm); font-size: 11px; font-weight: 600;">NIEDRIG</span>
                                        </div>
                                        <div style="background: var(--color-bg); padding: var(--space-3); border-radius: var(--radius-md); margin-bottom: var(--space-3);">
                                            <div style="font-size: 12px; color: var(--color-text-muted); margin-bottom: var(--space-1);">Ursache</div>
                                            <div style="font-size: 13px;">S235 Rohteile haben oft 0.3-0.5mm Übermaß. Zusätzlicher Planfräs-Durchgang nötig.</div>
                                        </div>
                                        <div style="display: flex; align-items: center; gap: var(--space-3);">
                                            <span style="font-size: 13px;">💡 <strong>Vorschlag:</strong> Rohteil-Aufmaß auf 1.0mm bei S235</span>
                                            <button class="btn btn-sm btn-primary" onclick="applyPattern('s235_aufmass', 1.0)">Anwenden</button>
                                            <button class="btn btn-sm btn-secondary" onclick="ignorePattern('s235_aufmass')">Ignorieren</button>
                                        </div>
                                    </div>
                                    
                                </div>
                            </div>
                        </div>
                        
                        <!-- Empfehlungen aus Feedback -->
                        <div class="card">
                            <div class="card-header"><span>💡 Empfehlungen aus Feedback</span></div>
                            <div class="card-body" style="padding: 0;">
                                <div id="recommendationsContainer">
                                    <div style="padding: var(--space-3) var(--space-4); border-bottom: 1px solid var(--color-border-light); display: flex; align-items: center; gap: var(--space-3);">
                                        <span style="font-size: 18px;">📌</span>
                                        <div style="flex: 1;">
                                            <div style="font-size: 13px;">"Bei Parallelspanner Fräskanten einplanen"</div>
                                            <div style="font-size: 11px; color: var(--color-text-muted);">3× gemeldet • Zuletzt: 05.02.2026</div>
                                        </div>
                                    </div>
                                    <div style="padding: var(--space-3) var(--space-4); border-bottom: 1px solid var(--color-border-light); display: flex; align-items: center; gap: var(--space-3);">
                                        <span style="font-size: 18px;">📌</span>
                                        <div style="flex: 1;">
                                            <div style="font-size: 13px;">"h5-Toleranz: Vorschub -20%, Messzeit einplanen"</div>
                                            <div style="font-size: 11px; color: var(--color-text-muted);">2× gemeldet • Zuletzt: 04.02.2026</div>
                                        </div>
                                    </div>
                                    <div style="padding: var(--space-3) var(--space-4); display: flex; align-items: center; gap: var(--space-3);">
                                        <span style="font-size: 18px;">📌</span>
                                        <div style="flex: 1;">
                                            <div style="font-size: 13px;">"S235 Rohteil oft mit Übermaß — erst planfräsen"</div>
                                            <div style="font-size: 11px; color: var(--color-text-muted);">1× gemeldet • Zuletzt: 03.02.2026</div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        
                    </div>
                    
                    <!-- TAB: Historie -->
                    <div id="feedback-historie" style="display: none;">
                        <div class="card">
                            <div class="card-header">
                                <span>📋 Feedback-Historie</span>
                                <div>
                                    <button class="btn btn-sm btn-secondary" onclick="exportFeedbackCSV()">📤 Export CSV</button>
                                </div>
                            </div>
                            <div class="card-body" style="padding: 0; overflow-x: auto;">
                                <table class="table">
                                    <thead>
                                        <tr>
                                            <th>Datum</th>
                                            <th>Projekt</th>
                                            <th>Erfasser</th>
                                            <th class="right">Kalk.</th>
                                            <th class="right">Ist</th>
                                            <th class="right">Delta</th>
                                            <th>Hauptgrund</th>
                                            <th>Ergebnis</th>
                                        </tr>
                                    </thead>
                                    <tbody id="feedbackHistoryTable">
                                        <tr>
                                            <td class="mono">05.02.2026</td>
                                            <td class="mono">2500473.01</td>
                                            <td>M. Schmidt</td>
                                            <td class="mono right">42 min</td>
                                            <td class="mono right">48 min</td>
                                            <td class="mono right" style="color: var(--color-error);">+14%</td>
                                            <td>Einrichtung</td>
                                            <td>✅ i.O.</td>
                                        </tr>
                                        <tr>
                                            <td class="mono">04.02.2026</td>
                                            <td class="mono">2500112.03</td>
                                            <td>K. Weber</td>
                                            <td class="mono right">28 min</td>
                                            <td class="mono right">26 min</td>
                                            <td class="mono right" style="color: var(--color-success);">-7%</td>
                                            <td>—</td>
                                            <td>✅ i.O.</td>
                                        </tr>
                                        <tr>
                                            <td class="mono">03.02.2026</td>
                                            <td class="mono">2500098.01</td>
                                            <td>M. Schmidt</td>
                                            <td class="mono right">35 min</td>
                                            <td class="mono right">43 min</td>
                                            <td class="mono right" style="color: var(--color-error);">+23%</td>
                                            <td>Toleranz</td>
                                            <td>⚠️ Nacharbeit</td>
                                        </tr>
                                        <tr>
                                            <td class="mono">02.02.2026</td>
                                            <td class="mono">2500087.02</td>
                                            <td>T. Müller</td>
                                            <td class="mono right">52 min</td>
                                            <td class="mono right">55 min</td>
                                            <td class="mono right" style="color: var(--color-warning);">+6%</td>
                                            <td>Material</td>
                                            <td>✅ i.O.</td>
                                        </tr>
                                        <tr>
                                            <td class="mono">01.02.2026</td>
                                            <td class="mono">2500076.01</td>
                                            <td>K. Weber</td>
                                            <td class="mono right">18 min</td>
                                            <td class="mono right">17 min</td>
                                            <td class="mono right" style="color: var(--color-success);">-6%</td>
                                            <td>—</td>
                                            <td>✅ i.O.</td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                        </div>
                        
                        <div class="info-box" style="margin-top: var(--space-4);">
                            <strong>Daten:</strong> 12 Feedback-Einträge • Ø Abweichung: +18% • 
                            <span style="color: var(--color-success);">83% i.O.</span> • 
                            <span style="color: var(--color-warning);">17% Nacharbeit</span>
                        </div>
                    </div>
                    
                </div>
                
                <!-- ========================================
                     SECTION: EINSTELLUNGEN
                     ======================================== -->
                <div class="section" id="section-settings">
                    <!-- TAB: Firmendaten -->
                    <div id="settings-firma">
                        <div class="card">
                            <div class="card-header"><span>🏢 Firmendaten (für Angebote & Dokumente)</span></div>
                            <div class="card-body">
                                <div class="grid-2" style="gap: var(--space-4);">
                                    <div class="form-group">
                                        <label class="form-label">Firmenname</label>
                                        <input type="text" class="input" value="Muster CNC GmbH" id="firmaName">
                                    </div>
                                    <div class="form-group">
                                        <label class="form-label">Ansprechpartner</label>
                                        <input type="text" class="input" value="Max Mustermann" id="firmaAnsprech">
                                    </div>
                                    <div class="form-group">
                                        <label class="form-label">Straße</label>
                                        <input type="text" class="input" value="Industriestraße 42" id="firmaStrasse">
                                    </div>
                                    <div class="form-group">
                                        <label class="form-label">PLZ / Ort</label>
                                        <input type="text" class="input" value="01234 Musterstadt" id="firmaOrt">
                                    </div>
                                    <div class="form-group">
                                        <label class="form-label">Telefon</label>
                                        <input type="text" class="input" value="+49 123 456789" id="firmaTel">
                                    </div>
                                    <div class="form-group">
                                        <label class="form-label">E-Mail</label>
                                        <input type="email" class="input" value="info@muster-cnc.de" id="firmaEmail">
                                    </div>
                                    <div class="form-group">
                                        <label class="form-label">Steuernummer</label>
                                        <input type="text" class="input" value="DE123456789" id="firmaSteuer">
                                    </div>
                                    <div class="form-group">
                                        <label class="form-label">Bankverbindung</label>
                                        <input type="text" class="input" value="DE89 3704 0044 0532 0130 00" id="firmaIBAN">
                                    </div>
                                </div>
                            </div>
                        </div>
                        
                        <div class="card" style="margin-top: var(--space-5);">
                            <div class="card-header"><span>Angebotseinstellungen</span></div>
                            <div class="card-body">
                                <div class="grid-3" style="gap: var(--space-4);">
                                    <div class="form-group" style="margin-bottom: 0;">
                                        <label class="form-label">Gültigkeit (Tage)</label>
                                        <input type="number" class="input input-mono" value="30" id="angebotsGueltigkeit">
                                    </div>
                                    <div class="form-group" style="margin-bottom: 0;">
                                        <label class="form-label">Standard-Lieferzeit</label>
                                        <input type="text" class="input" value="3-4 Wochen" id="standardLieferzeit">
                                    </div>
                                    <div class="form-group" style="margin-bottom: 0;">
                                        <label class="form-label">Zahlungsziel (Tage)</label>
                                        <input type="number" class="input input-mono" value="14" id="zahlungsziel">
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <!-- Buttons -->
                    <div style="margin-top: var(--space-5); display: flex; gap: var(--space-3); padding-top: var(--space-4); border-top: 1px solid var(--color-border);">
                        <button class="btn btn-primary" onclick="saveSettings()">💾 Einstellungen speichern</button>
                        <button class="btn btn-secondary" onclick="resetSettings()">↺ Zurücksetzen</button>
                        <button class="btn btn-secondary" style="margin-left: auto;" onclick="exportSettings()">📤 Export</button>
                        <button class="btn btn-secondary" onclick="importSettings()">📥 Import</button>
                    </div>
                    
                    <p style="margin-top: var(--space-4); font-size: 12px; color: var(--color-text-muted);">
                        Einstellungen werden lokal im Browser gespeichert (localStorage). Export erstellt eine JSON-Datei für Backup oder Übertragung auf andere Geräte.
                    </p>
                </div>
            </div>
        </main>
    </div>
    
    <!-- ================================================================
         JAVASCRIPT
         ================================================================ -->
    <script>
        // ================================================================
        // DATA
        // ================================================================
        
        const MATERIALS = {
            // Edelstahl
            '1.4301': { name: '1.4301 (V2A)', price: 8.50, density: 7.90, timeFactor: 1.25 },
            '1.4404': { name: '1.4404 (V4A)', price: 12.00, density: 7.95, timeFactor: 1.30 },
            '1.4571': { name: '1.4571', price: 14.00, density: 8.00, timeFactor: 1.35 },
            // Baustahl
            'S235JR': { name: 'S235JR', price: 6.79, density: 7.85, timeFactor: 1.00 },
            'S355J2': { name: 'S355J2', price: 7.50, density: 7.85, timeFactor: 1.02 },
            'C45': { name: 'C45', price: 3.50, density: 7.85, timeFactor: 1.05 },
            // Vergütungsstahl
            '42CrMo4': { name: '42CrMo4', price: 4.20, density: 7.85, timeFactor: 1.15 },
            '34CrNiMo6': { name: '34CrNiMo6', price: 5.50, density: 7.85, timeFactor: 1.20 },
            // Aluminium
            'AlMg3': { name: 'AlMg3', price: 6.50, density: 2.66, timeFactor: 0.65 },
            'AlMgSi1': { name: 'AlMgSi1', price: 7.00, density: 2.70, timeFactor: 0.68 },
            'Al7075': { name: 'Al7075-T6', price: 12.00, density: 2.81, timeFactor: 0.75 },
            // Buntmetalle
            'CuZn39Pb3': { name: 'Messing', price: 8.50, density: 8.47, timeFactor: 0.70 },
            'CuSn8': { name: 'Bronze', price: 15.00, density: 8.80, timeFactor: 0.75 },
            // Kunststoff
            'POM': { name: 'POM', price: 4.50, density: 1.41, timeFactor: 0.45 },
            'PA6': { name: 'PA6 (Nylon)', price: 5.00, density: 1.14, timeFactor: 0.50 },
            'PEEK': { name: 'PEEK', price: 85.00, density: 1.32, timeFactor: 0.55 }
        };
        
        const CLAMPING = {
            'schraubstock': { time: 15, desc: 'Teil in Maschinenschraubstock spannen, Parallelität prüfen, Nullpunkt antasten.' },
            'schraubstock2': { time: 25, desc: 'Zwei Schraubstöcke für Langteile. Beide auf gleiche Höhe ausrichten.' },
            'tischspannung': { time: 35, desc: 'Tischspannung mit Pratzen. Für große oder unregelmäßige Werkstücke.' },
            'nullpunkt': { time: 5, desc: 'Nullpunktspannsystem. Schnellstes Wechseln, höchste Wiederholgenauigkeit.' },
            'spezial': { time: 45, desc: 'Sondervorrichtung. Aufwändiger Aufbau, für Serienteile rentabel.' }
        };
        
        const PROJECTS = {
            verbindungsplatte: {
                id: 'verbindungsplatte',
                name: 'Verbindungsplatte',
                partNumber: '2500473.01.11.02.00.001',
                material: 'S235JR',
                dims: { x: 440, y: 50, z: 20 },
                baseTime: 12.5,
                unitPrice: 28.40,
                thumbnail: 'demo-parts/2500473.01.11.02.00.001.pdf.png'
            },
            adapterplatte: {
                id: 'adapterplatte',
                name: 'Adapterplatte',
                partNumber: '2500473.01.01.02.01.001',
                material: 'AlMg3',
                dims: { x: 85, y: 70, z: 55 },
                baseTime: 24.8,
                unitPrice: 52.15,
                thumbnail: 'demo-parts/2500473.01.01.02.01.001.pdf.png'
            }
        };
        
        let RATES = {
            cnc: { labor: 49, machine: 42 },
            saegen: { labor: 43, machine: 12 },
            entgraten: { labor: 32, machine: 4 }
        };
        
        let currentProject = null;
        
        // ================================================================
        // NAVIGATION
        // ================================================================
        
        const SECTION_TITLES = {
            'part': 'Teil',
            'params': 'Parameter',
            'result': 'Kalkulation',
            'calculation': 'Detailkalkulation',
            'tools': 'Werkzeuge',
            'quote': 'Angebot',
            'instructions': 'Fertigungsanweisung',
            'code': 'NC-Code',
            'feedback': 'Feedback',
            'settings': 'Einstellungen'
        };
        
        function confirmAndGoToParams() {
            const isConfirmed = confirm(
                'Bitte prüfen Sie alle Eingaben:\n\n' +
                '• Werkstoff korrekt gewählt?\n' +
                '• Rohmaße vollständig?\n' +
                '• Stückzahl eingetragen?\n\n' +
                'Mit diesen Angaben zu den Parametern fortfahren?'
            );
            
            if (isConfirmed) {
                const paramBtn = document.querySelector('[data-section="params"]');
                showSection('params', paramBtn);
            }
        }
        
        function showSection(name, btn) {
            document.querySelectorAll('.nav-item').forEach(item => item.classList.remove('active'));
            if (btn) btn.classList.add('active');
            
            document.querySelectorAll('.section').forEach(section => section.classList.remove('active'));
            
            if (name === 'instructions') {
                document.getElementById('section-instructions').classList.add('active');
                document.getElementById('mainTitle').textContent = SECTION_TITLES[name] || name;
                return;
            }
            
            if (name === 'result') {
                document.getElementById('section-result').classList.add('active');
                document.getElementById('section-calculation').classList.add('active');
                document.getElementById('mainTitle').textContent = SECTION_TITLES[name] || name;
                return;
            }
            
            document.getElementById('section-' + name).classList.add('active');
            document.getElementById('mainTitle').textContent = SECTION_TITLES[name] || name;
        }
        
        function showParamTab(tab) {
            document.getElementById('param-fertigung').style.display = 'none';
            document.getElementById('param-preis').style.display = 'none';
            document.getElementById('param-maschine').style.display = 'none';
            
            document.getElementById('tabParamFertigung').className = 'btn btn-sm btn-secondary';
            document.getElementById('tabParamPreis').className = 'btn btn-sm btn-secondary';
            document.getElementById('tabParamMaschine').className = 'btn btn-sm btn-secondary';
            
            document.getElementById('param-' + tab).style.display = 'block';
            if (tab === 'fertigung') {
                document.getElementById('tabParamFertigung').className = 'btn btn-sm btn-primary';
            } else if (tab === 'preis') {
                document.getElementById('tabParamPreis').className = 'btn btn-sm btn-primary';
            } else if (tab === 'maschine') {
                document.getElementById('tabParamMaschine').className = 'btn btn-sm btn-primary';
            }
        }
        
        function toggleScope() {
            const content = document.getElementById('scopeContent');
            const chevron = document.getElementById('scopeChevron');
            content.classList.toggle('expanded');
            chevron.style.transform = content.classList.contains('expanded') ? 'rotate(180deg)' : 'rotate(0)';
        }
        
        function toggleDrawing(contentId = 'drawingContent', chevronId = 'drawingChevron') {
            const content = document.getElementById(contentId);
            const chevron = document.getElementById(chevronId);
            if (content.style.display === 'none') {
                content.style.display = 'block';
                chevron.textContent = '▼';
            } else {
                content.style.display = 'none';
                chevron.textContent = '▶';
            }
        }
        
        function openDrawingFullscreen(imageId = 'drawingImage') {
            const img = document.getElementById(imageId);
            if (img && img.src) {
                window.open(img.src, '_blank');
            }
        }
        
        function toggleOpDetail(opId) {
            const detail = document.getElementById(opId + '-detail');
            if (detail) {
                detail.style.display = detail.style.display === 'none' ? 'block' : 'none';
            }
        }
        
        // ================================================================
        // PART SELECTION
        // ================================================================
        
        function renderPartGrid() {
            const grid = document.getElementById('partGrid');
            grid.innerHTML = Object.values(PROJECTS).map(p => `
                <div class="part-card ${currentProject?.id === p.id ? 'selected' : ''}" onclick="selectProject('${p.id}')">
                    <div class="part-thumb">
                        <img src="${p.thumbnail}" alt="${p.name}" onerror="this.parentElement.innerHTML='<span style=\\'color:var(--color-text-muted);font-size:11px;\\'>Keine Vorschau</span>'">
                    </div>
                    <div class="part-info">
                        <div class="part-name">${p.name}</div>
                        <div class="part-number">${p.partNumber}</div>
                        <div class="part-meta">
                            <span>${p.baseTime} min</span>
                            <span>${p.material}</span>
                            <span class="part-price">€${p.unitPrice.toFixed(2).replace('.', ',')}</span>
                        </div>
                    </div>
                </div>
            `).join('');
        }
        
        function selectProject(id) {
            currentProject = PROJECTS[id];
            
            // Show loading animation
            showLoading();
            
            document.getElementById('materialSelect').value = currentProject.material;
            document.getElementById('dimX').value = currentProject.dims.x;
            document.getElementById('dimY').value = currentProject.dims.y;
            document.getElementById('dimZ').value = currentProject.dims.z;
            
            renderPartGrid();
            calculate();
            
            // Update instruction header
            document.getElementById('faPartName').textContent = `${currentProject.name} — ${currentProject.partNumber}`;
            document.getElementById('quoteDesc').textContent = `${currentProject.name} ${currentProject.partNumber}`;
            
            // Show params section after loading completes
            setTimeout(() => {
                showSection('params', document.querySelector('.nav-item[data-section="params"]'));
            }, 2500);
        }
        
        // ================================================================
        // CALCULATION
        // ================================================================
        
        function calculate() {
            const mat = MATERIALS[document.getElementById('materialSelect').value];
            const x = parseFloat(document.getElementById('dimX').value) || 100;
            const y = parseFloat(document.getElementById('dimY').value) || 100;
            const z = parseFloat(document.getElementById('dimZ').value) || 20;
            const qty = parseInt(document.getElementById('quantity').value) || 1;
            const margin = parseFloat(document.getElementById('marginInput').value) || 10;
            const scrap = parseFloat(document.getElementById('settingScrap')?.value) || 10;
            const toolWear = parseFloat(document.getElementById('settingToolWear')?.value) || 20.74;
            const vat = parseFloat(document.getElementById('settingVat')?.value) || 19;
            
            // Clamping
            const clampingType = document.getElementById('clampingSelect').value;
            const clampingData = CLAMPING[clampingType];
            const setupCount = parseInt(document.getElementById('setupCount').value) || 1;
            const totalSetupTime = clampingData.time + (setupCount - 1) * (clampingData.time * 0.6);
            
            // Update clamping description
            document.getElementById('clampingDescription').textContent = clampingData.desc;
            
            // Rates
            const cncRate = RATES.cnc.labor + RATES.cnc.machine;
            const entgratenRate = RATES.entgraten.labor + RATES.entgraten.machine;
            const saegenRate = RATES.saegen.labor + RATES.saegen.machine;
            
            // Setup cost
            const setupCost = (totalSetupTime / 60) * cncRate;
            const setupCostPerPiece = setupCost / qty;
            
            // Volume & Weight
            const volumeMm3 = x * y * z;
            const volumeCm3 = volumeMm3 / 1000;
            const weightKg = (volumeCm3 * mat.density) / 1000;
            
            // Material cost
            const materialCost = weightKg * mat.price * (1 + scrap / 100);
            
            // Machining time
            const refVolume = currentProject ? (currentProject.dims.x * currentProject.dims.y * currentProject.dims.z) / 1000 : 440;
            const baseTime = currentProject ? currentProject.baseTime : 12.5;
            const sizeFactor = volumeCm3 / refVolume;
            const machiningTime = baseTime * Math.pow(sizeFactor, 0.7) * mat.timeFactor;
            
            // Machine cost
            const machineCost = (machiningTime / 60) * cncRate;
            
            // Additional operations
            let additionalCost = 0;
            let additionalDesc = [];
            
            if (document.getElementById('opEntgraten').checked) {
                const t = parseFloat(document.getElementById('opEntgratenTime').value) || 5;
                additionalCost += (t / 60) * entgratenRate;
                additionalDesc.push('Entgraten ' + t + ' min');
            }
            if (document.getElementById('opSaegen').checked) {
                const t = parseFloat(document.getElementById('opSaegenTime').value) || 3;
                additionalCost += (t / 60) * saegenRate;
                additionalDesc.push('Sägen ' + t + ' min');
            }
            if (document.getElementById('opPruefung').checked) {
                const t = parseFloat(document.getElementById('opPruefungTime').value) || 5;
                additionalCost += (t / 60) * cncRate;
                additionalDesc.push('Prüfung ' + t + ' min');
            }
            
            // Tool cost
            const toolCost = toolWear * mat.timeFactor;
            
            // ================================================================
            // ZUSCHLAGSKALKULATION (Industriestandard)
            // ================================================================
            
            // Zuschlagssätze aus Einstellungen lesen
            const zuschlagMGK = parseFloat(document.getElementById('zuschlagMGK')?.value) || 10;      // Materialgemeinkosten
            const zuschlagAV = parseFloat(document.getElementById('zuschlagAV')?.value) || 8;        // AV-Aufschlag
            const zuschlagVwGK = parseFloat(document.getElementById('zuschlagVwGK')?.value) || 12;   // Verwaltung
            const zuschlagVtGK = parseFloat(document.getElementById('zuschlagVtGK')?.value) || 5;    // Vertrieb
            const zuschlagGewinn = parseFloat(document.getElementById('zuschlagGewinn')?.value) || 10; // Gewinn
            
            // 1. Materialkosten + MGK
            const materialMitGK = materialCost * (1 + zuschlagMGK / 100);
            
            // 2. Fertigungskosten (Maschine + Rüsten + Nebenzeiten)
            const fertigungskosten = machineCost + setupCostPerPiece + additionalCost;
            
            // 3. Fertigungskosten + AV-Aufschlag
            const fertigungMitAV = fertigungskosten * (1 + zuschlagAV / 100);
            
            // 4. HERSTELLKOSTEN (HK)
            const herstellkosten = materialMitGK + fertigungMitAV + toolCost;
            
            // 5. + Verwaltungs-GK + Vertriebs-GK = SELBSTKOSTEN (SK)
            const vwGKBetrag = herstellkosten * (zuschlagVwGK / 100);
            const vtGKBetrag = herstellkosten * (zuschlagVtGK / 100);
            const selbstkosten = herstellkosten + vwGKBetrag + vtGKBetrag;
            
            // 6. + Gewinn = ANGEBOTSPREIS
            const gewinnBetrag = selbstkosten * (zuschlagGewinn / 100);
            const angebotspreis = selbstkosten + gewinnBetrag;
            
            // Für Kompatibilität: alte Variablen updaten
            const totalCost = herstellkosten;  // Herstellkosten als "Kosten"
            const marginAmount = gewinnBetrag;
            const sellPrice = angebotspreis;
            const orderTotal = sellPrice * qty;
            const mwstAmount = orderTotal * (vat / 100);
            const totalWithVat = orderTotal + mwstAmount;
            
            // Deckungsbeitrag
            const deckungsbeitrag = angebotspreis - (materialCost + fertigungskosten + toolCost);
            const dbProzent = (deckungsbeitrag / angebotspreis) * 100;
            
            // Confidence
            let confidenceClass = 'confidence-medium';
            let confidenceText = '🟡 ±15% — Standardteil';
            if (mat.timeFactor > 1.2) {
                confidenceClass = 'confidence-low';
                confidenceText = '🔴 ±25% — Schwerzerspanbarer Werkstoff';
            } else if (currentProject && Math.abs(volumeCm3 - refVolume) < refVolume * 0.2) {
                confidenceClass = 'confidence-high';
                confidenceText = '🟢 ±10% — Ähnlich wie Referenzteil';
            }
            
            // Update UI
            document.getElementById('setupTimeDisplay').textContent = Math.round(totalSetupTime) + ' min';
            document.getElementById('setupCostDisplay').textContent = '€' + setupCost.toFixed(2).replace('.', ',');
            
            document.getElementById('liveWeight').textContent = weightKg.toFixed(2).replace('.', ',') + ' kg';
            document.getElementById('liveMaterial').textContent = '€' + materialCost.toFixed(2).replace('.', ',');
            document.getElementById('liveTime').textContent = machiningTime.toFixed(1).replace('.', ',') + ' min';
            document.getElementById('liveMachine').textContent = '€' + machineCost.toFixed(2).replace('.', ',');
            
            document.getElementById('priceDisplay').textContent = '€' + sellPrice.toFixed(2).replace('.', ',');
            document.getElementById('confidenceBadge').className = 'confidence-badge ' + confidenceClass;
            document.getElementById('confidenceBadge').innerHTML = '<span>' + confidenceText.split(' ')[0] + '</span> ' + confidenceText.split(' ').slice(1).join(' ');
            
            document.getElementById('matCost').textContent = '€' + materialMitGK.toFixed(2).replace('.', ',');
            document.getElementById('matFormula').textContent = weightKg.toFixed(2).replace('.', ',') + ' kg × €' + mat.price.toFixed(2).replace('.', ',') + ' + ' + zuschlagMGK + '% MGK';
            document.getElementById('machCost').textContent = '€' + fertigungMitAV.toFixed(2).replace('.', ',');
            document.getElementById('machFormula').textContent = machiningTime.toFixed(1).replace('.', ',') + ' min × €' + cncRate + '/h + ' + zuschlagAV + '% AV';
            document.getElementById('setupCost').textContent = '€' + setupCostPerPiece.toFixed(2).replace('.', ',');
            document.getElementById('setupFormula').textContent = Math.round(totalSetupTime) + ' min × €' + cncRate + '/h ÷ ' + qty;
            document.getElementById('toolCost').textContent = '€' + toolCost.toFixed(2).replace('.', ',');
            document.getElementById('additionalCost').textContent = '€' + (vwGKBetrag + vtGKBetrag).toFixed(2).replace('.', ',');
            document.getElementById('additionalFormula').textContent = zuschlagVwGK + '% VwGK + ' + zuschlagVtGK + '% VtGK';
            document.getElementById('totalCost').textContent = '€' + selbstkosten.toFixed(2).replace('.', ',');
            document.getElementById('marginDisplay').textContent = zuschlagGewinn;
            document.getElementById('marginCost').textContent = '€' + gewinnBetrag.toFixed(2).replace('.', ',');
            document.getElementById('sellPrice').textContent = '€' + angebotspreis.toFixed(2).replace('.', ',');
            document.getElementById('orderTotal').textContent = '€' + orderTotal.toFixed(2).replace('.', ',');
            
            // Quantity table with full Zuschlagskalkulation
            const qtys = [1, 5, 10, 25, 50];
            document.getElementById('quantityTable').innerHTML = qtys.map(q => {
                const setupPerPiece = setupCost / q;
                const fert = machineCost + setupPerPiece + additionalCost;
                const fertMitAV = fert * (1 + zuschlagAV / 100);
                const hk = materialMitGK + fertMitAV + toolCost;
                const sk = hk * (1 + (zuschlagVwGK + zuschlagVtGK) / 100);
                const ap = sk * (1 + zuschlagGewinn / 100);
                const totalSell = ap * q;
                return `<tr>
                    <td class="mono">${q}</td>
                    <td class="right mono">€${ap.toFixed(2).replace('.', ',')}</td>
                    <td class="right mono">€${totalSell.toFixed(2).replace('.', ',')}</td>
                </tr>`;
            }).join('');
            
            // Quote
            document.getElementById('quoteQty').textContent = qty;
            document.getElementById('quoteEP').textContent = sellPrice.toFixed(2).replace('.', ',');
            document.getElementById('quoteGP').textContent = orderTotal.toFixed(2).replace('.', ',');
            document.getElementById('quoteSubtotal').textContent = '€' + orderTotal.toFixed(2).replace('.', ',');
            document.getElementById('quoteMwst').textContent = '€' + mwstAmount.toFixed(2).replace('.', ',');
            document.getElementById('quoteTotal').textContent = '€' + totalWithVat.toFixed(2).replace('.', ',');
            
            // Instructions
            document.getElementById('faMaterial').innerHTML = '<strong>' + mat.name + '</strong>';
            document.getElementById('faRawDims').textContent = x + ' × ' + y + ' × ' + z + ' mm';
            document.getElementById('faWeight').textContent = weightKg.toFixed(2).replace('.', ',') + ' kg';
            document.getElementById('faMachiningTime').innerHTML = '<strong>' + machiningTime.toFixed(1).replace('.', ',') + ' min</strong>';
            
            // Plausibility warnings
            checkPlausibility(x, y, z, mat, clampingType);
        }
        
        function checkPlausibility(x, y, z, mat, clamping) {
            const warnings = [];
            
            if (x > 400 && clamping === 'schraubstock') {
                warnings.push({ type: 'warning', text: `Länge ${x}mm: Prüfen ob Schraubstock-Kapazität ausreicht. 2× Schraubstock empfohlen.` });
            }
            if (z > 100) {
                warnings.push({ type: 'warning', text: `Höhe ${z}mm: Werkzeugüberhang beachten. Vibrationsgefahr bei tiefen Taschen.` });
            }
            if (mat.timeFactor > 1.3) {
                warnings.push({ type: 'info', text: `Schwerzerspanbarer Werkstoff (${mat.name}): Kühlmittel und Werkzeugverschleiß beachten.` });
            }
            
            const container = document.getElementById('warningsContainer');
            if (warnings.length > 0) {
                container.innerHTML = warnings.map(w => `
                    <div class="${w.type === 'warning' ? 'warning-box' : 'info-box'}" style="margin-bottom: var(--space-3);">
                        <strong>⚠️ ${w.type === 'warning' ? 'Warnung' : 'Hinweis'}:</strong> ${w.text}
                    </div>
                `).join('');
            } else {
                container.innerHTML = '';
            }
        }
        
        // ================================================================
        // SETTINGS
        // ================================================================
        
        function updateRates() {
            RATES.cnc.labor = parseFloat(document.getElementById('rateCncLabor').value) || 49;
            RATES.cnc.machine = parseFloat(document.getElementById('rateCncMachine').value) || 42;
            RATES.saegen.labor = parseFloat(document.getElementById('rateSaegenLabor').value) || 43;
            RATES.saegen.machine = parseFloat(document.getElementById('rateSaegenMachine').value) || 12;
            RATES.entgraten.labor = parseFloat(document.getElementById('rateEntgratenLabor').value) || 32;
            RATES.entgraten.machine = parseFloat(document.getElementById('rateEntgratenMachine').value) || 4;
            
            document.getElementById('rateCncTotal').textContent = '€' + (RATES.cnc.labor + RATES.cnc.machine);
            document.getElementById('rateSaegenTotal').textContent = '€' + (RATES.saegen.labor + RATES.saegen.machine);
            document.getElementById('rateEntgratenTotal').textContent = '€' + (RATES.entgraten.labor + RATES.entgraten.machine);
            
            calculate();
        }
        
        function updateMaterials() {
            MATERIALS['S235JR'].price = parseFloat(document.getElementById('matS235JR').value) || 6.79;
            MATERIALS['1.4571'].price = parseFloat(document.getElementById('mat14571').value) || 14.00;
            MATERIALS['AlMg3'].price = parseFloat(document.getElementById('matAlMg3').value) || 6.50;
            MATERIALS['42CrMo4'].price = parseFloat(document.getElementById('mat42CrMo4').value) || 4.20;
            calculate();
        }
        
        function saveSettings() {
            const settings = { RATES, MATERIALS };
            localStorage.setItem('cncplanner_settings_v16', JSON.stringify(settings));
            alert('✅ Einstellungen gespeichert.');
        }
        
        function loadSettings() {
            const saved = localStorage.getItem('cncplanner_settings_v16');
            if (saved) {
                const settings = JSON.parse(saved);
                Object.assign(RATES, settings.RATES);
                Object.assign(MATERIALS, settings.MATERIALS);
            }
        }
        
        function resetSettings() {
            localStorage.removeItem('cncplanner_settings_v16');
            location.reload();
        }
        
        // ================================================================
        // FEEDBACK SYSTEM
        // ================================================================
        
        // Initialize feedback storage
        let feedbackHistory = JSON.parse(localStorage.getItem('cncplanner_feedback') || '[]');
        
        function showFeedbackTab(tab) {
            // Hide all tabs
            document.getElementById('feedback-eingabe').style.display = 'none';
            document.getElementById('feedback-learnings').style.display = 'none';
            document.getElementById('feedback-historie').style.display = 'none';
            
            // Reset all buttons
            document.getElementById('tabFeedbackEingabe').className = 'btn btn-sm btn-secondary';
            document.getElementById('tabFeedbackLearnings').className = 'btn btn-sm btn-secondary';
            document.getElementById('tabFeedbackHistorie').className = 'btn btn-sm btn-secondary';
            
            // Show selected tab
            document.getElementById('feedback-' + tab).style.display = 'block';
            document.getElementById('tabFeedback' + tab.charAt(0).toUpperCase() + tab.slice(1)).className = 'btn btn-sm btn-primary';
            
            // Update displays
            if (tab === 'learnings') updateCrossLearnings();
            if (tab === 'historie') updateFeedbackHistory();
        }
        
        function updateFeedbackDelta(input) {
            const row = input.closest('tr');
            const kalkCell = row.cells[2].textContent;
            const kalkMin = parseFloat(kalkCell.replace(',', '.').replace(' min', ''));
            const istMin = parseFloat(input.value) || 0;
            const deltaCell = row.querySelector('[data-delta]');
            
            if (istMin > 0) {
                const delta = istMin - kalkMin;
                const sign = delta >= 0 ? '+' : '';
                deltaCell.textContent = sign + delta.toFixed(1).replace('.', ',') + ' min';
                deltaCell.style.color = delta > 0 ? 'var(--color-error)' : 'var(--color-success)';
            } else {
                deltaCell.textContent = '—';
                deltaCell.style.color = '';
            }
            
            updateGesamtzeit();
        }
        
        function updateSetupDelta() {
            const kalk = 25; // Kalkulierte Setup-Zeit
            const ist = parseFloat(document.getElementById('fbSetupIst').value) || 0;
            const deltaEl = document.getElementById('fbSetupDelta');
            
            if (ist > 0) {
                const delta = ist - kalk;
                const sign = delta >= 0 ? '+' : '';
                deltaEl.textContent = sign + delta + ' min';
                deltaEl.style.color = delta > 0 ? 'var(--color-error)' : 'var(--color-success)';
            } else {
                deltaEl.textContent = '—';
                deltaEl.style.color = '';
            }
            
            updateGesamtzeit();
        }
        
        function updateGesamtzeit() {
            let gesamtIst = 0;
            let gesamtKalk = 42; // Demo value
            
            // Sum all OP times
            document.querySelectorAll('#feedbackOpsTable input[type="number"]').forEach(input => {
                gesamtIst += parseFloat(input.value) || 0;
            });
            
            // Add setup
            gesamtIst += parseFloat(document.getElementById('fbSetupIst').value) || 0;
            
            if (gesamtIst > 0) {
                document.getElementById('fbGesamtIst').textContent = gesamtIst.toFixed(1).replace('.', ',') + ' min';
                const delta = ((gesamtIst - gesamtKalk) / gesamtKalk * 100);
                const sign = delta >= 0 ? '+' : '';
                document.getElementById('fbGesamtDelta').textContent = sign + delta.toFixed(0) + '%';
                document.getElementById('fbGesamtDelta').style.color = delta > 0 ? 'var(--color-error)' : 'var(--color-success)';
            }
        }
        
        function saveFeedback() {
            const feedback = {
                id: Date.now(),
                projektNr: document.getElementById('fbProjektNr').value,
                datum: document.getElementById('fbDatum').value,
                erfasser: document.getElementById('fbErfasser').value || 'Anonym',
                zeitKalk: 42, // Demo
                zeitIst: parseFloat(document.getElementById('fbGesamtIst').textContent) || 42,
                setupKalk: 25,
                setupIst: parseFloat(document.getElementById('fbSetupIst').value) || 25,
                setupGrund: document.getElementById('fbSetupGrund').value,
                setupNotiz: document.getElementById('fbSetupNotiz').value,
                ergebnis: document.querySelector('input[name="fbErgebnis"]:checked')?.value || 'io_erst',
                empfehlung: document.getElementById('fbEmpfehlung').value,
                ops: []
            };
            
            // Collect OP data
            document.querySelectorAll('#feedbackOpsTable tr').forEach(row => {
                const opCell = row.cells[0];
                if (opCell && opCell.textContent.startsWith('OP')) {
                    const istInput = row.querySelector('input[type="number"]');
                    const grundSelect = row.querySelector('select');
                    const notizInput = row.querySelectorAll('input[type="text"]')[0];
                    
                    if (istInput && istInput.value) {
                        feedback.ops.push({
                            op: opCell.textContent,
                            kalk: parseFloat(row.cells[2].textContent.replace(',', '.')) || 0,
                            ist: parseFloat(istInput.value) || 0,
                            grund: grundSelect?.value || '',
                            notiz: notizInput?.value || ''
                        });
                    }
                }
            });
            
            // Save
            feedbackHistory.push(feedback);
            localStorage.setItem('cncplanner_feedback', JSON.stringify(feedbackHistory));
            
            alert('✅ Feedback gespeichert!\n\nDanke für die Rückmeldung. Das System lernt mit jedem Feedback.');
            clearFeedbackForm();
        }
        
        function clearFeedbackForm() {
            document.querySelectorAll('#feedbackOpsTable input').forEach(i => i.value = '');
            document.querySelectorAll('#feedbackOpsTable select').forEach(s => s.selectedIndex = 0);
            document.querySelectorAll('[data-delta]').forEach(d => { d.textContent = '—'; d.style.color = ''; });
            document.getElementById('fbSetupIst').value = '';
            document.getElementById('fbSetupDelta').textContent = '—';
            document.getElementById('fbSetupGrund').selectedIndex = 0;
            document.getElementById('fbSetupNotiz').value = '';
            document.getElementById('fbGesamtIst').textContent = '— min';
            document.getElementById('fbGesamtDelta').textContent = '—';
            document.getElementById('fbEmpfehlung').value = '';
        }
        
        function updateCrossLearnings() {
            const count = feedbackHistory.length;
            document.getElementById('feedbackCount').textContent = count;
            
            if (count > 0) {
                // Calculate average deviation
                let totalDev = 0;
                feedbackHistory.forEach(f => {
                    totalDev += ((f.zeitIst - f.zeitKalk) / f.zeitKalk) * 100;
                });
                const avgDev = totalDev / count;
                document.getElementById('avgDeviation').textContent = (avgDev >= 0 ? '+' : '') + avgDev.toFixed(0) + '%';
                document.getElementById('avgDeviation').style.color = avgDev > 15 ? 'var(--color-error)' : avgDev > 0 ? 'var(--color-warning)' : 'var(--color-success)';
            }
        }
        
        function updateFeedbackHistory() {
            const tbody = document.getElementById('feedbackHistoryTable');
            if (feedbackHistory.length === 0) return;
            
            // Add real feedback to table (prepend to demo data)
            const realRows = feedbackHistory.slice(-5).reverse().map(f => {
                const delta = ((f.zeitIst - f.zeitKalk) / f.zeitKalk * 100);
                const deltaColor = delta > 10 ? 'var(--color-error)' : delta < -5 ? 'var(--color-success)' : 'var(--color-warning)';
                const ergebnis = f.ergebnis === 'io_erst' || f.ergebnis === 'io_korrektur' ? '✅ i.O.' : f.ergebnis === 'nacharbeit' ? '⚠️ Nacharbeit' : '❌ Ausschuss';
                
                return `<tr>
                    <td class="mono">${f.datum.split('-').reverse().join('.')}</td>
                    <td class="mono">${f.projektNr}</td>
                    <td>${f.erfasser}</td>
                    <td class="mono right">${f.zeitKalk} min</td>
                    <td class="mono right">${f.zeitIst.toFixed(0)} min</td>
                    <td class="mono right" style="color: ${deltaColor};">${delta >= 0 ? '+' : ''}${delta.toFixed(0)}%</td>
                    <td>${f.setupGrund || '—'}</td>
                    <td>${ergebnis}</td>
                </tr>`;
            }).join('');
        }
        
        function applyPattern(patternId, value) {
            // Apply pattern to calculation
            if (patternId === 'setup_parallel') {
                alert('✅ Muster angewendet!\n\nSetup-Zeit bei Parallelspanner wird um +' + value + ' min erhöht.');
                localStorage.setItem('pattern_setup_parallel', value);
            } else if (patternId === 'tolerance_factor') {
                alert('✅ Muster angewendet!\n\nToleranz-Faktor für h5/H7 auf ' + value + '× gesetzt.');
                localStorage.setItem('pattern_tolerance_factor', value);
            } else if (patternId === 's235_aufmass') {
                alert('✅ Muster angewendet!\n\nRohteil-Aufmaß für S235 auf ' + value + ' mm gesetzt.');
                localStorage.setItem('pattern_s235_aufmass', value);
            }
        }
        
        function ignorePattern(patternId) {
            alert('Muster ignoriert. Wird bei genügend neuen Feedbacks erneut geprüft.');
        }
        
        function exportFeedbackCSV() {
            if (feedbackHistory.length === 0) {
                alert('Keine Feedback-Daten vorhanden.');
                return;
            }
            
            let csv = 'Datum;Projekt;Erfasser;Kalk (min);Ist (min);Delta %;Grund;Ergebnis;Empfehlung\n';
            feedbackHistory.forEach(f => {
                const delta = ((f.zeitIst - f.zeitKalk) / f.zeitKalk * 100).toFixed(0);
                csv += `${f.datum};${f.projektNr};${f.erfasser};${f.zeitKalk};${f.zeitIst};${delta};${f.setupGrund};${f.ergebnis};${f.empfehlung}\n`;
            });
            
            const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
            const link = document.createElement('a');
            link.href = URL.createObjectURL(blob);
            link.download = 'cnc_feedback_export.csv';
            link.click();
        }
        
        function showSettingsTab(tab) {
            // Hide all tabs
            document.getElementById('settings-stunden').style.display = 'none';
            document.getElementById('settings-material').style.display = 'none';
            document.getElementById('settings-zuschlag').style.display = 'none';
            document.getElementById('settings-firma').style.display = 'none';
            
            // Reset all buttons
            document.getElementById('tabStunden').className = 'btn btn-sm btn-secondary';
            document.getElementById('tabMaterial').className = 'btn btn-sm btn-secondary';
            document.getElementById('tabZuschlag').className = 'btn btn-sm btn-secondary';
            document.getElementById('tabFirma').className = 'btn btn-sm btn-secondary';
            
            // Show selected tab
            document.getElementById('settings-' + tab).style.display = 'block';
            document.getElementById('tab' + tab.charAt(0).toUpperCase() + tab.slice(1)).className = 'btn btn-sm btn-primary';
        }
        
        function exportSettings() {
            const settings = { RATES, MATERIALS };
            const blob = new Blob([JSON.stringify(settings, null, 2)], { type: 'application/json' });
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'cncplanner-settings.json';
            a.click();
        }
        
        function importSettings() {
            alert('Import-Funktion: Datei auswählen (Coming soon)');
        }
        
        // ================================================================
        // EXPORT
        // ================================================================
        
        function exportCSV() {
            alert('CSV Export — Coming soon');
        }
        
        function copyCode() {
            const code = document.querySelector('#codeBlock pre').textContent;
            navigator.clipboard.writeText(code);
            alert('Code kopiert!');
        }
        
        function downloadCode() {
            const code = document.querySelector('#codeBlock pre').textContent;
            const blob = new Blob([code], { type: 'text/plain' });
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'programm.h';
            a.click();
        }
        
        function setCodeFormat(format) {
            document.querySelectorAll('[id^="btn"]').forEach(btn => {
                btn.classList.remove('btn-primary');
                btn.classList.add('btn-secondary');
            });
            document.getElementById('btn' + format.charAt(0).toUpperCase() + format.slice(1)).classList.remove('btn-secondary');
            document.getElementById('btn' + format.charAt(0).toUpperCase() + format.slice(1)).classList.add('btn-primary');
            // TODO: Switch code templates
        }
        
        // ================================================================
        // LOADING ANIMATION
        // ================================================================
        
        function showLoading() {
            document.getElementById('loadingOverlay').classList.add('active');
            animateLoadingSteps();
        }
        
        function hideLoading() {
            document.getElementById('loadingOverlay').classList.remove('active');
            document.querySelectorAll('.loading-step').forEach(step => {
                step.classList.remove('active', 'done');
            });
        }
        
        function animateLoadingSteps() {
            const steps = ['loadStep1', 'loadStep2', 'loadStep3', 'loadStep4', 'loadStep5'];
            let i = 0;
            
            function nextStep() {
                if (i > 0) {
                    document.getElementById(steps[i - 1]).classList.remove('active');
                    document.getElementById(steps[i - 1]).classList.add('done');
                    document.getElementById(steps[i - 1]).querySelector('.loading-step-icon').textContent = '✓';
                }
                if (i < steps.length) {
                    document.getElementById(steps[i]).classList.add('active');
                    i++;
                    setTimeout(nextStep, 400 + Math.random() * 200);
                } else {
                    setTimeout(hideLoading, 300);
                }
            }
            
            nextStep();
        }
        
        // ================================================================
        // FEEDBACK
        // ================================================================
        
        let selectedFeedback = null;
        
        function selectFeedback(el, type) {
            document.querySelectorAll('.feedback-option').forEach(opt => opt.classList.remove('selected'));
            el.classList.add('selected');
            selectedFeedback = type;
        }
        
        function submitFeedback() {
            const comment = document.getElementById('feedbackComment').value;
            if (!selectedFeedback && !comment) {
                alert('Bitte wählen Sie eine Feedback-Option oder geben Sie einen Kommentar ein.');
                return;
            }
            
            // In production: send to server
            console.log('Feedback:', { type: selectedFeedback, comment, project: currentProject?.id });
            
            alert('Vielen Dank für Ihr Feedback! Wir nutzen es, um die Kalkulation zu verbessern.');
            
            // Reset
            document.querySelectorAll('.feedback-option').forEach(opt => opt.classList.remove('selected'));
            document.getElementById('feedbackComment').value = '';
            selectedFeedback = null;
        }
        
        // ================================================================
        // INIT
        // ================================================================
        
        document.addEventListener('DOMContentLoaded', function() {
            loadSettings();
            renderPartGrid();
            calculate();
            
            // Set today's date
            const today = new Date();
            const dateStr = today.toLocaleDateString('de-DE');
            document.getElementById('quoteDate').textContent = dateStr;
            const validUntil = new Date(today.getTime() + 30 * 24 * 60 * 60 * 1000);
            document.getElementById('quoteValidUntil').textContent = validUntil.toLocaleDateString('de-DE');
        });
    </script>
</body>
</html>
