---
id: kubernetes-writing-portable-configuration-9fac4033
type: concept
title: Writing Portable Configuration
description: If you're writing configuration templates or examples that run on a wide
  range of clusters
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/storage/persistent-volumes/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Writing Portable Configuration

If you're writing configuration templates or examples that run on a wide range of clusters
and need persistent storage, it is recommended that you use the following pattern:

- Include PersistentVolumeClaim objects in your bundle of config (alongside
  Deployments, ConfigMaps, etc).
- Do not include PersistentVolume objects in the config, since the user instantiating
  the config may not have permission to create PersistentVolumes.
- Give the user the option of providing a storage class name when instantiating
  the template.
  - If the user provides a storage class name, put that value into the
    `persistentVolumeClaim.storageClassName` field.
    This will cause the PVC to match the right storage
    class if the cluster has StorageClasses enabled by the admin.
  - If the user does not provide a storage class name, leave the
    `persistentVolumeClaim.storageClassName` field as nil. This will cause a
    PV to be automatically provisioned for the user with the default StorageClass
    in the cluster. Many cluster environments have a default StorageClass installed,
    or administrators can create their own default StorageClass.
- In your tooling, watch for PVCs that are not getting bound after some time
  and surface this to the user, as this may indicate that the cluster has no
  dynamic storage support (in which case the user should create a matching PV)
  or the cluster has no storage system (in which case the user cannot deploy
  config requiring PVCs).