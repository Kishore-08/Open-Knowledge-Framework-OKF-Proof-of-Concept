---
id: kubernetes-kubernetes-scheduler-c57f4146
type: concept
title: Kubernetes Scheduler
description: In Kubernetes, *scheduling* refers to making sure that [Pods](https://kubernetes.io/docs/concepts/workloads/pods/
  "A Pod represents a set of running containers in your cluster.")
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/scheduling-eviction/kube-scheduler/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

# Kubernetes Scheduler

In Kubernetes, *scheduling* refers to making sure that [Pods](https://kubernetes.io/docs/concepts/workloads/pods/ "A Pod represents a set of running containers in your cluster.")
are matched to [Nodes](https://kubernetes.io/docs/concepts/architecture/nodes/ "A node is a worker machine in Kubernetes.") so that
[Kubelet](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet "An agent that runs on each node in the cluster. It makes sure that containers are running in a pod.") can run them.