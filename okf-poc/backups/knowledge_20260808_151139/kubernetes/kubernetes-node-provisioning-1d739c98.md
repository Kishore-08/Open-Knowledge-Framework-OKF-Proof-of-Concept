---
id: kubernetes-node-provisioning-1d739c98
type: concept
title: Node provisioning
description: If there are Pods in a cluster that can't be scheduled on existing Nodes,
  new Nodes can be
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/node-autoscaling/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Node provisioning

If there are Pods in a cluster that can't be scheduled on existing Nodes, new Nodes can be
automatically added to the cluster—*provisioned*—to accommodate the Pods. This is
especially useful if the number of Pods changes over time, for example as a result of
[combining horizontal workload with Node autoscaling](https://kubernetes.io/docs/concepts/cluster-administration/node-autoscaling/#horizontal-workload-autoscaling).

Autoscalers provision the Nodes by creating and deleting cloud provider resources backing them. Most
commonly, the resources backing the Nodes are Virtual Machines.

The main goal of provisioning is to make all Pods schedulable. This goal is not always attainable
because of various limitations, including reaching configured provisioning limits, provisioning
configuration not being compatible with a particular set of pods, or the lack of cloud provider
capacity. While provisioning, Node autoscalers often try to achieve additional goals (for example
minimizing the cost of the provisioned Nodes or balancing the number of Nodes between failure
domains).

There are two main inputs to a Node autoscaler when determining Nodes to
provision—[Pod scheduling constraints](https://kubernetes.io/docs/concepts/cluster-administration/node-autoscaling/#provisioning-pod-constraints),
and [Node constraints imposed by autoscaler configuration](https://kubernetes.io/docs/concepts/cluster-administration/node-autoscaling/#provisioning-node-constraints).

Autoscaler configuration may also include other Node provisioning triggers (for example the number
of Nodes falling below a configured minimum limit).

#### Note:

Provisioning was formerly known as *scale-up* in Cluster Autoscaler.