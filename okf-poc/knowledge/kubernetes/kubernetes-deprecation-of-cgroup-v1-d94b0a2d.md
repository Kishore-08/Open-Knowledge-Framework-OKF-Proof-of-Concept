---
id: kubernetes-deprecation-of-cgroup-v1-d94b0a2d
type: concept
title: Deprecation of cgroup v1
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/architecture/cgroups/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Deprecation of cgroup v1

FEATURE STATE:
`Kubernetes v1.35 [deprecated]`

Kubernetes has deprecated cgroup v1.
Removal will follow [Kubernetes deprecation policy](https://kubernetes.io/docs/reference/using-api/deprecation-policy/).

Kubelet will no longer start on a cgroup v1 node by default.
To disable this setting a cluster admin should set `failCgroupV1` to false in the [kubelet configuration file](https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/).