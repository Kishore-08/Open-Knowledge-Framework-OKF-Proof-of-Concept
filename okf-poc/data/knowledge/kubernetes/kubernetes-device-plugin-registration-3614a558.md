---
id: kubernetes-device-plugin-registration-3614a558
type: concept
title: Device plugin registration
description: 'The kubelet exports a `Registration` gRPC service:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Device plugin registration

The kubelet exports a `Registration` gRPC service:

```
service Registration {
	rpc Register(RegisterRequest) returns (Empty) {}
}
```

A device plugin can register itself with the kubelet through this gRPC service.
During the registration, the device plugin needs to send:

- The name of its Unix socket.
- The Device Plugin API version against which it was built.
- The `ResourceName` it wants to advertise. Here `ResourceName` needs to follow the
  [extended resource naming scheme](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#extended-resources)
  as `vendor-domain/resourcetype`.
  (For example, an NVIDIA GPU is advertised as `nvidia.com/gpu`.)

Following a successful registration, the device plugin sends the kubelet the
list of devices it manages, and the kubelet is then in charge of advertising those
resources to the API server as part of the kubelet node status update.
For example, after a device plugin registers `hardware-vendor.example/foo` with the kubelet
and reports two healthy devices on a node, the node status is updated
to advertise that the node has 2 "Foo" devices installed and available.

Then, users can request devices as part of a Pod specification
(see [`container`](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/#Container)).
Requesting extended resources is similar to how you manage requests and limits for
other resources, with the following differences:

- Extended resources are only supported as integer resources and cannot be overcommitted.
- Devices cannot be shared between containers.