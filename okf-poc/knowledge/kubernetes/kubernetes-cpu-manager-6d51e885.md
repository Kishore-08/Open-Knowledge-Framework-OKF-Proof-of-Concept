---
id: kubernetes-cpu-manager-6d51e885
type: concept
title: CPU manager
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/resource-management/resource-managers/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

## CPU manager

FEATURE STATE:
`Kubernetes v1.26 [stable]`(enabled by default)

*CPU Manager* is a kubelet component that provides exclusive resource allocation
for CPU resources. It consults with the Topology Manager to make resource
assignment decisions. To learn more, read
[Control CPU Management Policies on the Node](https://kubernetes.io/docs/tasks/administer-cluster/cpu-management-policies/).