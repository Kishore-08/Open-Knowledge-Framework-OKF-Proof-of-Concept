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
Shell
 
Node Affinity Issues 
Example: 
nodeSelector: 
  env: production 
No node matches. 
 
PVC Pending 
kubectl get pvc 
If storage isn't available, pod remains pending. 
 
Image Pull Secrets / Scheduling Constraints 
Affinity or anti-affinity may prevent scheduling. 
 
Senior Interview Answer 
Always start with: 
kubectl describe pod 
Most Pending issues are scheduling, resource, affinity, taint, or storage related. 
 
