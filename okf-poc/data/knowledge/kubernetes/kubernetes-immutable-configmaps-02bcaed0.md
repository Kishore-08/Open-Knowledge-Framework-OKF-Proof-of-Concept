---
id: kubernetes-immutable-configmaps-02bcaed0
type: concept
title: Immutable ConfigMaps
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/configuration/configmap/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Immutable ConfigMaps

FEATURE STATE:
`Kubernetes v1.21 [stable]`

The Kubernetes feature *Immutable Secrets and ConfigMaps* provides an option to set
individual Secrets and ConfigMaps as immutable. For clusters that extensively use ConfigMaps
(at least tens of thousands of unique ConfigMap to Pod mounts), preventing changes to their
data has the following advantages:

- protects you from accidental (or unwanted) updates that could cause applications outages
- improves performance of your cluster by significantly reducing load on kube-apiserver, by
  closing watches for ConfigMaps marked as immutable.

You can create an immutable ConfigMap by setting the `immutable` field to `true`.
For example:

```
apiVersion: v1
kind: ConfigMap
metadata:
  ...
data:
  ...
immutable: true
```

Once a ConfigMap is marked as immutable, it is *not* possible to revert this change
nor to mutate the contents of the `data` or the `binaryData` field. You can
only delete and recreate the ConfigMap. Because existing Pods maintain a mount point
to the deleted ConfigMap, it is recommended to recreate these pods.