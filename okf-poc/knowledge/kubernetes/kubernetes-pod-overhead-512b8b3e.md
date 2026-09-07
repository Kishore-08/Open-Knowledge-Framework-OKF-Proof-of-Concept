---
id: kubernetes-pod-overhead-512b8b3e
type: concept
title: Pod Overhead
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/scheduling-eviction/pod-overhead/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

# Pod Overhead

FEATURE STATE:
`Kubernetes v1.24 [stable]`

When you run a Pod on a Node, the Pod itself takes an amount of system resources. These
resources are additional to the resources needed to run the container(s) inside the Pod.
In Kubernetes, *Pod Overhead* is a way to account for the resources consumed by the Pod
infrastructure on top of the container requests & limits.

In Kubernetes, the Pod's overhead is set at
[admission](https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/#what-are-admission-webhooks)
time according to the overhead associated with the Pod's
[RuntimeClass](https://kubernetes.io/docs/concepts/containers/runtime-class/).

A pod's overhead is considered in addition to the sum of container resource requests when
scheduling a Pod. Similarly, the kubelet will include the Pod overhead when sizing the Pod cgroup,
and when carrying out Pod eviction ranking.

## Configuring Pod overhead

You need to make sure a `RuntimeClass` is utilized which defines the `overhead` field.