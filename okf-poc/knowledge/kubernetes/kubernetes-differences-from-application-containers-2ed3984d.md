---
id: kubernetes-differences-from-application-containers-2ed3984d
type: concept
title: Differences from application containers
description: Sidecar containers run alongside *app containers* in the same pod. However,
  they do not
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/pods/sidecar-containers/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

## Differences from application containers

Sidecar containers run alongside *app containers* in the same pod. However, they do not
execute the primary application logic; instead, they provide supporting functionality to
the main application.

Sidecar containers have their own independent lifecycles. They can be started, stopped,
and restarted independently of app containers. This means you can update, scale, or
maintain sidecar containers without affecting the primary application.

Sidecar containers share the same network and storage namespaces with the primary
container. This co-location allows them to interact closely and share resources.

From a Kubernetes perspective, the sidecar container's graceful termination is less important.
When other containers take all allotted graceful termination time, the sidecar containers
will receive the `SIGTERM` signal, followed by the `SIGKILL` signal, before they have time to terminate gracefully.
So exit codes different from `0` (`0` indicates successful exit), for sidecar containers are normal
on Pod termination and should be generally ignored by the external tooling.