---
id: kubernetes-container-runtime-integration-9edb5061
type: concept
title: Container runtime integration
description: The kubelet uses the container runtime API, and directs the container
  runtime to
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/swap-memory-management/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Container runtime integration

The kubelet uses the container runtime API, and directs the container runtime to
apply specific configuration (for example, in the cgroup v2 case, `memory.swap.max`) in a manner that will
enable the desired swap configuration for a container. For runtimes that use control groups, or cgroups,
the container runtime is then responsible for writing these settings to the container-level cgroup.

## Observability for swap use