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
app: front-end 
 
Step 3: DNS issues 
 
Step 4: Network Policies blocking traffic 
 
Interview Answer 
Most service issues are caused by selector mismatch or missing endpoints. 
 
44. Pods cannot resolve DNS. How do you 
debug? 
Answer 
Step 1 
Check CoreDNS: 
kubectl get pods -n kube-system 
 
Step 2 
Check resolv.conf inside pod: 
