---
id: kubernetes-1-configure-the-cri-implementation-on-nodes-3540e4aa
type: concept
title: 1. Configure the CRI implementation on nodes
description: The configurations available through RuntimeClass are Container Runtime
  Interface (CRI)
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/containers/runtime-class/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

### 1. Configure the CRI implementation on nodes

The configurations available through RuntimeClass are Container Runtime Interface (CRI)
implementation dependent. See the corresponding documentation ([below](https://kubernetes.io/docs/concepts/containers/runtime-class/#cri-configuration)) for your
CRI implementation for how to configure.

#### Note:

RuntimeClass assumes a homogeneous node configuration across the cluster by default (which means
that all nodes are configured the same way with respect to container runtimes). To support
heterogeneous node configurations, see [Scheduling](https://kubernetes.io/docs/concepts/containers/runtime-class/#scheduling) below.

The configurations have a corresponding `handler` name, referenced by the RuntimeClass. The
handler must be a valid [DNS label name](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#dns-label-names).