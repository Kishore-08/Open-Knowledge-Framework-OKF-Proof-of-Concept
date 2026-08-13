---
id: kubernetes-storageclass-objects-1915a01d
type: concept
title: StorageClass objects
description: Each StorageClass contains the fields `provisioner`, `parameters`, and
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/storage/storage-classes/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

## StorageClass objects

Each StorageClass contains the fields `provisioner`, `parameters`, and
`reclaimPolicy`, which are used when a PersistentVolume belonging to the
class needs to be dynamically provisioned to satisfy a PersistentVolumeClaim (PVC).

The name of a StorageClass object is significant, and is how users can
request a particular class. Administrators set the name and other parameters
of a class when first creating StorageClass objects.

As an administrator, you can specify a default StorageClass that applies to any PVCs that
don't request a specific class. For more details, see the
[PersistentVolumeClaim concept](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims).

Here's an example of a StorageClass:

[`storage/storageclass-low-latency.yaml`](https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples/storage/storageclass-low-latency.yaml)![](https://kubernetes.io/images/copycode.svg "Copy storage/storageclass-low-latency.yaml to clipboard")

```
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: low-latency
  annotations:
    storageclass.kubernetes.io/is-default-class: "false"
provisioner: csi-driver.example-vendor.example
reclaimPolicy: Retain # default value is Delete
allowVolumeExpansion: true
mountOptions:
  - discard # this might enable UNMAP / TRIM at the block storage layer
volumeBindingMode: WaitForFirstConsumer
parameters:
  guaranteedReadWriteLatency: "true" # provider-specific
```