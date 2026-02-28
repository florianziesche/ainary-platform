#!/usr/bin/env python3
"""
Polymarket Weather Scanner
Compares NOAA/Open-Meteo forecasts against Polymarket weather market prices.
Finds mispricings where forecast probability differs significantly from market price.
"""

import json
import sys
from datetime import datetime, timedelta
from urllib.request import urlopen, Request
from urllib.parse import quote

# ─── Config ───
CLOB_BASE = "https://clob.polymarket.com"
GAMMA_BASE = "https://gamma-api.polymarket.com"
OPEN_METEO_BASE = "https://api.open-meteo.com/v1/forecast"

# Cities with NOAA stations / Open-Meteo coords
CITIES = {
    "New York": {"lat": 40.7128, "lon": -74.0060},
    "Chicago": {"lat": 41.8781, "lon": -87.6298},
    "Miami": {"lat": 25.7617, "lon": -80.1918},
    "Los Angeles": {"lat": 34.0522, "lon": -118.2437},
    "Seattle": {"lat": 47.6062, "lon": -122.3321},
    "Denver": {"lat": 39.7392, "lon": -104.9903},
    "Houston": {"lat": 29.7604, "lon": -95.3698},
    "Phoenix": {"lat": 33.4484, "lon": -112.0740},
    "Atlanta": {"lat": 33.7490, "lon": -84.3880},
    "Boston": {"lat": 42.3601, "lon": -71.0589},
}


def fetch_json(url):
    """Fetch JSON from URL."""
    req = Request(url, headers={"User-Agent": "AinaryWeatherScanner/1.0"})
    with urlopen(req, timeout=15) as resp:
        return json.loads(resp.read())


def get_weather_markets():
    """Fetch active weather markets from Polymarket Gamma API."""
    url = f"{GAMMA_BASE}/markets?tag=weather&active=true&limit=100"
    try:
        data = fetch_json(url)
        return data
    except Exception as e:
        print(f"  Error fetching Gamma API: {e}")
        # Fallback: try CLOB simplified markets
        try:
            url2 = f"{CLOB_BASE}/simplified-markets?tag=weather&limit=100"
            return fetch_json(url2).get("data", [])
        except Exception as e2:
            print(f"  Error fetching CLOB API: {e2}")
            return []


def get_forecast(city, lat, lon, days=3):
    """Get forecast from Open-Meteo for a city."""
    url = (
        f"{OPEN_METEO_BASE}?latitude={lat}&longitude={lon}"
        f"&daily=temperature_2m_max,temperature_2m_min,precipitation_sum,precipitation_probability_max"
        f"&temperature_unit=fahrenheit"
        f"&timezone=America%2FNew_York"
        f"&forecast_days={days}"
    )
    try:
        data = fetch_json(url)
        return data.get("daily", {})
    except Exception as e:
        print(f"  Error fetching forecast for {city}: {e}")
        return {}


def parse_temp_range(question):
    """Try to extract temperature range and city from market question."""
    q = question.lower()
    
    city_match = None
    for city in CITIES:
        if city.lower() in q:
            city_match = city
            break
    
    # Common patterns: "above X°F", "X-Y°F", "below X°F", "higher than X"
    import re
    
    temp_high = None
    temp_low = None
    
    # "above X" or "higher than X" or ">= X" or "X or above" or "X°F or higher"
    m = re.search(r'(?:above|higher than|>=?|at least)\s*(\d+)', q)
    if m:
        temp_low = int(m.group(1))
    
    m = re.search(r'(\d+)\s*(?:°?f?\s*)?(?:or (?:above|higher|more))', q)
    if m:
        temp_low = int(m.group(1))
    
    # "below X" or "lower than X" or "<= X"
    m = re.search(r'(?:below|lower than|under|<=?)\s*(\d+)', q)
    if m:
        temp_high = int(m.group(1))
    
    # "X-Y" range
    m = re.search(r'(\d+)\s*[-–]\s*(\d+)\s*°?f?', q)
    if m:
        temp_low = int(m.group(1))
        temp_high = int(m.group(2))
    
    # Detect if it's about high temp, low temp, or precipitation
    is_high = any(w in q for w in ['high', 'highest', 'max'])
    is_low = any(w in q for w in ['low', 'lowest', 'min', 'overnight'])
    is_precip = any(w in q for w in ['rain', 'precip', 'snow', 'inch'])
    
    return {
        "city": city_match,
        "temp_low": temp_low,
        "temp_high": temp_high,
        "is_high": is_high,
        "is_low": is_low,
        "is_precip": is_precip,
    }


def estimate_probability(forecast_temp, temp_low, temp_high, std_dev=3.5):
    """
    Estimate probability that actual temp falls in range [temp_low, temp_high].
    Uses normal distribution around forecast_temp with typical forecast error std_dev.
    """
    from math import erf, sqrt
    
    def normal_cdf(x, mu, sigma):
        return 0.5 * (1 + erf((x - mu) / (sigma * sqrt(2))))
    
    if temp_low is not None and temp_high is not None:
        p = normal_cdf(temp_high + 0.5, forecast_temp, std_dev) - normal_cdf(temp_low - 0.5, forecast_temp, std_dev)
    elif temp_low is not None:
        p = 1 - normal_cdf(temp_low - 0.5, forecast_temp, std_dev)
    elif temp_high is not None:
        p = normal_cdf(temp_high + 0.5, forecast_temp, std_dev)
    else:
        p = 0.5
    
    return max(0.01, min(0.99, p))


