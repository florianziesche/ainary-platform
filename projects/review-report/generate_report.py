#!/usr/bin/env python3
"""
Google Reviews Sentiment Analysis Pipeline
Generates professional PDF reports for businesses.
"""

import argparse
import json
import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional
import re

try:
    import openai
except ImportError:
    print("❌ openai module not found. Install: pip3 install openai")
    sys.exit(1)


class ReviewScraper:
    """Scrapes Google Reviews using goplaces CLI."""
    
    def __init__(self):
        self.goplaces_available = self._check_goplaces()
    
    def _check_goplaces(self) -> bool:
        """Check if goplaces CLI is available."""
        try:
            subprocess.run(['which', 'goplaces'], capture_output=True, check=True)
            return True
        except subprocess.CalledProcessError:
            return False
    
    def scrape_business(self, name: str, location: str) -> Optional[Dict]:
        """Scrape reviews for a business."""
        if not self.goplaces_available:
            print("⚠️  goplaces CLI not available. Install from: github.com/gocolly/goplaces")
            return None
        
        print(f"🔍 Searching for: {name} in {location}")
        
        # Step 1: Search for place
        search_query = f"{name} {location}"
        try:
            result = subprocess.run(
                ['goplaces', 'search', search_query],
                capture_output=True,
                text=True,
                timeout=30
            )
            
            if result.returncode != 0:
                print(f"⚠️  Search failed: {result.stderr}")
                return None
            
            # Parse search results (expecting JSON output)
            lines = result.stdout.strip().split('\n')
            if not lines:
                print("⚠️  No results found")
                return None
            
            # Take first result
            try:
                first_result = json.loads(lines[0])
                place_id = first_result.get('place_id')
                if not place_id:
                    print("⚠️  No place_id in result")
                    return None
            except json.JSONDecodeError:
                # Fallback: extract place_id from text output
                for line in lines:
                    if 'place_id' in line.lower() or 'ChIJ' in line:
                        # Try to extract ChIJ... pattern
                        match = re.search(r'(ChIJ[a-zA-Z0-9_-]+)', line)
                        if match:
                            place_id = match.group(1)
                            break
                else:
                    print(f"⚠️  Could not parse place_id from output:\n{result.stdout[:200]}")
                    return None
            
            print(f"✓ Found place_id: {place_id}")
            
            # Step 2: Get details
            details_result = subprocess.run(
                ['goplaces', 'details', place_id],
                capture_output=True,
                text=True,
                timeout=30
            )
            
            if details_result.returncode != 0:
                print(f"⚠️  Details fetch failed: {details_result.stderr}")
                return None
            
            try:
                details = json.loads(details_result.stdout)
            except json.JSONDecodeError:
                print(f"⚠️  Could not parse details JSON")
                return None
            
            # Step 3: Get reviews
            reviews_result = subprocess.run(
                ['goplaces', 'reviews', place_id],
                capture_output=True,
                text=True,
                timeout=30
            )
            
            reviews = []
            if reviews_result.returncode == 0:
                try:
                    reviews_data = json.loads(reviews_result.stdout)
                    reviews = reviews_data.get('reviews', [])
                except json.JSONDecodeError:
                    # Try parsing line-by-line
                    for line in reviews_result.stdout.strip().split('\n'):
                        try:
                            review = json.loads(line)
                            reviews.append(review)
                        except:
                            pass
            
            return {
                'name': details.get('name', name),
                'rating': details.get('rating', 0),
                'total_reviews': details.get('user_ratings_total', len(reviews)),
                'address': details.get('formatted_address', location),
                'reviews': reviews[:50]  # Limit to 50 reviews
            }
            
        except subprocess.TimeoutExpired:
            print("⚠️  Request timed out")
            return None
        except Exception as e:
            print(f"⚠️  Error: {e}")
            return None
    
    def find_competitors(self, category: str, location: str, count: int = 3) -> List[Dict]:
        """Find competitor businesses in the same category/location."""
        if not self.goplaces_available:
            return []
        
        print(f"🔍 Finding {count} competitors: {category} in {location}")
        
        # Search for category + location
        search_query = f"{category} {location}"
        try:
            result = subprocess.run(
                ['goplaces', 'search', search_query],
                capture_output=True,
                text=True,
                timeout=30
            )
            
            if result.returncode != 0:
                return []
            
            competitors = []
            lines = result.stdout.strip().split('\n')
            
            for line in lines[:count + 2]:  # Get a few extra in case some fail
                if len(competitors) >= count:
                    break
                
                try:
                    place = json.loads(line)
                    place_id = place.get('place_id')
                    if not place_id:
                        continue
                    
                    # Get basic info
                    competitors.append({
                        'name': place.get('name', 'Unknown'),
                        'rating': place.get('rating', 0),
                        'total_reviews': place.get('user_ratings_total', 0)
                    })
                    
                except json.JSONDecodeError:
                    continue
            
            print(f"✓ Found {len(competitors)} competitors")
            return competitors
            
        except Exception as e:
            print(f"⚠️  Competitor search error: {e}")
            return []


