---
id: kubernetes-scaling-workloads-vertically-3fee6faa
type: concept
title: Scaling workloads vertically
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/autoscaling/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Scaling workloads vertically

FEATURE STATE:
`Kubernetes v1.25 [stable]`

You can automatically scale a workload vertically using a [VerticalPodAutoscaler](https://kubernetes.io/docs/concepts/workloads/autoscaling/vertical-pod-autoscale/) (VPA).
Unlike the HPA, the VPA doesn't come with Kubernetes by default, but is a an add-on that you or a cluster administrator may need to deploy before you can use it.

Once installed, it allows you to create [CustomResourceDefinitions](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/ "Custom code that defines a resource to add to your Kubernetes API server without building a complete custom server.")
(CRDs) for your workloads which define *how* and *when* to scale the resources of the managed replicas.

#### Note:

You will need to have the [Metrics Server](https://github.com/kubernetes-sigs/metrics-server)
installed to your cluster for the VPA to work.

#### In-place pod vertical scaling

FEATURE STATE:
`Kubernetes v1.35 [stable]`(enabled by default)

As of Kubernetes 1.36, VPA does not support resizing pods in-place,
but this integration is being worked on.
For manually resizing pods in-place, see [Resize Container Resources In-Place](https://kubernetes.io/docs/tasks/configure-pod-container/resize-container-resources/).