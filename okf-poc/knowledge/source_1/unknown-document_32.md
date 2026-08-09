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
22. Explain Ingress. When would you use 
it? 
Answer 
Ingress provides HTTP/HTTPS routing into the cluster. 
Without Ingress: 
Service A -> LoadBalancer 
Service B -> LoadBalancer 
Service C -> LoadBalancer 
Many load balancers. 
 
With Ingress: 
Internet 
    | 
Ingress Controller 
    | 
+------------+ 
| /api       | 
| /web       | 
| /admin     | 
+------------+ 
