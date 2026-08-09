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
Desired Pods = 3 
Current Pods = 0 
Creates Pods. 
 
Step 7 
Scheduler detects unscheduled Pods. 
Chooses nodes. 
 
Step 8 
kubelet on selected nodes starts containers. 
 
Step 9 
Pod becomes Running. 
 
Interview Gold Answer 
The entire process is driven by reconciliation loops and controllers. 
 
3. Why is etcd critical in Kubernetes? 
Answer 
etcd is the source of truth. 
Everything in Kubernetes is stored in etcd. 
