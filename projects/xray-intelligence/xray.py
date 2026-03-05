#!/usr/bin/env python3
"""
X-Ray Intelligence — 4 Use Cases, 1 CLI
=========================================

  xray dd       "NOMOS Glashütte"           # VC Due Diligence
  xray pitch    "BMW AG"                     # Consulting Pitch Prep
  xray compete  "NOMOS" --vs "Mühle"         # Competitor Intel
  xray city     "Glashütte"                  # Standort-Analyse

Each generates a professional HTML report from 8+ open data sources.
"""

import sys, os, json, asyncio, argparse, re, time
from datetime import datetime, date
from pathlib import Path
from html import escape

# ─── Env ──────────────────────────────────────────────────────

VENV = Path.home() / "ainary-tools"
sys.path.insert(0, str(VENV / "lib/python3.12/site-packages"))

OUTPUT_DIR = Path.home() / ".openclaw/workspace/projects/xray-intelligence/reports"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# ─── Data Collection Layer ────────────────────────────────────

class IntelCollector:
    """Collects intelligence from multiple German open data sources."""

    def __init__(self, verbose=True):
        self.verbose = verbose
        self.data = {}
        self._timings = {}

    def log(self, msg):
        if self.verbose:
            print(f"  🔍 {msg}", file=sys.stderr)

    def _timed(name):
        def decorator(fn):
            def wrapper(self, *a, **kw):
                t0 = time.time()
                result = fn(self, *a, **kw)
                self._timings[name] = round(time.time() - t0, 1)
                return result
            return wrapper
        return decorator

    # 1. Bundesanzeiger — Financial Reports
    @_timed("bundesanzeiger")
    def collect_bundesanzeiger(self, company):
        self.log(f"Bundesanzeiger: {company}")
        try:
            from deutschland.bundesanzeiger import Bundesanzeiger
            from bs4 import BeautifulSoup
            ba = Bundesanzeiger()
            reports = ba.get_reports(company)
            results = []
            for key, report in reports.items():
                raw = report.get("raw_report", "")
                if "<" in raw and ">" in raw:
                    soup = BeautifulSoup(raw, "lxml")
                    tables = []
                    for table in soup.find_all("table"):
                        rows = []
                        for tr in table.find_all("tr"):
                            cells = [td.get_text(strip=True) for td in tr.find_all(["td", "th"])]
                            if any(cells):
                                rows.append(" | ".join(cells))
                        if rows:
                            tables.append("\n".join(rows))
                    clean_text = soup.get_text(separator="\n", strip=True)
                    content = ""
                    if tables:
                        content = "--- TABELLEN ---\n" + "\n\n".join(tables[:5]) + "\n\n--- VOLLTEXT ---\n"
                    content += clean_text[:5000]
                else:
                    content = raw[:5000]

                results.append({
                    "id": key,
                    "name": report.get("name", ""),
                    "date": str(report.get("date", "")),
                    "type": report.get("report_type", ""),
                    "content": content
                })
            self.data["bundesanzeiger"] = results
            self.log(f"  → {len(results)} Berichte")
            return results
        except Exception as e:
            self.log(f"  ⚠️ {e}")
            self.data["bundesanzeiger"] = []
            return []

    # 2. offeneregister.de — Company Registry
    @_timed("offeneregister")
    def collect_offeneregister(self, search_term, limit=100, timeout_sec=30):
        self.log(f"offeneregister.de: {search_term}")
        import bz2, signal as _signal

        path = VENV / "data/de_companies.jsonl.bz2"
        if not path.exists():
            self.log("  ⚠️ Dataset not downloaded")
            self.data["offeneregister"] = []
            return []

        results = []
        search_lower = search_term.lower()

        class _Timeout(Exception):
            pass

        def _handler(signum, frame):
            raise _Timeout()

        old_handler = _signal.signal(_signal.SIGALRM, _handler)
        _signal.alarm(timeout_sec)
        try:
            with bz2.open(str(path), 'rt', errors='replace') as f:
                for line in f:
                    if search_lower in line.lower():
                        try:
                            obj = json.loads(line)
                        except json.JSONDecodeError:
                            continue
                        addr = (obj.get("registered_address_in_full", "") or "").lower()
                        name = (obj.get("name", "") or "").lower()
                        if search_lower in name or search_lower in addr:
                            results.append({
                                "name": obj.get("name", "N/A"),
                                "status": obj.get("current_status", "unknown"),
                                "type": obj.get("company_type", "N/A"),
                                "address": obj.get("registered_address_in_full", "N/A"),
                                "officers": obj.get("officers", []),
                                "register": obj.get("company_number", "N/A"),
                                "registry": obj.get("jurisdiction_code", "N/A")
                            })
                            if len(results) >= limit:
                                break
        except (_Timeout, EOFError):
            self.log(f"  ⚠️ Scan stopped (timeout/{timeout_sec}s or truncated file) — {len(results)} results so far")
        except Exception as e:
            self.log(f"  ⚠️ Partial read: {e}")
        finally:
            _signal.alarm(0)
            _signal.signal(_signal.SIGALRM, old_handler)

        self.data["offeneregister"] = results
        self.log(f"  → {len(results)} Firmen")
        return results

    # 3. Web Crawl — Company Website
    @_timed("website")
    def collect_website_sync(self, url):
        """Sync wrapper around crawl."""
        self.log(f"Website: {url}")
        try:
            from crawl4ai import AsyncWebCrawler
            async def _crawl():
                async with AsyncWebCrawler(verbose=False) as crawler:
                    return await crawler.arun(url=url)
            result = asyncio.get_event_loop().run_until_complete(_crawl()) if asyncio.get_event_loop().is_running() else asyncio.run(_crawl())
            content = result.markdown[:8000] if result.markdown else ""
            self.data.setdefault("websites", {})[url] = {
                "url": url,
                "length": len(result.markdown) if result.markdown else 0,
                "content": content
            }
            self.log(f"  → {len(content)} chars")
            return content
        except Exception as e:
            self.log(f"  ⚠️ {e}")
            self.data.setdefault("websites", {})[url] = {"url": url, "length": 0, "content": ""}
            return ""

    async def collect_website(self, url):
        self.log(f"Website: {url}")
        try:
            from crawl4ai import AsyncWebCrawler
            async with AsyncWebCrawler(verbose=False) as crawler:
                result = await crawler.arun(url=url)
                content = result.markdown[:8000] if result.markdown else ""
                self.data.setdefault("websites", {})[url] = {
                    "url": url,
                    "length": len(result.markdown) if result.markdown else 0,
                    "content": content
                }
                self.log(f"  → {len(content)} chars")
                return content
        except Exception as e:
            self.log(f"  ⚠️ {e}")
            self.data.setdefault("websites", {})[url] = {"url": url, "length": 0, "content": ""}
            return ""

    # 4. Insolvency Check
    @_timed("insolvency")
    def collect_insolvency(self, company):
        self.log(f"Insolvenzbekanntmachungen: {company}")
        try:
            from InsolvencyAnnouncementsGer import insol_proc_scr
            results_df = insol_proc_scr(name=company, search_type="d")
            results = results_df if isinstance(results_df, list) else []
            # If it returns a DataFrame
            if hasattr(results_df, 'iterrows'):
                results = []
                for _, row in results_df.iterrows():
                    results.append(row.to_dict())
            insolvencies = []
            for r in results:
                if isinstance(r, dict):
                    insolvencies.append({
                        "court": r.get("court", r.get("gericht", r.get("ins_court", "N/A"))),
                        "date": str(r.get("date", r.get("datum", "N/A"))),
                        "type": r.get("type", r.get("art", r.get("subject", "N/A"))),
                        "content": str(r.get("content", r.get("text", r.get("announcement", ""))))[:500]
                    })
                else:
                    insolvencies.append({
                        "court": getattr(r, 'court', getattr(r, 'gericht', 'N/A')),
                        "date": str(getattr(r, 'date', getattr(r, 'datum', 'N/A'))),
                        "type": getattr(r, 'type', getattr(r, 'art', 'N/A')),
                        "content": str(getattr(r, 'content', getattr(r, 'text', '')))[:500]
                    })
            self.data["insolvency"] = insolvencies
            self.log(f"  → {len(insolvencies)} Verfahren")
            return insolvencies
        except Exception as e:
            self.log(f"  ⚠️ {e}")
            self.data["insolvency"] = []
            return []

    def full_company_scan(self, company, url=None):
        """Run all collectors for one company."""
        self.collect_bundesanzeiger(company)
        self.collect_offeneregister(company)
        self.collect_insolvency(company)
        if url:
            asyncio.run(self.collect_website(url))
        return self.data


