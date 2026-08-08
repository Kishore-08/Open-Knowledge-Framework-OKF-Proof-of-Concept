---
id: kubernetes-workload-resources-and-pod-templates-ebd20ed7
type: concept
title: Workload resources and Pod templates
description: Pods are often created indirectly, by creating a [workload
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/security/pod-security-admission/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Workload resources and Pod templates

Pods are often created indirectly, by creating a [workload
object](https://kubernetes.io/docs/concepts/workloads/controllers/) such as a [Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/ "Manages a replicated application on your cluster.") or [Job](https://kubernetes.io/docs/concepts/workloads/controllers/job/ "A finite or batch task that runs to completion."). The workload object defines a
*Pod template* and a [controller](https://kubernetes.io/docs/concepts/architecture/controller/ "A control loop that watches the shared state of the cluster through the apiserver and makes changes attempting to move the current state towards the desired state.") for the
workload resource creates Pods based on that template. To help catch violations early, both the
audit and warning modes are applied to the workload resources. However, enforce mode is **not**
applied to workload resources, only to the resulting pod objects.