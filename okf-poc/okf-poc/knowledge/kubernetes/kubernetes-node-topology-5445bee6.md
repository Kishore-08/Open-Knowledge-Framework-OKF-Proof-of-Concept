---
id: kubernetes-node-topology-5445bee6
type: concept
title: Node topology
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/architecture/nodes/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Node topology

FEATURE STATE:
`Kubernetes v1.27 [stable]`(enabled by default)

If you have enabled the `TopologyManager`
[feature gate](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/), then
the kubelet can use topology hints when making resource assignment decisions.
See [Control Topology Management Policies on a Node](https://kubernetes.io/docs/tasks/administer-cluster/topology-manager/)
for more information.