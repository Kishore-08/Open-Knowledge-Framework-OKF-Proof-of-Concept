---
id: kubernetes-pod-conditions-9184beed
type: concept
title: Pod Conditions
description: In Kubernetes, many objects have *conditions*.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/pods/pod-condition/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

# Pod Conditions

In Kubernetes, many objects have *conditions*.
Conditions are markers for some aspect of the actual state of the thing the object represents.
Pods have conditions, and Kubernetes Pod conditions are an important aspect of how controllers
(and people doing troubleshooting) can understand the health of a Pod.

A Pod's [phase](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-phase) provides a high-level
summary of where the Pod is in its lifecycle, but a single value cannot capture the full
picture. For example, a Pod may be in the `Running` phase but not yet ready to serve traffic.
Pod conditions complement the phase by tracking multiple aspects of the Pod's state
independently, such as whether it has been scheduled, whether its containers are ready,
whether a resize is in progress, or whether the Pod is about to be disrupted due to a
[taint](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/ "A core object consisting of three required properties: key, value, and effect. Taints prevent the scheduling of pods on nodes or node groups.").