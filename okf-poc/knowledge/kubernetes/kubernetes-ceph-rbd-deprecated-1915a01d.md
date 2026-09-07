---
id: kubernetes-ceph-rbd-deprecated-1915a01d
type: concept
title: Ceph RBD (deprecated)
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/storage/storage-classes/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Ceph RBD (deprecated)

#### Note:

FEATURE STATE:
`Kubernetes v1.28 [deprecated]`

This internal provisioner of Ceph RBD is deprecated. Please use
[CephFS RBD CSI driver](https://github.com/ceph/ceph-csi).

[`storage/storageclass/storageclass-ceph-rbd.yaml`](https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples/storage/storageclass/storageclass-ceph-rbd.yaml)![](https://kubernetes.io/images/copycode.svg "Copy storage/storageclass/storageclass-ceph-rbd.yaml to clipboard")

```
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: fast
provisioner: kubernetes.io/rbd # This provisioner is deprecated
parameters:
  monitors: 198.19.254.105:6789
  adminId: kube
  adminSecretName: ceph-secret
  adminSecretNamespace: kube-system
  pool: kube
  userId: kube
  userSecretName: ceph-secret-user
  userSecretNamespace: default
  fsType: ext4
  imageFormat: "2"
  imageFeatures: "layering"
```

- `monitors`: Ceph monitors, comma delimited. This parameter is required.
- `adminId`: Ceph client ID that is capable of creating images in the pool.
  Default is "admin".
- `adminSecretName`: Secret Name for `adminId`. This parameter is required.
  The provided secret must have type "kubernetes.io/rbd".
- `adminSecretNamespace`: The namespace for `adminSecretName`. Default is "default".
- `pool`: Ceph RBD pool. Default is "rbd".
- `userId`: Ceph client ID that is used to map the RBD image. Default is the
  same as `adminId`.
- `userSecretName`: The name of Ceph Secret for `userId` to map RBD image. It
  must exist in the same namespace as PVCs. This parameter is required.
  The provided secret must have type "kubernetes.io/rbd", for example created in this
  way:

  ```
  kubectl create secret generic ceph-secret --type="kubernetes.io/rbd" \
    --from-literal=key='QVFEQ1pMdFhPUnQrSmhBQUFYaERWNHJsZ3BsMmNjcDR6RFZST0E9PQ==' \
    --namespace=kube-system
  ```
- `userSecretNamespace`: The namespace for `userSecretName`.
- `fsType`: fsType that is supported by kubernetes. Default: `"ext4"`.
- `imageFormat`: Ceph RBD image format, "1" or "2". Default is "2".
- `imageFeatures`: This parameter is optional and should only be used if you
  set `imageFormat` to "2". Currently supported features are `layering` only.
  Default is "", and no features are turned on.