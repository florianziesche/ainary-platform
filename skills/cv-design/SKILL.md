# CV & Cover Letter Design — LaTeX Design Skill Document

> The definitive design reference for professional/finance/VC resumes and cover letters in LaTeX.
> Goal: **"Designed but not over-designed"** — the look of someone who pays attention to detail without trying to be a graphic designer.

---

## 1. Typography

### 1.1 The Serif vs. Sans-Serif Decision

| Context | Recommendation | Why |
|---------|---------------|-----|
| **Finance / IB / PE / VC** | Serif body + sans-serif headers (or all sans-serif) | Serif signals tradition & gravitas; sans-serif signals modernity. Mixing both = sophisticated. |
| **Consulting (MBB)** | Clean sans-serif throughout | McKinsey decks are Helvetica/Arial. Match their aesthetic. |
| **Tech-adjacent VC** | Sans-serif throughout | Signals you understand the startup world. |
| **Cover letter** | Match your resume font exactly | Consistency = personal brand. |

### 1.2 Best Fonts — Tiered Ranking

**Tier 1: "Sophisticated Professional" (Stand out quietly)**
| Font | Type | LaTeX Package | Signal |
|------|------|--------------|--------|
| **Garamond / EB Garamond** | Serif | `ebgaramond` or `fontspec` | Old-money elegance, literary intelligence. Used by elite law firms & journals. |
| **Minion Pro** | Serif | `fontspec` (system font) | The Economist, academic publishing. Quietly expensive-looking. |
| **Cormorant Garamond** | Serif | `fontspec` (Google Font) | Modern interpretation of Garamond. Lighter, more airy. |
| **Inter** | Sans-serif | `fontspec` (Google Font) | Silicon Valley default. GitHub, Linear, Figma use it. Perfect for tech VC. |
| **Source Sans Pro** | Sans-serif | `sourcesanspro` | Adobe's professional workhorse. Clean without being generic. |

**Tier 2: "Safe & Professional" (Never wrong, never memorable)**
| Font | Type | LaTeX Package | Signal |
|------|------|--------------|--------|
| **Calibri** | Sans-serif | `fontspec` (system) | Microsoft default since 2007. Safe but signals "didn't think about font." |
| **Helvetica / Arial** | Sans-serif | `helvet` | The corporate standard. Clean but invisible. |
| **Georgia** | Serif | `fontspec` (system) | Designed for screens. Trustworthy but dated. |
| **Cambria** | Serif | `fontspec` (system) | Microsoft's serif. Fine, unremarkable. |

**Tier 3: "Avoid for Finance"**
| Font | Why Not |
|------|---------|
| Times New Roman | Screams "default Word document" or "undergraduate." Paradoxically, using the most "traditional" font looks lazy. |
| Comic Sans | Obviously. |
| Papyrus | See above. |
| Any decorative/display font | This isn't a wedding invitation. |

### 1.3 Recommended Font Pairings for Finance/VC

```
Option A (The Classic):         EB Garamond body + Lato headers
Option B (The Modern):          Inter body + Inter headers (weight variation only)
Option C (The Hybrid):          Source Sans Pro body + Cormorant Garamond name
Option D (The Minimalist):      Libertinus Serif body + Libertinus Sans headers
```

### 1.4 Font Sizes — Exact Specifications

| Element | Size | Weight | Notes |
|---------|------|--------|-------|
| **Your Name** | 20–26pt | Bold or semibold | 1.8–2.2× body size. This is the largest element on the page. |
| **Subtitle / Tagline** | 10–11pt | Regular or light | Optional. E.g., "VC Associate · Ex-McKinsey · HBS '24" |
| **Section Headers** | 11–13pt | Bold + SMALL CAPS or ALL CAPS | Must be clearly distinct from body. Use letter-spacing (tracking) of +50–80. |
| **Job Title / Company** | 10–11pt | Bold | Same size as body or 1pt larger. |
| **Body Text** | 10–11pt | Regular | **10.5pt is the sweet spot** — professional density without squinting. |
| **Dates / Location** | 9–10pt | Regular or italic | Slightly smaller to create hierarchy. Right-aligned or in a sidebar column. |
| **Contact Info** | 9–10pt | Regular | Small but legible. Can use `·` or `|` as separators. |

