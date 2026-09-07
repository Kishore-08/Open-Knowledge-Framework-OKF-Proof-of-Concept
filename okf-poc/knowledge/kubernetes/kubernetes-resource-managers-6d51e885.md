---
id: kubernetes-resource-managers-6d51e885
type: concept
title: Resource managers
description: In order to support latency-critical and high-throughput workloads, Kubernetes
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/resource-management/resource-managers/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

# Resource managers

In order to support latency-critical and high-throughput workloads, Kubernetes
offers a suite of Resource Managers. The managers aim to co-ordinate and
optimize the alignment of node's resources for pods configured with a specific
requirement for CPUs, devices, and memory (hugepages) resources.