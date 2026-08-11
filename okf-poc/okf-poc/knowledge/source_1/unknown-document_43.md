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
None
None
Verify StorageClass. 
kubectl get storageclass 
 
Step 3 
Check available PVs. 
kubectl get pv 
 
Common Causes 
No Matching StorageClass 
PVC requests: 
premium 
StorageClass doesn't exist. 
 
Insufficient Capacity 
PVC: 
500Gi 
Available: 
