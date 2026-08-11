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
 
Senior Interview Answer 
Loss of etcd means loss of cluster state. 
 
4. Explain the Reconciliation Loop. 
Answer 
Kubernetes continuously compares: 
Desired State 
vs 
Actual State 
 
Example: 
Deployment: 
replicas: 5 
Current: 
Only 4 Pods running 
 
Deployment Controller detects mismatch. 
Creates 1 additional Pod. 
 
