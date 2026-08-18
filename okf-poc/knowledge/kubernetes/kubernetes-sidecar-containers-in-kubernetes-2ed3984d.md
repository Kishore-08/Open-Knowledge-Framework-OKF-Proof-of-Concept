---
id: kubernetes-sidecar-containers-in-kubernetes-2ed3984d
type: concept
title: Sidecar containers in Kubernetes
description: Kubernetes implements sidecar containers as a special case of
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/pods/sidecar-containers/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Sidecar containers in Kubernetes

Kubernetes implements sidecar containers as a special case of
[init containers](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/); sidecar containers remain
running after Pod startup. This document uses the term *regular init containers* to clearly
refer to containers that only run during Pod startup.

Provided that your cluster has the `SidecarContainers`
[feature gate](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/) enabled
(the feature is active by default since Kubernetes v1.29), you can specify a `restartPolicy`
for containers listed in a Pod's `initContainers` field.
These restartable *sidecar* containers are independent from other init containers and from
the main application container(s) within the same pod.
These can be started, stopped, or restarted without affecting the main application container
and other init containers.

You can also run a Pod with multiple containers that are not marked as init or sidecar
containers. This is appropriate if the containers within the Pod are required for the
Pod to work overall, but you don't need to control which containers start or stop first.
You could also do this if you need to support older versions of Kubernetes that don't
support a container-level `restartPolicy` field.