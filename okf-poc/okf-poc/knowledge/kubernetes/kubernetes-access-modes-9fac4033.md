---
id: kubernetes-access-modes-9fac4033
type: concept
title: Access Modes
description: A PersistentVolume can be mounted on a host in any way supported by the
  resource
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/storage/persistent-volumes/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Access Modes

A PersistentVolume can be mounted on a host in any way supported by the resource
provider. As shown in the table below, providers will have different capabilities
and each PV's access modes are set to the specific modes supported by that particular
volume. For example, NFS can support multiple read/write clients, but a specific
NFS PV might be exported on the server as read-only. Each PV gets its own set of
access modes describing that specific PV's capabilities.

The access modes are:

`ReadWriteOnce`
:   the volume can be mounted as read-write by a single node. ReadWriteOnce access
    mode still can allow multiple pods to access (read from or write to) that volume when the pods are
    running on the same node. For single pod access, please see ReadWriteOncePod.

`ReadOnlyMany`
:   the volume can be mounted as read-only by many nodes.

`ReadWriteMany`
:   the volume can be mounted as read-write by many nodes.

`ReadWriteOncePod`
:   FEATURE STATE:
    `Kubernetes v1.29 [stable]`

    the volume can be mounted as read-write by a single Pod. Use ReadWriteOncePod
    access mode if you want to ensure that only one pod across the whole cluster can
    read that PVC or write to it.

#### Note:

The `ReadWriteOncePod` access mode is only supported for
[CSI](https://kubernetes.io/docs/concepts/storage/volumes/#csi "The Container Storage Interface (CSI) defines a standard interface to expose storage systems to containers.") volumes and Kubernetes version
1.22+. To use this feature you will need to update the following
[CSI sidecars](https://kubernetes-csi.github.io/docs/sidecar-containers.html)
to these versions or greater:

- [csi-provisioner:v3.0.0+](https://github.com/kubernetes-csi/external-provisioner/releases/tag/v3.0.0)
- [csi-attacher:v3.3.0+](https://github.com/kubernetes-csi/external-attacher/releases/tag/v3.3.0)
- [csi-resizer:v1.3.0+](https://github.com/kubernetes-csi/external-resizer/releases/tag/v1.3.0)

In the CLI, the access modes are abbreviated to:

- RWO - ReadWriteOnce
- ROX - ReadOnlyMany
- RWX - ReadWriteMany
- RWOP - ReadWriteOncePod

#### Note:

Kubernetes uses volume access modes to match PersistentVolumeClaims and PersistentVolumes.
In some cases, the volume access modes also constrain where the PersistentVolume can be mounted.
Volume access modes do **not** enforce write protection once the storage has been mounted.
Even if the access modes are specified as ReadWriteOnce, ReadOnlyMany, or ReadWriteMany,
they don't set any constraints on the volume. For example, even if a PersistentVolume is
created as ReadOnlyMany, it is no guarantee that it will be read-only. If the access modes
are specified as ReadWriteOncePod, the volume is constrained and can be mounted on only a single Pod.

> **Important!** A volume can only be mounted using one access mode at a time,
> even if it supports many.

| Volume Plugin | ReadWriteOnce | ReadOnlyMany | ReadWriteMany | ReadWriteOncePod |
| --- | --- | --- | --- | --- |
| AzureFile | ✓ | ✓ | ✓ | - |
| CephFS | ✓ | ✓ | ✓ | - |
| CSI | depends on the driver | depends on the driver | depends on the driver | depends on the driver |
| FC | ✓ | ✓ | - | - |
| FlexVolume | ✓ | ✓ | depends on the driver | - |
| HostPath | ✓ | - | - | - |
| iSCSI | ✓ | ✓ | - | - |
| NFS | ✓ | ✓ | ✓ | - |
| RBD | ✓ | ✓ | - | - |
| VsphereVolume | ✓ | - | - (works when Pods are collocated) | - |
| PortworxVolume | ✓ | - | ✓ | - |