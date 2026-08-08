---
id: kubernetes-container-probes-6ed556c1
type: concept
title: Container probes
description: A *probe* is a diagnostic performed periodically by the kubelet on a
  container.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/pods/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Container probes

A *probe* is a diagnostic performed periodically by the kubelet on a container.
To perform a diagnostic, the kubelet can invoke different actions:

- `ExecAction` (performed with the help of the container runtime)
- `TCPSocketAction` (checked directly by the kubelet)
- `HTTPGetAction` (checked directly by the kubelet)

You can read more about [probes](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#container-probes)
in the Pod Lifecycle documentation.