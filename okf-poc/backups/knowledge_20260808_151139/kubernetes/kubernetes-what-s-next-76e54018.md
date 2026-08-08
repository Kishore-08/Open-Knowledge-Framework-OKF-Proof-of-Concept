---
id: kubernetes-what-s-next-76e54018
type: concept
title: What's next
description: 'For examples on using limits, see:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/policy/limit-range/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## What's next

For examples on using limits, see:

- [how to configure minimum and maximum CPU constraints per namespace](https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/cpu-constraint-namespace/).
- [how to configure minimum and maximum Memory constraints per namespace](https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/memory-constraint-namespace/).
- [how to configure default CPU Requests and Limits per namespace](https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/cpu-default-namespace/).
- [how to configure default Memory Requests and Limits per namespace](https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/memory-default-namespace/).
- [how to configure minimum and maximum Storage consumption per namespace](https://kubernetes.io/docs/tasks/administer-cluster/limit-storage-consumption/#limitrange-to-limit-requests-for-storage).
- a [detailed example on configuring quota per namespace](https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/quota-memory-cpu-namespace/).

Refer to the [LimitRanger design document](https://git.k8s.io/design-proposals-archive/resource-management/admission_control_limit_range.md)
for context and historical information.