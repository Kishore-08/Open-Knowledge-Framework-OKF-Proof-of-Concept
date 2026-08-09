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
 
Step 2 
kubectl sends request to API Server. 
 
Step 3 
API Server: 
●​ Authenticates 
●​ Authorizes 
●​ Validates YAML 
 
Step 4 
Object stored in etcd. 
Example: 
Deployment: 
replicas = 3 
image = nginx 
 
Step 5 
Deployment Controller detects new Deployment. 
Creates ReplicaSet. 
 
Step 6 
ReplicaSet Controller notices: 
