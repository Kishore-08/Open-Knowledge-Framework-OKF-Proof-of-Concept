---
id: kubernetes-how-it-fits-together-cabfab21
type: concept
title: How it fits together
description: The relationship between controllers, Workloads, CompositePodGroups,
  PodGroups, and
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/compositepodgroup-api/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

## How it fits together

The relationship between controllers, Workloads, CompositePodGroups, PodGroups, and
Pods follows this pattern:

1. The workload controller creates a `Workload` defining a tree of
   `CompositePodGroupTemplates` and leaf `PodGroupTemplates`.
2. For each runtime instance, the controller creates a root `CompositePodGroup`,
   descendant `CompositePodGroup` objects, and leaf `PodGroup` objects in a top-down manner.
3. The controller creates `Pods` that reference their leaf `PodGroup` via
   `spec.schedulingGroup.podGroupName`.

The following example illustrates a complete manifest hierarchy for a two-level workload:

```
apiVersion: scheduling.k8s.io/v1alpha3
kind: Workload
metadata:
  name: hierarchical-workload
  namespace: default
spec:
  compositePodGroupTemplates:
  - name: root
    schedulingPolicy:
      gang:
        minGroupCount: 2
    podGroupTemplates:
    - name: workers-a
      schedulingPolicy:
        gang:
          minCount: 4
    - name: workers-b
      schedulingPolicy:
        gang:
          minCount: 4
---
apiVersion: scheduling.k8s.io/v1alpha3
kind: CompositePodGroup
metadata:
  name: root-group-0
  namespace: default
spec:
  workloadRef:
    workloadName: hierarchical-workload
    templateName: root
  schedulingPolicy:
    gang:
      minGroupCount: 2
---
apiVersion: scheduling.k8s.io/v1alpha3
kind: PodGroup
metadata:
  name: workers-a-0
  namespace: default
spec:
  parentCompositePodGroupName: root-group-0
  workloadRef:
    workloadName: hierarchical-workload
    templateName: workers-a
  schedulingPolicy:
    gang:
      minCount: 4
---
apiVersion: scheduling.k8s.io/v1alpha3
kind: PodGroup
metadata:
  name: workers-b-0
  namespace: default
spec:
  parentCompositePodGroupName: root-group-0
  workloadRef:
    workloadName: hierarchical-workload
    templateName: workers-b
  schedulingPolicy:
    gang:
      minCount: 4
---
apiVersion: v1
kind: Pod
metadata:
  name: worker-a-0
  namespace: default
spec:
  schedulingGroup:
    podGroupName: workers-a-0
  containers:
  - name: worker
    image: registry.k8s.io/pause:3.9
```

The `Workload` acts as a long-lived policy template, while `CompositePodGroup` and
`PodGroup` resources handle per-instance runtime scheduling state.