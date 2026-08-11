---
id: kubernetes-quota-for-infrastructure-resources-193abbf6
type: concept
title: Quota for infrastructure resources
description: You can limit the total sum of
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/policy/resource-quotas/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Quota for infrastructure resources

You can limit the total sum of
[compute resources](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/)
that can be requested in a given namespace.

The following resource types are supported:

| Resource Name | Description |
| --- | --- |
| `limits.cpu` | Across all pods in a non-terminal state, the sum of CPU limits cannot exceed this value. |
| `limits.memory` | Across all pods in a non-terminal state, the sum of memory limits cannot exceed this value. |
| `requests.cpu` | Across all pods in a non-terminal state, the sum of CPU requests cannot exceed this value. |
| `requests.memory` | Across all pods in a non-terminal state, the sum of memory requests cannot exceed this value. |
| `hugepages-<size>` | Across all pods in a non-terminal state, the number of huge page requests of the specified size cannot exceed this value. |
| `cpu` | Same as `requests.cpu` |
| `memory` | Same as `requests.memory` |