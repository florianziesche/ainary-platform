#!/usr/bin/env python3
"""
knowledge_graph.py — Cross-report knowledge graph.

Tracks CONFIRMS / CONTRADICTS / EXTENDS relationships between reports.
Grows with every pipeline run. Enables compound intelligence.

Usage:
    python3 knowledge_graph.py add <report_id> <pipeline_dir>
    python3 knowledge_graph.py show
    python3 knowledge_graph.py links <report_id>
    python3 knowledge_graph.py html
"""

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

WORKSPACE = Path.home() / ".openclaw" / "workspace"
GRAPH_PATH = WORKSPACE / "research-base" / "knowledge-graph.json"


def load_graph() -> dict:
    if GRAPH_PATH.exists():
        return json.loads(GRAPH_PATH.read_text())
    return {"nodes": {}, "edges": [], "updated": None}


def save_graph(graph: dict):
    graph["updated"] = datetime.now(timezone.utc).isoformat()
    GRAPH_PATH.write_text(json.dumps(graph, indent=2))


def add_report(report_id: str, pipeline_dir: str):
    """Add a report to the knowledge graph and detect links to existing reports."""
    graph = load_graph()
    pdir = Path(pipeline_dir)

    # Load report metadata
    brief_path = pdir / "research-brief.json"
    brief = json.loads(brief_path.read_text()) if brief_path.exists() else {}

    bpz_path = pdir / "synthesis-v3" / "beipackzettel.json"
    bpz = json.loads(bpz_path.read_text()) if bpz_path.exists() else {}

    report_path = pdir / "synthesis-v3" / f"final-report-{brief.get('version', 'v1')}.md"
    report_text = report_path.read_text() if report_path.exists() else ""
    word_count = len(report_text.split())

    # Add node
    graph["nodes"][report_id] = {
        "title": brief.get("topic", "Unknown"),
        "thesis": brief.get("original_thesis_target", ""),
        "audience": brief.get("audience_tag", "PUBLIC"),
        "confidence": bpz.get("confidence_pct", 50),
        "word_count": word_count,
        "date": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "path": str(pdir),
        "sub_questions": brief.get("sub_questions", []),
    }

    # Detect links to existing reports
    new_edges = []
    for existing_id, existing_node in graph["nodes"].items():
        if existing_id == report_id:
            continue

        # Check if this report cites the other
        if existing_id in report_text:
            new_edges.append({
                "from": report_id,
                "to": existing_id,
                "type": "CITES",
                "auto": True,
            })

        # Check keyword overlap for potential EXTENDS
        existing_keywords = set(existing_node.get("title", "").lower().split())
        new_keywords = set(brief.get("topic", "").lower().split())
        overlap = existing_keywords & new_keywords - {"the", "a", "an", "and", "or", "for", "in", "of", "to", "with"}
        if len(overlap) >= 3:
            new_edges.append({
                "from": report_id,
                "to": existing_id,
                "type": "RELATED",
                "keywords": list(overlap),
                "auto": True,
            })

    # Add manual edge types (can be edited later)
    graph["edges"].extend(new_edges)
    save_graph(graph)

    print(f"Added {report_id}: {brief.get('topic', 'Unknown')}")
    print(f"  Word count: {word_count}")
    print(f"  New edges: {len(new_edges)}")
    for e in new_edges:
        print(f"    {e['from']} → {e['to']} ({e['type']})")


def show_graph():
    """Display the knowledge graph."""
    graph = load_graph()
    print(f"Knowledge Graph — {len(graph['nodes'])} reports, {len(graph['edges'])} edges")
    print(f"Updated: {graph.get('updated', 'never')}\n")

    for rid, node in sorted(graph["nodes"].items()):
        conf = node.get("confidence", "?")
        words = node.get("word_count", "?")
        print(f"  {rid}: {node['title']}")
        print(f"    Confidence: {conf}% | Words: {words} | Date: {node.get('date', '?')}")

        # Show edges
        for e in graph["edges"]:
            if e["from"] == rid:
                print(f"    → {e['type']} {e['to']}")
            elif e["to"] == rid:
                print(f"    ← {e['type']} {e['from']}")
        print()


