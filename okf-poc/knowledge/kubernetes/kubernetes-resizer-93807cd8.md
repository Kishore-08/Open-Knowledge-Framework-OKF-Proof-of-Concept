---
id: kubernetes-resizer-93807cd8
type: concept
title: Resizer
description: Each VolumeAttributesClass has a resizer that determines what volume
  plugin is used
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/storage/volume-attributes-classes/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Resizer

Each VolumeAttributesClass has a resizer that determines what volume plugin is used
for modifying PVs. The field `driverName` must be specified.

The modifying volume feature support for VolumeAttributesClass is implemented in
[kubernetes-csi/external-resizer](https://github.com/kubernetes-csi/external-resizer).

For example, an existing PersistentVolumeClaim is using a VolumeAttributesClass named silver:

```
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: test-pv-claim
spec:
  …
  volumeAttributesClassName: silver
  …
```

A new VolumeAttributesClass gold is available in the cluster:

```
apiVersion: storage.k8s.io/v1
kind: VolumeAttributesClass
metadata:
  name: gold
driverName: pd.csi.storage.gke.io
parameters:
  iops: "4000"
  throughput: "60"
```

The end user can update the PVC with the new VolumeAttributesClass gold and apply:

```
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: test-pv-claim
spec:
  …
  volumeAttributesClassName: gold
  …
```

To understand how the resizer works with VolumeAttributesClass, refer to
the [CSI external-resizer documentation](https://kubernetes-csi.github.io/docs/external-resizer.html).