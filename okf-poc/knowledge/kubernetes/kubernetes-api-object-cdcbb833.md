---
id: kubernetes-api-object-cdcbb833
type: concept
title: API object
description: The HorizontalPodAutoscaler is an API kind in the Kubernetes
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

## API object

The HorizontalPodAutoscaler is an API kind in the Kubernetes
`autoscaling` API group. The current stable version can be found in
the `autoscaling/v2` API version which includes support for scaling on
memory and custom metrics. The new fields introduced in
`autoscaling/v2` are preserved as annotations when working with
`autoscaling/v1`.

When you create a HorizontalPodAutoscaler API object, make sure the name specified is a valid
[DNS subdomain name](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#dns-subdomain-names).
More details about the API object can be found at
[HorizontalPodAutoscaler Object](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.36/#horizontalpodautoscaler-v2-autoscaling).