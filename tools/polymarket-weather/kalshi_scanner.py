#!/usr/bin/env python3
"""
Kalshi Weather Scanner v1
Compares Open-Meteo forecasts vs Kalshi temperature market prices.
Finds mispricings where forecast probability differs from market price.

Usage: python3 kalshi_scanner.py [--city NYC] [--threshold 10]
"""

import json
import sys
import time
from datetime import datetime, timedelta
from math import erf, sqrt
from urllib.request import urlopen, Request

# ─── Config ───
KALSHI_BASE = "https://api.elections.kalshi.com/trade-api/v2"
OPEN_METEO = "https://api.open-meteo.com/v1/forecast"
REQUEST_DELAY = 1.2  # Kalshi rate limit: ~1 req/sec

# City configs: series ticker prefix → coords + name
CITIES = {
    "NY": {"name": "New York", "lat": 40.7128, "lon": -74.0060, "series": "KXHIGHNY"},
    "MI": {"name": "Miami", "lat": 25.7617, "lon": -80.1918, "series": "KXHIGHMI"},
    "CH": {"name": "Chicago", "lat": 41.8781, "lon": -87.6298, "series": "KXHIGHCH"},
    "LA": {"name": "Los Angeles", "lat": 34.0522, "lon": -118.2437, "series": "KXHIGHLA"},
    "SE": {"name": "Seattle", "lat": 47.6062, "lon": -122.3321, "series": "KXHIGHSE"},
    "DN": {"name": "Denver", "lat": 39.7392, "lon": -104.9903, "series": "KXHIGHDN"},
    "HO": {"name": "Houston", "lat": 29.7604, "lon": -95.3698, "series": "KXHIGHHO"},
    "PH": {"name": "Phoenix", "lat": 33.4484, "lon": -112.0740, "series": "KXHIGHPH"},
    "AT": {"name": "Atlanta", "lat": 33.7490, "lon": -84.3880, "series": "KXHIGHAT"},
    "BO": {"name": "Boston", "lat": 42.3601, "lon": -71.0589, "series": "KXHIGHBO"},
}

# Forecast error std dev by forecast horizon (days out)
STD_DEV = {0: 2.5, 1: 3.5, 2: 4.5, 3: 5.5}


def fetch_json(url, delay=0):
    """Fetch JSON with optional delay for rate limiting."""
    if delay:
        time.sleep(delay)
    req = Request(url, headers={"User-Agent": "AinaryWeatherBot/1.0", "Accept": "application/json"})
    with urlopen(req, timeout=15) as resp:
        return json.loads(resp.read())


def get_forecast(lat, lon, days=3):
    """Get temperature forecast from Open-Meteo."""
    url = (
        f"{OPEN_METEO}?latitude={lat}&longitude={lon}"
        f"&daily=temperature_2m_max,temperature_2m_min"
        f"&temperature_unit=fahrenheit"
        f"&timezone=America%2FNew_York"
        f"&forecast_days={days}"
    )
    return fetch_json(url)


def normal_cdf(x, mu, sigma):
    """Standard normal CDF."""
    return 0.5 * (1 + erf((x - mu) / (sigma * sqrt(2))))


def estimate_prob(forecast_temp, floor, cap, std_dev):
    """
    Estimate probability that actual temp falls in [floor, cap].
    floor=None means 'below cap', cap=None means 'above floor'.
    """
    if floor is not None and cap is not None:
        p = normal_cdf(cap + 0.5, forecast_temp, std_dev) - normal_cdf(floor - 0.5, forecast_temp, std_dev)
    elif floor is not None:
        # "X or above"
        p = 1 - normal_cdf(floor - 0.5, forecast_temp, std_dev)
    elif cap is not None:
        # "below X"
        p = normal_cdf(cap + 0.5, forecast_temp, std_dev)
    else:
        p = 0.5
    return max(0.01, min(0.99, p))


def get_kalshi_markets(series, delay=REQUEST_DELAY):
    """Fetch open markets for a series ticker."""
    url = f"{KALSHI_BASE}/markets?series_ticker={series}&limit=50&status=open"
    try:
        data = fetch_json(url, delay=delay)
        return data.get("markets", [])
    except Exception as e:
        return []


