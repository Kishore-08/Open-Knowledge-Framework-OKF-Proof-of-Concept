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
frontend = 10.1.1.10 
backend = 10.1.2.15 
Communication: 
frontend 
   | 
   v 
10.1.2.15 
 
Same Node 
Traffic stays local. 
 
Different Nodes 
Traffic flows through the cluster network managed by the CNI. 
 
Common Components 
●​ Overlay Network 
●​ Routing Tables 
●​ VXLAN/BGP (depending on CNI) 
 
Interview Answer 
Pod communication is enabled through the CNI layer which creates a flat, routable network 
across all cluster nodes. 
