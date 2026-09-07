---
id: kubernetes-azure-file-deprecated-1915a01d
type: concept
title: Azure File (deprecated)
description: '[`storage/storageclass/storageclass-azure-file.yaml`](https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples/storage/storageclass/storageclass-azure-file.yaml)![](https://kubern'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/storage/storage-classes/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Azure File (deprecated)

[`storage/storageclass/storageclass-azure-file.yaml`](https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples/storage/storageclass/storageclass-azure-file.yaml)![](https://kubernetes.io/images/copycode.svg "Copy storage/storageclass/storageclass-azure-file.yaml to clipboard")

```
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: azurefile
provisioner: kubernetes.io/azure-file
parameters:
  skuName: Standard_LRS
  location: eastus
  storageAccount: azure_storage_account_name # example value
```

- `skuName`: Azure storage account SKU tier. Default is empty.
- `location`: Azure storage account location. Default is empty.
- `storageAccount`: Azure storage account name. Default is empty. If a storage
  account is not provided, all storage accounts associated with the resource
  group are searched to find one that matches `skuName` and `location`. If a
  storage account is provided, it must reside in the same resource group as the
  cluster, and `skuName` and `location` are ignored.
- `secretNamespace`: the namespace of the secret that contains the Azure Storage
  Account Name and Key. Default is the same as the Pod.
- `secretName`: the name of the secret that contains the Azure Storage Account Name and
  Key. Default is `azure-storage-account-<accountName>-secret`
- `readOnly`: a flag indicating whether the storage will be mounted as read only.
  Defaults to false which means a read/write mount. This setting will impact the
  `ReadOnly` setting in VolumeMounts as well.

During storage provisioning, a secret named by `secretName` is created for the
mounting credentials. If the cluster has enabled both
[RBAC](https://kubernetes.io/docs/reference/access-authn-authz/rbac/) and
[Controller Roles](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#controller-roles),
add the `create` permission of resource `secret` for clusterrole
`system:controller:persistent-volume-binder`.

In a multi-tenancy context, it is strongly recommended to set the value for
`secretNamespace` explicitly, otherwise the storage account credentials may
be read by other users.