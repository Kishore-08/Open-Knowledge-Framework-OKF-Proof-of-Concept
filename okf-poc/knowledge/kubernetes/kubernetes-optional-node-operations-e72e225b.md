---
id: kubernetes-optional-node-operations-e72e225b
type: concept
title: Optional node operations
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/resource-management/dynamic-resource-allocation/dra-features/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

## Optional node operations

FEATURE STATE:
`Kubernetes v1.37 [alpha]`(disabled by default)

In Dynamic Resource Allocation (DRA), the `kubelet` coordinates with a node-local
driver via gRPC to prepare allocated devices before container start
(`NodePrepareResources`) and to unprepare them upon Pod termination
(`NodeUnprepareResources`). While this setup is critical for node-local hardware
such as GPUs or FPGAs, some resources are managed entirely in the control plane
and require no node-local setup.

The optional node operations feature allows resource drivers to declare that
specific node-local gRPC operations can be skipped. When configured, the `kubelet`
bypasses driver lookup and gRPC calls for those devices, eliminating the need to
deploy and maintain empty node-local drivers on every worker node.