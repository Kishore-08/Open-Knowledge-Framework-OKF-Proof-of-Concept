---
id: kubernetes-types-of-ephemeral-volumes-c2988c6c
type: concept
title: Types of ephemeral volumes
description: Kubernetes supports several different kinds of ephemeral volumes for
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/storage/ephemeral-volumes/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Types of ephemeral volumes

Kubernetes supports several different kinds of ephemeral volumes for
different purposes:

- [emptyDir](https://kubernetes.io/docs/concepts/storage/volumes/#emptydir): empty at Pod startup,
  with storage coming locally from the kubelet base directory (usually
  the root disk) or RAM
- [configMap](https://kubernetes.io/docs/concepts/storage/volumes/#configmap),
  [downwardAPI](https://kubernetes.io/docs/concepts/storage/volumes/#downwardapi),
  [secret](https://kubernetes.io/docs/concepts/storage/volumes/#secret): inject different
  kinds of Kubernetes data into a Pod
- [image](https://kubernetes.io/docs/concepts/storage/volumes/#image): allows mounting container image files or artifacts,
  directly to a Pod.
- [CSI ephemeral volumes](https://kubernetes.io/docs/concepts/storage/ephemeral-volumes/#csi-ephemeral-volumes):
  similar to the previous volume kinds, but provided by special [CSI](https://kubernetes.io/docs/concepts/storage/volumes/#csi "The Container Storage Interface (CSI) defines a standard interface to expose storage systems to containers.") drivers
  which specifically [support this feature](https://kubernetes-csi.github.io/docs/ephemeral-local-volumes.html)
- [generic ephemeral volumes](https://kubernetes.io/docs/concepts/storage/ephemeral-volumes/#generic-ephemeral-volumes), which
  can be provided by all storage drivers that also support persistent volumes

`emptyDir`, `configMap`, `downwardAPI`, `secret` are provided as
[local ephemeral storage](https://kubernetes.io/docs/concepts/storage/ephemeral-storage/).
They are managed by kubelet on each node.

CSI ephemeral volumes *must* be provided by third-party CSI storage
drivers.

Generic ephemeral volumes *can* be provided by third-party CSI storage
drivers, but also by any other storage driver that supports dynamic
provisioning. Some CSI drivers are written specifically for CSI
ephemeral volumes and do not support dynamic provisioning: those then
cannot be used for generic ephemeral volumes.

The advantage of using third-party drivers is that they can offer
functionality that Kubernetes itself does not support, for example
storage with different performance characteristics than the disk that
is managed by kubelet, or injecting different data.