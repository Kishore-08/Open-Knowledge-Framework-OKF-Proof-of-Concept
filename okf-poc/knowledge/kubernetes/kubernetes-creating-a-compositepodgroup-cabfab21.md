---
id: kubernetes-creating-a-compositepodgroup-cabfab21
type: concept
title: Creating a CompositePodGroup
description: Workload controllers create `CompositePodGroup` objects automatically
  from `Workload`
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/compositepodgroup-api/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

## Creating a CompositePodGroup

Workload controllers create `CompositePodGroup` objects automatically from `Workload`
templates at runtime.

The following manifest creates a root `CompositePodGroup` with a gang scheduling policy
that requires at least 2 child groups to be schedulable simultaneously:

```
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
```

You can inspect `CompositePodGroup` resources in your cluster:

```
kubectl get compositepodgroups
```

To view details for a specific composite group:

```
kubectl describe compositepodgroup root-group-0
```