# Google Reviews Sentiment Analysis Pipeline

Professional sentiment analysis reports for Google Business Reviews.

## Overview

This tool automatically:
1. **Scrapes** Google Reviews for a business + 3 competitors
2. **Analyzes** sentiment, topics, trends using OpenAI GPT-4
3. **Generates** a professional HTML report (PDF-ready)

Perfect for:
- Lead generation (free report → sales conversation)
- Customer success (identify improvement areas)
- Competitive intelligence

## Requirements

```bash
# Install dependencies
pip3 install openai

# Install goplaces CLI (recommended for reliable scraping)
brew install goplaces
# OR: https://github.com/gocolly/goplaces

# Set API keys
export OPENAI_API_KEY="sk-..."
export GOOGLE_PLACES_API_KEY="your-google-api-key"  # Required for goplaces
```

## Quick Test (No API Keys Required)

```bash
# Generate a test report with mock data to see the output format
python3 test_with_mock_data.py
# Opens: example/erbgericht_report.html
```

## Usage

```bash
# Basic usage (requires API keys)
python3 generate_report.py "Hotel Erbgericht" "Glashütte" --output report.html

# With custom category for competitor search
python3 generate_report.py "Müller GmbH" "Dresden" --category "restaurant" -o mueller_report.html
```

### Arguments

- `business_name` — Name of the business to analyze
- `location` — City or area (e.g., "Glashütte", "Dresden Altstadt")
- `--output` / `-o` — Output file path (default: `report.html`)
- `--category` / `-c` — Business category for competitor search (optional, auto-detected)

## Output

The report includes:

**Cover Page**
- Ainary Ventures branding
- Business name
- Confidentiality notice

**Executive Summary**
- Overall rating
- Total reviews count
- Sentiment score (0-100)
- Trend indicator (improving/stable/declining)
- Sentiment distribution (positive/neutral/negative)

**Insights**
- Top 5 praised aspects
- Top 5 complaints
- Trend explanation
- Keyword cloud

**Competition**
- Comparison table with 3 competitors
- Contextual analysis

**Recommendations**
- 5 prioritized action items (high/medium/low)
- Detailed descriptions

**Back Cover**
- CTA for conversation
- Contact information

## How to Save as PDF

1. Open the HTML file in your browser
2. Press `Cmd+P` (Mac) or `Ctrl+P` (Windows)
3. Select "Save as PDF"
4. Adjust margins if needed (recommended: default)

The report is optimized for A4 print format.

## Design

- **Colors:** Ainary brand (#0a0a0a black, #2563eb blue)
- **Typography:** System fonts (SF Pro, Segoe UI)
- **Layout:** A4 format, 25mm margins
- **Language:** German throughout
- **Style:** Professional, McKinsey-style consulting report

## Troubleshooting

### "goplaces not found"
Install goplaces CLI or use alternative scraping methods (automatic fallback).

### "OpenAI API error"
- Check `OPENAI_API_KEY` is set: `echo $OPENAI_API_KEY`
- Verify API quota/billing: https://platform.openai.com/account/usage

### "No reviews found"
- Verify business name spelling
- Try adding more location context (e.g., "Dresden Altstadt" instead of "Dresden")
- Check if business has Google My Business listing

### Report looks broken
- Open in Chrome/Safari (best compatibility)
- Ensure UTF-8 encoding (automatic in modern browsers)

## Examples

```bash
# Restaurant analysis
python3 generate_report.py "Zum Goldenen Löwen" "Leipzig" -o restaurant_report.html

# Hotel analysis
python3 generate_report.py "Hotel Vier Jahreszeiten" "München" -c hotel -o hotel_report.html

# Service business
python3 generate_report.py "Schmidt Autowerkstatt" "Berlin Mitte" -o autowerkstatt.html
```

## Tech Stack

- **Python 3** — Core logic
- **goplaces CLI** — Google Places API wrapper (primary data source)
- **OpenAI API** — GPT-4o-mini for sentiment analysis
- **HTML/CSS** — Report generation (no JS dependencies)

## License

Internal tool — Ainary Ventures

## Contact

Florian Ziesche  
florian@ainaryventures.com  
https://ainaryventures.com
