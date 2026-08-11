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
tolerations: 
- key: dedicated 
  operator: Equal 
  value: db 
 
Use Cases 
●​ Dedicated nodes 
●​ GPU nodes 
●​ Database nodes 
 
Interview Answer 
Taints protect nodes; tolerations allow selected workloads to use those nodes. 
 
15. Difference Between NoSchedule, 
PreferNoSchedule, and NoExecute. 
Answer 
NoSchedule 
New Pods blocked. 
Existing Pods stay. 
 
PreferNoSchedule 
Soft rule. 
Scheduler tries to avoid node. 
