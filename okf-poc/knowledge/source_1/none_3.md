---
id: none
type: concept
title: None
description: Step 2 kubectl sends request to API Server. Step 3
category: kubernetes
tags:
- none
- step
- kubectl
- sends
- request
source: null
created_at: '2026-08-06'
updated_at: '2026-08-06'
aliases: []
related: []
document_type: Kubernetes
trust_level: Medium
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
