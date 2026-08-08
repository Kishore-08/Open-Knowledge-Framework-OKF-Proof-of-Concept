---
id: kubernetes-pod-scheduling-constraints-1d739c98
type: concept
title: Pod scheduling constraints
description: Pods can express [scheduling constraints](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/)
  to
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/node-autoscaling/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Pod scheduling constraints

Pods can express [scheduling constraints](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/) to
impose limitations on the kind of Nodes they can be scheduled on. Node autoscalers take these
constraints into account to ensure that the pending Pods can be scheduled on the provisioned Nodes.

The most common kind of scheduling constraints are the resource requests specified by Pod
containers. Autoscalers will make sure that the provisioned Nodes have enough resources to satisfy
the requests. However, they don't directly take into account the real resource usage of the Pods
after they start running. In order to autoscale Nodes based on actual workload resource usage, you
can combine [horizontal workload autoscaling](https://kubernetes.io/docs/concepts/cluster-administration/node-autoscaling/#horizontal-workload-autoscaling) with Node
autoscaling.

Other common Pod scheduling constraints include
[Node affinity](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#node-affinity),
[inter-Pod affinity](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#inter-pod-affinity-and-anti-affinity),
or a requirement for a particular [storage volume](https://kubernetes.io/docs/concepts/storage/volumes/).