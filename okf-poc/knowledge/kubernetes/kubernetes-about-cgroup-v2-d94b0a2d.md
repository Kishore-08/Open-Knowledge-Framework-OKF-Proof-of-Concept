---
id: kubernetes-about-cgroup-v2-d94b0a2d
type: concept
title: About cgroup v2
description: On Linux, [control groups](https://kubernetes.io/docs/reference/glossary/?all=true#term-cgroup
  "A group of Linux processes with optional resource isolation, accounting and limits.")
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/architecture/cgroups/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

# About cgroup v2

On Linux, [control groups](https://kubernetes.io/docs/reference/glossary/?all=true#term-cgroup "A group of Linux processes with optional resource isolation, accounting and limits.")
constrain resources that are allocated to processes.

The [kubelet](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet "An agent that runs on each node in the cluster. It makes sure that containers are running in a pod.") and the
underlying container runtime need to interface with cgroups to enforce
[resource management for pods and containers](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/) which
includes cpu/memory requests and limits for containerized workloads.

There are two versions of cgroups in Linux: cgroup v1 and cgroup v2. cgroup v2 is
the new generation of the `cgroup` API.