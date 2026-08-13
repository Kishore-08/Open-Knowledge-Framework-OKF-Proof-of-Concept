---
id: kubernetes-uses-for-ephemeral-containers-798d1764
type: concept
title: Uses for ephemeral containers
description: Ephemeral containers are useful for interactive troubleshooting when
  `kubectl exec` is insufficient because a container has crashed or a container image
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/pods/ephemeral-containers/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

## Uses for ephemeral containers

Ephemeral containers are useful for interactive troubleshooting when `kubectl exec` is insufficient because a container has crashed or a container image
doesn't include debugging utilities.

In particular, [distroless images](https://github.com/GoogleContainerTools/distroless)
enable you to deploy minimal container images that reduce attack surface
and exposure to bugs and vulnerabilities. Since distroless images do not include a
shell or any debugging utilities, it's difficult to troubleshoot distroless
images using `kubectl exec` alone.

When using ephemeral containers, it's helpful to enable [process namespace
sharing](https://kubernetes.io/docs/tasks/configure-pod-container/share-process-namespace/) so
you can view processes in other containers.

## What's next

- Learn how to [debug pods using ephemeral containers](https://kubernetes.io/docs/tasks/debug/debug-application/debug-running-pod/#ephemeral-container).