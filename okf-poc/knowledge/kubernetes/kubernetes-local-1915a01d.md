---
id: kubernetes-local-1915a01d
type: concept
title: Local
description: '[`storage/storageclass/storageclass-local.yaml`](https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples/storage/storageclass/storageclass-local.yaml)![](https://kubernetes.io/im'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/storage/storage-classes/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Local

[`storage/storageclass/storageclass-local.yaml`](https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples/storage/storageclass/storageclass-local.yaml)![](https://kubernetes.io/images/copycode.svg "Copy storage/storageclass/storageclass-local.yaml to clipboard")

```
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: local-storage
provisioner: kubernetes.io/no-provisioner # indicates that this StorageClass does not support automatic provisioning
volumeBindingMode: WaitForFirstConsumer
```

Local volumes do not support dynamic provisioning in Kubernetes 1.37;
however a StorageClass should still be created to delay volume binding until a Pod is actually
scheduled to the appropriate node. This is specified by the `WaitForFirstConsumer` volume
binding mode.

Delaying volume binding allows the scheduler to consider all of a Pod's
scheduling constraints when choosing an appropriate PersistentVolume for a
PersistentVolumeClaim.