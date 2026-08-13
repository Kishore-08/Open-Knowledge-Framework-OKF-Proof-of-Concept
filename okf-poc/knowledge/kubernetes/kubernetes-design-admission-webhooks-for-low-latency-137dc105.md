---
id: kubernetes-design-admission-webhooks-for-low-latency-137dc105
type: concept
title: Design admission webhooks for low latency
description: Mutating admission webhooks are called in sequence. Depending on the
  mutating
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/admission-webhooks-good-practices/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

### Design admission webhooks for low latency

Mutating admission webhooks are called in sequence. Depending on the mutating
webhook setup, some webhooks might be called multiple times. Every mutating
webhook call adds latency to the admission process. This is unlike validating
webhooks, which get called in parallel.

When designing your mutating webhooks, consider your latency requirements and
tolerance. The more mutating webhooks there are in your cluster, the greater the
chance of latency increases.

Consider the following to reduce latency:

- Consolidate webhooks that perform a similar mutation on different objects.
- Reduce the number of API calls made in the mutating webhook server logic.
- Limit the match conditions of each mutating webhook to reduce how many
  webhooks are triggered by a specific API request.
- Consolidate small webhooks into one server and configuration to help with
  ordering and organization.