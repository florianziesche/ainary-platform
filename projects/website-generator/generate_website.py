#!/usr/bin/env python3
"""
Website Generator for Small Businesses
Generates professional, self-contained HTML websites from business data.

Usage:
    python3 generate_website.py "Firma Name" "Ort" --branche "Bäckerei" --output output/

Requirements:
    - goplaces CLI (for business data)
    - BRAVE_API_KEY env var (for web search)
    - OPENAI_API_KEY env var (for content generation)
"""

import argparse
import json
import os
import re
import subprocess
import sys
import urllib.request
import urllib.parse
from datetime import datetime
from pathlib import Path


def log(msg):
    """Print with timestamp"""
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}")


def run_command(cmd, capture=True):
    """Run shell command and return output"""
    try:
        if capture:
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=30)
            return result.stdout.strip() if result.returncode == 0 else None
        else:
            subprocess.run(cmd, shell=True, timeout=30)
            return True
    except Exception as e:
        log(f"Command failed: {cmd[:50]}... - {e}")
        return None


def search_goplaces(name, location):
    """Search for business using goplaces CLI"""
    log(f"Searching Google Places for '{name}' in '{location}'...")
    query = f"{name} {location}"
    cmd = f'goplaces search "{query}" --json --limit 1'
    output = run_command(cmd)
    
    if not output:
        log("goplaces search failed (might need GOOGLE_PLACES_API_KEY)")
        return None
    
    try:
        data = json.loads(output)
        # goplaces returns {"places": [...]}
        places = data.get('places', [])
        if places and len(places) > 0:
            place = places[0]
            place_id = place.get('id')
            if place_id:
                # Get detailed place info
                cmd_details = f'goplaces details {place_id} --json'
                details_output = run_command(cmd_details)
                if details_output:
                    return json.loads(details_output)
            return place
        return None
    except json.JSONDecodeError as e:
        log(f"Failed to parse goplaces output: {e}")
        return None


def brave_search(query):
    """Search web using Brave Search API"""
    api_key = os.getenv('BRAVE_API_KEY')
    if not api_key:
        log("BRAVE_API_KEY not set, skipping web search")
        return None
    
    log(f"Brave Search: '{query}'")
    url = f"https://api.search.brave.com/res/v1/web/search?q={urllib.parse.quote(query)}"
    
    try:
        req = urllib.request.Request(url)
        req.add_header('Accept', 'application/json')
        req.add_header('X-Subscription-Token', api_key)
        
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode())
            return data.get('web', {}).get('results', [])
    except Exception as e:
        log(f"Brave search failed: {e}")
        return None


def fetch_website_content(url):
    """Fetch and extract content from URL using simple scraping"""
    log(f"Fetching content from {url}")
    
    try:
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        })
        
        with urllib.request.urlopen(req, timeout=15) as response:
            html = response.read().decode('utf-8', errors='ignore')
            
            # Simple text extraction (remove HTML tags)
            text = re.sub(r'<script[^>]*>.*?</script>', '', html, flags=re.DOTALL | re.IGNORECASE)
            text = re.sub(r'<style[^>]*>.*?</style>', '', text, flags=re.DOTALL | re.IGNORECASE)
            text = re.sub(r'<[^>]+>', ' ', text)
            text = re.sub(r'\s+', ' ', text)
            
            # Extract meta description
            meta_match = re.search(r'<meta[^>]*name=["\']description["\'][^>]*content=["\']([^"\']+)["\']', html, re.IGNORECASE)
            meta_desc = meta_match.group(1) if meta_match else ""
            
            return {
                'text': text[:5000],  # Limit to 5000 chars
                'meta_description': meta_desc
            }
    except Exception as e:
        log(f"Failed to fetch {url}: {e}")
        return None


