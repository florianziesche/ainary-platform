#!/usr/bin/env python3
"""
Ainary RAG — Build vector index from city JSON data.
Embeds all entities (KB entries) from data/cities/*.json using Voyage AI.
Outputs: rag/index.json (chunks + embeddings + metadata)

Usage: python3 rag/build_index.py
"""

import json, os, sys, time
import numpy as np
import voyageai

CITIES_DIR = "data/cities"
INDEX_FILE = "rag/index.json"
VOYAGE_MODEL = "voyage-3-lite"  # Fast + cheap, good for structured data

def chunk_entity(city_id: str, entity_id: str, entity: dict, tenant: dict) -> list[dict]:
    """Convert one KB entity into searchable text chunks."""
    chunks = []
    name = entity.get("name", entity_id)
    role = entity.get("role", "")
    party = entity.get("party", "")
    summary = entity.get("summary", "")
    city_name = tenant.get("gemeinde", city_id)
    wahl = tenant.get("wahl", "")
    
    # Main chunk: identity + summary
    main_text = f"{name} — {role} ({party}), {city_name}"
    if wahl:
        main_text += f", Wahl: {wahl}"
    if summary:
        main_text += f"\n{summary}"
    
    chunks.append({
        "id": f"{city_id}/{entity_id}/main",
        "city": city_id,
        "entity": entity_id,
        "type": "summary",
        "text": main_text,
        "name": name
    })
    
    # Properties chunk
    props = entity.get("properties", [])
    if props:
        prop_lines = [f"{name} — Eigenschaften ({city_name}):"]
        for p in props:
            # Strip HTML tags for embedding
            val = p.get("val", "").replace("<strong>", "").replace("</strong>", "")
            val = val.replace("<strong style='color:var(--amber)'>", "").replace("<strong style='color:var(--green)'>", "").replace("<strong style='color:var(--red)'>", "")
            prop_lines.append(f"- {p.get('key', '')}: {val} [{p.get('src', '')}]")
        chunks.append({
            "id": f"{city_id}/{entity_id}/properties",
            "city": city_id,
            "entity": entity_id,
            "type": "properties",
            "text": "\n".join(prop_lines),
            "name": name
        })
    
    # Controversies chunk
    contros = entity.get("controversies", [])
    if contros:
        contro_lines = [f"{name} — Kontroversen/Skandale ({city_name}):"]
        for c in contros:
            contro_lines.append(f"- {c.get('title', '')}: {c.get('text', '')} [Schwere: {c.get('severity', '')}, Confidence: {c.get('conf', '')}%]")
        chunks.append({
            "id": f"{city_id}/{entity_id}/controversies",
            "city": city_id,
            "entity": entity_id,
            "type": "controversies",
            "text": "\n".join(contro_lines),
            "name": name
        })
    
    # Connections chunk
    conns = entity.get("connections", [])
    if conns:
        conn_lines = [f"{name} — Verbindungen ({city_name}):"]
        for c in conns:
            conn_lines.append(f"- {c.get('type', '')}: {name} → {c.get('target', '')} — {c.get('desc', '')}")
        chunks.append({
            "id": f"{city_id}/{entity_id}/connections",
            "city": city_id,
            "entity": entity_id,
            "type": "connections",
            "text": "\n".join(conn_lines),
            "name": name
        })
    
    # Karriere/Timeline chunk
    karriere = entity.get("karriere", [])
    if karriere:
        kar_lines = [f"{name} — Karriere ({city_name}):"]
        for k in karriere:
            kar_lines.append(f"- {k.get('zeitraum', '')}: {k.get('titel', '')} — {k.get('beschreibung', '')} [{k.get('quelle', '')}]")
        chunks.append({
            "id": f"{city_id}/{entity_id}/karriere",
            "city": city_id,
            "entity": entity_id,
            "type": "karriere",
            "text": "\n".join(kar_lines),
            "name": name
        })
    
    # Zitate chunk
    zitate = entity.get("zitate", [])
    if zitate:
        zit_lines = [f"{name} — Zitate ({city_name}):"]
        for z in zitate:
            zit_lines.append(f'- "{z.get("text", "")}" — {z.get("kontext", "")} [{z.get("quelle", "")}]')
        chunks.append({
            "id": f"{city_id}/{entity_id}/zitate",
            "city": city_id,
            "entity": entity_id,
            "type": "zitate",
            "text": "\n".join(zit_lines),
            "name": name
        })
    
    return chunks


