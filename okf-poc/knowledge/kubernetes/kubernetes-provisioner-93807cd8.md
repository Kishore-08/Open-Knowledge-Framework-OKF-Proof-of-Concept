---
id: kubernetes-provisioner-93807cd8
type: concept
title: Provisioner
description: Each VolumeAttributesClass has a provisioner that determines what volume
  plugin is used for
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/storage/volume-attributes-classes/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

### Provisioner

Each VolumeAttributesClass has a provisioner that determines what volume plugin is used for
provisioning PVs. The field `driverName` must be specified.

The feature support for VolumeAttributesClass is implemented in
[kubernetes-csi/external-provisioner](https://github.com/kubernetes-csi/external-provisioner).

You are not restricted to specifying the [kubernetes-csi/external-provisioner](https://github.com/kubernetes-csi/external-provisioner).
You can also run and specify external provisioners,
which are independent programs that follow a specification defined by Kubernetes.
Authors of external provisioners have full discretion over where their code lives, how
the provisioner is shipped, how it needs to be run, what volume plugin it uses, etc.

To understand how the provisioner works with VolumeAttributesClass, refer to
the [CSI external-provisioner documentation](https://kubernetes-csi.github.io/docs/external-provisioner.html).