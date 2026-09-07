---
id: kubernetes-nfs-1915a01d
type: concept
title: NFS
description: To configure NFS storage, you can use the in-tree driver or the
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/storage/storage-classes/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### NFS

To configure NFS storage, you can use the in-tree driver or the
[NFS CSI driver for Kubernetes](https://github.com/kubernetes-csi/csi-driver-nfs#readme)
(recommended).

[`storage/storageclass/storageclass-nfs.yaml`](https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples/storage/storageclass/storageclass-nfs.yaml)![](https://kubernetes.io/images/copycode.svg "Copy storage/storageclass/storageclass-nfs.yaml to clipboard")

```
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: example-nfs
provisioner: example.com/external-nfs
parameters:
  server: nfs-server.example.com
  path: /share
  readOnly: "false"
```

- `server`: Server is the hostname or IP address of the NFS server.
- `path`: Path that is exported by the NFS server.
- `readOnly`: A flag indicating whether the storage will be mounted as read only (default false).

Kubernetes doesn't include an internal NFS provisioner.
You need to use an external provisioner to create a StorageClass for NFS.
Here are some examples:

- [NFS Ganesha server and external provisioner](https://github.com/kubernetes-sigs/nfs-ganesha-server-and-external-provisioner)
- [NFS subdir external provisioner](https://github.com/kubernetes-sigs/nfs-subdir-external-provisioner)