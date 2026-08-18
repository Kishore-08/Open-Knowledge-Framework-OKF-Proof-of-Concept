---
id: kubernetes-list-streaming-1ee2fe16
type: concept
title: List streaming
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/containers/cri/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## List streaming

FEATURE STATE:
`Kubernetes v1.36 [alpha]`(disabled by default)

The standard CRI list RPCs (`ListContainers`, `ListPodSandbox`, `ListImages`) return
all results in a single unary response. On nodes with a large number of containers
(for example, more than roughly 10,000 including both running and stopped), these
responses can exceed gRPC's default 16 MiB message size limit, causing the kubelet
to fail when reconciling state with the container runtime.

With the `CRIListStreaming` feature gate enabled, the kubelet uses server-side
streaming RPCs (such as `StreamContainers`, `StreamPodSandboxes`,
`StreamImages`) that allow the container runtime to divide results across
multiple response messages, bypassing the per-message size limit. This is
particularly useful for:

- High container churn environments (CI/CD systems)
- Large-scale batch processing workloads

If the container runtime does not support streaming RPCs, the kubelet
automatically falls back to the standard unary RPCs for backward
compatibility.

## What's next

- Learn more about the CRI [protocol definition](https://github.com/kubernetes/cri-api/blob/v0.33.1/pkg/apis/runtime/v1/api.proto)