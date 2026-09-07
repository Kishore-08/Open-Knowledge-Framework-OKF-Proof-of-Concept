---
id: kubernetes-example-e72e225b
type: concept
title: Example
description: Consider a GPU that can operate in either MIG mode or vGPU mode. The
  driver
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/resource-management/dynamic-resource-allocation/dra-features/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Example

Consider a GPU that can operate in either MIG mode or vGPU mode. The driver
publishes two devices, each consuming 4 GiB from the same shared memory counter
of 8 GiB. Based on counter capacity alone, both devices could be allocated
together. Each device declares its operating mode as a compatibility group,
making the two modes mutually exclusive:

```
apiVersion: resource.k8s.io/v1
kind: ResourceSlice
metadata:
  name: gpu-counters
spec:
  nodeName: worker-1
  pool:
    name: gpu-pool
    generation: 1
    resourceSliceCount: 2
  driver: gpu.example.com
  sharedCounters:
  - name: gpu-0-memory
    counters:
      memory:
        value: 8Gi
---
apiVersion: resource.k8s.io/v1
kind: ResourceSlice
metadata:
  name: gpu-devices
spec:
  nodeName: worker-1
  pool:
    name: gpu-pool
    generation: 1
    resourceSliceCount: 2
  driver: gpu.example.com
  devices:
  - name: gpu-0-mig
    consumesCounters:
    - counterSet: gpu-0-memory
      counters:
        memory:
          value: 4Gi
      compatibilityGroups:
      - mig
  - name: gpu-0-vgpu
    consumesCounters:
    - counterSet: gpu-0-memory
      counters:
        memory:
          value: 4Gi
      compatibilityGroups:
      - vgpu
```

In this example:

- `gpu-0-mig` belongs to the `mig` group.
- `gpu-0-vgpu` belongs to the `vgpu` group.

If a Pod or PodGroup requests two devices from this pool, the scheduler checks
whether the two chosen devices share a common compatibility group on the
`gpu-0-memory` counter set. Since `{"mig"} ∩ {"vgpu"} = ∅`, the pair is
rejected — even though the counter set has enough memory for both. Both
requests can only be satisfied by two MIG devices (or two vGPU devices) from a
pool where such pairs exist.