class SentimentAnalyzer:
    """Analyzes reviews using OpenAI API."""
    
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv('OPENAI_API_KEY')
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY not set")
        
        self.client = openai.OpenAI(api_key=self.api_key)
    
    def analyze_reviews(self, business_data: Dict, competitors: List[Dict]) -> Dict:
        """Analyze reviews and generate insights."""
        
        reviews = business_data.get('reviews', [])
        
        if not reviews:
            return self._generate_fallback_analysis(business_data, competitors)
        
        # Prepare review texts
        review_texts = []
        for i, review in enumerate(reviews[:30]):  # Analyze max 30 reviews
            text = review.get('text', '')
            rating = review.get('rating', 0)
            review_texts.append(f"Review {i+1} ({rating}★): {text}")
        
        reviews_combined = "\n\n".join(review_texts)
        
        # Build prompt
        prompt = f"""Analysiere die folgenden Google-Bewertungen für das Unternehmen "{business_data['name']}".

BEWERTUNGEN:
{reviews_combined}

WETTBEWERBER:
{json.dumps(competitors, ensure_ascii=False)}

Erstelle eine strukturierte Analyse im JSON-Format:

{{
  "sentiment_distribution": {{
    "positive": <Anzahl positiver Reviews>,
    "neutral": <Anzahl neutraler Reviews>,
    "negative": <Anzahl negativer Reviews>
  }},
  "top_praise": [
    "Punkt 1",
    "Punkt 2",
    "Punkt 3",
    "Punkt 4",
    "Punkt 5"
  ],
  "top_complaints": [
    "Punkt 1",
    "Punkt 2",
    "Punkt 3",
    "Punkt 4",
    "Punkt 5"
  ],
  "trend": "verbessert|stabil|verschlechtert",
  "trend_explanation": "Kurze Begründung",
  "competitor_comparison": "Kurzer Vergleich mit Wettbewerbern (2-3 Sätze)",
  "recommendations": [
    {{
      "title": "Empfehlung 1",
      "description": "Details",
      "priority": "hoch|mittel|niedrig"
    }},
    // ... 4 weitere
  ],
  "keywords": ["Keyword1", "Keyword2", ...],  // Top 15 häufigste Wörter
  "sentiment_score": <0-100>  // Gesamtstimmung
}}

Antworte NUR mit dem JSON, keine Erklärung davor oder danach."""

        print("🤖 Analyzing with OpenAI...")
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "Du bist ein Experte für Sentiment-Analyse von Kundenbewertungen. Antworte immer mit validem JSON."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3,
                max_tokens=2000
            )
            
            content = response.choices[0].message.content.strip()
            
            # Extract JSON if wrapped in markdown
            if content.startswith('```'):
                content = re.sub(r'^```json?\n', '', content)
                content = re.sub(r'\n```$', '', content)
            
            analysis = json.loads(content)
            print("✓ Analysis complete")
            return analysis
            
        except Exception as e:
            print(f"⚠️  OpenAI API error: {e}")
            return self._generate_fallback_analysis(business_data, competitors)
    
    def _generate_fallback_analysis(self, business_data: Dict, competitors: List[Dict]) -> Dict:
        """Generate basic analysis without LLM."""
        return {
            "sentiment_distribution": {
                "positive": 0,
                "neutral": 0,
                "negative": 0
            },
            "top_praise": [
                "Keine ausreichenden Daten",
                "", "", "", ""
            ],
            "top_complaints": [
                "Keine ausreichenden Daten",
                "", "", "", ""
            ],
            "trend": "stabil",
            "trend_explanation": "Nicht genug Daten für Trend-Analyse",
            "competitor_comparison": "Wettbewerbsdaten nicht verfügbar",
            "recommendations": [
                {
                    "title": "Mehr Bewertungen sammeln",
                    "description": "Aktiv Kunden um Bewertungen bitten",
                    "priority": "hoch"
                }
            ],
            "keywords": [],
            "sentiment_score": int(business_data.get('rating', 3) * 20)
        }


