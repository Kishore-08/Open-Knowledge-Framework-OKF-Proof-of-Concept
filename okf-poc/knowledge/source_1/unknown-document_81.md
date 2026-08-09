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
 
60. Design a highly available Kubernetes 
platform for a global SaaS application 
Answer 
Architecture 
US Cluster 
EU Cluster 
APAC Cluster 
       | 
 Global Load Balancer 
 
Key Principles 
1. Multi-region clusters 
Each region is independent. 
 
2. Stateless application design 
State stored outside cluster. 
 
3. Global traffic routing 
●​ GeoDNS 
●​ Latency-based routing 
