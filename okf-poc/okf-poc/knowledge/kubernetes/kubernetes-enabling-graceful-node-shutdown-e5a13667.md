---
id: kubernetes-enabling-graceful-node-shutdown-e5a13667
type: concept
title: Enabling graceful node shutdown
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/node-shutdown/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Enabling graceful node shutdown



FEATURE STATE:
`Kubernetes v1.21 [beta]`(enabled by default)

On Linux, the graceful node shutdown feature is controlled with the `GracefulNodeShutdown`
[feature gate](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/) which is
enabled by default in 1.21.

#### Note:

The graceful node shutdown feature depends on systemd since it takes advantage of
[systemd inhibitor locks](https://www.freedesktop.org/wiki/Software/systemd/inhibit/) to
delay the node shutdown with a given duration.

FEATURE STATE:
`Kubernetes v1.34 [beta]`(enabled by default)

On Windows, the graceful node shutdown feature is controlled with the `WindowsGracefulNodeShutdown`
[feature gate](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/)
which is introduced in 1.32 as an alpha feature. In Kubernetes 1.34 the feature is Beta
and is enabled by default.

#### Note:

The Windows graceful node shutdown feature depends on kubelet running as a Windows service,
it will then have a registered [service control handler](https://learn.microsoft.com/en-us/windows/win32/services/service-control-handler-function)
to delay the preshutdown event with a given duration.

Windows graceful node shutdown can not be cancelled.

If kubelet is not running as a Windows service, it will not be able to set and monitor
the [Preshutdown](https://learn.microsoft.com/en-us/windows/win32/api/winsvc/ns-winsvc-service_preshutdown_info) event,
the node will have to go through the [Non-Graceful Node Shutdown](https://kubernetes.io/docs/concepts/cluster-administration/node-shutdown/#non-graceful-node-shutdown) procedure mentioned above.

In the case where the Windows graceful node shutdown feature is enabled, but the kubelet is not
running as a Windows service, the kubelet will continue running instead of failing. However,
it will log an error indicating that it needs to be run as a Windows service.