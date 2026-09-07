---
id: kubernetes-scheduling-3540e4aa
type: concept
title: Scheduling
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/containers/runtime-class/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

## Scheduling

FEATURE STATE:
`Kubernetes v1.16 [beta]`

By specifying the `scheduling` field for a RuntimeClass, you can set constraints to
ensure that Pods running with this RuntimeClass are scheduled to nodes that support it.
If `scheduling` is not set, this RuntimeClass is assumed to be supported by all nodes.

To ensure pods land on nodes supporting a specific RuntimeClass, that set of nodes should have a
common label which is then selected by the `runtimeclass.scheduling.nodeSelector` field. The
RuntimeClass's nodeSelector is merged with the pod's nodeSelector in admission, effectively taking
the intersection of the set of nodes selected by each. If there is a conflict, the pod will be
rejected.

If the supported nodes are tainted to prevent other RuntimeClass pods from running on the node, you
can add `tolerations` to the RuntimeClass. As with the `nodeSelector`, the tolerations are merged
with the pod's tolerations in admission, effectively taking the union of the set of nodes tolerated
by each.

To learn more about configuring the node selector and tolerations, see
[Assigning Pods to Nodes](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/).