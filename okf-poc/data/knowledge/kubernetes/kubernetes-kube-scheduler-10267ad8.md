---
id: kubernetes-kube-scheduler-10267ad8
type: concept
title: kube-scheduler
description: Control plane component that watches for newly created
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/architecture/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### kube-scheduler

Control plane component that watches for newly created
[Pods](https://kubernetes.io/docs/concepts/workloads/pods/ "A Pod represents a set of running containers in your cluster.") with no assigned
[node](https://kubernetes.io/docs/concepts/architecture/nodes/ "A node is a worker machine in Kubernetes."), and selects a node for them
to run on.

Factors taken into account for scheduling decisions include:
individual and collective [resource](https://kubernetes.io/docs/reference/glossary/?all=true#term-infrastructure-resource "A defined amount of infrastructure available for consumption (CPU, memory, etc).")
requirements, hardware/software/policy constraints, affinity and anti-affinity specifications,
data locality, inter-workload interference, and deadlines.