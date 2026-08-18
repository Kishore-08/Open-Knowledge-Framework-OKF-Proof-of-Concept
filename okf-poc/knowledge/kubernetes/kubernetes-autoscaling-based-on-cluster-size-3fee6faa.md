---
id: kubernetes-autoscaling-based-on-cluster-size-3fee6faa
type: concept
title: Autoscaling based on cluster size
description: For workloads that need to be scaled based on the size of the cluster
  (for example
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/autoscaling/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Autoscaling based on cluster size

For workloads that need to be scaled based on the size of the cluster (for example
`cluster-dns` or other system components), you can use the
[*Cluster Proportional Autoscaler*](https://github.com/kubernetes-sigs/cluster-proportional-autoscaler).
Just like the VPA, it is not part of the Kubernetes core, but hosted as its
own project on GitHub.

The Cluster Proportional Autoscaler watches the number of schedulable [nodes](https://kubernetes.io/docs/concepts/architecture/nodes/ "A node is a worker machine in Kubernetes.")
and cores and scales the number of replicas of the target workload accordingly.

If the number of replicas should stay the same, you can scale your workloads vertically according to the cluster size using
the [*Cluster Proportional Vertical Autoscaler*](https://github.com/kubernetes-sigs/cluster-proportional-vertical-autoscaler).
The project is **currently in beta** and can be found on GitHub.

While the Cluster Proportional Autoscaler scales the number of replicas of a workload,
the Cluster Proportional Vertical Autoscaler adjusts the resource requests for a workload
(for example a Deployment or DaemonSet) based on the number of nodes and/or cores in the cluster.