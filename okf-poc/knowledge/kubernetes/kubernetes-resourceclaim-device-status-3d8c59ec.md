---
id: kubernetes-resourceclaim-device-status-3d8c59ec
type: concept
title: ResourceClaim device status
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/resource-management/dynamic-resource-allocation/dra-observability/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### ResourceClaim device status

FEATURE STATE:
`Kubernetes v1.37 [stable]`(enabled by default)

DRA drivers can report driver-specific
[device status](https://kubernetes.io/docs/concepts/overview/working-with-objects/#object-spec-and-status)
data for each allocated device in the `status.devices` field of a ResourceClaim.
For example, the driver might list the IP addresses that are assigned to a
network interface device. Updating this field requires specific synthetic RBAC permissions,
see
[Hardening Guide - Dynamic Resource Allocation](https://kubernetes.io/docs/concepts/security/hardening-guide/dynamic-resource-allocation/)
and
[Harden Dynamic Resource Allocation in Your Cluster](https://kubernetes.io/docs/tasks/administer-cluster/hardening-dra/).

The accuracy of the information that a driver adds to a ResourceClaim
`status.devices` field depends on the driver. Evaluate drivers to decide whether
you can rely on this field as the only source of device information.

If you disable the
[`DRAResourceClaimDeviceStatus` feature gate](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/#DRAResourceClaimDeviceStatus), the
`status.devices` field automatically gets cleared when storing the ResourceClaim.
A ResourceClaim device status is supported when it is possible, from a DRA
driver, to update an existing ResourceClaim where the `status.devices` field is
set.

In the following example, the `status.devices` field of a ResourceClaim has been
populated by the driver (`resource-driver.example.com`) responsible for managing
the allocated device:

```
apiVersion: resource.k8s.io/v1
kind: ResourceClaim
metadata:
  name: macvlan-eth0
spec:
...
status:
  allocation:
    devices:
      results:
      - device: eth0
        driver: resource-driver.example.com
        pool: nic-worker-a
        request: macvlan-eth0
        shareID: 8e7acdf9-0290-4ecd-a801-a654b021d2b7
        consumedCapacity:
          resource-driver.example.com/bandwidth: 1G
  devices:
  - conditions:
    - lastTransitionTime: "2025-10-21T08:38:17Z"
      message: Device successfully allocated and assigned to the pod
      reason: NetworkReady
      status: "True"
      type: NetworkReady
    device: eth0
    driver: resource-driver.example.com
    networkData:
      hardwareAddress: 00:01:ec:84:fb:51
      interfaceName: net1
      ips:
      - 10.10.1.2/24
      - 2001:db8::1/64
    pool: nic-worker-a
    shareID: 8e7acdf9-0290-4ecd-a801-a654b021d2b7
```

If a device has not been allocated, a driver's request to update the `status.devices`
field of the ResourceClaim with that device is rejected. When a device is
deallocated (removed from `status.allocation.devices`), the corresponding entry in
`status.devices` is automatically removed.

For details about the `status.devices` field, see the
[ResourceClaim](https://kubernetes.io/docs/reference/kubernetes-api/resource/resource-claim-v1/#ResourceClaimStatus) API reference.