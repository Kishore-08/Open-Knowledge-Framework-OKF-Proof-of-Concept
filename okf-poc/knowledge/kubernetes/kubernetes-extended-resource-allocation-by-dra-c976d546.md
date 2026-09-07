---
id: kubernetes-extended-resource-allocation-by-dra-c976d546
type: concept
title: Extended resource allocation by DRA
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/resource-management/dynamic-resource-allocation/dra-api/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

## Extended resource allocation by DRA

FEATURE STATE:
`Kubernetes v1.37 [stable]`(enabled by default)

You can provide an extended resource name for a DeviceClass. The scheduler will then
select the devices matching the class for the extended resource requests.
This allows users to continue using extended resource requests in a pod to request
either extended resources provided by device plugin, or DRA devices.
The same extended resource can be provided either by device plugin, or DRA on one single cluster node.
The same extended resource can be provided by device plugin on some nodes, and DRA on other nodes in the same cluster.

In the example below, the DeviceClass is given an extendedResourceName `example.com/gpu`.
If a pod requested for the extended resource `example.com/gpu: 2`, it can be scheduled to
a node with two or more devices matching the DeviceClass.

```
apiVersion: resource.k8s.io/v1
kind: DeviceClass
metadata:
  name: gpu.example.com
spec:
  selectors:
  - cel:
      expression: device.driver == 'gpu.example.com' && device.attributes['gpu.example.com'].type
        == 'gpu'
  extendedResourceName: example.com/gpu
```

In addition, users can use a special extended resource to allocate devices without
having to explicitly create a ResourceClaim. Using the extended resource name
prefix `deviceclass.resource.kubernetes.io/` and the DeviceClass name.
This works for any DeviceClass, even if it does not specify an extended resource name.
The resulting ResourceClaim will contain a request for an `ExactCount` of the
specified number of devices of that DeviceClass.

Extended resource allocation by DRA is controlled by the
[`DRAExtendedResource` feature gate](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/#DRAExtendedResource)
in the `kube-apiserver`, `kube-scheduler`, `kube-controller-manager`, and `kubelet`.

For a hands-on walkthrough of requesting extended resources, see
[Assign Extended Resources to a Container](https://kubernetes.io/docs/tasks/configure-pod-container/extended-resource/).