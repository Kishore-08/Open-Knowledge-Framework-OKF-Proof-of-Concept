---
id: kubernetes-vertical-workload-autoscaling-1d739c98
type: concept
title: Vertical workload autoscaling
description: When using Node autoscaling, it's important to set Pod resource requests
  correctly. If the requests
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/node-autoscaling/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Vertical workload autoscaling

When using Node autoscaling, it's important to set Pod resource requests correctly. If the requests
of a given Pod are too low, provisioning a new Node for it might not help the Pod actually run.
If the requests of a given Pod are too high, it might incorrectly prevent consolidating its Node.

[Vertical workload autoscaling](https://kubernetes.io/docs/concepts/workloads/autoscaling/#scaling-workloads-vertically)
automatically adjusts the resource requests of your Pods based on their historical resource usage.

You can use Node autoscaling together with vertical workload autoscaling in order to adjust the
resource requests of your Pods while preserving Node autoscaling capabilities in your cluster.

#### Caution:

When using Node autoscaling, it's not recommended to set up vertical workload autoscaling for
DaemonSet Pods. Autoscalers have to predict what DaemonSet Pods on a new Node will look like in
order to predict available Node resources. Vertical workload autoscaling might make these
predictions unreliable, leading to incorrect scaling decisions.

## Related components

This section describes components providing functionality related to Node autoscaling.