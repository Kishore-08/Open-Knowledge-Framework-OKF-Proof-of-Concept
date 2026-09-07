---
id: kubernetes-partitionable-devices-e72e225b
type: concept
title: Partitionable devices
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/resource-management/dynamic-resource-allocation/dra-features/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

## Partitionable devices

FEATURE STATE:
`Kubernetes v1.36 [beta]`(enabled by default)

Devices represented in DRA don't necessarily have to be a single unit connected to a single machine,
but can also be a logical device comprised of multiple devices connected to multiple machines.
These devices might consume overlapping resources of the underlying phyical devices,
meaning that when one logical device is allocated other devices will no longer be available.

In the ResourceSlice API, this is represented as a list of named CounterSets, each of which
contains a set of named counters. The counters represent the resources available on the physical
device that are used by the logical devices advertised through DRA.

Logical devices can specify the ConsumesCounters list. Each entry contains a reference to a CounterSet
and a set of named counters with the amounts they will consume. So for a device to be allocatable,
the referenced counter sets must have sufficient quantity for the counters referenced by the device.

CounterSets must be specified in separate ResourceSlices from devices.
Devices can consume counters from any CounterSet defined in the same resource pool as the device.

Here is an example of two devices, each consuming 6Gi of memory from a shared counter with 8Gi of memory.
Thus, only one of the devices can be allocated at any point in time.
The scheduler handles this and it is transparent to the consumer as the ResourceClaim API is not affected.

```
apiVersion: resource.k8s.io/v1
kind: ResourceSlice
metadata:
  name: resourceslice-with-countersets
spec:
  nodeName: worker-1
  pool:
    name: pool
    generation: 1
    resourceSliceCount: 2
  driver: dra.example.com
  sharedCounters:
  - name: gpu-1-counters
    counters:
      memory:
        value: 8Gi
---
apiVersion: resource.k8s.io/v1
kind: ResourceSlice
metadata:
  name: resourceslice-with-devices
spec:
  nodeName: worker-1
  pool:
    name: pool
    generation: 1
    resourceSliceCount: 2
  driver: dra.example.com
  devices:
  - name: device-1
    consumesCounters:
    - counterSet: gpu-1-counters
      counters:
        memory:
          value: 6Gi
  - name: device-2
    consumesCounters:
    - counterSet: gpu-1-counters
      counters:
        memory:
          value: 6Gi
```

Partitionable devices is controlled by the
[`DRAPartitionableDevices` feature gate](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/#DRAPartitionableDevices)
in the `kube-apiserver` and `kube-scheduler`.