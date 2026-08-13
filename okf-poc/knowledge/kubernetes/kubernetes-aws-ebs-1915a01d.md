---
id: kubernetes-aws-ebs-1915a01d
type: concept
title: AWS EBS
description: Kubernetes 1.36 does not include a `awsElasticBlockStore` volume type.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/storage/storage-classes/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

### AWS EBS

Kubernetes 1.36 does not include a `awsElasticBlockStore` volume type.

The AWSElasticBlockStore in-tree storage driver was deprecated in the Kubernetes v1.19 release
and then removed entirely in the v1.27 release.

The Kubernetes project suggests that you use the [AWS EBS](https://github.com/kubernetes-sigs/aws-ebs-csi-driver)
out-of-tree storage driver instead.

Here is an example StorageClass for the AWS EBS CSI driver:

[`storage/storageclass/storageclass-aws-ebs.yaml`](https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples/storage/storageclass/storageclass-aws-ebs.yaml)![](https://kubernetes.io/images/copycode.svg "Copy storage/storageclass/storageclass-aws-ebs.yaml to clipboard")

```
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: ebs-sc
provisioner: ebs.csi.aws.com
volumeBindingMode: WaitForFirstConsumer
parameters:
  csi.storage.k8s.io/fstype: xfs
  type: io1
  iopsPerGB: "50"
  encrypted: "true"
  tagSpecification_1: "key1=value1"
  tagSpecification_2: "key2=value2"
allowedTopologies:
- matchLabelExpressions:
  - key: topology.ebs.csi.aws.com/zone
    values:
    - us-east-2c
```

`tagSpecification`: Tags with this prefix are applied to dynamically provisioned EBS volumes.