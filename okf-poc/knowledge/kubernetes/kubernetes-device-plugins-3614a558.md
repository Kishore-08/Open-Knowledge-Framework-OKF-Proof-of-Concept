---
id: kubernetes-device-plugins-3614a558
type: concept
title: Device Plugins
description: Device plugins let you configure your cluster with support for devices
  or resources that require vendor-specific setup, such as GPUs, NICs, FPGAs, or non-volatile
  main memory.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

# Device Plugins

Device plugins let you configure your cluster with support for devices or resources that require vendor-specific setup, such as GPUs, NICs, FPGAs, or non-volatile main memory.

FEATURE STATE:
`Kubernetes v1.26 [stable]`

Kubernetes provides a device plugin framework that you can use to advertise system hardware
resources to the [Kubelet](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet "An agent that runs on each node in the cluster. It makes sure that containers are running in a pod.").

Instead of customizing the code for Kubernetes itself, vendors can implement a
device plugin that you deploy either manually or as a [DaemonSet](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset "Ensures a copy of a Pod is running across a set of nodes in a cluster.").
The targeted devices include GPUs, high-performance NICs, FPGAs, InfiniBand adapters,
and other similar computing resources that may require vendor specific initialization
and setup.