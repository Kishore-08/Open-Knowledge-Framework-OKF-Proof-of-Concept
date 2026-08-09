---
id: kubernetes-startup-probe-3e34f258
type: concept
title: Startup probe
description: Startup probes verify whether the application within a container is started.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Startup probe

Startup probes verify whether the application within a container is started.
If a startup probe is configured, Kubernetes does not execute liveness or
readiness probes until the startup probe succeeds, allowing the application
time to finish its initialization.

This type of probe is only executed at startup, unlike liveness and readiness
probes, which are run periodically.

If the startup probe fails, the kubelet kills the container, and the container
is subjected to its [restart policy](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#restart-policy).