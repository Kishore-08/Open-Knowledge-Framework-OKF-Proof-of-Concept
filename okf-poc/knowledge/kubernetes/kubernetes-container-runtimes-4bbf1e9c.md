---
id: kubernetes-container-runtimes-4bbf1e9c
type: concept
title: Container runtimes
description: A fundamental component that empowers Kubernetes to run containers effectively.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/containers/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

## Container runtimes

A fundamental component that empowers Kubernetes to run containers effectively.
It is responsible for managing the execution and lifecycle of containers within the Kubernetes environment.

Kubernetes supports container runtimes such as
[containerd](https://containerd.io/docs/ "A container runtime with an emphasis on simplicity, robustness and portability"), [CRI-O](https://cri-o.io/#what-is-cri-o "A lightweight container runtime specifically for Kubernetes"),
and any other implementation of the [Kubernetes CRI (Container Runtime
Interface)](https://github.com/kubernetes/community/blob/main/contributors/devel/sig-node/container-runtime-interface.md).

Usually, you can allow your cluster to pick the default container runtime
for a Pod. If you need to use more than one container runtime in your cluster,
you can specify the [RuntimeClass](https://kubernetes.io/docs/concepts/containers/runtime-class/)
for a Pod to make sure that Kubernetes runs those containers using a
particular container runtime.

You can also use RuntimeClass to run different Pods with the same container
runtime but with different settings.

---

##### [Container Environment](https://kubernetes.io/docs/concepts/containers/container-environment/)

##### [Container Lifecycle Hooks](https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/)

##### [Container Runtime Interface (CRI)](https://kubernetes.io/docs/concepts/containers/cri/)