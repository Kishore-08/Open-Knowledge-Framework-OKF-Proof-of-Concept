---
id: kubernetes-configuring-graceful-node-shutdown-e5a13667
type: concept
title: Configuring graceful node shutdown
description: Note that by default, both configuration options described below,
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/node-shutdown/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Configuring graceful node shutdown

Note that by default, both configuration options described below,
`shutdownGracePeriod` and `shutdownGracePeriodCriticalPods`, are set to zero,
thus not activating the graceful node shutdown functionality.
To activate the feature, both options should be configured appropriately and
set to non-zero values.

Once the kubelet is notified of a node shutdown, it sets a `NotReady` condition on
the Node, with the `reason` set to `"node is shutting down"`. The kube-scheduler honors this condition
and does not schedule any Pods onto the affected node; other third-party schedulers are
expected to follow the same logic. This means that new Pods won't be scheduled onto that node
and therefore none will start.

The kubelet **also** rejects Pods during the `PodAdmission` phase if an ongoing
node shutdown has been detected, so that even Pods with a
[toleration](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/ "A core object consisting of three required properties: key, value, and effect. Tolerations enable the scheduling of pods on nodes or node groups that have a matching taint.") for
`node.kubernetes.io/not-ready:NoSchedule` do not start there.

When kubelet is setting that condition on its Node via the API,
the kubelet also begins terminating any Pods that are running locally.

During a graceful shutdown, kubelet terminates pods in two phases:

1. Terminate regular pods running on the node.
2. Terminate [critical pods](https://kubernetes.io/docs/tasks/administer-cluster/guaranteed-scheduling-critical-addon-pods/#marking-pod-as-critical)
   running on the node.

The graceful node shutdown feature is configured with two
[`KubeletConfiguration`](https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/) options:

- `shutdownGracePeriod`:

  Specifies the total duration that the node should delay the shutdown by. This is the total
  grace period for pod termination for both regular and
  [critical pods](https://kubernetes.io/docs/tasks/administer-cluster/guaranteed-scheduling-critical-addon-pods/#marking-pod-as-critical).
- `shutdownGracePeriodCriticalPods`:

  Specifies the duration used to terminate
  [critical pods](https://kubernetes.io/docs/tasks/administer-cluster/guaranteed-scheduling-critical-addon-pods/#marking-pod-as-critical)
  during a node shutdown. This value should be less than `shutdownGracePeriod`.

#### Note:

There are cases when Node termination was cancelled by the system (or perhaps manually
by an administrator). In either of those situations the Node will return to the `Ready` state.
However, Pods which already started the process of termination will not be restored by kubelet
and will need to be re-scheduled.

For example, if `shutdownGracePeriod=30s`, and
`shutdownGracePeriodCriticalPods=10s`, kubelet will delay the node shutdown by
30 seconds. During the shutdown, the first 20 (30-10) seconds would be reserved
for gracefully terminating normal pods, and the last 10 seconds would be
reserved for terminating [critical pods](https://kubernetes.io/docs/tasks/administer-cluster/guaranteed-scheduling-critical-addon-pods/#marking-pod-as-critical).

#### Note:

When pods were evicted during the graceful node shutdown, they are marked as shutdown.
Running `kubectl get pods` shows the status of the evicted pods as `Terminated`.
And `kubectl describe pod` indicates that the pod was evicted because of node shutdown:

```
Reason:         Terminated
Message:        Pod was terminated in response to imminent node shutdown.
```