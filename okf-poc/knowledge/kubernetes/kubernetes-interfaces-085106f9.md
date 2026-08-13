---
id: kubernetes-interfaces-085106f9
type: concept
title: Interfaces
description: The following picture shows the scheduling context of a Pod and the interfaces
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/scheduling-eviction/scheduling-framework/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

## Interfaces

The following picture shows the scheduling context of a Pod and the interfaces
that the scheduling framework exposes.

One plugin may implement multiple interfaces to perform more complex or
stateful tasks.

Some interfaces match the scheduler extension points which can be configured through
[Scheduler Configuration](https://kubernetes.io/docs/reference/scheduling/config/#extension-points).

![](https://kubernetes.io/images/docs/scheduling-framework-extensions.png)

#### Scheduling framework extension points