def parse_date_from_ticker(ticker):
    """Extract date from ticker like KXHIGHNY-26MAR01-T45 → 2026-03-01"""
    parts = ticker.split("-")
    if len(parts) >= 2:
        date_str = parts[1]  # e.g., 26MAR01
        try:
            return datetime.strptime(date_str, "%y%b%d").strftime("%Y-%m-%d")
        except:
            return None
    return None


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Kalshi Weather Scanner")
    parser.add_argument("--city", default="all", help="City code (NY, MI, CH, etc.) or 'all'")
    parser.add_argument("--threshold", type=float, default=8.0, help="Min edge %% to flag")
    args = parser.parse_args()

    print("=" * 65)
    print("  KALSHI WEATHER SCANNER v1")
    print(f"  {datetime.now().strftime('%Y-%m-%d %H:%M')} | Threshold: {args.threshold}%")
    print("=" * 65)

    cities = CITIES if args.city == "all" else {args.city.upper(): CITIES[args.city.upper()]}
    opportunities = []

    for code, cfg in cities.items():
        print(f"\n{'─' * 40}")
        print(f"  {cfg['name']} ({code})")
        print(f"{'─' * 40}")

        # 1. Get forecast
        try:
            fc = get_forecast(cfg["lat"], cfg["lon"])
            daily = fc.get("daily", {})
            dates = daily.get("time", [])
            highs = daily.get("temperature_2m_max", [])
            lows = daily.get("temperature_2m_min", [])
        except Exception as e:
            print(f"  Forecast error: {e}")
            continue

        for i, (d, h, l) in enumerate(zip(dates[:3], highs[:3], lows[:3])):
            print(f"  {d}: High {h:.0f}°F ({(h-32)*5/9:.0f}°C) Low {l:.0f}°F ({(l-32)*5/9:.0f}°C)")

        # 2. Get Kalshi markets
        markets = get_kalshi_markets(cfg["series"])
        if not markets:
            print(f"  No open markets (rate limited?)")
            continue

        print(f"  {len(markets)} open markets")

        # Group by date
        by_date = {}
        for m in markets:
            ticker = m.get("ticker", "")
            date = parse_date_from_ticker(ticker)
            if date:
                by_date.setdefault(date, []).append(m)

        # 3. Analyze each date
        for date, date_markets in sorted(by_date.items()):
            # Find matching forecast
            try:
                idx = dates.index(date)
                forecast_high = highs[idx]
                days_out = idx
            except ValueError:
                continue

            std = STD_DEV.get(days_out, 5.5)

            print(f"\n  {date} (forecast high: {forecast_high:.0f}°F, ±{std}°F)")

            for m in sorted(date_markets, key=lambda x: x.get("floor_strike") or 0):
                ticker = m.get("ticker", "")
                floor = m.get("floor_strike")
                cap = m.get("cap_strike")
                yes_bid = m.get("yes_bid", 0) / 100  # cents → probability
                yes_ask = m.get("yes_ask", 0) / 100
                no_bid = m.get("no_bid", 0) / 100
                no_ask = m.get("no_ask", 0) / 100
                vol = m.get("volume", 0)

                if yes_ask <= 0 and yes_bid <= 0:
                    continue

                mid_price = (yes_bid + yes_ask) / 2 if yes_ask > 0 else yes_bid

                # Range label
                if floor and cap:
                    label = f"{floor}-{cap}°F"
                elif floor:
                    label = f"≥{floor}°F"
                elif cap:
                    label = f"≤{cap}°F"
                else:
                    label = "?"

                our_prob = estimate_prob(forecast_high, floor, cap, std)
                edge = our_prob - mid_price

                # Determine actionable edge
                if edge > 0 and yes_ask > 0:
                    # We think YES is underpriced
                    actual_edge = our_prob - yes_ask
                    direction = "BUY YES"
                    entry_price = yes_ask
                elif edge < 0 and no_ask > 0:
                    actual_edge = (1 - our_prob) - no_ask
                    direction = "BUY NO"
                    entry_price = no_ask
                else:
                    actual_edge = edge
                    direction = "BUY YES" if edge > 0 else "BUY NO"
                    entry_price = mid_price

                flag = ""
                if abs(actual_edge) * 100 >= args.threshold:
                    flag = " ◀◀◀ EDGE"
                    opportunities.append({
                        "ticker": ticker,
                        "city": cfg["name"],
                        "date": date,
                        "range": label,
                        "forecast": forecast_high,
                        "mid_price": mid_price,
                        "our_prob": our_prob,
                        "edge": actual_edge,
                        "direction": direction,
                        "entry": entry_price,
                        "volume": vol,
                    })

                print(f"    {label:>10}  mkt={mid_price:5.1%}  ours={our_prob:5.1%}  edge={edge*100:+5.1f}%  vol={vol:>5}{flag}")

    # Summary
    print("\n" + "=" * 65)
    print("  OPPORTUNITIES")
    print("=" * 65)

    if opportunities:
        opportunities.sort(key=lambda x: abs(x["edge"]), reverse=True)
        for i, opp in enumerate(opportunities[:15], 1):
            ev = opp["edge"] * 100  # Expected value per $1
            print(f"\n  {i}. {opp['direction']} {opp['ticker']}")
            print(f"     {opp['city']} {opp['date']} | {opp['range']}")
            print(f"     Forecast: {opp['forecast']:.0f}°F | Entry: {opp['entry']:.0%} | Our: {opp['our_prob']:.0%}")
            print(f"     Edge: {ev:+.1f}% | EV per $1: ${abs(opp['edge']):.2f}")
            print(f"     Volume: {opp['volume']}")
    else:
        print(f"\n  No opportunities above {args.threshold}% edge.")
        print("  Markets may be efficient, or try --threshold 5")

    print(f"\n  Scanned {len(cities)} cities, {sum(len(m) for m in [get_kalshi_markets] if False)} markets")
    print(f"  Timestamp: {datetime.now().isoformat()}")


if __name__ == "__main__":
    main()
