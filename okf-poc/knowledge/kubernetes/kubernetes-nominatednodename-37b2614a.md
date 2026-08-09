---
id: kubernetes-nominatednodename-37b2614a
type: concept
title: nominatedNodeName
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## nominatedNodeName

FEATURE STATE:
`Kubernetes v1.35 [beta]`(enabled by default)

`nominatedNodeName` can be used for external components to nominate node for a pending pod.
This nomination is best effort: it might be ignored if the scheduler determines the pod cannot go to a nominated node.

Also, this field can be (over)written by the scheduler:

- If the scheduler finds a node to nominate via the preemption.
- If the scheduler decides where the pod is going, and move it to the binding cycle.
  - Note that, in this case, `nominatedNodeName` is put only when the pod has to go through `WaitOnPermit` or `PreBind` extension points.

Here is an example of a Pod status using the `nominatedNodeName` field:

```
apiVersion: v1
kind: Pod
metadata:
  name: nginx
...
status:
  nominatedNodeName: kube-01
```