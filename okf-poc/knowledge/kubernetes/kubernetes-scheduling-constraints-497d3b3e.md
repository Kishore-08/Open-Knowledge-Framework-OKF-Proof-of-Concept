---
id: kubernetes-scheduling-constraints-497d3b3e
type: concept
title: Scheduling constraints
description: The scheduling constraints block carries the topology constraints documented
  in
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/workload-api/workloadbuilder/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Scheduling constraints

The scheduling constraints block carries the topology constraints documented in
[Topology-aware workload scheduling](https://kubernetes.io/docs/concepts/workloads/workload-api/topology-aware-scheduling/):
a node label key naming the domain (such as a rack or a zone) that every Pod in the group
must share, with at most one topology constraint per group. Controllers should freeze the
field after creation, since constraints are immutable in the compiled Workload.