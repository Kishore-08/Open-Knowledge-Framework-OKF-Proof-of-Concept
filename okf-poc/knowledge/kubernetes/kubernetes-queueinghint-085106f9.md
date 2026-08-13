---
id: kubernetes-queueinghint-085106f9
type: concept
title: QueueingHint
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/scheduling-eviction/scheduling-framework/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

### QueueingHint

FEATURE STATE:
`Kubernetes v1.34 [stable]`(enabled by default)

QueueingHint is a callback function for deciding whether a Pod can be requeued to the active queue or backoff queue.
It's executed every time a certain kind of event or change happens in the cluster.
When the QueueingHint finds that the event might make the Pod schedulable,
the Pod is put into the active queue or the backoff queue
so that the scheduler will retry the scheduling of the Pod.