# ─── Analysis Layer ───────────────────────────────────────────

class IntelAnalyzer:
    """Risk scoring and pattern detection."""

    WARNING_WORDS_DE = [
        "verlust", "überschuldung", "liquidität", "insolvenz", "going concern",
        "eigenkapital negativ", "fortführung", "sanierung", "zahlungsunfähig",
        "stundung", "gläubiger", "abwicklung", "nachschuss"
    ]

    POSITIVE_WORDS_DE = [
        "gewinn", "wachstum", "umsatzsteigerung", "eigenkapital", "dividende",
        "expansion", "innovation", "patent", "ausschüttung"
    ]

    def __init__(self, data):
        self.data = data

    def _scan_content(self, content, wordlist):
        content_lower = content.lower()
        return [w for w in wordlist if w in content_lower]

    def analyze_company(self, company_name):
        """Full risk analysis for a single company."""
        analysis = {
            "name": company_name,
            "timestamp": datetime.now().isoformat(),
            "data_sources": [],
            "risk_signals": [],
            "positive_signals": [],
            "financials": {},
            "governance": {},
            "score": {}
        }

        # Bundesanzeiger
        reports = self.data.get("bundesanzeiger", [])
        if reports:
            analysis["data_sources"].append("Bundesanzeiger")
            analysis["score"]["financial_transparency"] = min(10, len(reports) * 2)
            all_content = " ".join([r.get("content", "") for r in reports])

            warnings = self._scan_content(all_content, self.WARNING_WORDS_DE)
            if warnings:
                analysis["risk_signals"].append({
                    "source": "Bundesanzeiger", "level": "HIGH",
                    "detail": f"Warnwörter: {', '.join(warnings)}"
                })

            positives = self._scan_content(all_content, self.POSITIVE_WORDS_DE)
            if positives:
                analysis["positive_signals"].append({
                    "source": "Bundesanzeiger",
                    "detail": f"Positive Signale: {', '.join(positives)}"
                })

            # Extract financial numbers (basic)
            self._extract_financials(all_content, analysis)
        else:
            analysis["risk_signals"].append({
                "source": "Bundesanzeiger", "level": "MEDIUM",
                "detail": "Keine Jahresabschlüsse veröffentlicht"
            })

        # Handelsregister
        companies = self.data.get("offeneregister", [])
        if companies:
            analysis["data_sources"].append("offeneregister.de")
            match = None
            for c in companies:
                if company_name.lower() in c.get("name", "").lower():
                    match = c
                    break
            if match:
                officers = match.get("officers", [])
                analysis["governance"] = {
                    "status": match.get("status", "unknown"),
                    "type": match.get("type", "N/A"),
                    "register": match.get("register", "N/A"),
                    "officers": officers,
                    "officer_count": len(officers)
                }
                if officers:
                    analysis["score"]["governance"] = min(10, len(officers) * 3)
                status = match.get("status", "")
                if status and status not in ["currently registered", "unknown", ""]:
                    analysis["risk_signals"].append({
                        "source": "Handelsregister", "level": "HIGH",
                        "detail": f"Status: {status}"
                    })

        # Insolvency
        insolvencies = self.data.get("insolvency", [])
        if insolvencies:
            analysis["data_sources"].append("Insolvenzbekanntmachungen")
            analysis["risk_signals"].append({
                "source": "Insolvenzbekanntmachungen", "level": "CRITICAL",
                "detail": f"{len(insolvencies)} Insolvenzverfahren gefunden"
            })
        else:
            analysis["data_sources"].append("Insolvenzbekanntmachungen")
            analysis["positive_signals"].append({
                "source": "Insolvenzbekanntmachungen",
                "detail": "Keine Verfahren — sauber"
            })

        # Website
        websites = self.data.get("websites", {})
        for url, site in websites.items():
            analysis["data_sources"].append(f"Website ({url})")
            if site.get("length", 0) > 1000:
                analysis["score"]["digital_presence"] = 7
            elif site.get("length", 0) > 0:
                analysis["score"]["digital_presence"] = 4
            else:
                analysis["risk_signals"].append({
                    "source": "Website", "level": "LOW",
                    "detail": f"Keine/minimale Online-Präsenz: {url}"
                })

        # Overall risk
        high = len([r for r in analysis["risk_signals"] if r["level"] in ["HIGH", "CRITICAL"]])
        medium = len([r for r in analysis["risk_signals"] if r["level"] == "MEDIUM"])
        if high > 0:
            analysis["overall_risk"] = "HIGH"
            analysis["risk_color"] = "#f87171"
        elif medium > 1:
            analysis["overall_risk"] = "MEDIUM"
            analysis["risk_color"] = "#fb923c"
        else:
            analysis["overall_risk"] = "LOW"
            analysis["risk_color"] = "#34d399"

        analysis["data_source_count"] = len(analysis["data_sources"])
        return analysis

    def _extract_financials(self, text, analysis):
        """Try to pull key financial numbers from report text."""
        import re
        patterns = {
            "umsatz": r"(?:Umsatz|Umsatzerlöse)[:\s]*([0-9.,]+)\s*(?:EUR|€|T€|TEUR|Mio)",
            "gewinn": r"(?:Jahresüberschuss|Gewinn|Ergebnis)[:\s]*([0-9.,]+)\s*(?:EUR|€|T€|TEUR|Mio)",
            "eigenkapital": r"(?:Eigenkapital)[:\s]*([0-9.,]+)\s*(?:EUR|€|T€|TEUR|Mio)",
            "bilanzsumme": r"(?:Bilanzsumme)[:\s]*([0-9.,]+)\s*(?:EUR|€|T€|TEUR|Mio)",
            "mitarbeiter": r"(?:Mitarbeiter|Beschäftigte|Arbeitnehmer)[:\s]*([0-9.,]+)"
        }
        for key, pattern in patterns.items():
            m = re.search(pattern, text, re.IGNORECASE)
            if m:
                analysis["financials"][key] = m.group(1)

    def analyze_city(self, city_name, companies):
        total = len(companies)
        active = len([c for c in companies if c.get("status") in ["currently registered", "unknown", None, ""]])
        inactive = total - active
        types = {}
        for c in companies:
            t = c.get("type", "unknown")
            types[t] = types.get(t, 0) + 1
        return {
            "city": city_name,
            "total_companies": total,
            "active": active,
            "inactive": inactive,
            "active_rate": round(active / total * 100, 1) if total > 0 else 0,
            "company_types": dict(sorted(types.items(), key=lambda x: -x[1])[:10]),
            "timestamp": datetime.now().isoformat()
        }

    def compare_companies(self, analyses):
        """Compare multiple company analyses side-by-side."""
        comparison = {
            "companies": [],
            "winner": None,
            "timestamp": datetime.now().isoformat()
        }
        for a in analyses:
            entry = {
                "name": a["name"],
                "risk": a["overall_risk"],
                "data_sources": a["data_source_count"],
                "risk_signals": len(a["risk_signals"]),
                "positive_signals": len(a.get("positive_signals", [])),
                "financials": a.get("financials", {}),
                "governance": a.get("governance", {})
            }
            # Simple score: positive signals - (risk signals * 2)
            entry["net_score"] = entry["positive_signals"] - (entry["risk_signals"] * 2)
            comparison["companies"].append(entry)

        # Determine winner
        if comparison["companies"]:
            comparison["companies"].sort(key=lambda x: x["net_score"], reverse=True)
            comparison["winner"] = comparison["companies"][0]["name"]

        return comparison


