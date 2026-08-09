---
id: kubernetes-resource-capacity-tracking-5445bee6
type: concept
title: Resource capacity tracking
description: 'Node objects track information about the Node''s resource capacity:
  for example, the amount'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/architecture/nodes/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Resource capacity tracking

Node objects track information about the Node's resource capacity: for example, the amount
of memory available and the number of CPUs.
Nodes that [self register](https://kubernetes.io/docs/concepts/architecture/nodes/#self-registration-of-nodes) report their capacity during
registration. If you [manually](https://kubernetes.io/docs/concepts/architecture/nodes/#manual-node-administration) add a Node, then
you need to set the node's capacity information when you add it.

The Kubernetes [scheduler](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-scheduler/ "Control plane component that watches for newly created pods with no assigned node, and selects a node for them to run on.") ensures that
there are enough resources for all the Pods on a Node. The scheduler checks that the sum
of the requests of containers on the node is no greater than the node's capacity.
That sum of requests includes all containers managed by the kubelet, but excludes any
containers started directly by the container runtime, and also excludes any
processes running outside of the kubelet's control.

#### Note:

If you want to explicitly reserve resources for non-Pod processes, see
[reserve resources for system daemons](https://kubernetes.io/docs/tasks/administer-cluster/reserve-compute-resources/#system-reserved).