---
id: kubernetes-resource-pool-status-3d8c59ec
type: concept
title: Resource pool status
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/resource-management/dynamic-resource-allocation/dra-observability/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

## Resource pool status

FEATURE STATE:
`Kubernetes v1.36 [alpha]`(disabled by default)

You can query the availability of devices in resource pools using the
ResourcePoolStatusRequest API. This provides visibility into how many devices
are available, allocated, or unavailable across your cluster's DRA resource pools.

To check resource pool status:

1. Create a ResourcePoolStatusRequest specifying the driver name (required) and
   optionally a limit on the number of pools returned. You can also limit it to a single pool by specifying a pool name:

   ```
   apiVersion: resource.k8s.io/v1alpha3
   kind: ResourcePoolStatusRequest
   metadata:
     name: check-gpus
   spec:
     driver: example.com/gpu
     # Optional: filter to a specific pool
     # poolName: my-pool
     # Optional: limit number of pools returned (default: 100, max: 1000)
     # limit: 10
   ```
2. Wait for the controller to process the request:

   ```
   kubectl wait --for=condition=Complete resourcepoolstatusrequest/check-gpus --timeout=30s
   ```
3. Read the status to see pool availability:

   ```
   kubectl get resourcepoolstatusrequest/check-gpus -o yaml
   ```

   The status includes:

   - `poolCount`: total number of pools matching the filter (may exceed the number
     of pools listed if truncated by the limit).
   - `pools`: a list of pool details, each containing:
     - `driver` and `poolName`: identify the pool.
     - `generation`: the latest pool generation observed across ResourceSlices.
     - `resourceSliceCount`: the number of ResourceSlices making up the pool.
     - `totalDevices`: total devices in the pool.
     - `allocatedDevices`: devices currently allocated to claims.
     - `availableDevices`: devices available for allocation
       (totalDevices - allocatedDevices - unavailableDevices).
     - `unavailableDevices`: devices not available due to taints or other conditions.
     - `nodeName`: the node associated with the pool, if any.
     - `validationError`: set when the pool's data could not be fully validated
       (for example, during a generation rollout). When set, device count fields
       may be unset.
     - `partitionSummary`: for [partitionable](https://kubernetes.io/docs/concepts/resource-management/dynamic-resource-allocation/dra-features/#partitionable-devices)
       pools, per-partition-type allocatability (see
       [Partition summary](https://kubernetes.io/docs/concepts/resource-management/dynamic-resource-allocation/dra-observability/#resource-pool-partition-summary)).
     - `shareableSummary`: for pools with [shareable devices](https://kubernetes.io/docs/concepts/resource-management/dynamic-resource-allocation/dra-features/#consumable-capacity),
       aggregate capacity usage (see
       [Shareable summary](https://kubernetes.io/docs/concepts/resource-management/dynamic-resource-allocation/dra-observability/#resource-pool-shareable-summary)).
   - `conditions`: includes `Complete` (success) or `Failed` (error) condition types.
4. Delete the request when done:

   ```
   kubectl delete resourcepoolstatusrequest/check-gpus
   ```

ResourcePoolStatusRequest objects are processed once by a controller in
kube-controller-manager. The spec is immutable once created, and the entire
object becomes immutable once the status is populated. To get updated
availability data, delete and recreate the request. Completed requests are
automatically cleaned up after 1 hour.

This feature requires explicit RBAC permissions on the ResourcePoolStatusRequest
resource. No default ClusterRoles include this permission.

Resource pool status is controlled by the
[`DRAResourcePoolStatus` feature gate](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/#DRAResourcePoolStatus)
in the `kube-apiserver` and `kube-controller-manager`.