---
id: unknown-document
type: concept
title: Unknown Document
description: Metadata extraction failed.
category: unknown
tags:
- unclassified
source: null
created_at: '2026-08-05'
updated_at: '2026-08-05'
aliases: []
related: []
document_type: Unknown
trust_level: Low
---

None
None
None
Pod Anti-Affinity 
Separate pods. 
Example: 
Replica1 -> Node1 
Replica2 -> Node2 
for HA. 
 
Interview Answer 
nodeSelector is simple; affinity and anti-affinity provide advanced placement control. 
 
13. How would you ensure two replicas 
never run on the same node? 
Answer 
Use Pod Anti-Affinity. 
Example: 
podAntiAffinity: 
  requiredDuringSchedulingIgnoredDuringExecution: 
 
Result: 
Replica1 -> Node1 
