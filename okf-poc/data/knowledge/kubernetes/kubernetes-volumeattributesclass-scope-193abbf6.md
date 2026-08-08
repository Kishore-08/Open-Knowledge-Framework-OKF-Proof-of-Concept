---
id: kubernetes-volumeattributesclass-scope-193abbf6
type: concept
title: VolumeAttributesClass scope
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/policy/resource-quotas/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### VolumeAttributesClass scope

FEATURE STATE:
`Kubernetes v1.36 [stable]`(enabled by default)

This scope only tracks quota consumed by PersistentVolumeClaims.

PersistentVolumeClaims can be created with a specific
[VolumeAttributesClass](https://kubernetes.io/docs/concepts/storage/volume-attributes-classes/), and might be modified after creation.
You can control a PVC's consumption of storage resources based on the associated
VolumeAttributesClasses, by using the `scopeSelector` field in the quota spec.

The PVC references the associated VolumeAttributesClass by the following fields:

- `spec.volumeAttributesClassName`
- `status.currentVolumeAttributesClassName`
- `status.modifyVolumeStatus.targetVolumeAttributesClassName`

A relevant ResourceQuota is matched and consumed only if the ResourceQuota has a `scopeSelector` that selects the PVC.

When the quota is scoped for the volume attributes class using the `scopeSelector` field, the quota object is restricted to track only the following resources:

- `persistentvolumeclaims`
- `requests.storage`

Read [Limit Storage Consumption](https://kubernetes.io/docs/tasks/administer-cluster/limit-storage-consumption/) to learn more about this.