# ─── HTML Report Templates ────────────────────────────────────

CSS = """
:root {
  --bg: #fafaf9; --surface: #ffffff; --border: #e5e5e0;
  --text: #1c1c1a; --text2: #737373; --accent: #c8aa50; --accent-bg: #faf6eb;
  --green: #16a34a; --red: #dc2626; --orange: #ea580c; --blue: #2563eb;
  --font: 'SF Mono', 'Fira Code', monospace;
  --sans: -apple-system, BlinkMacSystemFont, 'Inter', sans-serif;
}
@media (prefers-color-scheme: dark) {
  :root { --bg: #0a0a0f; --surface: #12121a; --border: #2a2a3a; --text: #e4e4ed; --text2: #8888a0; --accent-bg: rgba(200,170,80,0.08); }
}
* { margin: 0; padding: 0; box-sizing: border-box; }
body { background: var(--bg); color: var(--text); font-family: var(--sans); line-height: 1.6; }
.report { max-width: 960px; margin: 0 auto; padding: 40px 24px; }
.report-header { border-bottom: 3px solid var(--accent); padding-bottom: 24px; margin-bottom: 32px; }
.report-brand { font-size: 12px; text-transform: uppercase; letter-spacing: 3px; color: var(--accent); font-weight: 700; margin-bottom: 8px; }
.report-title { font-size: 32px; font-weight: 800; line-height: 1.2; }
.report-subtitle { font-size: 14px; color: var(--text2); margin-top: 8px; }
.report-meta { display: flex; gap: 24px; margin-top: 16px; font-size: 12px; color: var(--text2); font-family: var(--font); flex-wrap: wrap; }
.confidential { background: var(--accent-bg); border: 1px solid var(--accent); border-radius: 6px; padding: 8px 16px; font-size: 11px; text-align: center; margin-bottom: 24px; color: var(--accent); font-weight: 600; text-transform: uppercase; letter-spacing: 1px; }
.section { margin-bottom: 32px; }
.section-title { font-size: 18px; font-weight: 700; padding-bottom: 8px; border-bottom: 1px solid var(--border); margin-bottom: 16px; display: flex; align-items: center; gap: 8px; }
.card { background: var(--surface); border: 1px solid var(--border); border-radius: 8px; padding: 16px; margin-bottom: 12px; }
.card-title { font-weight: 600; font-size: 14px; margin-bottom: 4px; }
.card-meta { font-size: 12px; color: var(--text2); }
.card-content { font-size: 13px; margin-top: 8px; white-space: pre-wrap; max-height: 200px; overflow: hidden; }
table { width: 100%; border-collapse: collapse; font-size: 13px; }
th { text-align: left; padding: 8px 12px; background: var(--accent-bg); font-weight: 600; font-size: 11px; text-transform: uppercase; letter-spacing: 0.5px; }
td { padding: 8px 12px; border-bottom: 1px solid var(--border); }
tr:hover td { background: var(--accent-bg); }
.signal { display: flex; align-items: flex-start; gap: 10px; padding: 10px 14px; border-radius: 6px; margin-bottom: 8px; font-size: 13px; }
.signal-critical { background: #fef2f2; border-left: 3px solid #dc2626; }
.signal-high { background: #fff7ed; border-left: 3px solid #ea580c; }
.signal-medium { background: #fefce8; border-left: 3px solid #ca8a04; }
.signal-low { background: #f0f9ff; border-left: 3px solid #2563eb; }
.signal-positive { background: #f0fdf4; border-left: 3px solid #16a34a; }
.signal-level { font-weight: 700; font-size: 11px; text-transform: uppercase; min-width: 60px; }
.stats { display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 12px; margin-bottom: 24px; }
.stat { background: var(--surface); border: 1px solid var(--border); border-radius: 8px; padding: 16px; text-align: center; }
.stat-value { font-size: 28px; font-weight: 800; font-family: var(--font); }
.stat-label { font-size: 11px; color: var(--text2); text-transform: uppercase; letter-spacing: 0.5px; margin-top: 4px; }
.report-footer { margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--border); font-size: 11px; color: var(--text2); text-align: center; }
.comparison-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin-bottom: 24px; }
.comparison-card { background: var(--surface); border: 2px solid var(--border); border-radius: 12px; padding: 20px; }
.comparison-card.winner { border-color: var(--accent); }
.comparison-card h3 { font-size: 16px; margin-bottom: 12px; }
.verdict { background: var(--accent-bg); border: 2px solid var(--accent); border-radius: 8px; padding: 16px 24px; margin: 24px 0; font-size: 14px; }
.verdict-title { font-weight: 800; font-size: 16px; color: var(--accent); margin-bottom: 8px; }
.pitch-section { background: var(--surface); border: 1px solid var(--border); border-radius: 12px; padding: 24px; margin-bottom: 16px; }
.pitch-section h3 { font-size: 15px; font-weight: 700; margin-bottom: 12px; color: var(--accent); }
.pitch-bullet { padding: 4px 0; font-size: 13px; }
.pitch-bullet::before { content: "→ "; color: var(--accent); font-weight: 700; }
@media (prefers-color-scheme: dark) {
  .signal-critical { background: rgba(220,38,38,0.1); } .signal-high { background: rgba(234,88,12,0.1); }
  .signal-medium { background: rgba(202,138,4,0.1); } .signal-low { background: rgba(37,99,235,0.1); }
  .signal-positive { background: rgba(22,163,74,0.1); }
}
"""


