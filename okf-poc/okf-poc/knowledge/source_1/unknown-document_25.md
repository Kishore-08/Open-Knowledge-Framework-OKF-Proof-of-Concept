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
Pod 
 | 
 v 
CNI Network 
 | 
 v 
Node 
 | 
 v 
Cluster Network 
 
Interview Answer 
Kubernetes provides a flat network where every pod has a unique routable IP and can 
communicate directly with other pods. 
 
18. How does Pod-to-Pod communication 
work? 
Answer 
Each pod receives an IP address from the CNI plugin. 
Example: 
