---
id: kubernetes-scheduling-cycle-binding-cycle-085106f9
type: concept
title: Scheduling cycle & binding cycle
description: The scheduling cycle selects a node for the Pod, and the binding cycle
  applies
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/scheduling-eviction/scheduling-framework/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Scheduling cycle & binding cycle

The scheduling cycle selects a node for the Pod, and the binding cycle applies
that decision to the cluster. Together, a scheduling cycle and binding cycle are
referred to as a "scheduling context".

Scheduling cycles are run serially, while binding cycles may run concurrently.

A scheduling or binding cycle can be aborted if the Pod is determined to
be unschedulable or if there is an internal error. The Pod will be returned to
the queue and retried.