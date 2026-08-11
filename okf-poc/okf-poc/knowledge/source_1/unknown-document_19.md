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
None
Replica2 -> Node2 
Replica3 -> Node3 
 
Alternative: 
Topology Spread Constraints 
 
Interview Answer 
Use required pod anti-affinity or topology spread constraints. 
 
14. Explain Taints and Tolerations. 
Answer 
Taints repel pods. 
 
Apply taint: 
kubectl taint nodes worker1 dedicated=db:NoSchedule 
Meaning: 
Do not schedule Pods here 
 
Pod must have matching toleration. 
