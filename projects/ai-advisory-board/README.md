# AI Advisory Board

Get 6 expert perspectives on any decision in seconds.

## Concept

Input a question or decision, and get instant feedback from 6 AI advisors with distinct perspectives:

1. **The Operator** - Ex-CEO, execution focus
2. **The Investor** - VC Partner, ROI focus  
3. **The Contrarian** - Devil's advocate, finds flaws
4. **The Technologist** - CTO, technical feasibility
5. **The Strategist** - McKinsey partner, frameworks
6. **The Customer** - End-user perspective

## Installation

```bash
npm install
```

## Setup

1. Copy `.env.example` to `.env`
2. Add your OpenAI API key:
```bash
export OPENAI_API_KEY=your-key-here
```

## Usage

```bash
node board.js "Your question here"
```

### Example

```bash
node board.js "Should I launch on Monday with an MVP or wait until the product is polished?"
```

This will:
- Consult all 6 advisors in parallel (using GPT-4o)
- Generate a beautiful HTML report with dark mode & glassmorphism
- Save to `output/your-question-slug.html`

## Features

✅ **6 Parallel API Calls** - Fast responses from all advisors  
✅ **Dark Mode Design** - Beautiful glassmorphism UI  
✅ **SVG Icons** - No emoji, clean vector graphics  
✅ **Google Fonts (Inter)** - Professional typography  
✅ **Print CSS** - PDF-ready reports  
✅ **Email-Gated Downloads** - Capture leads for deeper analysis  
✅ **Feedback Section** - Collect user input  
✅ **Gold Accent (#c8aa50)** - Distinct from other tools  

## Output

Reports are saved to `output/` directory with URL-friendly slugs.

Open the HTML file in any browser to view your advisory board session.

## Tech Stack

- **Node.js** - Runtime
- **OpenAI GPT-4o** - AI reasoning
- **Vanilla HTML/CSS/JS** - No framework bloat
- **Inter Font** - Google Fonts
- **Glassmorphism** - Modern UI design

## Design System

- **Background**: `#0a0a0a`
- **Accent**: `#c8aa50` (Gold)
- **Typography**: Inter (Google Fonts)
- **Cards**: Glassmorphism with backdrop blur
- **Icons**: SVG, no emoji

## License

MIT

---

Built with ❤️ by Florian Ziesche
