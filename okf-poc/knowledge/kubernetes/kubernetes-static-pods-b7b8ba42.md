---
id: kubernetes-static-pods-b7b8ba42
type: concept
title: Static Pods
description: It is possible to create Pods by writing a file to a certain directory
  watched by Kubelet. These
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Static Pods

It is possible to create Pods by writing a file to a certain directory watched by Kubelet. These
are called [static pods](https://kubernetes.io/docs/tasks/configure-pod-container/static-pod/).
Unlike DaemonSet, static Pods cannot be managed with kubectl
or other Kubernetes API clients. Static Pods do not depend on the apiserver, making them useful
in cluster bootstrapping cases. Also, static Pods may be deprecated in the future.