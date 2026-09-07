---
id: kubernetes-differences-from-regular-containers-0818d160
type: concept
title: Differences from regular containers
description: Init containers support all the fields and features of app containers,
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/pods/init-containers/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Differences from regular containers

Init containers support all the fields and features of app containers,
including resource limits, [volumes](https://kubernetes.io/docs/concepts/storage/volumes/), and security settings. However, the
resource requests and limits for an init container are handled differently,
as documented in [Resource sharing within containers](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/#resource-sharing-within-containers).

Regular init containers (in other words: excluding sidecar containers) do not support the
`lifecycle`, `livenessProbe`, `readinessProbe`, or `startupProbe` fields. Init containers
must run to completion before the Pod can be ready; sidecar containers continue running
during a Pod's lifetime, and *do* support some probes. See [sidecar container](https://kubernetes.io/docs/concepts/workloads/pods/sidecar-containers/)
for further details about sidecar containers.

If you specify multiple init containers for a Pod, kubelet runs each init
container sequentially. Each init container must succeed before the next can run.
When all of the init containers have run to completion, kubelet initializes
the application containers for the Pod and runs them as usual.