> **Golden Rule:** Your font size hierarchy should be: Name > Section Headers > Job Titles > Body > Dates/Contact. Every level must be visually distinct.

### 1.5 Line Spacing & Letter Spacing

| Parameter | Value | LaTeX Implementation |
|-----------|-------|---------------------|
| **Body line height** | 1.08–1.20× font size | `\linespread{1.08}` or `\setstretch{1.15}` via `setspace` |
| **Between bullet points** | 1–3pt extra | `\itemsep=1.5pt` via `enumitem` |
| **Between sections** | 8–14pt | `\vspace{10pt}` or `\addvspace{12pt}` |
| **After section header** | 4–6pt | `titlesec`: `\titlespacing*{\section}{0pt}{12pt}{4pt}` |
| **Letter spacing (tracking) for headers** | +50 to +80 (0.05–0.08em) | `\addfontfeatures{LetterSpace=5}` via `fontspec` or `\textls[50]{TEXT}` via `microtype` |
| **Letter spacing for body** | 0 (default) | Don't touch body tracking. Let `microtype` handle micro-adjustments. |

> **Key insight:** Slightly loose line spacing (1.12–1.15) makes a dense one-page resume feel breathable. Below 1.08 feels cramped. Above 1.25 wastes space.

---

## 2. Layout & Whitespace

### 2.1 Page Format

| Parameter | US Letter (8.5" × 11") | A4 (210mm × 297mm) | Notes |
|-----------|----------------------|---------------------|-------|
| **Top margin** | 0.5"–0.75" (12.7–19mm) | 15–20mm | Name goes here; less margin = more space. |
| **Bottom margin** | 0.5"–0.75" (12.7–19mm) | 15–20mm | Match top or slightly less. |
| **Left margin** | 0.6"–0.8" (15–20mm) | 15–20mm | Wider than top/bottom for visual comfort. |
| **Right margin** | 0.6"–0.8" (15–20mm) | 15–20mm | Match left margin exactly. |

**The "Professional Tight" setup (recommended for 1-page finance CV):**
```latex
\usepackage[a4paper, top=15mm, bottom=15mm, left=18mm, right=18mm]{geometry}
```

**The "Breathing Room" setup (if content allows):**
```latex
\usepackage[a4paper, top=20mm, bottom=20mm, left=22mm, right=22mm]{geometry}
```

