---
id: kubernetes-types-of-persistent-volumes-9fac4033
type: concept
title: Types of Persistent Volumes
description: 'PersistentVolume types are implemented as plugins. Kubernetes currently
  supports the following plugins:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/storage/persistent-volumes/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Types of Persistent Volumes

PersistentVolume types are implemented as plugins. Kubernetes currently supports the following plugins:

- [`csi`](https://kubernetes.io/docs/concepts/storage/volumes/#csi) - Container Storage Interface (CSI)
- [`fc`](https://kubernetes.io/docs/concepts/storage/volumes/#fc) - Fibre Channel (FC) storage
- [`hostPath`](https://kubernetes.io/docs/concepts/storage/volumes/#hostpath) - HostPath volume
  (for single node testing only; WILL NOT WORK in a multi-node cluster;
  consider using `local` volume instead)
- [`iscsi`](https://kubernetes.io/docs/concepts/storage/volumes/#iscsi) - iSCSI (SCSI over IP) storage
- [`local`](https://kubernetes.io/docs/concepts/storage/volumes/#local) - local storage devices
  mounted on nodes.
- [`nfs`](https://kubernetes.io/docs/concepts/storage/volumes/#nfs) - Network File System (NFS) storage

The following types of PersistentVolume are deprecated but still available.
If you are using these volume types except for `flexVolume`, `cephfs` and `rbd`,
please install corresponding CSI drivers.

- [`awsElasticBlockStore`](https://kubernetes.io/docs/concepts/storage/volumes/#awselasticblockstore) - AWS Elastic Block Store (EBS)
  (**migration on by default** starting v1.23)
- [`azureDisk`](https://kubernetes.io/docs/concepts/storage/volumes/#azuredisk) - Azure Disk
  (**migration on by default** starting v1.23)
- [`azureFile`](https://kubernetes.io/docs/concepts/storage/volumes/#azurefile) - Azure File
  (**migration on by default** starting v1.24)
- [`cinder`](https://kubernetes.io/docs/concepts/storage/volumes/#cinder) - Cinder (OpenStack block storage)
  (**migration on by default** starting v1.21)
- [`flexVolume`](https://kubernetes.io/docs/concepts/storage/volumes/#flexvolume) - FlexVolume
  (**deprecated** starting v1.23, no migration plan and no plan to remove support)
- [`gcePersistentDisk`](https://kubernetes.io/docs/concepts/storage/volumes/#gcePersistentDisk) - GCE Persistent Disk
  (**migration on by default** starting v1.23)
- [`portworxVolume`](https://kubernetes.io/docs/concepts/storage/volumes/#portworxvolume) - Portworx volume
  (**migration on by default** starting v1.31)
- [`vsphereVolume`](https://kubernetes.io/docs/concepts/storage/volumes/#vspherevolume) - vSphere VMDK volume
  (**migration on by default** starting v1.25)

Older versions of Kubernetes also supported the following in-tree PersistentVolume types:

- [`cephfs`](https://kubernetes.io/docs/concepts/storage/volumes/#cephfs)
  (**not available** starting v1.31)
- `flocker` - Flocker storage.
  (**not available** starting v1.25)
- `glusterfs` - GlusterFS storage.
  (**not available** starting v1.26)
- `photonPersistentDisk` - Photon controller persistent disk.
  (**not available** starting v1.15)
- `quobyte` - Quobyte volume.
  (**not available** starting v1.25)
- [`rbd`](https://kubernetes.io/docs/concepts/storage/volumes/#rbd) - Rados Block Device (RBD) volume
  (**not available** starting v1.31)
- `scaleIO` - ScaleIO volume.
  (**not available** starting v1.21)
- `storageos` - StorageOS volume.
  (**not available** starting v1.25)