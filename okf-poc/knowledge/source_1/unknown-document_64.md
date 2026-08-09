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
Step 1: Check limits 
resources: 
  limits: 
    memory: "512Mi" 
 
Step 2: Check usage 
kubectl top pod 
 
Step 3: Increase limits 
 
Step 4: Analyze memory leaks 
 
Step 5: JVM/GC tuning if applicable 
 
Interview Answer 
OOMKilled means container exceeded memory limits; fix involves tuning limits or application 
memory usage. 
 
47. Kubernetes API Server becomes slow. 
How do you troubleshoot? 
