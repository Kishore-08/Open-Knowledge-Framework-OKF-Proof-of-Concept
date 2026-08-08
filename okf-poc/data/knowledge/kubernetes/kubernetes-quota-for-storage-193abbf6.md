---
id: kubernetes-quota-for-storage-193abbf6
type: concept
title: Quota for storage
description: You can limit the total sum of [storage](https://kubernetes.io/docs/concepts/storage/persistent-volumes/)
  for volumes
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/policy/resource-quotas/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Quota for storage

You can limit the total sum of [storage](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) for volumes
that can be requested in a given namespace.

In addition, you can limit consumption of storage resources based on associated
[StorageClass](https://kubernetes.io/docs/concepts/storage/storage-classes/).

| Resource Name | Description |
| --- | --- |
| `requests.storage` | Across all persistent volume claims, the sum of storage requests cannot exceed this value. |
| `persistentvolumeclaims` | The total number of [PersistentVolumeClaims](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims) that can exist in the namespace. |
| `<storage-class-name>.storageclass.storage.k8s.io/requests.storage` | Across all persistent volume claims associated with the `<storage-class-name>`, the sum of storage requests cannot exceed this value. |
| `<storage-class-name>.storageclass.storage.k8s.io/persistentvolumeclaims` | Across all persistent volume claims associated with the `<storage-class-name>`, the total number of [persistent volume claims](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims) that can exist in the namespace. |

For example, if you want to quota storage with `gold` StorageClass separate from
a `bronze` StorageClass, you can define a quota as follows:

- `gold.storageclass.storage.k8s.io/requests.storage: 500Gi`
- `bronze.storageclass.storage.k8s.io/requests.storage: 100Gi`

#### Quota for local ephemeral storage

FEATURE STATE:
`Kubernetes v1.8 [alpha]`

| Resource Name | Description |
| --- | --- |
| `requests.ephemeral-storage` | Across all pods in the namespace, the sum of local ephemeral storage requests cannot exceed this value. |
| `limits.ephemeral-storage` | Across all pods in the namespace, the sum of local ephemeral storage limits cannot exceed this value. |
| `ephemeral-storage` | Same as `requests.ephemeral-storage`. |

#### Note:

When using a CRI container runtime, container logs will count against the ephemeral storage quota.
This can result in the unexpected eviction of pods that have exhausted their storage quotas.

Refer to [Logging Architecture](https://kubernetes.io/docs/concepts/cluster-administration/logging/) for details.