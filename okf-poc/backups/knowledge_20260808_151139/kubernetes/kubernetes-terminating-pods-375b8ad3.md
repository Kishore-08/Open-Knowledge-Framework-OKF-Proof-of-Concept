---
id: kubernetes-terminating-pods-375b8ad3
type: concept
title: Terminating Pods
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Terminating Pods

FEATURE STATE:
`Kubernetes v1.35 [beta]`(enabled by default)

You can enable this feature by setting the `DeploymentReplicaSetTerminatingReplicas`
[feature gate](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/)
on the [API server](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-apiserver/)
and on the [kube-controller-manager](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-controller-manager/)

Pods that become terminating due to deletion or scale down may take a long time to terminate, and may consume
additional resources during that period. As a result, the total number of all pods can temporarily exceed
`.spec.replicas`. Terminating pods can be tracked using the `.status.terminatingReplicas` field of the ReplicaSet.