---
id: kubernetes-cluster-level-logging-architectures-16136ba9
type: concept
title: Cluster-level logging architectures
description: While Kubernetes does not provide a native solution for cluster-level
  logging, there are
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/logging/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

## Cluster-level logging architectures

While Kubernetes does not provide a native solution for cluster-level logging, there are
several common approaches you can consider. Here are some options:

- Use a node-level logging agent that runs on every node.
- Include a dedicated sidecar container for logging in an application pod.
- Push logs directly to a backend from within an application.