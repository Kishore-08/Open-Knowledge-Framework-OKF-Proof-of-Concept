---
id: kubernetes-cpu-quota-cfs-0cecd4eb
type: concept
title: CPU quota (CFS)
description: When running mixed workloads within a Pod, the `kubelet` enforces isolation
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/resource-management/pod-level-resource-managers/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### CPU quota (CFS)

When running mixed workloads within a Pod, the `kubelet` enforces isolation
differently depending on the allocation:

- **Exclusive containers:** Containers with exclusive CPU slices have their
  CPU CFS quota enforcement disabled, allowing them to run without
  throttling by the Linux scheduler.
- **Pod shared pool containers:** Containers in the Pod shared pool have
  CPU CFS quotas enabled, ensuring they do not consume more than the
  leftover Pod budget and preventing them from interfering with the
  exclusive containers.