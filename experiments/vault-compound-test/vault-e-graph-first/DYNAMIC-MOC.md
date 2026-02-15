---
type: navigation
status: active
confidence: high
source: [system]
created: 2026-02-14
modified: 2026-02-15
tags: [moc, dynamic]
---
# Dynamic Map of Content

## All Claims
```dataview
TABLE confidence, source
FROM #claim
SORT file.name ASC
```

## All Concepts
```dataview
TABLE confidence, source
FROM #concept
SORT file.name ASC
```

## All Insights
```dataview
TABLE confidence, source
FROM #insight
SORT file.name ASC
```

## All Decisions
```dataview
TABLE confidence, status
FROM #decision
SORT file.name ASC
```

## Most Connected Notes
```dataview
TABLE length(file.outlinks) as "Outgoing Links", length(file.inlinks) as "Incoming Links"
SORT length(file.outlinks) + length(file.inlinks) DESC
LIMIT 10
```

## Connection Suggestions
Notes with fewer than 5 links that might benefit from more connections:
```dataview
TABLE length(file.outlinks) as "Links"
WHERE length(file.outlinks) < 5
SORT length(file.outlinks) ASC
```
