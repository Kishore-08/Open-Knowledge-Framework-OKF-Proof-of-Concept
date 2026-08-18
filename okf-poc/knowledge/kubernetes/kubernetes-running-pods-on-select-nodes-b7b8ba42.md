---
id: kubernetes-running-pods-on-select-nodes-b7b8ba42
type: concept
title: Running Pods on select Nodes
description: If you specify a `.spec.template.spec.nodeSelector`, then the DaemonSet
  controller will
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Running Pods on select Nodes

If you specify a `.spec.template.spec.nodeSelector`, then the DaemonSet controller will
create Pods on nodes which match that [node selector](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/).
Likewise if you specify a `.spec.template.spec.affinity`,
then DaemonSet controller will create Pods on nodes which match that
[node affinity](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/).
If you do not specify either, then the DaemonSet controller will create Pods on all nodes.