def research_business(name, location):
    """Research business from multiple sources"""
    log(f"=== Researching: {name} in {location} ===")
    
    data = {
        'name': name,
        'location': location,
        'google_business': None,
        'website_url': None,
        'website_content': None,
        'web_results': []
    }
    
    # 1. Google Places
    place_data = search_goplaces(name, location)
    if place_data:
        data['google_business'] = place_data
        log(f"✓ Found on Google: {place_data.get('name', 'N/A')}")
        
        # Extract website if available
        if 'website' in place_data:
            data['website_url'] = place_data['website']
    
    # 2. Brave Search
    search_query = f"{name} {location}"
    web_results = brave_search(search_query)
    if web_results:
        data['web_results'] = web_results[:5]
        log(f"✓ Found {len(web_results)} web results")
        
        # Try to find official website from search results
        if not data['website_url']:
            for result in web_results[:3]:
                url = result.get('url', '')
                # Simple heuristic: skip social media, directories
                if any(skip in url for skip in ['facebook.com', 'instagram.com', 'yelp.', 'tripadvisor.']):
                    continue
                data['website_url'] = url
                break
    
    # 3. Fetch existing website if found
    if data['website_url']:
        log(f"Found website: {data['website_url']}")
        content = fetch_website_content(data['website_url'])
        if content:
            data['website_content'] = content
            log("✓ Extracted website content")
    
    return data


def load_industry_template(branche):
    """Load industry template from industries.json"""
    json_path = Path(__file__).parent / 'industries.json'
    
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            templates = json.load(f)
        
        # Map common terms to template keys
        branche_map = {
            'bäckerei': 'baeckerei',
            'bäcker': 'baeckerei',
            'café': 'gastronomie',
            'restaurant': 'gastronomie',
            'gasthof': 'gastronomie',
            'elektriker': 'handwerk',
            'installateur': 'handwerk',
            'maler': 'handwerk',
            'schreiner': 'handwerk',
            'arzt': 'gesundheit',
            'zahnarzt': 'gesundheit',
            'physiotherapie': 'gesundheit',
            'steuerberater': 'dienstleistung',
            'rechtsanwalt': 'dienstleistung',
            'friseur': 'dienstleistung'
        }
        
        branche_lower = branche.lower() if branche else 'default'
        key = branche_map.get(branche_lower, branche_lower)
        
        if key in templates:
            return templates[key]
        
        # Fallback to category detection
        if any(word in branche_lower for word in ['bäck', 'back', 'konditor']):
            return templates['baeckerei']
        elif any(word in branche_lower for word in ['restaurant', 'café', 'gast', 'hotel']):
            return templates['gastronomie']
        elif any(word in branche_lower for word in ['handwerk', 'elektriker', 'install', 'maler', 'schrein']):
            return templates['handwerk']
        elif any(word in branche_lower for word in ['arzt', 'zahnarzt', 'physio', 'therapie', 'praxis']):
            return templates['gesundheit']
        elif any(word in branche_lower for word in ['berater', 'anwalt', 'steuer', 'rechts', 'friseur']):
            return templates['dienstleistung']
        elif any(word in branche_lower for word in ['laden', 'geschäft', 'shop', 'handel']):
            return templates['einzelhandel']
        
        return templates['default']
        
    except Exception as e:
        log(f"Failed to load industries.json: {e}")
        # Return minimal default
        return {
            'name': 'Professional',
            'color_primary': '#1e293b',
            'color_accent': '#0ea5e9',
            'services': [],
            'faqs': []
        }


