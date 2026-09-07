---
id: kubernetes-pod-template-bc994bad
type: concept
title: Pod Template
description: The `.spec.template` is the only required field of the `.spec`.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/job/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Pod Template

The `.spec.template` is the only required field of the `.spec`.

The `.spec.template` is a [pod template](https://kubernetes.io/docs/concepts/workloads/pods/#pod-templates).
It has exactly the same schema as a [Pod](https://kubernetes.io/docs/concepts/workloads/pods/ "A Pod represents a set of running containers in your cluster."),
except it is nested and does not have an `apiVersion` or `kind`.

In addition to required fields for a Pod, a pod template in a Job must specify appropriate
labels (see [pod selector](https://kubernetes.io/docs/concepts/workloads/controllers/job/#pod-selector)) and an appropriate restart policy.

Only a [`RestartPolicy`](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#restart-policy)
equal to `Never` or `OnFailure` is allowed.