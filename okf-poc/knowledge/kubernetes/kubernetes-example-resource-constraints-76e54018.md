---
id: kubernetes-example-resource-constraints-76e54018
type: concept
title: Example resource constraints
description: 'Examples of policies that could be created using LimitRange are:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/policy/limit-range/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Example resource constraints

Examples of policies that could be created using LimitRange are:

- In a 2 node cluster with a capacity of 8 GiB RAM and 16 cores, constrain Pods in a
  namespace to request 100m of CPU with a max limit of 500m for CPU and request 200Mi
  for Memory with a max limit of 600Mi for Memory.
- Define default CPU limit and request to 150m and memory default request to 300Mi for
  Containers started with no cpu and memory requests in their specs.

In the case where the total limits of the namespace is less than the sum of the limits
of the Pods/Containers, there may be contention for resources. In this case, the
Containers or Pods will not be created.

Neither contention nor changes to a LimitRange will affect already created resources.