def generate_content_with_llm(research_data, industry_template):
    """Generate website content using OpenAI API"""
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        log("ERROR: OPENAI_API_KEY not set")
        return None
    
    log("Generating content with GPT-4o-mini...")
    
    # Prepare context for LLM
    context_parts = [
        f"Business: {research_data['name']}",
        f"Location: {research_data['location']}"
    ]
    
    if research_data['google_business']:
        gb = research_data['google_business']
        context_parts.append(f"Address: {gb.get('formatted_address', 'N/A')}")
        context_parts.append(f"Phone: {gb.get('formatted_phone_number', 'N/A')}")
        context_parts.append(f"Rating: {gb.get('rating', 'N/A')} ({gb.get('user_ratings_total', 0)} reviews)")
        context_parts.append(f"Opening Hours: {json.dumps(gb.get('opening_hours', {}))}")
        
        if 'reviews' in gb and gb['reviews']:
            reviews_text = "\n".join([
                f"- {r.get('rating', 0)}★: {r.get('text', '')[:200]}"
                for r in gb['reviews'][:5]
            ])
            context_parts.append(f"Top Reviews:\n{reviews_text}")
    
    if research_data['website_content']:
        context_parts.append(f"Existing website content: {research_data['website_content']['text'][:1000]}")
    
    context = "\n\n".join(context_parts)
    
    # Build prompt
    prompt = f"""You are a professional web copywriter creating content for a small business website in Germany.

BUSINESS CONTEXT:
{context}

INDUSTRY: {industry_template['name']}

Generate website content in GERMAN. Output ONLY valid JSON with this structure:

{{
  "hero_headline": "Compelling headline (6-10 words, emotional not generic)",
  "hero_subline": "Subline explaining value (1 sentence, 15-20 words)",
  "about_title": "Über uns / Über mich",
  "about_text": "2-3 paragraphs about the business (from real data if available, otherwise industry-appropriate). Personal, authentic, NOT corporate speak.",
  "services": ["Service 1", "Service 2", "Service 3", "Service 4"],
  "services_intro": "1 sentence introducing the services",
  "reviews": [
    {{"text": "Testimonial text", "author": "Author name or anonymous", "rating": 5}}
  ],
  "cta_primary": "Main call-to-action button text (3-5 words)",
  "cta_secondary": "Secondary CTA (3-5 words)",
  "meta_description": "SEO meta description (150-160 chars)"
}}

RULES:
- ALL TEXT IN GERMAN
- Use real data from context when available
- Be specific, not generic
- Reviews: use real Google reviews if available (top 3-5), otherwise write realistic ones
- Services: if real data available use it, otherwise use industry defaults
- Hero headline: emotional, benefit-focused, NOT "[Business Name] - [City]"
- NO marketing fluff, NO superlatives without proof
- Authentic voice, not corporate

OUTPUT ONLY THE JSON, NO OTHER TEXT:"""

    # Call OpenAI API
    try:
        url = "https://api.openai.com/v1/chat/completions"
        data = {
            "model": "gpt-4o-mini",
            "messages": [
                {"role": "system", "content": "You are a professional German copywriter. Output only valid JSON."},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.7,
            "max_tokens": 2000
        }
        
        req = urllib.request.Request(
            url,
            data=json.dumps(data).encode('utf-8'),
            headers={
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {api_key}'
            }
        )
        
        with urllib.request.urlopen(req, timeout=60) as response:
            result = json.loads(response.read().decode())
            
        content_text = result['choices'][0]['message']['content'].strip()
        
        # Extract JSON (remove markdown code blocks if present)
        content_text = re.sub(r'^```json\s*', '', content_text)
        content_text = re.sub(r'\s*```$', '', content_text)
        
        content = json.loads(content_text)
        log("✓ Content generated successfully")
        return content
        
    except Exception as e:
        log(f"OpenAI API failed: {e}")
        return None


def generate_html(research_data, content, industry_template):
    """Generate complete self-contained HTML website"""
    
    # Extract business data
    name = research_data['name']
    location = research_data['location']
    
    gb = research_data.get('google_business') or {}
    address = gb.get('formatted_address', f"{location}, Deutschland")
    phone = gb.get('formatted_phone_number', '')
    website = research_data.get('website_url', '')
    rating = gb.get('rating', 0)
    rating_count = gb.get('user_ratings_total', 0)
    
    # Opening hours
    hours_data = gb.get('opening_hours', {})
    hours_list = hours_data.get('weekday_text', [])
    hours_html = ""
    if hours_list:
        hours_items = "".join([f"<div>{h}</div>" for h in hours_list])
        hours_html = f"""
        <div class="opening-hours">
            <h3>Öffnungszeiten</h3>
            {hours_items}
        </div>
        """
    
    # Reviews
    reviews_html = ""
    if content.get('reviews'):
        reviews_items = ""
        for review in content['reviews'][:5]:
            stars = "★" * review.get('rating', 5) + "☆" * (5 - review.get('rating', 5))
            reviews_items += f"""
            <div class="review-card">
                <div class="review-stars">{stars}</div>
                <p class="review-text">"{review.get('text', '')}"</p>
                <p class="review-author">— {review.get('author', 'Kunde')}</p>
            </div>
            """
        reviews_html = f"""
        <section id="bewertungen" class="section">
            <div class="container">
                <h2>Was unsere Kunden sagen</h2>
                <div class="reviews-grid">
                    {reviews_items}
                </div>
            </div>
        </section>
        """
    
    # Services
    services_html = ""
    if content.get('services'):
        services_items = "".join([
            f'<div class="service-card"><h3>{service}</h3></div>'
            for service in content['services']
        ])
        services_intro = content.get('services_intro', '')
        services_html = f"""
        <section id="leistungen" class="section section-dark">
            <div class="container">
                <h2>Unsere Leistungen</h2>
                {f'<p class="section-intro">{services_intro}</p>' if services_intro else ''}
                <div class="services-grid">
                    {services_items}
                </div>
            </div>
        </section>
        """
    
    # FAQ
    faq_html = ""
    if industry_template.get('faqs'):
        faq_items = "".join([
            f"""
            <div class="faq-item">
                <h3>{faq['question']}</h3>
                <p>{faq['answer']}</p>
            </div>
            """
            for faq in industry_template['faqs']
        ])
        faq_html = f"""
        <section id="faq" class="section">
            <div class="container">
                <h2>Häufig gestellte Fragen</h2>
                <div class="faq-grid">
                    {faq_items}
                </div>
            </div>
        </section>
        """
    
    # Google Maps
    maps_html = ""
    if address:
        maps_query = urllib.parse.quote(address)
        maps_html = f"""
        <div class="map-container">
            <iframe 
                src="https://www.google.com/maps?q={maps_query}&output=embed" 
                width="100%" 
                height="400" 
                style="border:0;" 
                allowfullscreen="" 
                loading="lazy">
            </iframe>
        </div>
        """
    
    # Colors
    color_primary = industry_template.get('color_primary', '#1e293b')
    color_accent = industry_template.get('color_accent', '#0ea5e9')
    
    # Schema.org structured data
    schema_data = {
        "@context": "https://schema.org",
        "@type": "LocalBusiness",
        "name": name,
        "address": {
            "@type": "PostalAddress",
            "streetAddress": address.split(',')[0] if ',' in address else address,
            "addressLocality": location,
            "addressCountry": "DE"
        }
    }
    if phone:
        schema_data["telephone"] = phone
    if website:
        schema_data["url"] = website
    if rating > 0:
        schema_data["aggregateRating"] = {
            "@type": "AggregateRating",
            "ratingValue": str(rating),
            "reviewCount": str(rating_count)
        }
    
    schema_json = json.dumps(schema_data, ensure_ascii=False)
    
    # Phone link
    phone_link = ""
    if phone:
        phone_clean = re.sub(r'[^\d+]', '', phone)
        phone_link = f'<a href="tel:{phone_clean}" class="btn btn-secondary">Jetzt anrufen</a>'
    
    # Meta description
    meta_desc = content.get('meta_description', f"{name} in {location} - {content.get('hero_subline', '')}")
    
    # Generate HTML
    html = f"""<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name} - {location}</title>
    <meta name="description" content="{meta_desc}">
    <meta property="og:title" content="{name} - {location}">
    <meta property="og:description" content="{meta_desc}">
    <meta property="og:type" content="website">
    <script type="application/ld+json">
    {schema_json}
    </script>
    <style>
        /* Reset & Base */
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        html {{
            scroll-behavior: smooth;
        }}
        
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            font-size: 18px;
            line-height: 1.7;
            color: #1a1a1a;
            background: #ffffff;
        }}
        
        /* Container */
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 24px;
        }}
        
        /* Navigation */
        nav {{
            position: sticky;
            top: 0;
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border-bottom: 1px solid #e5e5e5;
            z-index: 100;
            padding: 20px 0;
        }}
        
        nav .container {{
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        
        .logo {{
            font-size: 24px;
            font-weight: 700;
            color: {color_primary};
            text-decoration: none;
        }}
        
        .nav-links {{
            display: flex;
            gap: 32px;
            list-style: none;
        }}
        
        .nav-links a {{
            color: #4a4a4a;
            text-decoration: none;
            font-weight: 500;
            font-size: 16px;
            transition: color 0.2s;
        }}
        
        .nav-links a:hover {{
            color: {color_accent};
        }}
        
        .mobile-menu {{
            display: none;
        }}
        
        /* Hero Section */
        .hero {{
            padding: 120px 0;
            background: linear-gradient(135deg, {color_primary} 0%, {color_accent} 100%);
            color: white;
            text-align: center;
        }}
        
        .hero h1 {{
            font-size: 56px;
            font-weight: 800;
            line-height: 1.2;
            margin-bottom: 24px;
            letter-spacing: -0.02em;
        }}
        
        .hero p {{
            font-size: 22px;
            line-height: 1.6;
            margin-bottom: 40px;
            opacity: 0.95;
            max-width: 700px;
            margin-left: auto;
            margin-right: auto;
        }}
        
        /* Buttons */
        .btn {{
            display: inline-block;
            padding: 16px 32px;
            font-size: 18px;
            font-weight: 600;
            text-decoration: none;
            border-radius: 8px;
            transition: all 0.2s;
            cursor: pointer;
            border: none;
        }}
        
        .btn-primary {{
            background: white;
            color: {color_primary};
        }}
        
        .btn-primary:hover {{
            transform: translateY(-2px);
            box-shadow: 0 8px 24px rgba(0,0,0,0.15);
        }}
        
        .btn-secondary {{
            background: transparent;
            color: white;
            border: 2px solid white;
        }}
        
        .btn-secondary:hover {{
            background: white;
            color: {color_primary};
        }}
        
        .cta-buttons {{
            display: flex;
            gap: 16px;
            justify-content: center;
            flex-wrap: wrap;
        }}
        
        /* Sections */
        .section {{
            padding: 100px 0;
        }}
        
        .section-dark {{
            background: #f8f9fa;
        }}
        
        .section h2 {{
            font-size: 42px;
            font-weight: 700;
            margin-bottom: 48px;
            text-align: center;
            color: {color_primary};
            letter-spacing: -0.01em;
        }}
        
        .section-intro {{
            text-align: center;
            font-size: 20px;
            color: #666;
            max-width: 700px;
            margin: -24px auto 48px;
        }}
        
        /* About */
        .about-content {{
            max-width: 800px;
            margin: 0 auto;
            font-size: 19px;
            line-height: 1.8;
        }}
        
        .about-content p {{
            margin-bottom: 24px;
        }}
        
        /* Services Grid */
        .services-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 32px;
        }}
        
        .service-card {{
            background: white;
            padding: 40px;
            border-radius: 12px;
            box-shadow: 0 4px 24px rgba(0,0,0,0.08);
            transition: transform 0.2s, box-shadow 0.2s;
        }}
        
        .service-card:hover {{
            transform: translateY(-4px);
            box-shadow: 0 8px 32px rgba(0,0,0,0.12);
        }}
        
        .service-card h3 {{
            font-size: 22px;
            color: {color_primary};
            margin-bottom: 12px;
        }}
        
        /* Reviews */
        .reviews-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 32px;
        }}
        
        .review-card {{
            background: white;
            padding: 32px;
            border-radius: 12px;
            box-shadow: 0 4px 24px rgba(0,0,0,0.08);
        }}
        
        .review-stars {{
            font-size: 24px;
            color: #fbbf24;
            margin-bottom: 16px;
        }}
        
        .review-text {{
            font-size: 17px;
            line-height: 1.6;
            color: #4a4a4a;
            margin-bottom: 16px;
            font-style: italic;
        }}
        
        .review-author {{
            font-size: 15px;
            color: #999;
            font-weight: 500;
        }}
        
        /* FAQ */
        .faq-grid {{
            max-width: 800px;
            margin: 0 auto;
        }}
        
        .faq-item {{
            margin-bottom: 32px;
            padding-bottom: 32px;
            border-bottom: 1px solid #e5e5e5;
        }}
        
        .faq-item:last-child {{
            border-bottom: none;
        }}
        
        .faq-item h3 {{
            font-size: 22px;
            color: {color_primary};
            margin-bottom: 12px;
        }}
        
        .faq-item p {{
            font-size: 18px;
            color: #666;
            line-height: 1.7;
        }}
        
        /* Contact Section */
        .contact-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 48px;
            margin-top: 48px;
        }}
        
        .contact-info h3 {{
            font-size: 20px;
            color: {color_primary};
            margin-bottom: 16px;
        }}
        
        .contact-info p {{
            margin-bottom: 12px;
            color: #4a4a4a;
        }}
        
        .contact-info a {{
            color: {color_accent};
            text-decoration: none;
        }}
        
        .contact-info a:hover {{
            text-decoration: underline;
        }}
        
        .opening-hours {{
            background: #f8f9fa;
            padding: 24px;
            border-radius: 8px;
        }}
        
        .opening-hours h3 {{
            font-size: 18px;
            margin-bottom: 16px;
            color: {color_primary};
        }}
        
        .opening-hours div {{
            padding: 8px 0;
            border-bottom: 1px solid #e5e5e5;
            font-size: 16px;
        }}
        
        .opening-hours div:last-child {{
            border-bottom: none;
        }}
        
        .map-container {{
            margin-top: 48px;
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 4px 24px rgba(0,0,0,0.08);
        }}
        
        /* Footer */
        footer {{
            background: #1a1a1a;
            color: white;
            padding: 60px 0 32px;
        }}
        
        .footer-content {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 48px;
            margin-bottom: 48px;
        }}
        
        .footer-section h3 {{
            font-size: 18px;
            margin-bottom: 16px;
        }}
        
        .footer-section p, .footer-section a {{
            color: #999;
            text-decoration: none;
            font-size: 15px;
            line-height: 1.8;
        }}
        
        .footer-section a:hover {{
            color: {color_accent};
        }}
        
        .footer-bottom {{
            text-align: center;
            padding-top: 32px;
            border-top: 1px solid #333;
            color: #666;
            font-size: 14px;
        }}
        
        .footer-bottom a {{
            color: #999;
            text-decoration: none;
        }}
        
        .footer-bottom a:hover {{
            color: {color_accent};
        }}
        
        /* Responsive */
        @media (max-width: 768px) {{
            .nav-links {{
                display: none;
            }}
            
            .hero {{
                padding: 80px 0;
            }}
            
            .hero h1 {{
                font-size: 36px;
            }}
            
            .hero p {{
                font-size: 18px;
            }}
            
            .section {{
                padding: 60px 0;
            }}
            
            .section h2 {{
                font-size: 32px;
            }}
            
            .cta-buttons {{
                flex-direction: column;
            }}
            
            .btn {{
                width: 100%;
                text-align: center;
            }}
        }}
        
        /* Animations */
        @keyframes fadeIn {{
            from {{
                opacity: 0;
                transform: translateY(20px);
            }}
            to {{
                opacity: 1;
                transform: translateY(0);
            }}
        }}
        
        .fade-in {{
            animation: fadeIn 0.6s ease-out;
        }}
    </style>
</head>
<body>
    <!-- Navigation -->
    <nav>
        <div class="container">
            <a href="#" class="logo">{name}</a>
            <ul class="nav-links">
                <li><a href="#ueber-uns">Über uns</a></li>
                <li><a href="#leistungen">Leistungen</a></li>
                {f'<li><a href="#bewertungen">Bewertungen</a></li>' if reviews_html else ''}
                <li><a href="#kontakt">Kontakt</a></li>
            </ul>
            <div class="mobile-menu">☰</div>
        </div>
    </nav>

    <!-- Hero Section -->
    <section class="hero">
        <div class="container">
            <h1 class="fade-in">{content.get('hero_headline', name)}</h1>
            <p class="fade-in">{content.get('hero_subline', f'Ihr Partner in {location}')}</p>
            <div class="cta-buttons fade-in">
                <a href="#kontakt" class="btn btn-primary">{content.get('cta_primary', 'Jetzt Kontakt aufnehmen')}</a>
                {phone_link}
            </div>
        </div>
    </section>

    <!-- About Section -->
    <section id="ueber-uns" class="section">
        <div class="container">
            <h2>{content.get('about_title', 'Über uns')}</h2>
            <div class="about-content">
                {content.get('about_text', '').replace(chr(10), '</p><p>')}
            </div>
        </div>
    </section>

    <!-- Services Section -->
    {services_html}

    <!-- Reviews Section -->
    {reviews_html}

    <!-- FAQ Section -->
    {faq_html}

    <!-- Contact Section -->
    <section id="kontakt" class="section section-dark">
        <div class="container">
            <h2>Kontakt</h2>
            <div class="contact-grid">
                <div class="contact-info">
                    <h3>Kontaktieren Sie uns</h3>
                    <p><strong>{name}</strong></p>
                    <p>{address}</p>
                    {f'<p>Tel: <a href="tel:{re.sub(r"[^\\d+]", "", phone)}">{phone}</a></p>' if phone else ''}
                    {f'<p><a href="{website}" target="_blank">Website besuchen</a></p>' if website else ''}
                    {hours_html}
                </div>
            </div>
            {maps_html}
        </div>
    </section>

    <!-- Footer -->
    <footer>
        <div class="container">
            <div class="footer-content">
                <div class="footer-section">
                    <h3>{name}</h3>
                    <p>{address}</p>
                    {f'<p>{phone}</p>' if phone else ''}
                </div>
                <div class="footer-section">
                    <h3>Schnelllinks</h3>
                    <p><a href="#ueber-uns">Über uns</a></p>
                    <p><a href="#leistungen">Leistungen</a></p>
                    <p><a href="#kontakt">Kontakt</a></p>
                </div>
            </div>
            <div class="footer-bottom">
                <p>© {datetime.now().year} {name}. Alle Rechte vorbehalten.</p>
                <p style="margin-top: 8px;">Website erstellt von <a href="https://ainaryventures.com" target="_blank">Ainary Ventures</a></p>
            </div>
        </div>
    </footer>

    <!-- Minimal JavaScript -->
    <script>
        // Smooth scroll
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {{
            anchor.addEventListener('click', function (e) {{
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {{
                    target.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
                }}
            }});
        }});
        
        // Fade in on scroll
        const observerOptions = {{
            threshold: 0.1,
            rootMargin: '0px 0px -100px 0px'
        }};
        
        const observer = new IntersectionObserver((entries) => {{
            entries.forEach(entry => {{
                if (entry.isIntersecting) {{
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                }}
            }});
        }}, observerOptions);
        
        document.querySelectorAll('.service-card, .review-card, .faq-item').forEach(el => {{
            el.style.opacity = '0';
            el.style.transform = 'translateY(20px)';
            el.style.transition = 'opacity 0.6s ease-out, transform 0.6s ease-out';
            observer.observe(el);
        }});
    </script>
</body>
</html>"""
    
    return html


def main():
    parser = argparse.ArgumentParser(description='Generate professional websites for small businesses')
    parser.add_argument('name', help='Business name')
    parser.add_argument('location', help='City/Location')
    parser.add_argument('--branche', help='Industry/Branch (e.g., Bäckerei, Restaurant, Elektriker)', default='')
    parser.add_argument('--output', help='Output directory', default='output')
    
    args = parser.parse_args()
    
    # Validate required env vars
    if not os.getenv('OPENAI_API_KEY'):
        log("ERROR: OPENAI_API_KEY environment variable not set")
        sys.exit(1)
    
    # Create output directory
    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Sanitize folder name
    folder_name = re.sub(r'[^\w\s-]', '', args.name.lower())
    folder_name = re.sub(r'[\s]+', '-', folder_name)
    website_dir = output_dir / f"{folder_name}-{args.location.lower()}"
    website_dir.mkdir(parents=True, exist_ok=True)
    
    log(f"Starting website generation for: {args.name} ({args.location})")
    log(f"Output: {website_dir}")
    
    # Step 1: Research
    research_data = research_business(args.name, args.location)
    
    # Step 2: Load industry template
    industry_template = load_industry_template(args.branche)
    log(f"Using industry template: {industry_template['name']}")
    
    # Step 3: Generate content with LLM
    content = generate_content_with_llm(research_data, industry_template)
    
    if not content:
        log("Failed to generate content. Using fallback...")
        content = {
            'hero_headline': args.name,
            'hero_subline': f'Ihr Partner in {args.location}',
            'about_title': 'Über uns',
            'about_text': 'Willkommen bei uns.',
            'services': industry_template['services'][:4],
            'reviews': [],
            'cta_primary': 'Jetzt Kontakt aufnehmen',
            'meta_description': f"{args.name} in {args.location}"
        }
    
    # Step 4: Generate HTML
    html = generate_html(research_data, content, industry_template)
    
    # Step 5: Write to file
    output_file = website_dir / 'index.html'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html)
    
    log(f"✓ Website generated: {output_file}")
    log(f"✓ Open in browser: file://{output_file.absolute()}")
    
    # Try to open in browser
    try:
        import webbrowser
        webbrowser.open(f"file://{output_file.absolute()}")
        log("✓ Opened in browser")
    except:
        log("Could not auto-open browser. Please open manually.")
    
    log("=== DONE ===")


if __name__ == '__main__':
    main()
