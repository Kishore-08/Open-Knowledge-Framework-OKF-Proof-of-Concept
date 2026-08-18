---
id: kubernetes-bare-pods-b7b8ba42
type: concept
title: Bare Pods
description: It is possible to create Pods directly which specify a particular node
  to run on. However,
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Bare Pods

It is possible to create Pods directly which specify a particular node to run on. However,
a DaemonSet replaces Pods that are deleted or terminated for any reason, such as in the case of
node failure or disruptive node maintenance, such as a kernel upgrade. For this reason, you should
use a DaemonSet rather than creating individual Pods.