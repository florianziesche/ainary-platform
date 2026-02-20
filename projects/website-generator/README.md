# Website Generator for Small Businesses

Automated pipeline to create professional, self-contained HTML websites for local businesses using real business data.

## Features

- **Research-driven**: Scrapes Google Business Profile, existing websites, and web search results
- **LLM-powered content**: Uses GPT-4o-mini to generate authentic German copy
- **World-class design**: Professional, modern, responsive (like Stripe/Linear/Vercel)
- **Zero dependencies**: Pure HTML + CSS + vanilla JS (no Bootstrap, no jQuery, no CDN)
- **SEO-ready**: Meta tags, Schema.org structured data, semantic HTML
- **Mobile-first**: Works perfectly on all devices
- **Fast**: Optimized for 95+ Lighthouse Performance score

## Requirements

1. **Python 3** (standard library only)
2. **goplaces CLI**: Install from [goplaces](https://github.com/peterheb/goplaces)
   ```bash
   # macOS
   brew install goplaces
   ```
3. **Environment variables**:
   ```bash
   export OPENAI_API_KEY="sk-..."
   export BRAVE_API_KEY="..."  # Optional but recommended
   ```

## Installation

```bash
cd ~/.openclaw/workspace/projects/website-generator
chmod +x generate_website.py
```

## Usage

```bash
python3 generate_website.py "Firma Name" "Ort" --branche "Bäckerei" --output output/
```

### Arguments

- `name` (required): Business name
- `location` (required): City/town
- `--branche` (optional): Industry type (Bäckerei, Restaurant, Elektriker, etc.)
- `--output` (optional): Output directory (default: `output/`)

### Examples

```bash
# Bakery in Glashütte
python3 generate_website.py "Bäckerei Müller" "Glashütte" --branche "Bäckerei"

# Restaurant in Dresden
python3 generate_website.py "Gasthof Zur Post" "Dresden" --branche "Restaurant"

# Electrician in Berlin
python3 generate_website.py "Elektro Schmidt" "Berlin" --branche "Elektriker"

# Auto-detect industry
python3 generate_website.py "Café Glück" "München"
```

## Pipeline Steps

### 1. Research the Business

- **Google Places**: Business details, reviews, photos, hours, phone, address
- **Brave Search**: Find existing website, social media, additional info
- **Web Scraping**: If existing website found, extract content

### 2. Generate Content (LLM)

Uses OpenAI GPT-4o-mini to create:

- Hero headline (emotional, not generic)
- Subline (benefit-focused)
- About section (from real data or industry-appropriate)
- Services/Products (real or industry defaults)
- Testimonials (real Google reviews or realistic generated ones)
- CTAs (action-oriented)
- Meta description (SEO)

**All content in German**

### 3. Generate HTML/CSS

Creates a single `index.html` file with:

- **Sections**: Hero, Über Uns, Leistungen, Bewertungen, FAQ, Kontakt, Footer
- **Design**: Professional, generous whitespace, large typography
- **Responsive**: Mobile-first, works on all devices
- **Fast**: No external dependencies, optimized images (CSS gradients for visuals)
- **Accessible**: Semantic HTML, ARIA labels, high contrast
- **Interactive**: Smooth scroll, fade-in animations, hover effects
- **Contact**: Google Maps embed, click-to-call phone link
- **SEO**: Schema.org LocalBusiness, meta tags, semantic structure
- **Branding**: "Website erstellt von Ainary Ventures" in footer

## Industry Templates

Pre-configured color schemes and content for:

- **Handwerk**: Elektriker, Installateur, Maler, Schreiner
- **Gastronomie**: Restaurant, Café, Bäckerei
- **Gesundheit**: Arzt, Physiotherapie, Zahnarzt
- **Dienstleistung**: Steuerberater, Rechtsanwalt, Friseur
- **Einzelhandel**: Blumen, Mode, Optiker
- **Default**: Neutral professional

Templates include:
- Primary color (trust, professionalism)
- Accent color (CTAs, highlights)
- Default services
- Industry-specific FAQs

## Output

```
output/
└── firma-name-ort/
    └── index.html    # Self-contained website (double-click to open)
```

The HTML file:
- Can be opened directly in any browser
- Can be deployed to any static host (Netlify, Vercel, GitHub Pages)
- Contains all CSS inline (no external stylesheets)
- Works offline

## Design Quality

**Principles:**
- Generous whitespace (padding: 80px+ between sections)
- Large typography (hero: 56px, body: 18px, line-height: 1.7)
- Subtle animations (fade-in on scroll, hover effects)
- One accent color + neutrals (no rainbow)
- Cards with subtle shadows
- Star ratings for reviews (pure CSS)
- Sticky navigation with blur backdrop
- Professional, not template-y

**Reference quality:** Like Stripe, Linear, Vercel landing pages — but for local businesses.

## Customization

### Edit Industry Templates

Edit `industries.json` to change:
- Colors (primary, accent)
- Default services
- FAQ questions/answers

### Modify Design

Edit the `<style>` section in `generate_website.py`:
- Colors: Search for `color_primary`, `color_accent`
- Typography: Search for `font-size`
- Spacing: Search for `padding`, `margin`
- Animations: Search for `@keyframes`, `transition`

## Testing

```bash
# Generate test website for a real business
python3 generate_website.py "Goldschmidt Café" "Glashütte" --branche "Café"

# Open output/goldschmidt-cafe-glashuette/index.html in browser
open output/goldschmidt-cafe-glashuette/index.html
```

**Checklist:**
- [ ] Opens in browser without errors
- [ ] All sections render correctly
- [ ] Mobile responsive (test on phone/tablet)
- [ ] Smooth scroll works
- [ ] Animations trigger on scroll
- [ ] Google Maps embed loads
- [ ] Phone link works (click-to-call)
- [ ] All text in German
- [ ] No Lorem Ipsum
- [ ] Footer includes "Ainary Ventures" credit

## Troubleshooting

**"goplaces: command not found"**
```bash
brew install goplaces
# or download from https://github.com/peterheb/goplaces
```

**"OPENAI_API_KEY not set"**
```bash
export OPENAI_API_KEY="sk-your-key-here"
```

**"No results found"**
- Check business name spelling
- Try adding more location details
- Verify business exists on Google Maps

**Content looks generic**
- Run again (LLM generates different content each time)
- Edit `index.html` manually after generation
- Improve prompt in `generate_content_with_llm()` function

## Roadmap

- [ ] Multi-page websites (Impressum, Datenschutz)
- [ ] Image optimization and hosting
- [ ] Form backend integration (contact forms)
- [ ] CMS integration (for client self-service)
- [ ] A/B testing variants
- [ ] Lighthouse score reporting

## License

MIT License

## Credits

**Design Principles**: Based on `standards/WEBSITE-DESIGN-GUIDE.md`  
**Built by**: Ainary Ventures  
**Website**: https://ainaryventures.com
