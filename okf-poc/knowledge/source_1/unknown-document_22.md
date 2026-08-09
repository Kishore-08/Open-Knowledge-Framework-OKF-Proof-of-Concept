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

Shell
None
Shell
None
Answer 
A Pending pod means Kubernetes accepted the pod but could not start it. 
Step 1: Describe the Pod 
kubectl describe pod <pod-name> 
Look at the Events section first. 
 
Common Causes 
Insufficient Resources 
0/10 nodes available: 
Insufficient CPU 
Insufficient Memory 
Check: 
kubectl top nodes 
 
Taints 
Node has: 
dedicated=db:NoSchedule 
Pod lacks toleration. 
