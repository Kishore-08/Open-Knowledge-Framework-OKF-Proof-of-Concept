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
Zero-downtime upgrades rely on rolling upgrades with node draining, PDBs, and maintaining 
pod redundancy. 
 
50. How would you migrate workloads 
between Kubernetes clusters? 
Answer 
Approach 1: Blue-Green Migration 
Cluster A (old) 
Cluster B (new) 
Switch traffic gradually 
 
Step 1: Deploy workloads in new cluster 
Same manifests or GitOps sync. 
 
Step 2: Sync data 
●​ Databases replication 
●​ Persistent volume migration 
 
Step 3: Validate 
●​ Smoke tests 
●​ Load tests 
 
