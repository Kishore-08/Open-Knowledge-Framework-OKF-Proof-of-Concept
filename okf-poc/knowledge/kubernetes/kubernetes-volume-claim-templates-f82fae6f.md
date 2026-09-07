---
id: kubernetes-volume-claim-templates-f82fae6f
type: concept
title: Volume Claim Templates
description: You can set the `.spec.volumeClaimTemplates` field to create a
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Volume Claim Templates

You can set the `.spec.volumeClaimTemplates` field to create a
[PersistentVolumeClaim](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims).
This will provide stable storage to the StatefulSet if either:

- The StorageClass specified for the volume claim is set up to use [dynamic
  provisioning](https://kubernetes.io/docs/concepts/storage/dynamic-provisioning/).
- The cluster already contains a PersistentVolume with the correct StorageClass
  and sufficient available storage space.