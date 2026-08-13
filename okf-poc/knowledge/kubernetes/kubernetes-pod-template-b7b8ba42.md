---
id: kubernetes-pod-template-b7b8ba42
type: concept
title: Pod Template
description: The `.spec.template` is one of the required fields in `.spec`.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

### Pod Template

The `.spec.template` is one of the required fields in `.spec`.

The `.spec.template` is a [pod template](https://kubernetes.io/docs/concepts/workloads/pods/#pod-templates).
It has exactly the same schema as a [Pod](https://kubernetes.io/docs/concepts/workloads/pods/ "A Pod represents a set of running containers in your cluster."),
except it is nested and does not have an `apiVersion` or `kind`.

In addition to required fields for a Pod, a Pod template in a DaemonSet has to specify appropriate
labels (see [pod selector](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/#pod-selector)).

A Pod Template in a DaemonSet must have a [`RestartPolicy`](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#restart-policy)
equal to `Always`, or be unspecified, which defaults to `Always`.