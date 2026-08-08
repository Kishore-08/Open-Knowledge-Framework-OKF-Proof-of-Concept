---
id: kubernetes-pod-subresources-6ed556c1
type: concept
title: Pod subresources
description: The above update rules apply to regular pod updates, but other pod fields
  can be updated through *subresources*.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/pods/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Pod subresources

The above update rules apply to regular pod updates, but other pod fields can be updated through *subresources*.

- **Resize:** The `resize` subresource allows container resources (`spec.containers[*].resources`) to be updated.
  See [Resize Container Resources](https://kubernetes.io/docs/tasks/configure-pod-container/resize-container-resources/) for more details.
- **Ephemeral Containers:** The `ephemeralContainers` subresource allows
  [ephemeral containers](https://kubernetes.io/docs/concepts/workloads/pods/ephemeral-containers/ "A type of container type that you can temporarily run inside a Pod")
  to be added to a Pod.
  See [Ephemeral Containers](https://kubernetes.io/docs/concepts/workloads/pods/ephemeral-containers/) for more details.
- **Status:** The `status` subresource allows the pod status to be updated.
  This is typically only used by the Kubelet and other system controllers.
- **Binding:** The `binding` subresource allows setting the pod's `spec.nodeName` via a `Binding` request.
  This is typically only used by the [scheduler](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-scheduler/ "Control plane component that watches for newly created pods with no assigned node, and selects a node for them to run on.").