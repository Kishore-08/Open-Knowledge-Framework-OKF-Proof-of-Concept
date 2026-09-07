---
id: kubernetes-workflow-for-kubernetes-d98ef934
type: concept
title: Workflow for Kubernetes
description: '1. **ResourceSlice creation**: drivers in the cluster create ResourceSlices
  that'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/resource-management/dynamic-resource-allocation/how-dra-works/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Workflow for Kubernetes

1. **ResourceSlice creation**: drivers in the cluster create ResourceSlices that
   represent one or more devices in a managed pool of similar devices.
2. **Workload creation**: the cluster control plane checks new workloads for
   references to ResourceClaimTemplates or to specific ResourceClaims.

   - If the workload uses a ResourceClaimTemplate, a controller named the
     `resourceclaim-controller` generates ResourceClaims for the workload.
   - If the workload uses a specific ResourceClaim, Kubernetes checks whether
     that ResourceClaim exists in the cluster. If the ResourceClaim doesn't
     exist, the Pods won't deploy.
3. **ResourceSlice filtering**: for every Pod, Kubernetes checks the
   ResourceSlices in the cluster to find a device that satisfies all of the
   following criteria:

   - The nodes that can access the resources are eligible to run the Pod.
   - The ResourceSlice has unallocated resources that match the requirements of
     the Pod's ResourceClaim.
4. **Resource allocation**: after finding an eligible ResourceSlice for a
   Pod's ResourceClaim, the Kubernetes scheduler updates the ResourceClaim
   with the allocation details. The scheduler uses a first-fit strategy and
   evaluates pools and ResourceSlices in lexicographical order by their names.
   Drivers can prioritize specific slices or pools by naming them appropriately.
   For details, see
   [Naming and prioritization](https://kubernetes.io/docs/concepts/resource-management/dynamic-resource-allocation/dra-api/#resourceslice-naming-and-prioritization).
5. **Pod scheduling**: when resource allocation is complete, the scheduler
   places the Pod on a node that can access the allocated resource. The device
   driver and the `kubelet` on that node coordinate via gRPC to configure the
   device and the Pod's access to the device, unless the driver declared
   [optional node operations](https://kubernetes.io/docs/concepts/resource-management/dynamic-resource-allocation/dra-features/#optional-node-operations)
   for devices that do not require node-local preparation or cleanup.