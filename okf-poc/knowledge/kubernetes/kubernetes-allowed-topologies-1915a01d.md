---
id: kubernetes-allowed-topologies-1915a01d
type: concept
title: Allowed topologies
description: When a cluster operator specifies the `WaitForFirstConsumer` volume binding
  mode, it is no longer necessary
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/storage/storage-classes/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Allowed topologies

When a cluster operator specifies the `WaitForFirstConsumer` volume binding mode, it is no longer necessary
to restrict provisioning to specific topologies in most situations. However,
if still required, `allowedTopologies` can be specified.

This example demonstrates how to restrict the topology of provisioned volumes to specific
zones and should be used as a replacement for the `zone` and `zones` parameters for the
supported plugins.

[`storage/storageclass/storageclass-topology.yaml`](https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples/storage/storageclass/storageclass-topology.yaml)![](https://kubernetes.io/images/copycode.svg "Copy storage/storageclass/storageclass-topology.yaml to clipboard")

```
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: standard
provisioner:  example.com/example
parameters:
  type: pd-standard
volumeBindingMode: WaitForFirstConsumer
allowedTopologies:
- matchLabelExpressions:
  - key: topology.kubernetes.io/zone
    values:
    - us-central-1a
    - us-central-1b
```