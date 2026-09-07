---
id: kubernetes-details-for-dra-driver-authors-d98ef934
type: concept
title: Details for DRA Driver Authors
description: DRA drivers declare this node allocatable resource footprint using the
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/resource-management/dynamic-resource-allocation/how-dra-works/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Details for DRA Driver Authors

DRA drivers declare this node allocatable resource footprint using the
`nodeAllocatableResources` field on devices within a ResourceSlice.
This defines the translation of the requested DRA device or capacity into standard
resources that are tracked in the node's `status.allocatable` (note that extended
resources are not supported for this field). This is useful both for drivers that directly
expose native resources (like a CPU or Memory DRA driver) and for devices that
require auxiliary node dependencies (like an accelerator that needs host memory).

The `nodeAllocatableResources` field supports two different use cases:

- **Mapping**: Used when the DRA device directly represents the standard resource
  (e.g., a CPU or Memory DRA driver). The scheduler calculates the exact quantity
  by scaling the capacity using `capacityMultiplier`, or scaling the device count
  using `deviceMultiplier`.
- **Overhead**: Used when the device requires auxiliary node dependencies (e.g.,
  host memory consumed by a GPU). This can be defined as a flat `perPod` cost or
  a variable `perContainer` cost that scales linearly with the number of
  referencing containers.

#### Example: CPU DRA Driver (Mapping)

Here is an example where a CPU DRA driver exposes a CPU socket as a pool of 128
CPUs using [DRA consumable capacity](https://kubernetes.io/docs/concepts/resource-management/dynamic-resource-allocation/how-dra-works/#consumable-capacity). The `capacityKey` links the consumed
`cpu.example.com/cpu` capacity directly to the node's standard `cpu`
allocatable resource:

```
apiVersion: resource.k8s.io/v1
kind: ResourceSlice
metadata:
  name: my-node-cpus
spec:
  driver: cpu.example.com
  nodeName: my-node
  pool:
    name: socket-cpus
    generation: 1
    resourceSliceCount: 1
  devices:
  - name: socket0cpus
    allowMultipleAllocations: true
    capacity:
      "cpu.example.com/cpu": "128"
    nodeAllocatableResources:
      mapping:
        cpu:
          capacityKey: "cpu.example.com/cpu"
  - name: socket1cpus
    allowMultipleAllocations: true
    capacity:
      "cpu.example.com/cpu": "128"
    nodeAllocatableResources:
      mapping:
        cpu:
          capacityKey: "cpu.example.com/cpu"
          capacityMultiplier: 1
```

#### Example: Accelerator with Auxiliary Resources (Overhead)

Here is an example of a resource slice where an accelerator requires an
additional 8Gi of memory per Pod to function:

```
apiVersion: resource.k8s.io/v1
kind: ResourceSlice
metadata:
  name: my-node-xpus
spec:
  driver: xpu.example.com
  nodeName: my-node
  pool:
    name: xpu-pool
    generation: 1
    resourceSliceCount: 1
  devices:
  - name: xpu-model-x-001
    attributes:
      example.com/model:
        string: "model-x"
    nodeAllocatableResources:
      overhead:
        memory:
          perPod: "8Gi"
```

After a Pod is successfully bound to the node, the exact quantities of
node allocatable resources allocated via DRA are aggregated by the `kube-scheduler`
and embedded directly into the Pod's `status.nodeAllocatableResourceClaimStatuses` field.
This provides a clear, persistent handoff from the scheduler to the `kubelet`.

Crucially, the `kubelet` natively consumes this API to perfectly align system-level boundaries:

- **cgroups**: Pod and container cgroups would now include DRA based allocations, preventing workloads from being artificially throttled by the kernel.
- **OOM Scores**: The `kubelet` factors the container's DRA memory requests into its effective memory request.

Node allocatable resources is an alpha feature and is enabled when the
[`DRANodeAllocatableResources` feature gate](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/#DRANodeAllocatableResources) is enabled in the `kube-apiserver`,
`kube-scheduler`, and `kubelet`.