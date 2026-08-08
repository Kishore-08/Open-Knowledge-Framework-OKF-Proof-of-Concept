---
id: kubernetes-why-volumes-are-important-4142258a
type: concept
title: Why volumes are important
description: '- **Data persistence:** On-disk files in a container are ephemeral,
  which presents some problems for'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/storage/volumes/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Why volumes are important

- **Data persistence:** On-disk files in a container are ephemeral, which presents some problems for
  non-trivial applications when running in containers. One problem occurs when
  a container crashes or is stopped; the container state is not saved, so all of the
  files that were created or modified during the lifetime of the container are lost.
  After a crash, kubelet restarts the container with a clean state.
- **Shared storage:** Another problem occurs when multiple containers are running in a `Pod` and
  need to share files. It can be challenging to set up
  and access a shared filesystem across all of the containers.

The Kubernetes [volume](https://kubernetes.io/docs/concepts/storage/volumes/ "A directory containing data, accessible to the containers in a pod.") abstraction
can help you to solve both of these problems.

Before you learn about volumes, PersistentVolumes, and PersistentVolumeClaims, you should read up
about [Pods](https://kubernetes.io/docs/concepts/workloads/pods/ "A Pod represents a set of running containers in your cluster.") and make sure that you understand how
Kubernetes uses Pods to run containers.