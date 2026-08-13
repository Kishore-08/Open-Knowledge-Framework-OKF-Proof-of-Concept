---
id: kubernetes-provisioner-1915a01d
type: concept
title: Provisioner
description: Each StorageClass has a provisioner that determines what volume plugin
  is used
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/storage/storage-classes/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

## Provisioner

Each StorageClass has a provisioner that determines what volume plugin is used
for provisioning PVs. This field must be specified.

| Volume Plugin | Internal Provisioner | Config Example |
| --- | --- | --- |
| AzureFile | ✓ | [Azure File](https://kubernetes.io/docs/concepts/storage/storage-classes/#azure-file) |
| CephFS | - | - |
| FC | - | - |
| FlexVolume | - | - |
| iSCSI | - | - |
| Local | - | [Local](https://kubernetes.io/docs/concepts/storage/storage-classes/#local) |
| NFS | - | [NFS](https://kubernetes.io/docs/concepts/storage/storage-classes/#nfs) |
| PortworxVolume | ✓ | [Portworx Volume](https://kubernetes.io/docs/concepts/storage/storage-classes/#portworx-volume) |
| RBD | - | [Ceph RBD](https://kubernetes.io/docs/concepts/storage/storage-classes/#ceph-rbd) |
| VsphereVolume | ✓ | [vSphere](https://kubernetes.io/docs/concepts/storage/storage-classes/#vsphere) |

You are not restricted to specifying the "internal" provisioners
listed here (whose names are prefixed with "kubernetes.io" and shipped
alongside Kubernetes). You can also run and specify external provisioners,
which are independent programs that follow a [specification](https://git.k8s.io/design-proposals-archive/storage/volume-provisioning.md)
defined by Kubernetes. Authors of external provisioners have full discretion
over where their code lives, how the provisioner is shipped, how it needs to be
run, what volume plugin it uses (including Flex), etc. The repository
[kubernetes-sigs/sig-storage-lib-external-provisioner](https://github.com/kubernetes-sigs/sig-storage-lib-external-provisioner)
houses a library for writing external provisioners that implements the bulk of
the specification. Some external provisioners are listed under the repository
[kubernetes-sigs/sig-storage-lib-external-provisioner](https://github.com/kubernetes-sigs/sig-storage-lib-external-provisioner).

For example, NFS doesn't provide an internal provisioner, but an external
provisioner can be used. There are also cases when 3rd party storage
vendors provide their own external provisioner.