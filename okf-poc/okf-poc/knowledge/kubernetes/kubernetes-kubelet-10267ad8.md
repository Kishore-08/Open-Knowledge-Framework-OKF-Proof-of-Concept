---
id: kubernetes-kubelet-10267ad8
type: concept
title: kubelet
description: An agent that runs on each [node](https://kubernetes.io/docs/concepts/architecture/nodes/
  "A node is a worker machine in Kubernetes.") in the cluster. It makes sure that
  [containers](https://kubernete
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/architecture/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### kubelet

An agent that runs on each [node](https://kubernetes.io/docs/concepts/architecture/nodes/ "A node is a worker machine in Kubernetes.") in the cluster. It makes sure that [containers](https://kubernetes.io/docs/concepts/containers/ "A lightweight and portable executable image that contains software and all of its dependencies.") are running in a [Pod](https://kubernetes.io/docs/concepts/workloads/pods/ "A Pod represents a set of running containers in your cluster.").

The [kubelet](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/) takes a set of PodSpecs that
are provided through various mechanisms and ensures that the containers described in those
PodSpecs are running and healthy. The kubelet doesn't manage containers which were not created by
Kubernetes.