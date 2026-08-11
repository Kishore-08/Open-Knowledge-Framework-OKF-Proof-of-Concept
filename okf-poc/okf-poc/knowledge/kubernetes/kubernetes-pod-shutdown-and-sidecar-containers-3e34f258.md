---
id: kubernetes-pod-shutdown-and-sidecar-containers-3e34f258
type: concept
title: Pod shutdown and sidecar containers
description: If your Pod includes one or more
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Pod shutdown and sidecar containers

If your Pod includes one or more
[sidecar containers](https://kubernetes.io/docs/concepts/workloads/pods/sidecar-containers/)
(init containers with an `Always` restart policy), the kubelet will delay sending
the TERM signal to these sidecar containers until the last main container has fully terminated.
The sidecar containers will be terminated in the reverse order they are defined in the Pod spec.
This ensures that sidecar containers continue serving the other containers in the Pod until they
are no longer needed.

This means that slow termination of a main container will also delay the termination of the sidecar containers.
If the grace period expires before the termination process is complete, the Pod may enter [forced termination](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-termination-beyond-grace-period).
In this case, all remaining containers in the Pod will be terminated simultaneously with a short grace period.

Similarly, if the Pod has a `preStop` hook that exceeds the termination grace period, emergency termination may occur.
In general, if you have used `preStop` hooks to control the termination order without sidecar containers, you can now
remove them and allow the kubelet to manage sidecar termination automatically.