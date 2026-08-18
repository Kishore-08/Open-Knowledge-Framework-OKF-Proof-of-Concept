---
id: kubernetes-the-api-1ee2fe16
type: concept
title: The API
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/containers/cri/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## The API

FEATURE STATE:
`Kubernetes v1.23 [stable]`

The kubelet acts as a client when connecting to the container runtime via gRPC.
The runtime and image service endpoints have to be available in the container
runtime, which can be configured separately within the kubelet by using the
`--container-runtime-endpoint`
[command line flag](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/).

For Kubernetes v1.26 and later, the kubelet requires that the container runtime
supports the `v1` CRI API. If a container runtime does not support the `v1` API,
the kubelet will not register the node.