---
id: kubernetes-what-s-next-f82fae6f
type: concept
title: What's next
description: '- Learn about [Pods](https://kubernetes.io/docs/concepts/workloads/pods/).'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

## What's next

- Learn about [Pods](https://kubernetes.io/docs/concepts/workloads/pods/).
- Find out how to use StatefulSets
  - Follow an example of [deploying a stateful application](https://kubernetes.io/docs/tutorials/stateful-application/basic-stateful-set/).
  - Follow an example of [deploying Cassandra with Stateful Sets](https://kubernetes.io/docs/tutorials/stateful-application/cassandra/).
  - Follow an example of [running a replicated stateful application](https://kubernetes.io/docs/tasks/run-application/run-replicated-stateful-application/).
  - Learn how to [scale a StatefulSet](https://kubernetes.io/docs/tasks/run-application/scale-stateful-set/).
  - Learn what's involved when you [delete a StatefulSet](https://kubernetes.io/docs/tasks/run-application/delete-stateful-set/).
  - Learn how to [configure a Pod to use a volume for storage](https://kubernetes.io/docs/tasks/configure-pod-container/configure-volume-storage/).
  - Learn how to [configure a Pod to use a PersistentVolume for storage](https://kubernetes.io/docs/tutorials/configuration/configure-persistent-volume-storage/).
- `StatefulSet` is a top-level resource in the Kubernetes REST API.
  Read the
  [StatefulSet](https://kubernetes.io/docs/reference/kubernetes-api/apps/stateful-set-v1/)
  object definition to understand the API for stateful sets.
- Read about [PodDisruptionBudget](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/) and how
  you can use it to manage application availability during disruptions.