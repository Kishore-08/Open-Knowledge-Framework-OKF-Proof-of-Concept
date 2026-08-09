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

●​ GPU nodes 
 
3. Use of autoscaling 
●​ Cluster Autoscaler 
●​ HPA for pods 
 
4. Observability layer 
●​ Central monitoring using: 
○​ Prometheus 
○​ Thanos 
○​ Grafana 
 
Interview Answer 
At this scale, you must move to multi-cluster architecture with workload isolation, autoscaling, 
and centralized observability. 
 
49. How would you perform a Kubernetes 
cluster upgrade with zero downtime? 
Answer 
Strategy: Rolling Node Upgrade 
 
Step 1: Upgrade Control Plane First 
●​ API server 
●​ scheduler 
●​ controller manager 
●​ etcd (carefully) 
