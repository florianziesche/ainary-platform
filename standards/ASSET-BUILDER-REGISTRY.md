# Asset Builder — Naming, Tags, Ontology (v1.0)

## ID format
AB-[topicslug]-[TYPE]-[0001]
TYPE: NOTE | PLAY | TMPL | ENT

## Topic slug rules
- lowercase
- hyphens
- max 4 words
Examples:
- prompt-engineering
- exec-research
- rfp-evaluation

## Canonical tags (examples)
- domain/prompt-engineering
- domain/exec-research
- asset/atomic-note
- asset/playbook
- asset/template
- risk/prompt-injection
- qa/traceability
- governance/tier-2
- governance/tier-3

## When to create an Entity
Create ENT records for:
- recurring concepts (e.g., “prompt injection”, “few-shot prompting”)
- tools/platforms (e.g., “ChatGPT Projects”)
- methods (e.g., “claim ledger”, “rubric review”)
- organizations/standards if central to the report

## Relation guidance
- supports: asset A provides justification or evidence for asset B
- depends_on: asset B requires asset A to work
- mitigates: asset A reduces risk described in asset B
- comparable_to: assets are alternatives or comparable approaches
- contradicts: explicit disagreement (carry caveats and implications)
