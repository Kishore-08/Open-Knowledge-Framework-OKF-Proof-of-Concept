---
id: kubernetes-status-for-pod-readiness-9184beed
type: concept
title: Status for Pod readiness
description: To set these `status.conditions` for the Pod, applications and
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/pods/pod-condition/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

### Status for Pod readiness

To set these `status.conditions` for the Pod, applications and
[operators](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/ "A specialized controller used to manage a custom resource") should use
the `PATCH` action on the Pod's status subresource. You can use `kubectl patch`
with `--subresource=status`, or a [Kubernetes client library](https://kubernetes.io/docs/reference/using-api/client-libraries/) to write
code that sets custom Pod conditions for Pod readiness.

For a Pod that uses custom conditions, that Pod is evaluated to be ready **only** when both the following statements apply:

- All containers in the Pod are ready.
- All conditions specified in `readinessGates` are `True`.

When a Pod's containers are Ready but at least one custom condition is missing or `False`,
the kubelet sets the Pod's `Ready` condition to `status: "False"` with `reason: ReadinessGatesNotReady`.