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
 
Interview Answer 
Use PVs for production workloads requiring durable storage. 
 
27. How does dynamic volume 
provisioning work? 
Answer 
Without dynamic provisioning: 
Admin creates PV manually. 
 
With dynamic provisioning: 
Application creates PVC. 
StorageClass automatically provisions storage. 
 
Flow: 
PVC 
  | 
StorageClass 
  | 
Cloud Provider 
  | 
