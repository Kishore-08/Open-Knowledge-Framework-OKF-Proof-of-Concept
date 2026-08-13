---
id: kubernetes-disruptiontarget-9184beed
type: concept
title: DisruptionTarget
description: A dedicated Pod `DisruptionTarget` condition is added to indicate that
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/pods/pod-condition/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

### DisruptionTarget

A dedicated Pod `DisruptionTarget` condition is added to indicate that
the Pod is about to be deleted due to a [disruption](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/ "An event that leads to Pod(s) going out of service").
The `reason` field of the condition additionally
indicates one of the following reasons for the Pod termination:

`PreemptionByScheduler`
:   Pod is due to be [preempted](https://kubernetes.io/docs/concepts/scheduling-eviction/pod-priority-preemption/#preemption "Preemption logic in Kubernetes helps a pending Pod to find a suitable Node by evicting low priority Pods existing on that Node.") by a scheduler in order to accommodate a new Pod with a higher priority. For more information, see [Pod priority preemption](https://kubernetes.io/docs/concepts/scheduling-eviction/pod-priority-preemption/).

`DeletionByTaintManager`
:   Pod is due to be deleted by Taint Manager (which is part of the node lifecycle controller within `kube-controller-manager`) due to a `NoExecute` taint that the Pod does not tolerate; see [taint](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/ "A core object consisting of three required properties: key, value, and effect. Taints prevent the scheduling of pods on nodes or node groups.")-based evictions.

`EvictionByEvictionAPI`
:   Pod has been marked for [eviction using the Kubernetes API](https://kubernetes.io/docs/concepts/scheduling-eviction/api-eviction/ "API-initiated eviction is the process by which you use the Eviction API to create an Eviction object that triggers graceful pod termination.") .

`DeletionByPodGC`
:   Pod, that is bound to a no longer existing Node, is due to be deleted by [Pod garbage collection](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-garbage-collection).

`TerminationByKubelet`
:   Pod has been terminated by the kubelet, because of either [node pressure eviction](https://kubernetes.io/docs/concepts/scheduling-eviction/node-pressure-eviction/ "Node-pressure eviction is the process by which the kubelet proactively fails pods to reclaim resources on nodes."),
    the [graceful node shutdown](https://kubernetes.io/docs/concepts/architecture/nodes/#graceful-node-shutdown),
    or preemption for [system critical pods](https://kubernetes.io/docs/tasks/administer-cluster/guaranteed-scheduling-critical-addon-pods/).

In all other disruption scenarios, like eviction due to exceeding
[Pod container limits](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/),
Pods don't receive the `DisruptionTarget` condition because the disruptions were
probably caused by the Pod and would reoccur on retry.

#### Note:

A Pod disruption might be interrupted. The control plane might re-attempt to
continue the disruption of the same Pod, but it is not guaranteed. As a result,
the `DisruptionTarget` condition might be added to a Pod, but that Pod might then not actually be
deleted. In such a situation, after some time, the
Pod disruption condition will be cleared.

Along with cleaning up the pods, the Pod garbage collector (PodGC) will also mark them as failed if they are in a non-terminal
phase (see also [Pod garbage collection](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-garbage-collection)).

When using a Job (or CronJob), you may want to use these Pod disruption conditions as part of your Job's
[Pod failure policy](https://kubernetes.io/docs/concepts/workloads/controllers/job/#pod-failure-policy).

For more details, see [Disruptions](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/).