---
id: kubernetes-self-healing-capabilities-869e3f86
type: concept
title: Self-Healing capabilities
description: '- **Container-level restarts:** If a container inside a Pod fails, Kubernetes
  restarts it based on the [`restartPolicy`](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#restart-polic'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/architecture/self-healing/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

## Self-Healing capabilities

- **Container-level restarts:** If a container inside a Pod fails, Kubernetes restarts it based on the [`restartPolicy`](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#restart-policy).
- **Replica replacement:** If a Pod in a [Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) or [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/) fails, Kubernetes creates a replacement Pod to maintain the specified number of replicas.
  If a Pod that is part of a [DaemonSet](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/) fails, the control plane
  creates a replacement Pod to run on the same node.
- **Persistent storage recovery:** If a node is running a Pod with a PersistentVolume (PV) attached, and the node fails, Kubernetes can reattach the volume to a new Pod on a different node.
- **Load balancing for Services:** If a Pod behind a [Service](https://kubernetes.io/docs/concepts/services-networking/service/) fails, Kubernetes automatically removes it from the Service's endpoints to route traffic only to healthy Pods.

Here are some of the key components that provide Kubernetes self-healing:

- **[kubelet](https://kubernetes.io/docs/concepts/architecture/#kubelet):** Ensures that containers are running, and restarts those that fail.
- **Deployment (via ReplicaSet), ReplicaSet, StatefulSet and DaemonSet controllers:** Maintain the desired number of Pod replicas.
- **PersistentVolume controller:** Manages volume attachment and detachment for stateful workloads.