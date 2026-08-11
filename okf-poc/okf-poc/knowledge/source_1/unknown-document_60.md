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
None
Check 
kubectl get events 
 
Interview Answer 
Missing replicas usually result from scheduling, image, or node-level issues. 
 
43. Service is not routing traffic to pods. 
Troubleshoot. 
Answer 
Step 1: Check Endpoints 
kubectl get endpoints 
If empty → selector issue. 
 
Step 2: Labels mismatch 
Service: 
app: frontend 
Pod: 
