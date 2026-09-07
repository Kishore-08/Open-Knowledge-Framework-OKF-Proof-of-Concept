---
id: kubernetes-aws-efs-1915a01d
type: concept
title: AWS EFS
description: To configure AWS EFS storage, you can use the out-of-tree [AWS\_EFS\_CSI\_DRIVER](https://github.com/kubernetes-sigs/aws-efs-csi-driver).
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/storage/storage-classes/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### AWS EFS

To configure AWS EFS storage, you can use the out-of-tree [AWS\_EFS\_CSI\_DRIVER](https://github.com/kubernetes-sigs/aws-efs-csi-driver).

[`storage/storageclass/storageclass-aws-efs.yaml`](https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples/storage/storageclass/storageclass-aws-efs.yaml)![](https://kubernetes.io/images/copycode.svg "Copy storage/storageclass/storageclass-aws-efs.yaml to clipboard")

```
kind: StorageClass
apiVersion: storage.k8s.io/v1
metadata:
  name: efs-sc
provisioner: efs.csi.aws.com
parameters:
  provisioningMode: efs-ap
  fileSystemId: fs-92107410
  directoryPerms: "700"
```

- `provisioningMode`: The type of volume to be provisioned by Amazon EFS. Currently, only access point based provisioning is supported (`efs-ap`).
- `fileSystemId`: The file system under which the access point is created.
- `directoryPerms`: The directory permissions of the root directory created by the access point.

For more details, refer to the [AWS\_EFS\_CSI\_Driver Dynamic Provisioning](https://github.com/kubernetes-sigs/aws-efs-csi-driver/blob/master/examples/kubernetes/dynamic_provisioning/README.md) documentation.