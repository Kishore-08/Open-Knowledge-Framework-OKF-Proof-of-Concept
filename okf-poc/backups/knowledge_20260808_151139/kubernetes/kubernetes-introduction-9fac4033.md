---
id: kubernetes-introduction-9fac4033
type: concept
title: Introduction
description: Managing storage is a distinct problem from managing compute instances.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/storage/persistent-volumes/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Introduction

Managing storage is a distinct problem from managing compute instances.
The PersistentVolume subsystem provides an API for users and administrators
that abstracts details of how storage is provided from how it is consumed.
To do this, we introduce two new API resources: PersistentVolume and PersistentVolumeClaim.

A *PersistentVolume* (PV) is a piece of storage in the cluster that has been
provisioned by an administrator or dynamically provisioned using
[Storage Classes](https://kubernetes.io/docs/concepts/storage/storage-classes/). It is a resource in
the cluster just like a node is a cluster resource. PVs are volume plugins like
Volumes, but have a lifecycle independent of any individual Pod that uses the PV.
This API object captures the details of the implementation of the storage, be that
NFS, iSCSI, or a cloud-provider-specific storage system.

A *PersistentVolumeClaim* (PVC) is a request for storage by a user. It is similar
to a Pod. Pods consume node resources and PVCs consume PV resources. Pods can
request specific levels of resources (CPU and Memory). Claims can request specific
size and access modes (e.g., they can be mounted ReadWriteOnce, ReadOnlyMany,
ReadWriteMany, or ReadWriteOncePod, see [AccessModes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#access-modes)).

While PersistentVolumeClaims allow a user to consume abstract storage resources,
it is common that users need PersistentVolumes with varying properties, such as
performance, for different problems. Cluster administrators need to be able to
offer a variety of PersistentVolumes that differ in more ways than size and access
modes, without exposing users to the details of how those volumes are implemented.
For these needs, there is the *StorageClass* resource.

See the [detailed walkthrough with working examples](https://kubernetes.io/docs/tutorials/configuration/configure-persistent-volume-storage/).