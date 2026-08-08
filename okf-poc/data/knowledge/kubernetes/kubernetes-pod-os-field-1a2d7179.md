---
id: kubernetes-pod-os-field-1a2d7179
type: concept
title: Pod OS field
description: Kubernetes lets you use nodes that run either Linux or Windows. You can
  mix both kinds of
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/security/pod-security-standards/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Pod OS field

Kubernetes lets you use nodes that run either Linux or Windows. You can mix both kinds of
node in one cluster.
Windows in Kubernetes has some limitations and differentiators from Linux-based
workloads. Specifically, many of the Pod `securityContext` fields
[have no effect on Windows](https://kubernetes.io/docs/concepts/windows/intro/#compatibility-v1-pod-spec-containers-securitycontext).

#### Note:

Kubelets prior to v1.24 don't enforce the pod OS field, and if a cluster has nodes on versions earlier than v1.24 the Restricted policies should be pinned to a version prior to v1.25.