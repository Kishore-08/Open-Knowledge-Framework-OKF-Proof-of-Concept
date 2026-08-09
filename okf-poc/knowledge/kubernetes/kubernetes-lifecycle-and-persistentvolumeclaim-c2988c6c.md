---
id: kubernetes-lifecycle-and-persistentvolumeclaim-c2988c6c
type: concept
title: Lifecycle and PersistentVolumeClaim
description: The key design idea is that the
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/storage/ephemeral-volumes/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Lifecycle and PersistentVolumeClaim

The key design idea is that the
[parameters for a volume claim](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.36/#ephemeralvolumesource-v1-core)
are allowed inside a volume source of the Pod. Labels, annotations and
the whole set of fields for a PersistentVolumeClaim are supported. When such a Pod gets
created, the ephemeral volume controller then creates an actual PersistentVolumeClaim
object in the same namespace as the Pod and ensures that the PersistentVolumeClaim
gets deleted when the Pod gets deleted.

That triggers volume binding and/or provisioning, either immediately if
the [StorageClass](https://kubernetes.io/docs/concepts/storage/storage-classes "A StorageClass provides a way for administrators to describe different available storage types.") uses immediate volume binding or when the Pod is
tentatively scheduled onto a node (`WaitForFirstConsumer` volume
binding mode). The latter is recommended for generic ephemeral volumes
because then the scheduler is free to choose a suitable node for
the Pod. With immediate binding, the scheduler is forced to select a node that has
access to the volume once it is available.

In terms of [resource ownership](https://kubernetes.io/docs/concepts/architecture/garbage-collection/#owners-dependents),
a Pod that has generic ephemeral storage is the owner of the PersistentVolumeClaim(s)
that provide that ephemeral storage. When the Pod is deleted,
the Kubernetes garbage collector deletes the PVC, which then usually
triggers deletion of the volume because the default reclaim policy of
storage classes is to delete volumes. You can create quasi-ephemeral local storage
using a StorageClass with a reclaim policy of `retain`: the storage outlives the Pod,
and in this case you need to ensure that volume clean up happens separately.

While these PVCs exist, they can be used like any other PVC. In
particular, they can be referenced as data source in volume cloning or
snapshotting. The PVC object also holds the current status of the
volume.