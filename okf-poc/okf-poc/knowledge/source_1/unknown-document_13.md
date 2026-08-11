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
Running 
   | 
Succeeded/Failed 
 
9. What happens if a node running a pod 
crashes? 
Answer 
Node Controller detects failure. 
Default timeout: 
~40 seconds 
 
Node marked: 
NotReady 
 
Pods become unavailable. 
 
Controller notices missing replicas. 
Creates replacement pods on healthy nodes. 
 
Example: 
