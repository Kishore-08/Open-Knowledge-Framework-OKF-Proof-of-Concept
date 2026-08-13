---
id: kubernetes-scaling-workloads-manually-3fee6faa
type: concept
title: Scaling workloads manually
description: Kubernetes supports *manual scaling* of workloads. Horizontal scaling
  can be done
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/autoscaling/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

## Scaling workloads manually

Kubernetes supports *manual scaling* of workloads. Horizontal scaling can be done
using the `kubectl` CLI.
For vertical scaling, you need to *patch* the resource definition of your workload.

See below for examples of both strategies.

- **Horizontal scaling**: [Running multiple instances of your app](https://kubernetes.io/docs/tutorials/kubernetes-basics/scale/scale-intro/)
- **Vertical scaling**: [Resizing CPU and memory resources assigned to containers](https://kubernetes.io/docs/tasks/configure-pod-container/resize-container-resources/)