---
id: kubernetes-how-pods-with-resource-requests-are-scheduled-d3611dbe
type: concept
title: How Pods with resource requests are scheduled
description: When you create a Pod, the Kubernetes scheduler selects a node for the
  Pod to
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

## How Pods with resource requests are scheduled

When you create a Pod, the Kubernetes scheduler selects a node for the Pod to
run on. Each node has a maximum capacity for each of the resource types: the
amount of CPU and memory it can provide for Pods. The scheduler ensures that,
for each resource type, the sum of the resource requests of the scheduled
containers is less than the capacity of the node.
Note that although actual memory
or CPU resource usage on nodes is very low, the scheduler still refuses to place
a Pod on a node if the capacity check fails. This protects against a resource
shortage on a node when resource usage later increases, for example, during a
daily peak in request rate.