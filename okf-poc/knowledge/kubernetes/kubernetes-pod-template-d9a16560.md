---
id: kubernetes-pod-template-d9a16560
type: concept
title: Pod Template
description: The `.spec.template` and `.spec.selector` are the only required fields
  of the `.spec`.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/deployment/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Pod Template

The `.spec.template` and `.spec.selector` are the only required fields of the `.spec`.

The `.spec.template` is a [Pod template](https://kubernetes.io/docs/concepts/workloads/pods/#pod-templates). It has exactly the same schema as a [Pod](https://kubernetes.io/docs/concepts/workloads/pods/ "A Pod represents a set of running containers in your cluster."), except it is nested and does not have an `apiVersion` or `kind`.

In addition to required fields for a Pod, a Pod template in a Deployment must specify appropriate
labels and an appropriate restart policy. For labels, make sure not to overlap with other controllers. See [selector](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#selector).

Only a [`.spec.template.spec.restartPolicy`](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#restart-policy) equal to `Always` is
allowed, which is the default if not specified.