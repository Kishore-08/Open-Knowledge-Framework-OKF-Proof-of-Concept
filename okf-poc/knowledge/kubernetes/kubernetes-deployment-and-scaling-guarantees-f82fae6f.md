---
id: kubernetes-deployment-and-scaling-guarantees-f82fae6f
type: concept
title: Deployment and Scaling Guarantees
description: '- For a StatefulSet with N replicas, when Pods are being deployed, they
  are created sequentially, in order from {0..N-1}.'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Deployment and Scaling Guarantees

- For a StatefulSet with N replicas, when Pods are being deployed, they are created sequentially, in order from {0..N-1}.
- When Pods are being deleted, they are terminated in reverse order, from {N-1..0}.
- Before a scaling operation is applied to a Pod, all of its predecessors must be Running and Ready. If [`.spec.minReadySeconds`](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/#minimum-ready-seconds) is set, predecessors must be available (Ready for at least `minReadySeconds`).
- Before a Pod is terminated, all of its successors must be completely shutdown.

The StatefulSet should not specify a `pod.Spec.TerminationGracePeriodSeconds` of 0. This practice
is unsafe and strongly discouraged. For further explanation, please refer to
[force deleting StatefulSet Pods](https://kubernetes.io/docs/tasks/run-application/force-delete-stateful-set-pod/).

When the nginx example above is created, three Pods will be deployed in the order
web-0, web-1, web-2. web-1 will not be deployed before web-0 is
[Running and Ready](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/), and web-2 will not be deployed until
web-1 is Running and Ready. If web-0 should fail, after web-1 is Running and Ready, but before
web-2 is launched, web-2 will not be launched until web-0 is successfully relaunched and
becomes Running and Ready.

If a user were to scale the deployed example by patching the StatefulSet such that
`replicas=1`, web-2 would be terminated first. web-1 would not be terminated until web-2
is fully shutdown and deleted. If web-0 were to fail after web-2 has been terminated and
is completely shutdown, but prior to web-1's termination, web-1 would not be terminated
until web-0 is Running and Ready.