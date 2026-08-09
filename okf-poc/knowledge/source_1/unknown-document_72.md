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
Key Components 
●​ Geo DNS routing 
●​ Global load balancing 
●​ Replicated clusters 
 
Data Layer 
●​ Active-active or active-passive databases 
●​ Replication across regions 
 
Observability 
Centralized via: 
●​ Thanos 
 
Failover Strategy 
If region A fails: 
Traffic → Region B 
 
Interview Answer 
Multi-region Kubernetes requires independent clusters per region with global traffic routing and 
replicated data. 
 
52. How do you monitor Kubernetes? 
Answer 
