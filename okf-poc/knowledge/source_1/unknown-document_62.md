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
Shell
cat /etc/resolv.conf 
 
Step 3 
Test DNS: 
nslookup kubernetes.default 
 
Common Issues 
●​ CoreDNS crash 
●​ Network policy blocking DNS 
●​ Misconfigured cluster DNS 
 
Interview Answer 
DNS issues usually originate from CoreDNS or network policies. 
 
45. Node becomes NotReady. What do you 
check? 
Answer 
Step 1: Node status 
kubectl describe node 