class ReportGenerator:
    """Generates HTML report."""
    
    def __init__(self):
        self.template_path = Path(__file__).parent / 'template.html'
    
    def generate(self, business_data: Dict, analysis: Dict, competitors: List[Dict], output_path: str):
        """Generate HTML report."""
        
        # Load template
        if self.template_path.exists():
            template = self.template_path.read_text()
        else:
            template = self._get_default_template()
        
        # Prepare data
        created_date = datetime.now().strftime('%d.%m.%Y')
        
        sentiment_dist = analysis.get('sentiment_distribution', {})
        total_analyzed = sum(sentiment_dist.values()) or 1
        
        # Calculate percentages
        positive_pct = int((sentiment_dist.get('positive', 0) / total_analyzed) * 100)
        neutral_pct = int((sentiment_dist.get('neutral', 0) / total_analyzed) * 100)
        negative_pct = int((sentiment_dist.get('negative', 0) / total_analyzed) * 100)
        
        # Top praise/complaints
        top_praise_html = self._generate_list(analysis.get('top_praise', []))
        top_complaints_html = self._generate_list(analysis.get('top_complaints', []))
        
        # Competitors table
        competitors_html = self._generate_competitors_table(business_data, competitors)
        
        # Recommendations
        recommendations_html = self._generate_recommendations(analysis.get('recommendations', []))
        
        # Keywords word cloud
        keywords_html = self._generate_keywords(analysis.get('keywords', []))
        
        # Trend indicator
        trend = analysis.get('trend', 'stabil')
        trend_icons = {
            'verbessert': '📈',
            'stabil': '➡️',
            'verschlechtert': '📉'
        }
        trend_icon = trend_icons.get(trend, '➡️')
        
        # Replace placeholders
        html = template
        replacements = {
            '{{BUSINESS_NAME}}': business_data.get('name', 'Unbekannt'),
            '{{CREATED_DATE}}': created_date,
            '{{OVERALL_RATING}}': f"{business_data.get('rating', 0):.1f}",
            '{{TOTAL_REVIEWS}}': str(business_data.get('total_reviews', 0)),
            '{{SENTIMENT_SCORE}}': str(analysis.get('sentiment_score', 0)),
            '{{TREND}}': trend.capitalize(),
            '{{TREND_ICON}}': trend_icon,
            '{{POSITIVE_PCT}}': str(positive_pct),
            '{{NEUTRAL_PCT}}': str(neutral_pct),
            '{{NEGATIVE_PCT}}': str(negative_pct),
            '{{POSITIVE_COUNT}}': str(sentiment_dist.get('positive', 0)),
            '{{NEUTRAL_COUNT}}': str(sentiment_dist.get('neutral', 0)),
            '{{NEGATIVE_COUNT}}': str(sentiment_dist.get('negative', 0)),
            '{{TOP_PRAISE}}': top_praise_html,
            '{{TOP_COMPLAINTS}}': top_complaints_html,
            '{{COMPETITORS_TABLE}}': competitors_html,
            '{{RECOMMENDATIONS}}': recommendations_html,
            '{{KEYWORDS}}': keywords_html,
            '{{TREND_EXPLANATION}}': analysis.get('trend_explanation', ''),
            '{{COMPETITOR_COMPARISON}}': analysis.get('competitor_comparison', 'Keine Vergleichsdaten verfügbar'),
            '{{ADDRESS}}': business_data.get('address', '')
        }
        
        for placeholder, value in replacements.items():
            html = html.replace(placeholder, str(value))
        
        # Write output
        output_file = Path(output_path)
        output_file.write_text(html, encoding='utf-8')
        
        print(f"✅ Report generated: {output_path}")
        print(f"   Open in browser to save as PDF (Cmd+P → Save as PDF)")
    
    def _generate_list(self, items: List[str]) -> str:
        """Generate HTML list."""
        html = '<ul class="insight-list">'
        for item in items:
            if item and item.strip():
                html += f'<li>{item}</li>'
        html += '</ul>'
        return html
    
    def _generate_competitors_table(self, business: Dict, competitors: List[Dict]) -> str:
        """Generate competitor comparison table."""
        html = '<table class="competitors-table">'
        html += '<tr><th>Unternehmen</th><th>Bewertung</th><th>Anzahl Reviews</th></tr>'
        
        # Add main business first
        html += f'''<tr class="main-business">
            <td><strong>{business.get('name', 'Unbekannt')}</strong> (Sie)</td>
            <td>{business.get('rating', 0):.1f} ★</td>
            <td>{business.get('total_reviews', 0)}</td>
        </tr>'''
        
        # Add competitors
        for comp in competitors:
            html += f'''<tr>
                <td>{comp.get('name', 'Unbekannt')}</td>
                <td>{comp.get('rating', 0):.1f} ★</td>
                <td>{comp.get('total_reviews', 0)}</td>
            </tr>'''
        
        html += '</table>'
        return html
    
    def _generate_recommendations(self, recommendations: List[Dict]) -> str:
        """Generate recommendations section."""
        html = ''
        
        priority_colors = {
            'hoch': '#dc2626',
            'mittel': '#f59e0b',
            'niedrig': '#10b981'
        }
        
        for i, rec in enumerate(recommendations, 1):
            priority = rec.get('priority', 'mittel')
            color = priority_colors.get(priority, '#6b7280')
            
            html += f'''
            <div class="recommendation">
                <div class="recommendation-header">
                    <span class="recommendation-number">{i}</span>
                    <h3>{rec.get('title', 'Empfehlung')}</h3>
                    <span class="priority" style="background-color: {color};">{priority.upper()}</span>
                </div>
                <p>{rec.get('description', '')}</p>
            </div>
            '''
        
        return html
    
    def _generate_keywords(self, keywords: List[str]) -> str:
        """Generate keyword word cloud (CSS-based)."""
        if not keywords:
            return '<p class="no-data">Keine Keywords verfügbar</p>'
        
        html = '<div class="word-cloud">'
        
        # Size by position (first = biggest)
        for i, keyword in enumerate(keywords[:15]):
            size = max(12, 28 - i * 1.2)  # Descending size
            html += f'<span style="font-size: {size}px;">{keyword}</span> '
        
        html += '</div>'
        return html
    
    def _get_default_template(self) -> str:
        """Return default HTML template."""
        return """<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kundenanalyse – {{BUSINESS_NAME}}</title>
    <style>
        @page {
            size: A4;
            margin: 0;
        }
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            line-height: 1.6;
            color: #0a0a0a;
            background: #fff;
        }
        
        .page {
            width: 210mm;
            min-height: 297mm;
            padding: 25mm;
            margin: 0 auto;
            background: white;
            page-break-after: always;
        }
        
        .cover {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            min-height: 247mm;
        }
        
        .logo {
            font-size: 32px;
            font-weight: 700;
            color: #0a0a0a;
            margin-bottom: 60px;
            letter-spacing: -0.5px;
        }
        
        h1 {
            font-size: 48px;
            font-weight: 700;
            margin-bottom: 20px;
            color: #0a0a0a;
        }
        
        .subtitle {
            font-size: 24px;
            color: #6b7280;
            margin-bottom: 10px;
        }
        
        .company-name {
            font-size: 36px;
            font-weight: 600;
            color: #2563eb;
            margin: 30px 0;
        }
        
        .date {
            font-size: 14px;
            color: #6b7280;
            margin-top: 60px;
        }
        
        .confidential {
            font-size: 12px;
            color: #9ca3af;
            margin-top: 20px;
            font-style: italic;
        }
        
        .content {
            padding-top: 20mm;
        }
        
        h2 {
            font-size: 28px;
            font-weight: 700;
            margin-bottom: 20px;
            color: #0a0a0a;
            border-bottom: 3px solid #2563eb;
            padding-bottom: 10px;
        }
        
        h3 {
            font-size: 20px;
            font-weight: 600;
            margin: 25px 0 15px 0;
            color: #0a0a0a;
        }
        
        .kpi-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 20px;
            margin: 30px 0;
        }
        
        .kpi-card {
            background: #f9fafb;
            border: 1px solid #e5e7eb;
            border-radius: 8px;
            padding: 20px;
            text-align: center;
        }
        
        .kpi-value {
            font-size: 42px;
            font-weight: 700;
            color: #2563eb;
            margin: 10px 0;
        }
        
        .kpi-label {
            font-size: 14px;
            color: #6b7280;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        
        .sentiment-bars {
            margin: 30px 0;
        }
        
        .sentiment-bar {
            margin-bottom: 15px;
        }
        
        .sentiment-label {
            display: flex;
            justify-content: space-between;
            margin-bottom: 5px;
            font-size: 14px;
        }
        
        .bar-container {
            height: 30px;
            background: #f3f4f6;
            border-radius: 6px;
            overflow: hidden;
            position: relative;
        }
        
        .bar-fill {
            height: 100%;
            transition: width 0.3s;
            display: flex;
            align-items: center;
            padding-left: 10px;
            color: white;
            font-weight: 600;
            font-size: 13px;
        }
        
        .bar-positive { background: #10b981; }
        .bar-neutral { background: #f59e0b; }
        .bar-negative { background: #dc2626; }
        
        .insight-list {
            list-style: none;
            padding: 0;
        }
        
        .insight-list li {
            padding: 12px 0;
            border-bottom: 1px solid #f3f4f6;
            padding-left: 25px;
            position: relative;
        }
        
        .insight-list li:before {
            content: "→";
            position: absolute;
            left: 0;
            color: #2563eb;
            font-weight: bold;
        }
        
        .competitors-table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }
        
        .competitors-table th {
            background: #f9fafb;
            padding: 12px;
            text-align: left;
            font-weight: 600;
            border-bottom: 2px solid #e5e7eb;
        }
        
        .competitors-table td {
            padding: 12px;
            border-bottom: 1px solid #f3f4f6;
        }
        
        .competitors-table .main-business {
            background: #eff6ff;
            font-weight: 600;
        }
        
        .recommendation {
            background: #f9fafb;
            border-left: 4px solid #2563eb;
            padding: 20px;
            margin-bottom: 20px;
            border-radius: 4px;
        }
        
        .recommendation-header {
            display: flex;
            align-items: center;
            gap: 15px;
            margin-bottom: 10px;
        }
        
        .recommendation-number {
            background: #2563eb;
            color: white;
            width: 32px;
            height: 32px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 700;
            flex-shrink: 0;
        }
        
        .recommendation h3 {
            margin: 0;
            flex-grow: 1;
            font-size: 18px;
        }
        
        .priority {
            padding: 4px 12px;
            border-radius: 12px;
            color: white;
            font-size: 11px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        
        .word-cloud {
            background: #f9fafb;
            padding: 30px;
            border-radius: 8px;
            text-align: center;
            line-height: 2.5;
            margin: 20px 0;
        }
        
        .word-cloud span {
            display: inline-block;
            margin: 5px 10px;
            color: #2563eb;
            font-weight: 600;
        }
        
        .back-cover {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            min-height: 247mm;
            background: linear-gradient(135deg, #0a0a0a 0%, #1e293b 100%);
            color: white;
        }
        
        .back-cover .logo {
            color: white;
            margin-bottom: 40px;
        }
        
        .cta {
            font-size: 28px;
            font-weight: 600;
            margin-bottom: 30px;
            max-width: 600px;
            line-height: 1.4;
        }
        
        .contact {
            font-size: 18px;
            margin: 10px 0;
            color: #cbd5e1;
        }
        
        .contact a {
            color: #60a5fa;
            text-decoration: none;
        }
        
        .footer {
            position: absolute;
            bottom: 20mm;
            left: 25mm;
            right: 25mm;
            text-align: center;
            font-size: 11px;
            color: #9ca3af;
            padding-top: 20px;
            border-top: 1px solid #e5e7eb;
        }
        
        .no-data {
            color: #9ca3af;
            font-style: italic;
            padding: 20px;
            text-align: center;
        }
        
        @media print {
            body {
                background: white;
            }
            .page {
                margin: 0;
                page-break-after: always;
            }
            .footer {
                position: fixed;
            }
        }
    </style>
</head>
<body>
    <!-- Cover Page -->
    <div class="page cover">
        <div class="logo">AINARY VENTURES</div>
        <h1>Kundenanalyse</h1>
        <div class="subtitle">Google Reviews Sentiment Report</div>
        <div class="company-name">{{BUSINESS_NAME}}</div>
        <div class="date">Erstellt am {{CREATED_DATE}}</div>
        <div class="confidential">Vertraulich – erstellt für {{BUSINESS_NAME}}</div>
    </div>
    
    <!-- Executive Summary -->
    <div class="page content">
        <h2>Überblick</h2>
        
        <div class="kpi-grid">
            <div class="kpi-card">
                <div class="kpi-label">Gesamtbewertung</div>
                <div class="kpi-value">{{OVERALL_RATING}} ★</div>
            </div>
            <div class="kpi-card">
                <div class="kpi-label">Anzahl Bewertungen</div>
                <div class="kpi-value">{{TOTAL_REVIEWS}}</div>
            </div>
            <div class="kpi-card">
                <div class="kpi-label">Sentiment Score</div>
                <div class="kpi-value">{{SENTIMENT_SCORE}}</div>
            </div>
            <div class="kpi-card">
                <div class="kpi-label">Trend</div>
                <div class="kpi-value" style="font-size: 32px;">{{TREND_ICON}} {{TREND}}</div>
            </div>
        </div>
        
        <h3>Standort</h3>
        <p>{{ADDRESS}}</p>
        
        <h3>Sentiment-Verteilung</h3>
        <div class="sentiment-bars">
            <div class="sentiment-bar">
                <div class="sentiment-label">
                    <span>😊 Positiv</span>
                    <span>{{POSITIVE_COUNT}} ({{POSITIVE_PCT}}%)</span>
                </div>
                <div class="bar-container">
                    <div class="bar-fill bar-positive" style="width: {{POSITIVE_PCT}}%;">
                        {{POSITIVE_PCT}}%
                    </div>
                </div>
            </div>
            
            <div class="sentiment-bar">
                <div class="sentiment-label">
                    <span>😐 Neutral</span>
                    <span>{{NEUTRAL_COUNT}} ({{NEUTRAL_PCT}}%)</span>
                </div>
                <div class="bar-container">
                    <div class="bar-fill bar-neutral" style="width: {{NEUTRAL_PCT}}%;">
                        {{NEUTRAL_PCT}}%
                    </div>
                </div>
            </div>
            
            <div class="sentiment-bar">
                <div class="sentiment-label">
                    <span>😞 Negativ</span>
                    <span>{{NEGATIVE_COUNT}} ({{NEGATIVE_PCT}}%)</span>
                </div>
                <div class="bar-container">
                    <div class="bar-fill bar-negative" style="width: {{NEGATIVE_PCT}}%;">
                        {{NEGATIVE_PCT}}%
                    </div>
                </div>
            </div>
        </div>
        
        <div class="footer">
            Seite 2 · Ainary Ventures · {{CREATED_DATE}}
        </div>
    </div>
    
    <!-- Insights -->
    <div class="page content">
        <h2>Erkenntnisse</h2>
        
        <h3>✅ Top 5 – Was läuft gut</h3>
        {{TOP_PRAISE}}
        
        <h3>⚠️ Top 5 – Verbesserungspotenzial</h3>
        {{TOP_COMPLAINTS}}
        
        <h3>📊 Trend-Analyse</h3>
        <p>{{TREND_EXPLANATION}}</p>
        
        <h3>🔤 Häufigste Begriffe</h3>
        {{KEYWORDS}}
        
        <div class="footer">
            Seite 3 · Ainary Ventures · {{CREATED_DATE}}
        </div>
    </div>
    
    <!-- Competition -->
    <div class="page content">
        <h2>Wettbewerbsvergleich</h2>
        
        {{COMPETITORS_TABLE}}
        
        <h3>Einordnung</h3>
        <p>{{COMPETITOR_COMPARISON}}</p>
        
        <div class="footer">
            Seite 4 · Ainary Ventures · {{CREATED_DATE}}
        </div>
    </div>
    
    <!-- Recommendations -->
    <div class="page content">
        <h2>Handlungsempfehlungen</h2>
        
        {{RECOMMENDATIONS}}
        
        <div class="footer">
            Seite 5 · Ainary Ventures · {{CREATED_DATE}}
        </div>
    </div>
    
    <!-- Back Cover -->
    <div class="page back-cover">
        <div class="logo">AINARY VENTURES</div>
        <div class="cta">
            Möchten Sie Ihre Bewertungen systematisch verbessern?<br>
            Sprechen Sie mit uns.
        </div>
        <div class="contact">
            <a href="mailto:florian@ainaryventures.com">florian@ainaryventures.com</a>
        </div>
        <div class="contact">
            <a href="https://ainaryventures.com">ainaryventures.com</a>
        </div>
    </div>
</body>
</html>
"""


