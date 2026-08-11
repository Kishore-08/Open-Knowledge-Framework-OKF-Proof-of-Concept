---
id: kubernetes-nodes-5445bee6
type: concept
title: Nodes
description: Kubernetes runs your [workload](https://kubernetes.io/docs/concepts/workloads/
  "A workload is an application running on Kubernetes.")
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/architecture/nodes/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

# Nodes

Kubernetes runs your [workload](https://kubernetes.io/docs/concepts/workloads/ "A workload is an application running on Kubernetes.")
by placing [containers](https://kubernetes.io/docs/concepts/containers/ "A lightweight and portable executable image that contains software and all of its dependencies.") into Pods to run on *Nodes*.
A node may be a virtual or physical machine, depending on the cluster. Each node
is managed by the
[control plane](https://kubernetes.io/docs/reference/glossary/?all=true#term-control-plane "The container orchestration layer that exposes the API and interfaces to define, deploy, and manage the lifecycle of containers.")
and contains the services necessary to run
[Pods](https://kubernetes.io/docs/concepts/workloads/pods/ "A Pod represents a set of running containers in your cluster.").

Typically you have several nodes in a cluster; in a learning or resource-limited
environment, you might have only one node.

The [components](https://kubernetes.io/docs/concepts/architecture/#node-components) on a node include the
[kubelet](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet "An agent that runs on each node in the cluster. It makes sure that containers are running in a pod."), a
[container runtime](https://kubernetes.io/docs/setup/production-environment/container-runtimes "The container runtime is the software that is responsible for running containers."), and the
[kube-proxy](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-proxy/ "kube-proxy is a network proxy that runs on each node in the cluster.").