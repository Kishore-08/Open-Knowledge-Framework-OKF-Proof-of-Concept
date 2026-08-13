---
id: kubernetes-sidecar-containers-and-pod-lifecycle-2ed3984d
type: concept
title: Sidecar containers and Pod lifecycle
description: If an init container is created with its `restartPolicy` set to `Always`,
  it will
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/pods/sidecar-containers/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

## Sidecar containers and Pod lifecycle

If an init container is created with its `restartPolicy` set to `Always`, it will
start and remain running during the entire life of the Pod. This can be helpful for
running supporting services separated from the main application containers.

If a `readinessProbe` is specified for this init container, its result will be used
to determine the `ready` state of the Pod.

Since these containers are defined as init containers, they benefit from the same
ordering and sequential guarantees as regular init containers, allowing you to mix
sidecar containers with regular init containers for complex Pod initialization flows.

Compared to regular init containers, sidecars defined within `initContainers` continue to
run after they have started. This is important when there is more than one entry inside
`.spec.initContainers` for a Pod. After a sidecar-style init container is running (the kubelet
has set the `started` status for that init container to true), the kubelet then starts the
next init container from the ordered `.spec.initContainers` list.
That status either becomes true because there is a process running in the
container and no startup probe defined, or as a result of its `startupProbe` succeeding.

Upon Pod [termination](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#termination-with-sidecars),
the kubelet postpones terminating sidecar containers until the main application container has fully stopped.
The sidecar containers are then shut down in the opposite order of their appearance in the Pod specification.
This approach ensures that the sidecars remain operational, supporting other containers within the Pod,
until their service is no longer required.