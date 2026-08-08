---
id: kubernetes-csi-driver-restrictions-c2988c6c
type: concept
title: CSI driver restrictions
description: CSI ephemeral volumes allow users to provide `volumeAttributes`
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/storage/ephemeral-volumes/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### CSI driver restrictions

CSI ephemeral volumes allow users to provide `volumeAttributes`
directly to the CSI driver as part of the Pod spec. A CSI driver
allowing `volumeAttributes` that are typically restricted to
administrators is NOT suitable for use in an inline ephemeral volume.
For example, parameters that are normally defined in the StorageClass
should not be exposed to users through the use of inline ephemeral volumes.

Cluster administrators who need to restrict the CSI drivers that are
allowed to be used as inline volumes within a Pod spec may do so by:

- Removing `Ephemeral` from `volumeLifecycleModes` in the CSIDriver spec, which prevents the
  driver from being used as an inline ephemeral volume.
- Using an [admission webhook](https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/)
  to restrict how this driver is used.