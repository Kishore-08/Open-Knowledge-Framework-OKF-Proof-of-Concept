---
id: kubernetes-resourceslice-c976d546
type: concept
title: ResourceSlice
description: Each ResourceSlice represents one or more
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/resource-management/dynamic-resource-allocation/dra-api/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### ResourceSlice

Each ResourceSlice represents one or more
[devices](https://kubernetes.io/docs/reference/glossary/?all=true#term-device "Any resource that's directly or indirectly attached your cluster's nodes, like GPUs or circuit boards.") in a pool. The pool is
managed by a device driver, which creates and manages ResourceSlices. The
resources in a pool might be represented by a single ResourceSlice or span
multiple ResourceSlices.

ResourceSlices provide useful information to device users and to the scheduler,
and are crucial for dynamic resource allocation. Every ResourceSlice must include
the following information:

- **Resource pool**: a group of one or more resources that the driver manages.
  The pool can span more than one ResourceSlice. Changes to the resources in a
  pool must be propagated across all of the ResourceSlices in that pool. The
  device driver that manages the pool is responsible for ensuring that this
  propagation happens.
- **Devices**: devices in the managed pool. A ResourceSlice can list every
  device in a pool or a subset of the devices in a pool. The ResourceSlice
  defines device information like attributes, versions, and capacity. Device
  users can select devices for allocation by filtering for device information
  in ResourceClaims or in DeviceClasses.
- **Nodes**: the nodes that can access the resources. Drivers can choose which
  nodes can access the resources, whether that's all of the nodes in the
  cluster, a single named node, or nodes that have specific node labels.

Drivers use a [controller](https://kubernetes.io/docs/concepts/architecture/controller/ "A control loop that watches the shared state of the cluster through the apiserver and makes changes attempting to move the current state towards the desired state.") to
reconcile ResourceSlices in the cluster with the information that the driver has
to publish. This controller overwrites any manual changes, such as cluster users
creating or modifying ResourceSlices.

Consider the following example ResourceSlice:

```
apiVersion: resource.k8s.io/v1
kind: ResourceSlice
metadata:
  name: cat-slice
spec:
  driver: "resource-driver.example.com"
  pool:
    generation: 1
    name: "black-cat-pool"
    resourceSliceCount: 1
  # The allNodes field defines whether any node in the cluster can access the device.
  allNodes: true
  devices:
  - name: "large-black-cat"
    attributes:
      color:
        string: "black"
      size:
        string: "large"
      cat:
        bool: true
```

This ResourceSlice is managed by the `resource-driver.example.com` driver in the
`black-cat-pool` pool. The `allNodes: true` field indicates that any node in the
cluster can access the devices. There's one device in the ResourceSlice, named
`large-black-cat`, with the following attributes:

- `color`: `black`
- `size`: `large`
- `cat`: `true`

A DeviceClass could select this ResourceSlice by using these attributes, and a
ResourceClaim could filter for specific devices in that DeviceClass.

#### Naming and prioritization

The order in which the Kubernetes scheduler evaluates devices for allocation is
determined by the lexicographical sorting of ResourceSlice and resource pool names.
The scheduler uses a first-fit strategy, meaning it selects the first available device
that satisfies the claim's requirements.

This allows the priority of resource allocation to be influenced by the names
assigned to pools and ResourceSlices. Note that pools without
[binding conditions](https://kubernetes.io/docs/concepts/resource-management/dynamic-resource-allocation/dra-features/#device-binding-conditions)
are always evaluated before those
with binding conditions, regardless of their names.

For drivers built using the `k8s.io/dynamic-resources/kubeletplugin` Go package or
the ResourceSlice controller from that module, these components automatically handle
ResourceSlice naming to ensure they are evaluated in the order specified by the driver.