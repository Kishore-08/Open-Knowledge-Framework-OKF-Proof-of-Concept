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
Node1 Crash 
   | 
ReplicaSet 
   | 
New Pod on Node2 
 
Important 
Local data may be lost. 
Persistent volumes survive. 
 
10. How does Kubernetes handle 
self-healing? 
Answer 
Through controllers. 
Examples: 
Pod Crash 
kubelet restarts container. 
 
Node Failure 
ReplicaSet creates replacement Pod. 
 
Failed Deployment 
Rolling update rollback. 
