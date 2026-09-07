---
id: kubernetes-considerations-for-pod-authors-d98ef934
type: concept
title: Considerations for Pod Authors
description: 'When authoring a PodSpec using claims for these types of devices, there
  are a few things to be aware of:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/resource-management/dynamic-resource-allocation/how-dra-works/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Considerations for Pod Authors

When authoring a PodSpec using claims for these types of devices, there are a few things to be aware of:

- When Pod-level resources are used, the scheduler strictly validates them against both container requests and limits:
  - The sum of all container requests and DRA claim resources must not exceed the Pod-level requests; otherwise, the Pod will fail to schedule.
  - Each individual container's limit plus its DRA allocations must not exceed the Pod-level limits; otherwise, the Pod will fail to schedule.
- A container's total resource requirement is the sum of its container-level resources
  and any node allocatable resources from its associated resource claims.
- **Claim Sharing Restriction**: Claims that use direct resource mappings (`mapping`) cannot be shared across multiple Pods. Claims for devices
  with `overhead` can support device sharing and overhead is tracked per Pod or per container.
- Pods with DRA claims support in-place resizing for standard requests in `spec`. The scheduler ensures
  that resized standard requests combined with static DRA allocations still fit on the node.