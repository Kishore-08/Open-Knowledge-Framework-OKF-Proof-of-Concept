---
id: kubernetes-how-nodes-handle-container-logs-16136ba9
type: concept
title: How nodes handle container logs
description: A container runtime handles and redirects any output generated to a containerized
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/logging/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### How nodes handle container logs

A container runtime handles and redirects any output generated to a containerized
application's `stdout` and `stderr` streams.
Different container runtimes implement this in different ways; however, the integration
with the kubelet is standardized as the *CRI logging format*.

By default, if a container restarts, the kubelet keeps one terminated container with its logs.
If a pod is evicted from the node, all corresponding containers are also evicted, along with their logs.

The kubelet makes logs available to clients via a special feature of the Kubernetes API.
The usual way to access this is by running `kubectl logs`.