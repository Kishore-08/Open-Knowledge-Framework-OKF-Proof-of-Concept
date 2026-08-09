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
1. Explain the Kubernetes Control Plane 
Architecture. 
Answer 
The Control Plane manages the entire Kubernetes cluster. 
Components 
kube-apiserver 
The central entry point. 
Responsibilities: 
●​ Accepts API requests 
●​ Validates requests 
●​ Updates etcd 
●​ Serves cluster state 
 
etcd 
Distributed key-value store. 
Stores: 
●​ Pods 
●​ Deployments 
●​ Services 
●​ Secrets 
●​ ConfigMaps 
●​ Cluster state 
Example: 
Desired replicas = 3 
