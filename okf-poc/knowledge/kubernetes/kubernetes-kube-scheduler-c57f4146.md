---
id: kubernetes-kube-scheduler-c57f4146
type: concept
title: kube-scheduler
description: '[kube-scheduler](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-scheduler/)'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/scheduling-eviction/kube-scheduler/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## kube-scheduler

[kube-scheduler](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-scheduler/)
is the default scheduler for Kubernetes and runs as part of the
[control plane](https://kubernetes.io/docs/reference/glossary/?all=true#term-control-plane "The container orchestration layer that exposes the API and interfaces to define, deploy, and manage the lifecycle of containers.").
kube-scheduler is designed so that, if you want and need to, you can
write your own scheduling component and use that instead.

Kube-scheduler selects an optimal node to run newly created or not yet
scheduled (unscheduled) pods. Since containers in pods - and pods themselves -
can have different requirements, the scheduler filters out any nodes that
don't meet a Pod's specific scheduling needs. Alternatively, the API lets
you specify a node for a Pod when you create it, but this is unusual
and is only done in special cases.

In a cluster, Nodes that meet the scheduling requirements for a Pod
are called *feasible* nodes. If none of the nodes are suitable, the pod
remains unscheduled until the scheduler is able to place it.

The scheduler finds feasible Nodes for a Pod and then runs a set of
functions to score the feasible Nodes and picks a Node with the highest
score among the feasible ones to run the Pod. The scheduler then notifies
the API server about this decision in a process called *binding*.

Factors that need to be taken into account for scheduling decisions include
individual and collective resource requirements, hardware / software /
policy constraints, affinity and anti-affinity specifications, data
locality, inter-workload interference, and so on.