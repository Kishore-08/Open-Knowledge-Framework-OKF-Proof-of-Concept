---
id: kubernetes-class-9fac4033
type: concept
title: Class
description: A claim can request a particular class by specifying the name of a
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/storage/persistent-volumes/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Class

A claim can request a particular class by specifying the name of a
[StorageClass](https://kubernetes.io/docs/concepts/storage/storage-classes/)
using the attribute `storageClassName`.
Only PVs of the requested class, ones with the same `storageClassName` as the PVC,
can be bound to the PVC.

PVCs don't necessarily have to request a class. A PVC with its `storageClassName` set
equal to `""` is always interpreted to be requesting a PV with no class, so it
can only be bound to PVs with no class (no annotation or one set equal to `""`).
A PVC with no `storageClassName` is not quite the same and is treated differently
by the cluster, depending on whether the
[`DefaultStorageClass` admission plugin](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/#defaultstorageclass)
is turned on.

- If the admission plugin is turned on, the administrator may specify a default StorageClass.
  All PVCs that have no `storageClassName` can be bound only to PVs of that default.
  Specifying a default StorageClass is done by setting the annotation
  `storageclass.kubernetes.io/is-default-class` equal to `true` in a StorageClass object.
  If the administrator does not specify a default, the cluster responds to PVC creation
  as if the admission plugin were turned off.
  If more than one default StorageClass is specified, the newest default is used when
  the PVC is dynamically provisioned.
- If the admission plugin is turned off, there is no notion of a default StorageClass.
  All PVCs that have `storageClassName` set to `""` can be bound only to PVs
  that have `storageClassName` also set to `""`.
  However, PVCs with missing `storageClassName` can be updated later once default StorageClass becomes available.
  If the PVC gets updated it will no longer bind to PVs that have `storageClassName` also set to `""`.

See [retroactive default StorageClass assignment](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#retroactive-default-storageclass-assignment) for more details.

Depending on installation method, a default StorageClass may be deployed
to a Kubernetes cluster by addon manager during installation.

When a PVC specifies a `selector` in addition to requesting a StorageClass,
the requirements are ANDed together: only a PV of the requested class and with
the requested labels may be bound to the PVC.

#### Note:

Currently, a PVC with a non-empty `selector` can't have a PV dynamically provisioned for it.

In the past, the annotation `volume.beta.kubernetes.io/storage-class` was used instead
of `storageClassName` attribute. This annotation is still working; however,
it won't be supported in a future Kubernetes release.

#### Retroactive default StorageClass assignment

FEATURE STATE:
`Kubernetes v1.28 [stable]`

You can create a PersistentVolumeClaim without specifying a `storageClassName`
for the new PVC, and you can do so even when no default StorageClass exists
in your cluster. In this case, the new PVC creates as you defined it, and the
`storageClassName` of that PVC remains unset until default becomes available.

When a default StorageClass becomes available, the control plane identifies any
existing PVCs without `storageClassName`. For the PVCs that either have an empty
value for `storageClassName` or do not have this key, the control plane then
updates those PVCs to set `storageClassName` to match the new default StorageClass.
If you have an existing PVC where the `storageClassName` is `""`, and you configure
a default StorageClass, then this PVC will not get updated.

In order to keep binding to PVs with `storageClassName` set to `""`
(while a default StorageClass is present), you need to set the `storageClassName`
of the associated PVC to `""`.

This behavior helps administrators change default StorageClass by removing the
old one first and then creating or setting another one. This brief window while
there is no default causes PVCs without `storageClassName` created at that time
to not ha