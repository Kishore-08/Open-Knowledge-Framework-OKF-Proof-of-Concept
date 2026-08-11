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
 
Types 
Mutating 
Modify requests. 
Example: 
●​ Inject sidecars 
 
Validating 
Reject invalid requests. 
Example: 
●​ Block privileged containers 
 
Flow 
kubectl → API Server → Admission Controller → etcd 
 
Interview Answer 
Admission controllers enforce policies and modify requests before they are stored. 
 
58. Difference between Helm, Kustomize, 
Argo CD 
Answer 
