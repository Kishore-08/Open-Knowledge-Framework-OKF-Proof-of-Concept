---
id: kubernetes-scaling-a-replicaset-375b8ad3
type: concept
title: Scaling a ReplicaSet
description: A ReplicaSet can be easily scaled up or down by simply updating the `.spec.replicas`
  field. The ReplicaSet controller
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Scaling a ReplicaSet

A ReplicaSet can be easily scaled up or down by simply updating the `.spec.replicas` field. The ReplicaSet controller
ensures that a desired number of Pods with a matching label selector are available and operational.

When scaling down, the ReplicaSet controller chooses which pods to delete by sorting the available pods to
prioritize scaling down pods based on the following general algorithm:

1. Pending (and unschedulable) pods are scaled down first
2. If `controller.kubernetes.io/pod-deletion-cost` annotation is set, then
   the pod with the lower value will come first.
3. Pods on nodes with more replicas come before pods on nodes with fewer replicas.
4. If the pods' creation times differ, the pod that was created more recently
   comes before the older pod (the creation times are bucketed on an integer log scale).

If all of the above match, then selection is random.