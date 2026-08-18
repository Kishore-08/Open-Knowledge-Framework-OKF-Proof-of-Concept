---
id: kubernetes-queuesort-085106f9
type: concept
title: QueueSort
description: These plugins are used to sort Pods in the scheduling queue. A queue
  sort plugin
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/scheduling-eviction/scheduling-framework/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### QueueSort

These plugins are used to sort Pods in the scheduling queue. A queue sort plugin
essentially provides a `Less(Pod1, Pod2)` function. Only one queue sort
plugin may be enabled at a time.