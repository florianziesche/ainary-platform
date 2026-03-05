#!/usr/bin/env python3
"""
Ainary Report — FastAPI Backend
Wraps xray.py intelligence engine with SSE progress streaming.
"""

import sys, os, json, asyncio, time, uuid
from pathlib import Path
from datetime import date

# Add venv
VENV = Path.home() / "ainary-tools"
sys.path.insert(0, str(VENV / "lib/python3.12/site-packages"))

# Add xray module
XRAY_DIR = Path(__file__).parent.parent / "xray-intelligence"
sys.path.insert(0, str(XRAY_DIR))

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI(title="Ainary Report", version="1.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

# Serve frontend
STATIC_DIR = Path(__file__).parent
REPORTS_DIR = Path(__file__).parent / "reports"
REPORTS_DIR.mkdir(exist_ok=True)

# In-memory job store
jobs = {}


@app.get("/", response_class=HTMLResponse)
async def index():
    return (STATIC_DIR / "index.html").read_text()


@app.post("/api/scan")
async def start_scan(request: Request):
    """Start a company scan. Returns job_id for SSE progress."""
    body = await request.json()
    company = body.get("company", "").strip()
    mode = body.get("mode", "dd")  # dd, pitch, compete, city
    url = body.get("url", "")
    vs = body.get("vs", "")

    if not company:
        return JSONResponse({"error": "Company name required"}, status_code=400)

    job_id = str(uuid.uuid4())[:8]
    jobs[job_id] = {
        "status": "queued",
        "company": company,
        "mode": mode,
        "url": url,
        "vs": vs,
        "progress": [],
        "result": None,
        "started": time.time()
    }

    # Run scan in background
    asyncio.create_task(run_scan(job_id, company, mode, url, vs))

    return {"job_id": job_id, "status": "started"}


async def run_scan(job_id, company, mode, url, vs):
    """Execute the intelligence scan with progress updates."""
    job = jobs[job_id]
    job["status"] = "running"

    try:
        from xray import IntelCollector, IntelAnalyzer, ReportGenerator, slugify

        collector = IntelCollector(verbose=False)
        t0 = time.time()

        # Step-by-step with progress
        steps = []

        if mode == "city":
            steps = [
                ("Handelsregister durchsuchen...", lambda: collector.collect_offeneregister(company, limit=300)),
            ]
        else:
            steps = [
                ("Bundesanzeiger prüfen...", lambda: collector.collect_bundesanzeiger(company)),
                ("Handelsregister durchsuchen...", lambda: collector.collect_offeneregister(company)),
                ("Insolvenzbekanntmachungen...", lambda: collector.collect_insolvency(company)),
            ]
            if url:
                steps.append(("Website analysieren...", lambda: asyncio.get_event_loop().run_until_complete(collector.collect_website(url))))

        for i, (label, fn) in enumerate(steps):
            job["progress"].append({"step": label, "status": "running", "index": i})
            await asyncio.sleep(0.1)  # Let SSE pick it up

            try:
                # Run blocking IO in thread
                await asyncio.to_thread(fn)
                job["progress"][-1]["status"] = "done"
            except Exception as e:
                job["progress"][-1]["status"] = "error"
                job["progress"][-1]["error"] = str(e)

        # Analyze
        job["progress"].append({"step": "Analyse läuft...", "status": "running", "index": len(steps)})
        await asyncio.sleep(0.1)

        analyzer = IntelAnalyzer(collector.data)
        gen = ReportGenerator()
        duration = round(time.time() - t0, 1)

        if mode == "dd":
            analysis = analyzer.analyze_company(company)
            html = gen.dd_report(analysis, collector.data, duration)
            report_file = f"dd-{slugify(company)}-{date.today()}.html"
        elif mode == "pitch":
            analysis = analyzer.analyze_company(company)
            html = gen.pitch_report(analysis, collector.data, duration)
            report_file = f"pitch-{slugify(company)}-{date.today()}.html"
        elif mode == "city":
            companies = collector.data.get("offeneregister", [])
            analysis = analyzer.analyze_city(company, companies)
            html = gen.city_report(analysis, companies, duration)
            report_file = f"city-{slugify(company)}-{date.today()}.html"
        elif mode == "compete" and vs:
            # Scan competitor too
            job["progress"].append({"step": f"Scanne {vs}...", "status": "running", "index": len(steps) + 1})
            await asyncio.sleep(0.1)

            collector2 = IntelCollector(verbose=False)
            await asyncio.to_thread(lambda: collector2.full_company_scan(vs))

            job["progress"][-1]["status"] = "done"

            analysis1 = analyzer.analyze_company(company)
            analyzer2 = IntelAnalyzer(collector2.data)
            analysis2 = analyzer2.analyze_company(vs)

            comparison = analyzer.compare_companies([analysis1, analysis2])
            all_data = {company: collector.data, vs: collector2.data}
            html = gen.compete_report([analysis1, analysis2], comparison, all_data, duration)
            report_file = f"compete-{slugify(company)}-vs-{slugify(vs)}-{date.today()}.html"
        else:
            analysis = analyzer.analyze_company(company)
            html = gen.dd_report(analysis, collector.data, duration)
            report_file = f"dd-{slugify(company)}-{date.today()}.html"

        # Save report
        report_path = REPORTS_DIR / report_file
        report_path.write_text(html)

        job["progress"][-1]["status"] = "done"

        # Build stats for Pokédex display
        stats = _extract_stats(analysis, mode)

        job["status"] = "complete"
        job["result"] = {
            "report_url": f"/reports/{report_file}",
            "stats": stats,
            "duration": duration,
            "company": company,
            "mode": mode
        }

    except Exception as e:
        job["status"] = "error"
        job["result"] = {"error": str(e)}


def _extract_stats(analysis, mode):
    """Extract Pokémon-style stats from analysis."""
    if mode == "city":
        return {
            "type": "Stadt",
            "type_icon": "🏙️",
            "hp": min(100, analysis.get("active_rate", 50)),
            "hp_label": f"{analysis.get('active_rate', 0)}% aktiv",
            "atk": min(100, analysis.get("total_companies", 0) // 3),
            "atk_label": f"{analysis.get('total_companies', 0)} Firmen",
            "def": 50,
            "def_label": "Wirtschaftsstruktur",
            "spd": min(100, len(analysis.get("company_types", {})) * 15),
            "spd_label": f"{len(analysis.get('company_types', {}))} Branchen",
            "risk": "N/A",
            "risk_color": "#6366f1"
        }

    risk = analysis.get("overall_risk", "MEDIUM")
    risk_colors = {"LOW": "#22c55e", "MEDIUM": "#f59e0b", "HIGH": "#ef4444"}

    # Calculate stats
    ba_count = len(analysis.get("data_sources", []))
    risk_count = len(analysis.get("risk_signals", []))
    pos_count = len(analysis.get("positive_signals", []))
    gov = analysis.get("governance", {})
    fin = analysis.get("financials", {})

    # HP = Financial Health (more financials = more HP)
    hp = min(100, 30 + len(fin) * 15 + pos_count * 10 - risk_count * 15)
    hp = max(5, hp)

    # ATK = Market Position (governance + transparency)
    atk = min(100, 20 + gov.get("officer_count", 0) * 10 + ba_count * 8)
    atk = max(5, atk)

    # DEF = Reputation (inverse of risk signals)
    defense = min(100, 80 - risk_count * 20 + pos_count * 10)
    defense = max(5, defense)

    # SPD = Digital Maturity
    score = analysis.get("score", {})
    spd = min(100, score.get("digital_presence", 3) * 12 + score.get("financial_transparency", 3) * 5)
    spd = max(5, spd)

    return {
        "type": _guess_type(analysis),
        "type_icon": _type_icon(analysis),
        "hp": hp,
        "hp_label": "Financial Health",
        "atk": atk,
        "atk_label": "Market Position",
        "def": defense,
        "def_label": "Reputation",
        "spd": spd,
        "spd_label": "Digital Maturity",
        "risk": risk,
        "risk_color": risk_colors.get(risk, "#6366f1"),
        "sources": ba_count,
        "risk_signals": risk_count,
        "positive_signals": pos_count
    }


def _guess_type(analysis):
    """Guess company type from available data."""
    name = analysis.get("name", "").lower()
    gov = analysis.get("governance", {})
    corp_type = gov.get("type", "").lower()

    if "gmbh" in corp_type or "gmbh" in name:
        return "GmbH"
    elif "ag" in corp_type or " ag" in name:
        return "AG"
    elif "ug" in corp_type:
        return "UG"
    elif "ohg" in corp_type:
        return "OHG"
    elif "kg" in corp_type:
        return "KG"
    return "Unternehmen"


def _type_icon(analysis):
    name = analysis.get("name", "").lower()
    if any(w in name for w in ["tech", "software", "digital", "ai", "it"]):
        return "💻"
    elif any(w in name for w in ["auto", "motor", "fahrzeug"]):
        return "🚗"
    elif any(w in name for w in ["bau", "immobil"]):
        return "🏗️"
    elif any(w in name for w in ["bank", "finanz", "versicher"]):
        return "🏦"
    elif any(w in name for w in ["uhr", "schmuck", "luxus"]):
        return "⌚"
    elif any(w in name for w in ["pharma", "medizin", "health"]):
        return "💊"
    return "🏢"


@app.get("/api/progress/{job_id}")
async def get_progress(job_id: str):
    """SSE stream for scan progress."""
    if job_id not in jobs:
        return JSONResponse({"error": "Job not found"}, status_code=404)

    async def event_stream():
        last_idx = 0
        while True:
            job = jobs.get(job_id)
            if not job:
                break

            # Send new progress steps
            while last_idx < len(job["progress"]):
                step = job["progress"][last_idx]
                yield f"data: {json.dumps({'type': 'progress', 'step': step})}\n\n"
                last_idx += 1

            if job["status"] in ("complete", "error"):
                yield f"data: {json.dumps({'type': 'done', 'status': job['status'], 'result': job['result']})}\n\n"
                break

            await asyncio.sleep(0.3)

    return StreamingResponse(event_stream(), media_type="text/event-stream")


@app.get("/reports/{filename}", response_class=HTMLResponse)
async def serve_report(filename: str):
    path = REPORTS_DIR / filename
    if not path.exists():
        return HTMLResponse("Report not found", status_code=404)
    return HTMLResponse(path.read_text())


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8888)
