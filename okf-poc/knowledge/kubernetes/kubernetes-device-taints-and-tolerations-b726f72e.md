---
id: kubernetes-device-taints-and-tolerations-b726f72e
type: concept
title: Device taints and tolerations
description: Instead of tainting entire nodes, administrators can also [taint individual
  devices](https://kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation#device-taints-and-tolerations)
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

## Device taints and tolerations

Instead of tainting entire nodes, administrators can also [taint individual devices](https://kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation#device-taints-and-tolerations)
when the cluster uses [dynamic resource allocation](https://kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation)
to manage special hardware. The advantage is that tainting can be targeted towards exactly the hardware that
is faulty or needs maintenance. Tolerations are also supported and can be specified when requesting
devices. Like taints they apply to all pods which share the same allocated device.