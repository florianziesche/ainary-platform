# Asset Builder — RAG JSON Spec (v1.0)

## Overview
The Asset Builder outputs a JSON array. Each element is one of:
- asset
- entity
- relation

## Common fields (assets)
- id (string): AB-[topicslug]-[TYPE]-[0001]
- type (string): NOTE | PLAY | TMPL | ENT
- title (string)
- this_answers (string)
- tags (array of strings)
- classification (string): Evidenced | Derived | Operational
- confidence (string): High | Med | Low
- sources (array of objects): [{ "citation": "[1]", "url": "...", "access_date": "YYYY-MM-DD" }] OR []
- caveats (array of strings)

## Asset object
{
  "object": "asset",
  "id": "AB-prompt-engineering-NOTE-0007",
  "type": "NOTE|PLAY|TMPL",
  "title": "...",
  "this_answers": "...",
  "content_markdown": "...",
  "tags": ["..."],
  "classification": "Evidenced|Derived|Operational",
  "confidence": "High|Med|Low",
  "sources": [],
  "caveats": [],
  "relations": [{"type":"depends_on","target_id":"..."}]
}

## Entity object
{
  "object": "entity",
  "id": "AB-prompt-engineering-ENT-0001",
  "type": "ENT",
  "name": "...",
  "entity_kind": "concept|tool|org|person|method",
  "aliases": ["..."],
  "description": "...",
  "tags": ["..."]
}

## Relation object
{
  "object": "relation",
  "source_id": "...",
  "relation_type": "supports|contradicts|depends_on|comparable_to|example_of|implements|mitigates|risk_of",
  "target_id": "...",
  "evidence": [{"citation":"[1]"}],
  "notes": "optional"
}

## Validation rules (must satisfy)
- Every relation source_id and target_id must exist in the output.
- Every asset must have: id, type, title, this_answers, classification, confidence.
- classification ∈ {Evidenced, Derived, Operational}
- confidence ∈ {High, Med, Low}
- IDs must be unique within the output array.
