---
id: kubernetes-associated-lifetimes-3e34f258
type: concept
title: Associated lifetimes
description: When something is said to have the same lifetime as a Pod, such as a
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Associated lifetimes

When something is said to have the same lifetime as a Pod, such as a
[volume](https://kubernetes.io/docs/concepts/storage/volumes/ "A directory containing data, accessible to the containers in a pod."),
that means that the thing exists as long as that specific Pod (with that exact UID)
exists. If that Pod is deleted for any reason, and even if an identical replacement
is created, the related thing (a volume, in this example) is also destroyed and
created anew.

![A multi-container Pod that contains a file puller sidecar and a web server. The Pod uses an ephemeral emptyDir volume for shared storage between the containers.](https://kubernetes.io/images/docs/pod.svg)

#### Figure 1.

A multi-container Pod that contains a file puller [sidecar](https://kubernetes.io/docs/concepts/workloads/pods/sidecar-containers/) and a web server. The Pod uses an [ephemeral `emptyDir` volume](https://kubernetes.io/docs/concepts/storage/volumes/#emptydir) for shared storage between the containers.