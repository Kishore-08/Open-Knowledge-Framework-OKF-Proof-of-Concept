---
id: kubernetes-status-for-pod-readiness-3e34f258
type: concept
title: Status for Pod readiness
description: The `kubectl patch` command does not support patching object status.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Status for Pod readiness

The `kubectl patch` command does not support patching object status.
To set these `status.conditions` for the Pod, applications and
[operators](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/ "A specialized controller used to manage a custom resource") should use
the `PATCH` action.
You can use a [Kubernetes client library](https://kubernetes.io/docs/reference/using-api/client-libraries/) to
write code that sets custom Pod conditions for Pod readiness.

For a Pod that uses custom conditions, that Pod is evaluated to be ready **only**
when both the following statements apply:

- All containers in the Pod are ready.
- All conditions specified in `readinessGates` are `True`.

When a Pod's containers are Ready but at least one custom condition is missing or
`False`, the kubelet sets the Pod's [condition](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-conditions) to `ContainersReady`.