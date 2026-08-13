---
id: kubernetes-taints-and-tolerations-b726f72e
type: concept
title: Taints and Tolerations
description: '[*Node affinity*](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#affinity-and-anti-affinity)'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

# Taints and Tolerations

[*Node affinity*](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#affinity-and-anti-affinity)
is a property of [Pods](https://kubernetes.io/docs/concepts/workloads/pods/ "A Pod represents a set of running containers in your cluster.") that *attracts* them to
a set of [nodes](https://kubernetes.io/docs/concepts/architecture/nodes/ "A node is a worker machine in Kubernetes.") (either as a preference or a
hard requirement). *Taints* are the opposite -- they allow a node to repel a set of pods.

*Tolerations* are applied to pods. Tolerations allow the scheduler to schedule pods with matching
taints. Tolerations allow scheduling but don't guarantee scheduling: the scheduler also
[evaluates other parameters](https://kubernetes.io/docs/concepts/scheduling-eviction/pod-priority-preemption/)
as part of its function.

Taints and tolerations work together to ensure that pods are not scheduled
onto inappropriate nodes. One or more taints are applied to a node; this
marks that the node should not accept any pods that do not tolerate the taints.