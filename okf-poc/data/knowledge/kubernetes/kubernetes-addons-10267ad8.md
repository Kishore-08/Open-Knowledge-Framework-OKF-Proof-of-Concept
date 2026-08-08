---
id: kubernetes-addons-10267ad8
type: concept
title: Addons
description: Addons use Kubernetes resources ([DaemonSet](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset
  "Ensures a copy of a Pod is running across a set of nodes in a cluster."),
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/architecture/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Addons

Addons use Kubernetes resources ([DaemonSet](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset "Ensures a copy of a Pod is running across a set of nodes in a cluster."),
[Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/ "Manages a replicated application on your cluster."), etc) to implement cluster features.
Because these are providing cluster-level features, namespaced resources for
addons belong within the `kube-system` namespace.

Selected addons are described below; for an extended list of available addons,
please see [Addons](https://kubernetes.io/docs/concepts/cluster-administration/addons/).