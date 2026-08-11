---
id: kubernetes-pod-lifetime-3e34f258
type: concept
title: Pod lifetime
description: While a Pod is running, the kubelet is able to restart containers to
  handle
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Pod lifetime

While a Pod is running, the kubelet is able to restart containers to handle
some kind of faults. Within a Pod, Kubernetes tracks different container
[states](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#container-states) and determines what action to take to make the Pod
healthy again. This is done in a [polling
loop](https://kubernetes.io/docs/reference/node/kubelet-sync-loop/) that periodically reconciles the
desired state (a Pod spec) with the actual state of the running containers.

In the Kubernetes API, Pods have both a specification and an actual status. The
status for a Pod object consists of a set of [Pod conditions](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-conditions).
You can also inject [custom readiness information](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-readiness-gate) into the
condition data for a Pod, if that is useful to your application.

Pods are only [scheduled](https://kubernetes.io/docs/concepts/scheduling-eviction/) once in their lifetime;
assigning a Pod to a specific node is called *binding*, and the process of selecting
which node to use is called *scheduling*.
Once a Pod has been scheduled and is bound to a node, Kubernetes tries
to run that Pod on the node. The Pod runs on that node until it stops, or until the Pod
is [terminated](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-termination); if Kubernetes isn't able to start the Pod on the selected
node (for example, if the node crashes before the Pod starts), then that particular Pod
never starts.

You can use [Pod Scheduling Readiness](https://kubernetes.io/docs/concepts/scheduling-eviction/pod-scheduling-readiness/)
to delay scheduling for a Pod until all its *scheduling gates* are removed. For example,
you might want to define a set of Pods but only trigger scheduling once all the Pods
have been created.