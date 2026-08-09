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
