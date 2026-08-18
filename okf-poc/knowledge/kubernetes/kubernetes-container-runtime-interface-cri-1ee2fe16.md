---
id: kubernetes-container-runtime-interface-cri-1ee2fe16
type: concept
title: Container Runtime Interface (CRI)
description: The CRI is a plugin interface which enables the kubelet to use a wide
  variety of
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/containers/cri/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

# Container Runtime Interface (CRI)

The CRI is a plugin interface which enables the kubelet to use a wide variety of
container runtimes, without having a need to recompile the cluster components.

You need a working
[container runtime](https://kubernetes.io/docs/setup/production-environment/container-runtimes "The container runtime is the software that is responsible for running containers.") on
each Node in your cluster, so that the
[kubelet](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet "An agent that runs on each node in the cluster. It makes sure that containers are running in a pod.") can launch
[Pods](https://kubernetes.io/docs/concepts/workloads/pods/ "A Pod represents a set of running containers in your cluster.") and their containers.

The Container Runtime Interface (CRI) is the main protocol for the communication between the [kubelet](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet "An agent that runs on each node in the cluster. It makes sure that containers are running in a pod.") and Container Runtime.

The Kubernetes Container Runtime Interface (CRI) defines the main
[gRPC](https://grpc.io) protocol for the communication between the
[node components](https://kubernetes.io/docs/concepts/architecture/#node-components)
[kubelet](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet "An agent that runs on each node in the cluster. It makes sure that containers are running in a pod.") and
[container runtime](https://kubernetes.io/docs/setup/production-environment/container-runtimes "The container runtime is the software that is responsible for running containers.").