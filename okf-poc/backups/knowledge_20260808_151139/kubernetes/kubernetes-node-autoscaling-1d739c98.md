---
id: kubernetes-node-autoscaling-1d739c98
type: concept
title: Node Autoscaling
description: Automatically provision and consolidate the Nodes in your cluster to
  adapt to demand and optimize cost.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/node-autoscaling/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

# Node Autoscaling

Automatically provision and consolidate the Nodes in your cluster to adapt to demand and optimize cost.

In order to run workloads in your cluster, you need
[Nodes](https://kubernetes.io/docs/concepts/architecture/nodes/ "A node is a worker machine in Kubernetes."). Nodes in your cluster can be *autoscaled* -
dynamically [*provisioned*](https://kubernetes.io/docs/concepts/cluster-administration/node-autoscaling/#provisioning), or [*consolidated*](https://kubernetes.io/docs/concepts/cluster-administration/node-autoscaling/#consolidation) to provide needed
capacity while optimizing cost. Autoscaling is performed by Node [*autoscalers*](https://kubernetes.io/docs/concepts/cluster-administration/node-autoscaling/#autoscalers).