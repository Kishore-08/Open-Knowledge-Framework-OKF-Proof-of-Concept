---
id: kubernetes-enhanced-pod-readiness-9184beed
type: concept
title: Enhanced Pod readiness
description: Your application can inject extra feedback or signals into the Pod's
  `.status`;
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/pods/pod-condition/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Enhanced Pod readiness

Your application can inject extra feedback or signals into the Pod's `.status`;
this is known as *enhanced Pod readiness*.
To use this, set `readinessGates` in the Pod's `spec` to specify a list of additional
conditions that the kubelet evaluates for Pod readiness.
You then implement, or install, a controller that manages these custom conditions,
and the kubelet uses that as an extra input to decide if the Pod is ready.

Readiness gates are determined by the current state of `status.condition` fields for the Pod.
If Kubernetes cannot find such a condition in the `status.conditions` field of a Pod, the status of the condition is defaulted to "`False`".

```
kind: Pod
...
spec:
  readinessGates:
    - conditionType: "www.example.com/feature-1"
status:
  conditions:
    - type: Ready                              # a built-in PodCondition
      status: "False"
      lastProbeTime: null
      lastTransitionTime: 2018-01-01T00:00:00Z
    - type: "www.example.com/feature-1"        # an extra PodCondition
      status: "False"
      lastProbeTime: null
      lastTransitionTime: 2018-01-01T00:00:00Z
  containerStatuses:
    - containerID: docker://abcd...
      ready: true
...
```

The Pod conditions you add must have names that meet the Kubernetes [label key format](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#syntax-and-character-set).