def get_links(report_id: str):
    """Show all connections for a specific report."""
    graph = load_graph()
    node = graph["nodes"].get(report_id)
    if not node:
        print(f"Report {report_id} not found in graph")
        return

    print(f"{report_id}: {node['title']}")
    print(f"Thesis: {node.get('thesis', 'N/A')}\n")

    for e in graph["edges"]:
        if e["from"] == report_id:
            target = graph["nodes"].get(e["to"], {})
            print(f"  → {e['type']} {e['to']}: {target.get('title', '?')}")
        elif e["to"] == report_id:
            source = graph["nodes"].get(e["from"], {})
            print(f"  ← {e['type']} {e['from']}: {source.get('title', '?')}")


def generate_html():
    """Generate an HTML visualization of the knowledge graph."""
    graph = load_graph()
    nodes_js = json.dumps([
        {"id": rid, "label": rid, "title": n.get("title", ""),
         "confidence": n.get("confidence", 50)}
        for rid, n in graph["nodes"].items()
    ])
    edges_js = json.dumps([
        {"from": e["from"], "to": e["to"], "label": e["type"],
         "arrows": "to"}
        for e in graph["edges"]
    ])

    html = f"""<!DOCTYPE html>
<html><head>
<title>Ainary Knowledge Graph</title>
<script src="https://unpkg.com/vis-network/standalone/umd/vis-network.min.js"></script>
<style>
  body {{ font-family: Inter, sans-serif; margin: 0; background: #fafaf8; }}
  #graph {{ width: 100%; height: 80vh; border: 1px solid #e5e3dc; }}
  h1 {{ padding: 20px; color: #1a1a1a; font-size: 1.4rem; }}
  .info {{ padding: 0 20px; color: #666; font-size: 0.85rem; }}
</style>
</head><body>
<h1><span style="color:#c8aa50">●</span> Ainary Knowledge Graph</h1>
<p class="info">{len(graph['nodes'])} reports, {len(graph['edges'])} connections</p>
<div id="graph"></div>
<script>
var nodes = new vis.DataSet({nodes_js});
var edges = new vis.DataSet({edges_js});
var container = document.getElementById('graph');
var data = {{ nodes: nodes, edges: edges }};
var options = {{
  nodes: {{ shape: 'box', font: {{ size: 14 }}, color: {{ background: '#1a1a1a', font: {{ color: '#fff' }} }} }},
  edges: {{ font: {{ size: 11, color: '#888' }}, color: '#c8aa50' }},
  physics: {{ stabilization: true }}
}};
new vis.Network(container, data, options);
</script>
</body></html>"""

    out = WORKSPACE / "research" / "knowledge-graph.html"
    out.write_text(html)
    print(f"Graph HTML: {out}")


def inject_graph_context(report_id: str) -> str:
    """Generate context string for Opus about related reports. Used in synthesis prompt."""
    graph = load_graph()
    lines = []
    for e in graph["edges"]:
        if e["from"] == report_id or e["to"] == report_id:
            other_id = e["to"] if e["from"] == report_id else e["from"]
            other = graph["nodes"].get(other_id, {})
            lines.append(
                f"- {e['type']} {other_id}: \"{other.get('title', '?')}\" "
                f"(Confidence: {other.get('confidence', '?')}%, "
                f"Thesis: {other.get('thesis', 'N/A')[:200]})"
            )
    if not lines:
        return ""
    return "RELATED AINARY REPORTS (cite where relevant):\n" + "\n".join(lines)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: knowledge_graph.py [add|show|links|html] ...")
        sys.exit(1)

    cmd = sys.argv[1]
    if cmd == "add" and len(sys.argv) >= 4:
        add_report(sys.argv[2], sys.argv[3])
    elif cmd == "show":
        show_graph()
    elif cmd == "links" and len(sys.argv) >= 3:
        get_links(sys.argv[2])
    elif cmd == "html":
        generate_html()
    else:
        print("Usage: knowledge_graph.py [add|show|links|html] ...")
