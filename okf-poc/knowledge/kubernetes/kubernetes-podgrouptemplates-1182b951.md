---
id: kubernetes-podgrouptemplates-1182b951
type: concept
title: PodGroupTemplates
description: The `spec.podGroupTemplates` list defines the distinct components of
  your workload.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/workload-api/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### PodGroupTemplates

The `spec.podGroupTemplates` list defines the distinct components of your workload.
For example, a machine learning job might have a `driver` template and a `worker` template.

Each entry in `podGroupTemplates` must have:

1. A unique `name` that will be used to reference the template in the `PodGroup`'s `spec.podGroupTemplateRef`.
2. A [scheduling policy](https://kubernetes.io/docs/concepts/workloads/workload-api/policies/) (`basic` or `gang`).

Each entry can also have
[priority and disruption mode](https://kubernetes.io/docs/concepts/workloads/workload-api/disruption-and-priority/)
fields.

#### Note:

In v1.36 the [priority and disruption mode](https://kubernetes.io/docs/concepts/workloads/workload-api/disruption-and-priority/)
fields were enabled by a
[`WorkloadAwarePreemption`](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/#WorkloadAwarePreemption)
feature gate. This gate was merged into
[`GenericWorkload`](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/#GenericWorkload) in v1.37.

The maximum number of PodGroupTemplates in a single Workload is 8.

```
apiVersion: scheduling.k8s.io/v1beta1
kind: Workload
metadata:
  name: training-job-workload
  namespace: some-ns
spec:
  controllerRef:
    apiGroup: batch
    kind: Job
    name: training-job
  podGroupTemplates:
  - name: workers
    schedulingPolicy:
      gang:
        # The gang is schedulable only if 4 pods can run at once
        minCount: 4
    priorityClassName: high-priority
    disruptionMode:
      all: {}
```

When a workload controller creates a `PodGroup` from one of these templates, it copies the
`schedulingPolicy` into the `PodGroup`'s own spec. Changes to the `Workload` only affect
newly created `PodGroups`, not existing ones.