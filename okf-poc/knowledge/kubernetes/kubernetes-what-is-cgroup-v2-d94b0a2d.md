---
id: kubernetes-what-is-cgroup-v2-d94b0a2d
type: concept
title: What is cgroup v2?
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/architecture/cgroups/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## What is cgroup v2?

FEATURE STATE:
`Kubernetes v1.25 [stable]`

cgroup v2 is the next version of the Linux `cgroup` API. cgroup v2 provides a
unified control system with enhanced resource management
capabilities.

cgroup v2 offers several improvements over cgroup v1, such as the following:

- Single unified hierarchy design in API
- Safer sub-tree delegation to containers
- Newer features like [Pressure Stall Information](https://www.kernel.org/doc/html/latest/accounting/psi.html)
- Enhanced resource allocation management and isolation across multiple resources
  - Unified accounting for different types of memory allocations (network memory, kernel memory, etc)
  - Accounting for non-immediate resource changes such as page cache write backs

Some Kubernetes features exclusively use cgroup v2 for enhanced resource
management and isolation. For example, the
[MemoryQoS](https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/#memory-qos-with-cgroup-v2) feature improves memory QoS
and relies on cgroup v2 primitives.