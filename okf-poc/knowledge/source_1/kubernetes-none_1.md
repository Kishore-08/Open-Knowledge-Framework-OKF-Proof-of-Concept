---
id: kubernetes-none
type: concept
title: None
description: Current replicas = 2 Stored in etcd. kube-scheduler
category: kubernetes
tags:
- none
- current
- replicas
- stored
- etcd
source: null
created_at: '2026-08-06'
updated_at: '2026-08-06'
aliases: []
related: []
document_type: Kubernetes
trust_level: Medium
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