def main():
    print("=" * 60)
    print("  POLYMARKET WEATHER SCANNER")
    print(f"  {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("=" * 60)
    
    # 1. Fetch forecasts for all cities
    print("\n[1] Fetching forecasts...")
    forecasts = {}
    for city, coords in CITIES.items():
        daily = get_forecast(city, coords["lat"], coords["lon"])
        if daily:
            forecasts[city] = daily
            temps_max = daily.get("temperature_2m_max", [])
            temps_min = daily.get("temperature_2m_min", [])
            dates = daily.get("time", [])
            if temps_max and dates:
                print(f"  {city}: {dates[0]} High {temps_max[0]:.0f}°F / Low {temps_min[0]:.0f}°F")
    
    # 2. Fetch Polymarket weather markets
    print("\n[2] Fetching Polymarket weather markets...")
    markets = get_weather_markets()
    
    if not markets:
        print("  No markets found. Trying alternative endpoint...")
        # Try events endpoint
        try:
            url = f"{GAMMA_BASE}/events?tag=weather&active=true&limit=50"
            events = fetch_json(url)
            print(f"  Found {len(events)} weather events")
            for ev in events[:10]:
                title = ev.get("title", ev.get("question", "?"))
                print(f"    - {title}")
                sub_markets = ev.get("markets", [])
                for m in sub_markets:
                    q = m.get("question", m.get("groupItemTitle", "?"))
                    price = m.get("outcomePrices", m.get("bestAsk", "?"))
                    print(f"      [{price}] {q}")
            markets = []
            for ev in events:
                markets.extend(ev.get("markets", []))
        except Exception as e:
            print(f"  Events endpoint also failed: {e}")
    
    print(f"\n  Total markets: {len(markets)}")
    
    if not markets:
        print("\n  Cannot access Polymarket API from this network.")
        print("  Showing forecast data only:\n")
        for city, daily in forecasts.items():
            dates = daily.get("time", [])
            highs = daily.get("temperature_2m_max", [])
            lows = daily.get("temperature_2m_min", [])
            precip = daily.get("precipitation_sum", [])
            precip_prob = daily.get("precipitation_probability_max", [])
            print(f"\n  {city}:")
            for i in range(min(3, len(dates))):
                print(f"    {dates[i]}: High {highs[i]:.0f}°F ({(highs[i]-32)*5/9:.0f}°C) "
                      f"Low {lows[i]:.0f}°F ({(lows[i]-32)*5/9:.0f}°C) "
                      f"Rain: {precip[i]:.1f}mm ({precip_prob[i]}%)")
        return
    
    # 3. Analyze: compare forecast vs market price
    print("\n[3] Scanning for mispricings...\n")
    
    opportunities = []
    
    for market in markets:
        question = market.get("question", market.get("groupItemTitle", ""))
        if not question:
            continue
        
        parsed = parse_temp_range(question)
        city = parsed["city"]
        
        if not city or city not in forecasts:
            continue
        
        # Get market price (YES probability)
        try:
            prices = market.get("outcomePrices", "")
            if isinstance(prices, str) and prices:
                prices = json.loads(prices)
            if isinstance(prices, list) and len(prices) >= 1:
                market_yes = float(prices[0])
            else:
                market_yes = float(market.get("bestAsk", 0))
        except:
            continue
        
        if market_yes <= 0 or market_yes >= 1:
            continue
        
        # Get forecast temp
        daily = forecasts[city]
        if parsed["is_high"] or (not parsed["is_low"] and not parsed["is_precip"]):
            forecast_temp = daily.get("temperature_2m_max", [None])[0]
        elif parsed["is_low"]:
            forecast_temp = daily.get("temperature_2m_min", [None])[0]
        else:
            continue  # Skip precip for now
        
        if forecast_temp is None:
            continue
        
        # Estimate probability
        forecast_prob = estimate_probability(
            forecast_temp, parsed["temp_low"], parsed["temp_high"]
        )
        
        # Calculate edge
        edge = forecast_prob - market_yes
        
        if abs(edge) > 0.08:  # >8% mispricing
            direction = "BUY YES" if edge > 0 else "BUY NO"
            opportunities.append({
                "question": question,
                "city": city,
                "market_price": market_yes,
                "forecast_prob": forecast_prob,
                "forecast_temp": forecast_temp,
                "edge": edge,
                "direction": direction,
            })
    
    # Sort by absolute edge
    opportunities.sort(key=lambda x: abs(x["edge"]), reverse=True)
    
    if opportunities:
        print(f"  Found {len(opportunities)} potential mispricings:\n")
        for i, opp in enumerate(opportunities[:15], 1):
            edge_pct = abs(opp["edge"]) * 100
            print(f"  {i}. {opp['question']}")
            print(f"     City: {opp['city']} | Forecast: {opp['forecast_temp']:.0f}°F")
            print(f"     Market: {opp['market_price']:.0%} | Our estimate: {opp['forecast_prob']:.0%}")
            print(f"     Edge: {edge_pct:.1f}% → {opp['direction']}")
            print()
    else:
        print("  No significant mispricings found (>8% edge).")
        print("  This could mean markets are efficient or we need better parsing.")


if __name__ == "__main__":
    main()
