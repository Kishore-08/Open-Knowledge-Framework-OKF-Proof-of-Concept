---
id: none
type: concept
title: None
description: 'Shell Examples: ●​ Load Balancers'
category: kubernetes
tags:
- none
- shell
- examples
- load
- balancers
source: null
created_at: '2026-08-06'
updated_at: '2026-08-06'
aliases: []
related: []
document_type: Kubernetes
trust_level: Medium
---

None
Shell
Examples: 
●​ Load Balancers 
●​ Volumes 
●​ Node lifecycle 
 
Architecture Flow 
kubectl 
   | 
   v 
API Server 
   | 
   v 
etcd 
 
Scheduler 
   | 
Controller Manager 
   | 
Worker Nodes 
 
2. What happens internally when you run 
kubectl apply -f deployment.yaml? 
Answer 
Step 1 
User executes: 
kubectl apply -f deployment.yaml 
