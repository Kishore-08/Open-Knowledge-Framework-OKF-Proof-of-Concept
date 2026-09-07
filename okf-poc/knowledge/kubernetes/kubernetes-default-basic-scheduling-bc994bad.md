---
id: kubernetes-default-basic-scheduling-bc994bad
type: concept
title: Default (Basic) scheduling
description: A Job that omits `.spec.scheduling` defaults to `Basic`, which acts as
  an implicit
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/job/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Default (Basic) scheduling

A Job that omits `.spec.scheduling` defaults to `Basic`, which acts as an implicit
opt-out of gang scheduling. Its Pods schedule the same way as an ordinary Job,
while a `Basic` `Workload` and `PodGroup` are still created:

```
apiVersion: batch/v1
kind: Job
metadata:
  name: batch-processor
  namespace: batch
spec:
  parallelism: 10
  completions: 10
  # .spec.scheduling omitted -> defaults to Basic scheduling.
  template:
    spec:
      restartPolicy: Never
      containers:
      - name: processor
        image: processor-image:v1
```