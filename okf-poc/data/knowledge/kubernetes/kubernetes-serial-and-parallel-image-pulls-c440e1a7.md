---
id: kubernetes-serial-and-parallel-image-pulls-c440e1a7
type: concept
title: Serial and parallel image pulls
description: By default, the kubelet pulls images serially. In other words, the kubelet
  sends
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/containers/images/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Serial and parallel image pulls

By default, the kubelet pulls images serially. In other words, the kubelet sends
only one image pull request to the image service at a time. Other image pull
requests have to wait until the one being processed is complete.

Nodes make image pull decisions in isolation. Even when you use serialized image
pulls, two different nodes can pull the same image in parallel.

If you would like to enable parallel image pulls, you can set the field
`serializeImagePulls` to false in the [kubelet configuration](https://kubernetes.io/docs/reference/config-api/kubelet-config.v1beta1/).
With `serializeImagePulls` set to false, image pull requests will be sent to the image service immediately,
and multiple images will be pulled at the same time.

When enabling parallel image pulls, ensure that the image service of your container
runtime can handle parallel image pulls.

The kubelet never pulls multiple images in parallel on behalf of one Pod. For example,
if you have a Pod that has an init container and an application container, the image
pulls for the two containers will not be parallelized. However, if you have two
Pods that use different images, and the parallel image pull feature is enabled,
the kubelet will pull the images in parallel on behalf of the two different Pods.