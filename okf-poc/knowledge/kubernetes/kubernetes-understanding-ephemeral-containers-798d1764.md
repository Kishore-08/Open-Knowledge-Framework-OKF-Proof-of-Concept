---
id: kubernetes-understanding-ephemeral-containers-798d1764
type: concept
title: Understanding ephemeral containers
description: '[Pods](https://kubernetes.io/docs/concepts/workloads/pods/ "A Pod represents
  a set of running containers in your cluster.") are the fundamental building'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/pods/ephemeral-containers/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Understanding ephemeral containers

[Pods](https://kubernetes.io/docs/concepts/workloads/pods/ "A Pod represents a set of running containers in your cluster.") are the fundamental building
block of Kubernetes applications. Since Pods are intended to be disposable and
replaceable, you cannot add a container to a Pod once it has been created.
Instead, you usually delete and replace Pods in a controlled fashion using
[deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/ "Manages a replicated application on your cluster.").

Sometimes it's necessary to inspect the state of an existing Pod, however, for
example to troubleshoot a hard-to-reproduce bug. In these cases you can run
an ephemeral container in an existing Pod to inspect its state and run
arbitrary commands.