class ReportGenerator:
    """Generates professional HTML reports for each use case."""

    def _wrap(self, title, subtitle, source_count, duration, sources_list, content, use_case_badge=""):
        return f"""<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>X-Ray — {escape(title)}</title>
<style>{CSS}</style>
</head>
<body>
<div class="report">
  <div class="confidential">⚠️ Vertraulich — Nur für internen Gebrauch {use_case_badge}</div>
  <div class="report-header">
    <div class="report-brand">♔ X-Ray Intelligence</div>
    <h1 class="report-title">{escape(title)}</h1>
    <p class="report-subtitle">{escape(subtitle)}</p>
    <div class="report-meta">
      <span>📅 {date.today().strftime("%d.%m.%Y")}</span>
      <span>🔍 {source_count} Datenquellen</span>
      <span>⏱️ {duration}s</span>
    </div>
  </div>
  {content}
  <div class="report-footer">
    <p>♔ X-Ray Intelligence — Ainary Ventures</p>
    <p>Quellen: {escape(sources_list)} | Stand: {date.today().strftime("%d.%m.%Y")}</p>
    <p style="margin-top:8px">Automatisch generiert. Alle Angaben ohne Gewähr.</p>
  </div>
</div>
</body>
</html>"""

    def _risk_signals_html(self, signals):
        html = ""
        for sig in signals:
            cls = f"signal-{sig['level'].lower()}"
            html += f'<div class="signal {cls}"><span class="signal-level">{sig["level"]}</span><span><strong>{escape(sig["source"])}:</strong> {escape(sig["detail"])}</span></div>'
        return html

    def _positive_signals_html(self, signals):
        html = ""
        for sig in signals:
            html += f'<div class="signal signal-positive"><span class="signal-level">✅</span><span><strong>{escape(sig["source"])}:</strong> {escape(sig["detail"])}</span></div>'
        return html

    def _financials_html(self, financials):
        if not financials:
            return ""
        rows = ""
        labels = {"umsatz": "Umsatz", "gewinn": "Jahresüberschuss", "eigenkapital": "Eigenkapital",
                  "bilanzsumme": "Bilanzsumme", "mitarbeiter": "Mitarbeiter"}
        for key, val in financials.items():
            rows += f"<tr><td>{labels.get(key, key)}</td><td style='font-family:var(--font);text-align:right'>{escape(val)}</td></tr>"
        return f"""<div class="section"><div class="section-title">💰 Finanzkennzahlen (extrahiert)</div>
        <table><thead><tr><th>Kennzahl</th><th style="text-align:right">Wert</th></tr></thead><tbody>{rows}</tbody></table></div>"""

    def _bundesanzeiger_html(self, reports):
        if not reports:
            return ""
        cards = ""
        for r in reports[:5]:
            preview = escape(r.get("content", "")[:400])
            cards += f'<div class="card"><div class="card-title">{escape(r.get("name", "N/A"))}</div><div class="card-meta">{r.get("date", "N/A")} · {r.get("type", "N/A")}</div><div class="card-content">{preview}…</div></div>'
        return f'<div class="section"><div class="section-title">📑 Bundesanzeiger</div><p style="font-size:13px;color:var(--text2);margin-bottom:12px">{len(reports)} Berichte</p>{cards}</div>'

    def _companies_table_html(self, companies, title="🏢 Handelsregister", limit=30):
        if not companies:
            return ""
        rows = ""
        for c in companies[:limit]:
            status = "🟢" if c.get("status") in ["currently registered", "unknown", None, ""] else "🔴"
            officers = c.get("officers", [])
            of_str = ", ".join([o.get("name", str(o)) if isinstance(o, dict) else str(o) for o in officers[:2]]) if officers else "—"
            rows += f'<tr><td>{status} {escape(c.get("name", "N/A"))}</td><td>{escape(c.get("type", "N/A"))}</td><td style="font-size:11px">{escape(of_str)}</td><td style="font-family:var(--font);font-size:11px">{escape(c.get("register", "N/A"))}</td></tr>'
        return f'<div class="section"><div class="section-title">{title}</div><table><thead><tr><th>Firma</th><th>Rechtsform</th><th>GF</th><th>Register</th></tr></thead><tbody>{rows}</tbody></table></div>'

    def _insolvency_html(self, insolvencies):
        if insolvencies:
            items = ""
            for i in insolvencies[:5]:
                items += f'<div class="signal signal-critical"><span class="signal-level">INSOLVENZ</span><span><strong>{escape(i.get("court","N/A"))}</strong> — {i.get("date","N/A")}<br>{escape(i.get("content","")[:200])}</span></div>'
            return f'<div class="section"><div class="section-title">⚠️ Insolvenzbekanntmachungen</div>{items}</div>'
        return '<div class="section"><div class="section-title">✅ Insolvenzprüfung</div><p style="color:var(--green);font-weight:600">Keine Verfahren gefunden.</p></div>'

    # ─── USE CASE 1: VC Due Diligence ─────────────────────────

    def dd_report(self, analysis, data, duration):
        """Deep due diligence: risk-focused, investment-ready."""
        sections = []

        # Executive Summary
        risk_class = analysis["overall_risk"].lower()
        sections.append(f"""
        <div class="section">
          <div class="section-title">📊 Executive Summary</div>
          <div class="stats">
            <div class="stat"><div class="stat-value" style="color:{analysis.get('risk_color','#737373')}">{analysis['overall_risk']}</div><div class="stat-label">Gesamtrisiko</div></div>
            <div class="stat"><div class="stat-value">{analysis['data_source_count']}</div><div class="stat-label">Quellen geprüft</div></div>
            <div class="stat"><div class="stat-value">{len(analysis.get('risk_signals',[]))}</div><div class="stat-label">Risk Signals</div></div>
            <div class="stat"><div class="stat-value">{len(analysis.get('positive_signals',[]))}</div><div class="stat-label">Positive Signals</div></div>
          </div>
          {self._risk_signals_html(analysis.get('risk_signals', []))}
          {self._positive_signals_html(analysis.get('positive_signals', []))}
        </div>""")

        # Governance
        gov = analysis.get("governance", {})
        if gov:
            officers_html = ""
            for o in gov.get("officers", []):
                name = o.get("name", str(o)) if isinstance(o, dict) else str(o)
                role = o.get("position", o.get("role", "")) if isinstance(o, dict) else ""
                officers_html += f'<tr><td>{escape(name)}</td><td>{escape(role)}</td></tr>'
            if officers_html:
                sections.append(f"""
                <div class="section"><div class="section-title">👥 Governance & Führung</div>
                <div class="stats">
                  <div class="stat"><div class="stat-value">{gov.get('officer_count', 0)}</div><div class="stat-label">Organe</div></div>
                  <div class="stat"><div class="stat-value" style="font-size:16px">{escape(gov.get('type','N/A'))}</div><div class="stat-label">Rechtsform</div></div>
                  <div class="stat"><div class="stat-value" style="font-size:16px">{escape(gov.get('status','N/A'))}</div><div class="stat-label">Status</div></div>
                </div>
                <table><thead><tr><th>Name</th><th>Position</th></tr></thead><tbody>{officers_html}</tbody></table></div>""")

        # Financials
        sections.append(self._financials_html(analysis.get("financials", {})))

        # Bundesanzeiger
        sections.append(self._bundesanzeiger_html(data.get("bundesanzeiger", [])))

        # Insolvency
        sections.append(self._insolvency_html(data.get("insolvency", [])))

        # Investment Verdict
        risk = analysis["overall_risk"]
        if risk == "LOW":
            verdict = "Keine kritischen Risiken identifiziert. Due Diligence auf Basis öffentlicher Daten gibt grünes Licht für vertiefte Prüfung."
            verdict_icon = "🟢"
        elif risk == "MEDIUM":
            verdict = "Moderate Risiken erkannt. Empfehlung: Gezielte Nachfragen zu den markierten Signalen vor Investment-Entscheidung."
            verdict_icon = "🟡"
        else:
            verdict = "Signifikante Risiken identifiziert. Empfehlung: Erweiterte Due Diligence oder Abbruch bis Klärung der Risk Signals."
            verdict_icon = "🔴"

        sections.append(f"""
        <div class="verdict">
          <div class="verdict-title">{verdict_icon} Investment Verdict</div>
          <p>{verdict}</p>
        </div>""")

        return self._wrap(
            title=f"Due Diligence: {analysis['name']}",
            subtitle=f"VC Investment Due Diligence · {analysis['data_source_count']} Quellen · Risk: {analysis['overall_risk']}",
            source_count=analysis["data_source_count"],
            duration=duration,
            sources_list=", ".join(analysis.get("data_sources", [])),
            content="\n".join(s for s in sections if s),
            use_case_badge="| 🎯 VC DUE DILIGENCE"
        )

    # ─── USE CASE 2: Consulting Pitch Prep ────────────────────

    def pitch_report(self, analysis, data, duration):
        """Know the client better than they know themselves."""
        sections = []

        # Quick Intel
        ba_count = len(data.get("bundesanzeiger", []))
        reg_count = len(data.get("offeneregister", []))
        insol_count = len(data.get("insolvency", []))
        gov = analysis.get("governance", {})

        sections.append(f"""
        <div class="section">
          <div class="section-title">🎯 Quick Intel — Dein Gesprächsvorteil</div>
          <div class="stats">
            <div class="stat"><div class="stat-value" style="font-size:16px">{escape(gov.get('type','N/A'))}</div><div class="stat-label">Rechtsform</div></div>
            <div class="stat"><div class="stat-value">{gov.get('officer_count', '?')}</div><div class="stat-label">Führungskräfte</div></div>
            <div class="stat"><div class="stat-value">{ba_count}</div><div class="stat-label">Finanzberichte</div></div>
            <div class="stat"><div class="stat-value" style="color:{'var(--green)' if insol_count==0 else 'var(--red)'}">{insol_count}</div><div class="stat-label">Insolvenzverfahren</div></div>
          </div>
        </div>""")

        # Talking Points
        talking_points = []
        financials = analysis.get("financials", {})
        if financials.get("umsatz"):
            talking_points.append(f"Umsatz liegt bei {financials['umsatz']} — frag nach Wachstumsrate")
        if financials.get("mitarbeiter"):
            talking_points.append(f"{financials['mitarbeiter']} Mitarbeiter — frag nach Hiring-Plänen")
        if gov.get("officers"):
            names = [o.get("name", str(o)) if isinstance(o, dict) else str(o) for o in gov["officers"][:3]]
            talking_points.append(f"Geschäftsführung: {', '.join(names)} — recherchiere LinkedIn-Profile")
        if analysis.get("positive_signals"):
            for sig in analysis["positive_signals"][:2]:
                talking_points.append(f"{sig['detail']}")
        if analysis.get("risk_signals"):
            for sig in analysis["risk_signals"][:2]:
                if sig["level"] != "LOW":
                    talking_points.append(f"⚠️ {sig['detail']} — vorsichtig ansprechen")

        if not talking_points:
            talking_points = ["Wenig öffentliche Daten — im Gespräch mehr herausfinden", "Nach Strategie und Wachstumsplänen fragen"]

        tp_html = "".join([f'<div class="pitch-bullet">{escape(tp)}</div>' for tp in talking_points])
        sections.append(f"""
        <div class="pitch-section">
          <h3>🗣️ Talking Points für dein Meeting</h3>
          {tp_html}
        </div>""")

        # What they probably DON'T want you to know
        risk_points = []
        for sig in analysis.get("risk_signals", []):
            risk_points.append(f"{sig['source']}: {sig['detail']}")

        if risk_points:
            rp_html = "".join([f'<div class="pitch-bullet">{escape(rp)}</div>' for rp in risk_points])
            sections.append(f"""
            <div class="pitch-section" style="border-color:var(--orange)">
              <h3 style="color:var(--orange)">🔒 Was sie wahrscheinlich NICHT erzählen</h3>
              {rp_html}
            </div>""")

        # Financials
        sections.append(self._financials_html(financials))

        # Governance Detail
        if gov.get("officers"):
            officers_html = ""
            for o in gov["officers"]:
                name = o.get("name", str(o)) if isinstance(o, dict) else str(o)
                role = o.get("position", o.get("role", "")) if isinstance(o, dict) else ""
                officers_html += f'<tr><td><strong>{escape(name)}</strong></td><td>{escape(role)}</td></tr>'
            sections.append(f"""
            <div class="section"><div class="section-title">👥 Wer sitzt am Tisch?</div>
            <table><thead><tr><th>Name</th><th>Position</th></tr></thead><tbody>{officers_html}</tbody></table></div>""")

        # Prep Checklist
        sections.append("""
        <div class="pitch-section" style="border-color:var(--accent)">
          <h3>✅ Meeting Prep Checklist</h3>
          <div class="pitch-bullet">LinkedIn-Profile der GF gecheckt?</div>
          <div class="pitch-bullet">Letzte News / Pressemitteilungen gelesen?</div>
          <div class="pitch-bullet">Branchenkontext verstanden?</div>
          <div class="pitch-bullet">Eigene Value Proposition auf deren Pain Points angepasst?</div>
          <div class="pitch-bullet">Konkretes Angebot / nächsten Schritt vorbereitet?</div>
        </div>""")

        return self._wrap(
            title=f"Pitch Prep: {analysis['name']}",
            subtitle=f"Consulting Meeting Vorbereitung · Wisse mehr als dein Gegenüber",
            source_count=analysis["data_source_count"],
            duration=duration,
            sources_list=", ".join(analysis.get("data_sources", [])),
            content="\n".join(s for s in sections if s),
            use_case_badge="| 💼 PITCH PREP"
        )

    # ─── USE CASE 3: Competitor Intel ─────────────────────────

    def compete_report(self, analyses, comparison, all_data, duration):
        """Side-by-side competitor comparison."""
        sections = []

        # Comparison Grid
        cards = ""
        for comp in comparison["companies"]:
            is_winner = comp["name"] == comparison.get("winner")
            winner_class = "winner" if is_winner else ""
            winner_badge = " 👑" if is_winner else ""
            risk_color = {"LOW": "var(--green)", "MEDIUM": "var(--orange)", "HIGH": "var(--red)"}.get(comp["risk"], "var(--text2)")

            fin_html = ""
            for k, v in comp.get("financials", {}).items():
                fin_html += f'<div style="font-size:12px;padding:2px 0"><span style="color:var(--text2)">{k}:</span> {escape(v)}</div>'

            cards += f"""
            <div class="comparison-card {winner_class}">
              <h3>{escape(comp['name'])}{winner_badge}</h3>
              <div class="stats" style="grid-template-columns:1fr 1fr">
                <div class="stat"><div class="stat-value" style="color:{risk_color};font-size:20px">{comp['risk']}</div><div class="stat-label">Risiko</div></div>
                <div class="stat"><div class="stat-value" style="font-size:20px">{comp['risk_signals']}</div><div class="stat-label">Warnings</div></div>
              </div>
              {fin_html if fin_html else '<p style="font-size:12px;color:var(--text2)">Keine Finanzdaten extrahiert</p>'}
            </div>"""

        sections.append(f"""
        <div class="section">
          <div class="section-title">⚔️ Head-to-Head Vergleich</div>
          <div class="comparison-grid">{cards}</div>
        </div>""")

        # Verdict
        if comparison.get("winner"):
            sections.append(f"""
            <div class="verdict">
              <div class="verdict-title">👑 Stärkeres Profil: {escape(comparison['winner'])}</div>
              <p>Basierend auf öffentlichen Daten: weniger Risiko-Signale, mehr positive Indikatoren. Detailanalyse je Firma unten.</p>
            </div>""")

        # Per-company details
        for a in analyses:
            name = a["name"]
            d = all_data.get(name, {})
            sections.append(f'<div class="section"><div class="section-title">📋 Detail: {escape(name)}</div>')
            sections.append(self._risk_signals_html(a.get("risk_signals", [])))
            sections.append(self._positive_signals_html(a.get("positive_signals", [])))
            sections.append('</div>')
            sections.append(self._financials_html(a.get("financials", {})))

        names = " vs ".join([a["name"] for a in analyses])
        return self._wrap(
            title=f"Competitor Intel: {names}",
            subtitle=f"Wettbewerbsanalyse · {len(analyses)} Unternehmen verglichen",
            source_count=sum(a["data_source_count"] for a in analyses),
            duration=duration,
            sources_list="Bundesanzeiger, offeneregister.de, Insolvenzbekanntmachungen",
            content="\n".join(s for s in sections if s),
            use_case_badge="| ⚔️ COMPETITOR INTEL"
        )

    # ─── USE CASE 4: City / Standort ──────────────────────────

    def city_report(self, city_analysis, companies, duration):
        sections = []

        # Stats
        sections.append(f"""
        <div class="section">
          <div class="section-title">📊 Wirtschaftsübersicht</div>
          <div class="stats">
            <div class="stat"><div class="stat-value">{city_analysis['total_companies']}</div><div class="stat-label">Firmen gesamt</div></div>
            <div class="stat"><div class="stat-value" style="color:var(--green)">{city_analysis['active']}</div><div class="stat-label">Aktiv</div></div>
            <div class="stat"><div class="stat-value" style="color:var(--red)">{city_analysis['inactive']}</div><div class="stat-label">Inaktiv</div></div>
            <div class="stat"><div class="stat-value">{city_analysis['active_rate']}%</div><div class="stat-label">Aktiv-Quote</div></div>
          </div>
        </div>""")

        # Company Types Bar Chart
        types = city_analysis.get("company_types", {})
        if types:
            max_val = max(types.values())
            bars = ""
            for t, count in types.items():
                w = min(100, count / max_val * 100)
                bars += f'<div style="display:flex;align-items:center;gap:10px;margin-bottom:6px;font-size:13px"><span style="min-width:250px">{escape(t)}</span><div style="flex:1;height:8px;background:var(--border);border-radius:4px"><div style="height:100%;width:{w}%;background:var(--accent);border-radius:4px"></div></div><span style="font-family:var(--font);min-width:30px;text-align:right">{count}</span></div>'
            sections.append(f'<div class="section"><div class="section-title">🏭 Unternehmensstruktur</div>{bars}</div>')

        # Companies Table
        sections.append(self._companies_table_html(companies, f"🏢 Firmen in {city_analysis['city']}", 40))

        return self._wrap(
            title=f"Standort {city_analysis['city']}",
            subtitle=f"Kommunale Wirtschaftsintelligenz · {city_analysis['total_companies']} Unternehmen",
            source_count=1,
            duration=duration,
            sources_list="offeneregister.de",
            content="\n".join(s for s in sections if s),
            use_case_badge="| 🏙️ STANDORT-ANALYSE"
        )