def main():
    parser = argparse.ArgumentParser(
        description='Generate Google Reviews Sentiment Analysis Report'
    )
    parser.add_argument('business_name', help='Name of the business')
    parser.add_argument('location', help='Location (city/area)')
    parser.add_argument('--output', '-o', default='report.html', help='Output file path')
    parser.add_argument('--category', '-c', help='Business category for competitor search (auto-detected if not provided)')
    
    args = parser.parse_args()
    
    print("=" * 60)
    print("Google Reviews Sentiment Analysis Pipeline")
    print("=" * 60)
    
    # Step 1: Scrape reviews
    scraper = ReviewScraper()
    business_data = scraper.scrape_business(args.business_name, args.location)
    
    if not business_data:
        print("❌ Could not fetch business data. Exiting.")
        sys.exit(1)
    
    # Step 2: Find competitors
    category = args.category or args.business_name.split()[0]  # Use first word as category
    competitors = scraper.find_competitors(category, args.location, count=3)
    
    # Step 3: Analyze with LLM
    try:
        analyzer = SentimentAnalyzer()
        analysis = analyzer.analyze_reviews(business_data, competitors)
    except Exception as e:
        print(f"⚠️  Analysis failed: {e}")
        print("Generating basic report without LLM analysis...")
        analysis = {
            "sentiment_distribution": {"positive": 0, "neutral": 0, "negative": 0},
            "top_praise": ["Keine Daten verfügbar"],
            "top_complaints": ["Keine Daten verfügbar"],
            "trend": "stabil",
            "trend_explanation": "Analyse nicht verfügbar",
            "competitor_comparison": "Vergleich nicht verfügbar",
            "recommendations": [],
            "keywords": [],
            "sentiment_score": 0
        }
    
    # Step 4: Generate report
    generator = ReportGenerator()
    generator.generate(business_data, analysis, competitors, args.output)
    
    print("=" * 60)
    print("✅ Pipeline complete!")
    print(f"   Open: {args.output}")
    print(f"   Save as PDF: Cmd+P → Save as PDF")
    print("=" * 60)


if __name__ == '__main__':
    main()
