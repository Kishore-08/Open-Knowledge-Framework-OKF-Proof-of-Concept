---
id: kubernetes-pod-priority-based-graceful-node-shutdown-e5a13667
type: concept
title: Pod Priority based graceful node shutdown
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/node-shutdown/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Pod Priority based graceful node shutdown

FEATURE STATE:
`Kubernetes v1.24 [beta]`(enabled by default)

To provide more flexibility during graceful node shutdown around the ordering
of pods during shutdown, graceful node shutdown honors the PriorityClass for
Pods, provided that you enabled this feature in your cluster. The feature
allows cluster administrators to explicitly define the ordering of pods
during graceful node shutdown based on
[priority classes](https://kubernetes.io/docs/concepts/scheduling-eviction/pod-priority-preemption/#priorityclass).

The [Graceful Node Shutdown](https://kubernetes.io/docs/concepts/cluster-administration/node-shutdown/#graceful-node-shutdown) feature, as described
above, shuts down pods in two phases, non-critical pods, followed by critical
pods. If additional flexibility is needed to explicitly define the ordering of
pods during shutdown in a more granular way, pod priority based graceful
shutdown can be used.

When graceful node shutdown honors pod priorities, this makes it possible to do
graceful node shutdown in multiple phases, each phase shutting down a
particular priority class of pods. The kubelet can be configured with the exact
phases and shutdown time per phase.

Assuming the following custom pod
[priority classes](https://kubernetes.io/docs/concepts/scheduling-eviction/pod-priority-preemption/#priorityclass)
in a cluster,

| Pod priority class name | Pod priority class value |
| --- | --- |
| `custom-class-a` | 100000 |
| `custom-class-b` | 10000 |
| `custom-class-c` | 1000 |
| `regular/unset` | 0 |

Within the [kubelet configuration](https://kubernetes.io/docs/reference/config-api/kubelet-config.v1beta1/)
the settings for `shutdownGracePeriodByPodPriority` could look like:

| Pod priority class value | Shutdown period |
| --- | --- |
| 100000 | 10 seconds |
| 10000 | 180 seconds |
| 1000 | 120 seconds |
| 0 | 60 seconds |

The corresponding kubelet config YAML configuration would be:

```
shutdownGracePeriodByPodPriority:
  - priority: 100000
    shutdownGracePeriodSeconds: 10
  - priority: 10000
    shutdownGracePeriodSeconds: 180
  - priority: 1000
    shutdownGracePeriodSeconds: 120
  - priority: 0
    shutdownGracePeriodSeconds: 60
```

The above table implies that any pod with `priority` value >= 100000 will get
just 10 seconds to shut down, any pod with value >= 10000 and < 100000 will get 180
seconds to shut down, any pod with value >= 1000 and < 10000 will get 120 seconds to shut down.
Finally, all other pods will get 60 seconds to shut down.

One doesn't have to specify values corresponding to all of the classes. For
example, you could instead use these settings:

| Pod priority class value | Shutdown period |
| --- | --- |
| 100000 | 300 seconds |
| 1000 | 120 seconds |
| 0 | 60 seconds |

In the above case, the pods with `custom-class-b` will go into the same bucket
as `custom-class-c` for shutdown.

If there are no pods in a particular range, then the kubelet does not wait
for pods in that priority range. Instead, the kubelet immediately skips to the
next priority class value range.

If this feature is enabled and no configuration is provided, then no ordering
action will be taken.

Using this feature requires enabling the `GracefulNodeShutdownBasedOnPodPriority`
[feature gate](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/),
and setting `ShutdownGracePeriodByPodPriority` in the
[kubelet config](https://kubernetes.io/docs/reference/config-api/kubelet-config.v1beta1/)
to the desired configuration containing the pod priority class values and
their respective shutdown periods.

#### Note:

The ability to take Pod priority into account during graceful node shutdown was introduced
as an Alpha feature in Kubernetes v1.23. In Kubernetes 1.36
the feature is Beta and is enabled by default.

Metrics `graceful_shutdown_start_time_seconds` and `graceful_shutdown_end_time_seconds`
are emitted under the kubelet subsystem to monitor node shut