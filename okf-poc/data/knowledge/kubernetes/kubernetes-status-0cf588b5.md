---
id: kubernetes-status-0cf588b5
type: concept
title: Status
description: The scheduler updates `status.conditions` to report whether the group
  has been
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/podgroup-api/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Status

The scheduler updates `status.conditions` to report whether the group has been
successfully scheduled. The primary condition is `PodGroupScheduled`, which is `True`
when all required Pods have been placed and `False` when scheduling fails.

#### Note:

The `PodGroupScheduled` condition reflects the initial scheduling decision only.
The scheduler does not update it if Pods later fail or are evicted. See
[Limitations](https://kubernetes.io/docs/concepts/workloads/podgroup-api/lifecycle/#limitations)
for details.

See the [PodGroup lifecycle](https://kubernetes.io/docs/concepts/workloads/podgroup-api/lifecycle/#podgroup-status)
page for the full list of conditions and reasons.