def chunk_tenant(city_id: str, tenant: dict) -> list[dict]:
    """Create chunks from tenant (city-level) data."""
    chunks = []
    city_name = tenant.get("gemeinde", city_id)
    
    # City overview
    overview_parts = [f"{city_name} — Kommunal-Intelligence"]
    overview_parts.append(f"Typ: {tenant.get('typ', '')}, Wahl: {tenant.get('wahl', '')}")
    overview_parts.append(f"Einwohner: {tenant.get('ew', '')}, {tenant.get('landkreis', '')}, {tenant.get('regierungsbezirk', '')}")
    
    sd = tenant.get("strukturdaten", {})
    if sd:
        for k, v in sd.items():
            if isinstance(v, list):
                overview_parts.append(f"{k}: {', '.join(v)}")
            else:
                overview_parts.append(f"{k}: {v}")
    
    chunks.append({
        "id": f"{city_id}/tenant/overview",
        "city": city_id,
        "entity": "_city",
        "type": "city_overview",
        "text": "\n".join(overview_parts),
        "name": city_name
    })
    
    # Alerts
    alerts = tenant.get("alerts", [])
    if alerts:
        alert_lines = [f"{city_name} — Aktuelle Alerts:"]
        for a in alerts:
            alert_lines.append(f"- [{a.get('priority', '')}] {a.get('title', '')} ({a.get('meta', '')})")
        chunks.append({
            "id": f"{city_id}/tenant/alerts",
            "city": city_id,
            "entity": "_city",
            "type": "alerts",
            "text": "\n".join(alert_lines),
            "name": city_name
        })
    
    # Gemeinderat
    gr = tenant.get("gemeinderat2020", [])
    if gr:
        gr_lines = [f"{city_name} — Gemeinderat 2020:"]
        for g in gr:
            gr_lines.append(f"- {g.get('partei', '')}: {g.get('prozent', '')}% ({g.get('sitze', '')} Sitze)")
        chunks.append({
            "id": f"{city_id}/tenant/gemeinderat",
            "city": city_id,
            "entity": "_city",
            "type": "gemeinderat",
            "text": "\n".join(gr_lines),
            "name": city_name
        })
    
    return chunks


def chunk_graph(city_id: str, graph: dict, tenant: dict) -> list[dict]:
    """Create a chunk from the network graph."""
    nodes = graph.get("nodes", [])
    links = graph.get("links", [])
    city_name = tenant.get("gemeinde", city_id)
    
    if not nodes:
        return []
    
    lines = [f"{city_name} — Netzwerk-Graph ({len(nodes)} Akteure, {len(links)} Verbindungen):"]
    lines.append("Akteure:")
    for n in nodes:
        lines.append(f"- {n.get('label', n.get('id', ''))}: {n.get('sub', '')} [{n.get('group', n.get('type', ''))}]")
    lines.append("Verbindungen:")
    for l in links:
        lines.append(f"- {l.get('source', '')} → {l.get('target', '')}: {l.get('label', '')}")
    
    return [{
        "id": f"{city_id}/graph",
        "city": city_id,
        "entity": "_graph",
        "type": "graph",
        "text": "\n".join(lines),
        "name": city_name
    }]