# ─── CLI ──────────────────────────────────────────────────────

def slugify(text):
    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')

async def cmd_dd(args):
    """USE CASE 1: VC Due Diligence"""
    t0 = time.time()
    print(f"♔ X-Ray Due Diligence: {args.company}", file=sys.stderr)
    print("=" * 50, file=sys.stderr)

    collector = IntelCollector()
    collector.full_company_scan(args.company, url=args.url)

    analyzer = IntelAnalyzer(collector.data)
    analysis = analyzer.analyze_company(args.company)
    duration = round(time.time() - t0, 1)

    if args.json:
        print(json.dumps({"analysis": analysis, "data": collector.data}, indent=2, ensure_ascii=False, default=str))
    else:
        gen = ReportGenerator()
        html = gen.dd_report(analysis, collector.data, duration)
        out = args.output or str(OUTPUT_DIR / f"dd-{slugify(args.company)}-{date.today()}.html")
        Path(out).write_text(html)
        print(f"\n✅ {out}", file=sys.stderr)
        print(f"   Risk: {analysis['overall_risk']} | Sources: {analysis['data_source_count']} | Signals: {len(analysis['risk_signals'])}", file=sys.stderr)

async def cmd_pitch(args):
    """USE CASE 2: Consulting Pitch Prep"""
    t0 = time.time()
    print(f"♔ X-Ray Pitch Prep: {args.company}", file=sys.stderr)
    print("=" * 50, file=sys.stderr)

    collector = IntelCollector()
    collector.full_company_scan(args.company, url=args.url)

    analyzer = IntelAnalyzer(collector.data)
    analysis = analyzer.analyze_company(args.company)
    duration = round(time.time() - t0, 1)

    if args.json:
        print(json.dumps({"analysis": analysis, "data": collector.data}, indent=2, ensure_ascii=False, default=str))
    else:
        gen = ReportGenerator()
        html = gen.pitch_report(analysis, collector.data, duration)
        out = args.output or str(OUTPUT_DIR / f"pitch-{slugify(args.company)}-{date.today()}.html")
        Path(out).write_text(html)
        print(f"\n✅ {out}", file=sys.stderr)
        print(f"   Talking Points generiert. Mach dich bereit. ♔", file=sys.stderr)

