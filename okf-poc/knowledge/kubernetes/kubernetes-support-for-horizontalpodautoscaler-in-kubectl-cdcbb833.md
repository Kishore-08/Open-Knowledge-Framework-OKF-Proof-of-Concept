---
id: kubernetes-support-for-horizontalpodautoscaler-in-kubectl-cdcbb833
type: concept
title: Support for HorizontalPodAutoscaler in kubectl
description: HorizontalPodAutoscaler, like every API resource, is supported in a standard
  way by `kubectl`.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Support for HorizontalPodAutoscaler in kubectl

HorizontalPodAutoscaler, like every API resource, is supported in a standard way by `kubectl`.
You can create a new autoscaler using `kubectl create` command.
You can list autoscalers by `kubectl get hpa` or get detailed description by `kubectl describe hpa`.
Finally, you can delete an autoscaler using `kubectl delete hpa`.

In addition, there is a special `kubectl autoscale` command for creating a HorizontalPodAutoscaler object.
For instance, executing `kubectl autoscale rs foo --min=2 --max=5 --cpu=80%`
will create an autoscaler for ReplicaSet *foo*, with target CPU utilization set to `80%`
and the number of replicas between 2 and 5.