> **Never go below 12mm (0.5") on any side.** Recruiters print resumes; content gets clipped.

### 2.2 Column Layout Decision

| Layout | Best For | Pros | Cons |
|--------|----------|------|------|
| **Single column** | Finance, IB, consulting, VC | Clean, traditional, ATS-perfect, Goldman/McKinsey standard | Less info density per page |
| **Sidebar (70/30 split)** | Tech, design, startup VC | Modern look, skills/contact in sidebar | ATS can misread column order; too "creative" for traditional finance |
| **Two-column (50/50)** | Academic CV, long-form | Maximum density | Never for a 1-page professional resume |

**→ For VC/Finance: Single column. Always.** Goldman Sachs, McKinsey, Harvard Business School — all use single column. The sidebar look signals "I used a Canva template," not "I belong at your fund."

### 2.3 Visual Hierarchy & Section Order

```
┌─────────────────────────────────────────────┐
│           FIRSTNAME LASTNAME                 │ ← 20–26pt, bold, centered or left
│    email · phone · city · linkedin           │ ← 9–10pt, centered or left
├─────────────────────────────────────────────┤
│ ─── EXPERIENCE ─────────────────────────     │ ← Section header with rule
│                                              │
│ Company Name — Job Title        Location     │ ← Bold company, regular title
│ Date Range                                   │ ← Right-aligned or under title
│ • Achievement with quantified result ($, %)  │
│ • Achievement with quantified result         │
│ • Achievement with quantified result         │
│                                              │
│ Company Name — Job Title        Location     │
│ ...                                          │
├─────────────────────────────────────────────┤
│ ─── EDUCATION ──────────────────────────     │
│                                              │
│ University — Degree             Year         │
│ Honors, GPA (if >3.5), relevant coursework   │
├─────────────────────────────────────────────┤
│ ─── ADDITIONAL ─────────────────────────     │
│ Skills, Languages, Certifications, Interests │
└─────────────────────────────────────────────┘
```

### 2.4 Whitespace Principles

Research-backed guidelines:

- **40–50% of the page should be whitespace** (margins + inter-element spacing). A resume with <35% whitespace feels "wall of text." Above 55% feels empty.
- **Golden ratio for typography:** For a 10.5pt body font, optimal line height ≈ 10.5 × 1.618 ≈ 17pt. In practice, 14–16pt works (1.33–1.52× multiplier) since resume text is shorter than book paragraphs.
- **Optimal line length:** 50–75 characters per line. With standard margins and 10.5pt font, this happens naturally on US Letter/A4.
- **Consistent vertical rhythm:** All spacing should be multiples of a base unit. If your base unit is 4pt: section spacing = 12pt (3×), bullet spacing = 4pt (1×), header-to-content = 8pt (2×).

---

## 3. Color Usage

### 3.1 Should You Use Color in a VC/Finance Resume?

**Yes — but with extreme restraint.**

Color done right says "attention to detail." Color done wrong says "trying too hard" or "used a template."

### 3.2 The Finance-Safe Color Palette

| Color | Hex Code | Where to Use | Psychology |
|-------|----------|-------------|------------|
| **Black** | `#000000` or `#1a1a1a` | Body text | Standard. `#1a1a1a` (95% black) is softer on the eye than pure black. |
| **Dark Navy** | `#1B2A4A` | Name, section headers, rules | Trust, authority, stability. The Goldman Sachs blue. |
| **Slate Blue** | `#2C3E6B` | Accent only (lighter alternative) | Professional but slightly more approachable. |
| **Charcoal** | `#2D2D2D` | Alternative to navy for headers | Sophisticated, modern, monochrome elegance. |
| **Dark Gray** | `#555555` | Dates, locations, secondary text | Creates hierarchy without adding a new color. |

### 3.3 Color Rules

1. **Maximum 2 colors** beyond black: one accent (navy/charcoal) + one gray for secondary text. That's it.
2. **Never use color for body text.** Body is always black or near-black.
3. **Use color consistently:** If section headers are navy, ALL section headers are navy. No exceptions.
4. **Color in the cover letter must match the resume exactly.** Same hex codes.
5. **Test in grayscale.** Print in B&W — does the hierarchy still work? If not, your color is doing too much work.
6. **Test on screen AND paper.** Navy blue on screen can look very different printed on a cheap office printer.

### 3.4 Color Implementation in LaTeX

```latex
\usepackage{xcolor}

% Define your palette
\definecolor{primary}{HTML}{1B2A4A}    % Dark navy — headers, name, rules
\definecolor{secondary}{HTML}{555555}   % Dark gray — dates, locations
\definecolor{body}{HTML}{1A1A1A}        % Near-black — body text
\definecolor{accent}{HTML}{2C3E6B}      % Slate blue — links only (optional)

% Apply globally
\color{body}  % Set default text color
```

### 3.5 ATS & Printing Considerations

- **ATS does NOT reject color.** Modern ATS (Greenhouse, Lever, Workable) parse text content, not visual styling. Color is irrelevant to parsing.
- **ATS DOES struggle with:** Text inside images, text in headers/footers, multi-column layouts parsed in wrong order, and non-standard fonts embedded incorrectly.
- **Printing:** Many offices print B&W. Your color should enhance hierarchy, not create it. The resume must be fully readable in pure B&W.
- **PDF text layer:** LaTeX-generated PDFs have a proper text layer by default — ATS can always extract the text regardless of visual styling.

---

## 4. Visual Elements

### 4.1 Horizontal Rules

| Style | When to Use | LaTeX |
|-------|------------|-------|
| **Thin rule under name** (0.4pt) | Always. Separates header from content. | `{\color{primary}\hrule height 0.4pt}` |
| **Thin rule under section headers** (0.4pt) | Recommended. Creates clear sections. | `\titlerule[0.4pt]` via `titlesec` |
| **Thick rule under name** (1.5–2pt) | Bold statement. Works if done once. | `{\color{primary}\hrule height 1.5pt}` |
| **No rules at all** | Minimalist look. Use extra spacing instead. | — |

> **Best practice for finance:** Thin (0.4–0.5pt) rules under section headers in your accent color. One slightly thicker rule (0.8–1pt) under the name. Clean, structured, not heavy.

### 4.2 Key Metrics / Highlights Bar

A "highlights bar" right below your name can be powerful for VC resumes:

```
────────────────────────────────────────────────────
$500M+ AuM  ·  12 investments  ·  3 exits  ·  2.8× MOIC
────────────────────────────────────────────────────
```

- Use `·` (middle dot) or `|` as separators
- Keep to one line, 3–5 metrics maximum
- Same font size as body or 1pt smaller
- Bold the numbers, regular the labels
- Only include if you have genuinely impressive metrics

### 4.3 Icons

| Verdict | Why |
|---------|-----|
| **No icons in finance/VC resumes** | Icons (phone, email, LinkedIn pictograms) are visual clutter that signal "template" not "professional." McKinsey, Goldman, and top VC resumes never use icons. |
| **Exception:** | A very subtle LinkedIn icon next to your profile URL is acceptable but not necessary. |
| **If you must:** | Use FontAwesome icons at small size (8–9pt), in gray, next to contact info only. Never in section headers. |

### 4.4 Subtle Design Touches That Signal Quality

These are the details that make a recruiter think "this person pays attention":

1. **Proper typographic dashes:** En-dash (–) for date ranges ("2022–2024"), not hyphens
2. **Consistent date formatting:** "Jan 2022 – Present" or "01/2022 – Present" — pick one, stick to it
3. **Optical margin alignment:** Bullet points should hang slightly into the margin (`enumitem` package)
4. **Non-breaking spaces:** Before units and between first/last name (`~` in LaTeX)
5. **Proper ellipsis:** `\ldots` not `...`
6. **Ligatures enabled:** fi, fl, ff ligatures (automatic with good fonts in XeLaTeX/LuaLaTeX)
7. **Microtypography:** `\usepackage{microtype}` — enables character protrusion and font expansion for optically even margins
8. **PDF metadata:** Set title, author, keywords in PDF properties (`hyperref` package)
9. **Matching header on cover letter:** Same name/contact block design on both documents

### 4.5 What Top-Tier Firm Resumes Look Like

**Goldman Sachs / JP Morgan / Morgan Stanley (Investment Banking):**
- Single column, single page
- No color (pure black & white)
- Conservative serif or basic sans-serif (Calibri, Arial, Times)
- Heavy emphasis on bullet points with quantified achievements
- Minimal formatting — the content does the talking
- Section order: Education first (for juniors), Experience first (for experienced)

**McKinsey / BCG / Bain (Consulting):**
- Single column, single page
- Clean sans-serif (Calibri, Arial)
- Very structured: each role has 3–4 bullets maximum
- No color, no rules, no visual flourish
- Emphasis on impact statements: "Led X, resulting in Y% improvement"

**Top VC Funds (a16z, Sequoia, Benchmark):**
- More personality allowed than IB/consulting
- Still single column, single page
- Clean but can have subtle design (thin rules, one accent color)
- Portfolio metrics and deal experience prominently featured
- Tech-savvy aesthetic (modern sans-serif, slightly more whitespace)

> **The pattern:** The more prestigious the firm, the simpler the resume design. Content > design. Always.

---

## 5. LaTeX-Specific Design

### 5.1 Document Class Selection

| Class | Best For | Pros | Cons |
|-------|----------|------|------|
| **`article`** (custom) | Finance, VC, consulting | Full control, minimal bloat, ATS-perfect | Must build everything yourself |
| **`awesome-cv`** | Tech, modern startups | Beautiful defaults, FontAwesome icons, color support | Opinionated design, hard to customize deeply, too "designed" for IB |
| **`moderncv`** | General professional | Multiple themes (banking, classic, casual), easy setup | Looks dated in 2025, limited customization |
| **`altacv`** | Two-column layouts | Marissa Mayer-style sidebar layout | Two-column = ATS risk, too creative for finance |
| **`europecv`** | EU/academic | Europass standard | Ugly, bureaucratic, never for private sector |

**→ Recommendation for finance/VC: Build on `article` class.** You get total control, the output is clean, and the resulting PDF is perfectly ATS-compatible. Use packages to add the features you need.

### 5.2 The Essential LaTeX Package Stack

```latex
% === ENGINE: Use XeLaTeX or LuaLaTeX for system fonts ===

\documentclass[10.5pt, a4paper]{article}

% --- Layout ---
\usepackage[a4paper, top=15mm, bottom=15mm, left=18mm, right=18mm]{geometry}
\usepackage{parskip}         % Paragraph spacing instead of indentation
\usepackage{setspace}        % Line spacing control
\usepackage{multicol}        % For skills section if needed

% --- Typography ---
\usepackage{fontspec}        % System font support (XeLaTeX/LuaLaTeX)
\usepackage{microtype}       % Microtypographic enhancements (protrusion, expansion)
\usepackage{titlesec}        % Section header customization
\usepackage{enumitem}        % List customization (bullet spacing, margins)

% --- Color ---
\usepackage{xcolor}          % Color definitions

% --- Visual Elements ---
\usepackage{tikz}            % For subtle graphical elements
\usepackage{tabularx}        % Flexible tables for date-aligned entries
\usepackage{fancyhdr}        % Header/footer control (or disable page numbers)

% --- Links & Metadata ---
\usepackage[hidelinks]{hyperref}  % Clickable links without ugly boxes
\hypersetup{
    pdftitle={Firstname Lastname - Resume},
    pdfauthor={Firstname Lastname},
    pdfsubject={Resume},
    pdfkeywords={venture capital, finance, resume}
}

% --- Utilities ---
\usepackage{calc}            % Arithmetic in lengths
\usepackage{ifthen}          % Conditional logic
\usepackage{lastpage}        % Total page count (if multi-page)
```

### 5.3 Font Setup Examples

**Option A: EB Garamond + Source Sans Pro (Classic Finance)**
```latex
\usepackage{fontspec}
\setmainfont{EB Garamond}[
    Numbers=OldStyle,        % Elegant numerals in body text
    Ligatures=TeX
]
\setsansfont{Source Sans Pro}[
    Ligatures=TeX,
    Scale=MatchLowercase
]
% Use \sffamily for headers, \rmfamily for body
```

**Option B: Inter (Modern Tech VC)**
```latex
\usepackage{fontspec}
\setmainfont{Inter}[
    Ligatures=TeX,
    UprightFont=*-Regular,
    BoldFont=*-SemiBold,     % SemiBold > Bold for cleaner look
    ItalicFont=*-Italic
]
```

**Option C: Libertinus (Self-Contained, No System Fonts Needed)**
```latex
\usepackage{libertinus}      % Ships with TeX Live
\usepackage[T1]{fontenc}     % Use with pdfLaTeX
```

### 5.4 Section Header Design

```latex
\usepackage{titlesec}
\usepackage{xcolor}

\definecolor{primary}{HTML}{1B2A4A}

% Clean header with thin rule underneath
\titleformat{\section}
    {\large\bfseries\sffamily\color{primary}\uppercase}  % Format
    {}                                                      % Label
    {0pt}                                                   % Sep
    {}                                                      % Before-code
    [\vspace{2pt}{\color{primary}\titlerule[0.4pt]}]       % After-code (the rule)

\titlespacing*{\section}{0pt}{12pt}{6pt}
```

### 5.5 TikZ Elements That Enhance (Not Clutter)

**Use TikZ for:**
- A subtle colored bar behind your name
- A thin decorative line element in the header
- A small "tag" or "badge" for key skills (used very sparingly)

**Example: Subtle header bar**
```latex
\begin{tikzpicture}[remember picture, overlay]
    \fill[primary, opacity=0.05] 
        (current page.north west) rectangle 
        ([yshift=-35mm]current page.north east);
\end{tikzpicture}
```

**Do NOT use TikZ for:**
- Skill level bars/circles (cliché and meaningless — what does "75% Python" mean?)
- Progress indicators
- Infographic elements
- Timeline graphics
- Circular profile picture frames

### 5.6 Print-Ready PDF Output

```latex
% Ensure PDF/A compliance for archival and ATS
\usepackage[a-1b]{pdfx}     % PDF/A-1b standard (or use hyperref setup below)

% Alternative: manual PDF settings
\hypersetup{
    pdfstartview=FitH,
    pdfpagemode=UseNone,
    pdfpagelayout=SinglePage
}

% Embed all fonts (default in XeLaTeX/LuaLaTeX)
% For pdfLaTeX: ensure T1 encoding
\usepackage[T1]{fontenc}

% Disable page numbers for single-page resume
\pagestyle{empty}

% Or minimal footer
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\renewcommand{\headrulewidth}{0pt}
\fancyfoot[C]{\footnotesize\color{secondary} Page \thepage}
```

### 5.7 Bullet Point Configuration

```latex
\usepackage{enumitem}

% Tight, clean bullet points
\setlist[itemize]{
    leftmargin=12pt,         % Minimal indent
    itemsep=1pt,             % Tight spacing between items
    parsep=0pt,              % No paragraph spacing
    topsep=2pt,              % Small gap before list starts
    label=\textbullet        % Standard bullet (•)
}

% Alternative: use en-dash as bullet for a modern look
% label=\textendash

% Alternative: use a small filled circle
% label={\small\textbullet}
```

---

## 6. What NOT to Do

### 6.1 Design Anti-Patterns

| Anti-Pattern | Why It Fails | What To Do Instead |
|-------------|-------------|-------------------|
| **Infographic resume** | ATS can't read it; screams "junior designer," not "finance professional" | Clean text-based layout |
| **Skill bars / progress circles** | Arbitrary, meaningless (what is "80% Excel"?), takes up space | List skills as text: "Financial Modeling, DCF, LBO, Comps" |
| **Multiple colors (3+)** | Looks like a children's book, not a professional document | Max 2 colors beyond black |
| **Gradients** | Screams 2010; prints terribly | Flat, solid colors only |
| **Background colors on sections** | Clutter, printing issues, ATS confusion | White background always |
| **Photo on resume** | Not standard in US/UK (discrimination concerns); wastes space | No photo unless required by local convention (Germany, some EU) |
| **Icons everywhere** | Visual noise; signals "I used a template from Creative Market" | Text labels only |
| **Fancy borders or boxes** | Makes resume look like a flyer | Clean whitespace separation |
| **Multiple font families (3+)** | Typographic chaos | Max 2 font families (serif + sans-serif, or one family with weight variation) |
| **Justified body text** | Creates uneven word spacing in narrow columns | Left-aligned (ragged right) for body text |
| **Cramming to fill every inch** | Recruiter fatigue; signals "can't prioritize" | Embrace whitespace; edit content ruthlessly |

### 6.2 Dated Design Trends to Avoid

| Trend | Era | Why It's Dated |
|-------|-----|---------------|
| Objective statements | Pre-2015 | Replaced by professional summary or nothing |
| "References available upon request" | Pre-2010 | Everyone knows this; wastes a line |
| Heavy black borders | 2005-era Word templates | Looks like a wanted poster |
| Colored sidebar backgrounds | 2015–2020 template trend | Every Canva/Etsy template has this |
| Circular skill indicators | 2016–2020 | The design equivalent of clipart |
| QR codes | 2012–2018 | Nobody scans them; use a hyperlink |
| Header with a colored banner | Peak Canva 2018 | Now says "I Googled 'modern resume template'" |

### 6.3 ATS Killers — Technical Failures

1. **Text in images:** If your name or sections are images, ATS sees nothing
2. **Headers/footers with critical info:** Many ATS skip header/footer zones
3. **Non-standard section names:** Use "Experience" not "My Journey"; "Education" not "Where I Learned"
4. **Tables for layout:** Some ATS struggle with table-based layouts (ironic since many templates use them). LaTeX `tabularx` for within-section alignment is fine; avoid wrapping the entire resume in a table.
5. **Columns parsed wrong:** ATS may read left column top-to-bottom, then right column — jumbling your timeline
6. **Missing text layer:** Image-only PDFs (from scanning or rasterized export) have no parseable text

---

## 7. Cover Letter Design

### 7.1 Design Matching

The cover letter must look like it belongs with the resume:

- **Same fonts** (identical family, weights, sizes for name/headers)
- **Same color palette** (same hex codes)
- **Same header block** (your name + contact info, identical layout)
- **Same margins** (or very close)
- **Same rule style** (if resume has a thin rule under the name, cover letter does too)

### 7.2 Cover Letter Layout

```
┌─────────────────────────────────────────────┐
│           FIRSTNAME LASTNAME                 │ ← Identical to resume header
│    email · phone · city · linkedin           │
│ ──────────────────────────────────────────── │ ← Same rule as resume
│                                              │
│ Date                                         │
│                                              │
│ Hiring Manager Name                          │
│ Company Name                                 │
│ Address (optional)                           │
│                                              │
│ Dear [Name / Hiring Team],                   │
│                                              │
│ [Opening paragraph — why this firm, why now] │
│                                              │
│ [Middle — 2-3 examples from your experience] │
│                                              │
│ [Closing — call to action]                   │
│                                              │
│ Sincerely,                                   │
│ Firstname Lastname                           │
└─────────────────────────────────────────────┘
```

### 7.3 Cover Letter Typography

| Element | Spec |
|---------|------|
| Body font size | Same as resume body (10–11pt) |
| Line spacing | 1.15–1.30 (slightly more generous than resume) |
| Paragraph spacing | 6–10pt between paragraphs |
| Total length | 3–4 paragraphs, never more than 1 page |
| Margins | Same as resume or slightly wider (20–25mm) |

---

## 8. Quick Decision Matrix

| If You're Applying To… | Font | Color | Layout | Vibe |
|------------------------|------|-------|--------|------|
| Goldman / Morgan Stanley | Calibri or Garamond, 10.5pt | Black only | Single column | Conservative, content-heavy |
| McKinsey / BCG / Bain | Calibri or Arial, 11pt | Black only | Single column | Structured, metric-driven |
| a16z / Sequoia / Benchmark | Inter or Source Sans Pro, 10.5pt | Navy accent | Single column | Modern, clean, slightly designed |
| Early-stage VC fund | Inter or EB Garamond, 10.5pt | Navy accent | Single column | Personality ok, still professional |
| Tech company (FAANG) | Roboto or Inter, 10.5pt | One accent color | Single column | Modern, ATS-optimized |
| Startup | More flexibility | Navy or brand color | Single column preferred | Show taste, not templates |

---

## 9. The "Designed But Not Over-Designed" Checklist

Before finalizing your resume, verify:

- [ ] Can I read every word when printed in B&W on a cheap office printer?
- [ ] Is there only ONE accent color (beyond black and gray)?
- [ ] Are all section headers formatted identically?
- [ ] Are all dates formatted identically and right-aligned?
- [ ] Is there zero decorative clutter (icons, bars, circles, borders)?
- [ ] Does the whitespace feel generous but not empty (~40–50%)?
- [ ] Would this look at home on a partner's desk at Goldman Sachs?
- [ ] Does the PDF text layer parse correctly? (Copy-paste test)
- [ ] Is the font embedded in the PDF? (Check in PDF properties)
- [ ] Does the cover letter header match the resume exactly?
- [ ] Are en-dashes used for date ranges?
- [ ] Is microtypography enabled (`microtype` package)?
- [ ] When I squint, is there a clear visual hierarchy (name > headers > content)?

---

## 10. Reference Measurements Summary

| Element | Measurement |
|---------|------------|
| Name font size | 20–26pt |
| Section header font size | 11–13pt |
| Body font size | 10–10.5pt (sweet spot: **10.5pt**) |
| Date/location font size | 9–10pt |
| Line height | 1.08–1.20× body font |
| Section spacing | 10–14pt |
| Bullet item spacing | 1–3pt |
| Header rule thickness | 0.4–0.5pt (sections), 0.8–1pt (under name) |
| Margins (tight) | 15mm all sides |
| Margins (comfortable) | 18–22mm all sides |
| Margin minimum | 12mm (below this = printing risk) |
| Optimal line length | 50–75 characters |
| Whitespace ratio | 40–50% of page |
| Letter spacing for headers | +50 to +80 (0.05–0.08em) |
| Maximum colors | 2 (beyond black) |
| Page count | 1 page (unless 10+ years experience) |

---

*Last updated: 2026-02-04*
*Sources: Goldman Sachs recruiter guidelines, Harvard OCS, Wall Street Oasis, NN/g design research, CTAN LaTeX documentation, typography psychology studies, ATS compatibility testing reports.*
