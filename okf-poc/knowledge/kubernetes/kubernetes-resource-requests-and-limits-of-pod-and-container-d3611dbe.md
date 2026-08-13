---
id: kubernetes-resource-requests-and-limits-of-pod-and-container-d3611dbe
type: concept
title: Resource requests and limits of Pod and container
description: For each container, you can specify resource limits and requests,
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

## Resource requests and limits of Pod and container

For each container, you can specify resource limits and requests,
including the following:

- `spec.containers[].resources.limits.cpu`
- `spec.containers[].resources.limits.memory`
- `spec.containers[].resources.limits.ephemeral-storage`
- `spec.containers[].resources.limits.hugepages-<size>`
- `spec.containers[].resources.requests.cpu`
- `spec.containers[].resources.requests.memory`
- `spec.containers[].resources.requests.ephemeral-storage`
- `spec.containers[].resources.requests.hugepages-<size>`

Although you can only specify requests and limits for individual containers,
it is also useful to think about the overall resource requests and limits for
a Pod.
For a particular resource, a *Pod resource request/limit* is the sum of the
resource requests/limits of that type for each container in the Pod.