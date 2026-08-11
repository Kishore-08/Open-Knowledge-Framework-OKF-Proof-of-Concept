---
id: kubernetes-creating-a-podgroup-0cf588b5
type: concept
title: Creating a PodGroup
description: A PodGroup API resource is part of the `scheduling.k8s.io/v1alpha2`
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/podgroup-api/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Creating a PodGroup

A PodGroup API resource is part of the `scheduling.k8s.io/v1alpha2`
[API group](https://kubernetes.io/docs/concepts/overview/kubernetes-api/#api-groups-and-versioning "A set of related paths in the Kubernetes API.").
(and your cluster must have that API group enabled, as well as the `GenericWorkload`
[feature gate](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/),
before you can use this API).

The following manifest creates a PodGroup with a gang scheduling policy that requires
at least 4 Pods to be schedulable simultaneously:

```
apiVersion: scheduling.k8s.io/v1alpha2
kind: PodGroup
metadata:
  name: training-worker-0
  namespace: default
spec:
  schedulingPolicy:
    gang:
      minCount: 4
```

You can inspect PodGroups in your cluster:

```
kubectl get podgroups
```

To see the full status including scheduling conditions:

```
kubectl describe podgroup training-worker-0
```