---
id: kubernetes-the-volumeattributesclass-api-93807cd8
type: concept
title: The VolumeAttributesClass API
description: Each VolumeAttributesClass contains the `driverName` and `parameters`,
  which are
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/storage/volume-attributes-classes/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

## The VolumeAttributesClass API

Each VolumeAttributesClass contains the `driverName` and `parameters`, which are
used when a PersistentVolume (PV) belonging to the class needs to be dynamically provisioned
or modified.

The name of a VolumeAttributesClass object is significant and is how users can request a particular class.
Administrators set the name and other parameters of a class when first creating VolumeAttributesClass objects.
While the name of a VolumeAttributesClass object in a `PersistentVolumeClaim` is mutable, the parameters in an existing class are immutable.

```
apiVersion: storage.k8s.io/v1
kind: VolumeAttributesClass
metadata:
  name: silver
driverName: pd.csi.storage.gke.io
parameters:
  provisioned-iops: "3000"
  provisioned-throughput: "50"
```