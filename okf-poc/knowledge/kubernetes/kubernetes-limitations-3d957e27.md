---
id: kubernetes-limitations-3d957e27
type: concept
title: Limitations
description: '- The Kubernetes scheduler doesn''t support'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/resource-management/dynamic-resource-allocation/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

## Limitations

- The Kubernetes scheduler doesn't support
  [preemption](https://kubernetes.io/docs/concepts/scheduling-eviction/pod-priority-preemption/) for
  DRA resources. This means that an existing Pod that's running on a node and is
  using DRA resources can't be preempted by a higher-priority Pod that also needs
  DRA resources. The high-priority Pod will remain in a pending state until the device
  becomes available, which happens when the conflicting Pod terminates or is
  manually deleted.