---
id: kubernetes-node-affinity-9fac4033
type: concept
title: Node Affinity
description: For most volume types, you do not need to set this field.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/storage/persistent-volumes/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Node Affinity

#### Note:

For most volume types, you do not need to set this field.
You need to explicitly set this for [local](https://kubernetes.io/docs/concepts/storage/volumes/#local) volumes.

A PV can specify node affinity to define constraints that limit what nodes this
volume can be accessed from. Pods that use a PV will only be scheduled to nodes
that are selected by the node affinity. To specify node affinity, set
`nodeAffinity` in the `.spec` of a PV. The
[PersistentVolume](https://kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/persistent-volume-v1/#PersistentVolumeSpec)
API reference has more details on this field.

#### Updates to node affinity

FEATURE STATE:
`Kubernetes v1.35 [alpha]`(disabled by default)

If the `MutablePVNodeAffinity` [feature gate](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/) is enabled in your cluster,
the `.spec.nodeAffinity` field of a PersistentVolume is mutable.
This allows cluster administrators or external storage controller to update the node affinity of a PersistentVolume when the data is migrated,
without interrupting the running pods.

When updating the node affinity, you should ensure that the new node affinity still matches the nodes where the volume is currently in use.
For the pods violating the new affinity, if the pod is already running, it may continue to run. But Kubernetes does not support this configuration.
You should terminate the violating pods soon.
Due to in memory caching, the pods created after the update may still be scheduled according to the old node affinity for a short period of time.

To use this feature, you should enable the `MutablePVNodeAffinity` feature gate on the following components:

- `kube-apiserver`
- `kubelet`