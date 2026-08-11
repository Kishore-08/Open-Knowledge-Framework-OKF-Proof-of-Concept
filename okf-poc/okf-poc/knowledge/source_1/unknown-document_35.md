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
None
Answer 
Step 1 
Verify service exists. 
kubectl get svc 
 
Step 2 
Check endpoints. 
kubectl get endpoints 
Empty endpoints often indicate selector mismatch. 
 
Step 3 
Verify labels. 
Service: 
selector: 
  app: payment 
Pod: 
app: payments 
Mismatch causes failures. 
