---
id: kubernetes-evictions-9edb5061
type: concept
title: Evictions
description: Configuring memory eviction thresholds for swap-enabled nodes can be
  tricky.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/swap-memory-management/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Evictions

Configuring memory eviction thresholds for swap-enabled nodes can be tricky.

With swap being disabled, it is reasonable to configure kubelet's eviction thresholds
to be a bit lower than the node's memory capacity.
The rationale is that we want Kubernetes to start evicting Pods before the node runs out of memory
and invokes the Out Of Memory (OOM) killer, since the OOM killer is not Kubernetes-aware,
therefore does not consider things like QoS, pod priority, or other Kubernetes-specific factors.

With swap enabled, the situation is more complex.
In Linux, the `vm.min_free_kbytes` parameter defines the memory threshold for the kernel
to start aggressively reclaiming memory, which includes swapping out pages.
If the kubelet's eviction thresholds are set in a way that eviction would take place
before the kernel starts reclaiming memory, it could lead to workloads never
being able to swap out during node memory pressure.
However, setting the eviction thresholds too high could result in the node running out of memory
and invoking the OOM killer, which is not ideal either.

To address this, it is recommended to set the kubelet's eviction thresholds
to be slightly lower than the `vm.min_free_kbytes` value.
This way, the node can start swapping before kubelet would start evicting Pods,
allowing workloads to swap out unused data and preventing evictions from happening.
On the other hand, since it is just slightly lower, kubelet is likely to start evicting Pods
before the node runs out of memory, thus avoiding the OOM killer.

The value of `vm.min_free_kbytes` can be determined by running the following command on the node:

```
cat /proc/sys/vm/min_free_kbytes
```