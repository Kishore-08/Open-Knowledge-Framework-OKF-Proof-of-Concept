---
id: kubernetes-differences-from-sidecar-containers-0818d160
type: concept
title: Differences from sidecar containers
description: Init containers run and complete their tasks before the main application
  container starts.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/pods/init-containers/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Differences from sidecar containers

Init containers run and complete their tasks before the main application container starts.
Unlike [sidecar containers](https://kubernetes.io/docs/concepts/workloads/pods/sidecar-containers/),
init containers are not continuously running alongside the main containers.

Init containers run to completion sequentially, and the main container does not start
until all the init containers have successfully completed.

init containers do not support `lifecycle`, `livenessProbe`, `readinessProbe`, or
`startupProbe` whereas sidecar containers support all these [probes](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#types-of-probe) to control their lifecycle.

Init containers share the same resources (CPU, memory, network) with the main application
containers but do not interact directly with them. They can, however, use shared volumes
for data exchange.