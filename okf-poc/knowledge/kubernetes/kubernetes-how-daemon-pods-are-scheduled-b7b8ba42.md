---
id: kubernetes-how-daemon-pods-are-scheduled-b7b8ba42
type: concept
title: How Daemon Pods are scheduled
description: A DaemonSet can be used to ensure that all eligible nodes run a copy
  of a Pod.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

## How Daemon Pods are scheduled

A DaemonSet can be used to ensure that all eligible nodes run a copy of a Pod.
The DaemonSet controller creates a Pod for each eligible node and adds the
`spec.affinity.nodeAffinity` field of the Pod to match the target host. After
the Pod is created, the default scheduler typically takes over and then binds
the Pod to the target host by setting the `.spec.nodeName` field. If the new
Pod cannot fit on the node, the default scheduler may preempt (evict) some of
the existing Pods based on the
[priority](https://kubernetes.io/docs/concepts/scheduling-eviction/pod-priority-preemption/#pod-priority)
of the new Pod.

#### Note:

If it's important that the DaemonSet pod run on each node, it's often desirable
to set the `.spec.template.spec.priorityClassName` of the DaemonSet to a
[PriorityClass](https://kubernetes.io/docs/concepts/scheduling-eviction/pod-priority-preemption/#priorityclass)
with a higher priority to ensure that this eviction occurs.

The user can specify a different scheduler for the Pods of the DaemonSet, by
setting the `.spec.template.spec.schedulerName` field of the DaemonSet.

The original node affinity specified at the
`.spec.template.spec.affinity.nodeAffinity` field (if specified) is taken into
consideration by the DaemonSet controller when evaluating the eligible nodes,
but is replaced on the created Pod with the node affinity that matches the name
of the eligible node.

```
nodeAffinity:
  requiredDuringSchedulingIgnoredDuringExecution:
    nodeSelectorTerms:
    - matchFields:
      - key: metadata.name
        operator: In
        values:
        - target-host-name
```