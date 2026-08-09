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
Current replicas = 2 
Stored in etcd. 
 
kube-scheduler 
Responsible for pod placement. 
Determines: 
Which node should run the pod? 
Considers: 
●​ CPU 
●​ Memory 
●​ Affinity rules 
●​ Taints/Tolerations 
●​ Resource requests 
 
kube-controller-manager 
Runs controllers: 
●​ Deployment Controller 
●​ ReplicaSet Controller 
●​ Job Controller 
●​ Node Controller 
Ensures actual state matches desired state. 
 
cloud-controller-manager 
Integrates Kubernetes with cloud providers. 
