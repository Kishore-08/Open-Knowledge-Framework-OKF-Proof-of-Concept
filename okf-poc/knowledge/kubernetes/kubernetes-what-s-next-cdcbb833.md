---
id: kubernetes-what-s-next-cdcbb833
type: concept
title: What's next
description: If you configure autoscaling in your cluster, you may also want to consider
  using
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

## What's next

If you configure autoscaling in your cluster, you may also want to consider using
[node autoscaling](https://kubernetes.io/docs/concepts/cluster-administration/node-autoscaling/)
to ensure you are running the right number of nodes.
You can also read more about [*vertical* Pod autoscaling](https://kubernetes.io/docs/concepts/workloads/autoscaling/vertical-pod-autoscale/).

For more information on HorizontalPodAutoscaler:

- Read a [walkthrough example](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale-walkthrough/) for horizontal pod autoscaling.
- Read documentation for [`kubectl autoscale`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands/#autoscale).
- If you would like to write your own custom metrics adapter, check out the
  [boilerplate](https://github.com/kubernetes-sigs/custom-metrics-apiserver) to get started.
- Read the [API reference](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/horizontal-pod-autoscaler-v2/) for HorizontalPodAutoscaler.