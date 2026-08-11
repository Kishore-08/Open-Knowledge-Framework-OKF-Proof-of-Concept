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
None
None
None
default service account 
 
Use Case 
Pods accessing Kubernetes API: 
list pods 
create secrets 
 
Example 
serviceAccountName: my-app-sa 
 
Token Mounting 
Service account tokens are mounted inside pods: 
/var/run/secrets/kubernetes.io/serviceaccount 
 
Interview Answer 
Service accounts provide identity and API access for workloads inside the cluster. 
 
