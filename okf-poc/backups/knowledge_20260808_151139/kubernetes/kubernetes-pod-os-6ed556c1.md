---
id: kubernetes-pod-os-6ed556c1
type: concept
title: Pod OS
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/pods/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Pod OS

FEATURE STATE:
`Kubernetes v1.25 [stable]`

You should set the `.spec.os.name` field to either `windows` or `linux` to indicate the
operating system that the containers in that Pod require. These two are the only operating
systems supported for now by Kubernetes. In the future, this list may be expanded.

The kubelet refuses to run a Pod if the value of `.spec.os.name` does not match the
operating system of the node. However, in Kubernetes
v1.36, the value of `.spec.os.name` does not affect
how the [kube-scheduler](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-scheduler/ "Control plane component that watches for newly created pods with no assigned node, and selects a node for them to run on.")
picks a node for the Pod to run on. In any cluster where there is more than one operating system for
running nodes, you should set the
[kubernetes.io/os](https://kubernetes.io/docs/reference/labels-annotations-taints/#kubernetes-io-os)
label correctly on each node, and define pods with a `nodeSelector` based on the operating system
label. The kube-scheduler assigns your pod to a node based on other criteria and may or may not
succeed in picking a suitable node placement where the node OS is right for the containers in that Pod.
The [Pod security standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/) also use this
field to avoid enforcing policies that aren't relevant to the operating system.