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
 
Step 2: kubelet status 
systemctl status kubelet 
 
Step 3: Check resources 
●​ Disk full 
●​ Memory pressure 
●​ CPU pressure 
 
Step 4: Network issues 
Node cannot reach API server. 
 
Effects 
Pods evicted after timeout. 
 
Interview Answer 
Node NotReady is usually caused by kubelet failure, resource exhaustion, or network issues. 
 
46. Pods frequently OOMKilled. What is 
your approach? 
Answer 
