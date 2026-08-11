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
17. Explain the Kubernetes Networking 
Model. 
Answer 
Kubernetes networking follows three core rules: 
Rule 1 
Every Pod gets its own IP. 
Pod A → 10.1.1.10 
Pod B → 10.1.1.11 
 
Rule 2 
Pods communicate directly without NAT. 
Pod A → Pod B 
using pod IP. 
 
Rule 3 
Nodes can communicate with all Pods. 
 
Architecture 
