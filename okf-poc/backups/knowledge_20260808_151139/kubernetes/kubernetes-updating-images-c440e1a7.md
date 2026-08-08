---
id: kubernetes-updating-images-c440e1a7
type: concept
title: Updating images
description: When you first create a [Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/
  "Manages a replicated application on your cluster."),
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/containers/images/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Updating images

When you first create a [Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/ "Manages a replicated application on your cluster."),
[StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/ "A StatefulSet manages deployment and scaling of a set of Pods, with durable storage and persistent identifiers for each Pod."), Pod, or other
object that includes a PodTemplate, and a pull policy was not explicitly specified,
then by default the pull policy of all containers in that Pod will be set to
`IfNotPresent`. This policy causes the
[kubelet](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet "An agent that runs on each node in the cluster. It makes sure that containers are running in a pod.") to skip pulling an
image if it already exists.