---
id: kubernetes-getallocatableresources-grpc-endpoint-3614a558
type: concept
title: '`GetAllocatableResources` gRPC endpoint'
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### `GetAllocatableResources` gRPC endpoint

FEATURE STATE:
`Kubernetes v1.28 [stable]`

GetAllocatableResources provides information on resources initially available on the worker node.
It provides more information than kubelet exports to APIServer.

#### Note:

`GetAllocatableResources` should only be used to evaluate [allocatable](https://kubernetes.io/docs/tasks/administer-cluster/reserve-compute-resources/#node-allocatable)
resources on a node. If the goal is to evaluate free/unallocated resources it should be used in
conjunction with the List() endpoint. The result obtained by `GetAllocatableResources` would remain
the same unless the underlying resources exposed to kubelet change. This happens rarely but when
it does (for example: hotplug/hotunplug, device health changes), client is expected to call
`GetAllocatableResources` endpoint.

However, calling `GetAllocatableResources` endpoint is not sufficient in case of cpu and/or memory
update and Kubelet needs to be restarted to reflect the correct resource capacity and allocatable.

```
// AllocatableResourcesResponses contains information about all the devices known by the kubelet
message AllocatableResourcesResponse {
    repeated ContainerDevices devices = 1;
    repeated int64 cpu_ids = 2;
    repeated ContainerMemory memory = 3;
}
```

`ContainerDevices` do expose the topology information declaring to which NUMA cells the device is
affine. The NUMA cells are identified using a opaque integer ID, which value is consistent to
what device plugins report
[when they register themselves to the kubelet](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/#device-plugin-integration-with-the-topology-manager).

The gRPC service is served over a unix socket at `pod-resources/kubelet.sock` within the
kubelet's root directory (typically `/var/lib/kubelet/pod-resources/kubelet.sock`).
Monitoring agents for device plugin resources can be deployed as a daemon, or as a DaemonSet.
The canonical directory `pod-resources` within the kubelet root directory (typically
`/var/lib/kubelet/pod-resources`) requires privileged access, so monitoring
agents must run in a privileged security context. If a device monitoring agent is running as a
DaemonSet, the `pod-resources` directory must be mounted as a
[Volume](https://kubernetes.io/docs/concepts/storage/volumes/ "A directory containing data, accessible to the containers in a pod.") in the device monitoring agent's
[PodSpec](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.36/#podspec-v1-core).

#### Note:

When accessing the `pod-resources/kubelet.sock` from DaemonSet
or any other app deployed as a container on the host, which is mounting socket as
a volume, it is a good practice to mount the `pod-resources` directory
instead of the socket file itself. This will ensure
that after kubelet restart, the container will be able to re-connect to this socket.

On a typical Linux node, this means mounting `/var/lib/kubelet/pod-resources/`
instead of `/var/lib/kubelet/pod-resources/kubelet.sock`.

Container mounts are managed by inode referencing the socket or directory,
depending on what was mounted. When kubelet restarts, the socket is deleted
and a new socket is created, while the directory stays untouched.
So the original inode for the socket becomes unusable. The inode to the directory
will continue working.