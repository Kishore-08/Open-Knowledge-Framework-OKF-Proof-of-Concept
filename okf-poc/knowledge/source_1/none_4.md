---
id: none
type: concept
title: None
description: Desired Pods = 3 Current Pods = 0 Creates Pods.
category: kubernetes
tags:
- none
- desired
- pods
- current
- creates
source: null
created_at: '2026-08-06'
updated_at: '2026-08-06'
aliases: []
related: []
document_type: Kubernetes
trust_level: Medium
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
