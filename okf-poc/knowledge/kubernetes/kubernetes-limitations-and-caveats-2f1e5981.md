---
id: kubernetes-limitations-and-caveats-2f1e5981
type: concept
title: Limitations and caveats
description: '- The functionality is only implemented for the `static` CPU Manager
  policy'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/resource-managers/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Limitations and caveats

- The functionality is only implemented for the `static` CPU Manager policy
  and the `Static` Memory Manager policy. Note that the `BestEffort` policy is
  not supported for the Memory Manager.
- This feature is only supported on Linux nodes. On Windows nodes, the
  resource managers will act as a no-op for pod-level allocations.