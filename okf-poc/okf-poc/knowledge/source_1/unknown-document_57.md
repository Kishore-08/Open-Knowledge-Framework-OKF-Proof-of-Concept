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
Flow 
HPA → more pods 
Cluster Autoscaler → more nodes 
VPA → bigger pods 
 
Interview Answer 
HPA handles workload scaling, VPA handles resource tuning, cluster autoscaler handles 
infrastructure scaling. 
 
40. Why might HPA not scale correctly? 
Answer 
Common Reasons 
Metrics Not Available 
Missing metrics server. 
 
Wrong Requests Defined 
HPA depends on CPU requests. 
 
Insufficient Resources 
Cluster cannot schedule new pods. 
 
