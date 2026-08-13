---
id: kubernetes-qualifying-criteria-bc994bad
type: concept
title: Qualifying criteria
description: The Job controller creates a Workload with a
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/job/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

### Qualifying criteria

The Job controller creates a Workload with a
[gang scheduling policy](https://kubernetes.io/docs/concepts/workloads/workload-api/policies/#gang-policy)
when the Job meets all of the following conditions:

- `.spec.parallelism` is greater than 1
- `.spec.completionMode` is `Indexed`
- `.spec.parallelism` equals `.spec.completions`
- `.spec.template.spec.schedulingGroup` is not set

Jobs that do not match these criteria continue to schedule Pods independently,
with no `Workload` or `PodGroup` created.

For example, the following Job runs 8 parallel indexed workers. When the feature
is enabled, the Job controller creates a `Workload` and `PodGroup` with
`minCount: 8` before creating any Pods, ensuring all 8 workers are
scheduled together:

```
apiVersion: batch/v1
kind: Job
metadata:
  name: distributed-training
  namespace: training
spec:
  parallelism: 8
  completions: 8
  completionMode: Indexed
  template:
    spec:
      restartPolicy: Never
      containers:
      - name: trainer
        image: training-image:latest
        resources:
          limits:
            nvidia.com/gpu: 1
```

When the Job controller processes this Job, it automatically:

1. Creates a [Workload](https://kubernetes.io/docs/concepts/workloads/workload-api/) object in the same namespace. The Workload contains a
   `podGroupTemplate` with a
   [gang scheduling policy](https://kubernetes.io/docs/concepts/workloads/workload-api/policies/#gang-policy)
   where `minCount` equals the Job's parallelism.
2. Creates a [PodGroup](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/workload-v1alpha1/)
   object based on that template.
   The PodGroup is a standalone runtime scheduling unit that carries an inline copy
   of the gang policy.
3. Creates Pods with `spec.schedulingGroup.podGroupName` set to the PodGroup name,
   linking each Pod to its scheduling group.

Discovery of these objects is based on spec references (`controllerRef` and
`podGroupTemplateRef`).

The Workload and PodGroup are owned by the Job (via `ownerReferences`) and are
automatically garbage collected when the Job is deleted.