async def cmd_compete(args):
    """USE CASE 3: Competitor Intel"""
    t0 = time.time()
    companies = [args.company] + (args.vs or [])
    if len(companies) < 2:
        print("❌ Mindestens 2 Firmen nötig. Nutze: xray compete 'Firma A' --vs 'Firma B'", file=sys.stderr)
        sys.exit(1)

    print(f"♔ X-Ray Competitor Intel: {' vs '.join(companies)}", file=sys.stderr)
    print("=" * 50, file=sys.stderr)

    analyses = []
    all_data = {}
    for company in companies:
        print(f"\n── {company} ──", file=sys.stderr)
        collector = IntelCollector()
        collector.full_company_scan(company)
        analyzer = IntelAnalyzer(collector.data)
        analysis = analyzer.analyze_company(company)
        analyses.append(analysis)
        all_data[company] = collector.data

    # Compare
    analyzer = IntelAnalyzer({})
    comparison = analyzer.compare_companies(analyses)
    duration = round(time.time() - t0, 1)

    if args.json:
        print(json.dumps({"comparison": comparison, "analyses": analyses}, indent=2, ensure_ascii=False, default=str))
    else:
        gen = ReportGenerator()
        html = gen.compete_report(analyses, comparison, all_data, duration)
        slug = "-vs-".join([slugify(c) for c in companies])
        out = args.output or str(OUTPUT_DIR / f"compete-{slug}-{date.today()}.html")
        Path(out).write_text(html)
        print(f"\n✅ {out}", file=sys.stderr)
        print(f"   Winner: {comparison.get('winner', 'N/A')} ♔", file=sys.stderr)

