---
id: kubernetes-logging-architecture-16136ba9
type: concept
title: Logging Architecture
description: Application logs can help you understand what is happening inside your
  application. The
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/logging/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

# Logging Architecture

Application logs can help you understand what is happening inside your application. The
logs are particularly useful for debugging problems and monitoring cluster activity. Most
modern applications have some kind of logging mechanism. Likewise, container engines
are designed to support logging. The easiest and most adopted logging method for
containerized applications is writing to standard output and standard error streams.

However, the native functionality provided by a container engine or runtime is usually
not enough for a complete logging solution.

For example, you may want to access your application's logs if a container crashes,
a pod gets evicted, or a node dies.

In a cluster, logs should have a separate storage and lifecycle independent of nodes,
pods, or containers. This concept is called
[cluster-level logging](https://kubernetes.io/docs/concepts/cluster-administration/logging/#cluster-level-logging-architectures).

Cluster-level logging architectures require a separate backend to store, analyze, and
query logs. Kubernetes does not provide a native storage solution for log data. Instead,
there are many logging solutions that integrate with Kubernetes. The following sections
describe how to handle and store logs on nodes.