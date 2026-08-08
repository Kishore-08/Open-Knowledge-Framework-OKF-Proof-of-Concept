---
id: kubernetes-maximum-parallel-image-pulls-c440e1a7
type: concept
title: Maximum parallel image pulls
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/containers/images/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Maximum parallel image pulls

FEATURE STATE:
`Kubernetes v1.35 [stable]`

When `serializeImagePulls` is set to false, the kubelet defaults to no limit on
the maximum number of images being pulled at the same time. If you would like to
limit the number of parallel image pulls, you can set the field `maxParallelImagePulls`
in the kubelet configuration. With `maxParallelImagePulls` set to *n*, only *n*
images can be pulled at the same time, and any image pull beyond *n* will have to
wait until at least one ongoing image pull is complete.

Limiting the number of parallel image pulls prevents image pulling from consuming
too much network bandwidth or disk I/O, when parallel image pulling is enabled.

You can set `maxParallelImagePulls` to a positive number that is greater than or
equal to 1. If you set `maxParallelImagePulls` to be greater than or equal to 2,
you must set `serializeImagePulls` to false. The kubelet will fail to start
with an invalid `maxParallelImagePulls` setting.