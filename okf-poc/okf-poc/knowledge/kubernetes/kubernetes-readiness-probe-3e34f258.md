---
id: kubernetes-readiness-probe-3e34f258
type: concept
title: Readiness probe
description: Readiness probes determine when a container is ready to accept traffic.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Readiness probe

Readiness probes determine when a container is ready to accept traffic.
This is useful when waiting for an application to perform time-consuming initial
tasks, such as establishing network connections, loading files, and warming
caches.
Readiness probes can also be useful later in the container's lifecycle,
for example, when recovering from temporary faults or overloads.

If the readiness probe returns a failed state, the
[EndpointSlice](https://kubernetes.io/docs/concepts/services-networking/endpoint-slices/ "EndpointSlices track the IP addresses of Pods for Services.")
controller removes the Pod's IP address from the EndpointSlices of all Services
that match the Pod.

Readiness probes run on the container during its whole lifecycle.