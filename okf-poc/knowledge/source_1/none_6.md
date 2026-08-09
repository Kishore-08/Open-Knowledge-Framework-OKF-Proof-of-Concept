---
id: none
type: concept
title: None
description: None None Senior Interview Answer
category: kubernetes
tags:
- none
- senior
- interview
- answer
- loss
source: null
created_at: '2026-08-06'
updated_at: '2026-08-06'
aliases: []
related: []
document_type: Kubernetes
trust_level: Medium
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
 
