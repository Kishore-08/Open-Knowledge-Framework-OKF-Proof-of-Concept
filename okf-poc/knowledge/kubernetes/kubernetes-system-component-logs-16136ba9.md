---
id: kubernetes-system-component-logs-16136ba9
type: concept
title: System component logs
description: 'There are two types of system components: those that typically run in
  a container,'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/logging/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

## System component logs

There are two types of system components: those that typically run in a container,
and those components directly involved in running containers. For example:

- The kubelet and container runtime do not run in containers. The kubelet runs
  your containers (grouped together in [pods](https://kubernetes.io/docs/concepts/workloads/pods/ "A Pod represents a set of running containers in your cluster."))
- The Kubernetes scheduler, controller manager, and API server run within pods
  (usually [static Pods](https://kubernetes.io/docs/tasks/configure-pod-container/static-pod/ "A pod managed directly by the kubelet daemon on a specific node.")).
  The etcd component runs in the control plane, and most commonly also as a static pod.
  If your cluster uses kube-proxy, you typically run this as a `DaemonSet`.