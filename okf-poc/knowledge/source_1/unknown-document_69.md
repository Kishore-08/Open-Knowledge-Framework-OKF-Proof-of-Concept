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
Shell
 
Step 2: Upgrade Worker Nodes Gradually 
Use: 
kubectl drain node-1 
 
Step 3: Update kubelet and kube-proxy 
 
Step 4: Uncordon node 
kubectl uncordon node-1 
 
Step 5: Repeat for all nodes 
 
Key Principle 
Never upgrade everything at once. 
 
Zero Downtime Requirements 
●​ Pod replicas > 1 
●​ PodDisruptionBudgets (PDBs) 
●​ Load balancers in place 
 
Interview Answer 
