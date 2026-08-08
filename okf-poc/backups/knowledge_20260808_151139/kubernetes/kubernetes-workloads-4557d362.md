---
id: kubernetes-workloads-4557d362
type: concept
title: Workloads
description: Your own workload can define its own use of Leases. For example, you
  might run a custom
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/architecture/leases/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Workloads

Your own workload can define its own use of Leases. For example, you might run a custom
[controller](https://kubernetes.io/docs/concepts/architecture/controller/ "A control loop that watches the shared state of the cluster through the apiserver and makes changes attempting to move the current state towards the desired state.") where a primary or leader member
performs operations that its peers do not. You define a Lease so that the controller replicas can select
or elect a leader, using the Kubernetes API for coordination.
If you do use a Lease, it's a good practice to define a name for the Lease that is obviously linked to
the product or component. For example, if you have a component named Example Foo, use a Lease named
`example-foo`.

If a cluster operator or another end user could deploy multiple instances of a component, select a name
prefix and pick a mechanism (such as hash of the name of the Deployment) to avoid name collisions
for the Leases.

You can use another approach so long as it achieves the same outcome: different software products do
not conflict with one another.