async def cmd_city(args):
    """USE CASE 4: Standort-Analyse"""
    t0 = time.time()
    print(f"♔ X-Ray Standort: {args.city}", file=sys.stderr)
    print("=" * 50, file=sys.stderr)

    collector = IntelCollector()
    companies = collector.collect_offeneregister(args.city, limit=300)

    analyzer = IntelAnalyzer(collector.data)
    city_analysis = analyzer.analyze_city(args.city, companies)
    duration = round(time.time() - t0, 1)

    if args.json:
        print(json.dumps({"city": city_analysis, "companies": companies}, indent=2, ensure_ascii=False, default=str))
    else:
        gen = ReportGenerator()
        html = gen.city_report(city_analysis, companies, duration)
        out = args.output or str(OUTPUT_DIR / f"city-{slugify(args.city)}-{date.today()}.html")
        Path(out).write_text(html)
        print(f"\n✅ {out}", file=sys.stderr)
        print(f"   {city_analysis['total_companies']} Firmen | {city_analysis['active_rate']}% aktiv", file=sys.stderr)


def main():
    parser = argparse.ArgumentParser(
        description="♔ X-Ray Intelligence — 4 Use Cases, 1 CLI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Use Cases:
  xray dd       "NOMOS Glashütte"                    VC Due Diligence
  xray pitch    "BMW AG" --url https://bmw.de         Consulting Pitch Prep
  xray compete  "NOMOS" --vs "Mühle-Glashütte"        Competitor Intel
  xray city     "Glashütte"                           Standort-Analyse
"""
    )
    sub = parser.add_subparsers(dest="command")

    # dd
    p_dd = sub.add_parser("dd", help="VC Due Diligence")
    p_dd.add_argument("company", help="Company name")
    p_dd.add_argument("--url", help="Company website URL")
    p_dd.add_argument("--output", "-o", help="Output file path")
    p_dd.add_argument("--json", action="store_true")

    # pitch
    p_pitch = sub.add_parser("pitch", help="Consulting Pitch Prep")
    p_pitch.add_argument("company", help="Company name")
    p_pitch.add_argument("--url", help="Company website URL")
    p_pitch.add_argument("--output", "-o", help="Output file path")
    p_pitch.add_argument("--json", action="store_true")

    # compete
    p_comp = sub.add_parser("compete", help="Competitor Intel")
    p_comp.add_argument("company", help="Primary company")
    p_comp.add_argument("--vs", nargs="+", help="Competitor(s) to compare against")
    p_comp.add_argument("--output", "-o", help="Output file path")
    p_comp.add_argument("--json", action="store_true")

    # city
    p_city = sub.add_parser("city", help="Standort-Analyse")
    p_city.add_argument("city", help="City name")
    p_city.add_argument("--output", "-o", help="Output file path")
    p_city.add_argument("--json", action="store_true")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    cmds = {"dd": cmd_dd, "pitch": cmd_pitch, "compete": cmd_compete, "city": cmd_city}
    asyncio.run(cmds[args.command](args))


if __name__ == "__main__":
    main()
