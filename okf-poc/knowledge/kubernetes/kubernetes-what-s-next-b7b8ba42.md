---
id: kubernetes-what-s-next-b7b8ba42
type: concept
title: What's next
description: '- Learn about [Pods](https://kubernetes.io/docs/concepts/workloads/pods/):'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

## What's next

- Learn about [Pods](https://kubernetes.io/docs/concepts/workloads/pods/):
  - Learn about [static Pods](https://kubernetes.io/docs/tasks/configure-pod-container/static-pod/), which are useful for running Kubernetes
    [control plane](https://kubernetes.io/docs/reference/glossary/?all=true#term-control-plane "The container orchestration layer that exposes the API and interfaces to define, deploy, and manage the lifecycle of containers.") components.
- Find out how to use DaemonSets:
  - [Perform a rolling update on a DaemonSet](https://kubernetes.io/docs/tasks/manage-daemon/update-daemon-set/).
  - [Perform a rollback on a DaemonSet](https://kubernetes.io/docs/tasks/manage-daemon/rollback-daemon-set/)
    (for example, if a roll out didn't work how you expected).
- Understand [how Kubernetes assigns Pods to Nodes](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/).
- Learn about [device plugins](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/) and
  [add ons](https://kubernetes.io/docs/concepts/cluster-administration/addons/), which often run as DaemonSets.
- `DaemonSet` is a top-level resource in the Kubernetes REST API.
  Read the
  [DaemonSet](https://kubernetes.io/docs/reference/kubernetes-api/apps/daemon-set-v1/)
  object definition to understand the API for daemon sets.