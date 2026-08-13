---
id: kubernetes-permit-085106f9
type: concept
title: Permit
description: '*Permit* plugins are invoked at the end of the scheduling cycle for
  each Pod, to'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/scheduling-eviction/scheduling-framework/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

### Permit

*Permit* plugins are invoked at the end of the scheduling cycle for each Pod, to
prevent or delay the binding to the candidate node. A permit plugin can do one of
the three things:

1. **approve**  
   Once all Permit plugins approve a Pod, it is sent for binding.
2. **deny**  
   If any Permit plugin denies a Pod, it is returned to the scheduling queue.
   This will trigger the Unreserve phase in [Reserve plugins](https://kubernetes.io/docs/concepts/scheduling-eviction/scheduling-framework/#reserve).
3. **wait** (with a timeout)  
   If a Permit plugin returns "wait", then the Pod is kept in an internal "waiting"
   Pods list, and the binding cycle of this Pod starts but directly blocks until it
   gets approved. If a timeout occurs, **wait** becomes **deny**
   and the Pod is returned to the scheduling queue, triggering the
   Unreserve phase in [Reserve plugins](https://kubernetes.io/docs/concepts/scheduling-eviction/scheduling-framework/#reserve).

#### Note:

While any plugin can access the list of "waiting" Pods and approve them
(see [`FrameworkHandle`](https://git.k8s.io/enhancements/keps/sig-scheduling/624-scheduling-framework#frameworkhandle)),
we expect only the permit plugins to approve binding of reserved Pods that are in "waiting" state.
Once a Pod is approved, it is sent to the [PreBind](https://kubernetes.io/docs/concepts/scheduling-eviction/scheduling-framework/#pre-bind) phase.