---
id: kubernetes-upgrading-1ee2fe16
type: concept
title: Upgrading
description: When upgrading the Kubernetes version on a node, the kubelet restarts.
  If the
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/containers/cri/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

## Upgrading

When upgrading the Kubernetes version on a node, the kubelet restarts. If the
container runtime does not support the `v1` CRI API, the kubelet will fail to
register and report an error. If a gRPC re-dial is required because the container
runtime has been upgraded, the runtime must support the `v1` CRI API for the
connection to succeed. This might require a restart of the kubelet after the
container runtime is correctly configured.