def main():
    # Load API key from OpenClaw config
    config_path = os.path.expanduser("~/.openclaw/openclaw.json")
    api_key = None
    try:
        with open(config_path) as f:
            config = json.load(f)
        api_key = config.get("agents", {}).get("defaults", {}).get("memorySearch", {}).get("apiKey")
        if not api_key:
            # Try env
            api_key = os.environ.get("VOYAGE_API_KEY")
    except:
        api_key = os.environ.get("VOYAGE_API_KEY")
    
    if not api_key:
        print("ERROR: No Voyage API key found")
        sys.exit(1)
    
    print(f"Voyage API key: {api_key[:8]}...")
    
    # Build chunks from all city data
    all_chunks = []
    for fname in sorted(os.listdir(CITIES_DIR)):
        if not fname.endswith(".json"):
            continue
        city_id = fname.replace(".json", "")
        with open(os.path.join(CITIES_DIR, fname)) as f:
            data = json.load(f)
        
        tenant = data.get("tenant", {})
        kb = data.get("kb", {})
        graph = data.get("graph", {})
        
        # City-level chunks
        all_chunks.extend(chunk_tenant(city_id, tenant))
        all_chunks.extend(chunk_graph(city_id, graph, tenant))
        
        # Entity chunks
        for eid, entity in kb.items():
            all_chunks.extend(chunk_entity(city_id, eid, entity, tenant))
        
        city_name = tenant.get("gemeinde", city_id)
        
        # News chunks
        news = data.get("news", [])
        if news:
            news_lines = [f"{city_name} — Nachrichten:"]
            for n in news:
                news_lines.append(f"- [{n.get('date','')}] {n.get('title','')} ({n.get('source','')}) — {n.get('body','')}")
            all_chunks.append({"id": f"{city_id}/news", "city": city_id, "entity": "_city", "type": "news", "text": "\n".join(news_lines), "name": city_name})
        
        # Hypotheses
        hypotheses = data.get("hypotheses", [])
        if hypotheses:
            hyp_lines = [f"{city_name} — Hypothesen/Szenarien:"]
            for h in hypotheses:
                hyp_lines.append(f"- {h.get('title','')}: {h.get('summary','')} [Conf: {h.get('confidence','')}%]")
            all_chunks.append({"id": f"{city_id}/hypotheses", "city": city_id, "entity": "_city", "type": "hypotheses", "text": "\n".join(hyp_lines), "name": city_name})
        
        # Forecast
        forecast = data.get("forecast", {})
        if forecast and forecast.get("kandidaten"):
            fc_lines = [f"{city_name} — Prognose ({forecast.get('method','')}, Conf: {forecast.get('confidence','')}%):"]
            for k in forecast.get("kandidaten", []):
                fc_lines.append(f"- {k.get('name','')} ({k.get('partei','')}): {k.get('min','')}-{k.get('max','')}%, zentral {k.get('zentral','')}%")
            for s in forecast.get("scenarios", []):
                fc_lines.append(f"- Szenario: {s.get('label','')} — {s.get('probability','')}")
            all_chunks.append({"id": f"{city_id}/forecast", "city": city_id, "entity": "_city", "type": "forecast", "text": "\n".join(fc_lines), "name": city_name})
        
        # Actions
        actions = data.get("actions", [])
        if actions:
            act_lines = [f"{city_name} — Handlungsempfehlungen:"]
            for a in actions:
                act_lines.append(f"- [{a.get('priority','')}] {a.get('title','')}: {a.get('body','')} (Deadline: {a.get('urgency','')})")
            all_chunks.append({"id": f"{city_id}/actions", "city": city_id, "entity": "_city", "type": "actions", "text": "\n".join(act_lines), "name": city_name})
        
        # Sentiment
        sentiment = data.get("sentiment", {})
        if sentiment and sentiment.get("topics"):
            sent_lines = [f"{city_name} — Stimmungsbild: {sentiment.get('overall','')}"]
            for topic in sentiment.get("topics", []):
                sent_lines.append(f"- {topic.get('topic','')}: {topic.get('desc','')} [Valenz: {topic.get('valence','')}]")
            all_chunks.append({"id": f"{city_id}/sentiment", "city": city_id, "entity": "_city", "type": "sentiment", "text": "\n".join(sent_lines), "name": city_name})
    
    print(f"Total chunks: {len(all_chunks)}")
    
    # Show chunk distribution
    by_type = {}
    for c in all_chunks:
        t = c["type"]
        by_type[t] = by_type.get(t, 0) + 1
    for t, count in sorted(by_type.items()):
        print(f"  {t}: {count}")
    
    # Embed with Voyage
    vo = voyageai.Client(api_key=api_key)
    texts = [c["text"] for c in all_chunks]
    
    print(f"\nEmbedding {len(texts)} chunks with {VOYAGE_MODEL}...")
    
    # Batch embed (Voyage supports up to 128 texts per call)
    all_embeddings = []
    batch_size = 64
    for i in range(0, len(texts), batch_size):
        batch = texts[i:i+batch_size]
        result = vo.embed(batch, model=VOYAGE_MODEL, input_type="document")
        all_embeddings.extend(result.embeddings)
        print(f"  Batch {i//batch_size + 1}: {len(batch)} chunks embedded")
        if i + batch_size < len(texts):
            time.sleep(0.5)  # Rate limit
    
    # Build index
    index = {
        "version": 1,
        "model": VOYAGE_MODEL,
        "created": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "chunks": [],
    }
    
    for chunk, embedding in zip(all_chunks, all_embeddings):
        index["chunks"].append({
            "id": chunk["id"],
            "city": chunk["city"],
            "entity": chunk["entity"],
            "type": chunk["type"],
            "name": chunk["name"],
            "text": chunk["text"],
            "embedding": embedding
        })
    
    # Save
    os.makedirs(os.path.dirname(INDEX_FILE), exist_ok=True)
    with open(INDEX_FILE, "w") as f:
        json.dump(index, f, ensure_ascii=False)
    
    size_mb = os.path.getsize(INDEX_FILE) / 1024 / 1024
    print(f"\nIndex saved: {INDEX_FILE} ({size_mb:.1f} MB, {len(index['chunks'])} chunks)")


if __name__ == "__main__":
    main()
