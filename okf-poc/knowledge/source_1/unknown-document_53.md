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

 
Interview Answer 
Pod Security enforces workload security policies at namespace level using admission controls. 
 
36. How would you secure a production 
Kubernetes cluster? 
Answer 
1. RBAC 
Least privilege access. 
 
2. Network Policies 
Restrict pod-to-pod communication. 
Example tools: 
●​ Calico 
●​ Cilium 
 
3. Secrets Encryption 
Encrypt etcd data. 
 
4. Image Security 
●​ Scan images 
●​ Use trusted registries 
 
