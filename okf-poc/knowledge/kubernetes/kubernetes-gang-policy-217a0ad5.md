---
id: kubernetes-gang-policy-217a0ad5
type: concept
title: Gang policy
description: The `gang` policy enforces "all-or-nothing" scheduling. This is essential
  for tightly-coupled
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/workload-api/policies/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Gang policy

The `gang` policy enforces "all-or-nothing" scheduling. This is essential for tightly-coupled
workloads where partial startup results in deadlocks or wasted resources.

This can be used for [Jobs](https://kubernetes.io/docs/concepts/workloads/controllers/job/)
or any other batch process where all workers must run concurrently to make progress.

The `gang` policy requires a `minCount` field, which is the minimum number of Pods that must be
schedulable simultaneously for the group to be feasible:

```
schedulingPolicy:
  gang:
    # The number of Pods that must be schedulable simultaneously
    # for the group to be admitted.
    minCount: 4
```