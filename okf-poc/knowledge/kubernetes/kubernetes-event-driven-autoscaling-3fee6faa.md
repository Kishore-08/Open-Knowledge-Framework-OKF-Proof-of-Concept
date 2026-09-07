---
id: kubernetes-event-driven-autoscaling-3fee6faa
type: concept
title: Event driven Autoscaling
description: It is also possible to scale workloads based on events, for example using
  the
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/autoscaling/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Event driven Autoscaling

It is also possible to scale workloads based on events, for example using the
[*Kubernetes Event Driven Autoscaler* (**KEDA**)](https://keda.sh/).

KEDA is a CNCF-graduated project enabling you to scale your workloads based on the number
of events to be processed, for example the amount of messages in a queue. There exists
a wide range of adapters for different event sources to choose from.