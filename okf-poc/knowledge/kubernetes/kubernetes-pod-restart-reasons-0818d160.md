---
id: kubernetes-pod-restart-reasons-0818d160
type: concept
title: Pod restart reasons
description: A Pod can restart, causing re-execution of init containers, for the following
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/pods/init-containers/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

### Pod restart reasons

A Pod can restart, causing re-execution of init containers, for the following
reasons:

- The Pod infrastructure container is restarted. This is uncommon and would
  have to be done by someone with root access to nodes.
- All containers in a Pod are terminated while `restartPolicy` is set to Always,
  forcing a restart, and the init container completion record has been lost due
  to [garbage collection](https://kubernetes.io/docs/concepts/architecture/garbage-collection/ "A collective term for the various mechanisms Kubernetes uses to clean up cluster resources.").

The Pod will not be restarted when the init container image is changed, or the
init container completion record has been lost due to garbage collection. This
applies for Kubernetes v1.20 and later. If you are using an earlier version of
Kubernetes, consult the documentation for the version you are using.